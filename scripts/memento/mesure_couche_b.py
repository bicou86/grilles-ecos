"""Les trois indicateurs de la couche B, mesures sur `apparier()`. Sortie 0.

    python3 scripts/memento/mesure_couche_b.py

POURQUOI EN AMONT DU RENDU. Les deux indicateurs essayes avant celui-ci se
mesuraient sur le document produit, et tous deux ont menti :

  - le TAUX D'ITEMS DE TETE SUFFIXES baisse de 0,5 point pendant que 67
    doublons disparaissent, parce qu'un item de tete devenu nu rend leur
    suffixe a ses sous-items : la marque descend d'un cran et devient exacte,
    et l'indicateur lit cela comme une stagnation ;
  - le NOMBRE D'ITEMS DE TETE, propose en repli, MONTE dans l'encadre 💊
    (1 046 -> 1 053). Sur Toux, « Diagnostic principal suspecté » ->
    « Diagnostic principal évoqué » change les porteurs de l'item, si bien que
    `lib_fusion.contenu_partage()` devient faux et que l'item redescend,
    duplique, dans cinq sous-blocs de diagnostic. Chaque copie dit vrai pour
    son diagnostic — ce n'est pas un defaut, mais l'indicateur est disqualifie.

Les deux pathologies viennent du RENDU : le decoupage du management par
diagnostic, et l'elision du suffixe herite. Mesurer sur `lib_fusion.apparier()`
les evite toutes deux.

Les trois indicateurs, et ce qu'on attend d'eux :

  GAIN    `G`, a faire BAISSER. Les groupes d'items de tete des sections
          anamnese et status, sur les SSP a deux grilles ou plus, portes par un
          SOUS-ENSEMBLE STRICT des grilles de leur SSP. C'est exactement la
          population des items dont le memento doit dire « seulement une partie
          des grilles » — reunir deux formulations la fait baisser de un.
  RESTE   les paires candidates A GRILLES DISJOINTES, qui dit quand s'arreter.
          Deux libelles que la MEME grille porte ne peuvent pas etre reunis
          (voir `check_vocabulaire.collisions`) : ils ne sont pas du stock, ils
          sont du bruit. Le reste atteignable, lui, est le vrai plafond de la
          couche B. Quand il ne contient plus que du bruit lexical, c'est fini.
  SURETE  le compteur de rapprochements abusifs de `check_vocabulaire`, qui
          doit rester A ZERO.

DETERMINISME : aucune date, aucun aleatoire, tout ensemble trie avant d'etre
compte ou ecrit.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import build_memento                                      # noqa: E402
import check_vocabulaire                                  # noqa: E402
import lib_fusion                                         # noqa: E402
import lib_ssp                                            # noqa: E402
import lib_vocabulaire                                    # noqa: E402
import lib_yaml                                           # noqa: E402
import report_doublons                                    # noqa: E402

REPO = Path(__file__).resolve().parents[2]
FUSIONNEES = ("a", "e")   # les sections que le memento fusionne entre grilles


def lot_rendu():
    """Les SSP du lot prioritaire qui recoivent effectivement un memento.

    Meme filtre que `build_memento.documents()` : une SSP dont le nom porte / ou
    " n'est pas ecrite, et n'a donc pas a peser dans la mesure.
    """
    groupes = build_memento.par_ssp(lib_ssp.lot_prioritaire())
    return {s: v for s, v in groupes.items() if "/" not in s and '"' not in s}


def gain(groupes):
    """`G` — items de tete d'anamnese et de status portes par une partie des grilles.

    Le seuil est le SOUS-ENSEMBLE STRICT, pas la moitie : un item porte par
    deux grilles sur trois est deja un item que le memento doit marquer, et
    c'est ce marquage-la que la couche B fait disparaitre quand il est faux.
    (Pour memoire, le seuil « moins de la moitie » donnerait 2 489 la ou
    celui-ci donne 2 743 : il ignorerait les items presque partages, qui sont
    precisement ceux qu'une seule formulation divergente separe du reste.)

    Les SSP a UNE grille sont ecartees : tout y est porte par toutes les
    grilles, elles ne peuvent rien apporter ni rien perdre.
    """
    total = 0
    for ssp in sorted(groupes):
        cas_list = groupes[ssp]
        if len(cas_list) < 2:
            continue
        for prefixe in FUSIONNEES:
            for groupe in lib_fusion.apparier(cas_list, prefixe, ssp):
                if len(groupe["cas"]) < len(cas_list):
                    total += 1
    return total


def reste(groupes, inventaire):
    """(paires candidates, celles a grilles disjointes).

    Les porteurs se lisent dans l'INVENTAIRE DES LIBELLES BRUTS et non dans les
    groupes appraies : la question posee est « ces deux ECRITURES cohabitent-
    elles dans une grille ? », qui porte sur le corpus, pas sur l'etat courant
    de la table. Un rapprochement deja fait ne doit pas changer retroactivement
    le verdict de recevabilite d'une paire voisine.
    """
    candidates = disjointes = 0
    for ssp in sorted(groupes):
        cas_list = groupes[ssp]
        if len(cas_list) < 2:
            continue
        titres = sorted({x["titre"]
                         for p in lib_vocabulaire.SECTIONS
                         for g in lib_fusion.apparier(cas_list, p, ssp)
                         for x in [g] + g["sous"]})
        for a, b in report_doublons.paires(titres):
            candidates += 1
            if not (inventaire[ssp].get(a, set()) & inventaire[ssp].get(b, set())):
                disjointes += 1
    return candidates, disjointes


def surete(groupes):
    """Le compteur de rapprochements abusifs — celui de check_vocabulaire, pas une copie."""
    vocabulaire = lib_yaml.lire_groupe(check_vocabulaire.TABLE)
    positions = lib_vocabulaire.positions_par_ssp(groupes)
    return len(check_vocabulaire.collisions(vocabulaire, positions))


def main():
    groupes = lot_rendu()
    inventaire = lib_vocabulaire.libelles_par_ssp(groupes)
    entrees = sum(len(v) for v in lib_yaml.lire_groupe(check_vocabulaire.TABLE).values())

    g = gain(groupes)
    candidates, disjointes = reste(groupes, inventaire)
    abusifs = surete(groupes)

    print(f"Couche B — {entrees} entrées, {len(groupes)} SSP rendues")
    print(f"  GAIN    {g:5d}  items de tête 📋+🩺 portés par une partie des grilles "
          "(à faire baisser)")
    print(f"  RESTE   {disjointes:5d}  paires candidates à grilles disjointes, "
          f"sur {candidates} (le plafond de la couche B)")
    print(f"  SÛRETÉ  {abusifs:5d}  rapprochements abusifs "
          f"({'conforme' if abusifs == 0 else 'DOIT ÊTRE ZÉRO'})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
