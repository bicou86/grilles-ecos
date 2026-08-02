# Procédure — volet `cases/rescos-locales` (165 grilles)

Ce document est le volet `rescos-locales` de la procédure du projet. Il suppose
lus `scripts/amboss/PROCEDURE.md` (la méthode de référence) et
`scripts/rescos/PROCEDURE-rescos.md` (le portage dont celui-ci hérite
l'architecture). Il ne répète que ce qui **diffère**.

---

## 0. Ce que ce corpus a de radicalement différent

**Les grilles sont autonomes.** Mesuré sur les 165 :

| | |
|---|---|
| `window.caseConfig` | **0 / 165** |
| `cases/scoring.js` | **0 / 165** |
| `cases/case-styles.css` | **0 / 165** |
| `<style>` en ligne | **165 / 165** |
| `calculateScores()` en ligne | **156 / 165** |

Les trois corpus précédents partageaient `cases/scoring.js`. Ici il y a
**156 copies du moteur de calcul**, une par grille notée, et 165 feuilles de
style en ligne. Toute intervention sur le comportement d'une grille est locale
à cette grille ; aucune correction centrale n'est possible en l'état.

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

Aucun `apply_lab_nomenclature.py` n'est fourni : ce volet **mesure**, il ne
corrige pas. Une passe de nomenclature devra en écrire un.

### `check_reachability` — la décision d'architecture

`check_reachability` des trois corpus précédents rejoue `cases/scoring.js`. Ici
chaque grille a son moteur. Deux voies étaient ouvertes :

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

## 3. Les portes — état au moment de l'inventaire

```
python3 scripts/rescos-locales/check_invariants.py     # OK, 165 grilles
python3 scripts/rescos-locales/check_reachability.py   # ÉCHEC, 1 grille
python3 scripts/rescos-locales/check_nomenclature.py   # ÉCHEC, 368 termes
```

`check_invariants` est vert par construction (le baseline vient d'être écrit) ;
`check_reachability` et `check_nomenclature` sont **rouges, et c'est le
constat** : rien n'a encore été corrigé dans ce corpus.

### Barème défaillant — 1 grille

**`RESCOS-63 - Toux - Pédiatrie`** : deux sections seulement (`anamnese` 0.25,
`management` 0.25), **somme des coefficients = 0,5**. Le global plafonne à
**50 %** grille parfaitement remplie, sans qu'aucune section ne soit en écart.

C'est un **cinquième mécanisme**, distinct des quatre déjà connus (critère hors
de la boucle · section vide pondérée · `count` trop grand · `maxScores` divergeant
du `<span>`). Les quatre contrôles précédents restent muets ; `coef_sum_anomaly()`
le nomme. Confirmé indépendamment en navigateur : 50 %, note E.

### Défaut de moteur — 156 grilles

Voir § 4. `check_reachability` ne le voit pas et ne peut pas le voir : le barème
reste calculable, l'exception survient **après** l'écriture des scores.

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

**Passage complet, 165 grilles :**

| | |
|---|---|
| sans exception ni erreur | **9 / 165** (les 9 feuilles porte) |
| à 100 % après remplissage | **155 / 156** notées |
| écrivant `ecos_registry` | **0 / 165** |
| exceptions `TypeError` | **13 446** |

**Toutes les grilles notées lèvent une exception, à chaque calcul.** La cause :
le moteur embarqué écrit `document.getElementById("missingItems").style.display`
**sans garde**, et le `<div id="missingItems">` est **commenté** dans les 156
grilles (`<!-- ÉLÉMENTS MANQUANTS (MASQUÉS) -->`). C'est le manque n° 1 de la
liste ci-dessous, réalisé.

**Conséquence : aucun score de ce corpus ne remonte au tableau de bord.**
`ecos_registry` n'est écrit qu'à un seul endroit du projet,
`cases/scoring.js:saveToRegistry()` — absent des 156 copies.

### Ce qui manque aux 156 moteurs, par rapport à `cases/scoring.js`

Exactement les six manques relevés par le lot r7 sur RESCOS-7 et RESCOS-9 :

1. la garde `if (missingEl)` ;
2. l'**appel** de `saveToRegistry()` ;
3. la **définition** de `saveToRegistry()` ;
4. le chargeur dynamique de `srs.js` ;
5. la détection du mode circuit et le retour à `exam.html` en fin de minuteur ;
6. `createNavBar()` / `createCircuitNav()`.

**La boucle de calcul, elle, est identique ligne pour ligne.** C'est ce qui
autorise la voie 2 du § 1.

**Voie de réparation recommandée**, par cohérence avec l'arbitrage de r7 : faire
charger `cases/scoring.js` aux 156 grilles et transposer leur configuration en
`window.caseConfig`. Un report des six corrections dans 156 copies reconduirait
le mécanisme de dérive. **Non fait par ce lot** : il ne modifie aucune grille.

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

### RESCOS-69 — deux fichiers, deux vignettes distinctes

| | `… - Basketteur 25 ans - …` | `… - Traumatisme MS - …` |
|---|---:|---:|
| taille | 180 435 o | 174 707 o |
| critères | 25 | 26 |
| items de contenu | 137 | 110 |

**3 items en commun**, 134 propres au premier, 106 au second. Ce ne sont **pas**
deux versions d'un même fichier : ce sont **deux vignettes cliniques
différentes** partageant le même thème (traumatisme du membre supérieur). La
seconde développe un volet médico-légal absent de la première (« documentation
photographique pour dossier médico-légal », « services d'aide aux victimes »).

**Conclusion : deux stations, pas une duplication.** Elles ont besoin d'un
suffixe distinctif, comme `57b` et `58b` — sinon `saveToRegistry()`, qui
indexe le registre sur le **nom de fichier**, les distinguera par un libellé que
rien ne relie à leur contenu.

### Trois autres paires suspectes, mesurées

* **`Fièvre et douleurs articulaires…` ⊂ `RCI-Fièvre et douleurs articulaires…`**
  — **inclusion stricte** : 105 items communs, **0 propre** à la première, 96
  propres à la seconde. La version `RCI-` est un enrichissement de l'autre.
  **C'est une duplication** ; la première est superflue.
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
