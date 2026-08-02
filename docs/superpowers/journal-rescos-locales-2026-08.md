# Journal — `cases/rescos-locales`, août 2026

Branche `refonte-amboss-suisse`. Base `260a903` (l'inventaire du lot `l2`).
Quatre réparations **techniques** : aucun contenu médical n'a été modifié.

| lot | commit | objet |
|---|---|---|
| `l2` | `260a903` | outillage + audit — **aucune** modification de grille |
| `l3` · défaut 1 | `ec4fd66` | bascule des 156 moteurs embarqués sur `cases/scoring.js` |
| `l3` · défaut 2 | `7e13f93` | RESCOS-63, somme des coefficients 0,5 → 1 |
| `l3` · défaut 3 | `73353a1` | RESCOS-69b, deux vignettes sous le même nom |
| `l3` · défaut 4 | `9c34f34` | 92 références d'image mortes retirées |
| `l4` | *(ce lot)* | passe de nomenclature suisse — 424 termes sur 108 grilles |

Les quatre commits sont `path`-scopés sur `cases/rescos-locales` et
`scripts/rescos-locales`, et **rien d'autre** — vérifié commit par commit.

### Mesure d'ensemble, avant et après

| | `260a903` | après `l3` |
|---|---:|---:|
| exceptions JavaScript, 165 grilles | **13 446** | **0** |
| grilles sans exception ni erreur | 9 / 165 | **165 / 165** |
| erreurs 404 (images) | 92 | **0** |
| grilles écrivant **leur** entrée `ecos_registry` | **0 / 165** | **156 / 165** |
| grilles à 100 % après remplissage complet | 155 / 156 | **156 / 156** |
| `check_reachability` | ÉCHEC, 1 grille | **OK, 156/156** |
| `check_invariants` | OK | **OK** |
| `report_redundancy` | 1258 | **1258** |
| `check_no_loss 260a903` | — | **0 item disparu / 156 grilles** |
| poids hors base64 | 27,1 Mo | **21,9 Mo** |
| témoin AMBOSS · RESCOS | 147 · 127 | **147 · 127** |

Les 9 grilles qui n'écrivent pas au registre sont **exactement** les 9 feuilles
porte : elles n'ont pas de score, et c'est correct.

> **Le décompte du registre demande une précaution.** `localStorage` est partagé
> par toutes les pages de la même origine : compter « `ecos_registry` non vide »
> rend **165/165** parce que chaque grille voit les entrées des précédentes. Le
> chiffre juste est celui des grilles qui écrivent **leur propre clé** —
> `saveToRegistry()` la construit depuis `location.pathname`, donc
> percent-encodée — à `pct: 100, grade: "A"`. C'est **156/165**.

---

## Défaut 1 — les 156 moteurs de calcul

**Ce qui était mesuré à `260a903`** : 156 grilles notées, chacune sa copie de
`calculateScores()`, **une seule variante** (empreinte SHA-256
`c3e2534e…` sur 156), et cette variante est la **même fourche périmée** que
celle de RESCOS-7 et RESCOS-9, avec les **six mêmes manques** — garde
`if (missingEl)`, appel **et** définition de `saveToRegistry()`, chargeur de
`srs.js`, mode circuit avec retour à `exam.html`, `createNavBar()` et
`createCircuitNav()`.

Le manque n° 1 se réalisait à chaque calcul : le
`<div class="missing-items" id="missingItems">` que le moteur adresse sans garde
est **commenté** dans les 156 grilles — vérifié en retirant d'abord les
commentaires HTML, 156/156, et non au `grep` brut, qui le trouve *dans* le
commentaire et conclut l'inverse.

### Décision : bascule, pas report

La même que r7, pour les mêmes raisons : l'écart est de **six** points et non de
deux ; la définition de `saveToRegistry()` manque aussi, donc un report devrait
recopier la fonction entière ; et reporter six corrections dans 156 copies
reconduirait le mécanisme de dérive que ce défaut réalise déjà.

`scripts/rescos-locales/apply_shared_engine.py` remplace le premier des deux
`<script>` en ligne par un `<script>` de configuration et
`<script src="../scoring.js"></script>`. Le second `<script>` (l'appel final à
`colorPatientResponses()`) est laissé intact — `cases/scoring.js` le porte
également en fin de fichier, et RESCOS-7/9 le conservent de même.

### Les trois vérifications que RESCOS-7/9 ne demandaient pas

**1. Chemin relatif.** `cases/rescos-locales/` est à deux niveaux sous la racine,
comme `cases/rescos/`. `../scoring.js` → `cases/scoring.js` ; le chargeur
dynamique `(location.pathname.indexOf('/cases/') >= 0 ? '../' : 'cases/') +
'srs.js'` → `cases/srs.js` ; les `../../index.html` et `../../exam.html` que le
moteur construit → la racine du dépôt. Confirmé par le harnais : aucun 404 de
script.

**2. CSS en ligne.** Les 165 grilles ont leur `<style>` et ne chargent pas
`cases/case-styles.css`. Mesure classe par classe, sur les 156 : `score-0`…
`score-5`, `score-max`, `score-a`…`score-e`, `lacune-rouge/orange/verte`,
`note-a`…`note-e`, `note-neutral`, `criteria-zero-points`, `criteria-one-point`,
`criteria-full-points`, `criteria-not-answered`, `communication-note-*`,
`communication-not-answered`, `timer-running/warning/critical`,
`status-running/warning/finished`, `revision-mode`, `exam-mode`, `has-content`,
`missing-item` — **0 absence**. Le CSS en ligne ne casse rien.

**3. La barre de navigation, elle, était absente — et entrait en collision.**
`createNavBar()` (manque n° 6) insère une `.case-nav-bar` en
`position: fixed; top: 20px; left: 20px`. Ses quatre classes n'existaient dans
aucune des 156 feuilles de style, et `top: 20px; left: 20px` est **exactement**
la place qu'y occupait `.timer-container` (156/156). `cases/case-styles.css`
avait déjà résolu la même collision pour les trois autres corpus en déplaçant le
minuteur à `top: 70px` : le script recopie ce geste et ajoute les règles
`.case-nav-bar` (lignes 1209-1221 et 3630-3698 du fichier partagé). Ni
`case-styles.css`, ni `persistence.js`, ni `theme-sync.js` ne sont chargés —
aucun des six manques ne les concerne.

### Transposition du barème

Vérifiée, pas supposée. Deux formes coexistaient :

* **déclarative** (154 grilles) — les trois membres droits `maxScores = …`,
  `coef = …`, `sectionInfo = …` sont repris **verbatim**, sans reformatage ;
* **impérative** (RESCOS-63 et « RESCOS-64 station double 2 », exactement la
  forme de RESCOS-7 et RESCOS-9) — reconstruite dans l'ordre des
  `sectionInfo.push({…})`, chaque champ recopié tel quel.

**Contrôle** : pour chacune des 156, `parse_config()` rend le **même
quadruplet** avant et après — `maxScores`, `coef`, `sectionInfo` (clé, préfixe,
`count`, `scoreId`, `isComm`) et dénominateurs affichés. **0 divergence.**

**Contrôle de morsure** (le silence du vérificateur ne vaut que s'il mord) :
`maxScores.anamnese` forcé de 42 à 41 sur une grille → `<<< ECART` ;
`src="../scoring.js"` remplacé par `../scoringX.js` → `MOTEUR INCONNU`.

### Outillage adapté

* `check_reachability.parse_config()` : branche `window.caseConfig` ajoutée, les
  deux anciennes conservées (elles décrivent ce que le corpus a porté, et c'est
  la seule chose qui distinguerait une grille réimportée du vault).
* `engine_fingerprint()` : rend le marqueur `shared:cases/scoring.js` pour une
  grille qui charge le moteur partagé. Un **marqueur** et non un SHA : ce qui
  justifiait une empreinte était l'invisibilité de 35 800 caractères de
  JavaScript noyés dans 170 000 de HTML ; `cases/scoring.js` est un fichier
  suivi par `git`, dont toute modification apparaît à son propre `diff`.
* `snapshot_invariants.config_form()` : nouvelle valeur `caseConfig`.
* **`check_no_loss.py` : `git diff -z`.** Sans `-z`, `core.quotepath` rendait
  `"cases/rescos-locales/AMC Urgences 1 - Polytraumatis\303\251 - Grille
  ECOS.html"` pour tout nom accentué ; le nom ainsi lu ne correspondait à aucun
  fichier du disque et ces grilles étaient **silencieusement sautées**. 132 des
  165 noms portent un accent. Symptôme mesuré : 156 grilles modifiées, **57
  seulement examinées**. Après correction : 156 sur 156, 0 item disparu.

### Baseline régénéré — chaque ligne

| champ | grilles touchées | pourquoi |
|---|---:|---|
| `engineFingerprint` | 156 | `c3e2534e…` → `shared:cases/scoring.js` : le moteur embarqué a disparu |
| `configForm` | 156 | `declarative` (154) / `imperative` (2) → `caseConfig` : la branche de lecture change |
| *tous les autres* | **0** | — |

`maxScores`, `coef`, `scoreSpans`, `sectionCounts`, `sectionPrefixes`, `blocks`,
`criteriaCount`, `detailCount`, `radioCount`, `checkboxCount`,
`boundsAnomalies`, `uncoveredContent` : **identiques sur les 165**. C'est la
démonstration la plus directe que l'échange a touché le moteur et **rien** du
contenu ni du barème.

---

## Défaut 2 — RESCOS-63, somme des coefficients = 0,5

`anamnese` 0,25 et `management` 0,25, et rien d'autre. Le global plafonnait à
**50 %** sur une grille parfaitement remplie, sans qu'aucune section soit en
écart — confirmé en navigateur : 50 %, note E, seule des 156 à ne pas atteindre
100 %.

**Redistribution : 0,5 · 0,5**, et les deux `section-header` passent de
« (25%) » à « (50%) » — le corpus affiche le coefficient dans l'intitulé de
section, vérifié sur RESCOS-64.

Quatre faits l'imposent, aucun ne dépend d'un jugement de contenu :

1. **La grille ne porte que deux sections réelles.** Deux `section-header`, deux
   `<span class="score">` (`anamneseScore` /29, `managementScore` /16), deux
   `id="…-percentage"`, et les seules entrées de la page sont `a1..a9` et
   `m1..m6`. Il n'y a pas de section à retrouver : le défaut est la **somme**.
2. **La déclaration exprimait déjà l'égalité** (0,25 = 0,25), et les deux
   en-têtes annonçaient le même « (25%) ». Doubler les deux est la seule
   correction qui rétablisse la somme **sans toucher au rapport voulu**.
3. **C'est la doctrine du corpus** : 155 des 156 grilles notées pondèrent à
   égalité, quel que soit leur nombre de points.
4. **Le prorata réintroduirait ce que le moteur neutralise.**
   `cases/scoring.js` calcule `(score / max) * 100` **par section** avant
   d'appliquer `coef`. Pondérer 29 contre 16 compterait les points **deux
   fois**.

Le mécanisme d'origine se lit dans le voisinage : le gabarit du corpus est
`0,25 × 4` — « RESCOS-64 station double 2 » le porte encore, avec quatre
sections inédites (`presentation`, `raisonnement`, `examens`, `management`).
RESCOS-63 en a supprimé deux sans remettre les coefficients à l'échelle.

**Résultat** : `check_reachability` rend 100 % ; navigateur, remplissage
complet : **100 %, note A**, `ecos_registry` écrit. Baseline : **une seule
ligne**, le `coef` de RESCOS-63.

---

## Défaut 3 — RESCOS-69, deux vignettes sous le même numéro

Deux fichiers distincts (180 435 et 174 707 octets à l'inventaire), **pas une
duplication** : 3 items communs, 134 et 106 propres. Même patient (« M/Mme
Norton, 25 ans »), même thème, mais la seconde développe un volet médico-légal
absent de la première.

Le problème est **fonctionnel** : `saveToRegistry()` indexe `ecos_registry` sur
le nom de fichier privé de son `.html`. Une fois le défaut 1 réparé, les deux
vignettes s'écraseraient l'une l'autre.

**Renommé : `RESCOS-69 - Traumatisme MS - Basketteur 25 ans` → `RESCOS-69b - …`.**
L'autre garde le numéro nu, sur deux faits :

* il porte la **forme canonique** `RESCOS-NN - Thème - Grille ECOS`, celle de
  RESCOS-65 à 68 — c'est celui que la numérotation désigne ;
* le précédent exact du projet est `cases/rescos/` : `RESCOS-9 - Boiterie
  pédiatrique` contre `RESCOS-9b - Boiterie pédiatrique - Fillette de 2 ans`.
  Le fichier qui **ajoute un descripteur de patient** prend le suffixe.

Le suffixe est porté aux **trois endroits** où `57b` et `58b` le portent : nom
de fichier, `<title>`, `<h1>`. Aucune autre occurrence de `RESCOS-69` ne
subsiste dans le fichier. `git mv` (rename détecté, `R`). Baseline : une clé
renommée, les **12 champs identiques** sous le nouveau nom. 137 items avant,
137 après, 0 disparu.

### Signalée, non traitée : une duplication réelle

**`Fièvre et douleurs articulaires - Infection gonococcique disséminée`
⊂ `RCI-Fièvre et douleurs articulaires - Infection gonococcique disséminée`** —
inclusion stricte, remesurée : **0 item propre** à la première (106 items, tous
retrouvés dans la seconde), 85 propres à la seconde (203 items ; 162 548 contre
197 308 octets). Doublon de **contenu**, pas de nom. Arbitrer la suppression
d'une grille est un geste éditorial, hors d'un mandat de réparation technique.

---

## Défaut 4 — 92 références d'image mortes

**92 balises `<img>` sur 35 grilles**, dont **75** un chemin absolu du poste de
l'auteur et **17** un chemin relatif sans racine dans le dépôt. Invisibles au
`grep` — rien ne distingue un chemin mort d'un chemin vivant — et détectées au
**404** par le harnais navigateur. Les **11** autres images du corpus sont en
base64 : elles vivent dans le fichier, elles ne sont pas concernées.

**Aucune n'a pu être re-pointée.** Le dépôt compte 45 fichiers image.
Confrontation des 92 noms de base par égalité exacte, puis après normalisation
(accents, casse, ponctuation), puis par ressemblance : **0 correspondance**. La
meilleure ressemblance vaut 0,62 et porte sur deux sujets différents
(« algorithme paracetamol » contre `neuro-algorithme-horton.png`, une image du
corpus German). Aucun répertoire `bbn/`, `decision-partagee/` ni `images/`
n'existe dans le dépôt.

**La légende porte l'information seule** — vérifié une par une : les 92 balises
sont dans un `annexe-item` nu portant **un** `annexe-title`, **une**
`annexe-description` et **une** `<img>`, et la description énonce ce que
l'examen montre (« Radiographie thoracique montrant des contusions pulmonaires
bilatérales et un pneumothorax gauche »). Seul le `<div class="annexe-image">`
est retiré ; titre et description restent.

**Conséquence mesurée** : **0 champ** du snapshot ne bouge sur les 165 grilles —
le bloc `annexe-image` se compte en `annexe-item` nus, qui sont préservés ;
`check_no_loss` rend 0 ; la redondance reste à 1258.

**Rien n'est fabriqué.** Inventaire complet ci-dessous, restaurable si les
fichiers sources refont surface. `prune_dead_images.py --list` le régénère
depuis n'importe quelle référence git.

### Inventaire des 92 chemins perdus

Préfixe des chemins absolus, omis dans le tableau :
`/Users/damienfulliquet/Documents/-Medecine/-EXAMEN_FEDERAL/-ECOS_2025/-SSP/Cas cliniques traduits/Traduits/HTML/grilles_generees/html/images/`
Les chemins qui commencent par `bbn/` ou `decision-partagee/` sont les 17
chemins **relatifs**, sans racine dans le dépôt.

| grille (` - Grille ECOS.html` omis) | n | fichiers |
|---|---:|---|
| `AMC Urgences 1 - Polytraumatisé` | 4 | `1-Radiographie du thorax.jpg` · `2-Radiographie du bassin.jpg` · `3-Echographie E-FAST.jpg` · `4-Echographie E-FAST.jpg` |
| `AMC Urgences 2A - Embolie pulmonaire massive` | 3 | `A1-ECG.jpg` · `A2-Echocardiographie comparitive normale.jpg` · `A3-Echocardiographie aux urgences.jpg` |
| `AMC Urgences 2B - Choc septique sur péritonite` | 2 | `B1-Score SOFA.jpg` · `B2-Score qSOFA.jpg` |
| `AMC Urgences 3A - Douleur thoracique aiguë - STEMI` | 7 | `A1-ECG3.jpg` · `A2-Spectre des SCA.jpg` · `A3-Critères IM type 1.jpg` · `A4-Critères IM type 2.jpg` · `A5-Temps cibles de prise en charge.jpg` · `A6-Contre-indications à la fibrinolyse.jpg` · `A7-Etapes et délais de la prise en charge STEMI.jpg` |
| `AMC Urgences 3B - Douleur thoracique aiguë - NSTEMI` | 5 | `B1-ECG.jpg` · `B2-Protocole de prise en charge des SCA au service des urgences HUG.jpg` · `B3-Stratégie de stratification du risque dans les NSTEMI:angor instable.jpg` · `B4-…(idem, seconde planche).jpg` · `B5-Causes élévation des troponines.jpg` |
| `AMC Urgences 3C - Douleur thoracique aiguë - Dissection aortique` | 1 | `C1-Radiographie du thorax.jpg` |
| `AMC Urgences 4 - Insuffisance respiratoire aiguë sur BPCO` | 2 | `1-Radiographie du thorax4.jpg` · `2-Categories insuffisances respiratoires.jpg` |
| `AMC Urgences 5A - Hémorragie sous-arachnoïdienne` | 5 | `A1-CT-scan cérébral comparatif normal.jpg` · `A1-CT-scan cérébral en urgence.jpg` · `A2-Angio-CT en urgence.jpg` · `A3-Classification clinique des HSA-WFNS grading system.jpg` · `A4-Classification radiologique des HSA-Fischer grading system.jpg` |
| `AMC Urgences 5B - AVC ischémique avec transformation maligne` | 8 | `B1-GFAST.jpg` · `B2-Algorithme-Suspicion AVC.jpg` · `B3-CT-scan cérébral en urgence.jpg` · `B4-Stratégie thérapeutique.jpg` · `B5-Critères de revascularisation aiguë post AVC.jpg` · `B6-…(seconde planche).jpg` · `B7-CT-scan cérébral J1.jpg` · `B8-Diagnostic de mort cérébrale.jpg` |
| `BBN - Cancer du sein` | 3 | `bbn/epices-framework.jpg` · `bbn/reactions-emotionnelles-cancer.jpg` · `bbn/ressources-soutien-oncologie.jpg` |
| `BBN - Limitation thérapeutique cancer` | 3 | `bbn/evolution-cancer-scanner.jpg` · `bbn/soins-palliatifs-organisation.jpg` · `bbn/accompagnement-fin-de-vie.jpg` |
| `BBN - Sclérose en plaques` | 3 | `bbn/irm-sep-lesions.jpg` · `bbn/evolution-formes-sep.jpg` · `bbn/ressources-sep-soutien.jpg` |
| `Douleur abdominale et diarrhée fébrile` | 3 | `ct-abdo-comparaison.jpg` · `endoscopie-colon.jpg` · `histologie-colon.jpg` |
| `Douleur thoracique - Vignette clinique` | 2 | `VignetteClinique_DRS-ECG1.jpg` · `VignetteClinique_DRS-ECG2.jpg` |
| `Dyspnée post-COVID` | 2 | `Intermed-Dyspnée-Labo-1.jpg` · `Intermed-Dyspnée-Labo-2.jpg` |
| `Fatigue TBL` | 4 | `Fatigue TBL-img1.jpg` · `Fatigue TBL-img2.jpg` · `Fatigue TBL-img3.jpg` · `Fatigue TBL-img4-Examens paracliniques.jpg` |
| `Intoxication - Arrêt cardio-respiratoire … opioïdes` | 2 | `toxidromes-tableau.jpg` · `algorithme-abcde-intox.jpg` |
| `Intoxication - Syndrome anticholinergique … Belladone` | 2 | `belladone-epinards-comparaison.jpg` · `syndrome-anticholinergique.jpg` |
| `Intoxication - Syndrome malin des neuroleptiques` | 2 | `effets-neuroleptiques.jpg` · `algorithme-intoxication.jpg` |
| `Intoxication médicamenteuse - Paracétamol et benzodiazépines` | 2 | `nomogramme-rumack-matthew.jpg` · `algorithme-paracetamol.jpg` |
| `Psy-Vignette 9 - Un homme qui crie la nuit` | 1 | `Psy-Vignette 9-Critères diagnostics Schizophrénie.jpg` |
| `Psy-Vignette 10 - Une femme triste` | 1 | `Psy-Vignette 10-Episode dépressif majeur.jpg` |
| `Pédiatrie - Vomissements et état fébrile - Méningite bactérienne` | 1 | `Méningite-Algorithme.jpg` |
| `Pédiatrie - État fébrile sans foyer - Bactériémie occulte` | 3 | `FUO-img1 - 0-2 mois.jpg` · `FUO-img2 - 0-2 mois.jpg` · `FUO-img3 - 2 mois-2 ans.jpg` |
| `RESCOS-68 - Eruption cutanée` | 1 | `rescos-68-zona-thoracique.jpg` |
| `RESCOS-69 - Traumatisme MS` | 2 | `rescos-69-rx-humerus-face.jpg` · `rescos-69-rx-humerus-profil.jpg` |
| `SD - Dépistage cancer colorectal` | 2 | `decision-partagee/depistage-colon-tableau-comparatif.jpg` · `decision-partagee/depistage-colon-deroulement.jpg` |
| `SD - Dépistage cancer du sein` | 3 | `decision-partagee/statistiques-depistage-sein.jpg` · `decision-partagee/balance-depistage-sein.jpg` · `decision-partagee/deroulement-mammographie.jpg` |
| `SD - Dépistage cancer prostate` | 3 | `decision-partagee/anatomie-prostate.jpg` · `decision-partagee/statistiques-depistage-prostate.jpg` · `decision-partagee/benefices-inconvenients-prostate.jpg` |
| `SMIG-1 - Syncope` | 2 | `SMIG-1-img1-Physiopathologie de la syncope.jpg` · `SMIG-1-img2-Types de syncopes selon les étiologies.jpg` |
| `SMIG-2 - Situation 1 - Crise convulsive - Hyponatrémie sur thiazides` | 1 | `SMIG-2-Situation 1-Approche diagnostique dune hyponatrémie.jpg` |
| `SMIG-2 - Situation 2 - Masse pulmonaire - SIADH sur cancer pulmonaire` | 1 | `SMIG-2-Situation 2-Critères diagnostiques du SIADH.jpg` |
| `SMIG-2 - Situation 3 - OMI - Hyponatrémie sur insuffisance cardiaque` | 1 | `SMIG-2-Situation 3-Diagnostic différentiel dune hypernatrémie.jpg` |
| `SMIG-3 - Douleurs abdominales et nausées - Acidocétose diabétique` | 3 | `SMIG-3-img1-Définitions et diagnostic du diabète.jpg` · `SMIG-3-img2-Mécanismes physiopathologiques des décompensations diabétiques.jpg` · `SMIG-3-img3-Tableau comparatif des décompensations acido-cétosique et hyperosmolaire.jpg` |
| `SMIG-4 - Fièvre prolongée et amaigrissement - Tuberculose` | 2 | `SMIG-4-img1-Radiographie thoracique tuberculose.jpg` · `SMIG-4-img2-Radiographie laterale tuberculose.jpg` |

---

## Le contrôle en navigateur, phase `--deep`

`browser_probe.js` a gagné un mode `--deep` : le mandat demandait de vérifier le
minuteur et les crochets colorés, que le harnais ne mesurait pas. La phase est
**isolée** — ses exceptions vont dans `errsTimer` et n'entrent pas dans le
comptage comparé avant/après, qui reste dans la même unité que la mesure de
`l2`.

Passage complet, 165 grilles :

| | |
|---|---|
| minuteur : 13:00 → autre après `switchMode('exam')` + `startTimer()` | **156 / 165** |
| `.case-nav-bar` présente **et** `position: fixed` | **156 / 165** |
| recouvrement barre de navigation / minuteur | **0 / 165** |
| exceptions de cette phase | **0 / 165** |
| grilles sans aucun crochet coloré | **10 / 165** |

Les 156 sont les grilles notées ; les 9 feuilles porte n'ont ni minuteur, ni
`<script>`, ni barre — c'est leur nature. Le **non-recouvrement à 0/165** est la
vérification directe du déplacement de `.timer-container` à `top: 70px` : sans
lui, la barre de navigation serait passée sous le minuteur sur les 156.

**Les 10 grilles sans crochet coloré : 9 feuilles porte + « RESCOS-64 Toux -
Station double 2 », et c'est correct.** Vérifié des deux côtés : hors de ses
`<script>` et de son `<style>`, cette grille ne porte **aucun** `[…]` — 0 à
`260a903`, 0 aujourd'hui — quand sa jumelle « Station double 1 » en porte 33.
C'est exactement le cas de RESCOS-7 dans r7.

---

## Un incident de coordination, et sa réparation

L'utilisateur travaillait en parallèle sur `cases/german/` **et** sur un volet
`cases/casecos/` menant la même migration de moteur. Deux conséquences :

**1. Un `git reset` parallèle a désindexé un `git mv`.** Le renommage de
RESCOS-69b avait été mis en index, puis l'index a été remis à plat par le
commit `6cd583f` de l'utilisateur. Détecté par `git status` avant le commit, et
re-mis en index.

**2. Un `git commit` sans `pathspec` a emporté le travail d'autrui.** Le commit
du défaut 3 a été fait par `git add -- <mes chemins>` **puis** `git commit` nu :
`git commit` sans pathspec valide **tout l'index**, et 205 fichiers de
`cases/casecos/`, `scripts/casecos/` et `docs/superpowers/` s'y trouvaient déjà,
mis en index par le volet parallèle.

**Réparé** : branche de secours `l3-avant-reparation` posée, `git reset --soft`
jusqu'au défaut 2, index remis à plat, puis les défauts 3 et 4 recommis depuis
le contenu **exact** de leurs commits d'origine
(`git checkout <commit> -- <mes chemins>` puis `git add -A -- <mes chemins>`).
Vérifié après coup : les quatre commits ne touchent que `cases/rescos-locales`
et `scripts/rescos-locales` ; l'arbre final est **identique** à l'arbre d'avant
la réparation pour ces chemins (`git diff` vide) ; les 205 fichiers du volet
parallèle sont revenus à l'état de travail non commité, contenu intact.

**Leçon, à porter dans la procédure du projet** : sur une branche partagée,
`git commit` doit **toujours** porter son `pathspec` —
`git commit -m … -- cases/<corpus> scripts/<corpus>` — et jamais se fier au
seul `git add` scopé qui l'a précédé.

---

## Un écart de chiffres qui n'est pas une régression

`report_import_defects.py` fait passer `chevron-nu` de **787 / 156 grilles** à
**475 / 104**. Les 312 disparus sont des **opérateurs JavaScript** des moteurs
supprimés (`i <= section.count`, `currentSeconds <= 30`, `currentSeconds <= 0`),
comptés parce que ce rapport balaye le HTML brut, `<script>` compris. Vérifié :
le nombre de `chevron-nu` situés **dans un `<script>`** à `260a903` vaut
**exactement 312**. C'est le même écart que r7 avait relevé sur RESCOS, à
l'échelle de ce corpus. Aucune autre famille ne bouge.

---

## Lot `l4` — la passe de nomenclature suisse

Base `29271b2`. **424 remplacements sur 108 grilles**, aucune des 9 feuilles
porte touchée (elles ne portent pas de biologie). `check_nomenclature` passe de
**368 / 103 grilles** à **0**.

### Le relevé annoncé n'était pas le relevé réel

368 termes étaient portés au constat de `l2`. La passe en a traité **424**,
dont **56 que la table ne voyait pas**. Ils ne se répartissent pas au hasard :
chacun des cinq manques est un défaut de *bordage* du motif, pas un oubli de
famille.

| ce que le motif ne voyait pas | termes | pourquoi |
|---|---:|---|
| `Gold standard` capitalisé | **8** | `gold standard` était borné en minuscules — un cinquième de la famille |
| `ng/ml` `pg/ml` `g/dl` `mEq/l` minuscules | **17** | la table AMBOSS borne la graphie canonique ; ce corpus écrit surtout la minuscule (9 `ng/ml` contre 5 `ng/mL`) |
| `ERCP` `MRCP` `COPD` `SLE` `BSA` `QD` | **23** | familles entières absentes de la table |
| `Plaquettes` / `Leucocytes` en tête de phrase | **3 valeurs** | `_HEMO` était sensible à la casse |
| `°F`, `Doliprane`, « appeler le 15 », CRP en `mg/mL` | **5** | aucun motif ne les couvrait |

Et **deux occurrences annoncées étaient fausses** — voir « les faux positifs »
plus bas. Le compte exact de la famille « numération implicite » n'est donc pas
8 mais **8 lignes portant 9 valeurs**, dont 2 des 8 annoncées étaient à écarter
et 3 valeurs n'avaient jamais été vues.

### L'analyte décide du facteur — et rien d'autre

C'est le seul endroit du lot où une erreur aurait été **silencieuse et
grave** : un nombre faux dans une grille se lit comme un nombre vrai.

| unité de départ | occurrences | analytes | facteur | unité d'arrivée |
|---|---:|---|---|---|
| `mg/dL` | 6 | créatinine (1) | **× 88,4** | µmol/L |
| | | glycémie (4) | **÷ 18** | mmol/L |
| | | bilirubine (1) | — | *déjà en SI, doublon retiré* |
| `g/dL` + `g/dl` | 7 | hémoglobine | **× 10** | g/L |
| `ng/mL` + `ng/ml` | 14 | D-dimères (8) | **× 1** | µg/L |
| | | PCT (4), PSA (1) | **× 1** | µg/L |
| | | troponine I (1) | **× 1000** | ng/L |
| `pg/mL` + `pg/ml` | 8 | BNP / NT-proBNP | **× 1** | ng/L |
| `mEq/L` + `mEq/l` | 4 | lactate, K⁺ (monovalents) | **× 1** | mmol/L |
| `/mm³` | 17 | LCR (7) | **× 1** | /µL |
| | | sang, liquide articulaire (10) | **× 0,001** | G/L |
| numération nue | 9 valeurs | hémogramme | **× 0,001** | G/L |

**Une seule unité de départ, trois unités d'arrivée.** Les 14 `ng/mL` en sont
la démonstration : la troponine est la seule à changer d'ordre de grandeur, et
elle partage sa ligne avec un BNP en `pg/mL`, autre analyte, autre facteur.

Deux vérifications ont changé le geste :

* **`mg/dL` de RESCOS-47** — « bilirubine >50 μmol/L (3 mg/dL) ». La valeur SI
  est *déjà là* ; le `mg/dL` n'est qu'un doublon américain. Converti, il aurait
  produit une seconde valeur redondante. **Retiré, pas converti.** Contrôle :
  3 × 17,1 = 51,3 µmol/L, cohérent avec le « >50 » écrit.
* **`mg/mL` sur la CRP**, 2 occurrences — « CRP [17 mg/ml - légèrement élevée] ».
  17 mg/mL vaudrait 17 000 mg/L. **C'est le qualificatif voisin qui prouve
  l'unité voulue** : « légèrement élevée » ne peut désigner que 17 mg/L. Le
  nombre est juste, l'unité est une coquille — redressée, pas convertie. Et le
  motif est borné à la CRP : `mg/mL` est l'unité légitime de la PC20 à la
  méthacholine (2 occurrences sur AMBOSS-18).

### Plusieurs valeurs sur une ligne — quatre lignes concernées

| grille | ligne | ce qu'une conversion partielle aurait laissé |
|---|---|---|
| AMC Urgences 1 | `Hb > 7-9 g/dL, plaquettes > 50 000` | un seuil de plaquettes muet à côté d'une Hb corrigée — **deux familles différentes** |
| AMC Urgences 5C | `Leucocytes < 4000 ou > 20000` | une borne convertie, l'autre non — **même analyte** |
| AMC Urgences 2A | `Troponine I > 0.4 ng/mL, BNP > 100 pg/mL` | deux analytes, deux facteurs (× 1000 et × 1) |
| RESCOS-50, RESCOS-58 | `Hb < 7-8 g/dL` | la borne haute laissée à 8 |

### Les faux positifs — cinq motifs évidents écartés sur mesure

Chacun a une **lecture française légitime dans ce corpus même** :

* **`HIV`** — classification de Fisher modifiée, grade 4 : « HSA + hématome
  intraparenchymateux ou **HIV** ». Ici HIV = **hémorragie
  intraventriculaire**. Un `sed HIV → VIH` aurait fait du virus une
  complication de l'hémorragie méningée. 1 occurrence sur 13. *(L'abréviation a
  été développée : elle se lisait « virus » pour n'importe quel lecteur.)*
* **`ACE`** — « ACE [métastases hépatiques] », « scanner TAP, ACE » :
  **antigène carcino-embryonnaire**, pas l'*angiotensin-converting enzyme*. Le
  corpus écrit d'ailleurs `IEC` 30 fois pour les inhibiteurs.
* **`EMS`** — 34 occurrences : **établissement médico-social**, terme suisse.
  Une grille entière s'intitule « Consultation téléphonique EMS ».
* **`HR`** — « CT thoracique HR » (haute résolution) et « HR bithérapie »
  (isoniazide + rifampicine). Deux lectures, aucune anglaise.
* **`LP`** — « Tramadol LP » : libération prolongée.

Et deux faux positifs **du motif de numération implicite**, qui expliquent
pourquoi 8 occurrences annoncées ne valaient pas 8 corrections :

* **un ratio** — « PL traumatique : 1 GB pour 500-1000 GR ». Le 500 n'a pas
  d'unité et n'en veut pas ; le convertir aurait inventé une numération.
* **une borne de norme** — « plaquettes 450 G/L (N: 150-400) ». Le motif
  s'accrochait au 150 de l'intervalle de référence, dont l'unité est portée par
  le résultat douze caractères plus tôt.

Trois autres ont été écartés **sans les activer**, sur le même principe :
`SMUR` (le service existe en Suisse romande), `Augmentin` (enregistré en
Suisse), **`Spasfon`** — et celui-là pour une raison plus forte que les autres :
son équivalent suisse, le Buscopan, est **une autre molécule**. Le substituer
aurait changé le médicament, pas son nom.

### Le critère qui a tranché les traductions

Six familles nouvelles ont été activées, et une règle mesurable a décidé de
chacune : **l'équivalent français est-il déjà employé par ce corpus ?**

| ajouté | rendu par | déjà présent dans le corpus |
|---|---|---:|
| `ERCP` | CPRE | **14** |
| `MRCP` | cholangio-IRM | **6** |
| `COPD` | BPCO | **122** |
| `SLE` | LES | **16** |
| `BSA` | surface corporelle | **11** |
| `QD` | 1x/j | `x/j` **37**, `x/jour` **44** |

Le même critère a **écarté** `PTSD` (7 occurrences), `DKA` et `HHS` (5 chacun) :
ni `TSPT`, ni `ESPT`, ni `SHH` n'apparaissent nulle part dans les quatre corpus.
Les traduire aurait introduit un terme que rien n'atteste. Ils sont **mesurés et
signalés**, non corrigés.

Écarté aussi, et pour une raison de précédent : `MCV`, `MCH`, `MCHC`, `CEA`,
`HBV`, `IGRA`, `DEXA` — ce sont les graphies des **rapports de laboratoire
suisses**, pas des anglicismes.

### Ce qu'un `sed` uniforme aurait cassé — huit endroits

* **`gold standard` × 1** — « Angioplastie primaire … Gold standard: » désigne
  un **traitement**. Rendu « traitement de référence ». C'est exactement le
  « Méthotrexate = gold standard » de la campagne rescos, retrouvé ici.
* **`gold standard` × 1** — « HAM-D : échelle de Hamilton, gold standard
  clinique » : ni examen ni traitement, une **échelle**. Rendu « référence
  clinique ».
* **`gold standard` × 3** — accords et élisions : « sont **le** gold standard »
  → « sont **la méthode** de référence » ; « qui est **le** gold standard » →
  « qui est **l'**examen de référence » ; « gold standard **diagnostique** » →
  « examen de référence » (le pléonasme retiré).
* **`DMARDs` × 2** — « Traitement de fond (DMARDs) » serait devenu
  « Traitement de fond (traitement de fond) ». La parenthèse est retirée.
* **`SCFE` × 1** — « Épiphysiolyse fémorale supérieure (SCFE) » : même piège,
  même geste.
* **`BMI` × 1** — score **BODE** : « B: BMI | O: Obstruction | D: Dyspnée |
  E: Exercise ». La lettre B du mnémonique *est* l'acronyme. Rendu « B: Body
  mass index (IMC) » : mnémonique intact, français présent.
* **`HIV` × 1** — « Sites web [drugs.com, **HIV drug interactions**] » est le
  nom propre du site de l'université de Liverpool. Rendu sous sa forme d'URL,
  `hiv-druginteractions.org`, comme le `drugs.com` qui le précède.
* **`NFS` × 3** — « FSC complète » se lirait « formule sanguine complète
  complète », et la FSC inclut déjà les plaquettes (« NFS-plaquettes » × 2).

Deux mnémoniques ont en revanche été traversés **sans dommage, et c'est
vérifié** : `A = ANA` du SOAP BRAIN MD (AAN commence aussi par A), et le `C =
CSF` du Guillain-Barré, laissé intact — `CSF` n'a pas été activé.

### Les régions intouchables

`apply_lab_nomenclature.py` masque `<style>`, `<script>` et les data-URI avant
toute substitution. Ce n'est pas une précaution de principe :

* **les 165 grilles portent leur CSS en ligne** (0 `case-styles.css`). Mesure
  qui l'a imposé : rendre `_HEMO` insensible à la casse ferait matcher le `gb`
  de `rgba(0,0,0,0.2)`, et le `z-index: 1000` deux lignes plus bas complèterait
  le motif de numération implicite — **165 grilles rouges sur une feuille de
  style**. D'où l'alternance lettre par lettre sur les mots (`[Pp]laquettes`) et
  la casse **stricte** sur les acronymes (`GB`, `PNN`, `PLT`).
* **156 grilles chargent `cases/scoring.js`** depuis `l3` et portent
  `window.caseConfig`. Vérifié après la passe, sur les 108 grilles modifiées :
  régions `<style>` / `<script>` / `data:` **identiques octet pour octet**,
  `window.caseConfig` présent 108/108, `../scoring.js` présent 108/108.

Contrôle préalable exigé et fait : **une seule** occurrence d'un terme à
remplacer tombait dans un `data-criteria` **et** dans le `.criteria-text`
correspondant (`HIV` de RESCOS-68, « Dépistage Immunologique (HIV ou autre) »).
`cases/scoring.js:159` y applique `.split(". ")[1].split(" [")[0]` : `VIH`
n'introduit ni `. ` ni ` [`, et les deux porteurs ont été traités ensemble pour
qu'ils ne divergent pas. 4602 attributs `data-criteria` et 3183 `.criteria-text`
examinés.

### Vérifications

| | avant | après |
|---|---|---|
| `check_nomenclature` | **368 / 103 grilles**, code 1 | **0**, code 0 |
| `check_invariants` | OK, 165 | **OK, 165**, code 0 |
| `check_reachability` | 156/156 à 100 % | **156/156 à 100 %**, code 0 |
| `report_redundancy` | 1258 | **1260** — voir ci-dessous |
| `check_no_loss 29271b2` | — | 12 signalés, **0 perte** |
| AMBOSS `report_redundancy` | 147 | **147** |
| RESCOS `report_redundancy` | 127 | **127** |
| AMBOSS / RESCOS invariants + nomenclature | code 0 | **code 0** |

**Les 12 items « disparus » ont tous un successeur**, vérifié un par un : ce
sont des items courts où « gold standard » (13 caractères) devient « examen de
référence » (19), ce qui fait tomber la ressemblance sous 0,72 —
`irm lombaire gold standard` → `irm lombaire examen de reference` mesure 0,552.
Aucun contenu n'a disparu.

### Le seul chiffre qui monte, et pourquoi ce n'est pas une régression

`report_redundancy` passe de **1258 à 1260**. Le décompte est exact, grille par
grille : +2 Hernie discale, +2 RESCOS-56, +1 Épilepsie absence, +1 RESCOS-63,
−2 Sémiologie MSQ, −1 Ostéoporose, −1 SMIG-3.

**Aucun contenu n'a été dupliqué.** Ce compteur est un seuil de *ressemblance*
(0,72), et unifier le vocabulaire déplace mécaniquement des paires des deux
côtés du seuil — quatre le franchissent vers le haut, quatre vers le bas.

Le cas de « Hernie discale » le montre au caractère près. **Avant la passe, la
grille écrivait déjà les deux graphies du même énoncé :**

```
[theorie]      irm lombaire examen de reference        ← déjà en français
[presentation] irm lombaire gold standard              ← même énoncé, autre graphie
```

ressemblance 0,610, donc invisible au compteur. Après :

```
[theorie]      irm lombaire examen de reference
[presentation] irm lombaire examen de reference        ← ressemblance 1,000
```

**La redondance était là ; c'étaient les deux graphies qui la cachaient.** La
passe ne l'a pas créée, elle l'a rendue mesurable. Même mécanisme pour les trois
autres gains (0,652 → 0,841 ; 0,684 → 0,737 ; 0,710 → 0,746) : dans chaque cas
les deux items sont **les mêmes avant et après**, seul le ratio bouge.

Une passe de déduplication est un geste éditorial, hors du mandat de ce lot.

### Un faux positif silencieux dans le harnais, corrigé au passage

`browser_probe.js --summary` comptait `ecos_registry` **de la manière que la
PROCÉDURE interdit explicitement** : `registryKeys.length > 0`, c'est-à-dire la
**non-vacuité** du registre. Or `localStorage` est partagé par toutes les pages
de la même origine et les 165 sondages se suivent dans le même profil. Le
harnais rendait donc **165/165**, en attribuant à chaque grille les entrées des
précédentes — **y compris aux 9 feuilles porte, qui n'ont aucun `<script>` et ne
peuvent rien écrire.**

C'est exactement le comptage naïf que le § 4 de la procédure décrivait, sans que
personne remarque que le script versionné le pratiquait. Vérifié sur profil
neuf : sondées seules, les 9 feuilles porte rendent **0 clé, 0 entrée**.

Le décompte porte désormais sur la **clé propre** de chaque grille —
`saveToRegistry()` la construit depuis `location.pathname`, donc
percent-encodée, et le harnais décode pour comparer. Il rend **156/165**, le
chiffre documenté par `l3`.

L'enjeu n'est pas cosmétique : `browser_probe.js` est le **seul** contrôle
capable de voir qu'un score ne remonte pas au tableau de bord — ni
`check_invariants`, ni `check_reachability`, ni `check_nomenclature` ne le
peuvent. Un 165/165 permanent aurait masqué exactement le défaut que `l3` avait
réparé, s'il était réapparu.

### Ce que ce lot n'a pas fait

* **Aucun contenu médical réécrit** hors nomenclature : les 424 remplacements
  sont des termes, des unités et des nombres convertis à unité constante.
* **Aucune numération sans unité inventée.** Deux valeurs à unité implicite
  qu'aucun motif ne couvre restent en l'état et sont signalées :
  « Hb 13.2, Ht 31%, GB 8 G/L » (« Enfant qui boîte ») et « Bactérien : > 1000
  GB » (« Pédiatrie — Vomissements »). Choisir leur unité serait une supposition.
* **Aucune déduplication** — voir ci-dessus.
* **Rien sous `cases/german/`, `scripts/german/` ni `cases/casecos/`** : lus
  pour le bordage des motifs sur cinq corpus, jamais écrits. Le commit est
  `path`-scopé sur `cases/rescos-locales`, `scripts/rescos-locales` et ce
  journal, et toutes les commandes git de contrôle emploient
  `core.quotepath=false` — 132 des 165 noms portent un accent.
* **Aucune lecture de grille entière avec `Read`.**
* **Aucune commande réseau, aucun `git push`, aucun `git gc` ni `git prune`.**

---

## Ce que le lot `l3` n'a pas n'a pas fait

* **Rien sous `cases/german/` ni `scripts/german/`** — ni lu, ni écrit, ni
  exécuté ; l'utilisateur y travaillait en parallèle et a commité `6cd583f`
  pendant le lot. Les quatre commits sont `path`-scopés sur
  `cases/rescos-locales` et `scripts/rescos-locales`.
* **Aucune modification de `cases/casecos/` ni de `scripts/casecos/`** : le
  volet parallèle qui y travaille a été emporté par erreur dans un commit, puis
  intégralement restitué — voir « Un incident de coordination ».
* **`docs/obsidian-mapping.yaml` n'a pas été touché.** Il désigne les deux
  RESCOS-69 par leur chemin **dans le vault**
  (`_bibliotheque/ECOS/rescos-grilles-locales/…`), pas dans le dépôt ; il est
  régénéré par un script en cours d'écriture chez l'utilisateur.
* **Aucune modification de `cases/scoring.js`**, `srs.js`, `persistence.js`,
  `case-styles.css` ni d'aucun fichier partagé.
* **Aucune passe de nomenclature** : 368 termes non suisses restent, et
  `check_nomenclature` reste rouge — c'est le constat de `l2`, inchangé.
* **Aucune image fabriquée.**
* **Aucune lecture de grille entière avec `Read`.**
* **Aucune commande réseau, aucun `git push`, aucun `git gc` ni `git prune`.**

---

## Lot `l5` — grille pilote RESCOS-58b, Rectorragies

Base `5d16c20`. **Une seule grille de `cases/` modifiée** :
`cases/rescos-locales/RESCOS-58b - Rectorragies - Grille ECOS.html`.
**Redondance inter-blocs : 41 → 14.** Corpus : 1260 → **1233** (−27, soit
exactement le gain de la grille : aucune paire d'une autre grille n'a bougé).

C'était la grille la plus redondante des 33 numérotées RESCOS-41 à 69.

### La page SSP qui dessert cette grille

`SSP ECOS/SSP — Rectorragies & Hémorragie Digestive Basse.md`, trouvée par
recherche de motif dans le vault — `docs/obsidian-mapping.yaml` ne couvre que
`cases/rescos/`. Elle **nomme explicitement RESCOS-58 et RESCOS-58b** dans son
bloc « Références PDF », avec sept autres grilles des quatre corpus.

**Le prédicteur du volet `rescos` se confirme, et se précise.** Le rendement du
niveau 1 ne tient pas au nombre de grilles desservies mais aux **cibles
chiffrées**. Ici la page en porte cinq (Hb < 70 g/L / < 80 g/L si cardiopathie
ischémique · Oakland ≤ 8 · GBS 0-1 · coloscopie ≤ 24 h · FIT/coloscopie
50-69 ans) — et le niveau 1 a tranché **trois** points, contre zéro sur
RESCOS-21. Là où r3 concluait « le niveau 1 ne servira presque jamais », ce
pilote montre que la conclusion dépend du sujet : une page à seuils tranche.

### Les trois corrections de niveau 1

**1. `theorie`/Causes selon l'âge — « ischémie mésentérique » → « colite
ischémique ».** La page SSP nomme la **colite ischémique** parmi les causes
coliques de rectorragies (« douleur abdominale brutale (typiquement flanc
gauche) + rectorragies, sujet > 60 ans, FRCV »), et sa carte ECOS fait de la
confusion avec l'ischémie mésentérique le piège du sujet : « ne pas manquer
l'**ischémie mésentérique aiguë** du grêle (douleur ≫ examen, terrain FA), qui,
elle, est une urgence vitale ». Le bloc citait la seconde à la place de la
première.

**2. `theorie`/Évaluation de la gravité — « Anémie aiguë: Hb < 100 g/L avec
microcytose ».** Deux défauts en un item, et la page SSP tranche les deux :

* elle écrit, au dosage de la FSC, « — la chute d'Hb peut être **tardive** en
  aigu », et sa carte ECOS en fait un piège : « se fier à l'Hb initiale : elle
  est faussement normale au début, l'hémodilution prenant plusieurs heures. Ce
  sont la FC, la PA et les marbrures qui décident. » Ériger `Hb < 100 g/L` en
  critère de gravité d'une hémorragie **aiguë** est exactement ce que la page
  interdit ;
* une microcytose ne peut pas accompagner une anémie aiguë — elle signe une
  spoliation **chronique**. L'item décrivait en fait le patient de la vignette
  (Hb 92 g/L, VGM 72 fL, section notée), pas une règle.

Réécrit : « Anémie: Hb < 100 g/L, mais l'Hb initiale est faussement rassurante
en aigu (hémodilution retardée); une microcytose signe un saignement
chronique ». Le seuil est conservé, les deux erreurs tombent.

**3. `annexe-dd`/Diverticulose colique — les arguments CONTRE étaient ceux de la
diverticul*ite*.** Le bloc portait « Absence de douleur abdominale » et « Pas de
fièvre » **CONTRE** l'hémorragie diverticulaire. Or la page SSP décrit
l'hémorragie diverticulaire comme « saignement **abondant, indolore**,
intermittent, > 50 ans ; cause la plus fréquente d'HDB sévère », et sa carte
ECOS nomme précisément cette confusion : « **Piège :** croire que
"diverticulite = saignement". Ce sont deux complications distinctes et quasi
exclusives : la diverticulite fait mal et ne saigne presque jamais. »

L'absence de douleur était donc un argument **POUR**, rangé du mauvais côté.
Corrigé :

| | avant | après |
|---|---|---|
| POUR | Âge > 50 ans · Saignement abondant · Alternance du transit | Âge > 50 ans · **Saignement abondant et indolore** |
| CONTRE | Absence de douleur abdominale · Pas de fièvre | **Saignement isolé, sans amaigrissement ni masse au TR** |

« Pas de fièvre » disparaît comme **erreur factuelle** (la fièvre ne discrimine
pas une hémorragie diverticulaire) ; le fait clinique survit trois fois — critère
noté « 4. Symptômes systémiques → Fièvre [Non] », `scenario`, et
`presentation`/Version longue. « Alternance du transit » quitte les arguments
POUR pour la même raison et reste porté par `annexe-dd`/Cancer du rectum,
`annexe-dd`/Cancer du côlon, `theorie` et `resume`.

**`annexe-dd` est éditable malgré son emplacement.** Il vit ici dans le
`criteria-row` du critère noté « 2. Hypothèses diagnostiques », mais ne porte
aucune case à cocher : le `<input>` appartient au critère englobant. Y toucher
ne peut pas déplacer le barème — c'est la règle du § 3 de
`scripts/amboss/PROCEDURE.md`, et c'est ce qui distingue `annexe-dd` de
`therapy` et `redflags`, qui sont, eux, des **attendus de correction**.

### Le trou du bloc canonique, trouvé par la méthode r3 § 6

`resume`/Prise en charge ne portait **que la stratégie oncologique** (RCP,
stades I à IV, suivi, dépistage, prévention). Aucune mesure immédiate — pour un
patient qui arrive aux urgences avec un saignement actif et une Hb à 92 g/L.

L'information reliait le noté (`therapy`, et le critère « 4. Propose une
hospitalisation (suivi hémoglobine et investigations) ») à `presentation`/§3
**sans passer par `resume`**. C'est exactement le symptôme décrit par r3 § 6, et
aucun contrôle ne le signale.

**Porté dans le canonique avant toute réduction de `presentation`** — sous-section
« Mesures immédiates » : hospitalisation avec surveillance rapprochée de
l'hémoglobine · arrêt de l'aspirine et des AINS · transfusion si Hb < 70 g/L ou
instabilité hémodynamique, **seuil < 80 g/L si cardiopathie ischémique**.

La nuance des 80 g/L est le **quatrième point de niveau 1** : elle vient de la
page SSP (« stratégie restrictive : seuil Hb < 70 g/L (< 80 g/L si cardiopathie
ischémique) ») et elle est pertinente ici — le patient a une aspirine cardio
« récemment introduite en prévention cardiaque ». Elle est portée dans le
**pédagogique** ; `therapy`, qui est dans la section notée, n'a pas été touché.

### Les quatre gestes de redondance, et leur rendement

| geste | paires | fondement |
|---|---:|---|
| `presentation`/§1 — fusion des puces POUR/CONTRE | −18 | r3 § 1.3, forme `structured` conservée |
| `presentation`/Touches ludiques — retrait de la liste « Red flags cancer colorectal » | −5 | règle du format : copie six-pour-six de `theorie`/Signes d'alarme |
| `presentation`/§2 et §3 — `presentation-reponse list` → registre parlé | −4 | « Redire à l'oral, pas en liste » |
| `annexe-dd`/Diverticulose — correction de niveau 1 | −3 | effet de bord de la correction ci-dessus |

**§1 est resté en forme `structured`.** La tentation était de le convertir en
`presentation-reponse text` ; le précédent r3 dit le contraire — RESCOS-21 a
gardé `reponse-pour` / `reponse-contre` et **fusionné les puces** en lignes plus
longues et plus discriminantes. C'est aussi la forme d'AMBOSS. 17 puces → 8
lignes ici ; la fusion suffit à faire tomber le ratio sous le seuil sans changer
la structure que les deux corpus partagent.

**La `mnemo-box` « RED FLAG » a été déplacée, pas supprimée** — de
`presentation`/Checklist mentale vers `presentation`/Touches ludiques, geste du
§ 3 de `scripts/amboss/PROCEDURE.md` (précédents AMBOSS-2 et AMBOSS-3). Elle est
strictement plus riche que la liste supprimée (elle ajoute `D` = dyspnée /
étourdissements, le symptôme d'appel du patient, et `G` = groupe sanguin) et
c'est un **changement de format**, donc protégé. La Checklist mentale redevient
une trame pure — axe 5 satisfait.

Deux mnémos coexistent désormais dans Touches ludiques, RED FLAG et CANCER. Ils
ne se doublent pas : le premier énumère les signaux d'alarme, le second le
tableau néoplasique. Leurs deux clés `R = Rectorragies persistantes` produisent
4 des 14 paires résiduelles — plancher irréductible, et les clés de mnémo ne se
retouchent pas.

### Les 14 paires résiduelles, justifiées

| # | score | couple | justification |
|---|---|---|---|
| 1 | 1,0 | annexe-dd ↔ theorie | « masse palpable au toucher rectal » : signe cardinal, argument POUR ↔ signe d'alarme |
| 2-3 | 0,96 ×2 | annexe-dd ↔ presentation | clé `R` des deux mnémos ↔ argument POUR — mnémos protégés |
| 4 | 0,88 | annexe-dd ↔ expert | intitulé d'hypothèse : liste de l'évaluateur ↔ raisonnement |
| 5 | 0,85 | annexe-dd ↔ theorie | « modification du transit » : plancher structurel |
| 6 | 0,77 | annexe-dd ↔ resume | « rectorragies persistantes » : plancher |
| 7 | 0,77 | annexe-dd ↔ theorie | « antécédent familial de cancer » : plancher |
| 8 | 0,76 | resume ↔ theorie | FSC : `resume` liste le bilan oncologique, `theorie` le bilan de l'hémorragie aiguë — deux listes complémentaires, indications portées (axe 1) |
| 9-10 | 0,75 ×2 | resume ↔ presentation | clé `R` des deux mnémos |
| 11 | 0,74 | theorie ↔ presentation | clé `G` du mnémo ↔ « groupe sanguin, RAI si transfusion envisagée » |
| 12 | 0,74 | annexe-dd ↔ expert | comme #4 |
| 13 | 0,73 | resume ↔ presentation | « habitudes de vie » : item de trame de la Checklist mentale (axe 5) |
| 14 | 0,73 | resume ↔ theorie | antécédents familiaux : plancher |

Six paires sur quatorze sont des clés de mnémo, cinq le plancher structurel de
r3 § 1.4, deux la liste de l'évaluateur, une l'axe 1.

**`expert` n'a pas été touché.** Sa liste de quatre diagnostics différentiels
double `annexe-dd` (paires #4 et #12), mais c'est la **fiche que l'évaluateur
tient à la station** : la retirer le priverait de sa référence de correction.
`expert` porte par ailleurs du contenu strictement unique — la carte de
laboratoire et le mannequin de toucher rectal.

### `check_no_loss 5d16c20` — 14 items, verdictés un à un

| item disparu | où il survit |
|---|---|
| `saignement abondant` | reformulé sur place : « Saignement abondant **et indolore** » |
| `alternance du transit` (POUR diverticulose) | correction de niveau 1 ; le fait est dans `annexe-dd` ×2, `theorie`, `resume` |
| `pas de fievre` (CONTRE diverticulose) | correction de niveau 1 ; le fait est dans le critère noté 4, `scenario`, Version longue |
| `anemie aigue hb 100 g l avec microcytose` | reformulé sur place |
| `rectorragies nouvelles apres 50 ans` | `theorie`/Signes d'alarme, mot pour mot |
| `anemie microcytaire` | fusionné dans §1 Q1 ; aussi `annexe-dd`/Cancer du côlon |
| `saignement possible` | remplacé par un énoncé plus fort (« première cause d'HDB sévère ») |
| `fsc crase groupe sanguin` | §2, registre parlé ; `resume`/Biologie ; `therapy` |
| `scanner tap metastases` | §2, registre parlé ; `resume`/Imagerie |
| `transfusion si hb 70 g l ou instabilite` | **porté dans `resume` avant retrait** ; §3 parlé ; `therapy` |
| `coloscopie biopsies` | §3 parlé ; `resume`/Imagerie ; `therapy` |
| `bilan extension irm pelvienne scanner tap` | §2 et §3 parlés ; `resume`/Imagerie |
| `discussion rcp …` | §3 parlé (« colloque multidisciplinaire (RCP) ») ; `resume`/Stratégie |
| `suivi oncologique et coloscopique regulier` | §3 parlé, mot pour mot ; `resume`/Suivi |

**Aucune perte.** Deux disparitions sont des **corrections factuelles** assumées,
les douze autres des reformulations ou des fusions.

### Barème — règle 1, strictement

Toutes les éditions portent sur `annexe-dd`, `resume`, `theorie` et
`presentation` — **aucun bloc noté**. 0 sous-item noté ajouté ou retiré ;
`maxScores`, `<span class="score">`, `sectionInfo[].count` et `coef` intacts ;
**baseline non régénérée**. `criteriaCount` 25, `detailCount` 32, `radioCount`
73, `checkboxCount` 32 — inchangés, et `check_invariants` le confirme sur les
165 grilles. Ni `window.caseConfig`, ni les `<script>`, ni un `.criteria-text`
n'ont été approchés. Les crochets de `cloture` sont intacts — la phase `--deep`
compte des crochets colorés sur la grille.

### Deux divergences consignées, non corrigées

**1. `therapy` (section notée) : « Coloscopie totale en urgence différée (dans
les 24-48h) » contre « ≤ 24 h » de la page SSP** (« en urgence (≤ 24 h, après
préparation) si HDB sévère / persistante »). C'est une divergence **dans une
section notée** : elle se consigne, elle ne se corrige pas. Aucun bloc
pédagogique ne porte de délai contradictoire — vérifié : `theorie`, `resume` et
`presentation` nomment la coloscopie sans délai. Rien à aligner.

**2. `annexe-dd`/Hémorroïdes : « Pas de douleur anale » en argument CONTRE.**
La page SSP décrit les hémorroïdes comme « sang rouge vif après les selles,
**indolore** » — l'absence de douleur ne plaide donc pas contre elles. Mais
l'intitulé du bloc est « Hémorroïdes **ou autre problème proctologique (fissure
etc)** », et pour une fissure anale (« douleur aiguë à la défécation », SSP)
l'argument est juste. La page ne tranche pas l'entrée **groupée** : niveau 3,
laissé en l'état. C'est la même famille d'erreur que celle corrigée sur la
diverticulose, mais sans l'appui explicite qui autorisait la correction.

### Vérifications

```
check_invariants.py                 OK — 165 grilles, code 0
check_nomenclature.py               OK — 0 terme, code 0
check_reachability.py               OK — 156/156 notées à 100 %, code 0
report_redundancy.py RESCOS-58b     41 -> 14
report_redundancy.py (corpus)       1260 -> 1233
check_no_loss.py 5d16c20            14 items, verdictés, 0 perte
browser_probe.js RESCOS-58b --deep  0 exception, 100 %, ecos_registry écrit,
                                    barre nav fixed sans recouvrement,
                                    crochets colorés présents
bounds_anomalies / uncovered_content  [] / {}
AMBOSS report_redundancy            147 (inchangé) · 3 portes code 0
RESCOS report_redundancy            127 (inchangé) · 3 portes code 0
```

### Ce que le lot `l5` n'a pas fait

* **Rien sous `cases/german/`, `scripts/german/`, `cases/casecos/` ni
  `scripts/casecos/`** — ni lu, ni écrit. Le commit est `path`-scopé sur
  `cases/rescos-locales/` et ce journal ; l'utilisateur travaillait en parallèle
  sur casecos et a commité `42aa4e0` pendant le lot.
* **Aucune modification de `cases/scoring.js`** ni d'aucun fichier partagé.
* **Aucun bloc créé** : `annexe-qr` et `feuille-porte` n'ont pas été approchés.
* **Aucune lecture de grille entière avec `Read`** — bornes par `block_spans`,
  puis `Read` avec `offset`/`limit`.
* **Aucune commande réseau, aucun `git push`, aucun `git gc` ni `git prune`.**

---

## Lot `l6a` — RESCOS-41 à 55, quinze grilles

Base `135dbca`. Quinze grilles de `cases/rescos-locales/` modifiées, rien
d'autre. **Redondance inter-blocs du lot : 87 → 1.** Corpus **1233 → 1147**
(−86, exactement le gain du lot — l'enseignement 6 du pilote se confirme à la
deuxième mesure). Témoins inchangés : AMBOSS **147**, RESCOS **127**.

### Avant / après, grille par grille

| grille | avant | après | gain |
|---|---:|---:|---:|
| RESCOS-41 — Dysurie (cervicite à Chlamydia) | 26 | **1** | −25 |
| RESCOS-42 — Dysurie (cystite simple) | 13 | **0** | −13 |
| RESCOS-43 — EM tabac | 0 | **0** | 0 |
| RESCOS-44 — Fatigue (diabète inaugural) | 0 | **0** | 0 |
| RESCOS-45 — Fatigue (dépression gériatrique) | 0 | **0** | 0 |
| RESCOS-46 — Fièvre (endocardite) | 15 | **0** | −15 |
| RESCOS-47 — Ictère (néoplasie pancréato-biliaire) | 16 | **0** | −16 |
| RESCOS-48 — Lombalgie | 0 | **0** | 0 |
| RESCOS-49 — Malaise (hypoglycémie) | 1 | **0** | −1 |
| RESCOS-50 — Malaise (syncope, anémie ferriprive) | 0 | **0** | 0 |
| RESCOS-51 — Œdèmes des MI (syndrome néphrotique) | 8 | **0** | −8 |
| RESCOS-52 — Paralysie (AIT) | 1 | **0** | −1 |
| RESCOS-53 — Parésie facio-brachiale (AVC) | 2 | **0** | −2 |
| RESCOS-54 — Présentation au CDC | 3 | **0** | −3 |
| RESCOS-55 — Colloque social | 2 | **0** | −2 |
| **total** | **87** | **1** | **−86** |

La paire résiduelle de RESCOS-41 est le **plancher structurel** de r3 § 1.4 :
`resume` liste les complications par sexe, `expert` les nomme comme risque à
signaler à la station. `expert` ne se touche pas.

### Le mapping inverse a couvert les quinze grilles

L'enseignement 2 du pilote se généralise sans exception. Une recherche
`RESCOS-(4[1-9]|5[0-5])` dans le vault rend **dix pages**, et chacune nomme ses
grilles dans son bloc « Références PDF » :

`SSP — Dysurie` (41, 42) · `Skills — Entretien Motivationnel` (43) ·
`SSP — Fatigue` (44, 45) · `SSP — Fièvre` (46) · `SSP — Ictère` (47) ·
`SSP — Lombalgies` (48) · `SSP — Malaise & PC brève` (49, 50) ·
`SSP — Œdèmes des MI` (51) · `SSP — Parésie - AVC` (52, 53) ·
`Skills — Présentation de Cas` (54, 55).

**Deux grilles relèvent d'une page « Skills » et non d'une page « SSP »** — le
motif de recherche doit couvrir tout le vault, pas le seul dossier `SSP ECOS/`.

### Le niveau 1 a tranché douze points

Le prédicteur du pilote — densité de seuils chiffrés sur la page — se vérifie :
les pages les plus chiffrées (`Parésie - AVC`, `Fièvre`, `Ictère`, `Dysurie`)
ont produit les arbitrages, la page `Entretien Motivationnel` aucun.

**Corrections d'erreur (5).**

1. **RESCOS-42 · `theorie` et `presentation` — nitrofurantoïne 100 mg x2/j.**
   `SSP — Dysurie` écrit **100 mg 3×/j pendant 5 j**. Le schéma 2×/j est la
   forme nord-américaine (monohydrate/macrocristaux) ; appliqué à la
   nitrofurantoïne du Compendium suisse, il **sous-dose**. Corrigé aux deux
   endroits. La posologie n'apparaît dans **aucun** sous-item noté : règle 1.
2. **RESCOS-46 · `resume` — « ETO préférable à ETT » et « ETO systématique ».**
   La page impose **ETT en première intention, ETO si la suspicion persiste**,
   et nomme le piège : « une ETT normale n'élimine pas l'endocardite
   (sensibilité ~60-70 %) ». Les deux items disaient l'inverse de la séquence
   suisse. Corrigés en portant la sensibilité.
3. **RESCOS-47 · `theorie` — « Seuil de visibilité : bilirubine > 50 µmol/L ».**
   La page écrit **~35-40 µmol/L**, subictère scléral dès 25-35. Corrigé.
4. **RESCOS-47 · `theorie` — « Triade classique : ictère + douleur + perte de
   poids ».** Contradiction interne et contradiction avec la page. `expert` et
   `presentation` disent tous deux *ictère + perte de poids + anorexie*, la
   ligne suivante de `theorie` dit « ictère indolore », et la page range la
   douleur parmi les caractères **absents** du cancer du pancréas. Corrigé en
   « ictère progressif INDOLORE, amaigrissement et anorexie », avec la mention
   explicite du piège. Voir « Préoccupations ».
5. **RESCOS-52 · `theorie` — « Définition moderne : symptômes < 1 heure ».**
   La définition actuelle de l'AIT est **tissulaire, non temporelle** :
   régression complète **sans lésion en DWI**. La page l'écrit mot pour mot.
   Corrigé, la durée reprise comme donnée descriptive (« < 24 h, le plus
   souvent < 1 h »).

**Précisions chiffrées portées depuis la page (7).** RESCOS-42 posologies de
`resume` (fosfomycine 3 g, pivmécillinam 400 mg ×3/j, nitrofurantoïne
100 mg ×3/j) et épargne des fluoroquinolones · RESCOS-46 définition de la fièvre
(≥ 38,0 °C tympanique / ≥ 38,3 °C rectal) et protocole d'hémocultures
(3 paires sur 24 h, 8-10 mL/flacon, bactériémie continue) · RESCOS-44 critères
diagnostiques du diabète (glycémie à jeun ≥ 7,0 mmol/L ×2 ou HbA1c ≥ 6,5 %) et
seuil d'Epworth > 10 · RESCOS-48 « > 90 % mécaniques, guérison en 4-6 semaines,
pas d'imagerie sans drapeau rouge » et **décompression < 48 h** dans la queue de
cheval · RESCOS-53 **TA cible avant thrombolyse < 185/110 mmHg**.

### Les trous du bloc canonique — sept, dont quatre de sécurité

L'enseignement 5 se confirme, et **s'étend au-delà de `resume`** : sur les onze
grilles de ce lot **sans `resume`** (43, 44, 45, 48, 49, 50, 51, 52, 53, 54,
55), c'est `theorie` qui joue le rôle de fiche canonique, et le même symptôme
s'y lit — une information que la page tient pour capitale et qu'aucun bloc de la
grille ne porte.

| grille | ce qui manquait | où porté |
|---|---|---|
| RESCOS-41 | la **ceftriaxone 250 mg IM** du co-traitement gonococcique — pourtant sous-item **noté** (`m4-detail-1`) et présent dans `presentation` | `resume`/Antibiothérapie |
| RESCOS-42 | toutes les **posologies** : `resume` disait « fosfomycine dose unique », « nitrofurantoïne 5 jours », sans une seule dose | `resume`/Antibiothérapie |
| RESCOS-46 | l'**évaluation de gravité** : aucun qSOFA, aucun lactate, pour une fièvre à 39,1 °C aux urgences | `resume`/Urgence |
| RESCOS-47 | l'**antibiothérapie de l'angiocholite** : `resume` nommait l'angiocholite deux fois et ne portait que le drainage. **Ceftriaxone 2 g + métronidazole** ajoutés. Et le **TP/facteur V**, que la page érige en seul marqueur précoce de gravité hépatique | `resume`/Prise en charge et /Biologie |
| RESCOS-48 | l'**anévrisme de l'aorte abdominale** : zéro occurrence dans toute la grille, pour un homme de 75 ans lombalgique. La page le range parmi les urgences et impose la palpation abdominale au-delà de 60 ans | `theorie`/Drapeaux rouges et /Examen clinique |
| RESCOS-50 | la **recherche du saignement digestif** : zéro occurrence de ferritine, de source de saignement ou d'endoscopie, pour un homme de 30 ans en anémie ferriprive. Règle du corpus SSP : « anémie ferriprive chez un homme = saignement digestif jusqu'à preuve du contraire » | `theorie`/Syncope et anémie et /Examens |
| RESCOS-53 | la **glycémie capillaire** : absente de la grille entière, alors que la page en fait la règle d'or (« l'hypoglycémie est le grand mimic », < 3,9 mmol/L) | `theorie`/Évaluation clinique |
| RESCOS-43 | la **pharmacothérapie** : `theorie` chiffrait « EM + pharmacothérapie : 15-30 % » sans jamais nommer une molécule | `theorie`/Sevrage tabagique |
| RESCOS-49 | l'**inefficacité du glucagon** quand les réserves hépatiques de glycogène sont épuisées — et l'alcool figure dans les causes listées par la grille elle-même | `theorie`/Rappels |
| RESCOS-52 | la **glycémie capillaire** et le score **ABCD2**, que la page nomme comme l'outil de stratification de l'AIT | `theorie`/Diagnostic |

### Les gestes de réduction, par famille

* **§2 et §3 convertis en `presentation-reponse text`** — les 4 grilles à
  `presentation` (41, 42, 46, 47), 8 listes converties. C'est le geste le plus
  rentable : **26 des 86 paires**.
* **§3 « Traitement immédiat » fusionné** — la `reponse-section` n'est pas une
  `presentation-reponse list` ; elle se **fusionne** comme §1, elle ne se
  convertit pas. 15 paires.
* **§1 fusionné, forme `structured` conservée** — enseignement 3 appliqué sans
  exception. 6 paires.
* **Listes de « Touches ludiques » recopiées** — une seule suppression pleine
  (RESCOS-41, « Complications possibles », copie 5/5 de `theorie`/Complications,
  vérifiée item par item) ; ailleurs, **fusion** plutôt que suppression, parce
  qu'un item propre s'y cachait toujours (« Confondre avec une cystite simple »,
  « Tabac facteur principal »).
* **`theorie` allongé face à `therapy`, `redflags` et `expert`** — sur les
  grilles sans `presentation` (51, 54, 55, 49, 52, 53), l'unique côté mobile est
  `theorie` et `annexe-dd`. 22 paires, toutes tombées en **enrichissant** le
  côté mobile, jamais en le tronquant.
* **`annexe-dd` retouché sur 3 grilles** (51, 53, 54) — enseignement 4 : aucune
  case à cocher, donc barème hors d'atteinte. Retouches d'enrichissement
  (œdème péri-orbitaire matinal du syndrome néphrotique, que la page nomme deux
  fois), pas de correction d'argument mal rangé — **aucun n'était mal rangé
  dans ce lot**.

### Barème — règle 1, strictement

Toutes les éditions portent sur `resume`, `theorie`, `presentation` et
`annexe-dd`. **Aucun bloc noté** : `therapy` et `redflags` (RESCOS-51, 54, 55)
n'ont pas été approchés, et les divergences qu'ils portent sont consignées
ci-dessous plutôt que corrigées. 0 sous-item ajouté ou retiré ; `maxScores`,
`<span class="score">`, `sectionInfo[].count` et `coef` intacts ; **baseline non
régénérée**. Vérifié sur le diff : aucune ligne touchant `window.caseConfig`,
`<script`, `criteria-text`, `criteria-detail`, `type="checkbox"`,
`type="radio"`, `maxScores`, `sectionInfo` ou `coef`.

### Vérifications

```
check_invariants.py                 OK — 165 grilles, code 0
check_nomenclature.py               OK — 0 terme, code 0
check_reachability.py               OK — 156/156 notées à 100 %, code 0
report_redundancy.py 41→55          87 -> 1
report_redundancy.py (corpus)       1233 -> 1147  (−86 = gain du lot)
check_no_loss.py 135dbca            67 items, verdictés un à un, 0 perte
browser_probe.js RESCOS-4x --deep   9/9 sans exception · 9/9 à 100 % · registry
browser_probe.js RESCOS-5x --deep   12/12 sans exception · 12/12 à 100 % · registry
                                    barre nav fixed sans recouvrement, crochets colorés
AMBOSS  report_redundancy 147 (inchangé) · 3 portes code 0
RESCOS  report_redundancy 127 (inchangé) · 3 portes code 0
```

Les sondes navigateur couvrent 21 grilles (les préfixes `RESCOS-4` et `RESCOS-5`
englobent 56 à 59 en plus des quinze du lot) : aucune régression sur les six
voisines.

### Ce que le lot `l6a` n'a pas fait

* **Rien sous `cases/german/`, `scripts/german/`, `cases/casecos/` ni
  `scripts/casecos/`** — ni lu, ni écrit. Commit `path`-scopé.
* **Aucun bloc créé.** Onze des quinze grilles n'ont ni `resume` ni
  `presentation` ; ils n'ont pas été fabriqués, l'information canonique
  manquante a été portée dans `theorie`.
* **Aucune lecture de grille entière avec `Read`** — bornes par `block_spans`,
  puis `Read` avec `offset`/`limit`.
* **Aucune modification de `cases/scoring.js`** ni d'aucun fichier partagé.
* **Aucune commande réseau, aucun `git push`, aucun `git gc` ni `git prune`.**

## Lot `l6b` — RESCOS-56 à 69, dix-sept grilles

Base `b646e68`. Dernier lot des 33 grilles numérotées. Seize grilles de
`cases/rescos-locales/` modifiées (la dix-septième, « RESCOS-64 station double
2 », ne porte aucun bloc mobile — voir plus bas). **Redondance inter-blocs du
lot : 133 → 3.** Corpus **1147 → 1017** (−130, exactement le gain du lot ;
l'enseignement 6 du pilote se vérifie à la troisième mesure). Témoins
inchangés : AMBOSS **147**, RESCOS **127**.

### Avant / après, grille par grille

| grille | avant | après | gain |
|---|---:|---:|---:|
| RESCOS-56 — Prurit (ictère obstructif) | 27 | **1** | −26 |
| RESCOS-57 — Ralentissement, EMS, téléphonique | 0 | **0** | 0 |
| RESCOS-57b — Ralentissement, téléphonique | 10 | **0** | −10 |
| RESCOS-58 — Rectorragies | 2 | **0** | −2 |
| RESCOS-59 — SD cholestérol | 0 | **0** | 0 |
| RESCOS-60 — SD iléus palliatif | 0 | **0** | 0 |
| RESCOS-61 — Suivi de grossesse | 2 | **0** | −2 |
| RESCOS-62 — Toux (pneumonie communautaire) | 16 | **0** | −16 |
| RESCOS-63 — Toux pédiatrique (coqueluche) | 19 | **0** | −19 |
| RESCOS-64 — Toux, station double 1 | 1 | **0** | −1 |
| RESCOS-64 — Toux, station double 2 | 0 | **0** | 0 |
| RESCOS-65 — Tremblements | 0 | **0** | 0 |
| RESCOS-66 — Troubles de l'équilibre | 1 | **0** | −1 |
| RESCOS-67 — Fatigue (hypothyroïdie) | 10 | **0** | −10 |
| RESCOS-68 — Éruption cutanée (zona) | 30 | **2** | −28 |
| RESCOS-69 — Traumatisme MS (médico-légal) | 2 | **0** | −2 |
| RESCOS-69b — Traumatisme MS, basketteur | 13 | **0** | −13 |
| **total** | **133** | **3** | **−130** |

Les trois paires résiduelles sont le **plancher structurel** : une clé de mnémo
JAUNE de RESCOS-56 face à `expert`, et les deux clés « A = Antécédent de
varicelle » des mnémos ZONA et PAVE de RESCOS-68 face à `expert`. Un mnémo est
un changement de format, il ne se démonte pas ; `expert` ne se touche pas.

### Le mapping inverse a couvert les dix-sept grilles

Une recherche `RESCOS-(5[6-9]|6[0-9])b?` sur le vault rend **treize pages**,
chacune nommant ses grilles :

`SSP — Prurit` (56) · `SSP — Confusion` (57, 57b) · `SSP — Rectorragies` (58) ·
`SSP — SD Counselling Dépistages` (59) · `Skills — Décision Partagée` (60) ·
`SSP — Grossesse` (61) · `SSP — Toux Chronique` (62, 63) ·
`SSP — Hémoptysie` **et** `Skills — Présentation de Cas` (64, une page par
station) · `SSP — Tremblement` (65) · `SSP — Trouble de la Marche` (66) ·
`SSP — Fatigue` (67) · `SSP — Éruption Cutanée` (68) ·
`SSP — Douleur d'Épaule` (69, 69b).

**Deux nuances nouvelles.** La station double 64 est desservie par **deux
pages différentes**, une par volet — la page de contenu pour la station
clinique, la page de compétence pour la station de présentation. Et
`SSP — Douleur d'Épaule` référence encore RESCOS-69b sous **son ancien nom**
(« RESCOS-69 - Traumatisme MS - Basketteur »), antérieur au renommage du lot
`l3` : le vault n'a pas été mis à jour, le lien local y est mort.

### Le niveau 1 a tranché quatorze points

**Corrections d'erreur (8).** Deux d'entre elles sont de la famille « énoncé
qui, appliqué, écarte le bon diagnostic » et sont détaillées à la section
« Préoccupations » du rapport `l6b`.

1. **RESCOS-67 · `theorie` — « TSH abaissée et T4 libre augmentée =
   hypothyroïdie primaire ».** Exactement l'inverse. Le `resume` de la même
   grille écrit correctement « TSH élevée + T4L basse ». Corrigé, avec le couple
   inverse et le cas de l'hypothyroïdie centrale.
2. **RESCOS-58 · `theorie` — « Hémoglobine < 80 g/L » en critère de gravité
   d'une hémorragie aiguë.** C'est l'erreur du pilote (RESCOS-58b portait
   `< 100 g/L`), sur la même page SSP, qui nomme le piège : l'Hb initiale est
   faussement rassurante. Corrigé.
3. **RESCOS-61 · `theorie` — « Tocolyse : β2-mimétiques, inhibiteurs calciques,
   atosiban ».** `SSP — Grossesse` écrit « atosiban, nifédipine — **pas de
   salbutamol** ». Les β2-mimétiques ne sont plus recommandés dans cette
   indication. Corrigé dans `theorie` ; la mention subsiste dans un sous-item
   **noté**, consignée.
4. **RESCOS-60 · `theorie` — métoclopramide listé sans réserve parmi les
   antiémétiques de l'iléus malin.** C'est un prokinétique : contre-indiqué dans
   l'obstruction complète, celle de la vignette (vomissements fécaloïdes, arrêt
   des matières et des gaz depuis 48 h). Borné à l'obstruction incomplète, avec
   l'alternative halopéridol + butylscopolamine ± octréotide.
5. **RESCOS-67 · `theorie` — « Débuter lévothyroxine à faible dose (25-50 µg/j) »
   sans réserve**, chez une femme de 38 ans. Le `resume` réserve correctement le
   départ prudent au sujet âgé ou coronarien. Corrigé : substitution complète
   d'emblée (≈ 1,6 µg/kg/j) chez l'adulte jeune sans cardiopathie.
6. **RESCOS-68 · `resume` et `theorie` — « vaccin Zostavax ou Shingrix après
   50 ans ».** `SSP — Éruption Cutanée` écrit « Shingrix > 65 ans ». Zostavax,
   vaccin vivant, n'est plus disponible en Suisse. Corrigé aux trois endroits,
   avec l'indication dès 18 ans chez l'immunodéprimé, et la finalité rectifiée
   (prévention de la névralgie post-zostérienne plutôt que des récidives).
7. **RESCOS-63 · `resume` et `presentation` — « déclaration obligatoire de la
   maladie ».** `theorie` de la même grille écrit « déclaration obligatoire
   (**cas groupés**) ». En Suisse la coqueluche n'est plus à déclaration
   individuelle ; ce sont les flambées qui se déclarent. Aligné sur `theorie`,
   la formulation la plus précise.
8. **RESCOS-56 · `resume` — antihistaminiques donnés au même rang que la
   cholestyramine** contre le prurit cholestatique, alors que `therapy` de la
   même grille écrit « antihistaminiques peu efficaces ». Corrigé, avec les
   posologies et la hiérarchie (cholestyramine 4 g 2-3×/j, rifampicine
   150-300 mg/j).

**Deux corrections mineures de même nature.** RESCOS-57b · `theorie` écrivait
« BRAT : Bananes, Riz, **Applesauce**, Toast » là où `therapy` et
`presentation` écrivent « compote » ; et RESCOS-58 · `theorie` portait
« Transfusion si Hb < **7g/dl** » — unité non SI **collée au chiffre**, que
`check_nomenclature` ne voit pas (voir « Un angle mort mesuré » ci-dessous).

**Précisions chiffrées portées depuis la page (6).** RESCOS-62 items et seuils
du CURB-65 (0-1 ambulatoire, 2 hospitalisation courte, ≥ 3 forme sévère) ·
RESCOS-61 seuils de l'HGPO 75 g (à jeun ≥ 5,1 · 1 h ≥ 10,0 · 2 h ≥ 8,5 mmol/L)
et col court < 25 mm · RESCOS-58 scores d'Oakland (≤ 8) et de Glasgow-Blatchford,
index de choc > 1, coloscopie ≤ 24 h, dépistage FIT/coloscopie 50-69 ans ·
RESCOS-64 seuil de l'hémoptysie massive (> 200 mL/24 h ou > 100 mL/h) ·
RESCOS-67 seuil d'Epworth > 10, cohérent avec RESCOS-44 du lot `l6a` ·
RESCOS-59 seuil de risque cardiovasculaire à 10 ans d'environ 10 % et
calculateur AGLA/GSLA.

### Les trous du bloc canonique — dix, dont six de sécurité

Le rôle canonique se répartit encore autrement que dans les deux lots
précédents : **six grilles ont un `resume`** (56, 57b, 62, 63, 64-SD1, 67, 68,
69b — huit en fait), **sept n'ont que `theorie`** (58, 59, 60, 61, 65, 66, 69),
**une n'a que `annexe-dd`** (57) et **une n'a rien du tout** (64-SD2).

| grille | ce qui manquait | où porté |
|---|---|---|
| RESCOS-57 | la **glycémie capillaire**, l'**hyponatrémie sous thiazidique** et le couple **globe vésical / fécalome** — zéro occurrence, chez un homme de 88 ans sous Cosaar Plus, porteur d'une HBP | `annexe-dd`, trois entrées ajoutées |
| RESCOS-57b | la **glycémie capillaire** et le **globe vésical** — zéro occurrence ; plus la forme **hypoactive** de l'état confusionnel et la règle « la démence prédispose mais n'explique pas » | `resume` |
| RESCOS-61 | l'**immunoglobuline anti-D à 28 SA** chez la femme Rh négatif — **zéro occurrence** dans une station de suivi de grossesse ; plus l'**aspirine 100-150 mg dès 12-16 SA** et les **contre-indications absolues** (IEC, sartans, AVK, méthotrexate, isotrétinoïne, statines) | `theorie`/Rappels et /Dépistage |
| RESCOS-66 | l'**hydrocéphalie à pression normale** et la triade de Hakim-Adams — **zéro occurrence**, chez une femme de 74 ans en trouble de l'équilibre, alors que c'est la seule cause curable de la liste ; plus le canal lombaire étroit et l'hypotension orthostatique | `theorie` |
| RESCOS-65 | la **TSH** et l'hyperthyroïdie — **zéro occurrence** ; plus les neuroleptiques et le métoclopramide comme causes de parkinsonisme réversible | `theorie` |
| RESCOS-64 SD1 | la **distinction hémoptysie / hématémèse / épistaxis postérieure déglutie** — zéro occurrence, alors que c'est le premier réflexe de la page ; plus le **décubitus latéral du côté qui saigne** et l'**isolement respiratoire** dès la suspicion de tuberculose | `resume` et `annexe-dd` |
| RESCOS-69 | le **nom des ressources d'aide aux victimes** : la grille NOTE « informe des offres de soutien à disposition » et ne nomme aucune structure. LAVI (0848 800 244) et 143 ajoutés | `theorie` |
| RESCOS-58 | le **rapport urée/créatinine** et la **gastroscopie première** devant une rectorragie chez un patient avec antécédent d'ulcère sous aspirine et AINS — zéro occurrence d'OGD dans la grille, alors que le barème lui-même liste l'ulcère gastroduodénal au différentiel | `theorie` |
| RESCOS-67 | le **β-hCG** chez une femme de 38 ans (zéro occurrence) et le dépistage du **SAHOS** | `theorie`/Examens |
| RESCOS-68 | la **sérologie VIH devant tout zona avant 50 ans**, et pas seulement devant les formes sévères ou récidivantes, chez un patient de 31 ans | `resume` |

Cinq compléments moindres : RESCOS-56 (TP/INR et CA 19-9 absents de
`resume`/Biologie, antibiothérapie de l'angiocholite non nommée) · RESCOS-62
(réévaluation à 48-72 h et **radiographie de contrôle à 4-6 semaines chez le
fumeur** absentes de `resume`) · RESCOS-63 (**hyperleucocytose > 30 puis
50 G/L** comme marqueur de la forme maligne, vaccination maternelle en fin de
grossesse, isolement gouttelettes) · RESCOS-59 (aucune référence suisse :
AGLA/GSLA, LPMéd art. 40, smarter medicine) · RESCOS-60 (teach-back, test SURE,
CC art. 16 / 370-373 / 377-378).

### Une grille sans aucun bloc mobile — « RESCOS-64 station double 2 »

`blocks_present()` rend **`[]`** : ni `resume`, ni `theorie`, ni
`presentation`, ni `expert`, ni `annexe-dd`, ni `scenario`. Le fichier pèse
108 808 caractères et ne contient que sa section notée. `uncovered_content()`
rend `{}` — ce n'est donc pas un angle mort de l'outillage, c'est un fait :
**la grille n'a aucun contenu pédagogique**. Rien n'y a été écrit, la consigne
« ne crée aucun bloc absent » s'appliquant intégralement. C'est la seule grille
des 33 numérotées dans ce cas.

### Les gestes de réduction, par famille

* **§2 et §3 convertis en `presentation-reponse text`** — huit grilles à
  `presentation`, 14 listes converties. Geste le plus rentable du lot.
* **§1 fusionné, forme `structured` conservée** — sans exception, sur les huit
  grilles. Deuxième gisement.
* **§3 « Traitement immédiat » fusionné** — la `reponse-section` se fusionne, elle
  ne se convertit pas (enseignement 3 du lot `l6a`, reconduit).
* **`annexe-dd` retouché sur 7 grilles** (56, 57, 57b, 62, 64-SD1, 67, 68) —
  aucune case à cocher, barème hors d'atteinte. Six fusions d'enrichissement et
  **deux entrées ajoutées** (fausses hémoptysies et sténose mitrale sur
  RESCOS-64 SD1, trois entrées sur RESCOS-57).
* **Listes de « Touches ludiques » fusionnées** — jamais supprimées ; sur
  RESCOS-56 les quatre sous-sections ont été réécrites en lignes discriminantes
  après vérification item par item de leur présence ailleurs.
* **`theorie` allongé face à `expert` et `therapy`** — sur les grilles sans
  `presentation`, l'unique côté mobile.

### Un angle mort mesuré de `check_nomenclature`

`RESCOS-58`/`theorie` écrivait **`Hb < 7g/dl`** — unité non SI, **collée au
chiffre**, et `check_nomenclature` rendait 0. Le motif du contrôle attend une
frontière de mot ou une espace avant l'unité ; `7g/dl` y échappe. Un balayage
du corpus après correction rend **0 occurrence de `g/dl`** et **11 occurrences
résiduelles** d'unités en litre minuscule (`mmol/l`, `g/l`, `UI/l`) plus deux
`40mcg`. Toutes sont hors de ce lot ou dans une **section notée**
(RESCOS-57/57b, `Pradif T 40mcg`) : consignées, non corrigées. Le correctif de
motif relève d'une passe dédiée, pas d'une retouche isolée.

### Barème — règle 1, strictement

Toutes les éditions portent sur `resume`, `theorie`, `presentation` et
`annexe-dd`. **Aucun bloc noté** : `therapy` et `redflags` n'ont pas été
approchés, `expert` non plus. 0 sous-item ajouté ou retiré ; `maxScores`,
`<span class="score">`, `sectionInfo[].count` et `coef` intacts ; **baseline non
régénérée**. Les coefficients 0.5/0.5 de RESCOS-63 réparés au lot `l3` sont
inchangés. Vérifié sur le diff complet : **0 ligne** touchant
`window.caseConfig`, `<script`, `criteria-text`, `criteria-detail`,
`type="checkbox"`, `type="radio"`, `maxScores`, `sectionInfo`, `coef` ou
`<span class="score">`.

### Vérifications

```
check_invariants.py                 OK — 165 grilles, code 0
check_nomenclature.py               OK — 0 terme, code 0
check_reachability.py               OK — 156/156 notées à 100 %, code 0
report_redundancy.py 56→69          133 -> 3
report_redundancy.py (corpus)       1147 -> 1017  (−130 = gain du lot)
check_no_loss.py b646e68            203 items, verdictés un à un, 0 perte
browser_probe.js RESCOS-5 --deep    12/12 sans exception · 12/12 à 100 % · registry
browser_probe.js RESCOS-6 --deep    12/12 sans exception · 12/12 à 100 % · registry
                                    barre nav fixed sans recouvrement du minuteur
AMBOSS  report_redundancy 147 (inchangé) · 3 portes code 0
RESCOS  report_redundancy 127 (inchangé) · 3 portes code 0
```

Les 203 items signalés par `check_no_loss` sont **tous** des conversions en
`presentation-reponse text` (que `all_items()` ne voit plus par construction),
des fusions, ou les huit corrections délibérées ci-dessus. Treize items dont la
couverture lexicale automatique tombait sous 0,6 ont été relus un à un et
retrouvés dans leur bloc d'arrivée. **Aucun retrait plein.**

La sonde `--deep` signale une grille sans crochet coloré : « RESCOS-64 station
double 2 ». Elle n'a **pas** été modifiée (aucune entrée au `git status`) et
ses critères ne portent aucune `patient-response` — état antérieur, pas une
régression.

### Ce que le lot `l6b` n'a pas fait

* **Rien sous `cases/german/`, `scripts/german/`, `cases/casecos/` ni
  `scripts/casecos/`** — ni lu, ni écrit. Commit `path`-scopé.
* **Aucun bloc créé**, y compris sur la grille qui n'en a aucun.
* **Aucune lecture de grille entière avec `Read`** — bornes par `block_spans`,
  puis `Read` avec `offset`/`limit`.
* **Aucune modification de `cases/scoring.js`** ni d'aucun fichier partagé.
* **Aucune commande réseau, aucun `git push`, aucun `git gc` ni `git prune`.**

### Un second incident de coordination, et ce qu'il enseigne

Le lot `l6b` a été **absorbé par un commit de l'utilisateur**. Le mécanisme, à
retenir : un `git add -- <mes chemins>` a été lancé quelques secondes avant la
validation, pour vérifier le `diff --cached` ; entre les deux, l'utilisateur a
lancé son propre `git commit`, qui a pris **tout l'index** — donc mes seize
grilles et ce journal, sous le message
« Crée les sections pédagogiques de 3 grilles german (53, 54, 55) » (`16a8133`).

**Aucun contenu n'est perdu** : les seize fichiers et le journal sont commités
à l'identique, `git status` est vide sur `cases/rescos-locales/`, et les trois
portes restent vertes après coup. Seule la traçabilité est atteinte : le message
de commit ne décrit pas ce lot.

L'histoire n'a **pas** été réécrite : l'utilisateur commite en parallèle, et un
`--amend` ou un rebase sous ses pieds coûterait plus cher que le défaut de
libellé.

**La leçon est plus stricte que la consigne existante.** Commiter avec un
`path` explicite protège de sweeper les fichiers d'autrui ; cela ne protège pas
de **se faire sweeper**. Tant qu'un travail concurrent est en cours, il ne faut
**jamais laisser quoi que ce soit dans l'index** : pas de `git add` préalable,
et la validation directement par `git commit -F msg -- <chemins>`, qui met en
index et valide dans le même geste.

---

## Lot `t1` — les 10 « AMC Urgences » et les 10 « Psy-Vignette »

Base `626fde7` (HEAD au moment de la mesure : `933dc45`, travail german de
l'utilisateur). Vingt fichiers modifiés, tous sous `cases/rescos-locales/`.
Rien lu ni écrit sous `cases/german/`, `scripts/german/`, `cases/casecos/` ni
`scripts/casecos/`.

**Premier lot des 132 grilles thématiques.** Il calibre les 112 suivantes, et
leur profil de blocs diffère assez des 33 numérotées pour changer la méthode.

### 1. Le profil des blocs — deux familles, deux régimes

| bloc | AMC Urgences (10) | Psy-Vignette (10) |
|---|---|---|
| `annexe-dd` | 10/10 | **10/10** |
| `therapy` | 7/10 | **10/10** (0 item extrait) |
| `cloture` | 10/10 | **10/10** |
| `theorie` | **10/10** | **0/10** |
| `expert` | 10/10 | **0/10** |
| `scenario` | 10/10 | **0/10** |
| `redflags` | 6/10 | 0/10 |
| `annexe-image` | 9/10 | 2/10 |
| `resume` · `presentation` | **0/10** | **0/10** |

* Chez les **AMC Urgences**, le rôle canonique est tenu par `theorie`, sans
  exception. Aucune des dix n'a de `resume` ni de `presentation` : la règle
  « §1 se fusionne, §2/§3 se convertissent » n'a **aucun point d'application**
  dans ce lot.
* Chez les **Psy-Vignette**, **personne ne tient le rôle** : ni `theorie`, ni
  `expert`, ni `resume`, ni `presentation`, ni même `scenario`. Les seuls blocs
  mobiles sont `annexe-dd` et `cloture` — `therapy` est un attendu de
  correction. C'est le profil le plus pauvre rencontré depuis le début du
  corpus, plus pauvre encore que RESCOS-57.

### 2. La mesure de redondance est structurellement muette sur ce lot

| | avant | après |
|---|---:|---:|
| AMC Urgences 1 — Polytraumatisé | 4 | **1** |
| AMC Urgences 4 — BPCO | 1 | **0** |
| AMC Urgences 5B — AVC | 1 | **0** |
| les 7 autres AMC Urgences | 0 | **0** |
| les 10 Psy-Vignette | **0** | **0** |
| **total du lot** | **6** | **1** |

Corpus **1017 → 1012** (−5, soit exactement le gain du lot : l'économie de
mesure se vérifie une **quatrième** fois).

Six paires pour vingt grilles, contre 133 pour dix-sept au lot `l6b`. La raison
est mécanique : la redondance inter-blocs se nourrit du couple
`presentation ↔ resume/theorie`, et **aucune des vingt grilles n'a de
`presentation`**. Les Psy-Vignette, avec trois blocs dont un sans item
extractible, ne peuvent structurellement produire aucune paire. **Un chiffre de
redondance nul n'y est pas un signe de qualité : c'est une absence de matière à
mesurer.**

La paire résiduelle d'AMC Urgences 1 est le plancher structurel :
`redflags`/« 3. Pneumothorax sous tension » face à `expert`/« Ne pas drainer un
pneumothorax sous tension ». Les deux blocs sont intouchables.

### 3. Un défaut d'import inédit — le mot `undefined` affiché

`<div class="cloture-content cloture-content-green">undefined</div>` :
la moulinette d'import a écrit la valeur JavaScript `undefined` là où le champ
« contenu » était vide, et le lecteur voit littéralement **« undefined »** sous
un titre comme « Réponse type » ou « Réponses types aux inquiétudes ». Le
contenu réel est dans le `exemples-phrases` qui suit ; le `div` est vide de
sens.

* **57 occurrences sur 48 grilles** de `cases/rescos-locales`.
* **0 dans AMBOSS, German et RESCOS** — c'est une signature propre à ce corpus,
  absente des sept familles de `report_import_defects.py`.
* **17 occurrences dans ce lot** (8 AMC Urgences, 9 Psy-Vignette), retirées.
* **40 occurrences subsistent sur 31 grilles** hors du lot.

Le retrait ne change rien au barème ni aux invariants : `undefined` fait
9 caractères, sous le seuil de 18 de `list_items()`, il n'a donc jamais été un
item ; et le `cloture-item` englobant reste, donc `blocks_present()` ne bouge
pas. **Le contrôle qui aurait dû le voir n'existe pas** : c'est un candidat
naturel pour une huitième famille de `report_import_defects.py`.

### 4. Les onze corrections d'erreur

Dix dans `theorie`, une dans `annexe-dd`. Les cinq premières sont des erreurs de
sécurité, développées au rapport `t1-report.md` § 7.

1. **AMC Urgences 1 — hypotension permissive sans la réserve du traumatisme
   crânien.** `theorie` écrivait « Permissive hypotension : PAS 80-90 mmHg avant
   contrôle chirurgical ». `SSP — Polytraumatisme` écrit « hypotension
   permissive (TAS ≈ 80-90 mmHg) … **sauf TC sévère (objectif TAS ≥ 110)** ».
   Le patient de la station est à **GCS 5, anisocorie, décérébration,
   TAS 75 mmHg** : c'est exactement l'exception.
2. **AMC Urgences 3B — coronarographie « dans les 24-72 h » chez une patiente en
   Killip III.** L'insuffisance cardiaque aiguë est un critère de **très haut
   risque** qui impose la coronarographie **immédiate**. La page le dit, et
   `expert` de la même grille écrit « Identification de l'insuffisance cardiaque
   aiguë (Killip III) ».
3. **AMC Urgences 3C — « D-dimères < 500 µg/L exclut quasi dissection ».**
   Chez une patiente à douleur déchirante, asymétrie tensionnelle, pouls fémoral
   absent et souffle d'insuffisance aortique nouveau.
4. **Psy-Vignette 4 — « pas de signes neurologiques focaux, pas de fièvre »
   rangés en arguments CONTRE une cause organique**, devant un premier épisode
   psychotique à 18 ans. C'est la présentation habituelle de l'encéphalite
   auto-immune à anticorps anti-NMDA.
5. **AMC Urgences 3A — dérivés nitrés sans la contre-indication de l'infarctus
   du ventricule droit.** La page l'écrit : « cave infarctus inférieur / droit :
   pas de nitré (précharge-dépendant) ».
6. **AMC Urgences 2A — contre-indications du fibrinolytique fausses.**
   « AVC < 3 mois » : l'AVC hémorragique est une contre-indication **à vie**, et
   l'AVC ischémique porte sur **6 mois**. Corrigé, avec la nuance décisive de
   l'EP à haut risque (les contre-indications absolues y deviennent relatives).
7. **AMC Urgences 2A — ténectéplase présenté à égalité avec l'altéplase** dans
   l'EP, alors qu'il n'y a pas d'autorisation et que PEITHO y a montré un excès
   d'hémorragies majeures.
8. **AMC Urgences 2B — « ScvO2 : objectif > 70 % ».** Cible de l'*early
   goal-directed therapy* de Rivers, abandonnée après ProCESS, ARISE et ProMISe ;
   `SSP — États de Choc` nomme le piège (« en choc septique, la ScvO₂ peut être
   normale ou haute … elle ne rassure pas »).
9. **AMC Urgences 5C — « Méningocoque : sérogroupes B, C, W, Y en France »**,
   dans un corpus suisse. Corrigé, avec le plan vaccinal OFSP/BAG.
10. **AMC Urgences 4 — « GOLD 3 → indication de trithérapie inhalée ».**
    Le grade spirométrique ne décide pas du traitement ; ce sont les groupes
    A/B/E, les exacerbations et les éosinophiles.
11. **AMC Urgences 5A — « Classification de Fisher modifiée »** dont le contenu
    est celui de l'échelle de Fisher **d'origine**. Les deux échelles sont
    données côte à côte, et le grade maximal n'est pas le même.

Une correction s'ajoute dans la **section notée** — la seule du lot, § 6.

### 5. Les trous du canonique comblés

Vingt-trois compléments, dont onze de sécurité. Les plus nets :

| grille | ce qui manquait |
|---|---|
| AMC Urgences 1 | la **glycémie capillaire** du D de l'ABCDE (0 occurrence) · le seuil de l'**hémothorax massif** (1500 mL, 200 mL/h) · la **cécité du FAST au rétropéritoine** · la pose de la **ceinture pelvienne aux grands trochanters** et l'interdiction de tester deux fois · la **sonde orogastrique** si fracture de la base · la **majoration de mortalité du TXA au-delà de 3 h** |
| AMC Urgences 2A | la **durée d'anticoagulation** (3 mois, EP provoquée par la chirurgie) — 0 occurrence, alors qu'`expert` reproche « oublier la prophylaxie anticoagulante ultérieure » · le **dépistage du CTEPH** à 3-6 mois · l'**altéplase 50 mg en bolus** si arrêt cardiaque · le détail du **sPESI** |
| AMC Urgences 2B | les **3 items du qSOFA** (0 occurrence, chez un patient qui cote 3/3) · le **contrôle du foyer dans les 6-12 h** · les **2 paires d'hémocultures** et la règle des 45 minutes |
| AMC Urgences 3A | la **stratégie de reperfusion** — angioplastie primaire si ≤ 120 min, sinon fibrinolyse dans les 10 min : 0 occurrence, alors qu'`expert` exige « stratégie de reperfusion claire » · les territoires **postérieur (V7-V9)** et **droit (V3R-V4R)** · l'**oxygène seulement si SpO2 < 90 %** · les critères de **Sgarbossa** |
| AMC Urgences 3B | les **inhibiteurs calciques non dihydropyridiniques** contre-indiqués dans l'IC à FE réduite, et l'**exception de l'amiodarone** — la grille écrivait « éviter … antiarythmiques classe I et III » · l'**inhibiteur du SGLT2** et l'**ARNI** |
| AMC Urgences 3C | le seuil de l'**asymétrie tensionnelle (> 20 mmHg)** · la **cible de fréquence < 60/min** · le **score ADD** |
| AMC Urgences 4 | l'**indication chiffrée de la VNI** (pH < 7,35 et PaCO2 > 6 kPa) — 0 occurrence, alors qu'`expert` exige d'en « contrôler l'indication » · ses **contre-indications**, dont le pneumothorax non drainé, que la station simule à 10 minutes · les **critères d'intubation** · la **thromboprophylaxie** |
| AMC Urgences 5A | le **délai de sécurisation de l'anévrysme** (< 24 h, au plus tard 72) — 0 occurrence, alors que la grille parle trois fois de l'« avant sécurisation » · la distinction **SIADH / cerebral salt wasting** et l'interdiction de restreindre l'eau · antalgie, laxatifs, arrêt des antithrombotiques |
| AMC Urgences 5B | la **glycémie capillaire comme mimic n° 1** — `hypoglycémie` à **0 occurrence**, alors que c'est la règle d'or de `SSP — Parésie - AVC` · l'**absence de place des corticoïdes** dans l'œdème ischémique · le **test de déglutition** · la **Stroke Unit** et le seuil féminin du CHA2DS2-VASc |
| AMC Urgences 5C | la **déclaration au médecin cantonal et à l'OFSP** · le **délai antibiotique** (< 1 h, idéalement 30 min, avant la PL si purpura) · la **dexaméthasone avant ou avec** la première dose · l'**isolement gouttelettes 24 h** · la **ceftriaxone 250 mg IM** chez la femme enceinte |

### 6. Les Psy-Vignette — un trou de protection sur les dix

Relevé sur les dix grilles, **avant** intervention :

| terme | occurrences |
|---|---|
| `PAFA` · `art. 426` · `art. 16 CC` · `APEA` / `KESB` | **0 sur 10 grilles** |
| `glycémie` | **0 sur 10** |
| `143` (La Main Tendue) | **1**, sur la seule Psy-Vignette 10 |
| `147` (Pro Juventute) | **0 sur 10** |
| `suicid*` | 0 sur Psy-Vignette 8 ; 1 sur les vignettes 1, 2, 3, 4 et 9 |

Une série de dix stations de psychiatrie suisse **ne nomme pas une seule fois le
placement à des fins d'assistance** — alors que la page
`SSP — Urgences Psychiatriques (Agitation, PAFA)` inscrit « Pas de mise en place
de PAFA quand critères réunis » parmi ses **pièges éliminatoires**, et que la
Psy-Vignette 9 fait littéralement dire au patient « je ne suis pas malade,
pourquoi m'hospitaliser ? » sans que la réponse type mentionne le cadre légal.

Conformément à la consigne (« enrichis, ne réduis pas »), une catégorie a été
ajoutée à l'`annexe-dd` de **chacune des dix**, et deux phrases à la `cloture`
des vignettes 5 et 9. Contenus portés : le PAFA avec ses trois conditions
cumulatives et sa distinction d'avec le traitement sans consentement
(art. 434 CC) ; la durée de 6 semaines (art. 429 CC), l'APEA/KESB et le recours
au juge dans les 10 jours (art. 439 CC) ; l'évaluation explicite du risque
suicidaire dans chaque vignette ; les causes organiques et toxiques à écarter ;
les numéros 143, 144, 147, 117 et LAVI.

**Un piège de la page elle-même a été évité.** `SSP — Urgences Psychiatriques`
énonce quatre fois « PAFA = incapacité de discernement + danger + absence
d'alternative », et **se contredit** dans sa propre carte ECOS, qui écrit
correctement « l'incapacité de discernement (art. 16 CC) n'est PAS une condition
du PAFA ». C'est la version de la carte, conforme à l'art. 426 CC, qui a été
portée dans les grilles — la hiérarchie à trois niveaux ne dit pas quoi faire
quand la page se contredit, et il a fallu trancher sur le texte légal.

### 7. La seule correction de la section notée

`AMC Urgences 5C`, sous-item noté : **« Déclaration obligatoire urgente à
l'ARS »**. L'Agence Régionale de Santé est une institution **française** ;
elle n'existe pas en Suisse. Corrigé en « Déclaration obligatoire urgente au
médecin cantonal et à l'OFSP ».

C'est une **erreur factuelle interne**, pas un jugement d'auteur ni une
divergence de conduite : la correction ne change ni ce que le candidat doit
faire, ni la structure. Vérifié : `detailCount`, `criteriaCount`, `radioCount`,
`checkboxCount`, `maxScores`, `coef`, `sectionInfo[].count` et les `<span
class="score">` sont **identiques** avant et après, sur les 20 grilles — les
douze champs du snapshot sont inchangés et la baseline n'a pas été régénérée.

Occurrence unique dans les 165 grilles. Le balayage a en revanche trouvé une
autre francité, **hors de ce lot** : `Crise convulsive - Homme de 77 ans` écrit
deux fois « suspension de conduite … **6 mois en France** », dont une fois dans
un sous-item noté. Signalé, non corrigé — la grille appartient à un lot suivant.

### 8. Vérifications

```
check_invariants.py                  OK — 165 grilles, code 0
check_nomenclature.py                OK — 0 terme, code 0
check_reachability.py                OK — 156/156 notées à 100 %, code 0
report_redundancy.py AMC Urgences    6 -> 1
report_redundancy.py Psy-Vignette    0 -> 0
report_redundancy.py (corpus)        1017 -> 1012   (−5 = gain du lot)
check_no_loss.py 626fde7             43 items, verdictés un à un, 0 perte
browser_probe.js "AMC Urgences" --deep   10/10 sans exception · 10/10 à 100 % · 10/10 registry
browser_probe.js "Psy-Vignette" --deep   10/10 sans exception · 10/10 à 100 % · 10/10 registry
                                     barre nav fixed, 0 recouvrement, crochets colorés sur 20/20
bounds_anomalies / uncovered_content [] / {} sur les 20
snapshot, champ par champ            0 divergence sur 12 champs × 20 grilles

AMBOSS  report_redundancy 147 (inchangé) · invariants / nomenclature / atteignabilité code 0
RESCOS  report_redundancy 127 (inchangé) · invariants / nomenclature / atteignabilité code 0
```

Les 43 items signalés par `check_no_loss` sont des réécritures sur place : le
contrôle de couverture lexicale n'en isole que **six** sous 0,75, et ce sont
exactement les six corrections délibérées (ScvO2, ténectéplase, D-dimères,
« en France », et les deux arguments CONTRE de la Psy-Vignette 4). Deux notions
avaient été perdues par inadvertance lors d'une réécriture — « risque élevé
d'exacerbations » (AMC 4) et le chiffre de 95 % du grade 3 de Fisher (AMC 5A) —
et ont été **restituées** avant validation.

German et casecos n'ont été ni lus ni mesurés.

### 9. Ce qui change pour les 112 grilles thématiques suivantes

1. **Identifier le porteur du rôle canonique grille par grille, et accepter
   qu'il n'y en ait pas.** `theorie` chez les AMC Urgences, personne chez les
   Psy-Vignette.
2. **Ne pas déduire du chiffre de redondance qu'il n'y a rien à faire.**
   Zéro paire sur 17 grilles du lot, et pourtant onze trous de sécurité. Sur ce
   sous-corpus, `report_redundancy` mesure surtout la présence de
   `presentation` — absente des vingt.
3. **Le rendement est ailleurs : dans le niveau 1 et dans ce qui n'est pas
   écrit.** Le prédicteur du pilote (compter les cibles chiffrées de la page)
   reste juste, mais il faut lui adjoindre un second réflexe : **relever à zéro
   occurrence** les items que la page tient pour capitaux, et surtout ceux que
   `expert` reproche d'oublier sans que la grille dise jamais quoi.
4. **`expert` est un révélateur de trous.** Quatre fois sur dix chez les AMC
   Urgences, il nomme un attendu (« stratégie de reperfusion claire »,
   « contrôler l'indication de la VNI », « oublier la prophylaxie
   anticoagulante ») dont la réponse n'existe nulle part dans la grille. Lire
   `expert` **avant** `theorie` oriente la recherche.
5. **Les vignettes de psychiatrie demandent un balayage de protection dédié**,
   qu'aucun outil ne déclenche : PAFA / art. 426 CC / APEA-KESB, risque
   suicidaire, glycémie, 143 · 144 · 147 · 117 · LAVI.
6. **Le mot `undefined` est à retirer sur les 31 grilles restantes.**

---

## Lot `t2` — 25 grilles thématiques A→D, et les 40 `undefined` restants

Branche `refonte-amboss-suisse`, base `6de0284`. **52 fichiers modifiés**, tous
sous `cases/rescos-locales/`. Rien touché sous `cases/german/`,
`scripts/german/`, `cases/casecos/` ni `scripts/casecos/` — ni lu, ni écrit.

### 1. Périmètre

Grilles thématiques (nom ne commençant pas par `RESCOS-<chiffre>`) dont le nom
commence par A à D, hors les 20 du lot `t1` (« AMC Urgences » ×10, dont les 10
commencent par A) et hors les 4 feuilles porte de la tranche (BPCO, Dépression
majeure, Dépression post-partum, Diabète pédiatrique). **32 candidates** ;
consigne appliquée : les **25 premières par ordre alphabétique** (collation
française, insensible aux accents), soit d'`Acné vulgaire` à
`Douleur thoracique - Vignette clinique`.

**Les 7 non traitées, à reprendre :** `Douleurs thoraciques - DRS` ·
`Dyspnée aigue` · `Dyspnée dans un contexte de polymorbidité` ·
`Dyspnée dans un contexte infectieux` · `Dyspnée et insuffisance cardiaque` ·
`Dyspnée et mal au cou` · `Dyspnée post-COVID`.

### 2. Le porteur du rôle canonique — quatre configurations sur 25

| porteur | grilles |
|---|---:|
| `theorie` | **24 / 25** |
| `expert` présent (détecteur, non éditable) | 19 / 25 |
| `resume` | 13 / 25 |
| `presentation` | 13 / 25 |
| **personne** (`annexe-dd` + `cloture` seuls) | **1** — `Diabète - Patient avec hyperglycémie nouvelle` |

`theorie` tient le rôle partout sauf sur `Diabète - Patient avec hyperglycémie
nouvelle`, qui n'a ni `theorie`, ni `expert`, ni `resume`, ni `presentation` :
ses seuls blocs mobiles sont `annexe-dd` et `cloture`. Tout y a été porté dans
`annexe-dd`.

### 3. Le mapping inverse — 25 / 25 desservies

Aucune grille orpheline. Le mapping ne se borne pas à `SSP ECOS/` : les trois
`BBN` relèvent de `Skills ECOS/Skills — Annonce Mauvaise Nouvelle (SPIKES)`.

| page | grilles de ce lot |
|---|---|
| `SSP — Douleur Abdominale` | Diverticulite · Douleur abdo (Vignette) · Douleur abdo (Vignettes) · Douleur abdo et diarrhée fébrile |
| `SSP — Céphalée` | Céphalées B3 · Céphalées Vignette |
| `SSP — Contraception & Conseil` | Contraception 28 ans · Contraception adolescente |
| `SSP — Dépression` | Dépression majeure · Dépression post-partum |
| `SSP — Diabète (Suivi & Complications)` | Diabète hyperglycémie · Diabète pédiatrique |
| `Skills — Annonce Mauvaise Nouvelle (SPIKES)` | BBN Cancer du sein · BBN Limitation thérapeutique · BBN Sclérose en plaques |
| `SSP — Diarrhée` | Diarrhées Vignettes |
| `SSP — Dyspnée` | BPCO exacerbation |
| `SSP — Détresse Respiratoire & Anaphylaxie` | Choc anaphylactique |
| `SSP — États de Choc` | Choc septique pulmonaire |
| `SSP — Claudication Intermittente & AOMI` | Claudication intermittente |
| `SSP — Douleur au Mollet & TVP` | Douleur non traumatique du MI |
| `SSP — Douleur Thoracique` | Douleur thoracique Vignette |
| `SSP — Malaise & Perte de Connaissance Brève` | Crise convulsive |
| `SSP — Lombalgies` | Baisse de l'état général (Guillain-Barré) |
| `SSP — Éruption Cutanée` | Acné vulgaire |

**Deux pages ne portent pas la matière de leur grille.** `SSP — Éruption
Cutanée` cite « Acné vulgaire » mais **n'a aucune section acné** (ni sévérité,
ni isotrétinoïne, ni photosensibilité des rétinoïdes) ; `SSP — Diabète` n'a
**aucune section pédiatrique**. Le niveau 2 a été appliqué sur ces deux points.

### 4. Les 40 `undefined` — tâche transverse, terminée

`<div class="cloture-content cloture-content-green">undefined</div>`, entre un
`<h4 class="cloture-title">` et un `<div class="exemples-phrases">`.

* **40 occurrences sur 31 grilles**, toutes conformes au **motif strict**
  (titre h4 → div `undefined` → `exemples-phrases`) : 40/40, 0 écart ;
* les 40 `exemples-phrases` suivants ont été vérifiés **non vides** (texte utile
  ≥ 20 caractères) : le titre voisin et les phrases-exemples portent
  l'information, la div `undefined` n'en portait aucune ;
* **40 retirées, 0 restante dans le corpus** ;
* neutralité mesurée : `undefined` fait 9 caractères, sous le seuil de 18 de
  `list_items()` (jamais un item), le `cloture-item` englobant reste
  (`blocks_present()` inchangé), et `check_invariants` reste vert sur les 165.

**19 des 31 grilles concernées sont hors du lot** et n'ont reçu que cette
correction ; elles expliquent l'écart entre 25 grilles traitées et 52 fichiers
modifiés (25 + 31 − 4 recouvrements).

### 5. Les erreurs corrigées — huit

1. **Choc septique pulmonaire — `ScvO2 > 70 %` en objectif de réanimation.**
   Récidive exacte de l'erreur d'AMC 2B (lot `t1`), sur une grille jumelle.
   `SSP — États de Choc` la nomme deux fois comme piège. § 8.1.
2. **Douleur thoracique (Vignette) — nitrés sans la contre-indication de
   l'infarctus du ventricule droit**, dans `theorie` **et** dans `therapy`.
   Récidive exacte de l'erreur d'AMC 3A. § 8.1 et § 7.
3. **Crise convulsive — « suspension de conduite : 6 mois en France »**, dans
   `theorie`, dans un `exemple-phrase` et **dans un sous-item noté**. § 7.
4. **Diverticulite sigmoïdienne — « résection sigmoïdienne élective après le
   2ᵉ épisode »**, règle abandonnée : le risque de complication ne croît pas
   avec le nombre d'épisodes. Remplacée par la décision individualisée
   (récidives invalidantes, complication, immunosuppression) et par la
   conduite `SSMI/SGAIM` selon Hinchey.
5. **Dépression post-partum — zuranolone présenté comme « approuvé »** : il ne
   l'est qu'aux États-Unis, et **n'est pas disponible en Suisse**. Le proposer
   à la patiente comme une option accessible est une promesse fausse.
6. **Claudication intermittente — cilostazol donné au même rang que les
   autres traitements** : `SSP — Claudication` écrit « peu utilisé / non
   remboursé en Suisse ».
7. **Claudication intermittente — échelle d'IPS incomplète et divergente** :
   la grille écrivait « < 0,90 » puis « 0,91-0,99 borderline » puis « > 1,40
   médiacalcose », sans **aucun seuil d'ischémie critique**. Alignée sur la
   page (≥ 1,3 · 0,9-1,3 · 0,7-0,9 · 0,4-0,7 · **< 0,4**), la nuance
   « borderline » conservée.
8. **Douleur abdominale et diarrhée fébrile — antibiothérapie empirique
   recommandée sans réserve** alors que la même grille liste le syndrome
   hémolytique et urémique à *E. coli* O157:H7 parmi les complications. § 8.1.

### 6. Les trous du canonique comblés — vingt-six, dont quatorze de sécurité

| grille | ce qui manquait |
|---|---|
| Choc anaphylactique | la **position du patient** — `expert` exige « position allongée », la grille ne disait rien : *on ne relève jamais un anaphylactique* (syndrome du ventricule vide) · **durée de surveillance** (≥ 6 h, 24 h si sévère) et réaction biphasique (≈ 20 %, 1-72 h) · **deux auto-injecteurs + démonstration** · **glucagon 1-5 mg IV sous bêtabloquant** · voie IM exclusive · l'erreur létale « traiter son asthme au salbutamol » |
| Claudication intermittente | l'**ischémie aiguë de membre** — **0 occurrence** des 6 P, de la fenêtre de 6 h, de Rutherford, alors que `expert` reproche « ne pas rechercher une ischémie critique » · seuil d'IPS < 0,4 · IPS faussement normal du diabétique · **test du vélo** (claudication neurogène) · LDL < 1,4 mmol/L · marche ≥ 30 min 3×/sem · syndrome de Leriche |
| Douleur non traumatique du MI | le **score de Wells** et les **D-dimères** — **0 occurrence**, alors que la page en fait son piège éliminatoire n° 1 · seuil ajusté à l'âge (âge × 10 µg/L) · Δ ≥ 3 cm à 10 cm sous la TTA · Homans non concluant · syndrome des loges · « ne pas faire marcher un suspect d'EP » |
| BPCO exacerbation | la **cible SpO2 88-92 %** — **0 occurrence** dans une station de sortie d'hospitalisation de BPCO · et sa réserve inverse (« l'hypoxie tue en minutes ») · **VNI si pH < 7,35** · corticoïdes systémiques et critères d'Anthonisen · **contenu du plan d'action écrit** que `expert` exige de fournir, dont « quand appeler le 144 » |
| Dépression majeure | **PAFA, art. 426 CC, art. 16 CC, 143, 144, 147 : 0 occurrence** · aucune méthode d'évaluation du risque suicidaire alors que `expert` la dit « obligatoire » · **arme de service à domicile** · dépistage bipolaire avant antidépresseur (virage 15-20 %) que `expert` nomme et que rien ne documentait · fenêtre J7-J15 de levée d'inhibition · benzodiazépine seule |
| Dépression post-partum | idem, plus l'**évaluation du risque infanticide** que `expert` exige nommément · distinction pensées intrusives égodystones / idéations infanticidaires · **APEA (KESB)** au lieu d'un « service de protection de l'enfance » générique · unité mère-bébé |
| Céphalées (les deux) | **Horton : prednisone 1 mg/kg/j immédiatement, sans attendre la biopsie** — la B3 ne nommait pas Horton du tout, la Vignette écrivait « Corticoïdes: artérite temporale » sans urgence ni dose, devant une cécité irréversible · CT normal à H24 n'exclut pas l'HSA · règle d'Ottawa · SNOOP4 · thrombose veineuse cérébrale · triptans et dissection |
| Contraception (28 ans) | l'**antagonisme ulipristal / progestatif pendant 5 jours** · **inducteurs enzymatiques** dont le millepertuis · **mesurer la TA** avant un œstroprogestatif · signes **ACHES** · catégories OMS 1-4 · thrombophilie, IMC > 35, allaitement < 6 sem |
| Contraception adolescente | la **contraception d'urgence — 0 occurrence** alors que `expert` en fait un piège · **art. 16 CC** comme fondement de la confidentialité (et non un âge) · **147 Pro Juventute**, Santé Sexuelle Suisse, gratuité cantonale avant 25 ans · APEA si danger |
| Crise convulsive | la **distinction syncope / crise** — 0 occurrence, alors que c'est le piège n° 1 de la page chez un homme de 77 ans : myoclonies < 15 s, morsure du bord latéral, ECG systématique, TA couché-debout, glycémie capillaire ; deux entrées ajoutées à l'`annexe-dd` (syncope cardiaque, hypoglycémie) |
| Diabète pédiatrique | le **traitement de l'hypoglycémie** — `expert` exige d'« enseigner la gestion », la grille ne donnait qu'un seuil : règle des 15, **glucagon 1 mg IM** à domicile · **règles des jours de maladie : l'insuline ne s'arrête jamais** · critères chiffrés de l'acidocétose · encadrement scolaire **suisse** (`expert` nomme le « PAI », dispositif français) |
| Diabète (hyperglycémie nouvelle) | **tout le canonique** : critères diagnostiques (≥ 7,0 mmol/L, HbA1c ≥ 6,5 %), cibles individualisées, les trois urgences glycémiques dont l'**acidocétose euglycémique sous SGLT2**, les trois réserves de la metformine (DFG < 30, réduction 30-45, suspension avant contraste), le calendrier de dépistage et le monofilament 10 g |
| Diarrhées (Vignettes) | le **traitement du *C. difficile*** (vancomycine PO 125 mg ×4/j 10 j ; le métronidazole n'est plus le 1ᵉʳ choix) et l'**inefficacité de la solution hydro-alcoolique sur les spores** · le **SHU** — 0 occurrence, alors que la grille jumelle le porte · calprotectine chiffrée · Ringer-lactate 20 mL/kg · 144 · 145 |
| Douleur abdo (Vignettes) | l'**anévrisme de l'aorte abdominale — 0 occurrence** dans une table d'orientation à neuf quadrants, alors que c'est le red flag n° 1 de la page, et la règle « après 60 ans, une première colique néphrétique est un AAA jusqu'à preuve du contraire » · ischémie mésentérique (douleur ≫ examen) · ordre I-A-P-P · Alvarado, Atlanta, Hinchey · metformine avant CT injecté |
| Diverticulite · Douleur abdo (Vignette) | la **contre-indication de la coloscopie en phase aiguë**, que `expert` nomme comme piège sans que `theorie` la dise · réévaluation à 48-72 h si abstention antibiotique · abcès > 2 cm et cavité close |
| Guillain-Barré | la **règle 20/30/40**, le *single breath count*, et surtout : **ne jamais attendre la désaturation ni l'hypercapnie pour intuber** — la grille faisait dépendre la gazométrie d'une dyspnée |
| BBN (les trois) | l'**évaluation suicidaire après annonce** — erreur éliminatoire de la page, **0 occurrence** sur les trois · **143**, **Ligue suisse contre le cancer 0800 11 88 11**, palliative.ch, Société suisse SEP · **INTERPRET, jamais un proche** · **LPMéd art. 40** et le **droit de ne pas savoir** · art. 370 ss CC et APEA · suivi < 24-48 h · ne jamais annoncer par téléphone · tracer au dossier |
| Acné | le **programme de prévention de la grossesse** sous isotrétinoïne chez une fille de 16 ans (contraception 1 mois avant / pendant / 1 mois après, test mensuel) — la grille ne prévoyait qu'un test de grossesse initial · **photosensibilité des rétinoïdes et de la doxycycline**, que `expert` reproche d'oublier · isotrétinoïne + cyclines contre-indiquées · dermatite périorale |
| Douleur thoracique (Vignette) | **ECG < 10 min**, **TA aux deux bras**, **PCI < 120 min / fibrinolyse < 10 min**, algorithme hs-cTnT 0/1 h chiffré, **coronarographie immédiate du très haut risque** (le « 24-72 h selon risque » restait seul), et l'interdit « ne jamais anticoaguler avant d'avoir exclu la dissection » |
| Choc septique | qSOFA chiffré (FR ≥ 22, TAS ≤ 100, GCS < 15), 2 paires d'hémocultures et la règle des 45 min, +7-8 % de mortalité par heure de retard, **contrôle du foyer**, noradrénaline en périphérie, piège du choc chaud et du bêtabloquant |

### 7. Barème — deux lignes touchées, l'exception assumée

Toutes les autres éditions portent sur `theorie` et `annexe-dd` : `redflags`,
`expert`, `resume`, `presentation` et `scenario` n'ont pas été approchés.

**Deux lignes de la section notée ont été modifiées, dans deux grilles :**

1. **`Crise convulsive`, sous-item noté `m6-detail-0`** :
   « Suspension de conduite **[6 mois en France]** » →
   « Suspension de conduite **[selon l'OAC art. 7 et les directives suisses]** ».
   Plus l'`exemple-phrase` voisin, qui commençait par « En France, ».
   La règle française n'existe pas en Suisse : l'aptitude relève de l'**OAC
   art. 7**, le vault écrit « règles SVM/OFROU, 1 an sans crise » pour une
   épilepsie avérée, et le signalement au **médecin cantonal** est prévu si le
   patient refuse de cesser de conduire. C'est une **erreur factuelle interne**
   de même nature exactement que l'« ARS » d'AMC 5C au lot `t1` : elle ne change
   ni ce que le candidat doit faire, ni la structure. Le chiffre suisse pour une
   **première** crise n'étant donné nulle part dans le vault, **il n'a pas été
   inventé** : le sous-item renvoie au texte réglementaire, et `theorie` porte
   le « ≥ 1 an sans crise » sourcé, explicitement rattaché à l'épilepsie avérée.
2. **`Douleur thoracique - Vignette clinique`, puce `therapy`** :
   « Nitroglycérine sublinguale 0.4mg (si TA > 90 mmHg systolique) » → même
   texte **+ « cave infarctus inférieur / du ventricule droit : pas de nitré
   (précharge-dépendant), enregistrer V3R-V4R devant tout sus-décalage
   inférieur »**. Correction d'une **erreur de sécurité sourcée** dans un bloc
   noté, au titre de l'arbitrage du lot `t2`. § 8.1.

**Preuve d'innocuité.** `check_invariants` est **vert sur les 165 grilles** : les
quatorze champs du snapshot (`maxScores`, `coef`, `scoreSpans`, `sectionCounts`,
`sectionPrefixes`, `engineFingerprint`, `configForm`, `blocks`,
`boundsAnomalies`, `uncoveredContent`, `criteriaCount`, `detailCount`,
`radioCount`, `checkboxCount`) sont identiques à la baseline. **Baseline non
régénérée.** Sur les 52 fichiers, le diff complet ne compte que **2 lignes**
portant `criteria-detail` — les deux faces de la correction n° 1 — et
**aucune** touchant `window.caseConfig`, `<script`, `criteria-text`,
`type="checkbox"`, `type="radio"`, `maxScores`, `sectionInfo`, `coef` ou
`<span class="score">`. **0 sous-item ajouté ou retiré.**

### 8. Préoccupations

#### 8.1 Quatre erreurs de sécurité, corrigées — dont deux dans un bloc noté

**1. Choc anaphylactique — la position du patient, absente.** `expert` inscrit
« Position allongée et oxygénothérapie » parmi ses points clés ; `theorie` ne
disait **rien** de la position. `SSP — Détresse Respiratoire & Anaphylaxie`
écrit : « faire asseoir ou lever le patient — pour le transférer, pour aller
aux toilettes — **des décès sont documentés à ce moment précis. On ne relève
jamais un anaphylactique** », et qualifie la position assise de **piège
éliminatoire** ; le mécanisme est le **syndrome du ventricule vide**. Une
station d'anaphylaxie dont la fiche de révision ne dit pas de coucher la
patiente jambes surélevées enseigne le geste par lequel on la tue. Corrigé, avec
les exceptions (demi-assis si détresse respiratoire, décubitus latéral gauche
si grossesse), la **surveillance ≥ 6-24 h** et le **glucagon sous
bêtabloquant** — trois autres attendus d'`expert` sans réponse dans la grille.

**2. Douleur thoracique (Vignette) — les nitrés sans la réserve du ventricule
droit, dans `theorie` ET dans `therapy`.** `SSP — Douleur Thoracique` écrit
« **cave infarctus inférieur / droit : pas de nitré** (précharge-dépendant) ».
La grille écrivait, en `theorie` « MONA … Nitrés » et, dans un bloc noté,
« Nitroglycérine sublinguale 0.4mg (si TA > 90 mmHg systolique) » — la seule
réserve étant la tension. Le ventricule droit infarci est précharge-dépendant :
le nitré y provoque un collapsus, et la tension **avant** l'administration est
normale, donc le garde-fou de la grille ne se déclenche pas. C'est l'erreur
exacte trouvée sur AMC 3A au lot `t1`, à ceci près qu'elle est ici **dans la
section notée**. Conditions de l'arbitrage réunies : erreur **sourcée** par la
page, et correction **sans ajout ni retrait de sous-item** (le texte de la puce
existante est complété). Corrigé aux deux endroits.

**3. Choc septique — `ScvO2 > 70 %` en objectif de réanimation.** Cible de
l'*early goal-directed therapy*, abandonnée après ProCESS/ARISE/ProMISe.
`SSP — États de Choc` va plus loin et nomme le **piège inverse** : « en choc
septique, la ScvO₂ peut être **normale ou haute** (défaut d'extraction
mitochondriale) — **elle ne rassure pas** ». Un candidat qui poursuit cet
objectif transfuse et perfuse de la dobutamine sans bénéfice ; pire, il peut
lire une ScvO₂ normale comme une preuve de réanimation réussie chez un patient
en défaillance. Corrigé, et l'occasion prise de porter la clairance du lactate
comme critère réel. **C'est la deuxième récidive de cette erreur** (AMC 2B au
lot `t1`, et AMC 5C la porte encore dans `therapy`, consignée alors).

**4. Douleur abdominale et diarrhée fébrile — antibiothérapie empirique sans
réserve devant une diarrhée sanglante.** `theorie` recommandait « Antibiotiques
empiriques: ciprofloxacine 500mg 2x/j ou azithromycine 1g dose unique » et
listait, quatre lignes plus haut, « **Syndrome hémolytique et urémique (*E.
coli* O157:H7)** » parmi les complications. **La grille se contredit
elle-même** : l'antibiothérapie et les ralentisseurs du transit sont associés à
un risque accru de SHU dans les infections à STEC. Corrigé en bornant
l'antibiothérapie empirique aux formes sévères ou dysentériques documentées et
au terrain à risque, avec la réserve STEC nommée.

#### 8.2 Le trou de protection des grilles thématiques — le motif des Psy-Vignette se répète

Relevé **avant** intervention sur les 25 :

| terme | occurrences |
|---|---|
| `PAFA` · `art. 426` · `art. 16 CC` · `APEA`/`KESB` | **0 sur 25** |
| `143` · `144` · `147` (hors coïncidences numériques) | **0 sur 25** |
| `LAVI` · `INTERPRET` · `LPMéd` | **0 sur 25** |

Les seules occurrences de « 143 » et « 144 » trouvées au balayage étaient une
**CRP à 143 mg/L** et un **score global sur 143** — des coïncidences
numériques. Cinq grilles de ce lot relèvent pourtant directement d'un thème de
protection : `Dépression majeure`, `Dépression post-partum`,
`Contraception adolescente` (mineure), et les trois `BBN` (risque suicidaire
post-annonce, que la page classe **erreur éliminatoire**). Conformément à la
consigne (« enrichis, ne réduis pas »), **rien n'a été retiré** : une ou deux
sections ont été **ajoutées** au `theorie` de chacune.

Point de méthode : `SSP — Contraception & Conseil` fonde la confidentialité de
la mineure sur l'**art. 16 CC** (« pas de seuil d'âge fixe »), pas sur l'art.
19c CC — que la page ne cite jamais, et qui n'apparaît dans le vault que sur la
page SPIKES, à propos du droit à l'information. **C'est l'art. 16 CC qui a été
porté**, conformément à la source, plutôt que l'article qu'on aurait attendu.

#### 8.3 Deux divergences laissées dans un bloc noté, consignées

1. **`Diverticulite sigmoidienne` — un sous-item noté demande la coloscopie
   « à 6-8 semaines »** sans dire qu'elle est contre-indiquée en phase aiguë,
   alors que `expert` de la même grille en fait un piège et instruit
   l'examinateur de « rappeler la contre-indication » si l'étudiant la propose.
   Ce n'est pas une erreur — l'item est juste — mais un **manque** ; il a été
   comblé dans `theorie`, non dans le barème.
2. **`Douleur thoracique - Vignette` — « Coronarographie dans les 24-72h selon
   risque » dans `therapy`**, sans que le très haut risque (insuffisance
   cardiaque aiguë, instabilité, ST dynamique) soit excepté. Le motif d'AMC 3B.
   La formule « selon risque » n'est pas fausse, seulement muette : la
   stratification complète a été portée dans `theorie`, le sous-item noté n'a
   pas été touché.

#### 8.4 Une contradiction interne à une page du vault, signalée

`SSP — Dépression` écrit, dans son bloc `redflag` : « URGENCE: hospitalisation
immédiate (**SDT/SDRE/SPI selon contexte**) » — la nomenclature de la loi
**française** sur les soins psychiatriques sans consentement, dans une page qui,
partout ailleurs, décrit correctement le **PAFA (art. 426 CC)**. Le vault est
hors du dépôt et n'a pas été modifié ; c'est le PAFA qui a été porté dans les
deux grilles. Le signalement vaut pour l'utilisateur.

#### 8.5 Deux mesures signalées, non corrigées

* `Dépression majeure` écrit « **Suicide : 15 % des patients dépressifs
  sévères** ». C'est l'estimation historique de Guze & Robins (1970), issue de
  cohortes hospitalières ; les estimations actuelles sont d'un ordre de
  grandeur inférieur. Le chiffre **surestime** le risque : il ne met personne en
  danger, et il n'est contredit par aucune source du vault. Consigné.
* `Douleur abdominale - Vignettes` écrit « **GB >16000** » dans le score de
  Ranson : numération en **unité implicite**, l'un des 8 cas relevés au lot
  `l4`. `check_nomenclature` ne la voit pas. Consigné.

#### 8.6 Un anglicisme introduit puis rattrapé

La première rédaction de `Douleur thoracique - Vignette` écrivait « centre
**PCI** » ; `check_nomenclature` l'a rejeté (« attendu : angioplastie
coronarienne »). Corrigé avant validation. La porte a fonctionné exactement
comme prévu — et c'est la première fois qu'elle attrape une régression
introduite par le traitement lui-même.

### 9. Vérifications

```
check_invariants.py                     OK — 165 grilles, code 0
check_nomenclature.py                   OK — 0 terme, code 0
check_reachability.py                   OK — 156/156 notées à 100 %, code 0
report_redundancy.py (lot de 25)        253 -> 252
   (6 grilles bougent : BPCO 6->8, Crise convulsive 14->15,
    Cephalees B3 4->3, Choc septique 36->35, Claudication 32->31,
    Douleur abdo Vignette 2->1 ; les 3 paires ajoutees opposent un
    ajout de `theorie` a une `presentation`/`resume` qui portait deja
    la notion sous une autre formulation — mecanisme de la passe `l4`)
report_redundancy.py (corpus)           1012 -> 1011   (−1 = gain du lot)
check_no_loss.py 6de0284                33 items, verdictés un à un, 0 perte
browser_probe.js (les 25) --deep        25/25 sans exception · 25/25 à 100 %
                                        25/25 registry · barre nav fixed
                                        0 recouvrement · crochets colorés 25/25
bounds_anomalies / uncovered_content    [] / {} sur les 25
undefined (corpus)                      40 -> 0

AMBOSS  report_redundancy 147 (inchangé) · invariants / nomenclature / atteignabilité code 0
RESCOS  report_redundancy 127 (inchangé) · invariants / nomenclature / atteignabilité code 0
```

Les 33 items signalés par `check_no_loss` sont des réécritures sur place. Le
contrôle de couverture lexicale n'en isole que **quatre** sous 0,75, et ce sont
exactement quatre corrections délibérées : `ScvO2 > 70 %`, « coût selon
pays/système », « normalisation des lactates » et « 6 mois en France ». Deux
notions menacées par une réécriture ont été **restituées** avant validation :
la bande **« IPS 0,91-0,99 borderline »** de `Claudication` et le mot
**« normalisation »** des lactates de `Choc septique`. **Aucun retrait plein.**

L'économie de mesure est confirmée une **cinquième** fois : corpus −1, soit
exactement la somme des gains par grille. Les 40 retraits d'`undefined` ne
déplacent pas le compteur — 9 caractères, sous le seuil de 18 de `list_items()`.

German et casecos n'ont été ni lus ni mesurés : l'utilisateur y travaille en
parallèle.

### 10. Ce qui change pour les 87 grilles thématiques restantes

1. **Le compteur de redondance est encore plus muet qu'annoncé.** 253 → 252 sur
   25 grilles, quand `l6b` faisait 133 → 3 sur 17. Et pourtant : **quatre
   erreurs de sécurité et vingt-six trous du canonique.** Cinq grilles de ce lot
   étaient à 0 ou 1 paire — dont `Douleur thoracique - Vignette`, qui portait
   l'erreur des nitrés dans un bloc noté.
2. **`expert` a tenu sa promesse, et au-delà.** Sur les 19 grilles qui en ont
   un, il a désigné **onze** attendus dont la réponse n'existait nulle part :
   position de l'anaphylactique, plan d'action BPCO, gestion de l'hypoglycémie
   pédiatrique, contraception d'urgence de l'adolescente, ischémie critique,
   coloscopie contre-indiquée, risque infanticide, dépistage bipolaire,
   photosensibilité des rétinoïdes, évaluation du risque suicidaire,
   surveillance de la réaction biphasique. **Six grilles sur 25 n'ont pas
   d'`expert`** ; ce sont celles où il faut lire la page en premier.
3. **La page peut être muette là où sa grille en a le plus besoin.**
   `SSP — Éruption Cutanée` n'a pas de section acné, `SSP — Diabète` pas de
   section pédiatrique, `SSP — Malaise` pas de durée de suspension de conduite.
   Vérifier que la page porte la matière, pas seulement le lien.
4. **Chercher les récidives, systématiquement.** Deux des huit erreurs de ce lot
   sont des répétitions exactes d'erreurs du lot `t1` sur des grilles jumelles
   (ScvO2, nitrés et VD). Le motif est désormais attesté trois fois.
5. **Le corpus est propre de tout `undefined`.** Le défaut est clos ; il reste à
   coder comme huitième famille de `report_import_defects.py`, avec les
   francités (`ARS`, « en France », « PAI », `SDT/SDRE/SPI`) que
   `check_nomenclature` ne couvre pas.

---

## Lot `t3` — 25 grilles thématiques, de « Douleurs thoraciques DRS » à « Intoxication opioïdes »

Branche `refonte-amboss-suisse`, base `74e51e7`. **25 fichiers modifiés**, tous
sous `cases/rescos-locales/`. Rien touché sous `cases/german/`,
`scripts/german/`, `cases/casecos/` ni `scripts/casecos/` — ni lu, ni écrit.

**Redondance du lot : 232 → 226.** Corpus **1011 → 1005** (−6, exactement le
gain du lot — sixième confirmation de l'économie de mesure). Les trois portes
sont vertes ; AMBOSS reste à **147**, RESCOS à **127**.

### 1. Le lot

123 grilles thématiques (nom ne commençant pas par `RESCOS-<chiffre>`, hors les
9 feuilles porte). 45 déjà traitées par `t1` et `t2` ; les **25 suivantes par
ordre alphabétique** (collation française, insensible aux accents) forment ce
lot, du rang 36 au rang 60.

| # | grille | redondance avant → après |
|---:|---|---:|
| 36 | Douleurs thoraciques - DRS | 3 → 3 |
| 37 | Dyspnée aigue | 1 → 1 |
| 38 | Dyspnée dans un contexte de polymorbidité | 3 → 3 |
| 39 | Dyspnée dans un contexte infectieux | 1 → 1 |
| 40 | Dyspnée et insuffisance cardiaque | 2 → **1** |
| 41 | Dyspnée et mal au cou | 6 → 6 |
| 42 | Dyspnée post-COVID | 1 → 1 |
| 43 | Enfant qui boîte — synovite transitoire | 22 → **21** |
| 44 | Entretien motivationnel - Activité physique | 1 → 1 |
| 45 | Entretien motivationnel - Compliance thérapeutique | 2 → 2 |
| 46 | Entretien motivationnel - Consommation d'alcool | 0 → 0 |
| 47 | Entretien motivationnel - Sevrage tabagique | 0 → 0 |
| 48 | Entretien motivationnel - Tabac | 1 → 1 |
| 49 | Épilepsie absence - Fille de 7 ans | 35 → 35 |
| 50 | Épisode dépressif majeur - Femme de 35 ans | 0 → 0 |
| 51 | Épisode maniaque - Homme de 28 ans | 1 → 1 |
| 52 | Érythème cutané avec douleur - Homme de 56 ans | 10 → 10 |
| 53 | Fatigue - Vignettes cliniques | 13 → 13 |
| 54 | Fatigue et maladies chroniques | 0 → 0 |
| 55 | Fatigue TBL | 2 → **1** |
| 56 | Fièvre et douleurs articulaires — gonococcie disséminée | 3 → 3 |
| 57 | Goutte - Accès aigu | 20 → **17** |
| 58 | Grille ECOS USIT2 - Diarrhée Hématochézie | 61 → 61 |
| 59 | Grille ECOS USIT2 - Hernie discale - Canal étroit | 43 → 43 |
| 60 | Intoxication — ACR sur intoxication aux opioïdes | 1 → 1 |
| | **total** | **232 → 226** |

**Les 53 non traitées** : de `Lésion de la coiffe des rotateurs` à
`Voyage au Brésil`, moins les 10 `Psy-Vignette` déjà faites au lot `t1`.

### 2. Le mapping inverse — 25 sur 25, dont 5 hors `SSP ECOS/`

Chaque grille du lot est citée nommément par une page, et une seule fois par
son bloc « Références PDF ». Treize pages couvrent les 25 :

| page | grilles |
|---|---|
| `SSP — Dyspnée` | 37, 38, 39, 40, 41, 42 |
| `Skills — Entretien Motivationnel` | 44, 45, 46, 47, 48 |
| `SSP — Fatigue` | 53, 54, 55 |
| `SSP — Douleurs Articulaires` | 56, 57 |
| `SSP — Douleur Thoracique` | 36 |
| `SSP — Boiterie de l'Enfant` | 43 |
| `SSP — Malaise & Perte de Connaissance Brève` | 49 |
| `SSP — Dépression` | 50 |
| `SSP — Troubles de l'Humeur` | 51 |
| `SSP — Éruption Cutanée` | 52 |
| `SSP — Rectorragies & Hémorragie Digestive Basse` | 58 |
| `SSP — Lombalgies` | 59 |
| `SSP — Intoxications Aiguës` | 60 |

**Les cinq grilles d'entretien motivationnel relèvent de `Skills ECOS/`, pas de
`SSP ECOS/`.** Borner la recherche à `SSP ECOS/` les aurait laissées sans
source, et c'est la page `Skills` qui porte la totalité des chiffres suisses
(verre standard, seuils OFSP, AUDIT-C, CIWA-Ar, contre-indications du bupropion,
numéros d'aide) dont les cinq grilles étaient dépourvues.

### 3. `expert` — le meilleur détecteur, encore

**16 grilles sur 25 ont un `expert`.** Il a désigné **sept** attendus dont la
réponse n'existait nulle part dans la grille :

| `expert` exige… | la grille disait… |
|---|---|
| « Oublier l'évaluation cardiaque (myocardite post-COVID) » | la myocardite en différentiel et en examen, **rien** sur l'arrêt du sport 3-6 mois |
| « Hospitalisation sous contrainte souvent nécessaire » | « hospitalisation sous contrainte », **0 occurrence** de PAFA, art. 426, APEA/KESB |
| « Ne pas sécuriser financièrement le patient » (manie) | **0 occurrence** de curatelle, d'art. 390, d'autorité de protection |
| « Penser à la fasciite nécrosante si progression rapide » | le mot « fasciite nécrosante » en étiquette d'item, **0 signe**, **0 mention de chirurgie** |
| « Oublier de vérifier la fonction rénale avant AINS » / « Débuter l'allopurinol pendant la crise » | la moitié de la règle : rien sur **ne pas l'arrêter** s'il est déjà pris, rien sur HLA-B*58:01, rien sur les interactions de la colchicine |
| « Ne pas maintenir une surveillance suffisante après naloxone » | « surveillance : durée minimale 60-90 minutes », chez une patiente sous **méthadone** |
| « Évaluer systématiquement le risque suicidaire » (dépression) | une ligne d'intention, **aucune méthode** — ni RUD, ni C-SSRS, ni MDQ, ni moyens létaux |

**Neuf grilles sur 25 n'ont pas d'`expert`** : les six `Dyspnée` et les trois
`Fatigue`. Ce sont exactement celles dont la redondance est la plus basse
(1 à 13) — et six d'entre elles portaient une erreur ou un trou. Le lot
confirme pour la troisième fois : **un chiffre bas ne dit rien.**

### 4. Sept erreurs de sécurité — dont deux dans un bloc noté

**1. `Douleurs thoraciques - DRS` — les nitrés sans la réserve du ventricule
droit, dans `theorie` ET dans `therapy`.** L'attendu noté écrivait « Dérivés
nitrés **si TA normale** » — le garde-fou tensionnel pour seul frein, alors que
la tension est précisément normale *avant* l'administration chez l'infarctus du
ventricule droit. `SSP — Douleur Thoracique` : « **cave infarctus inférieur /
droit : pas de nitré** (précharge-dépendant) » et « le territoire inférieur
impose deux réflexes : V3R-V4R … et la prudence avec les dérivés nitrés ». La
grille nomme elle-même le territoire inférieur dans son item d'ECG et n'a
**aucune occurrence** de « ventricule droit », « V3R » ni « V4R ». **Troisième
occurrence de cette erreur** après AMC 3A (`t1`) et
`Douleur thoracique - Vignette` (`t2`), et deuxième fois dans un bloc noté.
Conditions de l'arbitrage réunies : sourcée, corrigée **par complément du texte
de la puce existante**, sans ajout ni retrait de sous-item. Corrigé aux deux
endroits, plus les dérivations V3R-V4R et V7-V9 portées dans `theorie`.

**2. `Intoxication — ACR sur opioïdes` — 60-90 minutes de surveillance chez une
patiente sous méthadone, dans `therapy`.** L'attendu noté fixait « Surveillance
post-naloxone — durée minimale : 60-90 minutes », c'est-à-dire la durée d'action
de la **naloxone**, chez une patiente en substitution par **méthadone 60 mg/j**
(demi-vie 15-60 h). `SSP — Intoxications Aiguës` : « ⚠️ méthadone / opioïdes
longue durée → **surveillance prolongée ≥ 12-24 h, perfusion possible** », et son
piège n° 3 est nommément « Méthadone / opioïdes longue durée → surveillance
prolongée après naloxone (récidive) ». **La grille se contredit elle-même** :
son `expert` écrit « la durée d'action de la naloxone (30-90 min) est plus
courte que celle de la méthadone » et « ne pas maintenir une surveillance
suffisante après naloxone » — puis son attendu noté prescrit 90 minutes. **Une
sortie à 90 minutes après une intoxication à la méthadone est une re-narcose
mortelle hors de l'hôpital.** Corrigé dans les deux blocs, sans ajout ni retrait
de sous-item.

**3. `Dyspnée et insuffisance cardiaque` — diltiazem proposé pour ralentir une FA
« si IC ».** `theorie` écrivait « FA rapide : Diltiazem, bêtabloqueurs, digoxine
si IC ». Les inhibiteurs calciques non dihydropyridiniques sont **contre-indiqués
dans l'insuffisance cardiaque à FE réduite** (inotropes négatifs → décompensation)
— dans une grille dont le titre même est l'insuffisance cardiaque. C'est
exactement l'erreur relevée sur AMC 3B au lot `t1` (« vérapamil / diltiazem
contre-indiqués dans l'IC à FE réduite »), **deuxième occurrence**. Corrigé par
la conduite dépendant de la FEVG.

**4. `Goutte - Accès aigu` — l'absence de fièvre rangée CONTRE l'arthrite
septique.** `annexe-dd` opposait à l'arthrite septique « **Arguments CONTRE :
pas de porte d'entrée · pas de fièvre élevée · contexte évocateur de goutte** »,
et concluait « ponction articulaire **si doute** ».
`SSP — Douleurs Articulaires` en fait un *piège éliminatoire* — « traiter une
monoarthrite fébrile comme une crise de goutte sans ponction » — et écrit
« toute mono-arthrite aiguë est septique jusqu'à preuve du contraire », « goutte
et chondrocalcinose miment parfaitement l'infection — et les deux peuvent
coexister : **la présence de cristaux n'exclut PAS le sepsis** », « ponction
articulaire **AVANT toute** antibiothérapie ou infiltration ». C'est le motif de
la Psy-Vignette 4 du lot `t1` (l'absence d'un signe rangée contre le diagnostic
grave), **deuxième occurrence**. Les trois arguments ont été retournés en
« éléments souvent invoqués à tort comme rassurants », chacun avec sa réfutation.

**5. `Enfant qui boîte` — la grille jumelle portait le même défaut, aggravé d'une
biologie lue à l'envers.** Le contrôle des sœurs, déclenché par la découverte
précédente, a trouvé dans `annexe-dd` : « Arthrite septique — **Arguments
CONTRE : pas de fièvre actuelle · CRP normale (20 mg/l) · pas de signes
inflammatoires locaux** ». **Une CRP à 20 mg/l n'est pas normale** (norme
< 5-10 mg/l) : elle est modérément élevée, donc *compatible* avec une infection
débutante — la biologie est enseignée à l'envers, et sert d'argument rassurant.
S'y ajoute que la hanche est profonde, donc dépourvue de rougeur et de chaleur
même infectée. `SSP — Boiterie de l'Enfant` : « Kocher est une aide
probabiliste, pas un test — **un score bas n'exclut pas** ; en cas de doute la
ponction articulaire, AVANT antibiotiques, reste le seul diagnostic de
certitude ». Corrigé, avec les critères de Kocher rappelés en conclusion.

**6. `Érythème cutané avec douleur` — la fasciite nécrosante nommée sans un seul
signe ni la chirurgie.** La grille cite « Fasciite nécrosante » comme intitulé
d'un critère d'hospitalisation, et son `expert` en fait un piège — mais elle a
**0 occurrence** de « crépitation », « douleur disproportionnée », « nécro-
» hors ce titre, « chirurgical », « porte d'entrée ». `SSP — Éruption Cutanée` :
« **Érythème + crépitation + douleur disproportionnée** → fasciite nécrosante »
et « **débridement chirurgical urgent** + antibiothérapie IV ».
**Une station de dermohypodermite du diabétique qui nomme la fasciite sans dire
qu'aucun antibiotique ne la traite seul enseigne l'attente.** Section ajoutée,
avec la porte d'entrée (intertrigo / tinea pedis) dont l'omission fait la
récidive.

**7. `Entretien motivationnel - Sevrage tabagique` et `- Tabac` — le bupropion
proposé sans sa contre-indication épileptique.** `theorie` écrivait « Bupropion :
si contre-indication ou échec substituts », sans réserve.
`Skills — Entretien Motivationnel` : « **Bupropion LP (Zyban®) 150 → 300 mg/j ;
CI épilepsie, anorexie/boulimie, sevrage alcool, prise de IMAO** ». Le bupropion
abaisse le seuil épileptogène ; le prescrire sans nommer l'épilepsie est le type
d'omission que ce corpus répète. Corrigé sur les deux grilles jumelles, avec la
contre-indication psychiatrique de la varénicline.

### 5. Les huit autres corrections d'erreur

Toutes dans `theorie`, aucun bloc noté.

1. **`Douleurs thoraciques - DRS`** : « Nouveau BBG = équivalent STEMI ».
   `SSP — Douleur Thoracique` : « l'ancienne règle "BBG nouveau = STEMI" **n'est
   plus retenue** » — ce sont les critères de Sgarbossa modifiés qui tranchent.
   Portés, avec la réserve inverse (ne pas déclarer l'ECG « ininterprétable »).
2. **`Douleurs thoraciques - DRS`** : « MONA » sans réserve, alors que l'attendu
   noté de la même grille écrit correctement « Oxygène si SaO2 < 90 % ». Le
   mnémonique a été désamorcé (O₂ si SpO₂ < 90 % seulement, nitré contre-indiqué
   au VD, morphine non systématique).
3. **`Dyspnée dans un contexte infectieux`** : CURB-65, critère tensionnel écrit
   « Blood pressure **< 90/60 mmHg** » — la règle est TAS < 90 **OU** TAD ≤ 60 ;
   exiger les deux sous-cote la gravité et sous-triage le patient. Corrigé,
   qSOFA ajouté.
4. **`Dyspnée et insuffisance cardiaque`** : CHA₂DS₂-VASc, « Score ≥ 2 :
   anticoagulation recommandée » sans seuil sexué, alors que la grille compte
   elle-même 1 point pour le sexe féminin — une femme dont le score ne tient
   qu'à son sexe se retrouve anticoagulée. Corrigé (≥ 2 homme / ≥ 3 femme).
5. **`Dyspnée et mal au cou`** : « Groupes **A-D** selon symptômes et
   exacerbations ». GOLD a fusionné C et D en **E** depuis 2023. Corrigé, avec
   le rappel que le grade spirométrique ne décide pas du traitement (motif
   d'AMC 4 au lot `t1`).
6. **`Dyspnée et mal au cou`** : « pneumocoque **tous les 5 ans** » — schéma de
   l'ancien polysaccharidique 23-valent, remplacé en Suisse par une dose unique
   de conjugué chez l'adulte à risque. Corrigé.
7. **`Grille ECOS USIT2 - Diarrhée Hématochézie`** : « Dépistage systématique :
   **50-74 ans**, test FIT tous les 2 ans ». C'est la tranche du programme
   **français**. `SSP — Rectorragies` : « dépistage organisé **en Suisse 50-69
   ans** : test FIT tous les 2 ans ou coloscopie tous les 10 ans (OFSP /
   SSG-SGG) ». Troisième francité du corpus après « ARS » (`t1`) et « 6 mois en
   France » (`t2`). Corrigé.
8. **`Épisode dépressif majeur`** : « Gravité — Léger (5-6 symptômes), modéré
   (7-8), **sévère (≥ 9 symptômes)** ». Le DSM-5 ne compte que 9 critères : la
   règle telle qu'écrite réserve « sévère » au tableau complet, et classe
   « modéré » un épisode à 7 symptômes avec projet suicidaire précis. La
   sévérité combine nombre, intensité et retentissement. Corrigé, avec les
   bandes du **PHQ-9** que la page donne (5-9 / 10-14 / 15-19 / ≥ 20).
   Corrigé aussi : « antidépresseurs **IRRS** » → ISRS.

### 6. Les trous du canonique comblés — vingt-six

`theorie` tient le rôle canonique sur **25/25**. Aucune grille du lot n'en est
dépourvue, contrairement aux Psy-Vignette de `t1`.

| grille | ce qui manquait |
|---|---|
| 36 DRS | **V3R-V4R** et le ventricule droit — **0 occurrence** · Sgarbossa · dérivations postérieures V7-V9 · répétition de l'ECG à 15-30 min |
| 37 Dyspnée aigue | les **6 urgences vitales** nommées · le seuil de D-dimères **ajusté à l'âge** · la FR comme meilleur signe précoce · **144** et **145** |
| 38 Polymorbidité | seuils réels de la metformine (DFGe < 30 CI, 30-45 réduction) et surtout la **suspension aiguë** (sepsis, hypoxie, produit de contraste iodé) · l'ordre de traitement de l'hyperkaliémie (calcium d'abord) |
| 39 Infectieux | qSOFA · réserve du macrolide en monothérapie · amoxicilline en 1ʳᵉ intention (SSMI/SGAIM) |
| 40 Insuffisance cardiaque | **ARNI et SGLT2** — **0 occurrence** dans une grille d'IC · HAS-BLED ne justifie pas l'abstention |
| 41 Mal au cou | groupes GOLD A/B/E · PaO2 en **kPa** · réserve symétrique de l'O₂ chez le BPCO (« l'hypoxie tue en minutes ») |
| 42 post-COVID | **arrêt du sport 3-6 mois après myocardite** — la grille lançait une réhabilitation sans l'écarter · signes imposant le **144** |
| 43 Enfant qui boîte | **maltraitance** — **0 occurrence**, alors que la page en fait un red flag · **147 Pro Juventute** · **APEA/KESB** · arthrite septique = **urgence chirurgicale** (lavage) · épiphysiolyse = **interdiction de mise en charge** + **Lauenstein** · leucémie |
| 44 EM Activité physique | la **cible chiffrée** (150-300 min/sem + 2 renforcements) — une station de négociation d'un plan sans dose · OARS, Ask-Tell-Ask, échelles 0-10 |
| 45 EM Compliance | **DARN-CAT**, OARS, Ask-Tell-Ask · les traitements qui ne se suspendent pas (bêtabloquant, corticoïde, antiépileptique, antiagrégant post-stent) |
| 46 EM Alcool | **verre standard suisse**, seuils OFSP, **AUDIT-C** (≥ 4 H / ≥ 3 F), bandes de l'AUDIT · **CIWA-Ar ≥ 15 et delirium tremens** : ne pas faire initier un sevrage seul · **thiamine avant tout glucose** (Wernicke) · **143**, **144**, **0800 104 104**, **LAVI**, **147**, **APEA/KESB** |
| 47/48 EM Tabac | contre-indications du bupropion et de la varénicline · doses des substituts · **5 R** · ressources suisses (0848 000 181, 0800 11 88 11, CIPRET) |
| 49 Épilepsie absence | **valproate chez une fille** : tératogénicité, à réserver faute d'alternative · surveillance **FSC** sous éthosuximide · **noyade** : jamais de bain ni de baignade seule · information de l'école et projet d'accueil individualisé |
| 50 Épisode dépressif | **MDQ** — **0 occurrence** · **RUD / C-SSRS** et l'entonnoir complet · moyens létaux · **levée d'inhibition J7-J15** · **PAFA art. 426 CC**, **art. 16 CC** · **143 / 144 / 147** |
| 51 Épisode maniaque | **PAFA art. 426 CC** et ses trois conditions · la distinction avec le **traitement sans consentement (art. 434 CC)** · **curatelle art. 390 ss et 394-395 CC** via l'**APEA/KESB** — la réponse exacte au « sécuriser financièrement » de son `expert` · bilan pré-lithium complet · lithémie cible et rebond à l'arrêt |
| 52 Érythème cutané | tous les signes de la **fasciite nécrosante** et la chirurgie · **porte d'entrée** (intertrigo/tinea pedis) · délimitation de l'érythème au feutre |
| 53 Fatigue - Vignettes | **rupture splénique** de la MNI et le **rash à l'aminopénicilline** · **hydrocortisone 100 mg IV sans attendre le Synacthen** dans la crise surrénalienne · carence martiale = **cancer colorectal jusqu'à preuve du contraire** · PHQ-2, STOP-BANG, aptitude à la conduite · **143/144/147** |
| 54 Fatigue chroniques | risque suicidaire et **143** · **STOPP/START** · B-symptômes |
| 55 Fatigue TBL | magnésium avant de corriger la kaliémie · spironolactone · risque thrombo-embolique de l'hypercortisolisme |
| 56 Gonococcie | **doxycycline** en 1ʳᵉ ligne pour *Chlamydia* · ponction **avant** la 1ʳᵉ dose · déclaration OFSP et fenêtre de 60 jours détaillées |
| 57 Goutte | **ne jamais ARRÊTER l'allopurinol en crise** — la moitié manquante de la règle · **HLA-B*58:01 / DRESS-SJS** · interactions de la **colchicine** (macrolides, azolés, ciclosporine, statines) · allopurinol + azathioprine |
| 58 Diarrhée Hématochézie | **seuil transfusionnel Hb < 70 g/L (< 80 si cardiopathie ischémique)** · **10-15 % des HDB sévères sont des HDA → OGD d'abord** · Oakland, shock index · réversion des anticoagulants |
| 59 Hernie discale | **queue de cheval : IRM < 24 h, décompression < 24-48 h, 144** — absente de `theorie`, dont la liste d'indications chirurgicales autorisait 3-6 mois de conservateur · *smarter medicine* · STarT Back |
| 60 Opioïdes | **≥ 12-24 h et perfusion continue** après méthadone · doses de titration de la naloxone · CI complètes du flumazénil · **DON'T** et **thiamine avant glucose** · évaluation psychiatrique et **143** avant la sortie |

### 7. Le balayage de protection — troisième zéro consécutif

Relevé **avant** intervention sur les 25 :

| terme | grilles concernées |
|---|---|
| `PAFA` · `art. 426` · `art. 16 CC` · `APEA`/`KESB` · `curatelle` · `discernement` | **0 sur 25** |
| `143` La Main Tendue · `147` Pro Juventute | **0 sur 25** |
| `144` | **1** (Douleurs thoraciques - DRS) |
| `145` Tox Info Suisse | **1** (Intoxication opioïdes) |
| `LAVI` | **0** — les 3 occurrences du motif étaient « sus-**clavi**culaire » et « médio-**clavi**culaire » |
| `suicid*` | **1** (Épisode dépressif majeur) |

Les faux positifs valent d'être notés : « 143 » ne se trouvait que dans une
créatinine à 143, « 145 » que dans une TA à 145/90. Le balayage se fait à la
main, aucun outil ne le déclenche, et il faut relire chaque occurrence.

Six grilles du lot relèvent d'un thème de protection — les deux psychiatriques,
les cinq d'entretien motivationnel (alcool, tabac, observance) et la pédiatrique.
Conformément à la consigne, **rien n'a été retiré** ; une ou deux sections ont
été ajoutées à `theorie`.

### 8. Barème — deux lignes touchées, l'exception assumée

Les deux corrections dans un attendu de correction sont au § 4, points 1 et 2.
Toutes les autres éditions portent sur `theorie` et `annexe-dd` ; `redflags`,
`expert`, `resume`, `presentation` et `scenario` n'ont pas été approchés.

**Preuve d'innocuité.** `check_invariants` est vert sur les 165 : les quatorze
champs du snapshot sont identiques à la baseline. **Baseline non régénérée.**
Sur 25 fichiers, le diff complet compte 229 lignes ajoutées ou retirées, dont
**aucune** ne porte `window.caseConfig`, `<script`, `criteria-text`,
`criteria-detail`, `type="checkbox"`, `type="radio"`, `maxScores`,
`sectionInfo`, `coef`, `<span class="score">`, `points-display`,
`checkbox-group` ni `section-header`. **0 sous-item ajouté ou retiré.** Les deux
corrections notées sont des compléments de texte à l'intérieur d'une puce de
`therapy-section`, qui est une annotation du critère et non un sous-item coté.

### 9. `check_nomenclature` attrape une régression pour la deuxième fois

La première rédaction écrivait « éosinophiles ≥ 300/µL » (grille 41) et
« > 50 000 leucocytes/mm³ » (grille 57) — deux unités bannies, reprises telles
quelles de la source. La porte les a rejetées ; converties en 0,3 G/L et
50 G/L avant validation. **Deuxième lot consécutif où la porte rattrape le
traitement lui-même** : l'argument pour la câbler en CI se renforce.

### 10. Ce qui reste consigné, non corrigé

1. **`Dyspnée aigue`, `therapy`** : « Nitroglycérine (**Isoket**) 2 mg/h IV si
   TA > 100 mmHg ». Isoket® est du **dinitrate d'isosorbide**, pas de la
   nitroglycérine — coquille de dénomination dans un attendu noté. Elle ne
   change ni la conduite ni la classe ; la réserve du ventricule droit et le nom
   exact ont été portés dans `theorie`. **La page ne pose pas la réserve du VD
   pour l'OAP** (elle écrit « trinitrine IV si TAS > 100 »), donc la condition
   « sourcée » de l'arbitrage n'est pas remplie pour toucher l'attendu.
2. **`Dyspnée et insuffisance cardiaque`** : « Furosémide IV **continue (pas
   bolus)** ». L'essai DOSE n'a pas montré de supériorité de la perfusion
   continue ; la formule tranche une question ouverte. Pas une erreur de
   sécurité.
3. **`Entretien motivationnel - Sevrage tabagique`** : bandes du Fagerström
   « 0-2 pas de dépendance · 3-4 faible · 5-6 moyenne · 7-10 forte », contre
   « 0-2 faible · 3-4 moyenne · 5-7 forte · 8-10 très forte » sur la page. Les
   deux découpages existent dans la littérature et aucun n'est dangereux ;
   laissé tel quel plutôt que d'imposer un choix.
4. **`Fièvre et douleurs articulaires`, `therapy`** : « Alternative si allergie :
   **Spectinomycine 2 g IM 2×/j ou Azithromycine 2 g PO** ». La spectinomycine
   n'est pas disponible en Suisse et l'azithromycine 2 g en monothérapie n'est
   plus recommandée dans la gonorrhée. La réserve a été portée dans `theorie` ;
   l'attendu noté n'a pas été touché, la page ne traitant pas l'allergie.
5. **`Dyspnée dans un contexte de polymorbidité`** : « PaCO2 > 45 mmHg »,
   « PaO2 54 mmHg » — gaz du sang en mmHg dans un corpus suisse. Invisible à
   `check_nomenclature`, qui ne borne que les analytes. Comme les huit
   numérations en unité implicite du lot `l4`, c'est une famille à coder.

### 11. Deux préoccupations de fond

**`SSP — Dépression` se contredit toujours.** Son bloc `redflag` écrit
« hospitalisation immédiate (**SDT/SDRE/SPI selon contexte**) » — la nomenclature
de la loi **française** — quand les huit autres occurrences de la page disent
correctement **PAFA (art. 426 CC)**, et que sa carte ECOS ajoute la capacité de
discernement (art. 16 CC). C'est le même constat qu'au lot `t2` : la page n'a pas
bougé. C'est le **troisième** cas de page du vault qui se contredit, après
`SSP — Urgences Psychiatriques` (`t1`) et celle-ci. Le vault est hors du dépôt ;
c'est la version suisse qui a été portée dans les deux grilles psychiatriques.

**Deux pages ne portent pas la matière de leur grille.**
`SSP — Éruption Cutanée` cite « Érythème cutané avec douleur » mais n'a **aucune
section cellulite / érysipèle** (le mot « cellulite » y apparaît une fois, entre
parenthèses), **aucun score LRINEC**, **aucun délai chirurgical chiffré**,
**aucune mention du pied diabétique ni de la porte d'entrée**. `SSP — Malaise`
cite « Épilepsie absence - Fille de 7 ans » mais n'a **aucun contenu sur les
absences** — ni pointe-onde 3 Hz, ni éthosuximide, ni hyperpnée — et **aucun
délai chiffré de suspension de conduite** (constat déjà fait au lot `t2`). Le
niveau 2 a été appliqué dans les deux cas, et rien n'a été inventé : les signes
de la fasciite portés sont ceux que la page énonce (« crépitation, douleur
disproportionnée »), le LRINEC n'a **pas** été présenté comme sourcé.

### 12. Vérifications

```
check_invariants.py                     OK — 165 grilles, code 0
check_nomenclature.py                   OK — 0 terme, code 0
check_reachability.py                   OK — 156/156 notées à 100 %, code 0
report_redundancy.py (lot de 25)        232 -> 226
report_redundancy.py (corpus)           1011 -> 1005   (−6 = gain du lot)
check_no_loss.py 74e51e7                40 items, verdictés un à un, 0 perte
browser_probe.js (les 25) --deep        25/25 sans exception · 25/25 à 100 %
                                        25/25 registry · barre nav fixed
                                        0 recouvrement · crochets colorés 25/25
bounds_anomalies / uncovered_content    [] / {} sur les 25
format .criteria-text « N. Libellé »    0 écart sur les 25
crochets […] de cloture                 57, intacts

AMBOSS  report_redundancy 147 (inchangé) · invariants / nomenclature / atteignabilité code 0
RESCOS  report_redundancy 127 (inchangé) · invariants / nomenclature / atteignabilité code 0
```

Les 40 items signalés par `check_no_loss` sont des réécritures sur place —
aucune suppression. Quatre notions menacées par une réécriture ont été
**restituées** avant validation : la surveillance de la déshydratation sous
lithium (51), la cocaïne parmi les contre-indications du flumazénil (60), le
doublement des doses de substituts nicotiniques en cas de forte dépendance (47)
et le repos de 4-6 semaines de la MNI (53). **Aucun retrait plein.** Les seules
disparitions assumées sont les huit corrections d'erreur du § 5 et les sept du
§ 4.

German et casecos n'ont été ni lus ni mesurés : l'utilisateur y travaille en
parallèle.

---

## Lot `t4` — 25 grilles thématiques, des trois « Intoxication » à « Pharmacologie clinique 3 »

Branche `refonte-amboss-suisse`, base `fb78039`. **25 fichiers modifiés**, tous
sous `cases/rescos-locales/`. Rien touché sous `cases/german/`,
`scripts/german/`, `cases/casecos/` ni `scripts/casecos/` — ni lu, ni écrit.

**Redondance du lot : 193 → 190.** Corpus **1005 → 1002** (−3, exactement le
gain du lot ; septième confirmation de l'économie de mesure). Les trois portes
sont vertes ; AMBOSS reste à **147**, RESCOS à **127**.

### 1. Le lot — et une correction de la liste héritée de `t3`

123 grilles thématiques (nom ne commençant pas par `RESCOS-<chiffre>`, hors les
9 feuilles porte). 70 traitées par `t1` (rangs 2-11 et 89-98), `t2` (rangs 1 et
12-35) et `t3` (rangs 36-60).

**Le lot `t3` a énuméré 53 grilles restantes mais n'en a nommé que 50.** Les
trois manquantes sont les rangs 61 à 63, c'est-à-dire les trois `Intoxication`
autres que celle des opioïdes. Le mandat reçu reprenait cette énumération et
demandait de repartir à `Lésion de la coiffe des rotateurs` (rang 64) — ce qui
aurait laissé un trou de trois grilles derrière le front. **La règle a été
appliquée plutôt que l'ancre** : ce lot prend les **rangs 61 à 85**, ce qui
reste 25 grilles et ne laisse aucun trou. Vérification faite, les trois
`Intoxication` n'avaient été touchées par `74e51e7` que pour le retrait d'un
`undefined` — leur `diff` ne compte qu'une ligne, et aucun contenu pédagogique.

| # | rang | grille | redondance |
|---:|---:|---|---:|
| 1 | 61 | Intoxication — Syndrome anticholinergique (Belladone) | 1 → 1 |
| 2 | 62 | Intoxication — Syndrome malin des neuroleptiques | 1 → 1 |
| 3 | 63 | Intoxication médicamenteuse — Paracétamol et benzodiazépines | 0 → 0 |
| 4 | 64 | Lésion de la coiffe des rotateurs | 19 → 19 |
| 5 | 65 | Lupus érythémateux systémique — Femme de 26 ans | 26 → 26 |
| 6 | 66 | Mal à l'épaule — Douleur thoracique | 1 → 1 |
| 7 | 67 | Mal au dos — Syndrome de Guillain-Barré | 30 → **27** |
| 8 | 68 | Mal au dos — Syndrome de Guillain-Barré (1) | 3 → 3 |
| 9 | 69 | Mal au dos 2 — Syndrome de Guillain-Barré | 23 → 23 |
| 10 | 70 | Ménopause — Femme de 53 ans | 14 → 14 |
| 11 | 71 | Ostéoporose prévention — Femme de 56 ans | 19 → 19 |
| 12 | 72 | Otosclérose — Femme de 33 ans | 8 → 8 |
| 13 | 73 | Pédiatrie — Cardiopathie congénitale CIV | 0 → 0 |
| 14 | 74 | Pédiatrie — Détresse respiratoire bronchiolite et asthme | 1 → 1 |
| 15 | 75 | Pédiatrie — Enfant 3 ans avec toux | 0 → 0 |
| 16 | 76 | Pédiatrie — État fébrile sans foyer | 2 → 2 |
| 17 | 77 | Pédiatrie — Nourrisson 6 mois avec fièvre | 0 → 0 |
| 18 | 78 | Pédiatrie — Nouveau-né en détresse respiratoire | 0 → 0 |
| 19 | 79 | Pédiatrie — Nouveau-né normal et suivi | 0 → 0 |
| 20 | 80 | Pédiatrie — Occlusion sur bride | 0 → 0 |
| 21 | 81 | Pédiatrie — Torsion testiculaire | 0 → 0 |
| 22 | 82 | Pédiatrie — Vomissements et état fébrile — Méningite | 1 → 1 |
| 23 | 83 | Pemphigoïde bulleuse — Femme de 81 ans | 24 → 24 |
| 24 | 84 | Pharmacologie clinique 1 — Traitement de la douleur | 11 → 11 |
| 25 | 85 | Pharmacologie clinique 3 — Interactions médicamenteuses | 9 → 9 |
| | | **total** | **193 → 190** |

Les trois paires gagnées le sont sur `Mal au dos — Guillain-Barré`, par le même
mécanisme qu'aux lots précédents : allonger un item de `theorie` lui fait
franchir le seuil de 0,72 en sens inverse face à son jumeau de `presentation`.
Rien n'a été supprimé.

**Les 28 restantes**, dans l'ordre : `Pityriasis versicolor` ·
`Polymyalgia Rheumatica` · `Psoriasis - Femme de 42 ans` ·
`RCI-Fièvre et douleurs articulaires` · `Sclérose en plaques` ·
les **3 `SD - Dépistage …`** · les **2 `Sémiologie MSQ`** · `SMIG-1 Syncope` ·
les **3 `SMIG-2`** · `SMIG-3` · `SMIG-4` · `SMIG-5` ·
`Syndrome de Guillain-Barré - Homme de 42 ans` ·
`Syndrome de Stevens-Johnson` · `Syndrome du canal carpien` ·
`Syphilis secondaire` · `TDAH pédiatrique` · `Toux et maux de ventre` ·
`Transaminases élevées` · `Trouble panique` · `Urticaire allergique` ·
`Voyage à Madagascar` · `Voyage au Brésil`.

### 2. Le mapping inverse — 24 pages sur 25, dont deux hors de `SSP ECOS/`

Chaque grille du lot est citée nommément dans le bloc « Références PDF » d'une
page et d'une seule. **Dix-huit pages** les couvrent, dont **une de
`Skills ECOS/`** — `Skills — Réflexes Médicamenteux & Antidotes`, qui porte à
elle seule les deux `Pharmacologie clinique`. Une seule page en porte trois,
`SSP — Fièvre du Nourrisson` ; quatre en portent deux —
`SSP — Intoxications Aiguës` (plus celle du lot `t3`), `SSP — Ménopause`,
`SSP — Lombalgies` et `Skills — Réflexes Médicamenteux & Antidotes`.

**Une seule grille n'est citée nulle part** : `Mal au dos - Syndrome de
Guillain-Barré - Grille ECOS (1)`. C'est le doublon divergent déjà inventorié
au § 6 de la procédure ; ses deux sœurs sont citées par `SSP — Lombalgies`,
dont la matière lui a été appliquée à l'identique.

### 3. `expert` — la lecture d'abord, et ce qu'elle a rendu

**23 grilles sur 25 ont un `expert`** ; les deux qui n'en ont pas
(`Enfant 3 ans avec toux`, `Nourrisson 6 mois avec fièvre`) n'ont **pas non plus
de `theorie`**, et ce sont précisément les deux qui portaient les défauts les
plus nets du lot. **Quatrième confirmation** qu'une grille pauvre en blocs n'est
pas une grille saine.

**Neuf fois**, `expert` reproche au candidat d'oublier une chose dont la réponse
n'existe nulle part dans la grille :

| la grille exige… | elle disait… |
|---|---|
| « Confondre avec un syndrome sérotoninergique » (Belladone) | rien : 0 occurrence de clonus, hyperréflexie, Hunter, cyproheptadine |
| « Confondre avec un syndrome sérotoninergique » (SMN) | une entrée d'`annexe-dd`, sans un seul discriminant chiffré ni le traitement |
| « Méconnaître les polymorphismes CYP2D6 » (Pharmaco 1) | `CYP2D6` dans un attendu noté et dans `expert`, **rien** dans `theorie` |
| « Prescrire des AINS sans considérer les interactions (IEC, diurétiques) » | rien : 0 occurrence de *triple whammy* |
| « Savoir quand orienter vers la chirurgie » (coiffe) | ni critère, ni délai, ni notion de réparabilité |
| « Quelle est la différence entre stapédotomie et stapédectomie ? » | **la stapédectomie n'était nommée nulle part** hors de la question |
| « Ne pas oublier de rechercher les atteintes silencieuses » + patiente de 26 ans (LES) | 0 occurrence de contraception, tératogène, rétinopathie |
| « Méconnaître un corps étranger inhalé » (bronchiolite) | une ligne d'`annexe-dd`, sans syndrome de pénétration ni bronchoscopie |
| « Critères de sortie de maternité » (nouveau-né) | 0 occurrence de mort subite, d'atrésie des voies biliaires, de bilirubine conjuguée |

### 4. Sept erreurs de sécurité — dont deux dans un bloc noté

1. **`Nourrisson 6 mois avec fièvre` — deux absences de signe rangées CONTRE les
   deux diagnostics graves, dans la même `annexe-dd`.**
   « Méningite — **Arguments CONTRE** : fontanelle normale · pas de raideur »
   et « Pyélonéphrite — **Arguments CONTRE** : pas de signes urinaires · couches
   mouillées normalement », chez un nourrisson de 6 mois. Avant 12-18 mois, la
   raideur de nuque et le bombement de la fontanelle **manquent dans la majorité
   des méningites**, et l'infection urinaire se manifeste par une **fièvre
   isolée sans aucun signe urinaire** — c'est l'infection bactérienne sérieuse
   la plus fréquente à cet âge.
   **La grille jumelle le dit elle-même** : `État fébrile sans foyer` écrit
   « Méningite — **peut débuter sans signes méningés** » et « Pyélonéphrite —
   **pas toujours de signes urinaires à cet âge** », et
   `Vomissements et état fébrile` écrit « signes méningés **adaptés à l'âge** ».
   Trouvé par le contrôle des sœurs. Les deux entrées ont été retournées, et le
   « → Bandelette urinaire **si la fièvre persiste** » corrigé en bandelette
   d'emblée. **Troisième occurrence** du motif « absence de signe en argument
   CONTRE un diagnostic grave » (Psy-Vignette 4 au lot `t1`, Goutte et Enfant
   qui boîte au lot `t3`) — et la première où il frappe **deux fois dans la même
   grille**.
2. **`Paracétamol et benzodiazépines` — flumazénil recommandé exactement là où
   il est le plus dangereux.** `theorie` écrivait « Flumazénil : **uniquement si
   dépression respiratoire sévère**, risque de convulsions ».
   `SSP — Intoxications Aiguës` en fait un **piège éliminatoire** :
   « CONTRE-INDIQUÉ chez l'épileptique connu, en co-ingestion d'ATD tricycliques
   ou de toxique pro-convulsivant ». La station est une **intoxication volontaire
   polymédicamenteuse** dont l'inventaire n'est pas certain : c'est la situation
   type de la contre-indication. La grille **se contredit elle-même**, son
   `expert` inscrivant « Administrer du flumazénil systématiquement » parmi ses
   pièges. Corrigé : contre-indication explicite, conduite par soutien
   ventilatoire, et bicarbonate si QRS > 100 ms.
3. **`Lupus érythémateux systémique - Femme de 26 ans` — méthotrexate et
   mycophénolate proposés à une femme de 26 ans sans un mot sur la
   tératogénicité, dans l'attendu noté.** `SSP — Douleurs Articulaires` écrit
   « Grossesse / désir : méthotrexate et léflunomide **contre-indiqués** ;
   hydroxychloroquine et sulfasalazine compatibles » et « adapter le traitement
   si grossesse ». La grille n'avait **aucune occurrence** de « contraception »
   ni de « tératogène ». Corrigé dans `theorie` (volet complet : contraception,
   anti-Ro/SSA et BAV congénital, antiphospholipides et grossesse) **et** dans le
   `Détails` du `therapy`, sans ajout ni retrait de sous-item.
4. **`Ostéoporose prévention` — dénosumab sans l'avertissement du rebond.** La
   grille l'énumérait comme une option parmi d'autres. Son interruption, ou un
   simple retard d'injection, provoque un **rebond de résorption avec fractures
   vertébrales multiples** ; tout arrêt exige un relais immédiat par
   bisphosphonate. S'y ajoutaient l'absence de correction préalable de la
   carence en vitamine D (hypocalcémie sévère), l'absence des modalités de prise
   des bisphosphonates oraux et le relais obligatoire après tériparatide.
5. **`Belladone` — physostigmine sans la contre-indication qui tue.** La liste
   de `therapy` (« bloc AV, asthme, obstruction mécanique ») omet le **QRS
   élargi et la suspicion de tricycliques**, association qui a provoqué des
   asystolies — alors que la `theorie` de la même grille écrit que
   l'intoxication donne « parfois QRS élargi » et que son `annexe-dd` garde les
   tricycliques au différentiel. Porté dans `theorie` ; `therapy` non touché
   (voir § 7.2).
6. **`Mal à l'épaule — péricardite` — tamponnade décrite sans sa conduite.**
   `redflags` la nomme et en donne les signes ; rien nulle part sur la
   **péricardiocentèse en urgence** ni sur le fait que **diurétiques, dérivés
   nitrés et ventilation en pression positive y sont dangereux** (choc
   obstructif précharge-dépendant). C'est la **famille physiopathologique de la
   récidive des nitrés** : quatrième grille du corpus où un état
   précharge-dépendant est décrit sans sa réserve.
7. **`Cardiopathie congénitale CIV` — « Vaccination RSV (palivizumab) si < 2
   ans ».** Le palivizumab n'est **pas un vaccin** mais un anticorps monoclonal
   à administrer **mensuellement pendant la saison**, et il n'est pas indiqué
   chez tous les enfants de moins de 2 ans. Présenté comme une vaccination, il
   laisse croire à une protection acquise en une injection. Corrigé, avec le
   nirsévimab. Même grille : « Prophylaxie endocardite si indiquée » remplacé par
   les indications réelles — **une CIV isolée non opérée ne la justifie pas**.

### 5. Neuf autres corrections et compléments majeurs, dans `theorie`

* **Guillain-Barré (les 3)** — la surveillance respiratoire ne se fait ni à la
  saturation ni à la gazométrie (**l'hypercapnie est un signe tardif**) mais à
  la capacité vitale, PiMax et PeMax, règle des **20/30/40** ; pas de
  succinylcholine ; dysautonomie ; **ne pas associer Ig IV et plasmaphérèse** ;
  fenêtre de deux semaines ; doser les IgA avant les Ig IV. Et, les trois
  grilles se présentant comme des lombalgies : **0 occurrence de « queue de
  cheval »** avant intervention, alors que c'est le premier drapeau rouge de
  `SSP — Lombalgies`. Ajouté avec l'anévrisme fissuré, la spondylodiscite et la
  métastase.
* **Pharmacologie 1** — CYP2D6 et codéine : promédicament, métaboliseurs lents
  et ultra-rapides, **contre-indication avant 12 ans, après amygdalectomie et
  pendant l'allaitement** ; *triple whammy* ; aspirine et Reye ; AINS et
  varicelle ; AINS au 3e trimestre.
* **Pharmacologie 3** — la **désinduction** : l'arrêt d'un inducteur expose à un
  surdosage retardé de 1 à 3 semaines, à programmer et non à subir ; conduite de
  la torsade de pointes (**sulfate de magnésium 2 g**, kaliémie ≥ 4,0 mmol/L,
  jamais d'antiarythmique allongeant le QT) ; millepertuis et P-gp (échec de
  contraception, rejet de greffe).
* **SMN** — métoclopramide et arrêt de L-DOPA comme déclencheurs ;
  rhabdomyolyse au-delà de 1000 U/L, hyperkaliémie, CIVD, myoglobinurie ;
  soins intensifs ; réintroduction d'un antipsychotique à distance ; tableau
  différentiel complet avec le syndrome sérotoninergique.
* **Coiffe des rotateurs** — les trois familles à écarter avant de conclure :
  rachis cervical et Spurling, causes viscérales projetées (SCA, cholécystite,
  Pancoast chez cet ancien fumeur de 62 ans), arthrite septique, PPR et Horton,
  métastase. Puis les critères et le **délai** de l'adressage chirurgical.
* **Ménopause** — voie **transdermique** préférée si risque thromboembolique ;
  le traitement hormonal **n'est pas une contraception** (12 mois après 50 ans,
  24 avant) ; paroxétine et fluoxétine à éviter sous tamoxifène ; métrorragie
  post-ménopausique = cancer de l'endomètre jusqu'à preuve du contraire ;
  dépistages suisses, **colorectal 50-69 ans**.
* **Otosclérose** — la différence stapédotomie / stapédectomie, que l'`expert`
  demande et que la grille ne portait pas ; l'**oreille unique entendante**
  comme contre-indication.
* **Pemphigoïde bulleuse** — clobétasol sur tout le tégument au moins aussi
  efficace que la voie générale chez le sujet âgé ; **TPMT avant azathioprine** ;
  bouquet de prévention de la corticothérapie prolongée ; arrêt de la gliptine
  inductrice.
* **Pédiatrie** — ce qu'on **ne** fait pas dans la bronchiolite (dont la
  kinésithérapie respiratoire) ; corps étranger inhalé et syndrome de
  pénétration (**0 occurrence** dans `Enfant 3 ans avec toux`) ; minute d'or et
  cibles de saturation préductale du nouveau-né ; les deux ictères jamais
  physiologiques et l'**atrésie des voies biliaires avant 45-60 jours** ;
  prévention de la mort subite ; purpura fulminans et antibiotique avant tout ;
  signes de strangulation dans l'occlusion et fin du dogme de l'antalgie
  différée ; détorsion manuelle externe d'attente ; déclaration suisse du
  méningocoque en 2 heures.

### 6. Le balayage de protection — quatrième zéro consécutif

Relevé sur les 25, **avant** intervention :

| terme | occurrences |
|---|---|
| `PAFA` · `art. 426` · `art. 16 CC` · `APEA`/`KESB` · `curatelle` · `discernement` | **0 sur 25** |
| `143` · `147` | **0 sur 25** |
| `144` | 1, sur la seule grille de méningite |
| `145` | 4 (les 3 intoxications + Pharmacologie 3) |
| `LAVI` | 7 occurrences, **toutes** « sus-**clavi**culaire » ou « acromio-**clavi**culaire » |

**Quatre lots, 95 grilles, le même zéro.** Rien n'a été retiré ; deux sections
ont été ajoutées à `theorie` : le PAFA et ses conditions (art. 426 CC, en
distinguant l'art. 434 CC pour le traitement sans consentement) avec le filet de
sécurité 143/147 dans la grille de tentative de suicide, et la **capacité de
discernement du mineur (art. 16 CC)** dans la grille de torsion testiculaire —
un adolescent de 13-16 ans consent lui-même à une chirurgie potentiellement
mutilante, et la station ne le disait pas.

### 7. Préoccupations

#### 7.1 La liste des restantes, transmise fausse d'un lot à l'autre

Voir § 1. L'énumération de `t3` a perdu trois noms sans que son total le
signale, et le mandat de ce lot a repris l'ancre erronée. **Le contrôle qui
rattrape est le calcul de la liste par la règle**, pas la lecture du rapport
précédent. Recommandation : donner le rang numérique dans le rapport, et pas
seulement les noms.

#### 7.2 Trois divergences laissées dans un bloc noté, consignées

1. **`Belladone`, `therapy`** : « CI : bloc AV, asthme, vessie/intestin
   mécaniquement obstrués » — la liste est présentée comme complète et omet le
   QRS large. La page ne traite pas la physostigmine ; la condition « sourcée »
   de l'arbitrage n'était donc pas remplie, et la réserve a été portée dans
   `theorie` seule. **C'est la divergence la plus sérieuse du lot.**
2. **`Paracétamol`, `therapy`** : « Étape 2 : 150 mg/kg dans 1000 ml sur 24 h
   (**1×/jour pendant 3 jours**) » — la N-acétylcystéine intraveineuse est une
   perfusion continue de 21 h (schéma en trois poches) ou de 20 h (schéma en
   deux poches), prolongée en présentation tardive jusqu'à normalisation de
   l'INR — jamais trois doses journalières. Le schéma correct est porté dans
   `theorie`.
3. **`Bronchiolite`, `therapy`** : « Maintien saturation **> 94 %** », quand le
   `redflags` de la même grille fixe le seuil d'hypoxémie à **92 %**. La grille
   se contredit ; viser 94 % prolonge l'hospitalisation sans bénéfice. Seuil
   actuel porté dans `theorie`.

#### 7.3 Une déclaration obligatoire suisse imprécise, dans un sous-item noté

`Vomissements et état fébrile — Méningite` porte, dans un `criteria-text`,
« Déclaration obligatoire [**NON pour pneumocoque**] ». En Suisse, l'infection
invasive à pneumocoque **est** soumise à déclaration — par le laboratoire et
dans le délai ordinaire ; ce qui n'existe pas, c'est la déclaration urgente par
le clinicien et la chimioprophylaxie de l'entourage, réservées au méningocoque.
Le sous-item n'a pas été touché (règle 2 du barème) ; `theorie` porte désormais
la formulation exacte, **complémentaire et non contradictoire** avec l'attendu.

#### 7.4 Une page qui ne porte pas la matière de sa grille

`SSP — Éruption Cutanée` cite `Pemphigoïde bulleuse` mais n'a **aucune section
sur les dermatoses bulleuses auto-immunes** : le mot « pemphigoïde » n'y figure
que deux fois, dans un tableau de lésions élémentaires et sa légende. Constat
identique à celui du lot `t3` sur la même page pour la cellulite et la fasciite.
Niveau 2 appliqué. De même, `SSP — Troubles de la Croissance` cite
`Cardiopathie congénitale CIV` sans rien porter sur les cardiopathies, et
`SSP — Détresse Respiratoire (Adulte-Enfant non-néonatal)` est presque
entièrement adulte pour une grille de bronchiolite.

#### 7.5 Coordination

Aucun `git add`. Validation directe par
`git commit -F <fichier> -- cases/rescos-locales/ docs/superpowers/journal-…`.
`core.quotepath=false` sur toutes les commandes de contrôle. Aucun `git push`,
aucune commande réseau, aucun `git gc` ni `git prune`. Les fichiers de
l'utilisateur sous `cases/german/`, `cases/img/german/`, `cases/casecos/` et
`scripts/casecos/` étaient déjà modifiés au démarrage : ni touchés, ni inclus
dans le commit. Un `git stash push -- cases/rescos-locales/` a été employé deux
fois pour mesurer l'état « avant », toujours suivi immédiatement de son `pop`,
et toujours borné au seul chemin `cases/rescos-locales/`.

### 8. Vérifications

```
check_invariants.py                     OK — 165 grilles, code 0
check_nomenclature.py                   OK — 0 terme, code 0
check_reachability.py                   OK — 156/156 notées à 100 %, code 0
report_redundancy.py (lot de 25)        193 -> 190
report_redundancy.py (corpus)           1005 -> 1002   (−3 = gain du lot)
check_no_loss.py fb78039                25 items, verdictés un à un, 0 perte
browser_probe.js (les 25) --deep        25/25 sans exception · 25/25 à 100 %
                                        25/25 registry · barre nav fixed
                                        0 recouvrement · crochets colorés 25/25
bounds_anomalies / uncovered_content    [] / {} sur les 25
snapshot champ par champ                0 divergence — 14 champs × 25 grilles
diff : marqueurs de barème              0 ligne sur 325
format .criteria-text « N. Libellé »    0 écart sur les 25
crochets […] de cloture                 101 avant, 101 après

AMBOSS  report_redundancy 147 (inchangé) · invariants / nomenclature / atteignabilité code 0
RESCOS  report_redundancy 127 (inchangé) · invariants / nomenclature / atteignabilité code 0
```

Les 25 items signalés par `check_no_loss` sont des réécritures sur place. Un
contrôle de couverture lexicale n'en isole que **deux** sous 0,85, et ce sont
exactement les deux corrections délibérées : « uniquement si dépression
respiratoire **sévère** » (flumazénil) et « **RSV** » remplacé par « VRS »
— ce dernier a été rétabli sous la forme « VRS (virus respiratoire syncytial,
RSV) » avant validation, pour ne pas perdre l'acronyme anglophone à la
recherche. **Aucun retrait plein.** Les seules disparitions assumées sont les
corrections d'erreur des § 4 et 5.

`check_nomenclature` n'a **rien** rattrapé cette fois — première fois en trois
lots. Il a néanmoins été lancé avant validation, comme demandé.

German et casecos n'ont été ni lus ni mesurés : l'utilisateur y travaille en
parallèle.
