# Refonte pédagogique des 165 grilles ECOS `rescos-locales` — rapport de vérification finale

Corpus `cases/rescos-locales`, branche `refonte-amboss-suisse`, base d'import
`7c77e3e`, état vérifié `45e0986`. **165 grilles** — 156 stations notées et
9 feuilles porte. C'est le quatrième et le plus gros des corpus du projet après
CasECOS, et le seul dont aucune grille ne remontait son score au tableau de bord.

Onze lots (`l2` à `l6b`, puis `t1` à `t5`), treize commits, **156 grilles
modifiées sur 165** — les 9 feuilles porte n'ont rien reçu, elles n'en avaient
pas besoin.

---

## 0. Résultat des six vérifications

**Aucune des six vérifications n'échoue.** Les trois portes sortent en code 0,
le barème ne porte que les divergences admises, la structure est intacte sur les
165, et le contrôle en navigateur ne lève aucune exception.

| # | vérification | résultat |
|---|---|---|
| 1 | les sept vérificateurs sur les 165 | **code 0** — invariants, nomenclature, atteignabilité ; `bounds_anomalies` et `uncovered_content` vides sur les 165 |
| 2 | barème, 14 champs × 165 grilles vs `7c77e3e` | **313 divergences sur 2310, toutes admises** — 156 `engineFingerprint`, 156 `configForm`, 1 `coef` (RESCOS-63). **Aucune autre.** |
| 3 | intégrité structurelle des 165 | **0 problème** — `</html>` final 165/165, balises appariées 165/165, blocs conformes au snapshot, **464 crochets `[…]` de `cloture` avant et après** |
| 4 | redondance inter-blocs | **1258 → 1003** (−255, −20,3 %). Témoins AMBOSS **147**, RESCOS **127** — inchangés |
| 5 | non-perte (`check_no_loss 7c77e3e`) | 423 items signalés sur 87 grilles, **verdictés : aucune perte réelle** ; 9 items à couverture lexicale < 0,55 relus un à un et retrouvés |
| 6 | navigateur, `--deep`, 165 grilles | **0 exception**, 165/165 sans erreur, **156/165 à 100 %**, **`ecos_registry` 156/165**, minuteur 156/165, barre nav 156/165, **0 recouvrement**, RESCOS-63 **100 %, note A** |

Les témoins ont été relevés dans des **interpréteurs séparés**, un par corpus.
C'est une précaution mesurée, pas une formalité : voir § 7.7.

### Ce que cette vérification a trouvé, et qui n'est pas corrigé

Le mandat était de vérifier, pas de retoucher. Cinq constats sont sortis du
balayage final ; **aucun n'invalide une vérification**, et aucun n'a été réparé.

1. **`Enfant qui boîte` qualifie une CRP à 20 mg/l de « normale » en cinq
   endroits, dont un sous-item noté** — alors que le lot `t3` a corrigé
   *un seul* de ces endroits, dans l'`annexe-dd`, et y a écrit noir sur blanc
   « elle n'est pas normale (norme 5-10 mg/l) ». La grille se contredit
   maintenant avec elle-même, et c'est la version fausse qui est majoritaire.
   Détail au § 3.D.
2. **`AMC Urgences 3B` prescrit des dérivés nitrés dans deux sous-items notés
   avec la tension pour seul garde-fou**, sans une occurrence de « ventricule
   droit », « V3R » ni « V4R ». C'est la **quatrième occurrence** du motif que
   trois lots ont corrigé ailleurs, et aucun ne l'a vue ici. Détail au § 3.A.
3. **La ranitidine est présente sur deux grilles, pas une.** Le lot `t5` a
   consigné celle d'`Urticaire allergique` ; `Choc anaphylactique` en porte une
   seconde, « Anti-H2 [ranitidine 50mg IV] », **dans un sous-item noté**.
   La molécule est retirée du marché mondial depuis 2020.
4. **29 valeurs en unité « litre minuscule »** (`mmol/l`, `g/l`, `mg/l`,
   `µmol/l`, `UI/l`) sur **9 grilles**, et **8 gaz du sang en mmHg** sur
   **4 grilles** — la plupart dans des sous-items notés. `check_nomenclature`
   rend 0 : il borne les **analytes**, pas les **unités**. Angle mort mesuré,
   déjà signalé par `l6b` sur 11 occurrences ; le balayage élargi en trouve 37.
5. **`Pédiatrie — État fébrile sans foyer` range « pas de boiterie » et « pas de
   douleur osseuse localisée » en arguments CONTRE l'arthrite septique et
   l'ostéomyélite**, chez un nourrisson fébrile sans foyer. C'est la famille du
   défaut que `t4` a corrigé sur `Nourrisson 6 mois avec fièvre`. Candidat à
   relire — il n'est pas aussi net que les trois occurrences corrigées, et je
   n'ai pas tranché.

---

## 1. Ce qui a été fait

### Chiffres

| | avant (`7c77e3e`) | après (`45e0986`) |
|---|---:|---:|
| grilles | 165 | 165 |
| exceptions JavaScript par remplissage complet | **13 446** | **0** |
| grilles écrivant **leur** entrée dans `ecos_registry` | **0 / 165** | **156 / 165** |
| grilles à 100 % après remplissage complet | 155 / 156 | **156 / 156** |
| erreurs 404 (images) | 92 | **0** |
| termes non suisses (`check_nomenclature`) | **368 relevés / 424 réels**, 108 grilles | **0** |
| mot `undefined` affiché au lecteur | **57**, sur 48 grilles | **0** |
| redondance inter-blocs | **1258** | **1003** |
| items de contenu pédagogique | 19 168 | **20 147** (+979) |
| poids hors base64 | 27,2 Mo | 22,4 Mo |
| témoins AMBOSS · RESCOS | 147 · 127 | **147 · 127** |

Le poids baisse de 4,8 Mo alors que le contenu augmente de 979 items : ce sont
les 156 copies du moteur de calcul, environ 35 800 caractères de JavaScript par
grille, remplacées par un `<script src="../scoring.js">`.

**La passe de nomenclature a porté sur 424 termes, pas 368.** L'inventaire
initial en manquait 56, dans trois familles : six familles entières absentes de
la table (`ERCP` 9, `MRCP` 7, `BSA` 4, `COPD`, `SLE`, `QD`), les graphies
minuscules d'unités (`ng/ml` — **plus fréquente que `ng/mL`** —, `pg/ml`,
`g/dl`, `mEq/l`), et la casse (`Gold standard` capitalisé, 8 des 41). Toutes les
conversions d'unité ont été décidées par l'**analyte**, jamais par l'unité de
départ : les 14 `ng/mL` se répartissent en trois facteurs différents, et la seule
troponine change d'ordre de grandeur.

### Le travail par lot

| lot | périmètre | redondance | erreurs corrigées | trous du canonique comblés |
|---|---|---:|---:|---:|
| `l2` | outillage, **0 grille modifiée** | 1258 (mesure) | — | — |
| `l3` | les 4 défauts structurels, 165 grilles | 1258 → 1258 | — | — |
| `l4` | nomenclature, 108 grilles | 1258 → 1260 | 424 termes | — |
| `l5` | RESCOS-58b, pilote | 1260 → 1233 | 2 | 1 |
| `l6a` | RESCOS-41 à 55 | 1233 → 1147 | 5 | 7 (+3) |
| `l6b` | RESCOS-56 à 69 | 1147 → 1017 | 8 (+2) | 10 (+5) |
| `t1` | 10 AMC Urgences + 10 Psy-Vignette | 1017 → 1012 | 11 (+1 noté) | 23 |
| `t2` | 25 thématiques A→D, et les 40 `undefined` | 1012 → 1011 | 8 | 26 |
| `t3` | 25 thématiques, rangs 36-60 | 1011 → 1005 | 15 | 26 |
| `t4` | 25 thématiques, rangs 61-85 | 1005 → 1002 | 16 | — |
| `t5` | 28 thématiques, rangs 86-123 | 1003 → 1003 | 9 | 30 |

Le saut de 1002 à 1003 entre `t4` et `t5` n'appartient à aucun lot : c'est le
commit `e8bd11e` de l'utilisateur, qui corrige `norm()`. Voir § 7.4.

### Ce que cela change pour qui révise

**Le score compte enfin.** Avant, les 156 stations notées calculaient leur note,
l'affichaient — puis levaient une `TypeError` juste après, et **n'écrivaient
rien** dans `ecos_registry`. Aucune de ces 156 stations ne remontait au tableau
de bord ; un étudiant pouvait travailler le corpus entier sans qu'une seule
trace en subsiste. Elles y remontent toutes aujourd'hui, avec le minuteur, le
mode circuit et la barre de navigation qu'aucune n'avait.

**Une station qui plafonnait à 50 % n'y plafonne plus.** RESCOS-63, remplie
parfaitement, rendait « 50 %, note E ». Elle rend « 100 %, note A ».

**La fiche de révision dit maintenant ce que la station évalue.** Plus de cent
trente informations que la page de référence tient pour capitales, et dont la
grille ne portait **aucune occurrence**, ont été portées : la glycémie capillaire
du D de l'ABCDE chez un polytraumatisé, l'anévrisme de l'aorte abdominale chez
un lombalgique de 75 ans, la ferritine chez un homme de 30 ans en anémie
ferriprive, l'immunoglobuline anti-D dans une station de suivi de grossesse,
l'hydrocéphalie à pression normale chez une femme de 74 ans en trouble de
l'équilibre — seule cause curable de son différentiel.

**Le lecteur ne lit plus le mot `undefined`.** 57 blocs de clôture affichaient
littéralement `undefined` sous un titre comme « Réponse type ».

**Le vocabulaire est suisse.** 424 termes, dont 208 `NFS` → FSC, les
numérations en G/L, les glycémies en mmol/L, le 144 à la place du 15.

---

## 2. Les cinq bugs de barème du projet

Cinq corpus, cinq manières pour un barème de mentir sur ce qu'il déclare. **Ce
corpus en a apporté deux**, et le premier est de loin le plus étendu du projet.

### Les deux découverts ici

#### 1. Les 156 moteurs embarqués — 13 446 `TypeError`, `ecos_registry` à 0/165

**Aucune des 165 grilles ne chargeait `cases/scoring.js`.** Les 156 stations
notées embarquaient chacune leur propre copie de `calculateScores()`, et ces
156 copies étaient **identiques entre elles, octet pour octet** hors du bloc de
configuration : une seule empreinte SHA-256 sur 156. Une seule variante — donc
une seule fourche, et elle était périmée.

Le `diff` contre le moteur partagé rendait exactement six manques : la garde
`if (missingEl)`, l'**appel** de `saveToRegistry()`, sa **définition**, le
chargeur de `srs.js`, la détection du mode circuit, et `createNavBar()`.

Le premier manque se réalisait à chaque calcul. Le moteur écrit
`document.getElementById("missingItems").style.display` sans garde, et le
`<div id="missingItems">` est **commenté** dans le HTML des 156 grilles.
`getElementById` rend `null`, la dernière instruction de `calculateScores()`
échoue — au chargement, puis à chaque clic. **13 446 exceptions mesurées sur un
remplissage complet du corpus.**

**La conséquence n'est pas cosmétique.** `ecos_registry` n'est écrit qu'à un
seul endroit du projet, `cases/scoring.js:saveToRegistry()` — absent des 156
copies. Mesure au navigateur : **0 grille sur 165** écrivait sa propre entrée.
Aucun score de ce corpus n'atteignait le tableau de bord.

**Pourquoi les vérificateurs existants ne pouvaient pas le voir.** Le barème
reste *calculable* et *calculé* : l'exception survient **après** l'écriture des
scores de section, du total et de la note. `check_reachability` simule le
remplissage et rend 100 % ; `check_invariants` compare des nombres qui n'ont pas
bougé ; `check_nomenclature` lit du texte. Et l'empreinte du moteur n'était
suivie par rien : 35 800 caractères de JavaScript noyés dans un fichier de
170 000 ne se distinguent, dans un `diff` de grille, d'aucune retouche de
contenu. **Seul un banc d'essai en navigateur pouvait le trouver** — c'est
exactement le constat de CasECOS, dont un diagnostic statique avait déclaré le
même défaut absent.

**Réparé par bascule, pas par report** (lot `l3`) : les 156 grilles chargent
`../scoring.js` et déclarent leur barème en `window.caseConfig`. Reporter six
corrections dans 156 copies aurait reconduit le mécanisme de dérive que le
défaut réalise déjà. La transposition est vérifiée, pas supposée : pour chacune
des 156, la configuration relue rend le **même quadruplet** avant et après —
`maxScores`, `coef`, `sectionInfo`, dénominateurs affichés. **0 divergence.**

Un piège s'est révélé en chemin : `createNavBar()` insère une barre en
`position: fixed; top: 20px; left: 20px`, et c'est **exactement** la place
qu'occupait `.timer-container` dans les 156 feuilles de style en ligne.
Réparer le moteur sans rien d'autre aurait posé une barre non stylée par-dessus
le minuteur. Les deux règles de `cases/case-styles.css` qui avaient déjà résolu
la collision pour les trois autres corpus ont été recopiées. **Recouvrement
mesuré aujourd'hui : 0/165.**

#### 2. RESCOS-63 — la somme des coefficients vaut 0,5

Deux sections seulement, `anamnese` coefficient 0,25 et `management`
coefficient 0,25. **Somme = 0,5.** Le global plafonnait à **50 %, note E**,
grille parfaitement remplie, **sans qu'aucune section ne soit en écart** :
`anamnese 29/29/29`, `management 16/16/16`.

**C'est un cinquième mécanisme, distinct des quatre déjà connus** — critère hors
de la boucle, section vide pondérée, `count` trop grand, `maxScores` divergeant
du `<span>` affiché. Les quatre contrôles hérités restent muets : ils comparent
des nombres **à l'intérieur** d'une section, et à l'intérieur de chaque section
de RESCOS-63 tous les nombres sont d'accord. Le défaut ne vit que dans la
**somme des coefficients**, que personne ne vérifiait.

Le mécanisme d'origine se lit dans le voisinage : le gabarit du corpus est
`0,25 × 4` — « RESCOS-64 station double 2 » le porte encore avec quatre
sections — et RESCOS-63 en a supprimé deux sans remettre les coefficients à
l'échelle. Correction : `0,5 / 0,5`, la seule qui rétablisse la somme sans
toucher au rapport voulu par l'auteur (les deux en-têtes annonçaient le même
« 25 % »). Vérifié en simulation **et** au navigateur : 100 %, note A.

`coef` est désormais gelé au snapshot. C'est ce qui garantit qu'une
redistribution qui **conserve** la somme — donc invisible à
`check_reachability` — serait signalée.

### Les trois autres, et pourquoi chacun échappait

| corpus | l'espèce | ce qu'elle produisait | pourquoi elle passait |
|---|---|---|---|
| **AMBOSS-9** | plus de points **déclarés** qu'il n'en existe : `count: 13` pour 12 critères réels, 53 points annoncés pour 49 | « Score : 49/53 » tout coché, station plafonnée à **98 %** | `sectionInfo[].count` n'était dans aucun snapshot ; le contrôle comparait `maxScores` au `<span>` affiché, et les deux étaient d'accord |
| **RESCOS-12 / 13** | une section **vide** qui garde son quart de coefficient : `count: 0`, `maxScores: 0`, « 0/0 » | copie parfaite plafonnée à **75 %, note C**, sur deux stations de psychiatrie où l'examen physique n'a pas lieu d'être | les **trois nombres de la section sont d'accord entre eux** — il n'y a rien à comparer. Visible seulement par le total global, et seulement si l'on sait que 75 % est anormal |
| **RESCOS-7 / 9, puis les 198 de CasECOS** | un moteur embarqué périmé qui lève une `TypeError` | 16 et 51 exceptions par remplissage, aucun score au registre — puis la même chose sur 198 grilles | le barème est calculable et calculé ; l'exception survient après. **Aucune porte Python ne peut voir un défaut d'exécution** |

Le défaut de ce corpus est le troisième de la famille « moteur embarqué », et le
plus étendu du projet en nombre d'exceptions. Le seul corpus indemne reste
German : 880 champs de barème recalculés, zéro divergence.

**La leçon d'outillage, à sa quatrième répétition** : chaque corpus a apporté une
espèce que les vérificateurs du précédent ne pouvaient pas voir, et à chaque fois
le contrôle qui l'a trouvée a été **ajouté après coup**. `sectionCounts` après
AMBOSS-9, `coef` et `empty_weighted_sections()` après RESCOS-12/13,
`engineFingerprint` et le banc d'essai en navigateur ici, `coef_sum_anomaly()`
après RESCOS-63. Il n'y a aucune raison de penser que la série est close.

---

## 3. Les erreurs médicales trouvées

**Soixante-quatorze erreurs corrigées** — le décompte du tableau du § 1, hors
les 424 termes de nomenclature —, **dont trente-cinq de sécurité** au sens
strict : un candidat qui applique l'item tel qu'il était écrit fait, ou omet, un
geste qui nuit au patient de sa propre station.

**Le résultat le plus utile n'est pas leur nombre, c'est que cinq motifs
récidivent.** Une erreur isolée est un accident d'auteur ; un motif qui frappe
trois, quatre ou cinq grilles indépendantes est un défaut de conception du
corpus, et il se cherche.

### A. Une conduite dont la réserve manque — le motif le plus fréquent

**Les dérivés nitrés sans la contre-indication de l'infarctus du ventricule
droit : trois grilles corrigées, une quatrième trouvée par cette vérification.**

La page `SSP — Douleur Thoracique` écrit : « **cave infarctus inférieur / droit :
pas de nitré** (précharge-dépendant) ». Le ventricule droit infarci ne tolère
pas la baisse de précharge ; le nitré y provoque un collapsus.

| grille | ce qu'elle écrivait | où |
|---|---|---|
| `AMC Urgences 3A` (STEMI) | « CI si PAS < 90 mmHg » — et rien d'autre | `theorie` |
| `Douleur thoracique - Vignette` | « Nitroglycérine sublinguale 0.4 mg (si TA > 90 mmHg systolique) » | `theorie` **et sous-item noté** |
| `Douleurs thoraciques - DRS` | « Dérivés nitrés **si TA normale** » | `theorie` **et attendu noté** |
| **`AMC Urgences 3B`** (NSTEMI, Killip III) | « Dérivés nitrés IV si TA le permet » · « Vasodilatateurs (nitrés IV) si TA > 110 mmHg » | **deux sous-items notés** + `theorie` — **non corrigé** |

**Le mécanisme est le même dans les quatre : la tension pour seul garde-fou.**
Or dans l'infarctus du ventricule droit, la tension **avant** l'administration
est normale. Le garde-fou ne se déclenche jamais ; il ne protège de rien.

Le motif déborde les nitrés : c'est la famille des **états
précharge-dépendants**, et le corpus l'a produite **cinq fois**.

* `Mal à l'épaule — péricardite` décrivait une tamponnade sans dire que
  diurétiques, dérivés nitrés et ventilation en pression positive y sont
  dangereux ;
* `SMIG-5` nommait neuf fois une sténose aortique serrée, la mettait dans ses
  pièges, l'opérait par TAVI — et ne la décrivait jamais comme
  précharge-dépendante, alors que son `therapy` prescrit « Furosémide 80 mg IVL
  puis 40 mg IV × 2/j » à FEVG 25 %.

Autres réserves manquantes, même famille : le **métoclopramide** listé sans
réserve parmi les antiémétiques d'un iléus malin — c'est un prokinétique,
contre-indiqué dans l'obstruction complète, et la vignette décrit précisément une
obstruction complète (vomissements fécaloïdes, arrêt des matières et des gaz
depuis 48 h) ; le **flumazénil** recommandé dans une intoxication volontaire
polymédicamenteuse à inventaire incertain, c'est-à-dire sa contre-indication
type ; la **physostigmine** dont la liste de contre-indications omet le QRS
élargi, alors que la `theorie` de la même grille écrit que l'intoxication en
donne ; le **dénosumab** sans l'avertissement du rebond, dont l'interruption
provoque des fractures vertébrales multiples ; le **bupropion** sans sa
contre-indication épileptique, sur deux grilles jumelles ; l'**hypotension
permissive** appliquée sans réserve à un traumatisé crânien à GCS 5 avec
anisocorie et décérébration — l'hypotension est le premier facteur modifiable de
mortalité du traumatisme crânien grave.

### B. Une absence de signe rangée en argument CONTRE un diagnostic grave — trois fois

Le différentiel de la grille rangeait *l'absence d'un signe* du côté des
arguments **contre** un diagnostic, alors que ce diagnostic se présente
précisément **sans** ce signe.

1. **`Psy-Vignette 4`** — « Cause organique (encéphalite, tumeur) — Arguments
   CONTRE : pas de signes neurologiques focaux · pas de fièvre », devant un
   **premier épisode psychotique à 18 ans**. C'est la présentation de
   l'encéphalite auto-immune à anticorps anti-NMDA, qui débute par des symptômes
   purement psychiatriques, sans fièvre ni signe focal. Appliqué, l'argument fait
   **écarter la seule cause curable du différentiel**.
2. **`Goutte - Accès aigu`** — l'absence de fièvre rangée CONTRE l'arthrite
   septique, avec une ponction « **si doute** ». La page en fait un piège
   éliminatoire et rappelle que « la présence de cristaux n'exclut PAS le
   sepsis ».
3. **`Nourrisson 6 mois avec fièvre`** — **deux fois dans la même
   `annexe-dd`** : « Méningite — CONTRE : fontanelle normale · pas de raideur »
   et « Pyélonéphrite — CONTRE : pas de signes urinaires · couches mouillées
   normalement ». Avant 12-18 mois, les signes méningés manquent dans la
   majorité des méningites, et l'infection urinaire se manifeste par une fièvre
   isolée. **Les grilles jumelles le disaient elles-mêmes** — `État fébrile sans
   foyer` écrit « peut débuter sans signes méningés ».

Le pilote avait rencontré la variante inverse, un argument POUR rangé du côté
CONTRE : l'hémorragie diverticulaire est « abondante, **indolore**,
intermittente », et « absence de douleur abdominale » figurait en argument
CONTRE la diverticulose — l'auteur pensait à la diverticul**ite**.

**Un quatrième candidat sort de cette vérification et n'est pas tranché** :
`Pédiatrie — État fébrile sans foyer` range « pas de boiterie » CONTRE
l'arthrite septique et « pas de douleur osseuse localisée » CONTRE
l'ostéomyélite, chez un nourrisson fébrile sans foyer.

### C. Un tératogène prescrit sans un mot de contraception — trois fois

1. **`Lupus érythémateux systémique — Femme de 26 ans`** : méthotrexate et
   mycophénolate proposés dans l'attendu noté ; **0 occurrence** de
   « contraception » ni de « tératogène » dans la grille entière.
2. **`Psoriasis — Femme de 42 ans`** : méthotrexate ; `contraception`,
   `tératogène`, `grossesse` — **0 occurrence**.
3. **`Sémiologie MSQ — Polyarthrite rhumatoïde`** : même défaut, même molécule,
   trouvé par le contrôle de la grille sœur.

À rapprocher : **`Voyage au Brésil — Femme de 22 ans`**, où la page écrit « Zika
tératogène : microcéphalie » et la grille se contentait de « risque pour femmes
enceintes », en recommandant par ailleurs un **vaccin vivant** (fièvre jaune)
sans énoncer une seule de ses contre-indications.

*Contrôle de résidu fait pour ce rapport* : six grilles nomment encore un
tératogène sans un mot de contraception, mais toutes ont pour patient un homme
ou une femme hors âge de procréer. **Aucune nouvelle occurrence du motif.**

### D. Une valeur biologique qualifiée à l'envers

**`Enfant qui boîte`** — « Arthrite septique — Arguments CONTRE : pas de fièvre
actuelle · **CRP normale (20 mg/l)** ». Une CRP à 20 mg/l n'est pas normale ;
elle est modérément élevée, donc compatible avec une infection débutante.

**Le lot `t3` a corrigé cette ligne, et cette ligne seulement.** Le balayage
final montre que la grille porte la qualification fausse en **quatre autres
endroits**, dont un sous-item **noté** :

| endroit | texte |
|---|---|
| sous-item noté (`criteria-detail`) | `CRP [20 mg/l - normale]` |
| `annexe-dd`, entrée Ostéomyélite | « Arguments CONTRE : Pas de fièvre · **CRP normale** » |
| récit de la présentation | « une biologie normale (GB 8 G/L, **CRP 20 mg/l**, VS normale) » |
| différentiel du même récit | « arthrite septique (**mais CRP normale**, pas de fièvre actuelle) » |
| carte SBAR | « (déjà faits : épanchement, **CRP normale**) » |

**La grille se contredit désormais avec elle-même, et la ligne corrigée est
minoritaire.** C'est le défaut le plus net que cette vérification ait trouvé.

De la même famille, corrigées celles-là : la **relation TSH/T4 inversée** de
RESCOS-67 — « TSH abaissée et T4 libre augmentée = hypothyroïdie primaire », qui
est la définition de l'hyperthyroïdie, dans une station d'hypothyroïdie dont
l'`annexe-dd` donne TSH 20,6 mU/L et T4L 2,06 pmol/L ; l'**hémoglobine érigée en
critère de gravité d'une hémorragie aiguë** sur RESCOS-58b (`< 100 g/L`) puis
RESCOS-58 (`< 80 g/L`), alors que la page nomme le piège — « l'Hb initiale est
faussement normale au début, l'hémodilution prenant plusieurs heures » ; et le
**D-dimère érigé en test d'exclusion de la dissection aortique** chez une
patiente à probabilité clinique maximale (asymétrie tensionnelle à 30 mmHg,
abolition du pouls fémoral, souffle d'insuffisance aortique nouveau).

### E. Les francités — un corpus suisse écrit en partie pour la France

| ce qu'écrivait la grille | le fait suisse | où |
|---|---|---|
| « Déclaration obligatoire urgente à l'**ARS** » | l'Agence Régionale de Santé n'existe pas en Suisse : médecin cantonal et OFSP | `AMC 5C`, **sous-item noté** |
| « suspension de conduite … **6 mois en France** », deux fois | OAC art. 7 et directives SVM/OFROU | `Crise convulsive`, dont **un sous-item noté** |
| dépistage colorectal « **50-74 ans** » | programme suisse **50-69 ans** (OFSP / SSG-SGG) | `theorie` |
| « Appeler le **15** », ×2 | **144** | `theorie` |
| « sérogroupes B, C, W, Y **en France** » | corpus suisse | `AMC 5C` |
| `Doliprane` | Dafalgan | nomenclature |

Les deux corrections en sous-item noté ont été faites : ce sont des **erreurs
factuelles internes**, pas des jugements d'auteur ni des divergences de
conduite — elles ne changent ni ce que le candidat doit faire, ni la structure.
Le chiffre suisse de suspension après une **première** crise n'existant nulle
part dans le vault, **il n'a pas été inventé** : le sous-item renvoie au texte
réglementaire.

*Contrôle de résidu fait pour ce rapport* : `ARS`, « en France », « appeler le
15 », `Doliprane` — **0 occurrence** aujourd'hui, hors deux mentions
délibérément contrastives (« et non d'une règle française », « la tranche
50-74 ans correspond au programme français »). Reste **`Spasfon`**, une
occurrence, laissée sciemment : son équivalent suisse le Buscopan est **une
autre molécule**, et le substituer aurait changé le médicament, pas son nom.

### F. Les autres corrections

**Référentiels périmés** : `ScvO2 > 70 %` comme objectif de réanimation — cible
de l'*early goal-directed therapy*, abandonnée, et que la page désigne comme un
piège en rappelant qu'en choc septique la ScvO₂ **peut être normale ou haute** ;
« Zostavax ou Shingrix après 50 ans », alors que Zostavax est un vaccin vivant
retiré de Suisse et Shingrix recommandé dès 65 ans ; groupes GOLD A-D au lieu de
A/B/E ; « GOLD 3 → trithérapie inhalée », alors que le grade spirométrique ne
décide pas du traitement ; la définition **temporelle** de l'AIT (« < 1 heure »)
au lieu de la définition tissulaire ; le palivizumab présenté comme un
« vaccin RSV ».

**Posologies et délais** : nitrofurantoïne 100 mg **2×/j** (schéma
nord-américain, sous-dose la molécule du Compendium suisse) au lieu de 3×/j ;
coronarographie « dans les 24-72 h » chez une patiente en **Killip III**, que
l'`expert` de la même grille identifie pourtant comme critère de très haut
risque ; « 60-90 minutes de surveillance » après naloxone chez une patiente sous
**méthadone** (demi-vie 15-60 h) — une sortie à 90 minutes est une re-narcose
hors de l'hôpital ; contre-indications du fibrinolytique fausses (« AVC
< 3 mois », alors que l'AVC hémorragique est une contre-indication à vie).

**Contradictions internes**, où la grille se réfute elle-même : antibiothérapie
empirique devant une diarrhée sanglante, quatre lignes sous « syndrome
hémolytique et urémique (*E. coli* O157:H7) » dans les complications ;
métoclopramide alors que `therapy` décrit une obstruction complète ;
antihistaminiques au même rang que la cholestyramine contre le prurit
cholestatique, alors que `therapy` de la même grille écrit « antihistaminiques
peu efficaces » ; « ictère + douleur + perte de poids » en triade du cancer du
pancréas, quand la ligne suivante du même bloc dit « ictère indolore ».

---

## 4. Le trou de protection — le constat le plus lourd du corpus

**`PAFA`, `art. 426 CC`, `APEA`/`KESB`, `curatelle`, `143`, `147` : zéro
occurrence, sur cinq lots consécutifs, 123 grilles thématiques balayées avant
toute intervention.**

| lot | grilles balayées | occurrences |
|---|---:|---:|
| `t1` | 20, dont **10 vignettes de psychiatrie** | 0 (sauf un `143` sur une seule grille) |
| `t2` | 25 | 0 |
| `t3` | 25 | 0 |
| `t4` | 25 | 0 |
| `t5` | 28 | 0 |

Les rares correspondances du balayage étaient toutes des faux positifs : une CRP
à 143 mg/L, un score sur 143, un dénominateur « 0/147 », et des
« sus-**clavi**culaire » pour `LAVI`.

**Le cas le plus parlant est celui des dix Psy-Vignette.** Une série de dix
stations de psychiatrie suisse ne nommait pas une seule fois le placement à des
fins d'assistance, alors que :

* `SSP — Urgences Psychiatriques (Agitation, PAFA)` inscrit « **pas de mise en
  place de PAFA quand les critères sont réunis** » parmi ses *pièges
  éliminatoires* ;
* la **Psy-Vignette 9** fait littéralement dire au patient « **je ne suis pas
  malade, pourquoi m'hospitaliser ?** », et la « Réponse type » n'évoque aucun
  cadre légal ;
* la **Psy-Vignette 2** décrit un patient maniaque, délirant, hallucinant,
  irritable et agressif, sans un mot sur la dangerosité ni sur la contrainte ;
* la **Psy-Vignette 5** organise l'hospitalisation en urgence d'une mère
  psychotique et parle de « services de protection de l'enfance » — formulation
  générique, sans l'autorité suisse compétente.

**Et le trou n'est pas propre à la psychiatrie.** Le bloc `expert`, qui est le
corrigé remis à l'examinateur, réclamait explicitement la réponse à plusieurs
reprises sans que la grille la porte nulle part : « hospitalisation sous
contrainte » sans PAFA · « sécuriser financièrement le patient » sans curatelle
ni APEA · « évaluation systématique du risque suicidaire obligatoire » sans
méthode, sans numéro, sans cadre légal · l'autorisation parentale du voyage d'un
mineur, **réclamée deux fois** dans la même grille, absente de la grille.

De même : `glycémie` à zéro sur les dix vignettes de psychiatrie, alors que la
page impose « ABCDE + glycémie d'emblée » et « toujours exclure une cause
organique ». Et `suicid*` à zéro sur les **deux** grilles de trouble panique du
corpus — sur-risque suicidaire établi.

Conformément à la consigne « enrichis, ne réduis pas », **rien n'a été retiré** :
une catégorie a été ajoutée à l'`annexe-dd` de chacune des dix vignettes, et une
ou deux sections au `theorie` des grilles concernées des lots suivants.

**Un piège de la page de référence a été évité, et il vaut d'être signalé.**
`SSP — Urgences Psychiatriques` écrit **quatre fois** « PAFA = incapacité de
discernement + danger + absence d'alternative » — et **se contredit** dans sa
propre carte ECOS, qui énonce correctement que « l'incapacité de discernement
(art. 16 CC) **n'est PAS** une condition du PAFA ; elle l'est du traitement sans
consentement (art. 434 CC) ». C'est la version de la carte, conforme à
l'art. 426 CC, qui a été portée dans les dix grilles. La hiérarchie de décision
du projet ne prévoit pas le cas où la page se contredit elle-même : il a fallu
trancher sur le texte légal.

---

## 5. Ce qui reste non corrigé, et pourquoi

### 5.1 Vingt-quatre divergences consignées dans un bloc noté

`therapy`, `redflags` et les sous-items cotés sont des **attendus de
correction** : les toucher change ce sur quoi l'étudiant est évalué. La règle du
projet est de consigner, pas de corriger, sauf erreur factuelle interne sans
changement de structure. Elle produit un état où **la fiche pédagogique et le
barème de la même grille enseignent deux conduites différentes, et c'est le
second qui est évalué.**

Les plus sérieuses :

| grille | ce que le bloc noté prescrit | ce qu'il faudrait |
|---|---|---|
| `Urticaire allergique` | « Antihistaminique H2 — **Ranitidine** » | molécule **retirée du marché mondial en 2020** (nitrosamines), inexistante en Suisse |
| **`Choc anaphylactique`** | « Anti-H2 [**ranitidine** 50mg IV] » | **même molécule, seconde grille — non signalée par les lots** |
| `AMC Urgences 1` | « Permissive hypotension · PAS cible 80-90 mmHg » | chez un traumatisé crânien grave, cible ≥ 110 mmHg |
| `RESCOS-61` | « Tocolyse … [**β2-mimétiques**, antagonistes Ca2+] » | atosiban, nifédipine — **pas de salbutamol** (toxicité cardiovasculaire maternelle) |
| `Belladone` | « CI : bloc AV, asthme, vessie/intestin obstrués » présentée comme complète | il manque le **QRS élargi** et la suspicion de tricycliques — la contre-indication qui tue |
| `Paracétamol` | N-acétylcystéine « 150 mg/kg … **1×/jour pendant 3 jours** » | perfusion continue de 21 h, jamais trois doses journalières |
| `Toux et maux de ventre` | « Ibuprofène … en alternance » dans une pneumonie de l'enfant | l'`expert` de la même grille demande d'anticiper l'empyème que les AINS favorisent |
| `AMC Urgences 5C` | `ScvO2 > 70 %` dans le bundle sepsis | cible abandonnée, corrigée ailleurs dans le corpus |
| `Bronchiolite` | « Maintien saturation **> 94 %** » | le `redflags` de la même grille fixe le seuil à **92 %** |
| `RCI-Gonocoque` | « Azithromycine 2 g PO » en alternative | la monothérapie n'est plus acceptable pour la gonorrhée |
| `RESCOS-41` vs `RESCOS-42` | ceftriaxone **250 mg** IM contre **500 mg** dans la grille voisine | 250 mg est la posologie d'avant 2020 — **deux grilles du même corpus enseignent deux doses du même antibiotique** |

**Le motif est attesté sur les huit lots de traitement.** Il ne relève plus de la
consignation : il demande un arbitrage sur la règle elle-même.

### 5.2 Les 92 images perdues, non re-pointables

103 balises `<img>` dans le corpus au départ ; 11 en base64, conservées ;
**92 mortes sur 35 grilles** — 75 pointant un chemin absolu du poste de l'auteur
(`/Users/…/Documents/-Medecine/-EXAMEN_FEDERAL/…`), 17 un chemin relatif sans
racine dans le dépôt. Détectées au 404 en navigateur, pas au `grep`.

**Aucune n'a pu être re-pointée.** Le dépôt compte 45 fichiers image ;
confrontation des 92 noms de base par égalité exacte, puis après normalisation,
puis par ressemblance : **0 correspondance**, la meilleure ressemblance valant
0,62 sur deux sujets différents. Les 92 sont **perdues**, restaurables seulement
depuis le poste de l'auteur ou les sources d'origine.

Ce qui autorisait le retrait : la **légende porte l'information seule**, vérifié
une par une. Les 92 balises vivaient dans un `annexe-item` portant un titre et
une description qui énonce ce que l'examen montre (« Radiographie thoracique
montrant des contusions pulmonaires bilatérales et un pneumothorax gauche »).
Seul le `<div class="annexe-image">` a été retiré ; **titre et description
restent**. Conséquence mesurée : 0 champ du snapshot ne bouge, `check_no_loss`
rend 0, les 92 erreurs 404 tombent à 0.

**Rien n'a été fabriqué**, et la liste exacte est versionnée au journal, fichier
par fichier.

### 5.3 `RCI-Fièvre` et sa jumelle — la relation d'inclusion a été rompue

L'audit initial mesurait une **inclusion stricte** :
`Fièvre et douleurs articulaires — Infection gonococcique disséminée`
⊂ `RCI-Fièvre et douleurs articulaires — …`. **0 item propre** à la première sur
106 ; 85 propres à la seconde. C'était une duplication, et la première était
superflue.

**Ce n'est plus vrai, et c'est le traitement qui l'a rompu.** Le lot `t3` a
traité la version sans préfixe et lui a apporté quatre corrections —
azithromycine 2 g écartée, ponction articulaire avant la première dose,
déclaration OFSP et partenaires des 60 jours, doxycycline préférée pour la
chlamydiose. Elle porte donc désormais **4 items propres**. Le lot `t5` les a
reportées dans la `RCI-`, mais le principe demeure : **traiter une jumelle rompt
l'inclusion qui justifiait de ne pas traiter l'autre.**

La `RCI-` est le sur-ensemble (213 items contre 108) : c'est elle qu'il faut
garder. **Aucun fichier n'a été supprimé** — l'arbitrage est éditorial, et
surtout `SSP — Douleurs Articulaires` **cite la version sans préfixe**. Dans cet
ordre : (1) faire pointer la page sur la `RCI-` ; (2) vérifier qu'aucun autre
index ne cite l'autre ; (3) supprimer alors la version sans préfixe. Tant que
(1) n'est pas fait, supprimer casserait un lien du vault.

Deux autres paires suspectes restent ouvertes : `Mal au dos — Guillain-Barré (1)`
contre sa sœur sans `(1)` — 18 items communs, 85 et 178 propres, deux versions
divergentes dont la première n'est **citée par aucune page** ; et les deux
`RESCOS-69`, réglées par un renommage (`RESCOS-69b`) mais dont le vault ignore
encore le nouveau nom.

### 5.4 Les pages du vault qui se contredisent ou ne portent pas la matière de leur grille

Le vault est hors du dépôt et n'a pas été modifié. Les signalements valent pour
l'utilisateur.

**Trois pages se contredisent elles-mêmes :**

* `SSP — Urgences Psychiatriques` — quatre fois « PAFA = incapacité de
  discernement + danger + absence d'alternative », contredit par sa propre carte
  ECOS, qui est la version juste (§ 4) ;
* `SSP — Dépression` — son bloc `redflag` écrit « hospitalisation immédiate
  (**SDT/SDRE/SPI selon contexte**) », **la nomenclature de la loi française**,
  alors que les huit autres occurrences de la page disent correctement PAFA
  (art. 426 CC). Signalé au lot `t2`, **toujours présent au lot `t3`** ;
* `SSP — Douleur d'Épaule` référence `RESCOS-69b` sous son **ancien nom de
  fichier**, antérieur au renommage du lot `l3` : le lien `file://` est mort.

**Onze pages ne portent pas la matière de la grille qu'elles citent :**
`SSP — Éruption Cutanée` cite `Acné vulgaire`, `Érythème cutané` et
`Pemphigoïde bulleuse` sans section acné, sans section cellulite/érysipèle et
sans section sur les dermatoses bulleuses auto-immunes — **trois grilles, une
page, trois fois rien** ; `SSP — Diabète` n'a aucune section pédiatrique ;
`SSP — Malaise` n'a aucun contenu sur les absences ni aucune durée chiffrée de
suspension de conduite ; `SSP — Troubles de la Croissance` cite une cardiopathie
congénitale sans rien porter sur les cardiopathies ; `SSP — Détresse
Respiratoire (Adulte-Enfant non-néonatal)` est presque entièrement adulte pour
une grille de bronchiolite ; `SSP — Dyspnée` ne dit rien de la sténose aortique
de `SMIG-5` ; `SSP — Toux Chronique` couvre le SIADH d'une ligne ;
`SSP — SD Counselling Dépistages` porte ses tranches d'âge, ses rythmes et ses
coûts dans des **légendes d'images et des PDF joints** plutôt que dans son texte.

Une grille n'est citée par aucune page (`Mal au dos — Guillain-Barré (1)`), une
autre non plus (`RCI-Fièvre`) — dans les deux cas c'est la jumelle qui est
citée.

### 5.5 Les autres points laissés ouverts

* **`PTSD`, `DKA`, `HHS`** — 17 occurrences, laissées faute d'équivalent
  français attesté. Ni `TSPT`, ni `ESPT`, ni `SHH` n'apparaissent nulle part
  dans les quatre corpus ; les introduire aurait créé un terme que rien
  n'atteste. `PTSD` est aussi dans `cases/german/` (6) et `cases/casecos/` (3) :
  un arbitrage commun serait plus cohérent qu'un arbitrage par corpus.
* **Deux valeurs à unité implicite** — « Hb 13.2, Ht 31 %, GB 8 G/L » (l'Hb y
  est en g/dL sous-entendu, elle vaudrait 132 g/L) et « Bactérien : > 1000 GB »
  (qui hérite du `/mm³` de la ligne précédente). Leur unité n'est pas écrite ;
  la choisir serait une supposition.
* **Les 37 unités non suisses du § 0** — 29 en litre minuscule, 8 gaz du sang en
  mmHg. Le correctif relève d'une passe de motif sur les quatre corpus.
* **`CEA`** au lieu d'`ACE` (antigène carcino-embryonnaire) — reliquat non
  banni, parce qu'`ACE` figure justement parmi les faux positifs français de
  `check_nomenclature`.
* **« Suicide : 15 % des patients dépressifs sévères »** — estimation historique
  de Guze & Robins issue de cohortes hospitalières, d'un ordre de grandeur
  au-dessus des estimations actuelles. Elle **surestime** le risque : elle ne met
  personne en danger, et aucune source du vault ne la contredit.
* **`RESCOS-64 station double 2`** — 108 808 caractères de fichier et
  **aucun bloc mobile** : `blocks_present()` rend `[]`. Elle ne peut rien
  recevoir. Ses différentiels notés ne recoupent qu'à moitié ceux de la station
  1, si bien qu'un candidat préparé sur l'une est évalué, dans l'autre, sur trois
  hypothèses que la première ne nomme jamais.
* **Le corpus n'est pas encore publié** — `index.html` ne référence aucune
  grille de `cases/rescos-locales/`. Les 156 entrées d'`ecos_registry` sont
  écrites mais pas encore affichées. Quand le corpus y sera ajouté, les `href`
  devront être **percent-encodés** : `saveToRegistry()` construit sa clé depuis
  `location.pathname`, et 132 des 165 noms portent un accent.
* **Le mode circuit n'est pas exercé de bout en bout.** Le contrôle en
  navigateur a été mené hors circuit (`ecos_circuit` absent du `localStorage`).
  Le code est celui du fichier partagé, celui des trois autres corpus — mais il
  n'est pas mesuré. La collision de mise en page, elle, l'est : 0 recouvrement
  sur 165.

---

## 6. Ce que la campagne a appris sur la méthode

### 6.1 Le compteur de redondance ne prédit rien quand `presentation` est absent

C'est la leçon la plus coûteuse à apprendre, et la plus transposable.

`report_redundancy` a gouverné les trois premiers lots de traitement, et à juste
titre : `l6b` a fait passer 17 grilles de 133 paires à 3. Puis le premier lot
thématique est arrivé, et la mesure s'est éteinte.

**La redondance inter-blocs se nourrit d'un seul couple** : `presentation` face
à `resume`, `theorie`, `annexe-dd` ou `expert`. Mesuré aujourd'hui :
**718 des 1003 paires** impliquent `presentation`, et **914 des 1003** sont
portées par les **57 grilles** qui en ont une. Les **108 grilles sans
`presentation`** — les deux tiers du corpus — se partagent **89 paires**.

Le résultat opérationnel est net :

> Sur les 20 grilles du lot `t1`, **17 mesuraient zéro paire**, et **onze
> portaient un trou de sécurité.**

Les dix Psy-Vignette, avec trois blocs dont un sans item extractible, **ne
peuvent pas produire une seule paire** — quel que soit leur contenu. Un zéro n'y
est pas une qualité, c'est une absence de matière. Et le lot suivant a montré
que **le contraire est vrai aussi** : `Claudication intermittente` est à 31
paires, n'a pas bougé — ses paires sont le recouvrement légitime
`presentation ↔ resume` — et c'est pourtant la grille où il manquait
l'intégralité de l'ischémie aiguë de membre.

**La mesure de similarité est un filet à grosses mailles.** Elle est
structurellement aveugle à ce qui n'a jamais été écrit, et elle décroche dès que
les deux blocs comparés n'ont pas le même grain. Elle n'a trouvé **aucun** des
trous du canonique de ce corpus.

### 6.2 Le bloc `expert` est le meilleur détecteur de trou, et il est gratuit

`expert` est la fiche remise à l'examinateur : elle énumère ce que le candidat
doit avoir fait, et les pièges qu'il ne doit pas commettre. **Quand elle reproche
une omission dont la réponse n'existe nulle part dans la grille, il y a un
trou** — et la lecture coûte quelques secondes.

| lot | grilles avec `expert` | attendus sans réponse |
|---|---:|---:|
| `t1` (AMC Urgences) | 10 | **4** |
| `t2` | 19 | **11** |
| `t3` | 16 | **7** |
| `t4` | 23 | **9** |
| `t5` | 28 | **10** |

Quelques exemples : « Stratégie de reperfusion claire (angioplastie vs
thrombolyse) » face à une grille qui ne porte ni le seuil de 120 minutes ni le
délai de fibrinolyse · « Contrôler l'indication et la mise en place appropriée
de la VNI » face à une grille sans pH < 7,35, sans PaCO2 > 6 kPa, sans
contre-indication · « Oublier de parler de la contraception d'urgence » chez une
adolescente, dans une grille à **0 occurrence** de contraception d'urgence ·
« Ne pas rechercher une ischémie critique » sans les 6 P, sans la fenêtre de 6 h,
sans l'IPS < 0,4 · « Évaluer systématiquement le risque suicidaire **et
infanticide** » face à une ligne « risque suicidaire accru » et aucune méthode.

**Et le corollaire est aussi solide** : les grilles **sans** `expert` sont
exactement celles qu'il faut ouvrir avec la page en main. Elles sont
systématiquement à 0 ou 1 paire de redondance, et elles portent les défauts les
plus nets. Au lot `t4`, les deux seules grilles sans `expert` n'avaient pas non
plus de `theorie` — et ce sont les deux qui portaient les pires défauts du lot.

### 6.3 Les grilles jumelles partagent leurs défauts — et il faut aller les chercher

Le corpus compte de nombreuses fratries : trois `Mal au dos — Guillain-Barré`,
deux `Sémiologie MSQ`, deux `Entretien motivationnel` tabac, deux `RESCOS-69`,
deux `RESCOS-58`, deux `Trouble panique`, dix `Pédiatrie`. **À chaque fois qu'un
défaut a été trouvé sur l'une, le contrôle de la sœur en a trouvé un.**

* `Hb` en critère de gravité d'une hémorragie aiguë : RESCOS-58b (`< 100 g/L`)
  **et** RESCOS-58 (`< 80 g/L`), même page de référence, même piège nommé ;
* méthotrexate sans un mot de contraception : `Psoriasis` **et**
  `Sémiologie MSQ — Polyarthrite rhumatoïde` ;
* `suicid*` à zéro : `Psy-Vignette 8` **et** `Trouble panique` — les **deux**
  grilles de trouble panique du corpus ;
* bupropion sans contre-indication épileptique : `EM — Sevrage tabagique`
  **et** `EM — Tabac` ;
* biologie lue à l'envers : `Goutte` a conduit à ouvrir `Enfant qui boîte`, où
  la CRP à 20 mg/l était dite normale ;
* absence de signe rangée CONTRE : `Nourrisson 6 mois` trouvé en contrôlant
  `État fébrile sans foyer` et `Vomissements et état fébrile`.

Les jumelles divergent aussi, et l'écart est un signal en soi : `RESCOS-69`
écrivait « plâtre brachio-antébrachial 6-8 semaines » là où `RESCOS-69b` écrit
« brace fonctionnel 4-6 semaines », et la seconde version est la conduite
actuelle. `RESCOS-41` fixe la ceftriaxone à 250 mg, `RESCOS-42` à 500 mg.

### 6.4 Trois observations d'outillage

**Le passage systématique par la page de référence est le seul contrôle qui
trouve un trou.** `report_redundancy` mesure ce qui est écrit deux fois,
`check_no_loss` ce qui a disparu ; ni l'un ni l'autre ne voit ce qui n'a jamais
été écrit. Il faut chercher la page à la main — `docs/obsidian-mapping.yaml` ne
couvre pas ce corpus, mais le bloc « Références PDF » de chaque page liste ses
grilles, et c'est un mapping inverse fiable : 24, 25, 27 grilles sur 25 ou 28
selon les lots. **Ne pas borner la recherche à `SSP ECOS/`** : `Skills — …` porte
à lui seul cinq grilles d'un lot, et une station double peut relever de deux
pages.

**`check_nomenclature` a rattrapé le traitement lui-même, deux lots
consécutifs** — un « centre PCI » et un « éosinophiles ≥ 300/µL » repris d'une
source, rejetés avant validation. C'est l'argument le plus direct pour le câbler
en CI, maintenant qu'il est vert.

**« Le motif décide de ce qu'on trouve, pas la famille. »** L'inventaire initial
annonçait 368 termes, la passe en a traité 424 — 56 de plus, tous manqués pour
une raison de **bordage** et non de conception. Le même mécanisme a produit
l'angle mort de `g/dl` collé au chiffre, et produit encore les 37 unités du § 0.

---

## 7. Le détail des six vérifications

### 7.1 Les vérificateurs, sur les trois corpus outillés

```
python3 scripts/rescos-locales/check_invariants.py     OK — 165 grilles, code 0
python3 scripts/rescos-locales/check_nomenclature.py   OK — 0 terme non suisse, code 0
python3 scripts/rescos-locales/check_reachability.py   OK — 165 grilles (9 feuilles porte,
                                                       156 notées), 100 % par section, code 0
python3 scripts/rescos-locales/report_redundancy.py    TOTAL : 1003 paires
python3 scripts/rescos-locales/check_no_loss.py 7c77e3e  423 items / 87 grilles, rapport, code 0

python3 scripts/amboss/check_invariants.py             OK — 40 grilles, code 0
python3 scripts/amboss/check_nomenclature.py           OK, code 0
python3 scripts/amboss/check_reachability.py           OK — 40 grilles, code 0
python3 scripts/amboss/report_redundancy.py            TOTAL : 147  (témoin, inchangé)

python3 scripts/rescos/check_invariants.py             OK — 41 grilles, code 0
python3 scripts/rescos/check_nomenclature.py           OK, code 0
python3 scripts/rescos/check_reachability.py           OK — 41 grilles, code 0
python3 scripts/rescos/report_redundancy.py            TOTAL : 127  (témoin, inchangé)
```

`bounds_anomalies` et `uncovered_content` sont vérifiés **à zéro** par
`check_invariants` — ce sont les deux champs qu'il compare non pas au passé mais
au vide. Recalculés indépendamment pour ce rapport sur les 165 : **0 anomalie**.

`cases/german/`, `scripts/german/`, `cases/casecos/` et `scripts/casecos/`
n'ont été ni lus, ni exécutés, ni mesurés : l'utilisateur y travaille en
parallèle.

### 7.2 Barème — 2310 comparaisons, 313 divergences, toutes admises

Snapshot complet des **14 champs** reconstruit depuis les blobs de `7c77e3e` et
comparé à l'état du disque, les 165 grilles des deux côtés, en tenant compte du
renommage `RESCOS-69 → RESCOS-69b`.

| champ | grilles divergentes | motif |
|---|---:|---|
| `engineFingerprint` | **156** | `c3e2534e…` → `shared:cases/scoring.js` — la bascule sur le moteur partagé |
| `configForm` | **156** | `declarative` (154) / `imperative` (2) → `caseConfig` — la branche de lecture change |
| `coef` | **1** | RESCOS-63 : `{0.25, 0.25}` → `{0.5, 0.5}` |
| `maxScores` · `scoreSpans` · `sectionCounts` · `sectionPrefixes` · `blocks` · `boundsAnomalies` · `uncoveredContent` · `criteriaCount` · `detailCount` · `radioCount` · `checkboxCount` | **0** | — |

**Onze champs sur quatorze sont identiques sur les 165 grilles**, y compris sous
le nouveau nom de `RESCOS-69b`, y compris après le retrait des 92 images, y
compris après onze lots d'édition pédagogique. C'est la démonstration la plus
directe que le travail a touché le moteur, un coefficient, un nom de fichier et
des balises `<img>` — et **rien** du barème.

Les huit corrections faites dans une section notée (deux au lot `t1`, deux au
lot `t2`, deux au lot `t3`, deux au lot `t4`) ne déplacent aucun champ : elles
complètent le **texte** d'un sous-item existant, **sans ajout ni retrait**.
`criteriaCount`, `detailCount`, `radioCount` et `checkboxCount` en sont la
preuve mécanique.

### 7.3 Intégrité structurelle — 0 problème sur les 165

| contrôle | résultat |
|---|---|
| `<!DOCTYPE html>` en tête, `<html>` unique, `</body>`, `</html>` en fin de fichier | **165 / 165** |
| appariement de 19 balises à conteneur (`div`, `span`, `table`, `tr`, `td`, `ul`, `li`, `script`, `style`, `h1`-`h4`, `p`, `label`, `strong`, `em`), hors commentaires, `<script>` et `<style>` | **0 déséquilibre** |
| blocs présents et **nombre de segments par bloc**, comparés au snapshot | **0 écart** — 1466 segments, 12 blocs |
| `bounds_anomalies` / `uncovered_content` | **[] / {}** sur les 165 |
| format `« N. Libellé »` des `.criteria-text` | **0 écart** |
| **crochets `[…]` du bloc `cloture`** | **464 à `7c77e3e`, 464 sur le disque — 0 grille ne bouge** |

Le dernier contrôle n'est pas cosmétique. `cases/scoring.js:294`
(`colorPatientResponses()`) enveloppe chaque `[…]` d'un
`<span style="color: rgb(44, 90, 160); font-weight: 500;">` dans les
`.criteria-text`, `.detail-text`, `.cloture-content` et six autres classes :
ce sont **les réponses du patient simulé**, visuellement distinguées de la
consigne. En perdre un crochet, ou en ouvrir un sans le fermer, casse
l'affichage de toute la ligne. Le contrôle en navigateur le confirme du côté du
rendu : **crochets colorés présents sur 155 des 165 grilles**, les 10 sans étant
les 9 feuilles porte et « RESCOS-64 station double 2 », dont aucun critère ne
porte de `patient-response` — état antérieur, pas une régression.

### 7.4 Redondance — 1258 → 1003, et pourquoi le gain est faible en proportion

**Le corpus mesure 1003 paires inter-blocs aujourd'hui contre 1258 à l'import**,
soit −255 (−20,3 %). Les deux chiffres sont comparables : la mesure de
`7c77e3e` a été **refaite avec l'outillage courant** pour ce rapport, et elle
rend exactement 1258.

Le gain est faible en proportion, et il est attendu. **Le couple qui produit les
paires est absent des deux tiers du corpus.**

| | grilles | paires portées |
|---|---:|---:|
| grilles **avec** `presentation` | 57 / 165 | **914** |
| grilles **sans** `presentation` | 108 / 165 | **89** |

Les quatre couples de tête sont `presentation ↔ resume` (242),
`presentation ↔ theorie` (193), `annexe-dd ↔ presentation` (141),
`expert ↔ presentation` (118) : `presentation` est des deux côtés des quatre.
Là où elle existe, la réduction a été forte — `l6b` a fait 133 → 3 sur 17
grilles. Là où elle n'existe pas, **il n'y avait rien à réduire**, et c'est
précisément là que se trouvaient les trous.

#### Ce que sont les 1003 paires restantes

Échantillon de **22 grilles tirées au sort, 183 paires** lues une par une.
Distribution des ratios : 0,7 → 27 · 0,8 → 75 · 0,9 → 41 · **1,0 → 33
identiques**. Quatre familles, et une seule est réductible.

**1. Le plancher structurel — la majorité.** Le signe discriminant de la station
doit être nommé par chaque bloc dans sa fonction propre : `annexe-dd` l'oppose au
différentiel, `resume` le récapitule, `expert` en fait un attendu de correction,
`presentation` le fait dire au candidat. Trois exemples pris tels quels :

```
[1.0]  annexe-dd  <->  presentation     modification recente du transit
[1.0]  expert     <->  presentation     modification recente du transit
[1.0]  annexe-dd  <->  presentation     mobilite passive conservee
```

Retirer l'un des deux membres dégraderait le bloc appauvri sans rien apprendre.

**2. Les clés de mnémotechnique.** Un mnémo préfixe la phrase d'une lettre, ce
qui suffit à créer une paire quasi identique avec la phrase nue :

```
[0.95] resume  <-> presentation   « traumatisme recent »        vs « T traumatisme recent »
[0.84] theorie <-> presentation   « dissociation albumino-cytologique au LCR »
                                  vs « C CSF dissociation albumino-cytologique »
[0.77] annexe-dd <-> presentation « faiblesse progressive ascendante des 4 membres »
                                  vs « F faiblesse progressive et ascendante »
```

Un mnémo est un **changement de format**, donc protégé par la règle du projet.

**3. `expert` face au reste.** `expert` est la fiche de l'évaluateur : elle
redit par construction ce que la grille enseigne, du point de vue de la
correction (« prescrire trop d'examens d'emblée » face à « prescrire trop
d'examens inutiles »). `expert` ne se touche pas.

**4. Des synonymes qu'unifier a rendus visibles.** La passe de nomenclature a
fait franchir le seuil de 0,72 à des paires que deux graphies masquaient
(« piquetage » / « pitting », « CEA marqueur tumoral » / « marqueur tumoral
CEA » ). **La redondance était là ; ce sont les deux graphies qui la cachaient.**
C'est le mécanisme documenté du +2 de la passe `l4`, où quatre paires franchaient
le seuil vers le haut et quatre vers le bas, sans qu'un seul item soit dupliqué.

#### Le point de méthode : `norm()` déplace la mesure des quatre corpus

Le commit **`e8bd11e`** de l'utilisateur corrige `norm()` : les ligatures œ et æ
n'ont **aucune décomposition Unicode** — ni NFD ni NFKD ne les touchent, ce sont
des lettres à part entière et non des ligatures de compatibilité comme ﬁ. Le
filtre `[^a-z0-9 ]` les remplaçait donc par une espace : « œdème » se comparait
comme « deme », « cœur » comme « c ur », « manœuvre » comme « man uvre ».
**4045 occurrences dans `cases/`, sur 486 fichiers.**

`norm()` vit dans `scripts/amboss/lib_amboss.py` et **les quatre corpus en
dépendent**. L'ampleur a été mesurée pour ce rapport, corpus par corpus, en
rejouant `report_redundancy` avec l'ancienne implémentation :

| corpus | `norm()` avant `e8bd11e` | après | écart | grilles déplacées |
|---|---:|---:|---:|---|
| AMBOSS | 147 | 147 | **0** | **2** — AMBOSS-15 8→7, AMBOSS-19 9→10 |
| RESCOS | 127 | 127 | **0** | 0 |
| `rescos-locales` | 1002 | 1003 | **+1** | 1 — `Urticaire allergique` 19→20 |

`cases/german/` n'a pas été mesuré : ses vérificateurs sont hors mandat.

**Le total est presque neutre ; il ne l'est pas par absence d'effet mais par
compensation.** Sur AMBOSS, le total reste à 147 parce qu'une grille perd une
paire et une autre en gagne une. Un total stable ne prouve donc pas qu'une
retouche de `norm()` est sans effet : **il faut le relevé par grille.**

La mutilation était par ailleurs **symétrique** — les deux côtés d'une
comparaison la subissaient identiquement — donc elle ne produisait pas de faux
appariements ; elle scindait un mot en deux jetons et abaissait la similarité
mesurée sur du vocabulaire clinique central (œdème, cœur, manœuvre, fœtal,
œsophage). La correction va dans le sens de la justesse.

> **Signalement.** Toute retouche future de `norm()` déplace la mesure de
> redondance des quatre corpus. Elle devrait s'accompagner d'un relevé des
> quatre totaux **et** du détail par grille, faute de quoi une régression peut
> se cacher derrière un total stable.

### 7.5 Non-perte — 423 items signalés, aucune perte réelle

`check_no_loss.py 7c77e3e` a examiné les **155 grilles modifiées** (la 156ᵉ est
le renommage) et signale **423 items disparus sur 87 grilles**. Le volume est
important et il est attendu : il mesure l'effet de trois gestes délibérés — la
**fusion** de puces en lignes plus longues et plus discriminantes, la
**conversion** des `presentation-reponse list` en registre parlé, et la
**réécriture sur place** d'une notion corrigée.

**Recherche de motifs, comme demandé.** Deux angles ont été balayés.

**a) Un volume de suppression anormal sur une grille.** Le sommet du classement
est cohérent avec le travail : ce sont les grilles les plus redondantes des lots
`l5`, `l6a` et `l6b`, celles où la fusion de puces était le geste principal.

| items signalés | grille | redondance avant → après |
|---:|---|---|
| 35 | RESCOS-57b — Ralentissement, téléphonique | 10 → 0 |
| 34 | RESCOS-68 — Éruption cutanée | 30 → 2 |
| 30 | RESCOS-62 — Toux, ECC Poumon | 16 → 0 |
| 27 | RESCOS-56 — Prurit | 27 → 1 |
| 19 | RESCOS-41 — Dysurie | 26 → 1 |

**Aucune grille n'est en dehors de cette logique** : la corrélation entre volume
signalé et gain de redondance est directe, et les 68 grilles restantes sont
toutes sous 10 items.

**b) Des suppressions sur un thème sensible.** Filtrage des 423 items sur les
mots porteurs de cinq familles :

| famille | items signalés | dont couverture lexicale < 0,70 |
|---|---:|---:|
| dose, posologie, unité | 41 | 3 |
| seuil, cible, score | 11 | 0 |
| contre-indication, réserve | 17 | 1 |
| drapeau rouge, gravité, urgence | 4 | 0 |
| **protection** (PAFA, curatelle, 143/147, suicide, signalement, consentement) | **0** | — |

Les **69 items sensibles** ont vu leur couverture lexicale mesurée dans le texte
visible **actuel** de leur grille. **Cinq** tombent sous 0,70, et **neuf** items
au total (sensibles ou non) sous 0,55. Les quatorze ont été relus un à un et
retrouvés dans leur bloc d'arrivée, sous une formulation plus riche. Trois
exemples :

| item signalé disparu | ce que la grille dit aujourd'hui |
|---|---|
| RESCOS-58 · « transfusion si hb 7g dl ou signes de mauvaise tolérance » | « transfusion selon une stratégie restrictive : **seuil Hb 70 g/L, relevé à 80 g/L en cas de cardiopathie ischémique** — sur-transfuser fait reprendre le saignement » |
| RESCOS-56 · « antibiothérapie IV si angiocholite » | « angiocholite : hémocultures puis **ceftriaxone 2 g IV + métronidazole** sans attendre le résultat, et drainage biliaire en urgence » |
| RESCOS-48 · « la majorité des lombalgies sont bénignes et auto-résolutives » | « la cause est le plus souvent aspécifique et évolue **favorablement en quelques jours ou semaines** … plus de **90 % sont mécaniques non spécifiques et guérissent en 4 à 6 semaines** » |

**Zéro item de la famille « protection ».** C'est cohérent avec le § 4 : le
corpus n'en portait pas au départ, il n'a donc rien pu en perdre.

Chaque lot avait déjà verdicté ses propres items un par un — 14, 67, 203, 43,
33, 40, 25 et 2 selon les lots — et plusieurs notions menacées par une réécriture
ont été **restituées avant validation** : la bande « IPS 0,91-0,99 borderline »,
le mot « normalisation » des lactates, la surveillance de la déshydratation sous
lithium, la cocaïne parmi les contre-indications du flumazénil, le doublement des
substituts nicotiniques en forte dépendance, le repos de 4-6 semaines de la MNI,
le chiffre de 95 % du grade 3 de Fisher, l'acronyme `RSV` conservé entre
parenthèses derrière `VRS`. **Aucun retrait plein**, hors les corrections
d'erreur délibérées.

### 7.6 Contrôle fonctionnel en navigateur — `--deep`, les 165

Chrome for Testing piloté par le protocole DevTools sur le WebSocket natif de
Node 22, serveur statique sur `127.0.0.1`, `--host-resolver-rules=MAP *
~NOTFOUND, EXCLUDE 127.0.0.1` : **aucune requête ne peut sortir de la boucle
locale**, aucun paquet installé.

```
grilles sondées               : 165
sans exception ni erreur      : 165 / 165
à 100 % après remplissage     : 156 / 165
écrivant ecos_registry        : 156 / 165

--- phase --deep ---
minuteur 13:00 -> autre       : 156 / 165
barre nav présente + fixed    : 156 / 165
recouvrement barre/minuteur   : 0 / 165
sans aucun crochet coloré     : 10 / 165
exceptions de cette phase     : 0 / 165
```

**Les 9 grilles qui ne rendent ni score, ni registre, ni minuteur, ni barre sont
exactement les 9 feuilles porte** — nommément : BPCO exacerbation, Diabète
pédiatrique, Dépression majeure, Dépression post-partum, Lupus érythémateux
systémique, Ostéoporose prévention, Psoriasis, TDAH pédiatrique, Transaminases
élevées. Une feuille porte est la consigne remise au candidat devant la station
(intitulé, contexte, tâches, durée) : **0 `criteria-row`, 0 `<input>`,
0 `<script>`, 0 `maxScores`. Elle n'a pas de barème, et c'est correct.** Elles
sont reconnues sur trois faits conjoints, jamais sur leur nom de fichier, pour
qu'une grille notée qui perdrait son moteur ne puisse pas se glisser dans la même
catégorie.

**156/165, et non 165/165, est le chiffre juste.** Le décompte porte sur la
**clé propre** de chaque grille. `localStorage` est partagé par toutes les pages
de la même origine, et les 165 sondages se suivent dans le même profil : compter
« `ecos_registry` non vide » rend 165/165 en attribuant à chaque grille les
entrées des précédentes — **y compris aux 9 feuilles porte, qui ne peuvent rien
écrire**. Vérifié sur profil neuf : sondées seules, elles rendent 0 clé. Ce faux
positif a vécu deux lots dans le seul contrôle capable de voir le défaut de
moteur ; il est corrigé depuis `l4`.

**RESCOS-63, sondée seule :**

```
node scripts/rescos-locales/browser_probe.js "RESCOS-63" --deep --summary
  sans exception ni erreur   : 1/1
  à 100 % après remplissage  : 1/1        (c'était 50 %, note E)
  écrivant ecos_registry     : 1/1
  minuteur 13:00 -> autre    : 1/1
  barre nav présente + fixed : 1/1
  recouvrement               : 0/1
  crochets colorés           : présents
```

Les 10 grilles sans crochet coloré sont les 9 feuilles porte et
« RESCOS-64 station double 2 », dont aucun critère ne porte de
`patient-response`. État antérieur au projet, pas une régression.

### 7.7 Un piège de mesure, et comment il a été évité

Le lot `t5` a signalé une **collision de nom entre modules de corpus**. Un script
de mesure ad hoc important d'abord `scripts/amboss/` a fait résoudre
`import report_redundancy` sur la version **AMBOSS**, dont les `BLOCKS`
diffèrent : une grille mesurée à **64** paires au lieu de 11, un total de lot à
359 au lieu de 316 — **de façon cohérente avant et après**, donc parfaitement
invisible à la comparaison.

La consigne qui en découle a été appliquée ici : **un interpréteur par corpus**,
et une assertion sur `report_redundancy.__file__` avant toute mesure. Le piège
s'est d'ailleurs présenté pendant cette vérification — un `sys.path.insert(0, …)`
mis dans le mauvais ordre a fait charger le module AMBOSS pour une mesure
destinée à RESCOS. **L'assertion l'a arrêté net.** Sans elle, le chiffre publié
aurait été faux et cohérent.

C'est le même mécanisme qui avait rendu `check_no_loss` aveugle sur les deux
tiers du corpus au lot `l3` : son `git diff --name-only` sans `-z` recevait
`"cases/rescos-locales/AMC Urgences 1 - Polytraumatis\303\251 - …"` pour tout nom
accentué — `core.quotepath` — et sautait **silencieusement** ces grilles.
132 des 165 noms portent un accent ; 156 grilles étaient modifiées, **57
seulement étaient examinées**. Corrigé par `-z`.

**Un contrôle qui se trompe en silence est pire qu'un contrôle absent** : il
produit un chiffre, et le chiffre inspire confiance.

---

## 8. Coordination et périmètre

* **Aucun fichier sous `cases/` n'a été modifié par cette vérification.**
  `git status --porcelain -- cases/rescos-locales` rend **zéro ligne**.
* **Rien lu, écrit ni exécuté sous `cases/german/`, `scripts/german/`,
  `cases/casecos/` ni `scripts/casecos/`** — l'utilisateur y travaille en
  parallèle. Leurs vérificateurs n'ont pas servi de référence.
* **Aucun `git add`** : validation directe par
  `git commit -F <fichier> -- <chemins>`, qui met en index et valide dans le même
  geste. C'est la leçon de deux incidents : au lot `l3`, un `git commit` nu a
  emporté 205 fichiers d'un volet parallèle (restitués intégralement) ; au lot
  `l6b`, un `git add` préparatoire laissé quelques secondes dans l'index a fait
  absorber seize grilles par un commit de l'utilisateur. **Commiter avec un
  `path` explicite protège de sweeper les fichiers d'autrui ; cela ne protège pas
  de se faire sweeper.**
* **`core.quotepath=false`** sur toutes les commandes git — 132 des 165 noms
  portent un accent.
* **Aucune commande réseau, aucun `git push`, aucun `git gc`, aucun
  `git prune`, aucun `timeout`.**
* **Aucune grille lue en entier avec `Read`** : tout passe par `strip_base64`
  puis `block_spans` / `visible_text` / `list_items`.

---

## Annexe — comment reproduire les vérifications

```bash
# 1. Les portes — un interpréteur par corpus, jamais deux modules de corpus ensemble
python3 scripts/rescos-locales/check_invariants.py       # OK — 165 grilles, code 0
python3 scripts/rescos-locales/check_nomenclature.py     # OK — 0 terme, code 0
python3 scripts/rescos-locales/check_reachability.py     # OK — 156/156 notées, code 0

# 2. Les témoins, chacun dans son propre processus
python3 scripts/amboss/report_redundancy.py  --quiet     # TOTAL : 147
python3 scripts/rescos/report_redundancy.py  --quiet     # TOTAL : 127

# 3. Redondance du corpus — plusieurs minutes, O(n²) en items PAR grille
python3 scripts/rescos-locales/report_redundancy.py --quiet   # TOTAL : 1003

# 4. Non-perte — RAPPORT, code 0 en toutes circonstances.
#    Ne jamais le câbler comme porte : ce serait bloquer sur des suppressions légitimes.
python3 scripts/rescos-locales/check_no_loss.py 7c77e3e

# 5. Contrôle fonctionnel — strictement local, aucun paquet installé
node scripts/rescos-locales/browser_probe.js --deep --summary
node scripts/rescos-locales/browser_probe.js "RESCOS-63" --deep --summary
```

Le snapshot de barème se recalcule depuis n'importe quelle référence git en
appelant `snapshot_invariants.snapshot_one` sur le contenu d'un blob
(`git show <ref>:<chemin>`) plutôt que sur un fichier du disque ; le renommage
`RESCOS-69 → RESCOS-69b` doit être appliqué à la clé avant comparaison, sans quoi
la grille apparaît des deux côtés comme absente.

`report_redundancy.py` **exclut le bloc `scenario` par défaut** — c'est le script
du patient simulé, redire les symptômes est sa fonction — et `check_no_loss.py`
l'**inclut** : les deux scripts n'ont pas le même objet. Exclure le scénario
d'une mesure de doublons est un choix éditorial ; l'exclure d'un contrôle de
perte laisserait le réécrire sans trace.
