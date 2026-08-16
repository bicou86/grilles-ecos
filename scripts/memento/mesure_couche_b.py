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
  RESTE   les paires candidates que la propriete 8 LAISSE PASSER, qui dit
          quand s'arreter. Deux libelles qu'une meme grille distingue ne
          peuvent pas etre reunis : ils ne sont pas du stock, ils sont du
          bruit. La borne haute « a grilles disjointes » est rendue a cote,
          parce qu'elle est calibree et comparable d'une mesure a l'autre —
          voir `reste()`. Quand le stock ne contient plus que du bruit
          lexical, la couche B a fini.
  SURETE  le compteur de rapprochements abusifs de `check_vocabulaire`, qui
          doit rester A ZERO. Seul des trois a se mesurer sur le CORPUS ENTIER
          — voir `surete()`.

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


def reste(groupes, inventaire, positions):
    """(paires candidates, celles a grilles disjointes, celles reellement recevables).

    DEUX BORNES, ET L'ECART ENTRE ELLES EST INSTRUCTIF.

    « Grilles disjointes » — aucune grille ne porte les deux ECRITURES — est la
    borne haute, et c'est celle qui a ete calibree contre un comptage
    independant (1 573 / 2 291 sur la table de la ronde 1). Elle se lit dans
    l'inventaire des libelles bruts, donc elle ne bouge pas quand la table
    bouge : deux mesures successives restent comparables.

    Elle SUR-ESTIME pourtant le gisement, et la propriete 8 dit de combien. Des
    grilles disjointes ne garantissent pas l'absence de collision : German-32
    ne porte pas « Antecedents familiaux », mais il porte « Anamnese
    familiale », que la table aliase deja vers ce libelle — reunir
    « Antecedents cardiaques » avec lui confondrait deux items que German-32
    distingue. La seconde borne applique la regle exacte du controle et donne
    le gisement REELLEMENT atteignable.
    """
    candidates = disjointes = recevables = 0
    for ssp in sorted(groupes):
        cas_list = groupes[ssp]
        if len(cas_list) < 2:
            continue
        titres = sorted({x["titre"]
                         for p in lib_vocabulaire.SECTIONS
                         for g in lib_fusion.apparier(cas_list, p, ssp)
                         for x in [g] + g["sous"]})
        index = report_doublons.seaux_indexes(positions[ssp], ssp)
        for a, b in report_doublons.paires(titres):
            candidates += 1
            if inventaire[ssp].get(a, set()) & inventaire[ssp].get(b, set()):
                continue
            disjointes += 1
            bloquee = (report_doublons.irrecevable(a, b, index, ssp)
                       or report_doublons.irrecevable(b, a, index, ssp)
                       or lib_fusion.signature(a) == lib_fusion.signature(b))
            if not bloquee:
                recevables += 1
    return candidates, disjointes, recevables


def surete():
    """Le compteur de rapprochements abusifs — celui de check_vocabulaire, pas une copie.

    SUR LE CORPUS ENTIER, ET NON SUR LE LOT, contrairement aux deux autres
    indicateurs. `check_vocabulaire` tourne sur `par_ssp(None)` : une entree
    visant une SSP hors lot y serait comptee, et la compter zero ici ferait dire
    a l'indicateur le contraire du controle qu'il pretend appeler. Les deux
    autres indicateurs mesurent une PROGRESSION sur les mementos rendus, ce qui
    justifie leur perimetre plus etroit ; celui-ci mesure une SURETE, qui n'a
    pas de perimetre.
    """
    vocabulaire = lib_yaml.lire_groupe(check_vocabulaire.TABLE)
    positions = lib_vocabulaire.positions_par_ssp(build_memento.par_ssp(None))
    return len(check_vocabulaire.collisions(vocabulaire, positions))


def main():
    groupes = lot_rendu()
    inventaire = lib_vocabulaire.libelles_par_ssp(groupes)
    entrees = sum(len(v) for v in lib_yaml.lire_groupe(check_vocabulaire.TABLE).values())

    g = gain(groupes)
    positions = lib_vocabulaire.positions_par_ssp(groupes)
    candidates, disjointes, recevables = reste(groupes, inventaire, positions)
    abusifs = surete()

    print(f"Couche B — {entrees} entrées, {len(groupes)} SSP rendues")
    print(f"  GAIN    {g:5d}  items de tête 📋+🩺 portés par une partie des grilles "
          "(à faire baisser)")
    print(f"  RESTE   {recevables:5d}  paires que la propriété 8 laisse passer — "
          "toutes ne passeraient pas les neuf")
    print(f"          {disjointes:5d}  à grilles disjointes, sur {candidates} candidates "
          "(borne haute, calibrée)")
    print(f"  SÛRETÉ  {abusifs:5d}  rapprochements abusifs, sur le corpus entier "
          f"({'conforme' if abusifs == 0 else 'DOIT ÊTRE ZÉRO'})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
