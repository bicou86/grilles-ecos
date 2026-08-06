# Défauts relevés dans le vault Obsidian — campagne images d'août 2026

Relevé constitué au fil des 31 lots de la campagne de balisage et d'illustration
des corpus `rescos-locales`, `casecos`, `triage` et `usmle`. **Chaque entrée a
été vérifiée à la source**, par contrôle visuel de l'image ou par lecture de
l'en-tête du fichier ; rien n'est déduit du seul nom.

Plusieurs entrées ont été relevées **deux ou trois fois par des lots qui ne se
connaissaient pas** — la mention figure en regard. C'est la meilleure garantie
de fiabilité dont dispose ce document.

Ce document ne modifie rien. Il liste ce qui, corrigé côté vault, rendrait
utilisables des images aujourd'hui perdues — dont plusieurs documentent
littéralement un critère noté.

---

## 1. Fichiers dont l'extension ne correspond pas au format

`fetch_image.py` les refuse avec « en-tête incohérent ». **Le diagnostic de
l'outil est exact** : ce sont des PNG portant une extension `.jpg`. Un simple
renommage — dans le vault et dans la citation de la page — les rend disponibles.

| Fichier | Format réel | Ce qu'il prive |
|---|---|---|
| `pulmo-ep-score-geneve-revise.jpg` | PNG 1310×745 | score de Genève révisé — page Dyspnée |
| `pulmo-ep-algorithme-sans-choc-esc.jpg` | PNG 1669×1358 | algorithme ESC de l'EP |
| `pulmo-ep-algorithme-avec-choc-esc.jpg` | — | idem, branche avec choc |
| `neuro-tableau-hsa-fischer-grades.jpg` | PNG 1894×706 | gradation de Fisher — critère noté « Classification de gravité » |
| `neuro-tableau-hsa-wfns-grades.jpg` | PNG 1900×742 | gradation WFNS — même critère |
| `pharmaco-table-equivalence-corticoides-doses-physiologiques.jpg` | PNG 996×434 | équivalences de corticoïdes — 2 grilles de pharmacologie |
| `pedia-fievre-sans-foyer-0-2mois-algorithme.jpg` | PNG 1000×1446 | algorithme fièvre sans foyer du nourrisson |
| `pedia-fievre-sans-foyer-2mois-2ans-algorithme.jpg` | PNG 1098×1236 | idem, 2 mois – 2 ans |
| `pedia-fontanelles-sutures.jpg` | PNG 510×312 | — |
| `ped-algorithme-diagnostique-petite-taille-enfant.jpg` | PNG 1395×1040 | — |
| `pulmo-rx-thorax-opacite-lobe-superieur-droit.jpg` | PNG 1948×1640 | seule RX de condensation de la page Toux Chronique |
| `general-fatigue-examens-paracliniques.jpg` | PNG | bilan de la fatigue — 3 grilles |
| `endocrino-diabete-criteres-diagnostiques-glycemie.jpg` | en-tête incohérent | critères diagnostiques du diabète |
| `endocrino-dka-hhs-tableau-comparatif.jpg` | en-tête incohérent | comparatif ACD / SHH |
| `gyneco-anatomie-pelvienne.png` | en-tête incohérent | — |
| `gyneco-myomes-uterins-localisations-schema.jpg` | en-tête incohérent | — |
| `rachis-rx-lombaire-profil.jpg` | en-tête incohérent | — |
| `neuro-irm-cerebrale-comparative-des-demences.webp` | en-tête incohérent | — |
| `Aide-mémoire de la présentation de cas.jpg` | PNG 7038×4193 | — |
| `neuro-polygone-willis-schema.jpg` | PNG | polygone de Willis |
| `cardio-schema-idm-type1-criteres.jpg` | PNG | critères de l'IDM de type 1 |
| `pulmo-rx-thorax-nodules-bilateraux.jpg` | PNG | avec l'entrée précédente, **les deux radiographies de la page Toux Chronique sont perdues** |
| `gyneco-endometriose-pelvienne.webp` | en-tête incohérent | — |

**Deux algorithmes « fièvre sans foyer » sont exactement les images que
décrivent les trois légendes orphelines de la grille *État fébrile sans foyer*** :
les légendes existent déjà, seules les images manquent.

---

## 2. Fichiers dont le contenu ne correspond pas au nom

Trouvés **au contrôle visuel**, un par un. Aucun contrôle automatique ne pouvait
les détecter : le nom et le contenu sont tous deux plausibles isolément.

| Fichier | Ce que le nom annonce | Ce que l'image montre |
|---|---|---|
| `nephro-bilan-urodynamique-cystomanometrie-trace-courbe.jpg` | cystomanométrie | **photographie de tarmac d'aéroport avec trois avions** |
| `psy-stades-du-deuil-de-kubler-ross.svg` | stades du deuil | **schéma RH de conduite du changement** — « résistance : inertie, argumentation, révolte, sabotage » |
| `general-mecanisme-du-saos-obstruction-des-voies-aeriennes-superieure.png` | anatomie du SAOS | **diagramme de mécanique des fluides** — conduit convergent-divergent, « energy loss », « flow direction » |
| `neuro-territoires-arteriels-corticaux-aca-acm-acp.png` | territoires cérébraux | **planche de Gray de l'anastomose scapulaire** (relevé deux fois indépendamment) |
| `orl-tache-de-kiesselbach-plexus-vasculaire.png` | tache de Kiesselbach | **planche de Gray, anatomie de surface du cou** |
| `neuro-2b-spirale-d-archimede-…-micrographie-parkinsonienne-vs.jpg` | spirale d'Archimède | **échantillon d'écriture manuscrite de 1869** (« Catherine Metzger, 13 Octobre 1869 ») |
| `neuro-dat-scan-spect-ioflupane-parkinson-vs-tremblement-essentiel.jpg` | comparaison DaTscan | **une seule coupe, captation normale** — la légender comme annoncé enseignerait l'inverse |
| `derma-stevens-johnson-lyell-decollement-epidermique-nikolsky.jpg` | Lyell, Nikolsky | **exanthème maculopapuleux du dos** — aucune bulle, aucun décollement |
| `neuro-syndrome-extrapyramidal-…-dystonie-akathisi.png` | syndrome extrapyramidal | **rendu 3D d'une tête avec une flèche de rotation** (relevé trois fois) |
| `general-cachexie-denutrition-fonte-musculaire-sarcopenie.jpg` | cachexie | **photographie sépia ancienne**, aucune fonte musculaire visible |
| `gyneco-imagerie-mammaire-classification-bi-rads.jpg` | classification BI-RADS | **scintimammographie au 99mTc-(V)DMSA** |
| `general-syndrome-de-turner-stigmates-cliniques.jpg` | stigmates de Turner | 15 paires de portraits, aucun stigmate légendé |
| `abdo-palpation-testiculaire-manuvres-prehn-…` | Prehn, crémastérien | schéma corps entier avec repères A/B/C |
| `neuro-ct-cerebral-ischemique-vs-hemorragique.jpg` | comparaison | **une seule coupe**, hémorragie intraventriculaire |
| `neuro-hemorragie-sous-arachnoidienne-citernes-basales-ct.jpg` | HSA des citernes | **aucun sang** — citernes de densité liquidienne |
| `general-signe-du-godet-…-cotation-0-a-4.jpg` | signe du godet | **gros plan de visage**, œdème périorbitaire |
| `general-classification-figo-des-fibromes-types-0-8.png` | FIGO 0-8 | fibromes légendés **a à f** |
| `gyneco-placenta-praevia-vs-hematome-retroplacentaire.svg` | comparaison | **un seul volet**, praevia |
| `msk-goutte-aigue-podagre-mtp-i-tophi.jpg` | podagre | tophus sur une **grosse articulation**, aucune MTP |
| `msk-fracture-col-femoral-…-fracture-deplacee.jpg` | fracture déplacée | tête congruente, corticales continues — **non déplacée** |
| `nephro-anatomie-prostate-zones-hbp-…jpg` | zones prostatiques | coupe sagittale du bassin, **aucune zone** |
| `general-ceinture-pelvienne-…-t-pod-sam-sling.jpg` | T-POD, SAM-Sling | **un drap et deux colliers de serrage** |
| `general-enmg-axonale-vs-demyelinisante.gif` | comparaison ENMG | **tracé normal**, légendé en allemand |
| `general-depistage-classification.png` | dépistage | gradation du **pied diabétique** |
| `cardio-mapa-24-h-profil-tensionnel.jpg` | tracé de MAPA | **histogramme de recherche** dippers/non-dippers |
| `orl-audiogramme-tonal.jpg` | audiogramme tonal | titré **« Mixed Hearing Loss »**, surdité mixte |
| `vascu-lymphdeme-signe-de-stemmer.jpg` | manœuvre de Stemmer | lymphœdème constitué, **pas la manœuvre** |
| `hemato-frottis-…-goutte-epaisse-paludisme.jpg` | goutte épaisse | **frottis mince**, parasites indiscernables |
| `Réponses_attendues.png` | — | dessin de subluxation mandibulaire |
| `neuro-morsure-laterale-de-la-langue-syncope-vs-epilepsie.jpg` | morsure **latérale**, comparaison | érosions de la **pointe** — or le siège est ce qui discrimine : bord latéral → épilepsie, pointe → syncope. Légender selon le nom serait un contresens |
| `nephro-hematurie-caillotee.jpg` | hématurie caillotée | deux vignettes : orifice urétéral en endoscopie, fil-guide en fluoroscopie. Aucun caillotage |
| `general-obstruction-vas-enfant-epiglottite-croup.jpg` | comparaison épiglottite / croup | **un seul cliché**, radiographie cervicale de profil |
| `neuro-signes-parkinsoniens-tremblement-de-repos-pill-rolling-rigid.jpg` | tableau de signes | **gravure clinique ancienne** de l'attitude parkinsonienne, sans légende |
| `gyneco-atrophie-vulvo-vaginale-sgum-inspection-vulvaire.png` | inspection vulvaire | **schéma histologique** comparatif de l'épithélium vaginal |
| `gyneco-lichen-sclereux-vulvaire.jpg` | photographie clinique | **coupe histologique HE** |
| `general-hemostase-primaire-vs-secondaire-cascade-de-coagulation.svg` | primaire **et** secondaire | cascade de coagulation seule, étiquetée en anglais, glyphes vectorisés |
| `ophtalmo-ovcr-hemorragies-retiniennes-en-flammeches.jpg` | occlusion de la veine **centrale** | lésions groupées sur un seul secteur temporal supérieur, papille normale — pas la distribution des quatre quadrants |
| `cardio-tvp-clinique-mollet-unilateral-dematie-rouge.jpg` | mollet œdématié **rouge** | asymétrie de volume sans érythème franc |
| `orl-otoscopie-tympan-normal.jpg` | tympan normal de référence | membrane rosée, opaque, convexité pâle ; ni manche du marteau ni triangle lumineux. Normal mal éclairé ou bombé — indéterminable |

**Images en langue étrangère**, retenues avec la mention dans la légende :
`neuro-glasgow-coma-scale-e-v-m-3-15.png` (portugais) ·
`uro-debitmetrie-urinaire-qmax.png` (espagnol) ·
`pulmo-spirometrie-syndrome-obstructif-severe.jpg` (allemand) ·
`psy-voies-dopaminergiques-…svg` (anglais) ·
`abdo-aspect-endoscopique-varices-…png` (anglais).

---

## 3. Photographies de patients identifiables

Écartées au titre de la règle d'exclusion. Signalées ici parce qu'elles sont
citées par des pages du vault comme matériel d'enseignement.

`orl-tuberculose-ganglionnaire-cervicale-ecrouelles.jpg` (visage d'enfant, atlas
historique) · `general-signes-de-deshydratation-…jpg` (nourrisson dénutri de
corps entier) · `hepato-ictere.jpg` (visage entier) ·
`general-signe-du-godet-…jpg` (visage) · `tailledebout.jpg` (enfant en
sous-vêtements) · `ophtalmo-leucocorie-red-reflex.jpg` (yeux d'enfant) ·
`pedia-macrosomie-ftale-neonatale.jpg` (nouveau-né, bracelet d'identification) ·
`general-cpap-ppc-nocturne.jpg` · `ophtalmo-test-fluoresceine.jpg` ·
`pericardite-17-tamponnade-…jpg` (profil de patient dans la diapositive) ·
`derma-2b-urticaire-angideme-…jpg` (visage d'enfant) ·
`ophtalmo-champ-visuel-confrontation-doigts.jpg` (examinateur et patiente) ·
`orl-tamponnement-anterieur-posterieur.jpg` · `orl-kyste-branchial.jpg` ·
`general-tumeur-de-la-parotide-adenome-pleomorphe.png` ·
`neuro-epreuve-doigt-nez.png` · `general-syndrome-de-turner-…jpg` ·
`orl-laryngoscopie-indirecte-langue.jpg` (visage frontal) ·
`msk-epanchement-genou-gonflement-asymetrique.jpg` (bracelet d'identification
hospitalier visible) · `gyneco-col-visualisation-speculum.jpg` (périnée non
anonymisé) · `pedia-exanthemes-febriles-du-nourrisson-roseole-hhv-6-etc.jpg`
(enfant nu de corps entier en intérieur privé — écartée par trois lots
indépendamment).

**Cas limites, signalés comme jugements et non comme évidences** :
`rachis-test-schober.png` (modèle de démonstration, visage de profil sur une des
quatre vues) · `gyneco-hauteur-uterine.jpg` (photo de stock, menton et cheveux
au bord du cadre) · `neuro-epreuve-romberg.png` et `gals-inspection-marche.png`
(modèles de démonstration au visage net, dont un en sous-vêtements — posés sur
German-10 après arbitrage explicite du propriétaire).

---

## 4. Références citées mais absentes du vault

- **Toutes les `Résumé-SSP_page-NNNN.jpg`** — aucune n'existe dans le vault
  (`find` sur la racine : 0 fichier), alors que de nombreuses pages les citent.
  Elles amputent la couverture de plusieurs grilles.
- `G5rt9XF8OyqqQlfo__MHeJgVB2TIA7ruI.png`, citée par `SSP — Dysurie.md`.
- Les cinq dernières entrées de `SSP — Douleur Abdominale.md` sont des **URL
  GitHub distantes** (`raw.githubusercontent.com/.../FIG 3.jpg`), non
  reprenables et non conformes à l'exigence de fichier local.

---

## 5. Images pertinentes mais hors plafond de 600 Ko

Ce sont, pour la plupart, **la seule image du vault qui documente littéralement
un critère noté**. Le plafond a prévalu parce qu'un blob volumineux est
irréversible dans l'historique git, alors qu'une image manquante s'ajoute plus
tard. Une recompression — ces fichiers sont des photographies stockées en PNG —
les rendrait toutes utilisables, comme cela a été fait pour German-10 (5403 Ko
→ 469 Ko, sans perte visible).

| Fichier | Poids | Critère noté qu'il documente |
|---|---|---|
| `neuro-pallesthesie.png` | 10,0 Mo | sensibilité vibratoire |
| `main-test-phalen.png` | 11,3 Mo | manœuvre de Phalen |
| `neuro-signe-kernig.png` | 11,7 Mo | signe de Kernig |
| `abdo-punch-renal.png` | 9,0 Mo | examen des loges rénales (Giordano) |
| `dermato-furoncle.png` | 8,9 Mo | — |
| `hanche-genou-signe-glacon.png` | 8,2 Mo | signe du glaçon |
| `neuro-examen-pupilles.png` | 7,7 Mo | examen pupillaire |
| `rachis-test-lasegue.png` | 7,8 Mo | **test de Lasègue** — relevé par quatre lots |
| `abdo-palpation-aorte.png` | 7,5 Mo | palpation de l'aorte — AAA |
| `neuro-epreuve-mingazzini.png` | 7,5 Mo | épreuve de Mingazzini |
| `hanche-genou-log-roll-test.png` | 7,6 Mo | log roll |
| `hanche-genou-test-faber.png` | 8,5 Mo | test de FABER |
| `abdo-palpation-reins.png` | 7,2 Mo | palpation des reins |
| `gals-squeeze-test-mtp.png` | 6,1 Mo | squeeze test |
| `neuro-epreuve-romberg.png` | 5,4 Mo | épreuve de Romberg |
| `cardio-palpation-vasculaire.png` | 5,1 Mo | palpation des pouls |

---

## 6. Discordances de contenu entre une image et la grille qu'elle illustre

Toutes signalées dans la légende plutôt que masquées.

- `cardio-definition-du-cha2-ds2-va.png` donne le **CHA₂DS₂-VA** quand la fiche
  théorique cite encore le CHA₂DS₂-VASc.
- `pedia-convulsions-febriles-simples-vs-complexes.jpg` donne 80/20 % là où la
  fiche donne ~70/30 %.
- La diapositive HUG de la thrombectomie retient **8 heures** quand la fiche de
  la même grille étend la fenêtre à 24 heures avec mismatch.
- `pulmo-spirometrie-syndrome-obstructif-severe.jpg` montre un gain post-BD de
  +0,12 L / +10,5 %, **en deçà** du double seuil de réversibilité : retenue
  comme contre-exemple explicite.
- `abdo-algorithme-diarrhee-aigue-chez-l-adulte.png` est **rognée sur son bord
  gauche** dans le fichier source.
- `cardio-algorithme-tvp.png` est **rognée sur ses bords latéraux** : les
  encadrés « TVP proximale » et « bas compressif classe II » sont tronqués.

---

## 7. Une méthode pour contrôler les SVG

Les campagnes antérieures écartaient les `.svg` faute de pouvoir les regarder —
leurs glyphes sont souvent vectorisés, donc invisibles à toute recherche
textuelle. `qlmanage -t <fichier.svg>` les rend en PNG et permet le contrôle
visuel. Le rendu est carré et rogné pour les `viewBox` non carrées : utile,
mais partiel. C'est ainsi qu'a été établi que
`general-hemostase-primaire-vs-secondaire-…svg` ne porte que l'hémostase
secondaire.
