# Procédure de traitement d'une grille RESCOS

Volet RESCOS de la procédure. Il ne remplace pas
`scripts/amboss/PROCEDURE.md` : il en note les écarts. Tout ce qui n'est pas
mentionné ici s'y transpose tel quel — le contrat de rôle des blocs, la
hiérarchie à trois niveaux, la règle de dédoublonnage, les interdits.

**Corpus : 41 grilles**, `cases/rescos/RESCOS-*.html`, dont une `RESCOS-9b`
(le tri de `lib.grids()` est un couple `(numéro, suffixe)`, pas un entier).

---

## 0. Ce qui change par rapport à AMBOSS, en une page

RESCOS est **structurellement proche d'AMBOSS**, contrairement à German : les
trois fiches de fin de page existent, la zone pédagogique s'ouvre sur
`resume`/`annexes`, et `annexe-dd` vit dans la section Management. Quatre
écarts seulement :

| | AMBOSS | German | RESCOS |
|---|---|---|---|
| grilles | 40 | 88 | **41** |
| `annexe-expert` | 40 | 0 | **39** |
| `annexe-theorie` | 40 | 0 | **37** |
| `annexe-scenario` | 40 | 0 | **39** |
| `resume` | 25 | 14 | **25** |
| `presentation-patient` | 24 (+1 variante) | 10 | **25** |
| `annexe-dd` | 40 | 78 seg. / 77 gr. | **22** |
| `therapy-section` | (non couvert) | 126 seg. / 44 gr. | **47 seg. / 16 gr.** |
| `redflags-section` | (non couvert) | 10 / 10 | **6 / 6** |
| `cloture-item` | (non couvert) | — | **40 seg. / 13 gr.** |
| `annexe-image` | — | oui | **33 seg. / 12 gr.** |
| fin de zone pédagogique | `annexe-scenario` | `<!-- COMMENTAIRE GÉNÉRAL -->` | **`<!-- COMMENTAIRE GÉNÉRAL -->`** (41/41) |
| `caseConfig` | 40/40 | 88/88 | **39/41** |

Les quatre écarts :

1. **`cloture` est un bloc inédit** — absent du `BLOCKS` d'AMBOSS comme de
   celui de German. 40 segments sur 13 grilles, logés dans une cinquième
   section de page `<div class="section cloture-section">` (« Clôture de
   consultation »), placée entre Management et Communication. Cette section
   **ne porte aucun critère noté** (0 `criteria-row`, 0 `criteria-text`,
   0 `<input>`) : c'est du contenu rédactionnel pur — explication au patient,
   questions du patient, réponses adaptées.
2. **`therapy` et `redflags`** sont ceux de German, logés dans un
   `criteria-row` de la section notée.
   ⚠️ `grep -l therapy-section` rend **18** grilles ; le compte réel est **16**.
   Deux grilles ne portent la chaîne que dans leur feuille de style. Le compte
   qui fait foi est celui des `class="therapy-section"`.
3. **`annexe-dd` a deux emplacements** : 20 grilles le placent dans Management
   (fin sur le `criteria-row` suivant, comme AMBOSS) ; **RESCOS-14 et
   RESCOS-24** le placent en fin de page, *dans* `annexes-grid`, après la
   `presentation` — sa fin y tombe sur `annexe-scenario`. Conséquence :
   `peda_bounds()` et `dd_bounds()` **se recouvrent** sur ces deux grilles.
   Ne jamais concaténer les deux zones sans dédoublonner ; passer par
   `block_spans()`.
4. **Deux grilles n'ont pas de `caseConfig`** — voir § 5.

---

## 1. Situer les blocs — lecture ciblée, jamais le fichier entier

Identique à German. Une grille RESCOS pèse 55 à 105 ko, dont l'essentiel en
data-URI d'images. **Ne jamais ouvrir une grille entière avec `Read`.**

```python
import sys; sys.path.insert(0, "scripts/rescos")
import lib_rescos as lib
html = lib.strip_base64(path.read_text(encoding="utf-8"))
for start, end in lib.block_spans(html, "resume"):
    print(html[:start].count("\n") + 1, html[:end].count("\n") + 1)
```

`block_spans()` rend des **index de caractères** ; les convertir en numéros de
ligne pour `Read`, comme dans AMBOSS § 1.

---

## 2. Les dix blocs, leurs bornes, leur rôle

Le découpage se fait par **équilibrage des `<div>`** (`_balanced_end`), pas par
le motif de fin. Les 41 grilles sont globalement équilibrées : **0 écart entre
`<div` et `</div>`, 41 fois sur 41**. La « queue attendue » de `BLOCKS` est
vérifiée par `bounds_anomalies()` à chaque passage de `check_invariants.py`.

Relevé de référence — **313 segments**, 0 anomalie de borne, 0 classe de
contenu hors bloc :

| bloc | segments / grilles | items | rôle |
|---|---|---|---|
| `annexe-dd` | 22 / 22 | 590 | hypothèses diagnostiques, POUR/CONTRE |
| `redflags` | 6 / 6 | 26 | signes d'alarme, dans un `criteria-row` |
| `therapy` | 47 / 16 | 183 | réponse thérapeutique attendue, idem |
| `cloture` | 40 / 13 | 44 | clôture de consultation (bloc inédit) |
| `resume` | 25 / 25 | 1097 | fiche de synthèse, 6 sections |
| `expert` | 39 / 39 | 627 | Rôles / Points clés / Pièges |
| `theorie` | 37 / 37 | 1555 | rappels théoriques |
| `presentation` | 25 / 25 | 1259 | présentation orale, 5 sections |
| `scenario` | 39 / 39 | 1214 | script du patient simulé |
| `annexe-image` | 33 / 12 | 33 | images et tableaux de laboratoire |
| **total** | **313** | **6628** | 518 901 caractères de texte visible |

### `scenario` est borné mais exclu de la redondance

`report_redundancy.py` l'écarte par défaut (`lib.REDUNDANCY_EXCLUDED`) :
redire les symptômes déjà listés dans le `resume` est la fonction même du
script du patient. AMBOSS l'exclut déjà de fait. Le bloc **reste dans
`BLOCKS`** : borné, gelé au snapshot, vérifié par `bounds_anomalies`, protégé
par `check_no_loss`. Ce n'est pas un angle mort, c'est une exclusion
documentée ; `--with-scenario` la lève (610 → 689 paires).

---

## 3. Dédoublonner

Contrat de rôle et méthode identiques à AMBOSS § 3. Seuil et unité inchangés
(`SequenceMatcher > 0.72`, items de ≥ 18 caractères), pour que les trois
corpus se lisent dans la même unité.

**Mesure initiale : 610 paires inter-blocs, 323 intra-bloc.** Restreinte aux
cinq blocs que mesure AMBOSS (`annexe-dd`, `resume`, `expert`, `theorie`,
`presentation`), la mesure comparable est de **578 paires** — à comparer aux
**301 paires de départ d'AMBOSS** pour 40 grilles. La redondance de RESCOS est
donc environ **deux fois** celle d'AMBOSS à l'entrée du chantier.

Les trois couples qui portent 72 % du total :

| couple | paires |
|---|---|
| `presentation` ↔ `resume` | 153 |
| `annexe-dd` ↔ `presentation` | 141 |
| `presentation` ↔ `theorie` | 80 |

`presentation` est impliquée dans 440 des 610 paires : c'est le bloc par
lequel commencer.

---

## 4. Vérifier

```bash
python3 scripts/rescos/check_invariants.py        # gèle 41 grilles
python3 scripts/rescos/check_reachability.py      # barème atteignable ?
python3 scripts/rescos/check_nomenclature.py      # termes non suisses
python3 scripts/rescos/report_redundancy.py --intra --quiet
python3 scripts/rescos/check_no_loss.py <REF>     # rapport, sortie 0
python3 scripts/rescos/report_import_defects.py --quiet
```

Après toute modification d'un fichier sous `scripts/rescos/`, **relancer aussi
les vérificateurs d'AMBOSS et de German** : leurs mesures publiées (147 et 14
paires inter-blocs) ne doivent jamais bouger.

`snapshot_invariants.py` gèle, en plus des champs d'AMBOSS :
`sectionCounts` (le champ qui rendait AMBOSS-9 faux), `configForm`
(`caseConfig` / `inline`), le **nombre de segments** par bloc, et les deux
champs qui doivent rester vides — `boundsAnomalies` et `uncoveredContent`.

---

## 5. Le barème — deux formes de déclaration

39 grilles portent un `window.caseConfig` de la forme d'AMBOSS et délèguent le
calcul à `cases/scoring.js`.

**RESCOS-7 et RESCOS-9 n'ont aucun `caseConfig`** — cas inédit, aucune grille
des deux corpus précédents n'en manquait. Elles ne sont pas pour autant sans
barème : chacune embarque sa **propre copie de `calculateScores()`**, où la
configuration est construite ligne à ligne au lieu d'être déclarée :

```javascript
maxScores["anamnese"] = 41;
coef["anamnese"] = 0.7;
sectionInfo.push({key: "anamnese", prefix: "a", count: 14, label: "Anamnèse"});
```

Le corps de la fonction est **identique** à `cases/scoring.js` — même
traitement des cases de détail, même repli sur les radios, même table
communication A=4…E=0, même pondération. **Le barème y est parfaitement
calculable** et `check_reachability.py` s'y applique sans réserve : seul
`parse_config` lit l'autre forme. Les deux grilles sortent à 100 %.

> Ne pas les traiter comme « hors du domaine du vérificateur » : ce serait
> renoncer à contrôler deux barèmes qui se contrôlent très bien.

### Le quatrième écart : la section vide pondérée

Aux trois écarts d'AMBOSS (`count` trop grand, sous-item orphelin, `maxScores`
divergeant du `<span>`) s'en ajoute un, propre à ce corpus : une section
**déclarée vide** (`count: 0`, `maxScores: 0`, « Score : 0/0 », aucun critère)
qui **conserve son coefficient**. `scoring.js` calcule
`max > 0 ? (score/max)*100 : 0` : le pourcentage vaut 0 quoi que fasse le
candidat, et sa part de coefficient est perdue.

Ce cas passe les trois contrôles précédents sans bruit (0 == 0 == 0 pour la
section) et n'est visible que par le total global.
`empty_weighted_sections()` le nomme explicitement.

---

## 6. Pièges — ceux d'AMBOSS, et ce que RESCOS y ajoute

Tous les pièges d'AMBOSS § 6 et de German § 6 restent valables. Ce corpus en
rejoue trois et en ajoute deux.

* **Chevron nu** — 114 occurrences sur 30 grilles (`Hb < 10.5 g/dL`,
  `< 3 selles/semaine`). Un `re.sub(r'<[^>]+>', ...)` naïf avale la clause qui
  suit. **Importer `visible_text` de `lib_amboss`, ne jamais le recopier.** Le
  sous-cas résiduel (`<` collé à une lettre) est à zéro.
* **base64** — jamais de `grep` brut. Toujours `strip_base64` d'abord.
* **Puces textuelles `•`** — `annexe-dd` et `therapy` ne les balisent pas en
  `<li>`. `list_items()` les découpe.
* **`grep -l` compte les feuilles de style** — `therapy-section` : 18 grilles
  au `grep`, 16 en réalité. Compter les `class="…"`, jamais la chaîne nue.
* **`cloture-content` n'est ni `<li>` ni puce** — comme `redflags-text` dans
  German. Sans l'extension `_DIV_ITEM` de `list_items()`, les 13 blocs
  `cloture` rendraient zéro item et seraient invisibles à la redondance comme
  à `check_no_loss`.
* **Faux positifs** — un « texte tronqué » signalé par
  `report_import_defects.py` peut être intact (cf. les 2
  `troncature-x-molecule`, qui sont des posologies correctes). Toujours
  relire l'occurrence avant de corriger.

---

## 7. Défauts d'import — mesurés, non corrigés

`report_import_defects.py` rejoue les sept familles établies sur AMBOSS.

| famille | AMBOSS | German | RESCOS |
|---|---|---|---|
| `plage-coupee` (`500-: 1000 mg`) | 0 | 0 | **0** |
| `troncature-x-fragment` (`: xicilline`) | 1 | 0 | **0** |
| `troncature-x-molecule` | 5 | 0 | **2** (faux positifs) |
| `chevron-nu` | 144 | 27 | **114** (piège d'outillage) |
| `chevron-nu-colle-lettre` | 0 | 0 | **0** |
| `comparaison-manquante` | 17 | 2 | **13** (faux positifs) |
| `numeration-implicite` | 0 | 0 | **1** (réel) |

**RESCOS ne porte aucun des défauts durs d'import d'AMBOSS.** Les deux
signatures exactes de la moulinette (`plage-coupee`,
`troncature-x-fragment`) sont à zéro, comme dans German. Le seul défaut réel
est **une** numération en unité implicite (« plaquettes 422 », à lire 422 G/L).

La septième famille — *examens copiés sur le mauvais diagnostic* — n'est pas
mécanisable et se vérifie à la lecture du bloc `annexe-dd`.

---

## 8. `annexe-dd` : ne pas rejouer la passe de nettoyage de German

German portait un `annexe-dd` de **remplissage** : une seule formulation,
« À évaluer cliniquement », couvrait 207 des 1072 fragments d'arguments, et le
bloc ne comptait que 69,6 % de formulations distinctes. D'où
`prune_dd_filler.py`.

**RESCOS n'a pas ce défaut** :

| corpus | `<li>` | fragments | distincts | formulation la plus répétée |
|---|---|---|---|---|
| AMBOSS | 257 | 1296 | **95,4 %** | 4× « pas de fièvre » |
| German (avant nettoyage) | 484 | 1072 | **69,6 %** | **207×** « à évaluer cliniquement » |
| German (après) | 485 | 843 | 94,2 % | 6× « installation progressive » |
| **RESCOS** | **139** | **676** | **92,2 %** | **6× « âge jeune »** |

RESCOS est au niveau d'AMBOSS et de German *après* nettoyage. Sur ses 139
entrées, 51 portent à la fois des arguments POUR et CONTRE, 48 CONTRE seuls,
36 POUR seuls, et **139/139 portent la flèche « → examen qui départage »**.

> **Ne pas rejouer `prune_dd_filler.py` ici.** Il n'y a pas de remplissage à
> retirer ; le script ne trouverait rien et le faire tourner ne ferait que
> risquer une suppression à tort.

---

## Interdits

Identiques à ceux d'AMBOSS et de German :

* ne jamais lire une grille entière avec `Read` ;
* ne jamais `grep` un fichier de grille sans `strip_base64` ;
* ne jamais recopier `visible_text` — l'importer ;
* ne jamais câbler `check_no_loss.py` ni `report_import_defects.py` comme
  porte bloquante : ce sont des rapports, ils sortent toujours à 0 ;
* ne jamais modifier `scripts/amboss/` ni `scripts/german/` depuis ce volet ;
* ne jamais changer le comportement **par défaut** de
  `report_redundancy.py` : les mesures du projet cesseraient d'être
  comparables.
