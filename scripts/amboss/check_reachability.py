"""Verifie que le bareme declare est ATTEIGNABLE par le calcul. Sortie 1 si ecart.

Usage :
    python3 scripts/amboss/check_reachability.py [GRILLE_FILTRE]

Exemples :
    python3 scripts/amboss/check_reachability.py            # les 40 grilles
    python3 scripts/amboss/check_reachability.py AMBOSS-9_  # detail d'une grille


POURQUOI CE CONTROLE EST DISTINCT DE check_invariants.py
--------------------------------------------------------
`check_invariants.py` compare l'etat courant a un snapshot : il verifie que des
**comptes d'elements** n'ont pas bouge (maxScores, scoreSpans, criteriaCount,
detailCount, radioCount, checkboxCount). C'est un controle de NON-REGRESSION —
il repond a « le bareme est-il le meme qu'hier ? », jamais a « le bareme
est-il juste ? ». Un bareme faux depuis l'origine reste vert indefiniment, et
c'est exactement ce qui s'est produit : AMBOSS-9 declarait `anamnese: 53` pour
49 points calculables et `count: 13` pour 12 criteres joignables, defaut present
des le commit initial du depot, invisible a tous les garde-fous pendant toute
la duree du projet. La grille affichait « Score : 49/53 » meme tout coche et le
score global plafonnait a 98 %.

Ce script repond a l'autre question. Il ne compare rien a un passe : il rejoue
la logique de `cases/scoring.js` (`calculateScores()`) sur le DOM de chaque
grille et **simule le remplissage complet** — chaque case de detail cochee,
chaque radio a sa valeur maximale, chaque item de communication au niveau A
(4 points). Le maximum ainsi simule doit egaler, pour chaque section :

  1. `window.caseConfig.maxScores[key]` — le denominateur du calcul ;
  2. le `<span class="score">Score : <span id="…">0</span>/N</span>` — le
     denominateur AFFICHE au candidat, qui est une chaine litterale du HTML et
     peut donc diverger silencieusement du precedent.

Et le pourcentage global (somme des `coef` ponderes) doit tomber sur 100 %.

TROIS ECARTS POSSIBLES, tous detectes ici et par rien d'autre :

  * `count` trop grand — `calculateScores()` itere `prefix + i` pour i de 1 a
    `count`. Un critere promis par `count` mais absent de la page rapporte 0 :
    le maximum devient inatteignable. Signale « ABSENT ».
  * sous-item ORPHELIN — un critere qui existe dans la page sous un
    identifiant hors de la sequence `prefix1..prefixN` (cas d'`a12b` en
    AMBOSS-9 : la boucle produit `a1`…`a12`, jamais `a12b`). Ses cases sont
    cochables mais ne valent aucun point, et rien dans le DOM ne le dit.
  * `maxScores` et le `<span>` qui divergent l'un de l'autre.

`sectionInfo[].count` est desormais aussi capture par `snapshot_invariants.py`
et gele par `check_invariants.py` : une fois ce champ juste, il ne peut plus
deriver. Les deux controles sont complementaires — l'un fige, l'autre valide.
"""
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import lib_amboss as lib

# Bareme de la section communication, identique a scoring.js:17 et :125.
COMM = {"A": 4, "B": 3, "C": 2, "D": 1, "E": 0}


def detail_rules(html):
    """Seuils optionnels `detailRules`, identiques a scoring.js:officialDetailScore.

    Par defaut un critere a cases de detail vaut 1 point par case cochee. Une
    grille peut declarer des seuils pour retomber sur la notation 2/1/0 de la
    grille papier — `{a1: {oui: 3, partiel: 1}}` = « au moins 3 = oui, 1-2 = ±,
    aucun = non ». Absent partout ailleurs : le dictionnaire vide preserve
    exactement le calcul historique.

    `points` surcharge les valeurs 2/1 quand la grille papier plafonne la ligne
    plus bas — station 6, item 7 « troubles cognitifs » : `au moins 1 = Oui`
    vaut 1 point et non 2, colonne ± grisee.
    """
    m = re.search(r"detailRules:\s*\{", html)
    if not m:
        return {}
    # Equilibrage strict des accolades : le bloc contient des sous-objets, un
    # motif de fin non equilibre s'arreterait au premier `}` interne.
    depth, start = 0, m.end() - 1
    for i in range(start, len(html)):
        if html[i] == "{":
            depth += 1
        elif html[i] == "}":
            depth -= 1
            if depth == 0:
                blob = html[start + 1:i]
                break
    else:
        return {}

    rules = {}
    # `points: {...}` est un sous-objet : le capturer d'abord et le retirer du
    # corps, sinon `(\w+):\s*\{([^{}]*)\}` lirait `points` comme un critere.
    for cid, body in re.findall(r"(\w+):\s*\{((?:[^{}]|\{[^{}]*\})*)\}", blob):
        sur = re.search(r"points:\s*\{([^{}]*)\}", body)
        body = body[:sur.start()] + body[sur.end():] if sur else body
        oui = re.search(r"oui:\s*(\d+)", body)
        if not oui:
            continue
        partiel = re.search(r"partiel:\s*(\d+)", body)
        pts_oui = re.search(r"oui:\s*(\d+)", sur.group(1)) if sur else None
        pts_part = re.search(r"partiel:\s*(\d+)", sur.group(1)) if sur else None
        rules[cid] = {
            "oui": int(oui.group(1)),
            "partiel": int(partiel.group(1)) if partiel else None,
            "pointsOui": int(pts_oui.group(1)) if pts_oui else 2,
            "pointsPartiel": int(pts_part.group(1)) if pts_part else 1,
        }
    return rules


def detail_points(rule, coches):
    """Points d'un critere a seuils — meme branchement que scoring.js."""
    if coches >= rule["oui"]:
        return rule["pointsOui"]
    if rule["partiel"] is not None and coches >= rule["partiel"]:
        return rule["pointsPartiel"]
    return 0


def parse_config(html):
    """maxScores, coef, sectionInfo et denominateurs affiches d'une grille."""
    m = re.search(r"maxScores:\s*\{([^}]*)\}", html)
    max_scores = {k: int(v) for k, v in re.findall(r"(\w+):\s*(\d+)", m.group(1))} if m else {}

    m = re.search(r"coef:\s*\{([^}]*)\}", html)
    coef = {k: float(v) for k, v in re.findall(r"(\w+):\s*([\d.]+)", m.group(1))} if m else {}

    sections = []
    m = re.search(r"sectionInfo:\s*\[(.*?)\]", html, re.S)
    for blob in re.findall(r"\{[^{}]*\}", m.group(1) if m else ""):
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
            # scoreId: section.scoreId || section.key + "Score" (scoring.js:177)
            "scoreId": score_id.group(1) if score_id else key.group(1) + "Score",
            "isComm": re.search(r"isComm:\s*true", blob) is not None,
        })

    spans = {k: int(v) for k, v in re.findall(
        r'<span class="score">Score : <span id="(\w+)">0</span>/(\d+)</span>', html)}
    return max_scores, coef, sections, spans


def section_max(html, section):
    """Maximum atteignable d'une section, et le detail critere par critere.

    Reproduit la boucle de `calculateScores()` : pour i de 1 a `count`, le
    critere `prefix + i` vaut la somme de ses cases de detail si elles
    existent, sinon la plus forte valeur de ses radios. Un critere que la
    boucle appelle et que la page ne porte pas vaut 0 — c'est le cas
    « ABSENT », qui rend le bareme inatteignable.
    """
    total, detail, missing = 0, [], []
    rules = detail_rules(html)
    for i in range(1, section["count"] + 1):
        cid = f'{section["prefix"]}{i}'
        if section["isComm"]:
            levels = re.findall(
                r'<input type="radio"[^>]*name="%s"[^>]*value="(\w)"' % cid, html)
            best = max((COMM.get(v, 0) for v in levels), default=None)
        else:
            checks = re.findall(
                r'<input type="checkbox" id="%s-detail-\d+"[^>]*value="(\d+)"' % cid, html)
            if checks:
                coches = sum(int(v) for v in checks)
                if cid in rules:
                    best = detail_points(rules[cid], coches)
                    detail.append(
                        f"{cid} = {best} ({len(checks)} case(s) de detail, seuils officiels)")
                else:
                    best = coches
                    detail.append(f"{cid} = {best} ({len(checks)} case(s) de detail)")
            else:
                radios = re.findall(
                    r'<input type="radio"[^>]*name="%s"[^>]*value="(\d+)"' % cid, html)
                best = max((int(v) for v in radios), default=None)
                if best is not None:
                    detail.append(f"{cid} = {best} (radio)")
        if best is None:
            missing.append(cid)
            continue
        if section["isComm"]:
            detail.append(f"{cid} = {best} (communication, niveau A)")
        total += best
    return total, detail, missing


def orphan_criteria(html, sections):
    """Criteres portant des cases de detail mais hors de toute sequence iteree.

    `calculateScores()` ne connait que `prefix1..prefixN`. Un identifiant qui
    n'y figure pas — `a12b` — reste cochable a l'ecran sans jamais entrer dans
    le calcul : ses points sont perdus sans trace.
    """
    seen = sorted(set(re.findall(r'<input type="checkbox" id="([\w-]+?)-detail-\d+"', html)))
    known = {f'{s["prefix"]}{i}' for s in sections for i in range(1, s["count"] + 1)}
    return [c for c in seen if c not in known]


def check_one(path):
    """(ok, lignes) — verdict d'une grille et son detail lisible."""
    html = lib.strip_base64(path.read_text(encoding="utf-8"))
    max_scores, coef, sections, spans = parse_config(html)
    lines, ok, global_pct = [], True, 0.0

    if not sections:
        return False, ["    sectionInfo introuvable ou illisible"]

    for section in sections:
        key = section["key"]
        total, detail, missing = section_max(html, section)
        declared = max_scores.get(key)
        span = spans.get(section["scoreId"])
        ecart = not (total == declared == span)
        ok = ok and not ecart and not missing
        lines.append(
            f'    {key:<14} atteignable={total:<4} maxScores={declared}'
            f'  affiche=/{span}{"   <<< ECART" if ecart else ""}')
        if missing:
            lines.append(
                f'      count={section["count"]} promet {len(missing)} critere(s) '
                f'que la page ne porte pas : {", ".join(missing)}')
        if declared:
            global_pct += (total / declared) * coef.get(key, 0)
        lines.append(f"      {' · '.join(detail)}" if detail else "      (aucun critere)")

    orphans = orphan_criteria(html, sections)
    if orphans:
        ok = False
        lines.append(f"    critere(s) hors sequence, jamais calcule(s) : {', '.join(orphans)}")

    pct = round(global_pct * 100)
    lines.append(f"    global si tout est coche : {pct} %")
    if pct != 100:
        ok = False
    return ok, lines


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
