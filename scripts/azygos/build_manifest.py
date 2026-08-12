"""Consolide les manifestes par cas en un MANIFEST.tsv de corpus.

Même format que les autres corpus : nom_depot, sha256, octets, dimensions,
chemin_vault. La provenance étant ici une URL Supabase (et non le vault
Obsidian), la dernière colonne porte le chemin d'objet distant.

    python3 scripts/azygos/build_manifest.py
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import lib_azygos as lib  # noqa: E402


def main() -> None:
    entrees = []
    for fragment in sorted(lib.IMAGES.glob("_manifeste-*.json")):
        entrees.extend(json.loads(fragment.read_text(encoding="utf-8")))
    entrees.sort(key=lambda e: e["nom"])

    lignes = [
        "# Provenance des images des grilles azygos. Généré par "
        "scripts/azygos/build_manifest.py — ne pas éditer à la main.",
        "# nom_depot\tsha256\toctets\tdimensions\tsource",
    ]
    for e in entrees:
        lignes.append(
            f"{e['nom']}\t{e['sha256']}\t{e['octets']}\t{e['dimensions']}\t{e['source']}"
        )
    (lib.IMAGES / "MANIFEST.tsv").write_text("\n".join(lignes) + "\n", encoding="utf-8")

    for fragment in lib.IMAGES.glob("_manifeste-*.json"):
        fragment.unlink()

    presentes = {p.name for p in lib.IMAGES.glob("*.jpg")}
    listees = {e["nom"] for e in entrees}
    print(f"MANIFEST.tsv : {len(entrees)} images")
    if presentes - listees:
        print(f"  ⚠ sur disque mais absentes du manifeste : {sorted(presentes - listees)}")
    if listees - presentes:
        print(f"  ⚠ au manifeste mais absentes du disque : {sorted(listees - presentes)}")


if __name__ == "__main__":
    main()
