"""Passe nomenclature laboratoire du corpus RESCOS. Hors zones base64.

Meme forme que `scripts/amboss/apply_lab_nomenclature.py` : remplacements
1 pour 1, aucun ne touche a un `data-criteria` ni a un `.criteria-text`, donc
le bareme est preserve par construction (verifie avant application : 0
occurrence de `NFS` dans l'un ou l'autre, sur les 41 grilles).

DEUX FAMILLES DE REGLES, ET POURQUOI ELLES SONT SEPAREES
---------------------------------------------------------
`GLOBAL` est un remplacement de TERME : `NFS` -> `FSC` vaut partout, sans
lecture. 104 occurrences sur 28 grilles.

`LITTERAUX` est un remplacement de VALEUR. Une unite anglo-saxonne n'a pas de
facteur unique : il depend de l'ANALYTE, qu'il faut identifier avant de
convertir. Les sept conversions du corpus portent quatre analytes distincts et
trois facteurs differents :

  * hemoglobine  g/dL  -> g/L      x10        (Hb 7 g/dL   = 70 g/L)
  * LDL          mg/dL -> mmol/L   /38,67     (LDL 70      = 1,8 mmol/L)
  * leucocytes   /mm³  -> G/L      x0,001     (12 000/mm³  = 12 G/L)
  * plaquettes   (unite implicite) -> G/L     (422         = 422 G/L)

Appliquer le facteur de la creatinine (x88,4) aux `mg/dL` du corpus aurait
produit « LDL < 6187 µmol/L » : c'est pourquoi la regle est litterale, grille
par grille, et non un motif d'unite.

DEUX VALEURS SUR LA MEME LIGNE
------------------------------
Les deux lignes LDL portent DEUX seuils dans la meme unite
(« < 70 mg/dL, voire < 55 mg/dL »). Un remplacement d'unite seule aurait
converti le premier et laisse le second. Les litteraux couvrent la clause
ENTIERE, ce qui rend l'oubli impossible : si la clause a bouge, le motif ne
matche plus et le script le signale au lieu de convertir a moitie.

QUALIFICATIFS VOISINS
---------------------
Chaque conversion a ete relue avec le mot qui la qualifie :
« hyperleucocytose (> 12 G/L) » (RESCOS-9b) reste une hyperleucocytose, et la
meme grille ecrit deja « Leucocytes > 12 G/L » ailleurs — la conversion aligne
les deux ecritures au lieu de les opposer.
"""
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import lib_rescos as lib

# (motif, remplacement, commentaire) — appliques a toutes les grilles.
GLOBAL = [
    (r"\bNFS\b", "FSC", "numeration formule sanguine -> formule sanguine complete"),
]

# (fragment de nom de grille, texte exact, remplacement, commentaire).
# Le texte a remplacer est LITTERAL et unique dans sa grille : un compte
# different de 1 est une erreur, pas un avertissement.
LITTERAUX = [
    ("RESCOS-5_", "Hb <7 g/dL", "Hb <70 g/L",
     "hemoglobine, seuil transfusionnel — g/dL -> g/L, x10"),
    ("RESCOS-14_", "Hb < 10.5 g/dL", "Hb < 105 g/L",
     "hemoglobine, critere de colite aigue severe — g/dL -> g/L, x10"),
    ("RESCOS-9b", "hyperleucocytose (> 12 000/mm³)", "hyperleucocytose (> 12 G/L)",
     "leucocytes — /mm³ -> G/L, x0,001 ; la grille ecrit deja « > 12 G/L » ailleurs"),
    ("RESCOS-36_", "objectif LDL < 70 mg/dL, voire < 55 mg/dL si haut risque",
     "objectif LDL < 1.8 mmol/L, voire < 1.4 mmol/L si haut risque",
     "LDL cholesterol — mg/dL -> mmol/L, /38,67 ; DEUX seuils sur la ligne"),
    ("RESCOS-37_", "objectif LDL < 70 mg/dL, voire < 55 mg/dL si haut risque",
     "objectif LDL < 1.8 mmol/L, voire < 1.4 mmol/L si haut risque",
     "LDL cholesterol — mg/dL -> mmol/L, /38,67 ; DEUX seuils sur la ligne"),
    ("RESCOS-3_", "plaquettes 422)", "plaquettes 422 G/L)",
     "numeration plaquettaire en unite implicite ; la meme grille ecrit "
     "« plaquettes 422 G/L » dans la reponse du patient"),
]

# Segments a ne jamais toucher : les URI de donnees base64.
# `\bNFS\b` PEUT tomber dans un blob : l'alphabet base64 contient « + », « / »
# et « = », qui sont des frontieres de mot. Le decoupage n'est pas une
# precaution de principe.
DATAURI = re.compile(r'data:image[^"]*')


def _outside_chunks(html):
    """Decoupe (kind, texte) : 'uri' pour les data-URI, 'text' pour le reste."""
    chunks = []
    last = 0
    for m in DATAURI.finditer(html):
        chunks.append(("text", html[last:m.start()]))
        chunks.append(("uri", m.group(0)))
        last = m.end()
    chunks.append(("text", html[last:]))
    return chunks


def apply_to(html, name):
    """Applique les regles hors base64. Retourne (html, compte_par_libelle)."""
    counts = {}
    out = []
    for kind, chunk in _outside_chunks(html):
        if kind == "uri":
            out.append(chunk)
            continue
        for pattern, repl, _ in GLOBAL:
            chunk, n = re.subn(pattern, repl, chunk)
            counts[pattern] = counts.get(pattern, 0) + n
        for grid, old, new, _ in LITTERAUX:
            if grid not in name:
                continue
            n = chunk.count(old)
            if n:
                chunk = chunk.replace(old, new)
                # Cle (grille, texte) et non texte seul : deux grilles portent
                # la MEME clause LDL, un compteur par texte les additionnerait
                # et le controle « exactement 1 » deviendrait faux.
                counts[(grid, old)] = counts.get((grid, old), 0) + n
        out.append(chunk)
    return "".join(out), counts


def main():
    dry = "--dry-run" in sys.argv[1:]
    total = {}
    touched = 0
    for path in lib.grids():
        html = path.read_text(encoding="utf-8")
        new, counts = apply_to(html, path.name)
        for key, n in counts.items():
            total[key] = total.get(key, 0) + n
        if new != html:
            if not dry:
                path.write_text(new, encoding="utf-8")
            touched += 1
            detail = ", ".join(
                f"{n}x {k[1] if isinstance(k, tuple) else k}"
                for k, n in counts.items() if n)
            print(f"  {path.name}: {detail}")

    print(f"\n{touched} grille(s) modifiee(s)" + (" (DRY-RUN)" if dry else ""))
    for pattern, repl, comment in GLOBAL:
        print(f"  {total.get(pattern, 0):4d}x {pattern} -> {repl}   ({comment})")
    for grid, old, new, comment in LITTERAUX:
        n = total.get((grid, old), 0)
        flag = "" if n == 1 else "   ⚠ ATTENDU 1"
        print(f"  {n:4d}x {grid} {old!r} -> {new!r}{flag}")
        print(f"        {comment}")
    bad = [old for grid, old, _, _ in LITTERAUX if total.get((grid, old), 0) != 1]
    if bad:
        print(f"\nECHEC — {len(bad)} litteral(aux) non trouve(s) exactement une fois")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
