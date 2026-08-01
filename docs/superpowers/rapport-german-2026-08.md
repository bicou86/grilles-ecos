# Refonte pédagogique des 88 grilles ECOS German — rapport de vérification finale

Branche `refonte-amboss-suisse` · Référence d'origine (outillage en place, avant toute
modification de contenu) : `4819f53` · État vérifié : `32f8875`, sept commits plus loin ·
Journal détaillé : `docs/superpowers/journal-german-2026-08.md` · Procédure :
`scripts/german/PROCEDURE-german.md`

> Ce document est le pendant de `docs/superpowers/rapport-amboss-2026-08.md` pour le
> second corpus. Il en reprend la structure. Tout ce qui n'y est pas redit — la hiérarchie
> à trois niveaux, la règle du format, la règle anti-perte — reste valable tel quel.

---

## 0. Résultat des vérifications

Six vérifications ont été menées sur l'ensemble du corpus, et les quatre vérificateurs
d'AMBOSS rejoués pour établir que la campagne German n'a rien perturbé chez le voisin.
**Cinq passent. Une échoue.**

| # | Vérification | Résultat |
|---|---|---|
| 1 | Les six vérificateurs, sur les deux corpus | **OK** — German : invariants, nomenclature, atteignabilité au vert, `boundsAnomalies` et `uncoveredContent` vides sur les 88. AMBOSS : quatre vérificateurs au vert, redondance **147**, inchangée |
| 2 | Barème inchangé depuis `4819f53` | **OK** — 880 champs recalculés de part et d'autre sur les 88 grilles, **zéro divergence** |
| 3 | Intégrité structurelle | **ÉCHEC partiel** — balises et blocs sains sur 88/88, mais **21 entrées d'`annexe-dd` portent encore le défaut de gabarit** que les lots g5a/b/c ont réparé partout ailleurs. Voir « Le défaut » ci-dessous |
| 4 | Redondance | **OK** — 83 → 14 paires inter-blocs, 638 → 91 intra-bloc. 12 des 14 sont des clés de mnémo, protégées par la règle du format ; les 2 dernières sont des faux positifs de similarité, pas des doublons |
| 5 | Non-perte d'information | **OK** — 652 items signalés, aucune perte réelle retrouvée par l'analyse de motifs, y compris sur les thèmes sensibles |
| 6 | Contrôle fonctionnel en navigateur | **OK** — 88/88 grilles remplies intégralement dans Chrome sans interface : minuteur, score, dénominateur, coloration et absence de balise orpheline |

### Le défaut

**Vingt et une entrées d'`annexe-dd`, dans trois grilles, portent encore l'examen qui
départage à l'intérieur du nom du diagnostic au lieu de son propre élément.** German-27
(9 entrées sur 10), German-34 (9 sur 10), German-56 (3 sur 6).

C'est exactement le défaut d'import que les lots g5a, g5b et g5c ont recherché et réparé
**67 fois** dans les 63 grilles à `annexe-dd` seul. Il produit des hypothèses nommées
« Tendinopathie de la coiffe des rotateurs → Échographie ou IRM » ou « Cancer de
l'œsophage → Endoscopie digestive haute avec biopsies » : le nom du diagnostic et l'examen
qui le confirme sont fusionnés dans le même élément de titre.

**La cause est une chronologie, pas un oubli.** Le motif de recherche juste — *toute flèche
`→` située hors du `<div>` d'examen canonique* — n'a été établi qu'au lot g5a. Les treize
grilles riches avaient été traitées **avant**, aux tâches g3 et g4, avec le motif erroné
que g4 proposait (« `Arguments POUR:` suivi d'un `→` dans la même puce »), lequel ne rend
que 2 cas sur 32. Les lots g5a/b/c ont ensuite balayé, avec le bon motif, **les seules
grilles à `annexe-dd` seul** — leur périmètre. Personne n'est repassé sur les treize
grilles riches. Dix des treize sont indemnes ; trois ne le sont pas.

**Six des vingt et une entrées portent, en plus, une seconde ligne d'examens concurrente**
dans le `<div>` canonique — la configuration que le lot g5b a identifiée comme le meilleur
indicateur d'une erreur de fond, et qui a effectivement livré la plupart des corrections
médicales de la campagne :

| Grille | Examen prisonnier du nom | Examen concurrent dans le `<div>` |
|---|---|---|
| German-27 | Arthrose gléno-humérale → Radiographie standard | → Radiographie, IRM si nécessaire |
| German-27 | Arthrite inflammatoire → Bilan biologique, radiographie | → VS, CRP, facteur rhumatoïde, anti-CCP |
| German-34 | **Cancer de l'œsophage → Endoscopie digestive haute avec biopsies** | **→ Imagerie (CT/IRM), biopsie, marqueurs tumoraux** |
| German-34 | Cancer ORL *(flèche dans les arguments : « • larynx, pharynx → Laryngoscopie, CT ORL »)* | **→ Imagerie (CT/IRM), biopsie, marqueurs tumoraux** |
| German-34 | Achalasie → Manométrie œsophagienne | → Manométrie si l'endoscopie est normale |
| German-34 | AVC, pathologie du tronc cérébral → IRM cérébrale | → CT cérébral, IRM cérébrale |
| German-34 | Sclérose latérale amyotrophique → EMG, consultation neurologique | → IRM cérébrale et médullaire, ponction lombaire |

Quatre de ces couples sont compatibles (le `<div>` précise ou complète le nom). **Deux ne
le sont pas, et ce sont les deux cancers de German-34** : l'examen juste — l'endoscopie
avec biopsies pour l'œsophage, la laryngoscopie pour l'ORL — est prisonnier du nom ou des
arguments, tandis que le `<div>` affiche pour les deux le même « Imagerie (CT/IRM),
biopsie, marqueurs tumoraux ». Ce sont deux des huit occurrences restantes du boilerplate
« marqueurs tumoraux », et le lot g5c a précisément jugé ce boilerplate **faux pour
l'œsophage et l'ORL** (§ 4). Un étudiant qui lit cette entrée voit d'abord une imagerie
là où le geste diagnostique est l'endoscopie.

**Rien n'a été corrigé** : ce rapport est une vérification, pas une passe de traitement.
Le défaut est mesurable en une commande, et le geste de réparation est celui, déjà rodé,
des lots g5a/b/c.

Ce défaut n'a aucune conséquence sur le barème ni sur le rendu de la page : les balises
restent équilibrées, le contrôle fonctionnel passe sur les trois grilles concernées, et le
barème y est identique à `4819f53` champ par champ.

---

## 1. Ce qui a été fait

Les 88 grilles ont été balayées, 80 ont été modifiées. Le travail a porté sur la **zone
pédagogique** — `annexe-dd`, `resume`, `presentation`, `annexe-image` — et jamais sur les
sections notées ni sur les deux blocs de niveau 2 qui y vivent (`therapy`, `redflags`).

### Chiffres

| Mesure | `4819f53` | `32f8875` |
|---|---|---|
| Termes non suisses | **64** | **0** |
| Puces de remplissage « À évaluer cliniquement » | **345** | **0** |
| Examens génériques (« Examens complémentaires selon contexte clinique » et 3 variantes) | **262** | **0** |
| Paires quasi identiques **entre** blocs | **83** | **14** (−83 %) |
| Paires quasi identiques **dans** un même bloc | **638** | **91** (−86 %) |
| Réponses Q/R en liste (`presentation-reponse list`) | **31** | **0** |
| Défauts de gabarit d'`annexe-dd` réparés | — | **67** |
| Boilerplate « marqueurs tumoraux » | 13 | **8** |
| Boilerplate « US si doute » | 4 | **2** |
| Items de contenu, tous blocs | 2 656 | 2 123 |
| Volume rédactionnel | 199 540 c. | 193 009 c. |

Volume de diff : 668 lignes ajoutées, 1 789 supprimées dans `cases/german`, sur 80 fichiers.

Les 8 grilles non modifiées sont celles qui n'avaient rien dans le périmètre : les sept
sans aucun bloc pédagogique (German-38, 39, 70, 73, 84, 86, 87) et German-54, qui ne porte
que des `therapy-section` de niveau 2 et aucun terme de nomenclature à suissifier.

### Ce que cela change pour qui révise

**Le bloc des diagnostics différentiels raisonne au lieu de meubler.** Il portait
345 puces d'argument dont le texte entier était « À évaluer cliniquement » — 59 % de ses
puces — et 262 lignes d'examen qui ne nommaient aucun examen. Elles ont été retirées, pas
remplacées : là où le raisonnement n'existait pas, l'entrée est réduite au nom du
diagnostic, ce qui est une hypothèse à évoquer et non un faux enseignement. Là où le
contenu existait **ailleurs dans le fichier** — les arguments POUR/CONTRE case-appliqués de
la fiche de présentation orale — il a été porté dans le bloc où il a sa place : 38
hypothèses ont ainsi reçu leurs arguments.

**La fiche de révision et la restitution orale ne se recopient plus.** Le couple
`resume ↔ presentation` portait 62 des 83 paires de départ. Il en reste 11, toutes des
clés de mnémo. Le levier n'a presque jamais été la suppression : sur les paires résolues,
la majorité l'a été en rendant à la `presentation` son registre — une réponse parlée au
lieu d'une liste recopiée. Les 31 réponses Q/R écrites en `<ul>` sont tombées à zéro, et le
volume de ce bloc a **augmenté** de 8 300 caractères pendant que son nombre d'items
tombait de 602 à 286 : c'est la signature d'un passage de la liste à la phrase.

**Les mnémos sont sortis de la check-list.** Treize d'entre eux vivaient dans la
« Checklist mentale », dont ils cassaient la fonction de trame. Il n'en reste aucun ;
les trois `mnemo-box` encore hors de la section dédiée (German-56, 69, 88) sont des
légendes SBAR placées sous la version express dont elles expliquent l'acronyme.

**Le vocabulaire est suisse.** 63 `NFS` sont devenues `FSC`, et l'unique valeur en unité
non SI du corpus — l'œstradiol de German-63, `< 50 pg/mL` — a été convertie en
`< 184 pmol/L`. Aucun `mg/dL`, `g/dL`, `ng/mL`, `/mm³`, `/µL`, `CBC`, `BMP`, `911` ni
`SAMU` n'existait dans ce corpus.

**Le barème n'a pas bougé.** Scores maximaux, dénominateurs affichés, nombre de critères
itérés, de sous-items, de boutons et de cases : 880 champs recalculés indépendamment de
part et d'autre de l'historique, sur les 88 grilles, **zéro divergence**. Le nombre de
`criteria-row`, de réponses patient et de règles de notation est lui aussi identique.

---

## 2. Ce qui distingue ce corpus d'AMBOSS

Le patron de traitement d'AMBOSS n'était pas transposable tel quel, et le pilote German-44
a servi à le refaire. Quatre écarts structurels expliquent tout le reste.

### 2.1 Deux blocs manquants font tomber quatre axes du contrat sur sept

`annexe-expert` et `annexe-theorie` : **0 occurrence sur 88 grilles**. Les axes 1, 2, 6
et 7 de `scripts/amboss/PROCEDURE.md` § 3 reposent sur eux et sont **sans objet** — il n'y
a pas de « pourquoi » à garder dans une théorie, pas de fiche expert canonique, pas de
couple expert/résumé à différencier.

**La conséquence est contre-intuitive et vaut d'être dite : la section « Pièges ECOS » de
la présentation orale ne se supprime pas ici, alors qu'elle se supprimait sur AMBOSS.** Sur
AMBOSS l'axe 6 la supprimait parce que le bloc expert portait les pièges canoniques ; ici
c'est le seul bloc de pièges de la grille. Un implémenteur qui aurait transposé l'axe 6
mécaniquement aurait détruit du contenu sur les 13 grilles concernées. Aucune n'a été
supprimée.

### 2.2 Deux blocs de niveau 2 qu'AMBOSS n'a pas, et qui ne cèdent jamais

`therapy-section` (126 segments, 44 grilles) et `redflags-section` (10 segments, 10
grilles) vivent **à l'intérieur** du `criteria-row` de la section notée : ils sont le
corrigé du critère qui les héberge, donc du **niveau 2**. Quand un item pédagogique les
double, c'est le pédagogique qui cède — jamais l'inverse. Ils représentent 25 876
caractères, 13 % du volume rédactionnel, et une transposition naïve de l'outillage
d'AMBOSS ne les aurait pas vus : le `redflags` ne contient ni `<li>` ni puce, ses items
sont des `<div class="redflags-text">`.

### 2.3 L'arbitrage se joue au niveau 2, pas au niveau 1

Sur AMBOSS, la page de référence du vault SSP tranchait couramment. Ici, elle est le plus
souvent muette : la page « SSP — Éruption Cutanée » dessert **14 grilles ECOS** couvrant
psoriasis, acné, pemphigoïde, pityriasis, SJS, syphilis et urticaire, et ne peut trancher
le détail d'aucune. Sur les treize grilles riches, **un seul** point a été tranché par le
niveau 1.

L'autorité réelle de ce corpus est la **section notée** — riche, détaillée, avec les
réponses du patient entre crochets. C'est elle qui a départagé la quasi-totalité des
modifications de fond, y compris chacune des corrections médicales du § 3.

### 2.4 Le levier principal est la conversion de format, pas la suppression

Sur AMBOSS, dédoublonner voulait dire supprimer. Ici, la `presentation` recopie le
`resume` — et parfois la section notée — sous des en-têtes Q/R en listes, ce que la
procédure qualifie explicitement de **non-changement de format**. Le geste juste n'est pas
de supprimer mais de rendre à ce bloc son registre parlé : l'information reste, elle change
de forme. Sur German-44, 7 des 15 paires résolues l'ont été ainsi ; sur les 12 grilles
riches suivantes, 68 réponses ont été converties ou fusionnées contre 13 sous-sections
supprimées.

Conséquence sur la mesure : **la redondance inter-blocs est un indicateur peu sensible pour
ce corpus.** 63 des 88 grilles n'ont qu'`annexe-dd` pour tout bloc et ne peuvent former
aucune paire inter-blocs. Le volet qui a retiré 607 éléments n'a fait bouger le chiffre de
référence que de 83 à 82 — pendant que l'intra-bloc s'effondrait de 638 à 118. Sur German,
c'est l'intra-bloc qu'il faut lire.

---

## 3. Les erreurs médicales trouvées

Toutes sont **préexistantes** : elles étaient dans les grilles avant la campagne. Elles
vivaient dans un bloc pédagogique, donc elles ont pu être corrigées ; celles qui vivent
dans une section notée sont au § 4, consignées et intactes.

### A. Le motif dominant — une chaîne d'examens copiée d'une entrée voisine et posée sur le mauvais diagnostic

**C'est le mécanisme d'erreur central de ce corpus, et il mérite d'être nommé, parce qu'il
se reconnaît sans connaissance clinique.** L'import qui a produit les grilles a dupliqué
des lignes « → examens » d'une entrée à l'autre, parfois à l'intérieur de la même liste,
parfois d'une grille à l'autre. À la source la chaîne est juste ; à destination elle est
fausse — et elle est fausse **de façon invisible**, parce qu'elle a l'air d'un vrai
protocole. La signature mécanique est une chaîne strictement identique sous deux
diagnostics sans rapport, et le meilleur indicateur est la **coexistence de deux lignes
d'examens** dans la même entrée.

| Grille | Le diagnostic | Ce qu'on lui faisait faire | D'où venait la chaîne |
|---|---|---|---|
| German-55 (ictère) | Lithiase **biliaire**/cholédocienne | « → CT abdominal sans contraste, US rénal » | mot pour mot la chaîne de la lithiase **urinaire** de German-51. Une modalité choisie pour voir un calcul rénal, sur un obstacle biliaire qu'elle ne montrera pas |
| German-31 (douleur thoracique) | Syndrome coronarien **aigu** | « → ECG, troponines, **test d'effort** » | la chaîne du syndrome coronarien **chronique**, telle quelle en German-33. **L'épreuve d'effort est contre-indiquée dans un SCA** |
| German-46 (fatigue) | Anémie **hémolytique** auto-immune | « → FSC, ferritine, B12, folates » | la chaîne des trois entrées d'anémie **carentielle** de la même grille. Un bilan carentiel ne dit rien d'une hémolyse |
| German-71 (polyurie) | Diabète **insipide** | « → Glycémie à jeun, HbA1c » | l'entrée « Diabète **sucré** », quatre lignes plus haut dans la même liste. C'est l'examen qui **exclut** le diagnostic par définition : la glycémie y est normale |
| German-28 (otalgie, **pédiatrie**) | Pharyngite/angine | « → **ECG, test d'effort, coronarographie** » | un bilan coronarien complet dans une station d'otalgie de l'enfant. La grille ne porte aucun critère cardiologique |
| German-79 (**consultation téléphonique**, 21 h, fillette de 5 ans) | Crise d'asthme | « → **Spirométrie avec test de réversibilité, peak flow** » | la chaîne de l'asthme **chronique** de German-36 et 78. Ni faisable au téléphone, ni interprétable en crise, ni praticable à 5 ans |
| German-19 (douleur abdominale) | Colite **infectieuse** post-voyage | « → Coloscopie, calprotectine fécale » | les examens de la **MICI** |
| German-13 (diarrhée) | Colite à *C. difficile* | « → Coloscopie, calprotectine fécale » | l'entrée « Colite ulcéreuse », deux lignes plus haut |
| German-85 (**pédiatrie**) | Diabète sucré décompensé | « → Glycémie **à jeun**, HbA1c » en concurrence avec « → Glycémie, glycosurie » | la chaîne du dépistage du diabète chronique. Chez un enfant qui vomit et se déshydrate, mettre à jeun est exactement ce qu'il ne faut pas faire |
| German-40, 51, 71 | Infection urinaire | « → FSC, CRP, hémocultures si fièvre » (3 exemplaires) | la chaîne d'un sepsis, là où la bandelette et l'ECBU font le diagnostic |

Deux traits se répètent : **les stations pédiatriques héritent de protocoles d'adulte**
(German-28, 79, 85), et **les paires de diagnostics homonymes se contaminent**
(sucré/insipide, biliaire/urinaire, aigu/chronique, carentielle/hémolytique).

### B. Un examen que l'organe ne permet pas

| Grille | Ligne fausse | Pourquoi |
|---|---|---|
| German-5 | Hernie discale cervicale → « Examen clinique, **US si doute** » | l'ultrason n'explore pas le rachis cervical |
| German-33 | Hernie hiatale → « Examen clinique, **US si doute** » | même chaîne, même défaut |
| German-77 | Abcès pulmonaire → « **US** ou CT selon localisation, **ponction** » | l'ultrason ne traverse pas le poumon aéré ; « selon localisation » + « ponction » est le protocole d'un abcès des parties molles |
| German-75 | Néoplasie pulmonaire → « Imagerie (CT/**IRM**), biopsie, marqueurs tumoraux » | l'IRM n'explore pas le parenchyme pulmonaire |

### C. Un boilerplate posé sans discernement

« **Marqueurs tumoraux** » figurait à l'identique sous des diagnostics sans rapport :
cancer de l'œsophage, tumeur cérébrale, tumeur des tissus mous, néoplasie pulmonaire. Il a
été retiré là où l'organe n'a pas de marqueur utile (German-33, 41, 49, 75). **Il ne se
retire pas en masse** — voir § 4.

« **PSA, toucher rectal** » sous une prostatite aiguë (German-37) : le PSA y est
faussement élevé et n'a pas de valeur diagnostique. Retiré, sur une page de référence qui
ne contient aucune occurrence du terme.

### D. Un examen incomplet là où l'incomplétude change la conduite

| Grille | Ce qui manquait |
|---|---|
| German-46 | Saignement digestif occulte : gastroscopie seule, alors que l'entrée elle-même cite les MICI. **Coloscopie** ajoutée, avec le test *H. pylori* |
| German-51 | Infection urinaire sans **ECBU** |
| German-49 | Adénopathie dans une station de hernie inguinale, explorée par « FSC, CRP, ECBU, hémocultures » : l'**échographie inguinale**, que la section notée cote, était absente |

### E. Vocabulaire et référentiels périmés, tranchés par la page de référence

German-24 : « ligament annulaire antérieur » → **rétinaculum des fléchisseurs**, le terme
qu'employait déjà la section notée. German-12 : la radiographie abdominale, absente de la
page de référence, remplacée par **Rome IV + Bristol**. German-13 : *C. difficile* par
**GDH + toxines A/B (± PCR)** et recherche de parasites **sur trois jours consécutifs**.
German-5 : la clearance du rachis cervical par les **règles canadiennes ou NEXUS**.

---

## 4. Ce qui reste non corrigé, et pourquoi

### 4.1 Les huit « marqueurs tumoraux » restants — un arbitrage organe par organe

Le lot g5b avait transmis « marqueurs tumoraux » comme un boilerplate **faux à chaque
occurrence**, avec consigne de le rechercher. Le lot g5c a établi que **la généralisation
est trop large** :

- German-18, « US pelvienne, marqueurs tumoraux si suspecte » sur une masse ovarienne :
  le CA-125 **est** l'examen standard de cette situation ;
- German-12 et 13, cancer colorectal : l'**ACE** fait partie du bilan initial.

Le boilerplate est faux quand l'organe n'a pas de marqueur utile — poumon, cerveau, tissus
mous, œsophage, ORL. Il reste **8 occurrences dans 6 grilles** (German-12, 13, 18, 21 ×2,
29, 34 ×2). Deux d'entre elles sont celles de German-34 signalées au § 0 : elles doublent
un examen juste prisonnier du nom du diagnostic. **Une passe globale les retirerait toutes,
y compris les trois qui sont justes.**

### 4.2 German-75 — la station porte une tuberculose, son bloc de différentiels ne la porte pas

La station est une tuberculose pulmonaire (infirmière de 34 ans, toux de six semaines) et
la section notée lui consacre cinq critères. Mesure faite : le mot apparaît **12 fois dans
la grille et 0 fois dans `annexe-dd`**, dont les cinq hypothèses sont asthme allergique,
reflux, bronchite chronique, néoplasie pulmonaire et sarcoïdose. C'est l'écart le plus
visible du corpus pour un étudiant. L'enrichir ne demanderait aucune invention — le contenu
est dans le fichier — mais c'est un **ajout d'hypothèse**, hors du périmètre des lots.
German-6 est dans le même cas : la section notée y énumère quinze différentiels, le bloc
en porte six.

### 4.3 German-5 — une règle de décision fausse, dans le corrigé que lit l'examinateur

La section notée `m3` dit « **Critères d'Ottawa négatifs** » pour justifier l'absence
d'imagerie cervicale. Les règles d'Ottawa portent sur la cheville, le pied et le genou ; la
clearance du rachis cervical relève des règles canadiennes ou de NEXUS, que la page de
référence nomme huit fois sans jamais écrire « Ottawa ». **La divergence est *dans* la
section notée, que la procédure gèle.** Le versant pédagogique, lui, a été aligné : la
grille porte aujourd'hui les deux formulations, la fausse dans le corrigé et la juste dans
le bloc de révision. C'est le seul endroit du corpus où un étudiant peut apprendre une
règle de décision fausse.

### 4.4 Les divergences de sections notées, consignées

- **German-51 `m3`** : « PSA (si homme > 50 ans) » dans une station d'hématurie.
  Défendable — et signalé pour cohérence avec le retrait du PSA en German-37, où le
  contexte de prostatite aiguë est différent.
- **German-56** : le mnémo DAME repose sur « **A = Argenturie** », mot qui n'existe pas ;
  le terme est *urgenturie*. Corriger la coquille casse la clé du mnémo, ce que la
  procédure interdit. **C'est le seul endroit du corpus où un étudiant peut apprendre un
  mot faux.**
- **German-27** : la section notée cote le test de Jobe « moins de force, douloureux »
  quand la version longue dit « pas de perte de force nette ». La rupture de coiffe ne peut
  pas être formellement écartée chez cette patiente de 60 ans ; **aucun argument CONTRE
  n'a donc été écrit pour elle**, le diagnostic reste ouvert.
- **German-44** : le corrigé du critère « signes d'alerte » est vide (« 2. Signes
  d'alerte »). Le remplir, c'est écrire le corrigé à la place de l'auteur.

### 4.5 Les autres points laissés ouverts

- **2 « US si doute » résiduelles** (German-15, 21), à juger sur l'organe comme les
  marqueurs tumoraux.
- **Des noms de diagnostic entre crochets** — 27 relevés dans German-14, 21, 22, 72, 80 et
  83 — résidu d'import cosmétique, sans effet sur le barème (ni `.criteria-text`, ni
  réponse patient). À trancher sur le corpus entier plutôt que grille par grille.
- **Deux doublons d'intitulé** : « Angor stable » / « Syndrome coronarien chronique » dans
  German-33, « Syncope vasovagale » / « Syncope réflexe » dans German-61. Deux noms du même
  tableau dans la même liste — pas une erreur factuelle.
- **German-36** : l'entrée « Bronchectasies » n'a aucun examen qui départage, alors que
  seul le CT thoracique haute résolution tranche. Forme voulue par le volet B, non remplie.
- **145 entrées d'`annexe-dd` sur 485 sont aujourd'hui un nom de diagnostic nu**, sans
  argument ni examen — 127 l'étaient au sortir du retrait du remplissage. C'est l'arbitrage
  demandé, mais sur ces entrées le bloc n'enseigne plus que *quoi évoquer*, pas *comment
  trancher*. Elles sont identifiables mécaniquement — un `<li>` sans aucun `<div>` ni
  flèche — et ce sont elles qui mériteraient un enrichissement médical en premier.
- **L'anomalie structurelle de German-84** : le `criteria-row` du critère `m7` englobe les
  quatre `criteria-row` suivants, un `</div>` manquant localement et compensé plus loin.
  Seule grille du corpus dans ce cas sur 3 072 `criteria-row`. **Vérifiée inchangée depuis
  `4819f53`**, et sans conséquence : le fichier reste équilibré, le barème est identique, et
  la grille atteint 100 % sur ses quatre sections au contrôle en navigateur.

---

## 5. Ce que la campagne a appris sur la méthode

### 5.1 Trois corrections de patron en cours de route — et la dernière n'a pas été appliquée

**Le patron s'est corrigé trois fois, chaque fois parce qu'un lot a rencontré ce que le
précédent n'avait pas vu.** C'est le même constat que sur AMBOSS : aucun garde-fou n'a été
conçu à l'avance.

| Correction | Ce qui l'a motivée | Portée |
|---|---|---|
| **Le motif de recherche du défaut de structure était faux** | g4 proposait de chercher « `Arguments POUR:` suivi d'un `→` dans la même puce ». Ce motif rend **2 cas sur 32**. Le motif juste est *toute flèche hors du `<div>` d'examen canonique* | Établi par g5a, appliqué par g5b et g5c — mais **jamais rejoué sur les grilles traitées avant lui** : c'est l'origine du défaut du § 0 |
| **La consigne « marqueurs tumoraux » était trop large** | g5b la transmettait comme « faux à chaque occurrence ». g5c a établi que le CA-125 sur une masse ovarienne et l'ACE sur un cancer colorectal sont justes | Corrigée avant qu'un lot ne fasse une passe globale destructrice |
| **La propriété « tout ou rien » ne tient pas** | g5b observait que les grilles atteintes le sont sur la **totalité** de leurs entrées (7/7, 6/6, 8/8, 10/10) et en concluait qu'une seule entrée suffit à qualifier une grille. g5c a trouvé German-85 atteinte sur **4 de ses 5** entrées | Le raccourci reste bon pour *détecter* une grille atteinte, il ne l'est pas pour *dimensionner* la réparation |

**Une quatrième leçon découle du § 0 : une correction de patron doit s'accompagner d'un
rejeu sur ce qui a déjà été traité.** Les trois corrections ci-dessus ont toutes été
transmises au lot suivant ; aucune n'a été rejouée en arrière. C'est mécaniquement ce qui
laisse 21 défauts dans German-27, 34 et 56.

### 5.2 Un indicateur découvert : le rendement du niveau 1 se prédit sans ouvrir la page

Le lot g5a a remarqué que les pages de référence qui **tranchent** sont celles qui
desservent peu de grilles, et que les pages muettes en desservent beaucoup. Le relevé des
lots g5a, g5b et g5c tient sur toute la campagne :

| | Nombre de grilles ECOS desservies par la page |
|---|---|
| Pages qui ont tranché | 1, 2, 5, 6, 9 |
| Pages muettes | 14, 16, 19, 24, 26, 27 |

Le nombre de grilles desservies est lisible dans `docs/obsidian-mapping.yaml` **sans ouvrir
une seule page**, ce qui en fait un critère de tri directement utilisable. Il a
correctement trié les lectures de g5b : 4 pages lues sur 12 possibles, 3 rendements.

**Deux limites l'encadrent, et elles vont en sens inverse.**

- *Le nombre de grilles desservies prédit la précision d'une page, pas sa pertinence.*
  « SSP — Ballonnement » ne dessert que German-49 et reste pourtant muette : la station
  porte sur une hernie inguinale. Un mapping mono-grille peut être un mapping par défaut —
  et il peut aussi n'être qu'un point d'entrée : « SSP — Pollakiurie » ne donnait pas le
  bilan du diabète insipide, mais elle nommait la page qui le donne. Suivre les « Skills
  connexes » d'une page mono-grille est un geste rentable.
- *L'indicateur prédit le rendement en prescriptions, pas en réfutations.* « SSP — Toux
  Chronique » dessert 19 grilles et a pourtant tranché le point « marqueurs tumoraux » de
  German-75 — par une **absence mesurable** (zéro occurrence du terme, alors que la page
  détaille par ailleurs le bilan d'un cancer bronchique). Une page à forte cardinalité
  reste utile pour infirmer un examen. **Et une réfutation vaut une correction.**

### 5.3 Ce que l'outillage voit, et ce qu'il ne voit pas

- **Le rapport de non-perte sur-signale mécaniquement la conversion liste → narration**,
  qui est justement le levier principal de ce corpus. Le rapport de bruit s'inverse selon
  le geste : 0 perte réelle sur 235 signalements pour les grilles riches (conversion de
  format), mais 7 suppressions voulues sur 8 signalements pour un lot de réparations
  structurelles. Le script ne se lit pas de la même façon d'un lot à l'autre.
- **Le silence du script peut être une information positive.** Le remplacement de la
  chaîne du diabète insipide en German-71 n'a **pas** été signalé, parce que l'ancienne
  chaîne s'apparie encore à celle de « Diabète sucré » restée dans la grille. Ce silence
  est la preuve mécanique de la duplication qui motivait la correction.
- **La duplication entre le pédagogique et la section notée est invisible au rapport de
  redondance**, par construction : les sections notées ne sont pas des blocs. Elle se
  cherche à l'œil. Trois lots l'ont établi : c'est un risque de `resume` et de
  `presentation` — sept réponses « Suivi » recopiaient mot pour mot le corrigé de leur
  critère — et **pas d'`annexe-dd`**, où 36 appariements relevés sur les 63 grilles à
  `annexe-dd` seul se sont tous révélés être des recoupements légitimes de rôle.
- **Le seuil de longueur de l'extracteur d'items masque une vingtaine de puces réelles**
  devenues isolées après le retrait du remplissage. Elles existent dans les fichiers, mais
  aucune mesure du projet ne les voit — ni la redondance, ni la non-perte.
- **Un contrôle de couverture rend la revue de fond démontrable.** Résidu des entrées après
  retrait du nom, de l'élément d'examen et de l'élément d'arguments : **zéro caractère** sur
  les grilles auditées. C'est ce qui autorise à dire qu'une revue est exhaustive et non un
  sondage — sans lire une seule grille en entier.
- **Rien de tout cela n'établit qu'un contenu clinique est juste.** Les scripts établissent
  que le barème est atteignable et inchangé, que les fichiers sont sains, que rien n'a
  disparu sans trace et que le vocabulaire est suisse. La justesse médicale des corrections
  du § 3 relève d'une relecture par un médecin.

---

## 6. Le détail des six vérifications

### 6.1 Les six vérificateurs, sur les deux corpus

| Corpus | Commande | Résultat |
|---|---|---|
| German | `check_invariants.py` | **OK** — 88 grilles, 8 champs gelés, `boundsAnomalies` et `uncoveredContent` vides, code 0 |
| German | `check_nomenclature.py` | **OK** — aucun terme non suisse, code 0 |
| German | `check_reachability.py` | **OK** — 88 grilles, barème atteignable à 100 % sur chaque section, code 0 |
| German | `report_redundancy.py` | 14 paires inter-blocs |
| German | `report_redundancy.py --intra` | + 91 paires intra-bloc |
| German | `check_no_loss.py 4819f53` | 652 items signalés sur 80 grilles, rapport, code 0 |
| AMBOSS | `check_invariants.py` | **OK** — 40 grilles, code 0 |
| AMBOSS | `check_nomenclature.py` | **OK**, code 0 |
| AMBOSS | `check_reachability.py` | **OK** — 40 grilles à 100 %, code 0 |
| AMBOSS | `report_redundancy.py` | **147 paires — inchangé** |

`scripts/amboss/` n'a été modifié par aucun commit de la campagne. C'est vérifiable par
construction : l'outillage German **importe** les primitives de texte d'AMBOSS au lieu de
les recopier, de sorte qu'il n'existe qu'une seule implémentation du correctif du chevron
nu, du filtrage base64 et du découpage par puces.

`baseline.json` est **identique** à ce qu'il était au commit `4819f53` : il n'a jamais été
régénéré, donc la comparaison d'invariants porte bien sur l'état d'avant campagne.

### 6.2 Barème inchangé — 880 champs, zéro divergence

Recalcul indépendant de `baseline.json`, en relisant chaque grille à `4819f53` par
`git show` : `maxScores`, `<span class="score">`, `sectionInfo[].count`, `criteriaCount`,
`detailCount`, `radioCount`, `checkboxCount`, plus trois champs ajoutés pour l'occasion
(`criteria-row`, `patient-response`, règles de notation). 88 grilles de part et d'autre,
aucune disparue, aucune apparue. **Aucune divergence.**

C'était la seule attente possible : aucune tâche de la campagne n'a déclaré toucher au
barème, et chacune a vérifié mécaniquement que son diff ne contenait ni `.criteria-text`,
ni `<input>`, ni `<span class="score">`, ni `maxScores`, ni `sectionInfo`.

### 6.3 Intégrité structurelle

| Contrôle | Résultat |
|---|---|
| Balises appariées | `div` 63 085/63 085 · `ul` 368/368 · `li` 1 413/1 413 · `p` 310/310 · `span` 6 646/6 646 |
| Fermeture avant ouverture | aucune, sur aucun des cinq types |
| `</html>` final | **88/88** |
| Blocs attendus (`caseConfig`, `criteria-row`, `maxScores`, marqueur de fin de zone pédagogique) | **88/88** |
| Nombre de segments par bloc, contre `4819f53` | identique — aucun bloc créé ni supprimé |
| `criteria-row` équilibrés | 3 072/3 072 |
| `criteria-row` en englobant d'autres | **1** — German-84 `m7`, englobe 4. **Mesuré identique à `4819f53`** |
| Défaut de gabarit d'`annexe-dd` | **21 occurrences résiduelles** — German-27, 34, 56. Voir § 0 |

### 6.4 Redondance

**Inter-blocs : 83 → 14.** Les 14 ont été localisées une par une dans le HTML.

- **12 sont des clés de mnémo**, toutes dans une `mnemo-box` de la section « Touches
  ludiques / mnémos » : German-15 (DIVERTI, clé `I`), 19 (MICI, `C` ×2), 27 (ARC, `A` ×2 et
  `R`), 34 (ALARME, `E`), 44 (LUPUS, `S`, dont une face au bloc `redflags`), 56 (4R,
  `Rééducation`), 72 (GROWTH, `R`), 88 (PRURIT, `Rougeur`). La règle du format les protège :
  un mnémo n'est ni une liste ni une narration, et supprimer le mot d'origine casse la clé.
- **2 ne sont pas des clés de mnémo, et ne sont pas non plus des doublons.** German-68,
  couple `annexe-dd ↔ therapy` : « installation progressive » (l'installation graduelle
  d'une presbyacousie, argument du différentiel) face à « essai et adaptation progressive »
  (l'adaptation progressive d'un appareil auditif, geste thérapeutique). Deux contenus sans
  rapport, appariés à 0,73 par leur ressemblance de chaîne. **Ce sont des faux positifs de
  la mesure**, et le seul point du corpus où l'affirmation « les 14 restantes sont toutes
  des clés de mnémo » est inexacte. Aucune action n'est requise ; le fait est signalé pour
  que le chiffre 14 ne soit pas lu comme 14 mnémos.

**Intra-bloc : 638 → 118 après le retrait du remplissage → 91 aujourd'hui.** L'effondrement
initial (−81 %) est l'effet réel du volet de suppression, invisible sur le chiffre
inter-blocs qui ne bougeait que de 83 à 82. La suite est plus fine : `presentation` tombe
de 37 à 5 (conversion de format), `resume` de 21 à 19, tandis qu'`annexe-dd` **remonte** de
59 à 66 — l'ajout des arguments POUR/CONTRE et la sortie des examens hors du nom créent des
items courts qui se ressemblent. Le chiffre intra-bloc mesure, il ne prescrit pas.

### 6.5 Non-perte d'information

`check_no_loss.py 4819f53` signale **652 items sur 80 grilles**. Le volume est attendu : la
campagne a retiré 345 puces de remplissage et 262 examens génériques, et converti des
dizaines de listes en narration — un item converti « change de forme », il ne disparaît pas,
mais l'extracteur ne sait pas le suivre.

L'analyse a porté sur des **motifs**, pas sur un verdict item par item.

| Contrôle | Résultat |
|---|---|
| Volume par grille | médiane 6, moyenne 8,9, maximum 40. Les deux seules grilles au-delà du seuil d'attention (German-48 : 40 · German-34 : 33) sont des grilles riches où la conversion liste → narration a été massive. **Aucune grille au volume anormal hors de la population attendue** |
| Items dont le résidu, une fois les formulations de remplissage retirées, est **vide** | 209 — l'item disparu *était* le remplissage |
| Items dont **tous** les mots significatifs se retrouvent dans le texte visible actuel de la même grille | **565 sur 652 (87 %)** |
| Items ayant perdu au moins un mot significatif | 87, concentrés sur les 13 grilles riches et sur les grilles où une chaîne d'examens fausse a été retirée |
| Thèmes sensibles (contre-indication, dose, drapeau rouge, protection du patient) | 23 items relevés, **tous retrouvés reformulés** dans le fichier actuel |

Les items sensibles ont été recontrôlés un par un par extraction du contexte courant, jamais
par recherche brute. Trois exemples, représentatifs des trois formes de reformulation :

- German-48, « consulter en urgence si convulsions, déshydratation, altération de
  conscience » → devenu, au registre parlé, « je les reverrais dans 3 à 4 jours si la fièvre
  persiste, **en urgence en revanche devant une somnolence excessive, une convulsion, un
  refus de boire** », et conservé en liste dans le corrigé du critère « signes d'alarme à
  expliquer ».
- German-88, « orientation ophtalmologique si photophobie, baisse visuelle, douleur » →
  présent **deux fois**, en liste (« avis ophtalmologique si doute diagnostique,
  photophobie, douleur ou forme résistante ») et à l'oral (« je l'adresserais à
  l'ophtalmologue devant une baisse d'acuité visuelle, une douleur oculaire importante, une
  photophobie marquée »).
- German-43, « informer les parents des complications tardives (RAA, GNA post-strepto) » →
  « dépistage des complications tardives : glomérulonéphrite, RAA » dans le corrigé du
  critère d'information aux parents.

Les 87 items à mot perdu recouvrent, pour la moitié, **les suppressions voulues du § 3** :
le test d'effort de German-28 et 31, les marqueurs tumoraux de German-33, 41, 49 et 75, la
spirométrie de German-79, le « à jeun » de German-85, le CT sans contraste de German-55.
**Leur disparition est le résultat recherché.**

### 6.6 Contrôle fonctionnel en navigateur

Mené sur les **88 grilles**, dans Chrome sans interface piloté par le protocole DevTools
(aucun paquet installé, aucune connexion hors de la boucle locale). Pour chaque grille :
passage en mode examen, démarrage du minuteur, mesure de sa progression, retour en mode
révision, remplissage intégral — toutes les cases cochées, tous les boutons au maximum,
communication au meilleur niveau — puis lecture de l'affichage réel.

| Contrôle | Résultat |
|---|---|
| Chargement sans exception ni erreur de console | **88/88** |
| Minuteur : démarre, affiche « En cours », décompte (13:00 → 12:57 en 3 s) | **88/88** |
| Score de chaque section = dénominateur affiché | **88/88** — 352 sections, aucune en écart |
| Total global | **100 %**, note **A** — **88/88** |
| Réponses entre crochets colorées en `rgb(44, 90, 160)` | **4 227 crochets, 4 227 colorés** |
| Balise orpheline visible dans le texte rendu | **aucune** |

Les trois grilles qui portent le défaut de gabarit du § 0 passent le contrôle : le défaut
est un problème de lisibilité pédagogique, pas de rendu. German-84, avec son `criteria-row`
englobant, atteint elle aussi 100 % sur ses quatre sections — le défaut est cosmétique dans
le DOM et n'entre pas dans la boucle de calcul.

---

## Annexe — comment reproduire les vérifications

```bash
python3 scripts/german/check_invariants.py         # OK — 88 grilles, code 0
python3 scripts/german/check_nomenclature.py       # OK — aucun terme non suisse, code 0
python3 scripts/german/check_reachability.py       # OK — 88 grilles à 100 %, code 0
python3 scripts/german/report_redundancy.py        # TOTAL : 14 paire(s)
python3 scripts/german/report_redundancy.py --intra  # + 91 paire(s) intra-bloc
python3 scripts/german/check_no_loss.py 4819f53    # rapport, code 0 en toutes circonstances

python3 scripts/amboss/check_invariants.py         # OK — 40 grilles, code 0
python3 scripts/amboss/check_nomenclature.py       # OK, code 0
python3 scripts/amboss/check_reachability.py       # OK — 40 grilles à 100 %, code 0
python3 scripts/amboss/report_redundancy.py        # TOTAL : 147 paire(s)
```

Les trois premiers de chaque corpus sortent en erreur si un écart apparaît : ce sont des
portes. Les deux rapports listent sans juger et sortent toujours 0.

**Le défaut du § 0 se retrouve en une commande**, qui cherche toute flèche située hors de
l'élément d'examen canonique d'`annexe-dd` :

```bash
python3 -c "
import re, sys; sys.path.insert(0,'scripts/german'); import lib_german as lib
EX = re.compile(r'<div style=\"[^\"]*rgb\(52, 105, 46\)[^\"]*\">.*?</div>', re.S)
for p in sorted(lib.grids(), key=lib.grid_num):
    h = lib.strip_base64(p.read_text(encoding='utf-8'))
    n = sum(EX.sub(' ', s).count('→') for s in lib.block_segments(h, 'annexe-dd'))
    if n: print(f'{n:3d}  {p.name}')
"
```

Il rend aujourd'hui 25 occurrences : les **21 du défaut** (German-27, 34, 56) et **4
flèches sémantiques légitimes** (German-65, 66), qui emploient la flèche au sens « ce signe
oriente vers ce diagnostic » dans des catégories qui listent des signes et non des
hypothèses. Le motif doit être lu avec la catégorie qui le porte.

L'intégrité structurelle, la comparaison du barème avec `4819f53`, l'analyse par motifs du
rapport de non-perte et le contrôle fonctionnel en navigateur sont menés par des scripts
d'audit ponctuels, non versionnés — recalcul indépendant des deux côtés de l'historique
pour le barème, pilotage direct de Chrome par le protocole DevTools pour le contrôle
fonctionnel.
