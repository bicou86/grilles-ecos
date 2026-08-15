---
aliases:
  - "Mémento Troubles du Sommeil"
type: memento-ecos-ssp
ssp: "Troubles du Sommeil"
specialite: "Psychiatrie"
cas: 3
diagnostics: 3
attendus_documentes_ailleurs: 1
attendus_absents_du_corpus: 1
tags:
  - ecos/memento
  - ecos/grille-non-officielle
cssclasses:
  - skill-ecos
---

> [!info] Légende
>
> - 📋 = Anamnèse — ce qu'il faut absolument avoir demandé
> - 🩺 = Status — le geste ou le signe qui fait la différence
> - 💊 = Management — examens complémentaires **et** prise en charge
> - 🚨 = urgence
> - 🚩 = red flag à ne jamais rater
> - ⭐️ = SSP ou diagnostic fréquemment rencontré à l'ECOS

> [!warning] Mémento dérivé de grilles NON officielles
> Ces items viennent de grilles d'entraînement (RESCOS, AMBOSS, GERMAN,
> AZYGOS) qu'aucun jury n'a validées. Seul le mémento des neuf grilles
> officielles fait autorité — [[Mémento ECOS — Grilles officielles]].
>
> **Comment lire les suffixes.** Anamnèse et status sont fusionnés entre
> toutes les grilles de la SSP. Le suffixe décrit quelles grilles portent
> **cette formulation-là** :
>
> - un item **nu** : **toutes** les grilles de la SSP portent cette
>   formulation ;
> - `*(Diagnostic)*` : exactement toutes les grilles de ce diagnostic la
>   portent, et elles seules — au-delà de trois, ils sont comptés ;
> - `*(n grilles sur m)*` : une partie des grilles la porte, que les
>   diagnostics ne suffisent pas à désigner sans mentir ;
> - un **sous-item nu** hérite de la portée de son parent — il ne répète pas
>   son suffixe. Seul un sous-item dont la portée **diffère** du parent en
>   porte un.
>
> **Le management, lui, ne fusionne pas.** La prise en charge dépend du
> diagnostic : l'encadré 💊 se découpe en **un sous-bloc par diagnostic**,
> `💊 Management — si <diagnostic>`. À l'intérieur d'un sous-bloc,
> `*(n grilles sur m)*` compte les grilles **de ce diagnostic-là**, pas celles
> de la SSP.
>
> Un item porté par **deux diagnostics ou plus** remonte dans un encadré
> `💊 Management — partagé par plusieurs diagnostics`, en tête — **mais
> seulement si son contenu l'est aussi** : dès qu'un seul de ses sous-items
> n'appartient qu'à un diagnostic, l'item reste dans les sous-blocs, répété.
> Un item de tête partagé aux sous-items privés déménagerait votre révision
> dans un encadré qui ne vous concerne pas.
>
> Le suffixe d'un item partagé **nomme les diagnostics concernés** :
> `*(3 grilles sur 12)* — *Angor · STEMI*` se lit « 3 des 12 grilles de la SSP
> portent cet item, dont au moins une d'Angor et une de STEMI ». Le compte
> vient en tête, les noms après le tiret : il ne dit **pas** que toutes les
> grilles de ces diagnostics le portent. ⚠️ **Cet encadré se lit *avec* le
> sous-bloc de votre diagnostic, pas à sa place.** Il est absent quand aucun
> item n'est partagé, ce qui arrive souvent : le rapprochement entre grilles
> reste purement lexical, et deux grilles qui prescrivent la même chose
> autrement ne se rejoignent pas.
>
> Un sous-bloc existe pour **chacun des diagnostics attendus de la SSP**
> (docs/ecos-priorites-2026.yaml), y compris ceux qu'aucune grille de la SSP
> ne documente. Ce sous-bloc vide dit alors laquelle des deux situations
> s'applique : soit une **autre SSP** documente ce diagnostic, et il y renvoie ;
> soit le corpus l'ignore, et c'est un **trou de révision** à combler ailleurs.
>
> ⚠️ **Le suffixe parle des formulations, pas du contenu clinique.** Le
> rapprochement entre grilles est encore purement lexical : deux grilles qui
> disent la même chose autrement (« Motif de consultation » et « Motif de
> consultation principal », « Allergies » et « Allergies connues ») donnent
> **deux items distincts**, chacun marqué comme partiel. Un `*(1 grille sur 2)*`
> ne veut donc pas dire que l'autre grille néglige la question — seulement
> qu'elle l'écrit autrement. Tant que le vocabulaire canonique n'est pas
> rempli, lisez les libellés voisins ensemble.

# Troubles du Sommeil

*Psychiatrie · 3 grilles · 3 diagnostics documentés · 1 attendu documenté ailleurs · 1 attendu absent du corpus* — [[SSP — Troubles du Sommeil]]

> [!abstract] Les 3 grilles fusionnées
> - **AMBOSS-16** — Trouble anxieux `premier-dd` · [grille](<file:///Users/damienfulliquet/Developer/GitHub/grilles-ecos/cases/amboss/AMBOSS-16_-_Troubles_du_sommeil_-_Femme_32_ans_-_Grille_ECOS.html>)
> - **AZYGOS-49** — Dépression `diagnostic-travail` · [grille](<file:///Users/damienfulliquet/Developer/GitHub/grilles-ecos/.azygos-extraction/2895ae8e-443e-472c-acf0-c597e27cd05b.json>)
> - **German-82** — Hyperthyroïdie `corrige` · [grille](<file:///Users/damienfulliquet/Developer/GitHub/grilles-ecos/cases/german/German-82_-_Troubles_du_sommeil_-_Grille_ECOS.html>)

> [!note] 📋 Anamnèse
> - [ ] **1. Motif principal *(Trouble anxieux)***
> - [ ] **2. Caractérisation des troubles du sommeil *(Trouble anxieux)***
> 	- [ ] Début
> 	- [ ] Constant/intermittent
> 	- [ ] Événements précipitants
> 	- [ ] Progression
> 	- [ ] Épisodes antérieurs
> 	- [ ] Facteurs améliorants
> 	- [ ] Facteurs aggravants
> - [ ] **3. Symptômes associés *(Dépression · Trouble anxieux)***
> - [ ] **4. Recherche de symptômes spécifiques *(Trouble anxieux)***
> 	- [ ] Céphalées
> 	- [ ] Fatigue
> 	- [ ] Palpitations
> 	- [ ] Douleur thoracique
> 	- [ ] Dyspnée
> 	- [ ] Problèmes intestinaux
> 	- [ ] Appétit
> 	- [ ] Variations pondérales
> 	- [ ] Vertiges
> - [ ] **5. Analyse détaillée du sommeil *(Trouble anxieux)***
> 	- [ ] Difficulté d'endormissement
> 	- [ ] Réveils nocturnes fréquents
> 	- [ ] Réveil précoce
> 	- [ ] Sensation de fatigue au réveil
> - [ ] **6. Hygiène du sommeil *(Trouble anxieux)***
> 	- [ ] Routine du coucher
> 	- [ ] Alcool avant le coucher
> 	- [ ] Boissons caféinées
> 	- [ ] Gros repas avant le coucher
> 	- [ ] Exercice avant le coucher
> 	- [ ] TV dans la chambre
> - [ ] **7. État psychologique *(Trouble anxieux)***
> 	- [ ] Humeur
> 	- [ ] Durée de l'anxiété
> - [ ] **8. Symptômes d'hyperthyroïdie *(Trouble anxieux)***
> 	- [ ] Transpiration excessive/intolérance à la chaleur
> 	- [ ] Tremblements
> - [ ] **9. Antécédents médicaux et chirurgicaux *(Trouble anxieux)***
> 	- [ ] Antécédents médicaux
> 	- [ ] Antécédents chirurgicaux
> 	- [ ] Hospitalisations
> - [ ] **10. Allergies et médicaments *(Trouble anxieux)***
> 	- [ ] Allergies
> 	- [ ] Médicaments
> - [ ] **11. Antécédents familiaux**
> 	- [ ] Maladies thyroïdiennes *(Hyperthyroïdie)*
> 	- [ ] Autres maladies héréditaires *(Hyperthyroïdie)*
> - [ ] **12. Habitudes et mode de vie *(Trouble anxieux)***
> 	- [ ] Occupation
> 	- [ ] Domicile
> 	- [ ] Alcool
> 	- [ ] Drogues illicites
> 	- [ ] Tabac
> - [ ] **13. Question d'entrée *(Dépression)***
> - [ ] **14. Dimension temporelle *(Dépression)***
> - [ ] **15. Évolution *(Dépression)***
> - [ ] **16. Début / Durée *(Dépression)***
> - [ ] **17. Épisode *(Dépression)***
> - [ ] **18. Anamnèse du sommeil *(Dépression)***
> - [ ] **19. Difficulté d'endormissement *(Dépression)***
> - [ ] **20. Difficulté de maintien du sommeil / Réveil précoce *(Dépression)***
> - [ ] **21. Fatigue / Somnolence diurne *(Dépression)***
> - [ ] **22. Habitudes de sommeil *(Dépression)***
> - [ ] **23. Rythme veille-sommeil *(Dépression)***
> - [ ] **24. Utilisation d'écrans le soir *(Dépression)***
> - [ ] **25. Consommation de caféine *(Dépression)***
> - [ ] **26. Alcool comme aide au sommeil *(Dépression)***
> - [ ] **27. Déclencheur *(Dépression)***
> - [ ] **28. Retentissement dans la vie quotidienne *(Dépression)***
> - [ ] **29. Affectivité *(Dépression)***
> - [ ] **30. Humeur dépressive *(Dépression)***
> - [ ] **31. Intérêt / Plaisir *(Dépression)***
> - [ ] **32. Cognition / Comportement *(Dépression)***
> - [ ] **33. Concentration / Capacité de décision *(Dépression)***
> - [ ] **34. Estime de soi / Sentiments de culpabilité *(Dépression)***
> - [ ] **35. Désespoir *(Dépression)***
> - [ ] **36. Neurovégétatif *(Dépression)***
> - [ ] **37. Élan vital / Énergie *(Dépression)***
> - [ ] **38. Appétit / Poids *(Dépression)***
> - [ ] **39. Suicidalité *(Dépression)***
> - [ ] **40. Lassitude de vivre *(Dépression)***
> - [ ] **41. Idées suicidaires *(Dépression)***
> - [ ] **42. Plan suicidaire / Préparation *(Dépression)***
> - [ ] **43. Tentatives de suicide antérieures *(Dépression)***
> - [ ] **44. Capacité de s'engager à demander de l'aide *(Dépression)***
> - [ ] **45. Symptômes psychotiques *(Dépression)***
> - [ ] **46. Délire *(Dépression)***
> - [ ] **47. Hallucinations *(Dépression)***
> - [ ] **48. Troubles du moi *(Dépression)***
> - [ ] **49. Anamnèse systémique somatique *(Dépression)***
> - [ ] **50. Général / Symptômes B *(Dépression)***
> - [ ] **51. Tête / SNC *(Dépression)***
> - [ ] **52. Endocrinologique *(Dépression)***
> - [ ] **53. Cœur / Poumons / Apnée du sommeil *(Dépression)***
> - [ ] **54. Gastro-intestinal / Urogénital *(Dépression)***
> - [ ] **55. Neurologique *(Dépression)***
> - [ ] **56. DD Trouble bipolaire (Manie / Hypomanie) *(Dépression)***
> - [ ] **57. Fuite des idées / Tachypsychie *(Dépression)***
> - [ ] **58. Besoin de sommeil diminué *(Dépression)***
> - [ ] **59. Humeur élevée *(Dépression)***
> - [ ] **60. Augmentation de l'élan vital / Activité *(Dépression)***
> - [ ] **61. Logorrhée *(Dépression)***
> - [ ] **62. Comportement à risque *(Dépression)***
> - [ ] **63. DD ESPT *(Dépression)***
> - [ ] **64. Événement traumatique *(Dépression)***
> - [ ] **65. Intrusions / Flashbacks / Cauchemars *(Dépression)***
> - [ ] **66. DD Anxiété *(Dépression)***
> - [ ] **67. Anxiété généralisée / Inquiétudes *(Dépression)***
> - [ ] **68. Attaques de panique *(Dépression)***
> - [ ] **69. Phobies *(Dépression)***
> - [ ] **70. DD TOC *(Dépression)***
> - [ ] **71. Obsessions *(Dépression)***
> - [ ] **72. Impulsions obsessionnelles *(Dépression)***
> - [ ] **73. Compulsions *(Dépression)***
> - [ ] **74. Pensée formelle *(Dépression)***
> - [ ] **75. Rumination / Pensées circulaires *(Dépression)***
> - [ ] **76. Inhibition de la pensée / Ralentissement psychique *(Dépression)***
> - [ ] **77. Barrage de la pensée *(Dépression)***
> - [ ] **78. Antécédents médicaux *(Dépression)***
> - [ ] **79. Maladies chroniques / Douleurs *(Dépression)***
> - [ ] **80. Antécédents psychiatriques *(Dépression)***
> - [ ] **81. Médicaments / Automédication *(Dépression)***
> - [ ] **82. Consommation de substances *(Dépression)***
> - [ ] **83. Alcool *(Dépression)***
> - [ ] **84. Drogues *(Dépression)***
> - [ ] **85. Tabagisme *(Dépression)***
> - [ ] **86. Allergies *(Dépression)***
> - [ ] **87. Suicide dans la famille *(Dépression)***
> - [ ] **88. Profession *(Dépression)***
> - [ ] **89. Situation de logement *(Dépression)***
> - [ ] **90. Environnement social *(Dépression)***
> - [ ] **91. Soutien social *(Dépression)***
> - [ ] **92. Retrait social *(Dépression)***
> - [ ] **93. Facteurs de stress psychosociaux *(Dépression)***
> - [ ] **94. Facteur de personnalité *(Dépression)***
> - [ ] **95. Présentation du médecin *(Hyperthyroïdie)***
> 	- [ ] Se présenter avec nom, fonction et tâche
> - [ ] **96. Caractérisation du problème principal *(Hyperthyroïdie)***
> 	- [ ] Nature du trouble du sommeil
> 	- [ ] Durée
> 	- [ ] Évolution
> 	- [ ] Horaire des troubles (endormissement, réveils nocturnes, réveil précoce)
> - [ ] **97. Symptômes cardiocirculatoires *(Hyperthyroïdie)***
> 	- [ ] Palpitations
> 	- [ ] Transpiration excessive
> 	- [ ] Sensation de chaleur
> - [ ] **98. Symptômes digestifs *(Hyperthyroïdie)***
> 	- [ ] Modification du transit intestinal
> 	- [ ] Diarrhée ou constipation
> - [ ] **99. Symptômes pondéraux et alimentaires *(Hyperthyroïdie)***
> 	- [ ] Appétit
> 	- [ ] Évolution pondérale
> 	- [ ] Quantification de la perte de poids
> - [ ] **100. Symptômes oculaires et cutanés *(Hyperthyroïdie)***
> 	- [ ] Sensation oculaire
> 	- [ ] Changements visuels
> 	- [ ] Modifications cutanées
> - [ ] **101. Symptômes généraux *(Hyperthyroïdie)***
> 	- [ ] Sueurs nocturnes
> 	- [ ] Fièvre
> 	- [ ] Perte de poids
> - [ ] **102. Symptômes neurologiques et psychiques *(Hyperthyroïdie)***
> 	- [ ] Nervosité, irritabilité
> 	- [ ] Tremblements
> 	- [ ] Troubles de concentration
> 	- [ ] Anxiété
> - [ ] **103. Médicaments et substances *(Hyperthyroïdie)***
> 	- [ ] Médicaments actuels
> 	- [ ] Alcool
> 	- [ ] Tabac
> 	- [ ] Drogues
> 	- [ ] Caféine
> - [ ] **104. Antécédents personnels *(Hyperthyroïdie)***
> 	- [ ] Maladies antérieures
> 	- [ ] Hospitalisations
> 	- [ ] Allergies
> - [ ] **105. Antécédents chirurgicaux *(Hyperthyroïdie)***
> - [ ] **106. Anamnèse sociale et professionnelle *(Hyperthyroïdie)***
> 	- [ ] Profession
> 	- [ ] Situation familiale
> 	- [ ] Stress professionnel ou familial
> - [ ] **107. Anamnèse gynécologique *(Hyperthyroïdie)***
> 	- [ ] Cycles menstruels réguliers
> 	- [ ] Contraception
> 	- [ ] Possibilité de grossesse

> [!tip] 🩺 Status
> - [ ] **1. Mesures d'hygiène *(Trouble anxieux)***
> 	- [ ] Lavage des mains
> 	- [ ] Respect de la pudeur avec drap
> - [ ] **2. Examen de la tête, yeux, oreilles, nez et gorge *(Trouble anxieux)***
> 	- [ ] Examen des pupilles
> 	- [ ] Inspection des conjonctives
> - [ ] **3. Examen du cou *(Trouble anxieux)***
> 	- [ ] Examen de la glande thyroïde
> - [ ] **4. Examen cardiovasculaire *(Hyperthyroïdie · Trouble anxieux)***
> 	- [ ] Inspection du thorax *(Trouble anxieux)*
> 	- [ ] Palpation du pouls radial *(Trouble anxieux)*
> 	- [ ] Auscultation cardiaque
> 	- [ ] Recherche d'arythmie *(Hyperthyroïdie)*
> 	- [ ] Pouls périphériques *(Hyperthyroïdie)*
> - [ ] **5. Examen des extrémités *(Trouble anxieux)***
> 	- [ ] Inspection des mains
> - [ ] **6. Examen neurologique *(Hyperthyroïdie · Trouble anxieux)***
> 	- [ ] Examen ciblé des réflexes ostéo-tendineux *(Trouble anxieux)*
> 	- [ ] Réflexes ostéo-tendineux *(Hyperthyroïdie)*
> 	- [ ] Recherche de tremblements fins *(Hyperthyroïdie)*
> 	- [ ] Force musculaire *(Hyperthyroïdie)*
> - [ ] **7. Signes vitaux *(Hyperthyroïdie)***
> 	- [ ] Tension artérielle
> 	- [ ] Fréquence cardiaque
> 	- [ ] Température
> 	- [ ] Poids et taille (BMI)
> - [ ] **8. Inspection générale *(Hyperthyroïdie)***
> 	- [ ] État général
> 	- [ ] Morphologie
> 	- [ ] Agitation psychomotrice
> 	- [ ] Tremblements
> - [ ] **9. Examen ophtalmologique *(Hyperthyroïdie)***
> 	- [ ] Recherche d'exophtalmie
> 	- [ ] Rétraction palpébrale
> 	- [ ] Regard brillant
> - [ ] **10. Examen thyroïdien *(Hyperthyroïdie)***
> 	- [ ] Inspection du cou
> 	- [ ] Palpation thyroïdienne
> 	- [ ] Recherche de nodules
> 	- [ ] Auscultation (souffle thyroïdien)
> - [ ] **11. Examen cutané *(Hyperthyroïdie)***
> 	- [ ] Texture de la peau
> 	- [ ] Chaleur cutanée
> 	- [ ] Myxœdème prétibial

> [!success] 💊 Management — si Dépression
> - [ ] **1. Diagnostic présumé**
> - [ ] **2. Évaluation du risque suicidaire**
> - [ ] **3. Interventions de base**
> - [ ] **4. Activation comportementale**
> - [ ] **5. Psychoéducation**
> - [ ] **6. Hygiène du sommeil**
> - [ ] **7. Options thérapeutiques (Décision partagée)**
> - [ ] **8. Antidépresseur**
> - [ ] **9. Psychothérapie**
> - [ ] **10. Thérapie combinée**
> - [ ] **11. Éventuel arrêt de travail de courte durée**
> - [ ] **12. Contrôle de l'évolution**
> - [ ] **13. Filet de sécurité**

> [!success] 💊 Management — si Hyperthyroïdie
> - [ ] **1. Diagnostic principal suspecté**
> 	- [ ] Maladie de Basedow (hyperthyroïdie auto-immune)
> - [ ] **2. Diagnostics différentiels**
> - [ ] **3. Examens biologiques thyroïdiens**
> 	- [ ] TSH (thyréostimuline)
> 	- [ ] T3 libre (fT3)
> 	- [ ] T4 libre (fT4)
> 	- [ ] Anticorps anti-récepteurs de la TSH (TRAK)
> 	- [ ] Anticorps anti-TPO
> - [ ] **4. Autres examens biologiques**
> 	- [ ] FSC
> 	- [ ] Ionogramme
> 	- [ ] Fonction hépatique
> 	- [ ] Glycémie
> - [ ] **5. Examens d'imagerie**
> 	- [ ] Échographie thyroïdienne
> 	- [ ] Scintigraphie thyroïdienne
> - [ ] **6. Traitement médical**
> 	- [ ] Traitement thyréostatique (antithyroïdiens de synthèse)
> 	- [ ] Durée du traitement
> 	- [ ] Surveillance biologique régulière
> 	- [ ] Bêtabloquants si nécessaire (symptômes cardiovasculaires)
> - [ ] **7. Surveillance et évolution**
> 	- [ ] Contrôles biologiques réguliers
> 	- [ ] Tentative d'arrêt après 12-18 mois
> 	- [ ] Options en cas de récidive ou persistance
> 	- [ ] Éducation thérapeutique
> - [ ] **8. Options thérapeutiques alternatives**
> 	- [ ] Iode radioactif
> 	- [ ] Chirurgie (thyroïdectomie)
> 	- [ ] Indications et contre-indications
> - [ ] **9. Prise en charge symptomatique**
> 	- [ ] Repos
> 	- [ ] Éviter les stimulants
> 	- [ ] Soutien psychologique si nécessaire
> 	- [ ] Arrêt de travail si indiqué

> [!success] 💊 Management — si SAOS
> *Aucune grille de cette SSP ne documente ce diagnostic* — mais le corpus le documente ailleurs : [[Mémento — Fatigue]] (1 grille).

> [!success] 💊 Management — si Trouble anxieux
> - [ ] **1. Hypothèses diagnostiques**
> - [ ] **2. Examens complémentaires de première intention**
> 	- [ ] Agenda du sommeil
> 	- [ ] ECG
> 	- [ ] Toxicologie urinaire
> - [ ] **3. Examens biologiques**
> 	- [ ] Mesure de la pression artérielle sur 24 heures
> 	- [ ] TSH, T3 libre, T4 libre
> 	- [ ] FSC
> - [ ] **4. Communication avec la patiente**
> 	- [ ] Explications à la patiente des impressions diagnostiques préliminaires
> 	- [ ] Explication du plan de prise en charge
> 	- [ ] Utilisation d'un langage non médical et clarification des termes médicaux
> 	- [ ] Évaluation de l'accord de la patiente avec le plan diagnostique
> 	- [ ] Recherche des préoccupations et questions de la patiente
> - [ ] **5. Conseil et éducation**
> 	- [ ] Conseil sur l'hygiène du sommeil
> 	- [ ] Réaction appropriée au défi concernant l'arrêt de travail
> 	- [ ] Proposer des solutions à long terme
> 	- [ ] Éducation sur la gestion du stress
> 	- [ ] Discussion des options thérapeutiques

> [!success] 💊 Management — si Trouble du sommeil / Insomnie
> *Aucune grille du corpus ne documente ce diagnostic* — il est pourtant attendu de cette SSP. **Trou de révision à combler ailleurs.**
