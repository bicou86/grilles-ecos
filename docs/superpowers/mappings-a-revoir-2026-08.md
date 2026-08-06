# Appariements grille ↔ page du vault à revoir

Relevé constitué pendant la campagne d'illustration des cinq corpus. **Chaque
entrée a été vérifiée à la source** : lecture de la vignette et des critères
notés de la grille d'un côté, lecture de la page du vault et de son iconographie
de l'autre. Rien n'est déduit du seul titre.

Ce document ne modifie pas `docs/obsidian-mapping.yaml`. Il liste ce qui, corrigé
là-bas, rendrait ces grilles illustrables — plusieurs sont aujourd'hui sans image
ou avec une planche faible **parce que leur page ne parle pas de leur sujet**.

La règle de sourçage de la campagne interdit d'emprunter la page d'une autre
grille : c'est pourquoi ces cas se traduisent par une absence, et non par un
rattrapage silencieux.

---

## 1. Appariement fait sur un mot du titre, pas sur le contenu

| Grille | Page actuelle | Ce qu'est réellement la vignette |
|---|---|---|
| `RESCOS-11 - Chute` | SSP — Chute & Évaluation Gériatrique | **Traumatisme du coude** chez une femme de 24 ans, réception bras tendu, examen neuro-vasculaire radial-médian-ulnaire. La page traite la chute du sujet âgé : col fémoral, Romberg, Timed Up & Go, GDS-15. Le vault n'a **aucune page « coude »**. |
| `RESCOS-31 - Douleur lombaire` | SSP — Lombalgies | **Colique néphrétique**. La page reste exploitable par sa branche « origine non rachidienne », qui cite les calculs — mais l'appariement suit le titre. |
| `ECOS1-S2 - Méléna sous AVK` | SSP — Rectorragies & Hémorragie Digestive **Basse** | Hémorragie digestive **haute** sur surdosage. La grille ne mentionne ni coloscopie, ni côlon, ni dépistage. **1 image posée** sur 3 visées. |

## 2. Page dont le domaine ne recouvre pas la vignette

| Grille | Page actuelle | Écart, et page qui conviendrait |
|---|---|---|
| `AMC-MedInterne-P6` hypokaliémie et acidose | SSP — Fatigue | Gastro-entérite de 5 jours chez un homme de 74 ans, IRA fonctionnelle, acidose mixte. La page traite le syndrome de fatigue chronique, la dépression, la somnolence. → **Diarrhée**, **Vomissements** ou **Anurie-Oligurie**. **0 image posée.** |
| `AMC-Neuro-P1` sclérose en plaques | SSP — Amaurose & Baisse d'Acuité Visuelle | Ophtalmoplégie internucléaire et syndrome cérébelleux, **sans baisse d'acuité visuelle**. Seul pont : la névrite optique citée en théorie. **2 images**, aucune sur l'OIN ni l'ataxie. |
| `AMC-Neuro-P4` myasthénie | SSP — Fatigue | Rien sur la jonction neuromusculaire. Faiblesse **fatigable**, pas asthénie. |
| `AMC-Neuro-P2` hémangioblastome de la fosse postérieure | SSP — Trouble de la Marche | — |
| `AMC-ORL-P3` rhinosinusite compliquée | SSP — Céphalée | Ni sinusite, ni complication orbitaire, ni classification de Chandler sur la page. |
| `ECOS1-S6` traumatisme abdominal fermé | SSP — Urgences Abdominales Chirurgicales | Page entièrement bâtie sur l'abdomen aigu **non traumatique** (McBurney, psoas, Alvarado, occlusion, AAA). **1 image posée.** |
| `AMC-MCPR-ARC12` primo-infection VIH | SSP — SD Counselling Dépistages | 28 images, dont ~15 scans de dépistage colon/sein/poumon. **Aucune sur le VIH.** **1 image posée**, sous le plancher de 2. |
| `Pédiatrie - Cardiopathie congénitale CIV` | SSP — Troubles de la Croissance | Le vault n'a aucune page de cardiologie congénitale ; le rattachement vient probablement du retard de croissance de la vignette. **0 image.** |

## 3. Grilles non mappées, faute de page correspondante

Vérifié à la source : aucune page `SSP ECOS/` ni `Skills ECOS/` ne couvre ces
sujets. Ce n'est donc pas une erreur d'index mais une lacune du référentiel.

- `AMC-Psy-P12` TDAH de l'adulte · `AMC-Psy-P2` trouble paraphilique ·
  `AMC-Psy-P4` TSA de l'adulte — les seules pages qui parlent de TDAH
  (`CK — Psychiatrie`, `CK — Pédiatrie`, `SSP — Troubles du Développement`) sont
  hors du domaine du mapping et portent sur l'enfant.
- `AMC-MCPR-ARC21` bilan préopératoire — aucune page « bilan préopératoire »
  parmi les 135 pages `SSP ECOS/`.
- `Psy-Vignette 1` personnalité narcissique — aucune page « troubles de la
  personnalité ».
- `AMC-Chir3-ECG7` épicondylite chronique — **le vault n'a aucune page
  « coude »**, comme pour RESCOS-11.
- `AMC-Chir3-ECG1` fracture ouverte de jambe — mappée sur Polytraumatisme, dont
  les 6 images visent le polytraumatisé grave ; la vignette est un traumatisme
  sportif isolé.

## 4. Défauts de l'index de campagne, pas du mapping

Ces trois-là relèvent de `scripts/build_obsidian_mapping.py` :

- **`RESCOS-69b`** est marquée « NON MAPPÉE » à tort : le script mappe encore
  l'ancien nom `RESCOS-69 - Traumatisme MS - Basketteur 25 ans`, alors que le
  fichier a été renommé. La page voulue, `SSP — Douleur d'Épaule`, est correcte.
- **`RCI-Fièvre et douleurs articulaires`** est « NON MAPPÉE » alors que
  `SSP — Douleurs Articulaires` existe et conviendrait. **0 image posée**, la
  règle de sourçage interdisant d'emprunter la page de six autres grilles.
- **`Mal au dos - Guillain-Barré - Grille ECOS (1)`** est exclue comme doublon
  (« même patient Z.T. que Mal au dos 2 »). Son `annexe-theorie` est
  **identique à l'octet près** à celui de « Mal au dos 2 ». Si c'est bien le
  même cas, la planche de cette dernière s'y applique telle quelle.

## 5. Pages correctement appariées mais trop pauvres

Ni erreur de mapping ni lacune du référentiel : la page traite bien le sujet,
mais son iconographie ne suffit pas.

- `SSP — Capacité de Discernement & Éthique` — **aucune image**, seulement deux
  PDF. Prive `EthiqueLegale-V1` (violences conjugales), `-V2` (aptitude à la
  conduite) et `-V4` (consentement éclairé).
- `SSP — Intoxications Aiguës` et `SSP — Syndromes Iatrogènes Psychiatriques` —
  **aucune image raster**, uniquement des transclusions de PDF. Prive les trois
  grilles d'intoxication.
- `SSP — Œdème Scrotal` — aucune image citée.
- `SSP — Troubles de l'Humeur` — deux images au total.
- `SSP — Urgences Psychiatriques` — deux images, aucun message-clé.
- `SSP — Malaise & Perte de Connaissance Brève` — iconographie exclusivement
  syncopale ; prive `Épilepsie absence - Fille de 7 ans` et `RESCOS-49`
  (hypoglycémie sévère).
- `SSP — Toux Chronique` — adulte à 90 % ; sa seule image pédiatrique est un
  algorithme thématique. Prive `RESCOS-63` (coqueluche du nourrisson).
- `SSP — Douleur Abdominale` — rien sur les colites infectieuses ou
  inflammatoires ; sept grilles la partagent.
- `SSP — Dyspnée` — rien sur le SOH, le SAS, l'hypertension pulmonaire, le
  pneumomédiastin ni la tuberculose.
- `SSP — Troubles Thyroïdiens` — purement thyroïdienne, rien sur la parathyroïde
  ni l'hypercalcémie ; prive `AMC-Chir5-ECG3` (hyperparathyroïdie).
- `SSP — Adénopathie` — aucune image du médiastin ; prive `AMC-Chir5-ECG1`.
- `SSP — Fièvre au Retour de Voyage` — 13 de ses 14 images documentent la prise
  en charge d'un malade ; la quatorzième est allée à German-86.

---

## 6. Ajouts des corpus `triage` et `usmle`

### Un changement de page immédiatement applicable

**`Triage-30`** (masse testiculaire) est mappée à `SSP — Œdème Scrotal`, qui ne
cite **qu'un PDF et aucune image**. Or `SSP — Douleur Testiculaire` existe dans
le vault et porte **cinq images utilisables** — palpation testiculaire, canal
inguinal, transillumination, torsion. C'est le seul cas de tout le relevé où la
page de remplacement est identifiée et immédiatement disponible.

### Pages dont le contenu ne recouvre pas la vignette

| Grille | Page actuelle | Ce que la page ne contient pas |
|---|---|---|
| `Triage-9` coup de chaleur avec IRA sur AINS | SSP — Fièvre | page entièrement consacrée à la fièvre infectieuse (tuberculose, paludisme, MNI, endocardite, Centor) ; aucune image du coup de chaleur |
| `Triage-14` diabète de type 2 | SSP — Perte de Poids Involontaire | **aucune image du diabète**, qui est pourtant le diagnostic de la vignette |
| `Triage-17` acidocétose diabétique | SSP — Nausées, Vomissements & Hématémèse | page bâtie sur l'hémorragie digestive haute et la cirrhose ; aucune image d'acidocétose |
| `Triage-18` cholécystite, Murphy positif | idem | aucune image de vésicule biliaire |
| `Triage-19` GEU, maladie inflammatoire pelvienne | SSP — Douleur Abdominale | **aucune image gynécologique** |
| `USMLE-36` visite pré-embauche | page ne citant qu'une image, sur l'exposition au bruit | rien sur le versant respiratoire qui domine la vignette |

### La lacune la plus coûteuse du référentiel

**`SSP — Capacité de Discernement & Éthique` ne cite aucune image**, seulement
des PDF. Elle prive désormais **sept grilles** réparties sur quatre corpus :
`EthiqueLegale-V1` (violences conjugales), `-V2` (aptitude à la conduite),
`-V4` (consentement éclairé), `Arden` (col fémoral et discernement),
`Triage-39` (maltraitance), `USMLE-34` (violence domestique) et `USMLE-9`
(agression sexuelle).

Dans chacun de ces cas **l'appariement lui-même est juste** — c'est bien la page
du sujet. Enrichir cette page d'iconographie débloquerait sept stations d'un
coup, sans toucher au mapping.

Deux autres pages sont dans le même état : `SSP — Intoxications Aiguës` (prive
`Triage-40` et les trois grilles d'intoxication de rescos-locales) et
`SSP — Œdème Scrotal` (voir ci-dessus).
