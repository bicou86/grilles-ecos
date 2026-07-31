"""Passe nomenclature laboratoire et numero d'urgence.

Remplacements 1 pour 1, hors zones base64. Aucun ne modifie le nombre
de sous-items notes : le bareme est preserve par construction.
"""
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import lib_amboss as lib

# (motif, remplacement, commentaire)
RULES = [
    (r"\bNFS\b", "FSC", "numeration formule sanguine -> formule sanguine complete"),
    (r"\bCBC\b", "FSC", "complete blood count -> formule sanguine complete"),
    (r"\bBMP\b", "chimie sanguine", "basic metabolic panel"),
    (r"\b911\b", "144", "numero d'urgence US -> CH"),
    (r"\bSAMU\b", "144", "service d'urgence FR -> numero CH"),
]
# Volontairement absent : 112. La seule occurrence du corpus est
# « Score Global 0/112 » (AMBOSS-8), un total de bareme, pas un
# numero d'urgence. Le remplacer corromprait la grille.

# Segments a ne jamais toucher : les URI de donnees base64.
DATAURI = re.compile(r'data:image[^"]*')


def apply_to(html):
    """Applique les regles hors base64. Retourne (html, compte_par_regle)."""
    chunks = []
    last = 0
    counts = {p: 0 for p, _, _ in RULES}
    for m in DATAURI.finditer(html):
        chunks.append(("text", html[last:m.start()]))
        chunks.append(("uri", m.group(0)))
        last = m.end()
    chunks.append(("text", html[last:]))

    out = []
    for kind, chunk in chunks:
        if kind == "uri":
            out.append(chunk)
            continue
        for pattern, repl, _ in RULES:
            chunk, n = re.subn(pattern, repl, chunk)
            counts[pattern] += n
        out.append(chunk)
    return "".join(out), counts


def main():
    total = {p: 0 for p, _, _ in RULES}
    touched = 0
    for path in lib.grids():
        html = path.read_text(encoding="utf-8")
        new, counts = apply_to(html)
        if new != html:
            path.write_text(new, encoding="utf-8")
            touched += 1
        for k, v in counts.items():
            total[k] += v
    print(f"Fichiers modifies : {touched}")
    for pattern, repl, note in RULES:
        if total[pattern]:
            print(f"  {total[pattern]:3}x  {pattern} -> {repl}   ({note})")


if __name__ == "__main__":
    main()
