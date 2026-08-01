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

*Fix round 3 — anglicisme non traduit, détecté par le balayage large de la tâche 10b (tâche 10c)*

- annexe Diagnostics différentiels · intitulé : « Choledocholithiasis » → « Cholédocholithiase » —
  orthographe anglaise/latine (suffixe `-iasis`, sans accent) non traduite, incohérente avec la même
  entité correctement rendue en français dans AMBOSS-36 (« Cholédocholithiase »). Ni un germanisme ni
  lié au défaut du chevron nu (aucun `<` nu à proximité) : remontée par la passe B (filet large, mots
  collés ≥ 18 lettres) du balayage anglicismes/germanismes de la tâche 10b
  (`.superpowers/sdd/2026-07-30-amboss-refonte-pedagogique-suisse/task-10b-report.md` § 3.1).

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

### Passe unités SI — numérations en unité implicite, dernier lot (tâche 10c)

Complète la passe précédente (« fix round 3/5 de la tâche 7 » ci-dessus, qui se croyait exhaustive).
Quatre valeurs supplémentaires étaient en réalité invisibles à cette recherche, pour deux raisons
distinctes, établies et démontrées dans
`.superpowers/sdd/2026-07-30-amboss-refonte-pedagogique-suisse/task-10b-report.md` (§ 3.2) :

- **Défaut d'outillage.** `lib_amboss.visible_text()` traitait tout `<` nu (seuil de laboratoire
  écrit `plaquettes < 30 000`) comme l'ouverture d'une balise, avalant tout le texte jusqu'au `>` réel
  suivant : la valeur numérique disparaissait du texte examiné par toute recherche fondée sur
  `visible_text()`, alors que le terme de recherche (« plaquettes ») restait visible juste avant.
  Corrigé au commit `9df1484` (motif de balise restreint à un `<`/`</` suivi immédiatement d'une
  lettre ASCII). Explique directement 3 des 4 valeurs : AMBOSS-24 ×2, AMBOSS-34 ×1.
- **Angle mort de vocabulaire.** La recherche du round précédent couvrait « leucocytes » mais pas la
  variante substantive « leucocytose » (numération élevée) — explique la 4ᵉ valeur, AMBOSS-30, qui n'a
  pourtant aucun chevron nu à proximité.

**Modifications**

- **Leucocytes/plaquettes · unité implicite (`000` ou `k`) → `G/L`, × 0,001.** 4 valeurs, 3 grilles,
  toutes dans des blocs pédagogiques (`theorie`/`expert`), aucune en section notée :
  - AMBOSS-24, `theorie`/Purpura thrombopénique immunologique : « Traitement si plaquettes < 30 000
    ou saignements » → « … **< 30 G/L** ou saignements ».
  - AMBOSS-24, `theorie`/Rappels thérapeutiques : « PTI aigu : corticoïdes si plaquettes < 30 000 » →
    « … **< 30 G/L** ». Seuil clinique standard de traitement du PTI en cas de saignement ; cohérent
    avec les deux valeurs de plaquettes déjà correctement en G/L ailleurs dans la même grille
    (« plaquettes < 150 G/L », « Plaquettes 180 G/L (normale) »).
  - AMBOSS-34, `theorie`/Thrombolyse intraveineuse : « CI relatives : AVC étendu, INR > 1.7,
    plaquettes < 100k » → « … plaquettes **< 100 G/L** ». « 100k » est une abréviation (k = mille) et
    non un nombre écrit en toutes lettres : vérifié avant conversion qu'elle désigne sans ambiguïté
    100 000, lecture usuelle du seuil transfusionnel plaquettaire pré-thrombolyse. L'INR > 1.7 sur la
    même ligne n'est pas concerné — un INR est un rapport sans unité.
  - AMBOSS-30, `expert`/Rôles et interventions : « FSC : leucocytose 14 000, PNN 75% » →
    « FSC : leucocytose **14 G/L**, PNN 75% ». 14 G/L reste au-dessus de la norme (4-10 G/L) : le
    qualificatif « leucocytose » demeure exact après conversion. Le « 75% » de PNN, un pourcentage de
    formule et non une numération absolue, n'est pas concerné.

**Balayage de clôture (tâche 10c)**

Recherche refaite sur les 40 grilles avec `visible_text()` corrigé et un vocabulaire élargi à 16
variantes (leucocytes, leucocytose, hyperleucocytose, GB, globules blancs, plaquettes, thrombocytes,
thrombopénie, thrombocytose, PNN, polynucléaires, neutrophiles, lymphocytes, lymphocytose,
éosinophiles, éosinophilie), par deux méthodes indépendantes et convergentes (terme → nombre voisin,
et nombre → terme voisin), complétées par un audit manuel des 29 nombres bruts ≥ 1000 sans unité du
corpus toutes causes confondues (dates de publication, incidences épidémiologiques « X/100 000 »,
fréquences en Hz, doses déjà en mg/µg, poids de naissance déjà en g — aucun n'est une numération
sanguine non convertie). Seul candidat retenu par les deux méthodes : la divergence déjà consignée
d'AMBOSS-33 ci-dessus (« PL (si faite) : GR 50 000 ») — revérifiée, toujours à dessein non convertie
(numération de LCR, jamais en G/L), pas une nouvelle trouvaille. **Aucune numération en unité
implicite restante sur le corpus** à l'issue de ce lot.

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

### AMBOSS-7 — Toux et fièvre, fillette de 2 ans, bronchite avec suspicion de pneumonie (page SSP : Fièvre du Nourrisson)

Redondance : **5 paires → 2** (`report_redundancy.py AMBOSS-7_`). Quatre blocs présents.
**Pas de sous-section `presentation`/Pièges ECOS** — vérifié, axe 6 sans objet. Items ICE du critère
`m4` « Communication avec la mère » **non touchés**, ainsi que `theorie`/Gestion de l'anxiété
parentale, qui relève du même critère.

**Modifications**

*Sécurité — posologies pédiatriques (voir aussi les signalements en fin d'entrée)*

- theorie · Rappels · paracétamol : « Paracétamol 15 mg/kg/dose **Q4-6H** » → le plafond journalier
  devient le message, et `resume` reçoit la posologie complète « 15 mg/kg/dose **toutes les 6 h
  (max 60 mg/kg/j)** ». **Niveau 1** : la page SSP tranche explicitement. À 15 mg/kg toutes les 4 h
  sans plafond énoncé, on atteint 90 mg/kg/j, soit une fois et demie la dose maximale.
  source : SSP — Cartes ECOS — « Paracétamol : 15 mg/kg toutes les 6 h (**max 60 mg/kg/j**) » ;
  SSP — PRISE EN CHARGE — « Paracétamol 15 mg/kg/dose »
- resume · Traitement symptomatique · AINS : ajout de « ibuprofène 10 mg/kg/dose après 6 mois,
  **à éviter ici en raison de la déshydratation** » et de « **jamais d'aspirine chez l'enfant
  (syndrome de Reye)** ». **Niveau 1**, mise en garde que la page SSP ajoute (précédent AMBOSS-1) :
  l'enfant a une diarrhée et des signes de déshydratation débutants, et l'aspirine figure parmi les
  pièges éliminatoires de la page.
  source : SSP — Cartes ECOS — « **AINS contre-indiqués** en cas de varicelle […] et de
  **déshydratation** (rein) » ; SSP — frontmatter `pieges_eliminatoires` — « Aspirine chez enfant
  < 16 ans (Reye) » ; SSP — PRISE EN CHARGE — « **Jamais d'aspirine** chez l'enfant »
- theorie · Signes de détresse respiratoire : « Tachypnée : > 40/min (**2-5 ans**) » →
  « > 50/min (2-11 mois), > 40/min (**1-5 ans**), > 30/min (> 5 ans) ». **Correction factuelle
  interne** : les seuils OMS sont 1-5 ans, pas 2-5 ans ; la formule d'origine laissait sans seuil
  la tranche 1-2 ans, celle qui borde l'âge de la patiente. Ni la SSP ni la section notée ne
  définissent ces seuils — rien à arbitrer, un fait à corriger.

*Enrichissement du canonique (préalable au dédoublonnage, axes 1 et 2)*

- resume · Examens diagnostiques : ajout de « SpO₂ systématique ; gaz du sang si détresse
  respiratoire ou diarrhée profuse » et « Ionogramme et glycémie si diarrhée ou déshydratation ».
  Ces examens étaient **notés** mais absents du canonique, ce qui empêchait la réponse orale de
  `presentation` d'en être un sous-ensemble (axe 1).
  source : section notée `m2` — « Saturation en oxygène », « Gaz du sang artériel [troubles
  acido-basiques, diarrhée, symptômes respiratoires] », « Électrolytes, glucose [diarrhée liquide,
  peut être déshydratée ou hypoglycémique] »
- resume · Prise en charge : la SRO (50-100 mL/kg sur 4 h, Ringer lactate IV si modérée à sévère),
  le seuil d'oxygénothérapie et les critères d'hospitalisation (SpO₂ < 92 %, déshydratation,
  âge < 6 mois) et le protocole antibiotique (amoxicilline 80-90 mg/kg/j en **2-3 prises** ;
  azithromycine 10 mg/kg J1 puis 5 mg/kg J2-5) descendent de `theorie`/Rappels vers `resume`, qui
  est le canonique de l'axe 2. Formulations reprises de la section notée.
  source : section notée `m5` — « Antibiothérapie: Amoxicilline 80-90 mg/kg/j **x2-3/j** »,
  « Alternative: Azithromycine 10mg/kg J1 puis 5mg/kg J2-5 », « Hospitalisation si SpO2 < 92%,
  déshydratation, âge < 6 mois », « Réhydratation orale: SRO 50-100 mL/kg sur 4h »,
  « Réhydratation IV: Ringer lactate si modérée-sévère »
- resume · Suivi : ajout de « Si hospitalisation : surveillance FR, SpO₂, poids, diurèse et état
  général » — la réponse orale de `presentation`/Q3 le disait sans que le canonique le porte.
  source : section notée `m5` — « Surveillance: FR, SpO2, état général » et « Surveillance: Poids,
  diurèse, état conscience »

*Dédoublonnage (contrat de blocs, règle du format)*

- theorie · Bronchite aiguë chez l'enfant : cinq des six items redisaient `resume` au même format
  (étiologie virale > 90 %, symptômes, évolution 7-10 j, traitement supportif). Remplacés par le
  *pourquoi* — le rôle de l'adénovirus, qui donne à lui seul l'atteinte respiratoire **et**
  digestive et explique la diarrhée sans seconde infection ; la régénération de l'épithélium cilié,
  qui explique une toux qui traîne sans être un échec ; les trois signes de sortie de la bronchite
  simple. Les virus courants et les complications sont conservés dans le texte de remplacement.
  Axe 1. (Le point adénovirus vient de la section notée `m1` : « adénovirus peut causer symptômes
  respiratoires + GI ».)
- theorie · Pneumonie communautaire : « Critères d'hospitalisation » et « Traitement : amoxicilline »
  sont supprimés (portés dans `resume` ci-dessus) et remplacés par ce qui décide de
  l'hospitalisation — oxygénation, hydratation, réserve liée à l'âge — et par le fait que la
  radiographie confirme le foyer sans séparer viral et bactérien. Axe 2.
- theorie · Rappels thérapeutiques : le protocole recopiait `resume`. Remplacé par le rationnel —
  la fièvre visée pour le confort et non pour le chiffre, le risque rénal des AINS chez un enfant
  déshydraté, la voie orale préférée à la veineuse tant que l'enfant boit, l'inutilité des
  bronchodilatateurs hors sibilants, la forte dose d'amoxicilline contre les pneumocoques de
  sensibilité diminuée, et la distinction des deux seuils de SpO₂ (95 % = alerte, 92 % = oxygène et
  hospitalisation). Axe 2.
- presentation · mnémo **FEVER** : la `mnemo-box` de la Checklist mentale est **déplacée** vers
  Touches ludiques, la Checklist redevenant une trame pure (axe 5). Elle n'est pas supprimée :
  elle ne double pas « Pneumonie enfant = 4F », qui porte en propre le « Foyer pulmonaire ».
  Précédent AMBOSS-2 / AMBOSS-3 / AMBOSS-6.
- presentation · Q1 « Quels examens demanderiez-vous ? », Q2 « Traitement », Q3 « Suivi » : les trois
  listes deviennent des réponses orales (`presentation-reponse text`). Une liste sous un en-tête Q/R
  n'est pas un changement de format. Contenu intégralement repris, et enrichi de ce que la liste
  laissait implicite : pourquoi la FSC et l'hématocrite, pourquoi l'ionogramme, et les signes
  d'alerte concrets donnés à la mère. Axes 1 et 2.

**Divergences consignées**

- theorie · **« Incidence : 15-20% des bronchites peuvent évoluer »** (vers la pneumonie) : chiffre
  élevé au regard de l'évolution habituelle d'une bronchite aiguë, mais ni la page SSP ni la section
  notée ne le traitent, et je n'ai pas de source qui le contredise franchement. **Niveau 3** :
  laissé inchangé, consigné pour arbitrage.
- **paires de redondance restantes (2)**, toutes `resume` ↔ `presentation`, toutes justifiées par un
  changement de format :
  - « Altération de l'état général » ↔ « Altération état général » (0,90) et « Fièvre modérée ou
    absente » ↔ « Fièvre modérée-élevée » (0,74) : les seconds sont des items d'`arg-list` dans
    l'**argumentation pour/contre** d'une question d'examinateur — liste → argumentation
    (précédent AMBOSS-6).

**Signalements de sécurité** — deux, tous deux corrigés ci-dessus et remontés au rapport de tâche :
plafond journalier de paracétamol absent d'une posologie en mg/kg répétée toutes les 4 à 6 heures ;
ibuprofène proposé sans la contre-indication relative de la déshydratation chez une enfant qui en
présente les signes. Aucune posologie pédiatrique en dose adulte ni sans référence au poids n'a été
trouvée dans cette grille.

### AMBOSS-8 — Troubles du transit, homme de 32 ans, maladie de Crohn iléo-colique (page SSP : Diarrhée)

Redondance : **12 paires → 1** (`report_redundancy.py AMBOSS-8_`). Quatre blocs présents.
**Pas de sous-section `presentation`/Pièges ECOS** — vérifié, axe 6 sans objet.

**Modifications**

*Alignements sur une autorité*

- resume · Facteurs de risque : « Âge jeune (**< 30 ans**) » → « Adulte jeune : **pic d'incidence
  entre 15 et 35 ans** ». **Correction factuelle interne** : la borne d'origine excluait le patient
  lui-même, qui a 32 ans, et contredisait les trois autres blocs de la grille comme la section notée.
  source : section notée `m1` — « Âge typique (**15-35 ans**) » ; theorie — « pic 15-35 ans »
- resume · Facteurs de risque : « Antécédents familiaux de MICI » → « … **au 1ᵉʳ degré** ».
  **Niveau 1**, précision de la page SSP.
  source : SSP — ANAMNÈSE — « **ATCD familiaux 1ᵉʳ degré** : MICI, cancer colorectal, polypose,
  maladie cœliaque »
- resume · Examen périnéal et Check-list : ajout du **toucher rectal** (sang sur le doigtier, masse
  rectale, tonus sphinctérien). **Niveau 1 et niveau 2 convergents** : le canonique ne portait que
  l'« examen périnéal », alors que le TR est un sous-item noté et que la page SSP en fait un geste
  obligatoire ; `expert`/Pièges dit déjà « Oublier le toucher rectal ».
  source : SSP — EXAMEN CLINIQUE — « **Toucher rectal** : sang sur le doigtier, méléna, masse
  rectale, tonus sphinctérien » et « À faire ✅ : séquence IAPA + **TR (sang, masse)** » ;
  section notée `m2` — « **Examen rectal** [fait partie de l'examen abdominal complet et
  particulièrement important en cas de saignement] »
- resume · Examens diagnostiques : ajout de « **Recherche de sang occulte dans les selles** » et
  « **Coproculture et parasitologie des selles** (exclure C. difficile, giardiase, amibiase) ».
  Ces deux examens sont **notés** — la coproculture est même un critère à elle seule (`m3`) — et
  étaient absents de tout le pédagogique.
  source : section notée `m2` — « Recherche de sang occulte dans les selles » ; section notée `m3` —
  « Coproculture; microscopie des selles pour œufs et parasites [pour exclure […] C. difficile,
  giardiase et amibiase] » ; SSP — Diarrhée chronique — « Coproculture + parasites + *C. difficile*
  si non encore réalisés »
- resume · Imagerie : ajout de « US abdominale (épaississement pariétal) ; ASP si suspicion de
  complication (distension, pneumopéritoine) » — les deux sont notés (`m4`) et absents du canonique.
  source : section notée `m4` — « US abdominale [épaississement de la paroi] », « Radiographie
  abdominale simple [distension intestinale ou pneumopéritoine] » ; SSP — « **Imagerie** : ASP /
  échographie / CT abdominal injecté si suspicion de complication »
- resume · Traitement des poussées : « Corticothérapie orale (budesonide ou prednisone) » →
  « **budésonide ou prednisone 40-60 mg/j), puis décroissance progressive — jamais d'arrêt brutal** ».
  Posologie et décroissance reprises de la section notée.
  source : section notée `m6` — « Corticoïdes: **Prednisone 40-60mg/j puis décroissance** »
- resume · Traitement de fond : ajout de « **Vaccins à jour *avant* toute immunosuppression** ; sous
  azathioprine, **FSC, transaminases et créatinine mensuelles** ». Surveillance biologique d'un
  immunosuppresseur myélo- et hépatotoxique, notée mais portée nulle part dans le pédagogique.
  source : section notée `m6` — « Surveillance: FSC, transaminases, créatinine **mensuelle** » et
  « **Vaccinations à jour avant immunosuppression** »

*Dédoublonnage (contrat de blocs, règle du format)*

- theorie · Signes d'alarme dans les troubles fonctionnels : la check-list de sept drapeaux rouges
  était une **check-list actionnable logée dans `theorie`**, et doublait mot pour mot deux items de
  `presentation`. Réécrite en *pourquoi* — pourquoi le réveil nocturne est organique, pourquoi la
  perte de poids et l'anémie ne s'expliquent pas par un trouble de la motricité, pourquoi un
  saignement impose de voir la lésion plutôt que de la présumer hémorroïdaire, pourquoi l'âge et
  l'hérédité déplacent la probabilité *a priori*. **Les sept items sont conservés** dans le texte
  de remplacement.
- presentation · mnémo **ALARME** : `mnemo-box` **déplacée** de la Checklist mentale vers Touches
  ludiques (axe 5). Sa valeur « A = Age **< 50** avec symptômes évocateurs » est corrigée en
  « A = Âge : **début des symptômes après 50 ans** — ou cancer colorectal familial avant 50 ans » :
  la formule d'origine **inversait** le drapeau rouge. **Niveau 1**, la clé du mnémo reste intacte.
  La valeur « E » absorbe le réveil nocturne, repris de la sous-section supprimée ci-dessous.
  source : SSP — Red flags — « **Début des symptômes après 50 ans** » ; SSP — Mnémoniques —
  « Drapeaux rouges (diarrhée chronique) : sang · perte de poids · diarrhée nocturne · **âge > 50
  ans** · ATCD familiaux »
- presentation · **« ⚠️ Drapeaux rouges SII » supprimée** (Touches ludiques). Anti-perte vérifiée
  item par item **avant** suppression : sang, perte de poids, anémie, symptômes nocturnes et ATCD
  familiaux de cancer colorectal figurent tous les cinq dans `theorie`/Signes d'alarme réécrit, et
  quatre sur cinq dans le mnémo ALARME conservé.
- presentation · « 👉 Crohn vs RCH » : les trois items recopiaient le tableau `theorie`/Différences
  clés au même format. Réécrits en **image mnémotechnique** — « de la bouche à l'anus, en peau de
  léopard » contre « du rectum vers le haut, d'un seul tenant », et « la cigarette choisit son
  camp ». Changement de format de restitution, le tableau discriminant reste dans `theorie`.
- expert · Points clés : « Tabagisme = facteur aggravant Crohn, protecteur RCH » → « **Tabac = seul
  facteur de risque modifiable du dossier : attendre du candidat qu'il en conseille l'arrêt** ».
  L'item redisait `theorie` et `presentation` ; reformulé vers ce que l'examinateur **observe**
  (axe 7). Le contraste Crohn/RCH reste porté par `theorie` et par le mnémo.
- theorie · Rappels thérapeutiques : le protocole recopiait `resume`. Remplacé par le rationnel —
  pourquoi le 5-ASA, qui agit dans la lumière sur une muqueuse, rend davantage dans la RCH ;
  pourquoi le corticoïde n'entretient pas la rémission et se décroît toujours ; les 8 à 12 semaines
  de latence de l'azathioprine, qui imposent le chevauchement ; le risque infectieux et
  tuberculeux des anti-TNF, qui impose le bilan préalable ; la ciclosporine comme sauvetage ;
  et le siège iléal de la maladie, qui explique les carences en B12 et en sels biliaires.
  L'arrêt du tabac y est présenté comme le geste au meilleur rapport bénéfice-risque du dossier.
  Axe 2.
- presentation · Q1 « Quels examens », Q2 « Traitement », Q3 « Suivi » : les trois listes deviennent
  des réponses orales. Contenu intégralement repris et complété par ce que le canonique porte
  désormais (sang occulte, coproculture, décroissance des corticoïdes, surveillance biologique de
  l'azathioprine, oncogénétique nommée). Axes 1 et 2.

**Divergences consignées**

- theorie et section notée `m6` · **5-ASA dans la maladie de Crohn** : la section notée prescrit
  explicitement « Traitement de la maladie de **Crohn** légère-modérée • 5-ASA (mésalazine): 3-4g/j
  PO + suppositoires/lavements ». La mésalazine n'est pourtant pas retenue par les recommandations
  actuelles pour l'induction ni l'entretien du Crohn — son rendement est établi dans la RCH. La page
  SSP reste générique (« **MICI** : 5-ASA (mésalazine), corticoïdes (budésonide)… »), le pédagogique
  ne contredit pas la section notée, et le barème est gelé : **rien à arbitrer au sens du § 4**.
  `resume` reprend donc la ligne de la section notée telle quelle, et la nuance (« ce qui explique
  son rendement dans la RCH et **sa place discutée dans le Crohn** ») est portée par `theorie`.
  Consigné pour arbitrage éditorial. Remonté au rapport de tâche.
- **paire de redondance restante (1)** : « Tabac (facteur aggravant) » ↔ « Facteur aggravant tabac »
  (0,74) — le second est un item d'`arg-list` dans l'argumentation pour/contre de la question
  d'examinateur ; liste → argumentation (précédent AMBOSS-6).

### AMBOSS-9 — Douleurs dorsales, homme de 71 ans, hernie discale L3-L4 sur terrain à risque (page SSP : Lombalgies)

Redondance : **11 paires → 0** (`report_redundancy.py AMBOSS-9_`). Quatre blocs présents.
Grille de l'**axe 6** : `presentation`/Pièges ECOS supprimée après report dans `expert`/Pièges.

**Modifications**

*Sécurité thérapeutique — `theorie`/Rappels (voir les signalements en fin d'entrée)*

- theorie · Rappels · **myorelaxant** : « Myorelaxants : **Cyclobenzaprine** 5-10mg TID si spasmes »
  → « **tizanidine 2-4 mg × 2-3/j**, brièvement, si contracture », avec la raison du changement
  conservée dans l'item. **Niveau 1 et niveau 2 convergents** : la cyclobenzaprine n'est pas
  commercialisée en Suisse, et son effet anticholinergique marqué la rend inappropriée après 65 ans
  (confusion, chutes, rétention urinaire) — chez un homme de 71 ans.
  source : SSP — PRISE EN CHARGE — « **Myorelaxant (tizanidine)** courte période si contracture » ;
  section notée `m6` — « Myorelaxants si spasmes: **Tizanidine 2-4 mg × 2-3/j** »
- theorie · Rappels · **paracétamol** : « Paracétamol 1g QID première ligne (**attention dose
  maximale diabétique**) » → « 1 g × 3-4/j — **plafond 4 g/j, ramené à 3 g/j** si poids < 50 kg,
  insuffisance hépatique ou consommation chronique d'alcool. **La limite est hépatique, pas
  métabolique** ». **Correction factuelle interne** : le diabète ne modifie pas la dose maximale de
  paracétamol ; la mise en garde d'origine désignait la mauvaise contre-indication et masquait la
  vraie, chez un patient qui boit du vin.
  source (posologie) : SSP — PRISE EN CHARGE — « **Paracétamol 1 g × 3-4/j** » ; section notée `m6` —
  « Paracétamol 1g × 4/j »
- theorie · Rappels · **AINS** : ajout de « la durée la plus courte possible » et du contrôle de la
  fonction rénale et de la tension chez ce patient de 71 ans **diabétique**. **Niveau 1**, mise en
  garde ajoutée par la page SSP (précédent AMBOSS-1).
  source : SSP — PRISE EN CHARGE — « **AINS courte durée (si pas de CI)** »
- theorie · Rappels · **tramadol** : « si douleur sévère (prudence personne âgée) » → « **en réserve
  et pour quelques jours seulement** », avec le motif (chutes, hyponatrémie, seuil convulsif) et le
  rappel que l'opioïde au long cours est un piège éliminatoire. **Niveau 1**.
  source : SSP — PRISE EN CHARGE — « **tramadol en réserve, courte durée** » ; SSP — frontmatter
  `pieges_eliminatoires` — « **Opioïdes au long cours** » ; SSP — Cartes ECOS — « aucun bénéfice
  démontré au-delà de quelques jours […] tolérance, hyperalgésie induite, dépendance, chutes »
- theorie · Rappels · **gabapentine** : « Gabapentine 300mg TID » → « **titration progressive** à
  partir de 300 mg le soir, jusqu'à 900 mg × 3/j au maximum, **en adaptant à la fonction rénale** ».
  **Niveau 1 et niveau 2 convergents** : débuter d'emblée à 300 mg × 3/j chez un sujet âgé expose
  à la somnolence et à la chute.
  source : SSP — Lombalgie chronique — « gabapentine/prégabaline (Compendium, **titration**) » ;
  section notée `m6` — « Gabapentine: 300 mg **progressivement** jusqu'à 900 mg × 3/j »
- theorie · Rappels · notation : « QID », « TID », « Q6H » → « × 3-4/j », « × 3/j », « toutes les
  6 h » (précédent AMBOSS-6, lisibilité d'une posologie).

*Drapeaux rouges — renforcement du canonique (niveau 1)*

- resume · Signes d'alerte : ajout de trois drapeaux rouges de la page SSP qui manquaient au
  canonique alors qu'ils visent précisément ce patient — **fracture vertébrale** (traumatisme même
  minime, terrain ostéoporotique), **métastase vertébrale** (ATCD ou risque néoplasique, perte de
  poids, douleur non soulagée par le repos) et surtout l'**anévrisme de l'aorte abdominale** chez
  l'homme > 60 ans avec facteurs de risque cardiovasculaires. L'AAA n'apparaissait **nulle part**
  dans la grille — ni dans le pédagogique, ni dans la liste des diagnostics différentiels de la
  section notée — alors que le patient en réunit le portrait : 71 ans, 40 paquets-années, diabétique.
  source : SSP — Règle d'or — « chez l'homme > 60 ans avec FRCV, **palper l'abdomen (AAA fissuré)** » ;
  SSP — Points Clés ECOS, À faire absolument n° 3 — « **Palper l'abdomen chez l'homme > 60 ans avec
  FRCV (AAA)** » ; SSP — Pièges — « **Oublier les causes extra-spinales : AAA**, colique néphrétique,
  pathologie gynécologique » ; SSP — Red flags — fracture et métastase
- resume · Examen clinique et Check-list : ajout de l'examen **périnéal** (sensibilité en selle
  S2-S4, tonus sphinctérien au toucher rectal, globe vésical) et de la **palpation abdominale**
  (masse pulsatile, auscultation aortique, pouls). Le TR est un critère **noté** (`m2`) et le
  canonique ne le portait pas.
  source : SSP — EXAMEN CLINIQUE — « **Périnée** (si suspicion queue de cheval) : sensibilité en
  selle (S2-S4), tonus sphinctérien, globe vésical » et « **Palpation abdominale** : masse pulsatile
  (AAA), auscultation aortique, pouls » ; section notée `m2` — « **Examen rectal** [Les lésions des
  fibres nerveuses L3-S5 (syndrome de la queue de cheval)…] »
- resume · Examens diagnostiques : ajout de la biologie de drapeau rouge — « FSC, CRP/VS, calcémie,
  PAL, **électrophorèse des protéines (myélome)**, PSA chez l'homme > 50 ans » — et de l'indication
  de la **DEXA** (homme ≥ 70 ans, ou ≥ 50 ans avec facteurs de risque). La DEXA est un critère noté
  à elle seule (`m4`) ; le myélome n'était évoqué nulle part.
  source : SSP — EXAMENS COMPLÉMENTAIRES — « Si red flag ou > 6 semaines — Biologie : FSC, CRP, VS,
  calcémie, PAL, **électrophorèse des protéines (myélome)** » ; section notée `m4` — « Absorptiométrie
  biphotonique (DEXA) […] **hommes ≥ 70 ans** »
- resume · Prise en charge : « **Repos relatif** (éviter immobilisation prolongée) » → « **Maintien
  de l'activité (« rester actif ») — ni alitement ni immobilisation prolongée** », plus l'ajout de
  « **Réassurance argumentée** : plus de 90 % des lombalgies aiguës guérissent en 4 à 6 semaines ».
  **Niveau 1** : « repos relatif » affaiblissait le message central de la page SSP, dont l'absence
  de mobilisation précoce est un **piège éliminatoire**.
  source : SSP — PRISE EN CHARGE — « **Maintien de l'activité (« rester actif »), éviter l'alitement
  prolongé** » ; SSP — frontmatter `pieges_eliminatoires` — « **Pas de mobilisation précoce** » ;
  SSP — Points Clés, Pièges n° 5 — « **Oublier la mobilisation précoce / prescrire l'alitement** » ;
  SSP — Règle d'or — « > 90 % sont mécaniques non spécifiques et guérissent en < 4-6 semaines »
- resume et theorie · **Lasègue** : « positif si douleur **< 70°** » et « douleur irradiant dans le
  territoire radiculaire » → « douleur radiculaire **entre 30 et 60°** ». **Niveau 1**, la page SSP
  tranche le seuil ; au-delà de 60° c'est l'étirement des ischio-jambiers qu'on teste.
  source : SSP — Manœuvres radiculaires — « **Lasègue** (sciatique) : douleur radiculaire **30-60°**
  = positif »

*Axe 6 — `presentation`/Pièges ECOS supprimée, après report*

- expert · Pièges : **ajout en tête** de « **Ne pas examiner les sphincters ni la sensibilité en
  selle : manquer un syndrome de la queue de cheval est le piège éliminatoire n° 1** ». Report
  obligatoire avant suppression (précédent AMBOSS-3, tâche 5) : l'item n'existait **pas** dans
  `expert`/Pièges — il ne figurait que dans `expert`/Points clés sous la forme « Ne pas oublier
  l'examen rectal » — et c'est le premier piège éliminatoire de la page SSP.
  source : SSP — frontmatter `pieges_eliminatoires` — « **Manquer queue de cheval (urgence chir)** » ;
  SSP — Pièges — « **Minimiser le syndrome queue de cheval** » ; SSP — Règle d'or
- expert · Pièges : « Ne pas explorer les facteurs de risque néoplasiques » enrichi de « — **ici
  l'antécédent familial de cancer de la prostate** », qui était le contenu propre de l'item
  « Ignorer ATCD familial cancer (prostate) » de la sous-section supprimée.
- expert · Pièges : **ajout** de « **Rassurer sans filet de sécurité : la réassurance doit
  s'accompagner des signes qui imposent de reconsulter** », qui recueille l'item « Rassurer mais
  rester vigilant sur red flags » de la sous-section supprimée — le seul des cinq à n'avoir aucun
  équivalent dans `expert`.
  source : SSP — Cartes ECOS — « la réassurance doit être **active et argumentée** »
- presentation · **Pièges ECOS supprimée** (axe 6). Les deux items restants étaient déjà dans
  `expert`/Pièges : « Se limiter au diagnostic d'entorse musculaire » (à l'identique) et « Négliger
  ostéoporose chez homme > 70 ans » (« Oublier le dépistage ostéoporose chez homme > 70 ans »).

*Dédoublonnage (contrat de blocs, règle du format)*

- presentation · mnémo **DORSAL** : `mnemo-box` **déplacée** de la Checklist mentale vers Touches
  ludiques (axe 5). Sa valeur « R = Red flags (queue de cheval, métastases, infection) » devient
  « R = Red flags (**voir FRONT**) », renvoi au mnémo qui les détaille.
- presentation · « 👉 Red flags lombalgie » : la liste de cinq items recopiait `resume`/Signes
  d'alerte au même format. Convertie en **mnémo FRONT**, celui de la page SSP — Fièvre, Raideur
  matinale, Oncologie, Neuro (queue de cheval), Traumatisme — avec l'AAA en ligne hors rachis.
  Changement de format de restitution (liste → mnémo) ; les cinq items d'origine sont tous repris,
  et la Raideur matinale (spondylarthrite axiale) est **ajoutée** depuis la page SSP.
  source : SSP — Mnémoniques — « **Red flags = FRONT** : Fièvre · Raideur matinale · Oncologie ·
  Neuro (queue de cheval) · Traumatisme »
- presentation · « 👉 PEC initiale lombalgie » **supprimée**. Anti-perte vérifiée item par item :
  « Paracétamol ± AINS », « Maintien activité » et « Chirurgie si déficit neurologique » sont dans
  `resume`/Prise en charge, « Pas d'imagerie si pas de red flags » dans `resume`/Examens
  diagnostiques ; le mnémo DORSAL conservé en porte la synthèse (« A = Antalgiques + activité
  adaptée »).
- theorie · Examen clinique de la lombalgie : la check-list de six items était **actionnable dans
  `theorie`** et doublait `resume`/Check-list. Réécrite en *pourquoi* : ce que sépare la palpation
  d'une épineuse et celle des paravertébraux, ce que distingue une limitation segmentaire d'une
  raideur inflammatoire, pourquoi le Lasègue perd sa sensibilité après 60 ans — un Lasègue négatif
  n'écarte donc rien chez ce patient —, ce que le testing par racine transforme en niveau lésionnel,
  pourquoi le déficit sphinctérien de la queue de cheval est trop tardif pour être attendu, et
  pourquoi l'AAA érode la face antérieure des vertèbres. L'inspection est conservée. Axe 4.
- theorie · Prise en charge de la lombalgie aiguë : les six items redisaient `resume` au même
  format. Remplacés par le rationnel — le déconditionnement et la sensibilisation centrale
  produits par l'immobilisation, la réassurance argumentée contre le « ce n'est rien »,
  l'antalgie conçue comme un moyen de rendre le mouvement possible (et l'escalade comme un aveu
  d'échec), la physiothérapie qui traite le déconditionnement et non la lésion, l'infiltration qui
  agit sur l'inflammation radiculaire sans modifier l'histoire naturelle, et la chirurgie qui
  n'accélère que le délai de soulagement sauf déficit progressif ou queue de cheval. Axe 2.
- theorie · Imagerie · DEXA : l'indication (homme > 70 ans) descend dans `resume` et l'item porte
  désormais le motif — ostéoporose masculine sous-diagnostiquée et sous-traitée, mortalité
  post-fracture plus élevée que chez la femme.
- expert · Rôles et interventions : « DEXA scan : T-score -2.1 **(ostéopénie)** » → « T-score
  -2.1 ». La donnée de station reste dans `expert`, son interprétation (< -1 = ostéopénie,
  < -2.5 = ostéoporose) dans `theorie`/Examens complémentaires. Séparation des rôles.
- presentation · Q1 « Quels diagnostics », Q1 « Quels examens », Q1 « Traitement initial »,
  Q2 « Quand envisager la chirurgie », Q1 « Mesures au long terme » : les cinq listes deviennent des
  réponses orales. Contenu intégralement repris, et complété de ce que le canonique porte
  désormais : le raisonnement d'âge derrière chaque diagnostic différentiel, la biologie de drapeau
  rouge, la tizanidine à la place du myorelaxant anonyme, la surveillance rénale sous AINS chez un
  diabétique, la réassurance argumentée, le filet de sécurité, et le délai de 24-48 h de la
  décompression dans la queue de cheval. Axes 1 et 2.

**Divergences consignées**

- **délai avant chirurgie** : `resume` dit « douleur invalidante > 6-8 semaines », `theorie` disait
  « échec 6-12 semaines ». Ni la page SSP ni la section notée ne fixent ce délai. **Niveau 3** :
  aucune des deux bornes n'est arbitrée ; `resume` garde 6-8 semaines et la réécriture de `theorie`
  ne rouvre pas le chiffre (« les quelques semaines d'attente »). Consigné.
- **section notée `m6` · « Perte de poids si IMC 25 kg/m² »** : le signe de comparaison manque, la
  formule usuelle étant « > 25 kg/m² ». Divergence **interne à une section notée** : consignée,
  **non corrigée** (barème gelé). Même nature que le « 4cm » relevé en AMBOSS-6.
- **section notée `m6` · « Bloc radiculaire sélectif L: 3 guidé par imagerie »** : ponctuation
  visiblement corrompue pour « bloc radiculaire sélectif **L3** ». Consigné, non corrigé.
- **section notée `m6` · « Conseil sur les pratiques sexuelles sûres »** : sous-item noté du critère
  « Conseil et prévention » sans rapport apparent avec une lombalgie chez un homme de 71 ans, et
  qu'aucun élément de la vignette n'introduit. Consigné, **non corrigé** (barème gelé) — signalé
  pour arbitrage.
- **aucune paire de redondance restante** sur cette grille.

**Signalements de sécurité** — quatre, tous corrigés ci-dessus et remontés au rapport de tâche :
myorelaxant non commercialisé en Suisse et inapproprié après 65 ans ; contre-indication du
paracétamol désignée à tort comme métabolique ; gabapentine sans titration ni adaptation rénale
chez un sujet âgé ; anévrisme de l'aorte abdominale totalement absent des drapeaux rouges alors que
le patient en réunit le portrait.

### AMBOSS-11 — Selles noires, homme de 65 ans, ulcère gastrique hémorragique sous AINS (page SSP : Rectorragies & Hémorragie Digestive Basse)

Redondance : **20 paires → 5** (`report_redundancy.py AMBOSS-11_`). Quatre blocs présents.
Grille de l'**axe 6** : `presentation`/Pièges ECOS supprimée après report dans `expert`/Pièges.

**Modifications**

*Sécurité thérapeutique — `theorie`/Rappels (voir les signalements en fin d'entrée)*

- theorie · Rappels · **anti-H2** : « Ranitidine 150mg BID » → « **famotidine 20-40 mg × 2/j** — la
  ranitidine n'est plus commercialisée depuis son retrait mondial de 2020 (contamination par
  nitrosamines) ». **Correction factuelle interne** : la molécule proposée en cas d'intolérance aux
  IPP n'existe plus sur le marché. Ni la page SSP ni la section notée ne parlent d'anti-H2 — il n'y
  avait rien à arbitrer, seulement un fait devenu faux.
- theorie · Rappels · **paracétamol** : « Paracétamol 1g QID, tramadol si insuffisant » → « 1 g
  × 3-4/j — **plafond 4 g/j, ramené à 3 g/j** en cas de consommation chronique d'alcool (**le cas
  ici : 1-2 bières par jour**), de poids < 50 kg ou d'insuffisance hépatique ; tramadol en réserve ».
  Le patient boit tous les jours et l'alternative aux AINS est un **critère noté** (`m5`) : la
  posologie proposée en remplacement ne pouvait pas rester sans plafond. Précédent AMBOSS-9.
- theorie · Rappels · **allergie à la pénicilline** : « Alternative pénicilline : Métronidazole
  500mg BID » → « **Allergie à la pénicilline — le cas de ce patient** : l'amoxicilline est
  remplacée par métronidazole 500 mg × 2/j ». L'item existait mais ne disait pas qu'il s'appliquait
  à *ce* patient, dont l'allergie est un sous-item noté (`a7` — « Allergies [Pénicilline] »).
- resume · Traitement médical : la trithérapie d'éradication portait « IPP + amoxicilline +
  clarithromycine » **sans mention de l'allergie**. Ajout de « — **si allergie à la pénicilline :
  IPP + clarithromycine + métronidazole** », et de la durée (14 j) qui n'était que dans `theorie`.
  Le bloc canonique, celui que l'étudiant révise, proposait à ce patient un antibiotique auquel il
  est allergique.
- theorie · Rappels · notation et molécule : « BID », « QID » → « × 2/j », « × 3-4/j » (précédents
  AMBOSS-6 et 9) ; « Oméprazole 80mg bolus » → « **ésoméprazole** 80 mg en bolus », aligné sur le
  critère noté `m5` (« IPP IV: Ésoméprazole 80 mg bolus puis 8 mg/h ») — **niveau 2**, la page SSP
  ne nomme pas de molécule pour l'ulcère.

*Prise en charge de l'hémorragie — le canonique reçoit ce que `theorie` cessait de porter*

- resume · Prise en charge : **nouvelle sous-section « Hémorragie active — urgence »**. Le bloc
  canonique ne portait que la prise en charge de l'ulcère chronique alors que la station est un
  méléna : deux voies veineuses de gros calibre et remplissage, bilan initial (FSC, groupe + RAI et
  commande de CE, crase, chimie), IPP IV à forte dose sans attendre l'endoscopie, endoscopie < 24 h
  (< 12 h si instabilité) avec hémostase, transfusion si Hb < 70 g/L ou instabilité. Report
  **préalable** à la réécriture de `theorie` (règle d'anti-perte).
  source : SSP — PRISE EN CHARGE — « **2 voies veineuses périphériques de gros calibre (≥ 16-18 G)**,
  monitoring continu » et « **Transfusion de CE** selon stratégie restrictive » ; section notée `m5`
  — « Voie veineuse périphérique gros calibre: (18G) », « IPP IV: Ésoméprazole 80 mg bolus puis
  8 mg/h », « Endoscopie digestive haute dans les 24h »
- theorie · Prise en charge de l'HDH : la check-list numérotée de six points était **actionnable
  dans `theorie`** et doublait ce que `resume` porte désormais. Réécrite en *pourquoi* : pourquoi la
  réanimation précède l'enquête étiologique (on perd du sang total), pourquoi l'hémoglobine initiale
  est faussement rassurante (l'hémodilution demande des heures), pourquoi la stratégie
  transfusionnelle est restrictive, pourquoi l'IPP avant l'endoscopie stabilise le caillot sans
  dispenser du geste, pourquoi l'érythromycine précède l'endoscopie, et ce que signe le rapport
  urée/créatinine. Axe 2.
  source : SSP — Cartes ECOS — « on perd du sang TOTAL : l'urgence est de restaurer la volémie
  […] une stratégie transfusionnelle RESTRICTIVE améliore la survie » et « se fier à l'Hb initiale :
  elle est faussement normale au début » ; SSP — Cartes ECOS — « l'urée monte, alors que la
  créatinine reste normale »
- theorie · Prévention secondaire : les six mesures redisaient `resume` au même format. Remplacées
  par le rationnel — les 60 % de récidive à un an sans éradication, la gastroprotection qui ne
  remplace pas l'arrêt des AINS et le COX-2 qui perd son bénéfice sous aspirine, le tabac qui
  retarde la cicatrisation, le contrôle endoscopique qui exclut surtout un cancer ulcériforme
  (lequel cicatrise aussi sous IPP), et le contrôle d'éradication à faire IPP arrêté. Axe 2.
- resume · Suivi : ajout de « **Surveillance de l'hémoglobine et correction de la carence martiale
  si anémie** » et de « IPP arrêté » sur le contrôle d'éradication — les deux venaient de `theorie`
  et n'avaient pas d'équivalent dans le canonique.

*Seuil transfusionnel de la cardiopathie ischémique (niveau 1) — corrigé au fix round 1/5*

- theorie · Prise en charge de l'HDH : « transfusion si Hb < 70 g/L (**< 90 si coronarien**) » →
  « transfusion si Hb < 70 g/L, **seuil relevé à < 80 g/L en cas de cardiopathie ischémique** ».
  La page SSP tranche explicitement le point, et deux fois : **niveau 1**, elle fait foi. La borne
  de 90 g/L ne venait d'aucune source — ni de la page SSP, ni de la section notée, qui dit seulement
  « Transfusion si Hb: 70 g/L ou instabilité ». Le terme « coronarien » est également remplacé par
  « cardiopathie ischémique », la formulation de la page.
  source : SSP — PRISE EN CHARGE — « **Transfusion de CE** selon stratégie restrictive : seuil Hb
  < 70 g/L (**< 80 g/L si cardiopathie ischémique**) » ; SSP — Cartes ECOS, « HDB sévère — mesures
  initiales de réanimation et seuil transfusionnel ? » — « transfusion si Hb < 70 g/L
  (**< 80 si cardiopathie ischémique**) »
  historique : la clause existe depuis l'import (`main` : « < 7 g/dL (< 9 si coronarien) ») et a été
  convertie telle quelle par la passe unités (`5f9aafc` : « < 70 g/L (< 90 si coronarien) »). La
  conversion était juste au facteur 10 près ; c'est la valeur d'origine qui divergeait de la page.
  **Piège d'outillage à retenir** : `lib.visible_text()` supprime tout ce qui suit un `<` nu
  jusqu'au `>` suivant — dans « Hb < 70 g/L (< 90 si coronarien)</li> », le `<` ouvre une
  pseudo-balise qui court jusqu'au `>` de `</li>` et avale la clause entière. Toute recherche
  passant par `visible_text` sur le fichier entier renvoie **zéro occurrence** de « coronarien ».
  `report_redundancy.py` et `check_no_loss.py` y échappent (leur `list_items` capture l'intérieur du
  `<li>`, sans le `</li>`), mais une vérification écrite à la main sur `visible_text` produit un faux
  négatif. Chercher ces seuils sur le HTML brut après `strip_base64`, pas sur le texte visible.

*Alignement du délai de contrôle endoscopique (niveau 2)*

- resume · Suivi et presentation · Q3 : « Contrôle endoscopique à **8–12** semaines » → « à **6–8**
  semaines ». Les trois blocs pédagogiques se contredisaient (`theorie` disait 6-8, `resume` et
  `presentation` 8-12). La page SSP, consacrée à l'hémorragie **basse**, ne fixe aucun délai de
  contrôle d'un ulcère gastrique : **niveau 2**, la section notée fait foi.
  source : section notée `m5` — « Contrôle endoscopique à 6-8 semaines »

*Axe 6 — `presentation`/Pièges ECOS supprimée, après report*

- expert · Pièges : « Ne pas proposer d'alternative aux AINS » → « **Ne pas arrêter les AINS**, ou ne
  pas proposer d'alternative antalgique (paracétamol) ». Report obligatoire avant suppression : la
  sous-section supprimée portait « Oublier d'arrêter les AINS », qui n'était nulle part dans
  `expert`/Pièges — l'arrêt n'y figurait que par son corollaire antalgique.
- expert · Pièges : **ajout** de « **Confondre un méléna vrai avec des selles foncées par le fer, le
  bismuth ou la betterave : confirmer l'aspect goudronneux et fétide** ». **Niveau 1**, piège
  explicite de la page SSP sur le symptôme même de la station, absent de toute la grille.
  source : SSP — Pièges — « Confondre **méléna vrai** avec selles foncées (betterave, fer) —
  toujours confirmer l'aspect goudronné fétide et reclasser en HDA » ; SSP — frontmatter
  `pieges_eliminatoires` — « Confondre rectorragie et méléna »
- presentation · **Pièges ECOS supprimée** (axe 6). Les deux autres items étaient déjà dans
  `expert`/Pièges : « Ne pas faire de TR » (à l'identique, et repris par le N du mnémo MELENA) et
  « Retarder l'endoscopie en cas de patient "pressé" ».

*Dédoublonnage (contrat de blocs, règle du format)*

- presentation · mnémo **MELENA** : `mnemo-box` **déplacée** de la Checklist mentale vers Touches
  ludiques (axe 5), sans toucher à ses clés ni à ses valeurs. C'est le mnémo le plus complet de la
  grille.
- presentation · **Classification de Forrest supprimée** de Touches ludiques : les six stades y
  étaient recopiés de `theorie` au même format, avec les mêmes pourcentages. La version conservée
  (`theorie`) est la plus riche — elle nomme correctement les taches « pigmentées » et rattache le
  stade III au cas du patient. Anti-perte vérifiée stade par stade.
- presentation · Q1 « Quels examens », Q2 « Traitement », Q3 « Suivi » : les trois listes deviennent
  des **réponses orales**. Contenu intégralement repris, et complété de ce que le canonique porte
  désormais : la substitution du métronidazole chez ce patient allergique, le contrôle
  d'éradication IPP arrêté, le délai de 6-8 semaines, la prudence sur l'alcool pour le paracétamol.
  Axes 1 et 2.
- resume · Hémorragie active : la posologie exacte de l'IPP IV reste dans `theorie`/Rappels
  thérapeutiques (section de queue, rôle de référence posologique) ; `resume` porte la stratégie et
  y renvoie.

**Divergences consignées**

- **section notée `m5` · acide tranexamique** : « Acide tranexamique: 1g IV si saignement actif ».
  L'essai HALT-IT (2020) n'a montré aucun bénéfice de l'acide tranexamique dans l'hémorragie
  digestive, avec un excès d'événements thrombo-emboliques veineux ; il n'est plus recommandé dans
  cette indication. Divergence **interne à une section notée** : consignée, **non corrigée** (barème
  gelé) — signalée pour arbitrage.
- **section notée `m3` · test H. pylori** : « **Test d'anticorps** H. pylori ». La sérologie ne
  distingue pas l'infection active d'une infection passée ; les blocs pédagogiques disent, eux,
  « test respiratoire à l'urée, antigène fécal ou biopsie », ce qui est correct. Le pédagogique n'a
  **pas** été aligné sur la section notée (l'aligner l'aurait dégradé) : divergence consignée,
  section notée inchangée.
- **section notée `m5` · « Si cancer • Contrôle endoscopique à 6-8 semaines »** : le contrôle
  endoscopique à 6-8 semaines est celui de l'**ulcère gastrique**, pas du cancer. L'intitulé de la
  rubrique paraît interverti avec « Si ulcère ». Consigné, non corrigé.
- **section notée `m5` · signes de comparaison manquants** : « Transfusion si Hb: 70 g/L », « Objectif:
  TA  90/60 mmHg, FC  100/min ». Les « < » et « > » ont disparu. Même nature que le « 4cm »
  d'AMBOSS-6 et l'« IMC 25 kg/m² » d'AMBOSS-9. Consigné, non corrigé.
- **cinq paires de redondance restantes**, toutes acceptées : le M du mnémo MELENA face à
  `expert`/Points clés (liste → mnémo, changement de format de restitution) et quatre arguments
  POUR/CONTRE face à des items de `resume` (liste → argumentaire structuré).
- **page SSP de référence** : le mapping rattache cette station d'hémorragie digestive **haute** à
  la page « Rectorragies & Hémorragie Digestive Basse ». La page couvre le méléna et sa reclassification
  en HDA, mais sa section PRISE EN CHARGE vise l'HDB ; la page « SSP — Nausées, Vomissements &
  Hématémèse » porte, elle, l'algorithme d'HDH complet (pantoprazole 80 mg puis 8 mg/h, Rockall,
  Forrest). Aucune n'a été substituée à l'autre — le mapping est le choix de l'utilisateur —, mais
  un rattachement complémentaire mérite d'être arbitré.

**Signalements de sécurité** — quatre, tous corrigés ci-dessus, plus un non corrigé (barème gelé) :
anti-H2 retiré du marché mondial en 2020 encore proposé en alternative aux IPP ; paracétamol sans
plafond journalier chez un buveur quotidien, alors que c'est l'antalgique de remplacement noté ;
trithérapie d'éradication à l'amoxicilline dans le bloc canonique d'un patient allergique à la
pénicilline ; seuil transfusionnel du cardiopathe ischémique porté à 90 g/L au lieu de 80, soit une
stratégie plus libérale que celle de la page de référence sur un patient qui saigne. **Non corrigé** :
acide tranexamique dans l'hémorragie digestive (section notée).

### AMBOSS-22 — Dysphagie, femme de 60 ans, adénocarcinome de l'œsophage sur Barrett (page SSP : Dysphagie)

Redondance : **13 paires → 3** (`report_redundancy.py AMBOSS-22_`). Quatre blocs présents.
Pas de sous-section `presentation`/Pièges ECOS — vérifié, la grille n'est pas de l'axe 6.

**Modifications**

*Vignette — trois erreurs factuelles dans la Version longue (niveau 2)*

- presentation · Version longue : « elle **ne fume pas** et consomme occasionnellement de l'alcool »
  → « elle **fume un demi-paquet par jour depuis 32 ans** et boit une à deux bières le week-end ».
  Le tabagisme est un sous-item **noté** (`a10` — Habitudes et mode de vie), c'est un facteur de risque
  central du cas, et « Conseil sur l'arrêt du tabac » est lui-même noté (`m5`) : la présentation
  orale affirmait le contraire de la vignette. La version SBAR du même bloc disait, elle,
  « tabagisme chronique » — le bloc se contredisait.
  source : section notée `a10` — « Tabac [Oui, je fume un demi-paquet par jour depuis 32 ans] » et
  « Alcool [J'ai peut-être 1-2 bières le week-end] »
- presentation · Version longue : « elle est connue pour une **hypertension artérielle, traitée par
  inhibiteur calcique** » → « elle est connue pour un **reflux gastro-œsophagien qui évolue depuis
  18 ans**, qu'elle traite seule par antiacides (Rennie®), sans avoir jamais eu d'IPP ni
  d'endoscopie ». L'hypertension et son traitement n'existent nulle part dans la station ; le RGO
  ancien non traité est **l'** antécédent du cas (`a5` Antécédents médicaux, `a7` Médicaments) et la
  clé du Barrett.
- presentation · Version longue : « sa mère a eu un **cancer gastrique** » → « sa mère a une
  **diverticulose colique** ». L'antécédent familial est noté (`a9`) et sans
  rapport avec le diagnostic : l'erreur fabriquait un argument en faveur du cancer.

*Renforcement du canonique (niveau 1)*

- resume · Anamnèse : **nouvelle sous-section « Signes d'alarme (red flags) »**. Le bloc canonique
  n'en portait aucune alors que toute la station repose sur eux — progression rapide et passage des
  solides aux liquides, amaigrissement, anémie, âge > 50 ans, **impaction alimentaire (urgence
  endoscopique, 144)**, fausses routes et pneumopathies récidivantes. Report préalable des cinq
  items de `presentation`/Red flags (règle d'anti-perte).
  source : SSP — Signes d'alarme — « amaigrissement, anémie, âge > 50 ans, impaction, fausses
  routes » ; SSP — Red flags — « **Impaction alimentaire aiguë** avec impossibilité d'avaler la
  salive → urgence endoscopique · **144** »
- resume · Examens diagnostiques : ajout de « en **première intention** devant toute dysphagie » sur
  l'endoscopie, de « **Jamais de traitement d'épreuve par IPP** devant une dysphagie : il atténue les
  symptômes et retarde le diagnostic de cancer de plusieurs mois », et de « **Manométrie seulement
  après une endoscopie normale** — jamais avant, sous peine de méconnaître une pseudo-achalasie
  tumorale du cardia ». Les deux règles sont les pièges éliminatoires n° 1 et n° 4 de la page SSP et
  n'étaient portées par aucun bloc canonique.
  source : SSP — Règle d'or — « Toute **dysphagie** est un signe d'alarme → **OGD**, jamais de test
  IPP d'épreuve. […] L'**OGD** précède toujours la manométrie pour éliminer une pseudo-achalasie
  tumorale » ; SSP — frontmatter `pieges_eliminatoires`

*Dédoublonnage (contrat de blocs, règle du format)*

- presentation · mnémo **DYS-PHA-GIE** : `mnemo-box` **déplacée** de la Checklist mentale vers
  Touches ludiques (axe 5), clés et valeurs intactes.
- presentation · « ⚠️ Red flags de dysphagie » : la liste de cinq items recopiait `resume` au même
  format. Après report dans le canonique, elle est remplacée par le **mnémo « OÙ ? et QUOI ? »**,
  celui de la page SSP — siège et timing d'un côté, type d'aliment de l'autre, avec la progression
  solides → liquides qui doit faire peur et le rappel que le siège désigné par la patiente est
  trompeur. Changement de format de restitution (liste → mnémo), précédent AMBOSS-9/FRONT.
  source : SSP — Mnémoniques — « **Dysphagie** — 2 questions clés : **OÙ ?** […] et **QUOI ?** » ;
  SSP — Pièges — « Se fier au **siège désigné** par le patient […] plutôt qu'au **timing** »
- presentation · « Facteurs de risque cancer œsophagien » **supprimée** : ses deux items doublaient
  `theorie`/Cancer de l'œsophage au même format. Anti-perte vérifiée : le « régime pauvre en
  fruits/légumes » est dans `resume`/Facteurs de risque.
- presentation · « ⚡ Diagnostic clé » **supprimée** : « Endoscopie + biopsies = toujours première
  étape » est désormais dans `resume`/Examens diagnostiques et dans `expert`/Points clés ; « Transit
  baryté utile si suspicion trouble fonctionnel » est dans `theorie`/Approche diagnostique.
- expert · Points clés : « Endoscopie avec biopsies = gold standard diagnostic » → « **L'endoscopie
  avec biopsies est ce qu'on attend du candidat d'emblée, avant tout transit baryté** ». Axe 7 :
  `expert` dit ce que l'examinateur observe, `resume` ce que l'étudiant retient — les deux disaient
  la même phrase.
- presentation · Q1 « Quels examens », Q2 « Traitement », Q3 « Suivi » : les trois réponses en liste
  deviennent des **réponses orales**, complétées de l'ordre des examens (endoscopie d'abord, transit
  baryté et manométrie seulement après une endoscopie normale). L'« analyse orale » et l'« astuce
  révision » attenantes sont conservées, elles portent le *pourquoi* et la mémorisation. Axes 1 et 2.

**Divergences consignées**

- **section notée `m2` · transit baryté en première intention** : le critère « Examens
  complémentaires de première intention » place le **transit baryté** au même rang que la FOGD
  (« meilleur test initial pour suspicion d'anneau œsophagien et achalasie »). La page SSP tranche
  l'inverse — l'OGD est le premier examen de toute dysphagie, le TOGD ne venant que pour un Zenker,
  un trouble moteur ou une contre-indication —, et `expert`/Pièges compte « Faire transit baryté
  avant endoscopie » parmi les pièges. Le **pédagogique a été maintenu sur la page SSP** (niveau 1) ;
  la section notée est consignée, **non corrigée** (barème gelé).
  source : SSP — EXAMENS COMPLÉMENTAIRES — « **OGD (endoscopie haute) = 1ᵉʳ examen** devant une
  dysphagie œsophagienne » ; SSP — Points Clés ECOS — « Toute dysphagie = signe d'alarme → OGD »
- **trois paires de redondance restantes**, toutes acceptées : deux items de `resume` face à des
  arguments POUR (liste → argumentaire structuré) et une collision fortuite entre le piège
  « Oublier ECG (douleur thoracique) » et l'argument « Douleur thoracique ».

**Signalements de sécurité** — aucun signalement médicamenteux. Les trois erreurs de vignette
corrigées ci-dessus valent toutefois signalement pédagogique : la Version longue est ce que
l'étudiant récite, et elle inversait le statut tabagique de la patiente.

### AMBOSS-15 — Douleur abdominale chronique, garçon de 6 ans, maladie cœliaque (page SSP : à créer — alignement des PEC reporté)

Redondance : **8 paires → 3** (`report_redundancy.py AMBOSS-15_`). Quatre blocs présents.
Pas de sous-section `presentation`/Pièges ECOS — vérifié, la grille n'est pas de l'axe 6.

**Traitement partiel, assumé.** `docs/obsidian-mapping.yaml` place cette grille dans la liste
`unmapped`, avec la raison « douleur abdominale pédiatrique — **page pédiatrique à créer** ». La page
de référence **n'existe pas encore** : ce n'est pas qu'une page inadéquate ait été écartée, c'est
qu'aucune n'a encore été écrite pour ce motif. L'**étape 4 d'alignement des prises en charge n'a donc
pas été appliquée** : seul le dédoublonnage du § 3 l'a été, plus les corrections factuelles internes,
qui ne passent pas par la hiérarchie. Les zones restées **sans arbitre** sont listées en fin d'entrée
— elles constituent, telles quelles, la liste de ce que la future page pédiatrique devra trancher.

**Modifications**

*Dédoublonnage (contrat de blocs, règle du format)*

- theorie · Prise en charge de la maladie cœliaque : les six mesures étaient une **check-list
  actionnable dans `theorie`** et doublaient `resume`/Prise en charge. Réécrites en *pourquoi* :
  pourquoi l'éviction doit être totale (quelques dizaines de milligrammes par jour entretiennent
  l'atrophie), pourquoi la contamination croisée explique l'essentiel des échecs — bien plus que les
  écarts assumés —, pourquoi la diététicienne n'est pas un supplément de confort, pourquoi la
  supplémentation est transitoire, pourquoi la sérologie sert autant à l'observance qu'au
  diagnostic, et pourquoi l'absence d'amélioration à quelques semaines ne justifie pas de
  réintroduire le gluten. Axe 2.
- resume · Éducation et suivi : ajout de « **Contrôle sérologique tTG-IgA à 6 mois, 12 mois, puis
  annuel** » et de « **Normalisation attendue : muqueuse en 6 à 24 mois, rattrapage de la croissance
  chez l'enfant** ». Les deux venaient de `theorie` et n'avaient aucun équivalent dans le canonique :
  report **préalable** à la réécriture (règle d'anti-perte).
- resume · Anamnèse : **nouvelle sous-section « Drapeaux rouges (douleur abdominale chronique de
  l'enfant) »**, qui recueille les cinq items de `presentation`/Drapeaux rouges pédiatriques — perte
  de poids ou cassure de croissance, selles graisseuses ou sanglantes, fièvre persistante, douleurs
  nocturnes réveillant l'enfant, fatigue inhabituelle avec pâleur et intolérance à l'effort. Le
  canonique n'en portait aucun alors que c'est ce qui sépare l'organique du fonctionnel dans cette
  station. La sous-section de `presentation` est ensuite supprimée (donnée clinique, pas touche
  ludique).
- theorie · Approche globale : « Drapeaux rouges : perte poids, sang, fièvre, réveil nocturne » →
  « **Les drapeaux rouges font basculer vers l'organique ; leur absence, elle, ne suffit pas à
  conclure au fonctionnel** ». La liste vit désormais dans `resume` ; `theorie` en garde la valeur
  discriminante — ce qui compte dans un cas où 90 % des douleurs sont fonctionnelles et où l'enfant
  a bel et bien une cause organique.
- presentation · mnémo **PAIN** : `mnemo-box` **déplacée** de la Checklist mentale vers Touches
  ludiques (axe 5), à côté des mnémos 3A et BSA. Clés intactes ; « Paleur » corrigé en « **Pâleur** ».
- presentation · Q1 « Quels examens », Q2 « Traitement », Q3 « Suivi » : les trois listes deviennent
  des **réponses orales**. Contenu intégralement repris, et complété de ce que porte le canonique :
  la raison du dosage simultané des IgA totales, le fait que la supplémentation est transitoire, et
  la coexistence possible de l'anxiété de séparation avec la maladie cœliaque — sans qu'elle en soit
  l'explication. Axes 1 et 2.
- theorie · Présentation clinique pédiatrique : « Manifestations extra-intestinales : dermatite
  herpétiforme » → « Manifestations extra-intestinales **de l'enfant** : dermatite herpétiforme,
  **aphtose buccale récidivante, hypoplasie de l'émail dentaire définitif** ». L'item doublait
  `resume`/Manifestations extra-digestives ; il porte maintenant ce que `resume` ne dit pas et qui
  est propre à l'âge.

*Contradiction entre deux blocs pédagogiques — le contrat tranche*

- resume · Points clés : « Biopsies duodénales nécessaires avant de débuter le régime » → « …
  **chez l'enfant, les critères ESPGHAN autorisent seuls de s'en passer (tTG ≥ 10× la norme +
  anti-endomysium positifs)** ». `resume` posait la biopsie comme absolue là où `theorie` mentionnait
  la voie sans biopsie : **`resume` est canonique**, il reçoit donc la nuance plutôt que `theorie` ne
  perde l'information. La nuance ne change rien pour cet enfant (tTG 85 U/mL pour une norme < 20,
  soit environ 4× — la biopsie reste nécessaire).

**Divergences consignées**

- **alignement des prises en charge non appliqué**, la page de référence restant à écrire. Les zones
  restées **sans arbitre**, à reprendre dès que la page pédiatrique existera :
  1. `theorie`/Rappels thérapeutiques — les **posologies pédiatriques au poids** : fer élément
     3-6 mg/kg/j, acide folique 1 mg/j × 3 mois, vitamine D 800-1000 UI/j, calcium 500-1000 mg/j.
     Elles sont plausibles et le fer est bien rapporté au poids, mais **aucune source du vault ne les
     arbitre** ; la vitamine D à 800-1000 UI/j est une dose d'entretien plutôt que de correction
     d'une carence avérée. Non modifiées.
  2. `theorie`/Rappels — « **Probiotiques** : souches spécifiques peuvent aider transition », item
     sans molécule, sans indication et sans niveau de preuve. Non modifié, non supprimé (rien ne
     l'arbitre, et il ne porte aucun risque).
  3. `resume`/Prise en charge — « **Réintroduction des produits laitiers après 6 mois** si
     intolérance secondaire au lactose » : délai non arbitré.
  4. `theorie`/Diagnostic — le seuil ESPGHAN et la place de l'HLA-DQ2/DQ8 : cohérents entre eux et
     avec `resume` après la modification ci-dessus, mais sans page de référence pour les confirmer.
  5. L'ensemble du versant **psychosocial** (trouble anxieux de séparation, TCC, soutien parental),
     qui est un critère noté (`m5`) et n'a de page SSP correspondante ni en gastro ni en pédiatrie.
- **section notée `m3` · panel IgE** : « Panel IgE allergies pédiatriques » est proposé au motif d'un
  antécédent familial d'allergie aux arachides, alors que la vignette ne rapporte aucune association
  entre les symptômes et un aliment. L'examen ne serait pas de première intention hors de ce
  contexte. Consigné, **non corrigé** (barème gelé).
- **trois paires de redondance restantes**, toutes acceptées : deux collisions de check-list face à
  des arguments POUR (liste → argumentaire structuré) et la description des biopsies dans `resume`
  face au **résultat de station** d'`expert` (« Marsh 3b »), qui sont deux rôles distincts.

**Signalements de sécurité** — aucun. La relecture pédiatrique demandée (posologies au poids) n'a
trouvé **aucune dose adulte ni dose sans référence au poids** : la seule posologie pondérale de la
grille, le fer, est correctement exprimée en mg/kg/j ; il n'y a **pas de paracétamol** dans cette
grille. Les quatre posologies sont néanmoins listées ci-dessus comme non arbitrées, faute de page de
référence.

### AMBOSS-28 — Prise de poids, homme de 45 ans, trouble dépressif majeur avec hypothyroïdie comorbide (page SSP : Syndrome Métabolique)

Redondance : **17 paires → 4** (`report_redundancy.py AMBOSS-28_`). Quatre blocs présents.
Pas de sous-section `presentation`/Pièges ECOS — vérifié, la grille n'est pas de l'axe 6.

La page SSP est rattachée au **motif** (prise de poids) et non au diagnostic final : elle tranche
l'exploration d'une prise de poids, pas la prise en charge d'une dépression. L'arbitrage des points
psychiatriques est donc passé au niveau 2 (section notée), celui des points métaboliques au niveau 1.

**Modifications**

*Correction factuelle (interne au bloc)*

- resume · Points clés : « Prise de poids inexpliquée = penser à un trouble dépressif majeur,
  **surtout si appétit augmenté** » → « …, que l'appétit soit augmenté (forme atypique) ou diminué —
  une prise de poids **avec perte d'appétit** oriente d'abord vers une hypothyroïdie ». Le patient de
  la station a une **perte** d'appétit (`a3` — « Je n'ai pas eu beaucoup d'appétit dernièrement ») et
  `expert`/Points clés dit « Prise de poids + perte appétit = atypique pour TDM » : le point clé
  canonique orientait l'étudiant à l'inverse du cas. Même correction portée sur
  resume · Symptômes typiques (« Hyperphagie ou grignotage émotionnel » complété de l'alternative).

*Alignement des prises en charge*

- theorie · Rappels thérapeutiques · **niveau 2, sécurité** : « Hypothyroïdie : lévothyroxine
  1.6 μg/kg/j » → ajout de « initiation prudente à 25-50 μg/j puis paliers de 25 μg au-delà de
  50 ans ou en cas de cardiopathie — une dose pleine d'emblée peut démasquer un angor ou un trouble
  du rythme ». Le bloc prescrivait la dose pleine sans condition, alors que la section notée
  conditionne l'initiation à l'âge et au terrain.
  source : section notée `m6` — « Lévothyroxine: 25-50 μg/j initial si 50 ans · 1.6 μg/kg/j si jeune
  et sain · Ajustement par paliers de 25 μg »
- resume · Prise en charge · **niveau 2** : « ISRS (ex. : sertraline, **fluoxétine**) » →
  « ISRS (**sertraline, citalopram**), dose initiale faible puis augmentation progressive ». La
  section notée et `theorie` nomment tous deux citalopram ; `resume`, canonique, était seul à
  proposer la fluoxétine.
  source : section notée `m6` — « Pharmacothérapie: ISRS (sertraline, citalopram) · Dose initiale
  faible, augmentation progressive »
- resume · Surveillance · niveau 2 : « Suivi des effets indésirables des traitements » précisé de
  « réévaluation à 4-6 semaines ; TSH à 6-8 semaines si lévothyroxine ».
  source : section notée `m6` — « Surveillance effets secondaires 4-6 semaines · Contrôle TSH à
  6-8 semaines »

*Renforcement du canonique (niveau 1)*

- resume · Prise en charge : ajout de « Corriger la cause organique associée : **lévothyroxine si
  hypothyroïdie confirmée** » — le diagnostic de la station est « TDM **avec hypothyroïdie
  comorbide** » et le bloc canonique ne portait aucun traitement du versant endocrinien.
- resume · Prise en charge : ajout du **filet de sécurité** — « urgences ou **144** en cas d'idées
  suicidaires ; **143 (La Main Tendue)** joignable 24 h/24 ». Le 143 n'existait nulle part dans la
  grille.
  source : SSP — En Bref — « **Numéros utiles** : **144** urgences · **143** La Main Tendue » ;
  section notée, Clôture — « venez aux urgences immédiatement […] appelez s'il vous plaît le 144 »
- resume · Examens diagnostiques : la liste passe de trois à cinq items — **T4 libre**, **FSC**,
  **ionogramme avec calcium et magnésium**, seuil du **tour de taille ≥ 102 cm**, et une ligne
  « selon l'orientation » portant la **polysomnographie (STOP-BANG ≥ 3)** et le **cortisol libre
  urinaire des 24 h / freinage à la dexaméthasone 1 mg**. Aucun n'était dans le bloc canonique alors
  que tous figurent en section notée et dans `presentation`.
  source : SSP — EXAMENS COMPLÉMENTAIRES — « Polygraphie ventilatoire / polysomnographie si suspicion
  SAOS (questionnaire **STOP-BANG ≥ 3**) » ; SSP — Red flags — « Cortisol libre urinaire 24 h ou test
  à la **dexaméthasone 1 mg overnight** » ; SSP — Critères diagnostiques — « Tour de taille : ≥ 102 cm (H) »
- theorie · Apnée obstructive du sommeil : « Traitement : CPAP, perte poids, chirurgie » → seuil et
  alternative ajoutés (« CPAP si **IAH ≥ 15** ou forme symptomatique […] orthèse d'avancée
  mandibulaire si intolérance »), la chirurgie étant conservée en dernier recours (anti-perte).
  source : SSP — PRISE EN CHARGE — « SAOS modéré à sévère (IAH ≥ 15) : CPAP nocturne […] orthèse
  d'avancée mandibulaire en cas d'intolérance CPAP »

*Dédoublonnage (contrat de blocs, règle du format)*

- presentation · mnémo **SIGECAPS** : la `mnemo-box` de la Checklist mentale est **supprimée**, ses
  gloses françaises reportées au préalable sur la liste de Touches ludiques, qui reste seule
  porteuse du mnémo — clés anglaises conservées, traduction en valeur. Précédent AMBOSS-1/6F. Axe 5.
- theorie · Critères diagnostiques DSM-5 : la liste des neuf items SIGECAPS, qui doublait `resume` au
  même format, devient la **règle de comptage** (≥ 5 sur 9, ≥ 2 semaines, au moins un des deux
  symptômes cardinaux, retentissement fonctionnel, cause organique exclue, PHQ-9 gradue sans
  diagnostiquer). Anti-perte : les neuf items subsistent en français dans `resume` et avec leurs clés
  anglaises dans `presentation`/Touches ludiques ; « Au moins 1 : humeur dépressive OU anhédonie » est
  conservé et développé. Axe 1.
- presentation · Q1 « Quels examens », Q2 « Traitement », Q3 « Suivi » : les trois réponses en liste
  deviennent des **réponses orales**. L'« analyse orale » et l'« astuce révision » attenantes sont
  conservées. Axes 1 et 2.
- expert · Points clés : « Évaluation systématique risque suicidaire » → « **L'examinateur attend que
  le risque suicidaire soit abordé explicitement, par une question directe** : idées actuelles,
  scénario et moyens, facteurs protecteurs, puis plan de sécurité — l'omettre est éliminatoire ».
  Axe 7 : `expert` dit ce que l'examinateur observe, `resume` ce que l'étudiant retient.
  source : section notée `m4` — « Évaluation des idées suicidaires actuelles · Recherche de facteurs
  de risque · Évaluation des facteurs protecteurs · Plan de sécurité si risque élevé »

**Risque suicidaire — traitement volontairement conservateur.** Aucun item relatif au risque
suicidaire n'a été supprimé, y compris lorsque la redondance était détectée. Les deux paires
restantes sur ce thème (`resume`/« S : idées suicidaires » face au mnémo de Touches ludiques et aux
arguments POUR) sont **acceptées et documentées**, le coût d'une répétition y étant sans commune
mesure avec celui d'une omission. `theorie`/Évaluation du risque suicidaire est resté intact.

**Divergences consignées**

- **section notée `m6` · lévothyroxine** : « Lévothyroxine: 25-50 μg/j initial **si 50 ans** » — le
  signe de comparaison manque, la condition d'âge est donc illisible (lire « si > 50 ans »). Même
  nature que le « IMC 25 kg/m² » d'AMBOSS-9 et le « ou 4cm » d'AMBOSS-6. Consigné, **non corrigé**
  (barème gelé). La condition a été rendue explicite dans `theorie`, où elle est modifiable.
- **section notée et scénario · unités impériales** : le poids du patient est exprimé en **livres**
  (« J'ai pris au moins 7-10 livres », « je pèse plus de 200 livres »), dans un `criteria-text` et
  dans le scénario du patient standardisé — deux zones intouchables. Consigné, **non corrigé**.
- **quatre paires de redondance restantes**, toutes acceptées : deux mnémos face à `resume` (règle
  des mnémos, clé conservée) et deux items de `resume` face à des arguments POUR (liste →
  argumentaire structuré, précédent AMBOSS-22).

**Signalements de sécurité** — un signalement, corrigé : la **lévothyroxine à pleine dose d'emblée**
sans réserve d'âge ni de terrain cardiaque dans `theorie` (même famille que la gabapentine
d'AMBOSS-9). Corrigé par alignement de niveau 2. Le « si 50 ans » de la section notée reste, lui,
non corrigé et consigné ci-dessus.

### AMBOSS-30 — Mal de gorge, homme de 19 ans, pharyngite à streptocoque du groupe A (page SSP : Mal de Gorge (Angine))

Redondance : **18 paires → 4** (`report_redundancy.py AMBOSS-30_`). Quatre blocs présents.
Grille de l'**axe 6** : sous-section `presentation`/Pièges traitée avec l'anti-perte.

**Modifications**

*Alignement des prises en charge — niveau 1, sécurité*

- resume · Antibiothérapie : « **Amoxicilline** per os pendant **6 jours** (1ʳᵉ intention) ·
  Alternative : macrolide si allergie » → « **Pénicilline V (Ospen®) 500 mg × 2-3/j pendant
  10 jours — 1ʳᵉ ligne en Suisse** · Alternative : amoxicilline 1 g × 2/j × 10 jours · Allergie à la
  pénicilline : **clarithromycine ou clindamycine** — pas de macrolide en 1ʳᵉ ligne (résistances du
  SGA) ». Le bloc **canonique** plaçait l'amoxicilline en première intention dans une station dont la
  mononucléose est le diagnostic différentiel principal, dont la rate est « limite palpable » en
  `expert`, et dont la page SSP fait de l'ampicilline en MNI son piège éliminatoire n° 2.
  source : SSP — PRISE EN CHARGE — « **Pénicilline V (Ospen®/Stabicilline®) 10 jours (1ʳᵉ ligne CH)**
  — éviter les macrolides en 1ʳᵉ ligne (résistance) · Alternative : amoxicilline 50 mg/kg/j × 6-10
  jours · Allergie pénicilline : clarithromycine ou clindamycine » ; section notée `m5` —
  « Pénicilline V × 500 mg × 2-3/j × 10 jours »
- resume · Antibiothérapie : ajout de « ⚠️ **Amoxicilline et ampicilline contre-indiquées si
  mononucléose suspectée** : éruption maculo-papuleuse dans 90 % des cas ». La contre-indication
  n'existait que dans `expert`/Points clés, `theorie`/MNI et la Version longue — jamais dans le bloc
  canonique, c'est-à-dire jamais là où l'étudiant révise la prescription.
  source : SSP — Règle d'or — « **MNI = contre-indication à l'ampicilline/amoxicilline** (rash) »
- theorie · Rappels thérapeutiques · **niveau 1, sécurité** : « Paracétamol : **15 mg/kg × 4-6/j**
  pour fièvre/douleur » → « **1 g × 4/j chez l'adulte, sans dépasser 4 g/j** ; 15 mg/kg toutes les
  6 h chez l'enfant ». La posologie était **pédiatrique et sans plafond** dans une station de patient
  de 19 ans : 15 mg/kg six fois par jour représentent 90 mg/kg/j, soit plus de 6 g pour un adulte de
  70 kg, contre 4 g autorisés. Même famille que l'erreur d'AMBOSS-7.
  source : SSP — PRISE EN CHARGE — « **Paracétamol (1 g × 4/j adulte ; 15 mg/kg/6 h enfant)** »
- theorie · Rappels thérapeutiques : « Amoxicilline : 50 mg/kg/j » → forme adulte ajoutée
  (« 1 g × 2/j × 10 j chez l'adulte ; 50 mg/kg/j en 2 prises chez l'enfant, max 2 g/j »).
- theorie : « Si allergie : **azithromycine** 500 mg J1 puis 250 mg × 4j » et « Azithromycine :
  **12 mg/kg/j** × 5j » **supprimés**. Le second était une posologie pédiatrique dans une grille
  adulte et contredisait le premier au sein du même bloc. La page SSP désigne la clarithromycine ou
  la clindamycine, désormais portées par `resume`.
- resume · Traitement symptomatique : posologies adultes explicitées (paracétamol 1 g × 4/j max
  4 g/j, ibuprofène 400 mg × 3/j) et gargarismes salins ajoutés.

*Renforcement du canonique (niveau 1)*

- resume · Examens diagnostiques : le **score de McIsaac est porté en entier** — les quatre items à
  +1, le modificateur d'âge (3-14 ans +1 · 15-44 ans 0 · ≥ 45 ans −1) et les trois seuils (≤ 1 rien ·
  2-3 TDR · ≥ 4 TDR ou antibiothérapie). Le bloc canonique ne portait que « score Centor ≥ 2 », le
  détail vivant dans `theorie` et dans un mnémo.
  source : SSP — Score de McIsaac (Centor modifié), tableau et seuils
- resume · Examen clinique : ajout des **constantes** (T°, FC, FR, SpO₂, hydratation) et surtout de
  la **palpation de la rate** — la splénomégalie est le pivot du diagnostic différentiel de la
  station et le bloc canonique n'en portait pas trace.
  source : SSP — EXAMEN CLINIQUE — « **Splénomégalie** (MNI) » ; `expert` — « Rate : limite palpable »
- resume · Signes de gravité : ajout du drapeau rouge **épiglottite** — « stridor, hypersialorrhée,
  position en tripode → **ne pas examiner la gorge**, appeler l'anesthésiste, 144 ». Absent de toute
  la grille alors que c'est le piège éliminatoire n° 1 de la page SSP.
  source : SSP — Points Clés ECOS — « Suspicion d'épiglottite → **ne pas examiner la gorge**, appeler
  l'anesthésiste » ; SSP — Red flags
- resume · Bilan complémentaire : FSC, frottis sanguin et fiabilité comparée du monospot et de
  l'anti-VCA IgM ajoutés (ils n'existaient qu'en `theorie`, `presentation` et section notée).
- resume · Traitement symptomatique et expert · Pièges : **éviction des sports de contact 3-4
  semaines si MNI** — voir l'anti-perte de l'axe 6 ci-dessous.

*Corrections factuelles (internes aux blocs)*

- presentation · mnémo **CENTOR** : la `mnemo-box` **contredisait le score qu'elle prétendait
  résumer** — « C = Céphalée » (la céphalée n'est pas un critère), « T = Tonsillar swelling
  (**adénopathies sensibles**) » (la tuméfaction amygdalienne et les adénopathies sont **deux**
  critères distincts, confondus en un seul). Le mnémo est **déplacé** vers Touches ludiques et
  reconstruit sur les critères de la page SSP : C = Cough absent · E = Exsudat ou tuméfaction
  amygdalienne · N = Nodes · T = Température · OR = âge, puis les seuils. Clés d'origine conservées,
  traduction en valeur. Axe 5, précédents AMBOSS-2/3.
- presentation · Touches ludiques : la liste « Critères de Centor (4 points clés) » posait
  « Exsudat **ou pétéchies palatines** » comme un même critère. Les pétéchies sont hautement
  évocatrices de SGA mais ne comptent **pas** dans le score : la liste gonflait le score. Fusionnée
  dans le mnémo corrigé ci-dessus ; les pétéchies restent en `resume`/Examen clinique et
  `expert`/Points clés.
- expert · Points clés : « Critères de Centor : fièvre + adénopathies + pas toux + **< 45 ans** » —
  l'âge n'est pas un critère à +1 mais un modificateur, et il vaut **0** entre 15 et 44 ans, donc
  0 pour ce patient de 19 ans. Reformulé en énoncé d'examinateur (axe 7) : « L'examinateur attend que
  le score de McIsaac soit calculé à voix haute avant toute décision de test ou d'antibiotique —
  chez ce patient de 19 ans l'âge ne rapporte aucun point ».
- theorie · « Pétéchies palais mou (**pathognomonique**) » → « hautement suggestives de SGA, mais
  **non pathognomoniques** — on les voit aussi dans la MNI ». `expert` disait déjà « hautement
  suggestif » : le bloc théorique surclassait le signe.

*Dédoublonnage (contrat de blocs, règle du format)*

- presentation · sous-section « ⚠️ Pièges » **supprimée en entier** (axe 6). **Anti-perte
  préalable** : « Éviter amoxicilline si suspicion mononucléose (éruption 90 %) » a été porté dans
  `resume`/Antibiothérapie, où le bloc canonique ne le portait pas ; « Interdiction sport contact
  **3-4 semaines** si MNI » a été porté à la fois dans `resume`/Traitement symptomatique et dans
  `expert`/Pièges, dont l'item « Oublier risque rupture rate si MNI (football) » **ne portait aucune
  durée** — la durée n'existait nulle part ailleurs dans la grille. Reproduction du geste
  β-hCG d'AMBOSS-3.
- theorie · « Critères de Centor modifiés » (10 items chiffrés) → « **Pourquoi le score de
  McIsaac** » : ce que le score mesure, pourquoi la toux et la rhinorrhée le font chuter, pourquoi
  McIsaac ajoute l'âge, et le fait qu'à 4/4 la probabilité de SGA n'est que d'environ 50 % — le score
  sélectionne qui tester, il ne remplace pas le TDR. Le barème chiffré vit désormais dans `resume`
  (canonique) et le mnémo dans `presentation`. Axe 1.
  source : SSP — Cartes ECOS — « les 4 items de Centor sont les signes d'une infection bactérienne
  pyogène […] McIsaac y ajoute l'âge, car le SGA est une maladie de l'enfant. **Piège :** même à 4/4,
  la probabilité de SGA n'est que de ~50 % → le score sélectionne qui tester »
- theorie · « Traitement antibiotique pharyngite SGA » (liste de molécules) → « **Pourquoi ce
  traitement antibiotique** » : absence historique de résistance de *S. pyogenes* à la pénicilline,
  raison des 10 jours (éradication du portage et prévention du RAA, non le confort), mise à l'écart
  des macrolides, bénéfice symptomatique d'environ 16 heures. Les doses restent dans `resume` et
  `theorie`/Rappels. Axe 2.
  source : SSP — Cartes ECOS — « *Streptococcus pyogenes* n'a **jamais développé de résistance à la
  pénicilline** […] Les **10 jours** ne servent pas à raccourcir les symptômes […] mais à **éradiquer**
  le portage pharyngé et prévenir le **RAA** » ; « l'antibiotique ne raccourcit l'angine à SGA que de
  **~16 heures** »
- theorie · « Présentation clinique pharyngite SGA » → « **Ce qui distingue le SGA du viral** » : la
  liste de symptômes doublait `resume` (dont une paire à **1.00**, « adénopathies cervicales
  antérieures douloureuses », identique au caractère près). Ne subsiste que la valeur discriminante,
  avec la fréquence de l'exsudat (50-70 %) qui n'était portée que là. Anti-perte : l'**halitose**,
  absente du canonique, a été portée dans `resume`/Symptômes typiques avant réécriture.
- theorie · « Diagnostic pharyngite streptococcique » **supprimée** : elle doublait la section de
  queue `theorie-section-examens`, que la procédure fait primer. Anti-perte : la **PCR multiplex**,
  qu'elle seule portait, a été portée dans la section de queue avant suppression ; l'ASLO y a été
  fusionné.
- presentation · Q1 « Quels examens », Q2 « Traitement », Q3 « Suivi » : les trois réponses en liste
  deviennent des **réponses orales**. L'« astuce révision » 24-48-10 est conservée. Axes 1 et 2.
- presentation · Version longue et SBAR : « antibiothérapie par **amoxicilline ou pénicilline V** »
  → « **pénicilline V** pendant dix jours », propagation de l'alignement de niveau 1 (vérification
  qu'aucun bloc ne porte plus l'ancienne formule).

**Divergences consignées**

- **page SSP · durée d'éviction des sports de contact après MNI** : la page se contredit —
  PRISE EN CHARGE dit « **Éviter le sport de contact 4-6 semaines** », la carte ECOS dit
  « interdire les sports de contact **3-4 semaines** ». Aucune ne tranche l'autre : niveau 3. La
  valeur **3-4 semaines** de la grille, qui est aussi celle de la section notée `m5` et de la carte,
  a été **portée inchangée** — rien n'a été inventé, l'écart de la page SSP est consigné ici.
- **résumé antibiotique · durée de l'amoxicilline** : la page SSP admet « amoxicilline 50 mg/kg/j
  × **6-10 jours** », la section notée et `theorie` disent 10 jours. `resume` a été aligné sur
  10 jours ; l'option courte de 6 jours n'a pas été conservée, par cohérence avec la section notée.
- **quatre paires de redondance restantes**, toutes acceptées : la gloses du mnémo CENTOR face à
  `resume` (règle des mnémos), deux items de `resume` face à des arguments POUR, et
  `resume`/« adénopathies cervicales antérieures douloureuses » face au **résultat de station**
  d'`expert` (« bilatérales sensibles »), qui sont deux rôles distincts.

**Signalements de sécurité** — **trois**, tous corrigés :
1. **Amoxicilline en première intention dans le bloc canonique** d'une station où la mononucléose est
   le différentiel principal et la rate palpable — la contre-indication existait ailleurs dans la
   grille mais pas là où la prescription se révise.
2. **Paracétamol 15 mg/kg × 4-6/j sans plafond** chez un patient de 19 ans (jusqu'à 90 mg/kg/j pour
   4 g/j autorisés).
3. **Azithromycine 12 mg/kg/j**, posologie pédiatrique dans une grille adulte, contredisant la
   posologie adulte donnée deux sections plus haut dans le même bloc.

### AMBOSS-34 — Perte de vision, homme de 66 ans, AVC ischémique sylvien gauche sur sténose carotidienne (page SSP : Amaurose & Baisse d'Acuité Visuelle)

Redondance : **1 paire → 0** (`report_redundancy.py AMBOSS-34_`). **Trois blocs** — `resume`,
`expert`, `theorie`. Aucun bloc `presentation` n'a été créé ; `blocks` reste
`["resume", "expert", "theorie"]` dans `baseline.json`, vérifié par `check_invariants.py`.
Les axes 5 et 6 ne s'appliquent pas ; la grille n'a pas non plus de « Check-list rapide ECOS », donc
ni axe 3 ni axe 4. Axes 1, 2 et 7 traités.

**Anomalie de structure à signaler.** La grille porte bien une fiche de présentation orale
(Checklist mentale, Version longue, SBAR, mnémos, questions d'examinateur), mais sous la classe
`annexe-item annexe-presentation` et non `presentation-patient`. `lib_amboss.BLOCKS` ne reconnaît que
la seconde : **tout l'outillage est aveugle à ce bloc** — `report_redundancy.py` ne le compare à
aucun autre (d'où l'unique paire détectée sur cette grille), `blocks_present()` ne le liste pas.
Seul `check_no_loss.py`, qui travaille sur la zone entière, le voit. Le bloc n'a **pas** été renommé,
conformément à la consigne. Le contenu a été relu manuellement.

**Modifications**

*Correction factuelle — latéralité (interne au bloc, confirmée par la section notée)*

- expert · Rôles et interventions : « Champ visuel : **hémianopsie homonyme gauche** » → « déficit
  **monoculaire** gauche, l'œil droit voit normalement — **il ne s'agit pas d'une hémianopsie
  homonyme**, ce qui situe la lésion en avant du chiasma, dans le territoire de l'ophtalmique
  gauche ». Une lésion sylvienne **gauche** ne peut pas donner d'hémianopsie **gauche** : elle
  donnerait une hémianopsie droite. Surtout, l'énoncé détruisait le point d'enseignement central de
  la station — distinguer une perte monoculaire (pré-chiasmatique, carotide homolatérale) d'une
  hémianopsie (rétro-chiasmatique, hémisphère controlatéral).
  source : section notée `m1` — « Sténose carotidienne possible avec thromboembolie →
  **hypoperfusion artère ophtalmique G (perte vision œil G)** + division supérieure ACM G (faiblesse
  main D, déficit sensitif, aphasie) » ; SSP — Cartes ECOS — « le patient dit « j'ai perdu la vue à
  gauche » — faire préciser : un œil (carotide homolatérale) ou une moitié de champ (cortex occipital
  controlatéral) ? »

*Renforcement du canonique — niveau 1, drapeaux rouges absents*

Le bloc `resume` était un résumé d'**AVC ischémique** et ne portait **aucun** examen
ophtalmologique ni aucun différentiel oculaire, alors que le motif de consultation est une perte de
vision et que `expert` distribue une acuité, un champ visuel et une fundoscopie. Recherche sur le
fichier entier (après `strip_base64`) : **« Horton », « artérite », « cellules géantes », « artère
temporale », « VS », « CRP », « OACR », « fond d'œil », « DPAR » — zéro occurrence** avant
intervention.

- resume · Examen clinique : **nouvelle sous-section « Ophtalmologique — devant toute perte de
  vision »** — acuité visuelle de chaque œil, champ visuel par confrontation avec la règle de
  localisation monoculaire / hémianopsie, réflexe photomoteur et **DPAR (Marcus-Gunn)**, **fond
  d'œil** (macula « rouge cerise » de l'OACR, hémorragies en flammèches de l'OVCR, œdème papillaire),
  **palpation des artères temporales**.
  source : SSP — EXAMEN CLINIQUE, les six items ; SSP — Points Clés ECOS — « Mesurer l'acuité
  visuelle et le champ visuel de chaque œil · Rechercher un DPAR · palper les artères temporales si
  > 50 ans » ; SSP — Pièges à éviter n° 5 — « **Oublier le fond d'œil** »
- resume · Diagnostic différentiel : ajout de l'**OACR** (« perte monoculaire brutale et indolore,
  fenêtre < 90 min »), de l'**artérite de Horton** (« obligatoire à éliminer après 50 ans ») et du
  **décollement de rétine**.
  source : SSP — DD Top 5 et tableau « urgences par délai »
- resume · Examens d'urgence : ajout de « **VS + CRP en urgence** : toute perte visuelle après
  50 ans impose d'éliminer une artérite de Horton ».
  source : SSP — Règle d'or — « Toute perte visuelle après **50 ans** impose d'éliminer une artérite
  de Horton → **VS + CRP en urgence** » ; frontmatter `pieges_eliminatoires` n° 1
- resume · Prise en charge initiale : ajout de « Si artérite de Horton suspectée : **corticothérapie
  1 mg/kg/j d'emblée, AVANT la biopsie** d'artère temporale — la biopsie reste contributive une
  quinzaine de jours, la cécité controlatérale s'installe en heures ».
  source : SSP — PRISE EN CHARGE — « Artérite de Horton : **corticothérapie 1 mg/kg/j d'emblée,
  AVANT la biopsie** (risque de cécité bilatérale) »
- theorie · Amaurose fugace : deux items de rationnel ajoutés — la règle des 50 ans (le Horton est la
  seule cause dont le traitement urgent préserve l'œil controlatéral) et la fenêtre d'environ
  90 minutes de l'OACR.

*Alignement entre blocs pédagogiques — `resume` canonique*

- theorie · Rappels thérapeutiques : « Antiagrégation : **aspirine 325 mg** J1 » → « aspirine
  **160-300 mg** dès J1 si pas de thrombolyse, différée de 24 h sinon ». Les deux blocs pédagogiques
  se contredisaient sur la dose de charge ; le contrat fait de `resume` la source canonique, ce
  n'est pas un cas de niveau 3.
- theorie · Thrombolyse : « Surveillance : neuro q15min × 2h, PA < 180/105 » → les **deux** seuils
  explicités (« PA < 185/110 **avant** la thrombolyse, puis < 180/105 pendant les 24 h qui
  suivent »), `resume` ne portant que le premier et `theorie` que le second.

*Dédoublonnage (axe 1)*

- theorie · Examens complémentaires : « CT cérébral sans contraste : urgent, exclut hémorragie »,
  seule paire de redondance de la grille avec `resume`, devient le **pourquoi** : « il ne montre pas
  l'ischémie précoce, il sert uniquement à écarter l'hémorragie, seule contre-indication absolue à la
  thrombolyse — c'est sa rapidité, non sa sensibilité, qui le place en premier ».

*Réparations mineures*

- presentation · Touches ludiques : les deux sous-sections « **VITE pour AVC** » et « **Score ABCD²
  pour AIT** » étaient des **titres sans contenu**. Renseignées à partir de la grille elle-même
  (`theorie` définit ABCD² et ses critères de haut risque) et du numéro d'urgence du corpus (144).
- expert · Points clés : « **Crescendo TIA** » → « **AIT en crescendo** », le reste de la grille
  employant partout « AIT ».

**Divergences consignées**

- **section notée `m5` · aspirine 325 mg** : la section notée prescrit « Aspirine: 325 mg PO/PR dans
  les 48h ». Le dosage à 325 mg est une forme galénique **américaine, non commercialisée en
  Suisse** ; la dose de charge y est de 160-300 mg PO (ou 250-500 mg IV). Le pédagogique a été
  harmonisé sur `resume` (160-300 mg) ; la section notée est consignée, **non corrigée** (barème gelé).
- **section notée `m1` · absence de Horton et d'OACR du différentiel** : la liste des diagnostics
  différentiels d'une perte de vision chez un homme de 66 ans ne comporte ni artérite à cellules
  géantes ni occlusion de l'artère centrale de la rétine, qui sont les deux premiers de la page SSP
  pour ce motif et cet âge. Le pédagogique a été complété (niveau 1) ; la section notée est
  consignée, **non corrigée**.
- **section notée `m5` · seuils tronqués** : « Oxygène si SpO2 94% », « Thrombolyse IV (si 4.5h du
  début) », « INR 1.7 », « Endartériectomie carotidienne si sténose 70% », « Thrombectomie mécanique
  (si 6-24h) » — les signes de comparaison manquent, comme pour la lévothyroxine d'AMBOSS-28.
  Consigné, **non corrigé**. Les valeurs sont correctes et non ambiguës dans `resume` et `theorie`.
- **page SSP · fenêtre de l'OACR** : le frontmatter et une carte ECOS disent « < 6h », le corps de la
  page (red flags, tableau des délais, règle d'or, prise en charge, points clés, mnémoniques) dit
  « **< 90 min** ». La valeur du corps a été retenue, l'écart est consigné.
- **expert · NIHSS 8 (vision 2, …)** : l'item « champ visuel » du NIHSS cote 2 pour une hémianopsie
  complète ; une cécité monoculaire se cote habituellement 1. Le détail du score n'a **pas** été
  retouché — le total 8 est cohérent avec la somme affichée et rien dans la station ne l'arbitre
  (niveau 3). Consigné.
- **expert · acuité en notation de Snellen impériale** (« < 20/200 », « 20/20 ») : notation
  américaine en pieds, là où la Suisse emploie la notation décimale (0,1 · 1,0) ou 6/60 · 6/6.
  Non corrigée : la notation 20/xx est employée telle quelle dans la source AMBOSS, elle reste
  lisible, et `check_nomenclature.py` ne la vise pas. Consignée pour arbitrage éditorial.

**Signalements de sécurité** — **deux**, tous deux corrigés côté pédagogique :
1. **Drapeau rouge absent** : l'**artérite de Horton** n'était nommée nulle part dans une grille de
   perte de vision chez un patient de **66 ans**, alors que la page SSP en fait sa règle d'or et son
   piège éliminatoire n° 1 (« corticothérapie AVANT la biopsie, risque de cécité bilatérale »).
   Même famille que le drapeau rouge d'AMBOSS-9. L'**OACR** et le **fond d'œil** étaient absents au
   même titre.
2. **Latéralité fausse** dans le bloc que l'examinateur lit à voix haute (« hémianopsie homonyme
   gauche » pour une lésion sylvienne gauche), qui inversait le raisonnement de localisation.

**Correctif d'outillage (tâche 11b) — angle mort résolu.** L'anomalie signalée plus haut (bloc
`presentation` sous la classe `annexe-item annexe-presentation`, invisible à `lib_amboss.BLOCKS`) est
corrigée à la racine, sans toucher la grille. `BLOCKS` reconnaît désormais les deux classes du bloc
`presentation` — `presentation-patient` (24 grilles) et `annexe-item annexe-presentation` (AMBOSS-34
seule) — et le marqueur de fin de `theorie` porte la même alternative. Cette seconde correction était
nécessaire : sans elle, `theorie` engloutissait tout le bloc de présentation jusqu'à `annexe-scenario`.
Vérifié avant correctif : c'était bien le cas — le segment `theorie` mesurait 20067 caractères avant,
6685 après, l'écart (13382) correspondant exactement à la longueur du segment `presentation` désormais
isolé. Le défaut était donc plus grave qu'une simple absence de détection : `report_redundancy.py`
comparait un mélange théorie + présentation à `resume` et `expert` sous la seule étiquette « theorie ».

Simulation avant application, sur les 40 grilles : la nouvelle regex ne change `blocks_present()` ni
les segments extraits que sur AMBOSS-34 — bit à bit identiques aux anciens sur les 39 autres.
`baseline.json` régénéré (`snapshot_invariants.py`), ancien sauvegardé au préalable et comparé champ à
champ : **seule** différence sur les 40 grilles, `AMBOSS-34.blocks` passe de
`["resume", "expert", "theorie"]` à `["resume", "expert", "theorie", "presentation"]`. Aucun
`maxScores`, `criteriaCount`, `detailCount`, `radioCount` ni `checkboxCount` ne bouge, sur aucune des
40 grilles. `check_invariants.py` → OK, 40 grilles.

**Première mesure valide de la redondance d'AMBOSS-34** (`report_redundancy.py AMBOSS-34_`) :
**0 paire**, tous blocs confondus (y compris `presentation`, comparé pour la première fois aux trois
autres). La ligne d'en-tête de cette entrée (« Redondance : 1 paire → 0 ») avait été mesurée avec
l'outil encore aveugle à ce bloc : la « 1 paire » initiale, déjà résorbée par la relecture manuelle
décrite plus haut avant même ce correctif, portait sur du contenu mal étiqueté (théorie ⊃
présentation), pas sur une vraie paire théorie/présentation. La mesure corrigée confirme
rétroactivement, par la mesure et non plus seulement par relecture, que le bloc `presentation` ne
duplique aucun des trois autres.

Effet sur le total du corpus (`report_redundancy.py`, sans filtre) : **aucun** — 123 paires avant
comme après, vérifié par simulation bit à bit (même ensemble de paires nommées, pas seulement même
total) entre l'ancienne et la nouvelle regex sur le contenu actuel du disque. L'augmentation attendue
de ce correctif ne s'est pas produite : le contenu d'AMBOSS-34, une fois enfin mesurable dans son
intégralité, s'avère déjà propre — la tâche 11 l'avait correctement dédoublonné à l'œil, sans pouvoir
le vérifier par l'outil.

Voir aussi `PROCEDURE.md` § 6, « Angle mort corrigé : une variante de classe non prévue rend un bloc
entier invisible à l'outillage ».

### Passe unités impériales — livres vers kilogrammes (tâche 11b)

Angle mort distinct de la passe unités SI (tâches 7 et 10c, qui ne visait que les valeurs de
laboratoire) : le corpus portait encore des poids en livres dans le texte clinique lui-même —
réponses patient, scénarios d'examinateur. Deux situations, traitées différemment, sur cinq grilles
(AMBOSS-28, 31, 36, 37, 38).

**Modifications**

*AMBOSS-28 — livres seules, sans équivalent métrique : converties*

Cinq occurrences, toutes décrivant le même fait clinique (la prise de poids du patient), arrondies
comme le ferait un patient qui parle plutôt que calculées au gramme près (1 livre = 0,4536 kg :
7-10 livres ≈ 3,175-4,536 kg arrondi en « 3-4,5 kg » ; 200 livres ≈ 90,7 kg arrondi en « 90 kg ») :

- `criteria-text` `a1` (section notée), réponse patient : « J'ai pris au moins 7-10 livres » →
  « J'ai pris au moins 3-4,5 kg ». Format `N. Libellé [réponse]` et crochets inchangés, seul le
  contenu du crochet est modifié.
- `detail-text` `a2`, réponse patient : « Je pense que je pèse plus de 200 livres maintenant » →
  « … 90 kg maintenant ».
- scénario, Motif de consultation : « Plainte principale : J'ai pris au moins 7-10 livres. » →
  « … 3-4,5 kg. »
- scénario, Symptôme principal : « Prise de poids 7-10 livres en 2 mois » → « … 3-4,5 kg en 2 mois »
  et « Poids actuel > 200 livres » → « Poids actuel > 90 kg ».

Cette divergence était **déjà consignée** dans l'entrée d'AMBOSS-28 ci-dessus (« section notée et
scénario · unités impériales […] deux zones intouchables. Consigné, non corrigé »), écrite avant que
la conversion d'un poids en unité impériale au sein d'un `criteria-text` ou d'un scénario ne soit
explicitement demandée. Elle est résolue ici : ni l'une ni l'autre zone n'était réellement intouchable
pour une substitution de texte qui ne change ni le nombre de sous-items notés, ni le format
`N. Libellé [réponse]`, ni les crochets — seul le contenu entre crochets change, le barème reste gelé.
Cohérence interne vérifiée : la « Version longue » de `presentation` mentionne indépendamment (texte
non touché, déjà en métrique) « une prise de poids d'environ 3 à 5 kilos sur les deux derniers mois » —
plage proche mais non identique à « 3-4,5 kg », deux estimations orales indépendantes déjà ainsi avant
cette passe, hors périmètre de cette tâche (aucune des deux n'est en livres).

*AMBOSS-31, 37, 38 — livres en parenthèse explicative, équivalent métrique déjà présent : retirées*

Le nombre en livres est retiré, la valeur métrique déjà présente dans la même phrase reste seule, sans
recalcul :

- AMBOSS-31, `detail-text` `a3`, Variations pondérales : « J'ai perdu 5 kg (11 livres) au cours des
  3 derniers mois » → « J'ai perdu 5 kg au cours des 3 derniers mois ».
- AMBOSS-37 (nouveau-né), `detail-text` `a6`, Poids de naissance : « Elle pesait exactement 7 livres,
  ou 3 175 g - c'est le nombre que les médecins utilisaient toujours à l'hôpital » → « Elle pesait
  exactement 3 175 g - … ».
- AMBOSS-37, `detail-text` `a6`, Poids au dernier contrôle : « Quand nous avons quitté l'hôpital elle
  pesait 6 livres et 10 onces, ou 3 016 g » → « … elle pesait 3 016 g ». Les deux valeurs métriques du
  nouveau-né sont distinctes et toutes deux conservées telles quelles (3 175 g à la naissance,
  3 016 g au dernier contrôle) — aucune n'a été confondue avec l'autre.
- AMBOSS-38, `detail-text` `a3`, Changements de poids : « […] j'ai perdu 8 livres (3,6 kg) au cours
  des 4 derniers mois » → « […] j'ai perdu 3,6 kg au cours des 4 derniers mois ».

*AMBOSS-36 — cas mixte, non anticipé par le découpage initial de la tâche*

Le brief de tâche classait AMBOSS-36 entièrement dans la catégorie « parenthèse, métrique déjà
présent », sur la base de son occurrence en `detail-text` `a3` : « Oui, j'ai perdu environ 10 livres
(4,5 kg) au cours des 2 derniers mois. […] » → « Oui, j'ai perdu environ 4,5 kg au cours des
2 derniers mois. […] », traitée comme les trois grilles ci-dessus. Le balayage exhaustif du corpus
(voir Vérifications) a cependant trouvé une **seconde occurrence**, dans le scénario d'examinateur
(Symptômes associés), sans aucun équivalent métrique sur la ligne : « Perte poids 10 livres en
2 mois ». Rien à conserver après un simple retrait : elle relève en réalité de la catégorie
d'AMBOSS-28, et a été convertie avec la valeur métrique **déjà établie** ailleurs dans le même fichier
pour ce même fait (10 livres = 4,5 kg, ci-dessus), plutôt que recalculée indépendamment — « Perte
poids 4,5 kg en 2 mois ». Signalé : le découpage à deux catégories du brief ne couvrait pas ce cas,
découvert seulement par le balayage de clôture et non par la liste de citations fournie.

**Vérifications**

- Balayage du corpus entier avant cette passe (`strip_base64`, motifs `\blivres?\b`, `\blbs?\b`,
  `\bpounds?\b`, `\bonces?\b`, `\bpouces?\b`, `\binches\b`, `°F`) : 18 correspondances brutes, dont
  6 hors sujet — AMBOSS-10, AMBOSS-25 (×2), AMBOSS-39 (×2) : « pouce(s) » anatomique (pouce de la
  main dans un geste d'examen, sans rapport avec l'unité de longueur) ; AMBOSS-26 : « POUND », le
  mnémo des critères de céphalée (Pulsatile, One day, Unilateral, Nausea, Disabling), pas l'unité de
  poids — et 12 réelles (`livres` ×11, `onces` ×1), converties ou retirées en 11 éditions de texte (la
  phrase d'AMBOSS-37 « 6 livres et 10 onces » relève d'une seule édition pour les deux mots). Après
  cette passe : les 6 mêmes correspondances hors sujet subsistent, revérifiées une à une, et
  **aucune** occurrence de `livres?`, `lbs?`, `pounds?`, `onces?`, `pouces?`, `inches` ni `°F` ne
  reste dans le texte visible des 40 grilles.
- `check_invariants.py` → OK, 40 grilles. `check_nomenclature.py` → OK. Aucun `maxScores`, compte de
  critères, radios ou checkboxes modifié : les 11 éditions sont toutes des remplacements de texte
  1 pour 1, à l'intérieur d'un crochet de réponse patient ou d'un `<li>` de scénario, sans ajout ni
  retrait de sous-item noté.
- Format `.criteria-text` (`N. Libellé [réponse]`, requis par `cases/scoring.js:159`) et crochets des
  réponses patient (colorés en bleu par `cases/scoring.js`, motif `\[([^\]]+)\]`) : vérifiés intacts
  sur les cinq grilles. Seule l'occurrence d'AMBOSS-28 `a1` est un `.criteria-text` au sens strict du
  format `N. Libellé [réponse]` ; les dix autres sont des `detail-text` ou des `<li>` de scénario, hors
  du périmètre de ce format précis mais toujours à l'intérieur de crochets `[...]` de réponse patient
  là où le texte d'origine en portait déjà, également vérifiés intacts.
- `report_redundancy.py`, sans filtre : 123 paires, inchangé par cette passe — les zones touchées
  (`criteria-text`, `detail-text`, scénario) sont hors du périmètre des quatre blocs pédagogiques que
  compare ce script.

### AMBOSS-35 — Brûlures d'estomac, femme de 54 ans, angor d'effort sur coronaropathie avec RGO concomitant (page SSP : Pyrosis (RGO))

Redondance : **9 paires → 1** (`report_redundancy.py AMBOSS-35_`). Quatre blocs présents.
Pas de sous-section `presentation`/Pièges ECOS — vérifié, l'axe 6 ne s'applique pas.

**Modifications**

*Alignement des prises en charge*

- resume · nitrés · **niveau 1, sécurité** : « Nitroglycérine sublinguale si douleur persistante et
  PAS > **100** mmHg » → « … PAS > **90** mmHg — **jamais en cas d'infarctus inférieur ou du
  ventricule droit** (débit précharge-dépendant) ». La contre-indication au nitré dans l'infarctus
  droit n'existait nulle part dans la grille. Même correction qu'AMBOSS-14 en tâche 6, même source.
  source : SSP — Pyrosis renvoie explicitement à [[SSP — Douleur Thoracique]] pour le DD du SCA ;
  celle-ci, Prise en charge / SCA — « <span>nitroglycérine</span> SL si TA > 90 ; … — **cave
  infarctus inférieur / droit : pas de nitré** (précharge-dépendant) »
- resume · anticoagulation : « enoxaparine ou fondaparinux » → « **HNF**, énoxaparine ou
  fondaparinux ». · resume · stratégie invasive : « (coronarographie ± angioplastie) » → « … **en
  urgence si ST+ ou NSTEMI à haut risque** » — la précision n'existait que dans la check-list
  « PEC en 3 points », dont l'axe 3 fait un sous-ensemble strict du bloc parent.
- resume · Autres bilans · **niveau 1** : ajout de « Une fois la cause cardiaque écartée : **OGD avec
  biopsies** — imposée ici par l'âge > 50 ans et un RGO ancien de 10 ans (recherche d'un **œsophage
  de Barrett**) ». La patiente a 54 ans et dix ans de reflux : la page SSP en fait une indication
  d'endoscopie, et rien dans la grille ne la portait.
  source : SSP — Règle d'or — « Les drapeaux rouges (dysphagie, perte de poids, hémorragie digestive,
  anémie, **> 50 ans**, échec des IPP) imposent une **OGD**. […] Un **RGO ancien (> 5-10 ans)** impose
  de chercher un **œsophage de Barrett** »
- resume · Examen clinique : ajout des **constantes vitales** (TA, FC, FR, SpO₂, T°), absentes du bloc
  canonique alors que la check-list « Examens à faire » les exigeait (axe 4).

*Corrections factuelles (internes aux blocs)*

- expert · Rôles et interventions · **sécurité** : « Test nitroglycérine : soulagement partiel
  **suggère angor** » → « … **non discriminant** (les nitrés soulagent aussi le spasme œsophagien) ».
  L'énoncé transformait un test non discriminant en argument diagnostique, dans la station même dont
  tout l'enjeu est de ne pas conclure « c'est digestif » trop vite. Il contredisait de surcroît
  `theorie`, qui disait déjà « soulage angor ET spasme œsophagien ».
  source : SSP — Cartes ECOS — « un spasme œsophagien peut céder aux dérivés nitrés, et un angor peut
  être soulagé par un antiacide. La clinique seule ne peut donc structurellement pas trancher »
- theorie · Rappels thérapeutiques : « Aspirine : 75-100 mg/j (**prévention primaire** si risque) » →
  « … au long cours (**prévention secondaire**, une fois la coronaropathie établie) ». Chez une
  patiente dont le diagnostic retenu est un angor d'effort sur coronaropathie, cette dose est de la
  prévention secondaire ; l'aspirine en prévention primaire n'est plus recommandée en routine.
- presentation · mnémo **DOULOURED** : le mnémo comptait **neuf lettres pour huit items** — la
  seconde clé `U` n'avait aucune valeur. Elle reçoit « Urgence → appel 144 si suspicion de SCA »,
  reprise de `resume`/Prise en charge initiale : aucune donnée clinique nouvelle n'est introduite,
  seule la clé orpheline est comblée. Clés d'origine intactes, conformément à la règle des mnémos.

*Dédoublonnage (contrat de blocs, règle du format)*

- presentation · mnémo DOULOURED : la `mnemo-box` de la Checklist mentale est **déplacée** vers
  « Touches ludiques / mnémos » (la Checklist mentale redevient une trame pure, axe 5). Aucun mnémo
  ne l'y doublait — Touches ludiques ne portait que des listes comparatives.
- theorie · RGO vs Angor : les deux items « RGO : post-prandial, position, aliments acides » et
  « Angor : effort, stress, froid, soulagement repos » sont **supprimés** — paires à 0.85 et 0.95
  avec la sous-section « RGO vs Angor » de Touches ludiques, même format, même contenu. La section
  bascule sur le *pourquoi* (axe 1) et reçoit l'explication qui manquait à toute la grille :
  l'**innervation viscérale afférente commune (métamères T1-T5)**, qui rend les deux douleurs
  référées au même territoire. Le contraste mémorisable reste seul porté par Touches ludiques.
  source : SSP — Cartes ECOS — « l'œsophage et le cœur partagent la même innervation viscérale
  afférente (métamères **T1-T5**) : leurs douleurs sont référées au MÊME territoire rétrosternal »
- theorie · RGO vs Angor : l'item « IPP test : amélioration RGO en 1-2 semaines » reçoit la condition
  de prise — « à condition d'une prise **30 min avant le repas** — beaucoup d'« échecs d'IPP » ne sont
  qu'une erreur de prise ». La patiente a précisément arrêté son oméprazole.
  source : SSP — Mnémoniques — « **IPP** : à prendre **30 min AVANT le repas** […] beaucoup
  d'« échecs d'IPP » sont des erreurs de prise »
- expert · Points clés : réécrits en registre d'**observation d'examinateur** (axe 7), `resume`
  gardant le registre « ce que l'étudiant retient ». « Stress aidant = facteur de risque
  indépendant » disparaît du bloc expert — c'est de la théorie, et `theorie`/Syndrome de l'aidant la
  porte déjà en entier (risque CV +60 %, isolement social, dépression 40 %) : la paire à 0.72
  expert ↔ theorie tombe.
- presentation · Q1 « Quels examens », Q2 « Traitement », Q3 « Suivi » : les trois réponses en liste
  deviennent des **réponses orales**. Elles portaient quatre des neuf paires, dont une à **1.00**
  (« ECG 12 dérivations en urgence »). Contenu intégralement conservé, l'indication d'OGD y étant
  ajoutée par cohérence avec `resume`.
- presentation · Checklist mentale : « Facteurs de risque → tabac, HTA, dyslipidémie, ATCD familiaux,
  stress » → « Facteurs de risque cardiovasculaires → les énumérer, puis situer l'exposition au
  stress ». L'énumération recopiait `resume`/Contexte à risque (paire à 0.77) ; la trame conserve
  l'étape, pas la liste clinique (axe 5).

**Divergences consignées**

- **section notée `m5` · seuil d'oxygénothérapie** : la section notée dit « Oxygène si SpO2 94% »,
  `resume` et le mnémo disent « si SaO₂ < **90 %** ». Le pédagogique n'a **pas** été aligné sur la
  section notée, contrairement à ce que prescrirait le niveau 2, pour deux raisons : la doctrine du
  corpus tranche explicitement en faveur de 90 % — SSP — Douleur Thoracique, carte ECOS : « donner de
  l'O₂ à un coronarien **non hypoxémique** : c'est inutile voire délétère (vasoconstriction
  coronaire) — **pas d'O₂ si SpO₂ ≥ 90 %** » — et le texte de la section notée est **visiblement
  corrompu** à cet endroit (le `<` de « < 94 % » a disparu, comme le montrent les mutilations voisines
  « Aspirine 160-: 325 mg », « Nitroglycérine sublinguale 0.: 4 mg », « IEC si HTA/diabète
  (ramipril 2.5- » suivi d'un titre vide). Une section notée mutilée ne peut pas faire autorité sur un
  seuil chiffré. **Barème gelé** : rien n'a été modifié dans la section notée, l'écart est consigné ici.
- **une paire de redondance restante**, acceptée : la glose du mnémo DOULOURED (« Urgence → appel 144
  si suspicion de SCA ») face à `resume`/Prise en charge initiale — règle des mnémos, précédent CENTOR
  d'AMBOSS-30.

**Signalements de sécurité** — **trois**, tous corrigés sauf le premier qui est consigné :
1. **Seuil d'oxygénothérapie de la section notée** (SpO2 94 % au lieu de < 90 %, dans un texte
   corrompu) — non corrigé, barème gelé, consigné ci-dessus.
2. **Absence totale de contre-indication des nitrés dans l'infarctus inférieur / du ventricule
   droit**, dans une station de suspicion de SCA, avec un seuil tensionnel par ailleurs trop haut.
3. **« Le test à la nitroglycérine suggère un angor »** en bloc expert — un test non discriminant
   présenté comme argument diagnostique, exactement le raisonnement que la station veut faire échouer.

### AMBOSS-37 — Changements cutanés, nouveau-née de 4 jours, ictère d'allaitement (page SSP mappée : Éruption Cutanée)

Redondance : **5 paires → 0** (`report_redundancy.py AMBOSS-37_`). Quatre blocs présents.
Pas de sous-section `presentation`/Pièges ECOS — vérifié, l'axe 6 ne s'applique pas.

**Divergence de rattachement — à arbitrer en priorité**

`docs/obsidian-mapping.yaml` rattache AMBOSS-37 à **`SSP ECOS/SSP — Éruption Cutanée.md`**, page de
dermatologie qui ne contient **aucune** occurrence d'« ictère », « bilirubine », « nouveau-né »,
« Coombs » ni « photothérapie » (recherche exhaustive sur ses 498 lignes). Or la grille est une
station d'**ictère néonatal** : son `resume` s'intitule « Ictère néonatal (ictère d'allaitement) ».
Le rattachement vient manifestement du titre du cas (« Changements cutanés »).

Le vault possède une page exactement adéquate, **`SSP ECOS/SSP — Ictère Néonatal.md`**, aujourd'hui
rattachée à la seule USMLE-18 (« Garçon 5 jours, la peau et les yeux jaunes ») — le même tableau
clinique à un jour près. **Recommandation : rerattacher AMBOSS-37 à `SSP — Ictère Néonatal`.**
Le fichier de mapping n'a pas été modifié : il sort du périmètre de cette tâche.

Conséquence méthodologique assumée : la page mappée étant muette sur tout le sujet, elle place
l'intégralité de la grille au **niveau 3**. Les alignements ci-dessous citent donc
`SSP — Ictère Néonatal`, en le signalant à chaque fois — aucun n'est présenté comme venant de la page
mappée. Les points touchant à la sécurité néonatale ne pouvaient pas rester non arbitrés au seul
motif d'une ligne de mapping.

**Modifications**

*Alignement des prises en charge*

- resume · photothérapie · **niveau 2** : « Photothérapie si seuil dépassé selon **courbes de
  l'AAP** » → « … sur le **nomogramme de Bhutani** (âge en **heures de vie** + facteurs de risque) ».
  La section notée dit « Interprétation selon **nomogramme de Bhutani** », `theorie` a une section
  entière intitulée « Nomogramme de Bhutani » : le bloc canonique était le seul à invoquer une
  référence américaine, et il contredisait les deux autres.
  source : section notée `m5` — « Mesure transcutanée ou sérique de bilirubine · Interprétation selon
  nomogramme de Bhutani » ; corroboré par SSP — Ictère Néonatal — « **Photothérapie** selon seuils
  **Bhutani** (âge en **heures** + facteurs de risque) »
- resume · Examens initiaux : « Courbe percentile selon âge postnatal » → « **Report de la bilirubine
  totale sur le nomogramme de Bhutani** (percentiles selon l'âge en **heures de vie**) ». Résout la
  paire à 0.89 avec `theorie` et fixe l'unité de temps dans le bloc canonique.
- resume · ictère prolongé : « persistant > **10 jours** » → « > **2 semaines** », et de même dans le
  mnémo FEVER-YELLOW (« YELLOW = ictère prolongé > 10 jours ») et dans Touches ludiques (« persistant
  > 10j »). La grille se contredisait : `theorie`/Types d'ictère disait « > **J14** : Prolongé » et la
  section de queue « TSH : si ictère prolongé > **2 semaines** ». Les quatre mentions sont désormais
  cohérentes sur 2 semaines, valeur du seuil de référence.
  source : SSP — Ictère Néonatal — red flags, Règle d'or et Points Clés — « **Ictère prolongé > 2
  semaines** » (×3)

*Renforcement du canonique — sécurité néonatale*

- resume · Traitements spécifiques : ajout de « **Jamais de photothérapie sur un ictère à bilirubine
  conjuguée** : inefficace et exposant au « bronze baby » — c'est un bilan de cholestase qui
  s'impose ». Le bloc canonique prescrivait la photothérapie sur un seuil de bilirubine **totale**
  sans jamais mentionner que la fraction conjuguée en est une contre-indication. Absent de toute la
  grille.
  source : SSP — Ictère Néonatal, carte ECOS — « un ictère à bilirubine conjuguée ne se traite JAMAIS
  par photothérapie (inefficace, risque de « **bronze baby** ») »
- resume · Examens initiaux : ajout de « Toute **bilirubine conjuguée** élevée (> 20 % du total ou
  > 17 µmol/L) est **pathologique quelle que soit la valeur** : cholestase, atrésie des voies
  biliaires — la **chirurgie de Kasai doit être faite avant 60 jours de vie** ». La grille ne portait
  ni le seuil de la fraction conjuguée ni la fenêtre chirurgicale, qui est le fait le plus
  chrono-dépendant de tout l'ictère néonatal.
  source : SSP — Ictère Néonatal, Règle d'or — « **bilirubine conjuguée > 20 % du total ou > 17
  µmol/L** » ; Prise en charge — « **chirurgie de Kasai avant 60 jours** de vie »
- resume · Examen clinique : ajout de « **Signes de kernictère** : léthargie, hypotonie, cris aigus,
  opisthotonos — urgence absolue ». Le bloc canonique ne les portait pas ; ils n'existaient que dans
  la section notée (redflags) et, partiellement, dans une réponse de `presentation`.
  source : SSP — Ictère Néonatal, red flags — « Signes de **kernictère** (hypotonie, léthargie, cris
  aigus, opisthotonos) »
- theorie · Indications photothérapie · **sécurité** : le tableau de seuils indexé **par journée**
  (J1 > 170, J2 > 260, J3 > 310, J4+ > 340 µmol/L) contredisait la section « Nomogramme de Bhutani »
  du même bloc, qui indexe en **heures**. Les valeurs sont **conservées telles quelles** (niveau 3 :
  rien n'a été inventé) mais leur statut est explicité — « La décision se prend en reportant la
  bilirubine totale sur le nomogramme de Bhutani, à l'âge exact **en heures de vie**. Les valeurs
  ci-dessous ne sont que des **ordres de grandeur par journée** » — et la ligne manquante est ajoutée :
  « **Avant 24 h de vie, aucun seuil ne s'applique** : tout ictère y est pathologique et impose un
  bilan d'hémolyse, pas une décision de photothérapie sur un chiffre ». Un seuil « J1 » écrasait en un
  chiffre unique les 24 premières heures, précisément la fenêtre où le chiffre ne décide de rien.
  source : SSP — Ictère Néonatal, carte ECOS — « Le seuil dépend de l'âge **en heures** parce que la
  bilirubine suit une cinétique d'accumulation » ; Points Clés — « **Ictère < 24h = pathologique**
  (hémolyse jusqu'à preuve contraire) »

*Corrections factuelles (internes aux blocs)*

- presentation · mnémo **FEVER-YELLOW** : « **R = Recoloration** selles (décolorées = atrésie
  biliaire) » → « **R = Regarder les selles** (décolorées = atrésie biliaire) ». Le mnémo de drapeaux
  rouges nommait une « recoloration » là où le signe d'alarme est une **dé**coloration : le mot
  désignait le contraire du signe recherché. Clé R conservée.
- presentation · mnémo FEVER-YELLOW : « E = **Early onset** < 24h » → « E = **Émergence avant 24h de
  vie** ». Clé E conservée, valeur rendue en français — même règle clé/valeur que les glossaires de
  schéma.

*Dédoublonnage (contrat de blocs, règle du format)*

- presentation · mnémo JAUNE : la `mnemo-box` de la Checklist mentale est **déplacée** vers « Touches
  ludiques / mnémos » (la Checklist mentale redevient une trame pure, axe 5). Elle ne double pas
  FEVER-YELLOW, déjà présent : JAUNE est une trame de bilan, FEVER-YELLOW une liste de drapeaux
  rouges — les deux sont conservés.
- theorie · Nomogramme de Bhutani : l'item « Courbes percentiles selon âge postnatal (heures) » est
  supprimé (paire à 0.89 avec `resume`, désormais canonique sur ce point) et la section bascule sur le
  *pourquoi* (axe 1) : « la bilirubine suit une cinétique d'accumulation, si bien qu'une même valeur
  est rassurante à 96 h et alarmante à 24 h ». Les quatre zones de percentiles restent.
- theorie · section de queue Examens complémentaires : « TSH : si ictère prolongé > 2 semaines » →
  énoncé d'indication motivée (« l'hypothyroïdie congénitale ralentit la conjugaison — à demander
  devant tout ictère dépassant 2 semaines, **même chez un enfant qui va bien** »), pour se distinguer
  de la liste de `resume` (paire à 0.72). La section de queue est conservée à sa place, conformément
  au § 3.
- theorie · Types d'ictère : l'item cholestase reçoit la raison de l'urgence — « la fibrose progresse
  vite, passé 2-3 mois le Kasai échoue et seule la transplantation reste ».
- presentation · Q1 « Quels examens », Q2 « Traitement », Q3 « Suivi » : les trois réponses en liste
  deviennent des **réponses orales**. Le filet de sécurité parental y est explicité au lieu d'être
  résumé en « signes de gravité ».
  source : SSP — Ictère Néonatal, Script ECOS — « selles très pâles (blanches/grisâtres), bébé très
  mou ou difficile à réveiller, refus de téter […] → consultez sans attendre »

**Vérifications propres à la station néonatale**

- **Posologies au poids** : la zone pédagogique ne contient **aucune posologie médicamenteuse**. Les
  seules valeurs chiffrées de `theorie`/Rappels thérapeutiques sont des réglages de photothérapie
  (irradiance 30 puis 45-60 µW/cm²/nm, distance 30-50 cm, rotation toutes les 2-3 h), qui ne se
  calculent pas au poids. La seule dose pondérale de la grille, « Albumine 1 g/kg si
  hypoalbuminémie », est dans la section notée et **porte bien le `/kg`**.
- **Seuils sans référence temporelle** : aucun ne subsiste. Les quatre seuils de photothérapie
  portaient déjà une référence en journées ; leur statut d'ordre de grandeur et le renvoi à l'âge en
  heures ont été explicités ci-dessus.
- **Cohérence des deux passes antérieures** : « Visible si bilirubine > **85 μmol/L** » (conversion de
  la parenthèse « (5 mg/dL) » retirée en tâche 2) — 85 µmol/L = 4,97 mg/dL, conversion exacte, aucune
  mention résiduelle de `mg/dL` dans la grille. Poids de naissance en grammes : « **3 175 g** à la
  naissance, **3 016 g** à la sortie, soit une perte de poids de **5 %** » — (3175 − 3016)/3175 =
  5,007 %, le pourcentage du récit reste juste après la conversion, et les deux valeurs concordent
  avec les réponses patient des critères notés « Poids de naissance » et « Poids au dernier contrôle ».

**Divergences consignées**

- **rattachement SSP** : voir ci-dessus. C'est la divergence principale de cette grille.
- **seuils de photothérapie par journée** : les quatre valeurs (170 / 260 / 310 / 340 µmol/L) n'ont
  été ni modifiées ni recalculées — ni la page mappée, ni la section notée, ni
  `SSP — Ictère Néonatal` ne donnent de table chiffrée qui permettrait de les arbitrer. Niveau 3.

### AMBOSS-38 — Douleur à la cheville, femme de 28 ans, entorse de cheville grade I-II (page SSP : Entorse de Cheville)

Redondance : **15 paires → 1** (`report_redundancy.py AMBOSS-38_`). Quatre blocs présents.
Grille de l'**axe 6** : sous-section `presentation`/Pièges ECOS traitée avec l'anti-perte.

**Modifications**

*Dédoublonnage (contrat de blocs, règle du format)*

- presentation · sous-section « ⚠️ Pièges ECOS » **supprimée en entier** (axe 6). **Anti-perte
  préalable**, deux items portés dans `expert`/Pièges avant la suppression : « Négliger facteurs
  risque fracture stress » y devient « … **propres à cette patiente : coureuse de marathon en
  restriction calorique (triade de l'athlète féminine / RED-S)** » — l'ancrage au cas n'existait que
  dans la sous-section supprimée ; et « Omettre conseils prévention récidive » devient « … **au
  premier rang la rééducation proprioceptive** », seule mention du geste dans un bloc de pièges.
  Les trois autres items doublaient `expert` à 1.00, 0.98 et 0.88. Reproduction du geste β-hCG
  d'AMBOSS-3.
- presentation · mnémo OTTAWA : la `mnemo-box` de la Checklist mentale est **déplacée** vers « Touches
  ludiques / mnémos » (la Checklist mentale redevient une trame pure, axe 5), où elle **remplace** les
  trois sous-sections qui recopiaient `theorie` et `resume` au même format : « Classification des
  entorses » (paires à 0.81 et 0.73), « Classification de Weber » et « PEC initiale entorse
  (GREC/RICE) » (paires à 0.86 et 0.78). Vérification item par item avant suppression : les qualificatifs
  de laxité (« instabilité modérée », « instabilité majeure ») manquaient à `theorie` et y ont été
  **portés** ; les trois lignes de Weber y figuraient déjà en entier ; « Mobilisation précoce dès
  tolérance » a été porté dans `resume`, qui ne mentionnait nulle part la remise en charge (voir
  ci-dessous).
- theorie · Règles d'Ottawa : l'énumération des six critères est **supprimée** au profit du *pourquoi*
  (axe 1) — sensibilité 98-100 % lue comme une **règle d'exclusion** (30 à 40 % de radiographies
  évitées), raison du bord postérieur, limites d'applicabilité. **Anti-perte préalable** : les
  critères ont d'abord été rendus complets dans `resume` — la distinction Rx cheville / Rx pied selon
  la zone douloureuse, les 6 cm distaux, le naviculaire, et « à la fois immédiatement après le
  traumatisme **et à la consultation** » pour les 4 pas.
- presentation · Q1 diagnostics, Q1 examens, Q1 et Q2 prise en charge, Q1 prévention : les **cinq**
  réponses en liste deviennent des **réponses orales**. Contenu intégralement conservé.

*Alignement des prises en charge — niveau 1*

- resume · Prise en charge : ajout de « **Mise en charge et mobilisation précoces dès la tolérance :
  elles font mieux que l'immobilisation prolongée** ». La remise en charge précoce était répétée trois
  fois dans la grille (`expert`, `theorie`, Touches ludiques — trois paires de redondance) et absente
  du bloc canonique, c'est-à-dire absente de là où l'étudiant révise le traitement.
  source : SSP — Prise en charge — « **Mise en charge précoce** selon douleur (**mieux que
  l'immobilisation prolongée**) »
- resume · Traitement complémentaire · **sécurité** : ajout de « **Thromboprophylaxie** à discuter si
  immobilisation stricte en décharge avec facteurs de risque ». Absente de toute la grille, alors que
  la page SSP la mentionne deux fois.
  source : SSP — Prise en charge — « **Prophylaxie thrombo-embolique** à discuter en cas
  d'immobilisation stricte avec FdR » ; carte ECOS — « Ne pas oublier la **thromboprophylaxie** si
  immobilisation stricte + décharge »
- resume · Examen clinique · **sécurité** : ajout de « **Palpation systématique de la fibula
  proximale** — une fracture de Maisonneuve siège au col, très à distance de la cheville » et de
  « **Test de Thompson** si claquement dans le mollet ou perte de propulsion (rupture du tendon
  d'Achille) ». La palpation de la fibula proximale n'était citée que comme piège en bloc expert,
  jamais comme geste d'examen ; la rupture du tendon d'Achille était absente de la grille entière
  alors que `resume` interroge d'emblée sur un « craquement ».
  source : SSP — En Bref — « **Toujours rechercher : fracture de Maisonneuve** (fibula proximale) » ;
  carte ECOS — « La palpation de la **fibula proximale** (col/tête) — **systématique** devant toute
  entorse de cheville » ; Pièges — « Le **claquement** + impossibilité de propulsion n'est pas une
  entorse grave — exclure la **rupture du tendon d'Achille** (Thompson) »
- resume · Points clés : ajout de « **Mollet douloureux** après une entorse = exclure une **TVP**
  (score de Wells ou de Genève, écho-doppler) ; **cheville chaude ou fébrile** = ponction, jamais une
  simple entorse ». Deux des quatre Points Clés ECOS de la page SSP, absents de la grille.
  source : SSP — Points Clés ECOS (items 3 et 4)
- resume · Imagerie : ajout de « Radiographie de **jambe entière** si suspicion de fracture de
  Maisonneuve » — la radiographie de cheville seule y est normale ou peu parlante.
  source : SSP — Examens complémentaires — « **Rx jambe** si suspicion de Maisonneuve »
- resume · mécanisme : « Mécanisme en inversion ou éversion » → correspondance mécanisme → ligament
  (« inversion (supination) → **LTFA** ± calcanéo-fibulaire ± talo-fibulaire postérieur ; éversion
  (plus rare, plus sévère) → **ligament deltoïde** ± syndesmose »), ce qui différencie l'item de
  `theorie` (paire à 0.85), qui garde l'épidémiologie chiffrée.
  source : SSP — En Bref
- resume · antalgie : « paracétamol ± **AINS** » → « paracétamol ± **ibuprofène en cure courte** ».
  source : SSP — Prise en charge — « Antalgie palier OMS (paracétamol, **ibuprofène courte durée**) »

*Corrections factuelles (internes aux blocs)*

- resume · « Test en varus forcé (**stabilité sous-talienne**) » → « **Inversion forcée (talar tilt)** :
  bâillement augmenté = atteinte du **ligament calcanéo-fibulaire ± LTFA** ». Le test d'inversion
  forcée explore les ligaments latéraux de la cheville, non l'articulation sous-talienne : le libellé
  désignait la mauvaise structure.
  source : SSP — Tests spécifiques, tableau — « **Inversion forcée (talar tilt)** […] Bâillement
  augmenté = atteinte du **LCF** ± LTFA »
- presentation · mnémo **OTTAWA**, deux clés fausses corrigées, clés d'origine conservées :
  « T = **Talon** / 5e métatarsien douloureux » → « T = **Tubérosité de la base du 5e métatarsien** »
  (le calcanéus n'est **pas** un critère d'Ottawa — le mnémo faisait entrer un os étranger à la
  règle) ; « A = **Articulation** malléolaire latérale » → « A = **Arête postérieure de la malléole
  latérale (6 cm)** » (le critère porte sur le bord postérieur de l'os, non sur l'articulation, et
  c'est précisément la distinction qui fait la valeur de la règle). La clé « T = Tibia » reçoit la
  même précision, et la dernière clé A, « Anamnèse traumatique », devient « **Applicable ?** Ni avant
  18 ans, ni si intoxication, polytraumatisme, déficit sensitif ou trauma de plus de 10 jours » —
  les limites d'applicabilité étaient absentes de toute la grille.
  source : SSP — Règles d'Ottawa, pocketcard ; carte ECOS — « on palpe le **bord postérieur** de la
  malléole, car c'est là que court la corticale osseuse » ; « **Piège :** non applicable si < 18 ans,
  intoxication, polytraumatisme, déficit sensitif ou trauma > 10 jours »
- theorie · Règles d'Ottawa : la limite pédiatrique reçoit sa raison — « plaques de croissance non
  visibles sur radiographie standard, seuil abaissé ».
  source : SSP — Pièges
- theorie · Rappels thérapeutiques : « Cryothérapie : **10-20** min » → « **15-20** min », aligné sur
  `resume` (canonique) qui disait déjà 15-20 ; « pas direct sur peau » → « **jamais à même la peau** »,
  formule reprise dans `resume`.
- theorie · PEACE & LOVE : « - Avoid anti-inflammatoires : retardent guérison » → « … **à limiter en
  phase aiguë**, ils retardent la cicatrisation — **ibuprofène en cure courte si la douleur
  l'exige** ». L'item posait une interdiction que la page SSP ne pose pas. Clé « Avoid » conservée
  (mnémo), valeur nuancée.
  source : SSP — Prise en charge — « ibuprofène **courte durée** »
- theorie · Entorse de cheville : ajout de l'ordre de rupture des ligaments latéraux et de son
  corollaire — « une rupture complète peut être **moins douloureuse** qu'une rupture partielle, les
  fibres nociceptives étant sectionnées : **ne jamais grader sur la seule douleur** ».
  source : SSP — carte ECOS sur les grades

- expert · Points clés : réécrits en registre d'**observation d'examinateur** (axe 7) ; la paire à
  0.73 avec `theorie` sur la mobilisation précoce tombe, le geste vivant désormais dans `resume`
  (canonique) et sa temporalité (« J2-3 si toléré ») dans `theorie`/Rappels.

**Divergences consignées**

- **une paire de redondance restante**, acceptée : `resume`/« Tests de stabilité ligamentaire (tiroir
  antérieur, varus forcé) » face à `expert`/« Tests ligamentaires : tiroir antérieur négatif, varus
  forcé douloureux ». Ce sont deux rôles distincts — la check-list de ce qu'il faut faire d'un côté,
  le **résultat de station** que l'expert délivre de l'autre. Même arbitrage qu'en AMBOSS-30.

**Signalements de sécurité** — **quatre**, tous corrigés :
1. **Thromboprophylaxie absente de la grille entière**, alors que le traitement proposé comprend
   l'immobilisation par attelle et que la page SSP la mentionne deux fois.
2. **Rupture du tendon d'Achille jamais évoquée**, ni le test de Thompson, alors que `resume`
   interroge d'emblée sur un craquement — c'est le piège explicite de la page SSP.
3. **Palpation de la fibula proximale absente de l'examen clinique canonique** (elle n'existait que
   comme piège), dans une grille dont le diagnostic différentiel comprend la fracture de Maisonneuve.
4. **Mnémo OTTAWA enseignant deux critères faux** — le talon (calcanéus), qui n'appartient pas à la
   règle, et l'« articulation » malléolaire à la place du bord postérieur de l'os, c'est-à-dire
   exactement la distinction dont dépend la sensibilité de la règle.

### AMBOSS-39 — Douleur à l'épaule, homme de 52 ans, rupture du supra-épineux (page SSP : Douleur d'Épaule)

Redondance : **11 paires → 0** (`report_redundancy.py AMBOSS-39_`). Quatre blocs présents.
Grille de l'**axe 6** : sous-section `presentation`/Pièges ECOS traitée avec l'anti-perte.

**Vérification de la substitution de la tâche 3 (Vicodin → Tramal®)**

Substitution **cohérente et complète**. Les cinq mentions du corpus de la grille disent toutes
« Tramal® (tramadol) » : critère noté `6. Médicaments` (« J'ai essayé du Tramal® (tramadol) de ma
copine, qu'il lui restait d'une chirurgie l'année dernière »), Checklist mentale, Version longue,
scénario du patient standardisé (« Mentionner usage Tramal® (tramadol) copine »). **Aucune**
occurrence résiduelle de « Vicodin » ni d'« hydrocodone ». L'effet indésirable du récit,
**étourdissements**, reste plausible et même typique du tramadol (vertiges chez ~ 1 patient sur 4,
effet indésirable le plus fréquent après les nausées). La qualification d'« opioïde non prescrit »
qui structure `expert`/Points clés, `expert`/Pièges et le critère noté « Conseil sur l'utilisation
d'opioïdes sur ordonnance » reste exacte : le tramadol est bien un analgésique opioïde (agoniste μ
faible et inhibiteur de la recapture des monoamines).

**Modifications**

*Renforcement du canonique — sécurité*

- resume · Examens diagnostiques · **sécurité, niveau 1** : ajout de « **ECG et troponines** devant
  toute **épaule gauche** douloureuse **après 50 ans** : un SCA peut se projeter là et n'y donner
  aucun signe local ». Le patient a 52 ans et consulte pour une épaule **gauche**. La cause cardiaque
  n'existait dans la grille que sous forme de deux allusions en bloc expert (« Auscultation thorax :
  normale (éliminer cause cardiaque) », « Oublier causes cardiaques épaule gauche ») — jamais dans le
  bloc canonique, jamais comme examen à demander. C'est le **premier piège éliminatoire** de la page SSP.
  source : SSP — pièges éliminatoires — « **Manquer SCA atypique (ECG systématique chez > 50 ans)** » ;
  Red flags — « Douleur épaule **gauche** + douleur thoracique + dyspnée ou sueurs → **SCA** (douleur
  projetée) · **ECG** STAT + **troponines** » ; Points Clés — « Ne pas oublier les causes viscérales :
  **SCA (épaule G)** »
- resume · Points clés : ajout de « Avant de conclure à une cause locale : écarter les **causes
  projetées** — SCA pour l'épaule gauche, cholécystite ou abcès sous-phrénique pour la droite, tumeur
  de Pancoast — et **toujours examiner le rachis cervical** ».
  source : SSP — Points Clés ECOS (items 1 et 2)
- resume · Tests spécifiques : ajout de l'**examen du rachis cervical (manœuvre de Spurling)** —
  « une névralgie cervico-brachiale C5-C6 mime parfaitement une tendinopathie d'épaule ». Absent de
  la grille entière, alors que c'est le premier des Pièges de la page SSP.
  source : SSP — Pièges — « **Omettre l'examen cervical** : une névralgie cervico-brachiale C5-C6
  **mime parfaitement** une tendinopathie de l'épaule » ; Points Clés — « **Toujours examiner le
  rachis cervical** […] manœuvre de Spurling »
- resume · Examens diagnostiques : ajout de « **VS et CRP** si douleur bilatérale des ceintures avec
  raideur matinale après 50 ans : **polymyalgie rhumatismale**, à ne pas dissocier d'une **artérite de
  Horton** ». Le patient a 52 ans ; ni la PPR ni Horton n'apparaissaient dans la grille.
  source : SSP — Red flags — « **> 50 ans** : douleur ceintures scapulaire et pelvienne bilatérale +
  raideur matinale + **VS > 50 mm/h** → **Polymyalgie rhumatismale** ± **artérite de Horton** » ;
  Points Clés
- resume · Tests spécifiques : ajout du **drop-arm** (« chute brutale du bras à la descente = rupture
  massive, avis chirurgical ») et de l'**arc douloureux 60-120° avec Neer et Hawkins**, qui
  n'existaient que dans `theorie` et dans une sous-section de `presentation`.

*Corrections factuelles (internes aux blocs)*

- theorie · Tests cliniques : « **Patte (lift-off)** : infra-épineux/petit rond » → « **Patte :
  rotation externe contrariée en abduction à 90°** — infra-épineux et petit rond. **À ne pas confondre
  avec le lift-off, qui est le test de Gerber** ». La liste attribuait le **même** test — le lift-off —
  à deux manœuvres différentes, deux lignes de suite (« Patte (lift-off) », puis « Gerber
  (lift-off) »), et contredisait `resume`, qui distingue correctement « Test du Patte : rotation
  externe contrariée » et « Lift-off test (sous-scapulaire) ». `resume` étant canonique et exact, c'est
  `theorie` qui a été corrigé.
- resume · « Lift-off test (sous-scapulaire) » → « **Lift-off test de Gerber** (sous-scapulaire) »,
  l'éponyme n'existant que dans `theorie` et `presentation`.

*Dédoublonnage (contrat de blocs, règle du format)*

- presentation · sous-section « ⚠️ Pièges ECOS » **supprimée en entier** (axe 6). **Anti-perte
  préalable** : « Toujours comparer mobilité active vs passive » a été porté dans `expert`/Pièges
  (« **Ne pas comparer systématiquement la mobilité active à la mobilité passive — c'est ce qui sépare
  la coiffe de l'atteinte articulaire** »), où aucun item ne le portait ; le contenu clinique existait
  dans `resume` mais le **piège**, lui, n'existait nulle part ailleurs. Les quatre autres items
  doublaient `expert` à 0.92, 0.74 et 0.73. Reproduction du geste β-hCG d'AMBOSS-3.
- presentation · mnémo COIFFE : la `mnemo-box` de la Checklist mentale est **déplacée** vers « Touches
  ludiques / mnémos » (la Checklist mentale redevient une trame pure, axe 5), où elle **remplace** la
  sous-section « Tests spécifiques épaule » — liste recopiant `theorie`/Tests cliniques au même
  format, porteuse à elle seule de quatre paires dont **deux à 1.00** (« Gerber (lift-off) :
  subscapulaire » et « arc douloureux 60-120° = conflit sous-acromial ») et une à 0.94. Vérification
  item par item avant suppression : les cinq tests ont d'abord été rendus présents dans `resume`
  (arc douloureux, Neer et Hawkins avec leur technique y ont été **ajoutés**), `theorie` conservant
  Jobe, Patte, Gerber et drop-arm avec leur signification. La sous-section « Facteurs de risque
  rupture coiffe » est **conservée** : elle porte les ancrages professionnels du cas (peintre,
  carreleur, tennis) que le bloc canonique ne nomme pas.
- theorie · Tests cliniques : la liste bascule sur le *pourquoi* (axe 1) — ce que chaque manœuvre
  démontre, et surtout la hiérarchie qui les ordonne : « le premier partage n'est pas un test mais une
  comparaison : mobilité active diminuée avec passive conservée = atteinte de la coiffe ; les deux
  diminuées, surtout en rotation externe = atteinte articulaire ». La Se 86 % / Sp 50 % de Jobe y est
  lue (« sensible mais peu spécifique, il ouvre la question du supra-épineux, il ne la tranche pas »).
  source : SSP — Pièges — « Confondre limitation **active vs passive** : passive normale + active
  diminuée = **coiffe** ; toutes deux diminuées = **articulation** (capsulite, arthrose) »
- theorie · Anatomie : « Supra-épineux : abduction, plus fréquemment lésé » → « … **de loin le plus
  fréquemment lésé (environ 90 % des ruptures de coiffe)** » — le chiffre n'existait que dans
  `expert`/Points clés, réécrit par l'axe 7.
- presentation · Q1 examens, Q1 et Q2 prise en charge, Q1 prévention : les **quatre** réponses en
  liste deviennent des **réponses orales**. La réponse « examens » y gagne l'ECG (cohérence avec
  `resume`) et la réponse « traitement initial » le conseil sur le tramadol non prescrit, qui était
  porté par la sous-section Pièges supprimée.
- presentation · argument POUR « Douleur nocturne empêchant le sommeil » → « **Douleur nocturne
  invalidante, signe fort de rupture** » : l'item recopiait `resume` au caractère près (paire à
  **1.00**) ; un argument doit argumenter, non décrire — c'est le changement de format que la règle
  exige.
- expert · Points clés : réécrits en registre d'**observation d'examinateur** (axe 7).

**Signalements de sécurité** — **trois**, tous corrigés :
1. **Aucun ECG ni troponine dans le bloc canonique** d'une station de douleur d'**épaule gauche** chez
   un homme de **52 ans**, alors que « manquer un SCA atypique — ECG systématique chez > 50 ans » est
   le piège éliminatoire n° 1 de la page SSP. La cause cardiaque n'était qu'allusive, en bloc expert.
2. **Examen du rachis cervical absent de la grille entière** : la névralgie cervico-brachiale C5-C6,
   qui mime la tendinopathie d'épaule, n'était ni dans l'examen clinique ni dans le diagnostic
   différentiel.
3. **Le lift-off attribué à deux tests différents** dans la même liste de `theorie` — un candidat
   suivant ce bloc explore le sous-scapulaire en croyant tester l'infra-épineux.

**Vérifications communes aux quatre grilles**

- `check_invariants.py` → `OK — 40 grilles, tous les invariants preserves` (code 0). Les champs gelés
  couvrent `maxScores`, `scoreSpans`, `criteriaCount`, `detailCount`, `radioCount`, `checkboxCount` :
  **barème inchangé**, aucun sous-item noté ajouté ni retiré sur les quatre grilles.
- `check_nomenclature.py` → `OK — aucun terme non suisse detecte` (code 0). Aucune valeur en `g/dL`,
  `ng/mL`, `pg/mL`, `/mm³`, en livres ni en unité implicite n'a été introduite ; les seules unités
  ajoutées sont `µmol/L` (bilirubine conjuguée, AMBOSS-37) et `mmHg` (AMBOSS-35).
- `check_no_loss.py 544ea59` : 22 items signalés sur AMBOSS-35, 14 sur AMBOSS-37, 43 sur AMBOSS-38 et
  35 sur AMBOSS-39, **tous relus un par un**. Aucune perte : ce sont des reformulations, des
  corrections assumées et documentées ci-dessus, ou des passages de liste à réponse orale. Les items
  supprimés au titre de l'axe 6 ou de la règle du format ont été comparés au bloc canonique **avant**
  suppression, et ce qui leur était propre y a été porté d'abord.
- Aucun `.criteria-text` ni crochet de réponse patient touché ; items ICE du critère `m4` intacts ;
  aucun bloc créé. Équilibre `<div>` / `</div>` du fichier entier vérifié à zéro sur les quatre grilles.
- Redondance globale de ces quatre grilles : **40 paires → 2**.

### Passe typographique — caractère `:` parasite dans les valeurs numériques (tâche 12b)

**Exception au gel des sections notées, explicitement autorisée par l'utilisateur.** Les 14
corrections ci-dessous portent toutes sur des blocs `therapy-section` situés **hors** de la zone
pédagogique, donc dans du contenu gelé depuis le début du projet. L'utilisateur a autorisé cette
exception **au motif que la correction est purement typographique** : elle retire un caractère
parasite introduit à l'import, sans changer le nombre de sous-items, les checkboxes ni les
`maxScores`. Le gel portait sur l'ajout et le retrait d'items, pas sur la réparation d'un caractère
parasite. Treize corrections sur quatorze consistent au retrait exact de la chaîne `: `
(deux-points + espace) ; la quatorzième restaure les quatre lettres d'un nom de molécule tronqué.

**Origine du défaut** — présent **dès le commit initial** `0ba8bca` (« Initial commit via Netlify »)
sur les dix grilles concernées : c'est bien un défaut d'import, non une régression du projet. Aucune
version intacte n'existe donc dans l'historique git, et aucune reconstitution n'a pu être vérifiée
par `git show` — chacune l'a été par son contexte clinique et par des formes intactes voisines.

**Modifications** — décimales coupées (3)

- AMBOSS-14 · SCA : « Nitroglycérine sublinguale 0.: 4mg » → « Nitroglycérine sublinguale **0.4mg** »
- AMBOSS-35 · angor stable : « Nitroglycérine sublinguale 0.: 4 mg » → « Nitroglycérine sublinguale **0.4 mg** »
- AMBOSS-34 · thrombolyse : « Alteplase 0.: 9 mg/kg (max 90 mg) » → « Alteplase **0.9 mg/kg** (max 90 mg) »
  reconstitution confirmée par le plafond de la même ligne : 0,9 mg/kg × 100 kg = 90 mg.

**Modifications** — plages posologiques coupées (10)

- AMBOSS-14 · SCA : « Morphine 2-: 4mg IV » → « Morphine **2-4mg** IV »
- AMBOSS-29 · mononucléose : « Paracétamol 500-: 1000 mg × 3-4/j » → « Paracétamol **500-1000 mg** × 3-4/j »
- AMBOSS-30 · mononucléose : « Paracétamol 500-: 1000 mg × 3-4/j » → « Paracétamol **500-1000 mg** × 3-4/j »
- AMBOSS-33 · méningite : « Vancomycine 15-: 20 mg/kg × 2/j IV » → « Vancomycine **15-20 mg/kg** × 2/j IV »
- AMBOSS-35 · angor stable : « Aspirine 160-: 325 mg » → « Aspirine **160-325 mg** »
- AMBOSS-35 · angor stable : « métoprolol 25-: 50 mg × 2/j » → « métoprolol **25-50 mg** × 2/j »
- AMBOSS-38 · fracture de stress : « Apports calciques 1000-: 1200 mg/j » → « Apports calciques **1000-1200 mg/j** »
- AMBOSS-40 · paralysie faciale : « Prednisone 60-: 80 mg/j × 5j » → « Prednisone **60-80 mg/j** × 5j »
- AMBOSS-40 · Ménière, crise aiguë : « Diazépam 5-: 10 mg IV/IM » → « Diazépam **5-10 mg** IV/IM »  ← **hors liste initiale**
- AMBOSS-40 · Ménière, fond : « Bétahistine 16-: 24 mg × 2/j » → « Bétahistine **16-24 mg** × 2/j »  ← **hors liste initiale**

**Modification** — nom de molécule tronqué (1)

- AMBOSS-33 · méningite : « Ceftria: 2g × 2/j IV » → « **Ceftriaxone** 2g × 2/j IV »
  Vérification demandée, en trois points : (a) le bloc `annexe-theorie` de la même grille prescrit
  « Méningite empirique : **C3G** + vancomycine + ampicilline », et les trois autres lignes du bloc
  noté sont précisément vancomycine, ampicilline (si > 50 ans) et dexaméthasone — le terme manquant
  est donc une céphalosporine de 3ᵉ génération ; (b) parmi les C3G, seule la **ceftriaxone** possède
  le radical `Ceftria` conservé (la céfotaxime aurait laissé `Céfota`) ; (c) la posologie **2 g × 2/j
  IV** est bien la dose méningée de la ceftriaxone — le double de la dose des autres indications —,
  cohérente avec l'énoncé restant.

**Notation décimale** — le point a été retenu (`0.4`, `0.9`) et non la virgule, conformément à
l'usage majoritaire mesuré sur le corpus : 46 décimales au point contre 16 à la virgule en zone
notée, 52 contre 23 en zone pédagogique (bloc `<script>` exclu). L'usage local est plus net encore :
la ligne voisine d'AMBOSS-34 écrit « Thrombolyse IV (si **4.5**h du début) » et « INR **1.7** », celle
d'AMBOSS-35 « ramipril **2.5**- ». La virgule reste la forme des prose pédagogiques récemment
rédigées (« 37,5 °C », « NaCl 0,9 % ») : les deux conventions cohabitent par zone, et l'édition n'a
pas cherché à les uniformiser au-delà de son périmètre.

**Espacement** — préservé tel quel dans chaque site : la correction retire `: ` et rien d'autre.
AMBOSS-14 garde donc `0.4mg` et `2-4mg` sans espace, comme son voisin intact « Aspirine: 300mg » ;
AMBOSS-35 garde `0.4 mg` et `160-325 mg` avec espace. Forme cible confirmée par une plage **intacte**
du même fichier qu'une des corrections : AMBOSS-40 écrit « Antivertigineux: Méclizine **25-50** mg
× 3/j ».

**Divergences consignées** — quatre mots tronqués **non corrigés**, laissés à l'arbitrage

Le balayage a révélé que la troncature de `Ceftria` n'était pas isolée : le défaut coupe le mot à un
`x` et absorbe les lettres suivantes jusqu'au chiffre (`Ceftria|xone `, `Amo|xicilline `,
`Céfo|xitine `, `Ciproflo|xacine `, `Ma|ximum `). Ces quatre-là ne sont pas corrigés parce que leur
réparation exige de **restituer des lettres perdues** — ce n'est plus typographique — et parce que
la lecture n'est pas unique. La règle n'est du reste pas fiable : `Dexaméthasone: 10 mg`, dans le
même bloc qu'AMBOSS-33, contient un `x` et est resté intact.

- AMBOSS-2 · antibioprophylaxie péri-opératoire : « **Amo**: 2g IV » — « Amoxicilline 2 g » et
  « Amoxicilline-acide clavulanique 2 g » produisent le **même** tronçon `Amo`. Deux molécules
  distinctes : non corrigé.
- AMBOSS-2 · antibioprophylaxie péri-opératoire : « **Céfo**: 2g IV + métronidazole 500 mg IV » —
  la céfoxitine est la seule céphalosporine dont le radical donne `Céfo` (la céfuroxime donnerait
  `Céfuro`), mais son association au métronidazole est redondante, la céfoxitine couvrant déjà les
  anaérobies. Le contexte ne tranche pas : non corrigé.
- AMBOSS-2 · antibioprophylaxie péri-opératoire : « **Ciproflo**: 400 mg IV + métronidazole 500 mg
  IV » — « ciprofloxacine 400 mg IV » est la seule lecture plausible, mais la ligne appartient au
  même bloc de trois que les deux précédentes : corriger une ligne sur trois y serait arbitraire.
- AMBOSS-39 · infiltration : « **Ma**: <span>•</span> Maximum 3 injections/an » — le fragment `Ma: `
  précède un bullet intact « Maximum 3 injections/an ». La réparation consisterait à **supprimer** un
  fragment, donc à toucher au nombre de puces : hors mandat par construction.

**Divergences consignées** — deux autres artefacts d'import, non corrigés

- AMBOSS-39 · pronostic : « Taux guérison 95% avec **antiviraux action directe**x succès conservateur:
  70-80% ruptures partielles ». La mention d'antiviraux à action directe (vocabulaire de l'hépatite C)
  dans une station de **rupture de coiffe des rotateurs** est un contenu étranger ; le `x` accolé et
  le `: ` intercalé signent le même défaut d'import. Réécriture de fond, hors mandat typographique.
- AMBOSS-38 · fracture de stress : « Apports calciques 1000-1200 mg/j ; Vitamine D 800-1000 UI/j ;
  Éviter déficit énergétique **× Vitamine D 800-1000 UI/j** » — la mention de vitamine D est
  **dupliquée** dans la même puce, raccordée par un `×` parasite. Seule la plage `1000-: 1200` a été
  réparée ; la déduplication supposerait de retirer du texte d'une section notée.

**Vérifications**

- `check_invariants.py` → `OK — 40 grilles, tous les invariants preserves` (code 0). C'est la preuve
  que le barème n'a pas bougé : `maxScores`, `scoreSpans`, `blocks`, `criteriaCount`, `detailCount`,
  `radioCount`, `checkboxCount` tous identiques au snapshot.
- `check_nomenclature.py` → `OK — aucun terme non suisse detecte` (code 0).
- `report_redundancy.py` → `TOTAL : 85 paire(s)`, **identique** au total relevé avant les
  modifications.
- `check_no_loss.py f623e5a` → `TOTAL : 0 item(s) disparu(s) sur 8 grille(s) modifiee(s)`.
- Balayage final sur les 40 grilles (`strip_base64` appliqué, jamais de `grep` brut) : **0 occurrence
  résiduelle** des motifs `\d+\s*-\s*:\s*\d+` et `\d+[.,]\s*:\s*\d+`. Restent les 4 mots tronqués
  consignés ci-dessus, délibérément.
- `git diff --stat` : 8 fichiers, **14 insertions / 14 suppressions**, une ligne modifiée par
  correction. Aucun `.criteria-text` touché, aucun crochet de réponse patient touché, aucun sous-item
  ajouté ni retiré.

---

## Tâche 13 — cinq grilles allégées (AMBOSS-10, 16, 17, 20, 21)

Ces cinq grilles ne portent que **deux** blocs pédagogiques, `annexe-expert` et
`annexe-theorie` : ni `resume`, ni `presentation`. Les axes 1 à 6 du contrat, qui portent sur
ces deux blocs absents, ne s'appliquent pas. Le seul axe applicable est le contrat de rôle
`expert` (faire tourner la station) ↔ `theorie` (comprendre le cas), et l'axe 7 (points clés
différenciés). Aucun bloc n'a été créé : `blocks` reste `["expert", "theorie"]` sur les cinq,
vérifié par `check_invariants.py`.

`resume` n'existant pas, il n'y a pas de source canonique habituelle. Les contradictions entre
`expert` et `theorie` ont été arbitrées par la hiérarchie à trois niveaux, et à défaut par le
contrat de rôle : `theorie` porte le raisonnement, `expert` la conduite.

Redondance mesurée par `report_redundancy.py` : **4 paires → 0** (10 : 0→0 · 16 : 1→0 ·
17 : 1→0 · 20 : 0→0 · 21 : 2→0).

### AMBOSS-10 — Douleurs dorsales et raideur, homme de 26 ans (page SSP : Lombalgies)

**Modifications**

*Contrat de rôle — `expert`/Points clés purgé de la théorie*

- expert · Points clés : « HLA-B27 positif dans 90% spondylarthrite ankylosante » supprimé —
  épidémiologie pure, portée par `theorie`/Spondylarthrite ankylosante (« Association HLA-B27 :
  90-95% des cas », valeur **plus précise**) et par `theorie`/Examens (« Pas diagnostique seul,
  8% population générale positive »). Aucune perte.
- expert · Points clés : « Sacro-iliite précoce peut être uniquement clinique (IRM plus sensible
  que radio) » supprimé après **portage** de sa nuance dans `theorie`/Examens complémentaires
  (section de queue), dont la ligne radiographique devient « Sacro-iliite bilatérale — signe
  tardif, la radio peut rester normale des années (forme non radiographique, sacro-iliite d'abord
  clinique) ». Le portage précède la suppression, jamais l'inverse.

*Sécurité — niveau 1, la page SSP tranche*

- expert · Pièges : ajout de « Ne pas dépister le syndrome de la queue de cheval devant toute
  lombalgie : troubles sphinctériens, anesthésie en selle, déficit moteur bilatéral → IRM en
  urgence ».
  source : SSP — Lombalgies — frontmatter `pieges_eliminatoires` — « **Manquer queue de cheval
  (urgence chir)** » (piège éliminatoire n° 1) ; § EXAMEN CLINIQUE — « **À faire ✅** : toujours
  rechercher les troubles sphinctériens + sensibilité périnéale (queue de cheval) » ; § Red flags —
  « Sciatique bilatérale + anesthésie en selle + troubles sphinctériens → Syndrome de la queue de
  cheval · IRM lombaire en URGENCE immédiate ».
  Vérifié avant ajout : les motifs « queue de cheval », « sphinct » et « anesthésie en selle » ne
  figuraient **nulle part** dans la grille (recherche sur `strip_base64`, jamais de `grep` brut).
  La section notée dépiste bien les symptômes sous des libellés génériques (« Problèmes urinaires »,
  « Problèmes intestinaux », « Engourdissement (particulièrement membres inférieurs) », « Dysfonction
  érectile ») mais aucun bloc pédagogique n'en donnait la raison. Section notée intacte.

*Erreur factuelle interne (correction directe, hors hiérarchie)*

- theorie · Arthrite psoriasique : « Dactylite : **pathognomonique** des spondylarthropathies » →
  « Dactylite (« doigt en saucisse ») : **très évocatrice** des spondylarthropathies ». La dactylite
  n'est pas pathognomonique : elle s'observe aussi dans la drépanocytose, la sarcoïdose, la
  tuberculose et la goutte. Aucune autre source de la grille ne porte cet énoncé — il n'y avait rien
  à arbitrer, seulement un fait faux à corriger.

**Divergences consignées**

- theorie · Spondylarthrite ankylosante : « Prévalence : 0.5-1% population » est haut pour la
  spondylarthrite ankylosante stricte (0.1-0.5 % en Europe) mais compatible avec la
  spondyloarthrite axiale au sens large. Ni la page SSP ni la section notée ne donnent de chiffre :
  niveau 3, laissé inchangé.

### AMBOSS-16 — Troubles du sommeil, femme de 32 ans (page SSP : Troubles du Sommeil)

**Modifications**

*Contrat de rôle — la paire de redondance et son voisinage*

- expert · Points clés : « TCC-I = traitement première ligne insomnie chronique » supprimé — c'est
  la paire détectée à 0.83 par `report_redundancy.py` face à `theorie`/Rappels thérapeutiques
  (« TCC-I : 6-8 séances, première ligne insomnie chronique »). Même format, même contenu ;
  `theorie` en dit strictement plus (nombre de séances) et porte en outre toute la section TCC-I
  (efficacité, restriction de sommeil, contrôle du stimulus).
- expert · Points clés : « Éviter benzodiazépines (risque dépendance) » supprimé — porté deux fois
  ailleurs : `theorie`/Pharmacothérapie (« Benzodiazépines : éviter (tolérance, dépendance) »,
  rationnel) et `expert`/Pièges (« Prescrire hypnotiques d'emblée », conduite). Aucune perte.

*Sécurité — niveau 1, la page SSP tranche*

- expert · Pièges : ajout de « Banaliser le réveil précoce : ne pas rechercher une dépression ni le
  risque suicidaire (PHQ-9, question directe sur les idées noires) ».
  source : SSP — Troubles du Sommeil — § Points Clés ECOS — « 5. Devant un **réveil précoce** →
  rechercher une **dépression** et la **suicidalité** » ; § Pièges à éviter — « 3. Banaliser un
  réveil précoce (signe classique de dépression) » ; § Red flags — « Insomnie + dépression avec
  idéations suicidaires actives → Crise suicidaire · URGENCE psychiatrique ».
  La patiente **présente** le réveil précoce (section notée, « Réveil précoce [Oui. Je me réveille
  généralement avant que mon réveil sonne] ») ; aucun bloc de la grille ne mentionnait la
  suicidalité. `theorie`/Examens citait déjà le PHQ-9, sans jamais dire pourquoi.

*Incohérence interne à `theorie` — deux seuils de caféine*

- theorie · Rappels thérapeutiques : « Restriction caféine : Maximum 200-300mg/j, rien après 14h »
  → « Restriction caféine : sevrage progressif, cible ≤ 200-300 mg/j (2-3 tasses) chez
  l'insomniaque, rien après 14h ». Le même bloc portait deux plafonds différents sans qualificatif :
  `theorie`/Caféine et sommeil dit « Limite recommandée : 400mg/j », valeur que la page SSP tranche
  explicitement (§ Hygiène du sommeil — « Caféine (quantité, horaire — **seuil > 400 mg/j**) »).
  Les 200-300 mg/j sont une **cible thérapeutique** chez l'insomniaque, non un second plafond
  général : la qualification lève la contradiction sans rien retirer. Le « sevrage progressif »
  reprend `theorie`/Caféine (« Sevrage : céphalées, fatigue, irritabilité 24-48h »).

*Alignement niveau 1 — pratique suisse*

- theorie · Examens complémentaires : « Polysomnographie : Si suspicion apnées ou mouvements
  périodiques » → « Polygraphie nocturne ambulatoire (1er examen recommandé, moins coûteux) ou
  polysomnographie : … ».
  source : SSP — Troubles du Sommeil — § EXAMENS COMPLÉMENTAIRES — « **Polygraphie nocturne**
  (1ᵉʳ examen recommandé, moins coûteux) ou **polysomnographie** si suspicion de SAOS » ; repris au
  § Apports des Cours — « Polygraphie nocturne : 1ᵉʳ examen recommandé (moins coûteux que la
  polysomnographie complète) ».

**Divergences consignées**

- Section notée, critère m3 · « Mesure de la pression artérielle sur 24 heures [Parce que cette
  patiente présente une pression artérielle élevée (**directives AHA/ACC 2017**)…] » — référentiel
  américain dans une grille suissifiée. Barème gelé, section notée non touchée : consigné.
- SSP · syndrome des jambes sans repos : la page l'inscrit dans les cinq diagnostics à « toujours
  chercher » et prescrit la ferritine (cible > 75 µg/L). Aucun bloc de la grille ne le mentionne.
  Non ajouté : l'absence ne crée pas de risque pour la patiente (contrairement à la suicidalité),
  et la vignette ne comporte aucune impatience des jambes. Consigné pour arbitrage.

### AMBOSS-17 — Troubles de mémoire, femme de 70 ans (page SSP : Troubles de la Mémoire & Démences)

**Modifications**

*Contrat de rôle — `expert`/Points clés ramené à ce que l'examinateur observe (axe 7)*

- expert · Points clés : « MMSE < 24/30 = démence (ajuster selon éducation) » supprimé — seuil
  théorique porté à l'identique par `theorie`/Mini-Mental State Examination (« Seuils : Normal ≥ 27,
  démence < 24 (ajuster éducation) »).
- expert · Points clés : « Alzheimer = démence la plus fréquente (60-70%) » supprimé **après
  portage** du chiffre dans `theorie`/Maladie d'Alzheimer, dont l'introduction devient « Démence
  neurodégénérative la plus fréquente (**60-70 % des démences**) ». Chiffre confirmé par la page SSP
  (§ En Bref — « Maladie d'Alzheimer (60-70 %) > démence vasculaire (~20 %) »).
- expert · Points clés : « Diagnostic clinique + exclusion causes réversibles » supprimé — doublon
  interne du point suivant (« Toujours rechercher causes traitables (B12, thyroïde) », conservé) et
  de `theorie`/Bilan démence en entier.
- expert · Points clés : « Planification précoce (directives anticipées) » supprimé — c'est la paire
  détectée à 0.72 face à `theorie`/Prise en charge Alzheimer (« Anticipation : tutelle, directives
  anticipées, conduite »), qui en est un **sur-ensemble strict**.

*Sécurité — niveau 1, la page SSP tranche : la pseudo-démence dépressive*

- expert · Pièges : ajout de « Conclure à une démence sans avoir exclu une dépression du sujet âgé
  (pseudo-démence) ni un delirium — la patiente réunit humeur triste, anhédonie, réveil précoce et
  anorexie (GDS-15) ».
  source : SSP — Troubles de la Mémoire & Démences — § DD Top 5 — « Maladie d'Alzheimer ·
  **Pseudo-démence dépressive** · … » (2ᵉ diagnostic différentiel) ; § Pièges à éviter — « 1. Conclure
  « démence » sans exclure un delirium ou une **dépression du sujet âgé** » ; § Tests complémentaires
  — « **GDS-15** : dépister une dépression du sujet âgé ».
  La section notée déroule un syndrome dépressif **complet** (§ 6 État psychologique : humeur basse
  depuis le décès du caniche il y a un an, perte d'intérêt pour le backgammon, énergie faible,
  concentration effondrée ; § 4 : réveil vers 4h-5h, appétit diminué), et aucun bloc pédagogique ne
  nommait la pseudo-démence dépressive ni le GDS-15.
- theorie · Bilan démence : « Bilan causes réversibles : TSH, B12, folates, calcémie » → « … TSH,
  B12, folates, calcémie, **natrémie** ; **dépression du sujet âgé (GDS-15)** ; **revue des
  médicaments à risque cognitif** (anticholinergiques, benzodiazépines — critères STOPP/START) ».
  source : SSP — § Points Clés ECOS — « 3. Exclure les causes réversibles : delirium, **dépression**,
  B12, TSH, HPN, **iatrogénie**, hématome sous-dural » ; frontmatter `pieges_eliminatoires` —
  « Manquer cause réversible (TSH, B12, syphilis, **médicaments**) » ; § ANAMNÈSE — « Médication :
  … appliquer les critères **STOPP/START** ». La patiente prend de l'hydrochlorothiazide, d'où la
  natrémie. Aucun sous-item noté ajouté ni retiré.

*Erreur de suissification (niveau 1) — la tutelle n'existe plus pour l'adulte en Suisse*

- theorie · Prise en charge Alzheimer : « Anticipation : **tutelle**, directives anticipées,
  conduite » → « Anticipation : directives anticipées et **mandat pour cause d'inaptitude**
  (art. 360 ss CC), signalement à l'**APEA/KESB** pour une **curatelle** adaptée si besoin de
  protection (art. 390 ss CC), aptitude à la conduite (**art. 15d LCR**) ».
  source : SSP — § Aspects médico-légaux (cadre suisse) — « Directives anticipées et **mandat pour
  cause d'inaptitude** (art. 360 ss et 370 ss CC) … Si capacité de discernement altérée et besoin de
  protection → signalement à l'**APEA / KESB** → **curatelle** adaptée (art. 390 ss CC) … annonce
  possible au médecin cantonal / Service des automobiles (**art. 15d LCR**) ».
  La tutelle de l'adulte a été **abolie** par la révision du droit de la protection de l'adulte
  entrée en vigueur le 1ᵉʳ janvier 2013 ; le terme ne subsiste que pour les mineurs. L'employer pour
  une femme de 70 ans était faux en droit suisse. C'est également la reprise de la
  `pieges_eliminatoires` « Pas d'évaluation conduite (LCR art. 15d) ».

*Erreur factuelle interne (correction directe, hors hiérarchie)*

- theorie · Hydrocéphalie à pression normale : « IRM : dilatation ventriculaire, **angle calleux
  < 40°** » → « **angle calleux < 90° (normal 100-120°)** ». Le seuil de l'angle calleux dans l'HPN
  est de 90° (Ishii et al. : ~60° dans l'HPN contre ~104° dans la maladie d'Alzheimer) ; 40° n'est le
  seuil d'aucune référence et aurait fait manquer la **seule démence potentiellement curable**. Ni la
  page SSP ni la section notée ne donnent de valeur : rien à arbitrer, un fait faux à corriger.

**Divergences consignées**

- Section notée, critère « Mini-Mental State Examination » : deux américanismes dans les réponses
  de la patiente standardisée — « Répondre avec **président des États-Unis** incorrect » et
  « Répondre avec l'**État** correct ». L'orientation temporelle et spatiale d'un MMSE suisse
  interrogerait le conseiller fédéral / le président de la Confédération et le canton. Barème gelé,
  section notée non touchée : consigné.
- theorie · Rappels : la mémantine est indiquée « MMSE < 15 » tandis que `theorie`/Prise en charge
  place les anticholinestérasiques à « MMSE 10-26 » — il subsiste une zone (MMSE 15-19) où aucune
  ligne ne tranche. Les deux plages sont défendables : niveau 3, laissé inchangé.

### AMBOSS-20 — Diminution de sensation dans les extrémités, homme de 42 ans (page SSP : Neuropathie Périphérique)

**Vérification préalable — cohérence de la conversion B12 (tâche 12)**

Contrôlée avant et après travail, intacte : `expert` porte « Vitamine B12 : **63 pmol/L**
(N: **148-664**) » et la queue de `theorie` « Vitamine B12 sérique : **< 148 pmol/L** = déficit ».
63 < 148 → le déficit annoncé est bien lu, et la borne basse de l'intervalle coïncide au pmol près
avec le seuil de la queue. Les quatre nombres issus de « 85 pg/mL (N: 200-900) » restent cohérents
entre eux (× 0,738). **Aucune de ces deux lignes n'a été modifiée.**

**Modifications**

*Contrat de rôle — `expert`/Points clés purgé de la théorie*

- expert · Points clés : « IPP + malabsorption = double risque déficit B12 » supprimé —
  `theorie`/Déficit en vitamine B12 porte « Causes : malabsorption (**IPP, pancréatite**),
  alcoolisme, régime végétarien », sur-ensemble strict.
- expert · Points clés : « Traiter B12 avant folates (éviter aggravation neuro) » supprimé après
  **portage du rationnel** dans `theorie`/Rappels, dont la ligne devient « Folates : 5 mg/j APRÈS
  début B12 — **donnés seuls, ils corrigent l'anémie mais laissent progresser l'atteinte
  neurologique** ». La conduite reste par ailleurs dans `expert`/Pièges (« Donner folates avant
  B12 »). L'item figurait donc trois fois ; il en reste deux, chacune dans son bloc de rôle.
- expert · Points clés : « Pancréatite chronique → diabète secondaire fréquent » supprimé après
  **portage** dans `theorie`/Polyneuropathie diabétique, dont l'introduction devient « Complication
  microvasculaire du diabète — **y compris du diabète secondaire à une pancréatite chronique
  (type 3c), fréquent dans ce contexte** ». Cette information n'existait nulle part ailleurs : sans
  le portage, la suppression aurait été une perte.
- expert · Points clés : « Neuropathie peut être multifactorielle » supprimé — c'est la thèse même
  de `theorie`/Diagnostic le plus probable (« Polyneuropathie **mixte** : déficit sévère en B12 …
  **+** polyneuropathie alcoolique ») et la conduite est dans `expert`/Pièges (« Ne tester qu'une
  seule cause de neuropathie »).

Les deux points conservés dans `expert`/Points clés — « Romberg + = atteinte cordons postérieurs
(B12) » et « CAGE 4/4 = dépendance alcoolique sévère » — sont exactement les deux résultats positifs
que l'examinateur délivre et qui sont produits par la station (« Test de Romberg [Positif] » en
section notée ; les quatre questions CAGE toutes positives à l'anamnèse).

*Alignement niveau 1 — bilan de 1ʳᵉ intention de toute polyneuropathie*

- theorie · Examens complémentaires : « TSH, créatinine : éliminer autres causes » → « TSH,
  créatinine, **folates**, **thiamine**, **électrophorèse des protéines sériques** : éliminer les
  autres causes (hypothyroïdie, urémie, carences associées, **gammapathie monoclonale**) ».
  source : SSP — Neuropathie Périphérique — § Bilan de 1ʳᵉ intention (SGAIM/SSN) — « Vitamine B12
  (…), **folates** » et « **Électrophorèse des protéines sériques + immunofixation** (gammapathie
  monoclonale, MGUS, amyloïdose AL) » ; § Points Clés ECOS — « 5. Demander le bilan de 1ʳᵉ intention
  (glycémie / HbA1c, B12, TSH, **électrophorèse**) ». La section notée les demande déjà
  (critères m2 et m3), la théorie ne les justifiait pas.

**Divergences consignées**

- theorie · Rappels : « Gabapentine : 300 mg × 3/j, augmenter progressivement » se lit comme un
  **début** à 900 mg/j, ce qui est la dose du 3ᵉ jour du schéma de titration usuel, chez un patient
  éthylique à risque de sédation et de chute. La formulation reste défendable (le libellé Neurontin®
  atteint 300 mg × 3/j à J3) et ni la page SSP ni la section notée ne donnent de posologie :
  niveau 3, laissé inchangé, consigné.
- theorie · Rappels : la duloxétine, citée en 1ʳᵉ ligne de la douleur neuropathique par la page SSP
  (§ Douleur neuropathique — SGAIM/SSN), est absente de la grille. Non ajoutée : les trois autres
  molécules de 1ʳᵉ ligne y sont, l'absence ne crée pas de risque. Consigné.

### AMBOSS-21 — Hématurie, homme de 23 ans (page SSP : Hématurie)

**Vérification préalable — valeurs converties en tâche 3**

Contrôlées, cohérentes avec leurs qualificatifs voisins, **non touchées** :
« C3 : **0.45 g/L** (N: 0.9-1.8) - **abaissé** » (0,45 < 0,9 ✓), « C4 : **0.25 g/L** (N: 0.1-0.4) -
**normal** » (0,25 dans l'intervalle ✓, cohérent avec `theorie` « C4 normal : voie classique non
activée »), « Créatinine : **159 μmol/L** (**légèrement élevée**) » (~1,5 × la limite supérieure de
l'homme adulte ✓).

**Modifications**

*Contrat de rôle — les deux paires de redondance : le résultat à `expert`, le pourquoi à `theorie`*

Les deux paires détectées à 0.82 opposaient un **résultat de station** (dans `expert`) au **même
résultat** recopié dans la section de queue de `theorie`. La queue de `theorie` ne se supprime ni ne
se déplace : c'est son contenu qui a été ramené à son rôle, le *pourquoi* de l'examen.

- theorie · Examens complémentaires : « Analyse urine + sédiment : hématurie, protéinurie,
  cylindres » → « Analyse d'urine + sédiment : **hématies déformées et cylindres hématiques =
  origine glomérulaire** (hématies normales et caillots = origine urologique) ; quantifier par le
  **rapport protéinurie/créatininurie** ».
  source : SSP — Hématurie — § Glomérulaire vs urologique — distinction clé (tableau : « Sédiment —
  Hématies déformées, cylindres hématiques » vs « Hématies normales, pas de cylindre » ; « Caillots
  — Absents » vs « Présents ») ; § EXAMENS COMPLÉMENTAIRES, 1re intention — « FSC, créatinine,
  ionogramme · **rapport protéinurie / créatininurie** ». Le résultat reste dans `expert`
  (« Analyse urine : hématurie +++, protéinurie ++, cylindres hématiques »).
- theorie · Examens complémentaires : « Échographie rénale : reins augmentés taille, échostructure
  normale » → « Échographie **réno-vésicale** : **écarter une cause urologique** (lithiase, obstacle,
  masse, dilatation) — non contributive au diagnostic positif de GNAPS ».
  source : SSP — § EXAMENS COMPLÉMENTAIRES, 1re intention — « **Échographie réno-vésicale** : masse,
  lithiase, dilatation, résidu post-mictionnel ». Le résultat reste dans `expert` (« Échographie :
  reins taille augmentée, échostructure normale ») **et** dans la section notée (critère m2).

*Contrat de rôle — `expert`/Points clés*

- expert · Points clés : « Syndrome néphritique complet : hématurie + HTA + œdèmes » supprimé —
  `theorie`/Syndrome néphritique aigu développe la triade sur six items (hématurie, HTA, œdèmes,
  protéinurie, oligurie, cylindres) avec leur mécanisme.
- expert · Points clés : « C3 bas + ASLO élevé = diagnostic GNPS quasi certain » supprimé —
  `theorie`/Diagnostic biologique GNAPS porte les deux marqueurs et leur signification, et
  `theorie`/Néphropathie à IgA vs GNAPS porte la **combinaison** (« GNAPS : C3 bas transitoire,
  ASLO élevé »).
- expert · Points clés : « Pas de corticoïdes dans GNPS (différent autres GN) » supprimé après
  **portage** dans `theorie`/Rappels thérapeutiques : « Pas de corticoïdes ni d'immunosuppresseurs
  dans la GNAPS, à la différence des autres glomérulonéphrites : le traitement est symptomatique ».
  L'information n'existait nulle part ailleurs — sans le portage, la suppression aurait été une
  perte, et une perte thérapeutique.
- expert · Points clés : sigle harmonisé « GNPS » → « **GNAPS** », forme employée six fois par
  `theorie` et par le titre du diagnostic. Les deux sigles coexistaient dans la même grille.

*Contradiction `expert` ↔ `theorie` tranchée par le contrat de rôle*

- expert · Pièges : « Confondre avec néphropathie IgA (**délai 2-5 jours**) » → « Confondre avec
  néphropathie IgA (hématurie **synpharyngitique, 1-3 jours** après l'infection) ». `theorie`
  écrivait « IgA : hématurie **1-3 jours** post-infection (synpharyngitique) » : les deux blocs
  donnaient un délai différent pour le **discriminant même du cas**. Ni la page SSP (« Berger =
  post-IVRS du sujet jeune », sans délai) ni la section notée ne tranchent — niveau 3. Le contrat de
  rôle s'applique alors : le raisonnement appartient à `theorie`, c'est donc `expert` qui s'aligne.

*Posologies pédiatriques sur une station adulte — correction avec conservation des deux valeurs*

Le bloc `theorie`/Rappels était rédigé pour une GNAPS **de l'enfant** (pic 5-12 ans) alors que la
station est un homme de **23 ans**. Chaque ligne reçoit la valeur adulte, la valeur pédiatrique
étant conservée entre parenthèses — rien n'est perdu :

- « Furosémide : 1-2 mg/kg si œdèmes importants » → « Furosémide : **20-40 mg IV ou PO chez
  l'adulte** (1-2 mg/kg chez l'enfant) si œdèmes importants ».
- « Antihypertenseurs si TA > **95e percentile** » → « Antihypertenseurs si TA **≥ 140/90 mmHg chez
  l'adulte** (> 95e percentile chez l'enfant) ». Il n'existe pas de courbe de percentiles tensionnels
  pour l'adulte : le critère était inapplicable à cette station.
- « Pénicilline V : 250-500 mg × 2/j × 10j » → « Pénicilline V : **500 mg × 2/j × 10 j chez
  l'adulte** (250 mg × 2/j chez l'enfant) si streptocoque actif ». La borne basse de la plage était
  la dose de l'enfant de moins de 27 kg.

**Divergences consignées**

- `annexe-dd` (bloc de diagnostics différentiels, **hors zone pédagogique**, à l'intérieur de la
  section Management) prescrit « **Repos au lit** phase aiguë » tandis que `theorie`/Rappels dit
  « **Repos relatif** phase aiguë (**pas alitement strict**) ». La doctrine actuelle est celle de
  `theorie` ; `annexe-dd` n'est ni un bloc pédagogique au sens de l'outillage ni un critère noté, et
  se trouve hors du périmètre de la tâche. Non corrigé, consigné.
- L'hospitalisation : la page SSP la réserve au syndrome néphritique avec **HTA sévère** et IRA
  (§ Red flags). La TA du patient est 135/85 mmHg et la créatinine 159 μmol/L : « Surveillance simple
  suffit souvent, hospitalisation si sévère » (`expert`) reste juste pour ce cas. Aucune divergence.

**Vérifications (tâche 13)**

- `check_invariants.py` → `OK — 40 grilles, tous les invariants preserves` (code 0). `blocks` reste
  `["expert", "theorie"]` sur les cinq grilles ; `maxScores`, `scoreSpans`, `criteriaCount`,
  `detailCount`, `radioCount`, `checkboxCount` inchangés : **barème gelé**.
- `check_nomenclature.py` → `OK — aucun terme non suisse detecte` (code 0).
- `report_redundancy.py` par grille : **4 paires → 0** (10 : 0→0 · 16 : 1→0 · 17 : 1→0 · 20 : 0→0 ·
  21 : 2→0).
- `check_no_loss.py ce250fd` par grille : 4 + 3 + 6 + 6 + 7 = **26 items signalés**, tous relus
  un à un — 13 reformulations enrichies (l'item reste, réécrit), 8 suppressions dont le contenu est
  porté à l'identique ou en plus précis par un autre bloc, 4 portages explicites documentés
  ci-dessus (dont deux vers un `<p>`, invisible à `check_no_loss.py` qui ne lit que les `<li>`),
  1 correction intentionnelle (« tutelle », faux en droit suisse). **Aucune perte réelle.**
- `git diff --numstat` : 5 fichiers, **22 insertions / 33 suppressions**, toutes dans la zone
  pédagogique. Aucun `.criteria-text` touché, aucun crochet de réponse patient touché, aucun
  sous-item noté ajouté ni retiré, aucun item ICE touché.

## Tâche 14 — cinq grilles allégées (AMBOSS-23, 24, 25, 26, 27)

Comme en tâche 13, ces cinq grilles ne portent que **deux** blocs pédagogiques, `annexe-expert`
et `annexe-theorie` : ni `resume`, ni `presentation`. Les axes 1 à 6 du contrat ne s'appliquent
pas ; seul opère le contrat de rôle `expert` (faire tourner la station : résultats à délivrer,
pièges du candidat) ↔ `theorie` (comprendre le cas : raisonnement, physiopathologie). **Aucun
bloc n'a été créé** : `blocks` reste `["expert", "theorie"]` sur les cinq, vérifié par
`check_invariants.py`.

`resume` n'existant pas, il n'y a pas de source canonique. Les contradictions `expert` ↔
`theorie` ont été arbitrées par la hiérarchie à trois niveaux, et à défaut par le contrat de
rôle : `theorie` porte le raisonnement, `expert` la conduite.

Redondance mesurée par `report_redundancy.py` : **9 paires → 0** (23 : 4→0 · 24 : 2→0 ·
25 : 0→0 · 26 : 0→0 · 27 : 3→0).

### AMBOSS-23 — Perte auditive, homme de 65 ans (page SSP : Perte d'Audition)

**Modifications**

*Contrat de rôle — `expert`/Points clés purgé de la théorie (3 des 4 paires détectées)*

- expert · Points clés : « Presbyacousie = 1ère cause surdité > 65 ans » supprimé après
  **portage** dans `theorie`/Presbyacousie, dont la ligne d'épidémiologie devient « Prévalence :
  30% > 65 ans, 60% > 75 ans — **1ère cause de surdité après 65 ans** ». Le portage précède la
  suppression.
  source : SSP — § DD Top 5 — la `presbyacousie` y est citée en tête des cinq diagnostics.
- expert · Points clés : « Aspirine ototoxique réversible, cisplatine irréversible » supprimé —
  `theorie`/Ototoxicité médicamenteuse porte les deux molécules **en plus précis** (« Cisplatine :
  ototoxicité irréversible dose-dépendante (30-80%) », « Aspirine : ototoxicité réversible à forte
  dose (> 3g/j) »). Aucune perte.
- expert · Points clés : « Appareillage bilatéral meilleur que monaural » supprimé après
  **portage** du comparatif dans `theorie`/Appareillage auditif : « Appareillage bilatéral
  **préférable au monaural** : meilleure localisation spatiale **et meilleure compréhension en
  milieu bruyant** ». La gêne en milieu bruyant est le motif de consultation même du patient
  (réunions familiales, voix aiguë de la petite-fille).
- expert · Pièges : « Oublier médicaments ototoxiques » → « Oublier de **rechercher** les
  médicaments ototoxiques **à l'anamnèse** (cisplatine, aspirine à forte dose) ». L'item doublait
  `theorie`/Rappels « Éviter nouveaux médicaments ototoxiques » alors qu'il vise autre chose : le
  premier est un geste d'anamnèse (conduite), le second une consigne thérapeutique. Différenciés,
  rien supprimé. Le patient a reçu du cisplatine il y a 3 ans et prend de l'aspirine quotidienne.

*Contrat de rôle — le résultat à `expert`, le pourquoi à `theorie` (4e paire)*

Les deux dernières paires opposaient le **résultat de station** (`expert`/Rôles : « Audiométrie
vocale : 60% discrimination à 65 dB ») aux deux descriptions du test dans `theorie`. Le résultat
reste dans `expert` ; les deux lignes de `theorie` reçoivent chacune leur rôle propre :

- theorie · Évaluation audiométrique : « Audiométrie vocale : discrimination mots dans
  silence/bruit » → « Audiométrie vocale : **intelligibilité selon l'intensité** — mesure la
  compréhension et non la seule détection ; **discrimination effondrée au regard des seuils tonals
  = atteinte rétrocochléaire** ».
  source : SSP — § Cartes ECOS, neurinome — « la perte porte d'abord sur la **discrimination
  vocale**, disproportionnée par rapport à l'audiométrie tonale (le patient « entend mais ne
  comprend pas ») ».
- theorie · Examens complémentaires (queue) : « Audiométrie vocale : % discrimination selon
  intensité » → « Audiométrie vocale : **dans le silence et dans le bruit** (gêne réelle en
  conversation) », formulation reprise de la section notée m4 (« Audiométrie vocale dans le silence
  et le bruit »). Le « % discrimination selon intensité » supprimé ici est repris mot pour mot par
  la ligne ci-dessus : rien n'est perdu, les deux lignes cessent de se répéter.

*Suissification — niveau 1*

- theorie · Surdité professionnelle : « Maladie professionnelle indemnisable » → « Maladie
  professionnelle indemnisable : **annonce SUVA (assurance-accidents LAA)** ».
  source : SSP — § Skills connexes — « 🇨🇭 Filières & ressources : … **SUVA** (exposition
  professionnelle au bruit) ». Le patient a travaillé en aciérie avec protection auditive
  inconstante (section notée).

*Vocabulaire*

- theorie · Évaluation audiométrique : « **Otoacoustic emissions** » → « **Otoémissions
  acoustiques (OEA)** » et « Potentiels évoqués » → « Potentiels évoqués **auditifs (PEA)** »,
  sigles employés par la page SSP (« OEA / PEA »). Anglicisme résiduel dans un corpus francophone.
- theorie · Tests de Rinne et Weber : « - Neurosensoriel : latéralise côté sain » →
  « - Neurosensoriel **(= surdité de perception)** : latéralise côté sain ». La page SSP raisonne
  exclusivement en « transmission vs **perception** », la grille en « transmission vs
  **neurosensoriel** » (terme repris par la section notée, gelée) : l'équivalence est posée une
  fois, aucun terme n'est remplacé.

**Divergences consignées**

- theorie · Appareillage auditif : « Remboursement : **variable selon pays/assurance** » — la page
  SSP ne dit rien du remboursement des appareils auditifs. Niveau 3 : laissé inchangé, aucune règle
  suisse inventée. À arbitrer si le forfait AI/AVS doit être nommé.
- Les pièges éliminatoires « Manquer surdité brutale unilatérale » et « Manquer un cholestéatome »
  n'ont **aucune occurrence** dans la grille (recherche sur `strip_base64`) — vérifié, non ajoutés :
  la vignette est une perte **bilatérale, symétrique et progressive sur 5 ans**, sans otorrhée. Le
  piège applicable, l'IRM devant une asymétrie, est bien couvert (`expert` « Pas d'indication IRM
  (symétrique, progressif) » · `theorie`/queue « Si asymétrie > 15 dB : IRM IAC avec gadolinium »).

### AMBOSS-24 — Évaluation après chute, femme de 30 ans (page SSP : Capacité de Discernement & Éthique)

Grille de **violences conjugales** : la patiente déclare une chute dans les escaliers puis révèle,
si la question est posée directement, que son mari « la bouscule » une à deux fois par semaine.
Aucun contenu relatif à sa sécurité n'a été supprimé, même redondant entre blocs — le coût d'une
répétition y est très inférieur au coût d'une omission.

**Modifications**

*Contrat de rôle — les deux paires détectées*

- expert · Points clés : « Documentation photos + schéma corporel » → « **Proposer** la
  documentation des lésions **avec l'accord de la patiente** (utile si plainte ultérieure) ». La
  paire (0.78) opposait cet item à `theorie`/Rappels « Documentation : photos datées avec échelle,
  schéma corporel ». Plutôt que de supprimer un contenu de protection, les deux lignes sont
  différenciées : `expert` porte le **geste et le consentement**, `theorie` le **protocole
  technique**. Rien n'est retiré ; le résultat de station reste dans `expert`/Rôles (« Photos
  lésions : Documentées avec échelle ») et l'exigence de consentement dans `theorie`/Examens
  (« Photos lésions : médico-légal avec consentement »).
- expert · Points clés : « Cycle violence : tension → explosion → **lune de miel** » supprimé après
  **portage** du terme dans `theorie`/Violence conjugale : « Cycle violence : tension → explosion →
  réconciliation **(« lune de miel »)** → tension ». Le cycle est un contenu explicatif (pourquoi
  elle ne part pas), il appartient à `theorie` ; le synonyme est conservé.

*Sécurité — niveau 1, la page SSP tranche*

- expert · Points clés : « Confidentialité sauf danger enfants » → « Confidentialité **(secret
  médical, CP art. 321)** — mais enfants exposés en danger : **signalement APEA/KESB possible
  (CC art. 314c, CP art. 364)** ».
  source : SSP — § Secret professionnel — « **CP art. 364** : droit/devoir d'aviser l'autorité en
  cas de maltraitance d'enfant » ; « **CC art. 314c-314e** : signalement APEA/KESB pour mineur en
  danger ». Les articles cités sont ceux de la page SSP. La grille énonçait l'exception sans jamais
  nommer l'autorité ni le fondement légal ; `expert`/Pièges garde « Signalement sans consentement
  (adulte compétent) », qui reste exact (secret médical envers l'adulte capable).
- theorie · Approche clinique : « Évaluation sécurité immédiate (elle + enfants) » → même libellé
  **suivi des facteurs de gravité** : « arme au domicile (y compris arme de service), strangulation
  antérieure, menaces de mort, escalade en fréquence ou en intensité, grossesse, séparation en
  cours, alcool/drogues du conjoint ».
  Justification : la **section notée** fait chercher « Arme à feu à la maison », « Régularité des
  abus » et « Consommation alcool/drogues du conjoint » — le candidat pose donc les questions sans
  qu'aucun bloc ne lui dise **pourquoi** ni comment en tirer un niveau de risque, alors
  qu'`expert`/Rôles conclut « Évaluation sécurité : Risque modéré-élevé » sans critère. La page SSP
  impose de « vérifier la liberté du choix » sous « **partenaire violent** » (§ Red flags).
  La **strangulation** n'apparaissait nulle part dans la grille.
- theorie · Plan de sécurité : « Numéros urgence programmés téléphone » → « Numéros d'urgence
  programmés dans le téléphone : **117 (police), 144, 143** ».
  source : SSP — § Réseau éthique/juridique Suisse — « **143** Main Tendue · **144** urgences ·
  **117** » ; § Cas particuliers — « Maltraitance … **117 si danger imminent** ».
- theorie · Rappels thérapeutiques : « Ressources : ligne nationale, refuges, aide juridique » →
  « **Ressources suisses : centre LAVI (0848 800 244 / 0840 110 110)**, maison d'accueil pour
  femmes, consultation de médecine des violences, aide juridique ; **117 si danger imminent** ».
  source : SSP — § Secret professionnel — « Cas pratique fréquent : **violences conjugales /
  domestiques → LAVI**, médecin cantonal, **0840 110 110** (centre de consultation LAVI) » ;
  § Réseau — « **LAVI 0848 800 244 / 0840 110 110** violences conjugales ». La « ligne nationale »
  d'origine ne renvoyait à aucun numéro atteignable en Suisse — dans une station dont l'enjeu est
  d'orienter la patiente, c'était la ressource la plus utile de la grille et elle était vide.

*Précision de pratique*

- theorie · Manifestations : « Mortalité : homicide 1ère cause décès femmes enceintes » →
  « Mortalité : **la grossesse majore le risque** (l'homicide est la 1ère cause de décès des femmes
  enceintes **aux États-Unis**) ». La statistique est américaine (Horon & Cheng, MMWR/JAMA) ; en
  Europe les premières causes de mortalité maternelle sont médicales. Le fait est conservé, son
  périmètre est nommé.
- theorie · Violence conjugale : « Prévalence : 25-30% femmes subissent violence physique/sexuelle »
  → « … **au cours de leur vie** ». Sans cette précision, le chiffre se lit comme une prévalence
  annuelle ; il s'agit d'une prévalence vie entière (estimation OMS).
- theorie · Examens complémentaires : « Temps saignement : fonction plaquettaire globale » → « Temps
  **de** saignement : fonction plaquettaire globale — **test historique, remplacé en pratique par
  les tests d'occlusion plaquettaire (PFA)** ». Le test est abandonné des laboratoires suisses. La
  ligne n'est pas supprimée : la section notée m2 évalue « Temps de saignement, TP, TCA » et le
  barème est gelé — le bloc pédagogique explique donc le décalage au lieu de le contredire.

**Vérification des deux numérations converties en tâche 10c**

- theorie · PTI : « Traitement si plaquettes **< 30 G/L** ou saignements » et theorie · Rappels :
  « PTI aigu : corticoïdes si plaquettes **< 30 G/L** » — les deux seuils sont cohérents entre eux
  et avec le seuil thérapeutique usuel du PTI. Cohérents aussi avec leur voisinage : `expert`/Rôles
  donne « FSC : Plaquettes **180 G/L (normale)** » (norme 150-400 G/L) et la section notée
  « thrombocytopénie (plaquettes < 150 G/L) », « leucocytose (leucocytes > 10 G/L) ». Aucun
  qualificatif ne contredit sa valeur. **Lignes non modifiées.**

**Divergences consignées**

- Section notée m5, blocs `therapy-section` (hors zone pédagogique, barème gelé) : « **Services
  protection enfance** si besoin » et « Conseil juridique gratuit » — l'équivalent suisse est
  l'**APEA/KESB** et le **centre LAVI**, désormais nommés dans les blocs pédagogiques. Non corrigé
  (hors périmètre), consigné.
- La page SSP cite « **CP art. 364** » comme fondement du droit d'aviser ; la citation de la grille
  reprend celle de la page. Si cet article a été absorbé par les art. 314c-314d CC lors de la
  révision de 2019, c'est la page SSP qu'il faudrait mettre à jour, pas la grille : signalé.

### AMBOSS-25 — Douleur au genou, femme de 47 ans (page SSP : Douleur de Genou)

Vraie question de la station : une **TVP poplitée** derrière un traumatisme du genou.

**Modifications**

*Contradiction `expert` ↔ section notée — niveau 2, la section notée fait foi*

- expert · Rôles et interventions : « IRM genou : Œdème osseux, **LCL intact** » → « IRM genou :
  Œdème osseux, **déchirure du ligament collatéral latéral (LCL)** ».
  La section notée dit l'inverse en deux endroits : critère m3 (« IRM genou droit … **montrerait
  une rupture du ligament collatéral**, bien que ce ne soit pas typiquement requis pour le
  diagnostic ») et le bloc thérapeutique « **Si lésion LCL** : attelle articulée ou genouillère,
  AINS, physiothérapie ». Le bloc `annexe-dd` retient également « Déchirure du ligament collatéral
  latéral (LCL) » avec arguments POUR (sensibilité de la ligne articulaire latérale, mécanisme
  direct, limitation d'amplitude), tous présents à l'examen noté. L'expert délivrait donc un
  résultat qui rendait sans objet un traitement noté. Ni la page SSP ni rien d'autre ne tranche sur
  cette vignette : niveau 2, `expert` est aligné sur la section notée, barème intact.

*Contrat de rôle — `expert`/Points clés purgé de la théorie*

- expert · Points clés : « Triade Virchow : stase + lésion endothéliale + hypercoagulabilité »
  supprimé — `theorie`/Physiopathologie développe les trois facteurs **avec leurs exemples**
  (immobilisation/voyage/obésité, trauma/chirurgie/cathéters, cancer/grossesse/thrombophilie).
- expert · Points clés : « Écho-Doppler = gold standard diagnostic TVP » supprimé après **portage**
  dans `theorie`/Diagnostic TVP : « Écho-Doppler compression : **examen de référence actuel**,
  Se 95%, Sp 98% ». Le portage lève au passage une contradiction interne : `theorie` désignait la
  phlébographie comme « historique gold standard » sans jamais dire ce qui l'avait remplacée. La
  section notée porte « test de choix pour diagnostiquer une TVP ».
- expert · Points clés : « Anticoagulation immédiate si forte suspicion clinique » supprimé — le
  contenu est porté deux fois ailleurs : `theorie`/Rappels (« TVP proximale : anticoagulation
  immédiate même avant confirmation ») et `expert`/Pièges (« Retarder anticoagulation si forte
  suspicion »), qui est sa forme de conduite.

*Sécurité — niveau 1, la page SSP tranche*

- expert · Pièges : ajout de « Devant un genou chaud, gonflé et fébrile : conclure sans avoir
  écarté une **arthrite septique (ponction articulaire urgente)** ».
  source : SSP — Douleur de Genou — `pieges_eliminatoires` — « **Manquer arthrite septique
  (ponction)** » (piège éliminatoire n° 2) ; § Red flags — « Monoarthrite fébrile … → **Arthrite
  septique** · Ponction articulaire STAT » ; § En Bref — « Mono-arthrite chaude = exclure une
  arthrite septique **jusqu'à preuve du contraire** ».
  Vérifié avant ajout : ni « septique » ni « ponction » n'avaient **une seule occurrence** dans la
  grille (recherche sur `strip_base64`), alors que le bloc `annexe-dd` retient une « température
  subfébrile (37.8 °C) » et que la jambe est chaude et gonflée. Le piège est formulé
  conditionnellement : il n'affirme rien sur cette patiente.
- theorie · Examens complémentaires (queue) : ajout de « **Radiographie du genou : indication posée
  par les critères d'Ottawa** (âge ≥ 55 ans, sensibilité isolée de la rotule ou de la tête de la
  fibula, flexion impossible à 90°, appui impossible sur 4 pas) ».
  source : SSP — `pieges_eliminatoires` — « **Ne pas appliquer Ottawa Knee Rules** » (piège
  éliminatoire n° 1) ; § Règle d'or — « appliquer les **critères d'Ottawa pour le genou** pour la Rx
  post-trauma ». La radiographie est un sous-item noté (m3) qu'aucun bloc pédagogique ne justifiait ;
  la ligne enseigne la règle sans contredire l'indication retenue par la section notée.

*Erreur factuelle interne (correction directe, hors hiérarchie)*

- theorie · Examens complémentaires (queue) : « Radiographie thorax : **éliminer EP** si dyspnée » →
  « Radiographie thorax : **recherche d'un diagnostic alternatif** si dyspnée — **ne permet jamais
  d'exclure une EP** ». Une radiographie thoracique normale n'exclut pas une embolie pulmonaire ;
  telle quelle, la ligne pouvait faire renoncer à l'angio-CT. Aucune autre source de la grille ne
  porte cet énoncé : rien à arbitrer, un fait faux à corriger.

*Suissification*

- theorie · Traitement TVP : « AVK : **warfarine** INR cible 2-3 (moins utilisé) » → « AVK :
  **acénocoumarol (Sintrom®) ou phenprocoumone (Marcoumar®)**, INR cible 2-3 (moins utilisés) ».
  La warfarine (Coumadine®) n'est plus commercialisée en Suisse ; les deux AVK du marché suisse sont
  le Sintrom® et le Marcoumar®. Unique occurrence de « warfarine » dans les 40 grilles (recherche
  sur `strip_base64`). Même geste que « Vicodin → Tramal® » et « Tylenol → Dafalgan® » (tâche 2).

**Divergences consignées**

- `annexe-dd` (hors zone pédagogique) retient une « **température subfébrile (37.8 °C)** » alors que
  la section notée fait répondre « Fièvre/frissons [**Non**] ». Contradiction interne à la zone
  notée, hors périmètre : non corrigée, consignée.

### AMBOSS-26 — Céphalée, homme de 29 ans (page SSP : Céphalée)

Page SSP partagée avec AMBOSS-33, **non traitée ici** (tâche suivante).

**Modifications**

*Contradiction `expert` ↔ `theorie` — niveau 1, la page SSP tranche*

- expert · Points clés : « Triptans si **échec AINS** dans migraine sévère » → « Triptans si **crise
  sévère d'emblée ou** échec des AINS (ibuprofène déjà pris sans effet) ».
  `theorie`/Approche thérapeutique stratifiée disait l'inverse (« sévère → triptans **d'emblée** ») :
  les deux blocs donnaient deux règles de prescription différentes.
  source : SSP — § PRISE EN CHARGE, Migraine — « Crise **sévère ou échec d'AINS** : triptan
  (sumatriptan 50-100 mg PO ou 6 mg SC) ». La section notée va dans le même sens (« Traitement de
  crise sévère • Triptans »), et le patient a déjà pris de l'ibuprofène sans effet.

*Sécurité — niveau 1, la page SSP tranche*

- theorie · Rappels thérapeutiques : ajout de « **Triptans contre-indiqués si : coronaropathie, AVC,
  HTA non contrôlée, migraine hémiplégique ou basilaire** ».
  source : SSP — § PRISE EN CHARGE, Migraine — « triptan … — **CI** : coronaropathie, AVC, HTA non
  contrôlée, migraine hémiplégique / basilaire ». Aucune contre-indication n'était mentionnée dans
  la grille, alors qu'`expert` délivre « Si traitement : Sumatriptan 100 mg PO efficace » et que le
  patient fume **2 paquets/jour depuis l'âge de 15 ans** avec une mère victime d'AVC à 65 ans.
- theorie · Examens complémentaires (queue) : ajout, en tête de section, de « **Drapeaux rouges
  SNOOP4** à écarter avant de conclure à une céphalée primaire : Systémiques (fièvre, cancer,
  immunodépression) · Neurologiques · Onset en coup de tonnerre · Older (> 50 ans) · Pattern
  nouveau, Positionnelle, Papilledema (œdème papillaire), Progressive ».
  source : SSP — § Points Clés ECOS, À faire absolument n° 1 — « Rechercher **systématiquement** les
  red flags **SNOOP4** avant de conclure à une céphalée primaire » ; § Mnémoniques — la liste des
  huit lettres, reprise à l'identique. La grille disait « Pas d'imagerie sauf drapeaux rouges »
  (`expert`) sans que les drapeaux systémiques, positionnels et l'œdème papillaire figurent nulle
  part. Clés d'origine conservées, traduction en valeur (règle des glossaires).

*Précisions posologiques — niveau 1*

- theorie · Rappels : « Crise légère : **ibuprofène 600-800 mg** ou naproxène 500 mg » → « Crise
  légère : **paracétamol 1 g**, **ibuprofène 400-600 mg** ou naproxène 500 mg ».
  source : SSP — « Crise légère / modérée : **paracétamol 1 g** ou AINS (**ibuprofène 400-600 mg**,
  naproxène, aspirine 1 g) ». L'ibuprofène n'est d'ailleurs pas commercialisé en dosage 800 mg en
  Suisse.
- theorie · Rappels : « Prophylaxie 1ère ligne : propranolol 80-240 mg/j » → « Prophylaxie **si ≥ 3
  crises invalidantes/mois** — 1ère ligne : propranolol 80-240 mg/j ».
  source : SSP — « Prophylaxie (**≥ 3 crises invalidantes/mois**) : bêtabloquant … ».
  `expert`/Pièges reprochait « Ne pas évaluer fréquence pour prophylaxie » sans qu'aucun seuil ne
  soit donné : le piège devient vérifiable.

*Contrat de rôle et mnémo*

- expert · Points clés : « POUND : Pulsatile, One day, Unilateral, Nausea, Disabling » **déplacé**
  vers `theorie`/Critères diagnostiques IHS, avec traduction en valeur : « Mnémo POUND (en faveur
  d'une migraine) : Pulsatile · durée d'One day (4-72 h) · Unilatérale · Nausées · Disabling
  (invalidante) ». Un mnémo est un outil d'apprentissage — `expert` ne porte pas de liste
  d'apprentissage — et sa place naturelle est à côté des critères qu'il résume. Clés d'origine
  intactes, valeurs traduites (même règle que les glossaires de schéma). Libellé repris de la page
  SSP, § Mnémoniques.
- theorie · Migraine : coquille « Céphalée primaire **neurovaculaire** » → « **neurovasculaire** ».

**Divergences consignées**

- Section notée, bloc `therapy-section` : « **Prophylaxie si ≥ 4 crises/mois** » alors que la page
  SSP retient « **≥ 3 crises invalidantes/mois** ». Le bloc pédagogique est aligné sur la page SSP
  (niveau 1) ; la section notée est **gelée** et conserve son seuil. Écart consigné.
- Section notée : « AINS : Ibuprofène **600-800 mg** ou naproxène 500-**1000 mg** » — mêmes bornes
  hautes que celles corrigées dans le bloc pédagogique. Barème gelé, non corrigé.

### AMBOSS-27 — Fatigue, femme de 28 ans (page SSP : Fatigue)

Syndrome de Sheehan six mois après une hémorragie du post-partum.

**Modifications**

*Contrat de rôle — `expert`/Points clés purgé de la théorie (les 3 paires détectées)*

- expert · Points clés : « Triade classique : agalactie + aménorrhée + hypothyroïdie » supprimé —
  `theorie`/Diagnostic porte « Clinique : triade agalactie + aménorrhée + hypothyroïdie » et
  `theorie`/Manifestations en détaille chaque terme (déficit prolactine → agalactie, déficit
  gonadotrophines → aménorrhée, déficit TSH → hypothyroïdie secondaire).
- expert · Points clés : « Déficits multiples : ACTH, TSH, FSH/LH, GH, prolactine » supprimé —
  `theorie`/Physiopathologie porte la même liste (« Hypophyse antérieure : ACTH, TSH, FSH/LH, GH,
  prolactine »). Le message de conduite reste dans `expert`/Pièges (« Ne pas rechercher déficits
  hormonaux multiples »).
- expert · Points clés : « IRM : hypophyse 'vide' ou atrophique » supprimé — le **résultat de
  station** est dans `expert`/Rôles (« IRM hypophyse : hypophyse atrophique, tige fine ») et le
  **critère diagnostique** dans `theorie`. L'item répétait le résultat dans son propre bloc.
- theorie · Diagnostic : « IRM hypophysaire : hypophyse 'vide', atrophie, tige fine » → « IRM
  hypophysaire : **hypophyse augmentée et non rehaussée en phase aiguë, puis** selle turcique
  'vide' par atrophie (tige fine), **post-hypophyse conservée** ». La ligne cesse de recopier le
  résultat de l'expert et porte l'évolution dans le temps, seule information que le résultat ne
  donne pas.

*Erreur factuelle interne (correction directe, hors hiérarchie)*

- theorie · Syndrome de Sheehan : « Déficits hormonaux : ACTH > TSH > FSH/LH > GH > prolactine » →
  « Déficits hormonaux, **du plus grave au moins grave** : ACTH > TSH > FSH/LH > GH > prolactine
  (**l'ordre d'apparition est inverse : GH et prolactine touchées les premières**) ». Lue comme une
  chronologie, la ligne contredisait `theorie`/Physiopathologie deux sections plus loin
  (« Hiérarchie déficits : **GH et prolactine premiers touchés** », « ACTH et TSH : déficits **plus
  tardifs mais plus graves** »). Le sens de la flèche est explicité, la contradiction interne levée,
  aucune donnée retirée.
- theorie · Rappels thérapeutiques : « Œstrogènes : **si désir grossesse**, sinon symptomatique » →
  « Œstroprogestatifs : **substitution jusqu'à l'âge de la ménopause** (symptômes, capital osseux) ;
  **si désir de grossesse, induction de l'ovulation par gonadotrophines** ». L'énoncé d'origine
  inversait l'indication : la substitution œstroprogestative traite l'hypogonadisme (symptômes,
  ostéoporose) et n'induit pas l'ovulation ; un désir de grossesse relève des gonadotrophines.

*Sécurité — niveau 1, la page SSP tranche*

- theorie · Examens complémentaires (queue) : ajout de « **Bilan minimal de toute fatigue : FSC,
  ferritine, TSH, glycémie, CRP/VS** (ici anémie microcytaire → compléter par un bilan martial) ».
  source : SSP — Fatigue — `pieges_eliminatoires` — « **Ne pas faire bilan minimal (Hb, TSH,
  ferritine, glycémie, CRP, VS)** » ; § Mnémoniques — « **Bilan minimal** : Hb, TSH, ferritine,
  glycémie, CRP/VS ». La section de queue de cette grille ne listait que des dosages hypophysaires,
  alors que la station elle-même délivre une **FSC avec Hb 85 g/L** et que la section notée évalue
  « Fer sérique, ferritine, TIBC ».

**Divergences consignées**

- Section notée, bloc `therapy-section` : « Traitement œstro-progestatif **si désir fertilité** » —
  même inversion que celle corrigée dans `theorie`/Rappels. Barème gelé : non corrigé, consigné.
- theorie · Anémie ferriprive : « Traitement : fer per os 100-200 mg/j élémentaire » pour une Hb à
  **85 g/L** du post-partum. Le fer intraveineux se discute à ce niveau d'anémie, mais la page SSP
  reste générique (« Traitement de la cause identifiée ») et la section notée prescrit « Fer per
  os … **Fer : IV si intolérance digestive** » : bloc pédagogique et section notée concordent,
  niveau 3, laissé inchangé.

**Vérifications (tâche 14)**

- `check_invariants.py` → `OK — 40 grilles, tous les invariants preserves` (code 0). `blocks` reste
  `["expert", "theorie"]` sur les cinq grilles ; `maxScores`, `scoreSpans`, `criteriaCount`,
  `detailCount`, `radioCount`, `checkboxCount` inchangés : **barème gelé**.
- `check_nomenclature.py` → `OK — aucun terme non suisse detecte` (code 0). Aucune valeur introduite
  en `g/dL`, `ng/mL`, `pg/mL`, `/mm³`, en livres ni en unité implicite.
- `report_redundancy.py` par grille : **9 paires → 0** (23 : 4→0 · 24 : 2→0 · 25 : 0→0 · 26 : 0→0 ·
  27 : 3→0).
- `check_no_loss.py dfe2e4f` par grille : 6 + 6 + 6 + 2 + 4 = **24 items signalés**, tous relus un à
  un — 13 reformulations enrichies (l'item reste, réécrit), 6 suppressions dont le contenu est porté
  à l'identique ou en plus précis par un autre bloc, 3 portages explicites documentés ci-dessus,
  1 déplacement (mnémo POUND), 1 correction intentionnelle (œstrogènes). **Aucune perte réelle.**
- `git diff --numstat` : 5 fichiers, **35 insertions / 40 suppressions**, toutes dans la zone
  pédagogique (contrôlé ligne à ligne contre `peda_bounds`). Aucun `.criteria-text` touché, aucun
  crochet de réponse patient touché, aucun sous-item noté ajouté ni retiré, aucun item ICE touché.

### AMBOSS-29 — Fatigue, femme de 18 ans (page SSP : Fatigue)

Mononucléose infectieuse (EBV) sur suspicion d'anémie ferriprive par ménorragies. Deux blocs
pédagogiques seulement (`expert`, `theorie`) : axes 1 à 6 sans objet, seul opère le contrat de rôle.
Redondance : 5 paires → 0.

**Modifications**

*Contrat de rôle — `expert`/Points clés purgé de la théorie (2 des 5 paires)*

- expert · Points clés : « Lymphocytes atypiques > 10% = pathognomonique » supprimé après **portage**
  du seuil dans `theorie`/Diagnostic (voir la correction factuelle ci-dessous). Le portage précède
  la suppression.
- expert · Points clés : « Éviter amoxicilline : éruption dans 90% cas EBV » supprimé —
  `theorie`/Rappels porte « ÉVITER amoxicilline : éruption 90% cas », `theorie`/Présentation clinique
  « Éruption : 5-10% spontané, 90% si amoxicilline », et le message de conduite reste dans
  `expert`/Pièges (« Prescrire amoxicilline pour 'pharyngite' »). Aucune perte.

*Erreur factuelle interne (correction directe, hors hiérarchie)*

- theorie · Diagnostic : « Lymphocytes atypiques = cellules Downey pathognomoniques » →
  « Lymphocytes atypiques (cellules de Downey) > 10% : **caractéristiques du syndrome
  mononucléosique, évocateurs d'EBV mais non spécifiques (CMV, primo-infection VIH,
  toxoplasmose)** ». « Pathognomonique » était faux dans l'absolu et contredisait le propre
  `annexe-dd` de la grille, qui retient la primo-infection VIH et le CMV avec l'argument
  « syndrome mononucléosique ». La patiente a 2 partenaires sur l'année : conclure à l'EBV sur les
  lymphocytes atypiques ferait manquer une primo-infection VIH.

*Contrat de rôle — le résultat à `expert`, le seuil et le pourquoi à `theorie` (3 paires restantes)*

- theorie · Diagnostic : « FSC : lymphocytose > 50%, > 10% lymphocytes atypiques » → « FSC :
  **seuils d'interprétation** — lymphocytose relative > 50%, lymphocytes atypiques > 10% ; **y
  chercher aussi une anémie microcytaire (ménorragies)** ». La ligne cesse de doubler le résultat de
  station (`expert` « FSC : lymphocytose 60%, 15% lymphocytes atypiques ») et reprend ce que le
  critère noté m2 dit de la FSC (« pour évaluer l'anémie microcytaire hypochrome »).
- theorie · Présentation clinique : « Adénopathies : cervicales postérieures +++ (90%) » → ajout de
  « — la topographie **postérieure** oriente vers l'EBV, à l'inverse des adénopathies antérieures de
  l'angine à streptocoque ». La ligne cesse de répéter le résultat d'examen de `expert`.
- theorie · Examens complémentaires (queue) : « Transaminases : ASAT/ALAT souvent élevées » →
  « Transaminases : **recherche d'une hépatite EBV, anictérique dans la plupart des cas — et
  dépistage d'une hépatite virale devant toute fatigue** ». L'élévation reste portée par
  `theorie`/Diagnostic (« élévation modérée 80% cas ») : rien n'est perdu.

*Sécurité — niveau 1, la page SSP tranche*

- theorie · Examens complémentaires (queue) : ajout de « **β-hCG : systématique chez toute femme en
  âge de procréer** ». Aucune occurrence de β-hCG ni de test de grossesse dans la grille entière
  (recherche sur `strip_base64`) : la seule mention de grossesse est l'item d'anamnèse
  « Grossesses [Non] », qui est une gestité, pas un test.
  source : SSP — Fatigue — § Pièges — « Oublier la **grossesse** chez femme jeune (**βHCG
  systématique**) » ; § Examens complémentaires, légende — « FSC, VS, TSH, transaminases, ferritine
  et **test de grossesse** en bilan de base ». La patiente a 18 ans et déclare une activité sexuelle
  avec deux partenaires sur l'année (critère noté a11).
- theorie · Examens complémentaires (queue) : « TSH : si fatigue persistante > 3 mois » → « **Bilan
  minimal de toute fatigue, sans attendre : FSC, ferritine, TSH, glycémie, CRP/VS** (ici ATCD
  thyroïdien maternel) ». Différer la TSH de trois mois contredisait à la fois la page SSP et le
  critère noté m3, qui fait doser « TSH, T3 libre, T4 libre » sans condition de durée.
  source : SSP — Fatigue — `pieges_eliminatoires` — « **Ne pas faire bilan minimal (Hb, TSH,
  ferritine, glycémie, CRP, VS)** » ; § Règle d'or — « Bilan minimal incontournable : FSC, TSH,
  ferritine, glycémie, CRP/VS ». Même geste qu'en AMBOSS-27 (tâche 14), grille sœur de la même page.

**Divergences consignées**

- expert · Rôles : « Transaminases : **ASAT 85, ALAT 95** » — valeurs en unité implicite (U/L).
  Hors du champ de la passe d'unités, qui a porté sur l'hémogramme (PROCEDURE.md § 6, « angle mort
  assumé ») : non modifié, signalé pour une passe d'unités ultérieure.
- Section notée, bloc `therapy-section` « Si anémie ferriprive confirmée » : l'item « **Durée** » est
  orphelin, sans valeur après le mot. Barème gelé : non corrigé, consigné.
- La grille ne délivre **aucun résultat d'hémogramme rouge ni de bilan martial** : `expert`/Rôles
  donne la seule ligne lymphocytaire de la FSC, alors que le critère noté m2 fait demander la FSC
  « pour évaluer l'anémie microcytaire hypochrome », que m3 fait doser « fer sérique, ferritine,
  transferrine, TIBC », qu'un bloc thérapeutique entier traite l'anémie ferriprive et que
  `expert`/Pièges avertit de « négliger l'anémie ferriprive (ménorragies) ». La branche martiale de
  la station n'a donc aucun résultat à délivrer. Corriger imposerait d'**inventer** une hémoglobine
  et une ferritine chez cette patiente : niveau 3, laissé inchangé, consigné pour arbitrage.

### AMBOSS-32 — Lésion génitale, femme de 17 ans (page SSP : Leucorrhées)

Co-infection VPH (condylomes) + Chlamydia + gonocoque chez une mineure. Deux blocs pédagogiques.
Redondance : 0 paire avant et après — **aucune suppression n'a été faite sur cette grille**, en
application de la consigne de tâche : le coût d'une répétition sur un contenu de protection de la
patiente est très inférieur au coût d'une omission. `expert`/Points clés conserve donc ses six items,
y compris ceux qui recoupent `theorie` (préservatifs sans latex, vaccination VPH post-exposition,
confidentialité de la mineure).

**Modifications**

*Prise en charge — niveau 1, la page SSP tranche explicitement*

- theorie · Rappels : « Chlamydia : **azithromycine 1g dose unique (1ère ligne)** » / « Alternative :
  doxycycline 100 mg × 2/j × 7j » → « Chlamydia : **doxycycline 100 mg × 2/j × 7j (1ère ligne)** » /
  « Alternative : **azithromycine 1 g PO dose unique** (grossesse, doute sur l'observance —
  doxycycline CI aux T2-T3) ». Les deux molécules restent, leur rang s'inverse.
  source : SSP — Leucorrhées — § Cervicite (Chlamydia / Gonocoque) — « **Doxycycline 100 mg × 2/j
  × 7 j (Chlamydia 1ʳᵉ ligne)** … OU **azithromycine 1 g PO (alternative)** » ; § Mnémoniques —
  « Cervicite = IST : **doxycycline** + ceftriaxone + traitement partenaire + abstinence 7 j +
  déclaration OFSP » ; § Grossesse — « Doxycycline CI au T2-T3 → amoxicilline ou azithromycine ».
- theorie · Rappels : « Gonorrhée : ceftriaxone 500 mg IM **+ azithromycine 1g** » → « Gonorrhée :
  **ceftriaxone 500 mg-1 g IM dose unique, associée au traitement anti-chlamydia en cas de
  co-infection** ». Les deux tests sont positifs chez cette patiente.
  source : SSP — Leucorrhées — « **Ceftriaxone 500 mg-1 g IM dose unique** si gonocoque ».
- theorie · Rappels : « Test de contrôle : 3-4 semaines après traitement » → « **Test de guérison :
  PCR à 4-6 semaines si grossesse, persistance des symptômes ou doute sur l'observance** ».
  source : SSP — Leucorrhées — « **Test de guérison : PCR à 4-6 sem** si grossesse, persistance,
  doute observance ».
- theorie · Rappels : « Abstinence : 7 jours après traitement **monodose** » → « **Abstinence
  sexuelle : 7 jours après la fin du traitement** ». La restriction à la monodose laissait sans
  consigne le traitement de 7 jours devenu première ligne.
  source : SSP — Leucorrhées — « **Abstinence sexuelle 7 j** ».

*Suissification — niveau 1*

- theorie · Rappels : ajout de « **Déclaration obligatoire à l'OFSP : chlamydia, gonocoque,
  syphilis** ». La grille ne portait ce point que dans la section notée, sous la forme générique
  « Déclaration obligatoire ».
  source : SSP — Leucorrhées — § Points Clés ECOS — « Cervicite = IST → traiter le/les partenaire(s)
  + dépister les autres IST + **déclaration OFSP (gonocoque, chlamydia, syphilis)** ».
- theorie · Rappels : « Notification partenaires : 60 jours précédents » → ajout de « — notification
  anonyme possible par les **centres de santé sexuelle (Profa, Santé Sexuelle Suisse)** ».
  `expert`/Points clés annonçait « notification anonyme possible » sans nommer de canal.
  source : SSP — Leucorrhées — § Skills connexes — « **Notification anonyme partenaires** : centres
  de santé sexuelle (**Profa, Santé Sexuelle Suisse**) ».

*Sécurité — protection de la patiente mineure, niveau 1*

- theorie · Confidentialité médicale chez mineurs : ajout de « **Fondement en Suisse : la mineure
  capable de discernement (art. 16 CC) consent seule et sa confidentialité s'impose, y compris
  vis-à-vis des représentants légaux** ». La grille affirmait « Informer les parents sans consentement
  (illégal) » sans jamais nommer le critère qui fonde la règle, alors que c'est lui que la patiente
  oppose au défi de la station.
- theorie · Confidentialité médicale chez mineurs : ajout de « **Dépister une relation non consentie
  ou sous contrainte (partenaire en position d'autorité ou de dépendance, sexualité tarifée) — si
  suspicion d'abus sexuel : LAVI 0848 800 244, CURML, signalement adapté ; 147 Pro Juventute pour la
  patiente** ». Aucun dépistage d'abus ne figurait dans la grille : la maltraitance n'y apparaissait
  que comme une **limite** à la confidentialité, jamais comme quelque chose à rechercher. La patiente
  a 17 ans, déclare 8 partenaires sur l'année, « souvent des aventures d'un soir », et aucune
  protection barrière.
  source : SSP — Leucorrhées — § Red flags — « Suspicion d'**abus sexuel** → **LAVI**, **CURML**,
  signalement adapté » ; § En Bref — « **LAVI 0848 800 244** (violences sexuelles) » ; § Skills
  connexes — « **147 Pro Juventute** (ado) ».
- theorie · Confidentialité médicale chez mineurs : « Limites : danger imminent, maltraitance,
  **incapacité** » → « … **incapacité de discernement** », terme du droit suisse.
- theorie · Examens complémentaires (queue) : « Test VIH 4e génération : dépistage systématique si
  IST » → ajout de « — **un test négatif n'exclut pas une exposition récente, à refaire à 6 semaines
  (fenêtre sérologique)** ». `expert`/Rôles délivre « Test VIH : négatif (avec consentement) » à une
  patiente à exposition répétée non protégée : sans cette réserve, le résultat se lit comme une
  exclusion. Interprétation d'examen — rôle propre de la section.

**Divergences consignées**

- Section notée, bloc `therapy-section` : « **Azithromycine 1 g dose unique PO** / Ou doxycycline »
  et « Ceftriaxone 500 mg IM **PLUS azithromycine 1 g PO** » — le bloc pédagogique est désormais
  aligné sur la page SSP (niveau 1), la section notée reste gelée et diverge sur le rang des deux
  molécules et sur la bithérapie de la gonococcie. De même « Test de guérison à 3-4 semaines ».
- Aucune mention de la **PrEP** dans la grille, alors que la patiente cumule 8 partenaires sur
  l'année et l'absence de protection barrière. Ni la page SSP ni la section notée n'abordent la PrEP :
  niveau 3, rien inventé, signalé pour arbitrage.

### AMBOSS-33 — Céphalée, femme de 55 ans (page SSP : Céphalée)

Hémorragie sous-arachnoïdienne sur rupture d'anévrisme de la communicante antérieure, avec fièvre à
38.7 °C, Kernig et Brudzinski positifs et sinusite récente — méningite bactérienne co-suspectée.
Deux blocs pédagogiques. Redondance : 0 paire avant et après.

**Modifications**

*Contrat de rôle — `expert`/Points clés purgé de la théorie*

- expert · Points clés : « Nimodipine systématique si HSA (prévention vasospasme) » supprimé — porté
  trois fois ailleurs et en plus précis : `theorie`/Prise en charge (« Nimodipine : 60 mg × 6/j PO
  × 21j »), `theorie`/Rappels (« nimodipine 60 mg × 6/j PO × 21 jours systématique ») et le message
  de conduite dans `expert`/Pièges (« Oublier prévention vasospasme (nimodipine) »).
- expert · Points clés : « Mortalité HSA : 50% (25% avant hôpital) » supprimé — `theorie`/HSA porte
  la même donnée ventilée (« Mortalité : 50% (25% pré-hospitalier, **25% hospitalier**) »).

*Erreur factuelle interne et alignement — niveau 1, la page SSP tranche*

- theorie · Présentation clinique : « 'Pire céphalée de ma vie' : **pathognomonique** » → « 'Pire
  céphalée de ma vie', **maximale en moins d'une minute : HSA jusqu'à preuve du contraire, même si
  l'examen neurologique est strictement normal** ». « Pathognomonique » était faux — le coup de
  tonnerre est un drapeau rouge, non une certitude — et contredisait `expert`/Points clés, qui écrit
  correctement « = HSA **jusqu'à preuve contraire** ».
  source : SSP — Céphalée — § Cartes ECOS — « « la pire céphalée de ma vie », maximale d'emblée
  (< 1 min) = **HSA jusqu'à preuve du contraire, même si l'examen neuro est strictement normal** ».
- theorie · Examens complémentaires (queue) : « Si CT négatif **< 6h : angio-CT ou angio-IRM** » et
  « Si CT négatif > 6h : PL » → « Si CT négatif **et clinique évocatrice : PL (xanthochromie,
  spectrophotométrie), idéalement ≥ 12h après le début — la sensibilité du CT chute après 6-12h, un
  CT normal n'élimine pas l'HSA** » et « **Angio-CT ou angio-IRM une fois l'HSA confirmée**, puis
  angiographie 4 vaisseaux : localisation de l'anévrisme ». L'algorithme d'origine faisait de
  l'angio-CT l'étape suivant un CT négatif, alors que l'examen qui exclut l'HSA est la PL et que
  l'angio sert à localiser l'anévrisme **après** confirmation.
  source : SSP — Céphalée — § HSA — « **CT cérébral natif en urgence** (Se > 95 % si réalisé < 6 h) ;
  **si CT négatif et clinique évocatrice → PL** avec recherche de xanthochromie (**idéalement
  ≥ 12 h**) ; **angio-CT / angio-IRM si HSA confirmée** » ; § Cartes ECOS — « la sensibilité du CT
  chute (< 90 %) après 6-12h → un CT normal à H24 **N'ÉLIMINE PAS l'HSA : la PL reste obligatoire** » ;
  `pieges_eliminatoires` — « **Manquer HSA (CT puis PL si CT-)** ».
- theorie · Diagnostic HSA : « PL si CT négatif + forte suspicion : xanthochromie » → « … : **la
  xanthochromie (bilirubine) distingue l'HSA d'une PL traumatique** ». Rend interprétable le
  résultat que `expert` délivre (« PL (si faite) : GR 50 000, xanthochromie présente »), **sans
  toucher à cette ligne**.
  source : SSP — Céphalée — § Cartes ECOS — « La **xanthochromie (bilirubine) distingue l'HSA d'une
  PL traumatique** ».

*Sécurité — niveau 1, la page SSP tranche*

- theorie · Méningite bactérienne : « Traitement : ATB empirique urgente < 1h » → « … — **ne jamais
  la retarder pour le CT ou la PL : hémocultures, puis antibiotiques et dexaméthasone immédiatement,
  imagerie et PL ensuite** ». La grille poussait le candidat vers « CT IMMÉDIAT » puis PL après CT
  (`expert`/Pièges « Faire PL avant CT (risque engagement si HTIC) ») sans jamais dire que
  l'antibiothérapie ne s'ordonne pas dans cette file d'attente — chez une patiente à 38.7 °C avec
  méningisme, c'est l'erreur de séquence létale.
  source : SSP — Céphalée — § Red flags — « Fièvre + raideur de nuque (méningisme) → Méningite
  bactérienne · **Antibiothérapie empirique IV immédiate** » ; § Méningite bactérienne — « Purpura
  fulminans → ceftriaxone 2 g IV/IM en préhospitalier **sans délai** » ; « dexaméthasone **avant ou
  avec la 1ʳᵉ dose d'antibiotiques** ».
- theorie · Examens complémentaires (queue) : ajout de « **Hémocultures × 2 avant toute
  antibiothérapie si fièvre ou suspicion de méningite (ici T° 38.7 °C)** ». La section de queue,
  qui liste les examens à demander, n'en portait aucune ; les hémocultures ne figuraient que dans le
  critère noté m3.
  source : SSP — Céphalée — § Examens — « **Hémocultures × 2**, lactate, procalcitonine si suspicion
  de **méningite** / sepsis ».

**Points protégés — vérifiés intacts**

- `expert`/Rôles « PL (si faite) : **GR 50 000**, xanthochromie présente » : **non modifié**. Compte
  d'érythrocytes dans le LCR, rendu par µL, jamais en G/L (PROCEDURE.md § 6).
- Légende du schéma « Prise en charge de la méningite » : les clés `BMP :` et `CBC :` sont
  **conservées** telles quelles, l'image n'étant pas modifiée. `expert`/Rôles « FSC : GB 15 G/L »
  reste tel que corrigé en tâche 7.

**Divergences consignées**

- expert · Rôles : « Ionogramme : **Na 135**, glucose 7.2 mmol/L » — sodium en unité implicite
  (mmol/L). Signalé pour une passe d'unités ultérieure, non modifié.
- theorie · Prise en charge HSA et `theorie`/Rappels se recouvrent sur trois lignes (contrôle
  tensionnel, nimodipine, analgésie). Recouvrement **interne** à `theorie`, que
  `report_redundancy.py` ne mesure pas (il compare des blocs entre eux) et qu'aucun axe ne
  prescrit de traiter. Non restructuré, signalé.
- theorie · Rappels : « Anti-épileptique prophylactique : lévétiracétam » et `theorie`/PEC
  « **Triple-H** si vasospasme » sont présentés comme des standards, alors que la prophylaxie
  systématique et le triple-H ont l'un et l'autre reculé au profit d'une hypertension induite en
  euvolémie. Ni la page SSP ni la section notée ne tranchent (la section notée écrit elle aussi
  « triple-H thérapie ») : niveau 3, laissé inchangé.

### AMBOSS-36 — Fatigue, homme de 54 ans (page SSP : Fatigue)

Hépatite C aiguë sur hépatopathie alcoolique chez un usager de drogues intraveineuses. Deux blocs
pédagogiques. Redondance : 0 paire avant et après. **Alignement distinct de celui d'AMBOSS-29** :
même page SSP, tableaux sans recouvrement (femme de 18 ans / homme de 54 ans), aucune transposition.

**Modifications**

*Contrat de rôle — `expert`/Points clés purgé de la théorie*

- expert · Points clés : « **Window period : 4-10 semaines pour séroconversion** » supprimé après
  **portage** dans `theorie`/Examens complémentaires (queue), dont la ligne de sérologies devient
  « Sérologies virales : HBsAg, anti-HBc, anti-HCV, ARN-VHC — **l'anti-VHC reste négatif pendant la
  fenêtre sérologique de 4-10 semaines : en phase aiguë, c'est l'ARN-VHC qui fait le diagnostic** ».
  Le portage précède la suppression. La donnée était absente de `theorie`, qui ne portait que
  l'incubation (2-12 semaines) : sans elle, un anti-VHC négatif se lit comme une exclusion alors que
  le diagnostic retenu est une hépatite C **aiguë**.
- expert · Points clés : « Hépatite C aiguë : 75% asymptomatique, **25% ictère** » supprimé —
  `theorie`/Hépatite C aiguë porte « Incidence : 75% asymptomatique, **25% symptomatique** » et
  « ictère dans **20-30%** ». L'item supprimé confondait symptomatique et ictérique : c'est la
  version fausse qui disparaît, les deux exactes restent.
- expert · Points clés : « Alcool + virus = synergie pour progression cirrhose » supprimé — une
  **section entière** de `theorie` (« Co-infection VHC/alcool ») développe la synergie (progression
  × 3, CHC × 100, réponse antivirale diminuée, décompensation plus rapide).

*Sécurité — erreur factuelle interne (correction directe, hors hiérarchie)*

- theorie · Rappels : « Prophylaxie sevrage : **diazépam** selon score CIWA » → « Prophylaxie
  sevrage : **benzodiazépine** selon score CIWA — **en cas d'hépatopathie, préférer l'oxazépam ou le
  lorazépam (glucuronoconjugaison directe), le diazépam s'accumulant et pouvant précipiter une
  encéphalopathie** ». Le patient a une hépatite alcoolique avec risque de cirrhose ; le diazépam,
  à métabolisme oxydatif hépatique et à demi-vie longue, s'accumule et peut déclencher une
  encéphalopathie. La section notée reste générique (« benzodiazépines, thiamine ») : elle ne
  contredisait pas la ligne, il n'y avait donc rien à arbitrer, seulement un fait à corriger.

*Erreur factuelle interne — formule inutilisable en unités suisses*

- theorie · Hépatite alcoolique : « Score Maddrey : (4.6 × (**TP** patient - **TP** témoin)) + **bili
  totale** » → « Score de Maddrey : 4.6 × (**temps de prothrombine** du patient - témoin, **en
  secondes**) + bilirubine totale **÷ 17.1 (bilirubine en µmol/L)** ». Deux défauts : « TP » se lit
  en Suisse comme le *taux* de prothrombine en pourcentage alors que la formule prend un *temps* en
  secondes ; et la bilirubine, rendue en µmol/L par les laboratoires suisses, doit être convertie
  avant d'entrer dans la formule — sans le facteur, le score calculé est faux d'un ordre de grandeur
  et l'indication des corticoïdes (seuil ≥ 32) avec lui. Le facteur est écrit en division par 17.1
  plutôt qu'en nommant l'unité anglo-saxonne, bannie par `check_nomenclature.py`.

**Divergences consignées**

- theorie · Hépatite alcoolique : « ASAT/ALAT > 2, **ASAT < 300** » — valeur en unité implicite
  (U/L). Signalé pour une passe d'unités ultérieure, non modifié.
- theorie · Rappels : « Alternative : **pentoxifylline** 400 mg × 3/j si CI stéroïdes » — molécule
  dont le bénéfice n'a pas été confirmé dans l'hépatite alcoolique sévère. Ni la page SSP ni la
  section notée ne tranchent : niveau 3, laissé inchangé.
- Aucune mention de la **naloxone à emporter** ni de la vaccination **hépatite A** dans la prise en
  charge de réduction des risques d'un usager de drogues intraveineuses, alors que la surdose est
  la première cause de décès de cette population. Ni la page SSP (Fatigue) ni la section notée
  n'abordent le sujet : niveau 3, rien inventé, signalé pour arbitrage.
- Section notée, blocs `therapy-section` : trois artefacts d'import subsistent — « signes vitau**xx** »,
  « Pas d'antiviraux sauf forme sévère**x sauf forme sévère** », « antiviraux action directe**x
  guérison 95% avec antiviraux action directe** ». Barème gelé : non corrigés, consignés.

### AMBOSS-40 — Vertiges, homme de 25 ans (page SSP : Vertiges)

Zona auriculaire (syndrome de Ramsay Hunt). Deux blocs pédagogiques. Redondance : 1 paire → 0.

**Modifications**

*Contrat de rôle — `expert`/Points clés purgé de la théorie (la paire détectée)*

- expert · Points clés : « VZV réactivation ganglion géniculé » supprimé — `theorie` porte la même
  donnée deux fois, en tête de section (« Réactivation du VZV dans le ganglion géniculé (VII) ») et
  en item (« Pathogénie : réactivation VZV ganglion géniculé »). Aucune perte.

*Sécurité — niveau 1, la page SSP tranche ; drapeau rouge entièrement absent*

- theorie · Névrite vestibulaire : ajout de « **HINTS devant tout syndrome vestibulaire aigu : head
  impulse NORMAL, nystagmus changeant de sens ou skew deviation = AVC du tronc ou du cervelet
  jusqu'à preuve du contraire — c'est le head impulse pathologique qui rassure. Toujours tester la
  marche : impossible = central** ». Ni « HINTS », ni « skew », ni « AVC », ni « cérébelleux » n'avaient
  **une seule occurrence** dans la grille entière (recherche sur `strip_base64`) : une station de
  vertige aigu ne portait aucune trace de l'urgence qu'elle doit d'abord exclure. `expert` délivre
  pourtant un « Head thrust test : positif côté droit » sans que rien n'explique ce que ce résultat
  écarte — ni ce qu'un résultat normal aurait imposé.
  source : SSP — Vertiges — § Règle d'or — « Devant un **syndrome vestibulaire aigu continu**, c'est
  l'examen **HINTS+** (et non l'IRM précoce) qui exclut le mieux un **AVC du tronc / cervelet**. Un
  **AVC cérébelleux peut mimer une névrite vestibulaire isolée** → toujours réaliser HINTS+ et tester
  la marche » ; § Pièges — « **Head Impulse NORMAL en aigu = PLUS inquiétant (AVC postérieur), pas
  rassurant** » ; `pieges_eliminatoires` — « **Manquer AVC fosse postérieure · HINTS mal réalisé** ».
- theorie · Névrite vestibulaire : « Nystagmus : horizontal, unidirectionnel » → « … , **inhibé par
  la fixation — vertical, multidirectionnel ou non inhibé = central** ».
  source : SSP — Vertiges — § Orientation Périphérique vs Central — « Nystagmus | Horizontal ou
  rotatoire, unidirectionnel, **inhibé par la fixation** | **Multidirectionnel, vertical, non
  inhibé** ».

*Prise en charge — niveau 1, la page SSP tranche*

- theorie · Rappels : « Antivertigineux : méclizine 25 mg × 3/j **PRN** » → « … , **cure courte
  < 3 jours — au-delà ils freinent la compensation centrale** ». Le « PRN » ouvrait une prescription
  sans borne de durée, alors que `theorie` explique par ailleurs que la récupération passe par la
  « compensation centrale 6-12 semaines ».
  source : SSP — Vertiges — § Névrite vestibulaire — « Antivertigineux symptomatiques **courts
  (< 3 j, pour ne pas freiner la compensation centrale)** ».

**Divergences consignées**

- expert · Points clés « Paralysie faciale dans **60%** cas » face à `theorie`/Ramsay Hunt « **Triade** :
  vésicules auriculaires + **paralysie faciale** + otalgie », qui fait de la paralysie faciale un
  élément définitionnel, et « Extension possible : **VIII (60%)** ». La section notée tranche dans le
  sens de `expert` (signe d'alarme n° 1 : « Paralysie faciale — Zona = **risque 60%** → corticoïdes
  urgents ») : niveau 2, `expert` conservé, tension `theorie` consignée sans être corrigée faute de
  source qui départage la définition du syndrome de son risque évolutif.
- theorie · Rappels emploie « méclizine », la page SSP « méclozine » et la section notée
  « Méclizine ». Variante orthographique, non harmonisée pour ne pas s'écarter de la section notée
  gelée.

**Vérifications (tâche 15)**

- `check_invariants.py` → `OK — 40 grilles, tous les invariants preserves` (code 0). `blocks` reste
  `["expert", "theorie"]` sur les cinq grilles ; `maxScores`, `scoreSpans`, `criteriaCount`,
  `detailCount`, `radioCount`, `checkboxCount` inchangés : **barème gelé**.
- `check_nomenclature.py` → `OK — aucun terme non suisse detecte` (code 0). Aucune valeur introduite
  en `g/dL`, `ng/mL`, `pg/mL`, `/mm³`, en livres ni en unité implicite ; la conversion du score de
  Maddrey est écrite en facteur (÷ 17.1) et en µmol/L, sans nommer l'unité bannie.
- `report_redundancy.py` par grille : **6 paires → 0** (29 : 5→0 · 32 : 0→0 · 33 : 0→0 · 36 : 0→0 ·
  40 : 1→0).
- `check_no_loss.py 2d09e16` par grille : 3 + 7 + 8 + 6 + 2 = **26 items signalés**, tous relus un à
  un — 18 reformulations enrichies ou fusions (l'item reste, réécrit), 6 suppressions dont le contenu
  est porté à l'identique ou en plus précis par un autre bloc, 2 portages explicites documentés
  ci-dessus. **Aucune perte réelle.**
- `git diff --numstat` : 5 fichiers, **29 insertions / 32 suppressions**, toutes dans la zone
  pédagogique (contrôlé hunk par hunk contre `peda_bounds`). Aucun `.criteria-text` touché, aucun
  crochet de réponse patient touché, aucun sous-item noté ajouté ni retiré, aucun item ICE touché.
