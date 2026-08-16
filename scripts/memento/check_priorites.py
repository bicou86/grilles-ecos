"""La table de priorites est complete et son tier est valide. Sortie 1 si ecart.

La table est curee a la main (voir docs/ecos-priorites-2026.yaml) : un `ssp`
peut nommer une page qui n'existe pas encore dans le coffre. Ce n'est plus un
echec, seulement une information rapportee sous « pages SSP a creer ».

L'EXISTENCE D'UNE PAGE SE LIT DANS L'INSTANTANE, docs/ecos-ssp-coffre.yaml, et
non dans le coffre : ce controle listait sinon les 116 SSP comme « a creer » sur
toute machine sans coffre, en restant VERT. Un rapport faux qui ne se signale
pas est pire qu'un rapport absent.

DEUXIEME PROPRIETE, CONDITIONNELLE : quand le coffre est present, l'instantane
est re-compare a lui (fige_coffre.py --verifie). Quand il est absent, cette
propriete n'a AUCUN temoin, et elle le DIT au lieu de se taire."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import fige_coffre
import lib_ssp
import lib_yaml

REPO = Path(__file__).resolve().parents[2]
TABLE = REPO / "docs" / "ecos-priorites-2026.yaml"
TIERS_VALIDES = ("incontournable", "probable", "à connaître")


def main():
    table = lib_yaml.lire_groupe(TABLE)
    if not table:
        print("ÉCHEC — docs/ecos-priorites-2026.yaml est vide ou absent")
        return 1

    pages = lib_ssp.pages_connues()
    if not pages:
        print("ÉCHEC — docs/ecos-ssp-coffre.yaml est vide ou absent ;\n"
              "  le reconstruire avec python3 scripts/memento/fige_coffre.py")
        return 1

    ecarts, sans_ssp, a_creer = [], [], []
    for plainte, champs in table.items():
        ssp = champs.get("ssp", "").strip()
        if not ssp or ssp == "?":
            sans_ssp.append(plainte)
        elif ssp not in pages:
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
    coffre_present = lib_ssp.COFFRE.is_dir()
    if coffre_present:
        ecarts += [f"instantané : {e}" for e in fige_coffre.traite(verifie=True)[0]]

    if ecarts:
        print("\nÉCHEC —", len(ecarts), "écart(s) :")
        for e in ecarts:
            print("  ", e)
        return 1
    fidelite = (f"instantané du coffre re-vérifié ({len(pages)} pages)"
                if coffre_present else
                f"instantané du coffre NON vérifié ({len(pages)} pages figées, "
                "coffre absent, propriété sans témoin)")
    print(f"\nOK — table de priorités complète ; {fidelite}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
