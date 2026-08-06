#!/usr/bin/env python3
"""Injecte les blocs « 🥼 Grilles ECOS interactives » dans les pages Obsidian.

Source de vérité : docs/obsidian-mapping.yaml (page → grilles + libellés).
Idempotent : le bloc existant (callout `> [!figure]- 🥼 Grilles ECOS interactives`)
est remplacé ; s'il est identique, la page n'est pas réécrite. La section
`## 📚 Références PDF` est créée juste après le frontmatter si elle manque.

Usage :
    python3 scripts/inject_obsidian_blocks.py [--dry-run] [--mapping PATH]
"""
import argparse
import re
import sys
import unicodedata
import urllib.parse
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
HEADING = "## 📚 Références PDF"
BLOCK_START = "> [!figure]- 🥼 Grilles ECOS interactives"
CORPUS_LABEL = {"amboss": "AMBOSS", "german": "German", "rescos": "RESCOS",
                "rescos-locales": "RESCOS locales", "usmle": "USMLE",
                "triage": "Triage", "casecos": "CasECOS", "locales": "Locales"}
CORPUS_ORDER = list(CORPUS_LABEL)


def parse_mapping(path):
    """Parse le sous-ensemble YAML émis par build : pages/unmapped + app_base/vault."""
    conf = {"pages": {}}
    current_page, current_list, entry = None, None, None
    for raw in path.read_text(encoding="utf-8").splitlines():
        if raw.startswith("#") or not raw.strip():
            continue
        if raw.startswith("app_base:"):
            conf["app_base"] = raw.split(":", 1)[1].strip()
        elif raw.startswith("vault:"):
            conf["vault"] = raw.split(":", 1)[1].strip()
        elif raw.startswith("pages:"):
            current_list = None
        elif raw.startswith("unmapped:"):
            current_page = None
            current_list = None
        elif re.match(r'^  "', raw):
            current_page = re.match(r'^  "(.*)":\s*$', raw).group(1).replace('\\"', '"')
            current_list = conf["pages"].setdefault(current_page, [])
        elif current_list is not None and re.match(r"^    - file: ", raw):
            entry = {"file": re.match(r'^    - file: "(.*)"$', raw).group(1)}
            current_list.append(entry)
        elif current_list is not None and re.match(r"^      label: ", raw):
            entry["label"] = re.match(r'^      label: "(.*)"$', raw).group(1).replace('\\"', '"')
    return conf


def entry_corpus(e):
    if e["file"].startswith("cases/"):
        return e["file"].split("/")[1]
    # grille locale (hors app) : RESCOS-4x/5x/6x → groupe RESCOS, sinon Locales
    base = e["file"].rsplit("/", 1)[-1]
    return "rescos" if base.startswith("RESCOS-") else "locales"


def build_block(entries, app_base, vault):
    """Construit le callout. **Tous les liens sont locaux** — voir ci-dessous.

    Les grilles du dépôt pointaient vers `app_base` (l'application Replit), ce
    qui imposait une connexion pour ouvrir une grille depuis Obsidian. Elles
    pointent désormais vers le fichier local, comme le faisaient déjà les
    grilles du vault.

    Format retenu : `[libellé](<file:///chemin littéral>)`, espaces et accents
    en clair entre chevrons. C'est le seul `file://` qu'Obsidian ouvre de façon
    fiable — le percent-encoding y échoue. Le constat vient du traitement des
    grilles locales et vaut identiquement ici.

    `app_base` reste lu depuis le mapping : il ne sert plus qu'au pied du bloc,
    pour qui veut encore la version en ligne.
    """
    by_corpus = {}
    for e in entries:
        by_corpus.setdefault(entry_corpus(e), []).append(e)
    lines = [f"{BLOCK_START} ({len(entries)})"]
    for corpus in CORPUS_ORDER:
        if corpus not in by_corpus:
            continue
        lines.append(f"> **{CORPUS_LABEL[corpus]}**")
        for e in by_corpus[corpus]:
            rel = unicodedata.normalize("NFC", e["file"])
            if rel.startswith("cases/"):
                # grille du dépôt : chemin absolu vers le fichier de travail
                path = unicodedata.normalize("NFC", str(REPO)) + "/" + rel
            else:
                # grille locale du vault
                path = unicodedata.normalize("NFC", str(vault)) + "/" + rel
            lines.append(f"> [{e['label']}](<file://{path}>)")
        lines.append("> ")
    footer = "> 📂 Liens locaux — les grilles s'ouvrent depuis le dépôt de travail"
    if any(not e["file"].startswith("cases/") for e in entries):
        footer += " · 📁 = grille du vault"
    if app_base:
        footer += f" · 🔐 [version en ligne]({app_base}/)"
    lines.append(footer)
    return lines


def inject(text, block_lines):
    """Retourne (nouveau_texte, action). Garantit une ligne vide entre le bloc
    injecté et le contenu suivant (deux callouts adjacents fusionneraient)."""
    lines = text.split("\n")
    norm = [unicodedata.normalize("NFC", l).rstrip() for l in lines]
    head_nfc = unicodedata.normalize("NFC", HEADING)
    bs_nfc = unicodedata.normalize("NFC", BLOCK_START)
    if head_nfc in norm:
        h = norm.index(head_nfc)
        i = h + 1
        while i < len(lines) and norm[i] == "":
            i += 1
        if i < len(norm) and norm[i].startswith(bs_nfc):
            j = i
            while j < len(lines) and lines[j].startswith(">"):
                j += 1
            action = "bloc remplacé"
        else:
            j = h + 1
            action = "bloc inséré"
        tail = lines[j:]
        while tail and tail[0] == "":
            tail.pop(0)
        new = lines[:h + 1] + block_lines + ([""] + tail if tail else [])
        return "\n".join(new), action
    # section absente → la créer juste après le frontmatter
    end = lines.index("---", 1) if lines and lines[0] == "---" else -1
    pre = lines[:end + 1]
    tail = lines[end + 1:]
    while tail and tail[0] == "":
        tail.pop(0)
    new = pre + ([""] if pre else []) + [HEADING] + block_lines + ([""] + tail if tail else [])
    return "\n".join(new), "section créée"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--mapping", default=str(REPO / "docs" / "obsidian-mapping.yaml"))
    args = ap.parse_args()

    conf = parse_mapping(Path(args.mapping))
    vault = Path(conf["vault"])
    app_base = conf["app_base"].rstrip("/")
    stats = {"section créée": 0, "bloc remplacé": 0, "bloc inséré": 0, "inchangé": 0}
    missing = []

    for page, entries in sorted(conf["pages"].items()):
        # les fichiers du vault sont en NFD sur disque : essayer les deux formes
        path = vault / page
        if not path.exists():
            alt = vault / unicodedata.normalize("NFD", page)
            path = alt if alt.exists() else path
        if not path.exists():
            missing.append(page)
            continue
        text = path.read_text(encoding="utf-8")
        block = build_block(entries, app_base, vault)
        new_text, action = inject(text, block)
        if new_text == text:
            action = "inchangé"
        elif not args.dry_run:
            path.write_text(new_text, encoding="utf-8")
        stats[action] += 1
        print(f"{action:14} | {len(entries):3d} grilles | {page}")

    print("\nRésumé :", ", ".join(f"{k}: {v}" for k, v in stats.items()))
    if missing:
        print("⚠️ pages introuvables :", *missing, sep="\n  ")
        sys.exit(1)


if __name__ == "__main__":
    main()
