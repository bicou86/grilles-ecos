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

    Le repli couvre le libelle qui ne laisse aucun token une fois les mots
    vides retires : sans lui, tous ces libelles partageraient la cle vide et
    fusionneraient entre eux. Il se fait en deux temps parce que la
    numerotation retiree peut etre tout le libelle — « 2. » donne un titre nu
    vide, et sans le second repli sur le titre d'origine, « 2. » et « 3. »
    fusionneraient. Ne restent alors confondus que deux libelles reellement
    identiques, ce qui est le comportement voulu.

    Ce repli garde accents et ponctuation, deliberement : arrive la, le
    libelle n'a plus aucun contenu lexical, sa graphie brute est la seule
    information qui subsiste. La consequence ne peut etre que de SEPARER deux
    libelles degeneres, jamais d'en rapprocher deux a tort — le seul sens ou
    se tromper soit sans danger pour un appariement clinique. Normaliser
    davantage supposerait de recopier ici la normalisation de lib_cle, la
    duplication meme que ce module refuse.
    """
    nu = _NUMEROTATION.sub("", titre)
    return cle(nu) or nu.strip().lower() or titre.strip().lower()


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


def scinder_management(cas_list, diag_par_cas, ssp=None, attendus=()):
    """Management -> (items partages par plusieurs diagnostics, {diagnostic: items propres}).

    L'anamnese d'une SSP est presque superposable d'un cas a l'autre ; son
    management ne l'est pas — il depend du diagnostic. Un item PROPRE a un
    diagnostic va dans son sous-bloc ; un item porte par DEUX diagnostics OU
    PLUS part dans un encadre partage, en tete, ou il n'est ecrit qu'une fois.

    LE SEUIL EST « DEUX », PAS « TOUS » (decision de l'auteur, ronde 1 de la
    tache 9). La regle initiale — commun = porte par TOUS les diagnostics —
    ne se declenchait que sur 2 des 23 SSP a plusieurs diagnostics : au-dela
    de trois diagnostics, aucun item lexicalement identique ne les couvre
    tous, si bien que « Diagnostics differentiels » etait recopie dans huit
    sous-blocs de « Douleur Abdominale ». Le seuil a deux retire 31 % des
    lignes de ce memento, et ce sont les lignes creuses qui partent.

    LA CONTREPARTIE, et elle est reelle : l'encadre partage se lit AVEC le
    sous-bloc de son diagnostic, plus a sa place. C'est pourquoi chaque item
    partage NOMME ses diagnostics au rendu (`lib_rendu.marque_partage`) —
    sans quoi le seuil echangerait de la redondance contre de l'imprecision.

    `attendus` — decision de l'auteur du 2026-08-15 — est la liste des
    diagnostics que la SSP DEVRAIT couvrir (champ `diagnostics` de
    docs/ecos-priorites-2026.yaml). Chacun recoit une entree, meme si aucune
    grille du corpus ne le documente : le memento doit dire a l'etudiant ce
    qu'il devrait savoir, pas seulement ce que le corpus contient.

    Une entree vide est ambigue ici : elle dit « aucun item PROPRE », que ce
    soit faute de grille ou parce que tout le management de ce diagnostic est
    partage. Les deux se distinguent en lisant `diag_par_cas` et les sections,
    ce que fait le rendu — plutot que de rendre deux structures que
    l'appariement n'a aucun moyen d'interpreter.

    UN ITEM DONT AUCUNE GRILLE PORTEUSE N'A DE DIAGNOSTIC RESOLU part dans le
    partage : le renvoyer vers un sous-bloc est impossible (il n'y en a aucun
    a nommer) et l'ecarter le supprimerait du memento. C'est la seule raison
    pour laquelle le test porte sur `len(porteurs) != 1` et non `>= 2`.
    """
    apparies = apparier(cas_list, "m", ssp)
    diagnostics = {diag_par_cas[c["id"]] for c in cas_list if c["id"] in diag_par_cas}

    partage, propres = [], {d: [] for d in diagnostics | set(attendus)}
    for item in apparies:
        porteurs = {diag_par_cas[c] for c in item["cas"] if c in diag_par_cas}
        if len(porteurs) != 1:
            partage.append(item)
        else:
            propres[porteurs.pop()].append(item)
    return partage, propres


def restreindre(items, cas_cible):
    """Vue d'items limitee aux grilles de `cas_cible`, sans toucher aux originaux.

    Un item apparie porte les grilles de TOUTE la SSP. Dans un sous-bloc de
    diagnostic, le lire tel quel ferait dire a `lib_rendu.marque()` « 3 grilles
    sur 2 » : un numerateur compte sur la SSP, un denominateur compte sur le
    seul diagnostic. La vue restreinte rend les deux comparables.

    DEPUIS LE SEUIL A DEUX, cette restriction ne mord plus que dans un cas :
    un item porte a la fois par une grille du diagnostic et par une grille
    SANS diagnostic resolu. `scinder_management` n'envoie en effet dans un
    sous-bloc que les items dont tous les porteurs diagnostiques valent ce
    diagnostic-la — les porteurs sans diagnostic, eux, y restent. Le corpus
    n'en compte aucun aujourd'hui ; la fonction reste, parce qu'un seul cas
    suffirait a imprimer « 2 grilles sur 2 » la ou une seule porte l'item.

    Un item qu'aucune grille cible ne porte disparait de la vue, et un
    sous-item non plus porte — « 0 grille sur 2 » ne dit rien. Les originaux
    sont recopies, pas modifies : les memes items servent plusieurs sous-blocs.
    """
    cible = set(cas_cible)
    vue = []
    for item in items:
        porteurs = set(item["cas"]) & cible
        if not porteurs:
            continue
        sous = [{"titre": s["titre"], "cas": set(s["cas"]) & cible}
                for s in item.get("sous", [])]
        vue.append({"titre": item["titre"], "cas": porteurs,
                    "sous": [s for s in sous if s["cas"]]})
    return vue
