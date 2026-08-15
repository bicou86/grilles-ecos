"""Non-regression et idempotence des mementos. Sortie 1 si ecart."""
import hashlib
import subprocess
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
OFFICIEL = REPO / "docs" / "obsidian-memento" / "Mémento ECOS — Grilles officielles.md"
EMPREINTE = "a9ac22efb684bee06930e0d0aeb51d7f"


def md5(chemin):
    return hashlib.md5(chemin.read_bytes()).hexdigest()


def main():
    ecarts = []
    if not OFFICIEL.exists():
        print("ECHEC — le memento officiel a disparu")
        return 1

    avant = md5(OFFICIEL)
    if avant != EMPREINTE:
        ecarts.append(f"le memento officiel a change\n    attendu : {EMPREINTE}\n    obtenu  : {avant}")

    subprocess.run([sys.executable, str(REPO / "scripts" / "build_obsidian_memento.py")],
                   check=True, capture_output=True)
    if md5(OFFICIEL) != avant:
        ecarts.append("le generateur n'est pas idempotent")

    if ecarts:
        print("ECHEC —", len(ecarts), "ecart(s) :")
        for e in ecarts:
            print("  ", e)
        return 1
    print("OK — memento officiel inchange, generateur idempotent")
    return 0


if __name__ == "__main__":
    sys.exit(main())
