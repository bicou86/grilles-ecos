"""Construit toutes les grilles azygos dont l'extraction est disponible.

Le numéro de corpus (AZYGOS-N) suit l'ordre alphabétique de l'inventaire, qui
est celui de la collection en ligne — ainsi un cas garde le même numéro d'une
exécution à l'autre, même si l'extraction est partielle.

Usage :
    python3 scripts/azygos/build_all.py          # tout ce qui est extrait
    python3 scripts/azygos/build_all.py --liste  # état d'avancement seulement
"""

from __future__ import annotations

import json
import sys
import traceback
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import lib_azygos as lib  # noqa: E402
from build_grid import construit  # noqa: E402


def main() -> None:
    inventaire = json.loads(
        (Path(__file__).parent / "inventaire.json").read_text(encoding="utf-8")
    )
    cas = inventaire["cas"]
    liste_seule = "--liste" in sys.argv

    faits, manquants, echecs = [], [], []
    for numero, fiche in enumerate(cas, start=1):
        source = lib.EXTRACTION / f"{fiche['id']}.json"
        if not source.exists():
            manquants.append((numero, fiche["titre"]))
            continue
        if liste_seule:
            faits.append((numero, fiche["titre"]))
            continue
        try:
            construit(fiche["id"], numero, fiche)
            faits.append((numero, fiche["titre"]))
        except Exception:  # noqa: BLE001
            echecs.append((numero, fiche["titre"]))
            traceback.print_exc()

    print(f"\n{len(faits)}/{len(cas)} grilles construites")
    if manquants:
        print(f"{len(manquants)} extractions manquantes :")
        for n, t in manquants:
            print(f"   AZYGOS-{n} · {t}")
    if echecs:
        print(f"{len(echecs)} échecs :")
        for n, t in echecs:
            print(f"   AZYGOS-{n} · {t}")


if __name__ == "__main__":
    main()
