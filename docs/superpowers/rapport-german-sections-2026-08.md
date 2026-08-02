# Les sections pédagogiques du corpus German — rapport de vérification finale

**2026-08-02** · branche `refonte-amboss-suisse` · 88 grilles, `cases/german/`

Ce document rend compte du chantier qui a doté les 88 grilles ECOS du corpus
German d'un appareil pédagogique complet, et de la vérification indépendante
menée à son terme. Il est écrit pour être lu sans avoir suivi le détail des
lots.

---

## 1. Verdict

Les six vérifications demandées ont été rejouées de bout en bout, sans
s'appuyer sur les chiffres publiés par les lots.

| # | Vérification | Résultat |
|---|---|---|
| 1 | Vérificateurs sur les trois corpus | **vert** — AMBOSS 40, German 88, RESCOS 41, aux quatre contrôles ; 203 images, 0 lien cassé, 0 orpheline |
| 2 | Barème gelé depuis `4819f53` | **vert** — **0 écart** sur les 88 grilles, sur les sept champs du barème |
| 3 | Comptage transversal de gabarit sur les 88 | **2 défauts** — 8 spans imbriqués ; 1 image partagée à tort |
| 4 | Redondance | **vert** — 16 paires, toutes justifiées ; +2 seulement depuis l'avant-chantier, sur la grille pilote |
| 5 | Images | **1 réserve** — aucun lien cassé, aucune orpheline, aucun dépassement du plafond par image ; **5 grilles au-dessus du budget de 700 Ko par grille** |
| 6 | Contrôle visuel | **vert** — 40 rendus, 10 grilles × 2 thèmes × 2 largeurs, 0 image cassée, 0 débordement |

### Les défauts trouvés

**a) Huit spans de balisage imbriqués les uns dans les autres — German-27 (2) et
German-73 (6).** Un terme se retrouve bicolore : dans German-73, « grossesse
extra-utérine » est balisé en rouge (pathologie) mais le mot « grossesse » porte
à l'intérieur un second balisage rose (symptôme). Au navigateur, le lecteur voit
« *grossesse* » en rose suivi de « *extra-utérine* » en rouge — dans les deux
thèmes, vérifié par sonde sur les couleurs calculées. Six occurrences du même
terme dans German-73, deux dans German-27 (`c-red` imbriqué dans `c-blue`).
C'est la dette annoncée par le dernier lot : l'outil de balisage employé jusqu'à
German-79 repassait sur le texte déjà balisé, et l'assertion d'équilibre ne
voyait rien, un span imbriqué restant équilibré. **Aucun balayage n'avait été
fait ; il l'est ici, et le corpus n'en porte que ces huit.**

**b) German-48 et German-84 portent la même image alors qu'elles dépendent de la
même page SSP.** `pedia-convulsions-febriles-simples-vs-complexes.jpg` figure
dans les deux planches, et les deux grilles sont rattachées à
« SSP — Fièvre du Nourrisson ». La règle de sélection interdit exactement cela :
deux grilles d'une même page ne portent pas la même sélection, **à la seule
exception du message-clé** — et cette image n'en est pas un. C'est le contrôle
que la procédure désigne elle-même comme « le plus utile » de sa règle
d'iconographie, et le seul cas où il tombe. Les onze autres images partagées du
corpus sont, elles, régulières : trois sont des message-clés partagés par deux
grilles d'une même page (German-53/54, 46/47, 57/58), les huit autres sont
partagées entre grilles de **pages différentes**, ce que la règle n'interdit pas
et que la déduplication rend souhaitable.

**c) Cinq grilles dépassent le budget de 700 Ko d'images par grille.**
German-72 (1 049 Ko), German-42 (838), German-27 (833), German-66 (804),
German-70 (724). Pour German-42 et German-27, le dépassement tient entièrement
au message-clé, que la règle rend obligatoire et exempte de plafond *par image* —
mais aucune exemption n'a jamais été écrite pour le budget *par grille*, et le
conflit entre les deux règles n'a pas été tranché. Pour German-72, German-66 et
German-70, il n'y a pas de message-clé : le dépassement vient de trois images
ordinaires, chacune sous le plafond de 600 Ko.

**d) German-68 reste le seul écart de gabarit de la planche d'images.** Elle
porte deux `annexe-item` là où les 82 autres grilles imagées n'en portent qu'un,
et cinq images là où le plafond est de quatre. C'est l'état d'import, antérieur
au chantier et documenté comme tel ; le chantier ne l'a pas aggravé mais ne l'a
pas résorbé.

### Quatre corrections documentaires

La vérification a mesuré à neuf des grandeurs que les rapports de lot
publiaient. Quatre chiffres ne tiennent pas ; les grilles ne sont pas en cause,
seulement leur compte rendu.

1. **La densité de balisage a été sur-déclarée par deux lots.** Le corpus porte
   **22 621 spans dans 215 355 mots**, soit **1 span pour 9,5 mots** — chiffre
   obtenu deux fois par deux chemins indépendants. La somme des chiffres publiés
   par les lots donnerait 37 705 spans, soit 67 % de plus que le corpus n'en
   contient. Les écarts sont localisés : le lot des grilles 2 à 30 a publié
   16 180 spans / 143 655 mots là où la mesure en donne 6 773 / 66 323 ; le lot
   des grilles 31 à 52 a publié 9 571 / 90 892 là où la mesure en donne
   3 894 / 40 353. Les cinq autres lots concordent au mot près. Les **densités**
   publiées, elles, restent proches du vrai (1/8,9 et 1/9,5 contre 1/9,8 et
   1/10,4 mesurés) : l'erreur porte sur un double comptage des conteneurs, qui
   gonfle numérateur et dénominateur ensemble.
2. **Le nombre de grilles dont la page SSP ne couvre pas la vignette n'est pas
   douze mais trente** (§ 3). Douze était le cumul arrêté à mi-chantier ; les
   lots suivants ont continué d'en trouver, et un compteur reparti d'une base
   fausse a masqué la progression.
3. **Les « quinze références à 0 octet » du vault ne sont pas des fichiers vides
   mais des fichiers absents.** Le vault ne contient **aucun** fichier image de
   0 octet. Ce que les pages citent et qui n'existe pas se compte à **29
   références** sur les 53 pages du corpus (§ 4).
4. **`main-test-phalen.png` pèse 11,6 Mo et non 12,6 Mo** (11 620 129 octets,
   contre 188 226 pour `main-manoeuvre-de-phalen.png`). Le rapport de facteur
   reste de **62**, et la démonstration tient entière.

Aucun de ces quatre points ne remet en cause une grille. Ils sont signalés parce
qu'un chiffre de rapport sert à décider, et que trois d'entre eux servaient
d'argument.

---

## 2. Ce qui a été créé

Avant le chantier, une grille German typique s'ouvrait sur ses sections notées
et s'arrêtait là. Quatorze grilles sur 88 portaient un résumé, treize une
version orale, aucune une annexe théorique. Aujourd'hui les 88 portent les
quatre blocs, dans la même forme.

| Bloc | Rôle pour qui révise | Avant | Après | Volume |
|---|---|---|---|---|
| `resume` | Réviser vite. Source canonique de la grille : ce qui s'y trouve ne se redit nulle part ailleurs | 14 | **88** | 59 764 mots · médiane **672**/grille |
| `annexe-theorie` | Comprendre *pourquoi* : mécanisme, ce qui départage le différentiel, ce que chaque examen établit, seuils | **0** | **88** | 97 256 mots · médiane **1 098**/grille |
| `presentation-patient` | Restituer à l'oral — version longue, version express, moyen mnémotechnique, questions d'examinateur | 13 | **88** | 121 461 mots · médiane **1 399**/grille |
| Planche d'images | Voir la manœuvre, le score, le tracé, l'algorithme | 9 | **83** | 203 fichiers · 27,4 Mo |

**278 481 mots de contenu pédagogique**, soit environ **3 165 mots par grille**.
Le poids HTML du corpus passe de 8,0 à 11,6 Mio ; les images, servies en
fichiers référencés et non embarquées dans le HTML, ajoutent 27 Mo mutualisés —
203 fichiers pour 215 emplacements, une image citée par deux grilles n'étant
stockée qu'une fois.

**Les cartes de méthode.** Les 88 grilles ouvrent désormais leur version orale
sur deux cartes côte à côte, **SBAR** (transmettre un cas à un collègue) et
**SNAPPS** (présenter un cas à un superviseur), servies depuis `cases/img/` et
jamais embarquées. Elles remplacent une « Checklist mentale » que le gabarit
proscrit ; les 88 la portent, aucune ne porte plus l'ancienne section. Les
textes alternatifs — description intégrale des deux tableaux, 534 et
621 caractères — sont identiques sur les 88.

**Le balisage sémantique.** 22 621 termes colorés en huit registres : rouge la
pathologie, rose le symptôme, vert l'examen et le seuil, ambre le traitement,
violet le facteur de risque, orange la complication, bleu le mécanisme, jaune
surligné le concept-clé. Un terme coloré tous les 9,5 mots — soit la densité de
la page de référence de l'utilisateur, mesurée à 1/11,3 en moyenne et 1/7,6 sur
ses régions les plus denses.

Répartition : vert 5 331 · rose 4 965 · rouge 3 881 · jaune 2 558 · ambre 1 864 ·
bleu 1 811 · violet 1 535 · orange 676.

Le balisage est **cantonné à quatre conteneurs** : le résumé, l'annexe
théorique, le moyen mnémotechnique et les questions d'examinateur. Vérifié sur
les 88 : **0 span ailleurs**, en particulier **0 dans la version orale longue et
0 dans la version express** — la restitution orale reste du texte nu, pour que
la lecture à voix haute ne soit pas parasitée par la couleur — et **0 dans
`annexe-dd`**, qui garde sa coloration d'import.

**Ce que cela change concrètement.** Une grille German se lisait comme une
feuille de notation ; elle se lit maintenant comme une fiche : on révise sur le
`resume`, on comprend sur l'`annexe-theorie`, on s'entraîne à restituer sur la
`presentation-patient`, et la planche d'images montre le geste que le critère
note. Les quatre niveaux sont distincts et ne se répètent pas : c'est l'objet du
travail de dédoublonnage (§ 5).

**Cinq grilles restent sans image** : German-10 et German-11 (chute), German-17
(endométriose), German-79 (faux-croup au téléphone), German-87 (conseil de
voyage). Aucune n'est un défaut de sélection — toutes sont des pénuries de
source, détaillées au § 6.

---

## 3. La règle de sourçage, et ce qu'elle a coûté

**La règle.** Tout ce qui a été écrit vient de deux sources et de deux
seulement : la **page SSP** rattachée à la grille dans
`docs/obsidian-mapping.yaml`, et la **section notée** de la grille elle-même.
Rien n'a été comblé par de la connaissance générale, rien n'a été emprunté à une
autre page. Les images ne sont pas choisies dans le vault : elles sont prises
parmi celles que la page SSP de la grille cite elle-même.

**Ce que cela coûte.** Quand la source est muette, la section est courte — ou
absente. Seize grilles portent une section qui le dit en toutes lettres :
« Ce que la page ne dit pas », « Ce que la page SSP ne couvre pas ici ». Ce
n'est pas un aveu de faiblesse : c'est ce qui distingue une fiche sourcée d'une
fiche rédigée de mémoire.

### Le constat le plus utile du chantier : trente grilles mal appariées

**Trente des 88 grilles sont rattachées à une page SSP qui ne couvre pas leur
vignette.** Le motif est net et se répète : une vignette de **premier recours**
ou de **conseil** est rattachée à la page d'**urgence** qui porte le même mot
d'ordre — parce que le mapping associe la grille à la page dont le *titre*
correspond au motif de consultation, alors que la vignette occupe une autre case
du même champ clinique.

**Vingt-deux grilles où la page ne traite pas l'entité de la vignette.** Le
contenu a dû venir presque entièrement du corrigé.

| Grille | Vignette | Page rattachée | Ce que la page traite à la place |
|---|---|---|---|
| German-3 | Difficulté d'allaitement | Prévention Pédiatrique | Consultations systématiques ; aucune courbe de croissance, alors que la vignette est bâtie sur des percentiles |
| German-7 | **Bradycardie** | **Palpitations** | La tachycardie. Muette sur l'hypothyroïdie, la maladie du sinus, les indications du stimulateur (critère noté) et l'accumulation médicamenteuse — le diagnostic retenu |
| German-8 | Céphalée du restaurant chinois | Céphalée | Le diagnostic retenu du premier critère n'apparaît **nulle part** sur la page |
| German-10 | Chute avec déficit focal | Chute & Éval. gériatrique | Le red flag « AVC » y est, mais rien sur la thrombolyse, la tension à ne pas trop abaisser, la distinction AIT/AVC, la dissection carotidienne — quatre éléments notés |
| German-14 | **TDAH** | Troubles du Développement | Retard psychomoteur, TSA, croissance staturale. Le TDAH n'apparaît qu'en liste de différentiel |
| German-16 | Contraception et discernement | **Douleur Abdominale** | L'abdomen aigu chirurgical |
| German-17 | Endométriose | **Douleur Abdominale** | Idem — et **aucune iconographie gynécologique** sur toute la page |
| German-18 | Vignette gynécologique | **Douleur Abdominale** | Idem |
| German-19 | Rectocolite ulcéro-hémorragique | **Douleur Abdominale** | Idem — deux lignes sur les MICI, aucune image |
| German-21 | Reflux gastro-œsophagien | **Douleur Abdominale** | Idem — le reflux tient en une ligne de tableau |
| German-22 | Épicondylite | Douleurs Articulaires | Les arthropathies. Rien sur l'épicondylite : ni texte, ni image, ni message-clé |
| German-25 | Douleur au talon | Douleurs Articulaires | 3 lignes sur 380 touchent le talon ; aucune des six hypothèses du différentiel n'est documentée ; aucune des 15 images ne concerne le pied |
| German-30 | Traumatisme pariétal de l'adolescent | **Douleur Thoracique** | 653 lignes, 47 images, **deux lignes** de traumatologie pariétale |
| German-33 | **RGO** | **Douleur Thoracique** | L'urgence cardiovasculaire |
| German-37 | **Urétrite / IST** | Dysurie | Les infections urinaires |
| German-39 | **Conseil vaccinal** | Entretien Motivationnel | Une page de *méthode*, appliquée à l'alcool et au tabac. L'hésitation vaccinale n'y apparaît qu'en renvoi vidéo |
| German-49 | **Hernie inguinale** | Ballonnement | Les hernies pariétales n'y sont qu'une ligne d'examen |
| German-59 | **Colique néphrétique** | Lombalgies | La page ne la nomme que comme *piège* — et renvoie elle-même à `[[SSP — Colique Néphrétique]]`, **page qui existe dans le vault** |
| German-65 | Otite de l'enfant de 3 ans | Otalgie | Une page écrite pour l'adulte : otalgie référée, cancer pharyngo-laryngé, otite externe nécrosante du diabétique |
| German-79 | Faux-croup au téléphone | **Toux Chronique** | La toux de plus de huit semaines |
| German-86 | **Préparer** un voyage au Brésil | **Fièvre au Retour de Voyage** | Le patient déjà malade. Vaccinations, chimioprophylaxie, protection anti-vectorielle, trousse, assurance — rien de ce que les deux stations notent |
| German-87 | **Préparer** un voyage à Madagascar | **Fièvre au Retour de Voyage** | Idem |

**Huit grilles où la page couvre le raisonnement mais pas l'entité retenue.** Le
diagnostic se construit bien avec la page ; sa prise en charge vient du corrigé.

German-35 et German-36 (asthme d'effort et BPCO stable, page **Dyspnée**, qui
traite l'asthme aigu et l'exacerbation) · German-41 (bilan d'une première crise,
page **Malaise**, excellente sur le différentiel syncope/épilepsie et muette sur
le bilan) · German-54 (insuffisance cardiaque débutante, page **HTA**, dont la
moitié tensionnelle est intégralement couverte) · German-55 (santé publique de
l'hépatite A, page **Ictère**) · German-57 (ostéoporose, page **Lombalgies**,
qui ne porte que le FRAX) · German-70 (traitement de la poussée dentaire, page
**Enfant Irritable**, qui la nomme sans la traiter) · German-82 (traitement de
l'hyperthyroïdie, page **Troubles du Sommeil**).

### Ce qu'un rattachement corrigé rendrait

Cinq pages concentrent seize des trente cas : **Douleur Abdominale** (5),
**Douleurs Articulaires**, **Douleur Thoracique**, **Lombalgies**, **Fièvre au
Retour de Voyage** et **Dyspnée** (2 chacune).

Trois gestes, par ordre de rendement :

1. **Autoriser une grille à avoir deux pages de référence** — celle du *motif* et
   celle de l'*entité*. Le format actuel de `docs/obsidian-mapping.yaml` ne
   permet qu'une page par grille. C'est la limitation qui produit le cas
   German-59, où la bonne page **existe déjà** et où la page rattachée y renvoie
   elle-même. Ce seul changement de format débloquerait plusieurs cas sans
   écrire une ligne de contenu.
2. **Ré-appairer ce qui peut l'être immédiatement.** German-10 vers
   `SSP — Parésie - AVC`, German-59 vers `SSP — Colique Néphrétique` : deux
   pages qui existent, deux grilles qui les attendent.
3. **Créer les pages manquantes.** Cinq manques reviennent : *reflux et
   dyspepsie* (German-21, 33), *hernies de la paroi* (German-49), *conseil
   vaccinal* (German-39), *IST* (German-37), et une page **« Médecine du voyage
   — consultation avant départ »** (German-86, 87). Une page « TDAH » servirait
   German-14, une page « douleur au talon » German-25.

Chacun de ces gestes convertit un `annexe-theorie` bâti sur le seul corrigé en
un `annexe-theorie` sourcé sur une page — et, pour German-17 et German-25,
débloque une iconographie aujourd'hui absente.

---

## 4. Ce qui reste à faire côté vault

Le vault n'a été modifié à aucun moment. Cinq familles de défauts y ont été
mesurées ; elles rendent aujourd'hui inaccessibles **une dizaine d'images qui
documentent chacune un critère noté**. Tous les chemins sont donnés depuis
`/Users/damienfulliquet/Documents/Damien/Medecine/Obsidian/`.

### a) Onze fichiers dont l'extension ment sur le contenu

L'outil de reprise les refuse, à raison : il vérifie l'en-tête du fichier. Le
contenu est intact, seul le nom est faux. **Renommer l'extension suffit.**

| Fichier | Réel | Poids | Ce qu'il coûte |
|---|---|---|---|
| `Skills ECOS/img/pedia/pedia-fievre-sans-foyer-2mois-2ans-algorithme.jpg` | PNG | 221 Ko | L'algorithme qui couvre exactement German-48 **et** German-84 |
| `Skills ECOS/img/pedia/pedia-fievre-sans-foyer-0-2mois-algorithme.jpg` | PNG | 314 Ko | Idem |
| `Skills ECOS/img/pedia/pedia-fontanelles-sutures.jpg` | PNG | 56 Ko | Le critère `a11` de German-84 fait chercher une fontanelle bombée |
| `_bibliotheque/Ped-img/pedlaus_images/retard-de-croissance-general/ped-algorithme-diagnostique-petite-taille-enfant.jpg` | PNG | 76 Ko | L'arbre diagnostique de German-72 |
| `Skills ECOS/img/pulmo/pulmo-ep-algorithme-sans-choc-esc.jpg` | PNG | 158 Ko | Algorithme ESC de l'embolie pulmonaire — critère de management de German-31 |
| `Skills ECOS/img/pulmo/pulmo-ep-algorithme-avec-choc-esc.jpg` | PNG | 147 Ko | Idem |
| `Skills ECOS/img/pulmo/pulmo-rx-thorax-nodules-bilateraux.jpg` | PNG | 490 Ko | Page Toux Chronique |
| `Skills ECOS/img/pulmo/pulmo-rx-thorax-opacite-lobe-superieur-droit.jpg` | PNG | 2 044 Ko | Page Toux Chronique |
| `Skills ECOS/img/gyneco/gyneco-anatomie-pelvienne.png` | **JPEG** | 73 Ko | Page Saignement Vaginal (cas inverse) |
| `Skills ECOS/img/gyneco/gyneco-myomes-uterins-localisations-schema.jpg` | PNG | 659 Ko | Page Saignement Vaginal |
| `Skills ECOS/img/rachis/rachis-rx-lombaire-profil.jpg` | PNG | 3 118 Ko | Page Lombalgies |

**Onze occurrences sur cinq lots successifs cessent d'être un accident.** Un
balayage systématique des fichiers cités par les 53 pages, comparant la
signature d'en-tête à l'extension, est faisable avec l'outillage existant — il
n'y manque qu'un mode et l'autorisation de toucher au vault.

### b) Les deux SVG dits « vides » ne sont pas vides — mais ils sont inutilisables

- `Skills ECOS/img/pedia/pedia-gen-triangle-d-evaluation-pediatrique-pat.svg` —
  **912 octets**, 8 éléments graphiques
- `Skills ECOS/img/neuro/neuro-gen-demarche-steppante-deficit-du-nerf-fibulaire.svg` —
  **799 octets**, 11 éléments graphiques

**Correction au relevé des lots**, qui les décrivait tantôt « vides (0 Ko) »,
tantôt « sans tracé exploitable » : les deux fichiers s'ouvrent et **dessinent
réellement quelque chose** — un triangle avec ses trois étiquettes pour le
triangle d'évaluation pédiatrique, un bonhomme-bâton en segments de droite pour
la démarche steppante. Ce sont des schémas tracés à la main, réduits à
l'essentiel. Ils ne sont pas corrompus : ils sont **trop pauvres pour illustrer
un critère noté**, ce qui est un jugement éditorial et non un défaut de fichier.
La conséquence pratique est la même — ils sont écartés — mais le remède n'est
pas le même : il faut les **redessiner**, pas les réparer. À noter que l'outil de
reprise ne les aurait **pas** arrêtés : 800 octets ne sont pas zéro.

### c) Vingt-neuf références que les pages citent et qui n'existent pas

**Aucun fichier image de 0 octet n'existe dans le vault.** Ce que les rapports
de lot appelaient « références à 0 octet » sont des références **vers des
fichiers absents**. Mesuré sur les 53 pages du corpus German : **29 références
introuvables**, dont **28 sous la forme `Résumé-SSP_page-NNNN.jpg`**.

| Page SSP | Fichiers absents |
|---|---|
| Douleur Abdominale | `Résumé-SSP_page-0023` à `0027` |
| Céphalée | `Résumé-SSP_page-0056` à `0059` |
| Fatigue | `Résumé-SSP_page-0018` à `0022` |
| Amaurose & Baisse d'Acuité Visuelle | `Résumé-SSP_page-0051` à `0053` |
| Lombalgies | `Résumé-SSP_page-0048` à `0050` |
| Toux Chronique | `Résumé-SSP_page-0016`, `0017` |
| Œil Rouge | `Résumé-SSP_page-0069`, `0070` |
| Dyspnée · Dysphagie · Hématurie · Dysfonction Érectile | `page-0007` · `page-0028` · `page-0040` · `page-0075` |
| Dysurie | `G5rt9XF8OyqqQlfo__MHeJgVB2TIA7ruI.png` |

La numérotation continue laisse penser à **une même opération d'export
interrompue**. Les légendes que les pages posent sous ces références décrivent
les planches les plus utiles de la page « Douleur Abdominale » —
caractérisation de la douleur, drapeaux rouges, déroulé de l'examen, manœuvres
ciblées, différentiel par topographie, urgences abdominales. **Les rétablir
débloquerait d'un coup l'iconographie d'examen de cinq grilles.**

Note : la procédure affiche encore le chiffre de **36** références cassées ; la
mesure en donne **29**.

### d) Un fichier au contenu faux

`Skills ECOS/img/nephro/nephro-bilan-urodynamique-cystomanometrie-trace-courbe.jpg`
— 160 Ko, JPEG valide, s'ouvre normalement, et **contient une photographie
d'avions sur un tarmac d'aéroport**, pas un tracé de cystomanométrie. Aucun
contrôle automatique ne peut le voir ; il n'a été détecté qu'en ouvrant
l'image. À remplacer par le tracé qu'il prétend porter.

### e) Des images non optimisées, écartées au seul motif du poids

Le cas qui résume tout : **`Skills ECOS/img/main/main-manoeuvre-de-phalen.png`
pèse 188 226 octets et `Skills ECOS/img/main/main-test-phalen.png` en pèse
11 620 129 — un facteur 62 pour le même contenu.** Ce ne sont pas des images
lourdes par nature : ce sont des PNG non recompressés d'illustrations
vectorielles simples, parfois stockées en 4928 × 3736 pour un schéma rendu à
520 px.

Quinze fichiers écartés au seul motif du poids totalisent **98 Mo** et
documentent chacun un geste que l'examen note :

| Fichier (sous `Skills ECOS/img/`) | Poids | Critère noté |
|---|---|---|
| `main/main-manoeuvre-watson.png` | 10 109 Ko | German-24, examen de la main |
| `main/main-test-froment.png` | 10 024 Ko | German-24, examen de la main |
| `neuro/neuro-pallesthesie.png` | 9 955 Ko | German-83, pallesthésie au diapason gradué |
| `neuro/neuro-reflexe-achilleen-2.png` | 9 863 Ko | German-83, réflexe achilléen |
| `abdo/abdo-punch-renal.png` | 8 954 Ko | German-37 **et** German-51, Giordano |
| `hanche-genou/hanche-genou-test-faber.png` | 8 524 Ko | German-29 |
| `rachis/rachis-test-lasegue.png` | 7 774 Ko | 4 critères notés sur 3 grilles |
| `abdo/abdo-palpation-aorte.png` | 7 722 Ko | German-20, anévrisme de l'aorte |
| `abdo/abdo-palpation-reins.png` | 7 151 Ko | German-51 |
| `neuro/neuro-epreuve-romberg.png` | 5 403 Ko | German-10 |
| `hanche-genou/hanche-genou-test-pivot-shift.png` | 5 403 Ko | German-23 |
| `cardio/cardio-palpation-vasculaire.png` | 5 065 Ko | German-26, les quatre pouls |
| `gals/gals-inspection-marche.png` | 3 008 Ko | German-10 |
| `rachis/rachis-test-schober.png` | 1 030 Ko | Test de Schober |
| `neuro/neuro-epreuve-doigt-nez.png` | 797 Ko | German-80 |

**Une passe de recompression sur ces quinze fichiers est le geste au meilleur
rendement de tout ce relevé.** Elle rendrait éligibles une dizaine d'images qui
documentent chacune un critère noté, donnerait une planche à German-10 — l'une
des cinq grilles sans image — et compléterait German-83 et German-29. Elle est
préférable à un nouveau relèvement du plafond, qui laisserait entrer des
fichiers de 8 à 10 Mo dans un stock partagé sans corriger la cause.

### f) Deux pièges de nommage, résolus côté grille et pas côté vault

Sept fichiers sont stockés par macOS en forme Unicode décomposée alors que les
pages SSP les citent en forme composée — même chaîne à l'œil, octets
différents, **404 sur tout serveur qui ne normalise pas**. Seize noms portent un
espace, huit un caractère non-ASCII. Le chantier a supprimé le piège **dans les
grilles**, en normalisant les noms à la reprise et en traçant le renommage au
manifeste ; il reste entier dans le vault.

Par ailleurs, le dossier `.backup_transparents` est une copie intégrale de
`Skills ECOS/img/` : sans exclusion explicite, **46 des 664 images citées
deviendraient ambiguës**. L'exclusion est aujourd'hui codée en dur dans
l'outillage ; deux fichiers ont déjà été repris sans que l'ambiguïté soit
signalée.

---

## 5. La redondance : ce qu'elle mesure et où elle en est

Le principe : chaque information vit à **un seul endroit**. Le résumé est la
source canonique ; quand un item du résumé et un item de la version orale disent
la même chose, l'un des deux doit céder — et c'est toujours le pédagogique qui
cède, jamais le corrigé de la section notée.

| État | Paires |
|---|---|
| `4819f53`, avant tout travail sur German | **83** |
| `383ade6`, juste avant la création des sections | **14** |
| Aujourd'hui | **16** |

Le passage de 83 à 14 est l'œuvre des lots antérieurs, sur le bloc de
différentiel. Le chantier des sections, lui, part de 14 et arrive à 16 : **deux
paires ajoutées, toutes deux sur German-1**, la grille pilote, et documentées
comme telles dès le premier lot.

**Les seize paires restantes sont toutes justifiables par un changement de
format**, ce qui est le critère demandé :

- **Douze** opposent le `resume` à la version orale. Les douze, sans exception,
  opposent une phrase complète du résumé à **une ligne du moyen mnémotechnique** —
  vérifié : les douze items de la version orale sont logés dans la sous-section
  mnémotechnique, aucun ailleurs. Neuf sont même en forme d'acronyme :
  « coloscopie avec biopsies, diagnostic de certitude » contre « **C**oloscopie
  avec biopsies — diagnostic ». L'acronyme n'est pas une redite, c'est une aide
  à la mémorisation ; le supprimer viderait le moyen mnémotechnique de son objet.
- **Deux** opposent le différentiel au corrigé thérapeutique dans German-68
  (« installation progressive » / « essai et adaptation progressive », 0,73).
  Ces deux blocs sont du **niveau 2** — ils font partie du corrigé de la section
  notée, on n'y touche pas. Les deux paires sont antérieures au chantier.
- **Une** oppose le corrigé thérapeutique à la version orale de German-1
  (« hydratation et correction des troubles électrolytiques » / « hydratation et
  je corrige les électrolytes ») : la seconde est la **formulation parlée à la
  première personne**, qui est précisément ce que la version orale existe pour
  fournir.
- **Une** oppose un drapeau rouge à la version orale de German-44 (« évolution
  vers lupus systémique » / « **S**urveillance évolutive vers lupus
  systémique ») — même cas d'acronyme, sur un bloc de niveau 2 intouchable.

**AMBOSS reste à 147 paires et RESCOS à 127** : ces deux corpus n'ont pas connu
le même dédoublonnage et ne sont pas comparables au chiffre German.

---

## 6. Les arbitrages ouverts

Trois décisions n'ont pas été prises et attendent un arbitrage.

**a) Le balisage sémantique d'`annexe-dd`.** Le bloc de raisonnement différentiel
n'est **balisé sur aucune des 88 grilles**. La consigne d'origine demandait de
baliser aussi ce bloc quand il préexistait ; cinq lots consécutifs s'en sont
abstenus, pour la même raison : baliser 25 grilles sur 88 aurait créé une
hétérogénéité pire que l'abstention, et rendu la mesure de densité
incomparable. L'abstention a produit un corpus homogène — c'est son seul mérite,
et il est réel.

Deux difficultés si l'arbitrage est de baliser : la passe doit porter sur **les
88 en une fois** ; et les `annexe-dd` portent **déjà une coloration d'import**,
sous forme de styles écrits directement dans le HTML (`color: rgb(169,34,23)`),
étrangère au système des huit classes. Il faudra décider si l'une remplace
l'autre ou si elles coexistent.

**b) La frontière de l'exemption de plafond pour les manœuvres nommées.** Le
plafond de 600 Ko par image souffre deux exemptions : le message-clé obligatoire,
et l'image **désignée nommément par un critère noté**. Reste à savoir ce que
« désignée » veut dire. Un critère qui écrit « *Test de Lasègue* » **nomme une
manœuvre** ; désigne-t-il pour autant l'image de cette manœuvre ? Les lots ont
tranché **non** — l'exemption ne vaut que pour un renvoi explicite du type
« [Voir image en annexe] ». Cette lecture est défendable mais restrictive : elle
écarte `rachis-test-lasegue.png`, que quatre critères notés de trois grilles
nomment. Cinq lots ont demandé que la frontière soit posée. Elle se représentera
sur tout le musculo-squelettique.

Deux remarques pour éclairer la décision. D'une part, l'exemption n'a en
pratique **jamais servi** : aucun des 203 fichiers livrés ne dépasse 600 Ko, le
plus lourd étant à 595 Ko. D'autre part, si la recompression du vault (§ 4 e)
est faite, la question disparaît d'elle-même pour l'essentiel des cas — un
schéma de Lasègue recompressé passe très largement sous le plafond. **Traiter le
vault rend l'arbitrage largement sans objet.**

**c) Les cinq grilles sans image.** Aucune ne l'est par défaut de sélection.

| Grille | Motif |
|---|---|
| German-10 et German-11 (chute) | La page ne cite que 4 images, contre une médiane de 12. Deux passent le test de pertinence mais pèsent 5 403 et 3 008 Ko — 9 fois et 5 fois le plafond. Les deux autres échouent le test. **Recompresser les deux fichiers donne une planche à German-10** |
| German-17 (endométriose) | La page « Douleur Abdominale » ne porte **aucune iconographie gynécologique** — ni annexe, ni grossesse extra-utérine, ni torsion, ni kyste — alors qu'elle nomme ces entités dans son texte et ses drapeaux rouges |
| German-79 (faux-croup au téléphone) | La seule image pédiatrique de la page « Toux Chronique » est un algorithme de toux chronique de l'enfant. La retenir aurait été sélectionner **sur le thème et non sur la vignette** |
| German-87 (voyage à Madagascar) | Sur les 14 images de la page, 13 documentent la prise en charge d'un malade. La quatorzième est la seule pertinente — et elle a été attribuée à German-86, dont les critères notés la recoupent ligne à ligne. La règle interdisant à deux grilles d'une même page de porter la même sélection, German-87 reste sans image |

German-87 est le cas qui mérite l'arbitrage : la règle de non-partage, écrite
pour empêcher de sélectionner sur le thème, agit ici comme une règle
d'exclusion. Deux issues : autoriser explicitement le partage quand une page ne
fournit qu'un seul candidat valable, ou accepter la grille cadette sans image.
**C'est la seconde qui a été retenue** — et c'est aussi l'interdit que German-48
et German-84 enfreignent (§ 1 b), ce qui montre que la règle est appliquée de
façon inégale et gagnerait à être tranchée dans un sens ou dans l'autre.

**Une réserve d'affichage, hors arbitrage.** Les deux variantes de section de
l'annexe théorique qui portent un fond teinté — ambre pour les rappels
thérapeutiques, vert pour les examens — **atténuent en thème sombre** les deux
classes de balisage de même teinte : les molécules s'y lisent surtout comme du
gras. Aucune classe n'est écrasée (vérifié par sonde : zéro neutralisation sur
les huit classes, dans les deux thèmes), seulement moins contrastée. Deux
issues : désaturer ces deux fonds, ou admettre que la couleur y compte moins que
la graisse.

---

## 7. Ce que le chantier a appris sur la méthode

**a) Un périmètre défini par « le bloc qui manque » ne voit pas la forme du bloc
qui est là.** Treize grilles portaient déjà une version orale ; les lots ne leur
ont ajouté que ce qui leur manquait, sans jamais rouvrir ce qui existait. Elles
ont ainsi conservé pendant tout le chantier une « Checklist mentale » que le
gabarit proscrit, **sans figurer dans aucune liste de travail**. L'écart n'était
pas une régression : c'était un angle mort du périmètre.

La leçon vaut au-delà de ce cas : **un comptage transversal sur les 88 sans
référence aux lots** trouve ce qu'aucun lot ne pouvait trouver. Le présent
rapport en a rejoué une trentaine — présence des quatre blocs, cardinalité des
sous-sections, forme de la planche, confinement du balisage, absence des blocs
proscrits, intégrité du manifeste. Ils ont livré deux défauts réels (§ 1) que
sept lots successifs, tous verts sur leur propre périmètre, n'avaient pas vus.

**b) Un outil de balisage qui repasse sur son propre travail crée des défauts
qu'aucune assertion d'équilibre ne voit.** L'outil employé jusqu'aux dernières
grilles enveloppait « tremblement de repos », puis rebalayait le résultat avec
le motif « tremblement ». Le span imbriqué produit reste **parfaitement
équilibré** : le contrôle de structure ne le signale pas. Il n'a été trouvé
qu'en cherchant explicitement un span sémantique **à l'intérieur** d'un autre.
Corollaire de méthode : une assertion de bonne formation ne vaut pas assertion
de bonne forme.

**c) Le piège de `theme-sync.js`.** Le script de thème force le thème sombre au
chargement et **écrase tout attribut posé sur la page**. Un contrôle « en thème
clair » mené naïvement produit donc un rendu rigoureusement identique au sombre,
sans le moindre signal d'erreur — et valide un thème qui n'a jamais été affiché.
Le seul contrôle qui le détecte est l'**empreinte** : calculer la signature des
deux captures et exiger qu'elles diffèrent. La vérification finale a substitué
le démarrage de thème dans une copie temporaire, et vérifié par empreinte MD5
que les 20 couples sombre/clair **diffèrent réellement** — 20 sur 20. Sans cette
substitution, la moitié des rendus n'aurait rien prouvé.

**d) Une règle formulée en seuils chiffrés fait plus qu'une consigne de
prudence.** Le lot des grilles 61 à 79 a dû arbitrer 26 doublons en cours de
rédaction, dont **14 opposaient le résumé à l'annexe théorique** — les deux
blocs répétaient les mêmes chiffres. Le lot suivant a appliqué d'emblée une
règle explicite : dans l'annexe théorique, ne garder que **les chiffres qui
expliquent** (seuils de mécanisme, délais physiopathologiques) et laisser au
résumé **ceux qui servent à agir**. Résultat mesuré : **2 paires
résumé/théorie contre 14**, sur 21 doublons arbitrés au lieu de 26. Une règle de
répartition dit où mettre l'information ; une consigne de vigilance dit
seulement de faire attention.

**e) Compter deux fois par deux chemins.** Deux des sept lots ont publié des
volumes de balisage inexacts d'un facteur 2,4 sans que rien ne le signale, parce
que le chiffre n'a jamais été recoupé — ni contre le total du corpus, ni par une
seconde méthode. Un comptage brut sur tout le corpus l'aurait montré
immédiatement : la somme des lots dépassait de 67 % ce que le corpus contient.

---

## Annexe — ce qui a été vérifié, et comment

Mesures faites au commit `302f0d1`, sur le seul état du disque et de `git`,
sans réseau.

**Vérificateurs** — `check_invariants`, `check_nomenclature`,
`check_reachability`, `report_redundancy`, `check_no_loss` sur AMBOSS (40),
German (88) et RESCOS (41), plus `fetch_image.py --verify`. Tous verts. AMBOSS
n'a **aucune grille modifiée** depuis `4819f53` ; les modifications de RESCOS
relèvent de son propre chantier, mené en parallèle.

**Barème** — les sept champs (`maxScores`, `<span class="score">`,
`sectionInfo[].count`, `criteriaCount`, `detailCount`, `radioCount`,
`checkboxCount`) extraits de chacune des 88 grilles telles qu'elles sont sur le
disque **et telles que `git` les rend au commit `4819f53`**, puis comparés champ
à champ : **0 écart**. Le barème n'a pas bougé d'un point.

**Non-perte** — `check_no_loss` depuis `383ade6`, dernier commit avant la
création des sections : **131 items disparus**, qui sont exactement les items des
treize « Checklist mentale » retirées à dessein, et **rien d'autre**.

**Comptage transversal** — 88 grilles, sans référence aux lots. Quatre blocs
88/88 · `commcard-grid` et `section-commcards` 88/88, exactement une par grille ·
`commcard-item` 2/2 sur les 88, images servies depuis `../img/`, textes
alternatifs identiques sur les 88 · « Checklist mentale » **0** · `annexe-expert`
**0** · `annexe-scenario` **0** · `data-image-id` **0** · une seule planche par
`images-wrapper` **sauf German-68** · triplets titre/légende/image équilibrés sur
les 83 planches, **aucun `alt` manquant ou trop court** · sous-sections de la
version orale (cartes, longue, express, mnémotechnique, questions) exactement une
chacune sur les 88, cartes toujours en tête · balisage : **22 621 spans, 0 hors
des quatre conteneurs, 0 dans `annexe-dd`, 0 dans la version longue, 0 dans la
version express**, un seul registre par span, **8 spans imbriqués** (§ 1 a) ·
base64 : **10 images sur 9 grilles**, identiques une à une à l'état d'avant
chantier — aucune image embarquée nouvelle.

**Images** — 203 fichiers présents, 203 référencés, 215 emplacements, 0 lien
cassé, 0 orpheline. Manifeste : 203 lignes, **sha256 et taille conformes pour les
203**. Poids total **27,4 Mo**, médiane 105 Ko, maximum **595 Ko** — aucun
dépassement du plafond de 600 Ko, donc aucune exemption exercée. Par grille :
médiane 331 Ko, 5 grilles au-dessus de 700 Ko (§ 1 c). Répartition : 5 grilles à
0 image, 11 à 1, 14 à 2, **47 à 3** (la cible), 10 à 4, 1 à 5.

**Contrôle visuel** — Chrome sans interface, rendu local, aucune requête réseau.
Dix grilles couvrant tous les lots (German-1, 8, 17, 27, 39, 57, 68, 73, 84, 87),
deux thèmes, 1200 et 500 px : **40 rendus**. Démarrage de thème substitué dans une
copie temporaire, **empreintes MD5 différentes sur les 20 couples** — les deux
thèmes ont réellement été affichés. Zéro image non chargée, zéro dimension
naturelle nulle, **zéro débordement horizontal** aux deux largeurs, zéro classe de
balisage neutralisée, cartes de méthode côte à côte à 1200 px et empilées à
500 px sur les dix. Copies temporaires supprimées, absence vérifiée.

**Périmètre** — aucun fichier de `cases/` modifié. Aucune grille lue en entier.
Aucun `git push`, aucune commande réseau, aucun `git gc`, aucun `git prune`. Le
vault n'a pas été modifié.
