"""Verifie l'extraction AZYGOS depuis .azygos-extraction/. Sortie 1 si ecart."""
import glob
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import lib_extraction as L

REPO = Path(__file__).resolve().parents[2]
ONGLETS = {"Anamnèse": "a", "Examen clinique": "e", "Diagnostic": "m", "Procédure": "m"}


def main():
    fichiers = sorted(glob.glob(str(REPO / ".azygos-extraction" / "*.json")))
    if not fichiers:
        print("ECHEC — .azygos-extraction/ est vide ou absent")
        return 1

    ecarts, sans_items, longs = [], [], []
    for f in fichiers:
        cas = L.lire_azygos(f)
        if not cas["id"].startswith("AZYGOS"):
            ecarts.append(f"{f}: identifiant inattendu {cas['id']}")
        total = sum(len(v) for v in cas["sections"].values())
        if total == 0:
            sans_items.append(cas["id"])
        for lignes in cas["sections"].values():
            for genre, _, titre, _ in lignes:
                if genre == "item" and len(titre.split()) > 12:
                    longs.append(f"{cas['id']}: {titre[:60]}")

    if sans_items:
        ecarts.append(f"{len(sans_items)} extraction(s) sans aucun item : {sans_items[:5]}")
    if longs:
        ecarts.append(f"{len(longs)} titre(s) de plus de 12 mots — le pave didactique "
                      f"n'a pas ete separe : {longs[:3]}")

    if ecarts:
        print("ECHEC —", len(ecarts), "ecart(s) :")
        for e in ecarts:
            print("  ", e)
        return 1
    print(f"OK — {len(fichiers)} extractions AZYGOS, granularite conforme")
    return 0


if __name__ == "__main__":
    sys.exit(main())
