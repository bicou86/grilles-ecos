"""Mesure les defauts d'import du corpus CasECOS. RAPPORT, sortie toujours 0.

Usage :
    python3 scripts/casecos/report_import_defects.py [GRILLE_FILTRE] [--quiet]

Ce script MESURE, il ne corrige rien et ne bloque rien. Les sept familles de
motifs sont celles de `scripts/german/report_import_defects.py`, importees et
non recopiees : elles decrivent des defauts d'IMPORT (une moulinette qui a
casse des mots, des seuils et des plages), pas un corpus, et elles ont ete
etablies sur AMBOSS puis rejouees sur German et RESCOS. Les redefinir ici
garantirait qu'un affinage futur ne profite qu'a un corpus.

Le fichier German est lu, jamais ecrit, et la mesure ci-dessous a ete prise a un
etat donne de ce fichier — si ses familles changent, les chiffres CasECOS
changeront aussi, et c'est le comportement voulu : les quatre corpus doivent
rester comparables.

Toutes les recherches passent par `strip_base64` et travaillent sur le HTML
BRUT, jamais sur `visible_text()` : c'est la seule methode qui ne peut etre
trompee ni par un blob d'image ni par un chevron nu. (CasECOS ne contient
d'ailleurs AUCUN data-URI : 0 grille sur 198.)

RELEVE INITIAL CasECOS — le corpus ne porte AUCUN des trois defauts durs
------------------------------------------------------------------------
                              AMBOSS      German      RESCOS     CasECOS
  plage-coupee                  0 / 0       0 / 0       0 / 0       0 / 0
  troncature-x-fragment         1 / 1       0 / 0       0 / 0       2 / 2
  troncature-x-molecule         5 / 5       0 / 0       2 / 2       5 / 4
  chevron-nu                  144 / 35     27 / 20     88 / 29    2414 /198
  chevron-nu-colle-lettre       0 / 0       0 / 0       0 / 0       0 / 0
  comparaison-manquante        17 / 13      2 / 2      12 / 9     128 / 56
  numeration-implicite          0 / 0       0 / 0       0 / 0      26 / 18

Lecture :

* `plage-coupee` — la signature EXACTE et sans faux positif connu du defaut
  d'import d'AMBOSS (`500-: 1000 mg`, `0.: 4 mg`) : ZERO. Le corpus CasECOS
  n'a pas subi cette moulinette. Comme German, comme RESCOS.
* `troncature-x-fragment` — 2 occurrences, les DEUX fausses : « xanthomes,
  xanthélasma » et « xanthine (xanthinurie) ». Le motif cherche un fragment
  commencant par `x` juste apres un « : » ; il rencontre ici deux mots
  francais qui commencent legitimement par cette lettre. Aucun `: xicilline`,
  aucun `: xone` : la signature d'AMBOSS est absente.
* `troncature-x-molecule` — 5 occurrences, toutes FAUSSES : ce sont des
  posologies correctement ecrites (« Dose : 1 mg/kg/j », « Dose : 60 mg PO
  q4h »), que le motif attrape parce qu'il cherche un mot capitalise suivi de
  « : » puis d'une dose.
* `chevron-nu` — 2414 occurrences sur les 198 grilles, un ordre de grandeur
  au-dessus des trois autres corpus. Ce n'est PAS un defaut du contenu mais un
  piege d'outillage : ce sont des seuils legitimes (`Hb < 70 g/L`, `FE <40%`,
  `< 90 min`). Ils ne comptent que parce que tout controle fonde sur un
  `re.sub(r'<[^>]+>', ...)` naif avalerait la clause qui suit.

  SUR CE CORPUS, LE PIEGE S'EST REFERME UN ETAGE PLUS BAS QUE PREVU : le motif
  de balise `<(/?)(\\w+)([^>]*)>` employe par l'EQUILIBRAGE DE `<div>` de
  `lib_german` et `lib_rescos` reconnait « (T1a) <2 cm, ... </div> » comme une
  balise nommee « 2 » et avale la fermeture. 244 imbrications fantomes et 9
  blocs emballes jusqu'a la fin du fichier. `lib_casecos._TAG` porte le
  correctif ; voir son entete.
* `chevron-nu-colle-lettre` — le sous-cas RESIDUEL non traitable (un `<` colle
  a une lettre, indiscernable d'une vraie balise) est a ZERO, comme partout.
* `comparaison-manquante` — 128 occurrences, heuristiques et tres
  majoritairement FAUSSES : « température 36,2 °C », « IMC 47.6 kg/m² »,
  « VALGUS DU TALON : 12° à droite » sont des constantes MESUREES,
  correctement ecrites sans operateur. A relire une par une, pas a corriger en
  masse.
* `numeration-implicite` — 26 occurrences, dont une part REELLE
  (« leucocytes 12 000 », « leucocytes 17000 » : a lire en G/L) et une part
  fausse, ou l'unite est presente mais ecrite avec un « l » minuscule
  (« plaquettes 91000 G/l ») que la liste d'unites du motif German, qui ne
  connait que `G/L` et `g/L`, ne reconnait pas. A relire une par une.

Conclusion : sur les defauts d'import d'AMBOSS, CasECOS n'en porte
structurellement AUCUN — ni troncature au `x`, ni plage coupee par un « : », ni
chevron colle a une lettre. Le septieme defaut (« chaines d'examens copiees sur
le mauvais diagnostic ») n'est pas mecanisable et se verifie a la lecture, voir
PROCEDURE-casecos.md § Import.
"""
import importlib.util
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

_HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(_HERE))
import lib_casecos as lib  # noqa: E402

_GERMAN_DIR = _HERE.parent / "german"


def _german_families():
    """Les sept familles de motifs de `scripts/german/report_import_defects.py`.

    Chargement par chemin explicite, sous un alias propre a casecos : les quatre
    dossiers de corpus portent un script de ce nom, et un import ordinaire
    resoudrait selon l'ordre du chemin. Le module German importe lui-meme
    `lib_german`, ce qui est sans effet de bord ici — aucun fichier n'est lu au
    chargement.

    `sys.path` est RESTAURE en sortie. Le module German (comme celui de RESCOS)
    insere son propre dossier en tete de `sys.path` a l'import ; sans cette
    restauration, un `import snapshot_invariants` ulterieur dans le meme
    processus resoudrait vers celui de German. Aucun script de ce dossier ne le
    fait aujourd'hui — la restauration est la pour que ce soit encore vrai
    demain.
    """
    before = list(sys.path)
    try:
        path = _GERMAN_DIR / "report_import_defects.py"
        spec = importlib.util.spec_from_file_location(
            "_casecos_german_defects", path)
        module = importlib.util.module_from_spec(spec)
        sys.modules[spec.name] = module
        sys.path.append(str(_GERMAN_DIR))
        spec.loader.exec_module(module)
        return module.FAMILIES
    finally:
        sys.path[:] = before


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
        if not lib.matches(path, only):
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
        print(f"  {totals[name]:6d} occ / {len(grids_hit[name]):3d} grilles   {name}")
    print("\nRAPPORT — aucune correction appliquee, sortie 0.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
