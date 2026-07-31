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
