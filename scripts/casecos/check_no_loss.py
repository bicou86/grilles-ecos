"""Signale les items de contenu presents dans BASE_REF et disparus dans l'etat
courant du disque, pour les grilles CasECOS.

Usage :
    python3 scripts/casecos/check_no_loss.py BASE_REF [GRILLE_FILTRE]

Exemples :
    python3 scripts/casecos/check_no_loss.py HEAD
    python3 scripts/casecos/check_no_loss.py HEAD~1 "Migraine"

Pour chaque grille modifiee entre BASE_REF et le disque (comparaison via
`git diff`, donc les modifications non commitees comptent aussi), les items de
TOUS les blocs de contenu (`lib.all_items` : annexe-dd, redflags, therapy,
cloture, exemples, expert, theorie, scenario, defi, annexe-nu) sont extraits
avant et apres, puis compares avec le meme seuil de ressemblance que
`report_redundancy.py` (SequenceMatcher(...).ratio() > 0.72) : les deux scripts
mesurent la meme chose, cote disparition plutot que cote doublon restant.

La comparaison porte sur l'ensemble des blocs et non bloc par bloc : un item
deplace d'un bloc a l'autre — d'`annexe-dd` vers `theorie`, de `therapy` vers
`cloture` — est un deplacement legitime, pas une disparition.

COMME DANS GERMAN ET RESCOS, ON LIT LES BLOCS ET NON DEUX ZONES. La version
AMBOSS lit `peda_bounds` et `dd_bounds` ; ici cinq blocs sur dix (`annexe-dd`,
`redflags`, `therapy`, `cloture`, `exemples`) vivent en amont de la zone
pedagogique, disperses au fil de la page, et aucune zone continue ne les
englobe sans avaler aussi les criteres notes.

Le bloc `scenario` est ici INCLUS, alors que `report_redundancy.py` l'exclut de
son total : les deux scripts n'ont pas le meme objet. Exclure le scenario d'une
mesure de doublons est un choix editorial ; l'exclure d'un controle de perte
laisserait reecrire le script du patient sans trace.

Ceci est un RAPPORT, pas un test. Un item signale « disparu » n'est pas
forcement une perte : il peut avoir ete fusionne, reformule au point de passer
sous le seuil, ou legitimement supprime comme doublon strict. C'EST POURQUOI CE
SCRIPT SORT TOUJOURS AVEC LE CODE 0. Ne jamais le cabler comme porte bloquante :
ce serait bloquer le projet sur des suppressions parfaitement legitimes.

COUT : chaque grille compare ~190 items avant contre ~190 apres, en O(n x m).
Comptez une a deux secondes par grille modifiee. Sur ce corpus, ne le lancer
JAMAIS sans filtre a la suite d'une passe touchant les 198 grilles sans avoir
prevu le temps correspondant (~5 min).
"""
import subprocess
import sys
import unicodedata
from difflib import SequenceMatcher
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import lib_casecos as lib

ROOT = Path(__file__).resolve().parents[2]
THRESHOLD = 0.72  # identique a report_redundancy.py — meme mesure, face opposee.


def changed_grid_names(base_ref):
    """Noms des fichiers de grilles modifies entre base_ref et le disque courant.

    DEUX PIEGES, TOUS DEUX PROPRES A CE CORPUS — les trois precedents ont des
    noms de fichiers purement ASCII (`RESCOS-12_-_...`), ceux-ci sont des
    TITRES accentues. Sans les deux corrections ci-dessous, la fonction rend un
    ensemble qui ne recoupe jamais `path.name`, et ce script devient un NO-OP
    SILENCIEUX : il annonce « aucune grille modifiee » quoi qu'il arrive, et le
    filet anti-perte n'existe plus.

    1. `-z`. Sans lui, `git diff --name-only` rend les chemins non-ASCII
       ENTRE GUILLEMETS et echappes a la mode C :
           "cases/casecos/AMC-CasECOS C\\303\\251phal\\303\\251es - ....html"
       `-z` rend les chemins bruts, separes par des NUL — ce qui regle du meme
       coup le cas des espaces, dont ces noms sont pleins.

    2. NFC des deux cotes. Git rend les noms en NFC (`core.precomposeunicode`
       vaut `true` par defaut sur macOS) tandis que le systeme de fichiers les
       rend en NFD. Mesure : sans normalisation, 60 des 198 noms se
       correspondent — exactement les 60 sans accent.

    `git show` (dans `read_old`) n'a pas ce probleme : `core.precomposeunicode`
    lui fait accepter le chemin NFD tel quel.
    """
    result = subprocess.run(
        ["git", "diff", "--name-only", "-z", base_ref, "--", "cases/casecos"],
        cwd=ROOT, capture_output=True, encoding="utf-8",
    )
    if result.returncode != 0:
        print(f"git diff a echoue pour {base_ref!r} : {result.stderr.strip()}")
        return set()
    return {unicodedata.normalize("NFC", Path(entry).name)
            for entry in result.stdout.split("\0") if entry.strip()}


def read_old(base_ref, path):
    """Contenu du fichier a base_ref, ou None s'il n'existait pas a cette reference."""
    rel = path.relative_to(ROOT).as_posix()
    result = subprocess.run(
        ["git", "show", f"{base_ref}:{rel}"],
        cwd=ROOT, capture_output=True, encoding="utf-8",
    )
    return result.stdout if result.returncode == 0 else None


def disappeared(before, after):
    """Items de `before` sans equivalent (ratio > THRESHOLD) dans `after`."""
    return [item for item in before
            if not any(SequenceMatcher(None, item, other).ratio() > THRESHOLD
                       for other in after)]


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        return 0
    base_ref = sys.argv[1]
    only = sys.argv[2] if len(sys.argv) > 2 else None

    changed = changed_grid_names(base_ref)
    grids_checked = total_missing = 0
    for path in lib.grids():
        if not lib.matches(path, only):
            continue
        if unicodedata.normalize("NFC", path.name) not in changed:
            continue
        grids_checked += 1

        old_html = read_old(base_ref, path)
        if old_html is None:
            print(f"\n=== {path.name} — absente de {base_ref}, ignoree ===")
            continue

        missing = disappeared(lib.all_items(lib.strip_base64(old_html)),
                              lib.all_items(lib.strip_base64(
                                  path.read_text(encoding="utf-8"))))
        if missing:
            total_missing += len(missing)
            print(f"\n=== {path.name} — {len(missing)} item(s) disparu(s) ===")
            for item in missing:
                print(f"  - {item[:100]}")
        else:
            print(f"\n=== {path.name} — aucun item disparu ===")

    if grids_checked == 0:
        suffix = f" (filtre : {only})" if only else ""
        print(f"Aucune grille modifiee entre {base_ref} et l'etat courant du "
              f"disque{suffix}.")

    print(f"\nTOTAL : {total_missing} item(s) disparu(s) sur {grids_checked} grille(s) "
          f"modifiee(s) — a relire, une disparition n'est pas forcement une perte.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
