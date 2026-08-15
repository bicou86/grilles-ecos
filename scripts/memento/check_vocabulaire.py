"""Garde-fou de la couche B : toute entree du vocabulaire doit mordre. Sortie 1 si ecart.

LE DEFAUT QUE CE CONTROLE FERME. `docs/ecos-vocabulaire.yaml` est consulte par
`lib_fusion.canonique()` avec un `dict.get()` EXACT sur le libelle nu. Une
entree mal orthographiee — un accent de travers, une espace finale, une
majuscule de moins, un nom de SSP approximatif — ne leve rien, ne compte pour
rien, et laisse croire que la curation a eu lieu. Verifie avant d'ecrire ce
controle : trois variantes erronees d'un meme libelle, zero effet, zero
message. Une table de curation silencieusement morte est pire que pas de table
du tout, parce qu'on cesse de regarder le rendu.

SEPT PROPRIETES, de la plus grossiere a la plus fine :

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

Ce que ce controle ne peut PAS verifier, et qui reste a la relecture humaine :
que les deux libelles reunis parlent bien de la meme chose. Un rapprochement
abusif efface de l'information sans laisser de trace ; aucun test ne le voit.
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

    ecarts += _sans_effet(vocabulaire, groupes)
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
          "libellés réels du corpus et toutes agissantes")
    return 0


if __name__ == "__main__":
    sys.exit(main())
