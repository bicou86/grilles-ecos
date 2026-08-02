"""Mesure les defauts d'import du corpus rescos-locales. RAPPORT, sortie toujours 0.

Usage :
    python3 scripts/rescos-locales/report_import_defects.py [GRILLE_FILTRE] [--quiet]
    python3 scripts/rescos-locales/report_import_defects.py --corpus  # les 4 corpus

Ce script MESURE, il ne corrige rien et ne bloque rien.

POURQUOI LES MOTIFS SONT DEFINIS ICI ET NON IMPORTES
=====================================================
Les volets RESCOS et CasECOS importaient les sept familles de
`scripts/german/report_import_defects.py`. Ce volet ne le peut pas : son mandat
lui interdit d'ecrire, de lire ou d'importer quoi que ce soit sous
`scripts/german/`, ou l'utilisateur travaille en parallele. Les familles sont
donc RECONSTRUITES ici, et calibrees — la ou une cible existe — sur les chiffres
PUBLIES du corpus AMBOSS, qui sert de temoin :

    famille                    cible AMBOSS   obtenu ici
    plage-coupee                    0 / 0        0 / 0   exact
    troncature-x-fragment           1 / 1        1 / 1   exact
    chevron-nu                    144 / 35     144 / 35  exact
    chevron-nu-colle-lettre         0 / 0        0 / 0   exact
    troncature-x-molecule           5 / 5       24 / 15  RECONSTRUCTION
    comparaison-manquante          17 / 13      29 / 20  RECONSTRUCTION

Les quatre premieres familles reproduisent le chiffre publie AU CHIFFRE PRES :
leurs signatures sont exactes (`500-: 1000 mg`, `: xicilline`, un chevron suivi
d'un nombre), il n'y a pas de latitude d'ecriture. Les deux dernieres sont des
HEURISTIQUES ; ma reconstruction est plus large que l'originale et rend donc
davantage. Elle n'est PAS comparable aux chiffres publies par les volets
precedents, et ce script ne les cite pas comme s'ils l'etaient.

Cela ne coute rien a l'usage, parce que ces deux familles sont documentees comme
ne produisant QUE des faux positifs hors d'AMBOSS (posologies correctes, «
Cilostazol : 100mg x2/j » ; constantes mesurees, « BMI a 32.5 kg/m² »). Ce qu'on
leur demande est un signal d'ABSENCE, pas un compte. Une reconstruction plus
large rend ce signal plus severe, jamais plus indulgent.

Toutes les recherches passent par `strip_base64` et travaillent sur le HTML
BRUT, jamais sur `visible_text()` : c'est la seule methode qui ne peut etre
trompee ni par un blob d'image ni par un chevron nu.

Le septieme defaut d'AMBOSS — « chaines d'examens copiees sur le mauvais
diagnostic » — n'est PAS mecanisable et se verifie a la lecture.


RELEVE INITIAL — rescos-locales ne porte AUCUN des defauts durs
================================================================
Mesure de ce script, meme motifs, sur les quatre corpus :

                            AMBOSS     German     RESCOS   rescos-locales
  plage-coupee               0 / 0      0 / 0      0 / 0      0 / 0
  troncature-x-fragment      1 / 1      0 / 0      0 / 0      2 / 2    faux
  troncature-x-molecule     24 / 15     0 / 0      8 / 5     15 / 9    faux
  chevron-nu               144 / 35    27 / 20    88 / 29   787 / 156
  chevron-nu-colle-lettre    0 / 0      0 / 0      0 / 0      0 / 0
  comparaison-manquante     29 / 20     5 / 4     15 / 7     53 / 28   faux
  numeration-implicite       0 / 0      0 / 0      0 / 0      8 / 6   A RELIRE

Les DEUX SIGNATURES EXACTES de la moulinette d'AMBOSS — `plage-coupee` et
`troncature-x-fragment` — sont a ZERO. Ce corpus n'a pas subi cet import, pas
plus que German, RESCOS ou CasECOS.

`troncature-x-fragment` : 2 occurrences, TOUTES FAUSSES — « … : xanthochromie
apres 12h » et « PL: xanthochromie pathognomonique d'HSA ». Un mot francais qui
commence par un `x` derriere un « : », comme les « xanthomes » de CasECOS.
Aucun `: xicilline`, aucun `: xone`.

`chevron-nu` : 787 occurrences. Ce n'est PAS un defaut de contenu mais le PIEGE
D'OUTILLAGE du § 1 d'AMBOSS : ce sont des seuils legitimes (`Hb < 70 g/L`,
`FE < 40 %`, `< 3 sang/semaine`) qu'un `re.sub(r'<[^>]+>', ...)` naif avalerait
avec la clause qui les suit. Le `visible_text()` importe de `lib_amboss` les
traite correctement. Le sous-cas RESIDUEL non traitable (un `<` colle a une
lettre, indiscernable d'une vraie balise) est a ZERO.

`numeration-implicite` : 8 occurrences sur 6 grilles, les SEULES a relire — et
le seul defaut reel du corpus. Six sont vraies : « plaquettes > 50 000 »
(AMC Urgences 1), « GB 18000 » et « plaquettes si < 20000 » (AMC Urgences 2B),
« thrombopenie < 50 000 » (AMC Urgences 5C), « GB 8000 » deux fois (« Enfant qui
boite »). Deux sont fausses : « 1 GB pour 500-1000 GR » (rapport de LCR, pas une
numeration) et une capture tardive dans une ligne ou l'unite est presente
(RESCOS-58b, « plaquettes 450 G/L (N: 150-400) »).
"""
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import lib_rescos_locales as lib

# --- les familles ----------------------------------------------------------
#
# 1. `plage-coupee` — signature EXACTE de la moulinette d'AMBOSS : une plage de
#    posologie dont le tiret (ou le point) a ete suivi d'un « : » parasite,
#    « 500-: 1000 mg », « 0.: 4 mg ». Aucune latitude d'ecriture.
_PLAGE_COUPEE = r"\d\s*[-.]\s*:\s*\d"

# 2. `troncature-x-fragment` — l'autre signature EXACTE : un mot coupe en deux
#    dont la seconde moitie, commencant par un `x`, se retrouve derriere un
#    « : » (« Amoxicilline » -> « … : xicilline »). Le motif attrape aussi les
#    vrais mots francais en `x-` (« : xanthomes ») : c'est un faux positif
#    reconnaissable a la lecture, et il vaut mieux qu'un silence.
_TRONCATURE_X_FRAGMENT = r":\s+x[a-zà-ÿ]{3,}"

# 3. `troncature-x-molecule` — HEURISTIQUE (voir l'entete) : un nom de molecule
#    capitalise, un « : », une dose. Le defaut d'origine coupait la posologie au
#    « x » de « x3/j ».
_TRONCATURE_X_MOLECULE = (
    r"\b[A-ZÀ-Ý][a-zà-ÿ]{3,}\s*:\s*\d+\s?(?:mg|g|µg|mcg|UI|mL)\b")

# 4. `chevron-nu` — un `<` suivi d'un nombre (avec un `=` optionnel). Reproduit
#    le chiffre publie d'AMBOSS (144/35) et de RESCOS (88/29) au chiffre pres.
#    Ce n'est pas un defaut : c'est l'inventaire de ce qu'un `<[^>]+>` naif
#    detruirait.
_CHEVRON_NU = r"<\s*[=]?\s*\d"

# 5. `chevron-nu-colle-lettre` — le sous-cas RESIDUEL, indiscernable d'une vraie
#    balise : un `<` colle a une lettre qui n'ouvre aucune balise HTML connue.
#    C'est le seul cas que `visible_text()` ne peut pas sauver. Doit rester a
#    zero : une occurrence signifierait qu'un fragment de texte est perdu a
#    l'affichage.
_HTML_TAGS = (
    "a|abbr|b|body|br|button|canvas|caption|code|col|colgroup|dd|div|dl|dt|em|"
    "embed|fieldset|figcaption|figure|footer|form|h1|h2|h3|h4|h5|h6|head|header|"
    "hr|html|i|iframe|img|input|label|legend|li|link|main|mark|meta|nav|noscript|"
    "ol|optgroup|option|p|param|picture|pre|progress|q|script|section|select|"
    "small|source|span|strong|style|sub|summary|sup|svg|table|tbody|td|template|"
    "textarea|tfoot|th|thead|title|tr|u|ul|video|wbr")
_CHEVRON_NU_COLLE = r"</?(?!(?:%s)\b)[a-zA-Z][a-zA-Z0-9]*[^a-zA-Z0-9>]" % _HTML_TAGS

# 6. `comparaison-manquante` — HEURISTIQUE (voir l'entete) : un terme de
#    laboratoire ou de constante suivi directement d'une valeur et de son unite,
#    sans operateur de comparaison. Tres majoritairement FAUX : une constante
#    MESUREE s'ecrit bien « SpO2 94 % ». A relire, jamais a corriger en masse.
_LAB_TERM = (
    r"(?:Hb|h[ée]moglobine|CRP|VS|cr[ée]atinine|leucocytes?|plaquettes?|"
    r"glyc[ée]mie|troponine|D-dim[èe]res?|TSH|SpO2|SpO₂|FC|TA|temp[ée]rature|"
    r"T°|BMI|IMC|PaO2|pH|lactates?|INR|ur[ée]e|bilirubine|ASAT|ALAT|GGT)")
_UNIT = (r"(?:g/L|G/L|mg/L|mmol/L|µmol/L|umol/L|ng/mL|kg/m|%|°C|/min|mmHg|UI/L|U/L)")
_COMPARAISON_MANQUANTE = _LAB_TERM + r"\s+(?:\d[\d.,]*)\s*" + _UNIT

# 7. `numeration-implicite` — une numeration d'hemogramme sans unite
#    (« plaquettes 422 » se lit 422 G/L). Motif borde comme dans RESCOS : seuil
#    `\d{3,}` et non `\d{2,}` (a deux chiffres il coupe « 12 000/mm³ » en deux),
#    garde-fou d'ANNEE (« plaquettes en 2019 »), et lookahead negatif sur une
#    liste d'unites large — chaque unite manquante est un faux positif.
_HEMO = (
    r"(?:hyperleucocytoses?|hypoleucocytoses?|leucocytoses?|leucop[ée]nies?|leucocytes?"
    r"|globules?\s+blancs?|\bGB\b|polynucl[ée]aires?|neutrophiles?|\bPNN\b|granulocytes?"
    r"|lymphocytes?|lymphop[ée]nies?|[ée]osinophiles?|[ée]osinophilies?|monocytes?"
    r"|basophiles?|thrombop[ée]nies?|thrombocytoses?|thrombocytes?|plaquettes?|\bPLT\b)")
_NUM_UNITS = (
    r"(?:G/L|g/L|G/l|g/l|/mm|/\s?[µμ]L|%|10|mg|µg|mcg|ng|pg|mmol|µmol|umol|U/L|UI"
    r"|kg|cm|mm|ml|mL|bpm|°|/j|/h|ans?\b|mois\b|min\b|jours?\b|semaines?\b)")
_NUMERATION_IMPLICITE = (
    _HEMO
    + r"(?:[^<\n]|<(?![a-zA-Z/])){0,25}?\s(?!(?:19|20)\d\d\b)(\d{3,}(?:[  ]\d{3})?)"
    + r"(?![\d.,]*\s*" + _NUM_UNITS + r")")

FAMILIES = [
    ("plage-coupee", re.compile(_PLAGE_COUPEE)),
    ("troncature-x-fragment", re.compile(_TRONCATURE_X_FRAGMENT)),
    ("troncature-x-molecule", re.compile(_TRONCATURE_X_MOLECULE)),
    ("chevron-nu", re.compile(_CHEVRON_NU)),
    ("chevron-nu-colle-lettre", re.compile(_CHEVRON_NU_COLLE)),
    ("comparaison-manquante", re.compile(_COMPARAISON_MANQUANTE)),
    ("numeration-implicite", re.compile(_NUMERATION_IMPLICITE)),
]

# Les quatre corpus, pour `--corpus`. Le bordage des motifs se fait sur les
# quatre, jamais sur le seul corpus traite : `VRE` vaut « volume de reserve
# expiratoire » dans l'un, `QID` vaut « quadrant inferieur droit » dans l'un et
# « quater in die » dans l'autre. Un motif qui n'a ete vu que sur un corpus n'a
# pas ete borde.
_CASES = Path(__file__).resolve().parents[2] / "cases"
CORPORA = [
    ("AMBOSS", sorted((_CASES / "amboss").glob("AMBOSS-*.html"))),
    ("German", sorted((_CASES / "german").glob("German-*.html"))),
    ("RESCOS", sorted((_CASES / "rescos").glob("RESCOS-*.html"))),
    ("rescos-locales", None),  # rempli a l'appel, via lib.grids()
]


def scan(paths):
    """(totaux, grilles touchees, echantillons) pour une liste de fichiers."""
    totals, hit, samples = Counter(), defaultdict(set), defaultdict(list)
    for path in paths:
        html = lib.strip_base64(path.read_text(encoding="utf-8"))
        for name, pattern in FAMILIES:
            for m in pattern.finditer(html):
                totals[name] += 1
                hit[name].add(path.name)
                if len(samples[name]) < 400:
                    ctx = re.sub(r"\s+", " ", html[max(0, m.start() - 55):m.end() + 45])
                    samples[name].append(f"{path.name[:40]:<40} …{ctx}…")
    return totals, hit, samples


def main():
    args = sys.argv[1:]
    quiet = "--quiet" in args
    positional = [a for a in args if not a.startswith("--")]
    only = positional[0] if positional else None

    if "--corpus" in args:
        rows = []
        for label, paths in CORPORA:
            paths = lib.grids() if paths is None else paths
            totals, hit, _ = scan(paths)
            rows.append((label, len(paths), totals, hit))
        width = max(len(r[0]) for r in rows) + 2
        print("famille".ljust(26) + "".join(f"{r[0]} ({r[1]})".ljust(width + 8) for r in rows))
        for name, _ in FAMILIES:
            cells = "".join(f"{t[name]} / {len(h[name])}".ljust(width + 8)
                            for _, _, t, h in rows)
            print(name.ljust(26) + cells)
        print("\nRAPPORT — aucune correction appliquee, sortie 0.")
        return 0

    paths = [p for p in lib.grids() if not only or only in p.name]
    totals, hit, samples = scan(paths)
    for name, _ in FAMILIES:
        print(f"\n=== {name} : {totals[name]} occurrence(s) / "
              f"{len(hit[name])} grille(s) ===")
        if quiet:
            continue
        for line in samples[name][:60]:
            print("  " + line)
        if len(samples[name]) > 60:
            print(f"  … et {totals[name] - 60} autre(s)")

    print("\n--- recapitulatif ---")
    for name, _ in FAMILIES:
        print(f"  {totals[name]:6d} occ / {len(hit[name]):3d} grilles   {name}")
    print("\nRAPPORT — aucune correction appliquee, sortie 0.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
