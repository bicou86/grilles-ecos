"""Verifie la source AZYGOS versionnee, docs/azygos-grilles/. Sortie 1 si ecart.

La source lue est le MIROIR versionne, pas `.azygos-extraction/` : le chemin
vient de `lib_extraction.motif()`, seul endroit ou il est ecrit.

DEUXIEME PROPRIETE, CONDITIONNELLE : quand l'extraction brute est presente
localement, le miroir est re-compare a elle (fige_azygos.py --verifie). Sur un
clone frais elle est absente, et cette propriete-la n'a alors AUCUN temoin.
Elle le DIT au lieu de se taire : un controle sans temoin qui affiche « OK »
laisse croire qu'il a regarde.
"""
import glob
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import fige_azygos
import lib_extraction as L

REPO = Path(__file__).resolve().parents[2]


def main():
    fichiers = sorted(glob.glob(L.motif("azygos")))
    if not fichiers:
        print("ÉCHEC — docs/azygos-grilles/ est vide ou absent ; "
              "le reconstruire avec scripts/memento/fige_azygos.py")
        return 1

    ecarts = []
    sans_items, longs, onglets_inconnus, sections_manquantes = [], [], [], []
    for f in fichiers:
        cas = L.lire_azygos(f)
        candidats, inconnus = L.classifie_onglets(f)

        if not cas["id"].startswith("AZYGOS"):
            ecarts.append(f"{f}: identifiant inattendu {cas['id']}")

        total = sum(len(v) for v in cas["sections"].values())
        if total == 0:
            sans_items.append(cas["id"])

        for lignes in cas["sections"].values():
            for genre, _, titre, _ in lignes:
                if genre == "item" and len(titre.split()) > 12:
                    longs.append(f"{cas['id']}: {titre[:60]}")

        # Un onglet du JSON qui n'est ni rattache a une section, ni exclu
        # explicitement, doit se signaler plutot que disparaitre.
        for onglet in inconnus:
            onglets_inconnus.append(f"{cas['id']}: {onglet!r}")

        # Une section attendue (un onglet candidat existe dans le JSON) mais
        # absente ou vide dans le resultat trahit une correspondance ratee.
        for prefixe, onglets in candidats.items():
            if not cas["sections"].get(prefixe):
                sections_manquantes.append(
                    f"{cas['id']}: section {prefixe!r} vide malgre {onglets!r}")

    if sans_items:
        ecarts.append(f"{len(sans_items)} extraction(s) sans aucun item : {sans_items[:5]}")
    if longs:
        ecarts.append(f"{len(longs)} titre(s) de plus de douze mots — le pavé didactique "
                      f"n'a pas été séparé : {longs[:3]}")
    if onglets_inconnus:
        ecarts.append(f"{len(onglets_inconnus)} onglet(s) inconnu(s) — ni rattache a une "
                      f"section, ni exclu explicitement : {onglets_inconnus[:5]}")
    if sections_manquantes:
        ecarts.append(f"{len(sections_manquantes)} section(s) vide(s) malgre un onglet "
                      f"candidat dans le JSON : {sections_manquantes[:5]}")

    # Le miroir est-il fidele au brut ? Seulement mesurable si le brut est la.
    brut_present = any(fige_azygos.BRUT.glob("*.json"))
    if brut_present:
        ecarts += [f"miroir : {e}" for e in fige_azygos.traite(verifie=True)[0]]

    if ecarts:
        print("ÉCHEC —", len(ecarts), "écart(s) :")
        for e in ecarts:
            print("  ", e)
        return 1
    fidelite = ("fidélité au brut re-vérifiée" if brut_present else
                "fidélité au brut NON vérifiée (.azygos-extraction/ absent, "
                "propriété sans témoin)")
    print(f"OK — {len(fichiers)} extractions AZYGOS, granularité conforme ; {fidelite}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
