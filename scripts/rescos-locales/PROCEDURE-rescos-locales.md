# Procédure — volet `cases/rescos-locales` (165 grilles)

Ce document est le volet `rescos-locales` de la procédure du projet. Il suppose
lus `scripts/amboss/PROCEDURE.md` (la méthode de référence) et
`scripts/rescos/PROCEDURE-rescos.md` (le portage dont celui-ci hérite
l'architecture). Il ne répète que ce qui **diffère**.

---

## 0. Ce que ce corpus a de radicalement différent

**Les grilles étaient autonomes.** Mesuré sur les 165, à l'inventaire (`l2`)
puis après la bascule du lot `l3` :

| | inventaire | aujourd'hui |
|---|---|---|
| `window.caseConfig` | **0 / 165** | **156 / 165** |
| `cases/scoring.js` | **0 / 165** | **156 / 165** |
| `calculateScores()` en ligne | **156 / 165** | **0 / 165** |
| `cases/case-styles.css` | 0 / 165 | **0 / 165** |
| `<style>` en ligne | 165 / 165 | **165 / 165** |

Les trois corpus précédents partageaient `cases/scoring.js`. Ici il y avait
**156 copies du moteur de calcul**, une par grille notée — une seule variante,
et la **même fourche périmée** que RESCOS-7 et RESCOS-9, avec les mêmes six
manques (§ 4). `apply_shared_engine.py` les a remplacées par le fichier
partagé ; le barème est transposé en `window.caseConfig`, verbatim.

**La mise en page, elle, reste locale** : 165 feuilles de style en ligne, aucun
`case-styles.css`. C'est délibéré — les 165 `<style>` *sont* la mise en page de
ce corpus, et la vérification a montré que toutes les classes manipulées par
`cases/scoring.js` (`score-0`…`score-max`, `lacune-*`, `note-*`,
`criteria-*-points`, `communication-note-*`, `timer-*`, `status-*`,
`revision-mode` / `exam-mode`, `has-content`, `missing-item`) y sont déjà
définies : **0 absence sur 156**. Seule exception, traitée : la barre de
navigation que `createNavBar()` construit désormais — ses quatre classes
étaient absentes des 156 (voir § 4).

**Les 9 grilles sans `calculateScores` sont les feuilles porte** — la consigne
remise au candidat devant la station (`<div class="feuille-porte">`). Elles ne
portent aucun critère, aucun `<input>`, aucun `<script>` : **elles n'ont pas de
barème, et c'est correct.** Elles ont néanmoins une entrée dans `BLOCKS`, sans
quoi leur contenu rédactionnel serait invisible à tout l'outillage.

---

## 1. L'outillage

Même architecture que `scripts/rescos/` : dossier autonome, qui **importe** de
`scripts/amboss/lib_amboss.py` ce qui ne dépend d'aucun corpus (`strip_base64`,
`visible_text` et son correctif du chevron nu, `norm`, `BULLET`,
`_bullet_items`, la table `BANNED`, la simulation `section_max` /
`orphan_criteria`) et **redéfinit** ce qui décrit le corpus (`CASES`, `BLOCKS`,
`CONTENT_CLASSES`, `grids()`, les bornes, `list_items()`).

| script | rôle | sortie |
|---|---|---|
| `lib_rescos_locales.py` | bornes, blocs, items | — |
| `snapshot_invariants.py` | écrit `baseline.json` | — |
| `check_invariants.py` | **porte** : gel du barème, des blocs, du moteur | 1 si divergence |
| `check_reachability.py` | **porte** : barème atteignable | 1 si écart |
| `check_nomenclature.py` | **porte** : termes non suisses | 1 si présents |
| `report_redundancy.py` | mesure de redondance | 0 |
| `report_import_defects.py` | mesure des défauts d'import | 0 |
| `check_no_loss.py` | items disparus depuis une référence | **toujours 0** |
| `browser_probe.js` | contrôle en navigateur (Node + Chrome) | 0 |
| `apply_shared_engine.py` | **transformation** : bascule sur `cases/scoring.js` | 0 |

Aucun `apply_lab_nomenclature.py` n'est fourni : une passe de nomenclature devra
en écrire un.

> **`check_no_loss.py` était aveugle sur les deux tiers du corpus.** Son
> `git diff --name-only` sans `-z` recevait `"…Polytraumatis\303\251…"` —
> guillemets et octets échappés par `core.quotepath` — pour tout nom accentué,
> et ces grilles étaient **silencieusement sautées**. 132 des 165 noms portent
> un accent. Symptôme mesuré au moment de la bascule : 156 grilles modifiées,
> **57 seulement examinées**. Corrigé par `-z` ; le contrôle en couvre
> désormais 156 sur 156.

### `check_reachability` — la décision d'architecture

`check_reachability` des trois corpus précédents rejoue `cases/scoring.js`. Ici,
**à l'inventaire**, chaque grille avait son moteur. Deux voies étaient ouvertes :

1. simuler le moteur de **chaque** grille — interpréter 156 programmes ;
2. **vérifier d'abord que les 156 moteurs sont équivalents à un modèle connu**,
   puis simuler ce modèle unique.

**Voie 2 retenue.** L'équivalence est un fait mesuré (une seule empreinte
SHA-256 sur 156, configuration masquée), et la voie 1 porterait le risque
qu'elle prétend écarter — un interpréteur JavaScript écrit en Python serait
lui-même un modèle non vérifié. La voie 2 transforme « sont-ils tous
pareils ? » en **précondition vérifiée à chaque passage** :
`engine_fingerprint()` est recalculée par grille et comparée à
`REFERENCE_ENGINE`. Une grille dont le moteur dérive d'un octet **échoue** ;
elle ne passe pas en silence.

L'empreinte est en outre **gelée au snapshot** (`engineFingerprint`), ce qui la
rend visible à `check_invariants` : sans cela, une modification de 35 800
caractères de JavaScript noyée dans un fichier de 170 000 ne se distinguerait
d'aucune retouche de contenu dans un `diff`.

**Depuis la bascule**, ce raisonnement ne porte plus que sur l'histoire du
corpus. Les 156 grilles chargent le fichier partagé ; leur `engineFingerprint`
vaut le marqueur `shared:cases/scoring.js` et non un SHA, parce que
`cases/scoring.js` est un fichier suivi par `git` dont toute modification
apparaît à son propre `diff` — c'est la situation des trois autres corpus. La
branche qui lit le moteur embarqué est **conservée** : elle décrit ce que le
corpus a porté, et c'est la seule chose qui distinguerait une grille réimportée
du vault d'une grille déjà basculée.

---

## 2. `BLOCKS` — douze blocs, deux inédits

Découpage par **équilibrage** des `<div>` (les 165 grilles sont globalement
équilibrées : 0 écart entre `<div` et `</div>`), avec une **queue attendue**
vérifiée par `bounds_anomalies()` sur tout le corpus.

| bloc | segments | grilles | remarque |
|---|---:|---:|---|
| `annexe-dd` | 132 | 123 | section notée, sauf RESCOS-48 (dans `annexes-grid`) |
| `redflags` | 58 | 58 | dans un `criteria-row` |
| `therapy` | 260 | 104 | dans un `criteria-row` |
| `cloture` | 398 | 134 | section « Clôture de consultation », non notée |
| `resume` | 59 | 59 | |
| `expert` | 127 | 127 | |
| `theorie` | 138 | 138 | |
| `presentation` | 57 | 57 | |
| `scenario` | 118 | 118 | exclu par défaut de la redondance |
| **`annexe-qr`** | **1** | **1** | **INÉDIT** |
| `annexe-image` | 109 | 46 | `annexe-item` nu |
| **`feuille-porte`** | **9** | **9** | **INÉDIT** |

**Les deux blocs inédits sont la leçon d'AMBOSS-34 appliquée.** `annexe-qr`
(« Pédiatrie — État fébrile sans foyer ») est une fiche questions/réponses sous
une classe que ni AMBOSS, ni German, ni RESCOS ne connaissent ; `feuille-porte`
couvre neuf **grilles entières**. Sans entrée dédiée, l'une et les autres
seraient invisibles, et le seul symptôme aurait été un chiffre de redondance
anormalement bas.

`CONTENT_CLASSES` est établie par **mesure**, sur deux critères vérifiés
programmatiquement (`lib._selftest_content_classes()`) :

1. la classe est à 100 % **dans** un segment de `BLOCKS` ;
2. son motif `class="[^"]*\bCLS\b[^"]*"` ne matche **aucun** attribut `class`
   hors bloc — le tiret est une frontière de mot, donc `\btext\b` matcherait
   `class="detail-text criteria-detail"`, c'est-à-dire la section notée.

**Cas limite documenté : `exemple-phrase`.** Jeton **mixte** — 537 occurrences
dans un bloc, **222 dehors** sur 29 grilles, logées dans un `criteria-row`
juste après le `details-with-checkboxes` d'un critère noté. Ce n'est pas un bloc
autonome mais une **feuille** : une annotation du critère, au même titre que
`patient-response`. Elle est donc **hors** de `CONTENT_CLASSES` (l'y mettre
ferait crier `uncovered_content()` sur 29 grilles saines) mais **dans**
`_DIV_ITEM_CLASSES` : ses items sont extraits là où elle tombe dans un bloc.

---

## 3. Les portes

```
python3 scripts/rescos-locales/check_invariants.py     # OK, 165 grilles
python3 scripts/rescos-locales/check_reachability.py   # OK, 156/156 à 100 %
python3 scripts/rescos-locales/check_nomenclature.py   # ÉCHEC, 368 termes
```

| porte | inventaire (`l2`) | après `l3` |
|---|---|---|
| `check_invariants` | OK, 165 | **OK, 165** |
| `check_reachability` | ÉCHEC, 1 grille | **OK, 156/156 à 100 %** |
| `check_nomenclature` | ÉCHEC, 368 termes | ÉCHEC, 368 termes |

`check_nomenclature` reste **rouge, et c'est le constat** : aucune passe de
nomenclature n'a encore été menée sur ce corpus.

### Barème défaillant — 1 grille — **réparé (lot `l3`)**

**`RESCOS-63 - Toux - Pédiatrie`** : deux sections seulement (`anamnese` 0.25,
`management` 0.25), **somme des coefficients = 0,5**. Le global plafonnait à
**50 %** grille parfaitement remplie, sans qu'aucune section ne soit en écart.

C'est un **cinquième mécanisme**, distinct des quatre déjà connus (critère hors
de la boucle · section vide pondérée · `count` trop grand · `maxScores` divergeant
du `<span>`). Les quatre contrôles précédents restaient muets ;
`coef_sum_anomaly()` le nomme. Confirmé indépendamment en navigateur : 50 %,
note E.

**Redistribution retenue : `anamnese` 0.5 · `management` 0.5**, et les deux
`section-header` passent de « (25%) » à « (50%) ».

Quatre faits l'imposent, et aucun ne dépend d'un jugement de contenu.

1. **La grille ne porte que deux sections réelles** — vérifié : deux
   `section-header`, deux `<span class="score">` (`anamneseScore` /29,
   `managementScore` /16), deux `id="…-percentage"`, et les seules entrées de
   la page sont `a1..a9` et `m1..m6`. Il n'y a pas de section examen ni
   communication à retrouver ; le défaut est la **somme**, pas un oubli.
2. **La déclaration exprimait déjà l'égalité** (0.25 = 0.25), et les deux
   en-têtes annonçaient le même « (25%) ». Mettre les deux à 0.5 est la seule
   correction qui rétablisse la somme **sans toucher au rapport voulu par
   l'auteur**.
3. **C'est la doctrine constante du corpus** : 155 des 156 grilles notées
   pondèrent à égalité, quel que soit leur nombre de points.
4. **Le prorata réintroduirait ce que le moteur neutralise.**
   `cases/scoring.js` calcule `(score / max) * 100` **par section** puis
   applique `coef` : chaque section est déjà ramenée à un pourcentage. Pondérer
   29 contre 16 compterait donc le nombre de points **deux fois**.

Le mécanisme d'origine se lit dans le voisinage : le gabarit du corpus est
`0.25 × 4` (« RESCOS-64 station double 2 » le porte encore, quatre sections
inédites à 0.25). RESCOS-63 en a supprimé deux sans remettre les coefficients à
l'échelle.

Après correction : `check_reachability` rend **100 %**, et le navigateur
confirme **100 %, note A**.

### Défaut de moteur — 156 grilles — **réparé (lot `l3`)**

Voir § 4. `check_reachability` ne le voyait pas et ne pouvait pas le voir : le
barème restait calculable, l'exception survenait **après** l'écriture des
scores. Seul `browser_probe.js` le détectait.

---

## 4. Le contrôle en navigateur — `browser_probe.js`

Trois campagnes ont écrit trois fois le même harnais dans un scratchpad de
session (préoccupation n° 4 de `r7-report.md`). Il est désormais **versionné**.

```
node scripts/rescos-locales/browser_probe.js --summary
node scripts/rescos-locales/browser_probe.js "RESCOS-63" --summary
node scripts/rescos-locales/browser_probe.js > rapport.json
```

Strictement local : serveur statique sur `127.0.0.1`, Chrome for Testing lancé
avec `--host-resolver-rules=MAP * ~NOTFOUND, EXCLUDE 127.0.0.1`, protocole
DevTools sur le WebSocket natif de Node 22. Aucun paquet installé.

**Passage complet, 165 grilles — avant et après la bascule du lot `l3` :**

| | avant | après |
|---|---|---|
| sans exception ni erreur | **9 / 165** (les 9 feuilles porte) | voir § 6 |
| à 100 % après remplissage | 155 / 156 notées | **156 / 156** |
| écrivant `ecos_registry` | **0 / 165** | **156 / 165** |
| exceptions `TypeError` | **13 446** | **0** |

**Avant : toutes les grilles notées levaient une exception, à chaque calcul.**
La cause : le moteur embarqué écrivait
`document.getElementById("missingItems").style.display` **sans garde**, et le
`<div id="missingItems">` est **commenté** dans les 156 grilles
(`<!-- ÉLÉMENTS MANQUANTS (MASQUÉS) -->` — vérifié hors commentaire HTML,
156/156). C'était le manque n° 1 de la liste ci-dessous, réalisé.

**Conséquence mesurée : aucun score de ce corpus ne remontait au tableau de
bord.** `ecos_registry` n'est écrit qu'à un seul endroit du projet,
`cases/scoring.js:saveToRegistry()` — absent des 156 copies. C'est ce qui rend
la preuve inverse concluante : la présence de ces 156 entrées après la bascule
ne peut venir que du chargement du moteur partagé.

### Ce qui manquait aux 156 moteurs, par rapport à `cases/scoring.js`

Exactement les six manques relevés par le lot r7 sur RESCOS-7 et RESCOS-9 :

1. la garde `if (missingEl)` ;
2. l'**appel** de `saveToRegistry()` ;
3. la **définition** de `saveToRegistry()` ;
4. le chargeur dynamique de `srs.js` ;
5. la détection du mode circuit et le retour à `exam.html` en fin de minuteur ;
6. `createNavBar()` / `createCircuitNav()`.

**La boucle de calcul, elle, était identique ligne pour ligne.** C'est ce qui
autorisait la voie 2 du § 1, et ce qui rendait la bascule sans risque.

### La bascule — `apply_shared_engine.py`

Voie retenue, celle de r7 : **faire charger `cases/scoring.js`** plutôt que
reporter six corrections dans 156 copies, ce qui reconduirait le mécanisme de
dérive que ce défaut réalisait déjà. Le script remplace le premier des deux
`<script>` en ligne — celui du moteur — par un `<script>` de configuration et
`<script src="../scoring.js"></script>`. Le second `<script>` (l'appel final à
`colorPatientResponses()`) est laissé intact, comme dans RESCOS-7 et RESCOS-9.

**Le barème est transposé, pas recalculé.** Forme déclarative (154 grilles) :
les trois membres droits sont repris **verbatim**. Forme impérative (RESCOS-63
et « RESCOS-64 station double 2 », exactement la forme de RESCOS-7 et
RESCOS-9) : reconstruite dans l'ordre des `push`. **Vérification** : pour
chacune des 156, `parse_config()` rend le **même quadruplet** avant et après —
`maxScores`, `coef`, `sectionInfo` (clé, préfixe, `count`, `scoreId`, `isComm`)
et dénominateurs affichés. 0 divergence.

**Trois points que RESCOS-7/9 ne posaient pas, vérifiés ici :**

1. **Chemin relatif.** `cases/rescos-locales/` est à deux niveaux sous la
   racine, comme `cases/rescos/` : `../scoring.js` résout sur
   `cases/scoring.js`, `../srs.js` (chargeur dynamique) sur `cases/srs.js`, et
   les `../../index.html` / `../../exam.html` que le moteur construit résolvent
   sur la racine du dépôt.
2. **CSS en ligne.** Les classes que `cases/scoring.js` manipule sont **toutes
   définies** dans les 165 `<style>` — 0 absence sur 156, mesurée classe par
   classe. Ni `case-styles.css`, ni `persistence.js`, ni `theme-sync.js` ne
   sont ajoutés : aucun des six manques ne les concerne.
3. **Collision du minuteur.** `createNavBar()` insère une barre en
   `position: fixed; top: 20px; left: 20px` — la place exacte qu'occupait
   `.timer-container` dans les 156 feuilles de style en ligne (156/156 à
   `top: 20px`). `cases/case-styles.css` avait déjà résolu la même collision
   pour les trois autres corpus en déplaçant le minuteur à `top: 70px` ; le
   script recopie ce geste, et y ajoute les règles `.case-nav-bar` (absentes
   des 156, donc sans écrasement possible).

**Les 9 feuilles porte ne sont pas touchées** : 0 critère, 0 `<input>`,
0 `<script>` — elles n'ont pas de barème, et c'est correct.

---

## 5. Mesures initiales

| | AMBOSS (40) | German (88) | RESCOS (41) | **rescos-locales (165)** |
|---|---:|---:|---:|---:|
| poids hors base64 | — | — | 3,8 Mo | **27,1 Mo** |
| redondance inter-blocs | 147 | 14 | 127 | **1258** |
| redondance intra-bloc | — | — | — | **633** |
| par grille | 3,7 | 0,2 | 3,1 | **7,6** |
| termes non suisses | 0 | 0 | 0 | **368 / 103 grilles** |

Couples de blocs les plus redondants : `presentation ↔ resume` 311,
`presentation ↔ theorie` 245, `annexe-dd ↔ presentation` 194,
`expert ↔ presentation` 127. **`presentation` est des deux côtés des quatre
premiers couples** : c'est là que se concentre la recopie.

Volume pédagogique : 1466 segments de bloc, 132 `annexe-dd`, 398 `cloture`,
260 `therapy` — la clôture est le bloc le plus fréquent après les fiches.

---

## 6. Caractérisation du corpus

**Ossature interne des blocs : identique à AMBOSS et RESCOS.** Là où `resume`
existe, il porte toujours les quatre mêmes sections (`section-anamnese`,
`-examen`, `-management`, `-keypoints`) ; là où `presentation` existe, toujours
les cinq mêmes (`checklist`, `longue`, `express`, `mnemo`, `questions`) plus le
`mnemo-box` ; `theorie` porte toujours `rappels` + `examens`. Seule la
**couverture** diffère : 36 % des grilles ont un `resume` / une `presentation`,
contre ~60 % dans AMBOSS et RESCOS.

**`annexe-dd` : arguments réels, comme AMBOSS et RESCOS — pas du remplissage.**

| | grilles à `annexe-dd` | items | médiane | items < 30 car. | remplissage |
|---|---:|---:|---:|---:|---:|
| AMBOSS | 40 | 1214 | 40 car. | 23,1 % | 0,1 % |
| RESCOS | 22 | 590 | 34 car. | 35,8 % | 0,2 % |
| **rescos-locales** | **123** | **2186** | **35 car.** | **33,6 %** | **0,3 %** |

**Aucune passe de nettoyage `annexe-dd` n'est nécessaire.** Le corpus est dans
le registre de RESCOS, pas dans celui de German (« À évaluer cliniquement »,
examens génériques). Nuance à retenir : la forme *structurée* du différentiel
(`arg-title` / `reponse-pour` / `reponse-contre`) n'est présente que sur
**40 grilles sur 123** (24 % du corpus, contre 55 % dans AMBOSS et RESCOS) ;
les 83 autres énumèrent leurs arguments en puces simples.

**Défauts d'import : aucun des défauts durs.** Les deux signatures exactes de la
moulinette d'AMBOSS (`plage-coupee`, `troncature-x-fragment` réel) sont à
**zéro**. Voir l'en-tête de `report_import_defects.py` pour le tableau à quatre
corpus. Seul défaut réel : **8 numérations en unité implicite** sur 6 grilles,
dont 6 vraies (« GB 18000 », « plaquettes > 50 000 »). Les 787 `chevron-nu` sont
des **seuils légitimes**, pas un défaut — c'est l'inventaire de ce qu'un
`re.sub(r'<[^>]+>', …)` naïf détruirait.

**Un défaut d'import propre à ce corpus, non listé par AMBOSS : 92 références
d'image mortes.** 75 pointent un chemin **absolu du poste de l'auteur**
(`/Users/…/Documents/-Medecine/…`), 17 un chemin relatif (`bbn/…`,
`decision-partagee/…`) sans fichier dans le dépôt. Mesuré au 404 dans le
navigateur, sur 40 grilles. Seules 11 images du corpus sont en base64 — toutes
dans les grilles numérotées.

### Les 33 grilles numérotées RESCOS-41 à 69

Elles se distinguent nettement des 132 thématiques, et par **inversion de
profil** :

| | RESCOS-41…69 (33) | thématiques (132) |
|---|---:|---:|
| `expert` | **94 %** | 73 % |
| `scenario` | **97 %** | 65 % |
| `theorie` | 88 % | 83 % |
| `cloture` | 39 % | **92 %** |
| `therapy` | 30 % | **71 %** |
| `annexe-dd` | 48 % | **81 %** |
| `redflags` | 12 % | **41 %** |
| critères / grille | 22,5 | 18,5 |
| images base64 | **11** | 0 |

Les numérotées sont **« fiche-lourdes »** (pédagogie de fin de page quasi
universelle) ; les thématiques sont **« clôture-lourdes »** (commentaire dans la
section notée). Le barème est en revanche uniforme : 31/33 et 123/132 emploient
les mêmes quatre sections `anamnese / examen / management / communication`.

### RESCOS-69 — deux vignettes distinctes — **suffixé (lot `l3`)**

| | `… - Basketteur 25 ans - …` | `… - Traumatisme MS - …` |
|---|---:|---:|
| taille à l'inventaire | 180 435 o | 174 707 o |
| critères | 25 | 26 |
| items de contenu | 137 | 110 |

**3 items en commun**, 134 propres au premier, 106 au second. Ce ne sont **pas**
deux versions d'un même fichier : ce sont **deux vignettes cliniques
différentes** partageant le même thème (traumatisme du membre supérieur, même
patient « M/Mme Norton, 25 ans »). La seconde développe un volet médico-légal
absent de la première.

Le problème était **fonctionnel** : `saveToRegistry()` indexe le registre sur le
**nom de fichier**, débarrassé de son `.html`. Deux vignettes différentes sous
le même nom se seraient écrasées l'une l'autre dès la bascule du § 4.

**Renommé : `RESCOS-69 - Traumatisme MS - Basketteur 25 ans` →
`RESCOS-69b - …`.** C'est l'autre fichier qui garde le numéro nu, sur deux
faits :

* il porte la **forme canonique** `RESCOS-NN - Thème - Grille ECOS`, celle de
  RESCOS-65 à 68 — c'est celui que la numérotation désigne ;
* le précédent exact du projet est `cases/rescos/` : `RESCOS-9 - Boiterie
  pédiatrique` et `RESCOS-9b - Boiterie pédiatrique - Fillette de 2 ans`. Le
  fichier qui **ajoute un descripteur de patient** prend le suffixe.

Le suffixe est porté aux **trois endroits** où le corpus le porte, vérifié sur
`57b` et `58b` : nom de fichier, `<title>`, `<h1>`. Aucune autre occurrence de
`RESCOS-69` ne subsiste dans le fichier. Le renommage passe par `git mv`
(rename détecté, `R`), et les 12 champs du snapshot sont **identiques sous le
nouveau nom** : seule la clé change. 137 items avant, 137 après, 0 disparu.

### Une duplication réelle, mesurée et **non traitée**

**`Fièvre et douleurs articulaires - Infection gonococcique disséminée`
⊂ `RCI-Fièvre et douleurs articulaires - Infection gonococcique disséminée`** —
inclusion stricte : **0 item propre** à la première (106 items, tous retrouvés
dans la seconde), 85 propres à la seconde (203 items, 197 308 o contre
162 548 o). Ce n'est pas un doublon de nom mais un doublon de **contenu** : la
version `RCI-` est un enrichissement de l'autre. Arbitrer une suppression de
grille est un geste éditorial, hors du mandat de réparation technique.

### Deux autres paires suspectes, mesurées

* **`Mal au dos — Guillain-Barré (1)`** vs sans `(1)` : 18 items communs, 85 et
  178 propres. Deux versions divergentes, pas une copie. À arbitrer.
* **`Céphalées — Exemple station ECOS B3`** vs **`Céphalées — Vignette clinique`** :
  **0 item commun**. Deux stations distinctes malgré le thème partagé.

---

## 7. Ce que ce volet n'a pas fait

- **Aucune modification sous `cases/`.** Le corpus est à `7c77e3e`.
- **Rien sous `cases/german/` ni `scripts/german/`** : ni écrit, ni importé.
  C'est la raison pour laquelle les sept familles de `report_import_defects.py`
  sont **reconstruites** ici plutôt qu'importées, et pourquoi les tables
  `EXTRA` / `MICROBIO` / `ANGLICISMES` sont **copiées** de `scripts/rescos/`
  plutôt qu'importées (l'étoile, pas la chaîne). Les grilles de `cases/german/`
  n'ont été que **lues**, pour le bordage des motifs sur quatre corpus.
- **Aucune correction de nomenclature, de barème ni de moteur.**
- **Aucune lecture de grille entière avec `Read`** : tout passe par
  `strip_base64` puis `block_spans` / `visible_text` / `list_items`.
- **Aucune commande réseau, aucun `git push`, aucun `git gc` ni `git prune`.**

## 8. Témoins — inchangés

| | avant | après |
|---|---|---|
| AMBOSS `report_redundancy` | **147** | **147** |
| RESCOS `report_redundancy` | **127** | **127** |
| AMBOSS invariants / nomenclature / atteignabilité | code 0 | code 0 |
| RESCOS invariants / nomenclature / atteignabilité | code 0 | code 0 |
