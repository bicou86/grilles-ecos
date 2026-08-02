"""Verifie que le bareme declare est ATTEIGNABLE par le calcul. Sortie 1 si ecart.

Usage :
    python3 scripts/rescos/check_reachability.py [GRILLE_FILTRE]

Exemples :
    python3 scripts/rescos/check_reachability.py             # les 41 grilles
    python3 scripts/rescos/check_reachability.py RESCOS-12_  # detail d'une grille

La simulation elle-meme (`section_max`, `orphan_criteria`, `check_one`) est
importee de `scripts/amboss/check_reachability.py`, sans copie : elle rejoue
`cases/scoring.js` et ne depend d'aucune particularite de corpus. Seules
l'enumeration des grilles et la LECTURE DE LA CONFIGURATION sont redefinies ici.

DEUX FORMES DE DECLARATION DU BAREME
------------------------------------
39 grilles sur 41 portent un `window.caseConfig` de la meme forme qu'AMBOSS et
German (`maxScores`, `coef`, `sectionInfo[{key, prefix, count, scoreId,
isComm}]`) et delèguent le calcul au `cases/scoring.js` partage.

RESCOS-7 et RESCOS-9 n'ont AUCUN `caseConfig` — cas inedit, aucune grille des
deux corpus precedents n'en manquait. Elles ne sont pas pour autant sans
bareme : elles embarquent chacune leur PROPRE copie de `calculateScores()`,
ou la configuration est construite ligne a ligne au lieu d'etre declaree :

    scores["anamnese"] = 0;
    maxScores["anamnese"] = 41;
    coef["anamnese"] = 0.7;
    sectionInfo.push({key: "anamnese", prefix: "a", count: 14, label: "Anamnèse"});

Le corps de la fonction est identique a celui de `cases/scoring.js` — meme
traitement des cases de detail, meme repli sur les radios, meme table
communication A=4..E=0, meme ponderation par `coef`. Le bareme y est donc
PARFAITEMENT CALCULABLE, et ce script s'y applique sans reserve : `parse_config`
lit simplement l'autre forme. Il n'y a pas lieu de les exclure du controle.

Le remplacement de `parse_config` se fait sur le module AMBOSS charge sous un
alias PROPRE a rescos (`lib.amboss_module`, prefixe `_rescos_amboss_`), afin
qu'il ne puisse pas fuir vers German si les deux tournaient dans le meme
processus.

POURQUOI CE CONTROLE EST DISTINCT DE check_invariants.py
--------------------------------------------------------
`check_invariants.py` compare l'etat courant a un snapshot : il repond a « le
bareme est-il le meme qu'hier ? », jamais a « le bareme est-il juste ? ». Un
bareme faux depuis l'origine reste vert indefiniment — c'est ce qui s'est
produit sur AMBOSS-9, dont le defaut, present des le commit initial, n'a ete vu
qu'apres quinze taches.

Ce script ne compare rien a un passe : il simule le remplissage complet et
exige que le total tombe sur `maxScores[key]` ET sur le denominateur affiche au
candidat, et que le pourcentage global fasse 100 %.

UN QUATRIEME ECART, PROPRE A CE CORPUS : LA SECTION VIDE PONDEREE
-----------------------------------------------------------------
Aux trois ecarts que detectait deja la version AMBOSS (`count` trop grand,
sous-item orphelin, `maxScores` divergeant du `<span>`) s'en ajoute un
quatrieme, que RESCOS-12 et RESCOS-13 portent : une section DECLAREE VIDE
(`count: 0`, `maxScores: 0`, « Score : 0/0 », aucun critere dans la page) mais
qui conserve son COEFFICIENT. `scoring.js` calcule `max > 0 ? (score/max)*100 : 0`
— le pourcentage de cette section vaut donc 0 quoi que fasse le candidat, et
sa part de coefficient est perdue pour tout le monde. Le score global plafonne
a 75 %, meme grille parfaitement remplie.

Ce cas passe les trois controles precedents sans bruit (0 == 0 == 0 pour la
section), et n'est visible que par le total global. `empty_weighted_sections()`
le nomme explicitement plutot que de laisser lire « global 75 % » sans cause.
"""
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import lib_rescos as lib

_amboss = lib.amboss_module("check_reachability")
_parse_caseconfig = _amboss.parse_config
section_max = _amboss.section_max
orphan_criteria = _amboss.orphan_criteria


def parse_config(html):
    """maxScores, coef, sectionInfo et denominateurs affiches — les deux formes.

    Tente d'abord la forme declarative `window.caseConfig` (39 grilles). Si elle
    ne rend aucune section, relit la forme imperative de RESCOS-7 et RESCOS-9.
    Les denominateurs affiches (`<span class="score">`) sont lus de la meme
    facon dans les deux cas : ce sont des chaines litterales du HTML.
    """
    max_scores, coef, sections, spans = _parse_caseconfig(html)
    if sections:
        return max_scores, coef, sections, spans

    max_scores = {k: int(v) for k, v in
                  re.findall(r'maxScores\["(\w+)"\]\s*=\s*(\d+)', html)}
    coef = {k: float(v) for k, v in
            re.findall(r'coef\["(\w+)"\]\s*=\s*([\d.]+)', html)}
    for blob in re.findall(r"sectionInfo\.push\(\{([^}]*)\}\)", html):
        key = re.search(r'key:\s*"(\w+)"', blob)
        prefix = re.search(r'prefix:\s*"(\w+)"', blob)
        count = re.search(r"count:\s*(\d+)", blob)
        if not (key and prefix and count):
            continue
        score_id = re.search(r'scoreId:\s*"(\w+)"', blob)
        sections.append({
            "key": key.group(1),
            "prefix": prefix.group(1),
            "count": int(count.group(1)),
            # scoreId: section.scoreId || section.key + "Score"
            "scoreId": score_id.group(1) if score_id else key.group(1) + "Score",
            "isComm": re.search(r"isComm:\s*true", blob) is not None,
        })
    return max_scores, coef, sections, spans


# `check_one` appelle `parse_config` par son nom global : le remplacer dans le
# module AMBOSS suffit a lui faire lire les deux formes, sans en recopier la
# moindre ligne. L'alias du module est propre a rescos (voir l'entete).
_amboss.parse_config = parse_config
check_one = _amboss.check_one


def empty_weighted_sections(html):
    """Sections declarees vides mais conservant un coefficient non nul.

    Retourne [(key, coef), ...]. Leur pourcentage vaut 0 quoi qu'il arrive et
    leur part de coefficient est definitivement perdue : c'est la cause exacte
    d'un « global < 100 % » sans aucun ecart de section.
    """
    max_scores, coef, sections, _ = parse_config(html)
    return [(s["key"], coef.get(s["key"], 0)) for s in sections
            if s["count"] == 0 and not max_scores.get(s["key"])
            and coef.get(s["key"], 0)]


def main():
    only = sys.argv[1] if len(sys.argv) > 1 else None
    checked, bad = 0, 0
    for path in lib.grids():
        if only and only not in path.name:
            continue
        checked += 1
        ok, lines = check_one(path)
        if not ok:
            bad += 1
            empty = empty_weighted_sections(
                lib.strip_base64(path.read_text(encoding="utf-8")))
            for key, c in empty:
                lines.append(
                    f"    section VIDE mais PONDEREE : {key} (count=0, maxScores=0) "
                    f"garde coef={c} — {round(c * 100)} % du score global sont "
                    f"inatteignables par construction")
        if not ok or only:
            print(f'{path.name}  {"OK" if ok else "ECART"}')
            print("\n".join(lines))

    if only and checked == 0:
        print(f"Aucune grille ne correspond au filtre {only!r}.")
        return 1
    if bad:
        print(f"\nECHEC — {bad} grille(s) sur {checked} au bareme inatteignable")
        return 1
    print(f"\nOK — {checked} grille(s), bareme atteignable a 100 % sur chaque section")
    return 0


if __name__ == "__main__":
    sys.exit(main())
