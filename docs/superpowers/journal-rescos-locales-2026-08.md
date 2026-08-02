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
