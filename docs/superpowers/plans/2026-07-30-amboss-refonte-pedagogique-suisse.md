# Refonte pédagogique des 40 grilles AMBOSS — Plan d'implémentation

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Supprimer les répétitions des blocs pédagogiques des 40 grilles `cases/amboss/`, suisser leur nomenclature médicale, et aligner leurs prises en charge sur les pages SSP du vault Obsidian — sans toucher au barème des sections notées.

**Architecture:** Trois passes successives. D'abord un outillage de vérification qui fige les invariants (barèmes, structure, blocs présents) et mesure l'état initial. Ensuite deux passes de nomenclature, purement substitutives, validées par des scripts de contrôle. Enfin une passe éditoriale grille par grille, contre la page SSP de référence désignée par `docs/obsidian-mapping.yaml`, avec une grille pilote validée par l'utilisateur avant généralisation.

**Tech Stack:** Python 3 (stdlib uniquement — `re`, `json`, `glob`, `difflib`, `pathlib`), git, fichiers HTML statiques.

## Global Constraints

- **Barème gelé** : aucun ajout ni retrait de sous-item noté. `window.caseConfig.maxScores` et les `<span class="score">…/N</span>` doivent être **strictement identiques** avant et après chaque tâche.
- **Format des critères préservé** : `.criteria-text` garde la forme `N. Libellé [réponse]`. Ne jamais retirer la numérotation ni les crochets — `cases/scoring.js:159` fait `.split(". ")[1].split(" [")[0]`.
- **Crochets préservés** : les réponses patient restent entre `[...]`, colorées par `cases/scoring.js:290`.
- **Items ICE hors périmètre** : ne pas toucher au sous-item « Recherche des préoccupations et questions du patient » du critère `m4`.
- **Aucun bloc créé** : les 15 grilles sans `resume` ni `presentation` (10, 16, 17, 20, 21, 23, 24, 25, 26, 27, 29, 32, 33, 36, 40) n'en reçoivent pas. AMBOSS-34 garde son `resume` sans `presentation`.
- **Nomenclature médicale stricte** : noms de patients, lieux (Yosemite, New York) et sociétés savantes américaines (AHA/ACC, AAP) restent inchangés.
- **Jamais de lecture intégrale** : les fichiers font jusqu'à 2,77 Mo (95 % de base64). Lire par `offset`/`limit` sur la plage pédagogique.
- **Édition par remplacement exact de chaîne** : jamais de réécriture complète de fichier.
- **Travail strictement local** : aucun `git push`, aucune consultation de source externe. Le référentiel est `~/Documents/Damien/Medecine/Obsidian`.
- **Règle du format** : une information peut réapparaître si et seulement si elle change de format de restitution. Même format + même contenu = suppression.

## File Structure

**Créés :**

| Fichier | Responsabilité |
|---|---|
| `scripts/amboss/lib_amboss.py` | Fonctions partagées : bornes des blocs pédagogiques, extraction du texte visible, normalisation |
| `scripts/amboss/snapshot_invariants.py` | Capture l'état de référence (barèmes, blocs présents, compte de critères) dans un JSON |
| `scripts/amboss/check_invariants.py` | Compare l'état courant au snapshot ; sortie non nulle si divergence |
| `scripts/amboss/check_nomenclature.py` | Détecte les termes non suisses ; sortie non nulle si présents |
| `scripts/amboss/report_redundancy.py` | Liste les paires d'items quasi identiques entre blocs, par grille |
| `scripts/amboss/PROCEDURE.md` | Procédure de traitement d'une grille — livrable versionné référencé par les tâches 5 à 15 |
| `docs/superpowers/journal-amboss-2026-07.md` | Journal des modifications médicales et des divergences consignées |
| `scripts/amboss/baseline.json` | Snapshot des invariants (généré, versionné) |

**Modifiés :** les 40 fichiers `cases/amboss/AMBOSS-*.html`.

---

### Task 1: Outillage de vérification et mesure initiale

Le filet de sécurité. Sans lui, aucune des tâches suivantes n'est vérifiable.

**Files:**
- Create: `scripts/amboss/lib_amboss.py`
- Create: `scripts/amboss/snapshot_invariants.py`
- Create: `scripts/amboss/check_invariants.py`
- Create: `scripts/amboss/check_nomenclature.py`
- Create: `scripts/amboss/report_redundancy.py`
- Create: `scripts/amboss/PROCEDURE.md`
- Create: `docs/superpowers/journal-amboss-2026-07.md`

**Interfaces:**
- Produces: `lib_amboss.peda_bounds(text) -> (int, int)` — index de début et de fin de la zone pédagogique
- Produces: `lib_amboss.visible_text(html) -> str` — texte sans balises ni base64
- Produces: `lib_amboss.norm(s) -> str` — minuscules, sans accents, sans ponctuation
- Produces: `lib_amboss.list_items(segment) -> list[str]` — items `<li>` normalisés de plus de 18 caractères
- Produces: `lib_amboss.BLOCKS` — liste `(nom, regex_début, regex_fin)` des quatre blocs pédagogiques
- Produces: `scripts/amboss/baseline.json` — consommé par `check_invariants.py`

- [ ] **Step 1: Écrire la bibliothèque partagée**

Créer `scripts/amboss/lib_amboss.py` :

```python
"""Fonctions partagées pour le traitement des grilles AMBOSS."""
import re
import unicodedata
from pathlib import Path

CASES = Path(__file__).resolve().parents[2] / "cases" / "amboss"

# Bornes des quatre blocs pédagogiques. L'ordre reflète leur ordre dans le fichier.
BLOCKS = [
    ("resume", r'<div class="resume">', r'<div class="annexes">'),
    ("expert", r'<div class="annexe-item annexe-expert">',
     r'<div class="annexe-item annexe-theorie">'),
    ("theorie", r'<div class="annexe-item annexe-theorie">',
     r'<div class="presentation-patient">|<div class="annexe-item annexe-scenario">'),
    ("presentation", r'<div class="presentation-patient">',
     r'<div class="annexe-item annexe-scenario">'),
]


def grids():
    """Chemins des 40 grilles, triés par numéro."""
    return sorted(CASES.glob("AMBOSS-*.html"),
                  key=lambda p: int(re.search(r"AMBOSS-(\d+)", p.name).group(1)))


def grid_num(path):
    return int(re.search(r"AMBOSS-(\d+)", Path(path).name).group(1))


def strip_base64(html):
    """Remplace les URI de données par un marqueur — 95 % du poids des fichiers."""
    return re.sub(r'data:image[^"]*', "DATAURI", html)


def peda_bounds(html):
    """Index (début, fin) de la zone pédagogique.

    Début : <div class="resume"> si présent, sinon <div class="annexes">.
    Fin : <div class="annexe-item annexe-scenario">, sinon fin du fichier.
    Retourne (-1, -1) si aucune zone pédagogique n'est trouvée.
    """
    start = html.find('<div class="resume">')
    if start < 0:
        start = html.find('<div class="annexes">')
    if start < 0:
        return -1, -1
    end = html.find('<div class="annexe-item annexe-scenario">', start)
    return start, (end if end > 0 else len(html))


def blocks_present(html):
    """Noms des blocs pédagogiques présents dans ce fichier."""
    return [name for name, start, _ in BLOCKS if re.search(start, html)]


def block_segment(html, name):
    """Segment HTML d'un bloc, ou None s'il est absent."""
    for bname, start, end in BLOCKS:
        if bname != name:
            continue
        m = re.search(start, html)
        if not m:
            return None
        e = re.search(end, html[m.end():])
        return html[m.start(): m.end() + (e.start() if e else len(html))]
    return None


def visible_text(html):
    """Texte visible : sans balises, sans base64, espaces normalisés."""
    txt = re.sub(r"<[^>]+>", " ", strip_base64(html))
    txt = re.sub(r"&[a-z]+;", " ", txt)
    return re.sub(r"\s+", " ", txt).strip()


def norm(s):
    """Minuscules, sans accents, sans ponctuation — pour comparer du texte."""
    s = unicodedata.normalize("NFD", s.lower())
    s = "".join(c for c in s if unicodedata.category(c) != "Mn")
    return re.sub(r"\s+", " ", re.sub(r"[^a-z0-9 ]", " ", s)).strip()


def list_items(segment, min_len=18):
    """Items <li> normalisés, filtrés sur une longueur minimale."""
    items = [norm(visible_text(x))
             for x in re.findall(r"<li[^>]*>(.*?)</li>", segment, re.S)]
    return [i for i in items if len(i) >= min_len]
```

- [ ] **Step 2: Écrire le script de snapshot**

Créer `scripts/amboss/snapshot_invariants.py` :

```python
"""Capture l'état de référence des 40 grilles dans baseline.json."""
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import lib_amboss as lib

OUT = Path(__file__).parent / "baseline.json"


def snapshot_one(path):
    html = path.read_text(encoding="utf-8")
    m = re.search(r"maxScores:\s*\{([^}]*)\}", html)
    max_scores = {}
    if m:
        for k, v in re.findall(r"(\w+):\s*(\d+)", m.group(1)):
            max_scores[k] = int(v)
    spans = dict(re.findall(
        r'<span class="score">Score : <span id="(\w+)">0</span>/(\d+)</span>', html))
    return {
        "maxScores": max_scores,
        "scoreSpans": {k: int(v) for k, v in spans.items()},
        "blocks": lib.blocks_present(html),
        "criteriaCount": len(re.findall(r'class="criteria-text"', html)),
        "detailCount": len(re.findall(r'class="detail-text criteria-detail"', html)),
        "radioCount": len(re.findall(r'<input type="radio"', html)),
        "checkboxCount": len(re.findall(r'<input type="checkbox"', html)),
    }


def main():
    data = {p.name: snapshot_one(p) for p in lib.grids()}
    OUT.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"Snapshot de {len(data)} grilles ecrit dans {OUT.name}")


if __name__ == "__main__":
    main()
```

- [ ] **Step 3: Écrire le vérificateur d'invariants**

Créer `scripts/amboss/check_invariants.py` :

```python
"""Compare l'etat courant au snapshot. Sortie 1 si divergence."""
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import lib_amboss as lib
from snapshot_invariants import snapshot_one

BASE = Path(__file__).parent / "baseline.json"

# Champs dont toute variation est une regression.
FROZEN = ["maxScores", "scoreSpans", "blocks",
          "criteriaCount", "detailCount", "radioCount", "checkboxCount"]


def main():
    baseline = json.loads(BASE.read_text(encoding="utf-8"))
    problems = []
    for path in lib.grids():
        want = baseline.get(path.name)
        if want is None:
            problems.append(f"{path.name}: absent du snapshot")
            continue
        got = snapshot_one(path)
        for field in FROZEN:
            if got[field] != want[field]:
                problems.append(
                    f"{path.name}: {field} a change\n"
                    f"    attendu : {want[field]}\n"
                    f"    obtenu  : {got[field]}")
    if problems:
        print(f"ECHEC — {len(problems)} invariant(s) rompu(s) :\n")
        for p in problems:
            print("  " + p)
        return 1
    print(f"OK — {len(baseline)} grilles, tous les invariants preserves")
    return 0


if __name__ == "__main__":
    sys.exit(main())
```

- [ ] **Step 4: Écrire le vérificateur de nomenclature**

Créer `scripts/amboss/check_nomenclature.py` :

```python
"""Detecte les termes non suisses. Sortie 1 si presents."""
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import lib_amboss as lib

# Termes bannis et leur remplacement attendu.
BANNED = {
    r"\bNFS\b": "FSC",
    r"\bCBC\b": "FSC",
    r"\bBMP\b": "chimie sanguine",
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
```

- [ ] **Step 5: Écrire le rapport de redondance**

Créer `scripts/amboss/report_redundancy.py` :

```python
"""Liste les paires d'items quasi identiques entre blocs pedagogiques."""
import sys
from difflib import SequenceMatcher
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import lib_amboss as lib

THRESHOLD = 0.72


def pairs_for(path):
    html = path.read_text(encoding="utf-8")
    items = []
    for name, _, _ in lib.BLOCKS:
        seg = lib.block_segment(html, name)
        if seg:
            items += [(name, t) for t in lib.list_items(seg)]
    out = []
    for i in range(len(items)):
        for j in range(i + 1, len(items)):
            b1, t1 = items[i]
            b2, t2 = items[j]
            if b1 == b2:
                continue
            ratio = SequenceMatcher(None, t1, t2).ratio()
            if ratio > THRESHOLD:
                out.append((round(ratio, 2), b1, t1, b2, t2))
    return sorted(out, reverse=True)


def main():
    only = sys.argv[1] if len(sys.argv) > 1 else None
    grand = 0
    for path in lib.grids():
        if only and only not in path.name:
            continue
        found = pairs_for(path)
        grand += len(found)
        if found:
            print(f"\n=== {path.name} — {len(found)} paire(s) ===")
            for ratio, b1, t1, b2, t2 in found:
                print(f"  [{ratio}] {b1} <-> {b2}")
                print(f"      A: {t1[:100]}")
                print(f"      B: {t2[:100]}")
    print(f"\nTOTAL : {grand} paire(s) quasi identiques")


if __name__ == "__main__":
    main()
```

- [ ] **Step 6: Lancer le snapshot et vérifier qu'il capture bien 40 grilles**

Run: `python3 scripts/amboss/snapshot_invariants.py`
Expected: `Snapshot de 40 grilles ecrit dans baseline.json`

Run: `python3 -c "import json;d=json.load(open('scripts/amboss/baseline.json'));print(len(d));print(d['AMBOSS-1_-_Douleurs_abdominales_-_Femme_47_ans_-_Grille_ECOS.html']['maxScores'])"`
Expected: `40` puis `{'anamnese': 52, 'examen': 16, 'management': 17, 'communication': 20}`

- [ ] **Step 7: Vérifier que check_invariants passe sur un corpus non modifié**

Run: `python3 scripts/amboss/check_invariants.py`
Expected: `OK — 40 grilles, tous les invariants preserves`, code de sortie 0

- [ ] **Step 8: Vérifier que check_nomenclature ÉCHOUE — c'est le test rouge**

Run: `python3 scripts/amboss/check_nomenclature.py`
Expected: `ECHEC — 103 terme(s) non suisse(s) restant(s)`, code de sortie 1

Le détail attendu, vérifié sur le corpus :

| Motif | Occurrences | Grilles |
|---|---|---|
| `\bNFS\b` | 86 | 10, 11, 14, 15, 19, … |
| `\bVicodin\b` | 4 | 39 |
| `\bTylenol\b` | 4 | 7, 9 |
| `\bmg/dL\b` | 4 | 21, 37 |
| `\bTums\b` | 1 | 22 |
| `\bCBC\b` | 1 | 33 |
| `\bBMP\b` | 1 | 33 |
| `\b911\b` | 1 | 28 |
| `\bSAMU\b` | 1 | 35 |

Si le total diffère de 103, **ne pas poursuivre** : soit un motif attrape des faux
positifs, soit le corpus a changé. Vérifier avant d'appliquer le moindre remplacement.

Deux pièges déjà écartés, à ne pas réintroduire :

- `\bCBC\b` ne matche pas `ECBC` (AMBOSS-19, examen cytobactériologique des crachats) —
  la limite de mot le protège. Vérifié.
- `112` n'est **pas** dans la table : sa seule occurrence est `Score Global 0/112`
  dans AMBOSS-8, un total de barème. Un remplacement corromprait la grille.

- [ ] **Step 9: Enregistrer la mesure de redondance initiale**

Run: `python3 scripts/amboss/report_redundancy.py > /tmp/redundancy-initial.txt; tail -2 /tmp/redundancy-initial.txt`
Expected: `TOTAL : 301 paire(s) quasi identiques`

Ce nombre est la référence. La tâche 16 vérifiera qu'il a nettement baissé.

La mesure exploratoire menée pendant la conception annonçait 280. L'écart vient de
la normalisation : `lib.visible_text()` supprime les entités HTML (`&nbsp;`,
`&eacute;`…), ce que le script d'exploration ne faisait pas — les textes comparés
diffèrent donc légèrement, et les ratios de similarité avec eux. **La référence est
ce que produit `report_redundancy.py`**, puisque c'est lui qui mesurera aussi l'état
final : seule la comparaison initial/final par un même script a un sens. Ne jamais
ajuster le script pour retrouver un chiffre attendu.

- [ ] **Step 10: Écrire la procédure de traitement**

Créer `scripts/amboss/PROCEDURE.md`. Ce fichier est référencé par les tâches 4 à 15 ; il porte la procédure une seule fois.

````markdown
# Procédure de traitement d'une grille AMBOSS

Référence : `docs/superpowers/specs/2026-07-30-amboss-refonte-pedagogique-suisse-design.md`

## 1. Situer la zone pédagogique

```bash
python3 -c "
import sys; sys.path.insert(0,'scripts/amboss'); import lib_amboss as lib
p=[g for g in lib.grids() if 'AMBOSS-N_' in g.name][0]
h=p.read_text(encoding='utf-8'); s,e=lib.peda_bounds(h)
print('ligne debut :', h[:s].count(chr(10))+1)
print('ligne fin   :', h[:e].count(chr(10))+1)
print('blocs       :', lib.blocks_present(h))
"
```

Lire ensuite la grille avec `Read` en passant `offset` = ligne de début et
`limit` = (ligne de fin − ligne de début). **Ne jamais lire le fichier entier.**

## 2. Lire la page SSP de référence

La page est donnée par `docs/obsidian-mapping.yaml`. Racine du vault :
`/Users/damienfulliquet/Documents/Damien/Medecine/Obsidian`.

Sections utiles : `## 🔬 EXAMENS COMPLÉMENTAIRES`, `## 💊 PRISE EN CHARGE`,
`## 📌 Points Clés ECOS`.

## 3. Dédoublonner selon le contrat

| Bloc | Rôle exclusif | Ne porte jamais |
|---|---|---|
| `annexe-expert` | Faire tourner la station | Théorie, listes d'apprentissage |
| `annexe-theorie` | Comprendre le cas | Check-lists actionnables, mnémos, protocoles |
| `resume` | Réviser vite — **source canonique** | Redites de la théorie, formats oraux |
| `presentation-patient` | Restituer à l'oral | Toute donnée clinique nouvelle |

**Règle du format** : une information peut réapparaître si et seulement si elle
change de format de restitution (liste → narration, liste → SBAR, liste →
question d'examinateur). Même format + même contenu = suppression.

Les 7 axes à traiter :

1. **Examens complémentaires** — `resume` canonique ; `theorie` garde le *pourquoi*
   (Se/Sp, seuils, indications) sans la liste ; `presentation` garde sa Q/R, dont la
   réponse est un sous-ensemble strict de `resume`.
2. **Traitement / PEC** — `resume` canonique ; `theorie`/Rappels thérapeutiques garde
   le rationnel ; `presentation` garde sa réponse orale, sous-ensemble strict.
3. **PEC en 3 points** — check-list = sous-ensemble strict de `resume`/Prise en charge.
   Corriger toute divergence, ne rien ajouter.
4. **Examens à faire** — check-list = sous-ensemble strict de `resume`/Examen clinique.
5. **Checklist mentale** (`presentation`) — reste une **trame de présentation**
   (Intro → caractériser → symptômes → ATCD → examen → résumé → examens → PEC),
   jamais une liste de questions cliniques.
6. **Pièges** — `expert`/Pièges canonique. Supprimer `presentation`/Pièges ECOS.
   Concerne les grilles 1, 2, 3, 5, 6, 9, 11, 12, 13, 14, 30, 38, 39.
7. **Points clés** — les deux restent, différenciés : `expert` = ce que l'examinateur
   observe · `resume` = ce que l'étudiant retient.

Utiliser `python3 scripts/amboss/report_redundancy.py AMBOSS-N_` pour lister les
paires détectées sur cette grille précise.

## 4. Aligner les prises en charge

Trois cas, et trois seulement :

| Situation | Action |
|---|---|
| La page SSP traite le point et la grille en diverge | Aligner sur la page SSP, journaliser avec la ligne source |
| La page SSP ne traite pas le point | Laisser inchangé. **Ne rien inventer** |
| Contradiction de fond non tranchable sans avis clinique | Laisser inchangé, consigner au journal |

L'alignement ne concerne **que les blocs pédagogiques**. Toute divergence repérée
dans une section notée est consignée, jamais corrigée — le barème est gelé.

## 5. Journaliser

Ajouter une entrée dans `docs/superpowers/journal-amboss-2026-07.md` au format
défini en tête de ce fichier.

## 6. Vérifier

```bash
python3 scripts/amboss/check_invariants.py    # doit sortir OK
python3 scripts/amboss/check_nomenclature.py  # doit sortir OK
```

## Interdits

- Lire un fichier de grille en entier (jusqu'à 2,77 Mo).
- Réécrire un fichier complet — utiliser le remplacement exact de chaîne.
- Modifier `.criteria-text` : le format `N. Libellé [réponse]` est requis par
  `cases/scoring.js:159`.
- Retirer les crochets `[...]` des réponses patient (`cases/scoring.js:290`).
- Ajouter ou retirer un sous-item noté.
- Toucher aux items ICE du critère `m4`.
- Créer un bloc `resume` ou `presentation` absent.
````

- [ ] **Step 11: Créer le journal**

Créer `docs/superpowers/journal-amboss-2026-07.md` :

```markdown
# Journal de refonte — grilles AMBOSS

Référence : `docs/superpowers/specs/2026-07-30-amboss-refonte-pedagogique-suisse-design.md`

Deux types d'entrées :

- **Modification** — un changement appliqué, avec la ligne de page SSP qui le justifie.
- **Divergence** — un écart repéré mais **non corrigé**, laissé à l'arbitrage.

## Format

    ### AMBOSS-N — <motif> (page SSP : <nom>)

    **Modifications**
    - <bloc> · <sujet> : « <avant> » → « <après> »
      source : SSP — <section> — « <citation> »

    **Divergences consignées**
    - <zone> · <sujet> : la grille dit « <x> », la page SSP dit « <y> » — non corrigé (<raison>)

## Entrées
```

- [ ] **Step 12: Commit**

```bash
git add scripts/amboss/ docs/superpowers/journal-amboss-2026-07.md
git commit -m "Ajoute l'outillage de vérification des grilles AMBOSS

Snapshot des invariants (barèmes, structure, blocs), vérificateurs de
nomenclature et d'invariants, rapport de redondance, procédure de
traitement et journal.

État initial mesuré : 301 paires quasi identiques, 103 termes non suisses.

Co-Authored-By: Claude Opus 5 (1M context) <noreply@anthropic.com>"
```

---

### Task 2: Passe nomenclature — laboratoire et numéro d'urgence

Remplacements mécaniques, sans jugement médical. Aucun ne modifie le nombre de sous-items.

**Files:**
- Modify: les fichiers `cases/amboss/AMBOSS-*.html` concernés (86 `NFS`, 1 `CBC`, 1 `BMP`, 1 `911`, 1 `SAMU` — 90 remplacements)
- Create: `scripts/amboss/apply_lab_nomenclature.py`

**Interfaces:**
- Consumes: `lib_amboss.grids()`, `scripts/amboss/baseline.json` (Task 1)
- Produces: aucun ; la vérification passe par `check_invariants.py` et `check_nomenclature.py`

- [ ] **Step 1: Vérifier que `NFS` n'apparaît dans aucun attribut critique**

Run:
```bash
grep -o 'data-criteria="[^"]*NFS[^"]*"' cases/amboss/*.html | head
grep -o 'class="criteria-text">[^<]*NFS[^<]*' cases/amboss/*.html | head
```
Expected: aucune sortie pour les deux commandes.

Si l'une renvoie quelque chose, **arrêter** : le remplacement risquerait de casser
`identifyLacunes()` (`cases/scoring.js:152` et `:159`). Signaler à l'utilisateur.

- [ ] **Step 2: Écrire le script de remplacement**

Créer `scripts/amboss/apply_lab_nomenclature.py` :

```python
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
```

- [ ] **Step 3: Lancer le script**

Run: `python3 scripts/amboss/apply_lab_nomenclature.py`
Expected: le détail `86x \bNFS\b -> FSC`, `1x \bCBC\b -> FSC`, `1x \bBMP\b -> chimie sanguine`, `1x \b911\b -> 144`, `1x \bSAMU\b -> 144` — soit 90 remplacements au total.

- [ ] **Step 4: Vérifier que les invariants tiennent**

Run: `python3 scripts/amboss/check_invariants.py`
Expected: `OK — 40 grilles, tous les invariants preserves`, code de sortie 0

Si ce script échoue, faire `git checkout -- cases/amboss/` et signaler à l'utilisateur.

- [ ] **Step 5: Vérifier que les termes visés ont disparu**

Run: `python3 scripts/amboss/check_nomenclature.py`
Expected: `ECHEC — 13 terme(s) non suisse(s) restant(s)` — uniquement `Vicodin` (4), `Tylenol` (4), `Tums` (1) et `mg/dL` (4), traités en tâche 3. Aucune ligne `NFS`, `CBC`, `BMP`, `911`, `SAMU`.

- [ ] **Step 6: Vérifier visuellement un remplacement en zone notée**

Run: `grep -o 'class="detail-text criteria-detail">FSC[^<]*' cases/amboss/AMBOSS-31*.html`
Expected: `class="detail-text criteria-detail">FSC avec formule `

- [ ] **Step 7: Commit**

```bash
git add cases/amboss/ scripts/amboss/apply_lab_nomenclature.py
git commit -m "Suisse la nomenclature de laboratoire et le numéro d'urgence

NFS et CBC -> FSC (87 occurrences), BMP -> chimie sanguine,
911 et SAMU -> 144. Soit 90 remplacements.

Remplacements 1 pour 1 hors base64. Barèmes et structure vérifiés
inchangés par check_invariants.py.

Co-Authored-By: Claude Opus 5 (1M context) <noreply@anthropic.com>"
```

---

### Task 3: Passe nomenclature — médicaments et unités SI

Peu d'occurrences, mais chacune demande un jugement médical. Traitement manuel, pas de script.

**Files:**
- Modify: `cases/amboss/AMBOSS-39_-_Douleur_a__l_e_paule_-_Homme_52_ans_-_Grille_ECOS.html` (4 × Vicodin)
- Modify: `cases/amboss/AMBOSS-7_-_Toux_et_fie_vre_-_Fillette_2_ans_-_Grille_ECOS.html` (1 × Tylenol)
- Modify: `cases/amboss/AMBOSS-9_-_Douleurs_dorsales_-_Homme_71_ans_-_Grille_ECOS.html` (3 × Tylenol)
- Modify: `cases/amboss/AMBOSS-22_-_Dysphagie_-_Femme_60_ans_-_Grille_ECOS.html` (1 × Tums)
- Modify: `cases/amboss/AMBOSS-21_-_He_maturie_-_Homme_23_ans_-_Grille_ECOS.html` (3 × mg/dL)
- Modify: `cases/amboss/AMBOSS-37_-_Changements_cutane_s_-_Nouveau-ne_e_4_jours_-_Grille_ECOS.html` (1 × mg/dL)
- Modify: `docs/superpowers/journal-amboss-2026-07.md`

**Interfaces:**
- Consumes: `check_invariants.py`, `check_nomenclature.py` (Task 1)

- [ ] **Step 1: Localiser chaque occurrence avec son contexte**

Run:
```bash
python3 -c "
import sys,re; sys.path.insert(0,'scripts/amboss'); import lib_amboss as lib
for p in lib.grids():
    t=lib.visible_text(p.read_text(encoding='utf-8'))
    for term in ['Vicodin','Tylenol','Tums','mg/dL']:
        for m in re.finditer(re.escape(term),t):
            print(f'[{p.name[:12]}] ...{t[max(0,m.start()-70):m.end()+70]}...')
"
```
Expected: 13 lignes de contexte.

- [ ] **Step 2: Remplacer Vicodin dans AMBOSS-39**

Vicodin est de l'hydrocodone/paracétamol, non commercialisé en Suisse. Équivalent
d'usage : tramadol. Les quatre occurrences sont narratives (réponse patient, résumé,
version longue, scénario) — appliquer le même remplacement partout.

Utiliser `Edit` avec `replace_all: true` :
- `du Vicodin` → `du Tramal® (tramadol)`
- `essai Vicodin` → `essai Tramal® (tramadol)`
- `usage Vicodin` → `usage Tramal® (tramadol)`

Conserver le reste de chaque phrase à l'identique, y compris « de ma copine »,
« non prescrit, effet indésirable » et la mention des étourdissements — l'effet
indésirable décrit (vertiges) est cohérent avec le tramadol.

- [ ] **Step 3: Remplacer Tylenol dans AMBOSS-7 et AMBOSS-9**

- AMBOSS-7 (fillette de 2 ans) : `du Tylenol` → `du Dafalgan® (paracétamol)`
- AMBOSS-9 (homme de 71 ans) : `du Tylenol` → `du Dafalgan® (paracétamol)`,
  `de Tylenol` → `de Dafalgan®`

Le dosage « trois comprimés de 500 mg » d'AMBOSS-9 reste valide : Dafalgan existe
en 500 mg. Ne pas le modifier.

- [ ] **Step 4: Remplacer Tums dans AMBOSS-22**

`Je prends du Tums` → `Je prends du Rennie® (antiacide)`

- [ ] **Step 5: Convertir les unités d'AMBOSS-21**

Trois conversions, dans le bloc de résultats biologiques :

| Avant | Après |
|---|---|
| `C3 : 45 mg/dL (N: 90-180) - abaissé` | `C3 : 0.45 g/L (N: 0.9-1.8) - abaissé` |
| `C4 : 25 mg/dL (N: 10-40) - normal` | `C4 : 0.25 g/L (N: 0.1-0.4) - normal` |
| `Créatinine : 1.8 mg/dL (légèrement élevée)` | `Créatinine : 159 µmol/L (légèrement élevée)` |

Facteur de conversion de la créatinine : mg/dL × 88,4 = µmol/L, soit 1,8 × 88,4 ≈ 159.

- [ ] **Step 6: Retirer la parenthèse en mg/dL d'AMBOSS-37**

`Visible si bilirubine > 85 μmol/L (5 mg/dL)` → `Visible si bilirubine > 85 μmol/L`

La valeur SI est déjà présente ; seule la conversion américaine part.

- [ ] **Step 7: Vérifier que les invariants tiennent**

Run: `python3 scripts/amboss/check_invariants.py`
Expected: `OK — 40 grilles, tous les invariants preserves`

- [ ] **Step 8: Vérifier que la nomenclature est propre**

Run: `python3 scripts/amboss/check_nomenclature.py`
Expected: `OK — aucun terme non suisse detecte`, code de sortie 0

- [ ] **Step 9: Journaliser**

Ajouter sous `## Entrées` de `docs/superpowers/journal-amboss-2026-07.md` :

```markdown
### Passe nomenclature (tâches 2 et 3)

**Modifications**
- global · laboratoire : « NFS » (86×) et « CBC » (1×) → « FSC »
  source : SSP — tableaux Biologie, forme employée dans les 135 pages
- global · laboratoire : « BMP » → « chimie sanguine »
- AMBOSS-28 · urgence : « 911 » → « 144 » ; AMBOSS-35 · urgence : « SAMU » → « 144 »
  source : SSP — Mesures générales — « En Suisse : alerte 144 si instabilité »
  (« 112 » écarté : la seule occurrence du corpus est un total de barème)
- AMBOSS-39 · médicament : « Vicodin » → « Tramal® (tramadol) » — hydrocodone/paracétamol non commercialisé en CH
- AMBOSS-7, 9 · médicament : « Tylenol » → « Dafalgan® (paracétamol) »
- AMBOSS-22 · médicament : « Tums » → « Rennie® (antiacide) »
- AMBOSS-21 · unités : C3 45 mg/dL → 0.45 g/L ; C4 25 mg/dL → 0.25 g/L ;
  créatinine 1.8 mg/dL → 159 µmol/L (× 88,4)
- AMBOSS-37 · unités : retrait de la parenthèse « (5 mg/dL) », la valeur SI restant seule
```

- [ ] **Step 10: Commit**

```bash
git add cases/amboss/ docs/superpowers/journal-amboss-2026-07.md
git commit -m "Suisse les médicaments et les unités de laboratoire

Vicodin -> Tramal®, Tylenol -> Dafalgan®, Tums -> Rennie®.
Conversions SI : C3 et C4 en g/L, créatinine en µmol/L.

check_nomenclature.py passe désormais sans erreur.

Co-Authored-By: Claude Opus 5 (1M context) <noreply@anthropic.com>"
```

---

### Task 4: Pilote — AMBOSS-1 (Douleur Abdominale)

Grille de référence : elle cumule les défauts observés. **Validation utilisateur obligatoire avant la tâche 5.**

**Files:**
- Modify: `cases/amboss/AMBOSS-1_-_Douleurs_abdominales_-_Femme_47_ans_-_Grille_ECOS.html`
- Modify: `docs/superpowers/journal-amboss-2026-07.md`
- Read: `/Users/damienfulliquet/Documents/Damien/Medecine/Obsidian/SSP ECOS/SSP — Douleur Abdominale.md`
- Reference: `scripts/amboss/PROCEDURE.md`

**Interfaces:**
- Consumes: `PROCEDURE.md`, `report_redundancy.py`, `check_invariants.py` (Task 1)
- Produces: le patron éditorial validé que les tâches 5 à 15 appliquent

- [ ] **Step 1: Lister les paires de redondance de cette grille**

Run: `python3 scripts/amboss/report_redundancy.py AMBOSS-1_`
Expected: la liste des paires détectées entre `resume`, `expert`, `theorie` et `presentation`.

- [ ] **Step 2: Situer la zone pédagogique**

Run:
```bash
python3 -c "
import sys; sys.path.insert(0,'scripts/amboss'); import lib_amboss as lib
p=[g for g in lib.grids() if g.name.startswith('AMBOSS-1_')][0]
h=p.read_text(encoding='utf-8'); s,e=lib.peda_bounds(h)
print('debut', h[:s].count(chr(10))+1, '| fin', h[:e].count(chr(10))+1)
print('blocs', lib.blocks_present(h))
"
```
Expected: `debut 774 | fin 1246` et `blocs ['resume', 'expert', 'theorie', 'presentation']`

- [ ] **Step 3: Lire la zone pédagogique et la page SSP**

Lire la grille avec `Read`, `offset: 774`, `limit: 472`.
Lire `/Users/damienfulliquet/Documents/Damien/Medecine/Obsidian/SSP ECOS/SSP — Douleur Abdominale.md`.

- [ ] **Step 4: Fusionner le titre `Examens complémentaires` dupliqué**

`annexe-theorie` contient deux fois `<h4>Examens complémentaires</h4>`. La première
section liste les examens de première intention, la seconde leurs performances
(sensibilité de l'échographie, place de l'IRM/CPRE, du CT, de la scintigraphie HIDA).

Fusionner en une seule section intitulée `Examens complémentaires`, en gardant le
*pourquoi* (performances, indications) et en supprimant la liste redondante avec
`resume`/Examens diagnostiques — conformément à l'axe 1 du contrat.

- [ ] **Step 5: Appliquer l'axe 6 — supprimer `presentation`/Pièges ECOS**

Le bloc `presentation` contient une sous-section `<h5>⚠️ Pièges ECOS</h5>` dont les
quatre items reprennent `annexe-expert`/Pièges (RGO, sclérotiques, Murphy, poids).
Supprimer la sous-section entière de `presentation`.

- [ ] **Step 6: Appliquer l'axe des mnémos — les 6F apparaissent trois fois**

Les 6F figurent dans `annexe-theorie`/Facteurs de risque, dans `resume`/`mnemo-box`
et dans `presentation`/Touches ludiques. Le contrat place les mnémos dans
`presentation`. Conserver la liste des 6F dans `presentation`/Touches ludiques,
retirer la `mnemo-box` de `resume`, et dans `annexe-theorie` ne garder que ce qui
relève du raisonnement — l'application des critères à cette patiente (IMC 30,
47 ans, 2 enfants, mère avec calculs) — sans re-lister le moyen mnémotechnique.

- [ ] **Step 7: Appliquer l'axe Murphy**

Le signe de Murphy est décrit dans `resume`/Examen clinique, dans
`annexe-theorie`/Signe de Murphy et dans `presentation`/Signe de Murphy = MURPHY.
Garder la description technique et les valeurs (Se 65 %, Sp 87 %) dans
`annexe-theorie`, la mention actionnable dans `resume`, et le mnémo dans
`presentation`. Supprimer les redites de technique dans `presentation`.

- [ ] **Step 8: Décontaminer la check-list (axes 3 et 4)**

Vérifier que `resume`/Check-list rapide ECOS est un sous-ensemble strict des
sections détaillées : chaque item de « Questions à poser », « Examens à faire » et
« PEC en 3 points » doit correspondre à un item présent au-dessus, sans information
nouvelle ni formulation contradictoire. Corriger les divergences dans la check-list,
pas dans les sections détaillées.

- [ ] **Step 9: Aligner les PEC sur la page SSP**

Points à confronter à `SSP — Douleur Abdominale` :

| Sujet | Grille actuelle | Page SSP |
|---|---|---|
| Antalgie | « paracétamol, ± morphine » | « palier 1 paracétamol 1 g ; palier 2-3 métamizole (Novalgine®, fréquent en Suisse), morphine titrée IV ; éviter les AINS si suspicion d'ulcère, IRA ou patient âgé » |
| Antibiothérapie | « céphalosporine + métronidazole » | section Conduites ciblées — « Colique biliaire / cholécystite : écho HCD, antalgie, antibiothérapie si cholécystite, cholécystectomie laparoscopique précoce » |
| Remplissage | « perfusion IV » | « 2 voies veineuses de gros calibre, remplissage cristalloïde (NaCl 0,9 % ou Ringer-lactate) » |
| Antiémétique | « antiémétiques » | « ondansétron, métoclopramide » |
| Bilan | « CRP, hyperleucocytose, bilan hépatique, lipase » | tableau Biologie 1ʳᵉ intention — vérifier la présence de FSC, CRP, bilan hépatique, lipase, crase si pré-opératoire |

Appliquer la règle des trois cas de `PROCEDURE.md` § 4. En particulier : ajouter le
métamizole (Novalgine®) à l'antalgie, préciser le cristalloïde, nommer les
antiémétiques. Ne pas ajouter la crase si la page SSP ne la rattache pas
explicitement à ce contexte.

- [ ] **Step 10: Vérifier les invariants**

Run: `python3 scripts/amboss/check_invariants.py`
Expected: `OK — 40 grilles, tous les invariants preserves`

- [ ] **Step 11: Vérifier la baisse de redondance sur cette grille**

Run: `python3 scripts/amboss/report_redundancy.py AMBOSS-1_ | tail -1`
Expected: un total nettement inférieur à celui du Step 1. Chaque paire restante doit
correspondre à un changement de format documenté (SBAR, version longue, Q/R examinateur).

- [ ] **Step 12: Journaliser**

Ajouter une entrée `### AMBOSS-1 — Douleurs abdominales (page SSP : Douleur Abdominale)`
au format défini dans le journal, listant chaque modification avec sa source et chaque
divergence consignée.

- [ ] **Step 13: Commit**

```bash
git add cases/amboss/AMBOSS-1_*.html docs/superpowers/journal-amboss-2026-07.md
git commit -m "Refonte pédagogique AMBOSS-1 (pilote)

Fusionne le titre Examens complémentaires dupliqué, applique le contrat
de blocs aux 6F, au signe de Murphy et aux pièges, décontamine la
check-list, aligne les PEC sur SSP — Douleur Abdominale (métamizole,
cristalloïde, antiémétiques nommés).

Co-Authored-By: Claude Opus 5 (1M context) <noreply@anthropic.com>"
```

- [ ] **Step 14: POINT D'ARRÊT — validation utilisateur**

Présenter à l'utilisateur : `git show --stat HEAD`, le diff de la zone pédagogique,
et l'entrée de journal. **Ne pas enchaîner sur la tâche 5 sans son accord explicite.**

Si l'utilisateur demande des ajustements, les appliquer, mettre à jour
`scripts/amboss/PROCEDURE.md` en conséquence, et refaire valider.

---

### Task 5: Grilles 2 et 3 — Douleur Abdominale

Même page SSP que le pilote, déjà lue.

**Files:**
- Modify: `cases/amboss/AMBOSS-2_-_Douleurs_abdominales_-_Femme_23_ans_-_Grille_ECOS.html`
- Modify: `cases/amboss/AMBOSS-3_-_Douleurs_abdominales_-_Femme_34_ans_-_Grille_ECOS.html`
- Modify: `docs/superpowers/journal-amboss-2026-07.md`
- Read: `/Users/damienfulliquet/Documents/Damien/Medecine/Obsidian/SSP ECOS/SSP — Douleur Abdominale.md`
- Reference: `scripts/amboss/PROCEDURE.md`

**Interfaces:**
- Consumes: `PROCEDURE.md` tel que validé au Step 14 de la tâche 4

- [ ] **Step 1: Traiter AMBOSS-2 en suivant `scripts/amboss/PROCEDURE.md`**

Spécificités connues de cette grille :
- `annexe-theorie` contient un `<h4>Examens complémentaires</h4>` **dupliqué** — le fusionner comme au Step 4 de la tâche 4.
- Fait partie des 13 grilles avec `presentation`/Pièges ECOS — appliquer l'axe 6.
- Les quatre blocs sont présents.

- [ ] **Step 2: Traiter AMBOSS-3 en suivant `scripts/amboss/PROCEDURE.md`**

Spécificités : les quatre blocs sont présents ; fait partie des 13 grilles avec
`presentation`/Pièges ECOS.

- [ ] **Step 3: Vérifier les invariants**

Run: `python3 scripts/amboss/check_invariants.py`
Expected: `OK — 40 grilles, tous les invariants preserves`

- [ ] **Step 4: Vérifier la baisse de redondance**

Run: `python3 scripts/amboss/report_redundancy.py AMBOSS-2_; python3 scripts/amboss/report_redundancy.py AMBOSS-3_`
Expected: chaque paire restante correspond à un changement de format documenté.

- [ ] **Step 5: Journaliser les deux grilles**

- [ ] **Step 6: Commit**

```bash
git add cases/amboss/AMBOSS-2_*.html cases/amboss/AMBOSS-3_*.html docs/superpowers/journal-amboss-2026-07.md
git commit -m "Refonte pédagogique AMBOSS-2 et 3 (Douleur Abdominale)

Co-Authored-By: Claude Opus 5 (1M context) <noreply@anthropic.com>"
```

---

### Task 6: Grilles 12, 13, 14 — Douleur Thoracique

**Files:**
- Modify: `cases/amboss/AMBOSS-12_-_Douleur_thoracique_-_Femme_35_ans_-_Grille_ECOS.html`
- Modify: `cases/amboss/AMBOSS-13_-_Douleur_thoracique_-_Homme_35_ans_-_Grille_ECOS.html`
- Modify: `cases/amboss/AMBOSS-14_-_Douleur_thoracique_-_Homme_45_ans_-_Grille_ECOS.html`
- Modify: `docs/superpowers/journal-amboss-2026-07.md`
- Read: `/Users/damienfulliquet/Documents/Damien/Medecine/Obsidian/SSP ECOS/SSP — Douleur Thoracique.md`
- Reference: `scripts/amboss/PROCEDURE.md`

- [ ] **Step 1: Traiter les trois grilles en suivant `scripts/amboss/PROCEDURE.md`**

Les trois ont les quatre blocs. Toutes trois font partie des 13 grilles avec
`presentation`/Pièges ECOS — appliquer l'axe 6 à chacune.

- [ ] **Step 2: Vérifier les invariants**

Run: `python3 scripts/amboss/check_invariants.py`
Expected: `OK — 40 grilles, tous les invariants preserves`

- [ ] **Step 3: Vérifier la redondance sur les trois grilles**

Run: `for n in 12 13 14; do python3 scripts/amboss/report_redundancy.py "AMBOSS-$n\_" | tail -1; done`

- [ ] **Step 4: Journaliser les trois grilles**

- [ ] **Step 5: Commit**

```bash
git add cases/amboss/AMBOSS-1[234]_*.html docs/superpowers/journal-amboss-2026-07.md
git commit -m "Refonte pédagogique AMBOSS-12, 13, 14 (Douleur Thoracique)

Co-Authored-By: Claude Opus 5 (1M context) <noreply@anthropic.com>"
```

---

### Task 7: Grilles 18, 19, 31 — Toux Chronique

**Files:**
- Modify: `cases/amboss/AMBOSS-18_-_Toux_chronique_-_Femme_21_ans_-_Grille_ECOS.html`
- Modify: `cases/amboss/AMBOSS-19_-_Toux_chronique_-_Femme_53_ans_-_Grille_ECOS.html`
- Modify: `cases/amboss/AMBOSS-31_-_Toux_-_Homme_58_ans_-_Grille_ECOS.html`
- Modify: `docs/superpowers/journal-amboss-2026-07.md`
- Read: `/Users/damienfulliquet/Documents/Damien/Medecine/Obsidian/SSP ECOS/SSP — Toux Chronique.md`
- Reference: `scripts/amboss/PROCEDURE.md`

- [ ] **Step 1: Traiter les trois grilles en suivant `scripts/amboss/PROCEDURE.md`**

Les trois ont les quatre blocs. Aucune ne figure dans la liste des 13 grilles avec
`presentation`/Pièges ECOS — l'axe 6 ne s'applique pas ici.

- [ ] **Step 2: Vérifier les invariants**

Run: `python3 scripts/amboss/check_invariants.py`
Expected: `OK — 40 grilles, tous les invariants preserves`

- [ ] **Step 3: Journaliser les trois grilles**

- [ ] **Step 4: Commit**

```bash
git add cases/amboss/AMBOSS-1[89]_*.html cases/amboss/AMBOSS-31_*.html docs/superpowers/journal-amboss-2026-07.md
git commit -m "Refonte pédagogique AMBOSS-18, 19, 31 (Toux Chronique)

Co-Authored-By: Claude Opus 5 (1M context) <noreply@anthropic.com>"
```

---

### Task 8: Grilles 4, 5, 6 — gynécologie et digestif

**Files:**
- Modify: `cases/amboss/AMBOSS-4_-_Saignements_vaginaux_-_Femme_50_ans_-_Grille_ECOS.html`
- Modify: `cases/amboss/AMBOSS-5_-_Nause_es_-_Femme_19_ans_-_Grille_ECOS.html`
- Modify: `cases/amboss/AMBOSS-6_-_Douleurs_pelviennes_-_Femme_30_ans_-_Grille_ECOS.html`
- Modify: `docs/superpowers/journal-amboss-2026-07.md`
- Read: `SSP ECOS/SSP — Saignement Vaginal Anormal.md` (AMBOSS-4)
- Read: `SSP ECOS/SSP — Nausées, Vomissements & Hématémèse.md` (AMBOSS-5)
- Read: `SSP ECOS/SSP — Douleur - Masse Pelvienne.md` (AMBOSS-6)
- Reference: `scripts/amboss/PROCEDURE.md`

Racine du vault : `/Users/damienfulliquet/Documents/Damien/Medecine/Obsidian/`

- [ ] **Step 1: Traiter les trois grilles en suivant `scripts/amboss/PROCEDURE.md`**

Les trois ont les quatre blocs. AMBOSS-5 et AMBOSS-6 figurent parmi les 13 grilles
avec `presentation`/Pièges ECOS — appliquer l'axe 6 à ces deux-là, pas à AMBOSS-4.

- [ ] **Step 2: Vérifier les invariants**

Run: `python3 scripts/amboss/check_invariants.py`
Expected: `OK — 40 grilles, tous les invariants preserves`

- [ ] **Step 3: Journaliser les trois grilles**

- [ ] **Step 4: Commit**

```bash
git add cases/amboss/AMBOSS-[456]_*.html docs/superpowers/journal-amboss-2026-07.md
git commit -m "Refonte pédagogique AMBOSS-4, 5, 6

Co-Authored-By: Claude Opus 5 (1M context) <noreply@anthropic.com>"
```

---

### Task 9: Grilles 7, 8, 9 — pédiatrie, transit, lombalgies

**Files:**
- Modify: `cases/amboss/AMBOSS-7_-_Toux_et_fie_vre_-_Fillette_2_ans_-_Grille_ECOS.html`
- Modify: `cases/amboss/AMBOSS-8_-_Troubles_du_transit_-_Homme_32_ans_-_Grille_ECOS.html`
- Modify: `cases/amboss/AMBOSS-9_-_Douleurs_dorsales_-_Homme_71_ans_-_Grille_ECOS.html`
- Modify: `docs/superpowers/journal-amboss-2026-07.md`
- Read: `SSP ECOS/SSP — Fièvre du Nourrisson.md` (AMBOSS-7)
- Read: `SSP ECOS/SSP — Diarrhée.md` (AMBOSS-8)
- Read: `SSP ECOS/SSP — Lombalgies.md` (AMBOSS-9)
- Reference: `scripts/amboss/PROCEDURE.md`

- [ ] **Step 1: Traiter les trois grilles en suivant `scripts/amboss/PROCEDURE.md`**

Les trois ont les quatre blocs. AMBOSS-9 figure parmi les 13 grilles avec
`presentation`/Pièges ECOS.

Pour AMBOSS-7, la communication porte sur la mère : le critère `m4` s'intitule
« Communication avec la mère ». Ne pas y toucher — items ICE hors périmètre.

- [ ] **Step 2: Vérifier les invariants**

Run: `python3 scripts/amboss/check_invariants.py`
Expected: `OK — 40 grilles, tous les invariants preserves`

- [ ] **Step 3: Journaliser les trois grilles**

- [ ] **Step 4: Commit**

```bash
git add cases/amboss/AMBOSS-[789]_*.html docs/superpowers/journal-amboss-2026-07.md
git commit -m "Refonte pédagogique AMBOSS-7, 8, 9

Co-Authored-By: Claude Opus 5 (1M context) <noreply@anthropic.com>"
```

---

### Task 10: Grilles 11, 15, 22 — digestif haut et bas

**Files:**
- Modify: `cases/amboss/AMBOSS-11_-_Selles_noires_-_Homme_65_ans_-_Grille_ECOS.html`
- Modify: `cases/amboss/AMBOSS-15_-_Douleur_abdominale_chronique_-_Garc_on_6_ans_-_Grille_ECOS.html`
- Modify: `cases/amboss/AMBOSS-22_-_Dysphagie_-_Femme_60_ans_-_Grille_ECOS.html`
- Modify: `docs/superpowers/journal-amboss-2026-07.md`
- Read: `SSP ECOS/SSP — Rectorragies & Hémorragie Digestive Basse.md` (AMBOSS-11)
- Read: `SSP ECOS/SSP — Dysphagie.md` (AMBOSS-22)
- Reference: `scripts/amboss/PROCEDURE.md`

- [ ] **Step 1: Traiter AMBOSS-11 et AMBOSS-22 en suivant `scripts/amboss/PROCEDURE.md`**

Les deux ont les quatre blocs. AMBOSS-11 figure parmi les 13 grilles avec
`presentation`/Pièges ECOS.

- [ ] **Step 2: Traiter AMBOSS-15 — cas particulier, sans alignement des PEC**

`docs/obsidian-mapping.yaml` rattache AMBOSS-15 à
`Skills ECOS/Skills — Réflexes Médicamenteux & Antidotes.md`, qui ne porte pas de
prise en charge par motif. Pour cette grille :

- appliquer le dédoublonnage selon le contrat (§ 3 de `PROCEDURE.md`) ;
- **ne pas** appliquer l'étape 4 d'alignement des PEC ;
- consigner au journal que l'alignement est reporté faute de page SSP adéquate.

- [ ] **Step 3: Vérifier les invariants**

Run: `python3 scripts/amboss/check_invariants.py`
Expected: `OK — 40 grilles, tous les invariants preserves`

- [ ] **Step 4: Journaliser les trois grilles, dont la divergence AMBOSS-15**

- [ ] **Step 5: Commit**

```bash
git add cases/amboss/AMBOSS-11_*.html cases/amboss/AMBOSS-15_*.html cases/amboss/AMBOSS-22_*.html docs/superpowers/journal-amboss-2026-07.md
git commit -m "Refonte pédagogique AMBOSS-11, 15, 22

AMBOSS-15 : dédoublonnage seul, alignement PEC reporté faute de page
SSP de référence (rattachée à une page Skills).

Co-Authored-By: Claude Opus 5 (1M context) <noreply@anthropic.com>"
```

---

### Task 11: Grilles 28, 30, 34 — endocrino, ORL, ophtalmo

**Files:**
- Modify: `cases/amboss/AMBOSS-28_-_Prise_de_poids_-_Homme_45_ans_-_Grille_ECOS.html`
- Modify: `cases/amboss/AMBOSS-30_-_Mal_de_gorge_-_Homme_19_ans_-_Grille_ECOS.html`
- Modify: `cases/amboss/AMBOSS-34_-_Perte_de_vision_-_Homme_66_ans_-_Grille_ECOS.html`
- Modify: `docs/superpowers/journal-amboss-2026-07.md`
- Read: `SSP ECOS/SSP — Syndrome Métabolique.md` (AMBOSS-28)
- Read: `SSP ECOS/SSP — Mal de Gorge (Angine).md` (AMBOSS-30)
- Read: `SSP ECOS/SSP — Amaurose & Baisse d'Acuité Visuelle.md` (AMBOSS-34)
- Reference: `scripts/amboss/PROCEDURE.md`

- [ ] **Step 1: Traiter AMBOSS-28 et AMBOSS-30 en suivant `scripts/amboss/PROCEDURE.md`**

Les deux ont les quatre blocs. AMBOSS-30 figure parmi les 13 grilles avec
`presentation`/Pièges ECOS.

AMBOSS-28 contient des items relatifs au risque suicidaire (« Évaluation des idées
suicidaires actuelles », « Plan de sécurité si risque élevé »). Ce sont des items
cliniques légitimes, **pas** des items ICE : ne pas les supprimer.

- [ ] **Step 2: Traiter AMBOSS-34 — `resume` sans `presentation`**

Cette grille possède un `resume` mais **pas** de bloc `presentation`. Ne pas le
créer. Les axes 5 et 6 (qui portent sur `presentation`) ne s'appliquent pas.
Traiter les axes 1, 2, 3, 4 et 7.

- [ ] **Step 3: Vérifier les invariants**

Run: `python3 scripts/amboss/check_invariants.py`
Expected: `OK — 40 grilles, tous les invariants preserves`

En particulier, le champ `blocks` d'AMBOSS-34 doit rester `["resume", "expert", "theorie"]`.

- [ ] **Step 4: Journaliser les trois grilles**

- [ ] **Step 5: Commit**

```bash
git add cases/amboss/AMBOSS-28_*.html cases/amboss/AMBOSS-30_*.html cases/amboss/AMBOSS-34_*.html docs/superpowers/journal-amboss-2026-07.md
git commit -m "Refonte pédagogique AMBOSS-28, 30, 34

Co-Authored-By: Claude Opus 5 (1M context) <noreply@anthropic.com>"
```

---

### Task 12: Grilles 35, 37, 38, 39 — RGO, néonat, MSK

**Files:**
- Modify: `cases/amboss/AMBOSS-35_-_Bru_lures_d_estomac_-_Femme_54_ans_-_Grille_ECOS.html`
- Modify: `cases/amboss/AMBOSS-37_-_Changements_cutane_s_-_Nouveau-ne_e_4_jours_-_Grille_ECOS.html`
- Modify: `cases/amboss/AMBOSS-38_-_Douleur_a__la_cheville_-_Femme_28_ans_-_Grille_ECOS.html`
- Modify: `cases/amboss/AMBOSS-39_-_Douleur_a__l_e_paule_-_Homme_52_ans_-_Grille_ECOS.html`
- Modify: `docs/superpowers/journal-amboss-2026-07.md`
- Read: `SSP ECOS/SSP — Pyrosis (RGO).md` (AMBOSS-35)
- Read: `SSP ECOS/SSP — Éruption Cutanée.md` (AMBOSS-37)
- Read: `SSP ECOS/SSP — Entorse de Cheville.md` (AMBOSS-38)
- Read: `SSP ECOS/SSP — Douleur d'Épaule.md` (AMBOSS-39)
- Reference: `scripts/amboss/PROCEDURE.md`

- [ ] **Step 1: Traiter les quatre grilles en suivant `scripts/amboss/PROCEDURE.md`**

Les quatre ont les quatre blocs. AMBOSS-38 et AMBOSS-39 figurent parmi les 13
grilles avec `presentation`/Pièges ECOS.

AMBOSS-39 a été modifiée en tâche 3 (Vicodin → Tramal®). Vérifier que la mention
apparaît de façon cohérente dans les blocs pédagogiques et le scénario.

- [ ] **Step 2: Vérifier les invariants**

Run: `python3 scripts/amboss/check_invariants.py`
Expected: `OK — 40 grilles, tous les invariants preserves`

- [ ] **Step 3: Vérifier que la nomenclature reste propre**

Run: `python3 scripts/amboss/check_nomenclature.py`
Expected: `OK — aucun terme non suisse detecte`

- [ ] **Step 4: Journaliser les quatre grilles**

- [ ] **Step 5: Commit**

```bash
git add cases/amboss/AMBOSS-3[5789]_*.html docs/superpowers/journal-amboss-2026-07.md
git commit -m "Refonte pédagogique AMBOSS-35, 37, 38, 39

Co-Authored-By: Claude Opus 5 (1M context) <noreply@anthropic.com>"
```

---

### Task 13: Grilles allégées 10, 16, 17, 20, 21

Ces grilles n'ont **ni** `resume` **ni** `presentation` — seulement `annexe-expert` et
`annexe-theorie`. Le travail se limite à l'axe expert ↔ théorie et à l'alignement des PEC.

**Files:**
- Modify: `cases/amboss/AMBOSS-10_-_Douleurs_dorsales_et_raideur_-_Homme_26_ans_-_Grille_ECOS.html`
- Modify: `cases/amboss/AMBOSS-16_-_Troubles_du_sommeil_-_Femme_32_ans_-_Grille_ECOS.html`
- Modify: `cases/amboss/AMBOSS-17_-_Troubles_de_me_moire_-_Femme_70_ans_-_Grille_ECOS.html`
- Modify: `cases/amboss/AMBOSS-20_-_Diminution_de_sensation_dans_les_extre_mite_s_-_Homme_42_ans_-_Grille_ECOS.html`
- Modify: `cases/amboss/AMBOSS-21_-_He_maturie_-_Homme_23_ans_-_Grille_ECOS.html`
- Modify: `docs/superpowers/journal-amboss-2026-07.md`
- Read: `SSP ECOS/SSP — Lombalgies.md` (AMBOSS-10)
- Read: `SSP ECOS/SSP — Troubles du Sommeil.md` (AMBOSS-16)
- Read: `SSP ECOS/SSP — Troubles de la Mémoire & Démences.md` (AMBOSS-17)
- Read: `SSP ECOS/SSP — Neuropathie Périphérique.md` (AMBOSS-20)
- Read: `SSP ECOS/SSP — Hématurie.md` (AMBOSS-21)
- Reference: `scripts/amboss/PROCEDURE.md`

- [ ] **Step 1: Confirmer que ces cinq grilles n'ont que deux blocs**

Run:
```bash
python3 -c "
import sys; sys.path.insert(0,'scripts/amboss'); import lib_amboss as lib
for p in lib.grids():
    if lib.grid_num(p) in (10,16,17,20,21):
        print(lib.grid_num(p), lib.blocks_present(p.read_text(encoding='utf-8')))
"
```
Expected: `['expert', 'theorie']` pour les cinq.

- [ ] **Step 2: Traiter les cinq grilles**

Suivre `scripts/amboss/PROCEDURE.md`, en n'appliquant que ce qui les concerne :

- **Axe applicable** : `expert` ↔ `theorie` — retirer de `annexe-theorie` ce qui
  relève de la conduite de station (résultats à délivrer, pièges du candidat) et le
  laisser à `annexe-expert` ; retirer d'`annexe-expert` ce qui relève de la théorie.
- **Défaut connu** : vérifier la présence d'un `<h4>` dupliqué dans `annexe-theorie`
  (le cas est avéré sur AMBOSS-1 et 2 ; le contrôler ici).
- **Alignement des PEC** : appliquer le § 4 de `PROCEDURE.md` aux deux blocs.
- **Ne pas créer** de `resume` ni de `presentation`.

AMBOSS-21 a été modifiée en tâche 3 (conversions SI de C3, C4 et créatinine).
Vérifier que les valeurs converties sont cohérentes dans les deux blocs.

- [ ] **Step 3: Vérifier les invariants**

Run: `python3 scripts/amboss/check_invariants.py`
Expected: `OK — 40 grilles, tous les invariants preserves`

Le champ `blocks` de ces cinq grilles doit rester `["expert", "theorie"]`.

- [ ] **Step 4: Journaliser les cinq grilles**

- [ ] **Step 5: Commit**

```bash
git add cases/amboss/AMBOSS-10_*.html cases/amboss/AMBOSS-1[67]_*.html cases/amboss/AMBOSS-2[01]_*.html docs/superpowers/journal-amboss-2026-07.md
git commit -m "Refonte pédagogique AMBOSS-10, 16, 17, 20, 21 (grilles allégées)

Co-Authored-By: Claude Opus 5 (1M context) <noreply@anthropic.com>"
```

---

### Task 14: Grilles allégées 23, 24, 25, 26, 27

**Files:**
- Modify: `cases/amboss/AMBOSS-23_-_Perte_auditive_-_Homme_65_ans_-_Grille_ECOS.html`
- Modify: `cases/amboss/AMBOSS-24_-_E_valuation_apre_s_chute_-_Femme_30_ans_-_Grille_ECOS.html`
- Modify: `cases/amboss/AMBOSS-25_-_Douleur_au_genou_-_Femme_47_ans_-_Grille_ECOS.html`
- Modify: `cases/amboss/AMBOSS-26_-_Ce_phale_e_-_Homme_29_ans_-_Grille_ECOS.html`
- Modify: `cases/amboss/AMBOSS-27_-_Fatigue_-_Femme_28_ans_-_Grille_ECOS.html`
- Modify: `docs/superpowers/journal-amboss-2026-07.md`
- Read: `SSP ECOS/SSP — Perte d'Audition.md` (AMBOSS-23)
- Read: `SSP ECOS/SSP — Capacité de Discernement & Éthique.md` (AMBOSS-24)
- Read: `SSP ECOS/SSP — Douleur de Genou.md` (AMBOSS-25)
- Read: `SSP ECOS/SSP — Céphalée.md` (AMBOSS-26)
- Read: `SSP ECOS/SSP — Fatigue.md` (AMBOSS-27)
- Reference: `scripts/amboss/PROCEDURE.md`

- [ ] **Step 1: Traiter les cinq grilles**

Suivre `scripts/amboss/PROCEDURE.md`, axe `expert` ↔ `theorie` et alignement des PEC
uniquement. Ces cinq grilles n'ont que `annexe-expert` et `annexe-theorie` : ne créer
ni `resume` ni `presentation`.

AMBOSS-24 est rattachée à une page SSP portant sur la capacité de discernement.
L'alignement des PEC y porte sur la conduite d'évaluation, pas sur un traitement.

- [ ] **Step 2: Vérifier les invariants**

Run: `python3 scripts/amboss/check_invariants.py`
Expected: `OK — 40 grilles, tous les invariants preserves`

- [ ] **Step 3: Journaliser les cinq grilles**

- [ ] **Step 4: Commit**

```bash
git add cases/amboss/AMBOSS-2[34567]_*.html docs/superpowers/journal-amboss-2026-07.md
git commit -m "Refonte pédagogique AMBOSS-23, 24, 25, 26, 27 (grilles allégées)

Co-Authored-By: Claude Opus 5 (1M context) <noreply@anthropic.com>"
```

---

### Task 15: Grilles allégées 29, 32, 33, 36, 40

**Files:**
- Modify: `cases/amboss/AMBOSS-29_-_Fatigue_-_Femme_18_ans_-_Grille_ECOS.html`
- Modify: `cases/amboss/AMBOSS-32_-_Le_sion_ge_nitale_-_Femme_17_ans_-_Grille_ECOS.html`
- Modify: `cases/amboss/AMBOSS-33_-_Ce_phale_e_-_Femme_55_ans_-_Grille_ECOS.html`
- Modify: `cases/amboss/AMBOSS-36_-_Fatigue_-_Homme_54_ans_-_Grille_ECOS.html`
- Modify: `cases/amboss/AMBOSS-40_-_Vertiges_-_Homme_25_ans_-_Grille_ECOS.html`
- Modify: `docs/superpowers/journal-amboss-2026-07.md`
- Read: `SSP ECOS/SSP — Fatigue.md` (AMBOSS-29 et 36)
- Read: `SSP ECOS/SSP — Leucorrhées.md` (AMBOSS-32)
- Read: `SSP ECOS/SSP — Céphalée.md` (AMBOSS-33)
- Read: `SSP ECOS/SSP — Vertiges.md` (AMBOSS-40)
- Reference: `scripts/amboss/PROCEDURE.md`

- [ ] **Step 1: Traiter les cinq grilles**

Suivre `scripts/amboss/PROCEDURE.md`, axe `expert` ↔ `theorie` et alignement des PEC
uniquement. Ne créer ni `resume` ni `presentation`.

AMBOSS-33 a été modifiée en tâche 2 : la légende d'image qui expliquait les
abréviations américaines (`BMP : panel métabolique de base ; CBC : numération formule
sanguine`) porte désormais `chimie sanguine` et `FSC`. Vérifier que la phrase reste
lisible et retirer la glose devenue inutile si elle ne définit plus que des termes
français courants.

- [ ] **Step 2: Vérifier les invariants**

Run: `python3 scripts/amboss/check_invariants.py`
Expected: `OK — 40 grilles, tous les invariants preserves`

- [ ] **Step 3: Journaliser les cinq grilles**

- [ ] **Step 4: Commit**

```bash
git add cases/amboss/AMBOSS-29_*.html cases/amboss/AMBOSS-3[236]_*.html cases/amboss/AMBOSS-40_*.html docs/superpowers/journal-amboss-2026-07.md
git commit -m "Refonte pédagogique AMBOSS-29, 32, 33, 36, 40 (grilles allégées)

Co-Authored-By: Claude Opus 5 (1M context) <noreply@anthropic.com>"
```

---

### Task 16: Vérification finale et rapport

**Files:**
- Create: `docs/superpowers/rapport-amboss-2026-07.md`
- Read: `docs/superpowers/journal-amboss-2026-07.md`

**Interfaces:**
- Consumes: tous les scripts de la tâche 1, le journal alimenté par les tâches 3 à 15

- [ ] **Step 1: Vérifier les invariants sur l'ensemble**

Run: `python3 scripts/amboss/check_invariants.py`
Expected: `OK — 40 grilles, tous les invariants preserves`, code de sortie 0

- [ ] **Step 2: Vérifier la nomenclature sur l'ensemble**

Run: `python3 scripts/amboss/check_nomenclature.py`
Expected: `OK — aucun terme non suisse detecte`, code de sortie 0

- [ ] **Step 3: Mesurer la redondance finale**

Run: `python3 scripts/amboss/report_redundancy.py > /tmp/redundancy-final.txt; tail -1 /tmp/redundancy-final.txt`
Expected: un total nettement inférieur à **301** (référence mesurée en tâche 1).

- [ ] **Step 4: Vérifier que chaque paire restante est justifiée**

Run: `head -60 /tmp/redundancy-final.txt`

Chaque paire subsistante doit relever d'un changement de format : `presentation`
contre un autre bloc (SBAR, version longue, Q/R examinateur), ou `resume`/check-list
contre `resume`/section détaillée. Une paire `expert` ↔ `theorie` ou une paire
intra-format non justifiée est un défaut résiduel : la corriger avant de continuer.

- [ ] **Step 5: Vérifier l'intégrité structurelle des fichiers**

Run:
```bash
python3 -c "
import sys; sys.path.insert(0,'scripts/amboss'); import lib_amboss as lib
bad=0
for p in lib.grids():
    h=p.read_text(encoding='utf-8')
    o,c=h.count('<div'),h.count('</div>')
    if o!=c:
        print(f'{p.name}: {o} <div> pour {c} </div>'); bad+=1
    if '</html>' not in h[-200:]:
        print(f'{p.name}: fin de fichier anormale'); bad+=1
print('OK' if not bad else f'{bad} probleme(s)')
"
```
Expected: `OK`

- [ ] **Step 6: Vérifier qu'une grille s'ouvre et calcule correctement**

Ouvrir `cases/amboss/AMBOSS-1_-_Douleurs_abdominales_-_Femme_47_ans_-_Grille_ECOS.html`
dans un navigateur. Vérifier :

- le minuteur s'affiche et démarre ;
- cocher un critère d'anamnèse incrémente le score affiché ;
- le total de section correspond au dénominateur affiché ;
- les réponses patient entre crochets apparaissent en bleu ;
- les blocs pédagogiques s'affichent sans balise orpheline visible.

- [ ] **Step 7: Écrire le rapport**

Créer `docs/superpowers/rapport-amboss-2026-07.md` reprenant :

- l'état initial (301 paires, 103 termes non suisses) et l'état final mesuré ;
- le nombre de grilles traitées par catégorie (25 complètes, 15 allégées) ;
- la liste des divergences consignées au journal et non corrigées, qui constituent
  la matière d'une prochaine passe ;
- le rappel qu'AMBOSS-15 n'a pas reçu d'alignement de PEC faute de page SSP adéquate.

- [ ] **Step 8: Commit**

```bash
git add docs/superpowers/rapport-amboss-2026-07.md
git commit -m "Ajoute le rapport de refonte pédagogique AMBOSS

Co-Authored-By: Claude Opus 5 (1M context) <noreply@anthropic.com>"
```

- [ ] **Step 9: Présenter le résultat à l'utilisateur**

Présenter le rapport, la liste des divergences consignées, et demander si une
seconde passe est souhaitée sur les points laissés en arbitrage.

**Aucun `git push`** — le travail reste local, conformément à la consigne.
