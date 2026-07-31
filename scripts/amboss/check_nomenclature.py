"""Detecte les termes non suisses. Sortie 1 si presents."""
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import lib_amboss as lib

# Termes bannis et leur remplacement attendu.
# CBC et BMP : exclus uniquement quand ils servent de cle de glossaire
# (« CBC : ... », « BMP : ... »), immediatement suivis de « : ». Ce cas
# traduit les abreviations d'un schema anglophone dont l'image (base64)
# n'est pas modifiee : l'abreviation d'origine doit rester lisible en cle
# pour que le lecteur puisse relier la legende au schema (ex. AMBOSS-33,
# « BMP : chimie sanguine (panel metabolique de base) »). Le lookahead ne
# joue que dans ce cas precis ; un CBC ou BMP employe ailleurs comme terme
# medical (hors position de cle de glossaire) reste detecte normalement.
BANNED = {
    r"\bNFS\b": "FSC",
    r"\bCBC\b(?! : )": "FSC",
    r"\bBMP\b(?! : )": "chimie sanguine",
    r"\bVicodin\b": "Tramadol (Tramal®)",
    r"\bTylenol\b": "Paracetamol (Dafalgan®)",
    r"\bTums\b": "Antiacides (Rennie®)",
    r"\bmg/dL\b": "unites SI",
    r"\b911\b": "144",
    r"\bSAMU\b": "144",
}
# Pas de regle sur 112 : le corpus ne contient aucun numero d'urgence 112.
# La seule occurrence est « Score Global 0/112 » dans AMBOSS-8 — un total de
# bareme. La remplacer corromprait la grille.


def main():
    total = 0
    for path in lib.grids():
        html = lib.strip_base64(path.read_text(encoding="utf-8"))
        for pattern, repl in BANNED.items():
            hits = re.findall(pattern, html)
            if hits:
                total += len(hits)
                print(f"  {path.name}: {len(hits)}x {pattern} -> attendu {repl}")
    if total:
        print(f"\nECHEC — {total} terme(s) non suisse(s) restant(s)")
        return 1
    print("OK — aucun terme non suisse detecte")
    return 0


if __name__ == "__main__":
    sys.exit(main())
