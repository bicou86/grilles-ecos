"""Extrait les priorites 2026 vers une table curee.

La source est hors depot : ECOS_Priorites_2026.html, une analyse de recurrence
sur 374 cas et 12 editions. Ses donnees vivent dans un `const DATA` JavaScript.
On ne retient que les diagnostics « incontournable » et « probable ».

La correspondance plainte -> page SSP du coffre est CUREE : douze plaintes
tombent sur un homonyme, treize non (« Bilan », « Psychose », « Vertige »…).
Une valeur deja presente n'est jamais ecrasee.
"""
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import lib_yaml

REPO = Path(__file__).resolve().parents[2]
SOURCE = Path.home() / "Documents/Damien/Medecine/ECOS_Priorites_2026.html"
TABLE = REPO / "docs" / "ecos-priorites-2026.yaml"


def donnees():
    texte = SOURCE.read_text(encoding="utf8", errors="replace")
    depart = texte.index("=", texte.index("const DATA")) + 1
    profondeur = 0
    for i in range(depart, len(texte)):
        if texte[i] == "{":
            if profondeur == 0:
                debut = i
            profondeur += 1
        elif texte[i] == "}":
            profondeur -= 1
            if profondeur == 0:
                return json.loads(texte[debut:i + 1])
    raise ValueError("bloc DATA introuvable")


def main():
    existant = lib_yaml.lire_groupe(TABLE)
    par_plainte = {}
    for diag in donnees()["diags"]:
        if diag.get("tier") not in ("incontournable", "probable"):
            continue
        p = diag.get("plainte", "").strip() or "(sans plainte)"
        entree = par_plainte.setdefault(p, {"tier": diag["tier"], "pct": 0, "diagnostics": []})
        entree["diagnostics"].append(diag["nom"])
        entree["pct"] = max(entree["pct"], diag.get("pct", 0))
        if diag["tier"] == "incontournable":
            entree["tier"] = "incontournable"

    lignes = ["# Priorites de revision ECOS 2026 — TABLE CUREE.",
              "# Source : ECOS_Priorites_2026.html (recurrence 2011-2025, hors depot).",
              "# `ssp` doit nommer EXACTEMENT une page « SSP — <nom>.md » du coffre ;",
              "# mettre ? pour les plaintes sans page evidente, puis trancher a la main.",
              "# Une valeur deja presente n'est jamais ecrasee.",
              ""]
    for plainte in sorted(par_plainte):
        e = par_plainte[plainte]
        ancien = existant.get(plainte, {})
        lignes += [f'"{plainte}":',
                   f'  ssp: {ancien.get("ssp", "?")}',
                   f'  tier: {e["tier"]}',
                   f'  pct: {e["pct"]}',
                   f'  diagnostics: {" · ".join(sorted(e["diagnostics"]))}']
    TABLE.write_text("\n".join(lignes) + "\n", encoding="utf8")
    print(f"{len(par_plainte)} priorités -> {TABLE.relative_to(REPO)}")


if __name__ == "__main__":
    main()
