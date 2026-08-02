# Refonte pédagogique des 198 grilles ECOS CasECOS — rapport de vérification finale

Branche `refonte-amboss-suisse` · Base de mesure du corpus : `d0a89f4` · État vérifié :
`302f0d1` · Journal détaillé : `docs/superpowers/journal-casecos-2026-08.md` · Procédure :
`scripts/casecos/PROCEDURE-casecos.md` · Rapports de lot :
`.superpowers/sdd/2026-07-30-amboss-refonte-pedagogique-suisse/k5{a,b,c,d,e,f}-report.md`

> Ce document est le pendant de `rapport-amboss-2026-08.md`, `rapport-german-2026-08.md` et
> `rapport-rescos-2026-08.md` pour le quatrième et dernier corpus. Il en reprend la
> structure. Tout ce qui n'y est pas redit — la hiérarchie à trois niveaux, la règle du
> format, la règle anti-perte — reste valable tel quel.

> **Sur l'état vérifié.** `302f0d1` est le HEAD de la branche au moment de la vérification.
> Les six commits les plus récents relèvent du chantier `cases/german/` mené en parallèle
> et ne touchent pas ce corpus. Les neuf commits CasECOS de la campagne vont de `fae03ba`
> à `e4d3863`.

---

## 0. Résultat des vérifications

Sept vérifications ont été menées, dont deux témoins destinés à établir que la campagne
CasECOS n'a rien perturbé chez les voisins. **Les sept passent.**

| # | Vérification | Commande | Code | Résultat |
|---|---|---|---|---|
| 1 | Invariants | `scripts/casecos/check_invariants.py` | **0** | **198 grilles**, tous les invariants préservés |
| 2 | Nomenclature | `scripts/casecos/check_nomenclature.py` | **0** | aucun terme non suisse détecté |
| 3 | Atteignabilité du barème | `scripts/casecos/check_reachability.py` | **0** | **198/198**, barème atteignable à 100 % sur chaque section, moteur calculable |
| 4 | Non-perte d'information | `scripts/casecos/check_no_loss.py d0a89f4` | **0** | 150 items signalés sur 69 grilles, **verdictés, aucune perte** (§ 6.4) |
| 5 | Redondance CasECOS | `scripts/casecos/report_redundancy.py` (10 tranches agrégées) | **0** | **417** paires inter-blocs, 719 intra-bloc |
| 6 | Témoin AMBOSS | `scripts/amboss/report_redundancy.py` | **0** | **147 — inchangé** |
| 7 | Témoin RESCOS | `scripts/rescos/report_redundancy.py` | **0** | **127 — inchangé** |

**Les deux témoins n'ont pas bougé d'une paire.** C'est vérifiable par construction :
l'outillage CasECOS **importe** de `scripts/amboss/` tout ce qui ne décrit pas un corpus —
`strip_base64`, `visible_text`, `norm`, `_bullet_items`, la table `BANNED`, la simulation de
`cases/scoring.js` — de sorte qu'il n'existe qu'une seule implémentation de chacune.

`scripts/german/` n'a été ni écrit ni exécuté. Ses grilles ont été **lues** une fois, en
lecture seule, pour le décompte des quatre corpus du § 8 et pour le relevé de la ligature
du § 7.7.

### Sur le découpage de la mesure de redondance

Le corpus fait 198 grilles et la mesure y est en O(n×m) sur ~190 items par grille : une
passe unique dépasse 120 s. Elle a donc été découpée en **dix tranches de 20 grilles**
lancées en parallèle, puis agrégée. **Le découpage est exact et non approché** :
`report_redundancy.py` n'apparie que des items d'une **même** grille — il n'existe aucune
paire inter-grilles — donc la somme des tranches est le total, au sens strict.

**Deux contrôles indépendants confirment l'agrégat de 417 :**

1. **La somme des six lots.** Chaque lot k5 a publié son propre chiffre d'arrivée :
   27 + 58 + 41 + 46 + 111 + 134 = **417**. La mesure d'aujourd'hui, prise à `302f0d1` par
   un chemin entièrement différent, tombe sur le même nombre — donc rien n'a dérivé depuis
   `e4d3863`.
2. **Le couple `expert ↔ theorie`.** La somme des six lots donne 4 + 2 + 0 + 0 + 1 + 25 =
   **32**. La ventilation par couple de blocs de la mesure agrégée rend **32**.

---

## 1. Le périmètre et la méthode

### 1.1 Ce que porte une grille CasECOS

Les 198 grilles portent dix blocs de contenu — `annexe-dd`, `redflags`, `therapy`,
`cloture`, `exemples`, `expert`, `theorie`, `scenario`, `defi`, `annexe-nu` — dont
plusieurs vivent **en amont** de la zone pédagogique, dispersés au fil de la page. C'est
ce qui a imposé, ici comme dans German et RESCOS, de lire les blocs et non deux zones
continues : aucune zone ne les englobe sans avaler aussi les critères notés.

Quatre de ces blocs sont **notés** — `therapy`, `redflags`, `cloture`, `exemples` — et
sont intouchables par consigne. `scenario` est le script du patient simulé et reste exclu
de la mesure de redondance par défaut, comme dans les trois autres corpus.

### 1.2 Le contrat de blocs, et le test qui tranche `expert ↔ theorie`

Le livrable central du pilote k4 n'est pas une grille, c'est le **contrat de blocs**, écrit
au § 2 de `scripts/casecos/PROCEDURE-casecos.md`. Il tranche la frontière qui portait à
elle seule **405 des 830 paires** du relevé initial, soit près de la moitié de toute la
redondance du corpus.

La frontière `expert ↔ theorie` ne se trace **pas** sur le caractère actionnable de
l'item — ce critère intuitif ne départage rien — mais sur son **référent**, par une
question unique :

> **Changez le patient : l'item survit-il ?**
>
> Il survit → il appartient à `theorie`, le bloc canonique.
> Il meurt avec le patient → il appartient à `expert`.

Le motif que ce test révèle est constant sur les six lots : **`expert`/Points clés est, dans
ce corpus, un cours en réduction** — épidémiologie, classifications, posologies détaillées,
résultats d'études — que `theorie` porte déjà, presque toujours plus richement. Sur le
dernier lot, ce n'était même plus un cours en réduction mais **le cours de `theorie`
recopié en abrégé, ligne pour ligne**. `expert`/Rôles et `expert`/Pièges, eux, tiennent
leur rôle et n'ont presque pas bougé.

Deux sections de `theorie` échappent au test — « Diagnostic » et « Résumé du cas
clinique ». Elles y restent : elles sont le logement CasECOS du `resume` manquant, et aucun
autre bloc ne restitue le cas en narration synthétique.

**La règle de retrait, inchangée de k5a à k5f.** Un item d'`expert` n'est retiré que si :
(a) le test du référent l'attribue à `theorie` ; (b) `theorie` porte déjà son contenu
**intégral**, vérifié terme à terme — en portant d'abord dans `theorie` ce qui lui
manquait ; (c) `expert` garde le comportement observable correspondant dans `Rôles` ou
`Pièges`. Sinon l'item est **spécialisé** — le générique part dans `theorie`, la
formulation d'`expert` redevient une action observable *dans cette station* — ou laissé.
Aucune sous-section « Points clés » n'a été vidée ; contrôle posé avant application.

### 1.3 Pourquoi l'interdit AMBOSS ne se transpose pas

AMBOSS s'était donné une règle : **« `theorie` ne porte jamais de protocole »**. Elle ne
se transpose pas ici, et c'est un choix motivé, pas un relâchement.

**Cet interdit avait un bénéficiaire.** Chez AMBOSS, le protocole retiré de `theorie` avait
une destination : le bloc `resume`, canonique de ce corpus. L'interdit ne supprimait rien,
il déplaçait.

**CasECOS n'a pas de `resume`.** Ici, `theorie` *est* le canonique. Un protocole chassé de
`theorie` n'a aucune destination licite :

| destination | pourquoi elle est fermée |
|---|---|
| la suppression | c'est une perte sèche — l'information n'existe nulle part ailleurs |
| `expert` | casse le référent : un protocole survit au changement de patient, le test l'attribue à `theorie` |
| `therapy` | c'est une **section notée**, intouchable par consigne |

Le cas d'espèce est la section « Algorithme de prise en charge empirique (HUG) » du pilote.
Appliquer l'interdit AMBOSS l'aurait détruite. **Un interdit sans bénéficiaire n'est pas un
contrat, c'est une amputation** : il a été explicitement levé pour ce corpus, et le
corollaire est assumé — les `theorie` de CasECOS portent des protocoles.

### 1.4 Ce qui n'a pas été touché

- **Aucune section notée n'a été modifiée au titre du dédoublonnage.** Sur les 206 lignes
  de diff du dernier lot, 206 sont des `<li>` d'`expert` ou de `theorie` — mesuré par
  filtrage du diff, pas supposé.
- Les seules corrections en zone notée sont **institutionnelles** (§ 5.5), et aucune n'a
  changé de structure : `criteriaCount`, `detailCount`, `radioCount`, `checkboxCount`,
  `maxScores`, `coef`, `scoreSpans`, `sectionCounts` sont gelés au snapshot et verts sur
  les 198.
- **`annexe-dd` ne se nettoie pas** : le bloc de différentiels est riche et sain (97,5 % de
  formulations distinctes), et ses paires sont pour l'essentiel des artefacts de mesure
  (§ 4.3).

---

## 2. Les chiffres

### 2.1 Volume

| Mesure | `d0a89f4` | `302f0d1` |
|---|---|---|
| Grilles | 198 | **198** |
| Termes de nomenclature non suisses | **649** (relevé k1) → **889** traités | **0** |
| Grilles réécrites à la passe de nomenclature | — | **132** |
| Grilles touchées par le contrat de blocs | — | **163** |
| Diff du contrat de blocs | — | **298 insertions, 556 suppressions** |
| Diff total sur `cases/casecos` | — | 198 fichiers, 2 810 insertions, **153 350 suppressions** |
| Paires quasi identiques **entre** blocs | **830** | **417** |
| Paires quasi identiques **dans** un même bloc | — | 719 |
| Grilles à zéro paire inter-blocs | — | **72 / 198** |
| Trous du bloc canonique comblés | — | **97** (six lots) + 3 (pilote) |
| Grilles au barème atteignable à 100 % | 198 / 198 | **198 / 198** |
| Grilles levant une `TypeError` à chaque recalcul | **198** | **0** |
| Grilles remontant leur score au tableau de bord | **0** | **198** |

Les 153 350 suppressions sont massivement **du code, pas du contenu** : la bascule des 198
copies embarquées du moteur de calcul (~726 lignes chacune) vers `cases/scoring.js`
(§ 6). Le contenu médical, lui, se compte en centaines de lignes.

La redondance de départ vaut **830** au relevé k1 et **832** après la passe de nomenclature
— +2, expliquées grille par grille (§ 5.1). Les lots ont travaillé sur la base 832.

### 2.2 Par lot

| Lot | Grilles | Modifiées | Inter-blocs avant → après | `expert ↔ theorie` | Trous comblés |
|---|---|---|---|---|---|
| **k4** (pilote) | 1 | 1 | 0 → 0 | — | **3** |
| **k5a** | 25 | 24 | **66 → 27** (−59 %) | 36 → 4 (−89 %) | **8** (+1 hors table) |
| **k5b** | 35 | 28 | **149 → 58** (−61 %) | 81 → 2 (−97,5 %) | **15** |
| **k5c** | 40 | 27 (+7 hors lot) | **94 → 41** (−56 %) | 46 → **0** | **7** |
| **k5d** | 40 | 29 (+1 hors lot) | **86 → 46** (−47 %) | 35 → **0** | **16** |
| **k5e** | 32 | 23 (+1 hors lot) | **180 → 111** (−38 %) | 63 → 1 (−98 %) | **26** |
| **k5f** | 26 | 26 | **257 → 134** (−48 %) | 142 → 25 (−82 %) | **25** |
| **Total** | **198** | — | **832 → 417 (−49,9 %)** | **403 → 32 (−92,1 %)** | **97** |

k5e traite les rangs 141-170 **plus** les jumelles 179 et 194, que k5f exclut donc de son
périmètre : 25 + 35 + 40 + 40 + 32 + 26 = 198, sans recouvrement ni trou.

### 2.3 Où sont les 417 paires restantes

| Couple de blocs | Paires | Statut |
|---|---|---|
| **`theorie ↔ therapy`** | **137** | **le premier poste, et le seul qui n'ait jamais eu d'instrument propre** (§ 7.1) |
| `annexe-dd ↔ theorie` | 103 | `annexe-dd` ne se nettoie pas — pour partie artefact d'étiquette (§ 4.3) |
| `redflags ↔ theorie` | 52 | bloc **noté** contre canonique : le barème et le cours doivent se recouvrir |
| `annexe-dd ↔ redflags` | 38 | deux blocs non nettoyables, dont l'artefact de négation |
| `expert ↔ theorie` | **32** | résiduel irréductible (§ 4.2) |
| `annexe-dd ↔ expert` | 25 | script de révélation d'`expert` contre arguments d'`annexe-dd` |
| `expert ↔ redflags` · `annexe-dd ↔ therapy` · `redflags ↔ therapy` | 7 · 7 · 7 | — |
| `expert ↔ therapy` | 5 | — |
| `cloture ↔ *` | 4 | phrases modèles de « Réponses types du candidat » |

**Les paires restantes sont, à trente-deux près, entre des blocs que le contrat interdit de
dédoublonner.** Quatre des cinq premiers couples ont un côté noté ou `annexe-dd`.

Répartition intra-bloc, mesure additionnelle jamais additionnée au chiffre de référence :
`theorie` 330, `annexe-dd` 277, `expert` 76, `therapy` 17, `redflags` 16, `cloture` 3.

### 2.4 Concentration

72 grilles sur 198 sont à **zéro** paire inter-blocs. Les plus chargées :

| Grille | Inter | Intra |
|---|---|---|
| `Convulsion fébrile - Nourrisson 18 mois` | 17 | 8 |
| `Spondylarthrite axiale - Laborantin 30 ans` | 15 | 11 |
| `Péritonite par perforation ulcéreuse` | 14 | 12 |
| `Fracture vertébrale ostéoporotique` · `HSA avec convulsion` · `Vertiges aigus` | 13 | 7 · 4 · 4 |
| `Tendinite coiffe rotateurs` · `UIDC-Monsieur Arden` | 12 | 4 · 15 |

---

## 3. Les trous du bloc canonique comblés

**C'est le résultat le plus substantiel de la campagne, et il n'est pas une réduction : ce
sont 97 ajouts.** Des informations que la section **notée** faisait exécuter ou citer, et
que la fiche de révision ne portait pas. Un candidat qui révisait par `theorie` — le bloc
canonique, celui qui est fait pour cela — ne les rencontrait jamais.

Le cas extrême est `UIDC-Monsieur Marcel T.` : **`GOLD` compte huit occurrences dans la
seule section notée** — la cotation fait classer le patient en GOLD II — **et zéro dans
`theorie`**. La cotation exige un savoir que le cours ne porte pas.

Groupés par nature. Un même trou peut relever de deux familles ; il est classé par ce qui
le rend grave.

### A. L'instrument que la cotation exige et que le cours ne nomme pas

La figure la plus fréquente, et celle que le lot 6 a fait exploser en étendant le relevé
aux `criteria-detail` (§ 4.5). **Sept instruments nommés dans la cotation, absents du
cours** pour le seul dernier lot.

| Instrument | Grille |
|---|---|
| **classification GOLD** | `UIDC-Monsieur Marcel T.` — 8 occ. notées, 0 dans `theorie` |
| **test de Schober**, **BASFI**, **BASMI** | `Spondylarthrite axiale` |
| **ICIQ-UI / IIQ-7** | `UIDC-Madame Ondine` — vivait dans un `criteria-detail` seul |
| **index de Charlson** | `UIDC-Mme Victoria` — `criteria-detail` seul |
| **test de Grober et Buschke** | `UIDC-Madame Siaulat` |
| **score de Boyer** | `UIDC-Thomas` |
| **classification de Hinchey** | `UIDC-Mlle Olivia Veyre` |
| **échelle de Bristol**, sigle **CRM** | `UIDC-Monsieur Dupont` |
| **NIHSS** et **ASPECTS** — les deux scores qui gouvernent la station | `UIDC-Monsieur Paretic` |
| **score CRUSADE** | `STEMI - Femme 55 ans` |
| **sPESI** (Wells n'est que diagnostique), **CRB-65 / CURB-65** | `Dyspnée multifactorielle` |
| **score de Boey**, **Mannheim Peritonitis Index** | `Péritonite par perforation ulcéreuse` |
| **score CAGE / AUDIT-C** | `Méléna sous anticoagulant` |
| **échelle de désespoir de Beck** | `AMC-Psy-P5` — le fait était là, l'instrument non |
| **Timed Up and Go / Tinetti** | `Fracture vertébrale ostéoporotique` |
| **stratégie treat-to-target** | `AMC-MedInterne-P14` — la cible qui donne son sens au DAS28 déjà prescrit |
| **substrats électriques de la syncope** — QTc/Bazett, Brugada, WPW, ondes epsilon | `AMC-MedInterne-P1` — `theorie` prescrivait « ECG 12 dérivations » sans dire ce qu'on y cherche |
| **seuil du Glasgow-Blatchford** | `AMC-Chir2-ECG3` — et la seule occurrence existante était **fausse** (§ 5.1) |

### B. Le diagnostic grave à écarter, absent du canonique

| Manquait | Grille |
|---|---|
| **dissection aortique** — douleur déchirante migratrice, asymétrie tensionnelle, élargissement médiastinal | `UIDC-Monsieur H. Toinnes` (IDM) et `AMC-MCPR-ARC6` |
| **dissection vertébrale** | `Vertiges aigus - Adulte` |
| **infarctus de l'AICA** — le seul AVC qui imite un vertige périphérique ; **HINTS Plus** | `AMC-ORL-P2`, propagé à `AMC-ECOS1-S3` |
| **démence à corps de Lewy** et sa contre-indication aux neuroleptiques | `UIDC-Madame Siaulat` |
| **Creutzfeldt-Jakob**, démence rapidement progressive | `AMC-Psy-S4` |
| **syndrome de la queue de cheval** et **spondylodiscite** | `AMC-ECOS1-S9` |
| **compression médullaire** — l'urgence neurochirurgicale du myélome | `AMC-MedInterne-P11` |
| **NMOSD, MOGAD, ADEM** — les « diagnostics alternatifs » que McDonald 2017 exige d'exclure sans les nommer | `AMC-Neuro-P1` |
| **CTEPH** — la seule complication de l'EP curable chirurgicalement | `AMC-MedInterne Embolie pulmonaire` |
| **torsion d'annexe**, **salpingite** | `UIDC-Mlle Olivia Veyre` |
| **Mallory-Weiss**, Boerhaave, pneumomédiastin | `Anorexie boulimie`, propagé à `AMC-ECOS1-S1` |
| **syndrome de Conn**, **syndrome de Cushing**, réglisse | `UIDC-Monsieur H. Toinnes` (HTA) |
| **fistule aorto-duodénale**, dépistage des fratries > 55 ans | `AMC-Chir4-ECG3` (AAA) |
| **crise cholinergique** — l'autre cause d'aggravation aiguë du myasthénique, **dont le traitement est inverse** | `AMC-Neuro-P4` |
| **cirrhose** — le substrat des varices que `theorie` chiffrait déjà | `Méléna sous anticoagulant` |
| **DPPNI**, oligohydramnios / RCIU | `Prééclampsie - Femme 36 ans` |

**`UIDC-Monsieur H. Toinnes` décrivait le signe sans jamais nommer la maladie** :
« dissection » avait 0 occurrence dans le `theorie` d'une station de douleur thoracique
aiguë, contre 3 dans la section notée. La page SSP en compte 33, avec ce piège :
« anticoaguler pour un SCA sans avoir écarté la dissection — c'est l'erreur qui tue ».

### C. Le signe clinique ou l'éponyme d'examen

**signes de Kernig et de Brudzinski** (`AMC-Neuro-R1`, `Convulsion fébrile`,
`UIDC-Madame Kopf`, `UIDC-Thomas`) · **signe de Russell** (`Anorexie boulimie`, dans un
`criteria-detail` seul, 0 occurrence dans tous les blocs) · **signe de Hutchinson** et
**réflexe de Cushing**, les deux signes de l'engagement (`AMC-Neuro-P7`) · **signe
d'Hennebert** et la séquence d'érosion du cholestéatome (`AMC-ORL-P1`) · **Weber et Rinne**
au diapason (`Vertiges aigus`) · **purpura fébrile** et **bombement de la fontanelle**
(`UIDC-Thomas`) · **hyperréflexie ostéo-tendineuse**, éclampsie imminente
(`Prééclampsie`) · **fond d'œil** et évaluation clinique de l'HTIC (pilote k4, `Migraine`) ·
**œdème papillaire = signe d'HTIC** (`Céphalées - Homme 30 ans`) · **Se 91 % / Sp 26 %** du
Lasègue, 29/88 du Lasègue croisé (`Examen physique lombalgie`) · **triade
céphalées-palpitations-sueurs** et son caractère paroxystique (`AMC-Chir5-ECG5`) ·
composants de la **triade de Beck** (`AMC-Chir4-ECG5`) · **l'auscultation entière** de la
sténose aortique — `theorie` n'avait aucune section clinique (`AMC-Chir4-ECG6`).

### D. Le *pourquoi* du traitement — le rationnel logé dans une section notée

**Sept confirmations consécutives**, une par lot, du motif annoncé par le pilote : la
structure `Traitement : X` / `Détails : …` d'un `therapy-item` invite à loger le rationnel
dans une section **notée**, où le candidat qui révise ne le lit pas.

| Le rationnel manquant | Grille |
|---|---|
| **œdème cérébral**, mortalité 25 % — le *pourquoi* de la réhydratation lente | `UIDC-Caroline` (acidocétose) |
| **HTIC** — 7 occ. `therapy`, 2 `redflags`, **0 `theorie`** — le *pourquoi* des vasodilatateurs cérébraux proscrits | `HSA avec convulsion` |
| **rationnel de la cible HbA1c** — DCCT, risque d'hypoglycémie ×3 | `AMC-Chir2-Vignette5` |
| **syndrome de revascularisation** — hyperkaliémie, acidose, IRA myoglobinurique, Volkmann | `AMC-Chir4-ECG1` |
| **5-10 % d'instabilité chronique** — le *pourquoi* de la rééducation proprioceptive | `AMC-Chir3-Vignette3` |
| **complications post-gastrectomie** — anémie ~50 %, dumping, rationnel de la B12 | `AMC-Chir2-ECG2` |
| **germes d'Anthonisen** — *Haemophilus*, *S. pneumoniae*, *Branhamella* | `AMC-MedInterne-P3` |
| **station au sol > 1 h** — rhabdomyolyse, hypothermie, escarres, CK | `AMC-CasECOS Gériatrie` |
| **foyers infectieux pré-op / avis urologique** — sondage → infection prothétique | `AMC-Chir3-ARC1` |

### E. Le délai, le seuil, le chiffre pronostique

**90 min / 120 min** du STEMI, cinétique des troponines, complications mécaniques J3-J7 et
Dressler · **délai opératoire 24-48 h** et **mortalité 5-8 % à 1 mois, 20-30 % à 1 an** du
fémur proximal · **IRM < 24 h / décompression 24-48 h** de la queue de cheval, « au-delà,
les séquelles sphinctériennes sont définitives » · chirurgie **< 6 h** de la hernie
étranglée, risque d'étranglement **15-20 %** · **3 mois** de consolidation du 1/3 moyen du
scaphoïde, signal T2 de la nécrose, *humpback deformity* · survie de l'ostéosarcome
**60-70 % / 20-30 %** · **75 %/25 % à 5 ans** de l'AOMI · **10-20 % à 90 j** de la sténose
carotidienne · récidive du pneumothorax **30-50 % puis 50-70 %** · durée de la
**légionellose 14-21 j** — `theorie` portait 5-7 j et 7-14 j, pas celle-là · seuil fébrile
**38,5 °C** (deux grilles) · **mortalité la plus élevée** de toutes les maladies
psychiatriques, pour l'anorexie · épidémiologie **dépendante du lieu** : douleur pariétale
1 fois sur 2 et cardiovasculaire 16 % en premier recours contre **54 %** aux urgences —
dans une station intitulée « au cabinet médical ».

### F. La complication ou l'effet indésirable non nommé

**hyperglycémie transitoire post-infiltration** (`Tendinite coiffe rotateurs`) ·
**contre-indications des stimulants** — cardiopathie, psychose, glaucome à angle fermé,
hyperthyroïdie, IMAO — auxquelles `theorie` renvoyait **deux fois sans les nommer**
(`AMC-Psy-P12`) · **antidote de la digoxine** (fragments Fab, Digifab®) et les signes du
surdosage digitalique (`AMC-Pharmaco-S3`) · **SUDEP** — l'argument d'observance
(`AMC-Neuro-P5`) · **syndrome post-thrombotique**, 0 occurrence dans `theorie`, et filtre
cave (`AMC-Chir4-Vignette1`) · **syndrome optico-pyramidal** et **syndrome
d'hyperperfusion** (`AMC-Chir4-Vignette2`) · morbidité propre de la thyroïdectomie
(1-2 % / 10-30 % / 1-3 % / 1 %) · **SIADH, Cerebral Salt Wasting, Takotsubo, OAP
neurogène**, re-saignement, hydrocéphalie et DVE, vasospasme (`HSA et refus de soins`) ·
**SAOS** associé à l'hypertrophie adénoïdienne (`AMC-ORL-P9`) · **risque suicidaire de la
phobie sociale** — 0 occurrence de « suicid » dans `theorie` (`AMC-Psy-P6`).

### G. La molécule ou l'option thérapeutique absente

**anti-RANKL** (dénosumab) et **SERM** (raloxifène) et ses bouffées de chaleur
(`Fracture vertébrale ostéoporotique`) · **clopidogrel**, P2Y12 de 2ᵉ ligne (`STEMI`) ·
**CRASH-2** et l'acide tranexamique, **exsufflation à l'aiguille** du pneumothorax sous
tension (`Trauma abdominal pénétrant`) · **rivastigmine** et **galantamine**, à côté du seul
donépézil que `theorie` nommait (`UIDC-Madame Siaulat`) · **thérapie narrative d'exposition**
(`AMC-Psy-P3`) · fenestration sur malperfusion réfractaire (`AMC-Chir4-ECG5`) ·
**lésion de Maisonneuve** — 0 occurrence dans **toute** la grille, alors que les critères
d'Ottawa ne couvrent pas le péroné proximal (`AMC-Chir3-Vignette3`, puis `AMC-MCPR-ARC15`,
**la même station dupliquée**) · **infirmière scolaire** — le seul relais qu'une
adolescente puisse atteindre seule (`AMC-MCPR-ARC14`) · **pied diabétique** et « contrôler
tous les FRCV compte autant que la glycémie » (`AMC-MCPR-ARC17`).

---

## 4. La leçon d'instrumentation

**Aucun des 97 trous n'a été trouvé par `report_redundancy.py`.** Sept lots consécutifs
l'ont constaté et écrit. C'est le résultat méthodologique de la campagne, et il déborde
largement ce corpus.

### 4.1 Pourquoi le détecteur de doublons ne voit pas l'inclusion

`report_redundancy.py` mesure par `SequenceMatcher(None, a, b).ratio()`, qui vaut `2M/T` —
deux fois le nombre de caractères appariés, divisé par la longueur totale des deux chaînes.

**Conséquence arithmétique : un item long qui en contient intégralement un court plafonne
vers 0,60.** Si le court fait `c` caractères et le long `l`, avec inclusion parfaite,
`M = c` et `T = c + l`, donc `ratio = 2c/(c+l)`. Sur ce corpus :

| Lot | longueur moyenne `theorie` | longueur moyenne `therapy` | plafond sur inclusion parfaite |
|---|---|---|---|
| k4 (pilote) | 145 c. | 308 c. | **0,64** |
| k5a | 70 c. (n = 1 622) | 164 c. (n = 300) | **0,60** |

**Le seuil du projet est 0,72. Le plafond d'une inclusion parfaite est en dessous.** Une
inclusion totale — le pire doublon possible — est donc structurellement **invisible**, et
elle l'est d'autant plus qu'elle est plus flagrante. Le détecteur est aveugle exactement là
où il devrait crier.

Mesure directe, par recouvrement de vocabulaire (jetons de plus de 2 lettres, mots-outils
retirés), lot par lot :

| Lot | inclusions ≥ 90 % `theorie → therapy` | dont **invisibles** au seuil | paires effectivement mesurées |
|---|---|---|---|
| k5a | 30 | **24 (80 %)** | 11 |
| k5b | 97 | **91 (94 %)** | 14 |
| k5c | 64 | **60 (93 %)** | 7 |
| k5d | 75 | **68 (91 %)** | 15 |
| k5e | 94 | **70 (74 %)** | 24 |

**Sur `theorie ↔ therapy`, la mesure voit environ une inclusion sur dix.** Le chiffre publié
de 137 paires n'est pas un total, c'est un plancher, et un plancher très bas.

Le couple `expert ↔ theorie` a le même grain des deux côtés — 79 et 80 caractères en
moyenne — et k4 en avait conclu qu'il était exempt du biais. **Il ne l'est pas :** 25 % de
ses inclusions intégrales restent invisibles (« IRM = examen de référence pour
l'extension », inclusion 1,00, ratio 0,65). Et après traitement, **100 % du résiduel est
invisible au seuil** — sur k5c, k5d et k5e successivement. Le seuil de 0,72 a été poussé
jusqu'à son plancher sur ce couple.

**Le seuil n'a pas été touché.** C'est la mesure publiée du projet, elle garde AMBOSS (147),
RESCOS (127), German et CasECOS (417) comparables. Le corriger reviendrait à annuler la
comparabilité pour gagner une visibilité qu'un instrument séparé donne sans rien casser.

### 4.2 Les trois instruments qui ont réellement trouvé les trous

**1. Le relevé d'éponymes.** Relevé automatique des termes distinctifs — éponymes
capitalisés, acronymes de 3 à 6 lettres — présents dans les blocs **notés** et de compte
**nul** dans `theorie`, mesuré sur le texte visible bloc par bloc. Introduit à k5d, où « il
a rendu la majorité des trous du lot ».

Il a fallu le débruiter : le corpus écrit « CONTRE-INDICATIONS », « ATTENTION »,
« CRITIQUE », « ESSENTIEL », « URGENCE » en capitales pour insister, et un détecteur
d'acronymes naïf les rapporte tous. Le filtre retenu est empirique et se mesure sur le
corpus lui-même — **tout jeton dont la forme minuscule apparaît ≥ 8 fois en minuscules
dans les 198 grilles est un mot français d'emphase, pas un sigle**. Effet : le bruit passe
de 424 lignes à 68 entrées exploitables.

**2. L'usage inversé.** Appariement à **seuil abaissé (0,45)** des items de
`therapy`/`redflags` contre les blocs de restitution, en retenant ceux dont le meilleur
appariement est **ailleurs que dans `theorie`**, puis confirmation par comptage du terme
bloc par bloc.

> **La signature est exacte** : une information qui relie un bloc **noté** à un autre bloc
> **sans passer par le canonique** signale un manque du canonique. Un détecteur de doublons
> devient un détecteur de trous, sans une ligne de code de plus — mais **il faut le lire à
> l'envers, et abaisser son seuil.**

**3. Le détecteur direct** (k5f). Tout jeton de contenu présent ≥ 2 fois dans `therapy`,
`redflags` ou la section notée, absent de `theorie`, et de fréquence documentaire < 35 %
des 198 grilles. C'est lui qui a rendu `dissection` (4 occurrences), `GOLD` (8) et
`confusionnel` (9).

**La démonstration la plus directe** est que **plusieurs des grilles portant un trou
mesuraient zéro paire inter-blocs** — `AMC-Chir2-Vignette5`, `AMC-Chir3-ARC1`,
`AMC-MedInterne-P11`, `AMC-ORL-P2`. Un `report_redundancy.py` vide ne dit rien du travail à
faire. **C'est le contrat qui trouve le travail, et la mesure qui le confirme — jamais
l'inverse.**

### 4.3 Ce que la mesure voit et qui n'est pas une redondance

Symétriquement, une part du chiffre de 417 est de l'artefact. Quatre familles, toutes
mesurées :

- **L'artefact de négation.** `SequenceMatcher` ne voit pas la négation. « absence de
  facteurs de risque cardiovasculaire évidents » (`annexe-dd`, arguments CONTRE) contre
  « 5. Facteurs de risque cardiovasculaire élevés » (`redflags`) s'apparient à **0,83** en
  disant l'inverse l'un de l'autre. Cinq occurrences sur `AMC-ECOS1-S3`, sept sur
  `AMC-ECOS1-S5`. **Ne jamais résoudre une telle paire.**
- **L'artefact d'étiquette.** « 2. Thymome et autres tumeurs thymiques — arguments POUR »
  contre « 2. Thymomes et autres tumeurs thymiques (35-50 %) » : deux étiquettes de
  structure, aucun contenu. Quatre paires sur cinq d'une grille entière.
- **L'artefact de numérotation.** `redflags` titre « 1. », « 2. » ; `theorie` numérote ses
  classifications de même. D'où « 2. Retard de consolidation » contre « C : retard de
  consolidation » à **0,96**.
- **L'artefact de rôle.** Un Piège (« Oublier l'antibioprophylaxie ») ou un Rôle
  (« Évaluer la prise en compte des aspects éthiques ») s'apparie mécaniquement à l'item de
  `theorie` qu'il nie ou qu'il désigne. **18 des 25 paires `expert ↔ theorie` résiduelles du
  dernier lot** sont de cette famille.

### 4.4 Ce que cela implique pour les corpus déjà clos

**C'est le point à ne pas adoucir.**

`report_redundancy.py` mesure une **ressemblance de chaînes à longueurs voisines**. Il ne
mesure pas la redondance. Sur des blocs de grain comparable il en attrape une bonne part ;
dès que les grains divergent, il décroche, et il décroche **silencieusement** — un chiffre
bas se lit comme un corpus propre.

Trois conséquences, sans atténuation :

1. **Un chiffre de redondance bas ne certifie pas l'absence de redondance par inclusion.**
   Les mesures publiées d'AMBOSS (147), German et RESCOS (127) sont des mesures de
   ressemblance de surface. Aucune n'a été confrontée à une mesure d'inclusion. **On ne
   sait pas ce qu'elles cachent** — la seule chose établie est qu'ici, sur le couple le
   plus asymétrique, elles auraient caché neuf inclusions sur dix.
2. **Les trous du canonique sont un angle mort de tout l'outillage existant.**
   `check_no_loss` compare l'avant et l'après d'une même grille : il ne voit pas les trous,
   qui lui sont **antérieurs**. `check_invariants` gèle des structures, pas des contenus.
   `check_reachability` vérifie que le barème est atteignable, pas qu'il est enseigné.
   Aucun des trois n'a jamais pu voir qu'une station faisait coter un classement GOLD dont
   le cours ne dit pas un mot. **Les 97 trous étaient tous là, sous sept vérificateurs
   verts.**
3. **Le rendement des trois instruments n'a jamais fléchi.** 8, 15, 7, 16, 26, 25 sur six
   lots successifs — la courbe monte au lieu de descendre, parce que l'instrument s'est
   affiné plus vite que le gisement ne s'épuisait. **Rien n'autorise à penser que les trois
   autres corpus en soient exempts**, et RESCOS avait déjà rendu 20 trous par la seule
   lecture inversée, sans relevé d'éponymes ni extension aux `criteria-detail`.

### 4.5 La découverte du lot 6 : étendre le relevé aux `criteria-detail`

k5d avait borné le relevé d'éponymes à `redflags` et `therapy`. k5e a buté sur un contre-
exemple : le **signe de Russell** d'`Anorexie boulimie` n'est ni dans `redflags` ni dans
`therapy` — il est dans un **`criteria-detail` de la section notée** (« Signe de Russell
(cals/lésions sur le dos de la main dominante) »), avec **0 occurrence dans tous les blocs
de la grille**. L'instrument borné ne pouvait pas le voir. k5e a recommandé l'extension
sans la faire.

**k5f l'a faite, et neuf de ses vingt-cinq trous en viennent** — dont la totalité de ceux de
`UIDC-Madame Ondine`, `UIDC-Mme Victoria` et `UIDC-Monsieur Marcel T.`, trois grilles que
l'instrument précédent laissait entièrement dans l'ombre.

**La figure est toujours la même : la section notée fait exécuter un geste ou citer un
score que le canonique ne nomme pas.** Schober, ICIQ, Charlson, Boyer, Grober-Buschke,
Hinchey, GOLD — sept instruments nommés dans la cotation, absents du cours.

C'est l'extension la plus rentable de la campagne, elle est arrivée au dernier lot, et
**elle n'a jamais été rejouée sur les cinq lots précédents ni sur les trois autres
corpus.**

### 4.6 Un défaut que seule la lecture croisée pouvait voir

k5e a trouvé, hors de toute mesure, que `HSA avec convulsion`/`theorie` ouvrait par
« (Cf. cas HSA + refus de soins pour théorie complète) » alors que la grille pointée **ne
portait aucun** des trois points annoncés. **Le renvoi désignait une fiche moins complète
que celle qui renvoyait.** Aucune mesure de redondance ne peut voir cela ; il n'apparaît
qu'en lisant les deux jumelles ensemble.

k5f a clos la question par un balayage des renvois sur les 198 grilles : **20 occurrences,
2 renvois inter-grilles, tous deux justes** — celui de k5e étant devenu vrai non par
réécriture mais parce que k5e avait comblé sa cible. **Le corpus ne repose pas sur un réseau
de renvois fragiles.** Un seul défaut subsiste, au § 7.5.

---

## 5. Les erreurs de sécurité et de fond corrigées

Le journal tient un compteur d'erreurs factuelles internes : **il s'arrête à sept**. Les
deux derniers lots n'en ont rencontré aucune. S'y ajoutent les corrections de la passe de
nomenclature, d'une autre nature mais de même gravité.

### 5.1 Le score dont le sens était inversé

**`AMC-Chir2-ECG3`, score de Glasgow-Blatchford.** `expert`/Pièges portait « Score de
Glasgow-Blatchford **> 0 = nécessite endoscopie hospitalière** ». La page SSP est explicite
et chiffrée : « GBS = 0-1 → prise en charge ambulatoire envisageable », « identifie les bas
risques (0-1) ». **Le score sert à identifier les patients qu'on peut renvoyer chez eux ; la
grille en faisait un critère d'hospitalisation.** Corrigé, et le seuil porté dans `theorie`,
qui nommait les scores sans leurs bornes.

### 5.2 Le qualificatif qui désignait les diagnostics à écarter

**`AMC-Chir4-ECG6`, souffle de la sténose aortique.** La grille écrivait « souffle
**HOLOSYSTOLIQUE** 4/6 au 2e EIC droit avec irradiation aux carotides » dans `annexe-dd`,
`expert` et `defi`. Le souffle du rétrécissement aortique est **mésosystolique
éjectionnel** ; « holosystolique » désigne l'insuffisance mitrale, la CIV et l'insuffisance
tricuspide — **c'est-à-dire précisément les diagnostics dont il fallait le distinguer**. Un
étudiant qui apprenait cette grille apprenait à confondre. Corrigé aux trois endroits, tous
hors section notée, et l'auscultation complète portée dans `theorie`, qui n'en disait rien.

### 5.3 L'affirmation absolue là où la nuance existait

**`AMC-Neuro-P3`, syringomyélie.** `expert` qualifiait les troubles trophiques de
« **pathognomonique** » quand `theorie` écrit « **quasi** pathognomonique ». Le retrait de
l'item d'`expert` supprime l'affirmation absolue et laisse la formulation exacte.

### 5.4 Le seuil et le rang manquants

- **`AMC-Chir6-ARC1`** : « fièvre + colique = pyélonéphrite obstructive » **sans seuil**.
  La page SSP est chiffrée — « fièvre > 38,5 °C + frissons ». Seuil porté dans `theorie`.
- **`AMC-Chir1-MedLeg`, cascade des représentants** : `theorie` plaçait le curateur
  (rang 2) **avant** le mandat pour cause d'inaptitude (rang 3). L'art. 378 al. 1 CC met
  les directives anticipées et le mandat au **même chiffre 1**, le curateur au chiffre 2.
  Rangs rétablis, et la référence du curateur portée aux art. 394-396 CC.

### 5.5 Le droit québécois, enseigné à des étudiants suisses

**La correction la plus étendue, et la seule à avoir touché des sections notées.**
L'arbitrage a été rendu par l'utilisateur après k5b : **c'est une erreur factuelle**, au même
titre que la « tutelle » abolie corrigée sur AMBOSS-17. Un étudiant suisse ne doit pas
apprendre une procédure qui n'existe pas chez lui.

Six corrections, sept grilles :

| Grille | Le défaut | La correction |
|---|---|---|
| `AMC-ECOS1-S5` | « garde préventive » et *Loi sur la protection des personnes dont l'état mental présente un danger* — **9 occurrences, dont 3 en section notée** | PAFA art. 426 ss CC ; le canonique reçoit en outre la cascade art. 377-378, l'urgence vitale art. 379 et le recours au tribunal cantonal à 10 jours |
| `AMC-ECOS1-S1` | « Au Québec, à 14 ans et plus, un mineur peut consentir seul » | art. 19c CC — capacité appréciée **au cas par cas et pour chaque décision**, sans âge minimum fixe. « Secondaire 4 » → « 3ᵉ année du gymnase » |
| `AMC-ECOS1-S4` | « vaccins à jour selon le **calendrier québécois** » | « plan de vaccination suisse (OFSP) » |
| `AMC-Chir1-MedLeg`, `HSA et refus de soins` | **`PLAFA`, 11 occurrences** — sigle de l'**ancien** droit (art. 397a ss aCC, abrogé le 1.1.2013), collé au développé et aux articles du **nouveau** | `PAFA` |
| idem | **`APAE`** — inversion de lettres, dont une dans un `criteria-text` | `APEA` |
| `AMC-Psy-P1`, `AMC-Psy-P4` | **la tutelle de l'adulte, abolie en 2013** : « tuteur légal » comme autorité de PAFA — **doublement faux** ; « [tuteur, curateur ou parents] » en section notée | curateur ; APEA (art. 428 CC) ou médecin habilité par le canton (art. 429 CC) ; abolition mentionnée explicitement |

Les cinq grilles dont la zone notée a été touchée n'ont **pas changé de structure** — prouvé
par `check_invariants.py`, vert sur les 198 — et le format `N. Libellé [réponse]` qu'exige
`cases/scoring.js:159` a été préservé sur les deux `criteria-text` concernés.

### 5.6 Les erreurs d'unité et de dose, à la passe de nomenclature

889 occurrences traitées, dont plusieurs qui n'étaient pas de la nomenclature mais de la
sécurité :

- **La formule de Ganzoni.** « déficit en fer (mg) = poids × (Hb normale − Hb patient)
  **(g/dl) × 2,4** ». Convertir l'unité en g/L sans toucher au **coefficient** aurait
  **multiplié la dose de fer par dix**. Écrite désormais `(g/L) × 0,24`. Deux occurrences.
- **Deux seuils écrits mille fois trop grands à la source** : « NT-proBNP > 300 **ng/ml** »
  et « troponines T ultrasensibles > 14 **ng/ml** ». Appliquer la règle de conversion aurait
  donné 300 000 et 14 000 ng/L. Ce sont des **ng/L** : l'unité corrigée, la valeur gardée.
- **Deux CRP en mg/dL** (« CRP 32 mg/dl — modérée ») : 320 mg/L serait massive et
  contredirait le qualificatif, que la même grille chiffre ailleurs « CRP > 40 mg/L ».
- **Une seule valeur changée dans tout le corpus** : `AMC-Chir2-ECG3` portait « hémorragie
  digestive grave (**Hb 7,5 g/L**, choc compensé) » — une magnitude de g/dL sous une unité
  de g/L, contredisant **d'un facteur dix** le seuil transfusionnel « Hb > 70 g/L » énoncé
  trois lignes plus haut **dans la même grille**. Écrit 75 g/L.
- **`Coumadin` → `Sintrom®` (acénocoumarol), et non `Marcoumar®`**, tranché sur la
  chronologie du cas lui-même : la grille écrit « INR revenu à 1,8 après arrêt » et « on
  arrête quelques jours seulement ». L'acénocoumarol a une demi-vie de 8-11 h ; la
  phenprocoumone de 120-160 h, ce qui aurait rendu la grille incohérente avec son propre
  déroulé.
- **Onze numérations de liquides biologiques** — PNN de l'ascite (seuil 250 de la PBS),
  liquide synovial, LBA, LCR, plèvre — rendues en **/µL** et non en G/L : la règle du sang
  ne s'y applique pas.

### 5.7 Onze faux positifs écartés, chacun sur une mesure

La table `BANNED` n'a reçu que des motifs bordés par mesure sur les quatre corpus. Onze
jetons d'apparence anglophone se sont révélés être des homographes français ou suisses, et
les bannir aurait cassé des grilles correctes : **`MI`** (membres inférieurs, 113 occ. — le
corpus écrit `IDM` 108 fois pour l'infarctus), **`PTT`** (36 — la **crase suisse** : les
laboratoires suisses rendent `TP + PTT` là où la France écrit `TP + TCA`), **`IU`** (36,
infection urinaire), **`OAC`** (18 — l'**Ordonnance réglant l'admission à la circulation
routière**, texte fédéral suisse cité par article), **`HIT`** (19 — *Head Impulse Test* du
protocole HINTS), **`EGFR`** (21 — le récepteur en oncologie, pas le DFG), **`IBS`** (16 —
infection bactérienne sérieuse du nourrisson), plus `DAPT`, `NIPT`, `PCC` et `CD4`.

Même prudence sur `MST` : la table de RESCOS n'a **pas** été importée parce qu'elle aurait
signalé **« Morphine PO (Sevredol® 10 mg q4h, MST Continus®) »** — un nom de spécialité.
**Bannir ce sigle aurait corrompu une prescription.**

---

## 6. Les moteurs de barème

**C'est le défaut technique le plus étendu jamais trouvé dans le projet : il portait sur les
198 grilles, il était préexistant, et il plantait à chaque clic.**

### 6.1 Ce que les 198 grilles portaient

Aucune des 198 ne chargeait `cases/scoring.js`. Chacune embarquait sa **propre copie
complète** du moteur — ~726 lignes de JavaScript — où `maxScores`, `coef` et `sectionInfo`
étaient des variables locales au corps de `calculateScores()`.

Trois mesures ont établi que ces 198 copies étaient une seule et même fourche périmée :

1. **Une seule empreinte.** Les 198 blocs, **une fois leur configuration retirée**, rendent
   une **unique empreinte SHA-1**. Le texte restant est identique **caractère pour
   caractère** sur les 198.
2. **Ce moteur est `scoring.js` moins six ajouts.** `diff -u` du moteur canonicalisé contre
   le fichier partagé : 205 lignes ajoutées, 6 remplacées, **aucune supprimée**.
3. **Une seule forme de configuration** : quatre sections, `scoreId` sur `examen`, `isComm`
   sur `communication`, sur les 198.

### 6.2 La `TypeError`, et pourquoi le diagnostic statique l'a manquée

Le lot K1 avait conclu, par analyse statique : « **Aucune ne peut lever de `TypeError`**,
contrairement à RESCOS-7 et RESCOS-9. Les neuf identifiants déréférencés sans garde sont
présents dans les 198. »

**Le banc d'essai en navigateur dit le contraire : les 198 grilles levaient**

```
TypeError: Cannot read properties of null (reading 'style')
    at calculateScores
```

**à chaque recalcul — 341 à 503 fois par session de remplissage complet.**

La cause, et c'est elle qui a piégé le diagnostic statique : `#missingItems` et
`#missingList` n'existent que **dans un commentaire HTML**.

```html
<!-- ÉLÉMENTS MANQUANTS (MASQUÉS) -->
<!-- <div class="missing-items" id="missingItems" style="display: none;"> … </div> -->
```

198 grilles sur 198. Le contrôle `engine_defects()` cherchait `id="missingItems"` dans le
**HTML brut** : il le trouvait dans le commentaire, concluait « présent », et rendait la
porte **verte**. **Le navigateur, lui, ne construit pas les commentaires.**

> **La leçon vaut au-delà de ce corpus** : un contrôle qui interroge le texte du fichier
> répond sur le fichier, pas sur le document que le navigateur construit. Un identifiant
> commenté est, pour une recherche de chaîne, indiscernable d'un identifiant vivant. Il a
> fallu un banc d'essai réel pour trancher.

Conséquence en cascade, mesurée : la `TypeError` interrompait le gestionnaire
`DOMContentLoaded` **avant** `colorPatientResponses()`. Sur les 198, la coloration des
crochets ne devait son existence qu'à un rappel de secours placé en fin de page.

### 6.3 Le second défaut : aucune des 198 ne remontait son score

La copie embarquée ne connaissait pas `saveToRegistry()`. **Les 198 stations ne remontaient
jamais leur score au tableau de bord** — mesuré : `ecos_registry` renseigné sur **0 / 198**.

Ce n'était pas un état souhaitable mais un **défaut constaté**, et le champ gelé
`savesToRegistry` le figeait à `false` sur les 198 pour garantir que sa correction serait
un changement **vu et voulu**, et non un effet de bord. Le champ **mentait des deux côtés** :
sa première rédaction cherchait la chaîne `saveToRegistry` dans le HTML, donc elle aurait
rendu `false` **après** la bascule aussi, la fonction vivant désormais dans un fichier
séparé. Le champ existait pour voir un seul changement et l'aurait manqué. Il vaut
désormais `true` si la grille porte la fonction **ou** charge le moteur qui la porte.

### 6.4 La migration

`scripts/casecos/migrate_to_shared_engine.py` — huit assertions par grille, une seule qui
tombe et la grille reste intacte. **Zéro refus sur 198.** Chaque grille déclare désormais un
`window.caseConfig` puis charge `<script src="../scoring.js">`, et `persistence.js` avant
`</body>`.

Deux blocs `<script>` ont été **supprimés**, et ce ne sont pas des pertes : le rappel de
`colorPatientResponses()` est la **queue exacte** de `scoring.js` (le garder l'aurait fait
jouer deux fois), et la barre de navigation locale est le substitut de `createNavBar()`, que
`scoring.js` appelle désormais (la garder aurait affiché **deux barres superposées**).

**Aucun octet de contenu n'a bougé.** Preuve directe sur les 198 : le fichier **privé de ses
blocs `<script>`**, comparé à sa version `d0a89f4` privée des siens, ne diffère que par
`'\n    ' → '\n'` — l'indentation qui précédait le bloc supprimé. Rien d'autre.

### 6.5 Le résultat, mesuré en navigateur des deux côtés

Chrome sans interface piloté par le protocole DevTools, aucun paquet installé, contexte de
navigation isolé par grille, navigation **par les URL d'`index.html` et jamais par le
disque** — parce que macOS stocke les noms accentués en NFD et qu'`index.html` les porte
en NFC : une énumération du système de fichiers aurait mesuré un chemin que l'utilisateur
n'emprunte pas.

| | avant (`d0a89f4`) | après |
|---|---|---|
| **sans exception ni erreur de console** | **0** | **198** |
| **`ecos_registry` renseigné** | **0** | **198** |
| dont `pct: 100, grade: "A"` | 0 | **198** |
| clé du registre = `fileKey` d'`index.html` | — | **198 / 198** |
| réponses restituées après rechargement | 0 | **198** |
| `persistence.js` chargé · `srs.js` chargé | 0 · 0 | **198 · 198** |
| total = 100 % · note = A | 198 · 198 | **198 · 198** |
| grilles dont le total ou la note diffère | — | **0** |

`ecos_registry` n'est écrit qu'à **un seul endroit du dépôt**, `cases/scoring.js`, dans
`saveToRegistry()`. L'apparition des 198 entrées ne peut venir que du chargement du moteur
partagé.

### 6.6 Le trou d'outillage a été fermé

`check_reachability.live_dom()` neutralise désormais les commentaires HTML avant toute
recherche d'identifiant. **Contrôle de morsure** : le contrôle corrigé, appliqué au miroir de
`d0a89f4`, rend **198/198 en échec** et nomme exactement les deux identifiants que le
navigateur signalait. Trois autres contrôles de morsure ont été passés sur les portes
(`maxScores` altéré, `count` altéré, moteur ré-embarqué) : **les quatre mordent**.

`engineHash` vaut désormais `"shared:scoring.js"` et garde la charge de signaler toute
grille qui ré-embarquerait un moteur — c'est `git diff` qui couvre le moteur partagé.

---

## 7. Ce qui reste ouvert

Rien de ce qui suit n'est réglé, et rien n'est mineur au point d'être passé sous silence.

### 7.1 L'instrument `theorie ↔ therapy` n'a jamais été construit

**Six lots successifs l'ont demandé** — k4, k5a, k5b, k5c, k5d, k5e — et k5f le redemande
une septième fois. Il n'existe toujours pas.

C'est **le premier poste de redondance du corpus** : **137 des 417 paires**, soit 33 %. Et
c'est **le seul couple qui n'ait jamais eu d'instrument propre**. Les 34 paires du dernier
lot n'ont jamais été entamées.

Le chiffre de 137 est un **plancher très bas** : la mesure d'inclusion établit qu'environ
**neuf recouvrements sur dix y sont invisibles au seuil** (§ 4.1). Le vrai gisement se
compte probablement en centaines.

Il y a une raison de fond à ne pas simplement dédoublonner ce couple — **le barème et le
cours *doivent* se recouvrir** : ce qui est coté doit être enseigné. Mais cette raison
justifie de **ne pas supprimer**, pas de **ne pas mesurer**. Il faut un instrument qui
distingue le recouvrement légitime de la recopie, et il faut qu'il soit **publié à part**,
sans jamais toucher au seuil de 0,72.

### 7.2 Quatre grilles n'ont aucune page SSP

`AMC-MCPR-ARC21` (bilan préopératoire, trouvé à k5c), `AMC-Psy-P12` (TDAH de l'adulte),
`AMC-Psy-P2` (trouble paraphilique), `AMC-Psy-P4` (autisme de l'adulte) — les trois
derniers trouvés à k5e.

**Vérifié** : les quatre figurent dans `docs/obsidian-mapping.yaml`, non pas rattachées à
une page mais dans la liste des exclusions, avec pour raison « *page manquante* ». Ce ne
sont donc pas des oublis de mapping mais **des pages du vault qui n'existent pas**. Sur ces
quatre grilles, la hiérarchie à trois niveaux n'a jamais pu descendre au niveau 1 : rien ne
peut trancher une divergence.

k5f est le seul lot couvert à 26/26.

### 7.3 Deux associations françaises proposées à des patients suisses

**Vérifié à la mesure, blocs et hors-blocs :**

| Grille | Terme | Où |
|---|---|---|
| `AMC-Neuro-P4` (myasthénie) | **AFM** — Association Française contre les Myopathies | **1 occurrence, hors des blocs de contenu** — dans un `criteria-detail`, donc en **section notée** |
| `AMC-Psy-S4` (démence) | **France Alzheimer** | **2 occurrences — 1 dans `theorie`**, 1 hors des blocs |

Équivalents suisses existants : **ASRIMM** (Suisse romande) et **Muskelgesellschaft** pour
la première ; **Alzheimer Suisse / Alzheimer Schweiz** et ses antennes cantonales pour la
seconde.

**Non corrigées, et pour une raison cohérente** : k5c a tranché que le choix d'une ressource
associative est **éditorial, pas factuel** — à la différence du droit, qui est factuel. Rien
ne justifiait de traiter France Alzheimer autrement que l'AFM au seul motif qu'elle se
trouve, elle, dans un bloc éditable. **Les deux arbitrages sont à rendre ensemble.**

Deux autres cas de la même famille sont consignés hors du corpus des blocs : **AFDIAG**
(`UIDC-Lea`) et **France Lynch** (`UIDC-Monsieur Dupont`).

### 7.4 Trois grilles doublons obsolètes, toujours référencées

`AMC-ECOSDiag1` (spondyloarthrite axiale), `AMC-ECOSDiag2` (ulcère perforé),
`AMC-ECOSDiag3` (anémie ferriprive sur AINS).

**Vérifié** : les trois fichiers existent dans `cases/casecos/` et **`index.html` porte trois
références `ECOSDiag`**. Elles sont donc atteignables depuis le tableau de bord.

Les trois **ne portent aucun bloc de contenu** — elles sont sorties intactes du lot k5e pour
cette raison, et ne pouvaient être ni dédoublonnées ni enrichies. L'arbitrage est ouvert
depuis k1 et n'a jamais été rendu : **les supprimer, ou les retirer d'`index.html`, ou les
compléter.** En l'état, un étudiant peut ouvrir une station vide de tout support de
révision, dont le contenu existe ailleurs dans le corpus.

### 7.5 Un renvoi intra-grille pendant

**`Céphalées - Homme 30 ans`**, bloc `scenario` : « exiger fermement une IRM aujourd'hui en
évoquant la peur d'une tumeur cérébrale **(cf. cl2)** ».

**Vérifié : « cl2 » ne désigne rien.** Une seule occurrence de la chaîne dans tout le texte
visible de la grille — le renvoi lui-même. Aucune section « CL », aucun critère « CL2 »,
aucune grille du corpus ainsi nommée. Le seul référent plausible est **Management 2**
(« Examens complémentaires — approche Smarter Medicine »), qui traite bien l'exigence d'IRM
du défi.

**Consigné et non corrigé** : l'intention de l'auteur ne se déduit pas d'un code employé
deux fois dans 198 grilles, et deviner serait pire que signaler. C'est **le seul défaut de
renvoi du corpus**, sur 20 occurrences balayées.

### 7.6 Sept quasi-doublons `expert ↔ theorie` à écart de synonyme

Ils ne se résolvent pas sans une normalisation des sigles — `AEG` contre « altération de
l'état général », `EWGSOP` contre `EWGSOP2` — et sans le traitement de la ligature du § 7.7.

### 7.7 Le défaut de la ligature `œ` dans `norm()`

**Vérifié, et le chiffre est confirmé exactement.**

`scripts/amboss/lib_amboss.py:124` — la fonction `norm()`, **partagée par les quatre
corpus** (`lib_casecos.py:130`, `lib_rescos.py:113` font `norm = _base.norm`) — normalise en
NFD, retire les caractères de catégorie `Mn`, puis remplace tout ce qui n'est pas
`[a-z0-9 ]` par une espace. Le caractère `œ` (U+0153) traverse la normalisation intact et
tombe dans le dernier filtre :

| Entrée | `norm()` rend |
|---|---|
| `œdème` | `'deme'` |
| `cœur` | `'c ur'` |
| `manœuvre` | `'man uvre'` |
| `sœur` | `'s ur'` |
| `Œstrogènes` | `'strogenes'` |

**Ampleur, mesurée sur les quatre corpus :**

| Corpus | Grilles | Grilles touchées | Occurrences (texte visible) |
|---|---|---|---|
| AMBOSS | 40 | 36 | 349 |
| german | 88 | 74 | 788 |
| RESCOS | 41 | 27 | 203 |
| CasECOS | 198 | 167 | 1 688 |
| **Total** | **367** | **304** | **3 028** |

**Le chiffre annoncé de 3 028 sur 304 des 367 grilles est exact**, à condition de compter sur
le **texte visible** — celui que `norm()` consomme réellement. Sur le fichier brut, `<script>`
et `<style>` compris, le total est de **3 069**.

#### Deux redressements, que la mesure impose

**1. La cause n'est pas un défaut de décomposition NFKD.** L'explication couramment donnée —
« faute de décomposition NFKD » — est fausse, et vérifiable en une ligne :

```
unicodedata.decomposition('œ')  →  ''          (aucune décomposition)
unicodedata.normalize('NFKD', 'œ')  →  'œ'     (inchangé)
unicodedata.normalize('NFKD', 'ﬁ')  →  'fi'    (celle-là se décompose)
```

**U+0153 n'a aucune décomposition, ni canonique ni de compatibilité.** Unicode la traite
comme une **lettre** de l'alphabet latin étendu — ce qu'elle est en français — et non comme
une ligature typographique à la manière de `ﬁ` (U+FB01, `<compat> 0066 0069`). Même chose
pour `æ` (U+00E6). **Passer `norm()` de NFD à NFKD ne corrigerait rien.**

Le correctif tient toujours en une ligne, mais ce n'est pas celle-là : une **table de
translittération** appliquée avant la normalisation.

```python
LIGATURES = {0x153: "oe", 0x152: "OE", 0xe6: "ae", 0xc6: "AE"}
s = s.translate(LIGATURES)   # avant le unicodedata.normalize("NFD", …)
```

**2. Le correctif ne déplacerait pas les compteurs du projet.** C'est l'affirmation qu'il
fallait vérifier plutôt que reprendre, et **la mesure la contredit**. Le correctif ci-dessus
a été appliqué **en mémoire**, par substitution de fonction, sans modifier aucun fichier du
dépôt, puis les trois corpus outillés ont été remesurés :

| Corpus | Inter-blocs actuel | Inter-blocs corrigé | Intra actuel | Intra corrigé |
|---|---|---|---|---|
| **AMBOSS (témoin gelé)** | **147** | **147** | — | — |
| **RESCOS (témoin gelé)** | **127** | **127** | 209 | **208** |
| **CasECOS** | **417** | **417** | 719 | **714** |

**Aucun des trois chiffres publiés ne bouge.** Le correctif **mord** pourtant : sur AMBOSS
seul, **454 des 7 613 items extraits changent de texte**. Sur CasECOS, deux paires
s'échangent — une apparaît dans une tranche, une disparaît dans une autre — pour un solde
**exactement nul**. Seules les mesures **intra-bloc**, qui ne sont pas des chiffres de
référence du projet, se déplacent de −1 et −5.

L'explication est celle qui était déjà pressentie : **la mutilation est déterministe et
symétrique.** Les deux côtés d'une comparaison la subissent identiquement, `œdème` devient
`deme` des deux côtés, et le rapport de `SequenceMatcher` survit. Elle ne crée donc **aucun
faux appariement**.

**Ce qui reste vrai, et ce qui ne l'est pas.**

- **Vrai** : l'effet de la mutilation est d'**abaisser** la similarité mesurée, en scindant
  un mot en deux jetons dont l'un peut passer sous les seuils de longueur. **Le plancher de
  mesure est donc plus mou qu'annoncé** — de combien, on ne le sait pas, et c'est un
  cinquième angle mort à ajouter à ceux du § 4.4.
- **Vrai** : c'est un **défaut réel** de `lib_amboss.norm`, partagé par les quatre corpus,
  et il faut le corriger.
- **Faux** : que ce soit un arbitrage éditorial parce qu'il « déplacerait tous les
  compteurs, témoins gelés compris ». **Mesuré : il n'en déplace aucun.** Le seul obstacle
  qui subsiste est que le corpus german n'a pas été remesuré — l'utilisateur y travaillait
  en parallèle — et qu'un correctif touchant un fichier partagé par les quatre corpus ne se
  passe pas sans avoir mesuré les quatre.

**Recommandation :** rejouer cette mesure sur german quand son chantier sera clos, puis
appliquer le correctif. Si german se comporte comme les trois autres, il n'y a pas
d'arbitrage à rendre, seulement un défaut à corriger.

### 7.8 Les arbitrages hérités de k1, toujours ouverts

- **`numeration-implicite`** : 11 occurrences sur 7 grilles.
- **Le nom de fichier `… Surdosage de Coumadin …`** et son libellé dans `index.html`. Le
  `<title>` et le `<h1>` disent « Surdosage de Sintrom® » depuis la passe de nomenclature ;
  **le nom de fichier et le tableau de bord disent toujours Coumadin.** Renommer le fichier
  sort de `cases/casecos/`.
- **Le bug d'équilibrage latent de `lib_german` et `lib_rescos`** — le chevron nu, corrigé
  dans `lib_casecos` seul. Son bon point de chute est un module partagé
  `scripts/lib_grilles.py` qui n'existe pas.
- **Contradictions internes de sigles** non traitées : `HBV` 15 / `HCV` 42 contre `VHB` 50 /
  `VHC` 22 (l'une est dans un **nom de fichier**) ; `SCLC` 16 / `NSCLC` 14 contre `CBPC` 5 /
  `CBNPC` 7, **dans la même grille** ; `AOD` 62 et `ACOD` 15, deux formes françaises
  correctes.
- **Le style d'`expert`/Points clés**, ouvert depuis k5a : seules les paires *mesurées* ont
  été traitées. Le reste des Points clés déclaratifs — largement majoritaire — n'a pas été
  touché. C'est une question de style éditorial à trancher **pour le corpus entier**, pas
  grille par grille.
- **Les sous-titres de `theorie` portés par des `<li>`**, qui fabriquent des paires vides de
  contenu (§ 4.3). Les passer en `<h5>` déplacerait les chiffres publiés.

---

## 8. Clôture d'ensemble des quatre corpus

**Décompte fait à la mesure, en énumérant les grilles par la fonction `grids()` de chaque
bibliothèque :**

| Corpus | Grilles | Redondance inter-blocs | Portes |
|---|---|---|---|
| **AMBOSS** | **40** | **147** | invariants, nomenclature, atteignabilité — rc 0 |
| **german** | **88** | (chantier en cours, non mesuré) | — |
| **RESCOS** | **41** | **127** | invariants, nomenclature, atteignabilité — rc 0 |
| **CasECOS** | **198** | **417** | invariants, nomenclature, atteignabilité — rc 0 |
| **Total** | **367** | | |

**367 grilles.** CasECOS en représente **54 %** à lui seul — plus que les trois autres
corpus réunis.

### Ce que la série des quatre a établi

**Chaque corpus a apporté un défaut de barème d'une espèce nouvelle**, et aucun des
vérificateurs hérités ne pouvait voir le suivant :

| Corpus | L'espèce | Ce qu'elle produisait |
|---|---|---|
| AMBOSS-9 | plus de points **déclarés** qu'il n'en existe | station plafonnée à 98 %, non corrigée (barème gelé) |
| German | aucun | 880 champs recalculés, zéro divergence |
| RESCOS-12/13 | une section **vide** qui garde son quart de coefficient | copie parfaite plafonnée à **75 %, note C** |
| **CasECOS** | **198 copies périmées d'un moteur qui plante** | **`TypeError` à chaque clic, aucun score remonté au tableau de bord** |

Le défaut CasECOS est le plus étendu des quatre, et **le seul qu'un diagnostic statique ait
explicitement déclaré absent avant qu'un banc d'essai ne le trouve** (§ 6.2).

**Et la campagne CasECOS a établi une chose sur l'outillage lui-même** que les trois
précédentes n'avaient pas vue : **la mesure de similarité est un filet à grosses mailles.**
Elle décroche silencieusement dès que les deux blocs comparés n'ont pas le même grain, elle
est structurellement aveugle à l'inclusion — le pire doublon possible — et **elle n'a trouvé
aucun** des 97 trous du canonique. Ceux-ci l'ont été par le relevé d'éponymes, par l'usage
inversé, et — au tout dernier lot — par l'extension de ce relevé aux `criteria-detail`.

**Cette extension n'a jamais été rejouée sur les cinq premiers lots de CasECOS, ni sur
AMBOSS, ni sur German, ni sur RESCOS.** C'est le travail le plus rentable qui reste à faire
sur l'ensemble du projet.

---

## Annexe — comment reproduire les vérifications

```bash
python3 scripts/casecos/check_invariants.py       # OK — 198 grilles, code 0
python3 scripts/casecos/check_nomenclature.py     # OK — aucun terme non suisse, code 0
python3 scripts/casecos/check_reachability.py     # OK — 198/198 à 100 %, code 0
python3 scripts/casecos/check_no_loss.py d0a89f4  # rapport, code 0 en toutes circonstances

python3 scripts/amboss/report_redundancy.py       # TOTAL : 147 paire(s) — témoin
python3 scripts/rescos/report_redundancy.py       # TOTAL : 127 paire(s) — témoin
```

Les trois premiers sont des **portes** : ils sortent en erreur si un écart apparaît.
`check_no_loss.py` est un **rapport** et sort toujours 0 — **ne jamais le câbler comme porte
bloquante**, ce serait bloquer le projet sur des suppressions parfaitement légitimes.

**La redondance CasECOS ne se mesure pas en une passe** — 198 grilles en O(n×m) dépassent
120 s. Elle se découpe par index de grille, et le découpage est **exact** puisque aucune
paire ne franchit la frontière d'une grille :

```bash
python3 - <<'EOF'
import sys; from pathlib import Path
sys.path.insert(0, "scripts/casecos")
import lib_casecos as lib
from report_redundancy import pairs_for
DEBUT, FIN = 0, 20           # une tranche ; dix tranches couvrent les 198
n = sum(len([p for p in pairs_for(g, intra=True) if p[1] != p[3]])
        for g in list(lib.grids())[DEBUT:FIN])
print(n)
EOF
```

Somme des dix tranches : **417** paires inter-blocs, **719** intra-bloc.

**Le défaut de la ligature du § 7.7 se retrouve en trois lignes**, et son innocuité se
vérifie en substituant `norm()` en mémoire, sans modifier aucun fichier :

```bash
python3 -c "
import sys; sys.path.insert(0, 'scripts/amboss'); import lib_amboss as la
for m in ('œdème', 'cœur', 'manœuvre'): print(m, '->', repr(la.norm(m)))
"
# œdème -> 'deme'   cœur -> 'c ur'   manœuvre -> 'man uvre'
```

L'intégrité structurelle, la comparaison du barème avec `d0a89f4` et le contrôle fonctionnel
en navigateur sont menés par des scripts d'audit ponctuels, non versionnés — pilotage direct
de Chrome par le protocole DevTools pour le dernier.
