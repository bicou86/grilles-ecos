# Refonte du contenu pédagogique des 40 grilles AMBOSS — Design

Date : 2026-07-30 · Statut : design validé, implémentation à planifier

## Problème

Les blocs pédagogiques des 40 grilles `cases/amboss/*.html` répètent la même information à
plusieurs endroits, avec des formulations divergentes. Leur nomenclature mélange usages
français, américains et suisses. Leurs prises en charge n'ont jamais été confrontées à un
référentiel suisse.

Mesures sur le corpus :

- Le pédagogique pèse **54 %** du texte visible (337 634 caractères sur 628 374).
- **280 paires** d'items de liste quasi identiques (similarité > 0,72) entre blocs
  différents, sur 5 168 items analysés.
- Recouvrement lexical inter-blocs de **31 % à 47 %**.
- `NFS` (86 occurrences) coexiste avec `FSC` (77) dans le même corpus.

## Référentiel

Le vault Obsidian `~/Documents/Damien/Medecine/Obsidian` fait autorité, en particulier les
135 pages `SSP ECOS/*.md`. Elles sont déjà suissifiées : `FSC`, `crase (TP, INR, aPTT)`,
`stix + sédiment urinaire`, `métamizole (Novalgine®)`, alerte **144**, `Hb seuil ≈ 70 g/L`,
« Rx ASP : indication limitée en Suisse », SSMI/SGAIM cité nommément.

`docs/obsidian-mapping.yaml` relie **40/40 grilles AMBOSS** à leur page SSP. La paire
**(grille, page SSP)** est donc l'unité de travail, déterminée d'avance.

Aucune source externe n'est consultée : le travail est strictement local.

## Périmètre

### Inclus

- Réduction des répétitions dans les blocs pédagogiques existants.
- Nomenclature médicale suisse, dans les blocs pédagogiques **et** dans les sections notées.
- Alignement des prises en charge sur la page SSP correspondante, **dans les blocs
  pédagogiques uniquement**.

### Exclu

- **Items ICE** : hors périmètre sur décision explicite. Le sous-item « Recherche des
  préoccupations et questions du patient » du critère `m4` (section Management, 40/40
  grilles) reste en place, malgré son recoupement avec le critère `c1` de la section
  Communication.
- **Création de blocs manquants** : les 15 grilles sans `resume` ni `presentation`
  (n° 10, 16, 17, 20, 21, 23, 24, 25, 26, 27, 29, 32, 33, 36, 40) ne reçoivent aucun
  contenu nouveau. Elles bénéficient de la nomenclature et de la vérification des PEC dans
  `annexe-expert` / `annexe-theorie`. AMBOSS-34 possède un `resume` mais pas de
  `presentation` : on ne crée pas le bloc absent.
- **Marqueurs culturels non médicaux** : noms de patients, lieux (Yosemite, New York),
  sociétés savantes américaines (AHA/ACC, AAP) restent inchangés.
- **Barème des sections notées** : aucun ajout ni retrait de sous-item noté.

## Inventaire des blocs

| Bloc | Sous-sections fixes | Grilles |
|---|---|---|
| `annexe-expert` | Rôles et interventions · Points clés · Pièges | 40 |
| `annexe-theorie` | Diagnostic le plus probable · [sections libres] · Examens complémentaires · Rappels thérapeutiques | 40 |
| `resume` | Anamnèse · Examen clinique · Examens diagnostiques · Prise en charge · Points clés ECOS · Check-list rapide | 25 |
| `presentation-patient` | Checklist mentale · Version longue · Version express SBAR · Mnémos · Questions examinateur | 24 |

Grilles avec `resume` : 1–9, 11–15, 18, 19, 22, 28, 30, 31, 34, 35, 37, 38, 39.
Grilles avec `presentation` : les mêmes, sans 34.
Grilles avec `presentation`/Pièges ECOS : 1, 2, 3, 5, 6, 9, 11, 12, 13, 14, 30, 38, 39 (13).

## Contrat de blocs

Chaque bloc a un rôle exclusif. C'est la règle qui empêche la redondance de revenir.

| Bloc | Rôle exclusif | Porte | Ne porte jamais |
|---|---|---|---|
| `annexe-expert` | Faire tourner la station | Résultats à délivrer sur demande, points de notation, pièges du candidat | Théorie, listes d'apprentissage |
| `annexe-theorie` | Comprendre le cas | Diagnostic et argumentaire, physiopathologie, DD avec discriminants, valeurs de tests (Se/Sp) | Check-lists actionnables, mnémos, protocoles de traitement |
| `resume` | Réviser vite | Source canonique unique : anamnèse, examen, examens, PEC, suivi | Redites de la théorie, formats oraux |
| `presentation-patient` | Restituer à l'oral | Version longue, SBAR, mnémos, réponses aux questions d'examinateur | Toute donnée clinique nouvelle |

### Règle du format

Une information peut réapparaître **si et seulement si elle change de format de
restitution** (liste → narration, liste → SBAR, liste → question d'examinateur).

Même format + même contenu = suppression.

Cette règle est décidable paragraphe par paragraphe et vérifiable après coup, ce qui rend
la passe reproductible.

### Résolution des 7 axes de redondance

| # | Information | Écrite dans | Décision |
|---|---|---|---|
| 1 | Examens complémentaires | `resume` + `theorie` + `presentation` | `resume` canonique. `theorie` garde le *pourquoi* (Se/Sp, seuils, indications), pas la liste. `presentation` garde sa Q/R — c'est un format oral distinct — mais sa réponse doit être un sous-ensemble strict de `resume`, sans item absent de celui-ci ni formulation divergente |
| 2 | Traitement / PEC | `resume` + `theorie` + `presentation` | `resume` canonique. `theorie`/Rappels thérapeutiques garde le rationnel. `presentation` garde sa réponse orale, sous-ensemble strict de `resume` |
| 3 | PEC condensée | `resume`/Prise en charge + `resume`/PEC en 3 points | Les deux niveaux restent. La check-list devient un **sous-ensemble strict** : aucune information absente au-dessus, aucune formulation contradictoire |
| 4 | Examens à faire | `resume`/Examen clinique + `resume`/Examens à faire | Idem axe 3 |
| 5 | Questions d'anamnèse | `resume`/Questions à poser + `presentation`/Checklist mentale | `presentation`/Checklist mentale reste une **trame de présentation** (Intro → caractériser → … → PEC), pas une liste de questions cliniques |
| 6 | Pièges | `expert`/Pièges + `presentation`/Pièges ECOS | `expert` canonique (40/40 grilles). `presentation`/Pièges ECOS supprimé sur les 13 grilles concernées |
| 7 | Points clés | `expert`/Points clés + `resume`/Points clés ECOS | Les deux restent, différenciés : `expert` = ce que l'examinateur observe · `resume` = ce que l'étudiant retient |

### Défauts ponctuels à corriger

- AMBOSS-1 et AMBOSS-2 : le titre `<h4>Examens complémentaires</h4>` apparaît **deux fois**
  dans `annexe-theorie`. Fusionner les deux sections.

## Passe nomenclature

Remplacements 1 pour 1, applicables aux blocs pédagogiques **et** aux sections notées.
Aucun ne modifie le nombre de sous-items, donc aucun ne déplace le barème.

### Médicaments — 9 occurrences, 4 grilles

| Actuel | Suisse | Grilles |
|---|---|---|
| Vicodin | Tramadol (Tramal®) | 39 |
| Tylenol | Paracétamol (Dafalgan®) | 7, 9 |
| Tums | Antiacides (Rennie®) | 22 |

Vicodin est de l'hydrocodone/paracétamol, non commercialisé en Suisse. AMBOSS-9 mentionne
« trois comprimés de 500 mg » : le dosage reste valide avec Dafalgan.

### Laboratoire

| Actuel | Suisse | Occurrences |
|---|---|---|
| NFS | FSC | 86 (68 pédagogique, 18 grille notée) |
| CBC | FSC | 1 (AMBOSS-33, légende d'image) |
| BMP | Chimie sanguine | 1 (AMBOSS-33, légende d'image) |

Le vault emploie 111 `FSC` pour 59 `NFS`, et `FSC` exclusivement dans les tableaux
d'examens des pages SSP. `FSC` est donc la forme cible.

Les 18 occurrences en zone notée sont toutes dans des `detail-text criteria-detail`,
jamais dans un `.criteria-text` ni dans un attribut `data-criteria`.

### Unités → SI — 4 occurrences

| Actuel | Suisse | Grille |
|---|---|---|
| Créatinine 1,8 mg/dL | 159 µmol/L | 21 |
| C3 45 mg/dL (N 90–180) | C3 0,45 g/L (N 0,9–1,8) | 21 |
| C4 25 mg/dL (N 10–40) | C4 0,25 g/L (N 0,1–0,4) | 21 |
| « 85 µmol/L (5 mg/dL) » | retirer la parenthèse en mg/dL | 37 |

### Numéro d'urgence — 2 occurrences

`911` (AMBOSS-28) et `SAMU` (AMBOSS-35) → **144**.

Le vault emploie 144 à 405 reprises et n'écrit jamais 911.

`112` n'est **pas** remplacé : sa seule occurrence dans le corpus est
`Score Global 0/112` (AMBOSS-8), un total de barème et non un numéro d'urgence.
Un remplacement automatique corromprait la grille.

## Passe par grille

Pour chaque paire (grille, page SSP) issue de `docs/obsidian-mapping.yaml` :

1. **Lire** la plage pédagogique de la grille via `offset`/`limit` — jamais le fichier
   entier — et la page SSP correspondante.
2. **Dédoublonner** selon le contrat et la règle du format.
3. **Aligner les PEC** des blocs pédagogiques sur la page SSP : examens, traitements,
   seuils, orientation.
4. **Journaliser** chaque modification médicale et chaque divergence non traitée.

### Aligner ou consigner

L'étape 3 ne s'applique que lorsque la page SSP **couvre explicitement** le point. Trois cas :

| Situation | Action |
|---|---|
| La page SSP traite le point et la grille en diverge | Aligner la grille sur la page SSP, journaliser avec la ligne source |
| La page SSP ne traite pas le point | Laisser la grille inchangée. Ne rien inventer |
| La page SSP contredit la grille sur un fond non tranchable sans avis clinique | Laisser inchangé, consigner au journal pour arbitrage |

### Cas particulier AMBOSS-15

AMBOSS-15 (douleur abdominale chronique, garçon de 6 ans) ne figure pas dans la section
`pages:` de `docs/obsidian-mapping.yaml` mais dans sa liste **`unmapped:`**, avec la
raison « douleur abdominale pédiatrique — page pédiatrique à créer ». Elle n'a donc
aucune page de référence.

Pour cette grille, seules la nomenclature et le dédoublonnage s'appliquent ; l'alignement
des PEC est reporté et consigné au journal, avec la liste des zones restées sans arbitre,
pour que l'utilisateur puisse décider d'un rattachement.

*Correction du 2026-07-31 : une version antérieure de cette spec la disait rattachée à
`Skills — Réflexes Médicamenteux & Antidotes.md`, qui ne porte en réalité que deux grilles
RESCOS. L'erreur venait du script d'analyse initial. La conséquence opératoire est
identique — pas de page de référence — mais le motif diffère : la page n'existe pas encore,
elle n'est pas inadéquate.*

### Contrainte de lecture

Les fichiers font jusqu'à 2,77 Mo, dont ~95 % d'images base64 (`AMBOSS-21` : 2 770 741
octets bruts contre 95 145 hors base64). Les lire entièrement est impraticable. Les blocs
pédagogiques occupent une plage de lignes contiguë, de `<div class="resume">` (ou
`<div class="annexes">` si absent) à `<div class="annexe-item annexe-scenario">`.

### Journal

Un fichier de suivi, relu par l'utilisateur, consigne :

- chaque modification de prise en charge, avec la ligne de la page SSP qui la justifie ;
- chaque divergence repérée dans une **section notée** — non corrigée, puisque le barème
  est gelé — pour arbitrage ultérieur.

Exemple de divergence à consigner : une grille qui note `Rx ASP` alors que la page SSP
correspondante indique « indication limitée en Suisse — remplacée par le CT en cas de
doute ».

## Invariants techniques

| Invariant | Source | Conséquence |
|---|---|---|
| `.criteria-text` garde le format `N. Libellé [réponse]` | `cases/scoring.js:159` fait `.split(". ")[1].split(" [")[0]` | ne jamais retirer la numérotation ni les crochets |
| Les réponses patient restent entre crochets | `cases/scoring.js:290` les colore au chargement | ne pas supprimer les crochets |
| `maxScores` et `<span class="score">…/N</span>` doivent concorder | `window.caseConfig` en fin de fichier | interdit de modifier le nombre de sous-items notés |
| `data-criteria` prime sur le texte | `cases/scoring.js:152` | aucun ne contient de terme à corriger |

Les blocs pédagogiques ne sont lus par aucun script : `scoring.js`, `persistence.js`,
`srs.js` et `index.html` n'y accèdent pas. Leur modification est sans risque fonctionnel.

## Vérification

Après chaque étape :

1. **Barèmes inchangés** — extraire `caseConfig.maxScores` et les `<span class="score">`
   des 40 grilles avant et après, comparer. Toute différence est un bug.
2. **Structure HTML** — nombre de `<div>` ouvertes et fermées cohérent ; blocs attendus
   toujours présents (`resume` sur 25 grilles, `presentation` sur 24, `expert` et
   `theorie` sur 40).
3. **Nomenclature** — `grep` de contrôle : zéro `NFS`, `Vicodin`, `Tylenol`, `Tums`,
   `mg/dL`, `911`, `SAMU`, `112` dans `cases/amboss/`.
4. **Règle du format** — relancer la détection de paires quasi identiques ; le compte doit
   baisser nettement par rapport aux 280 de départ, et les paires restantes doivent toutes
   correspondre à un changement de format documenté.

## Séquencement

| Étape | Contenu | Commit |
|---|---|---|
| 1 | Passe nomenclature sur les 40 grilles | un commit |
| 2 | Grille pilote : AMBOSS-1 contre `SSP — Douleur Abdominale` | un commit, **validation utilisateur avant la suite** |
| 3 | Les 39 grilles restantes | un commit par lot de 5 grilles, dans l'ordre des numéros |

Le pilote AMBOSS-1 est choisi parce qu'il cumule les défauts observés : `h4` dupliqué,
6F trois fois, Murphy trois fois, pièges deux fois, et une page SSP de référence dense
(58 Ko).

Tout le travail est local. Aucun `git push`, aucune publication.

## Risques

| Risque | Traitement |
|---|---|
| Perte d'information pédagogique en dédoublonnant | La règle du format protège les reformulations utiles (SBAR, version longue). Le pilote est validé avant généralisation |
| Modification médicale erronée | Toute PEC modifiée est tracée à une ligne de page SSP dans le journal |
| Corruption HTML sur de gros fichiers | Édition par remplacement exact de chaîne, jamais de réécriture complète ; vérification structurelle après chaque étape |
| Barème silencieusement décalé | Barème gelé par décision de périmètre + vérification automatique avant/après |
| Page SSP en désaccord avec la grille sur un point non tranché | Consigné au journal, non corrigé unilatéralement |
