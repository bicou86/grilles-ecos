# Refonte pédagogique des 40 grilles ECOS AMBOSS — rapport de vérification finale

Branche `refonte-amboss-suisse` · Référence d'origine (avant toute modification de
contenu) : `a845c1b` · Journal détaillé : `docs/superpowers/journal-amboss-2026-07.md`

> **Ce document couvre deux phases.** Les sections 0 à 5 rapportent la **première
> phase** — état vérifié `30e3682`, 30 commits depuis `main`. Elles se lisent comme
> l'état des lieux de ce moment-là, et se terminent sur trente-neuf points laissés à
> l'arbitrage.
>
> La **§ 6 rapporte la seconde phase**, qui a traité ces trente-neuf points. Trois
> chiffres des sections 0 à 5 y sont révisés, et l'unique échec de la vérification n° 6
> ci-dessous est **corrigé**. En cas de divergence entre les deux, c'est la § 6 qui donne
> l'état actuel.

---

## 0. Résultat des vérifications (première phase)

Six vérifications ont été menées sur l'ensemble du corpus. **Cinq passent. Une échoue,
sur un défaut préexistant que la première phase n'a ni introduit ni pu corriger — il est
depuis corrigé, voir § 6.**

| # | Vérification | Résultat |
|---|---|---|
| 1 | Invariants et nomenclature | **OK** — `check_invariants.py` : 40 grilles, code 0 · `check_nomenclature.py` : aucun terme non suisse, code 0 |
| 2 | Barème inchangé depuis `a845c1b` | **OK** — 240 champs recalculés sur les 40 grilles, zéro divergence |
| 3 | Intégrité structurelle | **OK** — 40/40 fichiers, balises équilibrées, blocs attendus présents |
| 4 | Redondance | **OK avec une réserve** — 301 → 66 paires ; 65 justifiées, 1 résiduelle (AMBOSS-13) |
| 5 | Non-perte d'information | **OK** — 684 items signalés, aucune perte réelle retrouvée sur les thèmes sensibles |
| 6 | Contrôle fonctionnel | **ÉCHEC sur 1 grille / 40** — AMBOSS-9 · *corrigé en seconde phase* |

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

## 6. Seconde phase — traitement des points d'arbitrage

État vérifié : branche `refonte-amboss-suisse`, 43 commits depuis `main`.
Décisions et motifs : `docs/superpowers/arbitrages-amboss-2026-08.md`.

Les trente-neuf points laissés en attente au § 3 ci-dessus ont été traités. Le mandat
levait deux verrous : le **gel du barème**, remplacé par trois règles écrites
(correction sans changement de structure ; ajout ou retrait d'un sous-item, avec recalcul
synchronisé de `maxScores`, du dénominateur affiché et du snapshot ; jugement d'auteur
laissé intact et documenté), et le **périmètre**, élargi au bloc `annexe-dd`.

**Le défaut qui faisait échouer la vérification n° 6 ci-dessus est corrigé.** AMBOSS-9
atteint 100 %, comme les 39 autres. Un garde-fou permanent a été créé pour que ce type de
défaut ne puisse plus traverser un projet entier (§ 6.5).

## 6.1 Ce que la seconde phase a changé

### Redondance

La première phase mesurait sur quatre blocs. `annexe-dd` — présent dans les 40 grilles,
~70 000 caractères — était invisible à l'outillage pour deux raisons cumulées : hors de
la zone pédagogique par définition, et écrit en puces textuelles « • » plutôt qu'en
`<li>`. L'outillage a été étendu aux deux fronts, puis toutes les mesures ont été
refaites. Les chiffres ci-dessous sont **tous produits par la même version du script**,
appliquée rétroactivement à chaque état de l'historique — seule façon de les comparer.

| État | Total | dont `annexe-dd` | hors `annexe-dd` |
|---|---|---|---|
| Origine (`a845c1b`) | **495** | 194 | 301 |
| Fin de la première phase | **240** | 175 | 65 |
| Après dédoublonnage d'`annexe-dd` | **147** | 102 | 45 |
| Aujourd'hui | **147** | 102 | 45 |

Deux lectures, à ne pas confondre :

- **Le chiffre de la première phase (301 → 65, −78 %) reste exact** : c'est la colonne de
  droite, la zone qui était dans le périmètre.
- **Sur le corpus entier, l'état réel de départ était 495 paires, pas 301.** Un tiers de
  la redondance vivait dans une zone que personne ne mesurait. En comptant cette zone, la
  réduction totale est de **495 → 147, soit −70 %**.

La zone entrée tardivement dans le périmètre porte l'essentiel du travail de cette phase :
**175 → 102 paires** (−42 %), obtenu en 27 grilles pour **42 insertions et
580 suppressions**. La sous-section « Arguments pour et contre » de `presentation` passe
de 126 à 67 items sur les grilles 21 à 40. Le reste du corpus recule de **65 → 45**
(−31 %), effet indirect : dédoublonner `annexe-dd` supposait de porter des arguments dans
les blocs canoniques avant de les retirer, ce qui a reformulé des items ailleurs.

### Volume et barème

| Mesure | Première phase | Seconde phase | Total depuis l'origine |
|---|---|---|---|
| Grilles modifiées | 40 | 34 | 40 |
| Lignes dans `cases/` | +1 170 / −1 932 | **+154 / −694** | +1 310 / −2 612 |

Répartition de la seconde phase, par passe :

| Passe | Grilles | Diff |
|---|---|---|
| Dédoublonnage d'`annexe-dd` | 27 | +42 / −580 |
| Défauts d'import (négations, seuils, molécules) | 20 | +41 / −41 |
| Erreurs médicales en section notée | 12 | +27 / −24 |
| Alignements sur les référentiels actuels | 5 | +25 / −22 |
| AMBOSS-37 réalignée sur la bonne page SSP | 1 | +10 / −6 |
| AMBOSS-13, seuil de drainage | 1 | +5 / −5 |
| Retrait du critère `a12b` | 1 | −12 |
| Défauts résiduels (unités, remboursement, puce vide) | 6 | +8 / −8 |

**Le barème a bougé sur une seule grille des quarante.** AMBOSS-9 :
`maxScores.anamnese` 53 → 49, `maxScores.management` 17 → 16, les deux dénominateurs
affichés suivis à l'identique, `sectionInfo[].count` 13 → 12, un critère et cinq
sous-items notés retirés. Les 39 autres grilles sont identiques à l'origine sur les huit
champs gelés — vérifié champ par champ contre `a845c1b`, sans passer par le snapshot.

Non-perte d'information : 103 items signalés sur les 34 grilles modifiées par cette
phase ; chacun a été verdicté par la tâche qui l'a produit, aucune perte réelle retenue.
Les seuls items disparus sans équivalent sont les énoncés faux eux-mêmes — le 5-ASA du
Crohn, les valeurs de troponine erronées, le palier GINA périmé, l'argument « pas de
chute » d'une patiente qui avait chuté.

## 6.2 Les décisions prises, et leur motif

Chaque décision est tracée séparément dans `docs/superpowers/arbitrages-amboss-2026-08.md`,
pour qu'elle puisse être contestée sans remettre les autres en cause. En résumé :

| Groupe | Décision | Motif |
|---|---|---|
| Cadrage | Gel du barème levé, sous trois règles écrites | Le mandat le demandait ; les trois règles bornent ce qui devient possible, et la règle 2 impose le recalcul synchronisé plus la régénération du snapshot |
| 1 | AMBOSS-37 rerattachée à « SSP — Ictère Néonatal » | La page d'origine, « Éruption Cutanée », ne contient aucune occurrence d'ictère, bilirubine, nouveau-né, Coombs ni photothérapie sur 498 lignes |
| 1 | Périmètre élargi à `annexe-dd` | 130 duplications mesurées avec la zone auditée, contenu non noté, rôle assignable sans ambiguïté (raisonnement différentiel) |
| 2 | Défauts d'import corrigés (26 signes de comparaison, 3 molécules, 6 artefacts) | Cause unique identifiée : l'import tronque les mots à la lettre `x`. Le sens est univoque dans chaque cas, et l'ambiguïté est dangereuse — « oxygénothérapie si SpO2 92 % » s'inverse selon le signe |
| 3 | 14 erreurs médicales corrigées en section notée | Chacune citée à sa source ; toutes préexistantes |
| 4 | 7 alignements sur les référentiels actuels | Aucun n'a exigé de toucher au barème : vérification faite avant, sous-item par sous-item |
| 5 | Le vault n'est pas modifié | Il appartient à l'utilisateur et sert d'autres corpus. Les quatre points le concernant sont signalés, pas corrigés |
| 6 | Outillage : garde-fou d'atteignabilité, `sectionInfo[].count` gelé, mode intra-bloc | Voir § 6.5 |

### Deux arbitrages que j'ai dû corriger en cours de route

Un rapport qui tait ses erreurs de pilotage n'est pas fiable. Les deux ci-dessous sont des
erreurs du document d'arbitrage lui-même, c'est-à-dire de la personne qui décidait, pas de
celles qui exécutaient.

**1. Le motif erroné sur `a12b` (AMBOSS-9).** L'arbitrage justifiait le retrait du
treizième critère d'anamnèse par trois motifs, dont deux étaient faux :

- *« Le treizième critère n'existe pas. »* Faux. Il existe, sous l'identifiant `a12b`, et
  c'est précisément ce qui le rend injoignable : `calculateScores()` itère `prefix + i`,
  donc `a1`…`a12`, jamais `a12b`. La conclusion chiffrée était juste par accident.
- *« Il ne porte aucune case à cocher ni bouton. »* Faux également. Il portait quatre
  `<input type="checkbox">`. Ma vérification employait une expression régulière cassée par
  un double échappement, qui rendait zéro. Les trois groupes de boutons de la ligne étant
  effectivement vides, rien ne signalait l'erreur.

La décision de retrait tient sans ces deux motifs, sur le seul fait que le contenu est
hors sujet — une anamnèse d'IST chez un homme de 71 ans consultant pour lombalgie, pendant
exact du « Conseil sur les pratiques sexuelles sûres » retiré du même dossier. Mais sa
**conséquence** changeait : ce n'était pas un retrait sans effet sur les compteurs, c'était
un retrait relevant de la règle 2, avec régénération du snapshot. Le document d'arbitrage
porte les deux rectifications, datées.

Effet de bord instructif : `check_invariants` a signalé l'écart sur `criteriaCount`,
`detailCount` et `checkboxCount`, mais **ni sur `maxScores`, ni sur les dénominateurs
affichés**. C'est la preuve mécanique que ces quatre cases ne valaient aucun point — elles
étaient cochables et hors du calcul.

**2. Le signe inversé de mon relevé sur AMBOSS-12.** Le relevé des signes de comparaison
manquants indiquait, pour AMBOSS-12, un seuil à lire « SpO2 **<** 92 % », par analogie avec
les neuf autres occurrences du corpus, toutes des seuils de déclenchement
(« oxygénothérapie si SpO2 < 92 % »). La tâche d'exécution a lu la phrase entière —
« pour **maintenir** SpO2 92 % » — et corrigé en « **>** 92 % », qui est le sens inverse.
Elle avait raison : un objectif thérapeutique et un seuil de déclenchement s'écrivent avec
des signes opposés. Appliquer mon relevé aurait posé une consigne fausse dans une section
notée d'une grille d'embolie pulmonaire.

Le relevé initial était aussi incomplet : il annonçait 15 occurrences sur 11 grilles, le
balayage exhaustif en a trouvé **26 sur 20**.

## 6.3 Les erreurs médicales de la seconde phase

Toutes préexistantes. Regroupées par nature ; **corrigées** quand la correction était
fondée, **consignées** quand elle relevait d'un jugement d'auteur.

### A. Polarité inversée — l'énoncé disait le contraire de son intention

C'est la catégorie propre à cette phase, et la plus insidieuse : un argument rangé sous
« Arguments CONTRE » mais **privé de sa négation**, qui plaide donc *pour* le diagnostic
qu'il devrait écarter. Un candidat qui révise sur ce bloc apprend l'inverse du
raisonnement. Cinq cas trouvés, tous corrigés.

- **AMBOSS-9** (lombalgie, homme de 71 ans) — sous les arguments contre des **métastases
  osseuses** : « Sueurs nocturnes », « Symptômes urinaires ». La section notée fait
  répondre « Non » aux deux. Corrigés en « Absence de sueurs nocturnes », « Absence de
  symptômes urinaires ».
- **AMBOSS-36** (hépatite alcoolique) — « Ascite ou signes cutanés hépatiques » sous
  CONTRE, alors que l'examen de la station dit « pas d'ascite visible », « matité déclive
  négative », « angiomes stellaires absents », « érythème palmaire absent ». Corrigé en
  « Pas d'ascite ni de signes cutanés hépatiques ».
- **AMBOSS-38** (cheville) — « Œdème ou douleur intense au repos » sous les arguments
  contre une **fracture**, quand le même bloc écrit « douleur relativement légère au repos
  (2/10) » et l'examen « œdème minimal ».
- **AMBOSS-25** (mollet) — sous les arguments contre un **syndrome de loge aigu** :
  « Douleur extrême », « Tension compartiment ». Ce diagnostic n'avait aucun argument
  pour : ses deux seules puces, sous CONTRE et sans négation, énonçaient exactement ses
  deux signes cardinaux. Corrigés en « Absence de… ».
- **AMBOSS-3** (appendicite) — défaut **miroir** : une négation *parasite*, « Pas de
  symptômes chroniques, absents dans l'appendicite », chez une patiente dont la douleur
  dure depuis trois semaines. Corrigé en « Symptômes chroniques, absents dans
  l'appendicite ».

Le balayage a été exhaustif : **365 puces lues** — les 57 blocs de contre-arguments de
`presentation` (22 grilles), les 148 sections « Arguments CONTRE » d'`annexe-dd`
(37 grilles) et les 21 puces « Cependant : » que les grilles 1 à 3 emploient à leur place.

Deux cas voisins n'ont **pas** été corrigés, faute de correction univoque : AMBOSS-19,
où l'argument est bien signé mais rangé du mauvais côté (le corriger le déplacerait sous
POUR et laisserait la BPCO sans aucun argument contre) ; AMBOSS-12, où l'énoncé visé est
irrécouvrable — ni ajouter ni retirer la négation ne le rend cohérent avec le scénario.

### B. Un résultat d'examen qui contredit le diagnostic de la station

- **AMBOSS-14 — la troponine positive dans un angor instable.** Le bloc `expert`, seule
  source que l'examinateur lit à voix haute, délivrait « Troponine T à 3 h : 150 ng/L
  (**positive**) ». Une troponine positive définit un NSTEMI. Or **huit endroits de la
  même grille** enseignent l'inverse — la section notée (« négatives dans l'angor
  instable »), le différentiel, le résumé, les points clés, la théorie, le mnémo, et le
  diagnostic retenu lui-même, cité six fois. Le candidat qui répondait « angor instable »,
  la réponse attendue et notée, était contredit par le résultat qu'on venait de lui
  donner. Corrigé en 8 ng/L à l'admission puis 10 ng/L à 3 h, sous le 99ᵉ percentile suisse
  du dosage hypersensible (14 ng/L) et avec un delta non significatif. La cinétique
  surveillée est conservée : le piège « ne pas se contenter d'une troponine initiale
  normale » reste jouable.

  Ce point corrige aussi l'effet de bord de notre propre conversion d'unités, signalé au
  § 3.3 : « 20 ng/L (limite normale) » n'était plus vrai une fois l'unité passée de ng/mL
  à ng/L, qui connote en Suisse un dosage hypersensible.

### C. Un examen dont la lecture était inversée

- **AMBOSS-37 — le test de Coombs dans l'ictère néonatal.** La théorie affirmait « Test de
  Coombs : **positif dans incompatibilités** ». C'est faux dans le sens dangereux : dans
  l'incompatibilité ABO, le Coombs direct est souvent faiblement positif, voire négatif.
  L'énoncé autorisait donc à écarter une hémolyse sur un Coombs négatif, chez une
  nouveau-née dont la mère est O positif et pour qui l'incompatibilité ABO est le
  troisième diagnostic différentiel de la station. Corrigé en citant la page SSP retrouvée
  par le rerattachement : « souvent faiblement positif, voire négatif, dans
  l'incompatibilité ABO — une hémolyse réelle peut exister malgré un Coombs peu parlant ».
  Le lien Coombs ↔ incompatibilité subsiste ailleurs dans la grille : c'est la conclusion
  abusive qui disparaît, pas l'examen.

### D. Erreurs de fond en section notée, désormais corrigées

Ce sont les points que la première phase ne pouvait que consigner. Chacun est corrigé en
citant sa source.

| Grille | Défaut | Correction |
|---|---|---|
| 14 | Bêtabloquant « si pas de contre-indication » dans un spasme coronaire aux amphétamines | Déconseillé ici, motif nommé (effet alpha non opposé) |
| 8 | 5-ASA (mésalazine) pour la maladie de Crohn | Budésonide 9 mg/j ou prednisone ; le rendement du 5-ASA est établi dans la RCH, non dans le Crohn |
| 11 | Acide tranexamique 1 g IV dans l'hémorragie digestive | Ligne conservée en énoncé négatif, HALT-IT (2020) cité — aucun bénéfice, excès thrombo-embolique |
| 11 | Sérologie *H. pylori* | Antigène fécal ou test respiratoire à l'urée : la sérologie reste positive après éradication |
| 22 | Transit baryté « meilleur test initial » | Seconde intention ; toute dysphagie impose d'abord une endoscopie. La grille se contredisait déjà elle-même |
| 34 | Aspirine 325 mg PO/PR | 160-300 mg PO/IV — ni le dosage ni le suppositoire ne sont commercialisés en Suisse |
| 35 | « Oxygène si SpO2 94 % » | < 90 %, seuil de la page SSP et du reste de la grille |
| 26 | Ibuprofène 600-800 mg ; prophylaxie migraineuse à ≥ 4 crises/mois | 400-600 mg (800 mg n'existe pas en Suisse) ; ≥ 3 crises invalidantes/mois |
| 4 | « Dernières règles il y a 2 ans » avec « ménopause à 45 ans » chez une patiente de 50 ans | Porté à 5 ans, ainsi que les quatre autres occurrences de la même durée |
| 13 | Seuil de 2 cm appliqué à un pneumothorax traumatique ; mesures d'accompagnement rangées sous un titre faux | Les deux encadrés retitrés « Indications au drainage » et « Mesures d'accompagnement » ; le traumatique se draine d'emblée |
| 17 | MMSE demandant le président des États-Unis et l'État | Conseil fédéral et canton |
| 16 | « Pression artérielle élevée (directives AHA/ACC 2017) » à 135/70 mmHg | Normale-haute selon les seuils ESC/SSH ; l'indication de la MAPA, valable dans les deux cadres, est conservée |
| 9 | « Conseil sur les pratiques sexuelles sûres » dans une lombalgie du sujet de 71 ans | Sous-item retiré (règle 2) |
| 9 | Critère `a12b` « 13. Histoire sexuelle », même origine | Critère retiré en entier (règle 2) |

### E. Référentiels périmés

- **AMBOSS-19** — GOLD A/B/C/D → **ABE (2023)**, section notée comprise. Vérifié avant :
  aucun sous-item noté ne cote les groupes, la fusion n'a donc rien retiré au barème. Les
  grades spirométriques 1-4 n'ont **pas** été touchés — GOLD 2023 n'a fusionné que les
  groupes d'évaluation, et les confondre aurait cassé le diagnostic de la vignette.
- **AMBOSS-18** — palier 1 GINA « SABA seul » → **CSI-formotérol faible dose à la
  demande**. La réponse orale de `presentation` portait la même doctrine périmée : elle a
  été corrigée avec, faute de quoi le candidat aurait énoncé le contraire de ce que la
  théorie enseigne. Le SABA de secours reste partout où il est légitime.
- **AMBOSS-31** — dépistage par CT faible dose : 55-80 ans + 30 PA (NLST/USPSTF 2013) →
  **50-80 ans + 20 PA (USPSTF 2021)**, avec la précision qu'il n'existe **pas de programme
  de dépistage organisé en Suisse** — le point qui décide, pour un candidat suisse, si la
  question se pose en station.
- **AMBOSS-19** — score mMRC décrit « au repos » → **à l'effort**, avec sa définition. Une
  dyspnée de repos n'est pas une graduation mMRC.

### F. Autres corrections de contenu dans la zone nouvellement auditée

- **AMBOSS-4** — « la multiparité est légèrement protectrice » donnée comme argument
  contre le **cancer du col**. Elle en est un cofacteur de risque chez la femme
  HPV-positive ; elle n'est protectrice que pour l'endomètre — ce que la même grille dit
  correctement ailleurs. Item supprimé, non porté : la règle anti-perte protège
  l'information, pas l'erreur.
- **AMBOSS-31** — « retour depuis 6 mois » donné comme argument contre une **tuberculose**
  chez un patient revenu d'Inde. Le différentiel le classait correctement en argument
  pour. Réduit au seul élément défendable.
- **AMBOSS-25** — « Pas chute » chez une patiente qui a chuté dans les escaliers, à deux
  puces d'un « Douleur mollet après chute ».
- **Signes cardinaux absents du bloc canonique**, ajoutés : les deux signes de l'apnée
  obstructive du sommeil (AMBOSS-28), la léthargie et les vomissements qui feraient
  basculer un ictère néonatal vers l'urgence (AMBOSS-37), la mobilité passive conservée
  qui écarte une épaule gelée (AMBOSS-39), le rappel que des règles récentes n'écartent
  pas une grossesse extra-utérine (AMBOSS-2).
- **Défauts d'import résiduels** : la puce **`• Palier 1` vide** d'AMBOSS-18 et la puce
  **`• Durée` vide** d'AMBOSS-29, deux fragments dont le contenu avait disparu à
  l'import ; le second restitué d'après la théorie de la même grille (« 3-6 mois après
  normalisation de l'Hb »). Trois artefacts non répertoriés trouvés au balayage
  (AMBOSS-36 ×2, AMBOSS-35), dont la phrase source du fragment d'hépatite C qui
  polluait AMBOSS-39.
- **Unités** : trois valeurs sans unité hors hémogramme (transaminases d'AMBOSS-29,
  natrémie d'AMBOSS-33, seuil d'ASAT d'AMBOSS-36) et le seuil d'éosinophiles d'AMBOSS-19,
  écrit `/µL` — graphie strictement équivalente au `/mm³` déjà banni — porté en `G/L`.
- **Ancrages non suisses** : « IST la plus fréquente **aux États-Unis** » (AMBOSS-32),
  reformulé sans ancrage national faute de donnée suisse dans la page de référence ; le
  remboursement des appareils auditifs « variable selon pays/assurance » (AMBOSS-23),
  remplacé par le régime réel — forfait AI avant l'âge AVS, forfait AVS ensuite, limité au
  monaural, hors assurance de base.

## 6.4 Ce qui reste non corrigé, et pourquoi

### Les trois points de jugement d'auteur

Inchangés depuis le document d'arbitrage, et pour la même raison : les trancher exigerait
de réécrire le cas, pas de corriger une erreur.

1. **AMBOSS-3 (cancer de l'ovaire)** — le versant oncologique (chimiothérapie, thérapies
   ciblées, prophylaxie BRCA) n'a aucune page de référence. Un rattachement complémentaire
   serait plus solide qu'un arbitrage de notre part.
2. **AMBOSS-15 (maladie cœliaque, garçon de 6 ans)** — en liste `unmapped:`, « page
   pédiatrique à créer ». La grille n'a reçu qu'un dédoublonnage ; aucun alignement de
   prise en charge n'a été fait, et aucun ne peut l'être tant que la page n'existe pas.
3. **AMBOSS-24 et 32** — les contenus de protection (violences domestiques, patiente
   mineure) sont enrichis et **délibérément non déduplicés** : le coût d'une répétition y
   reste inférieur à celui d'une omission. Choix assumé, pas un oubli.

### Les valeurs créées pour AMBOSS-29

C'est la seule fois du projet où une donnée clinique a été **créée** plutôt que corrigée.
La grille notait deux critères et un bloc thérapeutique entier sur l'anémie ferriprive
sans délivrer le moindre résultat : le candidat qui demandait l'hémogramme ou le bilan
martial — geste explicitement noté, et explicitement listé comme piège à ne pas manquer —
n'obtenait rien. La branche était morte.

Trois contraintes ont borné les valeurs écrites (Hb 98 g/L, VGM 74 fL, TCMH 23 pg,
ferritine 5 µg/L, fer 5 µmol/L, transferrine 3,8 g/L, TIBC 95 µmol/L, saturation 5 %) :
le tableau de la vignette (ménorragies franches chez une jeune femme de 18 ans) ; le sens
que la section notée prescrit à chaque paramètre ; et la cohérence arithmétique interne —
la TIBC dérive de la transferrine par le facteur standard, la saturation du rapport des
deux, et l'hémoglobine, le VGM et la TCMH impliquent bien une hypochromie.

**Elles restent vraisemblables et cohérentes, sans source externe.** Aucun référentiel ne
les fonde : ce sont des valeurs de scénario, écrites pour rendre la station jouable. Elles
demandent une validation par un relecteur clinique, au même titre qu'une vignette qu'on
rédigerait.

### La réserve sur l'échocardiographie d'AMBOSS-14

Le bloc `expert` délivre « Échocardiographie : hypokinésie segmentaire latérale ». Une
anomalie de cinétique segmentaire au repos est classiquement associée à la nécrose — donc
plutôt à un infarctus qu'à l'angor instable retenu par la station. Elle est cependant
aussi décrite dans l'ischémie sévère et la sidération myocardique, et son territoire
concorde exactement avec le sous-décalage ST en V4-V6 du même bloc. **Défendable en
l'état** : cela relève du jugement d'auteur, non du fait faux — contrairement à la
troponine, qui a été corrigée. Signalé pour arbitrage.

### Les autres points laissés ouverts

- **AMBOSS-3 `m5`** — « Cytoréduction maximale: ximale si carcinose ». Même troncature au
  `x` que les molécules restituées, mais le préfixe perdu n'est pas restituable :
  le deviner serait inventer.
- **AMBOSS-2 `m5`** — « Appendicectomie laparoscopique en urgence: (gold standard) ×
  Traitement immédiat » : artefact dont les deux moitiés diffèrent, ordre d'origine
  indevinable. Et la céfoxitine restituée reste associée au métronidazole, association
  pharmacologiquement redondante : la restitution du nom est acquise, l'association est un
  choix d'auteur préexistant.
- **AMBOSS-26** — « Durée > 2h (AVF 15 min-3 h) » : le seuil tombe à l'intérieur de
  l'intervalle qu'il est censé exclure. Signe présent, valeur discutable.
- **AMBOSS-35** — le critère noté fait dire au patient qu'il « prend » un oméprazole que
  le scénario et la présentation déclarent arrêté. Reste plausible d'un patient qui décrit
  un traitement cessé, et peut être voulu par la station.
- **AMBOSS-34** — acuité visuelle notée « < 20/200 », notation de Snellen en pieds ; la
  Suisse emploie l'acuité décimale (0,1). En section notée, hors des points arbitrés.
- **Les quatre points du vault** (notations divergentes des D-dimères, deux pages qui se
  contredisent elles-mêmes, fondement juridique probablement périmé, portée insuffisante
  de deux pages) : signalés, **rien n'a été modifié dans le vault** — il appartient à
  l'utilisateur et sert d'autres corpus.
- **AMBOSS-23** — aucun montant en francs n'a été écrit pour les forfaits AI/AVS : ils
  sont chiffrés et révisables, les citer sans source datée les rendrait faux à terme.
- **236 paires de redondance intra-bloc** mesurées pour la première fois (§ 6.5) :
  mesurées, non traitées.

## 6.5 Ce que le projet a appris sur l'outillage

**Chaque garde-fou de ce projet a été créé après qu'un défaut lui a échappé.** Aucun n'a
été conçu à l'avance. C'est le constat le plus utile à retenir, parce qu'il vaut pour la
suite : le prochain défaut passera lui aussi par une porte que personne n'a encore pensé à
poser.

| Garde-fou | Le défaut qui l'a motivé |
|---|---|
| `check_no_loss.py` | Le dédoublonnage pouvait perdre de l'information sans qu'aucun script ne le voie. Créé en cours de route ; il a immédiatement trouvé **deux pertes réelles** que trois relectures successives avaient manquées |
| Correction de l'extracteur de texte | `<[^>]+>` traitait le `<` de « Hb < 70 g/L » comme une ouverture de balise et avalait la clause jusqu'au `</li>` suivant. Le défaut frappait **précisément les seuils de laboratoire** — la donnée la plus sensible du corpus — et a produit un faux négatif documenté (« < 90 si coronarien » déclaré inexistant) |
| Deuxième variante de classe dans `BLOCKS` | AMBOSS-34 portait sa présentation orale sous une classe non prévue : **13 382 caractères** étaient englobés dans le mauvais bloc, et sa redondance n'avait jamais été mesurée sur son contenu réel. Seul indice : un chiffre anormalement bas |
| Extension à `annexe-dd` et découpe sur « • » | Un bloc de ~70 000 caractères, présent dans les 40 grilles, invisible pour deux raisons cumulées. Il portait **194 des 495 paires** de redondance d'origine |
| `check_reachability.py` | AMBOSS-9 déclarait 53 points pour 49 calculables et 13 critères pour 12 écrits, depuis le commit initial. Aucun compte d'éléments ne pouvait le voir : `check_invariants` demande « le barème est-il le même qu'hier ? », jamais « est-il atteignable ? » |
| `sectionInfo[].count` gelé dans le snapshot | Le champ même qui rendait ce barème faux n'apparaissait dans aucun diff de baseline |
| Motif `/µL` dans la table de nomenclature | Graphie strictement équivalente au `/mm³` déjà banni. Une passe a « corrigé » une unité implicite en `/µL` **en notant elle-même** que cette forme était hors table, et le contrôle est resté vert |
| Mode intra-bloc du rapport de redondance | Les répétitions internes à un bloc n'avaient jamais été comptées — 236 paires, dont 108 hors du bloc où la répétition est structurellement légitime |

### Ce que `check_reachability.py` vérifie, et pourquoi c'est une autre question

Il rejoue le calcul de score de la page et **simule le remplissage complet** de la grille :
toutes les cases cochées, tous les boutons au maximum, communication au meilleur niveau.
Le total ainsi obtenu doit égaler, section par section, le maximum déclaré **et** le
dénominateur affiché au candidat, et le pourcentage global doit tomber sur 100 %. Il
signale trois écarts que rien d'autre ne voit : un critère promis par la configuration
mais absent de la page ; un sous-item **orphelin**, cochable à l'écran mais hors de la
boucle de calcul, donc sans valeur ; et un maximum déclaré désaccordé de l'affichage.
Contrairement au rapport de non-perte, **il sort en erreur** : c'est une porte.

Contrôle de non-régression : rejoué sur l'état d'origine d'AMBOSS-9, il rend exactement
le défaut — 49 atteignables pour 53 déclarés, un critère `a13` promis et absent, un
orphelin `a12b`, un global à 98 %.

### Les angles morts qui subsistent

- **Une valeur de laboratoire sans unité est indétectable par construction.** « GB 8500 »
  ne contient aucun motif à chercher. La recherche a été faite à la main, deux fois. Et le
  **critère** de la première recherche était lui-même un angle mort : elle ne portait que
  sur les valeurs ≥ 1000, ce qui a laissé passer le seuil d'éosinophiles à trois chiffres
  d'AMBOSS-19 pendant toute la première phase. Le critère d'un balayage exhaustif est
  aussi faillible que le motif d'un script, et il n'en laisse aucune trace.
- **Une variante de classe non prévue rend un bloc entier invisible.** Corrigé pour le cas
  rencontré ; le principe reste, sans garde-fou automatique possible — le seul symptôme
  observable est un chiffre de redondance anormalement bas sur une grille précise.
- **Un chevron nu suivi d'une lettre collée** resterait indiscernable d'une balise.
  Vérifié absent à cette date, non garanti pour l'avenir.
- **Le même piège produit aussi des faux positifs.** Un défaut signalé par une tâche —
  « AMBOSS-27 : *Cortisol 8h bas (*, parenthèse jamais fermée, contenu perdu » — s'est
  révélé inexistant à la vérification : le texte réel est `Cortisol 8h bas (< 100 nmol/L)`,
  complet. C'est un motif de recherche qui s'était arrêté sur le `<` du seuil. Contrôle
  fait depuis : **aucun élément de liste des 40 grilles ne porte de parenthèses
  déséquilibrées**, et neuf autres grilles écrivent la même construction. Un signalement
  produit par un outil se vérifie comme n'importe quelle autre affirmation.
- **Le rapport de non-perte ne reconnaît pas les paraphrases**, et le rapport de redondance
  ne sait pas isoler l'examen discriminant d'`annexe-dd` (la flèche « → » n'est pas un
  séparateur, parce qu'elle est d'usage courant ailleurs dans le corpus).
- **Rien de tout cela n'établit qu'un contenu clinique est juste.** Les scripts établissent
  que le barème est atteignable, que les fichiers sont sains, que rien n'a disparu sans
  trace et que le vocabulaire est suisse. La justesse médicale des corrections de cette
  phase, et des valeurs créées pour AMBOSS-29, relève d'une relecture par un médecin.

## 6.6 Vérifications finales

| Vérification | Commande | Résultat |
|---|---|---|
| Invariants | `check_invariants.py` | **OK** — 40 grilles, code 0 |
| Nomenclature suisse | `check_nomenclature.py` | **OK** — aucun terme non suisse, code 0 |
| Atteignabilité du barème | `check_reachability.py` | **OK** — 40 grilles à 100 %, code 0 |
| Redondance | `report_redundancy.py` | 147 paires (495 à l'origine, −70 %) |
| Redondance intra-bloc | `report_redundancy.py --intra` | 236 paires sur 37 grilles — mesurées, non traitées |
| Non-perte depuis l'origine | `check_no_loss.py a845c1b` | 781 items signalés, rapport, code 0 |
| Intégrité structurelle | audit ponctuel | `div` 27 008/27 008 · `ul` 1 329/1 329 · `li` 6 247/6 247 · `p` 736/736 · `span` 4 550/4 550 · `</html>` final 40/40 |
| Barème contre `a845c1b` | audit ponctuel | Écarts sur la seule AMBOSS-9, tous voulus et justifiés ligne à ligne |

---

## Annexe — comment reproduire les vérifications

```bash
python3 scripts/amboss/check_invariants.py        # OK — 40 grilles, code 0
python3 scripts/amboss/check_nomenclature.py      # OK — aucun terme non suisse, code 0
python3 scripts/amboss/check_reachability.py      # OK — 40 grilles à 100 %, code 0
python3 scripts/amboss/report_redundancy.py       # TOTAL : 147 paire(s)
python3 scripts/amboss/report_redundancy.py --intra   # + 236 paire(s) intra-bloc
python3 scripts/amboss/check_no_loss.py a845c1b   # rapport, code 0 en toutes circonstances
```

Les trois premiers sortent en erreur si un écart apparaît : ce sont des portes. Les deux
derniers listent sans juger et sortent toujours 0 — un item « disparu » peut être une
fusion légitime, une paire résiduelle peut être un changement de format voulu.

L'intégrité structurelle (balises appariées, `</html>` final) et la comparaison du barème
avec `a845c1b` restent menées par des scripts d'audit ponctuels, non versionnés : recalcul
indépendant des champs de barème des deux côtés de l'historique. Le contrôle fonctionnel
en navigateur réel (Chrome sans interface, remplissage complet des 40 grilles) date de la
première phase ; son unique échec — AMBOSS-9 — est depuis corrigé, et
`check_reachability.py` le reproduit désormais hors navigateur.
