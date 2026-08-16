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

Trois seaux, dans cet ordre de lecture : les RECEVABLES, triees par similarite
DECROISSANTE (l'ordre alphabetique mettait un faux positif en tete aussi
souvent qu'un vrai) ; les ⚠️ inertes ; les ⛔ irrecevables.

LA PORTEE DES COMPTES, parce que deux perimetres coexistent dans ce projet et
que les confondre a deja coute cinq erreurs de mesure : CE SCRIPT parcourt les
57 SSP du corpus qui portent au moins deux grilles, et en tire 3 264 paires.
`mesure_couche_b.py`, lui, ne compte que les 32 SSP du LOT PRIORITAIRE, d'ou
ses 2 297 paires et son reste atteignable de 1 579. Les deux chiffres sont
justes ; ils ne repondent pas a la meme question.

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


def main():
    lignes = ["# Doublons candidats — vocabulaire canonique", "",
              "Paires d'items d'une même SSP que le socle A n'a pas appariés",
              f"mais dont la similarité dépasse {SEUIL}.", "",
              "Titres de tête **et** sous-items confondus : la couche B s'applique aux",
              "deux. Les grilles porteuses suivent chaque libellé.", "",
              "Les paires recevables viennent d'abord, **triées par similarité",
              "décroissante** : la plus plausible en tête. Suivent deux catégories que",
              "`check_vocabulaire.py` refuserait — **ne les lisez que si tout le reste",
              "est traité** :", "",
              "- **⚠️ presque toujours inerte** : une même grille porte les deux, mais",
              "  dans des **sections différentes**. L'entrée ne réunirait rien — les",
              "  sections s'apparient séparément — et se contenterait de renommer ;",
              "- **⛔ irrecevable par construction** : soit l'entrée confondrait deux",
              "  libellés qu'une grille distingue **dans une même section** (propriété 8",
              "  — le test porte sur les signatures **après** la table, donc il attrape",
              "  aussi les variantes et les fusions indirectes), soit les deux libellés",
              "  ont **déjà la même signature** pour le socle A (propriété 6).", ""]
    total = refusees = 0
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
        recevables, douteuses, bloquees = [], [], []
        for a, b in candidates:
            ligne = (f"`{a}` {porteuses(a, inventaire[ssp])}"
                     f"  ⟷  `{b}` {porteuses(b, inventaire[ssp])}")
            # Les deux sens sont testes : le libelle retenu peut etre l'un ou
            # l'autre, et rien ne dit lequel un successeur choisira.
            ou = irrecevable(a, b, index, ssp) or irrecevable(b, a, index, ssp)
            communes = inventaire[ssp].get(a, set()) & inventaire[ssp].get(b, set())
            if ou:
                bloquees.append(f"- ⛔ {ligne} — **{ou}** distingue ces deux items")
            elif lib_fusion.signature(a) == lib_fusion.signature(b):
                # Meme signature socle A : ces deux titres ne coexistent que
                # parce qu'ils sont dans des SECTIONS differentes, que
                # l'appariement traite separement. Une entree serait refusee par
                # la propriete 6 de check_vocabulaire.
                bloquees.append(f"- ⛔ {ligne} — **même signature socle A**, "
                                "déjà appariés dans leur section")
            elif communes:
                douteuses.append(f"- ⚠️ {ligne} — **{', '.join(sorted(communes))}**, "
                                 "sections différentes")
            else:
                # TRI PAR PLAUSIBILITE DECROISSANTE. L'ordre alphabetique mettait
                # un faux positif en tete aussi souvent qu'un vrai ; la
                # similarite, deja calculee pour le seuil, ordonne gratuitement.
                recevables.append((-similarite(a, b), a, b, f"- {ligne}"))
        total += len(candidates)
        refusees += len(bloquees) + len(douteuses)
        lignes.append(f"## {ssp} — {len(cas)} cas · {len(recevables)} recevable(s), "
                      f"{len(douteuses)} ⚠️, {len(bloquees)} ⛔")
        lignes += [x[3] for x in sorted(recevables)] + douteuses + bloquees + [""]
    SORTIE.write_text("\n".join(lignes) + "\n", encoding="utf8")
    print(f"{total} paires candidates dont {total - refusees} recevables, "
          f"{refusees} écartées -> {SORTIE.relative_to(REPO)}")
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
