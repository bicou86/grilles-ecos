"""Inventaire des libelles bruts du corpus, par SSP — socle de la couche B.

POURQUOI UN MODULE PLUTOT QU'UNE FONCTION LOCALE. La couche B
(docs/ecos-vocabulaire.yaml) s'applique sur le LIBELLE NU LITTERAL :
`lib_fusion.canonique()` retire la numerotation de tete, coupe les espaces de
bord, puis fait un `dict.get()` exact. Une entree dont la cle differe d'un
accent, d'une espace ou d'une majuscule est SILENCIEUSEMENT sans effet — la
table est un dictionnaire, pas une grammaire, et un `get()` qui rate rend le
libelle d'origine sans rien signaler.

Trois consommateurs ont donc besoin de la MEME notion de « libelle reel » :
check_vocabulaire.py (qui refuse une entree qui ne correspond a rien),
report_doublons.py (qui propose des candidats) et l'auteur d'une entree.
Une copie locale de la regle divergerait au premier correctif de
`_NUMEROTATION` — c'est le raisonnement de lib_cle, applique ici.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import build_memento                                      # noqa: E402
import lib_fusion                                         # noqa: E402

SECTIONS = ("a", "e", "m")


def libelle_nu(titre):
    """Le libelle tel que la couche B le voit : numerotation de tete retiree, borde.

    Exactement la transformation que `lib_fusion.canonique()` applique avant
    son `get()`. Elle est reprise d'ici plutot que recopiee, pour qu'un
    changement de `_NUMEROTATION` ne puisse pas rendre l'inventaire faux sans
    rendre l'appariement faux de la meme facon.
    """
    return lib_fusion._NUMEROTATION.sub("", titre).strip()


def libelles_par_ssp(groupes):
    """SSP -> {libelle nu: {identifiants de grille qui le portent}}.

    Titres d'item ET sous-items confondus, sur les trois sections : la couche B
    s'applique aux deux sans distinction (`lib_fusion._fusionner` appelle
    `canonique()` sur le titre puis sur chaque sous-item), donc l'inventaire
    qui la garde doit couvrir les deux.
    """
    out = {}
    for ssp, cas_list in groupes.items():
        table = out.setdefault(ssp, {})
        for cas in cas_list:
            for prefixe in SECTIONS:
                for genre, _, titre, sous in cas["sections"].get(prefixe, []):
                    if genre != "item":
                        continue
                    for brut in [titre] + list(sous or []):
                        table.setdefault(libelle_nu(brut), set()).add(cas["id"])
    return out


def inventaire(lot=None):
    """Raccourci : l'inventaire du corpus entier (ou du lot donne)."""
    return libelles_par_ssp(build_memento.par_ssp(lot))
