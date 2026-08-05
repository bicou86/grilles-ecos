#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Injecte le bloc des classes sémantiques dans le `<style>` en ligne d'un corpus.

Pourquoi. Les classes `c-red` … `c-yellow` sont définies dans
`cases/case-styles.css` (thème clair) et `cases/mobile-responsive.css`
(surcharges `[data-theme="dark"]`). Les corpus `rescos-locales` et `casecos` ne
chargent pas ces feuilles de la même façon que `rescos`, `german` et `amboss` :

    rescos-locales   aucun <link> — ni feuille, ni theme-sync.js
    casecos          <link> mobile-responsive.css seul, + theme-sync.js

Conséquence sans correctif : le balisage sémantique est **visuellement inerte**
sur rescos-locales, et n'apparaît qu'en thème sombre sur casecos.

Ce que fait ce script. Il ajoute le bloc — et lui seul — à la fin du `<style>`
en ligne que chacune de ces grilles porte déjà. Il n'ajoute aucun `<link>` :
injecter les 3 800 lignes de `case-styles.css` dans 363 pages à mise en page
locale risquerait leur rendu, alors que ces quarante lignes ne portent que des
sélecteurs `.c-*`, absents partout ailleurs dans ces fichiers.

Il est **idempotent** : une grille déjà traitée est laissée telle quelle, à
l'octet près. Et il ne touche à rien d'autre — le contrôle de sortie vérifie que
retirer le bloc injecté redonne exactement le fichier d'entrée.

Usage
-----
    inject_semantic_css.py CORPUS [--check]

    --check   diagnostique sans écrire
"""
import argparse
import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]

MARQUE = "/* === Termes colorés : socle sémantique (injecté) === */"

#: Repris à l'identique de `case-styles.css` (bloc « socle partagé ») et de
#: `mobile-responsive.css` (« Termes colorés : variantes sombres »). La classe
#: doublée `.c-red.c-red` porte la spécificité à (0,2,0) — nécessaire pour
#: passer devant les règles de liste qui posent une couleur `!important`.
BLOC = MARQUE + """
.c-red.c-red    { color: var(--ecos-c-red,    #e5484d) !important; font-weight: 600; }
.c-pink.c-pink  { color: var(--ecos-c-pink,   #d6409f) !important; font-weight: 600; }
.c-green.c-green{ color: var(--ecos-c-green,  #30a46c) !important; font-weight: 600; }
.c-blue.c-blue  { color: var(--ecos-c-blue,   #3e63dd) !important; font-weight: 600; }
.c-amber.c-amber{ color: var(--ecos-c-amber,  #9e6c00) !important; font-weight: 600; }
.c-purple.c-purple { color: var(--ecos-c-purple, #8145b5) !important; font-weight: 600; }
.c-orange.c-orange { color: var(--ecos-c-orange, #c44a00) !important; font-weight: 600; }
/* Jaune : FOND de surlignage, pas une couleur de texte. */
.c-yellow.c-yellow {
  background: var(--ecos-c-yellow-bg, #f5c84238) !important;
  border-radius: 3px; padding: 0 0.18em; font-weight: 600;
}
[data-theme="dark"] .c-red.c-red    { color: var(--ecos-c-red,    #ff6369) !important; }
[data-theme="dark"] .c-pink.c-pink  { color: var(--ecos-c-pink,   #f65cb6) !important; }
[data-theme="dark"] .c-green.c-green{ color: var(--ecos-c-green,  #4cc38a) !important; }
[data-theme="dark"] .c-blue.c-blue  { color: var(--ecos-c-blue,   #849dff) !important; }
[data-theme="dark"] .c-amber.c-amber{ color: var(--ecos-c-amber,  #f5e147) !important; }
[data-theme="dark"] .c-purple.c-purple { color: var(--ecos-c-purple, #bf7af0) !important; }
[data-theme="dark"] .c-orange.c-orange { color: var(--ecos-c-orange, #ff9d4d) !important; }
[data-theme="dark"] .c-yellow.c-yellow { background: var(--ecos-c-yellow-bg, #f5c8422e) !important; }
/* === fin du socle sémantique === */
"""


def injecte(html):
    """Rend (html_modifie, etat). `etat` vaut 'deja', 'ok' ou un motif d'echec."""
    if MARQUE in html:
        return html, "deja"
    # Dernier `</style>` : les grilles n'en portent qu'un, mais viser le dernier
    # reste juste s'il y en avait plusieurs — le bloc doit gagner en cascade.
    i = html.rfind("</style>")
    if i < 0:
        return html, "pas de <style> en ligne"
    sortie = html[:i] + "\n" + BLOC + html[i:]
    # Controle d'inversibilite : retirer le bloc doit redonner l'entree exacte.
    if sortie.replace("\n" + BLOC, "", 1) != html:
        return html, "strip-back non inversible"
    return sortie, "ok"


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("corpus", help="nom du corpus, p. ex. rescos-locales")
    ap.add_argument("--check", action="store_true", help="diagnostique sans ecrire")
    args = ap.parse_args()

    rep = REPO / "cases" / args.corpus
    if not rep.is_dir():
        raise SystemExit("corpus introuvable : %s" % rep)

    faits = deja = 0
    echecs = []
    for p in sorted(rep.glob("*.html")):
        avant = p.read_text(encoding="utf-8")
        apres, etat = injecte(avant)
        if etat == "deja":
            deja += 1
        elif etat == "ok":
            faits += 1
            if not args.check:
                p.write_text(apres, encoding="utf-8")
        else:
            echecs.append((p.name, etat))

    verbe = "a injecter" if args.check else "injecte"
    print("%s : %d %s, %d deja pourvue(s), %d echec(s)"
          % (args.corpus, faits, verbe, deja, len(echecs)))
    for nom, motif in echecs:
        print("  ECHEC %s : %s" % (nom, motif))
    return 1 if echecs else 0


if __name__ == "__main__":
    sys.exit(main())
