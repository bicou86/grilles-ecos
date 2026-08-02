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
