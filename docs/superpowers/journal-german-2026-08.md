# Journal de refonte — grilles German

Corpus : `cases/german`, 88 grilles. Outillage : `scripts/german/`.
Procédure : `scripts/german/PROCEDURE-german.md`, pendant de `scripts/amboss/PROCEDURE.md`.

Pendant du `journal-amboss-2026-07.md`, dont il reprend le format. Deux types
d'entrées :

- **Modification** — un changement appliqué, avec ce qui le justifie.
- **Divergence** — un écart repéré mais **non corrigé**, laissé à l'arbitrage.

## Format

    ### <passe ou grille> — <motif>

    **Modifications**
    - <bloc> · <sujet> : « <avant> » → « <après> »
      source : <référentiel — citation>

    **Divergences consignées**
    - <zone> · <sujet> : la grille dit « <x> » — non corrigé (<raison>)

## Entrées

### Volet A — Passe nomenclature suisse (tâche g2)

Mesure de départ, `check_nomenclature.py` au commit `4819f53` : **64 termes non
suisses**, 63 `NFS` dans 37 grilles et 1 `pg/mL` dans German-63. Après la passe,
**0**.

Script : `scripts/german/apply_lab_nomenclature.py`, écrit pour ce corpus.
`scripts/amboss/apply_lab_nomenclature.py` n'est **pas** modifié — il a produit
les mesures publiées d'AMBOSS — et n'est pas non plus réutilisé tel quel : les
règles diffèrent (German ne porte ni `CBC`, ni `BMP`, ni `911`, ni `SAMU`, ni
`g/dL`, ni `ng/mL`, ni `/mm³`). Le principe, lui, est repris : substitution
1 pour 1, **hors zones base64** (`data:image[^"]*` mis de côté avant toute
substitution), aucune modification de structure, donc aucun sous-item noté
touché.

**Contrôle préalable au remplacement** — exigé parce que `cases/scoring.js:159`
découpe `.criteria-text` par `.split(". ")[1].split(" [")[0]` : recherche de
`\bNFS\b` dans tout attribut `data-criteria` et dans tout `.criteria-text` des
88 grilles → **0 occurrence** dans l'un comme dans l'autre. Le remplacement ne
peut donc pas déplacer le libellé qu'affiche la liste des items manquants.

**Contrôle du sens de chaque occurrence** — les 63 `NFS` ont été relus un à un
dans leur contexte visible : tous désignent la numération formule sanguine
(« NFS, CRP, ionogramme », « NFS avec formule [leucocytose] », « NFS (anémie) »).
Aucun n'est un total de barème ni un sigle homonyme. C'est le contrôle qui avait
manqué de corrompre `Score Global 0/112` sur AMBOSS ; aucune règle sur un nombre
n'est d'ailleurs introduite ici.

**Modifications**

- global · laboratoire : « NFS » → « **FSC** », 63 occurrences dans 37 grilles
  (German-1, 2, 3 ×2, 6, 7, 8, 9, 11, 12, 13 ×2, 15 ×6, 19 ×6, 26, 29, 34 ×5,
  35, 40, 43 ×3, 45, 46 ×6, 47 ×2, 48, 49 ×2, 50, 51 ×2, 52, 53, 55, 60, 61, 67,
  69, 71, 74, 75, 76, 85).
  source : nomenclature suisse de laboratoire — formule sanguine complète ;
  même table `BANNED` que le corpus AMBOSS, importée et non recopiée.
- German-63 · unités : `detail-text criteria-detail` du critère `m2`,
  « Dosage œstradiol (**< 50 pg/mL**) » → « Dosage œstradiol (**< 184 pmol/L**) ».
  Œstradiol : `pg/mL` → `pmol/L`, **× 3,671** (masse molaire 272,4 g/mol) ;
  50 × 3,671 = 183,55 → **184**. Arrondi à l'entier, comme les conversions
  d'AMBOSS (320 → 236, 85 → 63, 200-900 → 148-664).

  *Qualificatif voisin vérifié.* Le seul qualificatif porté par cette valeur est
  le **sens de l'inégalité** : « < 50 pg/mL » et « < 184 pmol/L » décrivent le
  même seuil, le « < » reste donc exact après conversion. Balayage de la grille
  entière (`œstradiol`, `estradiol`, `E2`) : aucune autre mention, donc aucun
  adjectif (« bas », « effondré ») à réaccorder ailleurs. Le sous-item voisin
  « Dosage FSH (> 30 UI/L) » est déjà en unité suisse et n'est pas touché ; les
  deux valeurs restent cohérentes entre elles (FSH haute + œstradiol bas =
  ménopause confirmée).

  *Piège des valeurs multiples sur une ligne.* Les conversions du script portent
  sur la **ligne entière** et non sur le seul nombre, et le compte attendu est
  déclaré (`1`) : le script échoue si la substitution ne s'applique pas
  exactement une fois. C'est ce qui manquait quand « Hb < 7 g/dL (< 9 si
  coronarien) » et « B12 : 85 pg/mL (N: 200-900) » ont failli produire des seuils
  faux sur AMBOSS. Vérification indépendante : `pg/mL` n'apparaît qu'une fois
  dans les 88 grilles, cette ligne ne porte donc pas de seconde valeur.

**Divergences consignées** — aucune.

**Vérifications** — `check_nomenclature.py` 64 → **0** ; `check_invariants.py`
OK (88 grilles, barème inchangé) ; `check_reachability.py` OK (88 grilles à
100 %) ; `report_redundancy.py` **83**, inchangé ; `check_no_loss.py 4819f53` :
**0 item disparu** sur les 38 grilles modifiées ; intégrité `<div>`/`<ul>`/
`<li>`/`<span>` appariés et `</html>` final sur les 88. AMBOSS inchangé :
`check_invariants`, `check_nomenclature`, `check_reachability` OK,
`report_redundancy` 147.

### Volet B — Suppression du remplissage automatique d'`annexe-dd` (tâche g2)

Arbitrage utilisateur : **le remplissage est supprimé, aucun contenu médical
n'est créé en remplacement.** Une entrée réduite à son seul nom de diagnostic
reste utile — la liste des hypothèses à évoquer est en soi le contenu principal
du bloc.

Script : `scripts/german/prune_dd_filler.py`.

**Ce que porte le bloc, mesuré et non échantillonné.** Les 78 segments
`annexe-dd` des 88 grilles portent **484 entrées `<li>`**, toutes de la même
forme, sans une seule exception (contrôlé : le résidu de chaque `<li>` une fois
ses trois éléments retirés est exactement `<br>`) :

    <li><strong>NOM</strong><br>
        <div …rgb(80, 90, 110)>ARGUMENTS</div>
        <div …rgb(52, 105, 46)>→ EXAMEN</div></li>

soit **588 puces d'arguments** (216 formulations distinctes) et **484 examens**
(129 formulations distinctes). Les deux listes ont été lues intégralement pour
établir la liste des formulations génériques — le critère retenu étant *une
formulation qui serait vraie pour n'importe quel diagnostic de n'importe quelle
grille*.

**Modifications**

- annexe-dd · arguments : **345 puces « À évaluer cliniquement » supprimées**,
  dans 71 grilles — 59 % des 588 puces. Une seule formulation générique existe
  dans tout le corpus, et ses 345 occurrences sont **toutes** seules dans leur
  `<div>` : aucun cas mixte où elle cohabiterait avec un argument réel. Le
  `<div>` entier part, jamais le seul texte.
- annexe-dd · examens : **262 flèches supprimées** sur 484, en **quatre**
  formulations — « Examens complémentaires selon contexte clinique » (258),
  « Bilan biologique spécifique » (2), « Évaluation clinique approfondie » (1),
  « Anamnèse » seule (1). Aucune ne nomme d'examen : ni organe, ni technique, ni
  analyte, ni score.
- annexe-dd · mise en forme : le `<br>` qui suivait le nom est retiré dans les
  **209 entrées réduites au nom seul**, où il n'a plus rien à séparer. Il est
  conservé partout ailleurs, ce qui laisse l'interligne existant inchangé.

**Ce qui subsiste** : les 484 noms de diagnostic (aucun n'est touché),
**243 puces d'arguments réelles** et **222 examens discriminants réels**. Sur
les 209 entrées réduites au nom seul, 82 portent déjà dans leur nom l'examen ou
la précision qui départage — « Achalasie → Manométrie œsophagienne », « Corps
étranger/calcul → Radiographie, échographie », « Irritation du nerf ulnaire
[Signe de Tinel] » — et 127 restent un nom nu, c'est-à-dire une hypothèse à
évoquer.

**Suppression d'élément, jamais de texte.** Le script ne fait que supprimer des
plages de caractères mesurées et disjointes, chacune couvrant un élément entier.
Preuve *a posteriori*, rejouée sur les 88 grilles : le contenu de chaque fichier
après passe est **exactement** son contenu avant passe privé des 816 plages
planifiées, et l'ensemble des chaînes retirées ne compte que **6 formes
distinctes** (les 4 `<div>` d'examen générique, le `<div>` d'argument générique,
et `<br>`), pour 70 401 caractères. Rien d'autre n'a bougé dans les 88 fichiers.
Le bloc `annexe-dd` étant le **frère** d'un `criteria-row` qui porte l'`<input
type="radio">` du critère englobant, c'est la propriété qui garantit qu'aucun
`</div>` n'a pu se déplacer — le défaut de German-84. German-84 ne porte
d'ailleurs aucun `annexe-dd` et n'est pas modifiée.

**Divergences consignées**

- annexe-dd · formulations **limites conservées**, parce qu'elles ne seraient
  pas vraies de n'importe quel diagnostic : arguments « rare » (2),
  « diagnostic d'exclusion », « peu probable vu l'âge », « sans cause évidente »,
  « processus inflammatoire » ; examens « Anamnèse médicamenteuse » (2),
  « Anamnèse, audiométrie », « Examen neurologique, imagerie », « Examen
  ophtalmologique », « Évaluation cognitive », « Révision du traitement »,
  « Examen clinique, évaluation environnement », « Critères temporels DSM-5 »,
  « Évaluation temporelle des symptômes », « Diagnostic clinique, biopsie si
  doute ». La plus discutable est **« Évaluation temporelle des symptômes »**
  (German-4, trouble de l'adaptation) : conservée parce que le calendrier est
  précisément ce qui la sépare du trouble dépressif persistant de la même liste,
  dont l'examen est « Critères temporels DSM-5 ».
- annexe-dd · les **89 flèches portées par le nom lui-même** (« Fracture
  vertébrale → Radiographie si critères présents ») ne sont pas touchées : elles
  font partie du nom, qui est hors périmètre. Elles expliquent qu'une entrée
  puisse perdre son `<div>` d'examen générique tout en conservant un examen.
- annexe-dd · trois formulations citées au brief comme génériques **n'existent
  pas dans ce bloc** : « selon contexte clinique » seul (0 — les 258 occurrences
  sont la formule longue), « Examen clinique complet » (2 occurrences, toutes
  **hors** `annexe-dd`, donc hors périmètre et non touchées), « Anamnèse et
  examen clinique » (0 dans tout le corpus).

**Vérifications** — `check_invariants.py` OK (barème inchangé : le bloc ne porte
aucune case à cocher) ; `check_reachability.py` OK, 88/88 à 100 % ;
`check_nomenclature.py` OK ; `bounds_anomalies()` et `uncovered_content()` vides
sur les 88 ; intégrité `<div>`/`<ul>`/`<li>`/`<span>` appariés et `</html>` final
sur les 88. Redondance **inter-blocs 83 → 82**, **intra-bloc 638 → 118**
(−81 %) : le remplissage était dupliqué d'une entrée à l'autre *dans* le même
bloc, donc intra ; le chiffre inter-blocs bouge peu parce que 63 des 88 grilles
n'ont qu'`annexe-dd` et aucun bloc avec quoi former une paire.
`check_no_loss.py 4819f53` : 405 items signalés sur 79 grilles, **audités un à
un**, aucune perte réelle — 379 ont un résidu vide (pur remplissage) ou retrouvé
tel quel ; les 26 restants sont des artefacts de mesure, vérifiés présents dans
le fichier caractère par caractère : 20 sont des puces réelles conservées mais
devenues plus courtes que le seuil `min_len=18` de `list_items()` (« AIT »,
« TVP », « FAI », « L2-L3 », « alcool d'hier », « signe de Déjérine »…), et 6
sont l'effet du renommage `NFS` → `FSC` du volet A dans le même intervalle.

### German-44 (Érythème — lupus érythémateux cutané) — grille pilote du corpus, tâche g3

Page SSP : `SSP ECOS/SSP — Éruption Cutanée.md` (mapping ligne 1254).
Blocs présents : `annexe-dd`, `redflags`, `therapy` ×2, `resume`, `presentation`,
`annexe-image`. **Ni `annexe-expert` ni `annexe-theorie`** — ils n'existent nulle
part dans ce corpus, donc les axes 1, 2, 6 et 7 de `scripts/amboss/PROCEDURE.md`
§ 3, qui reposent sur eux, sont **sans objet ici**. Restent applicables : `resume`
canonique (axes 3 et 4), la trame de présentation (axe 5), la règle du format et
la règle anti-perte.

**La page SSP ne tranche rien de cette grille.** Elle couvre l'éruption cutanée
générique — toxidermie, purpura fébrile, SJS/Lyell, DRESS, érysipèle — et ne porte
aucune occurrence de « lupus », « ANA », « anti-SSA », « hydroxychloroquine » ni
« photosensibilité ». Le seul point où elle recoupe la grille est
« Biopsie cutanée si doute diagnostique » (§ 🔬 EXAMENS COMPLÉMENTAIRES), que
`resume` porte déjà mot pour mot. **Niveau 3** sur toute la prise en charge : rien
à aligner, rien inventé. L'arbitrage s'est donc fait au niveau 2 (section notée)
et par le contrat de blocs.

**Modifications**

- annexe-dd · Psoriasis : « Arguments POUR : Plaques érythémato-squameuses bien
  délimitées · **Localisations typiques (coudes, genoux)** · **Antécédents
  familiaux possibles** » → POUR conservé sur la seule plaque, les deux autres
  **déplacés en Arguments CONTRE** sous leur forme négative
  (« Localisations typiques absentes (coudes, genoux, cuir chevelu) »,
  « Pas d'antécédents familiaux »).
  source : section notée `e2` « Examen cutané détaillé [Érythème rouge légèrement
  squameux **au niveau du dos**] » et `a11` « Antécédents familiaux [Grands-parents
  hypertendus après 65 ans, grand-père avec goutte] » — **niveau 2**. Le bloc
  affirmait comme arguments *pour* le psoriasis deux éléments que la section notée
  déclare absents chez cette patiente.
- annexe-dd · Photodermatose : « POUR : Éruption liée à l'exposition solaire ·
  **Amélioration à l'ombre** · **Récidive à chaque exposition** » → POUR resserré
  sur « Aggravation nette pendant les vacances en Italie », les deux autres
  critères **déplacés en CONTRE** en gardant leur nom
  (« Persistance après la fin de l'exposition, sans amélioration à l'ombre »,
  « Premier épisode, sans récidive à chaque exposition »), plus « Pas de prurit ».
  source : sections notées `a4` [Depuis environ 3 semaines], `a13` [Retour d'Italie
  il y a 2 semaines], `a5` [Non, premier épisode], `a3` [Pas de démangeaisons].
- annexe-dd · les cinq arguments CONTRE ci-dessus sont **portés depuis**
  `presentation`/« Arguments pour et contre » (Q2 et Q3), pas inventés. C'est le
  geste anti-perte : porter d'abord dans le bloc dont c'est le rôle, supprimer
  ensuite. Le bloc ne portait que des « Arguments POUR » et ne **départageait**
  donc rien, alors que c'est sa raison d'être au contrat.
- resume · Prise en charge / Traitement topique : « Inhibiteurs de calcineurine
  (tacrolimus, off-label) » → « … **— surtout sur le visage** ».
  source : `therapy` du critère noté `m5`, « Inhibiteurs de la calcineurine :
  Alternative aux corticoïdes, **surtout pour le visage** » — niveau 2. Porté
  avant la suppression de « Inhibiteurs de la calcineurine si visage » dans
  `presentation`.
- resume · Prise en charge : **nouvelle sous-section « Signes d'alarme (passage
  systémique) »** — atteinte rénale (protéinurie, hématurie), atteinte
  neurologique (convulsions, troubles cognitifs), arthrites franches, cytopénies
  inexpliquées. Portée depuis `presentation`/Touches ludiques, où elle était la
  seule **donnée clinique** que le bloc canonique ne portait pas — ce que le
  contrat interdit à `presentation` (« ne porte jamais : toute donnée clinique
  nouvelle »). Elle rend enfin actionnable le point clé « Toujours rechercher
  signes de passage en lupus systémique », qui restait sans contenu.
- presentation · Touches ludiques / **« Formes cliniques de lupus cutané »** :
  supprimée. Doublon strict de `resume`/Examen clinique/Formes cliniques
  principales, **même format** (liste) — 3 des 17 paires. Comparée item par item
  avant suppression : aigu, subaigu, chronique discoïde et tumidus figurent tous
  dans `resume` ; « risque alopécie cicatricielle » y est déjà (« parfois alopécie
  cicatricielle ») et « malaire » subsiste trois fois ailleurs dans la grille.
- presentation · Touches ludiques / **« PEC pratique »** : supprimée. Check-list
  actionnable — ce que le contrat interdit à `presentation` — doublant
  `resume`/Prise en charge et le `therapy` du critère `m5`. Ses cinq items sont
  tous retrouvés (le « visage » ayant été porté dans `resume` juste avant).
- presentation · Touches ludiques / Pièges ECOS : puce « Toujours relier à
  exposition solaire » supprimée. Même contenu et même format que
  `resume`/Questions à poser « Relation avec exposition solaire ? », et déjà le
  point clé n° 1 du `resume` (« Photosensibilité + lésions cutanées chroniques =
  évoquer lupus cutané »). Les trois autres pièges restent : **l'axe 6 d'AMBOSS
  — « supprimer `presentation`/Pièges ECOS » — est sans objet ici**, faute
  d'`annexe-expert` ; c'est le seul bloc de pièges de la grille.
- presentation · `mnemo-box` LUPUS **déplacée** de « Checklist mentale » vers
  « Touches ludiques / mnémos ». Geste de l'axe 5 et précédent AMBOSS-2/3 : la
  checklist redevient une trame pure. Les cinq clés sont intactes. État du corpus
  après coup : AMBOSS 15/15 en `section-mnemo`, German 11 encore en
  `section-checklist` et 3 en `section-express` — les 14 autres grilles à mnémo
  suivront.
- presentation · Q1 « Lupus érythémateux cutané » : « Érythème squameux chronique,
  non prurigineux » + « Aggravation après exposition solaire » **fusionnés** en
  « Érythème squameux chronique **photosensible**, non prurigineux ». Réduction
  aux arguments décisifs ; « photosensible » dit exactement l'aggravation solaire,
  qui figure par ailleurs dans la version longue, le SBAR et `annexe-dd`.
- presentation · Q2 « Psoriasis » et Q3 « Photodermatose » (POUR/CONTRE
  structurés) **remplacés par une seule réponse orale** : « Pourquoi écarter le
  psoriasis et la photodermatose ? ». C'est le miroir d'`annexe-dd` qui cède,
  après que le contenu discriminant y a été porté ; le passage liste → narration
  parlée est le changement de format que la règle autorise, et c'est le rôle même
  du bloc (restituer à l'oral).
- presentation · Q « Quels examens demanderiez-vous ? », Q2 « Traitement », Q3
  « Suivi » : les trois `presentation-reponse list` / `<ul>` **convertis en
  `presentation-reponse text`** en registre parlé.
  motif : « Une liste recopiée sous un en-tête Q/R ne constitue pas un changement
  de format » (`scripts/amboss/PROCEDURE.md` § 3, « Redire à l'oral, pas en
  liste »). Q3/Suivi recopiait de surcroît **mot pour mot** les quatre
  sous-items du critère noté `m7` — duplication de niveau 2 qu'aucune mesure de
  redondance ne peut voir, les sections notées n'étant pas des blocs. Contenu
  strictement conservé, `<span class="highlight-range">` et
  `<span class="highlight-important">` compris.

**Divergences consignées**

- redflags (`m6`) · le second signal d'alarme s'intitule **« 2. Signes d'alerte »**
  et ne dit rien. C'est le corrigé d'un critère noté (**niveau 2**), et le
  compléter reviendrait à écrire le corrigé à la place de l'auteur — règle 3 des
  arbitrages (jugement d'auteur). **Non corrigé.** Le contenu qui le remplirait
  est désormais dans `resume`/« Signes d'alarme (passage systémique) ». À noter
  que la procédure interdit par ailleurs de modifier `redflags` pour résoudre un
  doublon : ici il ne s'agissait pas d'un doublon, mais la conclusion est la même.
- resume · deux paires **intra-bloc** subsistent, structurelles : « Éviter
  médicaments inducteurs » (Prise en charge) ↔ « Prise de médicaments
  inducteurs ? » (Questions à poser) — une mesure et une question ; et « Biopsie
  cutanée confirme le diagnostic » (Points clés) ↔ « Biopsie cutanée si diagnostic
  incertain » (Examens à faire) — l'indication et son rendement. Le chiffre
  intra-bloc mesure, il ne prescrit pas.

**Vérifications** — `check_invariants.py` OK (88), `check_nomenclature.py` OK,
`check_reachability.py` OK 88/88 à 100 %. **Aucune modification du barème** : les
trois blocs touchés ne portent ni `<input>` ni case, `maxScores`, `scoreSpans`,
`sectionCounts`, `criteriaCount`, `detailCount`, `radioCount` et `checkboxCount`
sont inchangés — règle 1 des arbitrages, pas de régénération de `baseline.json`.
AMBOSS intact, redondance **147**. `<div>`/`<ul>`/`<li>`/`<span>` appariés (602,
21, 79, 87), équilibre bloc par bloc vérifié.

Redondance German-44 : **17 → 2** paires inter-blocs (corpus 82 → 67).
Les deux qui restent sont **le même item** — la clé `S` du mnémo LUPUS,
« S = Surveillance évolutive vers lupus systémique », face à
`resume`/PEC en 3 points et à `redflags`/`m6`. Un mnémo garde sa clé d'origine
(§ 3, « supprimer le mot d'origine casserait le mnémo ») : la paire est le prix
du format mnémotechnique, qui n'est ni une liste ni une narration.

`check_no_loss.py fbe42f9` : 18 items signalés, **verdictés un à un, aucune perte
réelle**. Cinq sont les arguments portés dans `annexe-dd`, un est la nuance
« visage » portée dans `resume`, quatre sont les items de « Formes cliniques » et
« PEC pratique » retrouvés dans `resume` ou `therapy`, et les huit derniers sont
l'effet mécanique des trois conversions liste → narration : `list_items()`
n'extrait pas le texte d'un `presentation-reponse text`, si bien qu'une réponse
orale complète y apparaît toujours comme une disparition. Présence contrôlée
chaîne par chaîne sur le HTML brut après `strip_base64` — jamais par `grep`.

### Tâche g4 — Les 12 grilles riches restantes (15, 19, 22, 27, 34, 42, 43, 48, 56, 69, 72, 88)

Départ `ff4605c`. Ce sont les 12 dernières grilles à porter simultanément
`resume`, `annexe-dd` et `presentation` — le seul couple pédagogique du corpus.
Le patron du pilote German-44 a été suivi dans l'ordre : (1) lire la section
notée en entier, (2) porter les CONTRE dans `annexe-dd`, (3) supprimer de
`presentation` ce qui double `resume` **au même format**, (4) convertir les
réponses Q/R en liste vers le registre parlé, (5) déplacer le mnémo, (6)
vérifier à l'œil qu'aucune réponse ne recopie un `criteria-text`. Les axes 1, 2,
6 et 7 d'AMBOSS restent sans objet (ni `annexe-expert` ni `annexe-theorie`), et
`presentation`/Pièges ECOS n'a été supprimé dans **aucune** grille.

**Pages SSP.** Les huit pages consultées (Douleur Abdominale, Douleurs
Articulaires, Douleur d'Épaule, Dysphagie, Éruption Cutanée, Fièvre du
Nourrisson, Incontinence Urinaire, Amaurose & BAV, Œil Rouge, Troubles de la
Croissance) confirment le constat du pilote : elles ne tranchent presque rien.
**Une seule occurrence de niveau 1** sur les 12 grilles, en German-15. Tout le
reste s'est arbitré au **niveau 2** (section notée), qui est riche.

**Modifications, par grille**

- **German-15** (diverticulite) · `resume` : « coloscopie à distance **4–6**
  semaines » → **6–8**, aux deux endroits (Examens diagnostiques et Examens à
  faire). source : `m7-detail-2` « Coloscopie 6-8 semaines après l'épisode » —
  **niveau 2** ; `presentation` disait déjà 6–8 en quatre endroits, `resume`
  était seul à dire 4–6.
- **German-15** · `resume`/Formes simples : ajout « abstention possible chez le
  patient sélectionné, immunocompétent et sans signe de gravité (SSMI/SGAIM) ».
  source : `SSP — Douleur Abdominale` l. 445, « non compliquée → antibiothérapie
  ambulatoire (voire abstention chez le patient sélectionné, SSMI/SGAIM) » —
  **niveau 1**, seule occurrence du lot.
- **German-15** · `annexe-dd` : Colite et Cancer colorectal reçoivent leurs
  **arguments CONTRE**, portés depuis `presentation` Q2/Q3 ; Q2 et Q3 fusionnent
  en une réponse orale. `presentation` Q « examens », Q2 « Traitement », Q3
  « Suivi » : `list` → `text`. Mnémo DIVERTI déplacé vers Touches ludiques.
- **German-19** (RCUH) · `annexe-dd` : Colite infectieuse et Maladie de Crohn
  reçoivent POUR **et** CONTRE ; l'examen qui départage la colite infectieuse
  passe de « Coloscopie, calprotectine fécale » à « Examen bactériologique et
  parasitologique des selles ; calprotectine et coloscopie si persistance ».
  source : `m3` « Examen bactériologique des selles » et `a17` « Anamnèse de
  voyage [Il y a 2 semaines en Égypte] » — **niveau 2**. Correction de fond : ce
  n'est pas la coloscopie qui tranche une colite infectieuse.
- **German-19** · `presentation`/Pièges : puce « Ne pas proposer coloscopie avec
  biopsies » supprimée — même contenu et même format que `resume`/PEC en
  3 points « Diagnostic par coloscopie avec biopsies », et le point clé n° 2 du
  `resume`. Les trois autres pièges restent. Mnémo SANG déplacé. Trois réponses
  `list` → `text` ; Q « examens » reçoit au passage les gamma-GT et phosphatases
  alcalines de `m3` (dépistage de CSP), qu'aucun bloc pédagogique ne portait.
- **German-22** (épicondylite) · `annexe-dd` : les **cinq** hypothèses reçoivent
  POUR/CONTRE case-appliqués, portés depuis `presentation` Q2-Q5 et depuis la
  sous-section « Diagnostic différentiel rapide » de Touches ludiques ; Q2-Q5
  fusionnent en une réponse orale.
- **German-22** · `presentation`/Touches ludiques : « Tests spécifiques Tennis
  elbow » et « Diagnostic différentiel rapide » supprimées. La première est un
  sous-ensemble strict de `resume`/Tests spécifiques au même format (Cozen, Mill,
  chaise, tous présents, `resume` en portant un quatrième) ; la seconde est du
  **raisonnement différentiel**, que le contrat réserve à `annexe-dd`, et son
  contenu y a été porté avant suppression. Mnémo ELBOW déplacé. Q « examens »,
  Q2, Q3 : `list` → `text`. Q3/Suivi recopiait `m4` (« Bon pronostic, durée
  semaines à mois », « Charge sportive uniquement jusqu'à absence de douleur »).
- **German-27** (conflit sous-acromial) · `annexe-dd` : entrée « Capsulite
  rétractile » **réparée** — son « → Diagnostic clinique, IRM si doute » avait
  été avalé dans la puce d'argument POUR (défaut de structure, pas d'import) —
  puis dotée du CONTRE décisif « Mobilité passive conservée ». Arthrose
  gléno-humérale et Névralgie cervico-brachiale reçoivent POUR/CONTRE.
- **German-27** · `presentation` : les **cinq** `presentation-reponse list`
  converties en `text` ; « Tests spécifiques » et « Conflit sous-acromial
  typique » supprimées de Touches ludiques (sous-ensembles stricts de `resume`,
  même format) ; mnémo ARC déplacé.
- **German-34** (cancer de l'œsophage) · `annexe-dd` : entrée « Compression
  extrinsèque » réparée (même défaut de structure qu'en German-27) ; Cancer ORL
  et Achalasie reçoivent POUR/CONTRE. Touches ludiques : « Signes d'alarme
  dysphagie », « Principaux diagnostics différentiels » et « Examens clés »
  supprimées — sous-ensembles stricts de `resume` pour la première et la
  troisième, d'`annexe-dd` pour la deuxième. Mnémo ALARME déplacé. Q1 examens,
  Q2, Q3 : `list` → `text` ; Q3/Suivi absorbe `m6` (information du patient).
- **German-42** (tinea corporis) · `annexe-dd` : Psoriasis — « coudes, genoux,
  antécédents familiaux » figuraient en **Arguments POUR** alors que la section
  notée les déclare absents ; **déplacés en CONTRE** sous forme négative, pas
  dupliqués (le piège signalé par le pilote). Dermatite atopique et Eczéma
  nummulaire reçoivent POUR/CONTRE. Q2-Q4 fusionnent en une réponse orale.
- **German-42** · Touches ludiques : « Examens utiles » et « PEC antifongique »
  supprimées (sous-ensembles stricts de `resume`, même format) ; le mnémo PED et
  les Pièges restent, RING est déplacé. Q « examens », Q2, Q3 : `list` → `text`.
  Q3/Suivi recopiait `m7` (contrôle à 2 semaines, guérison mycologique,
  adaptation) et `m6` (mesures d'hygiène).
- **German-43** (scarlatine) · `annexe-dd` : Rougeole — sa description (« macules
  puis papules descendantes, signe de Koplik ») figurait en **POUR** alors que
  ces signes sont absents ; restructurée en POUR/CONTRE. Varicelle et Rubéole
  reçoivent POUR/CONTRE. **Ajout de la Maladie de Kawasaki**, présente dans
  `resume`/Différentiels et dans `presentation` mais absente du bloc dont c'est
  le rôle. Q2-Q5 fusionnent en une réponse orale.
- **German-43** · `resume` : l'éruption devient « micropapuleuse, **rugueuse au
  toucher (« papier de verre »)**, accentuée dans les plis » — porté depuis
  `presentation` avant la suppression de « Signes typiques scarlatine » (sous-
  ensemble strict de `resume`/Signes caractéristiques). Traitement symptomatique
  reformulé pour cesser de recopier le `therapy` de `m4`. Mnémo FAR déplacé.
  Q « examens », Q2, Q3 : `list` → `text` ; Q3/Suivi recopiait `m5`, `m6` et `m7`.
- **German-48** (exanthème subit) · `annexe-dd` : la première catégorie ne
  contenait pas un différentiel mais deux fragments d'arguments du diagnostic
  principal (« Âge typique / POUR : 6 mois - 2 ans → Diagnostic clinique » et
  « Fièvre élevée avec bon état général → Surveillance ») ; **refondue en une
  entrée « Exanthème subit (HHV-6/7) — hypothèse principale »** avec POUR/CONTRE
  et examen. Rougeole, Rubéole et Érythème infectieux passent d'un descriptif
  fondu dans le titre à des POUR/CONTRE structurés ; **ajout de la Scarlatine**,
  présente partout ailleurs dans la grille.
- **German-48** · Touches ludiques : « Diagnostic typique exanthème subit »
  (sous-ensemble strict de `resume`), « Différentiels viraux » (rôle
  d'`annexe-dd`, porté) et « Signes d'alerte pédiatriques » supprimées. La
  dernière recopiait les cinq `redflags-text` de `m6` **et** ses cinq
  `detail-text` : duplication pédagogique ↔ section notée, invisible à
  `report_redundancy`. Mnémo 3-1-R déplacé. `resume` : trois formulations de
  « convulsions fébriles » précisées pour cesser de recopier `redflags`/`m6`
  (le pédagogique cède, jamais le corrigé). Q1-Q5 fusionnent en deux réponses
  orales ; Q « examens », Q2, Q3 : `list` → `text`. Le seuil de réévaluation de
  Q3 passe de « fièvre > 5 jours » à « 3 à 4 jours si persistance » —
  source `m5-detail-1`, **niveau 2**.
- **German-56** (incontinence d'effort) · `annexe-dd` : entrée « Vessie
  hyperactive secondaire » réparée (même défaut de structure) ; Vessie
  hyperactive idiopathique et Incontinence mixte reçoivent POUR/CONTRE. Q2/Q3
  fusionnent en une réponse orale. Mnémo MAPS-U déplacé. Q1 examens, Q2, Q3 :
  `list` → `text` ; Q3/Suivi recopiait `m5` mot pour mot.
- **German-69** (cataracte) · `annexe-dd` était déjà **exemplaire** — seul bloc
  du corpus à porter des CONTRE sur onze hypothèses. Il reçoit seulement les deux
  arguments POUR que `presentation` portait en plus (halos lumineux, myopie
  d'induction) et le POUR du glaucome chronique. Q1-Q3 fusionnent en deux
  réponses orales, Q1 examens, Q2, Q3 : `list` → `text`. Mnémo MAPS déplacé.
- **German-72** (maladie cœliaque) · `annexe-dd` : quatre des six hypothèses
  reçoivent POUR/CONTRE et leur examen discriminant (test de la sueur, âge
  osseux, TSH). Q2-Q5 fusionnent en une réponse orale. Mnémo GROWTH déplacé.
  Q1 examens, Q2, Q3 : `list` → `text` ; Q1 reçoit l'albumine et le caryotype de
  `m3`/`m4`, Q3 recopiait `m8` et ignorait `m9`.
- **German-88** (conjonctivite allergique) · `annexe-dd` : Conjonctivite
  infectieuse et Kératite/érosion sur lentilles reçoivent POUR/CONTRE et leur
  examen (prélèvement bactériologique, fluorescéine). `resume` : ajout de
  « **arrêt temporaire du port de lentilles** » et des compresses froides.
  source : `m6` « Arrêt temporaire des lentilles » et `m4` « Compresses froides »
  — **niveau 2** ; le patient porte des lentilles (`a8` « oui habituellement »)
  et aucun bloc pédagogique ne le disait. Mnémo PRURIT déplacé. Q2/Q3 fusionnent
  en une réponse orale ; Q1 examens, Q2, Q3 : `list` → `text`, et la dimension
  IST/Chlamydia de `m3` et `m7` entre enfin dans le pédagogique.

**Divergences consignées**

- **German-56** · le mnémo DAME repose sur « **A = Argenturie** », mot qui
  n'existe pas — le terme est *urgenturie*. Corriger la coquille casse la clé du
  mnémo, et la procédure interdit de supprimer le mot d'origine. **Non corrigé**,
  règle 3 (jugement d'auteur) : à trancher entre garder la coquille et refondre
  le mnémo.
- **German-56**, **German-69** et **German-88** · une `mnemo-box` « SBAR » vit
  dans `section-express`, immédiatement sous la version SBAR dont elle est la
  **légende**. L'axe 5 vise la Checklist mentale, pas la version express : ces
  trois mnémos sont **laissés en place**. État du corpus après cette passe :
  German **13** `mnemo-box` en `section-mnemo`, **3** en `section-express`,
  **0** en `section-checklist` (mesuré).
- **German-27** · la section notée `e4` cote le test de Jobe « Gauche : moins de
  force, douloureux » alors que la version longue dit « pas de perte de force
  nette » et que `resume` décrit le test comme « souvent douloureux mais non
  déficitaire ». Ce n'est pas une contradiction stricte (inhibition antalgique),
  mais la rupture de coiffe ne peut pas être formellement écartée : **aucun
  argument CONTRE n'a été écrit** pour elle dans `annexe-dd`. Consigné.
- **German-43**, **German-48** · deux formulations approximatives ont disparu au
  cours de la restructuration d'`annexe-dd` : « conjonctivite typique absente »
  pour la rubéole (la conjonctivite n'est pas le signe cardinal de la rubéole ;
  remplacée par l'adénopathie rétro-auriculaire) et « convulsions non typiques »
  pour l'érythème infectieux (l'enfant n'en a pas). Remplacements assumés, pas
  des pertes.
- `resume`/`therapy` · German-43 portait une paire `resume ↔ therapy` sur les
  antipyrétiques. Le pédagogique a cédé **par reformulation**, pas par
  suppression : le contenu doit rester dans `resume`, qui est la fiche de
  révision, tandis que `therapy` est le corrigé du critère. Aucun `therapy` ni
  `redflags` n'a été modifié dans les 12 grilles.

**Vérifications** — `check_invariants.py` OK (88), `check_nomenclature.py` OK,
`check_reachability.py` OK 88/88 à 100 %, AMBOSS aux trois verts et redondance
**147**. **Aucune modification du barème** : aucun `.criteria-text`, aucun
`<input>`, aucun `<span class="score">`, aucun `maxScores` n'apparaît dans le
diff (vérifié) — règle 1 des arbitrages, `baseline.json` non régénéré. Balises
appariées sur les 12 fichiers (`div`, `ul`, `li`, `span`), `boundsAnomalies` et
`uncoveredContent` vides.

Redondance : **63 → 10** paires inter-blocs sur les 12 grilles ; corpus German
**67 → 14** (les 4 autres sont German-44, 2, et German-68, 2 — hors périmètre).
Les 10 restantes sont **toutes** des clés de mnémo protégées par la règle du
format : DIVERTI/`I` (15), MICI/`C` ×2 (19), ARC/`A` ×2 et `R` (27),
ALARME/`E` (34), 4R/`Rééducation` (56), GROWTH/`R` (72), PRURIT/`Rougeur` (88).
Cinq grilles tombent à **0** : 22, 42, 43, 48 et 69.

`check_no_loss.py ff4605c` : **235 items signalés sur les 12 grilles, verdictés
un à un, aucune perte réelle**. Répartition : ~150 sont l'effet mécanique des
conversions liste → narration — **38 réponses Q/R converties** (29
`presentation-reponse list`, qui tombent ainsi de 29 à **0** sur les 88 grilles,
et 9 `reponse-section` à `<ul>`) et **30 réponses POUR/CONTRE structurées
fusionnées en 13 réponses orales** ; `list_items()` n'extrait pas le texte d'un
`presentation-reponse text` ; ~55 sont des arguments portés dans `annexe-dd`,
où ils ont été réécrits en forme case-appliquée ; ~25 sont les items des
**13 sous-sections** supprimées de Touches ludiques (2 en German-22, 2 en
German-27, 3 en German-34, 2 en German-42, 1 en German-43, 3 en German-48) et de
la puce de Pièges de German-19, tous retrouvés dans `resume`,
`annexe-dd`, `therapy` ou la section notée ; les 5 derniers sont des `<li>`
d'`annexe-dd` dont la normalisation a changé parce que le bloc a été
restructuré. Présence contrôlée chaîne par chaîne sur le HTML après
`strip_base64` — jamais par `grep`.

---

### Lot g5a — les 25 grilles à `annexe-dd` seul de German-1 à German-30

Périmètre établi : German-1 à 30, moins les 4 grilles riches déjà traitées au lot
g4 (15, 19, 22, 27 — `resume` **et** `presentation`) et moins German-1, sans
`annexe-dd` (3 `therapy-section` seulement, niveau 2, hors périmètre). Restent
**25 grilles** : 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 16, 17, 18, 20, 21,
23, 24, 25, 26, 28, 29, 30. German-24 y figure : elle porte un `resume` mais pas
de `presentation`, donc elle n'était pas du lot g4.

Aucun dédoublonnage inter-blocs possible (`report_redundancy.py` : **0 paire**
sur les 25 avant comme après). Le travail a porté sur les quatre points de la
consigne. **7 grilles modifiées** : 5, 6, 12, 13, 24, 28, 30.

#### 1. Le défaut de structure d'`annexe-dd` — **32 occurrences, 32 réparées**

Le lot g4 décrivait la flèche « → examen qui départage » avalée dans la puce
« Arguments POUR ». Le balayage de ce lot en trouve **deux variantes**, la
seconde étant de loin la plus fréquente et non encore documentée :

| Variante | Où tombe la flèche | Occurrences | Grilles |
|---|---|---:|---|
| **A** — celle de g4 | dans le `<div>` des arguments (`rgb(80, 90, 110)`) | **2** | 5, 6 |
| **B** — nouvelle | dans le `<strong>` du **nom du diagnostic** | **30** | 5, 6, 13, 28, 30 |

La variante B produit des noms d'hypothèse absurdes — « Fracture de côte →
Radiographie thoracique », « Colite à Clostridium difficile → Recherche de
toxines A et B » — et, dans 9 cas, **coexiste avec un `<div>` d'examen déjà
présent**, si bien que la même entrée porte deux lignes d'examens concurrentes.
Elle échappe entièrement au motif de recherche proposé par g4 (« `Arguments
POUR:` suivi d'un `→` dans la même puce ») : le balayage doit porter sur la
présence d'un `→` **hors** du `<div class` d'examen, pas sur les arguments.

Réparation, dans les deux variantes : l'examen quitte l'élément qui l'avait
avalé et rejoint son propre `<div style="… color: rgb(52, 105, 46);">`, la forme
canonique du corpus. Quand un `<div>` d'examen existait déjà, les deux listes
sont **fusionnées**, l'examen qui départage placé en tête, les doublons stricts
écartés — aucune suppression de contenu.

**Modifications**

- `annexe-dd` · German-30, 4 entrées : « Fracture de côte → Radiographie
  thoracique » + examen « → Radiographie, CT si complexe » → nom « Fracture de
  côte », examen « → Radiographie thoracique, CT si complexe ». Idem Contusion
  costale, Pneumothorax (fusion des trois modalités), Hémothorax.
- `annexe-dd` · German-28, 8 entrées : nom et examen séparés à l'identique
  (Otite moyenne aiguë virale / bactérienne, Otite externe, Pharyngite/angine,
  Douleur dentaire irradiée, Adénite cervicale, Tympan rouge par pleurs
  intenses, Corps étranger auriculaire).
- `annexe-dd` · German-13, 8 entrées : idem, avec fusion pour Colite ulcéreuse,
  Cancer colorectal et Tumeur neuroendocrine.
- `annexe-dd` · German-5, 6 entrées : 5 en variante B, 1 en variante A
  (« Arguments POUR: • WAD grade I-II → Diagnostic clinique » → argument
  « • WAD grade I-II », examen « → Diagnostic clinique »).
- `annexe-dd` · German-6, 6 entrées : 1 en variante A, 5 en variante B. Ces six
  entrées cumulaient un **troisième** défaut — les arguments cliniques logés
  dans le nom après un « : » (« Ménopause : âge compatible, troubles
  menstruels → FSH, LH, œstradiol »). Les trois éléments ont été rendus à leurs
  trois places : nom, `Arguments POUR:` en puces, examen. Contenu intégralement
  conservé, aucune formulation nouvelle.

#### 2. Erreurs factuelles internes — 3 corrections directes

- `annexe-dd` · **German-28**, Pharyngite/angine : l'examen qui départageait
  était « → **ECG, test d'effort, coronarographie** » — un bilan coronarien dans
  une station d'**otalgie pédiatrique**. Contamination d'import manifeste : la
  grille ne porte aucun critère cardiologique (`m1`-`m8` sont otoscopie,
  antibiothérapie, conseils aux parents), la section notée `m3` nomme au
  contraire « Test rapide streptocoque si suspicion d'angine associée ». Ligne
  **supprimée**, l'examen resté prisonnier du nom (« Test rapide streptocoque si
  indiqué ») prenant sa place. C'est la seule suppression sèche du lot.
- `annexe-dd` · **German-13**, Colite à *Clostridium difficile* : « → Coloscopie,
  calprotectine fécale » — ce sont les examens de la MICI, chaîne strictement
  identique à celle de l'entrée « Colite ulcéreuse » deux lignes plus haut.
  Même motif que la colite infectieuse de German-19 (lot g4). Remplacé par le
  test qui départage réellement, cf. § 4.
- `annexe-dd` · **German-5**, Hernie discale cervicale avec compression :
  « → Examen clinique, **US si doute** » — l'ultrason n'explore pas le rachis
  cervical. « US si doute » retiré ; l'IRM, prisonnière du nom (« → IRM si
  déficit neurologique »), reprend sa place : « → Examen neurologique, IRM si
  déficit neurologique ».

#### 3. Alignements de niveau 1 — la page SSP tranche, 4 fois

Contrairement au lot g4 (1 sur 10 pages), quatre points ont été tranchés — parce
que quatre de ces pages sont **mono-grille ou quasi** (AVP, Constipation,
Douleur au Poignet, Diarrhée), là où les pages génériques du lot g4 desservaient
jusqu'à 14 grilles.

**Modifications**

- `annexe-dd` · German-5, Fracture vertébrale : « → Radiographie si critères
  présents, CT si complexe » → « → **Imagerie seulement si les règles
  canadiennes du rachis cervical (CCR) ou NEXUS** ne permettent pas la
  clearance ; CT si complexe ».
  source : `SSP — AVP` — « **Rachis cervical** : palpation des épineuses sous
  MILS, **règles canadiennes (CCR)** ou **NEXUS** pour clearance » et
  « Exclure lésion grave par règles canadiennes (CCR) ou NEXUS ; **pas
  d'imagerie systématique** en WAD I-II ».
- `annexe-dd` · German-12, Constipation fonctionnelle : « → Radiographie
  abdominale, coloscopie si alarme » → « → **Critères de Rome IV et échelle de
  Bristol** ; coloscopie si drapeaux rouges ou début après 50 ans ». Même geste
  pour le SII avec constipation (« → Critères de Rome IV (SII-C) ; coloscopie si
  drapeaux rouges ») et pour le Cancer du côlon, dont l'examen diagnostique
  manquait (« → **Coloscopie avec biopsies** ; imagerie (CT/IRM), marqueurs
  tumoraux »).
  source : `SSP — Constipation`, Règle d'or — « Caractériser avec l'**échelle de
  Bristol** et les **critères de Rome IV** (constipation fonctionnelle). […]
  Une constipation d'apparition récente après 50 ans ou avec drapeaux rouges
  impose une **coloscopie** (cancer colorectal) ». La page ne contient **aucune**
  occurrence de « radiographie », et la section notée `m4` n'en nomme pas non
  plus (FSC/CRP, test FIT, US ou CT, coloscopie).
- `annexe-dd` · German-13, Colite à *C. difficile* : « → Coloscopie,
  calprotectine fécale » → « → **GDH + toxines A/B dans les selles (± PCR
  confirmatoire)** ».
  source : `SSP — Diarrhée` — « *C. difficile* : **GDH + toxines A/B** (± PCR
  confirmatoire) si ATB / hospitalisation < 8 sem ».
- `annexe-dd` · German-13, Infections parasitaires chroniques : le nom portait
  « → Examen parasitologique des selles » et l'argument une puce isolée
  « • 3 échantillons » → examen unique « → **Recherche de parasites dans les
  selles × 3 jours consécutifs** ; FSC, CRP, hémocultures si fièvre ».
  source : `SSP — Diarrhée` — « **Recherche de parasites × 3 jours** (lambliase,
  amibiase, cryptosporidies) ».
- `resume` · German-24, Traitement chirurgical : « section du **ligament
  annulaire antérieur** » → « section du **rétinaculum des fléchisseurs** ».
  source : `SSP — Douleur au Poignet` — « le nerf médian passe sous le
  **rétinaculum des fléchisseurs** avec les 9 tendons fléchisseurs » ; la page
  ne contient aucune occurrence de « ligament annulaire ». La section notée `m6`
  dit déjà « Section du rétinaculum des fléchisseurs » : l'alignement de
  niveau 1 supprime du même coup l'écart de vocabulaire avec le niveau 2.

#### 4. Duplication avec la section notée — **aucun cas**

Recherche menée hors outillage, l'angle mort étant structurel
(`report_redundancy.py` ne voit que des blocs, et les sections notées n'en sont
pas). Deux comparaisons systématiques sur les 25 grilles : items d'`annexe-dd`
et de `resume` contre les `criteria-text`/`detail-text` hors bloc (seuil 0.72),
puis les seuls `<div>` d'examen d'`annexe-dd` contre les `detail-text` (seuil
abaissé à 0.62). Les 18 appariements obtenus sont **tous** des recoupements
légitimes de rôle : le critère noté énumère les examens à proposer, `annexe-dd`
en rattache un à une hypothèse précise — « Coloscopie avec biopsies » figure
dans `m4` de German-13 et départage à la fois Crohn, RCH et cancer colorectal,
c'est exactement son emploi. Aucune reprise de l'ordre ni du découpage d'un
corrigé.

C'est un écart net avec le lot g4, qui trouvait le motif **systématique** (sept
réponses « Suivi » recopiant leur critère). L'explication est structurelle : le
motif de g4 vivait dans `presentation`, bloc **absent des 25 grilles de ce lot**.
Sur German, la duplication pédagogique ↔ noté est un risque de `presentation` et
de `resume`, pas d'`annexe-dd`.

Le seul couple relevé — German-24, `resume`/Traitement conservateur face à `m5`
(« Attelle nocturne en position neutre du poignet » ↔ « Port d'attelle nocturne
en position neutre » ; « Antalgiques ± infiltration cortisonée dans le canal
carpien » ↔ « Infiltration de corticoïdes dans le canal carpien ») — est une
**condensation**, pas une copie : `m5` porte six items dans un autre ordre, le
`resume` en retient trois reformulés. Laissé tel quel.

#### 5. Contrat de rôle — aucune violation

Balayage des 25 `annexe-dd` sur les marqueurs de check-list actionnable, de
conduite de station et de registre oral (guillemets, 1ʳᵉ/2ᵉ personne, verbes de
prescription, posologies, « suivi », « contrôle à »). **Deux occurrences**, toutes
deux légitimes : German-2 « → Audiométrie de suivi, dosage médicamenteux » et
German-11 « Médicaments • Benzodiazépines • Opiacés → Révision du traitement » —
cette dernière étant l'examen qui départage une chute iatrogène, conservée
délibérément par le volet B (`prune_dd_filler.py`, table `GENERIC_EXAMS`).
Rien à retirer, rien à porter ailleurs.

**Divergences consignées**

- section notée · **German-5**, `m3` « Justifie l'absence d'imagerie
  immédiate » : le sous-item dit « **Critères d'Ottawa négatifs** ». Les règles
  d'Ottawa portent sur la cheville, le pied et le genou ; la clearance du rachis
  cervical relève des règles canadiennes (CCR) ou de NEXUS. La page
  `SSP — AVP` le dit huit fois et ne contient **aucune** occurrence
  d'« Ottawa » : c'est un niveau 1 caractérisé. **Non corrigé** — la divergence
  est *dans* la section notée, que la procédure gèle (« une divergence repérée
  dans une section notée se consigne, elle ne se corrige pas »). Le pédagogique,
  lui, a été aligné (§ 3). **À arbitrer par vous** : c'est le seul endroit du lot
  où un étudiant peut apprendre une règle de décision fausse, et elle est dans le
  corrigé que lit l'examinateur.
- `annexe-dd` · **German-13**, Maladie cœliaque : « Anticorps
  anti-transglutaminase, anti-**gliadine**, anti-endomysium ». Les anticorps
  anti-gliadine natifs sont abandonnés au profit des anti-peptides désamidés ;
  la page `SSP — Diarrhée` nomme « sérologie (anti-tTG IgA + IgA totales) » sans
  écarter explicitement les anti-gliadine. Ni niveau 1 ni erreur interne
  caractérisée (la formulation reste défendable, seulement datée) → **niveau 3,
  non corrigé**.
- `annexe-dd` · **German-6** : la section notée `m2` énumère 15 diagnostics
  différentiels, `annexe-dd` n'en porte que 6 — manquent notamment les causes
  médicamenteuses, le syndrome de Cushing, l'abus d'alcool chronique et la
  rosacée. Enrichissement possible (le contenu est dans le fichier), **non
  fait** : hors des quatre points de la consigne, et le geste porterait sur dix
  hypothèses à documenter. Signalé.
- `annexe-dd` · **27 noms de diagnostic entre crochets** sur les 485 du corpus,
  dans 6 grilles (14, 21, 22, 72, 80, 83) — « [Trouble des conduites] ». German-14
  en porte 6, German-21 une. Ces crochets ne sont pas une convention de la
  grille (German-14 ne les emploie ailleurs que pour la question du patient en
  `m7`) ; ils ne touchent aucun `.criteria-text` ni aucune `patient-response` et
  ne peuvent donc pas déplacer le barème. Les lots g3 et g4 ne les ont pas
  touchés non plus dans German-22 et German-72. **Non corrigé**, cohérence de
  traitement ; défaut d'import cosmétique à arbitrer sur le corpus entier.
- `resume` · **German-24** : la fiche est cohérente et autonome, sans doublon
  avec la section notée (§ 4). Aucune modification hors l'alignement de
  niveau 1 du § 3.

**Vérifications** — `check_invariants.py` OK (88), `check_nomenclature.py` OK,
`check_reachability.py` OK 88/88 à 100 %, `report_redundancy.py` **14** (inchangé),
AMBOSS aux trois verts et redondance **147**. **Aucune modification du barème** :
`git diff` ne contient aucun `.criteria-text`, aucun `<input>`, aucun
`<span class="score">`, aucun `maxScores`, aucun `sectionInfo` — vérifié
mécaniquement, règle 1 des arbitrages, `baseline.json` non régénéré. Balises
appariées sur les 7 fichiers (`div`, `ul`, `li`, `span`, `strong`),
`boundsAnomalies` et `uncoveredContent` vides. Le diff est symétrique — 36
insertions pour 36 suppressions, aucune ligne créée ni détruite.

`check_no_loss.py deb95f5` : **10 items signalés sur 7 grilles, verdictés un à
un, aucune perte réelle**. Neuf sont l'effet mécanique de la séparation d'un
`<li>` en trois éléments — `list_items()` rendait auparavant le nom, les
arguments et l'examen en une seule chaîne. Le dixième est German-24, où le mot
remplacé est l'alignement lui-même. Chaque fragment conservé a été recontrôlé
par sa présence littérale dans le HTML après `strip_base64` — 89 chaînes
vérifiées, jamais par `grep` — et chacune des cinq suppressions voulues (« US si
doute », « Radiographie abdominale », « Coloscopie, calprotectine fécale »,
« coronarographie », « ligament annulaire ») confirmée absente.
