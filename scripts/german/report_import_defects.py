"""Mesure les defauts d'import du corpus German. RAPPORT, sortie toujours 0.

Usage :
    python3 scripts/german/report_import_defects.py [GRILLE_FILTRE] [--quiet]

Ce script MESURE, il ne corrige rien et ne bloque rien. Il rejoue sur les 88
grilles German les cinq familles de defauts identifiees sur AMBOSS (voir
`docs/superpowers/rapport-amboss-2026-08.md` § 4 et
`docs/superpowers/arbitrages-amboss-2026-08.md` groupe 2), pour savoir si le
corpus German les porte aussi, et en quelle quantite.

Toutes les recherches passent par `strip_base64` et travaillent sur le HTML
BRUT, jamais sur `visible_text()` : c'est la seule methode qui ne peut etre
trompee ni par un blob d'image (l'alphabet base64 fait apparaitre par hasard
n'importe quelle courte sequence alphanumerique) ni par un chevron nu.

LES CINQ FAMILLES
-----------------
1. `troncature-x` — l'import coupe les mots a la lettre `x` et absorbe les
   lettres suivantes jusqu'au chiffre, en laissant un « : » parasite :
   `Ceftria|xone`, `Amo|xicilline`, `Ma|ximum`. Deux signatures sures : un
   fragment orphelin commencant par `x` juste apres un `:`, et un mot capitalise
   suivi de `:` puis d'une dose.
2. `plage-coupee` — le meme mecanisme sur une plage ou une decimale :
   `500-: 1000 mg`, `0.: 4 mg`. Signature sure et sans faux positif connu.
3. `comparaison-manquante` — le signe `<`/`>`/`≤`/`≥` manque devant un seuil :
   `SpO2 92%`, `IMC 25 kg/m²`. Le sens s'inverse selon le signe.
4. `chevron-nu` — un `<` de seuil, non balise. Ce n'est pas un defaut du
   contenu mais un piege d'outillage : tout controle fonde sur un
   `re.sub(r'<[^>]+>', ...)` naif avale la clause suivante. On mesure aussi le
   sous-cas RESIDUEL non traitable : un `<` colle a une lettre, indiscernable
   d'une vraie balise.
5. `numeration-implicite` — une numeration sanguine sans unite, qui sous-entend
   le `/mm³` et doit se lire en `G/L`. Aucun motif d'unite ne peut l'attraper :
   « GB 8500 » ne contient rien a detecter. Le balayage est ici volontairement
   large (tout nombre >= 100 apres un terme d'hemogramme, sans unite derriere) —
   le seuil >= 1000 avait laisse passer « eosinophiles > 300 » sur AMBOSS-19.

Chaque famille est rendue avec ses occurrences pour relecture humaine : les
familles 3 et 5 sont heuristiques et produisent des faux positifs par
construction, les familles 1, 2 et 4 sont exactes.
"""
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import lib_german as lib

# Balises reellement employees par le corpus — sert a distinguer un vrai `<`
# de balise d'un chevron nu colle a une lettre.
KNOWN_TAGS = (r"html|head|body|meta|title|link|script|style|div|span|p|br|hr|h[1-6]|"
              r"ul|ol|li|table|thead|tbody|tr|td|th|strong|em|b|i|u|a|img|input|"
              r"label|button|textarea|select|option|form|svg|path|g|circle|rect|"
              r"line|text|defs|marker|polygon|polyline|small|sub|sup|nav|section|"
              r"header|footer|main|article|aside|figure|figcaption|canvas|iframe|"
              r"tspan|ellipse|use|symbol|pre|code|dl|dt|dd|caption|colgroup|col|"
              r"noscript|template|source|picture|video|audio|DOCTYPE")

HEMO = (r"leucocytes?|[ée]osinophiles?|neutrophiles?|lymphocytes?|monocytes?|"
        r"basophiles?|plaquettes?|thrombocytes?|globules?\s+blancs?|\bGB\b|\bPNN\b")

# Mots-cles de seuil : un nombre qui les suit sans operateur est suspect.
SEUIL = (r"SpO2|SpO₂|IMC|BMI|INR|st[ée]nose|r[ée]sidu|perte\s+de\s+poids|"
         r"perte\s+pond[ée]rale|fraction\s+d[e']\s?[ée]jection|FEVG|"
         r"temp[ée]rature|f[ièe]vre|TA[Ss]?|PAS|PAD|glyc[ée]mie|cr[ée]atinine")

FAMILIES = [
    ("plage-coupee",
     re.compile(r"[^\W\d_]?\d+\s*[-.]\s*:\s*\d")),
    ("troncature-x-fragment",
     re.compile(r":\s*x[a-zA-Zéèêàçï]{2,}")),
    ("troncature-x-molecule",
     re.compile(r"(?<![\w>])[A-ZÉÈ][a-zéèêàç]{1,9}\s*:\s*\d+\s*(?:g|mg|µg|mcg|UI|ml|mL)\b")),
    ("chevron-nu",
     re.compile(r"<\s*[\d≥≤=]")),
    ("chevron-nu-colle-lettre",
     re.compile(r"</?(?!(?:" + KNOWN_TAGS + r")\b)[a-zA-Z]")),
    ("comparaison-manquante",
     re.compile(r"(?:" + SEUIL + r")[^<>=≥≤\n]{0,12}?\s\d+([.,]\d+)?\s*(?:%|kg/m|cm|mm|h\b|ans\b|°)")),
    # Le « gap » accepte un CHEVRON NU (`leucocytes < 4000`, `eosinophiles > 300`)
    # mais pas une vraie balise : sans cette nuance, le cas meme qui a coute le
    # plus cher sur AMBOSS-19 — « eosinophiles > 300 », un seuil signe mais sans
    # unite — echappait au motif.
    ("numeration-implicite",
     re.compile(r"(?:" + HEMO + r")(?:[^<\n]|<(?![a-zA-Z/])){0,25}?\s"
                r"(\d{3,}(?:[  ]\d{3})?)(?![\d.,]*\s*(?:G/L|g/L|/mm|/[µμ]L|%|10))")),
]


def main():
    args = sys.argv[1:]
    quiet = "--quiet" in args
    positional = [a for a in args if not a.startswith("--")]
    only = positional[0] if positional else None

    totals = Counter()
    grids_hit = defaultdict(set)
    samples = defaultdict(list)

    for path in lib.grids():
        if only and only not in path.name:
            continue
        html = lib.strip_base64(path.read_text(encoding="utf-8"))
        for name, pattern in FAMILIES:
            for m in pattern.finditer(html):
                totals[name] += 1
                grids_hit[name].add(path.name)
                if len(samples[name]) < 400:
                    ctx = re.sub(r"\s+", " ", html[max(0, m.start() - 55):m.end() + 45])
                    samples[name].append(f"{path.name[:34]:<34} …{ctx}…")

    for name, _ in FAMILIES:
        print(f"\n=== {name} : {totals[name]} occurrence(s) / "
              f"{len(grids_hit[name])} grille(s) ===")
        if quiet:
            continue
        for line in samples[name][:60]:
            print("  " + line)
        if len(samples[name]) > 60:
            print(f"  … et {totals[name] - 60} autre(s)")

    print("\n--- recapitulatif ---")
    for name, _ in FAMILIES:
        print(f"  {totals[name]:6d} occ / {len(grids_hit[name]):2d} grilles   {name}")
    print("\nRAPPORT — aucune correction appliquee, sortie 0.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
