#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Reprend une image du vault Obsidian vers `cases/img/german/`.

Mode de livraison des images des grilles german : **fichier référencé**, jamais
base64 (cf. `PROCEDURE-german.md` § 8.6). Ce script est l'outil unique de cette
reprise. Il prend un nom d'image tel que la page SSP le cite, le retrouve dans le
vault, le copie s'il n'y est pas déjà, et rend le chemin à écrire dans la grille.

    $ python3 scripts/german/fetch_image.py '![[general-score-audit-c.png]]'
    ../img/german/general-score-audit-c.png

Il est **idempotent** : deux grilles citant la même image ne la copient qu'une
fois. Une reprise déjà faite est reconnue par empreinte SHA-256 et ne réécrit
rien — donc pas de blob git nouveau.

Il **s'arrête bruyamment** plutôt que de livrer quelque chose de faux :
référence introuvable (36 des 700 citées par les 53 pages german sont cassées),
fichier vide ou tronqué, en-tête qui ne correspond pas à l'extension, homonyme
ambigu, ou nom déjà pris dans le dépôt par un contenu différent.

Convention de nommage : le nom du vault, normalisé ASCII-minuscules-tirets.
Voir `normalize()` et `PROCEDURE-german.md` § 8.6.

Usage
-----
    fetch_image.py NOM [NOM ...]     reprend une ou plusieurs images
    fetch_image.py --check NOM ...   résout et diagnostique, ne copie rien
    fetch_image.py --verify          vérifie que tous les src des grilles existent
    fetch_image.py --json NOM ...    sortie machine

Chaque NOM accepte les formes `![[fichier.png]]`, `[[fichier.png]]`,
`fichier.png`, ou un chemin. Les suffixes Obsidian `|300` et `#ancre` sont
ignorés.

Sorties : 0 tout va bien · 1 au moins un échec · 2 usage.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import shutil
import struct
import sys
import unicodedata
from pathlib import Path

# --- Emplacements ----------------------------------------------------------

REPO = Path(__file__).resolve().parents[2]

#: Corpus connus : préfixe de nom de grille, et rien d'autre. Le reste des
#: chemins s'en déduit — `cases/<corpus>/` pour les grilles, `cases/img/<corpus>/`
#: pour les images. `--corpus` ne change que ces emplacements ; la résolution
#: dans le vault, le contrôle d'intégrité, la normalisation et le manifeste sont
#: identiques d'un corpus à l'autre, parce que la règle du § 8 l'est aussi
#: (PROCEDURE-german.md § 8 : « elle vaut pour AMBOSS et RESCOS si le chantier
#: s'y étend »). `german` reste le défaut : aucun appel existant ne change.
CORPORA = {
    "german": "German-*.html",
    "amboss": "AMBOSS-*.html",
    "rescos": "RESCOS-*.html",
    # Ces deux corpus n'ont pas de préfixe régulier : leurs grilles portent des
    # noms libres (« BBN - Cancer du sein - Grille ECOS.html »). Le glob prend
    # donc tout le répertoire, ce qui reste exact — il ne sert qu'à énumérer
    # les grilles d'un corpus, et chaque corpus a son propre répertoire.
    "rescos-locales": "*.html",
    "casecos": "*.html",
    "triage": "*.html",
    "usmle": "*.html",
}
CORPUS = "german"

DEST = REPO / "cases" / "img" / CORPUS
GRIDS = REPO / "cases" / CORPUS
MANIFEST = DEST / "MANIFEST.tsv"
GRID_GLOB = CORPORA[CORPUS]

#: Racine du vault. `ECOS_VAULT` prend le pas, pour qui travaille ailleurs.
VAULT = Path(
    os.environ.get(
        "ECOS_VAULT",
        "/Users/damienfulliquet/Documents/Damien/Medecine/Obsidian",
    )
).expanduser()

#: Chemin écrit dans la grille. Les grilles sont dans `cases/<corpus>/`, les
#: images dans `cases/img/<corpus>/` : un seul niveau à remonter.
HREF_PREFIX = "../img/%s/" % CORPUS


def set_corpus(name):
    """Bascule les emplacements sur un autre corpus. Appelé par `--corpus`.

    Les constantes restent des constantes pour tout appel qui ne dit rien :
    importer le module donne toujours `german`, comme avant.
    """
    global CORPUS, DEST, GRIDS, MANIFEST, GRID_GLOB, HREF_PREFIX, _SRC_RE
    if name not in CORPORA:
        raise SystemExit("corpus inconnu : %s (connus : %s)"
                         % (name, ", ".join(sorted(CORPORA))))
    CORPUS = name
    DEST = REPO / "cases" / "img" / name
    GRIDS = REPO / "cases" / name
    MANIFEST = DEST / "MANIFEST.tsv"
    GRID_GLOB = CORPORA[name]
    HREF_PREFIX = "../img/%s/" % name
    _SRC_RE = re.compile(r'src\s*=\s*"(\.\./img/%s/[^"]+)"' % name)

#: Répertoires que la résolution ignore. `.backup_transparents` est une copie
#: de sauvegarde de `Skills ECOS/img/` : sans cette exclusion, 46 des 664 images
#: citées deviendraient ambiguës alors qu'aucune ne l'est réellement.
SKIP_DIRS = {".obsidian", ".trash", ".git", ".backup_transparents", "node_modules"}

#: Extensions considérées comme images.
IMG_EXT = {".png", ".jpg", ".jpeg", ".svg", ".gif", ".webp"}

#: Quand plusieurs candidats subsistent, celui-ci l'emporte : c'est le dossier
#: d'images propre au projet ECOS, celui que les pages SSP visent.
PREFERRED_ROOT = "Skills ECOS/img/"

#: Plafond par image, en octets (§ 8.5 d ; révisé 400 -> 600 Ko le 2026-08-02).
#: Au-delà : avertissement, pas d'arrêt — c'est la règle de sélection qui
#: tranche, pas l'outil de copie. Les deux exemptions du § 8.5 d (message-clé
#: obligatoire du § 8.4, image désignée par un critère noté) ne sont pas
#: détectables depuis le seul nom du fichier : l'avertissement reste posé pour
#: elles aussi, à charge pour qui l'embarque de vérifier qu'une exemption
#: s'applique plutôt que de le prendre pour un refus.
SIZE_WARN = 600 * 1024

# --- Erreurs ---------------------------------------------------------------


class FetchError(Exception):
    """Échec bruyant : la référence ne peut pas être livrée telle quelle."""

    def __init__(self, kind, message, hint=""):
        super().__init__(message)
        self.kind = kind
        self.message = message
        self.hint = hint


# --- Nommage ---------------------------------------------------------------


def normalize(name):
    """Nom du vault → nom dans le dépôt.

    ASCII, minuscules, tirets ; extension canonique (`.jpeg` → `.jpg`).
    Sur les 664 images citées par les 53 pages german, la transformation est
    **l'identité pour 573 d'entre elles (86 %)** — les noms du vault sont déjà
    propres — et **ne provoque aucune collision**. Les 91 réécrites sont les
    noms hérités de `_bibliotheque/`, qui portent espaces, accents et
    majuscules : autant de percent-encoding dans un `src=` sinon.
    """
    stem, ext = os.path.splitext(name)
    stem = unicodedata.normalize("NFKD", stem)
    stem = stem.encode("ascii", "ignore").decode("ascii")
    stem = re.sub(r"[^A-Za-z0-9]+", "-", stem).strip("-").lower()
    ext = ext.lower()
    if ext == ".jpeg":
        ext = ".jpg"
    if not stem:
        raise FetchError("nom", "nom vide après normalisation : %r" % name)
    return stem + ext


def parse_ref(raw):
    """`![[fichier.png|300]]` → `fichier.png`. Tolère les formes nues."""
    s = raw.strip()
    m = re.search(r"!?\[\[(.+?)\]\]", s)
    if m:
        s = m.group(1)
    s = s.split("|", 1)[0].split("#", 1)[0].strip()
    s = os.path.basename(s)
    if not s:
        raise FetchError("nom", "référence vide : %r" % raw)
    return s


# --- Résolution dans le vault ----------------------------------------------

_index = None


def vault_index():
    """Nom de fichier → liste de chemins relatifs au vault. Construit une fois."""
    global _index
    if _index is not None:
        return _index
    if not VAULT.is_dir():
        raise FetchError(
            "vault",
            "vault introuvable : %s" % VAULT,
            "Définissez ECOS_VAULT sur la racine du vault Obsidian.",
        )
    idx = {}
    for dirpath, dirnames, filenames in os.walk(VAULT):
        dirnames[:] = [d for d in dirnames if d not in SKIP_DIRS]
        for fn in filenames:
            if fn.startswith("."):
                continue
            if os.path.splitext(fn)[1].lower() not in IMG_EXT:
                continue
            rel = os.path.relpath(os.path.join(dirpath, fn), VAULT)
            idx.setdefault(fn, []).append(rel)
    _index = idx
    return idx


def resolve(ref):
    """Nom cité → (chemin absolu dans le vault, mode d'appariement).

    Le mode vaut `exact` ou `normalise`. Le second signale que la page SSP
    n'écrit pas le nom comme le disque le porte — typiquement l'accent en NFD
    sous macOS contre le NFC de la page. L'appariement reste sûr : la
    normalisation ne produit aucune collision sur les 664 images citées, et
    l'ambiguïté résiduelle est refusée juste en dessous. Mais il est **signalé**,
    parce qu'une correspondance approchée qui passerait pour exacte est
    exactement ce que § 8.5 c interdit.

    Lève `FetchError` si introuvable (référence cassée) ou si l'ambiguïté
    subsiste après préférence pour `Skills ECOS/img/`.
    """
    idx = vault_index()
    matched = "exact"
    hits = idx.get(ref)
    if not hits:
        want = normalize(ref)
        hits = [
            p
            for name, paths in idx.items()
            if normalize(name) == want
            for p in paths
        ]
        matched = "normalise"
        if not hits:
            raise FetchError(
                "cassee",
                "référence introuvable dans le vault : %s" % ref,
                "RÉFÉRENCE CASSÉE. § 8.5 c : elle arrête le traitement de la "
                "grille. Ne pas lui substituer un fichier au nom voisin.",
            )
    if len(hits) > 1:
        pref = [p for p in hits if p.startswith(PREFERRED_ROOT)]
        if len(pref) == 1:
            hits = pref
        else:
            raise FetchError(
                "ambigu",
                "%d fichiers portent ce nom : %s" % (len(hits), ref),
                "Candidats :\n    " + "\n    ".join(sorted(hits)),
            )
    return VAULT / hits[0], matched


# --- Intégrité -------------------------------------------------------------


def dimensions(data, ext):
    """(largeur, hauteur) depuis l'en-tête, ou None. Sert de témoin de santé :
    une image corrompue rend 0×0 au navigateur."""
    try:
        if ext == ".png" and data[:8] == b"\x89PNG\r\n\x1a\n":
            w, h = struct.unpack(">II", data[16:24])
            return w, h
        if ext == ".gif" and data[:6] in (b"GIF87a", b"GIF89a"):
            w, h = struct.unpack("<HH", data[6:10])
            return w, h
        if ext == ".jpg" and data[:2] == b"\xff\xd8":
            i, n = 2, len(data)
            while i < n - 9:
                if data[i] != 0xFF:
                    i += 1
                    continue
                marker = data[i + 1]
                if marker in (0xD8, 0xD9) or 0xD0 <= marker <= 0xD7:
                    i += 2
                    continue
                seglen = struct.unpack(">H", data[i + 2 : i + 4])[0]
                if 0xC0 <= marker <= 0xCF and marker not in (0xC4, 0xC8, 0xCC):
                    h, w = struct.unpack(">HH", data[i + 5 : i + 9])
                    return w, h
                i += 2 + seglen
        if ext == ".webp" and data[:4] == b"RIFF" and data[8:12] == b"WEBP":
            return None
    except Exception:
        return None
    return None


def inspect(path):
    """Lit et contrôle un fichier source. Rend (octets, sha256, dimensions)."""
    data = path.read_bytes()
    if not data:
        raise FetchError(
            "vide", "fichier vide (0 octet) : %s" % path, "Rien à livrer."
        )
    ext = os.path.splitext(path.name)[1].lower()
    if ext == ".jpeg":
        ext = ".jpg"
    magic = {
        ".png": (b"\x89PNG\r\n\x1a\n",),
        ".jpg": (b"\xff\xd8\xff",),
        ".gif": (b"GIF87a", b"GIF89a"),
        ".webp": (b"RIFF",),
    }.get(ext)
    if magic and not any(data.startswith(m) for m in magic):
        raise FetchError(
            "corrompu",
            "en-tête %s incohérent : %s" % (ext, path.name),
            "Le fichier ne commence pas par la signature attendue — "
            "tronqué, ou mal nommé. Ne pas le livrer.",
        )
    if ext == ".png" and not data.rstrip().endswith(b"IEND\xaeB`\x82"):
        raise FetchError(
            "corrompu",
            "PNG sans marqueur de fin IEND : %s" % path.name,
            "Fichier tronqué. Ne pas le livrer.",
        )
    if ext == ".jpg" and data[-2:] != b"\xff\xd9":
        raise FetchError(
            "corrompu",
            "JPEG sans marqueur de fin EOI : %s" % path.name,
            "Fichier tronqué. Ne pas le livrer.",
        )
    return data, hashlib.sha256(data).hexdigest(), dimensions(data, ext)


# --- Manifeste -------------------------------------------------------------

_MANIFEST_HEADER = [
    "# Provenance des images des grilles german. Généré par "
    "scripts/german/fetch_image.py — ne pas éditer à la main.",
    "# nom_depot\tsha256\toctets\tdimensions\tchemin_vault",
]


def read_manifest():
    rows = {}
    if MANIFEST.exists():
        for line in MANIFEST.read_text(encoding="utf-8").splitlines():
            if not line.strip() or line.startswith("#"):
                continue
            parts = line.split("\t")
            if len(parts) >= 5:
                rows[parts[0]] = parts[1:5]
    return rows


def write_manifest(rows):
    lines = list(_MANIFEST_HEADER)
    for name in sorted(rows):
        lines.append("\t".join([name] + list(rows[name])))
    MANIFEST.write_text("\n".join(lines) + "\n", encoding="utf-8")


# --- Reprise ---------------------------------------------------------------


def recompresse(data, ext, plafond=SIZE_WARN):
    """Rend (octets, extension, dimensions, note) sous le plafond, ou None.

    Le vault stocke ses photographies de manœuvres d'examen en PNG : 205 images
    citées par les pages y dépassent 600 Ko, jusqu'à 12,7 Mo, alors qu'elles
    documentent souvent littéralement un critère noté. Le format est le
    coupable, pas la résolution — un réencodage JPEG rend 80 à 95 % sans perte
    visible, comme sur German-10 (5403 Ko -> 469 Ko).

    Le vault n'est jamais modifié : le dérivé ne vit que dans le dépôt, et le
    manifeste le signale.

    Rend None si l'image est déjà sous le plafond, si Pillow est absent, ou si
    aucun réglage n'y parvient sans descendre sous 900 px de large — en deçà,
    une planche annotée cesse d'être lisible.
    """
    try:
        from PIL import Image
    except ImportError:
        return None
    import io

    im = Image.open(io.BytesIO(data))
    im.load()
    if im.mode in ("RGBA", "LA", "P"):
        fond = Image.new("RGB", im.size, (255, 255, 255))
        im = im.convert("RGBA")
        fond.paste(im, mask=im.split()[-1])
        im = fond
    else:
        im = im.convert("RGB")

    for largeur in (1600, 1400, 1200, 1000, 900):
        if im.width < largeur:
            continue
        h = int(im.height * largeur / im.width)
        petit = im.resize((largeur, h), Image.LANCZOS)
        for q in (90, 88, 85, 82):
            buf = io.BytesIO()
            petit.save(buf, "JPEG", quality=q, optimize=True, progressive=True)
            if buf.tell() <= plafond:
                note = ("dérivé recompressé — source %dx%d, %.0f Ko ; "
                        "JPEG qualité %d à %d px" %
                        (im.width, im.height, len(data) / 1024.0, q, largeur))
                return buf.getvalue(), "jpg", (largeur, h), note
    # Image déjà étroite : réencoder sans redimensionner.
    for q in (88, 85, 82, 78):
        buf = io.BytesIO()
        im.save(buf, "JPEG", quality=q, optimize=True, progressive=True)
        if buf.tell() <= plafond:
            note = ("dérivé recompressé — source %.0f Ko ; JPEG qualité %d, "
                    "dimensions inchangées" % (len(data) / 1024.0, q))
            return buf.getvalue(), "jpg", im.size, note
    return None


def fetch(raw, dry_run=False, recompress=False):
    """Reprend une référence. Rend un dict décrivant le résultat.

    `status` vaut `copie` (nouvelle), `deja` (déjà en place, octet pour octet)
    ou `simule` (--check). Avec `recompress`, une image au-dessus du plafond est
    reprise sous forme de dérivé JPEG — le vault reste intact.
    """
    ref = parse_ref(raw)
    src, matched = resolve(ref)
    data, digest, dims = inspect(src)
    name = normalize(src.name)

    note_derive = None
    if recompress and len(data) > SIZE_WARN:
        red = recompresse(data, src.suffix.lower().lstrip("."))
        if red is not None:
            data, ext_neuf, dims, note_derive = red
            digest = hashlib.sha256(data).hexdigest()
            name = normalize(src.stem + "." + ext_neuf)
    dest = DEST / name
    rel_vault = os.path.relpath(src, VAULT)
    dim_s = "%dx%d" % dims if dims else "-"

    warnings = []
    if matched == "normalise":
        warnings.append(
            "appariement NON EXACT — la page cite %r, le disque porte %r ; "
            "vérifier que c'est bien la même image" % (ref, src.name)
        )
    if len(data) > SIZE_WARN:
        warnings.append(
            "%.0f Ko > plafond de 600 Ko (§ 8.5 d) — vérifier que la règle "
            "de sélection l'autorise, ou qu'une des deux exemptions "
            "(message-clé du § 8.4, image désignée par un critère noté) "
            "s'applique" % (len(data) / 1024.0)
        )

    status = "simule"
    if dest.exists():
        existing = hashlib.sha256(dest.read_bytes()).hexdigest()
        if existing == digest:
            status = "deja"
        else:
            raise FetchError(
                "collision",
                "%s existe déjà avec un contenu différent" % name,
                "Source : %s\n    Le nom normalisé entre en collision avec "
                "une image déjà reprise. Aucune collision n'existe sur les "
                "664 images citées — vérifiez la source." % rel_vault,
            )
    elif not dry_run:
        DEST.mkdir(parents=True, exist_ok=True)
        if note_derive is None:
            # copyfile, pas copy2 : on ne veut pas des mtimes du vault ici.
            shutil.copyfile(src, dest)
        else:
            dest.write_bytes(data)
        after = hashlib.sha256(dest.read_bytes()).hexdigest()
        if after != digest:
            dest.unlink(missing_ok=True)
            raise FetchError(
                "copie", "copie altérée (sha256 différent) : %s" % name
            )
        status = "copie"

    if not dry_run:
        rows = read_manifest()
        # La provenance reste le chemin du vault ; la note dit que le fichier du
        # dépôt en est un dérivé, donc que son sha256 ne s'y retrouve pas.
        prov = rel_vault if note_derive is None else rel_vault + "  [" + note_derive + "]"
        rows[name] = [digest, str(len(data)), dim_s, prov]
        write_manifest(rows)

    return {
        "ref": ref,
        "name": name,
        "href": HREF_PREFIX + name,
        "status": status,
        "bytes": len(data),
        "sha256": digest,
        "dimensions": dim_s,
        "vault": rel_vault,
        "matched": matched,
        "warnings": warnings,
    }


# --- Vérification des liens ------------------------------------------------

_SRC_RE = re.compile(r'src\s*=\s*"(\.\./img/german/[^"]+)"')


def verify():
    """Chaque `src="../img/german/…"` des grilles pointe-t-il vers un fichier ?

    Signale aussi les images orphelines — présentes mais citées par aucune
    grille — et les grilles restées en base64.
    """
    used, broken, b64 = set(), [], []
    for grid in sorted(GRIDS.glob(GRID_GLOB)):
        html = grid.read_text(encoding="utf-8", errors="replace")
        if 'src="data:image' in html:
            b64.append(grid.name)
        for href in _SRC_RE.findall(html):
            name = href[len(HREF_PREFIX) :]
            used.add(name)
            if not (DEST / name).is_file():
                broken.append((grid.name, href))
    present = (
        {p.name for p in DEST.iterdir() if p.is_file() and p.name != "MANIFEST.tsv"}
        if DEST.is_dir()
        else set()
    )
    return {
        "used": sorted(used),
        "broken": broken,
        "orphans": sorted(present - used),
        "base64": b64,
        "present": len(present),
    }


# --- CLI -------------------------------------------------------------------


def main(argv=None):
    ap = argparse.ArgumentParser(
        description="Reprend une image du vault vers cases/img/german/ et rend "
        "le chemin à écrire dans la grille.",
        epilog="Exemple : fetch_image.py '![[general-score-audit-c.png]]'",
    )
    ap.add_argument("refs", nargs="*", metavar="NOM",
                    help="nom cité par la page SSP, forme ![[…]] acceptée")
    ap.add_argument("--check", action="store_true",
                    help="résout et diagnostique sans rien copier")
    ap.add_argument("--verify", action="store_true",
                    help="vérifie les src des grilles et l'absence d'orphelins")
    ap.add_argument("--json", action="store_true", help="sortie machine")
    ap.add_argument("--recompress", action="store_true",
                    help="au-dessus du plafond, reprendre un dérivé JPEG "
                         "sous 600 Ko au lieu de la copie brute ; le vault "
                         "n'est jamais modifié")
    ap.add_argument("--corpus", default="german", choices=sorted(CORPORA),
                    help="corpus de destination (défaut : german)")
    args = ap.parse_args(argv)
    if args.corpus != CORPUS:
        set_corpus(args.corpus)

    if args.verify:
        rep = verify()
        if args.json:
            print(json.dumps(rep, ensure_ascii=False, indent=2))
        else:
            print("images présentes  : %d" % rep["present"])
            print("images référencées: %d" % len(rep["used"]))
            for grid, href in rep["broken"]:
                print("LIEN CASSÉ  %s → %s" % (grid, href))
            for name in rep["orphans"]:
                print("ORPHELINE   %s (aucune grille ne la cite)" % name)
            if CORPUS == "german":
                for name in rep["base64"]:
                    print("BASE64      %s (encore en base64, § 8.6)" % name)
            elif rep["base64"]:
                # AMBOSS porte 225 images en base64 que l'utilisateur a décidé de
                # laisser en place ; seuls les AJOUTS suivent le mode référencé.
                # Les lister une à une noierait les vrais défauts.
                print("base64 hérité     : %d grille(s) (mode référencé exigé "
                      "des ajouts seulement)" % len(rep["base64"]))
            if not rep["broken"] and not rep["orphans"]:
                print("OK — aucun lien cassé, aucune orpheline.")
        return 1 if rep["broken"] else 0

    if not args.refs:
        ap.print_help()
        return 2

    results, failed = [], 0
    for raw in args.refs:
        try:
            r = fetch(raw, dry_run=args.check, recompress=args.recompress)
            results.append(r)
            if not args.json:
                print(r["href"])
                print(
                    "    %-6s %s  %s  %d octets  sha256:%s"
                    % (r["status"], r["dimensions"], r["vault"],
                       r["bytes"], r["sha256"][:12])
                )
                for w in r["warnings"]:
                    print("    ATTENTION %s" % w)
        except FetchError as e:
            failed += 1
            results.append({"ref": raw, "error": e.kind, "message": e.message,
                            "hint": e.hint})
            if not args.json:
                print("ÉCHEC [%s] %s" % (e.kind, e.message), file=sys.stderr)
                if e.hint:
                    print("    %s" % e.hint, file=sys.stderr)
    if args.json:
        print(json.dumps(results, ensure_ascii=False, indent=2))
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
