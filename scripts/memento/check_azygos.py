"""Verifie l'extraction AZYGOS depuis .azygos-extraction/. Sortie 1 si ecart."""
import glob
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import lib_extraction as L

REPO = Path(__file__).resolve().parents[2]


def main():
    fichiers = sorted(glob.glob(str(REPO / ".azygos-extraction" / "*.json")))
    if not fichiers:
        print("ÉCHEC — .azygos-extraction/ est vide ou absent")
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

    if ecarts:
        print("ÉCHEC —", len(ecarts), "écart(s) :")
        for e in ecarts:
            print("  ", e)
        return 1
    print(f"OK — {len(fichiers)} extractions AZYGOS, granularité conforme")
    return 0


if __name__ == "__main__":
    sys.exit(main())
