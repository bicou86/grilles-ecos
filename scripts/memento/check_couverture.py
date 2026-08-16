"""Tout cas en perimetre est extrait et rattache, ou nomme. Sortie 1 si ecart."""
import glob
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import lib_extraction as L
import lib_ssp
import lib_yaml

REPO = Path(__file__).resolve().parents[2]

# Grilles dont la totalite des criteres sont hors du schema anamnese / examen
# / management (prefixe "c", communication) : aucun item a/e/m n'existe a
# extraire, ce n'est pas une lacune d'extraction. RESCOS-8, une autre grille
# BBN, repartit ses etapes SPIKES sur a/e/m normalement — seule RESCOS-7 est
# un cas a une section unique. Exclue explicitement plutot que masquee par
# lib_extraction, qui reste inchangee (elle est partagee et figee par
# check_identifiants.py / check_fusion.py).
#
# RESCOS-4 est une seconde raison d'exclusion : une grille ABCDE de
# reanimation (stabilisation, voies aeriennes, circulation...) qui a bien des
# items a/e/m, mais dont aucun ne nomme un diagnostic — le mot « diagnostic »
# n'apparait nulle part dans le fichier. La tache 6 (resolution du
# diagnostic par cascade) avait invente une valeur a partir d'un bloc
# « Mesures immediates » ; exclue ici plutot que de porter un diagnostic
# fabrique, meme constat que RESCOS-7 cote couverture.
HORS_PERIMETRE = {
    "RESCOS-7": "grille purement communication (criteres 'c' uniquement, "
                "aucun a/e/m) — cf. rapport tache 4",
    "RESCOS-4": "grille ABCDE de reanimation sans diagnostic identifiable "
                "(le mot 'diagnostic' n'apparait nulle part) — cf. relecture tache 6",
    "German-73": "exclue sur decision de l'auteur — le premier c-red est le "
                 "symptome (« Saignement vaginal du premier trimestre »), pas "
                 "un diagnostic tranche",
    "RESCOS-55": "exclue sur decision de l'auteur",
    "RESCOS-64-2": "station de PRESENTATION DE CAS, pas de rencontre clinique : "
                   "ses criteres portent les prefixes 'r' (raisonnement : « Arguments "
                   "POUR/CONTRE le cancer pulmonaire ») et 'p' (presentation : "
                   "« Identite, motif de consultation »), aucun a/e/m. Meme motif que "
                   "RESCOS-7. C'est la seule grille du corpus hors du schema a/e/m/c.",
}


def recap_lot1(rattache):
    """Combien de SSP prioritaires portent au moins une grille, et lesquelles n'en portent aucune."""
    table = lib_yaml.lire_groupe(REPO / "docs" / "ecos-priorites-2026.yaml")
    ssp_de_priorite = {champs["ssp"]: champs.get("tier", "?")
                        for champs in table.values() if champs.get("ssp", "?") != "?"}
    portees = set(rattache.values())
    avec, sans = [], []
    for ssp, tier in ssp_de_priorite.items():
        (avec if ssp in portees else sans).append((ssp, tier))

    print(f"Lot 1 — {len(ssp_de_priorite)} SSP prioritaires, "
          f"{len(avec)} portent au moins une grille, {len(sans)} n'en portent aucune :")
    for ssp, tier in sorted(sans):
        print(f"    {ssp} ({tier})")
    print()


def main():
    tout = "--lot" in sys.argv and "tout" in sys.argv
    lot = None if tout else lib_ssp.lot_prioritaire()
    rattache = lib_ssp.rattachements()
    recap_lot1(rattache)
    total, sans_ssp, sans_items = 0, [], []
    for corpus in lib_ssp.CORPUS:
        motif = L.motif(corpus)
        for f in sorted(glob.glob(motif)):
            cas = L.lire_azygos(f) if corpus == "azygos" else L.lire_html(f)
            total += 1
            if cas["id"] in HORS_PERIMETRE:
                continue          # exclusion nommee, voir HORS_PERIMETRE
            if lot is not None and rattache.get(cas["id"]) not in lot:
                continue          # hors lot 1 : reporte au lot 2
            if cas["id"] not in rattache:
                sans_ssp.append(f"{cas['id']} ({corpus})")
            if not sum(len(v) for v in cas["sections"].values()):
                sans_items.append(f"{cas['id']} ({corpus})")

    print(f"lot {'complet' if lot is None else 'prioritaire'} · "
          f"{total} grilles lues · {total - len(sans_ssp)} rattachees a une SSP")
    if HORS_PERIMETRE:
        print(f"({len(HORS_PERIMETRE)} exclue(s) explicitement — voir HORS_PERIMETRE) :")
        for cid, motif in HORS_PERIMETRE.items():
            print(f"    {cid} : {motif}")
    if sans_items:
        print(f"\nECHEC — {len(sans_items)} grille(s) sans aucun item extrait :")
        for x in sans_items:
            print("   ", x)
        return 1
    if sans_ssp:
        print(f"\nECHEC — {len(sans_ssp)} grille(s) sans rattachement SSP :")
        for x in sans_ssp:
            print("   ", x)
        print("\n  Completer docs/ecos-ssp-complements.yaml.")
        return 1
    print("OK — toutes les grilles sont extraites et rattachees")
    return 0


if __name__ == "__main__":
    sys.exit(main())
