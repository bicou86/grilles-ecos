"""Passe nomenclature suisse sur les 88 grilles German.

Pendant de `scripts/amboss/apply_lab_nomenclature.py`, dont il reprend le
principe — substitution 1 pour 1, HORS zones base64 — et dont il ne partage
volontairement pas le code : les regles ne sont pas les memes (le corpus German
ne porte ni `CBC`, ni `BMP`, ni `911`, ni `SAMU`) et le fichier AMBOSS a produit
les mesures publiees, il ne doit plus bouger.

Deux familles de regles, deliberement separees :

* RULES — substitutions de terme, sans arithmetique. Le nombre ne change pas,
  seul le sigle change. Aucune ne touche a un sous-item note : le bareme est
  preserve par construction.
* CONVERSIONS — conversions d'UNITE, qui recalculent la valeur. Chacune est
  ecrite en toutes lettres, avec son facteur et le compte attendu : une
  conversion silencieuse qui s'appliquerait 0 ou 3 fois au lieu de 1 serait un
  seuil faux, pas une coquille. Le script echoue si le compte diverge.

PIEGE DEJA RENCONTRE SUR AMBOSS — plusieurs valeurs dans la meme unite sur une
seule ligne (« Hb < 7 g/dL (< 9 si coronarien) », « B12 : 85 pg/mL (N: 200-900) »).
Une conversion qui ne traiterait que la premiere laisserait un seuil faux a cote
d'un seuil juste. Les CONVERSIONS portent donc sur la LIGNE ENTIERE et non sur
le seul nombre, et le controle de compte impose de les avoir toutes vues.

VERIFIE AVANT ECRITURE (0 occurrence sur les 88 grilles) : aucun terme substitue
ne se trouve dans un attribut `data-criteria` ni dans un `.criteria-text`, dont
`cases/scoring.js:159` decoupe le texte (`split(". ")[1].split(" [")[0]`).
"""
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import lib_german as lib

# (motif, remplacement, commentaire) — substitution de terme, valeur inchangee.
RULES = [
    (r"\bNFS\b", "FSC", "numeration formule sanguine -> formule sanguine complete"),
]
# Volontairement absentes : CBC, BMP, 911, SAMU, Vicodin, Tylenol, Tums,
# g/dL, ng/mL, /mm³, /µL. Le corpus German n'en porte aucune occurrence
# (mesure : `check_nomenclature.py` ne signale que NFS et pg/mL). Ajouter une
# regle sans occurrence, c'est ajouter un risque sans contrepartie.
# Volontairement absente aussi : 112. Meme raison qu'AMBOSS — la seule graphie
# de ce nombre dans un corpus de grilles est un TOTAL DE BAREME (« Score Global
# 0/112 »), jamais un numero d'urgence.

# (texte exact, remplacement, compte attendu, commentaire).
# Ligne entiere, jamais le seul nombre : voir l'entete.
CONVERSIONS = [
    ("Dosage œstradiol (< 50 pg/mL)",
     "Dosage œstradiol (< 184 pmol/L)", 1,
     "German-63, menopause : oestradiol pg/mL -> pmol/L, x3,671 "
     "(50 x 3,671 = 183,55 -> 184). Le qualificatif voisin est le sens de "
     "l'inegalite : « < 50 pg/mL » et « < 184 pmol/L » decrivent le meme seuil, "
     "le « < » reste exact. Le critere voisin « Dosage FSH (> 30 UI/L) » est "
     "deja en unite suisse et n'est pas touche."),
]

DATAURI = re.compile(r'data:image[^"]*')


def apply_to(html):
    """Applique regles et conversions hors base64. Rend (html, comptes)."""
    chunks = []
    last = 0
    counts = {p: 0 for p, _, _ in RULES}
    counts.update({t: 0 for t, _, _, _ in CONVERSIONS})
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
        for text, repl, _, _ in CONVERSIONS:
            n = chunk.count(text)
            if n:
                chunk = chunk.replace(text, repl)
                counts[text] += n
        for pattern, repl, _ in RULES:
            chunk, n = re.subn(pattern, repl, chunk)
            counts[pattern] += n
        out.append(chunk)
    return "".join(out), counts


def main():
    total = {p: 0 for p, _, _ in RULES}
    total.update({t: 0 for t, _, _, _ in CONVERSIONS})
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
        print(f"  {total[pattern]:3}x  {pattern} -> {repl}   ({note})")
    status = 0
    for text, repl, expected, note in CONVERSIONS:
        got = total[text]
        flag = "" if got == expected else f"  <-- ATTENDU {expected}"
        print(f"  {got:3}x  {text} -> {repl}{flag}\n       {note}")
        if got != expected:
            status = 1
    if status:
        print("\nECHEC — une conversion d'unite ne s'est pas appliquee "
              "le nombre de fois attendu ; verifier avant de commiter.")
    return status


if __name__ == "__main__":
    sys.exit(main())
