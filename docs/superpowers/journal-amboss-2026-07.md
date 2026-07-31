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

*Fix round 2 — perte détectée par `check_no_loss.py` (tâches 5b/5c)*

- theorie · Examens complémentaires (queue) : lors de la fusion des deux sections dupliquées
  ci-dessus, l'interprétation des transaminases (« ASAT, ALAT → atteinte hépatocellulaire ») avait
  été emportée avec la liste supprimée, alors que celle des marqueurs de cholestase (PAL, GGT,
  bilirubine) avait bien été conservée et même enrichie — l'étudiant apprenait à distinguer la
  cholestase mais plus la cytolyse. Détecté par `check_no_loss.py 3b19e2f AMBOSS-1_`
  (`.superpowers/sdd/2026-07-30-amboss-refonte-pedagogique-suisse/task-5b-report.md` § 5, item 2).
  Réparé par l'ajout d'un item sœur à « Bilan hépatique » dans la section de queue :
  « Transaminases (ASAT, ALAT) : atteinte hépatocellulaire plutôt que cholestatique » — interprétation
  concise, pas la liste d'examens (déjà canonique dans `resume`). Sans effet sur la redondance
  (toujours 4 paires) ni sur les invariants.

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

*Fix round 2 — perte détectée par `check_no_loss.py` (tâches 5b/5c)*

- theorie · Examens complémentaires (queue) : lors de la même fusion, la sémiologie échographique de
  l'appendicite (« signe de la cible », « épaississement pariétal ») avait disparu de la zone
  pédagogique — seule la sensibilité (86 %) restait enseignée ; la description ne survivait que dans
  `annexe-scenario` (script de l'examinateur, invisible à l'étudiant qui révise). Détecté par
  `check_no_loss.py 1873649 AMBOSS-2_`
  (`.superpowers/sdd/2026-07-30-amboss-refonte-pedagogique-suisse/task-5b-report.md` § 5, item 1).
  Réparé par l'ajout d'un item sœur à « US abdominale : Sensibilité 86 % » dans la section de queue :
  « US abdominale positive : signe de la cible (coupe transversale), épaississement pariétal » —
  interprétation de ce à quoi ressemble un examen positif, pas la liste d'examens (déjà canonique
  dans `resume`). Sans effet sur la redondance (toujours 3 paires) ni sur les invariants.

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
  ni dans ses conduites ciblées. Seul le versant « douleur abdominale de la femme en âge de
  procréer » a pu être arbitré au niveau 1 (β-hCG, ordre des examens, piège de la contraception).
  **Sont restées sans arbitre de niveau 1, faute de couverture par la page SSP** — chacune vérifiée
  comme non contredite par la section notée m6, donc traitée en niveau 3 et laissée inchangée :
  1. `resume`/Chimiothérapie — protocole platine + taxane, ± bevacizumab (anti-VEGF), voie
     intrapéritonéale ;
  2. `resume`/Thérapies ciblées — inhibiteurs de PARP (olaparib, niraparib, rucaparib), indication
     et place en entretien ;
  3. `resume`/En cas de récidive — seuil des 6 mois, notion de résistance au platine, place des
     soins palliatifs ;
  4. `resume`/Chirurgie — étendue de la stadification (hystérectomie, annexectomie, omentectomie,
     curage) et seuil de résidu ;
  5. `theorie`/Rappels thérapeutiques — prophylaxie BRCA+ (salpingo-ovariectomie après 35-40 ans),
     surveillance semestrielle dès 30 ans, réduction de risque par contraceptifs oraux ;
  6. `theorie`/Syndrome BRCA — pénétrances chiffrées et critères de test génétique.
  Un rattachement complémentaire à une seconde page SSP (masses annexielles / oncologie
  gynécologique) rendrait ces six zones arbitrables. Le mapping relevant du choix de l'utilisateur,
  aucune autre page n'a été consultée.

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

### AMBOSS-12 — Douleur thoracique, femme 35 ans, embolie pulmonaire (page SSP : Douleur Thoracique)

Redondance : 16 paires → 4 (`report_redundancy.py AMBOSS-12_`).

**Modifications**

*Dédoublonnage (contrat de blocs, règle du format)*

- theorie · Score de Wells pour EP : la table des 8 items pondérés était recopiée à l'identique dans
  `presentation`/Touches ludiques (paires à 0.92, 0.90, 0.78). La table est conservée **dans
  `presentation`** — c'est là que vivent les aide-mémoire — et la section de `theorie` est réécrite
  en *pourquoi* : ce que sert une probabilité pré-test (elle choisit l'examen suivant, pas le
  diagnostic), la raison bayésienne du recours aux D-dimères, le poids de l'item subjectif « EP plus
  probable qu'un autre diagnostic », le calcul appliqué à cette patiente (7.5, concordant avec la
  section notée), et le score de Genève révisé comme alternative entièrement objective.
  Anti-perte : avant suppression, deux précisions absentes de la copie conservée y ont été portées —
  « Immobilisation/chirurgie **< 4 semaines** » (la copie disait « récente ») et « probabilité
  élevée, **soit environ 40 % d'EP** ». Axe 1.
  source : SSP — Prise en charge / Suspicion d'EP — « **Genève révisé / Wells** (probabilité pré-test) »
- theorie · Approche diagnostique EP : les trois items d'algorithme (« Probabilité faible /
  intermédiaire : D-dimères → si + : angio-CT », « Probabilité élevée : angio-CT directe ») redisaient
  `resume`/Stratification clinique. Supprimés ; la section garde le *pourquoi* (VPN des D-dimères,
  Se/Sp de l'angio-CT, alternative V/Q) et gagne leur peu de spécificité (âge, inflammation, cancer,
  grossesse) et les contre-indications au CT. Anti-perte : le chaînage « D-dimères positifs →
  angio-CT », absent de `resume`, y a été porté **avant** la suppression (cf. alignements). Axe 1.
- theorie · Prise en charge aiguë EP : le protocole numéroté en 6 points recopiait `resume`/Prise en
  charge (paires resume↔theorie à 0.91 et 0.86 sur la thrombolyse) et, pour les posologies, la
  section de queue Rappels thérapeutiques. Remplacé par le rationnel — pourquoi anticoaguler avant la
  preuve (mortalité de 30 % non traitée, décès dans les premières heures), ce que fait et ne fait pas
  l'anticoagulation (elle n'est pas thrombolytique), pourquoi la thrombolyse est réservée à la
  défaillance du VD (risque hémorragique × 2-3), à quoi sert la stratification (elle commande
  l'orientation), et pourquoi l'oxygène n'est pas systématique. Axe 2.
  Anti-perte vérifiée item par item : ABC/monitoring/VVP et le seuil SpO₂ < 90 % → portés dans
  `resume`/Stabilisation initiale ; énoxaparine 1 mg/kg SC BID et rivaroxaban 15 mg BID × 21 j → déjà
  dans la section de queue ; anticoagulation immédiate et thrombolyse → `resume` et `expert`.
- theorie · Thrombose veineuse profonde : l'item « Facteurs risque : triade de Virchow » redisait la
  clé du mnémo de `presentation` (paire à 0.93) sans rien ajouter. Réécrit en mécanisme — c'est le
  cumul des trois branches, non un facteur isolé, qui fait le risque, ce qui introduit les
  potentialisations chiffrées qui suivent (CO × 3-4, vol × 2-3, tabac × 8-10).
- presentation · Pièges ECOS : sous-section supprimée en entier. Ses quatre items reprenaient
  `expert`/Pièges sans changer de format (antécédents familiaux coronariens, examen des MI,
  anticoagulation retardée, sPESI — cette dernière paire à 0.96). Aucun item propre : rien de porté.
  Axe 6.
- presentation · mnémo SOUFFLE : la `mnemo-box` de la Checklist mentale est déplacée dans « Touches
  ludiques / mnémos », où vivent les mnémos, et prend la forme `presentation-subsection` des mnémos
  déjà déplacés (AMBOSS-2, AMBOSS-3). La Checklist mentale redevient une trame pure (axe 5). Une fois
  côte à côte, la sous-section « Diagnostic rapide EP » s'est révélée être un sous-ensemble strict de
  SOUFFLE — même bloc, même format : ses cinq items (dyspnée brutale, douleur pleurétique, facteurs de
  risque, signes de TVP, ECG S1Q3T3) sont tous couverts par les clés S, L, O/F, U et E. Supprimée.
- presentation · Q3 « Suivi » : la réponse était une liste recopiant `theorie`/Rappels thérapeutiques
  (durée d'anticoagulation, arrêt de la CO, prophylaxie du vol — paire à 0.80). Réécrite en registre
  oral (`presentation-reponse text`), raison d'être du bloc, contenu intégralement conservé.

*Alignement des prises en charge sur la page SSP*

- resume · stratification : « Score bas/intermédiaire : dosage D-dimères » + « Score élevé : imagerie
  directe » → « … dosage des D-dimères — négatifs, ils excluent l'EP ; positifs, ils imposent
  l'angio-CT » + « Score élevé : angio-CT d'emblée, sans passer par les D-dimères ».
  source : SSP — Prise en charge / Suspicion d'EP — « <span>D-dimères</span> (seuil ajusté à l'âge si
  > 50 ans) ; **angio-CT** si positif ou proba haute »
- resume · oxygène et monitoring : « Oxygénothérapie » → « Oxygénothérapie si SpO₂ < 90 % (cible
  88-92 % chez le BPCO) » ; ajout de « Monitoring continu et voie veineuse périphérique ».
  source : SSP — Prise en charge / Suspicion de SCA — « ABCDE, monitoring, voie veineuse, O₂ si
  SpO₂ < 90 % » ; Cartes ECOS / oxygénothérapie — « Cible SpO₂ 88-92 % chez lui [le BPCO], 90-94 %
  sinon » et « pas d'O₂ si SpO₂ ≥ 90 % »
- resume · thrombolyse : « Thrombolyse IV si EP massive avec instabilité hémodynamique » →
  « Thrombolyse par altéplase si EP à haut risque (instabilité hémodynamique), puis soins intensifs ».
  Répercuté sur `resume`/PEC en 3 points et sur `presentation`/Q2, qui restent des sous-ensembles
  stricts (axes 2 et 3).
  source : SSP — Prise en charge / Suspicion d'EP — « <span>EP à haut risque</span> (instabilité) →
  **thrombolyse** (altéplase) + USI » ; Sévérité de l'EP — « haut risque = **soins intensifs** »
- theorie · orientation selon le risque : ajout, dans la section réécrite, de « haut risque → soins
  intensifs ; intermédiaire-haut → soins continus ; intermédiaire-bas → hospitalisation ; bas risque
  (sPESI 0) → traitement ambulatoire possible ». C'est ce qui donne son sens au piège « oublier la
  stratification (sPESI) » d'`expert`, qui l'énonçait sans dire à quoi elle sert.
  source : SSP — Prise en charge / Suspicion d'EP, Sévérité de l'EP — « haut risque = **soins
  intensifs** ; intermédiaire-haut = soins continus ; intermédiaire-bas = hospitalisation ; **bas
  risque (sPESI 0) = ambulatoire possible** »
- resume · β-hCG : **absent des quatre blocs** alors que la patiente a 35 ans, prend une contraception
  orale, et que la conduite proposée l'irradie (angio-CT) puis l'anticoagule. Ajout dans
  `resume`/Examens complémentaires (« β-hCG chez toute femme en âge de procréer, avant d'irradier et
  d'anticoaguler »), report dans la check-list Examens à faire, et ajout du piège correspondant dans
  `expert`/Pièges (« Oublier le β-hCG avant d'irradier et d'anticoaguler une femme de 35 ans »).
  source : **niveau 1** — SSP, pièges éliminatoires — « Oublier β-hCG femme jeune » ; Examens
  complémentaires / 1re ligne — « <span>β-hCG</span> chez toute femme en âge de procréer » ;
  Cartes ECOS — « Douleur thoracique chez une femme jeune — examen à ne pas oublier ? β-hCG …
  la grossesse conditionne l'irradiation (angio-CT) comme la prescription ». Le barème ne bouge pas.
- resume · troponine et NT-proBNP : ajout dans Examens complémentaires (« pas pour le diagnostic, pour
  la stratification du risque — souffrance du VD ») et dans la check-list. `presentation`/Q « Quels
  examens demanderiez-vous ? » demandait déjà la troponine sans que `resume`, source canonique, la
  porte : la Q/R n'était donc pas un sous-ensemble strict (axe 1).
  source : SSP — Examens complémentaires / 2e ligne — « <span>NT-proBNP / BNP</span> » ; Piège ECOS —
  « toute lésion myocardique élève la troponine : EP … c'est la cinétique + le contexte qui font le
  SCA » ; renforcé par `theorie`/Embolie pulmonaire (« Stratification risque : sPESI, troponine,
  échocardiographie »)
- theorie · Rappels thérapeutiques : ajout de « Grossesse : HBPM seule (AOD et AVK contre-indiqués) ;
  diagnostic par YEARS adapté et écho-doppler des MI avant d'irradier » — conséquence directe du
  β-hCG ajouté ci-dessus.
  source : SSP — Prise en charge / Suspicion d'EP — « <span>Grossesse</span> : <span>YEARS</span>
  adapté, <span>écho-doppler MI</span> d'abord ; <span>HBPM</span> seule (<span>AOD</span> CI) »

**Divergences consignées**

- section notée m2 · troponine : le détail noté dit « La troponine T … peut être mesurée 3-4 heures
  après le début de l'infarctus », alors que la page SSP impose l'algorithme hs 0/1 h (ESC) ou 0/3 h.
  Non corrigé : section notée, barème gelé. Sans effet sur l'alignement, aucun bloc pédagogique de
  cette grille ne portant de délai de troponine.
- `expert`/Rôles et interventions · unités : D-dimères en ng/mL et gaz du sang en mmHg. Non modifiés —
  `check_nomenclature.py` ne les considère pas comme non suisses et ils ne sont pas dans la liste des
  termes bannis. Consigné pour mémoire.

**Paires de redondance restantes (4) — justifiées par un changement de format**

- « Gaz du sang : hypoxémie, hypocapnie fréquente » (`resume`/Examens complémentaires) ↔ « Gaz du sang
  (hypoxémie, hypocapnie) » (`presentation`/Q « Quels examens demanderiez-vous ? ») : liste → réponse
  orale à une question d'examinateur, sous-ensemble strict de `resume` (axe 1, qui prescrit
  explicitement cette Q/R).
- « Thrombolyse par altéplase si EP à haut risque … » (`resume`/Traitement spécifique) ↔ « Thrombolyse
  par altéplase si haut risque, puis soins intensifs » (`presentation`/Q2 « Traitement ») : liste →
  réponse orale, sous-ensemble strict (axe 2, qui prescrit explicitement cette réponse).
- ×2 « Douleur thoracique de type pleurale » (`resume`/Symptômes principaux) ↔ « Douleur thoracique
  pleurétique » et « Douleur thoracique brutale » (`presentation`/Q1) : liste de symptômes → arguments
  POUR et CONTRE d'une argumentation pour/contre par hypothèse.

### AMBOSS-13 — Douleur thoracique, homme 35 ans, pneumothorax traumatique (page SSP : Douleur Thoracique)

Redondance : 18 paires → 2 (`report_redundancy.py AMBOSS-13_`).

**Modifications**

*Dédoublonnage (contrat de blocs, règle du format)*

- theorie · Prise en charge du pneumothorax : la liste de protocole (seuils, calibres, sites)
  n'appartenait pas à `theorie` et portait une erreur — « Drain thoracique : 14-16F, **2e EIC ligne
  médio-claviculaire** », qui est le site d'exsufflation à l'aiguille, non celui d'un drain, et qui
  contredisait à la fois `resume` (4e-5e EIC, ligne axillaire antérieure) et la section de queue
  (5e EIC, ligne axillaire moyenne). Section réécrite en *pourquoi* : ce que le seuil des 2 cm veut
  dire et pour quel type de pneumothorax il vaut, pourquoi le traumatique se draine largement (brèche
  alimentée, évolution possible sous tension, aggravée par la ventilation), à quoi sert l'aspiration
  simple, ce que la chirurgie traite réellement, et le mécanisme de la pleurodèse. Axe 2.
  Anti-perte : seuils, aspiration simple, indications chirurgicales et pleurodèse sont tous conservés
  dans la réécriture ; le calibre 14-16F reste dans la section de queue ; seul le site erroné est
  supprimé.
- theorie · Diagnostic du pneumothorax : « Radiographie thoracique debout : ligne pleurale visible »
  redisait `resume`/Imagerie de 1ère intention. Fusionné avec l'item de sensibilité, qui porte le
  *pourquoi* : « sensibilité 50-80 % seulement, meilleure en expiration — d'où l'exigence du cliché
  debout, l'air migrant à l'apex ». Anti-perte : « debout », que `resume` ne portait pas, y a été
  ajouté **avant** la fusion. Axe 1.
- theorie · Présentation clinique du pneumothorax : les trois items d'examen (murmure, hypersonorité,
  frémitus, signes de tension) recopiaient `resume`/Examen clinique — check-list actionnable, que
  `theorie` ne porte jamais. Remplacés par le mécanisme unique qui les explique (l'air interposé
  transmet mal les vibrations, n'amortit pas la percussion, éloigne le poumon de la paroi) et par ce
  qui fait passer sous tension (le retour veineux avant la trachée). Les signes eux-mêmes restent dans
  `resume`.
- theorie · Pneumothorax, facteurs de risque : « sexe masculin, morphotype longiligne, tabac (RR × 20) »
  doublait `expert`/Points clés (facteurs de récidive, paire à 0.74). Réécrit en mécanisme — les apex,
  plus étirés chez le longiligne, portent les blebs ; le tabac est le seul facteur modifiable.
- presentation · Pièges ECOS : sous-section supprimée. Deux de ses cinq items reprenaient
  `expert`/Pièges (pneumothorax simple vs sous tension, examen des autres traumatismes), un troisième
  aussi (explication de la radiographie, paire à 0.89). Les **deux items propres** ont été portés dans
  `expert`/Pièges **avant** la suppression : « Négliger l'analgésie » et « Ne pas vérifier le statut
  vaccinal antitétanique devant les égratignures des mains » (formulation rattachée au cas, la
  prophylaxie générique restant dans la section de queue). Axe 6.
- presentation · mnémo PNEUMO : la `mnemo-box` de la Checklist mentale est déplacée dans « Touches
  ludiques / mnémos » (la Checklist mentale redevient une trame pure, axe 5). Trois sous-sections y
  étaient des listes cliniques recopiant `resume` au même format, toutes supprimées après vérification
  item par item : « Triade clinique pneumothorax » (paires à 1.0 et 0.86 — sa seule valeur propre,
  *dyspnée*, a été absorbée dans la clé O du mnémo : « O = Oxygène nécessaire (dyspnée, désaturation) »),
  « Signes de pneumothorax sous tension » (sous-ensemble strict de `resume`/Signes de gravité, paire à
  1.0 sur la turgescence jugulaire) et « PEC rapide pneumothorax traumatique » (sous-ensemble strict de
  `resume`/Prise en charge et Examens à faire, paires à 0.82, 0.76, 0.75, 0.73).
- presentation · Q3 « Suivi » : la réponse était une liste recopiant `theorie`/Rappels thérapeutiques
  (kinésithérapie, paire à 1.0) et `expert`/Points clés (vol et plongée, paire à 0.86). Réécrite en
  registre oral, contenu intégralement conservé.

*Alignement des prises en charge sur la page SSP*

- resume · pneumothorax sous tension : « Spannungspneumothorax : ponction-évacuation immédiate (2e EIC,
  ligne médio-claviculaire) puis drain thoracique » → « Pneumothorax sous tension : exsufflation à
  l'aiguille immédiate — 2e EIC ligne médio-claviculaire, ou 4e-5e EIC ligne axillaire moyenne (paroi
  plus fine chez l'adulte) — puis drain thoracique ». Le titre de la sous-section
  « Signes de gravité (Spannungspneumothorax) » est francisé de la même façon : le terme allemand,
  hérité de la source, n'apparaît nulle part dans la page SSP, qui écrit systématiquement
  « pneumothorax sous tension ».
  source : **niveau 1** — SSP, Prise en charge / Suspicion de pneumothorax sous tension —
  « **Exsufflation à l'aiguille immédiate** : 2ᵉ EIC ligne médio-claviculaire, ou **4ᵉ-5ᵉ EIC ligne
  axillaire moyenne** (paroi plus fine chez l'adulte) → puis **drain thoracique** »
- resume · oxygène : « Oxygénothérapie haut débit » → « … — cible SpO₂ 88-92 % si BPCO connue ».
  Précision, non contradiction : l'oxygène à haut débit reste indiqué (il accélère la résorption par
  dénitrogénation, rationnel porté par `expert`/Points clés).
  source : **niveau 1** — SSP, pièges éliminatoires — « O₂ haute concentration sur BPCO » ; Cartes
  ECOS — « Cible SpO₂ 88-92 % chez lui »
- theorie · Rappels thérapeutiques, site de drainage : « 5e EIC ligne axillaire moyenne » →
  « 4e-5e EIC dans le triangle de sécurité (ligne axillaire antérieure à moyenne) », qui réconcilie la
  formulation de `resume` (antérieure) et celle de la queue (moyenne) sans contredire la page SSP.

**Divergences consignées**

- pédagogique · seuil de drainage du pneumothorax traumatique : `resume` (Traitement spécifique et PEC
  en 3 points) et `theorie`/Pneumothorax traumatique disent qu'il se draine **systématiquement** ;
  `expert`/Points clés et `presentation` (Checklist mentale, Q2) disent « si > 2 cm ou symptomatique ».
  La page SSP ne traite que le pneumothorax **sous tension** et ne donne aucun seuil pour le
  traumatique ; la section notée de cette grille ne comporte **aucun critère de prise en charge**.
  **Niveau 3** : laissé inchangé, rien inventé. C'est l'origine de la paire de redondance résiduelle
  n° 2 ci-dessous. À arbitrer par l'utilisateur.
- section notée · absence de critère de prise en charge : la grille n'évalue que l'anamnèse, l'examen,
  les hypothèses, les examens et la communication. Aucun arbitrage de niveau 2 n'était donc possible
  sur cette grille : tout ce que la page SSP ne tranche pas est resté en niveau 3.

**Paires de redondance restantes (2)**

- « Hypersonorité à la percussion » (`resume`/Signes respiratoires) ↔ idem (`presentation`/Q1) : liste
  de signes → argument POUR d'une argumentation pour/contre par hypothèse — changement de format.
- « Sinon : drainage thoracique systématique » (`resume`/PEC en 3 points) ↔ « Drainage thoracique si
  > 2 cm ou symptomatique » (`presentation`/Q2) : ce n'est pas une redondance mais la **divergence de
  seuil consignée ci-dessus**, laissée en l'état faute d'arbitre de niveau 1 ou 2.

### AMBOSS-14 — Douleur thoracique, homme 45 ans, SCA / angor instable sur amphétamines (page SSP : Douleur Thoracique)

Redondance : 20 paires → 6 (`report_redundancy.py AMBOSS-14_`).

**Modifications**

*Dédoublonnage (contrat de blocs, règle du format)*

- theorie · Prise en charge initiale du SCA : le protocole numéroté en 7 points recopiait
  `resume`/Urgences initiales et Traitement spécifique, et la section de queue pour les posologies
  (paires theorie↔presentation à 0.89, 0.77, 0.76, 0.75). Remplacé par le rationnel — pourquoi l'ECG
  passe avant tout (seul examen qui déclenche la reperfusion sans attendre la troponine, nécrose en
  front d'onde), pourquoi l'aspirine se croque, ce que les nitrés font et ne font pas, la
  contre-indication de l'infarctus inférieur / du VD, et l'interdit d'anticoaguler avant d'avoir
  écarté la dissection. Axe 2.
  Anti-perte vérifiée item par item : monitoring et VVP → `resume`/Urgences initiales ; ECG < 10 min →
  porté dans `resume`/Examens à faire **avant** la réécriture ; aspirine 300 mg → `resume` et queue ;
  nitrés → `resume` (seuil réaligné, cf. ci-dessous) ; morphine → `resume` ; bêtabloquants et double
  antiagrégation → `resume`/Traitement spécifique.
- theorie · Syndrome coronarien aigu : les quatre items de définition (types, angor instable, NSTEMI,
  STEMI) redisaient le mnémo INS de `presentation` et `resume`/Points clés (paire à 0.73). Réécrits en
  *pourquoi* : ce sont deux marqueurs seulement — la troponine et le sus-décalage ST — qui découpent le
  continuum, d'où les gradients de mortalité et d'urgence ; les trois présentations de l'angor instable
  (repos, de novo, crescendo) sont conservées, car c'est le changement de régime qui signe
  l'instabilité ; la physiopathologie gagne le fait que le spasme suffit seul, ce qui explique ce cas.
- theorie · Présentation clinique du SCA : les trois premiers items (qualité de la douleur,
  irradiations, symptômes végétatifs) recopiaient `resume`/Symptômes typiques et associés. Remplacés
  par le mécanisme (le cœur n'a pas de sensibilité propre, la douleur remonte par les métamères C8-T4)
  et enrichis des présentations atypiques de la page SSP. Axe 1.
- theorie · Examens complémentaires (queue) : « Bilan SCA : FSC, iono, urée/créat, glycémie, bilan
  lipidique » redisait `resume`/Autres bilans (paire à 0.72). Remplacé par le *pourquoi* de chaque
  examen — la créatinine conditionne la coronarographie et pèse dans le score GRACE, le bilan lipidique
  se prélève dans les 24 h avant que l'inflammation aiguë ne fasse chuter le LDL. Anti-perte :
  ionogramme et urée, présents dans la queue mais pas dans `resume`/Autres bilans, y ont été portés
  **avant** la réécriture. Axe 1.
- presentation · Pièges ECOS : sous-section supprimée. Deux de ses cinq items reprenaient
  `expert`/Pièges (traumatisme thoracique — paire à 0.80 —, toxicité des amphétamines) ; le cinquième
  (éducation et prévention secondaire) est déjà porté par le critère noté m6 (« Conseil sur l'arrêt des
  drogues illicites », « Conseil sur l'arrêt du tabac », « Éducation sur les facteurs de risque
  cardiovasculaires »). Les **deux items propres** ont été portés dans `expert`/Pièges **avant** la
  suppression : « Se contenter d'une troponine initiale normale sans la répéter » et « Ne pas citer la
  bithérapie antiplaquettaire (aspirine + P2Y12) ». Axe 6.
- presentation · mnémo MONA-BAS : la `mnemo-box` de la Checklist mentale est déplacée dans « Touches
  ludiques / mnémos » (la Checklist mentale redevient une trame pure, axe 5), où elle remplace la
  sous-section « Amphétamines = 5 effets CV majeurs » — liste recopiant `theorie`/Amphétamines et
  système cardiovasculaire au même format (paire à 0.99 sur la demande en O₂). Vérification item par
  item avant suppression : tachycardie, HTA et vasospasme sont couverts par « Libération catécholamines »
  et « Spasme coronaire », la demande en O₂ et l'activation plaquettaire par leurs items propres.
- presentation · Q3 « Suivi » : la réponse était une liste recopiant `resume` et la section de queue.
  Réécrite en registre oral, contenu intégralement conservé.

*Alignement des prises en charge sur la page SSP*

- resume · ECG : « ECG 12 dérivations (répéter si doute) » → « ECG 12 dérivations **dans les 10 min**
  (répéter si la douleur évolue) ». Le délai n'était porté que par `theorie` ; c'est le premier piège
  éliminatoire de la page SSP.
  source : **niveau 1** — SSP, pièges éliminatoires — « Ne pas faire ECG dans les 10 min » ; Prise en
  charge / Suspicion de SCA — « <span>**ECG dans les 10 min**</span> (SSC/SGK ; répéter si évolution) »
- resume · nitrés : « Trinitrine sublinguale si PAS > **100** mmHg » → « … si PAS > **90** mmHg —
  jamais en cas d'infarctus inférieur ou du ventricule droit (débit précharge-dépendant) ». Le seuil de
  100 contredisait la page SSP et les deux autres blocs de la grille, qui disaient déjà 90.
  source : **niveau 1** — SSP, Prise en charge / Suspicion de SCA — « <span>nitroglycérine</span> SL si
  TA > 90 ; … — **cave infarctus inférieur / droit : pas de nitré** (précharge-dépendant) »
- resume · troponine : « Dosages répétés indispensables » → « Algorithme troponine hs 0/1 h (ESC) ou
  0/3 h : une valeur isolée négative ne suffit jamais ». Répercuté sur la section de queue, qui disait
  « T0, T3h, T6h (protocole 0/3h si haute sensibilité) » : le dosage à 6 h relève du protocole
  pré-haute-sensibilité et n'est pas retenu par la page SSP.
  source : **niveau 1** — SSP, Examens complémentaires / 1re ligne — « <span>**Troponines hs**</span> :
  algorithme **0/1 h** (ESC) ou 0/3 h — *une troponine isolée négative ne suffit jamais* » ; Points Clés
  ECOS / Pièges — « Se contenter d'une troponine isolée négative sans algorithme 0/1h ou 0/3h »
- resume · P2Y12 : « aspirine + inhibiteur P2Y12 (clopidogrel, ticagrelor) » → « … (ticagrélor ou
  prasugrel ; clopidogrel en alternative) » — l'ordre de préférence suit la page SSP sans supprimer le
  clopidogrel, dont la posologie reste dans la section de queue.
  source : **niveau 1** — SSP, Prise en charge / Suspicion de SCA — « <span>**P2Y12**</span>
  (<span>ticagrélor</span> / <span>prasugrel</span>) »
- resume · anticoagulation : « (fondaparinux, énoxaparine) » → « (HNF, énoxaparine ou fondaparinux) —
  jamais avant d'avoir écarté une dissection aortique ».
  source : **niveau 1** — SSP, Prise en charge / Suspicion de SCA — « **anticoagulation** (<span>HNF</span>,
  <span>énoxaparine</span> ou <span>fondaparinux</span>) » ; Réflexes immédiats — « jamais anticoaguler
  avant d'avoir éliminé la dissection »
- resume · stratégie invasive : ajout du palier manquant — « en urgence et sans attendre si très haut
  risque (instabilité, douleur persistante, arythmie maligne, insuffisance cardiaque aiguë, ST
  dynamique) ». `theorie` ne connaissait que « haut risque = coronarographie < 24 h ».
  source : **niveau 1** — SSP, Stratification du risque NSTEMI — « le **très haut risque** (instabilité,
  douleur persistante, ACR, arythmie maligne, complication mécanique, IC aiguë, ST dynamique) impose une
  **coronarographie en urgence**, sans attendre »
- resume · morphine : « Morphine si douleur persistante » → « Morphine **IV titrée** si douleur
  persistante ».
  source : SSP — Prise en charge / Suspicion de SCA — « <span>Antalgie</span> : <span>morphine</span> IV
  titrée »
- resume · titre de sous-section : « Urgences initiales (**monothérapie** MONA) » → « (mnémotechnique
  MONA) » — MONA désigne quatre traitements, la mention d'une monothérapie était une corruption.
- theorie · qualité de la douleur : l'item supprimé disait « Douleur thoracique : oppression,
  serrement, **brûlure** ». La réécriture retient « une douleur constrictive oriente vers le SCA ; une
  brûlure oriente d'abord vers le reflux — mais aucune qualité ne suffit à trancher ».
  source : **niveau 1** — SSP, Anamnèse / SOCRATES — « **C**haracter … · Constrictive = <span>SCA</span>
  · Brûlure = <span>RGO</span> »

**Divergences consignées**

- pédagogique · bêtabloquant chez un consommateur d'amphétamines : `resume`, `theorie` (queue :
  métoprolol 25-50 mg BID) et le mnémo MONA-BAS prescrivent un bêtabloquant « si pas de
  contre-indication », alors que le diagnostic retenu est un **spasme coronaire induit par les
  amphétamines**. La page SSP ne liste comme contre-indications que « IC, bradycardie, hypotension » et
  ne dit rien des sympathomimétiques ; la section notée ne comporte **aucun critère de prise en
  charge**. **Niveau 3** : laissé inchangé, rien inventé. Point signalé à l'arbitrage de l'utilisateur
  (cf. rapport de tâche 6, § préoccupations).
- `expert`/Rôles et interventions · troponine et diagnostic retenu : l'expert donne « Troponine T à 3 h :
  0.15 ng/mL (positive) », alors que le diagnostic retenu partout est un **angor instable** et que
  `resume` enseigne « Troponines négatives (≠ NSTEMI où elles sont positives) » — ce que confirme le
  détail noté m3 (« négatives dans l'angor instable »). Une troponine positive à H3 définit un NSTEMI.
  Non corrigé : trancher supposerait soit de modifier une valeur du scénario de station, soit de
  contredire la section notée. Signalé à l'arbitrage.
- pédagogique · mnémo MONA / MONA-BAS : le M vaut « Monitoring » dans le mnémo de `presentation` et la
  Checklist mentale y ajoute « Morphine si besoin » comme cinquième terme d'un acronyme à quatre
  lettres ; la page SSP écrit « MONABASH ». Ni la page SSP ni la section notée n'imposent une
  correspondance lettre à lettre. **Niveau 3** : laissé inchangé.
- section notée · absence de critère de prise en charge : comme pour AMBOSS-13, aucun arbitrage de
  niveau 2 n'était possible sur le traitement ; tous les points non tranchés par la page SSP sont restés
  en niveau 3.

**Paires de redondance restantes (6)**

Quatre relèvent des Q/R explicitement prescrites par les axes 1 et 2 — `presentation` restitue à l'oral
un sous-ensemble strict de `resume` :

- « Statine forte dose » (`resume`/Traitement spécifique) ↔ idem (`presentation`/Q2 « Traitement »).
- « Échocardiographie transthoracique » (`resume`/Examens à faire) ↔ idem (`presentation`/Q « Quels
  examens demanderiez-vous ? »).
- « Bilan biologique standard (FSC, ionogramme, urée et créatinine, glycémie, bilan lipidique) »
  (`resume`/Autres bilans) ↔ « Bilan biologique : FSC, ionogramme, créatinine, glycémie, bilan
  lipidique » (`presentation`/Q « Quels examens demanderiez-vous ? »).
- « Morphine IV titrée si douleur persistante » (`resume`) ↔ « Morphine si douleur persistante »
  (`presentation`/Q2).

Deux sont des faux positifs du comparateur, appariés sur le seul mot « plaquettaire » :

- « Thrombose : activation plaquettaire » (`theorie`/Amphétamines — mécanisme) ↔ « Double
  anti-agrégation plaquettaire » (`presentation`/Q2 — traitement).
- « Double antiagrégation + anticoagulation » (`resume`/PEC en 3 points) ↔ « Double anti-agrégation
  plaquettaire » (`presentation`/Q2) : check-list → réponse orale, sous-ensemble strict (axe 3).

### AMBOSS-18 — Toux chronique, femme 21 ans, asthme d'effort sur terrain atopique (page SSP : Toux Chronique)

Redondance : 7 paires → 5 (`report_redundancy.py AMBOSS-18_`). Pas de sous-section
`presentation`/Pièges ECOS — vérifié, l'axe 6 ne s'applique pas.

**Modifications**

*Dédoublonnage (contrat de blocs, règle du format)*

- theorie · Diagnostic de l'asthme : la section était une liste de seuils recopiant
  `resume`/Examens diagnostiques (paires à 0.84 sur le FeNO, 0.75 sur la méthacholine). Réécrite en
  *pourquoi* — aucun symptôme n'est spécifique, seule la variabilité signe l'asthme ; une spirométrie
  normale entre les crises n'exclut rien ; le double critère de réversibilité (≥ 12 % **et** ≥ 200 mL)
  évite les faux positifs sur les petits volumes ; la méthacholine vaut par sa sensibilité, pas par sa
  spécificité ; le FeNO prédit la réponse aux CSI et s'abaisse sous tabac ou CSI déjà pris. Les seuils
  restent (axe 1 : `theorie` garde Se/Sp, seuils et indications). Axe 1.
- theorie · Asthme, item « Triggers » : recopiait `resume`/Symptômes typiques (« Déclenchés par :
  effort, allergènes, infections respiratoires, froid, émotions »). Remplacé par le mécanisme —
  l'inflammation abaisse le seuil de la voie réflexe bronchoconstrictrice, c'est l'hyperréactivité qui
  rend banals des stimuli inoffensifs. Les six déclencheurs sont conservés dans la reformulation.
- presentation · mnémo ASTHME : la `mnemo-box` de la Checklist mentale est **déplacée** dans « Touches
  ludiques / mnémos » (la Checklist mentale redevient une trame pure, axe 5), où elle **remplace**
  « Asthme = TRIade ». Vérification item par item avant absorption : T « Toux chronique variable » → clé
  T (« Toux chronique variable, nocturne ou à l'effort ») ; R « Réversible sous traitement » → clé M
  (« Mesure EFR obligatoire — obstruction réversible sous traitement ») ; I « Intermittente + déclenchée »
  → clé E (« Exacerbations déclenchées »). Les clés d'ASTHME restent intactes, seules leurs valeurs
  absorbent.
- presentation · « Asthme d'effort → PENSER à » : sous-section supprimée. C'était une liste clinique
  recopiant `theorie` au même format, vérifiée item par item : « Crises après 5–10 min d'effort » →
  `theorie`/Asthme d'effort « Timing : début 5-10 min exercice, pic 5-10 min post » ; « Régressent
  spontanément 20–60 min après » → `theorie` « Durée : résolution spontanée 20-90 min » (surensemble) ;
  « Prévention : salbutamol 15 min avant exercice » → `theorie`/Rappels thérapeutiques « Si AIE isolé :
  Salbutamol 2 bouffées 15min avant exercice » (plus précis, avec la posologie). Aucun item propre.
- presentation · Q3 « Suivi » : la réponse était une liste recopiant `theorie` (réévaluation à 3 mois,
  technique d'inhalation, paliers GINA). Réécrite en registre oral, contenu intégralement conservé et
  complétée du filet de sécurité de la page SSP.
  source : SSP — Prise en charge / Filet de sécurité — « Si vous crachez du sang, si vous êtes
  essoufflé·e au repos, si vous perdez du poids ou avez une fièvre prolongée, consultez rapidement. En
  cas de détresse respiratoire, appelez le 144. »

*Alignement des prises en charge sur la page SSP*

- resume · salbutamol : « Ventoline (salbutamol) » → « Salbutamol (Ventolin®) » (3 occurrences :
  Crise d'asthme, PEC en 3 points, Questions à poser où la marque disparaît au profit de la DCI).
  « Ventoline » est la marque française ; la spécialité suisse est **Ventolin®**. Même molécule, même
  posologie — alignement de dénomination, dans la lignée de la passe nomenclature des tâches 2 et 3.
  source : la page SSP n'emploie que la DCI (« salbutamol nébulisé 5 mg ») ; la forme de marque
  employée uniformément dans le vault est « Ventolin® » (Skills — Pulmonaire : « Salbutamol
  (Ventolin®), terbutaline (Bricanyl®) » ; SSP — Détresse Respiratoire : « Salbutamol (Ventolin®) 5 mg
  neb ×3 en 1 h »). Aucune occurrence de « Ventoline » dans le vault, aucune autre dans les 40 grilles.
- resume · signes de gravité de la crise : « tachypnée, cyanose, trouble conscience » → « tirage,
  cyanose, SpO₂ < 92 %, FR > 30/min, troubles de la conscience ». La tachypnée devient un seuil
  chiffré, la désaturation est ajoutée. Précision, non contradiction.
  source : **niveau 1** — SSP, Red flags — « **Détresse respiratoire aiguë** : tirage, cyanose,
  SaO2 < 92%, FR > 30/min → Asthme aigu grave… »
- resume · Crise d'asthme, item ajouté : « Détresse respiratoire aiguë : salbutamol 5 mg nébulisé
  ± ipratropium, oxygène et monitorage ». Le bloc ne connaissait que la voie inhalée par chambre
  (4-10 bouffées), adaptée à la crise légère à modérée ; la voie nébulisée de la détresse manquait.
  source : **niveau 1** — SSP, Red flags — « O2, monitoring, **salbutamol nébulisé 5 mg** ± ipratropium »
- resume · Examen physique : ajout de « Constantes et inspection : FR, SpO₂ à l'air ambiant, FC, TA,
  T° ; recherche de cyanose et de tirage ». La check-list « Examens à faire » demandait des constantes
  que le bloc canonique ne portait pas — l'axe 4 exige l'inverse (check-list ⊂ `resume`/Examen clinique).
  source : **niveau 1** — SSP, Examen clinique — « **Constantes & inspection** : FR, SpO₂ à l'air
  ambiant, FC, TA, T° ; cyanose, tirage, dyspnée »
- theorie · variabilité du débit de pointe : « variabilité > **20 %** sur 2 semaines » → « variabilité
  **diurne moyenne > 10 %** sur 2 semaines ». `resume`/Examens diagnostiques disait déjà « variabilité
  diurne > 10 % » : les deux blocs pédagogiques se contredisaient. Ce n'est pas un arbitrage de
  niveau 3 mais l'application du **contrat de blocs** — `resume` est la source canonique, `theorie`
  s'aligne sur elle. Les deux raisons convergent : le critère GINA actuel chez l'adulte est bien une
  variabilité diurne moyenne > 10 %, le 20 % relevant d'un critère plus ancien.
  source : contrat de blocs (`PROCEDURE.md` § 3, `resume` = source canonique) ; fix round 1/5

**Divergences consignées**

- pédagogique · palier 1 GINA : `theorie`/Traitement de l'asthme enseigne « **Palier 1 : SABA prn (si
  < 2×/semaine)** », schéma antérieur à la bascule GINA de 2019. Le schéma actuel ne reconnaît plus de
  palier SABA seul : le palier 1 est un **CSI-formotérol à la demande** (*anti-inflammatory reliever*),
  parce que le SABA seul laisse l'inflammation non traitée et augmente le risque d'exacerbation grave.
  La page SSP reste générique (« Corticostéroïde inhalé ± β2-agoniste si suspicion d'asthme ») et la
  section notée écrit un « • Palier 1 » **sans contenu** — elle n'affirme donc rien à quoi s'aligner.
  **Niveau 3** : laissé inchangé. Corriger supposerait de récrire le palier 1 dans `theorie` **et** de
  renseigner le sous-item vide de la section notée, donc de rouvrir le barème.
- section notée · absence de critère de prise en charge chiffré : la grille n'évalue que l'anamnèse,
  l'examen, les hypothèses, les examens et la communication ; aucun arbitrage de niveau 2 n'était
  possible sur le traitement.

**Paires de redondance restantes (5)**

Trois relèvent de la Q/R prescrite par l'axe 1 — `presentation` restitue à l'oral un sous-ensemble
strict de `resume` :

- « EFR : spirométrie avec test de réversibilité » (`resume`/Examens à faire) ↔ « Spirométrie avec test
  de réversibilité » (`presentation`/Q « Quels examens demanderiez-vous ? »).
- « Spirométrie avec test de réversibilité = examen clé » (`resume`/Points clés) ↔ idem.
- « Test de provocation (méthacholine) si diagnostic incertain » (`resume`) ↔ « Test de provocation à
  la méthacholine si besoin » (`presentation`/même Q).

Deux sont des faux positifs du comparateur :

- « Radiographie thoracique : Normale » (`expert`/Rôles — **résultat** à délivrer pendant la station)
  ↔ « Radiographie thoracique » (`presentation`/Q — **examen à demander**) : rôles de blocs opposés.
- « Hyperréactivité bronchique augmentée » (`theorie`/Cannabis et poumons — effet du cannabis) ↔
  « H = Hyperréactivité bronchique » (clé du mnémo ASTHME, protégée).

### AMBOSS-19 — Toux chronique, femme 53 ans, BPCO GOLD 3 avec cœur pulmonaire débutant (page SSP : Toux Chronique)

Redondance : 16 paires → 6 (`report_redundancy.py AMBOSS-19_`). Pas de sous-section
`presentation`/Pièges ECOS — vérifié, l'axe 6 ne s'applique pas.

**Modifications**

*Dédoublonnage (contrat de blocs, règle du format)*

- theorie · Manifestations cliniques BPCO : la section recopiait `resume`/Symptômes typiques et
  `resume`/Examen clinique (paires à 0.74 sur la toux matinale). Réécrite en *pourquoi le diagnostic se
  fait si tard* — le patient réduit son activité au rythme du déclin du VEMS, la toux matinale est
  attribuée au tabac par le patient comme par le médecin. Vérification item par item : toux matinale
  productive → `resume`/Symptômes typiques ; expectorations muqueuses à purulentes →
  `resume`/Exacerbation, triade ; dyspnée d'effort → `resume` ; temps expiratoire, sibilants, ronchi →
  `resume`/Examen clinique. Les deux items **propres** (phénotypes pink puffer / blue bloater,
  manifestations systémiques) sont conservés et enrichis. Ajout du piège inverse : un amaigrissement
  chez un fumeur de 70 PA n'est jamais « la BPCO » tant qu'un cancer n'est pas écarté.
- theorie · Diagnostic de la BPCO : liste d'examens recopiant `resume`/Examens diagnostiques et
  `expert`/Rôles (paire à **1.0** sur « Radiographie thorax : hyperinflation, aplatissement
  diaphragmes », 0.75 sur les gaz du sang, 0.74 sur la définition spirométrique). Réécrite en *ce que
  chaque examen apporte et ce qu'il n'apporte pas*. Anti-perte : « Test marche 6 min » et
  « α1-antitrypsine » n'existaient nulle part ailleurs sous cette forme — conservés dans la réécriture.
  Axe 1.
- theorie · BPCO, définition spirométrique : « VEMS/CVF < 0.70 post-bronchodilatateur » doublait
  `resume`/EFR. Remplacé par le *pourquoi* du seuil fixe (compromis qui sur-diagnostique après 70 ans
  et sous-diagnostique avant 45) et du post-bronchodilatateur (écarte l'asthme, dont l'obstruction se
  lève). L'item « Classification GOLD 1-4 selon VEMS » a été **porté d'abord** dans
  `resume`/Examens diagnostiques (« GOLD 1 léger > 80 %, GOLD 2 modéré 50–79 %, GOLD 3 sévère 30–49 %,
  GOLD 4 très sévère < 30 % ») et dans les libellés du tableau « GOLD staging » de `presentation`,
  **avant** d'être remplacé en `theorie` par le rationnel (le VEMS gradue l'obstruction mais prédit mal
  le handicap et les exacerbations).
- theorie · Traitement de la BPCO : liste doublant `resume`/Prise en charge. Réécrite en rationnel —
  l'arrêt du tabac ne restaure pas le VEMS mais ramène la pente du déclin à celle d'un non-fumeur ; les
  bronchodilatateurs agissent sur la distension dynamique, pas sur l'obstruction fixe ; l'oxygène de
  longue durée n'allonge la survie qu'à ≥ 15 h/j ; la réhabilitation casse la spirale dyspnée →
  sédentarité ; chaque exacerbation évitée est du VEMS préservé. Anti-perte : le seuil complet de
  l'oxygénothérapie (« ou < 60 avec polyglobulie ou cœur pulmonaire ») et l'indication complète des CSI
  (« si exacerbations fréquentes ou asthme associé, et si éosinophiles > 300/µL ») sont conservés. Axe 2.
- theorie · Arrêt du tabac, item « Approche 5A » : la liste des cinq A doublait le mnémo de
  `presentation`/Touches ludiques. Remplacée par le *pourquoi* d'une méthode structurée (le conseil bref
  seul obtient 2-3 % d'arrêts à un an ; la structure transforme une phrase en rendez-vous). Le mnémo
  conservé garde ses clés anglaises et reçoit la traduction en valeur — « Ask : demander le statut
  tabagique à chaque consultation », etc. — sur le modèle des glossaires de schéma.
- presentation · mnémo OLD COPS : la `mnemo-box` de la Checklist mentale est **déplacée** dans
  « Touches ludiques / mnémos » (axe 5), où elle **remplace** « BPCO = 3C ». Vérification item par item :
  « C = Crachats chroniques » → clé C (« Crachats matinaux chroniques ») ; « C = Clope (tabac) facteur
  principal » → clé L (« Longue histoire tabagique (la clope, facteur principal) ») ; « C = Capacité
  respiratoire ↓ (VEMS) » → clé O (« Obstruction bronchique (VEMS ↓, capacité respiratoire
  diminuée) »). 3C était un sous-ensemble strict d'OLD COPS.
- presentation · Q3 « Suivi » : la réponse était une liste recopiant `resume` et `expert`/Pièges (paire
  à 0.87 sur le dépistage du cancer pulmonaire). Réécrite en registre oral, contenu intégralement
  conservé, complétée du filet de sécurité de la page SSP.
- resume · Historique BPCO : « Vaccination : grippe, pneumocoque » → « Statut vaccinal : couverture
  OFSP à jour ? ». L'item est une **question d'anamnèse** ; la liste des vaccins vit dans
  `resume`/Mesures non pharmacologiques, canonique (paires à 1.0, 0.88, 0.86, 0.86, 0.79 et 0.73 —
  six des seize paires portaient sur la vaccination).

*Alignement des prises en charge sur la page SSP*

- resume · Points clés ECOS, item ajouté : « Toute toux chronique : réviser la liste médicamenteuse —
  l'IEC (ici lisinopril) est la cause iatrogène n° 1, à arrêter avec réévaluation à 4 semaines et
  relais par un sartan si HTA ». **La patiente prend du lisinopril** (critère noté d'anamnèse
  n° 7 : « Oui, je prends du lisinopril ») et **aucun** des quatre blocs pédagogiques ne mentionnait la
  toux sous IEC. C'est le piège éliminatoire de la page SSP.
  source : **niveau 1** — SSP, `pieges_eliminatoires` — « **Toux iatrogène (IEC) non dépistée** » ;
  Règle d'or — « Toujours **réviser les médicaments** (toux sèche sous IEC) » ; Points Clés ECOS / À
  faire absolument n° 2 — « Réviser la liste médicamenteuse — l'IEC est la cause iatrogène n°1 » ;
  Prise en charge / Approche empirique séquentielle n° 1 — « Arrêt d'un éventuel IEC → réévaluation à
  4 semaines (relais par un sartan si HTA) »
- expert · Pièges, item ajouté : « Ne pas relever le lisinopril : toux iatrogène sous IEC non
  dépistée » — versant examinateur du même point (axe 7 : `expert` = ce qui s'observe, `resume` = ce
  que l'étudiant retient).
  source : **niveau 1** — même citation
- resume · Check-list / Questions à poser, item ajouté : « Traitement antihypertenseur ? Un IEC peut
  donner une toux sèche même après des années ».
  source : **niveau 1** — SSP, Pièges — « Oublier les IEC comme cause de toux sèche chronique — TOUJOURS
  faire l'inventaire médicamenteux (incluant IEC pris depuis des années sans toux initiale) »
- resume · vaccinations : « Vaccination : grippe, pneumocoque, COVID, coqueluche, zona » →
  « Vaccinations OFSP : grippe annuelle, pneumocoque, COVID-19, dTpa (coqueluche), zona/varicelle selon
  le terrain ».
  source : **niveau 1** — SSP, Prise en charge / Surveillance & prévention — « **Vaccinations OFSP** :
  grippe annuelle, pneumocoque, COVID-19, dTpa, zona / varicelle selon le terrain »
- resume · antibiothérapie de l'exacerbation : « Antibiothérapie si critères : expectoration purulente,
  dyspnée + fièvre (ex : amox-clav) » → « Antibiothérapie si ≥ 2 des 3 critères d'Anthonisen
  (majoration de la dyspnée, du volume et de la purulence des expectorations), ou purulence isolée :
  co-amoxicilline (Co-Amoxi®) PO ». Deux corrections dans un même item : (a) la **fièvre n'est pas un
  critère d'Anthonisen** — le même bloc invoquait pourtant ces critères deux items plus haut
  (« Antibiotiques en cas d'exacerbation infectieuse (critères d'Anthonisen) »), l'item était donc en
  contradiction avec sa propre référence et élargissait indûment l'indication antibiotique ; (b) la
  dénomination.
  source : (b) **niveau 1** — SSP, Prise en charge / Surveillance & prévention — « **co-amoxicilline**
  si comorbidités (SSI/SSMI) » ; (a) ni la page SSP ni la section notée ne définissent les critères
  d'Anthonisen — correction de cohérence interne au bloc canonique, signalée à l'arbitrage.

**Divergences consignées**

- pédagogique et section notée · classification GOLD : `theorie`/Rappels thérapeutiques et la section
  notée raisonnent en **GOLD A/B/C/D** (« GOLD C/D: LABA + LAMA ± CSI »), alors que la page SSP renvoie
  à un pocketcard « **GOLD ABE** » — la révision 2023, qui fusionne C et D. La page SSP ne tranche pas
  explicitement (simple nom de pocketcard dans « Skills connexes ») ; **niveau 2** : la section notée
  fait foi, le pédagogique reste en A/B/C/D. Barème gelé, rien corrigé. À arbitrer.
- pédagogique · corticoïde de l'exacerbation : `resume` écrit « prednisolone 40 mg/j pendant 5 j »,
  `theorie`/Rappels thérapeutiques « prednisone 40 mg × 5 j ». Les deux molécules sont commercialisées
  en Suisse et les deux régimes sont équivalents ; ni la page SSP ni la section notée ne tranchent.
  **Niveau 3** : laissé inchangé.
- pédagogique · score mMRC : `resume`/Historique BPCO parle du « Score mMRC de dyspnée **au repos** »,
  alors que le mMRC gradue la dyspnée **à l'effort**. Ni la page SSP ni la section notée ne le
  mentionnent. **Niveau 3** : laissé inchangé, signalé.

**Paires de redondance restantes (6)**

Trois relèvent des Q/R prescrites par les axes 1 et 2 — `presentation` restitue à l'oral un
sous-ensemble strict de `resume` :

- « Oxygénothérapie à long terme si PaO2 < 55 mmHg » (`resume`/Formes sévères) ↔ « Oxygénothérapie si
  PaO2 < 55 mmHg » (`presentation`/Q2 « Traitement »).
- « Réhabilitation respiratoire (kiné, exercice) » (`resume`) ↔ « Réhabilitation respiratoire »
  (`presentation`/Q2).
- « Vaccinations (grippe, pneumocoque) à jour ? » (`resume`/Check-list — **question à poser**) ↔
  « Vaccination grippe + pneumocoque » (`presentation`/Q2 — **mesure à proposer**) : rôles distincts.

Deux portent sur des clés de mnémo, protégées :

- « Dyspnée d'effort progressive » (`resume`) ↔ « D = Dyspnée progressive » (mnémo OLD COPS).
- « Spirométrie indispensable au diagnostic » (`resume`/Points clés) ↔ « S = Spirométrie
  indispensable » (mnémo OLD COPS).

La dernière est un changement de format explicite :

- « Toux chronique productive (souvent matinale) » (`resume`) ↔ « Toux chronique productive > 5 ans »
  (`presentation`/Q1 — argument POUR d'une argumentation pour/contre).

### AMBOSS-31 — Toux et hémoptysie, homme 58 ans, cancer bronchopulmonaire probable (page SSP : Toux Chronique)

Redondance : 9 paires → 3 (`report_redundancy.py AMBOSS-31_`). Pas de sous-section
`presentation`/Pièges ECOS — vérifié, l'axe 6 ne s'applique pas. Le glossaire de schéma
(`UL : lobe supérieur ; ML : lobe moyen ; LL : lobe inférieur`) respecte déjà la règle clé-anglaise /
valeur-française : inchangé.

**Modifications**

*Dédoublonnage (contrat de blocs, règle du format)*

- theorie · Présentation clinique cancer poumon : la section recopiait `resume`/Symptômes respiratoires
  et systémiques (paire à 0.74 sur les symptômes B). Réécrite en *pourquoi ce cancer se révèle si tard,
  et par quoi* — le parenchyme n'a pas de sensibilité propre, la douleur signe déjà l'atteinte pleurale
  ou pariétale ; chez un fumeur qui tousse depuis des années, le signal n'est pas la toux mais son
  changement de caractère ; les syndromes paranéoplasiques précèdent parfois toute anomalie
  radiologique. **Tous les chiffres sont conservés** (toux 75 %, hémoptysie 30 %, perte de poids 50 %,
  douleur 25 %, hippocratisme 30 %), ainsi que les sites métastatiques et les deux complications de
  contiguïté. Axe 1.
- expert · Points clés : « Radiographie thoracique première urgence » doublait `resume`/Imagerie et
  `resume`/Examens à faire (paires à 0.77, 0.74 et 0.73 — quatre des neuf paires venaient de cet item).
  Réécrit du point de vue de l'examinateur, rôle propre du bloc (axe 7) : « Observer si le candidat
  demande l'imagerie d'emblée, sans la différer pour le coût ni attendre les résultats
  microbiologiques ». L'urgence de la radiographie reste portée par `resume`/Imagerie (1ʳᵉ intention),
  `resume`/Points clés et `presentation`/Q1 (« immédiate »).
- presentation · mnémo CANCER : la `mnemo-box` de la Checklist mentale est **déplacée** dans « Touches
  ludiques / mnémos » (axe 5), où elle **remplace** « Red flags toux chronique ». Vérification item par
  item avant absorption : « Hémoptysie » → clé C (« Crachat sanglant (hémoptysie) ») ;
  « Amaigrissement » → clé A ; « Sueurs nocturnes » → clé N (glose française ajoutée à la clé
  anglaise) ; « Changement de caractère d'une toux de fumeur » → clé C (« Cough (toux persistante, ou
  changement de caractère d'une toux de fumeur) ») ; « Hippocratisme digital » → porté en valeur de la
  clé C et déjà présent dans `resume`/Examen clinique, `expert`/Points clés et
  `theorie`/Hippocratisme digital.
- presentation · titre « ⚠️ Diagnostic différentiel toux chronique (4 grands) » → « ⚠️ Diagnostic
  différentiel **chez ce fumeur** (4 grands) ». Les quatre entrées (cancer, TB, BPCO/asthme,
  bronchectasies) sont justes pour ce cas mais ne sont pas le différentiel général de la toux
  chronique, que la page SSP tranche autrement (voir alignement ci-dessous). Les quatre entrées sont
  conservées telles quelles.
- presentation · Q3 « Suivi » : la réponse était une liste recopiant `resume`/Stratégie thérapeutique et
  Support symptomatique. Réécrite en registre oral, contenu intégralement conservé (stadification
  CT thoraco-abdomino-pelvien, PET-scan, échoendoscopie bronchique, colloque multidisciplinaire,
  chirurgie si localisé, chimio/immunothérapie, soins de support, surveillance).

*Alignement des prises en charge sur la page SSP*

- resume · Points clés ECOS, item ajouté : « Toux chronique (> 8 semaines) : chez le non-fumeur, penser
  d'abord UACS, asthme et RGO ; chez le fumeur, éliminer d'emblée cancer et tuberculose — et toujours
  réviser les médicaments, la toux sèche sous IEC étant la cause iatrogène n° 1 ». La grille ne
  connaissait que le différentiel du fumeur ; le cadre général de la page SSP manquait.
  source : **niveau 1** — SSP, En Bref — « **Top 3 causes** (adulte non-fumeur, immunocompétent) :
  UACS / écoulement post-nasal, asthme (incl. cough-variant), RGO » et « **Toujours éliminer** : cancer
  bronchique, tuberculose, IC gauche, embolie pulmonaire, toux iatrogène sous IEC » ; Règle d'or —
  « Toux > 8 semaines… Toujours **réviser les médicaments** (toux sèche sous IEC) »
- resume · antitussifs : « Antitussifs si toux invalidante » → « … — jamais avant la radiographie et le
  diagnostic, sous peine de masquer la tumeur ». Précision, non contradiction : l'antitussif reste
  indiqué en palliatif une fois le diagnostic posé.
  source : **niveau 1** — SSP, Pièges — « Prescrire un **antitussif** sans Rx ni diagnostic — risque de
  masquer un cancer broncho-pulmonaire chez fumeur »
- resume · symptômes systémiques : « Perte de poids, fatigue, fièvre » → « … , sueurs nocturnes ». Le
  bloc canonique ignorait les sueurs nocturnes, alors qu'elles sont le red flag tuberculeux de la page
  SSP et un symptôme majeur de ce patient.
  source : **niveau 1** — SSP, Red flags — « **Toux + fièvre prolongée + sueurs nocturnes +
  amaigrissement** ± contact / précarité / migration → Tuberculose pulmonaire »
- theorie · Examens complémentaires (queue), radiographie : « Radiographie thoracique face + profil :
  première intention » → « … premier examen, mais une radiographie normale n'exclut pas un cancer — les
  lésions centrales ou de petite taille lui échappent, et devant des red flags persistants on pousse
  jusqu'au scanner ». Le *pourquoi* remplace la redite (paire à 0.80 avec `resume`/Imagerie).
  source : **niveau 1** — SSP, Cartes ECOS — « attribuer la toux à la « bronchite chronique du fumeur ».
  Une **Rx normale n'exclut pas un cancer** — devant des red flags persistants, on pousse jusqu'au
  scanner » ; « **CT thoracique** même si la radio est normale »
- theorie · Examens complémentaires (queue), item ajouté : « PCR Xpert MTB/RIF sur les crachats :
  résultat en quelques heures, et détecte d'emblée la résistance à la rifampicine ». La queue ne
  connaissait que le Ziehl ×3, la culture et le QuantiFERON.
  source : **niveau 1** — SSP, Examens complémentaires / 2ᵉ ligne — « Suspicion de tuberculose :
  **crachats BAAR ×3 + PCR (Xpert MTB/RIF)**, IGRA (Quantiferon), isolement respiratoire »
- expert · Pièges, item ajouté : « Oublier la déclaration obligatoire à l'OFSP et l'enquête d'entourage
  si la TB est confirmée ». Aucun bloc pédagogique ne portait cette obligation, que la section notée
  exige pourtant (« Si tuberculose pulmonaire confirmée · Déclaration obligatoire, enquête entourage »).
  source : **niveau 1** — SSP, Examens complémentaires / 2ᵉ ligne — « **déclaration obligatoire à
  l'OFSP** » ; confirmé au **niveau 2** par la section notée
- theorie · Rappels thérapeutiques, item ajouté : « Vitamine B6 (pyridoxine) associée à l'isoniazide :
  prophylaxie de la neuropathie périphérique ». Le bloc donnait les quatre molécules du RIPE et leurs
  doses **sans la pyridoxine**, que la section notée exige (« Vitamine B6 prophylaxie neuropathie »).
  Omission à conséquence clinique : l'isoniazide sans pyridoxine expose à une neuropathie périphérique.
  source : **niveau 2** — section notée, Management / Conseil et soutien, « Si tuberculose pulmonaire
  confirmée » — « Vitamine B6 prophylaxie neuropathie »

**Divergences consignées**

- pédagogique · dépistage du cancer pulmonaire : `theorie`/Cancer du poumon enseigne « Dépistage : CT
  faible dose si **55-80 ans + 30 PA** », critère américain du NLST repris par l'USPSTF en 2013 et
  **abaissé à 50-80 ans + 20 PA en 2021**. Surtout, la Suisse n'a **pas** de programme de dépistage
  organisé du cancer pulmonaire. La page SSP ne mentionne aucun dépistage et la section notée non plus.
  **Niveau 3** : laissé inchangé, rien inventé. À arbitrer par l'utilisateur.
- `expert`/Rôles · unités : « FSC : Hb 11.2 g/dL » — l'hémoglobine se rend en g/L dans les laboratoires
  suisses (112 g/L). Hors périmètre de la passe nomenclature (seul `mg/dL` était banni) et hors
  périmètre de cette tâche ; signalé, non corrigé, pour ne pas désaligner cette grille du reste du
  corpus.

**Paires de redondance restantes (3)**

- « Toux chronique ± hémoptysie » (`resume`/Symptômes respiratoires) ↔ « Toux chronique > 3 sem avec
  hémoptysie » (`presentation`/Q2 « Tuberculose pulmonaire », argument POUR) : liste de symptômes →
  argument d'une argumentation pour/contre, changement de format.
- « Radiographie thoracique » (`resume`/Examens à faire) ↔ « Radiographie thoracique (immédiate) »
  (`presentation`/Q « Quels examens demander ? ») : axe 1, Q/R en sous-ensemble strict.
- « Radiographie thoracique (1ère intention) » (`resume`/Imagerie) ↔ idem : axe 1.

### Passe unités SI — `g/dL` et `ng/mL` (fix round 1/5 de la tâche 7)

Née de l'observation n° 7 du rapport de tâche 7 : l'hémoglobine d'AMBOSS-31 était rendue en `g/dL`.
Le manque dépassait cette grille — les passes de nomenclature des tâches 2 et 3 n'avaient banni que
`mg/dL`. Balayage du corpus entier : **12 occurrences de `g/dL`** (grilles 6, 8, 11, 15, 16, 17, 27,
31) et **8 de `ng/mL`** (grilles 12, 14, 15, 25), soit 20 conversions.

**Modifications**

Chaque analyte a reçu son facteur propre — il n'y a pas de conversion mécanique d'unité :

- **Hémoglobine · `g/dL` → `g/L`, × 10.** 12 valeurs, dont deux **dans une section notée**
  d'AMBOSS-11 (le bullet « Transfusion si Hb: 7 g/dL ou instabilité » et la description de red flag
  « Hb < 7 g/dL »). Remplacement 1 pour 1 de texte, aucun sous-item ajouté ni retiré —
  `check_invariants.py` reste vert. AMBOSS-11 portait aussi « Transfusion si Hb < 7 g/dL (**< 9** si
  coronarien) » : les **deux** valeurs ont été converties (< 70 g/L, < 90 si coronarien), la seconde
  étant implicitement en g/dL.
  source : le vault écrit uniformément g/L — « Hb < 70 g/L », « Hb transfusion ≥ 70 g/L »,
  « Hb F < 120 / H < 130 g/L » ; aucune occurrence de g/dL.
- **Troponine T · `ng/mL` → `ng/L`, × 1000.** 3 valeurs : AMBOSS-12 (0.08 → 80), AMBOSS-14 (0.02 → 20
  et 0.15 → 150). C'est la seule conversion qui déplace la virgule ; la convention suisse pour la
  troponine hypersensible est le ng/L, comme le vault le fait déjà pour les peptides natriurétiques
  (Skills — Cardiovasculaire : « BNP ≥ 35 ng/L ou NT-proBNP ≥ 125 ng/L »).
- **D-dimères et ferritine · `ng/mL` → `µg/L`, × 1.** 5 valeurs (D-dimères : 2850, 850, deux seuils à
  500 ; ferritine : 8). 1 ng/mL = 1 µg/L **exactement** : les nombres sont inchangés, seule la
  notation devient SI. Ce choix préserve deux choses que le passage en mg/L FEU aurait cassées : le
  seuil 500 tel que le vault l'écrit (Skills — Références Rapides : « D-dimères | < 500 ng/mL ») et la
  **règle âge-ajustée « âge × 10 »**, qui n'est définie qu'en µg/L (SSP — Dyspnée : « seuil ajusté
  (âge × 10 ng/mL si > 50 ans) »).
  source : ferritine — le vault écrit µg/L (7 occurrences, aucune en ng/mL).

`\bg/dL\b` et `\bng/mL\b` sont ajoutés à la table `BANNED` de `check_nomenclature.py`, avec le facteur
par analyte en commentaire, pour que le manque ne se reforme pas. Les deux motifs sont bordés : dans
`mg/dL` comme dans `ng/dL` il n'y a pas de frontière de mot avant le `g`, et `ng/mL` n'est sous-chaîne
ni de `pg/mL` ni de `U/mL` — vérifié par test avant activation, aucun faux positif sur le corpus.

**Divergences consignées**

- vault · D-dimères : après cette passe les grilles écrivent `µg/L` là où le vault écrit encore
  `ng/mL` (Skills — Références Rapides, SSP — Dyspnée). Les **nombres sont identiques**, seule la
  notation diffère ; c'est le vault qui gagnerait à s'aligner. Signalé, rien changé dans le vault.
- pédagogique · `pg/mL` restant, 4 occurrences hors périmètre de cette passe : vitamine B12
  (AMBOSS-17 « 320 pg/mL », AMBOSS-20 « 85 pg/mL (N: 200-900) ») — les laboratoires suisses rendent en
  **pmol/L** (× 0,738) ; BNP (AMBOSS-19 « 85 pg/mL ») — à rendre en **ng/L**, × 1, comme le vault.
- pédagogique · `/mm³` restant, 5 occurrences hors périmètre : leucocytes et plaquettes (AMBOSS-2, 8,
  24) — les laboratoires suisses rendent en **G/L** (10⁹/L), × 0,001.
- pédagogique · troponine T d'AMBOSS-14, après conversion : le bloc lit désormais « Troponine T
  initiale : 20 ng/L (limite normale) ». Le nombre est fidèle, mais **la conversion a déplacé le
  référentiel implicite du scénario** — en Suisse, `ng/L` connote un dosage **hypersensible**, dont le
  99ᵉ percentile est à ≈ 14 ng/L ; `ng/mL` connotait au contraire un dosage conventionnel, dont le
  seuil tournait autour de 0,03 ng/mL. Sous dosage hs, 20 ng/L n'est plus « limite normale » mais déjà
  au-dessus du seuil. La dynamique du cas reste cohérente dans les deux lectures (20 → 150, soit une
  ascension nette qui signe la nécrose) ; seul le **qualificatif** devient discutable. Trancher
  supposerait de décider quel dosage le scénario emploie — un choix d'auteur, pas de conversion.
  **Niveau 3** : qualificatifs laissés intacts, la conversion est restée 1 pour 1. À arbitrer par
  l'utilisateur : soit remplacer « limite normale » par « discrètement élevée » (lecture hs), soit
  ramener la valeur initiale sous 14 ng/L.

**Garde-fou — `mg/mL` d'AMBOSS-18 : ne jamais le bannir**

Les deux occurrences (« Test méthacholine : Positif (PC20 = 4 mg/mL) » dans `expert`/Rôles,
« Test méthacholine : PC20 < 8 mg/mL » dans `theorie`) désignent la **concentration de méthacholine
inhalée** lors du test de provocation bronchique. `mg/mL` en est l'unité internationale correcte : ce
n'est pas un résultat rendu par un automate de laboratoire, il n'y a rien à convertir en SI. Ajouter
`\bmg/mL\b` à `BANNED` corromprait le seuil diagnostique de l'asthme. La règle générale, désormais
écrite dans `PROCEDURE.md` § 6 et en commentaire dans `check_nomenclature.py` juste à côté de la table
`BANNED` — là où une passe future irait l'ajouter — est que **les règles d'unités SI ne visent que les
résultats de laboratoire, jamais les posologies ni les concentrations administrées** (mg/kg,
µg/bouffée, mg/mL).

### Passe unités SI — `pg/mL` et `/mm³` (fix round 2/5 de la tâche 7)

Complète la passe précédente sur les deux unités restantes identifiées au rapport de round 1.
Balayage du corpus : **4 occurrences de `pg/mL`** (grilles 17, 19, 20) et **5 de `/mm³`** (grilles 2,
8, 24), soit 9 conversions. Après cette passe, **aucune occurrence** de `g/dL`, `ng/mL`, `pg/mL` ni
`/mm³` ne subsiste dans le texte des 40 grilles.

**Modifications**

- **Vitamine B12 · `pg/mL` → `pmol/L`, × 0,738.** 3 valeurs. AMBOSS-17 : 320 → **236 pmol/L**,
  qualificatif « (normale) » vérifié — l'intervalle suisse est d'environ 145-570 pmol/L, 236 y est
  bien. AMBOSS-20 : la valeur **et son intervalle de référence** ont été convertis ensemble, 85 →
  **63 pmol/L** et « N: 200-900 » → **« N: 148-664 »** (200 × 0,738 = 147,6 ; 900 × 0,738 = 664,2) ;
  ne convertir que la valeur aurait fait passer un déficit franc pour une normale. AMBOSS-20, queue de
  `theorie` : « < 200 pg/mL = déficit » → **« < 148 pmol/L = déficit »**, même borne que celle de
  l'intervalle ci-dessus — la cohérence interne de la grille est préservée, et 63 reste bien sous 148.
- **BNP · `pg/mL` → `ng/L`, × 1.** AMBOSS-19 : 85 pg/mL → **85 ng/L**, nombre inchangé. Qualificatif
  « (légèrement élevé) » vérifié : le seuil d'insuffisance cardiaque du vault est « BNP ≥ 35 ng/L », 85
  est donc bien une élévation modérée.
  source : Skills — Cardiovasculaire — « **BNP ≥ 35 ng/L** ou **NT-proBNP ≥ 125 ng/L** »
- **Leucocytes et plaquettes · `/mm³` → `G/L`, × 0,001.** 5 valeurs, dont **deux dans une section
  notée** d'AMBOSS-24 (réponse patient du sous-item noté « FSC »). Qualificatifs vérifiés un à un :
  AMBOSS-2 « leucocytose à 14 000/mm³ » → **14 G/L**, au-dessus de la norme 4-10 G/L, le mot
  « leucocytose » reste exact ; AMBOSS-8 « leucocytes 12 000/mm³ » → **12 G/L** ; AMBOSS-24
  « plaquettes < 150 000/mm³ » → **< 150 G/L**, seuil de thrombopénie conservé, et « leucocytes
  > 10 000/mm³ » → **> 10 G/L** ; AMBOSS-24 « Plaquettes 180 000/mm³ (normale) » → **180 G/L**, dans
  la norme 150-400 G/L, qualificatif exact.

`\bpg/mL\b` et `/mm³` sont ajoutés à `BANNED`, portant à quatre les motifs d'unités de la table. La
barre oblique de `/mm³` est indispensable : elle borne le sens « par mm³ » (une concentration) et
laisse passer un volume écrit « 5 mm³ », qui est légitime. Bordage vérifié avant activation : aucun
des deux motifs n'attrape `ng/mL`, `mg/mL`, `U/mL`, `mm/h` ni un volume en mm³.

**Divergences consignées**

- pédagogique · **numérations sans unité**, 3 occurrences hors de portée de tout motif : AMBOSS-18
  « FSC : GB 8500 », AMBOSS-31 « leucocytes 12 000 », AMBOSS-33 « GB 15 000 ». Elles sont
  implicitement en /mm³ et devraient se lire 8,5 G/L, 12 G/L et 15 G/L. Aucun motif de `BANNED` ne
  peut les détecter — il n'y a pas d'unité à chercher. Signalées, **non converties** : les corriger
  demande une lecture au cas par cas, et rien ne garantit qu'il n'en existe pas d'autres formes. À
  traiter par une passe dédiée si l'utilisateur le souhaite.

### Passe unités SI — numérations en unité implicite (fix round 3/5 de la tâche 7)

Dernier volet de la passe unités. Les trois numérations sanguines écrites **sans unité du tout**,
signalées au round 2 comme hors de portée de tout motif, sont converties. Recherche d'exhaustivité
menée indépendamment sur les 40 grilles (tout nombre ≥ 1000 au voisinage d'un terme d'hémogramme :
GB, globules blancs, leucocytes, plaquettes, thrombocytes, PNN, neutrophiles, lymphocytes,
éosinophiles) : elle ne donne que ces trois-là.

**Modifications**

- **Leucocytes · unité implicite `/mm³` → `G/L`, × 0,001.** 3 valeurs, toutes dans `expert`/Rôles et
  interventions (données de station à délivrer au candidat) :
  - AMBOSS-18 : « FSC : GB 8500, éosinophiles 6% » → « FSC : **GB 8.5 G/L**, éosinophiles 6% ».
    8,5 G/L est **normal** (norme 4-10 G/L), ce qui est cohérent avec une station d'asthme sans
    infection bactérienne. Le « 6% » qui suit est un **pourcentage de formule**, pas une numération :
    laissé intact. Il reste d'ailleurs interprétable — 6 % de 8,5 G/L font 0,51 G/L d'éosinophiles,
    au-dessus du seuil d'éosinophilie, ce que la grille enseigne comme argument de terrain atopique.
  - AMBOSS-31 : « FSC : Hb 112 g/L, leucocytes 12 000 » → « … **leucocytes 12 G/L** ». 12 G/L est
    au-dessus de la norme, l'élévation modérée du cas est conservée.
  - AMBOSS-33 : « FSC : GB 15 000, plaquettes normales » → « FSC : **GB 15 G/L**, plaquettes
    normales ». 15 G/L reste franchement lisible comme une **hyperleucocytose**, attendue dans une
    hémorragie sous-arachnoïdienne (leucocytose de stress).

Aucune des trois n'est dans une section notée. Après ce round, **plus aucune valeur de laboratoire du
corpus n'est rendue en unité non suisse ni en unité implicite**.

**Vérifications de cohabitation `g/L` / `G/L`**

Deux lignes portent désormais les deux notations : AMBOSS-8 et AMBOSS-31, toutes deux
« FSC : Hb 112 g/L, leucocytes 12 G/L ». Vérifié : c'est la convention du vault, qui écrit `G/L` sans
glose et fait cohabiter les deux notations sur une même ligne (« plaquettes ≤ 100 G/L » à côté de
« fibrinogène < 1.5 g/L »). Aucune glose ajoutée — en ajouter divergerait de la source. La casse seule
distingue les deux unités, et les libellés (`Hb` vs `leucocytes`) lèvent toute ambiguïté résiduelle.
Le cas d'AMBOSS-8 date du round 2 et n'avait pas été signalé alors : il l'est ici.

**Divergences consignées**

- `expert`/Rôles d'AMBOSS-33 · **numération de LCR, à ne pas convertir** : « PL (si faite) : GR 50 000,
  xanthochromie présente ». C'est un compte d'**érythrocytes dans le liquide céphalorachidien**, rendu
  conventionnellement par µL (ou ×10⁶/L), **jamais en G/L** — l'unité G/L est celle de l'hémogramme.
  Hors périmètre de la recherche d'exhaustivité, qui portait sur les termes d'hémogramme. Signalé,
  **non converti** ; à traiter éditorialement avec le reste d'AMBOSS-33 si l'utilisateur le souhaite.

**Garde-fou — un angle mort qui ne peut pas être automatisé**

`check_nomenclature.py` cherche des unités ; une valeur écrite sans unité lui échappe **par
construction**. Aucun motif de `BANNED` ne peut détecter « GB 8500 » : il n'y a rien à chercher. La
règle est donc écrite dans `PROCEDURE.md` § 6 avec le résultat daté de la recherche exhaustive, et
avec sa limite : le corpus est propre à cette date, mais rien ne le maintiendra propre — toute grille
nouvelle, réécrite ou réimportée doit être relue à la main sur ce point.

### AMBOSS-4 — Saignements vaginaux, femme 50 ans, post-ménopause (page SSP : Saignement Vaginal Anormal)

Redondance : **13 paires → 1** (`report_redundancy.py AMBOSS-4_`). Quatre blocs présents.
Vérifié : cette grille **n'a pas** de sous-section `presentation`/Pièges ECOS — l'axe 6 ne
s'y applique pas (relecture directe du bloc `presentation`, confirmée par `seg.count`).

**Modifications**

*Alignements sur une autorité*

- resume · Dépistage 🎗️ Cancer du col : « Dès 25 ans **en France** (tous les 3 à 5 ans selon le test
  utilisé) » → « **Femmes 30-65 ans : frottis tous les 3 ans OU frottis + test HPV tous les 5 ans** ».
  **Niveau 2** : la page SSP ne fixe pas d'âge de dépistage ; la section notée le fixe, et le
  pédagogique la contredisait (25 ans vs 30-65 ans) tout en citant un référentiel national qui n'est
  pas la Suisse.
  source : section notée `m2` — critère « Frottis cervical et test HPV » — « Femmes 30-65 ans :
  frottis tous les 3 ans OU frottis + HPV tous les 5 ans »
  Vérifié après coup qu'aucun autre bloc ne porte l'ancienne formule : `theorie`/queue dit
  « Co-testing (frottis + HPV) : Stratégie optimale 30-65 ans » — cohérent.
- theorie · Saignements post-ménopausiques, épidémiologie : « Causes malignes dans **5-10 %** des
  cas » et « Causes bénignes : atrophie (**50 %**), polypes (**10-30 %**) » → « Cancer de l'endomètre :
  **10-15 %** des saignements post-ménopausiques, cause maligne la plus fréquente — à exclure en
  premier » et « Causes bénignes : atrophie (**60 %**), polypes (**20 %**), hyperplasie ». **Niveau 1.**
  source : SSP — DIAGNOSTIC DIFFÉRENTIEL, ligne « Post-ménopause » — « Atrophie (60 %), polypes
  (20 %), cancer de l'endomètre (10-15 %) »
- theorie · Saignements post-ménopausiques, item ajouté : « L'atrophie est la cause la plus fréquente,
  mais c'est un diagnostic d'élimination — jamais retenu en première intention ». **Niveau 1**, et
  correction de l'erreur factuelle décrite plus bas.
  source : SSP — Cartes ECOS, « Saignement post-ménopause » — « l'atrophie endométriale est la cause
  la plus fréquente — mais c'est un diagnostic d'élimination, jamais un diagnostic de première
  intention »

*Erreurs factuelles corrigées directement (pas d'arbitrage : aucune autre source ne les portait)*

- presentation · Touches ludiques, sous-section « Tout saignement post-ménopausique = CANCER » :
  l'item « Polype ou atrophie **plus rares** mais jamais à évoquer en premier » était **faux sur la
  fréquence** — l'atrophie est la cause la plus fréquente (60 %), pas une cause rare. L'information
  correcte (fréquence élevée + statut de diagnostic d'élimination) a été portée dans `theorie` **avant**
  la suppression de la sous-section (voir ci-dessous).
- presentation · Q3 « Suivi » : l'item « **Dépistage HPV pour partenaires** » a été retiré. Il n'existe
  pas de test HPV validé ni recommandé pour le partenaire masculin ; aucune source du dossier ne le
  porte, et la section notée prescrit au contraire préservatifs + vaccination. Remplacé, dans la
  réponse orale, par le contenu de la section notée.
  source : section notée `m5` — « Pratiques sexuelles sûres : Préservatifs systématiques »,
  « Vaccination HPV jusqu'à 45 ans : (rattrapage possible) », « Dépistage régulier : Frottis + HPV
  tous les 3-5 ans »
- presentation · Version longue : « la première fois que cela se produit depuis deux ans, **date de sa
  ménopause** » → « … **date de ses dernières règles** ». Le même paragraphe indiquait deux phrases
  plus loin « sa ménopause est survenue à 45 ans » : le bloc se contredisait lui-même. La formule
  retenue est celle de la section notée (« Dernières règles [Il y a 2 ans] »).

*Dédoublonnage (contrat de blocs, règle du format)*

- theorie · « Approche diagnostique systématique » → **« Pourquoi cette séquence diagnostique »**. La
  liste des cinq examens (examen pelvien, frottis + HPV, US transvaginale, biopsie, hystéroscopie)
  redisait `resume`/Examens diagnostiques au même format. Remplacée par le rationnel : l'échographie
  comme test de **tri** (8 mm ici, donc biopsie obligatoire), l'histologie seule décisive même si
  l'endomètre paraît fin, le col visualisé d'abord, et le parallélisme des deux voies (cervicale /
  endométriale). Axe 1. Anti-perte vérifiée item par item : les cinq examens figurent dans
  `resume`/Examens diagnostiques et `resume`/Examens à faire ; le seuil de 4 mm est conservé dans
  `theorie`/queue (« Endomètre < 4mm exclut cancer dans 99 % des cas »).
  source : SSP — Cartes ECOS — « seule l'histologie tranche ; l'échographie endovaginale sert de tri
  (endomètre > 4-5 mm → hystéroscopie), mais un saignement récidivant impose l'histologie même si
  l'endomètre paraît fin »
- theorie · Rappels thérapeutiques (section de queue, conservée) : le protocole recopiait
  `resume`/Traitement selon le stade et `resume`/Chirurgie. Remplacé par le rationnel — pourquoi le
  geste dépend de la profondeur d'invasion et non du volume, pourquoi la radiochimiothérapie remplace
  la chirurgie au stade localement avancé, pourquoi l'annexectomie complète l'hystérectomie
  (site métastatique + source œstrogénique), pourquoi la vaccination ne dispense ni du préservatif ni
  du dépistage, pourquoi le tabac agit sur la progression et pas seulement sur l'incidence. Axe 2.
  Précisions reprises **mot pour mot** de la section notée `m5` : conisation de la zone de
  transformation, hystérectomie radicale + lymphadénectomie, trachélectomie si désir de fertilité
  (IA2-IB1), radiothérapie externe + curiethérapie, rattrapage HPV jusqu'à 45 ans.
- theorie · Cancer de l'endomètre : item « Saignement post-ménopausique : symptôme cardinal »
  supprimé — doublon strict de `resume`/Symptômes fréquents (« Métrorragies post-ménopausiques
  (symptôme principal) »), même format. Axe 1 / règle du format.
- presentation · mnémo **POST** : la `mnemo-box` de la Checklist mentale est **déplacée** vers Touches
  ludiques, où elle remplace la sous-section « Tout saignement post-ménopausique = CANCER » dont les
  trois items la doublaient (P = Post-ménopause, O = Oncologie en premier). La Checklist mentale
  redevient une trame pure (axe 5). Clés P/O/S/T intactes, valeurs francisées : « S = Speculum exam
  obligatoire » → « S = Spéculum : visualisation du col obligatoire » ; « T = Transvaginal US +
  biopsie » → « T = Transvaginale (échographie) + biopsie de l'endomètre ».
- presentation · « 2. Examens complémentaires immédiats », Q1 : la liste de sept examens est réécrite
  en registre parlé (`presentation-reponse text`). Une liste recopiée sous un en-tête Q/R n'est pas un
  changement de format. Les sept items sont tous repris dans la réponse orale. Axe 1.
- presentation · « 3. … », Q2 « Traitement » : liste → réponse orale. Le point clé est explicité —
  il n'y a pas de traitement à ce stade, la priorité est l'histologie, la décision revient à la RCP.
  Axe 2.
- presentation · « 3. … », Q3 « Suivi » : liste → réponse orale (voir aussi la correction factuelle
  ci-dessus).

*Différenciation `expert` / `resume` (axe 7)*

- expert · Points clés : « Tout saignement post-ménopausique = cancer jusqu'à preuve du contraire »
  → « **Attendu du candidat** : nommer d'emblée le cancer devant ce saignement post-ménopausique et
  proposer hystéroscopie + biopsie — l'omission de l'histologie est éliminatoire ». `expert` dit
  désormais ce que l'**examinateur observe** ; `resume`/Points clés garde l'énoncé que l'étudiant
  retient.
  source : SSP — frontmatter `pieges_eliminatoires` — « Saignement post-ménopause sans hystéroscopie
  + biopsie »

*Anti-perte — informations portées dans le canonique*

- resume · Examens clés 🎗️ Cancer de l'endomètre : ajout de « FSC : retentissement hématologique du
  saignement (anémie ferriprive) ». La FSC n'existait que dans la liste Q/R de `presentation` que ce
  travail réécrit ; elle est exigée par la section notée et par la SSP.
  source : SSP — EXAMENS COMPLÉMENTAIRES — « FSC (anémie), fer / ferritine (carence martiale) » ;
  section notée `m2` — « FSC [pour évaluer une anémie] »
- resume · Inspection et palpation 🎗️ Cancer du col : ajout de « Constantes vitales, état général et
  recherche d'un épanchement (ascite, pleural) dans les formes avancées ». Ces deux éléments
  n'existaient que dans la check-list rapide ; l'axe 4 demande que la check-list soit un sous-ensemble
  strict de `resume`/Examen clinique — c'est le canonique qui les reçoit, pas la check-list qui les perd.
  source : SSP — Points Clés ECOS n° 4 — « Évaluer le retentissement (signes vitaux, pâleur, anémie,
  choc) »

**β-hCG — vérification explicite, aucune modification**

La patiente est **ménopausée depuis plus de 12 mois** (dernières règles il y a 2 ans, âge 50 ans) :
elle n'est pas « en âge de procréer » au sens de la règle d'or de la page SSP, dont la ligne
« Post-ménopause » du tableau de DD porte un tout autre drapeau (« Tout saignement = cancer jusqu'à
preuve du contraire »). La réponse type de la section notée le dit elle-même : « Par définition, si
vous n'avez pas eu de règles pendant 12 mois, vous êtes en ménopause ». **Aucun β-hCG n'est donc
ajouté** — l'ajouter serait une erreur d'orientation, pas une sécurité.

**Divergences consignées**

- section notée `a12` · **âge de la ménopause incohérent** : le critère porte simultanément
  « Dernières règles [Il y a 2 ans] » (soit ménopause à 48 ans) et « Âge de la ménopause [45 ans] ».
  Les deux valeurs ne peuvent pas être vraies ensemble. Divergence **interne à une section notée** :
  consignée, **non corrigée** (barème gelé). Le pédagogique a été rendu cohérent avec la première
  formulation, qui est celle du scénario de la patiente standardisée (« Premier épisode en 2 ans »).
  À trancher éditorialement si l'utilisateur souhaite unifier.
- resume · **paire de redondance restante (1)** : `resume`/Facteurs de risque « Absence de dépistage
  (frottis) » ↔ `presentation`/Q1 Arguments POUR « Absence de dépistage » (0,83). Conservée :
  changement de format légitime — liste de facteurs de risque → **argumentation pour/contre** devant
  une question d'examinateur, qui est la raison d'être du bloc `presentation`.

---

### AMBOSS-5 — Nausées, femme 19 ans, grossesse précoce sur implant (page SSP : Nausées, Vomissements & Hématémèse)

Redondance : **3 paires → 1** (`report_redundancy.py AMBOSS-5_`). Quatre blocs présents.
Grille de l'axe 6 : `presentation`/Pièges ECOS supprimée après report intégral dans `expert`/Pièges.

**Modifications**

*Alignements sur une autorité — sécurité*

- resume · Cas sévères (hyperémèse) : **ajout** de « **Thiamine (vitamine B1) 100 mg IM/IV AVANT tout
  apport glucosé** — sinon risque d'encéphalopathie de Gayet-Wernicke ». **Niveau 1** : la page SSP
  ajoute une mise en garde que la section notée ne porte qu'en partie (elle prescrit la thiamine mais
  pas l'antériorité par rapport au glucose, qui est tout l'enjeu). La section notée reste intacte.
  source : SSP — Cartes ECOS, « Femme en âge de procréer qui vomit » — « supplémenter en thiamine (B1)
  **AVANT tout apport glucosé** → sinon risque d'encéphalopathie de Gayet-Wernicke » ; posologie de la
  section notée `m5` — « Supplémentation : Thiamine (B1) 100 mg IM/IV »
- resume · Traitement médicamenteux : « Alternatives : métoclopramide, ondansétron (2e ligne) » →
  « Alternatives : métoclopramide, **puis** ondansétron (2e ligne, **avec prudence au 1er trimestre**) ».
  **Niveau 1**, précision ajoutée par la page SSP.
  source : SSP — PRISE EN CHARGE, Antiémétiques — « Grossesse : doxylamine + pyridoxine (vitamine B6)
  en 1ʳᵉ ligne, puis métoclopramide ; **ondansétron au T1 avec prudence** »

*Dédoublonnage (contrat de blocs, règle du format)*

- presentation · **Pièges ECOS supprimée** (axe 6). Anti-perte vérifiée item par item **avant**
  suppression, deux items ont dû être portés dans `expert`/Pièges :
  - « Croire à tort que l'implant contraceptif exclut une grossesse » → `expert` disait seulement
    « Se fier uniquement à la contraception par implant » ; l'item devient « Se fier uniquement à la
    contraception par implant, **en croyant à tort qu'il exclut une grossesse** ».
  - « Ne pas proposer de test de grossesse **chez une femme en âge de procréer** » → `expert` disait
    « Ne pas faire de test de grossesse systématique » ; l'item devient « … **chez toute femme en âge
    de procréer — piège éliminatoire** ». C'est la formulation de la règle d'or de la page SSP.
    source : SSP — Pièges — « Oublier β-HCG chez toute femme en âge de procréer » ; frontmatter
    `pieges_eliminatoires` — « Pas de β-hCG/glycémie/Na/K »
  - « Ignorer le vécu psychologique d'une grossesse imprévue » → `expert`/« Mauvaise gestion du déni de
    grossesse » devient « Mauvaise gestion du déni de grossesse **et du vécu psychologique d'une
    grossesse imprévue** ».
  - « Oublier d'exclure GEU ou MIP » : déjà présent à l'identique dans `expert`/Pièges, rien à porter.
- presentation · mnémo **PREGNANT** : la `mnemo-box` de la Checklist mentale est **déplacée** vers
  Touches ludiques, où elle **absorbe** la sous-section « Grossesse précoce = les 3N » — dont les trois
  items (Nausées, No rules/aménorrhée, Nycturie/pollakiurie) sont strictement inclus dans PREGNANT
  (N, R + A, P). Précédent AMBOSS-2 (APPENDIX ⊃ les 3A). Les huit clés restent intactes ; la valeur de
  P absorbe la nycturie. La Checklist mentale redevient une trame pure (axe 5).
  Valeurs anglophones francisées selon la règle des glossaires (clé conservée, traduction en valeur) :
  « G = GI symptoms (nausées, vomissements) » → « G = **Gastro-intestinal** : nausées et vomissements » ;
  « N = Nipple/breast changes » → « N = **Nipple (sein)** : sensibilité mammaire, parfois absente au
  début ». Même règle appliquée au mnémo RISK : « S = Surgery tubaire » → « S = **Surgery : chirurgie
  tubaire** ».
- theorie · queue Examens complémentaires : « FSC, ionogramme si vomissements importants » était le
  **doublon exact** (ratio 1,00) de la liste Q/R de `presentation`. La liste part de `presentation`
  (réécrite en oral) et l'item de `theorie` reçoit le *pourquoi* qui lui manquait : « hyponatrémie et
  hypokaliémie de déplétion signent la sévérité — avec la cétonurie et la perte de poids ≥ 5 %, ce
  sont elles qui font poser l'hospitalisation ». Axe 1.
  source : section notée `m5` — « Hospitalisation si perte poids 5 % ou cétonurie »
- presentation · « 2. Examens complémentaires immédiats », Q1 : liste → réponse orale. Les cinq items
  sont repris dans la réponse. Axe 1.
- presentation · « 3. … », Q2 « Traitement » : liste → réponse orale. Axe 2. La formulation retenue est
  celle de la page SSP (« doxylamine + pyridoxine en première intention »).

*Anti-perte — information portée dans le canonique*

- resume · Check-list rapide, Examens à faire : ajout de « **β-hCG urinaire ou plasmatique en premier**
  (règle d'or chez toute femme en âge de procréer) », en tête de liste. La check-list de la grille
  omettait l'examen qui fait le diagnostic, alors qu'il figure dans `resume`/Examens de confirmation et
  dans `resume`/Points clés.
  source : SSP — Règle d'or — « β-hCG chez toute femme en âge de procréer »

**β-hCG — vérification explicite**

Présent et central dans les quatre blocs avant intervention (`resume`/Points clés, `expert`/Points
clés et Rôles, `theorie`/DD et queue, `presentation`/mnémo PREGNANT « T = Test β-hCG systématique »).
Deux renforts seulement : la check-list de `resume` (ci-dessus) et la formulation « chez toute femme en
âge de procréer » dans `expert`/Pièges. Aucun ajout au barème.

**Divergences consignées**

- section notée `m5` vs page SSP · **ordre de la 1ʳᵉ ligne antiémétique de la grossesse** : la section
  notée procède par paliers — « Vitamine B6 (pyridoxine) : 10-25 mg × 3/j ; Doxylamine + pyridoxine
  (Diclectin) **si insuffisant** » — tandis que la page SSP donne d'emblée la **combinaison** en 1ʳᵉ
  ligne. `resume` est resté sur la page SSP (niveau 1) et porte « 1ère intention : doxylamine +
  pyridoxine (Vit. B6) ». Les deux formulations sont compatibles en pratique (escalade à l'intérieur de
  la même ligne) ; consignée pour mémoire, **rien n'a été modifié dans la section notée**.
- `presentation`/Version longue conserve « pyridoxine ± doxylamine », qui est l'ordre de la section
  notée. Laissé tel quel : ce n'est pas une redondance et les deux ordres sont défendables.
- **paire de redondance restante (1)** : `resume`/Contexte de grossesse « Test de grossesse positif »
  ↔ `expert`/Rôles et interventions « Test de grossesse : β-hCG positif à 2500 UI/L » (0,76).
  Conservée : rôles de blocs distincts — `expert` porte la **valeur que l'examinateur remet au
  candidat pour faire tourner la station**, `resume` porte l'élément d'anamnèse à retenir. Supprimer
  l'un des deux casserait soit la station, soit la révision.

---

### AMBOSS-6 — Douleurs pelviennes, femme 30 ans, fibromes / endométriose (page SSP : Douleur - Masse Pelvienne)

Redondance : **15 paires → 4** (`report_redundancy.py AMBOSS-6_`). Quatre blocs présents.
Grille de l'axe 6 : `presentation`/Pièges ECOS supprimée après report dans `expert`/Pièges.

**Modifications**

*Alignements sur une autorité — β-hCG*

- resume · Biologie : « Bêta-HCG **en cas de suspicion de grossesse** » → « **β-hCG systématique chez
  toute femme en âge de procréer** — avant toute imagerie irradiante ou tout médicament tératogène ».
  **Niveau 1** : la page SSP tranche explicitement et en fait sa règle d'or ; la section notée dit la
  même chose. Le pédagogique restreignait indûment l'indication de l'examen le plus important du cas.
  source : SSP — Règle d'or — « Devant toute douleur ou masse pelvienne chez une femme en âge de
  procréer : β-hCG urinaire / sanguin **IMMÉDIAT** » ; SSP — ANAMNÈSE — « β-hCG **systématique** chez
  femme en âge de procréer » ; section notée `m2` — « β-hCG urinaire [exclure grossesse avant examens
  invasifs car patiente essaie de concevoir] »
- expert · Pièges : **ajout en tête** de « Ne pas demander de β-hCG : toute douleur pelvienne chez une
  femme en âge de procréer impose d'exclure une grossesse — piège éliminatoire ». Report obligatoire
  avant la suppression de `presentation`/Pièges ECOS (précédent AMBOSS-3, tâche 5) : l'item n'existait
  **nulle part** dans `expert`, et c'est le piège éliminatoire n° 1 de la page SSP.
  source : SSP — frontmatter `pieges_eliminatoires` — « Ne pas demander β-hCG chez femme en âge
  procréer » ; SSP — Pièges

*Alignements sur une autorité — thérapeutique*

- resume · Traitements médicamenteux : « **Antagonistes GnRH (ex : élagolix)**, parfois en association
  hormonale » → « **Agonistes GnRH (leuprolide)** : réduction du volume avant chirurgie, **6 mois au
  maximum**, avec **add-back œstro-progestatif** si prolongé ». **Niveau 2** : la page SSP ne nomme
  aucun médicament de cette classe ; la section notée en nomme un, d'une autre classe, et le
  pédagogique la contredisait. Formulation reprise de la section notée.
  source : section notée `m6` — « Agonistes GnRH : leuprolide pour réduction pré-op (**max 6 mois**) »
  et « Agonistes GnRH + **add-back thérapy** (oestrogènes/progestatifs) »
  Vérifié après coup qu'aucun autre bloc ne porte l'ancienne formule : `theorie`/PEC de la
  dysménorrhée secondaire et `theorie`/Rappels disaient déjà « agonistes GnRH (leuprolide) ».
- theorie · Rappels thérapeutiques : la durée maximale et son motif sont ajoutés — « 6 mois au maximum,
  la déminéralisation osseuse limitant la durée — d'où l'add-back œstro-progestatif si le traitement
  doit être prolongé ». Le *pourquoi* revient à `theorie`, la consigne actionnable à `resume`.
- theorie · Rappels thérapeutiques · notation posologique : « ibuprofène 400-600mg **TID** » →
  « 400-600 mg **× 3/j** » et « Acide tranexamique 1g **TID** » → « 1 g **× 3/j** ». Abréviation latine
  remplacée par la notation de la section notée (« ibuprofène 400-600mg **x3/j** ») — lisibilité d'une
  posologie.

*Dédoublonnage (contrat de blocs, règle du format)*

- presentation · **Pièges ECOS supprimée** (axe 6). Anti-perte vérifiée item par item **avant**
  suppression : β-hCG porté dans `expert` (ci-dessus) ; « Oublier de rechercher une anémie **liée aux
  ménorragies** » a enrichi l'item `expert` qui disait seulement « Oublier de rechercher une anémie » ;
  « Oublier de relier symptômes au cycle menstruel » et « Ne pas explorer la question de l'infertilité »
  étaient déjà présents dans `expert` (« Manquer le lien entre symptômes et cycle menstruel », « Ne pas
  aborder la question de l'infertilité »).
- presentation · mnémo **5D de l'endométriose** : la `mnemo-box` de la Checklist mentale est
  **déplacée** vers Touches ludiques, où elle **absorbe** la sous-section « Endométriose = 3D » —
  strictement incluse. Titre explicité : « Endométriose = les 5D (les 3D classiques + 2) », ce qui
  préserve la triade classique que `theorie` continue de citer. La Checklist mentale redevient une
  trame pure (axe 5). Précédent AMBOSS-2 / AMBOSS-3.
- presentation · Checklist mentale : « Symptômes associés → dysménorrhée, dyspareunie, dyschésie,
  ménorragie, infertilité » → « Symptômes associés → **dérouler les 5D**, puis les ménorragies et leur
  retentissement ». La trame renvoie au mnémo au lieu de recopier `theorie`/Endométriose (« Symptômes
  classiques : 3D … »). Axe 5.
- theorie · « Approche diagnostique » → **« Pourquoi cette séquence diagnostique »**. La liste numérotée
  de six examens redisait `resume`/Imagerie et `theorie`/queue au même format. Remplacée par ce que
  chaque examen **ajoute** : l'échographie tranche l'essentiel mais ne voit pas l'endométriose
  péritonéale, l'IRM sépare fibrome et adénomyose, l'hystéroscopie identifie le fibrome sous-muqueux,
  la laparoscopie voit **et** traite, le CA-125 est trop peu spécifique pour la routine. Axe 1.
  Anti-perte : les deux items **uniques** de la liste — hystéroscopie / fibrome sous-muqueux, et
  CA-125 non recommandé en routine — n'existaient nulle part ailleurs et sont **conservés** dans le
  texte de remplacement ; les quatre autres figurent dans `resume` ou dans `theorie`/queue.
- theorie · Rappels thérapeutiques · AINS : l'item recopiait la posologie désormais portée par
  `resume`. Remplacé par le mécanisme — blocage des prostaglandines endométriales — et par sa
  conséquence pratique : débuter dès les premières douleurs ou la veille des règles plutôt qu'à la
  demande (la patiente prend justement de l'ibuprofène « quand la douleur est forte »). Axe 2.
- theorie · Impact sur la fertilité : « Évaluation fertilité : spermogramme partenaire, HSG, réserve
  ovarienne » était une **check-list actionnable dans `theorie`**, doublant `presentation`/Q3 Suivi.
  Remplacée par le rationnel : « L'infertilité est celle d'un couple : explorer l'endométriose sans
  spermogramme du partenaire, sans test de perméabilité tubaire ni évaluation de la réserve ovarienne,
  c'est risquer de traiter la mauvaise cause ». La liste actionnable reste dans `presentation`/Q3.
- presentation · « 2. Examens complémentaires immédiats », Q1 : liste → réponse orale. Les cinq items
  sont repris. Axe 1.
- presentation · « 3. … », Q2 « Traitement » : liste → réponse orale. Axe 2. La réponse explicite ce
  que la liste laissait implicite : la contraception hormonale continue supprimerait les symptômes mais
  est **incompatible avec le désir de conception**, qui est le motif profond de la consultation.

*Anti-perte — information portée dans le canonique*

- resume · Traitements médicamenteux : ajout de « **AINS en 1ʳᵉ ligne de la dysménorrhée : ibuprofène
  400-600 mg × 3/j** ». Les AINS figuraient dans la check-list « PEC en 3 points » sans figurer dans
  `resume`/Prise en charge : l'axe 3 demande que la check-list soit un sous-ensemble strict du
  canonique — c'est le canonique qui les reçoit.
  source : section notée `m6` — « AINS : ibuprofène 400-600mg x3/j pour dysménorrhée »

**β-hCG — vérification explicite**

Présent dans `resume` (Biologie, Examens à faire), `presentation` (Checklist mentale, Q1, Version
longue, SBAR), mais **absent d'`expert`/Pièges** et **restreint à tort** dans `resume`/Biologie. Les
deux points sont corrigés ci-dessus. Aucun ajout au barème.

**Divergences consignées**

- resume · **élagolix, non enregistré en Suisse** : la formule remplacée nommait « Antagonistes GnRH
  (ex : élagolix) ». L'élagolix n'est pas commercialisé en Suisse ; l'antagoniste GnRH enregistré en CH
  pour le fibrome et l'endométriose est l'association **relugolix/estradiol/noréthistérone (Ryeqo®)**.
  La correction appliquée suit la **section notée**, qui prescrit un **agoniste** (leuprolide), et non
  une substitution de molécule dans la même classe : ni la page SSP ni la section notée ne mentionnent
  d'antagoniste, il n'y avait donc rien à arbitrer de ce côté. Consigné pour arbitrage éditorial si
  l'utilisateur souhaite réintroduire la classe des antagonistes avec la molécule suisse.
- section notée `m6` · **seuil de taille probablement amputé** : « Myomectomie si fibromes sous-muqueux
  ou **4cm** ». Le signe de comparaison manque — la formule usuelle est « > 4 cm ». Divergence
  **interne à une section notée** : consignée, **non corrigée** (barème gelé).
- section notée `m6` · molécules non reprises dans le pédagogique, sans contradiction : « Progestatifs :
  dienogest 2 mg/j ou désogestrel 75 μg/j » et « Stimulation ovarienne : clomifène ou gonadotrophines ».
  `resume` étant centré sur le léiomyome, ces lignes relèvent de l'endométriose et de l'AMP. Rien de
  faux dans le pédagogique — **aucune modification**, signalé si l'utilisateur veut enrichir `resume`.
- **paires de redondance restantes (4)**, toutes `resume` ↔ `presentation`, toutes justifiées par un
  changement de format :
  - « Douleurs pelviennes chroniques ou pesanteur » ↔ « Douleurs pelviennes chroniques » (0,82) et
    ↔ « Douleurs pelviennes chroniques et cycliques » (0,79) : les seconds sont des items d'`arg-list`
    dans l'**argumentation pour/contre** d'une question d'examinateur — liste → argumentation.
  - « Antécédents familiaux de fibromes » ↔ « Antécédents familiaux » (0,78) : même argumentation
    pour/contre.
  - « Douleurs pelviennes chroniques ou pesanteur » ↔ « Douleur pelvienne chronique » (0,77) : le
    second est une **valeur du mnémo 5D**. Un mnémo ne se démembre pas — supprimer le D de « Douleur
    pelvienne chronique » casserait la clé.
