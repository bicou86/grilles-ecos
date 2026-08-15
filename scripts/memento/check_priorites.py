"""La table de priorites est complete et son tier est valide. Sortie 1 si ecart.

La table est curee a la main (voir docs/ecos-priorites-2026.yaml) : un `ssp`
peut nommer une page qui n'existe pas encore dans le coffre. Ce n'est plus un
echec, seulement une information rapportee sous « pages SSP a creer »."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import lib_yaml

REPO = Path(__file__).resolve().parents[2]
TABLE = REPO / "docs" / "ecos-priorites-2026.yaml"
TIERS_VALIDES = ("incontournable", "probable", "à connaître")

# lib_ssp (tache 4) n'existe pas encore : constante locale en attendant.
COFFRE = Path.home() / "Documents/Damien/Medecine/Obsidian/SSP ECOS"


def main():
    table = lib_yaml.lire_groupe(TABLE)
    if not table:
        print("ÉCHEC — docs/ecos-priorites-2026.yaml est vide ou absent")
        return 1

    ecarts, sans_ssp, a_creer = [], [], []
    for plainte, champs in table.items():
        ssp = champs.get("ssp", "").strip()
        if not ssp or ssp == "?":
            sans_ssp.append(plainte)
        elif not (COFFRE / f"SSP — {ssp}.md").exists():
            a_creer.append(f"{plainte} → {ssp}")
        if champs.get("tier") not in TIERS_VALIDES:
            ecarts.append(f"{plainte}: tier inattendu {champs.get('tier')!r}")

    if sans_ssp:
        ecarts.append(f"{len(sans_ssp)} plainte(s) sans SSP : {sans_ssp}")

    print(f"{len(table)} plaintes prioritaires · {len({c.get('ssp') for c in table.values()})} SSP visées")
    if a_creer:
        print(f"\n{len(a_creer)} page(s) SSP à créer :")
        for p in sorted(a_creer):
            print("  ", p)
    if ecarts:
        print("\nÉCHEC —", len(ecarts), "écart(s) :")
        for e in ecarts:
            print("  ", e)
        return 1
    print("\nOK — table de priorités complète")
    return 0


if __name__ == "__main__":
    sys.exit(main())
