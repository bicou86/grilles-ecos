"""Appariement des items entre grilles d'une meme SSP.

SOCLE A — normalisation lexicale, sans curation : la numerotation de tete est
retiree, puis `lib_cle.cle()` fait le reste (minuscules, accents, ponctuation,
mots vides francais, pluriel simple, ordre des mots neutralise). Deux libelles
de meme signature sont le meme item. La regle N'EST PAS redefinie ici : elle
est importee de lib_cle, source unique partagee avec check_referentiel.py
(tache 5). Une copie locale divergerait au premier correctif — c'est
exactement ce qui est arrive a l'ancienne regle « plus de trois lettres »,
abandonnee pour une liste explicite de mots vides (voir lib_cle).

Reserve connue, mineure et non bloquante (relecture tache 5) : MOTS_VIDES
contient "a", "d" et "l" pour couvrir les elisions, si bien qu'un prefixe
mnemotechnique d'une seule lettre ("A", "D", "L" en tete de libelle) est
efface de la signature. Aucune collision clinique n'en a resulte sur les
39 615 libelles audites ; la couche B reste le recours si un cas se presente.

COUCHE B — docs/ecos-vocabulaire.yaml donne, par SSP, la forme canonique d'un
libelle brut. Elle n'est consultee que si elle porte une entree : la couche B
corrige le socle A la ou il echoue, elle ne le remplace pas.

Le libelle affiche est celui du premier cas rencontre, sauf si la couche B en
impose un autre. `canonique()` preserve donc la casse et les accents du
libelle d'origine : c'est un libelle d'affichage, pas une cle. La cle de
comparaison, elle, est `signature(canonique(...))`.
"""
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import lib_yaml
from lib_cle import cle

REPO = Path(__file__).resolve().parents[2]
_VOCABULAIRE = None

# Numerotation de tete d'un libelle de grille (« 1. Anamnese »). Retiree avant
# la cle : lib_cle garde les chiffres, qui portent parfois le sens clinique
# (« Score de Wells 2 »), et ne peut pas distinguer seule un rang d'affichage
# d'un chiffre utile.
_NUMEROTATION = re.compile(r"^\d+\.\s*")


def _table():
    global _VOCABULAIRE
    if _VOCABULAIRE is None:
        _VOCABULAIRE = lib_yaml.lire_groupe(REPO / "docs" / "ecos-vocabulaire.yaml")
    return _VOCABULAIRE


def signature(titre):
    """Cle d'appariement du socle A.

    Le repli sur le titre nu couvre le libelle qui ne laisse aucun token une
    fois les mots vides retires : sans lui, deux libelles vides de sens
    lexical fusionneraient sur la cle vide.
    """
    nu = _NUMEROTATION.sub("", titre)
    return cle(nu) or nu.strip().lower()


def canonique(titre, ssp=None):
    """Forme canonique d'un libelle : couche B si elle en porte une, sinon le titre nu."""
    nu = _NUMEROTATION.sub("", titre).strip()
    if ssp:
        return _table().get(ssp, {}).get(nu, nu)
    return nu


def _fusionner(entrees, ssp):
    """[(titre, sous, id_cas)] -> [{titre, sous, cas}] apparies par signature."""
    groupes = {}
    for titre, sous, cid in entrees:
        cle_t = signature(canonique(titre, ssp))
        g = groupes.setdefault(cle_t, {"titre": canonique(titre, ssp), "sous": {}, "cas": set()})
        g["cas"].add(cid)
        for s in sous:
            cle_s = signature(canonique(s, ssp))
            gs = g["sous"].setdefault(cle_s, {"titre": canonique(s, ssp), "cas": set()})
            gs["cas"].add(cid)
    return [{"titre": g["titre"], "cas": g["cas"], "sous": list(g["sous"].values())}
            for g in groupes.values()]


def apparier(cas_list, prefixe, ssp=None):
    """Items d'une section, apparies entre tous les cas fournis."""
    entrees = []
    for cas in cas_list:
        for genre, _, titre, sous in cas["sections"].get(prefixe, []):
            if genre == "item":
                entrees.append((titre, sous or [], cas["id"]))
    return _fusionner(entrees, ssp)
