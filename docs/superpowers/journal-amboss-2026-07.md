# Journal de refonte — grilles AMBOSS

Référence : `docs/superpowers/specs/2026-07-30-amboss-refonte-pedagogique-suisse-design.md`

Deux types d'entrées :

- **Modification** — un changement appliqué, avec la ligne de page SSP qui le justifie.
- **Divergence** — un écart repéré mais **non corrigé**, laissé à l'arbitrage.

## Format

    ### AMBOSS-N — <motif> (page SSP : <nom>)

    **Modifications**
    - <bloc> · <sujet> : « <avant> » → « <après> »
      source : SSP — <section> — « <citation> »

    **Divergences consignées**
    - <zone> · <sujet> : la grille dit « <x> », la page SSP dit « <y> » — non corrigé (<raison>)

## Entrées

### Passe nomenclature (tâches 2 et 3)

**Modifications**
- global · laboratoire : « NFS » (86×) et « CBC » (1×) → « FSC »
  source : SSP — tableaux Biologie, forme employée dans les 135 pages
- global · laboratoire : « BMP » → « chimie sanguine »
- AMBOSS-28 · urgence : « 911 » → « 144 » ; AMBOSS-35 · urgence : « SAMU » → « 144 »
  source : SSP — Mesures générales — « En Suisse : alerte 144 si instabilité »
  (« 112 » écarté : la seule occurrence du corpus est un total de barème)
- AMBOSS-39 · médicament : « Vicodin » → « Tramal® (tramadol) » — hydrocodone/paracétamol non commercialisé en CH
- AMBOSS-7, 9 · médicament : « Tylenol » → « Dafalgan® (paracétamol) »
- AMBOSS-22 · médicament : « Tums » → « Rennie® (antiacide) »
- AMBOSS-21 · unités : C3 45 mg/dL → 0.45 g/L ; C4 25 mg/dL → 0.25 g/L ;
  créatinine 1.8 mg/dL → 159 μmol/L (× 88,4)
- AMBOSS-37 · unités : retrait de la parenthèse « (5 mg/dL) », la valeur SI restant seule

### AMBOSS-1 — Douleurs abdominales (page SSP : Douleur Abdominale)

Grille pilote. Redondance : 10 paires → 4 (`report_redundancy.py AMBOSS-1_`).

**Modifications**

*Dédoublonnage (contrat de blocs, règle du format)*

- theorie · Examens complémentaires : les deux sections `<h4>Examens complémentaires</h4>` sont
  fusionnées en une seule, celle de queue (`theorie-section-examens`, classe couleur commune aux
  40 grilles). La liste de première intention (« US abdominale : examen de choix / Bilan hépatique /
  Transaminases / Enzymes pancréatiques / FSC ») est supprimée — même format et même contenu que
  `resume`/Examens diagnostiques, qui reste canonique. La section conservée porte le *pourquoi* :
  Se 88 % de l'échographie, indications de l'IRM, du CT et de la scintigraphie HIDA, plus
  l'interprétation du bilan hépatique (PAL/GGT = cholestase, urines foncées et selles décolorées →
  obstacle de la voie biliaire principale). Axe 1.
- presentation · Pièges ECOS : sous-section supprimée en entier — ses quatre items reprenaient
  `expert`/Pièges (RGO, sclérotiques, Murphy, poids) sans changer de format. Axe 6.
- presentation · mnémo 6F : la `mnemo-box` de la Checklist mentale est supprimée. Elle doublait,
  dans le même bloc et au même format, la liste des 6F de Touches ludiques, qui reste seule
  porteuse du mnémo. Ses gloses françaises (« Fat : surcharge pondérale »…) ont été reportées sur
  la liste conservée, sur le modèle clé anglaise / valeur suisse des glossaires de schéma.
  (Le brief situait cette `mnemo-box` dans `resume` : elle est en fait dans `presentation`.)
- theorie · Facteurs de risque : la ré-énumération des 6F est remplacée par le raisonnement appliqué
  à cette patiente (IMC 30, 47 ans, deux grossesses, mère porteuse de calculs) et par ce qui explique
  ces facteurs (sursaturation biliaire en cholestérol, œstrogènes, vidange vésiculaire ralentie).
  Le mnémo lui-même n'est plus répété — renvoi à la fiche de présentation.
- presentation · Signe de Murphy = MURPHY : les quatre items de technique (main sous le rebord
  costal, inspiration profonde, arrêt de l'inspiration, hypochondre droit ciblé) redisaient
  `theorie`/Signe de Murphy. Ils sont condensés en un seul crochet mnémotechnique. La technique
  et les valeurs (Se 65 %, Sp 87 %) restent dans `theorie`, la mention actionnable dans `resume`.
- theorie · Rappels thérapeutiques : le protocole (jeûne, analgésie, antibiotiques, chirurgie ≤ 72 h,
  drainage) recopiait `resume`/Prise en charge. Remplacé par le rationnel — pourquoi la mise à jeun,
  pourquoi la cholécystectomie précoce (fibrose du triangle de Calot, conversions), pourquoi le
  drainage percutané n'est qu'un pont. Axe 2.
- presentation · Q3 « Suivi » : la réponse recopiait mot pour mot `resume`/Suivi sous forme de liste.
  Réécrite en registre oral (`presentation-reponse text`), qui est la raison d'être du bloc. Contenu
  inchangé. Axe 2.

*Check-list rapide ECOS (axes 3 et 4)*

- resume · Questions à poser : « Signes de gravité : malaise, sepsis, confusion ? » →
  « Signes de gravité : frissons, douleur devenue diffuse (sepsis, péritonite) ? » — malaise et
  confusion n'étaient adossés à aucune section détaillée ; frissons, sepsis et péritonite le sont.
- resume · PEC en 3 points : « Hospitalisation + jeûne + perfusion IV + antibiothérapie IV » →
  « Hospitalisation, jeûne, remplissage cristalloïde, antalgie et antibiothérapie IV » — mise en
  cohérence avec Mesures initiales réalignées.
- resume · Examens à faire : « Constantes vitales : TA, FC, FR, SpO₂, T° » conservé bien que
  `resume`/Examen clinique ne mentionne que la fièvre.
  source : SSP — Examen clinique / Signes vitaux — « FC, TA, FR, T° (fièvre ?), SpO₂ »

*Alignement des prises en charge sur la page SSP*

- resume · antalgie : « antalgiques (paracétamol, ± morphine) » → « antalgie par paliers :
  paracétamol 1 g, puis métamizole (Novalgine®) ou morphine titrée IV — éviter les AINS en cas de
  suspicion d'ulcère, d'insuffisance rénale aiguë ou chez le sujet âgé »
  source : SSP — Prise en charge / Mesures générales — « Analgésie (n'efface pas le diagnostic) :
  palier 1 paracétamol 1 g ; palier 2-3 métamizole (Novalgine®, fréquent en Suisse), morphine
  titrée IV ; éviter les AINS si suspicion d'ulcère, IRA ou patient âgé »
- resume · remplissage : « perfusion IV » → « 2 voies veineuses de gros calibre, remplissage
  cristalloïde (NaCl 0,9 % ou Ringer-lactate) »
  source : SSP — Prise en charge / Mesures générales — « ABCDE, monitoring, 2 voies veineuses de
  gros calibre, remplissage cristalloïde (NaCl 0,9 % ou Ringer-lactate) »
- resume · jeûne : « Hospitalisation » + « Jeûne » → « Hospitalisation, mise à jeun tant que la
  chirurgie n'est pas exclue »
  source : SSP — Prise en charge / Mesures générales — « Mise à jeun (NPO) tant qu'une chirurgie
  n'est pas exclue »
- resume · antiémétique : « antiémétiques » → « Antiémétique : ondansétron ou métoclopramide »
  source : SSP — Prise en charge / Mesures générales — « Antiémétique : ondansétron, métoclopramide »
  (la section notée m5 ne cite que le métoclopramide : pas de contradiction, seulement une addition)
- resume · biologie : « Syndrome inflammatoire (CRP ↑, hyperleucocytose) » → « FSC et CRP :
  syndrome inflammatoire (hyperleucocytose, CRP ↑) » ; ajout de « Créatinine, urée, électrolytes :
  déshydratation et troubles ioniques sur vomissements » — `presentation` demandait déjà un
  ionogramme sans que `resume`, source canonique, le porte.
  source : SSP — Examens complémentaires / Biologie 1ʳᵉ intention — « FSC, CRP | Syndrome
  inflammatoire, anémie, hyperleucocytose » et « Créatinine, urée, électrolytes | IRA,
  déshydratation, troubles ioniques »
- theorie · imagerie biliaire : « IRM/CPERM » → « IRM / cholangio-IRM », la CPRE étant rattachée
  au drainage et non au diagnostic.
  source : SSP — Examens complémentaires / Imagerie — « IRM / cholangio-IRM | Grossesse, suspicion
  de lithiase de la voie biliaire principale » ; Conduites ciblées — « Cholangite : antibiothérapie
  IV large spectre + drainage biliaire urgent (CPRE) »
- resume · chirurgie et échographie : inchangés — la page SSP dit « écho HCD, antalgie,
  antibiothérapie si cholécystite, cholécystectomie laparoscopique précoce » ; « ≤ 72 h » est
  l'opérationnalisation usuelle de « précoce », sans contradiction.

*Arbitrage utilisateur — fix round 1 (règle de hiérarchie à trois niveaux, `PROCEDURE.md` § 4)*

- resume · antibiothérapie, molécule : « Antibiothérapie IV empirique (ex : céphalosporine +
  métronidazole) » → « Antibiothérapie IV empirique : amoxicilline-acide clavulanique 1 g × 3/j IV ;
  si allergie, ciprofloxacine + métronidazole ».
  source : **niveau 2** — la page SSP reste générique (« Colique biliaire / cholécystite : […]
  antibiothérapie si cholécystite », sans molécule), donc la section notée `m5` de la grille fait
  foi : « 1ère ligne: amoxicilline-acide clavulanique 1g × 3/j IV » et « Si allergie:
  ciprofloxacine + métronidazole ». Vérifié : aucun autre bloc pédagogique ne portait l'ancienne
  formule (`presentation`/Q2 ne nomme pas de molécule).
- resume · β-hCG : ajout dans Examens diagnostiques / Biologie — « β-hCG chez toute femme en âge de
  procréer, y compris après 45 ans : règle d'or — toute douleur abdominale est une grossesse
  extra-utérine jusqu'à preuve du contraire ». Ajouté aussi à la réponse orale de
  `presentation`/Q « Quels examens demanderiez-vous ? » sous la forme « β-hCG (femme en âge de
  procréer) », qui reste un sous-ensemble strict de `resume` (axe 1).
  source : SSP — Examens complémentaires / Biologie 1ʳᵉ intention — « β-hCG | GEU (toute femme en
  âge de procréer) » ; Règle d'or — « Toute douleur abdominale chez une femme en âge de procréer
  est une GEU jusqu'à preuve du contraire → β-hCG » ; pièges éliminatoires — « Oublier β-hCG femme
  jeune ». Le barème ne bouge pas : l'étudiant l'apprend sans être noté dessus.

**Divergences consignées**

- section notée m5 · antibiothérapie, indication : la grille dit « Antibiothérapie si signes
  infectieux », la page SSP dit « antibiothérapie si cholécystite » (Conduites ciblées) — donc
  indiquée dès que le diagnostic est retenu. Non corrigé : la formulation est dans une section
  notée (barème gelé) et elle est reprise à l'identique par `theorie` et `presentation`, désormais
  cohérents avec elle par la règle de niveau 2.
- section notée m5 · AINS : la grille dit « Analgésie : paracétamol IV, AINS si pas de CI », la page
  SSP dit « éviter les AINS si suspicion d'ulcère, IRA ou patient âgé » — or la patiente prend des
  antiacides pour brûlures d'estomac. Traité en **niveau 1** : la page SSP tranche, la mise en garde
  est portée dans `resume` ; la section notée reste intacte. Précision, non contradiction.
- resume · crase : la page SSP liste la crase (TP, INR, aPTT) avec l'indication « pré-opératoire » et
  la grille conduit à une cholécystectomie ≤ 72 h. Non ajoutée : la page SSP ne la rattache pas
  explicitement à la cholécystite.

**Paires de redondance restantes (4) — justifiées par un changement de format**

- ×2 « nausées, vomissements » (`resume`/Symptômes typiques ↔ `presentation`/Q1 et Q3) : liste de
  symptômes → argument POUR dans une argumentation pour/contre par hypothèse.
- ×2 « échographie abdominale, examen clé » (`resume`/Imagerie et `resume`/Points clés ↔
  `presentation`/Q « Quels examens demanderiez-vous ? ») : liste → réponse orale à une question
  d'examinateur, sous-ensemble strict de `resume` (axe 1, qui prescrit explicitement cette Q/R).

### AMBOSS-2 — Douleurs abdominales, femme 23 ans, appendicite aiguë (page SSP : Douleur Abdominale)

Redondance : 6 paires → 3 (`report_redundancy.py AMBOSS-2_`).

**Modifications**

*Dédoublonnage (contrat de blocs, règle du format)*

- theorie · Examens complémentaires : les deux sections `<h4>Examens complémentaires</h4>` sont
  fusionnées en une seule, celle de queue (`theorie-section-examens`). La section du corps —
  liste « Test β-hCG / FSC / US abdominale / Examen pelvien / Prélèvements cervicaux » — est
  supprimée : même format et même contenu que `resume`/Examens diagnostiques, qui reste canonique.
  Ses deux items non couverts par la queue y sont reportés en *pourquoi* : la déviation gauche
  comme sortie médullaire de neutrophiles immatures (et l'inutilité d'une formule isolée), et
  l'examen pelvien comme seul geste qui départage appendice et annexe. Axe 1.
  Effet mesuré : disparition des paires expert↔theorie « test de grossesse obligatoire » (0.84) et
  resume↔theorie « β-hCG femme en âge de procréer » (0.76).
- theorie · Signes cliniques de l'appendicite : les cinq items redisaient `resume`/Signes abdominaux
  au même format (paire Rovsing à 0.88). Réécrits en mécanisme — projection de la base
  appendiculaire sur la paroi pour McBurney, déplacement rétrograde du gaz colique et distension
  cæcale pour Rovsing, distinction défense / contracture. `resume` reste la liste actionnable.
  source : SSP — Examen clinique / Signe de Rovsing — « déplacement rétrograde du gaz colique qui
  distend le cæcum » ; Signe de Blumberg — « Alternative moins douloureuse : douleur à la toux / à
  la percussion »
- theorie · Rappels thérapeutiques : le protocole (antibioprophylaxie, appendicectomie, couverture
  Chlamydia/gonocoque, traitement du partenaire, surveillance) recopiait `resume`/Prise en charge.
  Remplacé par le rationnel — pourquoi l'antibiotique avant l'incision et pas après, pourquoi ne
  pas attendre, pourquoi la cœlioscopie chez une femme jeune, pourquoi couvrir avant les
  prélèvements, pourquoi traiter le partenaire. Axe 2.
- presentation · Pièges ECOS : sous-section supprimée en entier. Trois de ses quatre items
  reprenaient `expert`/Pièges sans changer de format (β-hCG, histoire gynécologique, DD) ; le
  quatrième (« annoncer l'hospitalisation et la chirurgie ») est déjà porté par le critère noté m4
  « Explication du plan de prise en charge ». Rien de perdu. Axe 6.
- presentation · mnémo APPENDIX : la `mnemo-box` de la Checklist mentale est déplacée dans
  « Touches ludiques / mnémos », où vivent les mnémos, et remplace la liste « les 3A » (Anorexie,
  Abdominal pain migrant, Augmentation fièvre) qui en était un sous-ensemble strict — même bloc,
  même format. La Checklist mentale redevient une trame de présentation pure (axe 5). Le mnémo
  garde ses clés anglaises et reçoit sa glose française (`N = Nausea (nausées)`), règle des
  glossaires.
- presentation · Q3 « Suivi » : la réponse était une liste recopiant la section notée m5 / Suivi
  post-opératoire. Réécrite en registre oral (`presentation-reponse text`), raison d'être du bloc,
  contenu inchangé et complété du relais des prélèvements cervicaux au partenaire, déjà porté par
  `theorie`.

*Check-list rapide ECOS (axes 3 et 4)*

- resume · Examen clinique et Examens à faire : « Douleur à la palpation FID » → « Douleur à la
  palpation de la FID, maximale au point de McBurney » et « Palpation FID : défense, Blumberg,
  Rovsing » → « … : McBurney, défense, Blumberg, Rovsing ». Le signe est noté (critère e5) et
  détaillé par `theorie`, mais `resume`, source canonique, ne le portait pas.
  source : SSP — Examen clinique / Palpation — « McBurney, Rovsing, psoas, obturateur →
  appendicite »
- resume · PEC en 3 points : « Hospitalisation + jeûne + perfusion IV + antibiothérapie IV » →
  « Hospitalisation, mise à jeun, réhydratation IV, antalgie et antibioprophylaxie IV » — mise en
  cohérence avec Prise en charge / En urgence réalignée.

*Alignement des prises en charge*

- resume · antibiothérapie, molécules : « Antibiothérapie IV probabiliste (ex. : amox-clav +
  gentamicine) » → « Antibioprophylaxie IV dans l'heure précédant l'incision :
  amoxicilline-acide clavulanique, ou céphalosporine + métronidazole 500 mg IV, ou ciprofloxacine
  400 mg IV + métronidazole 500 mg IV — dose unique si appendicite simple, 3-5 jours si compliquée ».
  source : **niveau 2** — la page SSP reste générique (Conduites ciblées, « Appendicite : […] avis
  chirurgical, antibiothérapie péri-opératoire », sans molécule), donc la section notée m5 fait
  foi : « Initiation préopératoire (dans l'heure précédant l'incision) », « Amo: 2g IV », « Céfo:
  2g IV + métronidazole 500 mg IV », « Ciproflo: 400 mg IV + métronidazole 500 mg IV », « Dose
  unique si appendicite simple, 3-5j si compliquée ». L'aminoside n'apparaît nulle part dans la
  section notée. Vérifié : plus aucune occurrence de « gentamicine » ni d'« amox-clav » dans le
  fichier.
- resume · remplissage : « perfusion IV » → « Réhydratation IV (NaCl 0,9 % ou Ringer-lactate) »
  source : SSP — Prise en charge / Mesures générales — « remplissage cristalloïde (NaCl 0,9 % ou
  Ringer-lactate) » ; concordant avec la section notée m5 (« Réhydratation IV: NaCl 0.9% ou Ringer
  Lactate »)
- resume · antalgie : « antalgiques » → « antalgie sans attendre le diagnostic — elle n'efface pas
  l'examen : paracétamol 1 g IV × 4/j, ± morphine titrée si douleur intense »
  source : SSP — Points Clés ECOS / Pièges à éviter — « Croire qu'une antalgie masque le
  diagnostic — la morphine peut être administrée » ; Cartes ECOS — « les opiacés diminuent la
  douleur SANS modifier la sensibilité de l'examen abdominal ». Posologie reprise de la section
  notée m5 (« Paracétamol 1g IV × 4/j ± morphine si douleur intense »).
- resume · antiémétique : « antiémétiques » → « antiémétique (ondansétron ou métoclopramide) »
  source : SSP — Prise en charge / Mesures générales — « Antiémétique : ondansétron,
  métoclopramide »
- resume · jeûne : « Hospitalisation » + « Jeûne » → « Hospitalisation, mise à jeun tant que la
  chirurgie n'est pas exclue »
  source : SSP — Prise en charge / Mesures générales — « Mise à jeun (NPO) tant qu'une chirurgie
  n'est pas exclue »
- resume · délai opératoire : ajout de « idéalement dans les 12-24 h suivant le diagnostic ».
  source : **niveau 2** — la page SSP ne donne pas de délai pour l'appendicite ; la section notée
  m5 dit « Timing: Idéalement dans les 12-24h après le diagnostic ».
- resume · β-hCG : « Bêta-hCG chez la femme en âge de procréer » → « … chez toute femme en âge de
  procréer : règle d'or — toute douleur abdominale est une grossesse extra-utérine jusqu'à preuve
  du contraire, quelles que soient la contraception et la date des dernières règles »
  source : SSP — Règle d'or — « Toute douleur abdominale chez une femme en âge de procréer est une
  GEU jusqu'à preuve du contraire → β-hCG » ; pièges éliminatoires — « Oublier β-hCG femme jeune ».
  Le barème ne bouge pas.
- presentation · Q4 « Grossesse extra-utérine » : ajout d'un item aux arguments CONTRE — « Mais
  aucun de ces trois éléments n'écarte la GEU — les règles sont jugées normales par une patiente
  sur quatre : le β-hCG reste obligatoire ». Les trois arguments CONTRE existants (règles il y a
  1 semaine, pilule, pas de retard) sont exactement les trois éléments que la page SSP désigne
  comme le piège.
  source : **niveau 1** — SSP, Cartes ECOS / β-hCG — « Piège : se fier à la date des dernières
  règles ou à “une contraception bien suivie” : les métrorragies manquent dans un tiers des cas et
  les règles sont jugées normales par une patiente sur quatre »

**Divergences consignées**

- section notée m5 · antibiothérapie, noms tronqués : la grille écrit « Amo: 2g IV », « Céfo: 2g IV
  + métronidazole 500 mg IV », « Ciproflo: 400 mg IV ». « Céfo » ne permet pas de trancher entre
  céfuroxime, céfoxitine et ceftriaxone. Non corrigé : section notée, barème gelé. Conséquence sur
  l'alignement : `resume` reprend « céphalosporine » sans nommer la molécule, plutôt que d'inventer.
- resume · groupe sanguin : la page SSP liste « Groupe sanguin + Rh ± RAI | Avant transfusion /
  chirurgie » et la grille conduit à une appendicectomie en urgence. Non ajouté au bilan
  pré-opératoire — la page SSP ne le rattache pas explicitement à l'appendicite et le critère noté
  m2 ne le demande pas (même arbitrage que la crase en AMBOSS-1).

**Paires de redondance restantes (3) — justifiées par un changement de format**

- « Nausées, vomissements » (`resume`/Symptômes typiques) ↔ « Pas de vomissements »
  (`presentation`/Q1) : liste de symptômes → argument CONTRE d'une argumentation pour/contre.
- « Nausées, vomissements, anorexie ? » (`resume`/Questions à poser) ↔ « Nausées et anorexie »
  (`presentation`/Q1) : question de check-list → argument POUR.
- « Séquence typique d'appendicite (douleur diffuse → localisée) » (`theorie`/Particularités de
  cette patiente) ↔ « Séquence typique douleur diffuse → FID » (`presentation`/Q1) : constat
  appliqué au cas → argument POUR d'une argumentation pour/contre.

### AMBOSS-3 — Douleurs abdominales, femme 34 ans, suspicion de cancer ovarien BRCA+ (page SSP : Douleur Abdominale)

Redondance : 5 paires → 3 (`report_redundancy.py AMBOSS-3_`).

**Modifications**

*Dédoublonnage (contrat de blocs, règle du format)*

- theorie · Approche diagnostique : la section est supprimée. Sa liste (examen pelvien bimanuel,
  US transvaginale, CA-125, test BRCA, laparoscopie) redisait `resume`/Examens diagnostiques au
  même format, et sa valeur de CA-125 (« élevé dans 80 % des cancers épithéliaux ») entrait en
  tension avec celle de la section de queue (« 50 % stades I-II, 90 % stades III-IV »), plus
  informative. Ses deux items non couverts — examen pelvien bimanuel, laparoscopie diagnostique —
  sont reportés en *pourquoi* dans `theorie-section-examens` (seul geste percevant une masse
  annexielle avant l'imagerie ; histologie et stadification dans le même temps opératoire, la
  biopsie percutanée étant écartée pour risque d'essaimage). Axe 1. Pas de `<h4>` dupliqué dans
  cette grille : la duplication était structurelle et non titrée.
- theorie · CA-125 : ajout du *pourquoi* de son inutilité en dépistage — au stade où il se positive
  le plus souvent la maladie est déjà étendue, et il s'élève aussi dans l'endométriose, les
  fibromes, une grossesse ou toute irritation péritonéale. Donne son fondement au point clé de
  `resume` (« CA-125 = outil de surveillance, pas de dépistage »), qui l'affirmait sans l'expliquer.
- theorie · Facteurs de risque : la ré-énumération (histoire familiale, nulliparité, ménarche
  précoce, pas de contraception orale, âge) redisait `resume`/Facteurs de risque. Remplacée par le
  mécanisme qui les relie — l'ovulation incessante : chaque ovulation rompt puis répare
  l'épithélium ovarien, chaque réparation est une occasion d'erreur ; et par sa lecture appliquée
  à cette patiente (jamais enceinte, règles à 10 ans, aucune contraception hormonale). L'histoire
  familiale est distinguée comme facteur d'une autre nature (perte d'un mécanisme de réparation de
  l'ADN, non modulation du nombre de cycles).
- theorie · Rappels thérapeutiques : les quatre items (chirurgie de stadification, prophylaxie
  BRCA+, surveillance, contraceptifs oraux) énonçaient des protocoles, dont le premier recopiait
  `resume`/Chirurgie et Chimiothérapie. Remplacés par le rationnel — pourquoi la stadification est
  chirurgicale et non radiologique, pourquoi le résidu tumoral est le premier facteur pronostique,
  pourquoi la salpingo-ovariectomie prophylactique est la seule mesure qui réduise la mortalité,
  pourquoi la surveillance semestrielle ne la remplace pas, pourquoi la pilule réduit le risque de
  40-50 % (même mécanisme que la nulliparité, lu à l'envers). Axe 2.
- presentation · Pièges ECOS : sous-section supprimée. Trois de ses quatre items reprenaient
  `expert`/Pièges (douleur aiguë isolée, histoire familiale minimisée, défi sur la chirurgie). Le
  quatrième — « Oublier de demander un test β-hCG » — n'y figurait pas : il a été **porté dans
  `expert`/Pièges** avant la suppression, sous la forme « Oublier le β-hCG chez une femme de 34 ans
  dont la contraception est peu fiable ». `expert`/Pièges reste canonique et rien n'est perdu.
  Axe 6.
  source : SSP — pièges éliminatoires — « Oublier β-hCG femme jeune »
- presentation · mnémos : la `mnemo-box` OVAIRE est déplacée de la Checklist mentale vers « Touches
  ludiques / mnémos » (la Checklist mentale redevient une trame pure, axe 5). Une fois côte à côte,
  OVAIRE et NAFT doublaient deux entrées au même format et dans le même bloc (« A = Antécédents
  familiaux » ; « R = Risque génétique » vs « F = Facteurs génétiques »). NAFT est supprimé et ses
  deux items propres sont absorbés dans les valeurs d'OVAIRE — « R = Risque génétique (BRCA,
  syndrome de Lynch) » et « I = Irrégularités menstruelles — et tout ce qui multiplie les
  ovulations : nulliparité, ménarche précoce, ménopause tardive » —, les clés du mnémo restant
  intactes (règle des mnémos). Le mnémo des 3B, distinct, est conservé.
- presentation · Q3 « Suivi » : la réponse était une liste recopiant le bilan d'extension de la
  section notée m6. Réécrite en registre oral (`presentation-reponse text`), contenu inchangé.

*Alignement des prises en charge*

- resume · β-hCG : **absent du bloc canonique**, alors que le critère noté m2 l'exige et que trois
  blocs pédagogiques le mentionnaient. Ajout d'une sous-section « Biologie de première intention »
  en tête d'Examens diagnostiques : « β-hCG chez toute femme en âge de procréer, avant toute
  imagerie : règle d'or — toute douleur abdominale est une grossesse extra-utérine jusqu'à preuve
  du contraire, quelles que soient la contraception et la date des dernières règles » et « FSC et
  CRP : anémie (spoliation tumorale ou saignement aigu d'un kyste rompu), syndrome inflammatoire ».
  source : **niveau 1** — SSP, Règle d'or — « Toute douleur abdominale chez une femme en âge de
  procréer est une GEU jusqu'à preuve du contraire → β-hCG » ; Pièges — « Oublier la GEU chez toute
  femme en âge de procréer → bHCG AVANT toute imagerie » ; Examens complémentaires / Biologie
  1ʳᵉ intention — « β-hCG | GEU (toute femme en âge de procréer) » et « FSC, CRP | Syndrome
  inflammatoire, anémie, hyperleucocytose ». Renforcé par la section notée m2 (« β-hCG sérique » ;
  « FSC [pour évaluer une possible anémie due au cancer ou perte sanguine aiguë par rupture de
  kyste] »). Le barème ne bouge pas : c'est le pédagogique qui rattrape son retard sur le noté.
  Cas d'autant plus net que la patiente a 34 ans, est nullipare et utilise la méthode du calendrier.
- resume · PEC en 3 points : « Échographie pelvienne ± Doppler et dosage CA-125 » → « β-hCG
  d'abord, puis échographie pelvienne ± Doppler et dosage CA-125 » — la check-list devient un
  sous-ensemble strict de la sous-section Biologie ajoutée, et respecte l'ordre imposé par la page
  SSP (β-hCG avant toute imagerie). Axe 3.

**Divergences consignées**

- section notée m6 · traitement chirurgical : la grille écrit « Cytoréduction maximale: ximale si
  carcinose (objectif résidu 1cm) » — fragment tronqué, et le seuil est amputé de son signe
  (« < 1 cm » ailleurs dans la grille). Non corrigé : section notée, barème gelé.
- resume · épidémiologie de l'âge : `resume`/Facteurs de risque dit « Âge > 50 ans (pic à 55–64
  ans) », `theorie`/Syndrome BRCA dit « 63 ans population générale ». Ni la page SSP — qui ne
  traite pas du cancer de l'ovaire — ni la section notée ne tranchent. **Niveau 3** : laissé
  inchangé.
- resume · chimiothérapie intrapéritonéale et bevacizumab : `resume` les mentionne, la section
  notée m6 ne retient que carboplatine + paclitaxel (alternative : doxorubicine liposomale ;
  inhibiteurs de PARP si BRCA+) et la page SSP est muette. Pas de contradiction, seulement une
  addition. **Niveau 3** : laissé inchangé.
- portée de la page SSP : « Douleur Abdominale » ne cite le cancer de l'ovaire ni dans son DD Top 5
  ni dans ses conduites ciblées. Tout le versant oncologique de cette grille relève donc du niveau 2
  (section notée) ou du niveau 3 ; seul le versant « douleur abdominale de la femme en âge de
  procréer » a pu être arbitré au niveau 1.

**Paires de redondance restantes (3) — justifiées par un changement de format**

- « Douleurs abdominales ou pelviennes chroniques » (`resume`/Symptômes fréquents) ↔ « Douleurs
  abdominales chroniques » (`presentation`/Q1) : liste de symptômes → argument POUR d'une
  argumentation pour/contre.
- « Nulliparité, ménarche précoce, ménopause tardive » (`resume`/Facteurs de risque) ↔
  « Nulliparité, ménarche précoce » (`presentation`/Q1) : liste de facteurs de risque → argument
  POUR appliqué à cette patiente.
- « Échographie pelvienne (transvaginale) : masse ovarienne suspecte » (`resume`/Imagerie) ↔
  « Échographie pelvienne transvaginale » (`presentation`/Q « Quels examens demanderiez-vous ? ») :
  liste → réponse orale à une question d'examinateur, sous-ensemble strict de `resume` (axe 1, qui
  prescrit explicitement cette Q/R).
