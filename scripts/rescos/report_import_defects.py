"""Mesure les defauts d'import du corpus RESCOS. RAPPORT, sortie toujours 0.

Usage :
    python3 scripts/rescos/report_import_defects.py [GRILLE_FILTRE] [--quiet]

Ce script MESURE, il ne corrige rien et ne bloque rien. Les sept familles de
motifs sont celles de `scripts/german/report_import_defects.py`, importees et
non recopiees : elles decrivent des defauts d'IMPORT (une moulinette qui a
casse des mots, des seuils et des plages), pas un corpus, et elles ont ete
etablies sur AMBOSS puis rejouees sur German. Les redefinir ici garantirait
qu'un affinage futur ne profite qu'a un corpus.

Toutes les recherches passent par `strip_base64` et travaillent sur le HTML
BRUT, jamais sur `visible_text()` : c'est la seule methode qui ne peut etre
trompee ni par un blob d'image ni par un chevron nu.

RELEVE INITIAL RESCOS — le corpus ne porte AUCUN des trois defauts durs
-----------------------------------------------------------------------
                              AMBOSS      German      RESCOS
  plage-coupee                  0 / 0       0 / 0       0 / 0
  troncature-x-fragment         1 / 1       0 / 0       0 / 0
  troncature-x-molecule         5 / 5       0 / 0       2 / 2   (faux positifs)
  chevron-nu                  144 / 35     27 / 20    114 / 30
  chevron-nu-colle-lettre       0 / 0       0 / 0       0 / 0
  comparaison-manquante        17 / 13      2 / 2      13 / 9   (faux positifs)
  numeration-implicite          0 / 0       0 / 0       1 / 1

Lecture :

* `plage-coupee` et `troncature-x-fragment` — les deux signatures EXACTES du
  defaut d'import d'AMBOSS (`Amo|xicilline`, `500-: 1000 mg`) : ZERO. Le corpus
  RESCOS n'a pas subi cette moulinette. Comme German.
* `troncature-x-molecule` — 2 occurrences, toutes deux FAUSSES : « Cilostazol :
  100mg x2/j » et « Duloxétine : 60mg/j » sont des posologies correctement
  ecrites, que le motif attrape parce qu'il cherche un mot capitalise suivi de
  « : » puis d'une dose. Rien a corriger.
* `chevron-nu` — 114 occurrences. Ce n'est PAS un defaut du contenu mais un
  piege d'outillage : ce sont des seuils legitimes (`Hb < 10.5 g/dL`,
  `< 3 selles/semaine`). Ils ne comptent que parce que tout controle fonde sur
  un `re.sub(r'<[^>]+>', ...)` naif avalerait la clause qui suit. Le
  `visible_text()` importe de `lib_amboss` les traite correctement. Le sous-cas
  RESIDUEL non traitable (un `<` colle a une lettre, indiscernable d'une vraie
  balise) est a zero.
* `comparaison-manquante` — 13 occurrences, heuristiques et tres majoritairement
  FAUSSES : « BMI à 32.5 kg/m² », « SpO₂ 99 % », « T° 37,3 °C » sont des
  constantes MESUREES, correctement ecrites sans operateur. A relire une par
  une, pas a corriger en masse.
* `numeration-implicite` — 1 occurrence, celle-la REELLE : « VS 55, CRP 32,
  Hb 113, plaquettes 422 » — la numeration plaquettaire y est en unite
  implicite et doit se lire 422 G/L.

Conclusion : sur les six defauts d'import d'AMBOSS, RESCOS n'en porte
structurellement aucun, a l'exception d'UNE numeration en unite implicite. Le
septieme (« examens copies sur le mauvais diagnostic ») n'est pas mecanisable
et se verifie a la lecture — voir PROCEDURE-rescos.md § Import.
"""
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import lib_rescos as lib

_GERMAN_DIR = Path(__file__).resolve().parents[1] / "german"


def _german_families():
    """Les sept familles de motifs de `scripts/german/report_import_defects.py`.

    Chargement par chemin explicite, sous un alias propre a rescos : les trois
    dossiers de corpus portent un script de ce nom, et un import ordinaire
    resoudrait selon l'ordre du chemin. Le module German importe lui-meme
    `lib_german`, ce qui est sans effet de bord ici — aucun fichier n'est lu au
    chargement.
    """
    import importlib.util
    path = _GERMAN_DIR / "report_import_defects.py"
    spec = importlib.util.spec_from_file_location("_rescos_german_defects", path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    sys.path.append(str(_GERMAN_DIR))
    spec.loader.exec_module(module)
    return module.FAMILIES


FAMILIES = _german_families()


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
