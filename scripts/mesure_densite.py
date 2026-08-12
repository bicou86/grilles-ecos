#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Mesure la densité de balisage sémantique, par corpus et par bloc pédagogique.

Le NOMBRE de spans par grille ne veut rien dire : triage en a 26 par grille contre
252 pour german, mais ses sections pédagogiques font 228 mots contre 3 243. Seule la
densité rapportée au texte permet de comparer deux corpus. C'est cette mesure, et elle
seule, qui a servi à établir qu'azygos était le seul en déficit.

Usage :
    python3 scripts/mesure_densite.py                 # tous les corpus, bloc `theorie`
    python3 scripts/mesure_densite.py azygos          # un corpus
    python3 scripts/mesure_densite.py --bloc resume   # un autre bloc
"""
from __future__ import annotations

import argparse
import html
import re
import statistics
from pathlib import Path

CASES = Path(__file__).resolve().parents[1] / "cases"

CORPUS = ["amboss", "azygos", "casecos", "german", "rescos",
          "rescos-locales", "triage", "usmle"]

SPAN = re.compile(r'class="c-(?:red|pink|green|blue|amber|purple|orange|yellow)"')

#: Ouverture de chaque bloc pédagogique, et ce qui le termine. Le bornage est
#: la seule difficulté de cette mesure : trop large, il compte du texte non
#: colorisable (labels, titres de section notée) et écrase la densité.
BLOCS = {
    "resume": (r'<div class="resume">',
               r'<div class="annexes">'),
    "theorie": (r'<div class="annexe-item annexe-theorie">',
                r'<div class="annexe-item annexe-(?:expert|scenario|dd)"'
                r'|<div class="presentation-patient">'
                r'|<div class="images-wrapper">|<!--\s*COMMENTAIRE'),
    "presentation": (r'<div class="presentation-patient">',
                     r'<div class="annexe-item annexe-scenario"'
                     r'|<div class="images-wrapper">|<!--\s*COMMENTAIRE'),
}


def _zone(texte: str, bloc: str) -> str:
    ouv, fin = BLOCS[bloc]
    m = re.search(ouv, texte)
    if not m:
        return ""
    f = re.search(fin, texte[m.end():])
    return texte[m.start(): m.end() + f.start()] if f else texte[m.start():]


def _mots(segment: str) -> int:
    plat = re.sub(r"<[^>]+>", " ", segment)
    return len(re.sub(r"\s+", " ", html.unescape(plat)).split())


def densite(corpus: str, bloc: str = "theorie") -> dict:
    """Densité médiane de spans pour 1000 mots, sur les grilles qui portent le bloc."""
    spans = mots = grilles = 0
    par_grille: list[float] = []
    for fichier in sorted((CASES / corpus).glob("*.html")):
        zone = _zone(fichier.read_text(encoding="utf-8", errors="replace"), bloc)
        if not zone:
            continue
        n, m = len(SPAN.findall(zone)), _mots(zone)
        grilles += 1
        spans += n
        mots += m
        # Sous 100 mots, le rapport est trop instable pour entrer dans la médiane.
        if m >= 100:
            par_grille.append(1000 * n / m)
    return {"grilles": grilles, "spans": spans, "mots": mots,
            "mediane": statistics.median(par_grille) if par_grille else 0.0}


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("corpus", nargs="*", default=CORPUS, help="corpus à mesurer")
    ap.add_argument("--bloc", default="theorie", choices=sorted(BLOCS),
                    help="bloc pédagogique mesuré (défaut : theorie)")
    args = ap.parse_args()

    print(f"Densité de balisage sémantique — bloc `{args.bloc}`")
    print(f"{'corpus':16} {'grilles':>8} {'spans':>8} {'mots':>8} "
          f"{'spans/1000 mots':>16}")
    for nom in args.corpus:
        d = densite(nom, args.bloc)
        print(f"{nom:16} {d['grilles']:>8} {d['spans']:>8} {d['mots']:>8} "
              f"{d['mediane']:>16.1f}")


if __name__ == "__main__":
    main()
