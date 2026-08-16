#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Repartit les planches d'images d'un corpus entre deux colonnes et pleine largeur.

Pourquoi. Le `<style>` en ligne des grilles porte deux regles qui decident de la
largeur d'affichage :

    .annexe-item[data-image-id] { width: 49% !important; }
    .annexe-image img           { max-width: 100%; height: auto; }

`max-width` plafonne sans etirer. Une image plus etroite que sa colonne s'affiche
donc a sa taille native, qu'elle soit seule sur la ligne ou non : lui donner
toute la largeur ne lui apporte rien et laisse la moitie de la planche vide. Une
planche dense au contraire — message-cle, algorithme, tableau — mesure de 1500 a
3200 px et tombe de 1078 px a 528 px des qu'on la met en colonne : elle devient
illisible.

L'arbitrage precedent (`plates_to_fullwidth.py`, supprime par ce script) mettait
tout en pleine largeur pour proteger les planches denses, au prix d'une demi-page
blanche a cote de chaque photo de geste. L'arbitrage retenu ici est adaptatif :

    largeur native <= SEUIL px  ->  <div class="annexe-item" data-image-id="imgN">
    largeur native >  SEUIL px  ->  <div class="annexe-item">

Aucune regle CSS n'est touchee : c'est la presence ou l'absence de
`data-image-id` qui decide, exactement le vocabulaire deja present dans les
grilles. Un SVG est toujours mis en colonne — il est vectoriel, il se redessine
net a n'importe quelle taille. Une image illisible reste en pleine largeur, par
prudence.

Ce que fait ce script. Dans chaque `<div class="images-wrapper">`, il eclate les
`<div class="annexe-item"…>` en **un item par image**. La campagne precedente
avait concatene plusieurs triplets titre/description/image dans un meme item :
chacun retrouve ici son propre conteneur, et donc sa propre largeur.

Garanties verifiees avant ecriture, fichier par fichier :

  - la suite ordonnee des blocs annexe-title, annexe-description et annexe-image
    est identique avant et apres, a l'octet pres ;
  - le nombre d'`<img>` et de spans semantiques est inchange ;
  - les `<div>` restent equilibres.

Un fichier qui echoue une seule de ces garanties n'est pas ecrit.

Usage
-----
    plates_widths.py CORPUS [--seuil 1100] [--check]

    --check   diagnostique sans ecrire
"""
import argparse
import base64
import io
import re
import sys
from pathlib import Path

from PIL import Image

Image.MAX_IMAGE_PIXELS = None

REPO = Path(__file__).resolve().parents[1]
SEUIL_DEFAUT = 1100

OUVRE_WRAP = '<div class="images-wrapper">'
RE_ITEM = re.compile(r'<div class="([^"]*\bannexe-item\b[^"]*)"[^>]*>')
RE_BLOC = re.compile(r'<div class="annexe-(title|description|image)">')
RE_SRC = re.compile(r'<img[^>]*\ssrc="([^"]*)"')
# Classe posee par le socle AMBOSS pour forcer la pleine largeur d'un panneau de
# texte en image (cases/case-styles.css : flex 0 0 100%). Elle est conservee
# telle quelle et vaut decision : un item qui la porte ne prend jamais de
# data-image-id, quelle que soit la largeur mesuree.
PLEINE_LARGEUR = "annexe-message-cle"


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
    """Rend les couples (debut_du_contenu, fin_du_contenu) de chaque wrapper."""
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


def _blocs(seg):
    """Rend la suite des blocs annexe-title/description/image d'un segment.

    Chaque element est le triplet (genre, texte_integral_du_div, position).
    """
    out = []
    pos = 0
    while True:
        m = RE_BLOC.search(seg, pos)
        if not m:
            return out
        fin = _fin_equilibree(seg, m.start())
        if fin < 0:
            return out
        out.append((m.group(1), seg[m.start():fin + len("</div>")], m.start()))
        pos = fin + len("</div>")


def _classes_par_position(seg):
    """Rend les tranches (debut, fin, classes_en_plus) de chaque annexe-item.

    Sert a retrouver les classes de l'item qui contenait une unite donnee — le
    socle AMBOSS en pose une, `annexe-message-cle`, qui vaut decision de mise en
    page et ne doit pas disparaitre a la reecriture.
    """
    out = []
    pos = 0
    while True:
        m = RE_ITEM.search(seg, pos)
        if not m:
            return out
        fin = _fin_equilibree(seg, m.start())
        if fin < 0:
            return out
        sup = [c for c in m.group(1).split() if c != "annexe-item"]
        out.append((m.end(), fin, sup))
        pos = fin + len("</div>")


def _unites(blocs):
    """Groupe les blocs en unites, une par image : title, [description], image."""
    unites, courante = [], []
    for bloc in blocs:
        if bloc[0] == "title" and courante:
            unites.append(courante)
            courante = []
        courante.append(bloc)
    if courante:
        unites.append(courante)
    return unites


def largeur_native(src, racine):
    """Rend la largeur en px de l'image, ou None si elle est indechiffrable."""
    try:
        if src.startswith("data:"):
            brut = base64.b64decode(src.split(",", 1)[1])
            return Image.open(io.BytesIO(brut)).width
        if src.split("?")[0].lower().endswith(".svg"):
            return 0                       # vectoriel : toujours en colonne
        return Image.open((racine / src).resolve()).width
    except Exception:
        return None


def convertit(html, chemin, seuil):
    """Rend (html_converti, nb_colonnes, nb_pleine_largeur, motif_d_echec)."""
    racine = chemin.parent
    sortie = html
    n_col = n_plein = 0
    # De la fin vers le debut : les index des wrappers precedents restent valides.
    for deb, fin in reversed(_wrappers(sortie)):
        seg = sortie[deb:fin]
        unites = _unites(_blocs(seg))
        if not unites:
            continue
        tranches = _classes_par_position(seg)
        morceaux, rang = [], 0
        for unite in unites:
            ou = unite[0][2]
            sup = next((c for d, f, c in tranches if d <= ou < f), [])
            srcs = [m.group(1) for _, t, _ in unite for m in RE_SRC.finditer(t)]
            largeurs = [largeur_native(s, racine) for s in srcs]
            # Une image illisible, plus large que le seuil, ou dont l'item porte
            # deja la classe pleine largeur, n'est pas mise en colonne.
            colonne = (bool(largeurs)
                       and PLEINE_LARGEUR not in sup
                       and all(l is not None and l <= seuil for l in largeurs))
            classe = " ".join(["annexe-item"] + sup)
            if colonne:
                rang += 1
                n_col += 1
                ouvre = '<div class="%s" data-image-id="img%d">' % (classe, rang)
            else:
                n_plein += 1
                ouvre = '<div class="%s">' % classe
            corps = "".join("\n    " + t for _, t, _ in unite)
            morceaux.append(ouvre + corps + "\n</div>")
        sortie = sortie[:deb] + "\n" + "\n".join(morceaux) + "\n" + sortie[fin:]

    if sortie == html:
        return html, 0, 0, None

    # --- garanties -------------------------------------------------------
    def compte(s, motif):
        return len(re.findall(motif, s))

    for motif, nom in ((r"<img\b", "img"), (r'<span class="c-', "spans semantiques"),
                       (r'\b' + PLEINE_LARGEUR + r'\b', PLEINE_LARGEUR)):
        if compte(html, motif) != compte(sortie, motif):
            return html, 0, 0, "compte de %s modifie (%d -> %d)" % (
                nom, compte(html, motif), compte(sortie, motif))

    if (compte(sortie, r"<div\b") - compte(sortie, r"</div>")) != (
            compte(html, r"<div\b") - compte(html, r"</div>")):
        return html, 0, 0, "solde des <div> modifie"

    def corps_wrappers(s):
        return [b[:2] for deb, fin in _wrappers(s) for b in _blocs(s[deb:fin])]

    if corps_wrappers(html) != corps_wrappers(sortie):
        return html, 0, 0, "contenu des blocs modifie"

    return sortie, n_col, n_plein, None


def main():
    ap = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("corpus")
    ap.add_argument("--seuil", type=int, default=SEUIL_DEFAUT,
                    help="largeur native au-dela de laquelle l'image reste pleine largeur")
    ap.add_argument("--check", action="store_true", help="diagnostique sans ecrire")
    args = ap.parse_args()

    rep = REPO / "cases" / args.corpus
    if not rep.is_dir():
        raise SystemExit("corpus introuvable : %s" % rep)

    touchees = intactes = 0
    total_col = total_plein = 0
    echecs = []
    for p in sorted(rep.glob("*.html")):
        avant = p.read_text(encoding="utf-8")
        apres, n_col, n_plein, motif = convertit(avant, p, args.seuil)
        if motif:
            echecs.append((p.name, motif))
        elif n_col or n_plein:
            touchees += 1
            total_col += n_col
            total_plein += n_plein
            if not args.check:
                p.write_text(apres, encoding="utf-8")
        else:
            intactes += 1

    verbe = "a convertir" if args.check else "convertie(s)"
    print("%s (seuil %d px) : %d grille(s) %s, %d image(s) en colonne, "
          "%d en pleine largeur, %d deja conforme(s), %d echec(s)"
          % (args.corpus, args.seuil, touchees, verbe, total_col, total_plein,
             intactes, len(echecs)))
    for nom, motif in echecs:
        print("  ECHEC %s : %s" % (nom, motif))
    return 1 if echecs else 0


if __name__ == "__main__":
    sys.exit(main())
