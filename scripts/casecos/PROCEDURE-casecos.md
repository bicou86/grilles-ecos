# Procédure de traitement d'une grille CasECOS

Volet CasECOS de la procédure. Il ne remplace pas `scripts/amboss/PROCEDURE.md`
ni `scripts/rescos/PROCEDURE-rescos.md` : il en note les écarts. Tout ce qui
n'est pas mentionné ici s'y transpose tel quel — la hiérarchie à trois niveaux,
la règle de dédoublonnage, le grain, les interdits.

**Corpus : 198 grilles**, `cases/casecos/*.html`. **40,8 Mo de texte pur, aucun
data-URI** (0 grille sur 198 contient une image base64 — c'est le seul corpus du
dépôt dans ce cas). Taille : min 123 879, médiane 205 008, max 272 378
caractères.

**Les fichiers n'ont aucun identifiant numérique.** Pas de `CASECOS-12` : les
noms sont des titres (`AMC-Chir2-ECG3 Hémorragie aiguë du tube digestif -
M. Botari - Grille ECOS.html`). `lib.grids()` trie par nom de fichier ; il n'y a
pas de `grid_num()`, seulement `grid_key()`.

⚠️ **Les noms accentués sont un piège à part entière, et il a déjà mordu deux
fois.** Les trois corpus précédents ont des noms purement ASCII
(`RESCOS-12_-_...`) ; ceux-ci sont des titres français.

1. **Filtrer une grille au clavier exige `lib.matches()`.** macOS stocke les
   noms en NFD, un shell envoie du NFC : `"Céphalées" in path.name` est **faux**
   alors que les deux chaînes s'affichent à l'identique. Tous les scripts de ce
   dossier passent par `lib.matches()`. Ne jamais revenir à un `in` nu.
2. **`git diff --name-only` exige `-z` ET une normalisation NFC.** Sans `-z`,
   git rend les chemins non-ASCII entre guillemets et échappés à la mode C
   (`"cases/casecos/AMC-CasECOS C\303\251phal\303\251es - ....html"`) ; et même
   avec `-z`, il les rend en **NFC** quand le système de fichiers les rend en
   **NFD**. Mesure : sans normalisation, **60 des 198 noms** se correspondent —
   exactement les 60 sans accent. Sans les deux corrections,
   `check_no_loss.py` devient un **no-op silencieux** : il annonce « aucune
   grille modifiée » quoi qu'il arrive, et le filet anti-perte n'existe plus.
   `git show` n'a pas ce problème (`core.precomposeunicode` accepte le NFD).

---

## 0. Ce qui change par rapport à AMBOSS et RESCOS, en une page

| | AMBOSS | German | RESCOS | **CasECOS** |
|---|---|---|---|---|
| grilles | 40 | 88 | 41 | **198** |
| `resume` | 25 | 14 | 25 | **0** |
| `presentation-patient` | 24 (+1 variante) | 10 | 25 | **0** |
| `annexe-defi` | — | — | — | **195** |
| `annexe-expert` | 40 | 0 | 39 | **195** |
| `annexe-theorie` | 40 | 0 | 37 | **195** |
| `annexe-scenario` | 40 | 0 | 39 | **195** |
| `annexe-dd` | 40 | 78 seg. / 77 gr. | 22 | **188 seg. / 186 gr.** |
| `therapy-section` | (non couvert) | 126 / 44 | 47 / 16 | **759 / 190** |
| `redflags-section` | (non couvert) | 10 / 10 | 6 / 6 | **181 / 180** |
| `cloture-item` | (non couvert) | — | 40 / 13 | **595 / 194** |
| `exemples-phrases` | — | — | — | **383 / 190** |
| `annexe-item` nu | 1 (AMBOSS-34) | — | — | **1 (AMC-Psy-P10)** |
| `caseConfig` | 40/40 | 88/88 | 39/41 | **198/198** (0/198 avant k2) |
| `<script src=".../scoring.js">` | 40/40 | 88/88 | 41/41 | **198/198** (0/198 avant k2) |
| `persistence.js` | 40/40 | 88/88 | 41/41 | **198/198** (0/198 avant k2) |
| appel `saveToRegistry` | via scoring.js | via scoring.js | via scoring.js | **via scoring.js** (aucun avant k2) |
| fin de zone pédagogique | `annexe-scenario` | `<!-- COMMENTAIRE GÉNÉRAL -->` | idem | **idem (198/198)** |

Cinq écarts structurants :

1. **Il n'y a ni `resume` ni `presentation-patient`.** La source canonique du
   contrat des trois corpus précédents n'existe pas ici. Voir § 2.
2. **`annexe-defi` est la quatrième fiche** (« Défi pédagogique ») : une
   situation qui dérape — refus de soins, aggravation, question imprévue — puis
   « Type de réponse attendue ». Ce **n'est pas** l'homologue de
   `presentation-patient`. Voir § 2.
3. **`exemples-phrases` est un bloc inédit** : des phrases modèles d'annonce,
   entre guillemets. Il vit dans le `cloture-item` **371 fois sur 383** ; les
   **12 restantes** sont posées directement dans un `criteria-row` de
   Management, donc hors de tout autre bloc. Ce sont ces 12 orphelines qui
   imposent de le déclarer comme bloc — c'est `uncovered_content()` qui les a
   fait apparaître.
4. **Le barème ÉTAIT embarqué dans chaque grille** : ni `caseConfig`, ni
   `scoring.js`. Corrigé par le lot k2 — les 198 déclarent aujourd'hui un
   `window.caseConfig` et chargent le moteur partagé. Voir § 5.
5. **Aucune grille ne remontait son score au tableau de bord.** Corrigé par le
   même geste. Voir § 6.

---

## 1. Situer les blocs — lecture ciblée, jamais le fichier entier

Médiane 205 000 caractères. **Ne jamais `Read` une grille entière.** Comme dans
les trois corpus précédents, on convertit un index de caractère en numéro de
ligne :

```python
import sys; sys.path.insert(0, "scripts/casecos")
import lib_casecos as lib
html = lib.strip_base64(path.read_text(encoding="utf-8"))
a, b = lib.dd_bounds(html)          # ou lib.peda_bounds(html)
line = html[:a].count("\n") + 1     # -> Read(offset=line, limit=...)
```

`peda_bounds()` s'ouvre sur `<div class="annexes">` (il n'y a pas de `resume`)
et rend `(-1, -1)` pour les **3 grilles « ECOS Diag »**, seules sans `annexes`.
Elle ne couvre ni `annexe-dd`, ni `therapy`, `redflags`, `cloture`, `exemples` —
tous logés en amont, dispersés dans les sections notées. Pour lire tout le
contenu d'une grille : `lib.top_spans(html)`.

---

## 2. Les dix blocs, leurs bornes, leur rôle

| bloc | classe | segments / grilles | rôle |
|---|---|---|---|
| `annexe-dd` | `annexe-item annexe-dd` | 188 / 186 | diagnostics différentiels argumentés |
| `redflags` | `redflags-section` | 181 / 180 | signaux d'alarme, texte + description |
| `therapy` | `therapy-section` | 759 / 190 | traitements, un `therapy-item` par ligne |
| `cloture` | `cloture-item` | 595 / 194 | clôture de consultation |
| `exemples` | `exemples-phrases` | 383 / 190 | phrases modèles d'annonce |
| `expert` | `annexe-item annexe-expert` | 195 / 195 | fiche évaluateur |
| `theorie` | `annexe-item annexe-theorie` | 195 / 195 | théorie pratique |
| `scenario` | `annexe-item annexe-scenario` | 195 / 195 | script du patient simulé |
| `defi` | `annexe-item annexe-defi` | 195 / 195 | défi pédagogique |
| `annexe-nu` | `annexe-item` **nu** | 1 / 1 | variante de classe, AMC-Psy-P10 |

### `annexe-nu` — l'angle mort d'AMBOSS-34, retrouvé

`AMC-Psy-P10 Anorexie mentale — Melody, 17 ans` porte une **cinquième fiche**
sous `<div class="annexe-item">` nu, sans classe de rôle :
« Scenario Mere Standardisee », le script d'anamnèse collatérale auprès de la
mère. Sans entrée dans `BLOCKS`, cette fiche entière serait invisible à tout
l'outillage, et le seul symptôme serait un chiffre de redondance anormalement
bas — exactement AMBOSS-34.

**`annexe-item` figure dans `CONTENT_CLASSES`** (contrairement au choix de
`lib_rescos`, où le piège du `\b` l'imposait). C'est délibéré : `uncovered_content()`
devient ainsi un détecteur direct de fiche inédite. Toute
`<div class="annexe-item annexe-XYZ">` nouvelle sera signalée dès le premier
passage de `check_invariants.py`.

### Il n'y a pas de `resume` : sur quoi rebâtir le contrat

Les trois corpus précédents ancraient le contrat de rôle sur le `resume`
(synthèse) et la `presentation-patient` (annonce au patient). Aucun des deux
n'existe ici. Les éléments mesurés, à verser au dossier — **le contrat n'est pas
tranché par ce lot** :

* **`theorie` porte 29 % du volume pédagogique** (1,27 M caractères sur 4,41 M),
  et son ossature est **la même qu'AMBOSS** : `Rappels thérapeutiques` (194/195)
  et `Examens complémentaires` (197/195), une occurrence par fiche, plus des
  sections libres. Il y ajoute « Résumé du cas clinique » (80 grilles) et
  « Diagnostic » (49) — c'est là, et nulle part ailleurs, qu'on trouve
  aujourd'hui l'équivalent d'un `resume`.
* **`expert` est structurellement IDENTIQUE à AMBOSS** : trois titres, toujours
  les mêmes — `Points clés` (195), `Pièges` (195), `Rôles et interventions`
  (191). Aucun autre. C'est le bloc le plus normalisé du corpus, et le meilleur
  candidat à faire autorité sur « ce que l'évaluateur doit savoir ».
* **`annexe-dd` porte des arguments réels** (§ 8), pas du remplissage.
* **`defi` n'a aucun titre** : 390 `<p>` pour 195 fiches, soit deux paragraphes
  chacune — la situation, puis « Type de réponse attendue ». À comparer aux
  **six sections** de la `presentation-patient` d'AMBOSS (Version longue, Fiche
  ECOS, Checklist mentale, Version express SBAR, Touches ludiques, Questions de
  l'examinateur). **Les deux blocs n'ont pas le même rôle** : `defi` teste une
  situation difficile, `presentation-patient` outille une annonce.
* Les blocs notés `therapy` (12,4 % du volume), `redflags` (5,4 %) et `cloture`
  (10,5 %) sont ici la règle et non l'exception, contrairement à RESCOS.

### `scenario` est borné mais exclu de la redondance

Comme dans RESCOS : redire les symptômes déjà listés est la fonction même du
script du patient simulé. `lib.REDUNDANCY_EXCLUDED = {"scenario"}`, et
`--with-scenario` lève l'exclusion. Le bloc reste borné, gelé au snapshot,
vérifié par `bounds_anomalies` et protégé par `check_no_loss` : ce n'est pas un
angle mort.

`annexe-nu` n'est **pas** exclu, bien qu'il porte aujourd'hui un second
scénario : la classe est générique et rien ne garantit qu'une grille future y
logera encore un scénario.

---

## 3. Le recouvrement `exemples` ⊂ `cloture` : passer par `top_spans()`

`block_spans("exemples")` rend les 383 segments, dont 371 sont **à l'intérieur**
d'un `cloture-item`. Les compter à la fois sous leur nom et sous celui de
`cloture` doublerait 1 514 phrases modèles et ferait rapporter chaque doublon
deux fois.

**`lib.top_spans(html)` rend le découpage NON RECOUVRANT** : chaque caractère
appartient à exactement un segment, sous le nom du bloc le plus extérieur.
`all_items()` et `report_redundancy.py` l'utilisent. `uncovered_content()`
utilise `all_spans()`, qui les garde tous — c'est ce qu'il faut pour une mesure
de couverture.

⚠️ `top_spans(html, excluded=...)` retire les blocs **avant** le calcul du
premier niveau. Sinon exclure `cloture` ferait remonter ses `exemples`
imbriqués, et l'exclusion **augmenterait** le total au lieu de le réduire.

---

## 4. Vérifier

```bash
python3 scripts/casecos/check_invariants.py      # 198 grilles, doit être vert
python3 scripts/casecos/check_reachability.py    # barème atteignable ET calculable
python3 scripts/casecos/check_nomenclature.py    # ROUGE tant que la passe n'est pas faite
python3 scripts/casecos/report_redundancy.py --quiet          # ~3 min 30
python3 scripts/casecos/report_redundancy.py --quiet --intra  # ~7 min
python3 scripts/casecos/report_import_defects.py --quiet
python3 scripts/casecos/check_no_loss.py <BASE_REF>           # ~1-2 s / grille modifiée
```

`snapshot_invariants.py` ne se relance qu'après une modification **voulue et
relue**, jamais pour « faire passer » un contrôle rouge.

**Le contrôle navigateur n'est remplacé par aucun de ces scripts.** Aucun ne
peut dire que la page charge sans exception, que `ecos_registry` est renseigné,
ni que les réponses survivent au rechargement — ce sont trois faits d'exécution.
Il doit naviguer **par les URL d'`index.html`** et non par une énumération du
disque : voir § 6, « Clé du registre et noms accentués ».

`migrate_to_shared_engine.py` est le script du lot k2. Il est idempotent et sans
effet sur un corpus déjà basculé ; `--dry-run` reste le moyen de vérifier qu'une
grille nouvellement importée arriverait sous la forme embarquée.

**Toujours relancer les témoins des corpus précédents après une modification de
l'outillage** — `lib_casecos` importe `lib_amboss` :

```bash
python3 scripts/amboss/check_invariants.py && python3 scripts/rescos/check_invariants.py
python3 scripts/amboss/report_redundancy.py --quiet | tail -1   # doit dire 147
python3 scripts/rescos/report_redundancy.py --quiet | tail -1   # doit dire 127
```

---

## 5. Le barème a été embarqué dans chaque grille — il ne l'est plus

> **État depuis le lot k2 :** les 198 grilles portent un `window.caseConfig` et
> chargent `cases/scoring.js` + `cases/persistence.js`. Ce paragraphe décrit la
> forme d'origine, que les lecteurs de `snapshot_invariants.py` et de
> `check_reachability.py` savent toujours lire — en repli, après la forme
> déclarative — pour qu'un retour en arrière soit signalé et non silencieux.

Aucune grille n'avait de `window.caseConfig` (0/198), aucune ne chargeait
`cases/scoring.js` (0/198). **Chacune embarquait sa propre copie complète du
moteur**, avec la configuration en littéral local :

```js
let maxScores = {};                                    // déclaration VIDE
...
maxScores = {anamnese: 37, examen: 15, management: 14, communication: 20};
coef      = {anamnese: 0.25, examen: 0.25, management: 0.25, communication: 0.25};
sectionInfo = [
  {key: "anamnese", prefix: "a", count: 8,  label: "Anamnèse"},
  {key: "examen",   prefix: "e", count: 4,  label: "Examen clinique", scoreId: "statusScore"},
  ...
];
```

⚠️ **La déclaration vide précède l'affectation réelle.** Un motif
`maxScores\s*=\s*\{([^}]*)\}` naïf rend `{}` et le relevé est uniformément nul.
`snapshot_invariants._first_non_empty()` retient le premier groupe non vide ;
c'est le seul lecteur à employer.

### Les 198 copies étaient saines et identiques entre elles

C'est ce qui a rendu la bascule mécaniquement sûre. Mesure : les 198 blocs
`<script>` porteurs de `calculateScores()`, **nombres et chaînes neutralisés**,
rendaient **une seule empreinte** (`51866a7121a1`). Il n'y avait pas 198 moteurs
mais un seul, recopié 198 fois. Sans la neutralisation, chaque grille aurait eu
une empreinte unique — elle porte son propre barème — et le champ n'aurait rien
dit.

Cette empreinte était gelée par `snapshot_invariants.py` (champ `engineHash`) et
comparée à chaque passage. **C'était le pendant, pour un moteur embarqué, du
`git diff` sur `cases/scoring.js`** : il n'y avait rien à diff. Le moteur étant
redevenu partagé, le champ vaut désormais `"shared:scoring.js"` sur les 198 :
c'est `git diff` qui couvre le moteur, et le champ garde la charge de signaler
toute grille qui en ré-embarquerait un.

### Ce moteur était `cases/scoring.js` amputé de six ajouts postérieurs

Diff structurel, ligne à ligne, nombres et chaînes neutralisés :

| absent de CasECOS | conséquence |
|---|---|
| chargement dynamique de `srs.js` | pas de répétition espacée |
| indirection `window.caseConfig` | config en littéral local |
| gardes de nullité sur `#missingItems` / `#missingList` | aucune (les deux id existent 198/198) |
| mode circuit (`window.circuitMode`, `createCircuitNav`) | grilles inutilisables dans `exam.html` |
| `createNavBar()` | remplacé par un 3ᵉ bloc `<script>` équivalent |
| **`saveToRegistry()`** | **aucun score ne remonte au tableau de bord** (§ 6) |

**Le CALCUL était identique au caractère près** : traitement des cases de détail,
repli sur les radios, table communication A=4..E=0, pondération par `coef`,
`max > 0 ? (score/max)*100 : 0`. **C'est la raison pour laquelle la bascule ne
change aucune note** : elle rebranche ce qui manquait autour du calcul, pas le
calcul.

### Le moteur ne peut pas lever de `TypeError`

C'était le défaut des copies périmées de RESCOS-7 et RESCOS-9 : un
déréférencement DOM sans garde vers un élément absent, et le score n'était
jamais calculé. Les neuf identifiants déréférencés sans garde par le moteur
embarqué (`#missingItems`, `#missingList`, `#totalScore`, `#timerContainer`,
`#timerStatus`, `#timerDisplay`, `#startBtn`, `#stopBtn`, `#resetBtn`) étaient
présents **dans les 198 grilles** ; `cases/scoring.js` garde les deux premiers,
les sept autres restent nus et restent présents partout.
`check_reachability.engine_defects()` le revérifie à chaque passage — **contre le
moteur que chaque grille exécute réellement**, le fichier partagé si elle le
charge — plutôt que de s'en remettre à la mesure d'un jour.

### Relevé : 198/198 au barème atteignable

`check_reachability.py` est **vert sur les 198**. Aucun des trois défauts connus
n'est présent :

* pas de critère hors boucle (AMBOSS-9, `a12b`) — 0 orphelin ;
* pas de section vide pondérée (RESCOS-12/13) — 0 ;
* pas de moteur périmé (RESCOS-7/9) — 0.

Ni aucun quatrième : `maxScores`, le maximum simulé et le `<span>` affiché
coïncident sur chaque section de chaque grille, et le global tombe sur 100 %.

---

## 6. Le registre des scores : les 198 grilles étaient muettes

> **État depuis le lot k2 :** les 198 alimentent `ecos_registry`. Le champ
> `savesToRegistry` du snapshot vaut `true` sur les 198 et y est gelé : c'est
> désormais la régression inverse qui est interdite.

**Constat d'origine.** `saveToRegistry` : 0 occurrence sur 198. Ce n'était
**pas** le même constat que dans les autres corpus, où le compte est également 0
— là, la fonction est **définie et appelée par `cases/scoring.js`**, que les
grilles chargent. Ici il n'y avait pas de `scoring.js`, et la copie embarquée
**précédait** l'ajout de `saveToRegistry` : la chaîne était rompue des deux
côtés.

**C'est un défaut, pas un choix.** `index.html` :

* liste les **198 grilles CasECOS** en cartes `class="card casecos"`, section
  `data-section="casecos"`, titrée « Cas 1–198 » ;
* lit `localStorage["ecos_registry"]`, construit `cardRegistry`, et pour chaque
  carte dont la clé de fichier y figure ajoute la pastille
  `<div class="last-score">42% · C</div>`, la classe `attempted grade-c`, et
  incrémente le compteur « Complétés » de l'en-tête.

Le tableau de bord **attendait** donc ces grilles sans qu'aucune lui réponde :
elles ne pouvaient ni afficher de score, ni compter comme complétées, ni
alimenter les statistiques. `exam.html` (mode circuit) lit la même clé et ne
voyait rien non plus.

Deux manques du même geste, corrigés par le même :

* **`cases/persistence.js` n'était chargé par aucune des 198** (40/40, 88/88,
  41/41 ailleurs) : les réponses n'étaient pas sauvegardées d'une session à
  l'autre ;
* **`srs.js`** n'était jamais chargé : pas de répétition espacée. Il n'a pas de
  balise dans les grilles — aucun corpus ne lui en donne — c'est
  `cases/scoring.js` qui l'injecte lui-même.

### La correction, et pourquoi ce n'était pas un `sed`

Rebrancher `scoring.js` par `<script src="../scoring.js">` supprimait le moteur
embarqué **mais aussi la configuration locale** : il fallait, dans le même
geste, convertir les 198 littéraux en `window.caseConfig`.
`migrate_to_shared_engine.py` le fait, sous huit assertions par grille, et
supprime en outre les **deux substituts locaux devenus doubles** : le rappel de
`colorPatientResponses()` (queue exacte de `scoring.js`) et la barre de
navigation en ligne (substitut de `createNavBar()`, qui aurait affiché **deux**
barres). Le `<style>` de `.case-nav-bar` est conservé — les grilles CasECOS ne
chargent pas `cases/case-styles.css`.

**Clé du registre et noms accentués.** `saveToRegistry()` indexe par
`location.pathname.split("/").pop().replace(/\.html$/, "")` et `index.html` par
`href.split("/").pop().replace(/\.html$/, "")` : les deux coïncident **quand on
arrive par le lien du tableau de bord**, dont les `href` sont percent-encodés en
NFC. Ouvrir le fichier depuis le disque (macOS stocke ces noms en **NFD**)
produirait une clé `Ce%CC%81phale%CC%81es` au lieu de `C%C3%A9phal%C3%A9es`, et
la pastille n'apparaîtrait pas. C'est propre à ce corpus — seul corpus aux noms
accentués — et c'est la raison pour laquelle tout contrôle navigateur doit
naviguer par les URL d'`index.html`, jamais par une énumération du système de
fichiers.

---

## 7. Pièges — ceux d'AMBOSS et de RESCOS, et ce que CasECOS y ajoute

### Le chevron nu casse aussi l'ÉQUILIBRAGE des `<div>`, pas seulement le texte

C'est le piège neuf de ce corpus, et il coûte cher. `visible_text()` était déjà
corrigé pour ne pas avaler la clause qui suit un `<` de seuil. **Le même piège
existe un étage plus bas**, dans le motif de balise de `_balanced_end` :

```
... cancers intra-muqueux (T1a) <2 cm, bien différenciés</div>
```

Le motif `<(/?)(\w+)([^>]*)>` de `lib_german` et `lib_rescos` reconnaît ici une
balise nommée « 2 » qui s'étend jusqu'au `>` du `</div>`. **La fermeture est
avalée**, la profondeur ne redescend jamais, et le bloc engloutit tout ce qui
suit. Mesure sur les 198 grilles :

| | `\w+` | `[a-zA-Z][a-zA-Z0-9]*` |
|---|---|---|
| segments débordant l'`END_MARK` | **9** | **0** |
| imbrications bloc-dans-bloc | **244** | **0** |
| queues distinctes (`therapy`) | 12 | **3** |
| queues distinctes (`redflags`) | 7 | **1** |

`lib_casecos._TAG` n'accepte qu'un nom de balise commençant par une **lettre
ASCII**. Le corpus devient alors parfaitement régulier.

Ce bug est **latent** dans `lib_german` et `lib_rescos`. **Vérifié, non
supposé** : sur les 41 grilles RESCOS, les deux motifs rendent des bornes
identiques sur les **313 segments** de son `BLOCKS`. RESCOS porte pourtant 9
chevrons nus numériques précédant un `</div>` (AMBOSS 8) — aucun ne tombe sur
une frontière de bloc. CasECOS en porte **364**, et c'est ce qui fait la
différence. `lib_amboss` n'emploie d'ailleurs pas d'équilibrage : ses blocs sont
bornés par motif de fin.

German n'a pas été mesuré : son outillage est en cours de modification par
ailleurs. Corriger l'un ou l'autre est un refactor à part entière (le bon point
de chute reste un `scripts/lib_grilles.py` partagé) ; il n'entrait pas dans le
périmètre de ce lot.

### `\b112\b` : 593 occurrences, toutes fausses

La règle « ne jamais poser de motif sur 112 », héritée d'AMBOSS
(« Score Global 0/112 »), se vérifie ici à une échelle inédite : **593
occurrences sur les 198 grilles**, toutes dans la feuille de style —
`rgb(112, 188, 123)`, la couleur des phrases modèles.

### Homographes propres à ce corpus, mesurés, jamais bannis

| jeton | occ. | pourquoi il ne peut pas être banni |
|---|---|---|
| `CHF` | 20 | **franc suisse** (« coût 27-40 CHF »), pas *congestive heart failure* |
| `ASA` | 89 | **score ASA** (American Society of Anesthesiologists), et 5-ASA |
| `TB` | 19 | `TB-MDR` / `MDR-TB` (tuberculose), et « trouble bipolaire (TB) » |
| `MST` | 4 | **`MST Continus®`** = morphine à libération prolongée |
| `livres` | 3 | « Associations de patients, **livres**, groupes de soutien » |
| `Rx` | 51 | graphie **suisse** de la radiographie — faux ami parfait |
| `OR` | 3 | odds ratio · `AF` 2 : antécédents familiaux · `PE` 1 : prééclampsie |
| `AAA` | 124 | sigle français et anglais confondus |
| `HAS` | 15 | agence française citée en source — et homographe du verbe anglais |
| `Lopressor` | 13 | métoprolol, spécialité **Novartis**, enregistrée en Suisse |

La table `SANS_MOTIF` de `check_nomenclature.py` consigne chacun de ces refus
avec son chiffre, pour qu'un lot futur qui voudrait « compléter la table »
retrouve la raison.

### Un faux positif hérité, assumé

Le motif `/µL` d'AMBOSS rend **3 hits**, dont un faux : « lymphocytes **CD4** à
14/μL » — une numération CD4 s'exprime justement en cellules/µL. Les deux autres
(« éosinophiles ≥ 300/µL », AMC-Pharmaco-S2) sont réels, et sont exactement le
cas AMBOSS-19. Le motif vit dans `scripts/amboss/`, que ce volet ne modifie
pas : le faux positif est **documenté ici**, pas corrigé là-bas.

### La casse des unités

**Angle mort de la table AMBOSS mis au jour par ce corpus** : ses motifs
d'unités sont sensibles à la casse (`\bg/dL\b`, `\bng/mL\b`), or CasECOS écrit
trois fois sur quatre la graphie minuscule.

| | graphie AMBOSS | graphie minuscule | total réel |
|---|---|---|---|
| `mg/dL` | 2 | 5 | 7 |
| `g/dL` | 1 | 24 | 25 |
| `ng/mL` | 17 | 39 | 56 |
| `pg/mL` | 6 | 4 | 10 |
| `/mm³` | 19 | 4 (`/mm3`) | 23 |

Sans les cinq motifs ajoutés, **76 des 121 valeurs à convertir seraient
invisibles**.

⚠️ **Ne jamais bannir `mmol/l`, `mg/l`, `U/l`, `G/l`** (223 + 27 + 15
occurrences) : ce sont les unités SI **correctes**, avec un « l » minuscule.
Variante typographique, pas erreur de nomenclature.

---

## 8. `annexe-dd` : ne pas rejouer la passe de nettoyage de German

**Mesure sur les 186 grilles qui le portent** : 5 936 items, **5 788
formulations distinctes — 97,5 %**. Le témoin AMBOSS, après nettoyage, est à
96,8 % (1 175 / 1 214). CasECOS est donc **au niveau d'AMBOSS et de RESCOS**, et
non à celui de German avant nettoyage (69 %, dont 207 « à évaluer
cliniquement »).

Recherche explicite de remplissage dans les segments `annexe-dd` :

| formule | occ. |
|---|---|
| « à évaluer cliniquement » | **0** |
| « à compléter », « non renseigné », « argument clinique à… » | **0** |
| « à confirmer » | 9 (tous en contexte : « Pivot-shift positif (à confirmer) ») |
| « à préciser » | 4 · « à discuter » 3 · « selon le contexte » 3 · « à adapter » 1 |

Les 254 items (4,3 %) appartenant à une formulation répétée sont des **libellés
de structure** (`arguments pour`, `arguments contre`) ou des constats cliniques
brefs légitimement partagés entre cas voisins (`examen neurologique normal`).

Le bloc porte **8 diagnostics par grille en moyenne** (min 3, max 19), 32 items,
longueur moyenne d'item 70 caractères.

**Conclusion : aucune passe de nettoyage du remplissage n'est nécessaire sur
`annexe-dd`.** Ne pas transposer `scripts/german/prune_dd_filler.py`.

---

## 9. Défauts d'import — mesurés, non corrigés

`report_import_defects.py` rejoue les sept familles de
`scripts/german/report_import_defects.py` (importées, jamais recopiées).

| famille | AMBOSS | German | RESCOS | **CasECOS** |
|---|---|---|---|---|
| `plage-coupee` | 0/0 | 0/0 | 0/0 | **0/0** |
| `troncature-x-fragment` | 1/1 | 0/0 | 0/0 | **2/2** (faux) |
| `troncature-x-molecule` | 5/5 | 0/0 | 2/2 | **5/4** (faux) |
| `chevron-nu` | 144/35 | 27/20 | 88/29 | **2414/198** |
| `chevron-nu-colle-lettre` | 0/0 | 0/0 | 0/0 | **0/0** |
| `comparaison-manquante` | 17/13 | 2/2 | 12/9 | **128/56** |
| `numeration-implicite` | 0/0 | 0/0 | 0/0 | **26/18** |

**Le corpus ne porte structurellement aucun des défauts d'import d'AMBOSS.**
Les 2 `troncature-x-fragment` sont « xanthomes, xanthélasma » et « xanthine
(xanthinurie) » — des mots français qui commencent par un `x`. Les 5
`troncature-x-molecule` sont des posologies correctes (« Dose : 60 mg PO q4h »).
Les 128 `comparaison-manquante` sont des constantes mesurées (« température
36,2 °C », « IMC 47.6 kg/m² »). Les 2 414 `chevron-nu` sont des seuils
légitimes — voir § 7.

Seule famille à part réelle : `numeration-implicite`, 26 occurrences, dont
« leucocytes 12 000 », « leucocytes 17000 », « GB 15000 » (à lire en G/L) et des
faux où l'unité est présente mais en « l » minuscule (« plaquettes 91000 G/l »).
**À relire une par une.**

Le septième défaut — « chaînes d'examens copiées sur le mauvais diagnostic » —
n'est pas mécanisable et se vérifie à la lecture.

---

## 10. Les grilles atypiques

### Les 3 « ECOS Diag » sont des doublons non enrichis

`ECOS Diag 1 - Dos douloureux`, `ECOS Diag 2 - Abdomen Aigu aux Urgences`,
`ECOS Diag 3 - Dyspnée` sont les **seules sans aucun bloc de contenu** : ni
`annexes`, ni `expert`, `theorie`, `scenario`, `defi`, ni `therapy`, `redflags`,
`cloture`, `annexe-dd`. Elles n'ont **aucun sous-item de détail** (0 `detail-row`,
contre 89 en moyenne).

Chacune double un cas déjà présent sous forme enrichie, **avec exactement le même
nombre de critères notés** :

| doublon nu | version enrichie | critères | sous-items |
|---|---|---|---|
| `ECOS Diag 1 - Dos douloureux` | `AMC-ECOSDiag1 … Spondyloarthrite axiale` | 13 = 13 | 0 → 4 |
| `ECOS Diag 2 - Abdomen Aigu aux Urgences` | `AMC-ECOSDiag2 … Ulcère perforé` | 16 = 16 | 0 → 18 |
| `ECOS Diag 3 - Dyspnée` | `AMC-ECOSDiag3 … Anémie ferriprive sur AINS` | 17 = 17 | 0 → 17 |

Leur barème est atteignable, elles ne sont pas cassées — elles sont **obsolètes**.
Décision à prendre hors outillage : supprimer, ou conserver comme variante
courte. Ne rien faire sans arbitrage : elles sont référencées par `index.html`.

### Les 12 sans `annexe-dd`

Trois sont les doublons ci-dessus. Les **neuf autres** n'ont pas de bloc
`annexe-dd` parce que leur critère `m1` **n'est pas un critère de diagnostic
différentiel** : « Gestion de l'analgésie post-opératoire », « Démarche pratique
recommandée », « Fréquence et épidémiologie », « Définitions clés », « BILAN
ADDITIONNEL », « STRATÉGIE DIAGNOSTIQUE », « Poser et expliquer l'indication
opératoire ». Le bloc n'a **pas d'hôte** dans ces grilles — ce n'est pas un
oubli, c'est une conséquence de leur sujet (consentement, indication opératoire,
dépistage, éthique). Ne pas en fabriquer un pour uniformiser.

---

## 11. Mesures initiales (état au moment du portage)

| mesure | valeur |
|---|---|
| grilles | 198 |
| volume total | 40,8 Mo, 0 data-URI |
| texte visible dans les blocs | **4,41 M caractères** (22 285/grille ; AMBOSS 13 301/grille) |
| segments de bloc | **2 887** |
| items extraits | **37 172** (188/grille, min 0, max 376) |
| critères notés | 3 256 (16,4/grille) |
| sous-items de détail | 17 601 (88,9/grille) |
| **redondance inter-blocs** | **830 paires** (seuil 0,72, `scenario` exclu) |
| **redondance intra-bloc** | **752 paires** (mesure additionnelle) |
| nomenclature | **649 termes** sur 123 grilles |
| barème inatteignable | **0 / 198** |
| `bounds_anomalies` | **0** |
| `uncovered_content` | **0** |

Répartition du volume pédagogique : `theorie` 28,8 %, `scenario` 13,4 %,
`therapy` 12,4 %, `expert` 11,3 %, `annexe-dd` 11,1 %, `cloture` 10,5 %,
`defi` 6,8 %, `redflags` 5,4 %, `exemples` 0,3 %.

Couples de blocs les plus redondants : `expert ↔ theorie` **405**,
`theorie ↔ therapy` 135, `annexe-dd ↔ theorie` 104, `redflags ↔ theorie` 59,
`annexe-dd ↔ expert` 44, `annexe-dd ↔ redflags` 38.

Grilles les plus redondantes : `UIDC-Monsieur Arden` 28, `UIDC-Madame Kopf` 22,
`Convulsion fébrile - Nourrisson 18 mois` 21, `Fracture vertébrale
ostéoporotique` 19, `HSA avec convulsion` 19.

Nomenclature, par motif (top) : `NFS` 106, `BMI` 86, `gold standard` 76,
`Coumadin` 47, `ng/ml` 39, `HIV` 35, `MRSA` 33, `PCI` 31, `g/dl` 24, `/mm³` 19,
`ng/mL` 17, `FIT` 16, `Ativan` 13, `lbs` 9, `ANA` 9, `CABG` 8, `Pepto-Bismol` 8,
`Dilantin` 8, `Versed` 7, `pg/mL` 6, `mg/dl` 5, `Tylenol` 5, `EHPAD` 4, `IDE` 4,
`pg/ml` 4, `/mm3` 4, `SAMU` 3, `911` 3, `PID` 3, `DMARDs` 3, `mEq` 3, `BUN` 2,
`livres` 2, `mg/dL` 2, `COPD` 1, `g/dL` 1.

---

## Interdits

* **Ne jamais `Read` une grille entière** (médiane 205 000 caractères). Passer
  par `peda_bounds()`, `dd_bounds()`, `block_spans()`, `top_spans()`.
* **Ne jamais écrire dans `scripts/amboss/`, `scripts/german/` ni
  `scripts/rescos/`** depuis ce volet. Leurs mesures publiées (AMBOSS **147**
  paires inter-blocs, RESCOS **127**) doivent rester inchangées.
* **Ne jamais employer `re.sub(r'<[^>]+>', ...)`** : importer `visible_text()`.
  Et ne jamais recopier un équilibrage de `<div>` fondé sur `\w+` — voir § 7.
* **Ne jamais filtrer une grille par `only in path.name`**, et ne jamais lire
  `git diff --name-only` sans `-z` ni sans normaliser en NFC : passer par
  `lib.matches()` et par `check_no_loss.changed_grid_names()` (§ en-tête).
* **Ne jamais relancer `snapshot_invariants.py` pour faire passer un contrôle
  rouge.** Le snapshot se met à jour après une modification voulue et relue.
* **Ne jamais câbler `check_no_loss.py` comme porte bloquante** : il sort
  toujours 0, une disparition n'est pas forcément une perte.
* **Ne jamais ajouter à `BANNED` un motif sans l'avoir compté sur les 198
  grilles**, et sans avoir vérifié qu'il n'a pas d'homographe français (§ 7).
