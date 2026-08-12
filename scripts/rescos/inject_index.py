#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Régénère la section `rescos` d'index.html à partir des grilles présentes.

Pourquoi ce script existe. Les 34 grilles RESCOS-41 à 70 ont rejoint
`cases/rescos/` depuis `cases/rescos-locales/`. La section `rescos` de la page
d'accueil était écrite en dur avec ses 41 cartes d'origine ; il fallait y
verser les nouvelles sans perdre le travail de classement déjà fait.

D'où le principe : les cartes existantes sont RELUES dans `index.html`, pas
réinventées. Leur `data-system`, leur titre et leur sous-titre sont conservés
tels quels — c'est un classement éditorial, et le regénérer à partir d'une
heuristique le dégraderait. Seules les grilles absentes de la page reçoivent
des valeurs déduites de leur contenu.

Idempotent : relancé sans changement dans `cases/rescos/`, il réécrit une
section identique à l'octet près.

    python3 scripts/rescos/inject_index.py [--check]
"""
from __future__ import annotations

import argparse
import html as H
import re
import sys
import unicodedata
from pathlib import Path
from urllib.parse import quote, unquote

sys.path.insert(0, str(Path(__file__).parent))
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "amboss"))
import lib_rescos as lib  # noqa: E402

RACINE = Path(__file__).resolve().parents[2]
INDEX = RACINE / "index.html"

DEBUT_SECTION = '      <div class="section" data-section="rescos">'

# Reprise de `scripts/rescos-locales/inject_index.py` : mêmes familles, même
# ordre, première correspondance gagnante. Ne sert QUE pour les grilles encore
# absentes de la page.
SYSTEMES: list[tuple[str, str]] = [
    ("Urgences", r"urgence|polytraumatis|choc (septique|anaphylactique)|arr[êe]t cardio|intoxication"),
    ("Cardiologie", r"thoracique|stemi|infarctus|coronar|insuffisance cardiaque|palpitation|syncope"),
    ("Vasculaire", r"an[ée]vrisme|aomi|claudication|tvp|thrombose|embolie pulmonaire|oed[èe]mes? des mi"),
    ("Pneumologie", r"bpco|asthme|pneumonie|dyspn[ée]e|pneumothorax|toux|tuberculose"),
    ("Gastro-entérologie", r"abdomin|digestif|diarrh|constipation|rectorragie|ict[èe]re|il[ée]us|"
                           r"vomissement|dysphagie|h[ée]morro|cholest[ée]rol"),
    ("Neurologie", r"neurolog|avc|c[ée]phal[ée]|migraine|[ée]pilep|convuls|par[ée]sie|paralysie|"
                   r"vertige|tremblement|[ée]quilibre|ralentissement"),
    ("Psychiatrie", r"psy|d[ée]pression|d[ée]pressif|anxi|panique|suicid|alcool|tabac|"
                    r"entretien motivationnel|em "),
    ("Pédiatrie", r"p[ée]diatr|nourrisson|enfant|adolescent|boiterie"),
    ("Gynécologie", r"gyn[ée]colog|grossesse|obst[ée]tr|contraception|pelvien|sein"),
    ("Urologie/Néphrologie", r"urolog|n[ée]phro|urinaire|mictionnel|dysurie|h[ée]maturie|r[ée]nal"),
    ("Rhumatologie", r"rhumato|articul|arthrite|arthrose|lombalgie|dos\b|fracture|entorse|"
                     r"traumatisme|[ée]paule|genou|hanche|jambe|mollet"),
    ("Dermatologie", r"dermato|cutan|[ée]ruption|prurit|zona|[ée]ryth[èe]me"),
    ("ORL", r"orl|otite|angine|sinusite|[ée]pistaxis"),
    ("Ophtalmologie", r"ophtalmo|[œo]il|oculaire|amaurose|diplopie|vision"),
    ("Endocrinologie", r"endocrin|diab[èe]te|thyro[ïi]d|ob[ée]sit"),
    ("Hématologie/Oncologie", r"oncolog|cancer|tumeur|an[ée]mie|ad[ée]nopathie|palliati|bbn"),
    ("Gériatrie", r"g[ée]riatr|chute|ems|sujet [âa]g[ée]"),
    ("Médecine générale", r"."),
]


def _norm(txt: str) -> str:
    plat = unicodedata.normalize("NFD", txt.lower())
    return "".join(c for c in plat if unicodedata.category(c) != "Mn")


def systeme(titre: str) -> str:
    plat = _norm(titre)
    for nom, motif in SYSTEMES:
        if re.search(_norm(motif), plat):
            return nom
    return "Médecine générale"


def cartes_existantes(texte: str) -> dict[str, dict]:
    """Relit les cartes `rescos` déjà dans la page, indexées par nom de fichier."""
    connues: dict[str, dict] = {}
    motif = re.compile(
        r'<a\s*\n\s*class="card rescos"\s*\n'
        r'\s*data-system="([^"]*)"\s*\n'
        r'\s*href="cases/rescos/([^"]*)"\s*\n'
        r'\s*><span class="num">[^<]*</span>\s*\n'
        r'\s*<div class="info">\s*\n'
        r'\s*<div class="title">(.*?)</div>\s*\n'
        r'\s*<div class="sub">(.*?)</div>', re.S)
    # `H.unescape` est indispensable : les valeurs relues sont DÉJÀ échappées
    # dans la page, et les ré-échapper ferait grossir le fichier à chaque
    # exécution — `&amp;` devenant `&amp;amp;`. Mesuré avant correction :
    # +1 750 octets par passage.
    for m in motif.finditer(texte):
        connues[unquote(m.group(2))] = {
            "systeme": H.unescape(m.group(1)),
            "titre": H.unescape(re.sub(r"\s+", " ", m.group(3)).strip()),
            "sub": H.unescape(re.sub(r"\s+", " ", m.group(4)).strip()),
        }
    return connues


def lit(path: Path) -> tuple[str, str]:
    """Titre et description patient, lus DANS la grille."""
    texte = path.read_text(encoding="utf-8", errors="replace")
    m = re.search(r"<title>(.*?)</title>", texte, re.S)
    titre = H.unescape(m.group(1)).strip() if m else path.stem
    titre = re.sub(r"^RESCOS-[\w]+\s*[-–]\s*", "", titre)
    titre = re.sub(r"\s*[-–]\s*Grille ECOS\s*$", "", titre).strip()

    m = re.search(r"<p[^>]*>\s*👤\s*(.*?)</p>", texte, re.S)
    sub = "RESCOS"
    if m:
        sub = re.sub(r"\s+", " ", re.sub(r"<[^>]+>", "", H.unescape(m.group(1)))).strip(" .")
        if len(sub) > 120:
            sub = sub[:117].rstrip() + "…"
    return titre, sub


def section(texte: str) -> str:
    grilles = list(lib.grids())
    connues = cartes_existantes(texte)
    lignes = [DEBUT_SECTION,
              '        <div class="section-header">',
              '          <span class="badge rescos">RESCOS</span>',
              f"          <h2>{len(grilles)} cas</h2>",
              '          <span class="count"></span>', "        </div>",
              '        <div class="grid">']
    for path in grilles:
        num, suffixe = lib.grid_num(path)
        connue = connues.get(path.name)
        if connue:
            sys_, titre, sub = connue["systeme"], connue["titre"], connue["sub"]
        else:
            titre, sub = lit(path)
            sys_ = systeme(path.stem)
        lignes += [
            "          <a",
            '            class="card rescos"',
            f'            data-system="{H.escape(sys_, quote=True)}"',
            f'            href="cases/rescos/{quote(path.name)}"',
            f'            ><span class="num">{num}{suffixe}</span>',
            '            <div class="info">',
            f'              <div class="title">{H.escape(titre, quote=True)}</div>',
            f'              <div class="sub">{H.escape(sub, quote=True)}</div>',
            "            </div>",
            '            <span class="cat-tag">RES</span></a',
            "          >",
        ]
    lignes += ["        </div>", "      </div>"]
    return "\n".join(lignes) + "\n"


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--check", action="store_true", help="diagnostique sans écrire")
    args = ap.parse_args()

    texte = INDEX.read_text(encoding="utf-8")
    avant = len(texte)

    debut = texte.index(DEBUT_SECTION)
    # Fin de section : la prochaine ouverture de section, ou le bloc no-results.
    suite = re.compile(r'      <div class="section" data-section="|'
                       r'      <div class="no-results"|      <!-- ')
    m = suite.search(texte, debut + len(DEBUT_SECTION))
    if not m:
        print("ÉCHEC — fin de la section rescos introuvable")
        return 1
    fin = m.start()

    nouveau = texte[:debut] + section(texte) + texte[fin:]
    if args.check:
        print("identique" if nouveau == texte else "la section changerait")
        return 0

    INDEX.write_text(nouveau, encoding="utf-8")
    print(f"index.html : {avant} → {len(nouveau)} octets")
    print(f"  {nouveau.count('class=\"card rescos\"')} × class=\"card rescos\"")
    return 0


if __name__ == "__main__":
    sys.exit(main())
