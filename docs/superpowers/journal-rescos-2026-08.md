# Journal de refonte — grilles RESCOS

Corpus : `cases/rescos`, 41 grilles. Outillage : `scripts/rescos/`.
Procédure : `scripts/rescos/PROCEDURE-rescos.md`, volet du
`scripts/amboss/PROCEDURE.md`.

Pendant des `journal-amboss-2026-07.md` et `journal-german-2026-08.md`, dont il
reprend le format. Deux types d'entrées :

- **Modification** — un changement appliqué, avec ce qui le justifie.
- **Divergence** — un écart repéré mais **non corrigé**, laissé à l'arbitrage.

## Format

    ### <passe ou grille> — <motif>

    **Modifications**
    - <bloc> · <sujet> : « <avant> » → « <après> »
      source : <référentiel — citation>

    **Divergences consignées**
    - <zone> · <sujet> : la grille dit « <x> » — non corrigé (<raison>)

## Entrées

### Volet A — Passe nomenclature suisse (tâche r2)

Mesure de départ, `check_nomenclature.py` au commit `a82e036` : **111 termes non
suisses sur 28 grilles** — 104 `NFS`, 4 `mg/dL`, 2 `g/dL`, 1 `/mm³`. Après la
passe, **0** (code de sortie 0). S'y ajoute **1 numération en unité implicite**,
seul défaut d'import réel du corpus, traité dans la même passe : **112
modifications** au total.

Script : `scripts/rescos/apply_lab_nomenclature.py`, écrit pour ce corpus.
`scripts/amboss/apply_lab_nomenclature.py` n'est **pas** modifié — il a produit
les mesures publiées d'AMBOSS — ni réutilisé tel quel : RESCOS ne porte ni
`CBC`, ni `BMP`, ni `911`, ni `SAMU`, ni `ng/mL`, ni `pg/mL`, ni nom de marque
américaine. Le principe est repris : substitution 1 pour 1, **hors zones
base64** (`data:image[^"]*` mis de côté avant toute substitution), aucune
modification de structure, donc aucun sous-item noté touché.

Le découpage base64 n'est pas une précaution de principe : l'alphabet base64
contient `+`, `/` et `=`, qui sont des frontières de mot, si bien que `\bNFS\b`
**peut** tomber dans un blob d'image.

**Contrôle préalable au remplacement** — exigé parce que `cases/scoring.js:159`
découpe `.criteria-text` par `.split(". ")[1].split(" [")[0]` : recherche de
`\bNFS\b` dans tout attribut `data-criteria` et dans tout élément
`.criteria-text` des 41 grilles → **0 occurrence** dans l'un comme dans l'autre.
Le remplacement ne peut donc pas déplacer le libellé qu'affiche la liste des
items manquants.

**Modifications**

- global · laboratoire : « NFS » → « **FSC** », 104 occurrences dans 28 grilles
  (RESCOS-1 ×3, 2 ×4, 3 ×3, 4 ×2, 5 ×2, 6 ×6, 9 ×2, 9b ×2, 14 ×5, 15 ×7,
  17 ×4, 18 ×6, 19 ×7, 20 ×6, 21 ×5, 22 ×6, 23 ×6, 24 ×4, 25 ×7, 27 ×1,
  28 ×3, 29 ×2, 31 ×2, 35 ×1, 36 ×1, 37 ×1, 38 ×5, 39 ×1).
  source : nomenclature suisse de laboratoire — formule sanguine complète ;
  même table `BANNED` que les corpus AMBOSS et German, importée et non recopiée.

- RESCOS-5 · unités (`resume`, prise en charge du choc hémorragique) :
  « culots globulaires si Hb <7 g/dL » → « **Hb <70 g/L** ».
  analyte : hémoglobine — g/dL → g/L, **× 10**.
- RESCOS-14 · unités (`resume`, critères de colite aiguë sévère) :
  « fièvre > 38 °C, FC > 90 bpm, Hb < 10.5 g/dL » → « **Hb < 105 g/L** ».
  analyte : hémoglobine — g/dL → g/L, **× 10**.
- RESCOS-9b · unités (`resume`, biologie de l'arthrite septique) :
  « hyperleucocytose (> 12 000/mm³) » → « **hyperleucocytose (> 12 G/L)** ».
  analyte : leucocytes — /mm³ → G/L, **× 0,001**. La même grille écrivait déjà
  « Leucocytes > 12 G/L » deux fois ailleurs : la conversion **aligne** les
  trois écritures au lieu d'en opposer deux.
- RESCOS-36 et RESCOS-37 · unités (`resume`, prévention secondaire de
  l'angor) : « objectif LDL < 70 mg/dL, voire < 55 mg/dL si haut risque » →
  « objectif LDL < **1.8 mmol/L**, voire < **1.4 mmol/L** si haut risque ».
  analyte : **cholestérol LDL** — mg/dL → mmol/L, **÷ 38,67**. Ce sont les deux
  cibles ESC (1,8 et 1,4 mmol/L), retrouvées à l'arrondi près.
- RESCOS-3 · numération implicite (`expert`, bilan de la maladie de Horton) :
  « ici VS 55, CRP 32, Hb 113, plaquettes 422 » → « …, **plaquettes 422 G/L** ».
  source : la même grille écrit `[Hb 113 g/L, plaquettes 422 G/L]` dans la
  `patient-response` du critère correspondant — la mention abrégée en était la
  seule sans unité.

**Le piège des deux valeurs sur la même ligne, payé deux fois sur AMBOSS,
s'est effectivement présenté** : les deux lignes LDL portent **deux** seuils
dans la même unité. Une règle qui n'aurait remplacé que l'unité aurait converti
le premier et laissé le second, produisant « LDL < 1.8 mmol/L, voire
< 55 mg/dL ». Les règles littérales de `apply_lab_nomenclature.py` couvrent la
**clause entière** et exigent exactement **une** occurrence par grille : si la
clause bouge, le script échoue au lieu de convertir à moitié.

**Le piège du mauvais facteur s'est présenté aussi** : le brief annonçait la
créatinine (× 88,4) pour les `mg/dL`. L'analyte réel est le **LDL**. Appliquer
88,4 aurait produit « LDL < 6187 µmol/L ». C'est la raison pour laquelle les
conversions sont littérales, grille par grille, et non un motif d'unité.

**Qualificatifs voisins** — relus après conversion : « hyperleucocytose
(> 12 G/L) » reste une hyperleucocytose ; « Hb < 105 g/L » reste un critère de
sévérité ; « Hb <70 g/L » reste un seuil transfusionnel.

**Balayage des numérations sans unité** — le corpus a été balayé avec le
vocabulaire élargi demandé (leucocytes, leucocytose, hyperleucocytose, GB,
globules blancs, plaquettes, thrombocytes, thrombopénie, PNN, polynucléaires,
neutrophiles, lymphocytes, éosinophiles, monocytes, basophiles, granulocytes,
PLT) : **9 voisinages nombre/terme d'hémogramme**, dont **un seul** en unité
implicite (RESCOS-3). Les huit autres sont légitimes — deux « Leucocytes
> 12 G/L », un « hyperleucocytose > 10 G/L », un « plaquettes 422 G/L » déjà
unité, une thrombocytose exprimée en pourcentage de patients, un ratio
transfusionnel « plasma/plaquettes : 1:1:1 ».

**Divergences consignées**

- brief · localisation : la numération implicite était annoncée dans
  **RESCOS-10** ; elle est en réalité dans **RESCOS-3** (Amaurose / Horton).
  RESCOS-10 (Céphalée / thrombose veineuse cérébrale) ne contient aucune
  numération, ses occurrences de « thrombo… » désignent toutes la thrombose
  veineuse. Corrigé de fait par le balayage, consigné ici parce que la mesure
  du brief était fausse, pas le défaut.
- RESCOS-3 · `expert` : sur la même ligne, « VS 55 », « CRP 32 » et « Hb 113 »
  sont eux aussi sans unité — non corrigé. Ce ne sont pas des numérations
  d'hémogramme, aucun contrôle du corpus ne les couvre, et la valeur y est
  citée en rappel d'une réponse patient qui, elle, porte les unités. À
  arbitrer si l'on veut homogénéiser la ligne entière.

**Table `BANNED` — deux motifs ajoutés, bordés avant activation**

Ajoutés dans `scripts/rescos/check_nomenclature.py` (jamais dans
`scripts/amboss/` : c'est ce corpus qui a fait apparaître le manque, et le
volet RESCOS s'interdit d'écrire dans les dossiers des corpus précédents). Les
deux reposent sur une liste de termes d'hémogramme **élargie aux formes
cliniques du résultat** — c'est précisément le manque qui avait laissé passer
« éosinophiles > 300/µL » sur AMBOSS-19.

1. `numeration-implicite` — terme d'hémogramme suivi d'un nombre nu.
   Bordage mesuré : **1 hit avant la passe** (RESCOS-3), **0 sur AMBOSS**,
   **0 sur German**, **0 sur RESCOS après**.
   - seuil `\d{3,}` et non `\d{2,}`, **par mesure** : à deux chiffres le motif
     attrape « CRP > 20 mg/L, hyperleucocytose (> 12 000/mm³) » de RESCOS-9b —
     il capture « 12 », recule devant « 000/mm³ » et déclare nue une valeur dont
     l'unité est deux caractères plus loin. Un faux positif dans une porte
     **bloquante** coûte plus cher qu'un « plaquettes 45 » hypothétique que le
     corpus ne contient pas ; c'est aussi le seuil de la famille homonyme de
     `scripts/german/report_import_defects.py`, donc les deux mesures restent
     comparables.
   - garde-fou d'année `(?!(?:19|20)\d\d\b)`, ajouté après avoir vu
     « plaquettes en 2019 » déclencher le motif nu. **C'est la leçon du
     `\b112\b` d'AMBOSS transposée** : un motif numérique trop large finit par
     rencontrer un nombre qui n'est pas une valeur de laboratoire.
   - lookahead négatif d'unités, qui borne l'autre côté : sans lui,
     « leucocytes (norme 4-10 G/L), CRP 120 mg/L » comptait pour une numération
     nue parce que le nombre suivant portait une unité absente de la liste.
2. `/µL` à termes étendus — 0 hit sur RESCOS. Contrôle essentiel : la
   numération de LCR « PL : GR 50 000 /µL », **seule écriture correcte** de ce
   cas, n'est pas attrapée — `GR` est délibérément absent de la liste, comme
   dans la règle d'AMBOSS qu'elle élargit.

**Vérifications après le volet A**

| contrôle | avant | après |
|---|---|---|
| `check_nomenclature.py` | 111 (112 avec `EXTRA`) | **0**, code 0 |
| `check_invariants.py` | OK 41/41 | **OK 41/41** |
| `report_import_defects.py` · `numeration-implicite` | 1 | **0** |
| `report_redundancy.py` | 610 paires | **610 paires** |
| `check_no_loss.py a82e036` | — | **0 item disparu** sur 28 grilles |
| balises appariées + `</html>` final | 41/41 | **41/41** |
| AMBOSS · nomenclature / invariants / redondance | 0 · OK · 147 | **0 · OK · 147** |

### Volet B — Le barème de RESCOS-12 et RESCOS-13 (tâche r2)

**Le défaut.** Ces deux grilles (crise de panique, dépression) déclarent une
section « Examen clinique » **vide** — `count: 0`, `maxScores.examen: 0`,
« Score : 0/0 », aucun `criteria-row` dans la page — tout en lui laissant son
**coefficient 0,25**. `cases/scoring.js` calcule
`const percentage = max > 0 ? (score / max) * 100 : 0` : le pourcentage de
cette section vaut 0 quoi que fasse le candidat, et
`globalPercentage += percentage * coef[key]` en perd le quart.
**Un étudiant qui remplit parfaitement l'une de ces deux grilles plafonnait à
75 %**, avec la note globale C au lieu de A.

Le défaut passait les trois écarts déjà détectés (`count` trop grand,
sous-item orphelin, `maxScores` divergeant du `<span>`) sans bruit — pour la
section vide, 0 == 0 == 0 — et n'était visible que par le total global.

|  | anamnese | examen | management | communication |
|---|---|---|---|---|
| RESCOS-12 `maxScores` | 48 | **0** | 8 | 20 |
| RESCOS-13 `maxScores` | 36 | **0** | 22 | 20 |
| `coef` avant (les deux) | 0.25 | **0.25** | 0.25 | 0.25 |
| `coef` après (les deux) | **1/3** | **retiré** | **1/3** | **1/3** |

#### Décision : répartition ÉGALE, et pourquoi

Les deux répartitions proposées étaient défendables ; la mesure du corpus
tranche.

**1. Le corpus pondère les sections à égalité, indépendamment de leurs
points.** Sur les 39 grilles à `caseConfig`, **39 portent exactement**
`{anamnese: 0.25, examen: 0.25, management: 0.25, communication: 0.25}` — une
seule distribution, sans exception, alors que les `maxScores` varient du simple
au sextuple d'une section à l'autre (RESCOS-12 : anamnèse 48 points,
management 8 — même poids, 25 %). L'égalité des coefficients est donc une
**décision de barème**, pas un accident.

**2. `scoring.js` est construit pour que le nombre d'items ne pèse pas.** Il
normalise d'abord chaque section en pourcentage (`score / max * 100`), *puis*
applique le coefficient. Le nombre de cases à cocher est ainsi neutralisé par
construction. Une répartition **proportionnelle aux points réintroduirait
exactement la quantité que le moteur a été écrit pour neutraliser** : la
pondération d'une grille dépendrait alors du nombre de lignes que son auteur a
tapées.

**3. Elle rendrait les deux grilles incomparables entre elles.** Au prorata,
l'anamnèse vaudrait **63 %** de la note dans RESCOS-12 et **46 %** dans
RESCOS-13, le management **10,5 %** puis **28 %** — deux stations du même
registre (consultation psychiatrique sans examen physique), notées selon deux
échelles différentes, pour la seule raison que la seconde a plus de critères
de management. Rien de pédagogique ne justifie cet écart.

**4. Le précédent du corpus va dans le même sens.** Les deux grilles à barème
impératif, seules à ne pas avoir quatre sections, portent des coefficients
**ronds et manifestement choisis à la main** : RESCOS-7 (communication seule)
`coef 1` ; RESCOS-9 (anamnèse 41 pts, management 15 pts) `0.7 / 0.3` — et non
`0.732 / 0.268`, valeur qu'aurait donnée le prorata. Le corpus ne dérive jamais
ses coefficients de ses points.

Retenu : **1/3 sur chacune des trois sections restantes**, écrit
`0.3333333333333333` (le double le plus proche de 1/3).

#### Ce que `scoring.js` attend, vérifié

- **La somme des coefficients doit valoir 1** : `globalPercentage` est une
  somme de `pourcentage × coef` où chaque pourcentage plafonne à 100. Mesuré :
  `0.3333333333333333 × 3 = 1.0` **exactement** en IEEE 754 — la somme est
  juste au bit près.
- **Les arrondis absorbent le résidu.** L'accumulation réelle
  (`globalPercentage += 100 * coef`, trois fois) donne
  **99.99999999999999**, et non 100 : l'ordre des opérations diffère de la
  somme des coefficients. Trois consommateurs, trois fois sans conséquence :
  - `Math.round(globalPercentage)` → **100**, affiché « 100 % » ;
  - `getClass(globalPercentage)` teste `p >= 90` → **note A** ;
  - `saveToRegistry` stocke `Math.round(globalPercentage)` → **100**.
  Aucune comparaison `=== 100` n'existe dans `cases/*.js` — vérifié : le résidu
  n'a nulle part où faire de dégât.
- `check_reachability.py` calcule `round(global_pct * 100)` et exige 100 :
  **100**.

#### Preuve — simulation du remplissage complet

Simulation en Node de la boucle des pourcentages de `cases/scoring.js`,
recopiée **texte pour texte**, alimentée par les `caseConfig` réellement
présentes dans les fichiers et par les maxima **lus dans le DOM** (pas les
maxima déclarés) :

    RESCOS-12 — Crise de panique
       anamnese       rempli=48  max=48  affiché=/48  -> 100 % x coef 0.3333333333333333
       management     rempli=8   max=8   affiché=/8   -> 100 % x coef 0.3333333333333333
       communication  rempli=20  max=20  affiché=/20  -> 100 % x coef 0.3333333333333333
       somme des coef        = 1
       globalPercentage brut = 99.99999999999999
       affiché totalScore    = 100%
       note globale          = A

    RESCOS-13 — Dépression
       anamnese       rempli=36  max=36  affiché=/36  -> 100 % x coef 0.3333333333333333
       management     rempli=22  max=22  affiché=/22  -> 100 % x coef 0.3333333333333333
       communication  rempli=20  max=20  affiché=/20  -> 100 % x coef 0.3333333333333333
       somme des coef        = 1
       globalPercentage brut = 99.99999999999999
       affiché totalScore    = 100%
       note globale          = A

`check_reachability.py` confirme indépendamment : **41/41**, dont RESCOS-12 et
RESCOS-13 à **100 %** (75 % avant).

#### La section vide à l'affichage — elle NE disparaît PAS toute seule

Retirer `examen` de `sectionInfo` la retire du **calcul**, pas de la **page** :
son `<div class="section">` est du HTML statique et `scoring.js` ne masque
aucune section. Sans geste supplémentaire, la grille corrigée aurait continué
d'afficher **« Examen clinique (25%) — Score : 0/0 »** et une tuile
**« Examen clinique / 0 % »** dans le panneau des pourcentages, désormais
**morte** : `examen-percentage` n'étant plus mis à jour par personne, elle
serait restée à 0 % à vie. Un étudiant y aurait lu la perte d'un quart de sa
note — exactement le malentendu que la correction supprime.

Trois gestes de plus ont donc été faits, sur chacune des deux grilles :

- l'intitulé « Examen clinique (25%) » devient
  **« Examen clinique — section non cotée »** ;
- le `<span class="score">Score : <span id="statusScore">0</span>/0</span>` est
  **retiré** — un dénominateur nul n'est pas un barème ;
- la tuile de pourcentage « Examen clinique / 0 % » est **retirée** du panneau
  des totaux ;
- l'en-tête de tableau orphelin (« Critères / Oui / ± / Non / Points »), qui
  annonçait des colonnes sans aucune ligne, est retiré.

Ce qui **reste visible, délibérément** : la section elle-même et son
encadré de commentaire (« Commentaires sur l'examen clinique »). L'examinateur
peut vouloir consigner l'absence d'examen physique ; la section est signalée
non cotée, elle n'induit plus en erreur.

Les intitulés des trois sections cotées passent de **« (25%) »** à
**« (33,3%) »**.

#### Baseline régénéré — chaque ligne de différence

`git diff a82e036 -- scripts/rescos/baseline.json` : **6 lignes retirées, aucune
ajoutée, aucune modifiée.** Trois par grille, les mêmes dans les deux :

| ligne | grille | justification |
|---|---|---|
| `"maxScores": { "examen": 0 }` | 12 et 13 | la clé `examen` est retirée de `maxScores` avec la section ; sa valeur était 0, la somme des maxima (76 et 78) est donc inchangée, et l'affichage statique `0/76` / `0/78` reste juste |
| `"scoreSpans": { "statusScore": 0 }` | 12 et 13 | le `<span class="score">…/0</span>` de la section vide est supprimé ; il n'y a plus de dénominateur à geler |
| `"sectionCounts": { "examen": 0 }` | 12 et 13 | `sectionInfo` ne contient plus l'entrée `examen` : la boucle de `calculateScores()` n'itère plus dessus |

**Aucun autre champ ne bouge**, et c'est le contrôle qui compte :
`criteriaCount`, `detailCount`, `radioCount`, `checkboxCount`, `blocks`,
`configForm`, `boundsAnomalies`, `uncoveredContent` sont identiques sur les 41
grilles. Autrement dit : **aucun critère, aucun sous-item, aucune case et aucun
bloc de contenu n'a été touché** — la correction ne porte que sur la
pondération et sur l'affichage d'une section qui ne notait rien.

**Divergences consignées**

- ~~`scripts/rescos/snapshot_invariants.py` · couverture : **`coef` n'est gelé
  par aucun snapshot**~~ — **tranché et corrigé, voir le volet C ci-dessous.**
  Consigné tel quel pour la trace. Énoncé d'origine :
  « `coef` n'est gelé par aucun snapshot ». C'est pourtant le champ
  dont la valeur fausse a produit ce défaut. Le filet actuel est indirect :
  `check_reachability.py` rattrape toute modification de `coef` qui casse la
  somme à 100 %, mais **pas** une redistribution qui la conserve (par exemple
  `0.5 / 0.25 / 0.25`). L'ajouter au snapshot est un geste d'une ligne, mais il
  change le baseline des 41 grilles et sortait du périmètre annoncé
  (« `check_invariants.py` OK hors les différences justifiées de RESCOS-12 et
  13 »). À arbitrer.
- corpus · balayage : **aucune autre grille ne porte de section vide
  pondérée.** Mesuré sur les 41 : RESCOS-12 et RESCOS-13 étaient les deux
  seules à déclarer un `maxScores` nul, et `empty_weighted_sections()` rend
  désormais la liste vide partout.

**Vérifications après le volet B**

| contrôle | avant (a82e036) | après |
|---|---|---|
| `check_reachability.py` | **39/41** (12 et 13 à 75 %) | **41/41**, 12 et 13 à **100 %** |
| `check_invariants.py` | OK 41/41 | **OK 41/41** (baseline régénéré, 6 lignes) |
| `check_nomenclature.py` | 111 | **0**, code 0 |
| `report_redundancy.py` | 610 paires | **610 paires** (323 intra) |
| `report_import_defects.py` | 1 numération implicite | **0** |
| `check_no_loss.py a82e036` | — | **0 item disparu** sur 30 grilles |
| balises appariées + `</html>` | 41/41 | **41/41** |
| AMBOSS · invariants / nomenclature / barème / redondance | OK · 0 · 40/40 · 147 | **OK · 0 · 40/40 · 147** |

### Volet C — `coef` gelé au snapshot, sur les deux corpus

Arbitrage du contrôleur, en réponse à la divergence consignée au volet B.
Périmètre : **`scripts/rescos/` et `scripts/amboss/` uniquement**.
`scripts/german/` n'est ni lu ni écrit ni exécuté — l'utilisateur y travaille en
parallèle ; le même geste y reste à faire et lui sera signalé.

**Le trou.** `coef` gouverne la note globale
(`globalPercentage += percentage * coef[key]`) sans être reflété par aucun autre
champ du snapshot. `check_reachability.py` exige que le total tombe sur 100 %,
donc il rattrape toute valeur qui **casse la somme** — mais pas une
redistribution qui la **conserve**. C'est la leçon de `sectionInfo[].count` sur
AMBOSS-9 rejouée sur un autre champ.

**Modifications**

- `scripts/amboss/snapshot_invariants.py` · nouvelle fonction `coefs()`, champ
  `coef` ajouté à `snapshot_one()` (forme `caseConfig` — les 40 grilles AMBOSS
  la portent, aucune forme impérative).
- `scripts/rescos/snapshot_invariants.py` · nouvelle fonction `coefs()`, qui lit
  **les deux formes** comme `max_scores()` — sans quoi RESCOS-7 et RESCOS-9,
  qui n'ont pas de `caseConfig`, auraient un `coef` vide et le champ le plus
  sensible du barème resterait non gelé sur les deux seules grilles à moteur de
  calcul embarqué.
- `scripts/amboss/check_invariants.py` et `scripts/rescos/check_invariants.py` ·
  `"coef"` ajouté à `FROZEN`.

**Preuve que le trou est fermé.** Sur une copie de RESCOS-12, `coef` passé de
trois tiers égaux à `{0.5, 0.25, 0.25}` — **somme préservée à 1.0** :

    somme des coef falsifiés : 1.0
    check_reachability       : OK (ne voit RIEN) | global si tout est coché : 100 %
    check_invariants FROZEN  : ECHEC sur coef
       attendu : {anamnese: 0.333…, management: 0.333…, communication: 0.333…}
       obtenu  : {anamnese: 0.5,   management: 0.25,    communication: 0.25}

`check_reachability.py` déclare la grille parfaitement saine ; seul le nouveau
gel la rattrape. C'est exactement le cas que la divergence du volet B décrivait.

**Baselines régénérés — la seule différence admise, et la seule obtenue.**
Contrôle exécuté **avant** régénération, champ par champ et grille par grille :

| corpus | champs ajoutés | champs retirés | champs modifiés |
|---|---|---|---|
| AMBOSS (40) | `['coef']` | aucun | **0** |
| RESCOS (41) | `['coef']` | aucun | **0** |

`git diff --numstat` le confirme : **+240 / −0** sur `scripts/amboss/baseline.json`
(40 grilles × 6 lignes), **+239 / −0** sur `scripts/rescos/baseline.json`
(37 × 6 + 2 × 5 + 1 × 4 + 1 × 3 — les quatre distributions de sections du
corpus). **Aucune suppression, aucune modification** : le diff est une addition
pure.

**Ce que la lecture des `coef` a montré, en passant** — l'argument du volet B
tient sur les deux corpus :

| distribution | AMBOSS | RESCOS |
|---|---|---|
| `0.25` ×4 | **40 / 40** | 37 / 41 |
| `1/3` ×3 (volet B) | — | 2 |
| `1` (communication seule, RESCOS-7) | — | 1 |
| `0.7 / 0.3` (RESCOS-9) | — | 1 |

**80 grilles sur 81** pondèrent leurs sections **à égalité**, quelle que soit
leur masse de points. La seule exception, RESCOS-9, porte `0.7 / 0.3` pour 41 et
15 points — et non le `0.732 / 0.268` du prorata. Aucun coefficient du projet
n'est dérivé de ses points.

**Vérifications après le volet C**

| contrôle | AMBOSS | RESCOS |
|---|---|---|
| `check_invariants.py` (avec `coef` gelé) | **OK 40/40** | **OK 41/41** |
| `check_nomenclature.py` | **0** | **0** |
| `check_reachability.py` | **40/40** | **41/41** |
| `report_redundancy.py` | **147** | **610** |
| `check_no_loss.py a82e036` | 0 item disparu | 0 item disparu |

Aucun fichier de `cases/` n'est touché par ce volet : il ne modifie que
l'outillage et les deux snapshots.

---

## Dédoublonnage — pilote RESCOS-21

### RESCOS-21 — Douleur épigastrique en coup de poignard, perforation d'ulcère (page SSP : Douleur Abdominale)

**Redondance : 55 → 18 paires inter-blocs.** Grille pilote du corpus, la plus
redondante des trois corpus du projet.

**Niveau 1 non interrogé.** `SSP — Douleur Abdominale` dessert **31 grilles** :
au-delà de la fourchette où l'indicateur de rendement prédit un arbitrage utile
(2-6 grilles tranchent, 16-27 presque jamais). Aucun point de cette grille n'a
eu besoin d'elle — les deux arbitrages rencontrés se sont réglés au niveau 2
(section notée) ou par correction directe.

**Modifications**

- `theorie`/Rappels thérapeutiques · H. pylori : « Éradication H. pylori
  systématique » → « Recherche d'H. pylori sur les biopsies, éradication si
  positive »
  **niveau 2** — la section notée tranche : `m7-detail-0` porte
  « Éradication H. pylori si positive », et `presentation`/Suivi disait déjà
  « si positive ». Le bloc pédagogique contredisait seul l'attendu noté.
- `theorie`/Rappels thérapeutiques · antibiothérapie : « Antibiothérapie précoce
  large spectre » → « Antibiothérapie débutée avant l'incision (couverture BGN
  et anaérobies) »
  **niveau 2 + rôle du bloc** — reprise de la formulation du `therapy` noté
  (« Débutée avant le bloc opératoire », « Couverture BGN et anaérobies »).
  `theorie` porte désormais le *rationnel*, il ne redit plus la liste du
  `resume`.
- `resume`/Mesures initiales · ajout : « Antalgie par titration de morphine IV »
  **règle anti-perte** — l'antalgie figurait dans la section notée
  (`therapy`/Analgésie, « Morphine IV titrée ») et dans `presentation`
  (Checklist mentale, Version longue, Traitement), mais **pas dans le bloc
  canonique**. Une fiche de révision de la perforation d'ulcère sans antalgie
  est un trou réel ; l'axe 2 exige que `presentation` soit un sous-ensemble
  strict de `resume`.
- `expert`/Pièges · précision portée avant suppression : « Ne pas retarder la
  prise en charge pour examens » → « Ne pas retarder la chirurgie pour des
  examens inutiles »
  **règle anti-perte, axe 6** — la formulation d'origine pouvait se lire
  « ne pas faire d'examens » ; celle de `presentation`/Pièges ECOS était plus
  juste et a été portée dans le canonique **avant** sa suppression.
- `expert`/Pièges · « Perforation bouchée peut donner tableau incomplet » →
  « Perforation bouchée : tableau atténué, ne pas écarter le diagnostic »
  contrat — `theorie`/Formes cliniques décrit la forme, `expert` en tire la
  conséquence de station. Le doublon verbatim disparaît, les deux rôles se
  séparent.
- `expert`/Points clés · retrait de « Urgence chirurgicale absolue »
  **axe 7** — `expert` = ce que l'examinateur observe (les quatre équations
  signe → interprétation restent), `resume`/Points clés ECOS = ce que
  l'étudiant retient, et il porte déjà « C'est une urgence chirurgicale
  absolue ».
- `presentation`/Checklist mentale · suppression de la `mnemo-box`
  « TRIade perforation »
  **axe 5 + précédent AMBOSS-1** — elle doublait strictement la « Triade de
  perforation » de Touches ludiques. Son seul apport, « (ventre de bois) », a
  été porté dans le mnémo conservé avant la suppression. La Checklist mentale
  redevient une trame pure.
- `presentation`/Touches ludiques · « Contracture abdominale généralisée » →
  « Contracture abdominale généralisée (ventre de bois) » (port ci-dessus ;
  4 paires → 1).
- `presentation`/Pièges ECOS · **suppression de la sous-section entière**
  **axe 6** — les cinq pièges sont couverts par `expert`/Pièges. Le seul
  signalé par `check_no_loss` (« Toujours biopsier les berges de l'ulcère pour
  éliminer cancer ») survit à trois endroits : `expert`/Pièges, la section
  notée `m5-detail-6` et la Version longue.
- `presentation`/§1 Arguments pour et contre · les cinq hypothèses passent de
  17 puces recopiées d'`annexe-dd` à 10 lignes fusionnées
  **règle du format** — dix paires étaient à 0,84-1,0, c'est-à-dire du
  copier-coller sans changement de format. La sous-section est **conservée**
  (AMBOSS la garde 22 fois sur 25) ; c'est son contenu qui redevient une
  restitution orale. Aucun argument n'est perdu : « Antécédent d'ulcère » et
  « Silence abdominal » sont absorbés dans les deux lignes de Q1, « Nausées /
  vomissements » dans la ligne POUR de Q2, « Pas d'irradiation transfixiante »
  dans la ligne CONTRE de Q2, « Âge jeune » ×2 dans « Patient de 35 ans sans
  antécédent vasculaire » et « À 35 ans, sans masse abdominale pulsatile ».

**Divergences consignées**

- Aucune. Les deux contradictions rencontrées (H. pylori, antibiothérapie) ont
  été tranchées au niveau 2 par la section notée.

**Non traité, et pourquoi**

- `annexe-expert` de cette grille intitule sa troisième section « Techniques
  Examen » et non « Rôles et interventions » — un des 18 intitulés distincts
  du corpus (contre 3 dans AMBOSS). Renommer n'aurait rien changé au contenu ni
  à la redondance ; la normalisation des intitulés d'`annexe-expert` est une
  décision de corpus, à arbitrer séparément.
- `annexe-theorie` n'a pas de section d'ouverture « Diagnostic le plus
  probable » — écart de gabarit du corpus (5 grilles sur 37 l'ont), pas un
  défaut de cette grille.

**Barème** — aucune modification. Toutes les éditions portent sur des blocs non
notés ; `check_invariants` reste vert sans régénération de baseline. Aucun
sous-item noté ajouté ni retiré (**règle 1** du barème, exclusivement).

**Vérifications**

| contrôle | résultat |
|---|---|
| `check_invariants.py` | **OK 41/41** |
| `check_nomenclature.py` | **OK — 0 terme** |
| `check_reachability.py` | **OK 41/41 à 100 %** |
| `report_redundancy.py RESCOS-21_` | **55 → 18** |
| `check_no_loss.py 6d11c3c RESCOS-21_` | 1 item signalé, retrouvé 3× ailleurs |
| équilibrage `<div>` / `bounds_anomalies` | 0 / [] |
| AMBOSS (4 contrôles) | **OK — 147 paires, inchangé** |

---

### Volet r4a — Grilles RESCOS-1 à RESCOS-15 (dont RESCOS-9b)

Base `66a7049`. **16 grilles du lot, 7 modifiées.** Redondance inter-blocs du
lot : **127 → 36**. Corpus : **573 → 482**. Aucun fichier de `cases/german/`
ni de `scripts/german/` lu ou touché. AMBOSS inchangé à **147**.

| grille | avant | après | grille | avant | après |
|---|---|---|---|---|---|
| RESCOS-1 | 1 | 1 | RESCOS-9 | 2 | 2 |
| RESCOS-2 | 1 | 1 | RESCOS-9b | 10 | **2** |
| RESCOS-3 | 7 | **1** | RESCOS-10 | 16 | **3** |
| RESCOS-4 | 6 | **4** | RESCOS-11 | 0 | 0 |
| RESCOS-5 | 0 | 0 | RESCOS-12 | 1 | 1 |
| RESCOS-6 | 7 | **0** | RESCOS-13 | 0 | 0 |
| RESCOS-7 | 1 | 1 | RESCOS-14 | 42 | **6** |
| RESCOS-8 | 0 | 0 | RESCOS-15 | 33 | **14** |

Le patron du pilote se confirme : le gisement est dans `presentation`, et il
cède par **fusion de puces**. Trois gestes portent l'essentiel — réduction de
§1 Arguments, sortie de la `mnemo-box` de la Checklist mentale, suppression de
« Pièges ECOS » après port. S'y ajoute un quatrième, propre à ce lot :
**les listes recopiées de §2 Examens et §3 Traitement/Suivi deviennent une
restitution orale** (`presentation-reponse text`) — c'est l'application directe
de « redire à l'oral, pas en liste » d'AMBOSS § 3, et c'est ce qui a fait
tomber 14 des 16 paires de RESCOS-10.

`annexe-dd` n'a été modifié **dans aucune grille du lot**, conformément au
pilote.

#### Trous du bloc canonique — lecture inversée de `report_redundancy`

Cinq trous trouvés, tous portés dans `resume`. **Ce sont des ajouts, pas des
suppressions.**

**Modifications**

- RESCOS-14 · `resume`/Prise en charge : **ajout** « Mesures associées : arrêt
  des AINS, réhydratation et correction électrolytique, prophylaxie
  thromboembolique dès l'hospitalisation (MICI = état prothrombotique) »
  source : **règle anti-perte** — `theorie`/Rappels et `presentation`/§3 la
  portaient toutes deux, le canonique non. La MICI en poussée hospitalisée est
  un état prothrombotique reconnu ; l'omission allait vers le sous-traitement.
- RESCOS-14 · `resume`/Examens diagnostiques : **ajout** « β-hCG chez toute
  femme en âge de procréer »
  source : **niveau 1** — `SSP — Diarrhée.md`, « À faire absolument » n° 5 :
  « Doser le β-hCG chez la femme en âge de procréer ». Patiente de 37 ans
  chez qui on va introduire corticoïdes puis immunosuppresseurs.
- RESCOS-15 · `resume`/Prise en charge : **ajout** d'une sous-section « Forme
  compliquée, en urgence » (occlusion, anémie ferriprive symptomatique,
  indication opératoire d'emblée)
  source : **règle anti-perte** — signalée par la paire `therapy ↔ presentation`
  « hospitalisation si occlusion complète » ↔ « hospitalisation si
  occlusion/saignement », qui reliait la section notée à `presentation`
  **sans passer par `resume`** : signature exacte du trou décrite au pilote.
- RESCOS-15 · `resume`/Examens diagnostiques : **ajout** « Endoscopie haute si
  méléna : le sang digéré signe d'abord un saignement au-dessus de l'angle de
  Treitz »
  source : **niveau 2** — le bloc noté `redflags` dit « Méléna. Selles noires =
  hémorragie digestive haute nécessitant endoscopie » ; `presentation`/§2 le
  portait (« Gastroscopie si doute sur saignement haut »), `resume` non.
- RESCOS-3 · `resume`/Suivi à long terme : **ajout** « Dépistage de l'anévrisme
  aortique thoracique (imagerie annuelle) : complication tardive classique de
  la maladie »
  source : **règle anti-perte** — `presentation`/§3 Suivi le portait, le
  canonique non. Complication tardive documentée de l'artérite à cellules
  géantes.
- RESCOS-6 · `resume`/Mesures spécifiques : « Acide tranexamique IV si
  hémorragie active » → « …, **dans les 3 heures suivant le traumatisme
  (délétère au-delà)** »
  source : **règle anti-perte** — la fenêtre des 3 h n'existait que dans
  `presentation`/Touches ludiques. C'est le seul point du lot où l'omission
  pouvait conduire à une **administration nuisible** et non seulement à une
  omission.

#### Alignements de fond

**Modifications**

- RESCOS-9b · `resume`/Mesures initiales : « ATB probabiliste IV après
  ponction/hémocultures : céfotaxime + oxacilline (ou vancomycine si suspicion
  MRSA) » → « ATB probabiliste IV après ponction/hémocultures,
  anti-staphylococcique : céfuroxime ou amoxicilline-acide clavulanique IV
  selon l'âge (vancomycine si suspicion de SARM) »
  source : **niveau 1** — `SSP — Boiterie de l'Enfant.md`, § PRISE EN CHARGE :
  « Arthrite septique : lavage chirurgical + antibiothérapie IV empirique
  anti-Staph (céfuroxime / Co-Amoxi-Mepha® IV) selon l'âge ». La section notée
  ne nomme aucune molécule (« Antibiothérapie intraveineuse après
  prélèvements ») : le niveau 2 est muet, le niveau 1 tranche. `MRSA` →
  `SARM` au passage.
- RESCOS-9b · `theorie`/Rappels thérapeutiques : « Durée totale
  d'antibiothérapie: 3-6 semaines » → « 3-4 semaines (IV puis PO), plus longue
  si ostéomyélite associée » ; `presentation`/§3 Suivi alignée de même
  source : **contradiction entre deux blocs pédagogiques** — `resume`/Suivi
  disait « ~3-4 semaines », `theorie` et `presentation` « 3-6 ». Le contrat
  tranche : `resume` est canonique. La nuance « plus longue si ostéomyélite
  associée » est portée aux trois endroits pour que l'écart de 6 semaines,
  qui était réel, garde sa justification.
- RESCOS-9b · `resume`/tableau comparatif, ligne 0–3 ans : « Arthrite septique,
  ostéomyélite » → « …, **fracture sur maltraitance** »
  source : **niveau 1** — `SSP — Boiterie de l'Enfant.md`, « À faire
  absolument » n° 5 (« Évoquer la maltraitance si récit incohérent ou retard de
  consultation ») et mnémonique âge ↔ cause (« 0-3 ans : septique,
  ostéomyélite, maltraitance »). `theorie` de la grille le portait déjà ; le
  tableau du canonique, qui transcrit précisément cette mnémonique, ne le
  portait pas. Cas d'espèce : enfant de 2 ans, sept jours de boiterie avant
  consultation.

#### Ports avant suppression (axe 6 et anti-perte)

- RESCOS-14 · `expert`/Pièges : **ajout** « Ne pas étiqueter "MICI" avant
  d'avoir éliminé une cause infectieuse (voyage, IST) ou médicamenteuse
  (AINS) », **puis** suppression de `presentation`/« ⚠️ Pièges ECOS » (axe 6,
  les trois autres pièges étaient déjà dans `expert`).
- RESCOS-15 · `expert`/Pièges : **ajout** « Ne pas différer la coloscopie une
  fois la sub-occlusion levée » et « Ne pas prendre une fausse diarrhée du
  constipé (fécalome) pour une diarrhée vraie », **puis** suppression de
  `presentation`/« ⚠️ Pièges ECOS ».

#### Mnémos — trois traitements distincts, décidés par le contenu

Le précédent AMBOSS (« c'est la redondance qui décide, pas le type de bloc »)
s'applique tel quel, et donne trois issues différentes dans ce lot :

- **Déplacée** vers Touches ludiques — RESCOS-14 (RECTO), RESCOS-15 (SANG),
  RESCOS-6 (ABCDE + PELVIS) : le mnémo est unique dans sa grille, la Checklist
  mentale redevient une trame pure (axe 5).
- **Supprimée** — RESCOS-10 (HEAD) : ses quatre entrées doublent strictement les
  trois mnémos déjà présents dans Touches ludiques (3C, 4P, MRV = Must).
  RESCOS-9b (KOCHER) : ses quatre entrées doublent la liste « Critères de
  Kocher » de Touches ludiques, plus précise (VS > 40 vs « CRP/VS élevées »).
- **Laissée en place** — RESCOS-3 (3C-3E) : ce mnémo *est* la trame de
  présentation, il est à sa place dans la Checklist mentale et ne produit
  aucune paire.

Dans les deux cas de suppression, Touches ludiques conserve au moins un mnémo :
aucune grille du lot ne se retrouve sans mnémo.

#### Listes recopiées devenues restitution orale

`presentation`/§2 Examens et §3 Traitement/Suivi de RESCOS-3, 9b, 10, 14 et 15,
et §3 de RESCOS-6. Fondement : AMBOSS § 3, « Une liste recopiée sous un en-tête
Q/R ne constitue pas un changement de format et tombe sous la règle du format ;
quand `presentation` doit reprendre `resume`, il le fait en registre parlé ».
Aucun examen ni traitement n'est perdu — les 80 items signalés par
`check_no_loss` ont été relus un par un et sont tous soit fusionnés dans la
ligne orale correspondante, soit portés ailleurs (détail ci-dessus).

#### `cloture` de RESCOS-4 — reformulation, pas suppression

`cloture`/« Points clés à retenir » y porte cinq puces pédagogiques
(« Approche systématique ABCDE », « Ne jamais négliger l'immobilisation
rachidienne »…) qui doublent `expert`/Compétences clés et Points critiques —
contenu hors du rôle que le pilote a fixé à `cloture` (conduite de la clôture à
l'oral). Les cinq puces ont été **reformulées en registre de clôture**, pas
supprimées : supprimer le `cloture-item` aurait fait passer le bloc de 4 à 3
segments et cassé un invariant gelé au snapshot, pour un gain de deux paires à
0,74-0,77. Les crochets de « Questions de la patiente » n'ont pas été touchés
(`cases/scoring.js:294`).

**Divergences consignées**

- RESCOS-15 · `annexe-dd`/Cancer colorectal porte « Méléna (selles noires) »
  comme argument POUR, alors que `redflags` (noté), `expert` et `theorie` de la
  même grille définissent le méléna comme un saignement **haut**. Défendable
  pour une tumeur colique droite, mais l'articulation n'est explicitée nulle
  part. **Non corrigé** — `annexe-dd` est canonique dans ce corpus et le pilote
  n'y touche pas ; le manque a été comblé par l'autre bout, en portant
  l'indication d'endoscopie haute dans `resume` (ci-dessus). **Jugement
  d'auteur, règle 3 du barème par analogie.**
- RESCOS-4, RESCOS-2 · quatre des six paires résiduelles de RESCOS-4 et l'unique
  paire de RESCOS-2 ont un côté `therapy` : **non retirées**, c'est l'accord
  voulu entre l'attendu noté et la fiche (pilote § 1.2).
- RESCOS-15 · trois paires résiduelles ont un côté `redflags` : la sous-section
  `presentation`/« Signes d'alarme (Red Flags) » recopie mot pour mot les cinq
  `redflags-text` du bloc noté. **Non supprimée** pour la même raison. C'est le
  point du patron que je signalerais pour arbitrage : la règle « une paire
  `therapy`/`redflags` n'est pas une redondance à retirer » protège aussi les
  **copies verbatim** logées dans `presentation`, et pose de ce fait un plancher
  de 3 à 5 paires sur toute grille portant ces blocs.

**Non traité, et pourquoi**

- RESCOS-11 (aucun bloc), RESCOS-5, RESCOS-8, RESCOS-13 (0 paire) : rien à
  dédoublonner. **Aucun bloc absent n'a été créé.**
- RESCOS-1, 5, 7, 9, 12, 13 n'ont ni `resume` ni `presentation` : la lecture
  inversée de `report_redundancy` y est inapplicable, faute de bloc canonique.
  Leurs paires résiduelles sont toutes `expert ↔ theorie` — le plancher
  structurel du pilote : `expert` nomme ce que l'examinateur observe,
  `theorie` la règle qui le fonde (RESCOS-7 : « anévrisme de 9 mm avec
  indication chirurgicale formelle » ↔ « anévrismes > 7 mm : indication
  chirurgicale » — cohérents, à conserver tels quels).
- `annexe-expert` : intitulés non normalisés (RESCOS-4 « Compétences Clés » /
  « Points Critiques » / « Erreurs Courantes » / « Matériel Nécessaire »,
  RESCOS-15 « Techniques Examen »). Même arbitrage en attente qu'au pilote.

**Barème** — aucune modification. Les 7 grilles modifiées n'ont subi d'édition
que dans des blocs non notés (`resume`, `expert`, `theorie`, `presentation`,
`cloture`). Aucun `maxScores`, `<span class="score">`, `sectionInfo[].count`
ni `coef` touché ; **aucune régénération de baseline**. Strictement **règle 1**.
RESCOS-12 et RESCOS-13 n'ont reçu aucune modification : la redistribution de
coefficient de `c5243e1` est intacte.

**Vérifications**

| contrôle | résultat |
|---|---|
| `check_invariants.py` | **OK 41/41** |
| `check_nomenclature.py` | **OK — 0 terme** |
| `check_reachability.py` | **OK 41/41 à 100 %** |
| `report_redundancy.py` (lot RESCOS-1→15) | **127 → 36** |
| `report_redundancy.py` (corpus) | **573 → 482** |
| `check_no_loss.py 66a7049` | 80 items sur 7 grilles, tous relus — fusions ou ports |
| `report_import_defects.py` | inchangé (0 / 0 / 2 / 113 / 0 / 13 / **0**) |
| équilibrage `<div>` · `bounds_anomalies` · `uncovered_content` | 0 · [] · [] sur 41/41 |
| AMBOSS (4 contrôles) | **OK — 147 paires, inchangé** |

---

### Dédoublonnage — lot RESCOS-16 à RESCOS-30 (hors RESCOS-21, pilote)

Base `c883906`. **14 grilles traitées, 14 modifiées.** Redondance inter-blocs du
lot : **277 → 30**. Corpus : **482 → 235** (intra : 299 → 254). AMBOSS
inchangé à **147**.

| grille | avant | après | ce qui a cédé |
|---|---|---|---|
| RESCOS-16 | 18 | **3** | `theorie` doublons de section, §1, §2, §3, mnémo ABCD |
| RESCOS-17 | 6 | **0** | §1, §2 |
| RESCOS-18 | 26 | **0** | `theorie` doublons, `expert`, §1, §2, §3, Checklist |
| RESCOS-19 | 18 | **1** | Pièges ECOS, §1, §2, §3 |
| RESCOS-20 | 48 | **6** | `theorie` doublons, mnémo déplacé, Triade, Pièges ECOS, §1-3 |
| RESCOS-22 | 4 | **2** | Pièges ECOS, §1, §2, §3 |
| RESCOS-23 | 9 | **1** | Pièges ECOS, contraste réduit, §1, §2, §3 |
| RESCOS-24 | 38 | **4** | `theorie` doublons, mnémo déplacé, Signes typiques, Complications, Pièges ECOS, §1-3 |
| RESCOS-25 | 29 | **2** | mnémo déplacé, Signes typiques, Prostatite, Pièges ECOS, §1-3 |
| RESCOS-26 | 17 | **2** | `expert`, §1, §2, §3, Checklist |
| RESCOS-27 | 18 | **2** | `expert`, `theorie`, les cinq listes de §1-§5 |
| RESCOS-28 | 44 | **7** | `theorie` contraste, `expert`, Touches ludiques, Pièges ECOS, §1-4 |
| RESCOS-29 | 1 | **0** | `expert` reformulé en conduite |
| RESCOS-30 | 1 | **0** | `theorie` reformulé en raisonnement |

**Modifications**

*Geste 3 — trous du bloc canonique (lecture inversée `therapy`/`redflags` ↔
`presentation` sans `resume`) : sept trouvés, sept comblés.*

- RESCOS-18 · `resume`/Imagerie : « épaississement pariétal » → « épaississement
  pariétal **> 3 mm**, […] liquide péri-vésiculaire »
  source : `theorie` de la même grille — le seuil échographique n'existait que là.
- RESCOS-26 et RESCOS-27 · `resume`/Traitement médical : « Traitement
  antihypertenseur : cible < 130/80 mmHg » → « […], **IEC ou sartan privilégiés
  (protection vasculaire au-delà du seul contrôle tensionnel)** »
  source : `therapy` (noté) « IEC/ARA2 (protection vasculaire) » + `SSP —
  Claudication Intermittente & AOMI` L264 « IEC / sartan privilégiés ».
  L'indication de classe, distincte du contrôle tensionnel, était absente du canonique.
- RESCOS-27 · `resume` : « Rééducation à la marche (programme supervisé
  recommandé) » → « […] **3 séances de 30 à 60 min par semaine pendant au moins
  3 mois** » ; « Claudication invalidante malgré traitement médical +
  rééducation » → « […] malgré **3-6 mois** de traitement médical optimal »
  source : `therapy` (noté) et `SSP — Claudication Intermittente & AOMI`.
  Les paramètres de prescription du traitement de première intention, et la durée
  qui conditionne l'indication chirurgicale, manquaient au canonique.
- RESCOS-28 · `resume`/Prise en charge, **quatre ports** :
  « Aides techniques (cannes, semelles) » → « canne portée **du côté opposé** » ;
  « Infiltrations intra-articulaires (corticoïdes ou acide hyaluronique) » →
  « corticoïdes, **3 par an au maximum** » ; « Indiqué si échec du traitement
  conservateur » → « après échec d'un traitement médical bien conduit **pendant au
  moins 6 mois**, avec douleur invalidante ou limitation fonctionnelle » ;
  « Excellents résultats » → « […] ; **durée de vie de la prothèse : 15 à 20 ans** »
  source : `therapy` (noté) de la même grille pour les quatre ;
  `SSP — Douleur de Hanche` L249 « canne **controlatérale** » confirme le premier.

*Niveau 1 — deux arbitrages, tous deux sur pages SSP à faible fan-out.*

- RESCOS-26 et RESCOS-27 · `resume` : « Statine forte dose (objectifs LDL
  **< 0,55 mmol/L** si haut risque) » → « Statine de haute intensité (objectif
  LDL **< 1,4 mmol/L**) »
  source : `SSP — Douleur au Mollet & TVP` L360 « statine forte intensité
  (LDL < 1,4 mmol/L) » et `SSP — Claudication Intermittente & AOMI` L263
  « cible LDL < 1.4 mmol/L (recommandation SSC/ESC) ».
  **Erreur d'unité** : 0,55 est la valeur en g/L, écrite avec l'unité mmol/L —
  soit une cible dix fois trop basse. Hiérarchie niveau 1 explicite.

*Contradictions internes réglées par le contrat.*

- RESCOS-20 · `theorie` portait **deux modalités d'imagerie de seconde ligne**
  incompatibles (« IRM si US non conclusif » et « CT abdomino-pelvien si US non
  contributif »), là où `resume` et `presentation` disent IRM. Aligné sur IRM,
  avec la raison portée : « préférée au scanner chez la femme en âge de procréer
  (pas d'irradiation) ». `resume` est canonique.
- RESCOS-28 · `theorie` portait **deux seuils de raideur matinale** sans
  articulation (« < 60 minutes » dans les critères, « > 30 min » dans le
  différentiel mécanique/inflammatoire). Reformulé : « ≤ 60 min (seuil des
  critères ACR) — en pratique clinique, c'est un dérouillage > 30 min qui fait
  basculer vers l'inflammatoire ».
  source : `SSP — Douleur de Hanche` L110 « dérouillage > 30 min ».
- RESCOS-16 · `theorie` : « plasmaphorèse » (×3) → « plasmaphérèse » ;
  « mycophenolate » → « mycophénolate » ; `resume` « IVIg » → « IgIV »
  (le reste de la grille écrit IgIV) ; `theorie` « Tensilon/néostigmine » →
  « édrophonium, néostigmine » (Tensilon est une marque américaine).
- RESCOS-19 · **`ERCP` (×8) → `CPRE`** : la même grille écrivait déjà CPRE
  huit fois. `EUS` → « écho-endoscopie ». RESCOS-18 · « IRM biliaire (MRCP) » →
  « Cholangio-IRM » (`theorie` de la même grille écrit déjà Cholangio-IRM).
  RESCOS-23 · « Mise à jeun (NPO) » → « Mise à jeun ».
- RESCOS-26 · `presentation`/mnémo 5P : « Paresia » → « Paralysis (paralysie) ».
  RESCOS-28 · « Impôtence » → supprimé avec la liste, reformulé.

*Geste 4 — réduction des recopies de `therapy` dans `presentation` (arbitrage du
volet).* Appliqué à RESCOS-26 (§3 Q2 recopiait les trois `therapy-section`),
RESCOS-28 (§3 Q2 et §4 Q2 : indications chirurgicales et durée de vie
prothétique mot pour mot), RESCOS-25 (§3 Q2 « Spécifique »). **Les blocs notés
n'ont subi aucune modification.**

*Gestes 1 et 2 — les trois portes et les listes de §2/§3.* Les listes
`presentation-reponse list` sont converties en `presentation-reponse text`,
registre parlé, dans les 12 grilles qui en portaient. « Pièges ECOS » supprimée
dans 6 grilles (RESCOS-19, 20, 22, 23, 24, 25, 28), après **port explicite vers
`expert`/Pièges** de tout ce que ce bloc ne portait pas : RESCOS-22 (tolérance
orale, antibiothérapie systématique), RESCOS-23 (lipase), RESCOS-25 (AINS et
risque rénal, cystite masculine), RESCOS-28 (irradiation au genou, amplitudes,
radio avant IRM). Les `mnemo-box` de Checklist mentale déplacées vers Touches
ludiques dans RESCOS-20, 24, 25 (mnémo signature de la grille, axe 5) ;
laissées en place ailleurs.

*Sections dupliquées dans `theorie`.* Quatre grilles portaient **deux sections
de même titre** dans le même bloc (RESCOS-16 et RESCOS-18 : deux « Examens
complémentaires » ; RESCOS-20 : « Diagnostic » ⊂ « Examens complémentaires » ;
RESCOS-24 : « Prise en charge » ⊂ Rappels + Examens). Fusionnées en une seule,
après port item par item de ce que la section supprimée portait en propre
(« décrément » et « bilan auto-immun » dans RESCOS-16 ; CT et cholangio-IRM dans
RESCOS-18 ; `target sign` appendiculaire et sédiment urinaire dans RESCOS-20 ;
durée 10-14 j déjà présente dans `resume` pour RESCOS-24). RESCOS-20 : la
section « DD » de `theorie`, liste nue de cinq noms tous couverts par
`annexe-dd`, supprimée.

*Balayage microbiologique (les 41 grilles).*

- `HIV` → **`VIH`** : RESCOS-1 (×4, dont deux dans la section notée — libellé
  seul, format `N. Libellé` intact) et RESCOS-10 (×1). Le corpus écrivait déjà
  VIH dans RESCOS-2 et RESCOS-30.
- `PID` → **salpingite / infection génitale haute** : RESCOS-24 (×4, dont une
  dans `annexe-dd` : « Salpingite / PID » → « Salpingite (infection génitale
  haute) »).
- `TB` → **tuberculeuse** : RESCOS-34 (×1, étiologie de péricardite).
- `MRSA`, `MSSA`, `ESBL` : **zéro occurrence** restante (le `MRSA` de RESCOS-9b
  avait été corrigé au lot r4a).
- Dix motifs ajoutés à `BANNED` via `MICROBIO` dans
  `scripts/rescos/check_nomenclature.py` : `MRSA`, `MSSA`, `ESBL`, `MDRO`,
  `HIV`, `PID`, `UTI`, `STD`, `STI`, `TB`.

**Divergences consignées**

- RESCOS-26 et RESCOS-27 · `therapy` (**noté**) prescrit une cible
  « LDL < 0,7 g/L » (= 1,8 mmol/L), là où les deux pages SSP disent
  1,4 mmol/L (= 0,55 g/L). C'est l'ancienne cible « haut risque », alors que
  l'AOMI symptomatique relève du très haut risque. **Non corrigé** : les blocs
  notés sont intouchables. Le `resume` a été aligné sur la SSP ; l'écart entre
  le noté et le canonique subsiste et demande un arbitrage du barème.
- Corpus entier · **`gold standard`** : 17 occurrences sur 16 grilles, dont
  RESCOS-17. Anglicisme, mais usage établi et homogène du corpus, et large
  débordement de mon lot. **Non corrigé, non ajouté à `BANNED`** — corriger 2
  grilles sur 16 créerait l'irrégularité que le pilote reproche à la
  normalisation grille par grille.
- Anglicismes non microbiologiques repérés au balayage, **hors de mon lot et non
  corrigés** : `ESR` et `ANA` (RESCOS-3, → VS et AAN — la grille voisine
  RESCOS-38 écrit déjà AAN), `Giant cells` (RESCOS-3), `SCFE` (RESCOS-9b, →
  épiphysiolyse fémorale supérieure, déjà écrit en toutes lettres deux lignes
  plus bas), `anti-DNA` et `DMARD` (RESCOS-38), `CABG` et `PCI` (RESCOS-36 et
  37), `FIT` (RESCOS-15), `IVDU` et `MST` (RESCOS-1, → IST, que RESCOS-14 et 33
  emploient déjà), `PRN` (RESCOS-40). Aucun n'est microbiologique ; le mandat de
  balayage ne les couvre pas.
- `\bVRE\b` **écarté de `BANNED`, faux positif avéré** : AMBOSS-19 écrit
  « VRE = volume de réserve expiratoire ». Dans une porte bloquante, ce motif
  casserait toute grille portant des volumes pulmonaires. `\bCRE\b` écarté pour
  la même famille de risque, sans besoin mesuré (0 occurrence sur les deux
  corpus). `\bTB\b` ajouté : 0 sur RESCOS, mais **22 sur AMBOSS-31** — mesuré et
  consigné dans le docstring, sans effet puisque la table ne tourne que sur RESCOS.
- RESCOS-19 et RESCOS-23 · le mnémo **`5F`** (Female, Fat, Forty, Fertile, Fair)
  est présenté comme facteur de risque alors que le patient de RESCOS-19 est un
  **homme de 64 ans**. Le mnémo décrit le risque lithiasique en population, pas
  ce patient. **Non corrigé** — jugement d'auteur, règle 3.
- `annexe-expert` toujours non normalisé (RESCOS-28 « Techniques Examen »,
  RESCOS-25 et 22 « Rôles et interventions »). Même arbitrage en attente qu'au
  pilote et au lot r4a.

**Barème** — **aucune modification.** Les 14 grilles du lot n'ont été éditées que
dans `resume`, `expert`, `theorie`, `presentation` ; RESCOS-1, RESCOS-10 et
RESCOS-34 n'ont reçu que la substitution de nomenclature (libellé, pas de
structure). Aucun sous-item noté ajouté ni retiré, aucun `maxScores`,
`<span class="score">`, `sectionInfo[].count` ni `coef` touché, **aucune
régénération de baseline**. Strictement **règle 1**.

**Vérifications**

| contrôle | résultat |
|---|---|
| `check_invariants.py` | **OK 41/41** |
| `check_nomenclature.py` (table élargie) | **OK — 0 terme** |
| `check_reachability.py` | **OK 41/41 à 100 %** |
| `report_redundancy.py` (lot 16→30) | **277 → 30** |
| `report_redundancy.py` (corpus) | **482 → 235** (intra 299 → 254) |
| `check_no_loss.py c883906` | 223 items / 17 grilles — tous relus, 1 perte réelle trouvée et réparée |
| `report_import_defects.py` | 0 / 0 / 2 / 101 / 0 / 13 / **0** (chevrons nus : 114 → 101) |
| équilibrage `<div>` · `bounds_anomalies` · `uncovered_content` | 0 · [] · [] sur 41/41 |
| AMBOSS (4 contrôles) | **OK — 147 paires, inchangé** |

German n'a été ni lu ni mesuré.
