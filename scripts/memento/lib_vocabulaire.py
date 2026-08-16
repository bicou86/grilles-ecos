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


# NEGATION ASYMETRIQUE — l'angle mort que la ronde 1 de curation a paye cinq
# fois, et la raison pour laquelle cette regle vit ICI et non dans l'un de ses
# deux consommateurs.
#
# `report_doublons.antonymie()` exige un mot de CHAQUE cote : elle compare les
# mots propres a l'un aux mots propres a l'autre, et rend None des que l'un des
# deux ensembles est vide. Or « Hepatomegalie » et « Pas d'hepatomegalie » ne
# different que par un mot present d'UN SEUL cote. TROIS mecanismes regardaient
# exactement la sans rien voir : `ANTONYMES` ne connait ni « pas » ni « sans » ;
# `lib_cle.MOTS_VIDES` ne les efface pas ; et aucune grille ne portant les deux
# libelles, la propriete 8 de `check_vocabulaire` n'avait pas de temoin.
# Resultat mesure : cinq entrees ont retenu la forme NEGATIVE comme intitule, et
# il a fallu les inverser a la main apres coup — dans une checklist, « Pas de
# turgescence jugulaire » se lit comme un RESULTAT, pas comme un geste a faire.
#
# EFFACER CES MOTS DANS `lib_cle.MOTS_VIDES` SERAIT LE MAUVAIS CORRECTIF, et
# c'est le seul des trois angles morts qu'il ne faut SURTOUT PAS boucher ainsi :
# « Pas d'hepatomegalie » et « Hepatomegalie » partageraient alors leur
# SIGNATURE, et le socle A les confondrait tout seul, sans table, sans entree et
# sans trace. La negation doit rester VISIBLE dans la cle ; elle est SIGNALEE
# par `report_doublons` et REFUSEE par la propriete 10 de `check_vocabulaire` —
# deux consommateurs, une seule liste, comme lib_cle pour la cle.
#
# LES MOTS SONT DECLARES EN FRANCAIS PUIS CANONISES, JAMAIS ECRITS EN JETONS.
# `lib_cle._singulier` ampute le « s » final de tout mot de plus de trois
# lettres : « sans » devient « san » et « jamais » devient « jamai ». Une liste
# ecrite a la main en jetons aurait rate ces deux-la en silence.
#
# DEUX MOTS ONT ETE ECARTES APRES COMPTAGE SUR LE CORPUS, et le motif est garde
# pour qu'on ne les rajoute pas par reflexe :
#
#   « ni »                — ses trois occurrences accompagnent TOUTES une autre
#                           negation (« Jamais hospitalise ni opere », « Pas de
#                           si, ni de mais »). Le retirer de la liste ne change
#                           la reponse du detecteur sur aucun libelle du corpus :
#                           il serait un mot decoratif, que `check_negation.py`
#                           refuse par construction.
#   « negatif/negative »  — deux de ses sept occurrences ne nient rien, elles
#                           qualifient (« Poursuite malgre consequences
#                           NEGATIVES », « pression sociale NEGATIVE ») ; les
#                           cinq autres nient bien un resultat (« Criteres
#                           d'Ottawa negatifs »). Aucune paire candidate du
#                           rapport ne les oppose aujourd'hui : le mot
#                           n'apporterait que ses faux positifs.
NEGATIONS_MOTS = ("absence", "aucun", "aucune", "jamais", "non", "pas", "sans")
NEGATIONS = frozenset(t for m in NEGATIONS_MOTS for t in lib_fusion.cle(m).split())


def nie(libelle):
    """Les mots de negation que ce libelle porte, dans l'espace des jetons de la cle."""
    return set(lib_fusion.cle(libelle).split()) & NEGATIONS


def negation(a, b):
    """Le mot de negation qu'UN SEUL des deux libelles porte, ou None.

    Le test porte sur l'ASYMETRIE et non sur la presence : deux libelles qui
    nient tous les deux (« Pas de fievre » / « Pas de frissons ») ne sont pas
    signales, leur ecart n'etant pas la negation mais ce qui la suit.
    """
    na, nb = nie(a), nie(b)
    if bool(na) == bool(nb):
        return None
    return sorted(na | nb)[0]
