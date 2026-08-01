# Refonte pédagogique des 40 grilles ECOS AMBOSS — rapport de vérification finale

Branche `refonte-amboss-suisse` · 30 commits depuis `main` · état vérifié : `30e3682`
Référence d'origine (avant toute modification de contenu) : `a845c1b`
Journal détaillé : `docs/superpowers/journal-amboss-2026-07.md`

---

## 0. Résultat des vérifications

Six vérifications ont été menées sur l'ensemble du corpus. **Cinq passent. Une échoue,
sur un défaut préexistant que le projet n'a ni introduit ni pu corriger.**

| # | Vérification | Résultat |
|---|---|---|
| 1 | Invariants et nomenclature | **OK** — `check_invariants.py` : 40 grilles, code 0 · `check_nomenclature.py` : aucun terme non suisse, code 0 |
| 2 | Barème inchangé depuis `a845c1b` | **OK** — 240 champs recalculés sur les 40 grilles, zéro divergence |
| 3 | Intégrité structurelle | **OK** — 40/40 fichiers, balises équilibrées, blocs attendus présents |
| 4 | Redondance | **OK avec une réserve** — 301 → 66 paires ; 65 justifiées, 1 résiduelle (AMBOSS-13) |
| 5 | Non-perte d'information | **OK** — 684 items signalés, aucune perte réelle retrouvée sur les thèmes sensibles |
| 6 | Contrôle fonctionnel | **ÉCHEC sur 1 grille / 40** — AMBOSS-9 |

### Le défaut

**AMBOSS-9 (« Douleurs dorsales — homme 71 ans ») : le barème de l'anamnèse est
inatteignable. Le candidat plafonne à 49 points sur les 53 affichés.**

La configuration de la grille déclare treize critères d'anamnèse (`count: 13`) et un
maximum de 53 points. Le critère `a13` n'existe nulle part dans la page : il n'a ni
libellé, ni case, ni bouton. Les douze critères réellement présents totalisent 49 points.
Conséquence à l'écran : la section affiche « Score : 49/53 » même lorsque **tout** est
coché, et le score global de la station plafonne à 98 %.

Vérifié de deux façons indépendantes : par recalcul statique du DOM sur les 40 grilles
(seule anomalie du corpus) et par ouverture réelle de la page dans un navigateur, où le
remplissage complet de la grille s'arrête effectivement à 98 %.

**Ce défaut est préexistant** : il est présent à l'identique dans la toute première
version du fichier dans git (`9f4ab18`), dans `a845c1b`, et aujourd'hui. Il n'a pas été
introduit par la refonte. Il n'a pas non plus pu être corrigé : il vit dans la
configuration de notation, gelée par consigne. **Le corriger demande une décision : soit
ramener `maxScores.anamnese` à 49 et `count` à 12, soit écrire le treizième critère
manquant.** Les deux touchent au barème.

Les 39 autres grilles atteignent exactement 100 % lorsqu'elles sont remplies
intégralement, minuteur, coloration et affichage compris.

---

## 1. Ce qui a été fait

Les 40 grilles ont été relues une par une, avec pour chacune la page de référence
correspondante du vault SSP. Le travail a porté sur la **zone pédagogique** — les blocs
`resume`, `expert`, `theorie`, `presentation` — jamais sur les sections notées, à une
exception près décrite plus bas.

### Chiffres

| Mesure | Avant | Après |
|---|---|---|
| Paires d'items quasi identiques entre blocs | **301** | **66** (−78 %) |
| Termes non suisses détectés | **103** | **0** |
| Valeurs de laboratoire en unité non SI ou implicite | **36** | **0** |
| Mentions d'unités impériales (livres, onces, pouces, °F) | **11** | **0** |
| Grilles dont un bloc pédagogique a été modifié | — | **40 / 40** |

Volume : 1 170 lignes ajoutées, 1 932 supprimées dans `cases/`.

Répartition du corpus : **25 grilles complètes** (quatre blocs pédagogiques) et
**15 grilles allégées** (`expert` + `theorie` seuls — aucun bloc n'a été créé ni supprimé).

### Ce que cela change pour qui révise

**La même information n'est plus répétée sous quatre formes.** Chaque bloc a désormais un
rôle exclusif : `expert` fait tourner la station (ce que l'examinateur délivre et observe),
`theorie` explique le *pourquoi* (seuils, sensibilité, physiopathologie), `resume` est la
check-list canonique de révision, `presentation` est la restitution orale. Une information
ne réapparaît que si elle **change de format** — liste → narration, liste → SBAR,
liste → question d'examinateur. Réviser sur le `resume` suffit désormais à couvrir la
station ; les autres blocs apportent autre chose plutôt que la même chose.

**Les 66 paires qui subsistent sont ce changement de format.** 56 opposent le `resume`
(liste) à la `presentation` (restitution parlée ou clé de mnémo), 3 la `theorie` à la
`presentation`, 3 l'`expert` à la `presentation`, et 4 le `resume` à l'`expert` — ces
dernières opposant l'item générique de révision au résultat chiffré effectivement délivré
au candidat (« test de grossesse positif » face à « hCG positif à 2 500 UI/L »). **Aucune
paire `expert` ↔ `theorie` ne subsiste**, ce qui était le marqueur d'un dédoublonnage
incomplet.

**Une seule paire n'est justifiable par aucun changement de format** : AMBOSS-13, sur le
seuil de drainage du pneumothorax traumatique. Voir § 3.

**Les valeurs de laboratoire se lisent en unités suisses.** Hémoglobine en g/L, troponine
en ng/L, D-dimères en µg/L, numérations en G/L, créatinine en µmol/L. Les conversions ont
été faites analyte par analyte, jamais mécaniquement : chaque famille a son facteur propre,
et les intervalles de référence ont été convertis en même temps que les valeurs.

**Le vocabulaire est suisse.** FSC et non NFS, 144 et non 911 ou SAMU, Dafalgan® et non
Tylenol, Tramal® et non Vicodin, Sintrom®/Marcoumar® et non warfarine, curatelle APEA/KESB
et non tutelle (abolie en Suisse depuis 2013).

**Le barème n'a pas bougé.** Les scores maximaux, les dénominateurs affichés, le nombre de
critères, de sous-items, de boutons et de cases sont identiques à ce qu'ils étaient avant
le projet, sur les 40 grilles — vérifié champ par champ contre `a845c1b`.

---

## 2. Les erreurs de sécurité trouvées

Le journal recense une cinquantaine de signalements. **Toutes ces erreurs sont
préexistantes** : elles étaient dans les grilles avant le projet. Elles sont regroupées ici
par nature, et séparées selon qu'elles ont pu être **corrigées** (elles vivaient dans un
bloc pédagogique) ou seulement **consignées** (elles vivent dans une section notée, gelée).

### A. Drapeau rouge absent — le diagnostic à ne pas manquer n'était nulle part

C'est la catégorie la plus lourde. Il ne s'agit pas d'un drapeau rouge mal formulé, mais
d'une **absence totale** : aucune occurrence du terme dans l'ensemble du fichier, alors que
la page SSP correspondante en fait sa règle d'or ou son piège éliminatoire n° 1.

**Corrigées** (dans le pédagogique) :

- **AMBOSS-34** (perte de vision, homme 66 ans) — **aucune** occurrence de Horton, artérite
  temporale, VS, CRP, OACR, fond d'œil ni DPAR. Omission complète du diagnostic dont
  l'urgence conditionne la vue de l'œil controlatéral.
- **AMBOSS-9** (lombalgie, homme 71 ans, 40 paquets-années, diabétique) — anévrisme de
  l'aorte abdominale absent de toute la grille, différentiel de la section notée compris,
  chez un patient qui en réunit le portrait exact.
- **AMBOSS-10** (lombalgie) — ni « queue de cheval », ni « sphinct- », ni « anesthésie en
  selle ». La section notée dépiste le syndrome sous des libellés génériques (« Problèmes
  urinaires », « Engourdissement ») sans qu'aucun bloc n'en donne la raison.
- **AMBOSS-25** (genou chaud, gonflé, 37,8 °C) — ni « septique », ni « ponction ».
- **AMBOSS-40** (vertige aigu) — ni HINTS, ni skew, ni AVC, ni cérébelleux, alors que
  l'`expert` délivre un head thrust positif sans que rien n'explique ce qu'un résultat
  **normal** aurait imposé.
- **AMBOSS-39** (épaule **gauche**, homme 52 ans) — aucun ECG ni troponine dans le bloc
  canonique, ni aucun examen du rachis cervical.
- **AMBOSS-16** (troubles du sommeil) — risque suicidaire jamais évalué, alors que la
  patiente **présente** le réveil précoce et que la page SSP prescrit explicitement de le
  rechercher devant ce signe.
- **AMBOSS-17** (troubles de mémoire) — la section notée déroule un syndrome dépressif
  complet, et la pseudo-démence dépressive n'était mentionnée nulle part.
- **AMBOSS-32** (lésion génitale, patiente de **17 ans**, 8 partenaires, aucune protection)
  — aucun dépistage d'abus. Corrigé avec la filière LAVI / CURML / 147 et le fondement de
  l'art. 16 CC.
- **AMBOSS-29** et **AMBOSS-6** — β-hCG absent ou restreint à « si suspicion de grossesse »
  chez des femmes en âge de procréer avec douleur abdominale ou pelvienne.
- **AMBOSS-37** (ictère néonatal) — fenêtre de la hépatoportoentérostomie de Kasai (60 jours)
  absente.
- **AMBOSS-33** (méningite, 38,7 °C, Kernig et Brudzinski positifs) — la grille poussait
  vers un CT immédiat puis une PL sans jamais dire que l'antibiothérapie ne s'ordonne pas
  dans cette file d'attente.
- **AMBOSS-38** — ni thromboprophylaxie, ni rupture du tendon d'Achille évoquées.

**Consignée** : la section notée d'**AMBOSS-34** omet elle aussi Horton et l'OACR de son
différentiel. Le pédagogique a été complété ; la section notée reste en l'état.

### B. Dose ou plafond manquant

**Corrigées** :

- **AMBOSS-7** (fillette de 2 ans) — paracétamol 15 mg/kg toutes les 4-6 h **sans plafond
  journalier** : 90 mg/kg/j atteignables contre 60 autorisés.
- **AMBOSS-30** (patient de 19 ans) — même défaut, même molécule, même facteur.
- **AMBOSS-11** — paracétamol 4 g/j sans plafond chez un **buveur quotidien**, alors que
  l'alternative antalgique figurait dans la même grille.
- **AMBOSS-30** — azithromycine à **12 mg/kg/j**, dose pédiatrique, dans une grille adulte,
  contredisant la dose adulte donnée dans le même bloc.
- **AMBOSS-21** — bloc thérapeutique **entièrement pédiatrique** sur un patient de 23 ans,
  dont un critère littéralement inapplicable (« TA > 95e percentile » : il n'y a pas de
  percentile chez l'adulte), furosémide en mg/kg, pénicilline V à la dose de l'enfant.
- **AMBOSS-9** — gabapentine à pleine dose d'emblée chez un sujet âgé, sans titration ni
  adaptation rénale.
- **AMBOSS-6** — agonistes de la GnRH sans durée maximale de 6 mois (déminéralisation) ni
  traitement add-back.
- **AMBOSS-28** — lévothyroxine à pleine dose sans réserve d'âge ni cardiaque.

### C. Contre-indication absente

**Corrigées** :

- **AMBOSS-5** — hyperémèse gravidique traitée par apport glucosé **sans thiamine
  préalable** : risque d'encéphalopathie de Gayet-Wernicke. Thiamine 100 mg IM/IV ajoutée.
- **AMBOSS-31** — pyridoxine absente du schéma RIPE alors que la section notée l'exige.
  Isoniazide sans vitamine B6 = neuropathie périphérique.
- **AMBOSS-26** — sumatriptan délivré puis prescrit sans **aucune** contre-indication
  mentionnée nulle part, chez un fumeur à 28 paquets-années.
- **AMBOSS-7** — AINS proposé à une enfant déshydratée sans contre-indication ; le syndrome
  de Reye et l'interdit de l'aspirine étaient absents de toute la grille pédiatrique.
- **AMBOSS-9** — contre-indication du paracétamol présentée comme « diabétique » au lieu
  d'hépatique.
- **AMBOSS-37** — contre-indication de la photothérapie sur bilirubine **conjuguée** absente
  de toute la grille.

**Consignée — le doute clinique le plus important du projet** :

- **AMBOSS-14** — la grille prescrit un bêtabloquant « si pas de contre-indication »
  (métoprolol 25-50 mg × 2/j) alors que le mécanisme retenu est un **spasme coronaire induit
  par les amphétamines**, situation où le bêtabloquant est classiquement déconseillé (effet
  alpha non opposé). La page SSP ne liste que « insuffisance cardiaque, bradycardie,
  hypotension » comme contre-indications et la section notée n'a aucun critère de prise en
  charge : rien ne tranchait, rien n'a été inventé. **Point à arbitrer.**

### D. Molécule inadaptée au terrain ou indisponible en Suisse

**Corrigées** :

- **AMBOSS-11** — trithérapie d'éradication à l'**amoxicilline** dans le bloc canonique
  d'un patient dont l'**allergie à la pénicilline** est un sous-item noté de la même grille.
  L'incohérence n'était visible qu'en lisant les deux zones ensemble.
- **AMBOSS-11** — **ranitidine** encore proposée en alternative aux IPP, alors qu'elle a été
  retirée du marché mondial en 2020. Remplacée par la famotidine.
- **AMBOSS-9** — **cyclobenzaprine** prescrite à un homme de 71 ans : non commercialisée en
  Suisse et fortement anticholinergique, donc inappropriée après 65 ans. La page SSP **et**
  le critère noté nommaient tous deux la tizanidine.
- **AMBOSS-30** — amoxicilline en première intention alors que la mononucléose est le
  différentiel principal et la rate palpable (éruption chez ~90 %).
- **AMBOSS-36** — **diazépam** prescrit pour le sevrage d'un patient en hépatite alcoolique.
  Remplacé par oxazépam / lorazépam.
- **AMBOSS-6** — élagolix, antagoniste de la GnRH non enregistré en Suisse.
- **AMBOSS-25** — warfarine, non commercialisée en Suisse → Sintrom® / Marcoumar®.
- **AMBOSS-17** — **tutelle** prescrite pour une femme de 70 ans. La tutelle de l'adulte est
  **abolie depuis le 1er janvier 2013** ; elle ne subsiste que pour les mineurs. Remplacée
  par la curatelle via l'APEA/KESB (art. 390 ss CC), le mandat pour cause d'inaptitude
  (art. 360 ss CC) et l'art. 15d LCR pour la conduite.

**Consignée** : **AMBOSS-34** — aspirine 325 mg en section notée, forme galénique américaine
non commercialisée en Suisse. Le pédagogique a été harmonisé sur 160-300 mg ; la section
notée reste intacte.

### E. Erreur factuelle

**Corrigées** :

- **AMBOSS-17** — angle calleux de l'hydrocéphalie à pression normale donné à **« < 40° »**
  au lieu de « < 90° ». Le seuil n'est jamais atteint : appliqué tel quel, il ferait manquer
  la seule démence curable.
- **AMBOSS-13** — « Drain thoracique : 14-16F, 2e EIC ligne médio-claviculaire ». C'est le
  site d'**exsufflation à l'aiguille**, pas de drain. Item supprimé.
- **AMBOSS-38** — le mnémo OTTAWA enseignait **deux critères faux** : le calcanéus, qui ne
  fait pas partie de la règle, et l'« articulation » malléolaire au lieu du bord postérieur.
- **AMBOSS-19** — le `resume` invoquait « les critères d'Anthonisen » puis indiquait
  l'antibiothérapie sur « expectoration purulente, dyspnée + **fièvre** ». La fièvre n'est
  pas un critère d'Anthonisen : l'item contredisait sa propre référence et élargissait
  indûment l'indication antibiotique.
- **AMBOSS-25** — « Radiographie thorax : éliminer EP ». Une radiographie normale n'exclut
  jamais une embolie pulmonaire, dans une station dont le diagnostic est une TVP poplitée
  que la grille chiffre elle-même à 30-50 % de risque d'EP.
- **AMBOSS-4** — « Dépistage HPV pour partenaires » : aucun test HPV validé pour le
  partenaire masculin. Et « polype ou atrophie plus rares » était faux : l'atrophie est la
  cause n° 1 (≈ 60 %) des saignements post-ménopausiques.
- **AMBOSS-27** — indication œstroprogestative **inversée** (« si désir de grossesse »).
- **AMBOSS-24** — « Risque modéré-élevé » conclu sans aucun facteur de gravité (la
  strangulation était absente de toute la grille) et ressources renvoyant à une « ligne
  nationale » sans numéro. Facteurs de létalité ajoutés, ressources suissifiées
  (LAVI, 117 / 144 / 143, APEA/KESB).
- **AMBOSS-22** — la « Version longue » contredisait la vignette sur trois points :
  patiente déclarée non-fumeuse alors qu'elle fume un demi-paquet par jour depuis 32 ans
  (sous-item noté, et l'arrêt du tabac est un critère noté), hypertension sous inhibiteur
  calcique inventée à la place du RGO non traité depuis 18 ans, cancer gastrique maternel
  au lieu d'une diverticulose. Le bloc se contredisait lui-même.
- **AMBOSS-10** — « dactylite pathognomonique » : elle ne l'est pas (drépanocytose,
  sarcoïdose, tuberculose, goutte).
- **AMBOSS-16** — deux plafonds de caféine contradictoires dans le même bloc (400 mg/j
  contre 200-300 mg/j).
- **AMBOSS-32** — première ligne du traitement de la chlamydiose inversée.

**Consignées** (sections notées) :

- **AMBOSS-3** — « Cytoréduction maximale: ximale si carcinose » : texte corrompu. L'étudiant
  est noté sur un libellé illisible.
- **AMBOSS-2** — « Amo: 2g IV · Céfo: 2g IV + métronidazole · Ciproflo: 400 mg IV » : trois
  noms de molécules tronqués, dont « Céfo » qui ne permet pas de trancher entre céfuroxime,
  céfoxitine et ceftriaxone.
- **AMBOSS-4** — le critère `a12` porte simultanément « Dernières règles [Il y a 2 ans] » et
  « Âge de la ménopause [45 ans] » chez une patiente de 50 ans : incompatibles.
- **AMBOSS-9** — « Conseil sur les pratiques sexuelles sûres » dans une station de lombalgie
  chez un homme de 71 ans, qu'aucun élément de la vignette n'introduit. Ressemble à un
  résidu d'une autre station.
- **AMBOSS-36** — le score de Maddrey est inutilisable en unités suisses : la bilirubine n'a
  pas de facteur de conversion et le « TP » y est lu comme un taux.

---

## 3. Les points en attente d'arbitrage

Trente-quatre points ont été numérotés au fil du projet. Ils sont regroupés ici par type de
décision. Pour chacun : ce qui bloque, et ce qu'une décision débloquerait.

### 3.1 Défauts du corpus source — décision : ouvrir ou non le barème

Ces points sont dans des **sections notées**. Les corriger suppose de lever le gel.

| Point | Ce qui bloque | Ce qu'une décision débloque |
|---|---|---|
| **12 signes de comparaison manquants**, 10 grilles (AMBOSS-3 « résidu 1cm », 5 « perte poids 5% », 7 « SpO2 92% » ×2, 9 « IMC 25 kg/m² », 12, 14, 33, 34 ×2, 35, 37) | Le signe `<` ou `>` manque réellement dans le HTML. « Oxygénothérapie si SpO2 92% » est ambigu et **le sens s'inverse selon le signe** | Un balayage dédié, purement typographique, lèverait l'ambiguïté sur dix grilles |
| **4 noms de molécules tronqués** (AMBOSS-2 « Amo: », « Céfo: », « Ciproflo: » ; AMBOSS-39 « Ma: ») | Restituer des lettres perdues n'est plus typographique : « Amo » donne aussi bien amoxicilline qu'amoxicilline-acide clavulanique, deux molécules distinctes. AMBOSS-39 exigerait de **supprimer une puce**, donc de toucher au barème | Un arbitrage clinique, molécule par molécule, rendrait lisible le protocole antibiotique d'AMBOSS-2 |
| **AMBOSS-9 : `a13` inexistant, barème plafonné à 49/53** | Corriger exige soit de ramener `maxScores` à 49, soit d'écrire le critère manquant | La station redeviendrait notable à 100 % |
| **AMBOSS-4 `a12`** : dernières règles « il y a 2 ans » + ménopause « à 45 ans » chez une patiente de 50 ans | Données incompatibles dans le même critère noté | Cohérence de la vignette |
| **AMBOSS-9 `m6`** : « Conseil sur les pratiques sexuelles sûres » dans une lombalgie du sujet âgé | Résidu probable d'une autre station | Retrait d'un critère hors sujet |
| **AMBOSS-6 `m6`** « ou 4cm », **AMBOSS-9** « IMC 25 kg/m² », « Bloc radiculaire sélectif L: 3 » | Coquilles en section notée | Lisibilité |
| **2 artefacts d'import** : AMBOSS-39 « antiviraux action directe » (vocabulaire d'hépatite C dans une rupture de coiffe), AMBOSS-38 « Vitamine D 800-1000 UI/j » dupliqué dans la même puce | Contenu étranger à la vignette | Nettoyage |
| **AMBOSS-29** : la grille ne délivre **aucun** résultat d'hémogramme rouge ni de bilan martial, alors que deux critères notés et un bloc thérapeutique entier portent sur l'anémie ferriprive | La branche martiale de la station n'a littéralement rien à délivrer. Corriger imposerait d'**inventer** une hémoglobine et une ferritine | **C'est le point qui demande le plus d'arbitrage médical** : la station est aujourd'hui injouable sur la moitié de son contenu noté |
| **2 américanismes en section notée** : MMSE d'AMBOSS-17 (« président des États-Unis », « l'État ») ; AMBOSS-16 « directives AHA/ACC 2017 » | Un MMSE suisse interrogerait le président de la Confédération et le canton | Cohérence de la suissification |

### 3.2 Mapping SSP à revoir — décision éditoriale sur le vault

| Point | Ce qui bloque | Ce qu'une décision débloque |
|---|---|---|
| **AMBOSS-37 (ictère néonatal)** rattachée à « SSP — Éruption Cutanée », page de dermatologie sans **aucune** occurrence d'ictère, bilirubine, nouveau-né, Coombs ni photothérapie sur 498 lignes. Le vault possède « SSP — Ictère Néonatal » | Le mapping n'a pas été modifié ; l'alignement a été fait en citant la bonne page et en le signalant à chaque fois | Corriger `docs/obsidian-mapping.yaml` rendrait la traçabilité exacte |
| **AMBOSS-15 (maladie cœliaque, garçon de 6 ans)** est en liste `unmapped:` — « page pédiatrique à créer » | **Aucun alignement de prise en charge n'a été fait sur cette grille** : elle n'a reçu qu'un dédoublonnage | Créer la page rendrait la grille alignable comme les 39 autres |
| **AMBOSS-3 (cancer de l'ovaire)** largement hors périmètre de « Douleur Abdominale », qui ne cite pas ce diagnostic | Chimiothérapie, thérapies ciblées et prophylaxie BRCA sont restées sans arbitre | Un rattachement à une seconde page SSP |
| **Portée de « SSP — Douleur Thoracique »** : couvre SCA, EP et pneumothorax **sous tension**, mais ni le pneumothorax **traumatique** ni la toxicité cardiovasculaire des sympathomimétiques | Les deux zones d'AMBOSS-13 et 14 restées sans arbitre | Élargir la page trancherait deux des divergences ci-dessous |

### 3.3 Divergences entre la grille et la page de référence

**Divergence non résolue entre blocs pédagogiques — la seule paire de redondance résiduelle :**

- **AMBOSS-13, seuil de drainage du pneumothorax traumatique.** Le `resume` dit
  « drainage thoracique en urgence » puis « sinon : drainage thoracique **systématique** » ;
  la `theorie` dit explicitement que « le seuil des 2 cm et l'abstention ne valent que pour
  le **spontané** » ; mais l'`expert` et la `presentation` écrivent tous deux « indication
  de drainage **si > 2 cm ou symptomatique** » pour ce même pneumothorax traumatique. La
  grille porte donc, côte à côte, l'énoncé qui écarte le seuil et son application. Ni la
  page SSP (qui ne couvre que le pneumothorax sous tension) ni la section notée ne
  tranchent. **Risque : sous-drainage d'un pneumothorax traumatique. Décision requise.**

**Divergences avec une section notée gelée** (le pédagogique n'a pas été dégradé pour s'y
aligner ; la section notée reste telle quelle) :

- **AMBOSS-11 `m5`** — acide tranexamique 1 g IV si saignement actif. L'essai HALT-IT (2020)
  ne montre aucun bénéfice dans l'hémorragie digestive et un excès d'événements
  thrombo-emboliques.
- **AMBOSS-11 `m3`** — sérologie *H. pylori*, dont le rendement est inférieur aux tests actifs.
- **AMBOSS-22 `m2`** — transit baryté en première intention, que la page SSP **et les propres
  pièges de la grille** contredisent.
- **AMBOSS-8 `m6`** — 5-ASA (mésalazine) pour la maladie de Crohn. Non retenu par les
  recommandations actuelles dans le Crohn ; son rendement est établi dans la RCH.
  **Décision éditoriale requise.**
- **AMBOSS-35 `m5`** — « Oxygène si SpO2 94% » contre « < 90 % » dans le pédagogique. Le
  pédagogique n'a pas été aligné vers le bas : la doctrine du corpus tranche à 90 % et le
  texte de la section notée est visiblement mutilé à cet endroit.
- **AMBOSS-25** — l'`expert` disait « IRM : LCL intact » alors que la section notée décrit
  une rupture du ligament collatéral **et cote son traitement**. Tranché en alignant
  l'`expert` ; **mérite confirmation par un relecteur clinique**.
- **Trois divergences de section notée** : prophylaxie migraineuse à ≥ 4 crises/mois (SSP :
  ≥ 3 invalidantes) ; ibuprofène 600-800 mg (SSP 400-600, et le dosage 800 mg n'existe pas
  en Suisse) ; même inversion œstroprogestative qu'en AMBOSS-27.

**Divergences de référentiel ou de génération de recommandation :**

- **AMBOSS-19** raisonne en GOLD A/B/C/D, **section notée comprise**, alors que la page SSP
  renvoie au pocketcard GOLD **ABE** (2023). Passer à ABE suppose de rouvrir le barème.
- **AMBOSS-18** — palier 1 GINA « SABA prn », antérieur à la bascule vers le CSI-formotérol
  à la demande.
- **AMBOSS-19** — score mMRC décrit « au repos » alors qu'il gradue l'effort.
- **AMBOSS-31** — dépistage par CT faible dose « si 55-80 ans + 30 paquets-années » :
  critères NLST/USPSTF 2013, abaissés à 50-80 ans + 20 PA en 2021 — et la Suisse n'a pas de
  programme de dépistage organisé du cancer pulmonaire.
- **AMBOSS-14** — incohérence interne : l'`expert` donne « Troponine T à 3 h : 150 ng/L
  (positive) », ce qui définit un NSTEMI, alors que le diagnostic retenu partout est un
  angor instable et que le détail noté enseigne « négatives dans l'angor instable ».
  Trancher exige de modifier soit une valeur du scénario, soit une section notée.
- **AMBOSS-14, effet de bord de notre propre conversion** — la grille lit désormais
  « Troponine T initiale : 20 ng/L (limite normale) ». Le nombre est fidèle (0,02 ng/mL
  × 1000), mais l'unité ng/L porte en Suisse une connotation de dosage **hypersensible**
  (99e percentile ≈ 14 ng/L) que ng/mL ne portait pas. La dynamique du cas reste cohérente
  (20 → 150) ; seul le qualificatif « limite normale » devient discutable. Trancher suppose
  de décider si le scénario emploie un dosage conventionnel ou hypersensible — **décision
  d'auteur, non prise**.
- **AMBOSS-6** — si la classe des **antagonistes** de la GnRH est souhaitée (et non
  l'agoniste retenu), c'est relugolix/estradiol/noréthistérone (Ryeqo®) qui est enregistré
  en Suisse.
- **AMBOSS-23** — le remboursement des appareils auditifs reste « variable selon
  pays/assurance ». La page SSP est muette : rien n'a été inventé. À arbitrer si le forfait
  AI/AVS doit être nommé.

**Divergences internes au vault, à corriger côté vault et non côté grilles :**

- **Deux pages SSP se contredisent avec elles-mêmes** : « Mal de Gorge » sur l'éviction
  sportive après mononucléose (4-6 contre 3-4 semaines) ; « Amaurose » sur la fenêtre de
  l'OACR (< 6 h en frontmatter contre < 90 min dans le corps).
- **La page « Capacité de Discernement & Éthique »** fonde le droit d'aviser sur « CP
  art. 364 », article vraisemblablement absorbé par les art. 314c-314d CC en 2019. C'est
  **la page**, pas la grille, qui mériterait vérification.
- **Notation des D-dimères** : « Skills — Références Rapides » et « SSP — Dyspnée » écrivent
  ng/mL, les grilles écrivent µg/L. Nombres identiques, notation différente. C'est le vault
  qui gagnerait à s'aligner ; rien n'y a été modifié.

### 3.4 Périmètre à élargir

| Point | Ce qui bloque | Ce qu'une décision débloque |
|---|---|---|
| **Le bloc `annexe-dd`** (« Diagnostics différentiels à considérer ») est présent dans les **40 grilles**, ~1 800 caractères chacune, soit **~70 000 caractères**. Il se situe **à l'intérieur** de la section Management, donc **hors** de la zone pédagogique définie par la spec. **Aucune tâche ne l'a relu.** Il emploie des puces textuelles « • » et non des `<li>`, donc l'outillage de redondance et de non-perte ne le voit pas non plus. Mesure faite : **130 duplications sur 33 grilles** entre ce bloc et la zone auditée — à comparer aux 301 paires du corpus au départ. Son contenu n'est pas noté | Une divergence y est déjà repérée : AMBOSS-21 y prescrit « Repos au lit phase aiguë » quand la `theorie` dit « repos relatif, pas d'alitement strict » | Élargir le périmètre (≈ une passe de plus sur 33 grilles) ou l'assumer hors champ |
| **3 unités implicites hors hémogramme** (ASAT/ALAT, Na) | Hors du périmètre du balayage, qui portait sur les numérations | Une passe courte et bornée |
| **AMBOSS-34** : la fiche de présentation orale porte la classe `annexe-presentation`, seule des 40. `cases/case-styles.css` ne lui donne **aucune** règle : elle s'affiche en blanc bordé de gris au lieu du fond des 24 autres | Écart visuel **préexistant**. La classe n'a pas été renommée : corriger un outil ne doit pas se faire en modifiant les données qu'il lit | Une règle CSS de trois lignes, ou un renommage de classe |

---

## 4. Ce que le projet a révélé sur le corpus lui-même

Ces constats portent sur la **source** des grilles, pas sur le travail de refonte.

### Un défaut d'import qui tronque les mots au niveau du « x »

L'import qui a produit les grilles **coupe les mots à la lettre `x` et absorbe les lettres
suivantes jusqu'au chiffre** : Ceftria|xone, Amo|xicilline, Céfo|xitine, Ciproflo|xacine,
Ma|ximum. Le même mécanisme coupe les plages posologiques et les décimales, en laissant un
« : » parasite à la place des caractères perdus.

Dix-huit occurrences ont été trouvées dans neuf grilles, **toutes en section notée** :

- **Décimales coupées** — « Nitroglycérine sublinguale **0.: 4 mg** » (AMBOSS-14 **et** 35),
  « Alteplase **0.: 9 mg/kg** » (AMBOSS-34). *« 0.: 4 mg » peut se lire 4 mg au lieu de
  0,4 mg : facteur 10 sur un vasodilatateur. Même risque sur un thrombolytique.*
- **Plages posologiques coupées** — « Morphine 2-: 4mg », « Paracétamol 500-: 1000 mg »,
  « Vancomycine 15-: 20 mg/kg », « Aspirine 160-: 325 mg », « métoprolol 25-: 50 mg »,
  « Apports calciques 1000-: 1200 mg/j », « Prednisone 60-: 80 mg/j », « Diazépam 5-: 10 mg »,
  « Bétahistine 16-: 24 mg ».
- **Mot tronqué** — « Ceftria: 2g × 2/j IV » (AMBOSS-33).

**Quatorze ont été corrigées** (commit `ce250fd`), sur autorisation explicite : la nature
purement typographique de ces corrections ne touche ni sous-item, ni case, ni score — ce
que `check_invariants.py` confirme, et que la vérification n° 2 de ce rapport reconfirme
champ par champ. Les quatre restantes exigent de restituer des lettres perdues, ce qui
n'est plus typographique (§ 3.1).

**Le défaut est présent dès le commit initial du dépôt.** Aucune version intacte n'existe
dans git : chaque reconstitution a dû être validée par le contexte clinique, jamais par
l'historique.

### Douze signes de comparaison manquants

Distinct du précédent, mais de même origine : `<` et `>` disparus dans des sections notées
de dix grilles. Vérifié sur le HTML brut — les caractères manquent réellement, ce ne sont
pas des entités avalées à l'affichage. Détail au § 3.1.

### Des blocs à classe non standard

AMBOSS-34 porte sa fiche de présentation orale sous `annexe-item annexe-presentation` là où
les 24 autres emploient `presentation-patient`. La conséquence dépassait la non-détection :
faute d'alternative dans le marqueur de fin du bloc `theorie`, **13 382 caractères** de la
présentation orale étaient englobés dans le segment `theorie`, et la redondance d'AMBOSS-34
n'avait jamais été mesurée sur son contenu réel. Le seul indice disponible était un chiffre
de redondance anormalement bas pour une grille à quatre blocs. Corrigé côté outillage.

Rien n'empêche une grille future d'introduire une troisième variante de classe : ce serait
le même défaut, avec le même unique symptôme observable, sans garde-fou automatique
possible.

### Une zone jamais auditée

Le bloc `annexe-dd` — 40 grilles, ~70 000 caractères, 130 duplications mesurées avec la
zone auditée — n'a été relu par aucune tâche, et est doublement invisible à l'outillage
(hors de la zone pédagogique par définition ; puces « • » au lieu de `<li>`). Voir § 3.4.

### Trois numérations sanguines en unité implicite

« GB 8500 », « leucocytes 12 000 », « GB 15 000 » : des numérations écrites sans unité, qui
sous-entendent le `/mm³` et doivent se lire en G/L. Corrigées, ainsi que quatre autres
trouvées ensuite. Aucun garde-fou automatique n'est possible sur ce motif — voir § 5.

---

## 5. Limites et angles morts assumés

Documentés en détail dans `scripts/amboss/PROCEDURE.md` § 6.

**Les numérations en unité implicite échappent par construction à toute détection
automatique.** `check_nomenclature.py` cherche des unités ; une valeur écrite sans unité ne
présente rien à détecter — « GB 8500 » ne contient aucun motif. La recherche exhaustive a
été faite **une fois**, à la main, sur les 40 grilles. **Le corpus est propre à cette date,
mais rien ne le maintiendra propre** : toute grille nouvelle, réécrite ou réimportée doit
être relue manuellement sur ce point.

**Un `grep` brut sur une grille produit des faux positifs.** Les images encodées en base64
pèsent ~95 % des fichiers, et l'alphabet base64 contient les lettres, les chiffres, `+` et
`/` : n'importe quelle courte séquence de ces caractères y apparaît par hasard. Constaté :
`grep g/dL` renvoyait trois occurrences, toutes à l'intérieur de blobs d'image, alors qu'il
n'en restait aucune dans le texte. Un motif contenant un accent ou un espace est immunisé ;
les autres ne le sont pas. **Toujours passer par les scripts**, qui neutralisent les images
avant toute recherche.

**Le rapport de non-perte ne reconnaît pas les paraphrases.** Il compare des items par
ressemblance de chaînes avec un seuil fixe : une information reformulée, fusionnée dans une
puce plus longue, ou déplacée d'un registre à l'autre est signalée comme « disparue » alors
qu'elle est bien là. Sur les 684 items signalés dans ce projet (13,2 % des 5 187 items de
départ), l'examen des thèmes sensibles — contre-indication, dose, drapeau rouge, sécurité
du patient, risque suicidaire, protection d'un mineur — n'a retrouvé **aucune perte
réelle** : les items testés survivent tous, soit reformulés, soit fusionnés, soit
délibérément corrigés au titre des erreurs du § 2. Le volume de disparitions par grille
suit d'ailleurs la charge de correction : les quatre grilles les plus au-dessus de la
moyenne (AMBOSS-30 à 32 %, AMBOSS-9 à 28 %, AMBOSS-38 à 24 %, AMBOSS-39 à 20 %, contre
13,2 % en moyenne) sont précisément celles qui ont reçu le plus de corrections de sécurité.

**Le rapport de redondance ne mesure que les paires entre blocs différents.** Une
répétition à l'intérieur d'un même bloc — deux items voisins qui disent la même chose dans
le `resume` — n'est pas comptée. Le corpus en porte encore quelques-unes, visibles
indirectement dans le rapport (deux items du `resume` appariés au même item de la
`presentation`).

**Un chevron nu suivi d'une lettre collée resterait indiscernable d'une balise.**
L'extracteur de texte a été corrigé pour ne plus traiter `< 70 g/L` comme une ouverture de
balise — un défaut qui frappait précisément les seuils de laboratoire, la donnée la plus
sensible du corpus, et qui a produit au moins un faux négatif documenté. La limite
résiduelle (`<N` sans espace) est vérifiée absente à cette date, mais n'est pas garantie
pour l'avenir.

**Une variante de classe non prévue rend un bloc entier invisible.** Corrigé pour le cas
d'AMBOSS-34 ; le principe reste un angle mort, sans garde-fou automatique possible.

**Enfin, ce rapport vérifie la cohérence, pas la justesse médicale.** Les scripts
établissent que le barème n'a pas bougé, que les fichiers sont structurellement sains, que
les grilles calculent juste et que rien n'a disparu sans laisser de trace. Ils n'établissent
pas qu'un contenu clinique est correct. Les corrections du § 2 et les arbitrages du § 3
relèvent d'une relecture médicale, à laquelle ce document sert d'entrée.

---

## Annexe — comment reproduire les vérifications

```bash
python3 scripts/amboss/check_invariants.py       # OK — 40 grilles, code 0
python3 scripts/amboss/check_nomenclature.py     # OK — aucun terme non suisse, code 0
python3 scripts/amboss/report_redundancy.py      # TOTAL : 66 paire(s)
python3 scripts/amboss/check_no_loss.py a845c1b  # rapport, code 0 en toutes circonstances
```

La vérification n° 2 (barème inchangé depuis `a845c1b`) et la vérification n° 6 (contrôle
fonctionnel) ont été menées par des scripts d'audit ponctuels, non versionnés : recalcul
indépendant des six champs de barème des deux côtés de l'historique, et remplissage
complet des 40 grilles dans un navigateur réel (Chrome sans interface), section par
section, minuteur démarré. Résultats : 240 champs de barème identiques ; 39 grilles sur 40
atteignant 100 %, minuteur décomptant sur 40/40, 8 748 réponses patient colorées, zéro
balise orpheline visible, zéro erreur JavaScript.
