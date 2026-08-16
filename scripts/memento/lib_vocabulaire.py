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


def positions_par_ssp(groupes):
    """SSP -> {(grille, section): {libelle: {emplacements}}}.

    L'emplacement est « en tête » ou « sous « <parent> » ». Il sert au controle
    de collision : deux libelles qu'UNE MEME grille porte dans UNE MEME section
    ne sont pas deux facons de dire la meme chose, ce sont deux questions que
    l'auteur de cette grille a voulu distinguer. Les reunir effacerait sa
    distinction — et rien, au rendu, ne le dirait.

    LA SECTION SUFFIT A DELIMITER, PAS BESOIN DU PARENT. Un libelle de tete et
    un sous-item d'une meme section entrent aussi en concurrence : German-75
    (Toux) porte « Allergies » en tete AVEC « Allergies connues » en sous-item,
    et rabattre le second sur le premier ferait avaler a l'item son propre
    sous-item. L'emplacement est donc rapporte pour le diagnostic, pas retenu
    comme critere.
    """
    out = {}
    for ssp, cas_list in groupes.items():
        table = out.setdefault(ssp, {})
        for cas in cas_list:
            for prefixe in SECTIONS:
                seau = table.setdefault((cas["id"], prefixe), {})
                for genre, _, titre, sous in cas["sections"].get(prefixe, []):
                    if genre != "item":
                        continue
                    tete = libelle_nu(titre)
                    seau.setdefault(tete, set()).add("en tête")
                    for brut in (sous or []):
                        seau.setdefault(libelle_nu(brut), set()).add(f"sous « {tete} »")
    return out


def inventaire(lot=None):
    """Raccourci : l'inventaire du corpus entier (ou du lot donne)."""
    return libelles_par_ssp(build_memento.par_ssp(lot))
