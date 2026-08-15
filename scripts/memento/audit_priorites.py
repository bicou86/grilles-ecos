"""Audite la table de priorites 2026 face a la source. Sortie toujours 0.

La source est hors depot : ECOS_Priorites_2026.html, une analyse de recurrence
sur 374 cas et 12 editions. Ses donnees vivent dans un `const DATA` JavaScript.
On ne retient que les diagnostics « incontournable » et « probable ».

La table docs/ecos-priorites-2026.yaml est desormais curee a la main par
l'utilisateur (44 plaintes, un tier « a connaitre » que la source ne connait
pas, des plaintes absentes de la source). Elle n'est donc plus derivable et ce
script ne l'ecrit plus jamais : il se contente d'un rapport en deux volets —
les diagnostics prioritaires de la source qu'aucune entree de la table ne
couvre (oublis potentiels), et les plaintes de la table absentes de la source
(ajouts legitimes de l'utilisateur), pour information seulement.
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
    table = lib_yaml.lire_groupe(TABLE)

    diagnostics_table = set()
    for champs in table.values():
        for d in champs.get("diagnostics", "").split("·"):
            d = d.strip()
            if d:
                diagnostics_table.add(d)
    plaintes_table = set(table)

    diagnostics_source = {}
    plaintes_source = set()
    for diag in donnees()["diags"]:
        if diag.get("tier") not in ("incontournable", "probable"):
            continue
        plainte = diag.get("plainte", "").strip() or "(sans plainte)"
        plaintes_source.add(plainte)
        diagnostics_source[diag["nom"]] = plainte

    oublis = sorted(nom for nom in diagnostics_source if nom not in diagnostics_table)
    ajouts = sorted(plaintes_table - plaintes_source)

    print(f"{len(table)} plainte(s) dans la table · "
          f"{len(diagnostics_source)} diagnostic(s) prioritaire(s) dans la source")

    if oublis:
        print(f"\n{len(oublis)} diagnostic(s) prioritaire(s) de la source absent(s) "
              "de la table (oublis potentiels) :")
        for nom in oublis:
            print(f"   {nom}  (plainte source : {diagnostics_source[nom]})")
    else:
        print("\nAucun diagnostic prioritaire de la source n'est absent de la table.")

    if ajouts:
        print(f"\n{len(ajouts)} plainte(s) de la table absente(s) de la source "
              "(ajouts de l'utilisateur, pour information) :")
        for plainte in ajouts:
            print("  ", plainte)
    else:
        print("\nAucune plainte de la table n'est absente de la source.")

    return 0


if __name__ == "__main__":
    sys.exit(main())
