"""Signale, par SSP, les items que le socle A n'a pas apparies mais qui se
ressemblent. Ce sont les candidats du vocabulaire canonique. Sortie 0.

DEUX NIVEAUX, ET NON LE SEUL ITEM DE TETE. Le rapprochement lexical rate aussi
bien un titre qu'un sous-item, et c'est meme la que le gisement est le plus
dense : « Toux » porte cinq entrees « allergies » distinctes, dont quatre sont
des sous-items. Un rapport limite aux titres de tete en aurait montre une.

CHAQUE PAIRE EST TRIEE SELON SA RECEVABILITE, avec la regle EXACTE que
`check_vocabulaire` appliquera : le rapport ne doit jamais proposer ce que le
controle refusera. Une premiere redaction comparait les chaines brutes et
annoncait recevables 37 paires qui fusionnaient en realite deux items qu'une
grille distingue, dont douze antonymes (« Facteurs calmants » et « Facteurs
aggravants »). Le test porte donc sur les SIGNATURES APRES LA TABLE.

Quatre seaux, dans cet ordre de lecture. Les paires A JUGER d'abord, scindees
en ecart de FORME puis ecart de CONTENU (cf. `nature_de_lecart`), triees par
similarite DECROISSANTE — mais A L'INTERIEUR DE CHAQUE SSP seulement, le
document restant alphabetique : la premiere paire du fichier n'est PAS la plus
plausible du corpus, et le dire evite de le laisser croire. Puis les ⚠️, qui
melangent deux motifs distincts : l'INERTE (les deux titres ne vivent pas au
meme endroit, la propriete 7 refuserait) et l'ANTONYME PRESUME. Puis les ⛔.

CE SEAU S'EST APPELE « RECEVABLE », ET LE MOT INVITAIT AU TRAITEMENT EN LOT.
Il ne voulait dire que « qui passerait `check_vocabulaire` » — jamais « qu'il
faut fusionner ». Combine au tri par similarite decroissante, il se lisait
comme une file d'attente a vider, alors que les neuf proprietes du controle
sont faites pour attraper ce qu'une GRILLE distingue, pas ce qu'un CLINICIEN
distingue : « Echographie abdominale » ⟷ « Echographie vaginale »,
« Examens complementaires initiaux » ⟷ « ... urgents », « Palpation des
organes » ⟷ « ... des reins » les passent toutes les neuf. Le seau s'appelle
maintenant « a juger », et il est SCINDE selon la nature de l'ecart, pour que
la partie ou il n'y a rien a perdre se distingue de celle ou il y a une
distinction clinique a effacer.

LA NEGATION ASYMETRIQUE EST UNE MARQUE, PAS UN SEAU. Une paire dont un seul
cote nie reste dans le seau ou elle tombe — elle merite souvent d'etre reunie —
mais sa ligne porte un ⚠️ qui dit la seule chose qui compte : retenir la forme
POSITIVE. La ronde 1 a retenu cinq fois la negative, faute que quoi que ce soit
dans la chaine la voie. Voir `NEGATIONS` et la propriete 10 de
`check_vocabulaire`.

Il a fallu deux redactions pour que « qui passerait le controle » soit meme
vrai. La premiere annoncait 2 014 paires dont deux sur trois tombaient en
realite sur la propriete 7 : le seau promettait un gisement qu'il ne mesurait
pas. `contextes()` tranche maintenant la question avant l'affichage.

LA PORTEE DES COMPTES, parce que deux perimetres coexistent dans ce projet et
que les confondre a deja coute cinq erreurs de mesure : CE SCRIPT parcourt les
57 SSP du corpus qui portent au moins deux grilles, et en tire 3 264 paires.
`mesure_couche_b.py`, lui, ne compte que les 32 SSP du LOT PRIORITAIRE, d'ou
ses 2 297 paires. Les deux chiffres sont justes ; ils ne repondent pas a la
meme question.

Le rapport ne PROPOSE que des candidats : la decision reste humaine, et un
rapprochement abusif — reunir deux items cliniquement distincts — efface de
l'information sans laisser de trace, la ou un rapprochement rate reste visible.
"""
import sys
from difflib import SequenceMatcher
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import build_memento
import lib_fusion
import lib_vocabulaire

REPO = Path(__file__).resolve().parents[2]
SORTIE = REPO / "docs" / "superpowers" / "rapport-doublons-memento.md"
SEUIL = 0.72


# COUPLES ANTONYMIQUES — le seul defaut connu que la propriete 8 ne peut pas
# voir. Elle exige un TEMOIN, une grille portant les deux libelles ; quand les
# grilles sont disjointes, rien ne voit rien. Et le tri par plausibilite AGGRAVE
# le cas : un antonyme forme par echange de prefixe est lexicalement quasi
# identique, donc il remonte en TETE du seau recevable. Mesure : « Signes
# d'hyperthyroidie » (German-74) / « Signes d'hypothyroidie » (German-7) est
# rang 1 sur 40 des recevables de Palpitations, a 0,93 de similarite, et
# fusionnerait hyper et hypo sans qu'aucune des neuf proprietes ne bronche.
#
# CE FILTRE NE FERME PAS LA CLASSE, IL EN SIGNALE UNE PARTIE. L'information qui
# manque n'est pas dans le code, elle est absente du corpus. Une liste de
# couples ne couvre que ce qu'elle nomme ; elle ne dira rien de deux libelles
# qui s'opposent par le sens sans s'opposer par la forme.
ANTONYMES = [
    ("hyper", "hypo"), ("hypo", "hyper"),
    ("aggravant", "soulageant"), ("aggravant", "calmant"), ("aggravant", "ameliorant"),
    ("aggravation", "amelioration"), ("flexion", "extension"),
    ("abduction", "adduction"), ("actif", "passif"), ("anterieur", "posterieur"),
    ("proximal", "distal"), ("interne", "externe"), ("superieur", "inferieur"),
    ("droit", "gauche"), ("gauche", "droit"), ("positif", "negatif"),
    ("presence", "absence"), ("avec", "sans"), ("augmentation", "diminution"),
    ("ouverture", "fermeture"), ("inspiration", "expiration"),
    ("systolique", "diastolique"), ("primaire", "secondaire"),
]

# Prefixes privatifs : « asymetrique » / « symetrique », « indolore » /
# « douloureux ». Testes sur les tokens de la cle, pas sur la chaine, pour ne
# pas confondre « anamnese » avec un « a- » privatif.
PRIVATIFS = ("a", "in", "im", "non", "dys", "anti")


# NEGATION ASYMETRIQUE — la regle vit dans `lib_vocabulaire`, avec l'inventaire
# des libelles, parce qu'elle a DEUX consommateurs : ce rapport, qui la SIGNALE,
# et la propriete 10 de `check_vocabulaire`, qui la REFUSE. Une copie locale
# divergerait au premier mot ajoute. Voir `lib_vocabulaire.NEGATIONS` pour le
# detail de l'angle mort qu'elle ferme, et pour la raison de ne SURTOUT PAS la
# boucher du cote de `lib_cle.MOTS_VIDES`.
negation = lib_vocabulaire.negation


def signal_negation(a, b):
    """Le fragment de ligne que le rapport imprime pour une negation, ou "".

    Rendu par une fonction plutot qu'ecrit sur place pour que `check_negation.py`
    puisse verifier CE QUE LE RAPPORT DIT, et pas seulement ce que le detecteur
    trouve : un detecteur juste dont le resultat n'est pas affiche ne garde rien.
    """
    mot = negation(a, b)
    if not mot:
        return ""
    return (f"  ⚠️ **négation asymétrique** (« {mot} ») : un seul des deux libellés "
            "nie. Réunir reste possible, mais **le libellé retenu doit être la forme "
            "POSITIVE** — dans une checklist, « Pas de turgescence jugulaire » se lit "
            "comme un résultat, pas comme un geste à faire.")


def _tokens(libelle):
    return set(lib_fusion.cle(libelle).split())


def antonymie(a, b):
    """Le couple oppose qui separe ces deux libelles, ou None.

    Compare les TOKENS canoniques : la comparaison porte sur des mots entiers,
    pas sur des sous-chaines, faute de quoi « hyperuricemie » et « hypotension »
    se repondraient alors qu'ils ne s'opposent pas.
    """
    ta, tb = _tokens(a), _tokens(b)
    propres_a, propres_b = ta - tb, tb - ta
    if not propres_a or not propres_b:
        return None
    for x in sorted(propres_a):
        for y in sorted(propres_b):
            for gauche, droite in ANTONYMES:
                if x.startswith(gauche) and y.startswith(droite) \
                        and x[len(gauche):] == y[len(droite):]:
                    return f"{gauche} / {droite}"
            for prefixe in PRIVATIFS:
                if x == prefixe + y or y == prefixe + x:
                    return f"préfixe privatif « {prefixe}- »"
    return None


# NATURE DE L'ECART, entre deux libelles que rien n'interdit de reunir.
#
# Le seau « candidats a juger » ne dit qu'une chose : `check_vocabulaire` ne
# les refuserait pas. Il ne dit RIEN de l'opportunite clinique — et ses neuf
# proprietes ne le peuvent pas, elles sont faites pour attraper ce qu'une
# GRILLE distingue, pas ce qu'un CLINICIEN distingue. Echantillon reel de
# Douleur Abdominale : « Echographie abdominale » ⟷ « Echographie vaginale »,
# « Palpation des organes » ⟷ « Palpation des reins », « Examens
# complementaires initiaux » ⟷ « ... urgents » passent les neuf.
#
# D'ou cette partition, qui porte sur les MOTS QUI DIFFERENT, une fois les
# mots vides et les pluriels simples deja neutralises par lib_cle.cle() :
#
#   ecart de FORME    — les deux libelles disent les memes mots, a l'accord,
#                       au genre ou a la graphie pres (« familial » /
#                       « familiaux », « bi-manuelle » / « bimanuelle »).
#                       Reunir n'efface rien.
#   ecart de CONTENU  — au moins un mot present d'un cote n'a pas de
#                       correspondant de l'autre, ou les deux mots qui se
#                       repondent sont des mots differents (« abdominale » /
#                       « vaginale »). Reunir efface une distinction.
#
# La partition ne tranche pas a la place du relecteur : elle met devant lui,
# en tete, les paires ou il n'y a rien a perdre.
_LONGUEUR_RACINE = 4   # prefixe commun minimal pour parler de meme mot
_LONGUEUR_FLEXION = 4  # ce qui reste apres la racine, au plus, de chaque cote


def _meme_mot(x, y):
    """Vrai si x et y sont deux formes d'un meme mot (accord, genre, graphie).

    « familial »/« familiaux » : racine « famil », restes « ial »/« iaux ».
    « veineuse »/« veineux » : racine « veineu ». En revanche
    « cholecystite »/« choledocholithiase » partagent « chole » mais laissent
    « cystite » et « docholithiase » : deux mots, pas deux accords.
    """
    n = 0
    while n < min(len(x), len(y)) and x[n] == y[n]:
        n += 1
    return (n >= _LONGUEUR_RACINE
            and len(x) - n <= _LONGUEUR_FLEXION
            and len(y) - n <= _LONGUEUR_FLEXION)


def _appariables(propres_a, propres_b):
    """Vrai si chaque mot propre d'un cote a son accord de l'autre, un pour un."""
    if len(propres_a) != len(propres_b):
        return False
    restants = list(propres_b)
    for x in propres_a:
        jumeau = next((y for y in restants if _meme_mot(x, y)), None)
        if jumeau is None:
            return False
        restants.remove(jumeau)
    return True


def nature_de_lecart(a, b):
    """« forme » ou « contenu ». Deterministe, sans dictionnaire ni corpus."""
    propres_a = sorted(_tokens(a) - _tokens(b))
    propres_b = sorted(_tokens(b) - _tokens(a))
    if not propres_a or not propres_b:
        # Un cote porte un mot que l'autre n'a pas du tout : « Palpation » et
        # « Palpation profonde » ne disent pas la meme chose.
        return "contenu"
    if "".join(propres_a) == "".join(propres_b):
        # Une seule difference : ou passe la coupure entre les mots.
        # « cardio pulmonaire » et « cardiopulmonaire ».
        return "forme"
    return "forme" if _appariables(propres_a, propres_b) else "contenu"


def similarite(a, b):
    return SequenceMatcher(None, a.lower(), b.lower()).ratio()


def paires(libelles):
    """Les couples de libelles dont la similarite depasse le seuil, ordre stable."""
    tries = sorted(libelles)
    return [(a, b) for n, a in enumerate(tries) for b in tries[n + 1:]
            if similarite(a, b) > SEUIL]


def seaux_indexes(seaux, ssp):
    """(grille, section) -> (libelles par forme canonique, libelles par signature canonique).

    Precalcul qui rend le test de collision constant par seau, au lieu de
    reparcourir tous les libelles pour chacune des milliers de paires. Les
    valeurs sont des ensembles de SIGNATURES de libelles bruts : c'est ce que
    compte le test, deux libelles de meme signature etant deja un seul item
    pour le socle A.
    """
    index = {}
    for cle_seau, seau in seaux.items():
        par_canonique, par_signature = {}, {}
        for libelle in sorted(seau):
            forme = lib_fusion.canonique(libelle, ssp)
            brut = lib_fusion.signature(libelle)
            par_canonique.setdefault(forme, set()).add(brut)
            par_signature.setdefault(lib_fusion.signature(forme), set()).add(brut)
        index[cle_seau] = (par_canonique, par_signature)
    return index


def irrecevable(a, b, index, ssp):
    """La grille et la section ou l'entree « a -> b » ferait un rapprochement abusif.

    MEME REGLE QUE `check_vocabulaire.collisions`, et c'est tout l'interet : le
    rapport ne doit jamais proposer ce que le controle refusera. La regle porte
    sur les SIGNATURES APRES LA TABLE, pas sur les chaines brutes — sans quoi 37
    des paires que ce rapport presentait comme recevables fusionnaient en
    realite deux items qu'une grille distingue, dont douze antonymes.

    Le test tient en deux ensembles parce que la table courante ne collisionne
    pas : le groupe qui BOUGE (les libelles dont la forme canonique est
    exactement `a`) rejoint le groupe CIBLE (ceux dont la signature canonique
    vaut celle de `b`). Si l'union porte deux signatures brutes distinctes, deux
    items que le socle A separait viennent d'etre confondus.
    """
    signature_b = lib_fusion.signature(b)
    for (cid, prefixe), (par_canonique, par_signature) in sorted(index.items()):
        bouge = par_canonique.get(a)
        if bouge and len(bouge | par_signature.get(signature_b, set())) > 1:
            return f"{cid}, section « {prefixe} »"
    return None


def contextes(cas_list, ssp):
    """titre affiche -> {endroits ou il vit}, au sens ou `_fusionner` les separe.

    Sert a dire si une entree REUNIRAIT quelque chose, sans passer par le test
    de partition de `check_vocabulaire` (trop lent a l'echelle de milliers de
    paires). Deux titres ne peuvent se rejoindre que s'ils vivent au meme
    endroit : meme section ET meme niveau, et pour deux sous-items, sous le meme
    groupe de tete. Sinon l'entree ne fait que renommer, et la propriete 7 la
    refuse.

    C'EST LA CORRECTION D'UNE SUR-PROMESSE : « recevable » laissait entendre
    « acceptee par le controle », alors que deux paires sur trois tombaient sur
    la propriete 7. Le seau recevable ne contient plus que ce qui passerait.
    """
    out = {}
    for prefixe in lib_vocabulaire.SECTIONS:
        for groupe in build_memento.lib_fusion.apparier(cas_list, prefixe, ssp):
            cle = lib_fusion.signature(groupe["titre"])
            out.setdefault(groupe["titre"], set()).add(f"T:{prefixe}")
            for sous in groupe["sous"]:
                out.setdefault(sous["titre"], set()).add(f"S:{prefixe}:{cle}")
    return out


def main():
    lignes = ["# Doublons candidats — vocabulaire canonique", "",
              "Paires d'items d'une même SSP que le socle A n'a pas appariés",
              f"mais dont la similarité dépasse {SEUIL}.", "",
              "Titres de tête **et** sous-items confondus : la couche B s'applique aux",
              "deux. Les grilles porteuses suivent chaque libellé.", "",
              "## Ce que « à juger » veut dire, et ce que ça ne veut pas dire", "",
              "Les paires **à juger** viennent d'abord. « À juger » signifie **une seule",
              "chose** : `check_vocabulaire` ne les refuserait pas. Ce n'est **pas** une",
              "recommandation de les fusionner, et surtout pas en lot. Les neuf propriétés",
              "du contrôle attrapent ce qu'une **grille** distingue ; elles ne voient pas",
              "ce qu'un **clinicien** distingue. `Échographie abdominale` ⟷ `Échographie",
              "vaginale` les passe toutes les neuf.", "",
              "D'où deux sous-seaux, et lire le second **une paire à la fois** :", "",
              "- **écart de forme** — les deux libellés disent les mêmes mots, à l'accord,",
              "  au genre ou à la graphie près (`familial` / `familiaux`, `bi-manuelle` /",
              "  `bimanuelle`). Réunir n'efface rien ;",
              "- **écart de contenu** — un mot de contenu diffère, ou n'existe que d'un",
              "  côté (`abdominale` / `vaginale`, `initiaux` / `urgents`, `des organes` /",
              "  `des reins`). Réunir **efface une distinction clinique** : chaque paire",
              "  est un jugement, pas une ligne d'une liste.", "",
              "À l'intérieur de chaque sous-seau, tri par similarité **décroissante**.",
              "⚠️ Ce tri est **local à la section** : le document, lui, est alphabétique",
              "par SSP, donc la première paire du fichier n'est **pas** la plus plausible",
              "du corpus. Les dix plus similaires (0,983 → 0,964) sont ailleurs —",
              "`Auscultation cardio-pulmonaire` ⟷ `cardiopulmonaire`, `Palpation",
              "bi-manuelle` ⟷ `bimanuelle`.", "",
              "Suivent deux catégories à ne lire **que si tout le reste est traité** :", "",
              "- **⚠️ inerte ou antonyme présumé**. *Inerte* : les deux titres ne vivent",
              "  pas au même endroit (section ou parent différents), donc l'entrée ne",
              "  réunirait rien et la propriété 7 la refuserait. *Antonyme présumé* : les",
              "  libellés s'opposent par un motif connu (`hyper`/`hypo`, `flexion`/",
              "  `extension`…) et **aucune grille ne les porte ensemble**, donc la",
              "  propriété 8 n'a pas de témoin — c'est la seule classe que rien",
              "  n'automatise, voir la section finale ;",
              "- **⛔ irrecevable par construction** : soit l'entrée confondrait deux",
              "  libellés qu'une grille distingue **dans une même section** (propriété 8",
              "  — le test porte sur les signatures **après** la table, donc il attrape",
              "  aussi les variantes et les fusions indirectes), soit les deux libellés",
              "  ont **déjà la même signature** pour le socle A (propriété 6).", "",
              "## Négation asymétrique — un signal, pas un seau", "",
              "Une paire dont **un seul côté nie** (`pas`, `sans`, `non`, `absence`,",
              "`aucun`, `ni`, `jamais`, `négatif`) porte désormais une marque ⚠️ **sur sa",
              "propre ligne**, dans le seau où elle tombe. Elle n'est pas écartée : la",
              "réunion se défend souvent, c'est l'**intitulé retenu** qui ne se défend pas.",
              "La règle est donc : réunir si l'on veut, mais **retenir la forme",
              "POSITIVE**. La classe complète est listée en fin de document.", ""]
    total = refusees = forme_total = contenu_total = 0
    antonymiques = []
    negations = []
    groupes = build_memento.par_ssp()
    inventaire = lib_vocabulaire.libelles_par_ssp(groupes)
    positions = lib_vocabulaire.positions_par_ssp(groupes)
    for ssp, cas in sorted(groupes.items()):
        if len(cas) < 2:
            continue
        # Les libelles APPARIES, un par groupe : deux libelles que le socle A a
        # deja reunis ne sont plus qu'un seul titre ici, et ne peuvent donc pas
        # ressortir en candidats.
        titres = sorted({i["titre"] for p in ("a", "e", "m")
                         for g in build_memento.lib_fusion.apparier(cas, p, ssp)
                         for i in [g] + g["sous"]})
        candidates = paires(titres)
        if not candidates:
            continue
        index = seaux_indexes(positions[ssp], ssp)
        ou_vit = contextes(cas, ssp)
        de_forme, de_contenu, douteuses, bloquees = [], [], [], []
        for a, b in candidates:
            ligne = (f"`{a}` {porteuses(a, inventaire[ssp])}"
                     f"  ⟷  `{b}` {porteuses(b, inventaire[ssp])}")
            # Les deux sens sont testes : le libelle retenu peut etre l'un ou
            # l'autre, et rien ne dit lequel un successeur choisira.
            ou = irrecevable(a, b, index, ssp) or irrecevable(b, a, index, ssp)
            oppose = antonymie(a, b)
            nie = negation(a, b)
            if nie:
                # LA CLASSE ENTIERE EST RELEVEE, quel que soit le seau ou la
                # paire tombe. Une negation dans un seau ⚠️ ou ⛔ ne demande
                # aucune decision aujourd'hui, mais elle en demandera une le
                # jour ou la table bougera autour d'elle — et c'est precisement
                # ce qui est arrive en ronde 1 : les paires devenues voisines
                # apres coup sont celles qu'aucune relecture n'avait vues.
                negations.append((ssp, a, b, nie))
            if ou:
                bloquees.append(f"- ⛔ {ligne} — **{ou}** distingue ces deux items")
            elif lib_fusion.signature(a) == lib_fusion.signature(b):
                # Meme signature socle A : ces deux titres ne coexistent que
                # parce qu'ils sont dans des SECTIONS differentes, que
                # l'appariement traite separement. Une entree serait refusee par
                # la propriete 6 de check_vocabulaire.
                bloquees.append(f"- ⛔ {ligne} — **même signature socle A**, "
                                "déjà appariés dans leur section")
            elif oppose:
                # AVANT le test d'inertie, et non apres. Cinq des six antonymes
                # du corpus sont AUSSI inertes, donc rattrapes PAR ACCIDENT par
                # la propriete 7 : les classer « inerte » les ferait disparaitre
                # de la liste que le relecteur doit voir, et ferait croire que la
                # classe est mince. Elle n'est pas mince, elle est mal gardee.
                agit = bool(ou_vit.get(a, set()) & ou_vit.get(b, set()))
                antonymiques.append((ssp, a, b, oppose, agit))
                douteuses.append(
                    f"- ⚠️ {ligne} — **antonymes présumés** ({oppose}) : aucune grille "
                    "ne les porte ensemble, donc la propriété 8 n'a pas de témoin. "
                    + ("**L'entrée mordrait — à vérifier à la main.**" if agit else
                       "*(Par ailleurs inerte : la propriété 7 la refuserait.)*"))
            elif not (ou_vit.get(a, set()) & ou_vit.get(b, set())):
                douteuses.append(f"- ⚠️ {ligne} — **inerte** : ces deux titres ne "
                                 "vivent pas au même endroit (section ou parent "
                                 "différents), l'entrée ne réunirait rien")
            else:
                # TRI PAR PLAUSIBILITE DECROISSANTE. L'ordre alphabetique mettait
                # un faux positif en tete aussi souvent qu'un vrai ; la
                # similarite, deja calculee pour le seuil, ordonne gratuitement.
                # Mais la similarite ne dit rien de ce qu'on perdrait : d'ou la
                # partition forme/contenu, qui, elle, le dit.
                seau = (de_forme if nature_de_lecart(a, b) == "forme" else de_contenu)
                seau.append((-similarite(a, b), a, b, f"- {ligne}{signal_negation(a, b)}"))
        total += len(candidates)
        refusees += len(bloquees) + len(douteuses)
        a_juger = len(de_forme) + len(de_contenu)
        forme_total += len(de_forme)
        contenu_total += len(de_contenu)
        lignes.append(f"## {ssp} — {len(cas)} cas · {a_juger} à juger "
                      f"({len(de_forme)} de forme, {len(de_contenu)} de contenu), "
                      f"{len(douteuses)} ⚠️, {len(bloquees)} ⛔")
        if de_forme:
            lignes += ["", "**À juger — écart de forme** (accord, genre, graphie : "
                       "réunir n'efface rien)", ""]
            lignes += [x[3] for x in sorted(de_forme)]
        if de_contenu:
            lignes += ["", "**À juger — écart de contenu** (un mot de contenu diffère : "
                       "réunir efface une distinction, à examiner de près)", ""]
            lignes += [x[3] for x in sorted(de_contenu)]
        if douteuses or bloquees:
            lignes.append("")
        lignes += douteuses + bloquees + [""]

    if antonymiques:
        lignes += ["## ⚠️ Antonymes présumés — la classe que rien n'automatise", "",
                   "Aucune grille ne porte ces libellés **ensemble**, donc la propriété 8",
                   "n'a pas de témoin et ne peut rien dire. Le filtre lexical les signale ;",
                   "il ne les juge pas, et il ne prétend pas les avoir tous.", ""]
        lignes += [f"- **{ssp}** — `{a}` ⟷ `{b}` *({motif})* — "
                   + ("**l'entrée mordrait**" if agit else "par ailleurs inerte")
                   for ssp, a, b, motif, agit in antonymiques] + [""]

    if negations:
        lignes += ["## ⚠️ Négations asymétriques — la classe complète", "",
                   "Un seul des deux libellés nie. La réunion n'est pas interdite ; ce qui",
                   "l'est, c'est de retenir la forme **négative** comme intitulé du mémento.",
                   "La ronde 1 l'a fait cinq fois, et les cinq ont dû être inversées après",
                   "coup. `check_vocabulaire` refuse maintenant ce sens-là (propriété 10),",
                   "mais il ne peut pas deviner qu'une paire mérite d'être réunie : c'est",
                   "cette liste-ci qui le dit.", ""]
        lignes += [f"- **{ssp}** — `{a}` ⟷ `{b}` *(« {mot} »)*"
                   for ssp, a, b, mot in negations] + [""]

    SORTIE.write_text("\n".join(lignes) + "\n", encoding="utf8")
    print(f"{total} paires candidates dont {total - refusees} à juger "
          f"({forme_total} de forme, {contenu_total} de contenu), "
          f"{refusees} écartées ({len(antonymiques)} antonymes présumés, "
          f"{len(negations)} négations asymétriques tous seaux confondus) "
          f"-> {SORTIE.relative_to(REPO)}")
    return 0


def porteuses(libelle, table):
    """« (German-53) » — les grilles qui portent ce libelle, ou rien si inconnu.

    Un libelle affiche peut venir de la couche B et n'etre porte, tel quel, par
    aucune grille : le cas est signale plutot que tu, pour que le lecteur ne
    prenne pas un silence pour une absence de porteur.
    """
    cids = table.get(libelle)
    return f"({', '.join(sorted(cids))})" if cids else "(forme canonique)"


if __name__ == "__main__":
    sys.exit(main())
