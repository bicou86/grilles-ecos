"""Appariement des items entre grilles d'une meme SSP.

SOCLE A — normalisation lexicale, sans curation : la numerotation de tete est
retiree, puis `lib_cle.cle()` fait le reste (minuscules, accents, ponctuation,
mots vides francais, pluriel simple, ordre des mots neutralise). Deux libelles
de meme signature sont le meme item. La regle N'EST PAS redefinie ici : elle
est importee de lib_cle, source unique partagee avec rapport_referentiel.py
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


def desambigue(cas, prefixe, ssp=None):
    """Les items d'une section d'UNE grille, homonymes qualifies par leur groupe.

    LE GROUPE EST UNE INFORMATION DE LA GRILLE, PAS UNE DECORATION. AZYGOS-24
    (Dysphonie) cote « Inspection » TROIS fois — sous « Respiration », sous
    « Bouche », sous « Cou » — et « Palpation » deux fois. Le socle A ne voit
    que le libelle : les trois inspections partageaient une signature et
    fusionnaient entre elles, si bien que l'inspection du cou et la palpation
    cervicale disparaissaient du memento en tant que gestes cotes distincts.
    Meme perte sur AZYGOS-44 (« Inspection » de l'abdomen contre celle du col
    au speculum ; « Affections tumorales » personnelles contre familiales),
    AZYGOS-36 (« Inspection » du nez contre celle de la bouche), AZYGOS-21
    (« Antecedents » deux fois) et AZYGOS-27 (« Arguments POUR » / « CONTRE »,
    repetes pour chacun de ses trois diagnostics differentiels).

    Releve du corpus : 85 occurrences surnumeraires, 80 dans AZYGOS et 5 dans
    RESCOS, reparties sur 42 couples (grille, section).

    LA QUALIFICATION PORTE SUR LA FORME CANONIQUE, pas sur le libelle brut :
    la couche B doit avoir dit son mot AVANT qu'on suffixe, sinon un homonyme
    perdrait la reecriture que la table lui destine.

    SEULS LES HOMONYMES QUI CHANGENT DE GROUPE SONT QUALIFIES. Un libelle
    repete DANS UN MEME groupe n'est pas ambigu, c'est un doublon : AZYGOS-36
    cote « Douleur faciale » deux fois sous « Anamnese orientee sur le
    probleme », et le suffixer n'aurait rien distingue — seulement enlaidi le
    libelle et casse son appariement avec les autres grilles. Le critere est
    donc le nombre de GROUPES distincts, jamais le nombre d'occurrences.

    LE PREMIER GROUPE GARDE LE LIBELLE NU, et c'est ce qui rend la correction
    STRICTEMENT ADDITIVE : aucun libelle qui existait ne disparait, seules
    s'ajoutent les occurrences qui se perdaient. Qualifier AUSSI la premiere
    a ete essaye et coute plus qu'il ne rapporte — « Antecedents medicaux »
    d'AZYGOS-27, qualifie, cessait de rejoindre « Antecedents medicaux
    personnels » de German-42, et deux entrees du vocabulaire devenaient
    inertes du meme coup (check_vocabulaire l'a dit). Le groupe suivant est
    ce que le corpus perdait ; le premier, lui, s'appariait deja.

    Un item sans groupe ne peut pas etre qualifie : il reste nu, et le
    comportement d'avant vaut pour lui.
    """
    lignes = cas["sections"].get(prefixe, [])
    groupe_de, groupe = [], None
    for genre, _, titre, _ in lignes:
        if genre == "titre":
            groupe = titre
        else:
            groupe_de.append(groupe)

    items = [(t, s or []) for g, _, t, s in lignes if g == "item"]
    # Premier groupe rencontre pour chaque signature, dans l'ordre du document
    # — pas de dependance a l'ordre d'un `set`, donc pas de dependance a
    # PYTHONHASHSEED.
    premier = {}
    for (titre, _), groupe in zip(items, groupe_de):
        premier.setdefault(signature(canonique(titre, ssp)), groupe)

    out = []
    for (titre, sous), groupe in zip(items, groupe_de):
        nom = canonique(titre, ssp)
        if groupe and premier[signature(nom)] != groupe:
            nom = f"{nom} ({groupe})"
        out.append((nom, sous))
    return out


def apparier(cas_list, prefixe, ssp=None):
    """Items d'une section, apparies entre tous les cas fournis."""
    entrees = []
    for cas in cas_list:
        for titre, sous in desambigue(cas, prefixe, ssp):
            entrees.append((titre, sous, cas["id"]))
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
    sous-blocs de « Douleur Abdominale ». Le seuil a deux retire ces lignes
    creuses.

    LE SEUIL PORTE SUR LE CONTENU, PAS SUR LE SEUL TITRE (ronde 2). Applique
    au seul item de tete, il deportait des sous-items qui, eux, n'etaient
    partages par personne : 90 % des lignes de sous-item de l'encadre partage
    ne portaient qu'un diagnostic, et seize diagnostics avaient plus de lignes
    LA-HAUT que dans leur propre sous-bloc — le reflux gastro-oesophagien
    voyait ses dix-neuf lignes propres (IPP, fundoplicature, Barrett) rangees
    sous « Prise en charge therapeutique » dans le partage, pendant que son
    sous-bloc annoncait « aucun item propre a ce diagnostic ». Un item ne
    monte donc que si son CONTENU l'est aussi : aucun sous-item, ou aucun
    sous-item propre a un seul diagnostic. Sinon il reste duplique dans les
    sous-blocs, comme avant le seuil.

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
    partage quoi qu'il arrive : le renvoyer vers un sous-bloc est impossible
    (il n'y en a aucun a nommer) et l'ecarter le supprimerait du memento.
    """
    apparies = apparier(cas_list, "m", ssp)
    diagnostics = {diag_par_cas[c["id"]] for c in cas_list if c["id"] in diag_par_cas}

    partage, propres = [], {d: [] for d in diagnostics | set(attendus)}
    for item in apparies:
        porteurs = _porteurs(item, diag_par_cas)
        if not porteurs or (len(porteurs) > 1 and contenu_partage(item, diag_par_cas)):
            partage.append(item)
        else:
            for d in porteurs:
                propres[d].append(item)
    return partage, propres


def _porteurs(item, diag_par_cas):
    """Les diagnostics qu'un item apparie porte, via ses grilles."""
    return {diag_par_cas[c] for c in item["cas"] if c in diag_par_cas}


def contenu_partage(item, diag_par_cas):
    """Aucun sous-item de cet item n'est propre a un seul diagnostic.

    LA CONDITION QUI MANQUAIT au seuil de la ronde 1. Un item de tete porte
    par deux diagnostics peut n'avoir que des sous-items mono-diagnostic :
    « Examens complementaires - Fonction respiratoire » est cote par la grille
    d'asthme ET par celle de BPCO, mais ses huit sous-items se repartissent
    quatre pour l'asthme, quatre pour la BPCO. Monter l'item entier deportait
    le contenu du sous-bloc vers un encadre qui ne le concerne pas — jusqu'a
    dix-neuf lignes strictement RGO annoncees comme partagees, pendant que le
    sous-bloc RGO disait « aucun item propre a ce diagnostic ».

    Un sous-item qu'aucun diagnostic ne porte (aucune grille porteuse n'a de
    diagnostic resolu) n'empeche pas la montee : il n'appartient a aucun
    sous-bloc, donc le laisser en haut ne prive personne. Meme raisonnement
    que pour l'item de tete, d'ou le meme test `!= 1`.
    """
    return all(len(_porteurs(sous, diag_par_cas)) != 1 for sous in item.get("sous", []))


def restreindre(items, cas_cible):
    """Vue d'items limitee aux grilles de `cas_cible`, sans toucher aux originaux.

    Un item apparie porte les grilles de TOUTE la SSP. Dans un sous-bloc de
    diagnostic, le lire tel quel ferait dire a `lib_rendu.marque()` « 3 grilles
    sur 2 » : un numerateur compte sur la SSP, un denominateur compte sur le
    seul diagnostic. La vue restreinte rend les deux comparables.

    LE SEUIL RESTREINT AU CONTENU l'a rendue de nouveau active : un item dont
    les sous-items ne sont pas tous partages RESTE duplique dans les sous-blocs
    de chacun de ses diagnostics, et c'est la que la restriction mord — 63 fois
    sur le corpus complet. (Une redaction anterieure de cette docstring, ecrite
    sous le seuil « des deux diagnostics », affirmait le contraire : « aucun cas
    aujourd'hui ». Elle sous-estimait la fonction d'un facteur soixante.)

    Elle mord aussi, plus rarement, sur un item porte a la fois par une grille
    du diagnostic et par une grille SANS diagnostic resolu — le corpus n'en
    compte aucun, mais check_diagnostic plafonne a 90 % de resolution, donc le
    contrat du projet l'autorise.

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
