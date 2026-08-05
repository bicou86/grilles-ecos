#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Convertit les planches d'images d'un corpus en disposition pleine largeur.

Pourquoi. Le `<style>` en ligne des grilles porte deux règles qui décident de la
largeur d'affichage :

    .annexe-item[data-image-id] { width: 49% !important; }
    .annexe-image img           { max-width: 100%; height: auto; }

`max-width` **plafonne sans étirer**. Une planche dense — message-clé,
algorithme, tableau — large de 2190 px s'affiche donc à 496 px dans une colonne
à 49 %, contre 1078 px si l'item occupe toute la largeur. L'arbitrage retenu
pour la campagne est la pleine largeur, sur les deux corpus.

Ce que fait ce script. Dans chaque `<div class="images-wrapper">`, il fusionne
les `<div class="annexe-item"…>` en **un seul** `<div class="annexe-item">` sans
`data-image-id`, en concaténant leur contenu dans l'ordre. Rien n'est supprimé,
rien n'est réordonné : seules disparaissent les balises d'item intermédiaires.

Garanties vérifiées avant écriture, fichier par fichier :

  - le contenu concatené des items est identique avant et après, à l'octet près ;
  - le nombre d'`<img>`, d'`annexe-title`, d'`annexe-description` et
    d'`annexe-image` est inchangé ;
  - les `<div>` restent équilibrés ;
  - le nombre de spans sémantiques est inchangé.

Un fichier qui échoue une seule de ces garanties n'est pas écrit.

Usage
-----
    plates_to_fullwidth.py CORPUS [--check]

    --check   diagnostique sans écrire
"""
import argparse
import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]

OUVRE_WRAP = '<div class="images-wrapper">'
RE_ITEM = re.compile(r'<div class="annexe-item"(?=[ >])[^>]*>')


def _fin_equilibree(html, debut):
    """Rend l'index du `</div>` qui ferme la balise ouverte a `debut`."""
    prof = 0
    for m in re.finditer(r"<div\b|</div>", html[debut:]):
        if m.group(0) == "</div>":
            prof -= 1
            if prof == 0:
                return debut + m.start()
        else:
            prof += 1
    return -1


def _wrappers(html):
    """Rend les couples (debut, fin_du_contenu) de chaque images-wrapper."""
    out = []
    pos = 0
    while True:
        i = html.find(OUVRE_WRAP, pos)
        if i < 0:
            return out
        fin = _fin_equilibree(html, i)
        if fin < 0:
            return out
        out.append((i + len(OUVRE_WRAP), fin))
        pos = fin


def _items(seg):
    """Rend les couples (debut_balise, fin_balise, debut_contenu, fin_contenu)."""
    out = []
    pos = 0
    while True:
        m = RE_ITEM.search(seg, pos)
        if not m:
            return out
        fin = _fin_equilibree(seg, m.start())
        if fin < 0:
            return out
        out.append((m.start(), m.end(), m.end(), fin))
        pos = fin + len("</div>")


def convertit(html):
    """Rend (html_converti, nb_items_fusionnes, motif_d_echec_ou_None)."""
    fusions = 0
    sortie = html
    # De la fin vers le debut : les index des wrappers precedents restent valides.
    for deb, fin in reversed(_wrappers(sortie)):
        seg = sortie[deb:fin]
        items = _items(seg)
        if len(items) < 2 and not (items and "data-image-id" in seg[items[0][0]:items[0][1]]):
            continue                      # deja pleine largeur, rien a faire
        contenus = [seg[c0:c1] for _, _, c0, c1 in items]
        # Ce qui separe les items (indentation, sauts de ligne) est conserve tel
        # quel entre les contenus, pour que la comparaison reste a l'octet pres.
        avant_premier = seg[: items[0][0]]
        apres_dernier = seg[items[-1][3] + len("</div>"):]
        neuf = (avant_premier
                + '<div class="annexe-item">'
                + "".join(contenus)
                + "</div>"
                + apres_dernier)
        sortie = sortie[:deb] + neuf + sortie[fin:]
        fusions += len(items)

    if sortie == html:
        return html, 0, None

    # --- garanties -------------------------------------------------------
    def compte(s, motif):
        return len(re.findall(motif, s))

    for motif, nom in ((r"<img\b", "img"),
                       (r'<div class="annexe-title"', "annexe-title"),
                       (r'<div class="annexe-description"', "annexe-description"),
                       (r'<div class="annexe-image"', "annexe-image"),
                       (r'<span class="c-', "spans semantiques")):
        if compte(html, motif) != compte(sortie, motif):
            return html, 0, "compte de %s modifie (%d -> %d)" % (
                nom, compte(html, motif), compte(sortie, motif))

    if (compte(sortie, r"<div\b") - compte(sortie, r"</div>")) != (
            compte(html, r"<div\b") - compte(html, r"</div>")):
        return html, 0, "solde des <div> modifie"

    # Le texte des items, mis bout a bout, doit etre identique.
    def corps(s):
        bouts = []
        for deb, fin in _wrappers(s):
            seg = s[deb:fin]
            for _, _, c0, c1 in _items(seg):
                bouts.append(seg[c0:c1])
        return "".join(bouts)

    if corps(html) != corps(sortie):
        return html, 0, "contenu des items modifie"

    return sortie, fusions, None


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("corpus")
    ap.add_argument("--check", action="store_true", help="diagnostique sans ecrire")
    args = ap.parse_args()

    rep = REPO / "cases" / args.corpus
    if not rep.is_dir():
        raise SystemExit("corpus introuvable : %s" % rep)

    touchees = intactes = 0
    total_items = 0
    echecs = []
    for p in sorted(rep.glob("*.html")):
        avant = p.read_text(encoding="utf-8")
        apres, n, motif = convertit(avant)
        if motif:
            echecs.append((p.name, motif))
        elif n:
            touchees += 1
            total_items += n
            if not args.check:
                p.write_text(apres, encoding="utf-8")
        else:
            intactes += 1

    verbe = "a convertir" if args.check else "convertie(s)"
    print("%s : %d grille(s) %s (%d items fusionnes), %d deja conforme(s), %d echec(s)"
          % (args.corpus, touchees, verbe, total_items, intactes, len(echecs)))
    for nom, motif in echecs:
        print("  ECHEC %s : %s" % (nom, motif))
    return 1 if echecs else 0


if __name__ == "__main__":
    sys.exit(main())
