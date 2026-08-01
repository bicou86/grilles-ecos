# Arbitrage des 39 points en attente — grilles AMBOSS

Date : 2026-08-01 · Mandat : « Traite les 39 points d'arbitrage en changeant le mapping
d'AMBOSS-37 à ictère néonatal et élargis le périmètre sur la zone `annexe-dd`. Je te laisse
trancher toi-même les autres points de la façon la plus logique. »

Ce document trace **chaque décision et son motif**, pour que chacune puisse être contestée
séparément. Les points sont regroupés par nature de décision, non par numéro d'origine.

## Décision de cadrage : le gel du barème est levé, sous conditions

La majorité des points en attente vivent dans des **sections notées**, gelées depuis le
début du projet. Les traiter suppose d'y toucher. Le mandat le demande explicitement.

Le gel est donc remplacé par trois règles :

1. **Correction typographique ou factuelle sans changement de structure** — autorisée sans
   condition. Ne modifie ni le nombre de sous-items, ni les cases, ni `maxScores`.
   `check_invariants.py` reste vert. (Précédent : les 14 textes mutilés du commit `ce250fd`,
   déjà autorisés.)
2. **Ajout ou retrait d'un sous-item noté** — autorisé, mais impose le recalcul synchronisé
   de `window.caseConfig.maxScores` **et** du `<span class="score">…/N</span>`, puis une
   vérification que les deux concordent. Le snapshot de référence est régénéré et la
   différence justifiée ligne à ligne.
3. **Ce qui relève du jugement d'auteur** — reste non corrigé et documenté. Trois cas
   seulement, listés en fin de document.

## Groupe 1 — Décisions explicites du mandat

### 1.1 Mapping d'AMBOSS-37 → « SSP — Ictère Néonatal »

`docs/obsidian-mapping.yaml` rattache cette station d'**ictère néonatal** à
`SSP — Éruption Cutanée`, page de dermatologie qui ne contient aucune occurrence
d'« ictère », « bilirubine », « nouveau-né », « Coombs » ni « photothérapie » sur ses
498 lignes. Le vault possède `SSP — Ictère Néonatal`, jusqu'ici rattachée à la seule
USMLE-18 (garçon de 5 jours, même tableau à un jour près).

**Décision** : corriger le mapping, puis réaligner AMBOSS-37 sur la bonne page. L'alignement
provisoire de la tâche 12 avait déjà cité cette page en le signalant ; il devient régulier.

### 1.2 Élargissement du périmètre à `annexe-dd`

Le bloc `annexe-dd` (« Diagnostics différentiels à considérer », arguments POUR/CONTRE et
examens) est présent dans les **40 grilles**, ~1 800 caractères chacune, soit ~70 000
caractères. Il est situé **à l'intérieur** de la section Management, donc hors de la zone
pédagogique définie par `peda_bounds`. Son contenu n'est pas noté (aucune case).

Double invisibilité : il emploie des puces textuelles `•` et non des `<li>`, donc
`list_items` — et par conséquent `report_redundancy` et `check_no_loss` — ne le voit pas.

Mesure : **130 duplications sur 33 grilles** entre ce bloc et la zone auditée.

**Décision** : étendre le périmètre. Cela suppose, dans l'ordre :

1. étendre `lib_amboss` pour reconnaître le bloc et ses puces textuelles ;
2. régénérer le snapshot et mesurer la redondance réelle du corpus ;
3. traiter les 40 grilles selon le contrat de blocs.

**Rôle du bloc dans le contrat** : `annexe-dd` porte le **raisonnement différentiel** —
quelles hypothèses, quels arguments pour et contre, quel examen les départage. C'est une
extension naturelle du rôle d'`annexe-theorie` (comprendre le cas). Il ne doit donc porter
ni check-list actionnable, ni conduite de station, ni formulation orale.

## Groupe 2 — Défauts d'import du corpus source (correction typographique)

Ces défauts partagent une cause unique, identifiée en tâche 12b : **l'import tronque les
mots au niveau du `x`**, absorbant les lettres jusqu'au chiffre suivant — `Ceftria|xone`,
`Amo|xicilline`, `Céfo|xitine`, `Ciproflo|xacine`, `Ma|ximum`, `ma|ximale`.

### 2.1 Signes de comparaison manquants — 14 occurrences, 10 grilles

`SpO2 92%`, `IMC 25 kg/m²`, `sténose 70%`, `résidu 1cm`, `perte poids 5%`, `perte 10% poids`,
`fibromes sous-muqueux ou 4cm`, `lévothyroxine … si 50 ans`, `INR 1.7`, `si 4.5h du début`.

**Décision : corriger.** Le sens est univoque dans chaque cas et l'ambiguïté est dangereuse —
« oxygénothérapie si SpO2 92% » s'inverse selon le signe. Correction typographique pure :
aucun sous-item ajouté ni retiré.

### 2.2 Noms de molécules tronqués — 4 occurrences

- `Ceftria: 2g` → déjà restitué en `Ceftriaxone` (tâche 12b), validé par le contexte.
- **AMBOSS-2** `Amo: 2g IV`, `Céfo: 2g IV + métronidazole`, `Ciproflo: 400 mg IV`.

**Décision : corriger, avec le protocole suisse d'antibioprophylaxie de l'appendicectomie
comme arbitre.** Les trois lignes forment un bloc « 1ʳᵉ intention / alternative / si
allergie » : elles se lisent ensemble. `Ciproflo` ne peut être que la ciprofloxacine.
Pour `Amo` et `Céfo`, l'implémenteur devra trancher sur le contexte du bloc — association
au métronidazole, dose, place dans la séquence — et **signaler s'il ne peut pas conclure**
plutôt que de deviner.

- **AMBOSS-39** `Ma: • Maximum 3 injections/an` : réparer supposerait de supprimer une
  puce. **Décision : corriger en fusionnant le fragment orphelin avec la puce suivante**,
  ce qui retire un élément de liste sans toucher à un sous-item noté — à vérifier par
  `check_invariants`.

### 2.3 Contenu étranger à la vignette — 2 occurrences

- **AMBOSS-39** : « antiviraux action directe », vocabulaire d'hépatite C dans une station
  de rupture de coiffe des rotateurs. **Décision : retirer.** Aucun rapport avec le cas.
- **AMBOSS-38** : « Vitamine D 800-1000 UI/j » dupliqué dans la même puce, raccordé par un
  `×` parasite. **Décision : déduplicer.**

### 2.4 AMBOSS-9 — barème inatteignable

`caseConfig` déclare `count: 13` et `anamnese: 53` ; la page ne contient que 12 critères
totalisant 49 points. Le score plafonne à 98 %. Défaut présent dès la première version.

**Décision : ramener `maxScores.anamnese` à 49 et `count` à 12.** C'est la seule correction
qui n'invente rien. Écrire le 13ᵉ critère supposerait de créer du contenu médical noté que
personne n'a rédigé, et d'en fixer arbitrairement la valeur. Le `<span>` et le snapshot
sont mis à jour en conséquence.

## Groupe 3 — Erreurs médicales en section notée (correction de fond)

Chacune est corrigée en citant sa source. Toutes sont préexistantes.

| # | Grille | Défaut | Décision |
|---|---|---|---|
| [3] | 14 | Bêtabloquant « si pas de CI » dans un spasme coronaire aux amphétamines | **Corriger** : contre-indication ajoutée (effet alpha non opposé) |
| [15] | 8 | 5-ASA pour la maladie de Crohn | **Corriger** : rendement établi dans la RCH, pas dans le Crohn |
| [18] | 11 | Acide tranexamique 1 g IV dans l'hémorragie digestive | **Corriger** : HALT-IT (2020) — aucun bénéfice, excès thrombo-embolique |
| [19] | 11 | Sérologie H. pylori | **Corriger** : rendement inférieur aux tests actifs (antigène fécal, test respiratoire) |
| [20] | 22 | Transit baryté en 1ʳᵉ intention | **Corriger** : l'endoscopie prime ; la page SSP et les pièges de la grille le disent déjà |
| [22] | 34 | Aspirine 325 mg | **Corriger** : forme non commercialisée en Suisse → 160–300 mg |
| [25] | 35 | « Oxygène si SpO2 94% » | **Corriger** vers < 90 % : doctrine du corpus et de la page SSP |
| [30] | 26 | Prophylaxie migraineuse à ≥ 4 crises/mois ; ibuprofène 600–800 mg | **Corriger** : ≥ 3 invalidantes ; 400–600 mg (800 mg n'existe pas en Suisse) |
| [16] | 9 | « Conseil sur les pratiques sexuelles sûres » dans une lombalgie du sujet de 71 ans | **Retirer** : résidu d'une autre station, sans lien avec la vignette |
| [12] | 4 | « Dernières règles il y a 2 ans » + « ménopause à 45 ans » chez une patiente de 50 ans | **Corriger** : porter les dernières règles à 5 ans pour concorder |
| [38] | 13 | Seuil « > 2cm ou > 15% » sur une station de pneumothorax traumatique | **Corriger** : restreindre au spontané, conformément à `theorie` |
| [39] | 13 | Mesures d'accompagnement rangées sous « Pneumothorax bilatéral ou sous tension » | **Corriger** : réordonner sous le bon intitulé |
| [28] | 17, 16 | MMSE demandant le « président des États-Unis » et l'« État » ; « directives AHA/ACC 2017 » | **Suissifier** : Conseil fédéral et canton ; société savante suisse ou formulation neutre |
| [29] | 25 | `expert` dit « IRM : LCL intact » quand la section notée cote le traitement d'une rupture | **Corriger `expert`** : aligné en tâche 14, à confirmer |

## Groupe 4 — Alignements sur les référentiels actuels

| # | Grille | Décision |
|---|---|---|
| [7] | 31 | Dépistage CT : **corriger** en 50–80 ans + 20 PA (USPSTF 2021), en précisant qu'il n'existe pas de programme organisé en Suisse |
| [8] | 19 | GOLD A/B/C/D → **ABE** (2023), conformément à la page SSP. Impose un retrait de sous-item : recalcul synchronisé |
| [9] | 18, 19 | Palier 1 GINA → **CSI-formotérol à la demande** ; mMRC décrit comme graduant l'effort, non « au repos » |
| [14] | 6 | Élagolix : déjà aligné sur la section notée (leuprolide). **Confirmé** |
| [4] | 14 | Troponine « positive à 3 h » avec diagnostic d'angor instable | **Corriger** : angor instable = troponine négative. Aligner la valeur du scénario |
| [10] | 14 | « 20 ng/L (limite normale) » alors que le seuil hs suisse est 14 ng/L | **Corriger** : ramener la valeur initiale sous 14 ng/L, cohérent avec [4] |
| [33] | 29 | Aucun résultat d'hémogramme ni de bilan martial alors que la branche anémie est notée | **Ajouter au scénario** une hémoglobine et une ferritine cohérentes avec le tableau — sinon la station est injouable |

## Groupe 5 — Le vault, pas les grilles

Ces points concernent le référentiel. **Décision : les signaler dans le rapport, ne rien
modifier dans le vault** — il appartient à l'utilisateur et sert d'autres corpus.

- [11] Notation des D-dimères : le vault écrit `ng/mL`, les grilles `µg/L`. Mêmes nombres.
- [23] `SSP — Mal de Gorge` se contredit sur l'éviction sportive après MNI (4–6 vs 3–4 semaines) ;
  `SSP — Amaurose` sur la fenêtre de l'OACR (< 6 h en frontmatter vs < 90 min dans le corps).
- [31] `SSP — Capacité de Discernement` fonde le droit d'aviser sur `CP art. 364`,
  vraisemblablement absorbé par les art. 314c-314d CC en 2019.
- [2] et [6] Portée insuffisante de `SSP — Douleur Abdominale` (versant oncologique
  d'AMBOSS-3) et de `SSP — Douleur Thoracique` (pneumothorax traumatique, toxicité
  sympathomimétique).

## Groupe 6 — Outillage et documentation

- [34] Trois unités implicites hors hémogramme (ASAT/ALAT, Na) → **balayage et conversion**.
- [37] `report_redundancy.py` ignore les paires intra-bloc (`if b1 == b2: continue`) →
  **ajouter un mode intra-bloc** et mesurer, sans le rendre bloquant.
- [32] AMBOSS-23, remboursement des appareils auditifs « variable selon pays/assurance » →
  **suissifier** : forfait AI/AVS.
- [21], [24], [26], [27] : traités au groupe 2.
- [1], [5], [17], [35], [36] : traités aux groupes 2 et 3.

## Ce qui reste non corrigé, et pourquoi

Trois points relèvent du jugement d'auteur et ne peuvent être tranchés sans réécrire le cas :

1. **AMBOSS-3** — le versant oncologique (chimiothérapie, thérapies ciblées, prophylaxie
   BRCA) n'a aucune page de référence. Un rattachement complémentaire serait plus solide
   qu'un arbitrage de notre part.
2. **AMBOSS-15** — figure dans `unmapped:` du mapping, raison « page pédiatrique à créer ».
   Reste sans alignement de prise en charge tant que la page n'existe pas.
3. **AMBOSS-24 et 32** — les contenus de protection (violences domestiques, mineure) ont
   été enrichis mais jamais déduplicés : le coût d'une répétition y reste inférieur à celui
   d'une omission. C'est un choix assumé, pas un oubli.
