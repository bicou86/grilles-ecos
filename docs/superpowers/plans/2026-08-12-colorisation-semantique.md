# Colorisation sémantique — Plan d'implémentation

> **Pour les agents :** SOUS-COMPÉTENCE REQUISE — utiliser `superpowers:subagent-driven-development`
> (recommandé) ou `superpowers:executing-plans` pour exécuter ce plan tâche par tâche. Les
> étapes utilisent des cases à cocher (`- [ ]`).

**Objectif :** porter le bloc `theorie` du corpus azygos de 39,1 à 70–80 spans sémantiques
pour 1000 mots, et doter 20 grilles dépourvues de contenu pédagogique des blocs `resume`,
`theorie` et `presentation`.

**Architecture :** deux lots sans dépendance technique l'un envers l'autre. Le lot 1 modifie
le pipeline de génération d'azygos (`build_grid.py`, `lexique_semantique.py`) puis régénère —
le balisage est un produit du lexique, jamais une retouche du HTML. Le lot 2 introduit
`scripts/peda/`, où le contenu est rédigé en texte brut Python, colorisé par le même lexique,
puis injecté dans le HTML par un script idempotent.

**Pile technique :** Python 3.11 (bibliothèque standard seulement), Node 22 pour
`browser_probe.js`, Chrome for Testing (`~/.cache/puppeteer/chrome-headless-shell`).

**Spec :** `docs/superpowers/specs/2026-08-12-colorisation-semantique-design.md`

## Contraintes globales

- **Jamais de retrait de span.** Toutes les passes sont additives.
- **Jamais de modification des sections notées.** Aucun `criteria-row`, aucun `input`, aucun
  `window.caseConfig`, aucun barème n'est touché — dans les deux lots.
- **Le texte visible ne change pas** au lot 1 : le balisage enveloppe, il ne réécrit pas.
- **Nomenclature suisse** : `check_nomenclature.py` doit rester à 0 terme. `IST` et non `MST`,
  `FSC` et non `NFS`.
- **Aucune source médicale externe au lot 2.** Le contenu dérive des critères notés, de la
  clôture et du diagnostic différentiel de la grille elle-même.
- **Cible azygos : 70–80 spans / 1000 mots.** C'est un plafond autant qu'un objectif. Si elle
  n'est atteignable qu'en colorant des mots que les autres corpus laissent en noir, s'arrêter
  au niveau le plus haut obtenu sans empâtement et consigner le chiffre.
- Le lot 1 exige `.azygos-extraction/` (49 fichiers JSON, non versionné, présent localement).
  Sans ce répertoire, `build_all.py` ne régénère rien.

---

# LOT 1 — azygos

### Tâche 1 : outil de mesure de densité

C'est l'instrument qui objective tout le lot 1 : il donne le chiffre avant, puis le chiffre
après. Il doit exister et être fiable avant toute modification du pipeline.

**Fichiers :**
- Créer : `scripts/mesure_densite.py`

**Interfaces :**
- Produit : `densite(corpus: str, bloc: str = "theorie") -> dict` renvoyant
  `{"grilles": int, "spans": int, "mots": int, "mediane": float}` ; utilisable en ligne de
  commande pour tous les corpus à la fois.

- [ ] **Étape 1 : écrire le script**

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Mesure la densité de balisage sémantique, par corpus et par bloc pédagogique.

Le NOMBRE de spans par grille ne veut rien dire : triage en a 26 par grille contre
252 pour german, mais ses sections pédagogiques font 228 mots contre 3 243. Seule la
densité rapportée au texte permet de comparer deux corpus. C'est cette mesure, et elle
seule, qui a servi à établir qu'azygos était le seul en déficit.

Usage :
    python3 scripts/mesure_densite.py                 # tous les corpus, bloc `theorie`
    python3 scripts/mesure_densite.py azygos          # un corpus
    python3 scripts/mesure_densite.py --bloc resume   # un autre bloc
"""
from __future__ import annotations

import argparse
import html
import re
import statistics
from pathlib import Path

CASES = Path(__file__).resolve().parents[1] / "cases"

CORPUS = ["amboss", "azygos", "casecos", "german", "rescos",
          "rescos-locales", "triage", "usmle"]

SPAN = re.compile(r'class="c-(?:red|pink|green|blue|amber|purple|orange|yellow)"')

#: Ouverture de chaque bloc pédagogique, et ce qui le termine. Le bornage est
#: la seule difficulté de cette mesure : trop large, il compte du texte non
#: colorisable (labels, titres de section notée) et écrase la densité.
BLOCS = {
    "resume": (r'<div class="resume">',
               r'<div class="annexes">'),
    "theorie": (r'<div class="annexe-item annexe-theorie">',
                r'<div class="annexe-item annexe-(?:expert|scenario|dd)"'
                r'|<div class="presentation-patient">'
                r'|<div class="images-wrapper">|<!--\s*COMMENTAIRE'),
    "presentation": (r'<div class="presentation-patient">',
                     r'<div class="annexe-item annexe-scenario"'
                     r'|<div class="images-wrapper">|<!--\s*COMMENTAIRE'),
}


def _zone(texte: str, bloc: str) -> str:
    ouv, fin = BLOCS[bloc]
    m = re.search(ouv, texte)
    if not m:
        return ""
    f = re.search(fin, texte[m.end():])
    return texte[m.start(): m.end() + f.start()] if f else texte[m.start():]


def _mots(segment: str) -> int:
    plat = re.sub(r"<[^>]+>", " ", segment)
    return len(re.sub(r"\s+", " ", html.unescape(plat)).split())


def densite(corpus: str, bloc: str = "theorie") -> dict:
    """Densité médiane de spans pour 1000 mots, sur les grilles qui portent le bloc."""
    spans = mots = grilles = 0
    par_grille: list[float] = []
    for fichier in sorted((CASES / corpus).glob("*.html")):
        zone = _zone(fichier.read_text(encoding="utf-8", errors="replace"), bloc)
        if not zone:
            continue
        n, m = len(SPAN.findall(zone)), _mots(zone)
        grilles += 1
        spans += n
        mots += m
        # Sous 100 mots, le rapport est trop instable pour entrer dans la médiane.
        if m >= 100:
            par_grille.append(1000 * n / m)
    return {"grilles": grilles, "spans": spans, "mots": mots,
            "mediane": statistics.median(par_grille) if par_grille else 0.0}


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("corpus", nargs="*", default=CORPUS, help="corpus à mesurer")
    ap.add_argument("--bloc", default="theorie", choices=sorted(BLOCS),
                    help="bloc pédagogique mesuré (défaut : theorie)")
    args = ap.parse_args()

    print(f"Densité de balisage sémantique — bloc `{args.bloc}`")
    print(f"{'corpus':16} {'grilles':>8} {'spans':>8} {'mots':>8} "
          f"{'spans/1000 mots':>16}")
    for nom in args.corpus:
        d = densite(nom, args.bloc)
        print(f"{nom:16} {d['grilles']:>8} {d['spans']:>8} {d['mots']:>8} "
              f"{d['mediane']:>16.1f}")


if __name__ == "__main__":
    main()
```

- [ ] **Étape 2 : exécuter et vérifier que la mesure reproduit le diagnostic**

```bash
python3 scripts/mesure_densite.py
```

Attendu — azygos autour de **39** et nettement en dessous de tous les autres, qui doivent
tomber entre 82 et 113 :

```
azygos             ~39
german             ~83
amboss             ~97
triage            ~106
casecos           ~107
rescos-locales    ~108
rescos            ~109
usmle             ~113
```

Si azygos ne ressort pas isolé en bas de tableau, **arrêter** : le bornage du bloc est faux
et toute la suite du lot reposerait sur un chiffre erroné.

- [ ] **Étape 3 : consigner la mesure de départ**

```bash
python3 scripts/mesure_densite.py azygos > /tmp/azygos-avant.txt
cat /tmp/azygos-avant.txt
```

- [ ] **Étape 4 : commit**

```bash
git add scripts/mesure_densite.py
git commit -m "Ajoute l'outil de mesure de densité sémantique"
```

---

### Tâche 2 : coloriser les labels de `rend_theorie`

11 % du texte du bloc `theorie` est en labels `<strong>`, passés par `lib.echappe()` et jamais
par le lexique. Ce sont les intitulés cliniques — le vocabulaire le plus dense du bloc, écarté
par construction.

**Fichiers :**
- Modifier : `scripts/azygos/build_grid.py:332-345`

**Interfaces :**
- Consomme : `lex.colorise(texte: str) -> str` (échappe et enveloppe ; ne jamais lui passer du
  texte déjà échappé, cf. sa docstring).
- Produit : aucune nouvelle interface.

- [ ] **Étape 1 : relire le code visé**

```bash
sed -n '325,350p' scripts/azygos/build_grid.py
```

Deux occurrences de `lib.echappe` à l'intérieur d'un `<strong>` : celle du label de
sous-groupe (`item['label_sous_groupe']`) et celle du label d'item (`label`).

- [ ] **Étape 2 : remplacer les deux échappements par une colorisation**

Dans le `<li class="theorie-sous-groupe">` :

```python
                    lignes.append(
                        f'<li class="theorie-sous-groupe">'
                        f"<strong>{lex.colorise(item['label_sous_groupe'])}</strong> — "
                        f"{lex.colorise(item['info_sous_groupe'])}</li>"
                    )
```

Et dans le `<li>` d'item :

```python
                lignes.append(
                    f"<li><strong>{lex.colorise(label)}</strong> — "
                    f"{lex.colorise(item['info'])}</li>"
                )
```

`colorise()` échappe déjà son entrée : `lib.echappe` disparaît, il n'est pas cumulé.

- [ ] **Étape 3 : ne PAS coloriser le titre d'onglet**

Laisser `lib.echappe(lib.nettoie_onglet(onglet))` intact dans le `<h4>`. Les titres de section
ne sont colorisés dans aucun corpus ; les colorer ici créerait une divergence visible.

- [ ] **Étape 4 : régénérer une seule grille et mesurer l'effet isolé**

```bash
python3 - <<'PY'
import sys, json; sys.path.insert(0, "scripts/azygos")
import lib_azygos as lib
from build_grid import construit
inv = json.loads((lib.RACINE / "scripts/azygos/inventaire.json").read_text(encoding="utf-8"))
fiche = inv["cas"][9]                       # AZYGOS-10, cas témoin
data = json.loads((lib.EXTRACTION / f"{fiche['id']}.json").read_text(encoding="utf-8"))
construit(10, fiche, data)
print("AZYGOS-10 régénérée")
PY
python3 scripts/mesure_densite.py azygos
```

Attendu : la médiane monte de quelques points. Une seule grille sur 49 régénérée ne déplace
pas beaucoup la médiane — c'est normal, l'objet de cette étape est de vérifier que le HTML
produit reste valide et que rien ne casse.

- [ ] **Étape 5 : vérifier qu'aucun span n'est imbriqué dans un autre**

```bash
grep -o '<span class="c-[a-z]*"><span class="c-' cases/azygos/AZYGOS-10*.html | wc -l
```

Attendu : `0`. Une imbrication signalerait que `colorise()` a reçu du texte déjà colorisé.

- [ ] **Étape 6 : commit**

```bash
git add scripts/azygos/build_grid.py cases/azygos/
git commit -m "Colorise les labels du bloc théorie d'azygos"
```

---

### Tâche 3 : enrichir le lexique pour le raisonnement clinique

Les `infos` d'azygos ne sont pas du texte de résumé mais des justifications de raisonnement
(« pourquoi cette question », « ce qu'oriente telle réponse »). Le lexique, réglé sur du texte
de résumé, y reconnaît moins d'entités. On lui ajoute le vocabulaire de ce registre.

**Fichiers :**
- Modifier : `scripts/azygos/lexique_semantique.py` — liste `REGLES`, et `EXCLUS` si besoin.

**Interfaces :**
- Consomme : `_mots(*termes) -> str`, qui pose les frontières `\b` — indispensables, sans quoi
  « CT » se retrouve dans « conta**ct** ».
- Produit : `REGLES` étendue. L'ordre reste **du spécifique au général** ; le moteur retient la
  correspondance la plus longue, puis la première déclarée.

- [ ] **Étape 1 : relever le vocabulaire réellement présent et non couvert**

```bash
python3 - <<'PY'
import re, sys, html, collections
from pathlib import Path
sys.path.insert(0, "scripts/azygos")
import lexique_semantique as lex

mots = collections.Counter()
for f in sorted(Path("cases/azygos").glob("*.html")):
    t = f.read_text(encoding="utf-8", errors="replace")
    m = re.search(r'<div class="annexe-item annexe-theorie">', t)
    if not m:
        continue
    fin = re.search(r'<div class="annexe-item annexe-expert">|<!--\s*COMMENTAIRE', t[m.start():])
    zone = t[m.start(): m.start() + fin.start()] if fin else t[m.start():]
    # Texte HORS des spans déjà posés : c'est là que se trouve le manque.
    nu = re.sub(r'<span class="c-[a-z]+">.*?</span>', " ", zone, flags=re.S)
    nu = re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", " ", nu)))
    for w in re.findall(r"[a-zà-ÿ][a-zà-ÿ'’-]{4,}", nu.lower()):
        mots[w] += 1
for mot, n in mots.most_common(120):
    print(f"{n:>5}  {mot}")
PY
```

- [ ] **Étape 2 : ajouter les règles**

Les insérer dans `REGLES` **dans la famille correspondante**, avant les motifs génériques de
cette famille. Point de départ, à ajuster selon le relevé de l'étape 1 :

```python
    # ---- examen / normal / score : le vocabulaire de l'orientation --------
    ("c-green", _mots(
        r"anamnèse (?:ciblée|systématique|par systèmes?)", r"inspection",
        r"palpation", r"percussion", r"auscultation", r"otoscopie",
        r"acuité visuelle", r"champ visuel", r"réflexe photomoteur",
        r"paramètres? vitaux?", r"status neurologique", r"examen au spéculum",
    )),

    # ---- symptôme / signe : les descripteurs sémiologiques ---------------
    ("c-pink", _mots(
        r"unilatéral(?:e|es|aux)?", r"bilatéral(?:e|es|aux)?",
        r"aigu[ëe]?s?", r"chronique[s]?", r"brutal(?:e|es|aux)?",
        r"progressi(?:f|ve|ves)", r"irradiation", r"prodrome[s]?",
        r"intermittent(?:e|es|s)?", r"permanent(?:e|es|s)?",
    )),

    # ---- concept-clé : ce que la justification veut faire retenir --------
    ("c-yellow", r"\bcritères? de gravité\b"),
    ("c-yellow", r"\bà (?:éliminer|écarter) (?:en priorité|d[e’']emblée)\b"),
    ("c-yellow", r"\bdiagnostic d[e’']exclusion\b"),
```

- [ ] **Étape 3 : vérifier qu'aucun faux ami n'est attrapé**

```bash
python3 - <<'PY'
import sys; sys.path.insert(0, "scripts/azygos")
import lexique_semantique as lex
temoins = [
    "Le patient nécessite une prise en charge.",       # -ite : PAS une inflammation
    "La visite se déroule au cabinet.",
    "La main droite est normale.",
    "Il évite les contacts.",
    "La dose a été réduite.",
]
for phrase in temoins:
    sortie = lex.colorise(phrase)
    print(("KO  " if "<span" in sortie else "ok  ") + sortie)
PY
```

Attendu : **cinq lignes `ok`**. Toute ligne `KO` demande d'ajouter le mot à `EXCLUS`.

- [ ] **Étape 4 : mesurer le rendement des nouvelles règles avant de régénérer**

```bash
python3 - <<'PY'
import re, sys, html, statistics
from pathlib import Path
sys.path.insert(0, "scripts/azygos")
import lexique_semantique as lex
d = []
for f in sorted(Path("cases/azygos").glob("*.html")):
    t = f.read_text(encoding="utf-8", errors="replace")
    m = re.search(r'<div class="annexe-item annexe-theorie">', t)
    if not m: continue
    fin = re.search(r'<div class="annexe-item annexe-expert">|<!--\s*COMMENTAIRE', t[m.start():])
    zone = t[m.start(): m.start()+fin.start()] if fin else t[m.start():]
    txt = re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", " ", zone)))
    n = len(txt.split())
    if n >= 100:
        d.append(1000 * len(re.findall(r'<span class="c-', lex.colorise(txt))) / n)
print(f"rendement simulé du lexique : {statistics.median(d):.1f} spans / 1000 mots")
PY
```

Attendu : **entre 70 et 80**. Sous 70, ajouter des règles et refaire l'étape 3. Au-dessus de
85, en retirer : la contrainte globale fait de 80 un plafond.

- [ ] **Étape 5 : commit**

```bash
git add scripts/azygos/lexique_semantique.py
git commit -m "Étend le lexique sémantique au vocabulaire du raisonnement clinique"
```

---

### Tâche 4 : régénérer azygos et rejouer les portes

**Fichiers :**
- Modifier : `cases/azygos/*.html` (49 fichiers, par génération)

**Interfaces :**
- Consomme : `build_all.py`, qui lit `.azygos-extraction/*.json` et
  `scripts/azygos/inventaire.json`.

- [ ] **Étape 1 : vérifier que les sources d'extraction sont là**

```bash
ls .azygos-extraction/*.json | wc -l
```

Attendu : `49`. Si le compte est inférieur, **arrêter** — `build_all.py` saute silencieusement
les cas sans source, et le corpus se retrouverait amputé.

- [ ] **Étape 2 : régénérer**

```bash
python3 scripts/azygos/build_all.py
```

- [ ] **Étape 3 : mesurer après, et comparer au chiffre de départ**

```bash
cat /tmp/azygos-avant.txt
python3 scripts/mesure_densite.py azygos
```

Attendu : la médiane passe de ~39 à **70–80**. Si elle dépasse 85, revenir à la tâche 3 et
retirer des règles.

- [ ] **Étape 4 : vérifier que le texte visible n'a pas changé**

```bash
python3 - <<'PY'
import re, html, subprocess
from pathlib import Path

def visible(txt):
    b = re.sub(r"<script.*?</script>|<style.*?</style>", "", txt, flags=re.S)
    return re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", " ", b))).strip()

ecarts = 0
for f in sorted(Path("cases/azygos").glob("*.html")):
    avant = subprocess.run(["git", "show", f"HEAD:{f}"], capture_output=True,
                           text=True).stdout
    if not avant:
        continue
    if visible(avant) != visible(f.read_text(encoding="utf-8")):
        ecarts += 1
        print("TEXTE MODIFIÉ :", f.name)
print(f"{ecarts} grille(s) dont le texte visible a changé")
PY
```

Attendu : **0**. Le balisage enveloppe, il ne réécrit pas. Toute grille listée ici est un
défaut à instruire avant de continuer.

- [ ] **Étape 5 : rejouer les portes**

```bash
python3 scripts/azygos/check_invariants.py
node scripts/rescos-locales/browser_probe.js AZYGOS --summary
```

Attendu : `check_invariants` en code 0 ; le probe rend 0 exception et 100 % après remplissage.

> `browser_probe.js` vit dans `scripts/rescos-locales/` mais sert n'importe quel chemin de
> `cases/` : son filtre est un simple test de sous-chaîne sur le nom de fichier.

- [ ] **Étape 6 : commit**

```bash
git add cases/azygos/
git commit -m "Régénère azygos avec le lexique enrichi"
```

---

# LOT 2 — les 20 grilles sans contenu pédagogique

### Tâche 5 : le script d'injection

**Fichiers :**
- Créer : `scripts/peda/inject_peda_blocks.py`
- Créer : `scripts/peda/contenu/__init__.py` (vide)

**Interfaces :**
- Consomme : `lexique_semantique.colorise(texte) -> str`.
- Produit :
  - `rend(contenu: dict) -> str` — fabrique le HTML des trois blocs.
  - `injecte(html: str, bloc: str) -> tuple[str, str]` — renvoie `(html_modifié, état)` où
    `état` vaut `"ok"`, `"remplacé"` ou un motif d'échec. Même contrat que
    `scripts/inject_semantic_css.py`.
  - Format de `contenu`, respecté par tous les fichiers de `scripts/peda/contenu/` :

```python
CONTENU = {
    "grille": "rescos-locales/Psy-Vignette 10 - Une femme triste - Grille ECOS.html",
    "titre_resume": "Épisode dépressif majeur – Résumé ECOS",
    "resume": [
        ("🔍 Anamnèse", [
            ("Symptômes cardinaux", ["texte brut, colorisé automatiquement", "…"]),
            ("Ce qu'il faut avoir demandé", ["…"]),
        ]),
        ("⚙️ Prise en charge", [("Traitement", ["…"])]),
    ],
    "points_cles": ["…"],
    "checklist": [("Questions à poser", ["…"]), ("Examens à faire", ["…"])],
    "theorie": [("Titre de section", "paragraphe", ["puce", "puce"])],
    "presentation": {
        "checklist_mentale": ["…"],
        "mnemo": ("Titre du mnémo", ["L = …", "O = …"]),
        "version_longue": ["paragraphe", "paragraphe"],
        "sbar": {"S": "…", "B": "…", "A": "…", "R": "…"},
        "questions": [("Question de l'examinateur", "réponse")],
    },
}
```

- [ ] **Étape 1 : écrire le script**

Le HTML produit suit exactement le gabarit de RESCOS-70 — mêmes classes, même ordre. Le
marqueur d'insertion est `<!-- COMMENTAIRE GÉNÉRAL -->`, et le bloc s'insère juste avant :

```html
<!-- peda:début -->
<div class="resume">
<h3 class="resume-main-title">📚 🔥 {titre_resume}</h3>
<div class="resume-content">
  <div class="resume-section section-anamnese">
    <h4 class="section-title">{titre de section}</h4>
    <div class="resume-subsection">
      <h5 class="subsection-title">{titre de sous-section}</h5>
      <ul class="resume-subsection-points"><li>{puce colorisée}</li></ul>
    </div>
  </div>
  <div class="resume-section">
    <h4 class="section-title">✅ Points clés ECOS</h4>
    <ul class="resume-points"><li class="resume-bullet">{puce}</li></ul>
  </div>
  <div class="resume-section">
    <h4 class="section-title">📋 Check-list rapide ECOS</h4>
    <div class="resume-subsection">…</div>
  </div>
</div>
</div>
<div class="annexes">
<h3>Annexes</h3>
<div class="annexes-grid">
<div class="annexe-item annexe-theorie">
  <div class="annexe-title">Points théoriques et pratiques</div>
  <div class="annexe-theorie-content">
    <div class="theorie-section"><h4>{titre}</h4><p>{paragraphe}</p><ul><li>{puce}</li></ul></div>
  </div>
</div>
<div class="presentation-patient">
  <h3 class="presentation-main-title">📑 Fiche ECOS – Cas : {titre}</h3>
  <div class="presentation-content">
    <div class="presentation-section section-checklist">
      <h4 class="presentation-section-title">🧩 Checklist mentale (présentation systématisée)</h4>
      <ul class="presentation-points"><li>{item}</li></ul>
      <div class="mnemo-box">
        <div class="mnemo-title">💡 👉 Mnémo {nom}</div>
        <ul class="mnemo-items"><li>{ligne}</li></ul>
      </div>
    </div>
    <div class="presentation-section section-longue">
      <h4 class="presentation-section-title">🎤 Version longue (≈2-3 min)</h4>
      <div class="presentation-content"><p>{paragraphe}</p></div>
    </div>
    <div class="presentation-section section-express">
      <h4 class="presentation-section-title">⚡ Version express (SBAR, 30 sec)</h4>
      <div class="presentation-content"><p>S (Situation) : …</p><p>B (Background) : …</p>
      <p>A (Assessment) : …</p><p>R (Recommendation) : …</p></div>
    </div>
    <div class="presentation-section section-questions">
      <h4 class="presentation-section-title">❓ Questions probables de l'examinateur (avec réponses orales)</h4>
      <div class="presentation-subsection"><h5>{intitulé}</h5>
        <div class="qa-container"><div class="presentation-qa">
          <div class="presentation-question"><span class="q-number">Q1</span>
            <span class="q-text">{question}</span></div>
          <div class="presentation-reponse text">{réponse colorisée}</div>
        </div></div>
      </div>
    </div>
  </div>
</div>
</div>
</div>
<!-- peda:fin -->
```

Le nombre d'ouvertures et de fermetures `<div>` doit s'équilibrer : le vérifier avant écriture,
un déséquilibre casserait le découpage par `bounds_anomalies()` de tout le corpus.

Points non négociables du script :
- `MARQUE_DEBUT = "<!-- peda:début -->"` et `MARQUE_FIN = "<!-- peda:fin -->"` encadrent le
  bloc injecté ;
- si la marque est déjà présente, remplacer le bloc au lieu d'en ajouter un second ;
- contrôle d'inversibilité avant écriture — retirer le bloc doit redonner l'entrée à l'octet
  près ;
- tout texte passe par `lex.colorise()`, jamais par `html.escape()` seul, **sauf** les titres
  de section, qui ne sont colorisés dans aucun corpus.

- [ ] **Étape 2 : vérifier l'idempotence sur une copie**

```bash
cp "cases/rescos-locales/Psy-Vignette 10 - Une femme triste - Grille ECOS.html" /tmp/pilote.html
python3 scripts/peda/inject_peda_blocks.py psy-vignette-10 --cible /tmp/pilote.html
cp /tmp/pilote.html /tmp/pilote-1.html
python3 scripts/peda/inject_peda_blocks.py psy-vignette-10 --cible /tmp/pilote.html
diff /tmp/pilote.html /tmp/pilote-1.html && echo "IDEMPOTENT"
```

Attendu : `IDEMPOTENT`.

- [ ] **Étape 3 : vérifier que les sections notées sont intactes**

```bash
python3 - <<'PY'
import re
avant = open("cases/rescos-locales/Psy-Vignette 10 - Une femme triste - Grille ECOS.html",
             encoding="utf-8").read()
apres = open("/tmp/pilote.html", encoding="utf-8").read()
for motif, nom in [(r'<div class="criteria-row"', "criteria-row"),
                   (r'<input type="radio"', "radio"),
                   (r'<input type="checkbox"', "checkbox")]:
    a, b = len(re.findall(motif, avant)), len(re.findall(motif, apres))
    print(f"{nom:14} avant {a:>4}  après {b:>4}  {'OK' if a == b else 'ÉCART'}")
cfg_a = re.search(r"window\.caseConfig\s*=\s*\{.*?\};", avant, re.S)
cfg_b = re.search(r"window\.caseConfig\s*=\s*\{.*?\};", apres, re.S)
print("caseConfig    ", "identique" if (cfg_a and cfg_b and cfg_a.group() == cfg_b.group())
      else "MODIFIÉ")
PY
```

Attendu : trois `OK` et `identique`.

- [ ] **Étape 4 : commit**

```bash
git add scripts/peda/
git commit -m "Ajoute l'injecteur de blocs pédagogiques"
```

---

### Tâche 6 : le pilote — Psy-Vignette 10

**Fichiers :**
- Créer : `scripts/peda/contenu/psy_vignette_10.py`
- Modifier : `cases/rescos-locales/Psy-Vignette 10 - Une femme triste - Grille ECOS.html`
- Modifier : `scripts/rescos-locales/baseline.json` (régénéré)

**Sources à lire avant d'écrire — et les seules autorisées :**
- Les critères notés de la grille : sections Anamnèse (40 pts), Examen, Management,
  Communication.
- Le bloc `cloture` : clôture type, questions difficiles de la patiente, réponse type.
- Le bloc `annexe-dd` : critères DSM-5 cochés (9/9), sévérité modérée à sévère, PHQ-9 estimé
  15–20, diagnostics différentiels avec leurs arguments.

Faits déjà portés par la grille, à reprendre sans les inventer : Madame D, 45 ans, fatigue et
symptômes dépressifs depuis 3 mois ; perte de 8 kg ; insomnie ; ralentissement psychomoteur ;
idéation suicidaire présente ; épisode traité il y a 10 ans ; proposition d'antidépresseur plus
psychothérapie plus arrêt de travail temporaire.

- [ ] **Étape 1 : lire les trois sources**

```bash
python3 - <<'PY'
import re, html
from pathlib import Path
p = Path("cases/rescos-locales/Psy-Vignette 10 - Une femme triste - Grille ECOS.html")
t = p.read_text(encoding="utf-8")
b = re.sub(r"<script.*?</script>|<style.*?</style>", "", t, flags=re.S)
b = re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", " ", b)))
print(b)
PY
```

- [ ] **Étape 2 : écrire le contenu**

Trois blocs au format de la tâche 5. Volume cible : **1 200 à 1 800 mots**, l'ordre de
grandeur de rescos (1 644 mots médians). Écrire en texte brut — aucune balise, aucune classe
`c-*` posée à la main : le lexique s'en charge.

Règle de fond : **toute affirmation doit être traçable** à un critère noté, à la clôture ou au
diagnostic différentiel de cette grille. Les rappels physiopathologiques sont admis quand ils
relient deux faits déjà présents ; l'ajout d'un fait clinique nouveau ne l'est pas.

- [ ] **Étape 3 : injecter**

```bash
python3 scripts/peda/inject_peda_blocks.py psy-vignette-10
```

- [ ] **Étape 4 : mesurer la densité obtenue**

```bash
python3 scripts/mesure_densite.py rescos-locales --bloc resume
python3 scripts/mesure_densite.py rescos-locales --bloc theorie
```

Attendu : la médiane du corpus reste autour de **107**. Une grille sur 166 ne la déplace pas ;
la vérification porte sur le fait que la grille pilote elle-même n'en soit pas très éloignée.

- [ ] **Étape 5 : rejouer les portes du corpus**

```bash
python3 scripts/rescos-locales/check_reachability.py "Psy-Vignette 10"
python3 scripts/rescos-locales/check_nomenclature.py
python3 scripts/rescos-locales/check_no_loss.py
python3 scripts/rescos-locales/check_invariants.py
```

`check_reachability`, `check_nomenclature` et `check_no_loss` doivent être verts — ce dernier
prouve qu'aucun item de liste préexistant n'a disparu, ce qu'une insertion mal bornée pourrait
provoquer. **`check_invariants` va échouer** sur le champ `blocks` de cette grille : c'est
attendu, trois blocs ont été ajoutés.

- [ ] **Étape 6 : régénérer le snapshot et inspecter son diff**

```bash
python3 scripts/rescos-locales/snapshot_invariants.py
git diff --stat scripts/rescos-locales/baseline.json
git diff scripts/rescos-locales/baseline.json | grep '^-' | grep -v '^---'
```

Attendu : le diff ne touche **que** l'entrée de Psy-Vignette 10. Toute ligne supprimée
concernant une autre grille est une régression — arrêter et instruire.

- [ ] **Étape 7 : contrôle en navigateur**

```bash
node scripts/rescos-locales/browser_probe.js "Psy-Vignette 10" --deep --summary
```

Attendu : 0 exception, 100 % après remplissage, registre écrit.

- [ ] **Étape 8 : faire relire par l'auteur du dépôt**

Livrer le fichier et attendre validation du **format et du fond**. Ne pas enchaîner sur la
tâche 7 sans cet accord : le format validé ici est celui des 19 grilles suivantes.

- [ ] **Étape 9 : commit**

```bash
git add scripts/peda/contenu/psy_vignette_10.py \
        "cases/rescos-locales/Psy-Vignette 10 - Une femme triste - Grille ECOS.html" \
        scripts/rescos-locales/baseline.json
git commit -m "Dote Psy-Vignette 10 de ses blocs pédagogiques"
```

---

### Tâches 7 à 10 : les 19 grilles restantes

Quatre lots, un commit et une relecture par lot. **Chaque lot répète intégralement les
étapes 1 à 9 de la tâche 6**, une fois par grille, avec les portes du corpus concerné.

| Tâche | Grilles | Corpus | Portes à rejouer |
|---|---|---|---|
| 7 | Psy-Vignette 1 à 5 | rescos-locales | `scripts/rescos-locales/` |
| 8 | Psy-Vignette 6 à 9, Pédiatrie — Enfant 3 ans avec toux | rescos-locales | `scripts/rescos-locales/` |
| 9 | Pédiatrie — Nourrisson 6 mois avec fièvre, Diabète — hyperglycémie nouvelle, RESCOS-57, RESCOS-64 station 2, ECOS Diag 1 | rescos-locales puis casecos | les deux jeux |
| 10 | ECOS Diag 2, ECOS Diag 3, RESCOS-29, RESCOS-11 | casecos puis rescos | les deux jeux |

**Points d'attention par tâche :**

- **Tâche 9 et 10 franchissent une frontière de corpus.** ECOS Diag 1–3 sont dans `casecos`,
  RESCOS-11 et RESCOS-29 dans `rescos`. Chacun a son propre `baseline.json` et ses propres
  scripts de contrôle : `scripts/casecos/` et `scripts/rescos/`. Rejouer les portes du bon
  corpus, régénérer le bon snapshot.
- **RESCOS-29 et RESCOS-57 ont déjà `expert` et `scenario`.** Les blocs ajoutés s'insèrent
  avant `<!-- COMMENTAIRE GÉNÉRAL -->`, donc après eux — vérifier que l'ordre rendu reste
  `resume` → `annexes` → `expert` → `theorie` → `presentation` → `scenario`, conforme aux
  autres grilles du corpus.
- **ECOS Diag 1 à 3 et RESCOS-64 n'ont aucun bloc** : ni clôture, ni diagnostic différentiel.
  La rédaction s'appuie alors uniquement sur les critères notés. Si les critères ne suffisent
  pas à établir le diagnostic retenu, **ne pas l'inventer** : le signaler et laisser la grille
  de côté.
- **RESCOS-11 en dernier.** 805 mots au total, aucun bloc : c'est le cas le plus exposé à
  l'invention de tout le dépôt. Le traiter quand le format est stabilisé, et signaler
  explicitement s'il n'y a pas matière à rédiger honnêtement.

---

## Vérification finale du chantier

- [ ] **Mesure globale**

```bash
python3 scripts/mesure_densite.py
python3 scripts/mesure_densite.py --bloc resume
python3 scripts/mesure_densite.py --bloc presentation
```

Attendu : azygos entre 70 et 80 sur `theorie` ; aucun autre corpus n'a baissé.

- [ ] **Portes des trois corpus touchés**

```bash
for c in rescos casecos rescos-locales; do
  echo "=== $c ==="
  python3 "scripts/$c/check_invariants.py"   | tail -1
  python3 "scripts/$c/check_reachability.py" | tail -1
  python3 "scripts/$c/check_nomenclature.py" | tail -1
done
python3 scripts/azygos/check_invariants.py | tail -1
```

- [ ] **Décompte des grilles sans contenu pédagogique**

```bash
python3 - <<'PY'
import re
from pathlib import Path
reste = []
for f in sorted(Path("cases").glob("*/*.html")):
    t = f.read_text(encoding="utf-8", errors="replace")
    if "Feuille porte" in f.name:
        continue
    if not re.search(r'<div class="(?:resume|annexe-item annexe-theorie|presentation-patient)"', t):
        reste.append(f.name)
print(f"{len(reste)} grille(s) encore sans bloc pédagogique")
for n in reste:
    print("   ", n)
PY
```

Attendu : **0**, sauf les grilles explicitement laissées de côté faute de matière — auquel cas
elles sont nommées dans le message de commit du lot correspondant.

- [ ] **Mettre à jour la spec**

Passer son statut de « design validé, implémentation à planifier » à « implémenté le
2026-XX-XX », et y consigner la densité azygos réellement obtenue.
