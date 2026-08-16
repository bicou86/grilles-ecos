"""Signale, par SSP, les items que le socle A n'a pas apparies mais qui se
ressemblent. Ce sont les candidats du vocabulaire canonique. Sortie 0.

DEUX NIVEAUX, ET NON LE SEUL ITEM DE TETE. Le rapprochement lexical rate aussi
bien un titre qu'un sous-item, et c'est meme la que le gisement est le plus
dense : « Toux » porte cinq entrees « allergies » distinctes, dont quatre sont
des sous-items. Un rapport limite aux titres de tete en aurait montre une.

CHAQUE PAIRE EST TRIEE SELON SA RECEVABILITE. Deux libelles qu'UNE MEME grille
porte dans UNE MEME SECTION sont deux questions que son auteur a voulu
distinguer : `check_vocabulaire` refuse l'entree, et la proposer serait faire
perdre son temps au lecteur. Ces paires-la sont marquees ⛔ et reportees en fin
de section ; les recevables — celles a grilles DISJOINTES — viennent d'abord.
Elles sont 1 579 sur 2 297 pour les 32 SSP du lot : sans ce tri, deux
propositions sur cinq etaient irrecevables par construction.

Le rapport ne PROPOSE que des candidats : la decision reste humaine, et un
rapprochement abusif — reunir deux items cliniquement distincts — efface de
l'information sans laisser de trace, la ou un rapprochement rate reste visible.
"""
import sys
from difflib import SequenceMatcher
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import build_memento
import lib_vocabulaire

REPO = Path(__file__).resolve().parents[2]
SORTIE = REPO / "docs" / "superpowers" / "rapport-doublons-memento.md"
SEUIL = 0.72


def paires(libelles):
    """Les couples de libelles dont la similarite depasse le seuil, ordre stable."""
    tries = sorted(libelles)
    return [(a, b) for n, a in enumerate(tries) for b in tries[n + 1:]
            if SequenceMatcher(None, a.lower(), b.lower()).ratio() > SEUIL]


def irrecevable(a, b, seaux):
    """La grille et la section ou les deux libelles cohabitent, ou None.

    Meme regle que `check_vocabulaire.collisions` — meme notion de collision de
    part et d'autre, pour que le rapport ne propose jamais ce que le controle
    refusera.
    """
    for (cid, prefixe), seau in sorted(seaux.items()):
        if a in seau and b in seau:
            return f"{cid}, section « {prefixe} »"
    return None


def main():
    lignes = ["# Doublons candidats — vocabulaire canonique", "",
              "Paires d'items d'une même SSP que le socle A n'a pas appariés",
              f"mais dont la similarité dépasse {SEUIL}.", "",
              "Titres de tête **et** sous-items confondus : la couche B s'applique aux",
              "deux. Les grilles porteuses suivent chaque libellé.", "",
              "Deux marques, toutes deux reportées après les paires recevables —",
              "**ne les lisez que si tout le reste est traité** :", "",
              "- **⛔ irrecevable par construction** : une même grille porte les deux",
              "  libellés dans **une même section**, elle les distingue donc exprès, et",
              "  `check_vocabulaire.py` refusera l'entrée ;",
              "- **⚠️ presque toujours inerte** : une même grille porte les deux, mais",
              "  dans des **sections différentes**. L'entrée ne réunirait rien — les",
              "  sections s'apparient séparément — et se contenterait de renommer.", ""]
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
        seaux = positions[ssp]
        recevables, douteuses, bloquees = [], [], []
        for a, b in candidates:
            ligne = (f"- `{a}` {porteuses(a, inventaire[ssp])}"
                     f"  ⟷  `{b}` {porteuses(b, inventaire[ssp])}")
            ou = irrecevable(a, b, seaux)
            communes = inventaire[ssp].get(a, set()) & inventaire[ssp].get(b, set())
            if ou:
                bloquees.append(f"- ⛔ {ligne[2:]} — **{ou}**")
            elif communes:
                douteuses.append(f"- ⚠️ {ligne[2:]} — **{', '.join(sorted(communes))}**, "
                                 "sections différentes")
            else:
                recevables.append(ligne)
        total += len(candidates)
        refusees += len(bloquees) + len(douteuses)
        lignes.append(f"## {ssp} — {len(cas)} cas · {len(recevables)} recevable(s), "
                      f"{len(douteuses)} ⚠️, {len(bloquees)} ⛔")
        lignes += recevables + douteuses + bloquees + [""]
    SORTIE.write_text("\n".join(lignes) + "\n", encoding="utf8")
    print(f"{total} paires candidates dont {total - refusees} recevables "
          f"({refusees} ⛔ irrecevables) -> {SORTIE.relative_to(REPO)}")
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
