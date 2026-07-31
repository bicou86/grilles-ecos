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

**Divergences consignées**

- section notée m5 · antibiothérapie, indication : la grille dit « Antibiothérapie si signes
  infectieux », la page SSP dit « antibiothérapie si cholécystite » (Conduites ciblées) — donc
  indiquée dès que le diagnostic est retenu. Non corrigé : la formulation est dans une section
  notée (barème gelé) et elle est reprise à l'identique par `theorie` et `presentation` ; corriger
  le seul pédagogique créerait une contradiction interne à la grille.
- resume · antibiothérapie, molécule : la grille dit « céphalosporine + métronidazole », la section
  notée m5 de la même grille dit « amoxicilline-acide clavulanique 1 g × 3/j IV, ciprofloxacine +
  métronidazole si allergie ». Non corrigé : la page SSP ne nomme aucune molécule pour la
  cholécystite (§ 4 cas 2 — ne rien inventer). Arbitrage clinique demandé.
- section notée m5 · AINS : la grille dit « Analgésie : paracétamol IV, AINS si pas de CI », la page
  SSP dit « éviter les AINS si suspicion d'ulcère, IRA ou patient âgé » — or la patiente prend des
  antiacides pour brûlures d'estomac. Non corrigé (section notée) ; la mise en garde a été portée
  dans `resume`, bloc pédagogique.
- grille entière · β-hCG : la page SSP en fait sa règle d'or (« toute douleur abdominale chez une
  femme en âge de procréer est une GEU jusqu'à preuve du contraire ») et son premier piège
  éliminatoire ; la grille ne le mentionne ni au pédagogique ni au barème. Non ajouté : l'ajouter au
  seul pédagogique créerait un écart avec le barème gelé, et son applicabilité à 47 ans relève de
  l'avis clinique.
- resume · crase : la page SSP liste la crase (TP, INR, aPTT) avec l'indication « pré-opératoire » et
  la grille conduit à une cholécystectomie ≤ 72 h. Non ajoutée : la page SSP ne la rattache pas
  explicitement à la cholécystite.

**Paires de redondance restantes (4) — justifiées par un changement de format**

- ×2 « nausées, vomissements » (`resume`/Symptômes typiques ↔ `presentation`/Q1 et Q3) : liste de
  symptômes → argument POUR dans une argumentation pour/contre par hypothèse.
- ×2 « échographie abdominale, examen clé » (`resume`/Imagerie et `resume`/Points clés ↔
  `presentation`/Q « Quels examens demanderiez-vous ? ») : liste → réponse orale à une question
  d'examinateur, sous-ensemble strict de `resume` (axe 1, qui prescrit explicitement cette Q/R).
