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

---

## Lot r4c — RESCOS-31 à RESCOS-40, et la passe acronymes sur les 41 grilles

Base `803d550`. **Le corpus s'arrête à RESCOS-40** : il compte 41 grilles parce
qu'il porte une RESCOS-9b, pas parce qu'il va jusqu'à 41. Le lot annoncé
« 31 à 41 » est donc **dix grilles**, et il clôt le corpus (16 + 15 + 10 = 41).

**Redondance inter-blocs du lot : 151 → 46.** Corpus RESCOS : **235 → 131**
(intra : 254 → 210). AMBOSS reste à **147**. Rien lu ni touché sous
`cases/german/` ni `scripts/german/`.

### 1. Résultat par grille

| grille | avant | après | ce qui a cédé |
|---|---|---|---|
| RESCOS-31 | 2 | **1** | `theorie` — raisonnement de l'hydratation, posologie alpha-bloquant |
| RESCOS-32 | 10 | **7** | §1 fusionné, §2 en oral ; plancher des signes cardinaux de kératite |
| RESCOS-33 | 3 | 3 | — (plancher `expert ↔ theorie`, consentement et impact fonctionnel) |
| RESCOS-34 | 27 | **2** | Critères ≥2/4 et cycle de Holzmann (copies de `theorie`), Pièges, §1-§3, Checklist, `expert` reformulé en conduite |
| RESCOS-35 | 20 | **8** | Triade EP, Pièges, §1, §2, §3, Checklist |
| RESCOS-36 | 22 | **2** | Triade angineuse (double le mnémo TRI), Pièges, §1-§3, Checklist |
| RESCOS-37 | 17 | **6** | Triade angineuse (idem), Pièges, §1-§3, Checklist |
| RESCOS-38 | 46 | **14** | « Signes distinctifs de PR », mnémo déplacé, Pièges, §1-§4, `expert` reformulé |
| RESCOS-39 | 0 | 0 | **aucune édition** — 0 paire, et la page SSP ne contredit rien |
| RESCOS-40 | 4 | **3** | `theorie` — physiopathologie du remplissage sur obstacle fixe, TAVI |

RESCOS-39 est laissée intacte : mesurée à zéro, comparée à `SSP — Dyspnée`, elle
ne portait ni redondance ni divergence. Ne rien faire est un résultat.

### 2. Ce que ce lot ajoute au patron

**Un sixième gisement : la sous-section de `presentation` qui double le mnémo
placé trois lignes plus haut.** Quatre grilles du lot (34, 35, 36, 37) portaient,
sous « Touches ludiques », une « Triade » ou des « Critères » qui redisaient item
par item ce que la `mnemo-box` de la Checklist venait d'énoncer, ou ce que
`theorie` porte en propre. Ce n'est pas le geste 1 du pilote (les trois portes)
ni le geste 2 (les listes de §2-§3) : c'est une **quatrième sous-section
surnuméraire à l'intérieur du même bloc**, cousine du cinquième gisement de r4b
(les sections dupliquées de `theorie`). Elle se repère sans lire : un `<h5>`
« Triade… » ou « Critères… » dans `section-mnemo` alors que la `mnemo-box` ou
`theorie` dit déjà la même chose. Suppression sèche, zéro perte, 3 à 5 paires par
grille.

**Le geste « `expert` reformulé en conduite » rend beaucoup plus qu'attendu.**
r4b l'avait noté sur RESCOS-29 pour une paire. Ici, réécrire les « Points clés »
de `expert` en *ce que l'examinateur guette* — au lieu de la liste des signes que
`annexe-dd` et `resume` portent déjà — a fait 21 → 14 sur RESCOS-38 et 8 → 2 sur
RESCOS-34. Le contrat le prévoyait (« `expert` : conduite de station »), mais
c'est le premier lot où il paie à ce niveau. Signature : les `<li>` de
« Points clés » sont des **groupes nominaux** (« Polyarthrite symétrique
typique ») là où la conduite s'écrit en **verbes** (« Attendre que le candidat
qualifie la douleur avant de la localiser »).

### 3. Les trous du bloc canonique — six trouvés, six comblés

| grille | ce qui manquait | comment il s'est signalé |
|---|---|---|
| **RESCOS-38** | **acide folique** avec le méthotrexate, et sa posologie | `therapy` (noté) ↔ `presentation` **sans `resume`** — signature exacte |
| **RESCOS-38** | dépistage d'une **tuberculose latente** avant anti-TNF, sérologies B/C et VIH | niveau 1, `SSP — Douleurs Articulaires` (« Pré-DMARDs ») ; absent de la grille entière |
| **RESCOS-38** | **tératogénicité** du méthotrexate chez une femme de 45 ans | niveau 1, même page ; absent de la grille entière |
| RESCOS-38 | corticothérapie **< 10 mg/j**, protection gastrique, prévention de l'ostéoporose cortico-induite | `therapy` (noté), pas `resume` |
| **RESCOS-34** | colchicine **pendant 3 mois** | niveau 1, `SSP — Douleur Thoracique` ; `theorie` donnait la dose sans la durée |
| **RESCOS-32** | **jamais d'anesthésique local répété** sur un ulcère cornéen | niveau 1, `SSP — Œil Rouge` ; absent de la grille entière |
| RESCOS-34 | en tamponnade, la **vitesse** prime le volume ; ni diurétique ni nitré | niveau 1, même page |
| RESCOS-36 | activité physique **30 min/j** | `therapy` (noté) ↔ `resume`, la paire résiduelle portait le chiffre d'un seul côté |

Trois appartiennent à la famille de l'acide tranexamique du lot r4a — celle où
l'omission conduit à **faire** un geste délétère et non à en oublier un :
introduire un anti-TNF sans avoir dépisté une tuberculose latente, prescrire du
méthotrexate à une femme en âge de procréer sans contraception, et délivrer un
collyre anesthésique à un patient pour calmer son ulcère de cornée.

### 4. Niveau 1 — le prédicteur « chiffres » se vérifie, et il tranche par l'absence

Le déclencheur retenu par r4b (lire la SSP quand la grille porte des **cibles
chiffrées**, quel que soit le fan-out) tient sur les cinq lectures du lot.

| page SSP | grille(s) | ce qu'elle a tranché |
|---|---|---|
| `SSP — Douleurs Articulaires` | 38 | **trois points**, dont deux absents de la grille entière (TB latente, tératogénicité) |
| `SSP — Douleur Thoracique` | 34, 35, 36, 37 | **deux points** sur RESCOS-34 (durée de colchicine, tamponnade) ; **muette** sur la cible LDL |
| `SSP — Syndrome Métabolique` | 36, 37 | **la table des cibles LDL par strate de risque** — c'est elle qui a tranché |
| `SSP — Œil Rouge` | 32 | **un point** absent de la grille entière (anesthésique local) |
| `SSP — Colique Néphrétique` | 31 | confirme, et corrige le sens : « pas d'hyperhydratation forcée » |
| `SSP — Dyspnée` | 39, 40 | **rien** — elle ne porte pas les cibles du traitement chronique |

La nuance neuve : **la page qui porte le symptôme ne porte pas toujours le
chiffre**. `SSP — Douleur Thoracique` est muette sur la cible LDL des quatre
grilles de douleur thoracique du lot ; c'est `SSP — Syndrome Métabolique`, qui ne
dessert aucune grille du corpus par son intitulé, qui donne la table complète.
**Corollaire pratique : quand une grille porte un chiffre, chercher la page qui
porte ce chiffre, pas celle qui porte son symptôme.**

### 5. RESCOS-36 et 37 — la prédiction du lot précédent est réfutée

r4b annonçait que la cible LDL fautive de RESCOS-26/27 (« 0,55 mmol/L », valeur
en g/L portant l'unité mmol/L) était « vraisemblablement de corpus » et que
RESCOS-36 et 37 portaient « la même formule ». Vérification faite, **c'est faux
dans les deux sens** :

* **RESCOS-36 écrit `0.55 g/L` dans son `therapy` noté — avec la bonne unité.**
  0,55 g/L = 1,42 mmol/L, exactement la cible du très-haut-risque. Le bloc noté
  de RESCOS-36 est donc **à jour**, et c'est même le plus à jour de la grille.
* **RESCOS-37 n'a aucun bloc `therapy`.** L'affirmation « leurs blocs `therapy`
  notés prescrivent LDL < 0,7 g/L » ne vaut que pour RESCOS-26 et 27.

Le vrai défaut de RESCOS-36/37 est **l'inverse de celui annoncé** : leur `resume`
(et le `theorie` de 37) prescrivent « LDL < 1,8 mmol/L, voire < 1,4 si haut
risque ». Or 1,4 est la cible du **très haut risque**, auquel une coronaropathie
documentée appartient d'emblée ; 1,8 est celle du haut risque. La phrase inverse
les deux strates et donne comme cible principale une valeur trop haute.
**Corrigé sur les deux grilles**, sur autorité de la table explicite de
`SSP — Syndrome Métabolique` (« très haut risque < 1,4 ; haut risque < 1,8 ;
modéré < 2,6 ; faible < 3,0 ») et du `therapy` noté de RESCOS-36 lui-même.

### 6. Passe acronymes — recensement complet, seize motifs, sept écartés

Recensement exhaustif : tous les tokens majuscules de 2 à 8 caractères du texte
visible des 41 grilles, triés par fréquence, puis chaque candidat compté sur les
**trois** corpus avant décision. **56 substitutions sur 26 grilles.**

| motif | occ. RESCOS | remplacement | preuve d'incohérence interne |
|---|---|---|---|
| `gold standard` | 15 / 14 gr | examen (ou traitement) de référence | « examen de référence » déjà 7× sur 5 grilles |
| `BMI` | 16 / 10 gr | IMC | `IMC` déjà 20× sur 6 grilles ; RESCOS-18 écrivait **les deux dans la même ligne d'en-tête** |
| `DMARD(s)` | 5 | traitement de fond | RESCOS-38 écrivait « Traitement de fond (DMARDs) » |
| `PCI` | 4 | angioplastie | RESCOS-36 écrivait « PCI (angioplastie avec stent) » |
| `SCFE` | 3 | épiphysiolyse fémorale supérieure | RESCOS-9b l'écrivait en toutes lettres deux lignes plus bas |
| `ANA` | 2 | AAN | RESCOS-38 écrivait `AAN` |
| `CABG` | 2 | pontage coronarien | RESCOS-36 écrivait « pontage coronarien » |
| `MST` | 2 | IST | RESCOS-14 et 33 écrivaient `IST` |
| `DM` | 2 | diabète | — |
| `ESR` | 1 | VS | la parenthèse qui suit disait déjà « VS > 50 mm/h » |
| `Giant cells` | 1 | cellules géantes | — |
| `anti-DNA` | 1 | anti-ADN natif | — |
| `IVDU` | 1 | usage de drogues IV | — |
| `PRN` | 1 | à la demande | — |
| `FIT` | 1 | test immunologique fécal | — |
| `N/V` | 1 | nausées et vomissements | — |

**`gold standard` : tranché, et traité sur les 41 d'un coup**, comme r4b le
demandait. Le point qui justifiait le refus d'un `sed` : sur les 15 occurrences,
**une qualifiait un traitement et non un examen** (RESCOS-38, « Méthotrexate =
gold standard ») — un remplacement uniforme aurait produit « Méthotrexate =
examen de référence ». Remplacement occurrence par occurrence, avec assertion de
comptage sur chacune.

**Le bordage a payé deux fois.** `\bVRE\b` est reconfirmé faux positif
(AMBOSS-19, « volume de réserve expiratoire »). Et **un cas neuf, plus net** :
`\bQID\b` vaut **quadrant inférieur droit** dans RESCOS-22 (« QSD, QSG, QID,
QIG ») et **quater in die** dans AMBOSS-13 et 8. Même token, deux sens
légitimes, un par corpus : dans une porte bloquante, ce motif aurait cassé
RESCOS-22 pour un usage parfaitement correct. Écartés pour la même raison :
`\bASA\b` (5-ASA, molécule), `\bRx\b` (« Rx thorax » = graphie suisse de la
radiographie — faux ami parfait, `Rx` désignant l'ordonnance en anglais),
`\bAF\b` (anamnèse familiale), `\bAAA\b` (sigle identique en français),
`\bMI\b` / `\bCT\b` / `\bUS\b` / `\bPR\b` / `borderline` (usages installés).

**Seize motifs ajoutés à `BANNED`** via un dictionnaire `ANGLICISMES` dans
`scripts/rescos/check_nomenclature.py`, avec la mesure sur les trois corpus et
les sept exclusions consignées dans le docstring. `check_nomenclature` sort
**OK, 0 terme** ; les quatre contrôles d'AMBOSS sont inchangés.

**Coût mesuré de l'harmonisation : +2 paires**, sur RESCOS-14 et RESCOS-35, hors
lot. Deux items qui disaient déjà la même chose en deux mots différents la disent
maintenant dans les mêmes mots, et le comparateur les apparie. C'est le prix
exact de la cohérence terminologique ; le refuser reviendrait à préférer un
chiffre à la lisibilité.

### 7. Barème

**Aucune modification.** Toutes les éditions portent sur `resume`, `expert`,
`theorie`, `presentation`, plus **six substitutions de nomenclature dans la
section notée** — RESCOS-1 (`criteria-text` « 5. Facteurs de risque VIH et
IST », un `detail-text`, une `patient-response`), RESCOS-2 (`scoring-rule`),
RESCOS-15 et RESCOS-31 (`detail-text`), RESCOS-36 (`detail-text`). Libellés,
jamais structure ; le format `N. Libellé [réponse]` de `cases/scoring.js:159`
est intact, les crochets de `patient-response` conservés. Précédent posé par r4a
(`HIV` → `VIH` dans la section notée de RESCOS-1). Aucun sous-item ajouté ni
retiré, aucun `maxScores`, `<span class="score">`, `sectionInfo[].count` ni
`coef` touché, **aucune régénération de baseline**. Strictement **règle 1**.

Les blocs `therapy` et `redflags` n'ont subi **aucune** modification de contenu.

### 8. Vérifications

| contrôle | résultat |
|---|---|
| `check_invariants.py` | **OK 41/41** |
| `check_nomenclature.py` (table + 16 motifs) | **OK — 0 terme** |
| `check_reachability.py` | **OK 41/41 à 100 %** |
| `report_redundancy.py` (lot 31→40) | **151 → 46** |
| `report_redundancy.py` (corpus) | **235 → 131** (intra 254 → 210) |
| `check_no_loss.py 803d550` | 181 items / 27 grilles — filtrés par mots porteurs : 143 sains, **38 relus un par un**, 2 réductions réelles réparées |
| `report_import_defects.py` | 0 / 0 / 2 / **96** / 0 / **12** / 0 (chevrons nus 101 → 96) |
| équilibrage `<div>` · `bounds_anomalies` · `uncovered_content` | 0 · [] · [] sur 41/41 |
| AMBOSS (4 contrôles + redondance) | **OK — 40/40, 147 paires, inchangé** |

Les deux réductions réelles trouvées par le filtre : RESCOS-35 (« créatinine,
plaquettes » du suivi, devenu « fonction rénale ») et RESCOS-36 (« consultation
cardiologique régulière », disparue du suivi). Toutes deux restaurées. Les 36
autres sont des variantes morphologiques (« amélioration » → « améliore »,
« cutané » → « cutanée »), des fusions dans la ligne orale correspondante, ou
la correction voulue de la cible LDL.

German n'a été ni lu ni mesuré.

### 9. Préoccupations

**9.1 — L'écart noté ↔ SSP de RESCOS-26/27 subsiste, et il est isolé.** Leurs
`therapy` notés prescrivent « LDL < 0,7 g/L », soit 1,8 mmol/L — la cible du
haut risque, alors qu'une AOMI symptomatique relève du très haut risque. Le
`resume` corrigé par r4b dit 1,4. La divergence demeure et je ne peux pas la
réduire. Mais elle **ne concerne que ces deux grilles** : le contrôle mené ici
montre que RESCOS-36 porte la bonne valeur dans son bloc noté et que RESCOS-37
n'en a pas. L'arbitrage demandé par r4b (ouvrir le barème à la correction d'une
valeur chiffrée dans un `therapy` quand une SSP explicite la contredit) porte
donc sur **deux occurrences**, pas sur un défaut de corpus.

**9.2 — Une grille prescrit un AINS et une restriction hydrique au même
patient déshydraté.** RESCOS-31 : le `therapy` noté prescrit « kétoprofène
100 mg IV » et « restriction hydrique pendant la crise (500 mL/24 h) » chez un
sportif dont la section notée relève « déshydratation relative » et « hydratation
habituelle insuffisante ». La page SSP dit « pas d'**hyper**hydratation forcée »
— ce qui n'est pas la même consigne — et contre-indique les AINS sur rein
hypoperfusé. **Non corrigé** (bloc noté). J'ai porté le raisonnement dans
`theorie`, seul bloc pédagogique de cette grille, qui n'a pas de `resume`. C'est
le second cas du chantier où un bloc noté demande un geste potentiellement
délétère, après les infiltrations de RESCOS-28.

**9.3 — Le prédicteur « chiffres » a besoin d'un second étage.** Il dit *quand*
lire une SSP, mais pas *laquelle*. Ce lot montre que la page qui porte le
symptôme peut être muette sur le chiffre tandis qu'une page transversale le
porte en entier. Proposition : indexer les pages SSP par **cibles chiffrées**
plutôt que par symptôme, ce qui se mécanise (un motif « valeur + unité + strate »
sur le vault) et rendrait la lecture de niveau 1 dirigée au lieu d'être devinée.

**9.4 — `annexe-expert` toujours non normalisé.** Quatrième lot consécutif.
Ce lot ajoute « Criteres Diagnostiques » (RESCOS-38, déjà signalé pour
RESCOS-26), « Rôles et interventions » (RESCOS-34). Non renommés, même raison.

**9.5 — Le corpus s'arrête à 40, et le nom des lots l'a masqué.** Les trois
volets ont été annoncés « 1-15 », « 16-30 », « 31-41 », en supposant une
numérotation continue de 1 à 41. Il n'y a jamais eu de RESCOS-41 : le
quarante-et-unième fichier est RESCOS-9b. Aucune grille n'a été omise — le tri
de `lib.grids()` place bien 9b dans le premier lot, et r4a l'avait traitée —
mais un lot suivant qui se fierait à l'intitulé chercherait un fichier absent.

---

## Lot r7 — réparation des trois défauts de la vérification finale

Base `0e82963`. **Quatre grilles modifiées**, plus `scripts/rescos/baseline.json`.
Rien lu, écrit ni exécuté sous `cases/german/` ni `scripts/german/`. AMBOSS
témoin : **147, inchangé**.

### 1. RESCOS-7 et RESCOS-9 — le moteur embarqué, remplacé par `cases/scoring.js`

**Modification**

- RESCOS-7 · le bloc `<script>` de 723 lignes qui embarquait une copie de
  `calculateScores()` → `window.caseConfig = {maxScores: {communication: 30},
  coef: {communication: 1}, sectionInfo: [{key: "communication", prefix: "c",
  count: 15, label: "Communication"}]}` puis `<script src="../scoring.js">`.
- RESCOS-9 · idem, 727 lignes → `caseConfig` à deux sections, `anamnese`
  (41, coef 0,7, 14 critères) et `management` (15, coef 0,3, 6 critères).

**Le choix, et pourquoi celui-là.** Deux voies étaient ouvertes : reporter les
deux corrections manquantes dans les copies, ou basculer sur le fichier partagé.
Le `diff` a tranché.

1. **L'écart n'était pas de deux corrections mais de six.** Manquaient : la
   garde `if (missingEl)`, l'**appel** de `saveToRegistry()`, la **définition**
   de `saveToRegistry()`, le chargeur dynamique de `srs.js`, la détection du
   mode circuit (avec le retour à `exam.html` en fin de minuteur), et les deux
   constructeurs de barre de navigation `createNavBar()` / `createCircuitNav()`.
   Reporter deux corrections aurait laissé quatre régressions vivantes — dont
   une qui casse le mode circuit sur ces deux stations.
2. **Il n'y avait rien à préserver.** Les deux copies sont identiques entre
   elles et identiques à `cases/scoring.js` partout ailleurs — vérifié au
   `diff` ligne à ligne. Les seuls ajouts sont le bloc de configuration et un
   `isNewFormat = true` mort (déclaré, jamais lu ; `grep` : une occurrence par
   fichier). Ce n'était pas une variante, c'était une fourche périmée.
3. **Le report à la main aurait reconduit le mécanisme de dérive**, celui-là
   même que la préoccupation n° 7 de r2 avait nommé et que ce défaut réalise.

**Ce que la bascule a exigé de vérifier.** Ces deux grilles n'ont pas de
`caseConfig` — elles déclaraient leur barème par `sectionInfo.push({…})`.
`cases/scoring.js` lit exactement trois champs, `maxScores`, `coef` et
`sectionInfo` : la transposition est un pur changement de forme. Les lignes
`scores["…"] = 0` de la forme impérative sont redondantes (`scoring.js`
réinitialise puis écrase par section). RESCOS-7 déclare sa section
`communication` **sans `isComm`** — ses boutons sont numériques et non
l'échelle A–E ; la forme impérative ne le déclarait pas davantage, le
comportement est donc identique.

`check_reachability.py` lit désormais ces deux grilles par sa branche
`caseConfig` et rend 41/41 à 100 %. **Contrôle de morsure** :
`maxScores.anamnese` de RESCOS-9 forcé à 40 → `ECART · atteignable=41
maxScores=40 affiché=/41`. Le vérificateur mord, donc il valide.

**`configForm`, et pourquoi le baseline est régénéré.** Le champ passe de
`inline` à `caseConfig` sur ces deux grilles. `snapshot_invariants.py` rejoué :
la régénération **ne déplace que ces deux champs sur 41 grilles**.
`criteriaCount`, `detailCount`, `radioCount`, `checkboxCount`, `sectionCounts`,
le nombre de segments par bloc, `boundsAnomalies` et `uncoveredContent` sont
identiques partout — y compris sur RESCOS-15 et RESCOS-35, qui ne bougent pas
d'un champ. Le gel a fait son travail : il a signalé exactement le changement
voulu et rien d'autre.

**Effet de bord mesuré, bénin.** `report_import_defects.py` passe de 96 à 88
`chevron-nu`. Les huit disparus sont des opérateurs JavaScript des moteurs
supprimés (`i <= section.count`, `currentSeconds <= 30`, `currentSeconds <= 0`),
comptés parce que ce rapport balaye le HTML brut, `<script>` compris. Aucune
autre famille ne bouge. Même cause pour les 36 « crochets » que `visible_text()`
voyait dans RESCOS-7 à `0e82963` : des littéraux de tableau JS. Hors `<script>`,
RESCOS-7 porte **0 crochet, avant comme après**.

### 2. RESCOS-15 — la recopie de `redflags` dans `presentation`, réduite

**Modification**

- `presentation` / Touches ludiques / « 👉 Signes d'alarme (Red Flags) » ·
  les cinq `<li>` recopiés mot pour mot du bloc noté (« Méléna », « Modification
  récente du transit après 50 ans », « Occlusion (arrêt gaz/selles,
  distension) », « Perte de poids inexpliquée », « Anémie ferriprive ») →
  trois lignes organisées par mécanisme : « Saigner → visible dans les selles,
  ou occulte et déjà anémiant », « Boucher → arrêt des matières et des gaz,
  ventre distendu », « Retentir → amaigrissement que rien n'explique ».
  source : arbitrage du geste 4 de r4b — les blocs notés restent intouchables,
  seule leur recopie dans `presentation` se réduit.

L'arbitrage demandé par r4a (§ 8.2) avait bien été rendu, au lot r4b, mais
**après** le traitement de cette grille : RESCOS-25, 26 et 28 l'ont reçu, pas
RESCOS-15. Ce lot le lui applique.

**Réduite et non supprimée**, conformément à la lettre de l'arbitrage. Le geste
est aussi un retour au format : les `presentation-subsection` de « Touches
ludiques » du corpus sont des **mnémos** (TVC = 3C, 4P, APPUYER, 3F…), et
RESCOS-15 était la seule des six grilles à `redflags` à y loger une seconde
copie du bloc noté.

**Intouchés** : `redflags`, `expert`, `annexe-dd`, et la clé `N` du mnémo SANG
(« Nouvelle modification du transit après 50 ans »), protégée par la règle du
format.

**Mesure** : RESCOS-15 14 → **10** paires ; corpus 131 → **127** ; paires
`redflags` du corpus 5 → **3**. Les quatre paires retirées sont exactement les
quatre prévues (deux `redflags ↔ presentation`, une `expert ↔ presentation`, une
`annexe-dd ↔ presentation`, toutes issues de la même recopie). **Aucune paire
nouvelle**, dans cette grille ni ailleurs — vérifié en comparant les listes,
pas seulement les totaux.

**`check_no_loss.py 0e82963` signale un item, et c'est un faux positif** :
« occlusion arrêt gaz selles distension ». La ligne de remplacement dit « arrêt
des matières et des gaz, ventre distendu » — le comparateur ne voit pas le
voisinage morphologique parce que deux mots sur quatre changent. Et l'énoncé
subsiste **verbatim dans le bloc noté**, non modifié : « 3. Occlusion
intestinale — Arrêt matières et gaz = urgence chirurgicale potentielle ».

### 3. RESCOS-35 — « activité physique adaptée » restaurée

**Modification**

- `presentation` / § Questions / Q3 « Suivi » · « … et je reprendrais le tabac
  avec elle. » → « … et je reprendrais avec elle la prévention secondaire :
  l'arrêt du tabac, et la reprise d'une activité physique adaptée à son âge et
  à son état. »
  source : `a82e036`, même bloc, même question — « Prévention secondaire :
  arrêt tabac, activité physique adaptée ».

**Le bloc que le contrat désigne est `presentation`** : l'item est la réponse
orale à la question de l'examinateur, et c'est exactement l'endroit d'où la mise
au registre oral l'avait fait tomber. RESCOS-35 ne porte ni `therapy`, ni
`redflags`, ni `annexe-dd` — ses seuls blocs sont `resume`, `expert`, `theorie`,
`presentation` et `scenario`. La restauration remet aussi « prévention
secondaire », qui portait la fonction de l'item.

Aucune paire nouvelle : la seule autre occurrence d'« activité physique » de la
grille est « Activité physique : sédentaire » dans le `scenario`, qui décrit
l'habitude de la patiente et que `report_redundancy.py` exclut par défaut.

### 4. Vérifications

| Porte | Résultat |
|---|---|
| `check_invariants.py` | **OK**, 41 grilles, code 0 (après régénération du baseline, 2 champs `configForm`) |
| `check_nomenclature.py` | **OK**, code 0 |
| `check_reachability.py` | **OK**, 41/41 à 100 % |
| `report_redundancy.py` | **127** (131 avant) |
| `check_no_loss.py 0e82963` | 1 item, faux positif verdicté (§ 2) |
| `report_import_defects.py` | `chevron-nu` 96 → 88, tout le reste inchangé (§ 1) |
| AMBOSS — invariants + redondance | **OK**, **147**, inchangé |

**Navigateur, les 41 grilles.** Chrome for Testing piloté par le protocole
DevTools, WebSocket natif de Node 22, serveur statique sur `127.0.0.1` —
aucun paquet installé, aucune connexion hors boucle locale. Remplissage
**piloté par le DOM** (`checked = true` puis événement `change`, les
gestionnaires `onchange` en ligne font le reste).

| Contrôle | Avant r7 | Après r7 |
|---|---|---|
| Total 100 %, note A | 41/41 | **41/41** |
| Chargement sans exception ni erreur de console | 39/41 | **41/41** |
| `ecos_registry` à `pct: 100, grade: "A"` | 39/41 | **41/41** |
| Minuteur 13:00 → 12:58 (après `switchMode('exam')`) | 41/41 | **41/41** |

Avant/après mesuré sur un **miroir de `0e82963`** servi depuis le scratchpad,
avec le même harnais : RESCOS-7 **16 exceptions → 0**, RESCOS-9 **51 → 0**, et
`ecos_registry` **absent → présent** pour les deux. `ecos_registry` n'est écrit
qu'à un seul endroit du projet, `cases/scoring.js:804` dans `saveToRegistry()` :
l'apparition de ces deux entrées ne peut venir que du chargement du moteur
partagé.

Une seule grille rend zéro crochet coloré, **RESCOS-7, et c'est correct** :
hors de ses `<script>`, elle ne porte aucun `[…]` — station d'annonce de
mauvaise nouvelle, quinze critères de communication purs.

### 5. Préoccupations

**5.1 — Le mode circuit et la barre de navigation s'activent sur deux stations
qui ne les avaient jamais eus.** C'est la contrepartie assumée de la bascule :
RESCOS-7 et RESCOS-9 se comportent désormais comme les 39 autres. Le contrôle
en navigateur a été mené hors mode circuit (`ecos_circuit` absent du
`localStorage`), c'est-à-dire dans la branche `else` de `DOMContentLoaded` —
**le parcours circuit de ces deux grilles n'a pas été exercé de bout en bout.**
Il devrait maintenant fonctionner, puisqu'il est celui du fichier partagé ;
il n'est pas mesuré.

**5.2 — `check_reachability.py` garde une branche devenue morte.** Sa fonction
`parse_config` lisait la forme impérative en repli quand `caseConfig` ne rendait
aucune section. Plus aucune grille RESCOS n'emprunte ce chemin. Je l'ai
**laissée en place** : la retirer serait un geste sur l'outillage sans rapport
avec le mandat, et elle documente une forme que le corpus a portée. À signaler
si une passe de nettoyage de `scripts/rescos/` est ouverte.

**5.3 — Les figures d'import du § 7 de la procédure sont périmées depuis
avant ce lot.** `PROCEDURE-rescos.md` et l'en-tête de
`report_import_defects.py` annoncent 114 `chevron-nu`, 13
`comparaison-manquante` et 1 `numeration-implicite` : ce sont les valeurs à
`a82e036`. À `0e82963` le corpus était déjà à 96 / 12 / **0** — la numération
implicite « plaquettes 422 » a été corrigée en cours de campagne sans que la
figure de tête soit reprise. Ce lot amène 88 / 12 / 0. **Non corrigé dans la
procédure** : c'est un fichier de méthode partagé avec les autres volets, et le
mandat ne l'ouvre pas.

**5.4 — La règle qui protège `therapy` et `redflags` reste ambiguë sur les
recopies.** Telle qu'écrite au pilote (« une paire dont un côté est `therapy`
ou `redflags` n'est pas une redondance à retirer »), elle protège aussi bien
l'accord voulu entre le noté et le pédagogique que la **recopie pure** du noté
dans le pédagogique. C'est ce qui a laissé RESCOS-15 passer quatre lots. Le
geste 4 de r4b a tranché en pratique, pour `therapy` ; ce lot l'étend à
`redflags`. **La règle du § 3 de `PROCEDURE-rescos.md` n'a pas été récrite** —
même motif qu'en 5.3. Elle gagnerait la précision : *le pédagogique s'aligne
sur le noté, il ne le recopie pas.*
