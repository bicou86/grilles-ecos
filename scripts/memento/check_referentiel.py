"""Mesure l'ecart des grilles non officielles au corpus officiel.

Les neuf grilles officielles font autorite sur ce qu'est un item de memento
(spec § referentiel). Ce rapport ne bloque rien : il NOMME ce qui s'en ecarte,
pour qu'une relecture decide. Sortie 0 toujours : ce n'est pas une barriere.
"""
import glob
import sys
from collections import Counter
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import lib_extraction as L
import lib_ssp
from check_couverture import HORS_PERIMETRE
from lib_cle import cle

REPO = Path(__file__).resolve().parents[2]
SORTIE = REPO / "docs" / "superpowers" / "rapport-referentiel-memento.md"
OFFICIELLES = lib_ssp.OFFICIELLES


def tous_les_cas():
    for corpus in lib_ssp.CORPUS:
        motif = (str(REPO / ".azygos-extraction" / "*.json") if corpus == "azygos"
                 else str(REPO / "cases" / corpus / "*.html"))
        for f in sorted(glob.glob(motif)):
            yield L.lire_azygos(f) if corpus == "azygos" else L.lire_html(f)


def tableau_par_corpus(par_corpus):
    lignes = ["| Corpus | Items orphelins |", "|---|---|"]
    for c, n in par_corpus.most_common():
        lignes.append(f"| {c} | {n} |")
    return lignes


def tableau_par_ssp(autres, reference, rattache, lot):
    """Part d'items sans repondant officiel, par SSP prioritaire.

    Ne compte que les items des grilles non officielles (les officielles
    definissent la reference, leur part y est triviale). Une SSP prioritaire
    sans aucun item rattache est listee quand meme, part marquee absente,
    plutot que d'etre passee sous silence.
    """
    total_par_ssp, orphelins_par_ssp = Counter(), Counter()
    for cid, _, titre in autres:
        ssp = rattache.get(cid)
        if ssp not in lot:
            continue
        total_par_ssp[ssp] += 1
        if cle(titre) not in reference:
            orphelins_par_ssp[ssp] += 1

    def part(ssp):
        n = total_par_ssp.get(ssp, 0)
        return orphelins_par_ssp.get(ssp, 0) / n if n else -1.0

    lignes = ["| SSP prioritaire | Items | Sans répondant | Part |", "|---|---|---|---|"]
    for ssp in sorted(lot, key=lambda s: (-part(s), s)):
        n = total_par_ssp.get(ssp, 0)
        o = orphelins_par_ssp.get(ssp, 0)
        pct = f"{100 * o // n} %" if n else "— (aucun item)"
        lignes.append(f"| {ssp} | {n} | {o} | {pct} |")
    return lignes


def main():
    reference, autres = set(), []
    trouvees = set()
    for cas in tous_les_cas():
        if cas["id"] in HORS_PERIMETRE:
            continue
        officielle = cas["id"] in OFFICIELLES
        if officielle:
            trouvees.add(cas["id"])
        for lignes in cas["sections"].values():
            for genre, _, titre, sous in lignes:
                if genre != "item":
                    continue
                if officielle:
                    reference.add(cle(titre))
                    for s in sous:
                        reference.add(cle(s))
                else:
                    autres.append((cas["id"], cas["corpus"], titre))

    manquantes = sorted(OFFICIELLES - trouvees)

    orphelins = [(i, c, t) for i, c, t in autres if cle(t) not in reference]
    par_corpus = Counter(c for _, c, _ in orphelins)
    total = len(autres)

    rattache = lib_ssp.rattachements()
    lot = lib_ssp.lot_prioritaire()

    lignes = ["# Écart au référentiel officiel — mémentos", ""]
    if manquantes:
        lignes += [
            f"**ATTENTION** — {len(manquantes)} grille(s) officielle(s) introuvable(s) "
            f"parmi les cas lus : {', '.join(manquantes)}. Le référentiel ci-dessous "
            "est calculé sur les grilles officielles effectivement trouvées "
            f"uniquement ({len(trouvees)} sur {len(OFFICIELLES)} attendues) : "
            "les chiffres qui suivent sont amputés d'autant, pas silencieusement "
            "complets.", ""]
    lignes += [
        f"{len(reference)} formes canoniques tirées des {len(trouvees)} grilles "
        "officielles trouvées.",
        f"{total} items non officiels, dont **{len(orphelins)} sans répondant** "
        f"({100 * len(orphelins) // max(total, 1)} %).", "",
    ]
    lignes += tableau_par_corpus(par_corpus)
    lignes += ["", "## Les 60 libellés orphelins les plus fréquents", ""]
    for titre, n in Counter(t for _, _, t in orphelins).most_common(60):
        lignes.append(f"- `{titre}` — {n}×")
    lignes += ["", "## Part d'items sans répondant, par SSP prioritaire", "",
               f"Les {len(lot)} SSP de `docs/ecos-priorites-2026.yaml`, triées par "
               "part décroissante d'items non officiels sans répondant dans le "
               "référentiel. N'entrent dans les décomptes que les items des "
               "grilles non officielles rattachées à cette SSP.", ""]
    lignes += tableau_par_ssp(autres, reference, rattache, lot)

    SORTIE.write_text("\n".join(lignes) + "\n", encoding="utf8")
    print(f"{len(orphelins)}/{total} items sans répondant officiel "
          f"→ {SORTIE.relative_to(REPO)}")
    if manquantes:
        print(f"ATTENTION : {len(manquantes)} grille(s) officielle(s) introuvable(s) "
              f"— {', '.join(manquantes)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
