"""Garde-fou de la couche B : toute entree du vocabulaire doit mordre. Sortie 1 si ecart.

LE DEFAUT QUE CE CONTROLE FERME. `docs/ecos-vocabulaire.yaml` est consulte par
`lib_fusion.canonique()` avec un `dict.get()` EXACT sur le libelle nu. Une
entree mal orthographiee — un accent de travers, une espace finale, une
majuscule de moins, un nom de SSP approximatif — ne leve rien, ne compte pour
rien, et laisse croire que la curation a eu lieu. Verifie avant d'ecrire ce
controle : trois variantes erronees d'un meme libelle, zero effet, zero
message. Une table de curation silencieusement morte est pire que pas de table
du tout, parce qu'on cesse de regarder le rendu.

NEUF PROPRIETES, de la plus grossiere a la plus fine :

  1. STRUCTURE     le fichier se lit avec le lecteur du projet.
  2. SSP REELLE    chaque groupe nomme une SSP que le corpus rattache.
  3. CLE REELLE    chaque cle correspond a un libelle brut REELLEMENT porte
                   par une grille de cette SSP. C'est la propriete centrale.
  4. CIBLE REELLE  chaque valeur aussi. Une forme canonique inventee de toutes
                   pieces sortirait le memento du corpus : le lecteur ne
                   retrouverait plus l'item dans la grille d'origine.
  5. SANS CHAINE   une cle n'est jamais la valeur d'une autre entree de la
                   meme SSP. `canonique()` fait UNE substitution, pas un point
                   fixe : « A -> B » et « B -> C » donneraient A=B et B=C,
                   deux groupes la ou l'auteur en voulait un.
  6. EFFET REEL    l'entree change bien quelque chose : passee par
                   `canonique()`, la cle rend la valeur ; et cle et valeur
                   n'avaient pas deja la meme signature (auquel cas le socle A
                   les appariait seul et l'entree est un leurre).
  7. GAIN MESURE   chaque entree, RETIREE SEULE de la table, fait remonter le
                   nombre de groupes apparies de sa SSP. C'est la seule
                   propriete de bout en bout : elle passe par le vrai chemin
                   d'appel du generateur, donc elle survivrait a un
                   deplacement de la table ou a un changement de sa forme. Elle
                   attrape ce qu'aucune relecture ne voit — deux libelles
                   ranges sous des PARENTS differents ne se rejoindront jamais,
                   quoi qu'en dise la table.

  8. SANS COLLISION dans un seau (grille, section), deux libelles que le socle A
                   DISTINGUAIT ne se retrouvent pas CONFONDUS une fois la table
                   appliquee. C'est LE COMPTEUR DE SURETE, il doit rester a
                   zero. La regle porte sur `signature(canonique(x))` et NON sur
                   les chaines brutes : une redaction anterieure demandait a la
                   grille d'ecrire la cible au caractere pres, et laissait donc
                   passer 37 fusions abusives — dont douze antonymes — des que
                   la grille en ecrivait une variante. Voir `collisions()`.
  9. COUVERTURE    tout ce qu'une grille verse dans un meme groupe d'`apparier()`
                   tombe dans un seul seau de la propriete 8 — 23 005 temoins
                   sur le corpus. C'est le garde-fou de la propriete 8 elle-meme :
                   elle RECONSTRUIT la comparaison du moteur au lieu de
                   l'appeler, et c'est exactement dans cet ecart que le defaut
                   precedent vivait. Voir `couverture()`.

CE QUE CE CONTROLE NE PEUT TOUJOURS PAS VERIFIER, et qui reste a la relecture
humaine. La propriete 8 exige un TEMOIN : une grille qui porte les deux
libelles. Quand les grilles sont disjointes, rien ne voit rien — et
« Signes d'hyperthyroidie » (German-74) rabattu sur « Signes d'hypothyroidie »
(German-7) passe les neuf proprietes au vert. L'information qui manque n'est pas
dans le code, elle est ABSENTE DU CORPUS : deux grilles qui distinguent sans
jamais se croiser sont hors d'atteinte de tout controle automatique.
`report_doublons.py` en signale une partie par un filtre antonymique ; il
signale, il ne ferme pas.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import build_memento                                      # noqa: E402
import lib_fusion                                         # noqa: E402
import lib_vocabulaire                                    # noqa: E402
import lib_yaml                                           # noqa: E402

REPO = Path(__file__).resolve().parents[2]
TABLE = REPO / "docs" / "ecos-vocabulaire.yaml"


def proches(libelle, connus, maximum=3):
    """Les libelles connus de meme signature — l'indice qui nomme la faute de frappe.

    Deux libelles qui ne different que par un accent, la casse ou un pluriel
    partagent leur signature : c'est exactement la faute que ce controle
    attrape, et c'est donc la bonne facon de proposer la correction.
    """
    cible = lib_fusion.signature(libelle)
    return sorted(c for c in connus if lib_fusion.signature(c) == cible)[:maximum]


def _detail(libelle, connus):
    suggestions = proches(libelle, connus)
    if suggestions:
        return " — vouliez-vous dire " + " ou ".join(f"« {s} »" for s in suggestions) + " ?"
    return ""


def installee(vocabulaire):
    """Rend `lib_fusion` consultant LA table examinee, le temps des controles de bout en bout.

    Les proprietes 6 et 7 passent par `lib_fusion.canonique()` et
    `lib_fusion.apparier()`, qui lisent la table depuis le disque via un cache
    de module. En production c'est la meme table que celle recue ici, donc
    l'installation ne change rien ; en test de mutation, c'est ce qui permet de
    soumettre une table fautive AU VRAI CHEMIN D'APPEL plutot qu'a une copie
    du raisonnement. Sans cela, les deux controles les plus profonds seraient
    les seuls qu'aucune mutation ne pourrait exercer.
    """
    class _Bascule:
        def __enter__(self):
            self.avant = lib_fusion._VOCABULAIRE
            lib_fusion._VOCABULAIRE = vocabulaire

        def __exit__(self, *_):
            lib_fusion._VOCABULAIRE = self.avant
    return _Bascule()


def verifier(vocabulaire, inventaire, groupes):
    """La liste des ecarts, en clair. Vide = table saine."""
    with installee(vocabulaire):
        return _verifier(vocabulaire, inventaire, groupes)


def _verifier(vocabulaire, inventaire, groupes):
    ecarts = []
    for ssp in sorted(vocabulaire):
        entrees = vocabulaire[ssp]
        if ssp not in inventaire:
            candidates = sorted(s for s in inventaire if s.lower() == ssp.lower())
            indice = f" — SSP proche : « {candidates[0]} » ?" if candidates else ""
            ecarts.append(f"« {ssp} » n'est pas une SSP du corpus{indice}")
            continue
        connus = inventaire[ssp]
        cibles = set(entrees.values())
        for cle in sorted(entrees):
            valeur = entrees[cle]
            ou = f"{ssp} / « {cle} »"
            if cle not in connus:
                ecarts.append(f"{ou} — aucune grille de cette SSP ne porte ce libellé"
                              + _detail(cle, connus))
                continue
            if not valeur:
                ecarts.append(f"{ou} — forme canonique vide")
                continue
            if valeur not in connus:
                ecarts.append(f"{ou} → « {valeur} » — la forme canonique n'est portée par "
                              "aucune grille de cette SSP" + _detail(valeur, connus))
                continue
            if cle == valeur:
                ecarts.append(f"{ou} — l'entrée se renvoie à elle-même, elle ne fait rien")
                continue
            if cle in cibles:
                amont = sorted(k for k, v in entrees.items() if v == cle)
                ecarts.append(f"{ou} — cette clé est aussi la cible de "
                              + ", ".join(f"« {a} »" for a in amont)
                              + " : canonique() ne chaîne pas, visez directement "
                              f"« {valeur} »")
                continue
            if lib_fusion.signature(cle) == lib_fusion.signature(valeur):
                ecarts.append(f"{ou} → « {valeur} » — le socle A appariait déjà ces deux "
                              "libellés : l'entrée n'apparie rien de plus")
                continue
            rendu = lib_fusion.canonique(cle, ssp)
            if rendu != valeur:
                ecarts.append(f"{ou} — canonique() rend « {rendu} » au lieu de "
                              f"« {valeur} » : la table n'est pas consultée comme prévu")

    positions = lib_vocabulaire.positions_par_ssp(groupes)
    ecarts += collisions(vocabulaire, positions)
    ecarts += couverture(vocabulaire, groupes, positions)
    ecarts += _sans_effet(vocabulaire, groupes)
    return ecarts


def fentes(cas_list, prefixe, ssp):
    """[(grille, {libelles bruts})] — ce que chaque grille verse dans chaque groupe.

    Rejoue la semantique de `lib_fusion._fusionner` en gardant trace du libelle
    BRUT de chaque contribution : un item de tete est classe par
    `signature(canonique(titre))`, un sous-item par la meme cle mais A
    L'INTERIEUR du groupe de son parent. Une « fente » est un endroit ou le
    moteur peut confondre : tout ce qu'une meme grille verse au meme endroit.

    ON REND TOUTES LES CONTRIBUTIONS, PAS SEULEMENT CELLES QUI CONFONDENT, et
    c'est ce qui fait la difference entre un controle et un controle vide. Une
    premiere redaction ne signalait que les fentes ou deux signatures differentes
    se rencontraient : sur une table saine il n'y en a AUCUNE, si bien que le
    controle passait au vert sans jamais rien examiner — et une mutation qui
    amputait les seaux de leurs sous-items passait elle aussi. Rendre toutes les
    contributions donne des dizaines de milliers de temoins, vrais aujourd'hui,
    dont la moindre disparition signalerait que la propriete 8 a cesse de
    regarder ou le moteur travaille.
    """
    groupes = {}
    for cas in cas_list:
        for genre, _, titre, sous in cas["sections"].get(prefixe, []):
            if genre != "item":
                continue
            cle_t = lib_fusion.signature(lib_fusion.canonique(titre, ssp))
            g = groupes.setdefault(cle_t, {"tete": {}, "sous": {}})
            g["tete"].setdefault(cas["id"], set()).add(lib_vocabulaire.libelle_nu(titre))
            for brut in (sous or []):
                cle_s = lib_fusion.signature(lib_fusion.canonique(brut, ssp))
                g["sous"].setdefault(cle_s, {}).setdefault(cas["id"], set()).add(
                    lib_vocabulaire.libelle_nu(brut))

    out = []
    for g in groupes.values():
        for par_grille in [g["tete"]] + list(g["sous"].values()):
            out.extend(par_grille.items())
    return out


def couverture(vocabulaire, groupes, positions):
    """La propriete 8 couvre-t-elle tout ce que le moteur peut confondre ?

    LE GARDE-FOU DU GARDE-FOU. `collisions()` RECONSTRUIT la comparaison de
    `lib_fusion._fusionner` au lieu de l'appeler, et c'est precisement dans cet
    ecart que le defaut de la ronde 3 vivait : la regle comparait des chaines
    brutes quand le moteur comparait des signatures. Rien n'empeche un
    changement futur de `_fusionner` — un appariement qui traverserait les
    sections, une cle de groupe modifiee — de rouvrir le meme genre d'ecart en
    silence.

    Ce controle ferme la porte par l'autre bout : il demande au MOTEUR ou il
    confond, et verifie que chaque endroit tombe dans un seau que la propriete 8
    inspecte. La propriete 8 est aujourd'hui un SUR-ENSEMBLE STRICT de ce que
    `apparier()` peut confondre (elle refuse aussi des paires que le moteur ne
    reunirait pas, faute de partager un parent) : ce controle garde l'inclusion,
    pas l'egalite.

    POURQUOI NE PAS BRANCHER `collisions()` SUR `apparier()` PLUTOT. Parce que
    ce serait un ASSOUPLISSEMENT, pas un durcissement : la regle actuelle refuse
    des centaines de milliers de paires de plus, et se tromper dans ce sens est
    sans danger pour un appariement clinique. Le test d'inclusion donne la
    protection anti-derive sans rien lacher, et coute un dixieme de seconde.
    """
    ecarts = []
    with installee(vocabulaire):
        for ssp in sorted(groupes):
            for prefixe in lib_vocabulaire.SECTIONS:
                for cid, bruts in fentes(groupes[ssp], prefixe, ssp):
                    seau = positions.get(ssp, {}).get((cid, prefixe), {})
                    absents = sorted(b for b in bruts if b not in seau)
                    if absents:
                        ecarts.append(
                            f"{ssp} / {cid} / section « {prefixe} » — l'appariement réunit "
                            + ", ".join(f"« {b} »" for b in sorted(bruts))
                            + ", mais la propriété 8 ne regarde pas "
                            + ", ".join(f"« {b} »" for b in absents)
                            + " dans ce seau : la règle a divergé du moteur")
    return ecarts


def collisions(vocabulaire, positions):
    """LE COMPTEUR DE SURETE : il doit rester a zero.

    Une entree est un rapprochement abusif des qu'UNE grille porte ses DEUX
    libelles dans UNE MEME SECTION : l'auteur de cette grille les a distingues
    expres, et les reunir efface sa distinction sans laisser de trace. C'est le
    seul defaut de cette table qu'aucun autre controle ne voit — l'entree
    « mord » (la partition change), elle vise des libelles reels, elle ne
    chaine pas : tout est vert, et deux questions cliniques distinctes ont
    fusionne.

    LA REGLE ETAIT APPLIQUEE A LA MAIN, VINGT-TROIS FOIS, ET C'EST PRECISEMENT
    LE PROBLEME. Deux mutations le montrent, toutes deux vertes avant ce
    controle :

      - « Drogues » -> « Noxes » sur Cephalee : AZYGOS-3 porte les deux en
        items de TETE, section anamnese. « Noxes » est le bloc tabac + alcool +
        drogues, « Drogues » en est une ligne ;
      - « Alcool » -> « Drogues » sur Douleur Abdominale : trois grilles les
        distinguent — AZYGOS-14 en tete, RESCOS-17 sous « Habitudes »,
        RESCOS-19 sous « Antecedents personnels ».

    LA REGLE PORTE SUR LES SIGNATURES APRES LA TABLE, PAS SUR LES CHAINES
    BRUTES, et la premiere redaction se trompait exactement la. Comparer
    `cle in seau and valeur in seau` demandait a la grille d'ecrire la cible AU
    CARACTERE PRES : des qu'elle en ecrit une VARIANTE — casse, accent, pluriel,
    ou un libelle que la table aliase deja vers la meme cible — le controle ne
    voyait rien alors que la fusion avait bien lieu. Mesure de la breche : 37
    entrees d'une seule ligne passaient les huit proprietes au vert tout en
    fusionnant deux items qu'une grille distingue, dont DOUZE ANTONYMES
    (« Facteurs calmants » -> « Facteurs aggravants »,
    « Flexion de hanche » -> « Extension de la hanche »,
    « Uroculture » -> « Hemocultures »). Cas d'ecole :

        Douleur Thoracique / « Antecedents cardiaques » -> « Antecedents familiaux »
        German-32 ecrit « Antecedents cardiaques » ET « Anamnese familiale »,
        section a — et la table aliase deja « Anamnese familiale » vers
        « Antecedents familiaux ». Les deux items fusionnent, l'antecedent
        CARDIAQUE est avale par le FAMILIAL, zero ecart signale.

    Elle attrape aussi la FUSION INDIRECTE, qu'aucune entree ne trahit seule :
    « Drogues » -> « Toxiques » ET « Noxes » -> « Toxiques » sur Cephalee ne
    collisionnent ni l'une ni l'autre au sens des chaines brutes, et reunissent
    pourtant « Drogues » et « Noxes » d'AZYGOS-3 par un tiers libelle.

    D'ou la formulation retenue, qui ne parle plus d'entrees mais d'EFFET : dans
    un seau, deux libelles que le socle A distinguait
    (`signature(x) != signature(y)`) ne doivent pas se retrouver confondus une
    fois la table appliquee (`signature(canonique(x)) == signature(canonique(y))`).
    """
    ecarts = []
    with installee(vocabulaire):
        for ssp in sorted(positions):
            if ssp not in vocabulaire:
                continue      # sans entree, canonique() est l'identite
            for (cid, prefixe), seau in sorted(positions[ssp].items()):
                paquets = {}
                for libelle in sorted(seau):
                    apres = lib_fusion.signature(lib_fusion.canonique(libelle, ssp))
                    paquets.setdefault(apres, {})[lib_fusion.signature(libelle)] = libelle
                for apres, avant in sorted(paquets.items()):
                    if len(avant) < 2:
                        continue
                    confondus = [avant[s] for s in sorted(avant)]
                    ecarts.append(
                        f"{ssp} — RAPPROCHEMENT ABUSIF : {cid} distingue "
                        + " / ".join(f"« {x} » ({' et '.join(sorted(seau[x]))})"
                                     for x in confondus)
                        + f" dans la section « {prefixe} », et la table les confond. "
                        + "Entrée(s) en cause : "
                        + ", ".join(f"« {x} » → « {vocabulaire[ssp][x]} »"
                                    for x in confondus if x in vocabulaire[ssp]))
    return ecarts


def partition(cas_list, ssp):
    """QUI est regroupe avec qui, sans les libelles — l'effet reel d'une entree.

    Deux raisons de comparer des ensembles de grilles plutot que de COMPTER
    les groupes, l'une et l'autre trouvees sur un cas concret :

      - un COMPTE rate un regroupement a somme nulle. « Evoque un toucher
        rectal » (RESCOS-17, RESCOS-18) et « Évoque le toucher rectal »
        (RESCOS-19) partagent deja leur signature ; rabattre le premier sur
        « Toucher rectal » deplace deux grilles vers le bon item sans changer
        le nombre de groupes. L'entree mord, le compte ne le voit pas.
      - un compte de TETES seules raterait les sous-items, qui ne se fusionnent
        que si leurs parents se fusionnent d'abord — « Antihypertenseurs » sous
        « Médicaments actuels » ne change aucun compte de tete.

    A l'inverse, une entree qui se contente de RENOMMER sans rien rapprocher
    laisse la partition identique : c'est exactement ce qu'on veut declarer
    inerte, parce qu'elle habille le memento d'un libelle qu'aucune grille ne
    porte a cet endroit, sans rien reunir en echange.
    """
    out = []
    for prefixe in lib_vocabulaire.SECTIONS:
        for groupe in lib_fusion.apparier(cas_list, prefixe, ssp):
            sous = sorted(sorted(s["cas"]) for s in groupe["sous"])
            out.append((prefixe, sorted(groupe["cas"]), sous))
    return sorted(out)


def _sans_effet(vocabulaire, groupes):
    """Les entrees qui n'apparient rien — testees UNE PAR UNE, table complete moins elle.

    Le test par SSP ne suffisait pas : il declarait la SSP saine des qu'UNE
    entree mordait, et couvrait les autres. Or une entree inerte est exactement
    ce que ce controle existe pour trouver, et elle arrive pour une raison qui
    ne se voit pas a la lecture — deux libelles portes par des PARENTS
    differents ne se rejoindront jamais, quoi qu'en dise la table
    (« Carnet de suivi » sous « Éducation thérapeutique » ne rencontrera pas
    « Carnet de suivi tensionnel » sous « Suivi et éducation »). Retirer
    l'entree et regarder si le compte bouge est le seul test qui le voie.
    """
    ecarts = []
    for ssp in sorted(vocabulaire):
        if ssp not in groupes:
            continue
        with installee(vocabulaire):
            reference = partition(groupes[ssp], ssp)
        for cle in sorted(vocabulaire[ssp]):
            ampute = {s: dict(e) for s, e in vocabulaire.items()}
            del ampute[ssp][cle]
            with installee(ampute):
                if partition(groupes[ssp], ssp) == reference:
                    ecarts.append(
                        f"{ssp} / « {cle} » → « {vocabulaire[ssp][cle]} » — l'entrée ne "
                        "rapproche aucune grille : elle ne fait que renommer. Les deux "
                        "libellés ne se rencontrent jamais (sous-items de parents "
                        "différents, ou sections différentes)")
    return ecarts


def main():
    try:
        vocabulaire = lib_yaml.lire_groupe(TABLE)
    except ValueError as e:
        print("ÉCHEC — la table ne se lit pas :", e)
        return 1

    groupes = build_memento.par_ssp(None)
    inventaire = lib_vocabulaire.libelles_par_ssp(groupes)
    ecarts = verifier(vocabulaire, inventaire, groupes)

    entrees = sum(len(v) for v in vocabulaire.values())
    if ecarts:
        print("ÉCHEC —", len(ecarts), "écart(s) sur", entrees, "entrée(s) :")
        for e in ecarts:
            print("  ", e)
        return 1
    print(f"OK — {entrees} entrée(s) sur {len(vocabulaire)} SSP, toutes adossées à des "
          "libellés réels du corpus et toutes agissantes · "
          "0 rapprochement abusif (aucune grille ne voit deux de ses libellés, "
          "distincts pour le socle A, confondus par la table)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
