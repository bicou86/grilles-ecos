"""Signale, par SSP, les items que le socle A n'a pas apparies mais qui se
ressemblent. Ce sont les candidats du vocabulaire canonique. Sortie 0.

DEUX NIVEAUX, ET NON LE SEUL ITEM DE TETE. Le rapprochement lexical rate aussi
bien un titre qu'un sous-item, et c'est meme la que le gisement est le plus
dense : « Toux » porte cinq entrees « allergies » distinctes, dont quatre sont
des sous-items. Un rapport limite aux titres de tete en aurait montre une.

CHAQUE LIBELLE EST SUIVI DE SES GRILLES PORTEUSES. Sans elles, une paire ne se
juge pas : deux libelles portes par LA MEME grille sont deux questions que
cette grille a voulu distinguer, et les reunir effacerait une distinction que
son auteur a posee expres. Deux libelles portes par des grilles DISJOINTES sont
le cas ou la couche B est utile. La similarite lexicale ne dit rien de cela, et
c'est pourtant le premier tri a faire.

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


def main():
    lignes = ["# Doublons candidats — vocabulaire canonique", "",
              "Paires d'items d'une même SSP que le socle A n'a pas appariés",
              f"mais dont la similarité dépasse {SEUIL}.", "",
              "Titres de tête **et** sous-items confondus : la couche B s'applique aux",
              "deux. Les grilles porteuses suivent chaque libellé — deux libellés portés",
              "par la **même** grille sont une distinction voulue, pas un doublon.", ""]
    total = 0
    groupes = build_memento.par_ssp()
    inventaire = lib_vocabulaire.libelles_par_ssp(groupes)
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
        if candidates:
            total += len(candidates)
            lignes.append(f"## {ssp} — {len(cas)} cas")
            for a, b in candidates:
                lignes.append(f"- `{a}` {porteuses(a, inventaire[ssp])}"
                              f"  ⟷  `{b}` {porteuses(b, inventaire[ssp])}")
            lignes.append("")
    SORTIE.write_text("\n".join(lignes) + "\n", encoding="utf8")
    print(f"{total} paires candidates -> {SORTIE.relative_to(REPO)}")
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
