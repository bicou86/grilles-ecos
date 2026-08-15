---
aliases:
  - "Mémento Douleur Thoracique"
type: memento-ecos-ssp
ssp: "Douleur Thoracique"
specialite: "Cardiologie & Vasculaire"
cas: 12
diagnostics: 7
attendus_sans_grille: 1
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
> Quand un item est porté par **deux diagnostics ou plus**, il n'est pas
> recopié dans chaque sous-bloc : il remonte dans un encadré
> `💊 Management — partagé par plusieurs diagnostics`, en tête, où son suffixe
> **nomme les diagnostics concernés** — `*(Angor · STEMI — 3 grilles sur 12)*`
> se lit « au moins une grille d'Angor et une de STEMI le portent, 3 des
> 12 grilles de la SSP au total ». ⚠️ **Cet encadré se lit *avec* le sous-bloc
> de votre diagnostic, pas à sa place.** Il est absent quand aucun item n'est
> partagé, ce qui arrive souvent : le rapprochement entre grilles reste
> purement lexical, et deux grilles qui prescrivent la même chose autrement ne
> se rejoignent pas.
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

# Douleur Thoracique ⭐️

*Cardiologie & Vasculaire · 12 grilles · 7 diagnostics documentés · 1 attendu sans grille* — [[SSP — Douleur Thoracique]]

> [!abstract] Les 12 grilles fusionnées
> - **AMBOSS-12** — Embolie pulmonaire `premier-dd` · [grille](<file:///Users/damienfulliquet/Developer/GitHub/grilles-ecos/cases/amboss/AMBOSS-12_-_Douleur_thoracique_-_Femme_35_ans_-_Grille_ECOS.html>)
> - **AMBOSS-13** — Pneumothorax `premier-dd` · [grille](<file:///Users/damienfulliquet/Developer/GitHub/grilles-ecos/cases/amboss/AMBOSS-13_-_Douleur_thoracique_-_Homme_35_ans_-_Grille_ECOS.html>)
> - **AMBOSS-14** — Infarctus du myocarde / SCA `premier-dd` · [grille](<file:///Users/damienfulliquet/Developer/GitHub/grilles-ecos/cases/amboss/AMBOSS-14_-_Douleur_thoracique_-_Homme_45_ans_-_Grille_ECOS.html>)
> - **AZYGOS-22** — Pneumothorax `diagnostic-travail` · [grille](<file:///Users/damienfulliquet/Developer/GitHub/grilles-ecos/.azygos-extraction/36c2f5c1-90b6-4677-9a14-9d758632e1df.json>)
> - **German-30** — Contusion costale `corrige` · [grille](<file:///Users/damienfulliquet/Developer/GitHub/grilles-ecos/cases/german/German-30_-_Douleur_thoracique_-_Grille_ECOS.html>)
> - **German-31** — Embolie pulmonaire `corrige` · [grille](<file:///Users/damienfulliquet/Developer/GitHub/grilles-ecos/cases/german/German-31_-_Douleur_thoracique_-_Grille_ECOS.html>)
> - **German-32** — Pneumothorax `corrige` · [grille](<file:///Users/damienfulliquet/Developer/GitHub/grilles-ecos/cases/german/German-32_-_Douleur_thoracique_-_Grille_ECOS.html>)
> - **German-33** — Reflux gastro-œsophagien `corrige` · [grille](<file:///Users/damienfulliquet/Developer/GitHub/grilles-ecos/cases/german/German-33_-_Douleur_thoracique_-_Grille_ECOS.html>)
> - **RESCOS-34** — Péricardite / Myopéricardite `explicite` · [grille](<file:///Users/damienfulliquet/Developer/GitHub/grilles-ecos/cases/rescos/RESCOS-34_-_Douleur_thoracique_-_Grille_ECOS.html>)
> - **RESCOS-35** — Embolie pulmonaire `explicite` · [grille](<file:///Users/damienfulliquet/Developer/GitHub/grilles-ecos/cases/rescos/RESCOS-35_-_Douleur_thoracique_-_Grille_ECOS.html>)
> - **RESCOS-36** — Angor stable / Maladie coronarienne `premier-dd` · [grille](<file:///Users/damienfulliquet/Developer/GitHub/grilles-ecos/cases/rescos/RESCOS-36_-_Douleur_thoracique_-_Grille_ECOS.html>)
> - **RESCOS-37** — Angor stable / Maladie coronarienne `explicite` · [grille](<file:///Users/damienfulliquet/Developer/GitHub/grilles-ecos/cases/rescos/RESCOS-37_-_Douleur_thoracique_-_ECC_Cardiologie_-_Grille_ECOS.html>)

> [!note] 📋 Anamnèse
> - [ ] **1. Motif principal *(3 grilles sur 12)***
> - [ ] **2. Caractérisation de la douleur thoracique *(7 grilles sur 12)***
> 	- [ ] Localisation *(6 grilles sur 12)*
> 	- [ ] Intensité (échelle 0-10) *(3 grilles sur 12)*
> 	- [ ] Qualité *(6 grilles sur 12)*
> 	- [ ] Début *(3 grilles sur 12)*
> 	- [ ] Événements précipitants *(3 grilles sur 12)*
> 	- [ ] Progression/constant/intermittent *(3 grilles sur 12)*
> 	- [ ] Épisodes antérieurs *(3 grilles sur 12)*
> 	- [ ] Irradiation
> 	- [ ] Facteurs améliorants *(3 grilles sur 12)*
> 	- [ ] Facteurs aggravants *(4 grilles sur 12)*
> 	- [ ] Intensité *(2 grilles sur 12)*
> 	- [ ] Chronologie *(Péricardite / Myopéricardite)*
> 	- [ ] Développement *(Péricardite / Myopéricardite)*
> 	- [ ] Quantité *(1 grille sur 12)*
> 	- [ ] Facteurs atténuants *(1 grille sur 12)*
> 	- [ ] Localisation rétrosternale *(1 grille sur 12)*
> 	- [ ] Type constrictif *(1 grille sur 12)*
> 	- [ ] Début à l'effort *(1 grille sur 12)*
> 	- [ ] Durée *(Angor stable / Maladie coronarienne)*
> 	- [ ] Cède au repos *(1 grille sur 12)*
> - [ ] **3. Symptômes associés *(9 grilles sur 12)***
> 	- [ ] Dyspnée *(3 grilles sur 12)*
> 	- [ ] Nausées *(2 grilles sur 12)*
> 	- [ ] Transpiration *(1 grille sur 12)*
> 	- [ ] Palpitations *(5 grilles sur 12)*
> 	- [ ] Vertiges, syncope *(2 grilles sur 12)*
> 	- [ ] Toux/expectoration *(2 grilles sur 12)*
> 	- [ ] Fièvre *(1 grille sur 12)*
> 	- [ ] Douleurs abdominales *(2 grilles sur 12)*
> 	- [ ] Pyrosis *(2 grilles sur 12)*
> 	- [ ] Perte de connaissance *(1 grille sur 12)*
> 	- [ ] Toux *(2 grilles sur 12)*
> 	- [ ] Infection récente *(1 grille sur 12)*
> 	- [ ] Douleurs ou œdèmes des membres inférieurs *(1 grille sur 12)*
> 	- [ ] Crachats *(1 grille sur 12)*
> 	- [ ] Hémoptysie *(1 grille sur 12)*
> 	- [ ] Orthopnée *(1 grille sur 12)*
> 	- [ ] Dyspnée d'effort *(1 grille sur 12)*
> 	- [ ] Fatigue *(1 grille sur 12)*
> - [ ] **4. Recherche de symptômes spécifiques *(2 grilles sur 12)***
> 	- [ ] Traumatisme
> 	- [ ] Voyage récent
> 	- [ ] Gonflement des chevilles
> 	- [ ] Nausées/vomissements
> 	- [ ] Fièvre/frissons
> 	- [ ] Fatigue
> 	- [ ] Palpitations
> 	- [ ] Éruption/changements cutanés
> 	- [ ] Toux
> 	- [ ] Toux productive *(1 grille sur 12)*
> 	- [ ] Sang dans les crachats *(1 grille sur 12)*
> 	- [ ] Infections récentes
> 	- [ ] Vertiges
> 	- [ ] Douleur aux jambes *(1 grille sur 12)*
> - [ ] **5. Antécédents médicaux *(5 grilles sur 12)***
> - [ ] **6. Antécédents chirurgicaux *(4 grilles sur 12)***
> - [ ] **7. Allergies *(8 grilles sur 12)***
> - [ ] **8. Médicaments *(4 grilles sur 12)***
> - [ ] **9. Hospitalisations et contacts malades *(1 grille sur 12)***
> 	- [ ] Hospitalisations
> 	- [ ] Contacts malades
> - [ ] **10. Antécédents familiaux *(4 grilles sur 12)***
> - [ ] **11. Habitudes et mode de vie *(3 grilles sur 12)***
> 	- [ ] Occupation
> 	- [ ] Domicile
> 	- [ ] Alcool
> 	- [ ] Drogues illicites
> 	- [ ] Tabac
> 	- [ ] Exercice *(2 grilles sur 12)*
> 	- [ ] Alimentation *(1 grille sur 12)*
> 	- [ ] Consommation d'amphétamines (durée, fréquence, dernière prise) *(Infarctus du myocarde / SCA)*
> - [ ] **12. Recherche de symptômes spécifiques post-traumatiques *(1 grille sur 12)***
> 	- [ ] Céphalées
> 	- [ ] Nausées/vomissements
> 	- [ ] Fièvre/frissons
> 	- [ ] Palpitations
> 	- [ ] Éruption/changements cutanés (ecchymoses)
> 	- [ ] Toux
> 	- [ ] Infections récentes
> 	- [ ] Vertiges
> 	- [ ] Perte de connaissance
> 	- [ ] Blessure à une autre partie du corps
> 	- [ ] Consommation d'alcool ou de drogues avant le traumatisme
> 	- [ ] Faiblesse ou engourdissement
> 	- [ ] Dernier repas/boisson
> - [ ] **13. Hospitalisations *(2 grilles sur 12)***
> - [ ] **14. Question d'ouverture *(1 grille sur 12)***
> - [ ] **15. Dimension temporelle *(1 grille sur 12)***
> - [ ] **16. Début / Durée *(1 grille sur 12)***
> - [ ] **17. Évolution *(1 grille sur 12)***
> - [ ] **18. Épisode *(1 grille sur 12)***
> - [ ] **19. Déclencheur *(1 grille sur 12)***
> - [ ] **20. Traumatisme *(1 grille sur 12)***
> - [ ] **21. Toux / Éternuement *(1 grille sur 12)***
> - [ ] **22. Intervention *(1 grille sur 12)***
> - [ ] **23. Sport / Effort *(1 grille sur 12)***
> - [ ] **24. Localisation *(1 grille sur 12)***
> - [ ] **25. Irradiation *(2 grilles sur 12)***
> - [ ] **26. Qualité *(1 grille sur 12)***
> - [ ] **27. Intensité / Sévérité *(1 grille sur 12)***
> - [ ] **28. Facteurs aggravants *(2 grilles sur 12)***
> - [ ] **29. Facteurs soulageants *(1 grille sur 12)***
> - [ ] **30. Dyspnée *(3 grilles sur 12)***
> 	- [ ] Condition de survenue *(1 grille sur 12)*
> 	- [ ] Classification *(1 grille sur 12)*
> 	- [ ] Chronologie *(1 grille sur 12)*
> - [ ] **31. Survenue situationnelle *(1 grille sur 12)***
> - [ ] **32. Symptômes pulmonaires associés *(1 grille sur 12)***
> - [ ] **33. Toux *(1 grille sur 12)***
> - [ ] **34. Expectoration *(1 grille sur 12)***
> - [ ] **35. Hémoptysie *(2 grilles sur 12)***
> - [ ] **36. Signes infectieux *(1 grille sur 12)***
> - [ ] **37. Fièvre *(1 grille sur 12)***
> - [ ] **38. Frissons *(1 grille sur 12)***
> - [ ] **39. Symptômes circulatoires *(1 grille sur 12)***
> - [ ] **40. Vertiges *(1 grille sur 12)***
> - [ ] **41. Syncope *(1 grille sur 12)***
> - [ ] **42. Clarification diagnostique différentielle de la douleur thoracique *(1 grille sur 12)***
> - [ ] **43. Facteurs de risque d'embolie pulmonaire *(2 grilles sur 12)***
> 	- [ ] Œdème/douleur du mollet *(Reflux gastro-œsophagien)*
> 	- [ ] Voyage récent *(Reflux gastro-œsophagien)*
> 	- [ ] Chirurgie récente *(Reflux gastro-œsophagien)*
> 	- [ ] Cancer actif *(Reflux gastro-œsophagien)*
> 	- [ ] Antécédents familiaux de thrombophilie *(Reflux gastro-œsophagien)*
> - [ ] **44. SCA / Symptômes végétatifs associés *(1 grille sur 12)***
> - [ ] **45. Reflux / Brûlures d'estomac *(1 grille sur 12)***
> - [ ] **46. Toxiques *(2 grilles sur 12)***
> - [ ] **47. Tabagisme *(1 grille sur 12)***
> - [ ] **48. Alcool *(1 grille sur 12)***
> - [ ] **49. Drogues *(1 grille sur 12)***
> - [ ] **50. Profession *(1 grille sur 12)***
> - [ ] **51. Environnement social / Circonstances *(1 grille sur 12)***
> - [ ] **52. Présentation avec nom, fonction et tâche *(4 grilles sur 12)***
> - [ ] **53. Localisation de la douleur *(4 grilles sur 12)***
> - [ ] **54. Qualité de la douleur *(Contusion costale)***
> - [ ] **55. Début de la douleur *(Contusion costale)***
> - [ ] **56. Intensité sur une échelle de 1 à 10 *(Contusion costale)***
> - [ ] **57. Facteurs d'amélioration *(Contusion costale)***
> - [ ] **58. Autres douleurs (jambes, bras, tête...) *(Contusion costale)***
> - [ ] **59. Circonstances de la chute *(Contusion costale)***
> - [ ] **60. Perte de connaissance, vertiges, céphalées *(Contusion costale)***
> - [ ] **61. Médicaments actuels *(4 grilles sur 12)***
> - [ ] **62. Activités sportives, loisirs *(Contusion costale)***
> - [ ] **63. Anamnèse familiale *(4 grilles sur 12)***
> - [ ] **64. Anamnèse sociale *(4 grilles sur 12)***
> - [ ] **65. Identification des symptômes *(3 grilles sur 12)***
> - [ ] **66. Début et évolution des symptômes *(1 grille sur 12)***
> - [ ] **67. Intensité de la douleur *(3 grilles sur 12)***
> - [ ] **68. Caractère de la douleur *(3 grilles sur 12)***
> - [ ] **69. Douleur liée à la respiration *(3 grilles sur 12)***
> - [ ] **70. Irradiation de la douleur *(3 grilles sur 12)***
> - [ ] **71. Facteurs modulateurs *(3 grilles sur 12)***
> 	- [ ] Facteur atténuant *(Péricardite / Myopéricardite)*
> 	- [ ] Facteur aggravant *(Péricardite / Myopéricardite)*
> - [ ] **72. Traumatisme thoracique *(3 grilles sur 12)***
> - [ ] **73. Facteurs de risque cardiovasculaire *(4 grilles sur 12)***
> 	- [ ] Hypertension *(2 grilles sur 12)*
> 	- [ ] Diabète *(2 grilles sur 12)*
> 	- [ ] Dyslipidémie *(3 grilles sur 12)*
> 	- [ ] Antécédents familiaux d'infarctus *(2 grilles sur 12)*
> 	- [ ] Tabagisme
> 	- [ ] Stress professionnel *(1 grille sur 12)*
> 	- [ ] Sédentarité *(1 grille sur 12)*
> 	- [ ] Surpoids *(1 grille sur 12)*
> 	- [ ] Antécédents familiaux *(1 grille sur 12)*
> 	- [ ] Activité physique *(1 grille sur 12)*
> 	- [ ] Poids/IMC *(1 grille sur 12)*
> 	- [ ] Médicaments *(1 grille sur 12)*
> 	- [ ] Alcool *(1 grille sur 12)*
> - [ ] **74. Facteurs de risque d'embolie pulmonaire (Score de Wells) *(2 grilles sur 12)***
> 	- [ ] Œdème/douleur du mollet
> 	- [ ] Voyage récent
> 	- [ ] Chirurgie récente
> 	- [ ] Cancer actif
> 	- [ ] Antécédents familiaux de thrombophilie
> 	- [ ] Contraceptifs oraux *(1 grille sur 12)*
> 	- [ ] Grossesse *(1 grille sur 12)*
> - [ ] **75. Signes généraux *(3 grilles sur 12)***
> - [ ] **76. Antécédents personnels *(3 grilles sur 12)***
> - [ ] **77. Habitudes de vie *(4 grilles sur 12)***
> 	- [ ] Médicaments *(Péricardite / Myopéricardite)*
> 	- [ ] Tabac *(Péricardite / Myopéricardite)*
> 	- [ ] Cannabis *(Péricardite / Myopéricardite)*
> 	- [ ] Alcool *(Péricardite / Myopéricardite)*
> - [ ] **78. Début et évolution *(1 grille sur 12)***
> - [ ] **79. Événement déclenchant *(1 grille sur 12)***
> - [ ] **80. Antécédents cardiaques *(1 grille sur 12)***
> - [ ] **81. Asthme *(1 grille sur 12)***
> - [ ] **82. Antécédents de TVP/EP *(1 grille sur 12)***
> - [ ] **83. Durée des symptômes *(Reflux gastro-œsophagien)***
> - [ ] **84. Facteurs déclenchants et modulateurs *(Reflux gastro-œsophagien)***
> - [ ] **85. Lien avec l'effort physique *(Reflux gastro-œsophagien)***
> - [ ] **86. Raison de la visite *(Péricardite / Myopéricardite)***
> 	- [ ] Douleur à la poitrine
> - [ ] **87. Circonstances de survenue *(Péricardite / Myopéricardite)***
> 	- [ ] Circonstances
> - [ ] **88. Antécédents médicaux récents *(Péricardite / Myopéricardite)***
> 	- [ ] État grippal
> 	- [ ] Pneumonie
> - [ ] **89. Voyages récents *(Péricardite / Myopéricardite)***
> 	- [ ] Voyages récents
> - [ ] **90. Douleur thoracique - évolution temporelle *(1 grille sur 12)***
> 	- [ ] Chronologie
> 	- [ ] Évolution
> - [ ] **91. Antécédents et comorbidités *(1 grille sur 12)***
> 	- [ ] Maladies
> 	- [ ] Hospitalisations
> 	- [ ] Médicaments
> 	- [ ] Allergies
> - [ ] **92. Facteurs de risque *(1 grille sur 12)***
> 	- [ ] Tabagisme
> 	- [ ] Voyages récents
> 	- [ ] Chirurgie/immobilisation récente
> 	- [ ] Médicaments
> 	- [ ] Antécédents d'embolie pulmonaire/angine de poitrine/AVC
> - [ ] **93. Représentation de la maladie *(1 grille sur 12)***
> 	- [ ] Peur d'un cancer pulmonaire comme son mari
> - [ ] **94. Motif de consultation *(1 grille sur 12)***
> - [ ] **95. Circonstances déclenchantes *(1 grille sur 12)***
> 	- [ ] Effort physique
> 	- [ ] Stress émotionnel
> 	- [ ] Froid
> 	- [ ] Repas copieux
> 	- [ ] Jamais au repos
> 	- [ ] Pas la nuit
> - [ ] **96. Évolution dans le temps *(1 grille sur 12)***
> 	- [ ] Début
> 	- [ ] Fréquence croissante
> 	- [ ] Seuil d'effort diminué
> 	- [ ] Caractéristiques stables
> - [ ] **97. Classification CCS de l'angor *(1 grille sur 12)***
> 	- [ ] Classe I: Activités quotidiennes normales
> 	- [ ] Classe II: Limitation légère
> 	- [ ] Classe III: Limitation marquée
> 	- [ ] Classe IV: Angor au moindre effort ou repos
> - [ ] **98. Antécédents et traitements *(1 grille sur 12)***
> 	- [ ] Cholestérol élevé
> 	- [ ] Automédication aspirine
> - [ ] **99. Facteurs déclenchants et circonstances d'apparition *(1 grille sur 12)***
> 	- [ ] Facteur déclenchant 1er épisode
> 	- [ ] Facteur déclenchant 2ème épisode
> 	- [ ] Relation à l'effort
> 	- [ ] Facteurs soulageants
> 	- [ ] Évolution des crises
> - [ ] **100. Symptômes associés et recherche d'insuffisance cardiaque *(1 grille sur 12)***
> 	- [ ] Dyspnée d'effort
> 	- [ ] Dyspnée à la fin des escaliers
> 	- [ ] Orthopnée
> 	- [ ] Dyspnée paroxystique nocturne
> 	- [ ] Œdèmes membres inférieurs
> 	- [ ] Palpitations
> - [ ] **101. Classification de la sévérité (classes d'angine) *(1 grille sur 12)***
> 	- [ ] Impact fonctionnel
> 	- [ ] Limitation des activités
> 	- [ ] Angor au repos
> 	- [ ] Classification probable
> - [ ] **102. Antécédents personnels cardiovasculaires *(1 grille sur 12)***
> 	- [ ] Diabète
> 	- [ ] Hypertension artérielle
> 	- [ ] Hypercholestérolémie
> 	- [ ] Affections cardiaques
> 	- [ ] Hospitalisations
> - [ ] **103. Antécédents familiaux cardiovasculaires *(1 grille sur 12)***
> 	- [ ] Mère
> 	- [ ] Père
> 	- [ ] Frère
> 	- [ ] Oncle maternel
> 	- [ ] Recherche mort subite
> - [ ] **104. Anamnèse socioprofessionnelle et impact *(1 grille sur 12)***
> 	- [ ] Profession
> 	- [ ] Entourage familial
> 	- [ ] Impact sur activités
> 	- [ ] Préoccupations

> [!tip] 🩺 Status
> - [ ] **1. Mesures d'hygiène *(3 grilles sur 12)***
> 	- [ ] Lavage des mains
> 	- [ ] Respect de la pudeur avec drap
> - [ ] **2. Examen du cou *(3 grilles sur 12)***
> 	- [ ] Évaluation de la distension jugulaire
> 	- [ ] Auscultation des artères carotides *(Infarctus du myocarde / SCA)*
> - [ ] **3. Examen cardiovasculaire *(4 grilles sur 12)***
> 	- [ ] Palpation du pouls radial *(3 grilles sur 12)*
> 	- [ ] Auscultation cardiaque *(3 grilles sur 12)*
> 	- [ ] Inspection du thorax *(Infarctus du myocarde / SCA)*
> 	- [ ] Palpation du thorax *(Infarctus du myocarde / SCA)*
> 	- [ ] Palpation du choc de pointe *(Infarctus du myocarde / SCA · Péricardite / Myopéricardite)*
> 	- [ ] Observation des extrémités *(Péricardite / Myopéricardite)*
> 	- [ ] Auscultation des foyers cardiaques *(Péricardite / Myopéricardite)*
> 	- [ ] Prise des pouls aux 4 extrémités *(Péricardite / Myopéricardite)*
> 	- [ ] Prise de la fréquence cardiaque *(Péricardite / Myopéricardite)*
> 	- [ ] Mesure du temps de recoloration *(Péricardite / Myopéricardite)*
> 	- [ ] Observation d'une turgescence jugulaire *(Péricardite / Myopéricardite)*
> 	- [ ] Recherche d'œdème *(Péricardite / Myopéricardite)*
> 	- [ ] Recherche d'un reflux hépato-jugulaire *(Péricardite / Myopéricardite)*
> - [ ] **4. Examen thoracique *(3 grilles sur 12)***
> 	- [ ] Inspection du thorax *(2 grilles sur 12)*
> 	- [ ] Palpation du thorax *(2 grilles sur 12)*
> 	- [ ] Percussion des champs pulmonaires *(2 grilles sur 12)*
> 	- [ ] Auscultation pulmonaire
> 	- [ ] Recherche de frémitus *(2 grilles sur 12)*
> - [ ] **5. Examen des extrémités *(2 grilles sur 12)***
> 	- [ ] Inspection des membres inférieurs *(1 grille sur 12)*
> 	- [ ] Palpation des membres inférieurs *(1 grille sur 12)*
> 	- [ ] Signe de Homans *(1 grille sur 12)*
> 	- [ ] Recherche d'œdème prenant le godet
> 	- [ ] Palpation des pouls pédieux *(1 grille sur 12)*
> - [ ] **6. Examen corporel général *(1 grille sur 12)***
> - [ ] **7. Examen de la tête, yeux, oreilles, nez et gorge *(1 grille sur 12)***
> 	- [ ] Examen des pupilles
> 	- [ ] Examen des muscles oculomoteurs
> - [ ] **8. Examen neurologique *(1 grille sur 12)***
> 	- [ ] Examen de l'orientation dans le temps, l'espace et envers les personnes
> - [ ] **9. Paramètres vitaux *(1 grille sur 12)***
> - [ ] **10. Inspection de l'état général *(1 grille sur 12)***
> - [ ] **11. Inspection du thorax *(2 grilles sur 12)***
> - [ ] **12. Excursion thoracique *(1 grille sur 12)***
> - [ ] **13. Muscles respiratoires accessoires *(1 grille sur 12)***
> - [ ] **14. Signes de traumatisme *(1 grille sur 12)***
> - [ ] **15. Palpation du thorax *(1 grille sur 12)***
> - [ ] **16. Douleur à la pression *(1 grille sur 12)***
> - [ ] **17. Frémissement vocal *(1 grille sur 12)***
> - [ ] **18. Emphysème sous-cutané *(1 grille sur 12)***
> - [ ] **19. Percussion *(1 grille sur 12)***
> - [ ] **20. Auscultation *(1 grille sur 12)***
> - [ ] **21. Veines jugulaires *(1 grille sur 12)***
> - [ ] **22. Auscultation cardiaque *(4 grilles sur 12)***
> 	- [ ] Recherche de souffle *(1 grille sur 12)*
> 	- [ ] Rythme régulier *(1 grille sur 12)*
> 	- [ ] B3/B4 *(1 grille sur 12)*
> 	- [ ] Aortique *(1 grille sur 12)*
> 	- [ ] Pulmonaire *(1 grille sur 12)*
> 	- [ ] Mitral *(1 grille sur 12)*
> 	- [ ] Tricuspide *(1 grille sur 12)*
> 	- [ ] Bruits du cœur réguliers *(1 grille sur 12)*
> 	- [ ] Pas de souffle audible *(1 grille sur 12)*
> 	- [ ] Pas de galop *(1 grille sur 12)*
> 	- [ ] Pas de frottement péricardique *(1 grille sur 12)*
> - [ ] **23. Pouls périphériques *(1 grille sur 12)***
> - [ ] **24. Palpation *(Contusion costale)***
> - [ ] **25. Poumons *(Contusion costale)***
> - [ ] **26. Cœur *(Contusion costale)***
> - [ ] **27. Examen sommaire du rachis et des extrémités *(Contusion costale)***
> - [ ] **28. Bref examen neurologique *(Contusion costale)***
> - [ ] **29. Inspection générale *(4 grilles sur 12)***
> 	- [ ] Couleur de la peau (cyanose ?) *(1 grille sur 12)*
> 	- [ ] Excursions thoraciques symétriques et régulières *(1 grille sur 12)*
> 	- [ ] Fréquence respiratoire *(1 grille sur 12)*
> 	- [ ] Patient en bon état général *(1 grille sur 12)*
> 	- [ ] Pas de détresse respiratoire *(1 grille sur 12)*
> 	- [ ] Pas de cyanose *(1 grille sur 12)*
> 	- [ ] Pas de xanthélasmas *(1 grille sur 12)*
> 	- [ ] Arc cornéen *(1 grille sur 12)*
> - [ ] **30. État cardiopulmonaire *(3 grilles sur 12)***
> - [ ] **31. Inspection des membres inférieurs *(1 grille sur 12)***
> 	- [ ] Recherche de signes de TVP
> 	- [ ] Œdème, chaleur, rougeur
> 	- [ ] Signe de Homans
> - [ ] **32. Palpation abdominale *(1 grille sur 12)***
> 	- [ ] Recherche d'organomégalie
> 	- [ ] Douleur épigastrique
> - [ ] **33. Inspection des jambes *(1 grille sur 12)***
> - [ ] **34. Signes spécifiques du pneumothorax *(1 grille sur 12)***
> 	- [ ] Asymétrie thoracique
> 	- [ ] Diminution de l'ampliation thoracique du côté atteint
> 	- [ ] Déviation trachéale (si pneumothorax sous tension)
> - [ ] **35. Examen vasculaire *(Reflux gastro-œsophagien)***
> - [ ] **36. Examen abdominal *(Reflux gastro-œsophagien)***
> - [ ] **37. Recherche de signes d'alarme *(Reflux gastro-œsophagien)***
> 	- [ ] Dysphagie
> 	- [ ] Amaigrissement
> 	- [ ] Anémie
> 	- [ ] Hémorragie digestive
> - [ ] **38. Désinfection des mains *(Péricardite / Myopéricardite)***
> - [ ] **39. Examen pulmonaire *(Péricardite / Myopéricardite)***
> 	- [ ] Auscultation plages antérieures, postérieures et latérales
> 	- [ ] Percussion
> - [ ] **40. Position du patient pendant l'examen *(Péricardite / Myopéricardite)***
> 	- [ ] A fait coucher le patient à un moment du status
> - [ ] **41. Examen pulmonaire - inspection et percussion *(1 grille sur 12)***
> 	- [ ] Percussion
> 	- [ ] Ampliation thoracique
> - [ ] **42. Examen pulmonaire - auscultation *(1 grille sur 12)***
> 	- [ ] Plages postérieures (min 4)
> 	- [ ] Plages latérales des deux côtés
> 	- [ ] Réalise l'examen en comparant systématiquement les deux côtés
> - [ ] **43. Examen général *(1 grille sur 12)***
> 	- [ ] Extrémités dont les ongles
> 	- [ ] Langue
> - [ ] **44. Examen vasculaire périphérique *(1 grille sur 12)***
> 	- [ ] Pouls périphériques aux 4 extrémités
> 	- [ ] Temps de recoloration des extrémités
> 	- [ ] Recherche de souffle carotidien
> 	- [ ] Recherche de souffles fémoraux
> 	- [ ] Recherche de souffle abdominal
> - [ ] **45. Recherche de signes d'insuffisance cardiaque *(3 grilles sur 12)***
> 	- [ ] Œdèmes des membres inférieurs (signe du godet) *(1 grille sur 12)*
> 	- [ ] Turgescence jugulaire *(1 grille sur 12)*
> 	- [ ] Reflux hépato-jugulaire *(2 grilles sur 12)*
> 	- [ ] Pas de turgescence jugulaire *(1 grille sur 12)*
> 	- [ ] Pas de reflux hépato-jugulaire *(1 grille sur 12)*
> 	- [ ] Pas d'hépatomégalie *(1 grille sur 12)*
> 	- [ ] Pas d'œdèmes des membres inférieurs *(1 grille sur 12)*
> 	- [ ] Pas d'ascite *(1 grille sur 12)*
> 	- [ ] Œdèmes prétibiaux *(1 grille sur 12)*
> 	- [ ] Hépatomégalie *(1 grille sur 12)*
> 	- [ ] Auscultation pulmonaire *(1 grille sur 12)*
> - [ ] **46. Signes vitaux *(1 grille sur 12)***
> 	- [ ] SpO2 98% en air ambiant
> - [ ] **47. Auscultation pulmonaire *(1 grille sur 12)***
> 	- [ ] Pas de râles
> 	- [ ] Pas de sibilants
> 	- [ ] Symétrique bilatéralement
> - [ ] **48. Palpation des pouls périphériques *(1 grille sur 12)***
> 	- [ ] Pouls carotidiens symétriques
> 	- [ ] Pouls fémoraux présents
> 	- [ ] Pouls pédieux présents
> 	- [ ] Pouls tibiaux postérieurs présents
> 	- [ ] Pas de souffle abdominal
> - [ ] **49. Signes vitaux et mesures anthropométriques *(1 grille sur 12)***
> 	- [ ] Fréquence cardiaque
> 	- [ ] Tension artérielle
> 	- [ ] Fréquence respiratoire
> 	- [ ] Poids et taille
> - [ ] **50. Inspection générale et recherche de signes cardiovasculaires *(1 grille sur 12)***
> 	- [ ] Cyanose centrale
> 	- [ ] Cyanose périphérique
> 	- [ ] Signes cutanés
> 	- [ ] Inspection thoracique
> 	- [ ] Température des extrémités
> - [ ] **51. Évaluation du pouls veineux jugulaire *(1 grille sur 12)***
> 	- [ ] Positionnement du patient
> 	- [ ] Respiration par la bouche
> 	- [ ] Niveau du collapsus veineux
> 	- [ ] Réflux hépato-jugulaire
> - [ ] **52. Palpation cardiovasculaire *(1 grille sur 12)***
> 	- [ ] Pouls artériels
> 	- [ ] Choc de pointe
> 	- [ ] Aire précordiale
> 	- [ ] 2ème espace intercostal droit
> 	- [ ] Creux épigastrique
> - [ ] **53. Auscultation cardiaque systématique *(1 grille sur 12)***
> 	- [ ] 5 foyers d'auscultation
> 	- [ ] Identification B1 et B2
> 	- [ ] Utilisation cloche et membrane
> 	- [ ] Position du patient
> 	- [ ] Recherche de souffles et bruits surajoutés
> - [ ] **54. Auscultation des carotides *(1 grille sur 12)***
> 	- [ ] Auscultation bilatérale des carotides
> 	- [ ] Recherche de souffles carotidiens
> 	- [ ] Corrélation avec examen cardiaque

> [!success] 💊 Management — partagé par plusieurs diagnostics
> - [ ] **1. Hypothèses diagnostiques *(Embolie pulmonaire · Infarctus du myocarde / SCA · Pneumothorax · Péricardite / Myopéricardite — 4 grilles sur 12)***
> 	- [ ] Péricardite aiguë *(Péricardite / Myopéricardite — 1 grille sur 12)*
> - [ ] **2. Examens complémentaires urgents *(Embolie pulmonaire · Infarctus du myocarde / SCA · Pneumothorax — 3 grilles sur 12)***
> 	- [ ] ECG
> 	- [ ] Troponine T, CK-MB *(Embolie pulmonaire — 1 grille sur 12)*
> 	- [ ] Gaz du sang artériel, oxymétrie de pouls *(Pneumothorax — 1 grille sur 12)*
> 	- [ ] FSC *(Infarctus du myocarde / SCA — 1 grille sur 12)*
> 	- [ ] Échocardiographie *(Infarctus du myocarde / SCA — 1 grille sur 12)*
> - [ ] **3. Examens d'imagerie *(Embolie pulmonaire · Pneumothorax — 2 grilles sur 12)***
> 	- [ ] Échographie Doppler de compression des jambes *(Embolie pulmonaire — 1 grille sur 12)*
> 	- [ ] Échocardiographie transthoracique *(Embolie pulmonaire — 1 grille sur 12)*
> 	- [ ] Radiographie thoracique *(Embolie pulmonaire — 1 grille sur 12)*
> 	- [ ] Angiographie pulmonaire par CT *(Embolie pulmonaire — 1 grille sur 12)*
> 	- [ ] CT thoracique *(Pneumothorax — 1 grille sur 12)*
> - [ ] **4. Conseil et soutien *(Embolie pulmonaire · Pneumothorax — 2 grilles sur 12)***
> 	- [ ] Conseil sur l'arrêt du tabac
> 	- [ ] Réaction appropriée au défi concernant l'anxiété *(Embolie pulmonaire — 1 grille sur 12)*
> 	- [ ] Rassurer la patiente sur la prise en charge *(Embolie pulmonaire — 1 grille sur 12)*
> 	- [ ] Proposer présence famille/amis pour soutien *(Embolie pulmonaire — 1 grille sur 12)*
> 	- [ ] Réaction appropriée au défi de la radiographie *(Pneumothorax — 1 grille sur 12)*
> 	- [ ] Rassurer le patient sur la prise en charge *(Pneumothorax — 1 grille sur 12)*
> 	- [ ] Expliquer les prochaines étapes du traitement *(Pneumothorax — 1 grille sur 12)*
> - [ ] **5. Communication avec le patient *(Infarctus du myocarde / SCA · Pneumothorax — 2 grilles sur 12)***
> 	- [ ] Explications au patient des impressions diagnostiques préliminaires
> 	- [ ] Explication du plan de prise en charge
> 	- [ ] Utilisation d'un langage non médical et clarification des termes médicaux
> 	- [ ] Évaluation de l'accord du patient avec le plan diagnostique
> 	- [ ] Recherche des préoccupations et questions du patient
> - [ ] **6. Diagnostics différentiels *(Angor stable / Maladie coronarienne · Contusion costale · Embolie pulmonaire · Pneumothorax · Reflux gastro-œsophagien — 5 grilles sur 12)***
> 	- [ ] Contusion costale *(Contusion costale — 1 grille sur 12)*
> 	- [ ] Fracture de côte *(Contusion costale — 1 grille sur 12)*
> 	- [ ] Pneumothorax *(Contusion costale · Embolie pulmonaire — 2 grilles sur 12)*
> 	- [ ] Embolie pulmonaire *(Embolie pulmonaire · Pneumothorax — 2 grilles sur 12)*
> 	- [ ] Syndrome coronarien aigu *(Embolie pulmonaire — 1 grille sur 12)*
> 	- [ ] Pneumonie *(Embolie pulmonaire — 1 grille sur 12)*
> 	- [ ] Douleur musculosquelettique *(Embolie pulmonaire · Pneumothorax — 2 grilles sur 12)*
> 	- [ ] Reflux gastro-œsophagien *(Embolie pulmonaire — 1 grille sur 12)*
> 	- [ ] Pneumothorax spontané primaire *(Pneumothorax — 1 grille sur 12)*
> 	- [ ] Crise d'asthme *(Pneumothorax — 1 grille sur 12)*
> 	- [ ] Cardiomyopathie/myocardite *(Pneumothorax — 1 grille sur 12)*
> 	- [ ] Œsophagite peptique *(Reflux gastro-œsophagien — 1 grille sur 12)*
> 	- [ ] Hernie hiatale *(Reflux gastro-œsophagien — 1 grille sur 12)*
> 	- [ ] Angor stable *(Reflux gastro-œsophagien — 1 grille sur 12)*
> 	- [ ] Pathologie œsophagienne (sténose, cancer) *(Reflux gastro-œsophagien — 1 grille sur 12)*
> - [ ] **7. Énonce le diagnostic de suspicion principal *(Embolie pulmonaire · Pneumothorax · Reflux gastro-œsophagien — 3 grilles sur 12)***
> - [ ] **8. Examens diagnostiques *(Pneumothorax · Reflux gastro-œsophagien — 2 grilles sur 12)***
> 	- [ ] Radiographie thoracique (image typique de pneumothorax) *(Pneumothorax — 1 grille sur 12)*
> 	- [ ] Biologie : FSC, CRP, troponine, CK
> 	- [ ] Gazométrie artérielle *(Pneumothorax — 1 grille sur 12)*
> 	- [ ] ECG *(Pneumothorax — 1 grille sur 12)*
> 	- [ ] US thoracique si doute diagnostique *(Pneumothorax — 1 grille sur 12)*
> 	- [ ] ECG (éliminer cause cardiaque) *(Reflux gastro-œsophagien — 1 grille sur 12)*
> 	- [ ] Radiographie thoracique *(Reflux gastro-œsophagien — 1 grille sur 12)*
> 	- [ ] PH-métrie des 24 heures *(Reflux gastro-œsophagien — 1 grille sur 12)*
> 	- [ ] Endoscopie digestive haute (si signes d'alarme ou échec du traitement) *(Reflux gastro-œsophagien — 1 grille sur 12)*
> - [ ] **9. Prise en charge thérapeutique *(Pneumothorax · Reflux gastro-œsophagien — 2 grilles sur 12)***
> 	- [ ] Oxygénothérapie haut débit *(Pneumothorax — 1 grille sur 12)*
> 	- [ ] Analgésie adaptée *(Pneumothorax — 1 grille sur 12)*
> 	- [ ] Surveillance monitoring cardio-respiratoire *(Pneumothorax — 1 grille sur 12)*
> 	- [ ] Si pneumothorax < 2cm : observation *(Pneumothorax — 1 grille sur 12)*
> 	- [ ] Si pneumothorax > 2cm ou symptomatique : drainage thoracique *(Pneumothorax — 1 grille sur 12)*
> 	- [ ] Mesures hygiéno-diététiques *(Reflux gastro-œsophagien — 1 grille sur 12)*
> 	- [ ] Inhibiteurs de la pompe à protons (IPP) *(Reflux gastro-œsophagien — 1 grille sur 12)*
> - [ ] **10. Information du patient *(Pneumothorax · Reflux gastro-œsophagien — 2 grilles sur 12)***
> 	- [ ] Expliquer le diagnostic et le mécanisme *(Pneumothorax — 1 grille sur 12)*
> 	- [ ] Risque de récidive (30% à 2 ans) *(Pneumothorax — 1 grille sur 12)*
> 	- [ ] Importance de l'arrêt du tabac *(Pneumothorax — 1 grille sur 12)*
> 	- [ ] Signes d'alarme nécessitant une reconsultation urgente *(Pneumothorax — 1 grille sur 12)*
> 	- [ ] Expliquer la nature bénigne du RGO *(Reflux gastro-œsophagien — 1 grille sur 12)*
> 	- [ ] Importance des mesures hygiéno-diététiques *(Reflux gastro-œsophagien — 1 grille sur 12)*
> 	- [ ] Observance du traitement IPP *(Reflux gastro-œsophagien — 1 grille sur 12)*
> 	- [ ] Consulter si apparition de signes d'alarme *(Reflux gastro-œsophagien — 1 grille sur 12)*

> [!success] 💊 Management — si Angor stable / Maladie coronarienne
> - [ ] **1. Stratification du risque cardiovasculaire**
> 	- [ ] Score de risque SCORE2 ou Framingham *(1 grille sur 2)*
> 	- [ ] Évaluation du risque à 10 ans *(1 grille sur 2)*
> 	- [ ] Patient à haut risque (> 20%) *(1 grille sur 2)*
> 	- [ ] Nécessité d'une prise en charge agressive *(1 grille sur 2)*
> 	- [ ] Recherche de lésions d'organes cibles *(1 grille sur 2)*
> 	- [ ] Évaluation du risque global *(1 grille sur 2)*
> 	- [ ] Urgence de la prise en charge *(1 grille sur 2)*
> 	- [ ] Nécessité d'explorations rapides *(1 grille sur 2)*
> 	- [ ] Évaluation pronostic à court et long terme *(1 grille sur 2)*
> - [ ] **2. Examens complémentaires *(1 grille sur 2)***
> 	- [ ] ECG de repos 12 dérivations
> 	- [ ] Test d'effort sur tapis ou vélo
> 	- [ ] Échocardiographie de repos
> 	- [ ] Score calcique coronaire si doute
> 	- [ ] Coroscanner si test d'effort non concluant
> 	- [ ] Coronarographie si test positif
> 	- [ ] Bilan lipidique complet
> 	- [ ] Glycémie à jeun, HbA1c
> 	- [ ] Créatinine, microalbuminurie
> - [ ] **3. Traitement médical de l'angor stable *(1 grille sur 2)***
> - [ ] **4. Indications de revascularisation *(1 grille sur 2)***
> 	- [ ] Angor réfractaire au traitement médical optimal
> 	- [ ] Test d'ischémie fortement positif
> 	- [ ] Sténose du tronc commun > 50%
> 	- [ ] Sténose tritronculaire avec dysfonction VG
> 	- [ ] Sténose IVA proximale > 70%
> 	- [ ] Score SYNTAX pour choisir entre angioplastie et pontage
> - [ ] **5. Signes d'alarme nécessitant une prise en charge urgente *(1 grille sur 2)***
> - [ ] **6. Interprétation des symptômes et diagnostic principal *(1 grille sur 2)***
> 	- [ ] Évoque angor d'effort stable
> 	- [ ] Classe II selon classification CCS
> 	- [ ] Corrélation symptômes-effort
> 	- [ ] Élimination angor instable (pas de repos)
> - [ ] **7. Identification des facteurs de risque cardiovasculaire *(1 grille sur 2)***
> 	- [ ] Diabète non traité
> 	- [ ] Hypertension probable
> 	- [ ] Dyslipidémie
> 	- [ ] Tabagisme ancien
> 	- [ ] Surpoids
> 	- [ ] Sédentarité
> - [ ] **8. Proposition d'examens complémentaires appropriés *(1 grille sur 2)***
> 	- [ ] ECG de repos 12 dérivations
> 	- [ ] Test d'effort ou imagerie de stress
> 	- [ ] Bilan biologique
> 	- [ ] Échocardiographie de repos
> 	- [ ] Radiographie thoracique
> - [ ] **9. Initiation du traitement médical optimal *(1 grille sur 2)***
> 	- [ ] Antiagrégation plaquettaire
> 	- [ ] Bêta-bloquant
> 	- [ ] Statine
> 	- [ ] Dérivés nitrés
> 	- [ ] Traitement des facteurs de risque
> - [ ] **10. Conseils de prévention et modification du mode de vie *(1 grille sur 2)***
> 	- [ ] Arrêt tabac définitif
> 	- [ ] Activité physique régulière
> 	- [ ] Contrôle pondéral
> 	- [ ] Régime méditerranéen
> 	- [ ] Éducation thérapeutique
> - [ ] **11. Information du patient et planification du suivi *(1 grille sur 2)***
> 	- [ ] Explication du diagnostic d'angor stable
> 	- [ ] Information sur l'évolution et le pronostic
> 	- [ ] Conseils pour la vie quotidienne
> 	- [ ] Conduite à tenir en cas de crise
> 	- [ ] Suivi cardiologique régulier programmé

> [!success] 💊 Management — si Contusion costale
> - [ ] **1. Énonce le diagnostic de suspicion**
> - [ ] **2. Nomme les examens diagnostiques**
> - [ ] **3. Thérapie**
> 	- [ ] Analgésie adaptée (paracétamol, AINS, opioïdes si nécessaire)
> 	- [ ] Immobilisation relative
> 	- [ ] Physiothérapie respiratoire pour prévenir les complications
> - [ ] **4. Explique l'évolution naturelle et le pronostic**
> 	- [ ] Pas d'autre thérapie spécifique nécessaire
> 	- [ ] Guérison spontanée en 3-6 semaines
> 	- [ ] Pronostic excellent
> - [ ] **5. Rédige un certificat d'incapacité de travail**
> 	- [ ] 1 semaine d'arrêt initial
> 	- [ ] Contrôle prévu pour réévaluation
> 	- [ ] Adaptation selon l'évolution clinique

> [!success] 💊 Management — si Dissection aortique
> *Aucune grille du corpus ne documente ce diagnostic* — il est pourtant attendu de cette SSP. **Trou de révision à combler ailleurs.**

> [!success] 💊 Management — si Embolie pulmonaire
> - [ ] **1. Examens biologiques *(1 grille sur 3)***
> 	- [ ] FSC, VS, hémocultures
> 	- [ ] Gaz du sang artériel
> - [ ] **2. Communication avec la patiente *(1 grille sur 3)***
> 	- [ ] Explications à la patiente des impressions diagnostiques préliminaires
> 	- [ ] Explication du plan de prise en charge
> 	- [ ] Utilisation d'un langage non médical et clarification des termes médicaux
> 	- [ ] Évaluation de l'accord de la patiente avec le plan diagnostique
> 	- [ ] Recherche des préoccupations et questions de la patiente
> - [ ] **3. Examens diagnostiques urgents *(1 grille sur 3)***
> 	- [ ] ECG (éliminer SCA)
> 	- [ ] Radiographie thoracique
> 	- [ ] D-dimères (si probabilité faible/intermédiaire)
> 	- [ ] Gazométrie artérielle
> 	- [ ] FSC, CRP, troponine
> 	- [ ] Angio-CT thoracique si D-dimères positifs ou haute probabilité
> - [ ] **4. Prise en charge thérapeutique initiale *(1 grille sur 3)***
> 	- [ ] Oxygénothérapie si SpO2 < 94%
> 	- [ ] Analgésie adaptée
> 	- [ ] Anticoagulation si forte suspicion d'EP
> 	- [ ] Surveillance monitoring
> - [ ] **5. Information et suivi *(1 grille sur 3)***
> 	- [ ] Expliquer la gravité potentielle
> 	- [ ] Nécessité d'hospitalisation pour surveillance
> 	- [ ] Importance de l'observance thérapeutique
> 	- [ ] Contrôle INR si AVK, surveillance hémorragique
> - [ ] **6. Prévention secondaire *(1 grille sur 3)***
> 	- [ ] Arrêt du tabac impératif
> 	- [ ] Contrôle des facteurs de risque cardiovasculaire
> 	- [ ] Éviter immobilisation prolongée
> 	- [ ] Prophylaxie lors de voyages prolongés
> - [ ] **7. Indique à la patiente qu'elle devrait se rendre rapidement à l'hôpital *(1 grille sur 3)***
> - [ ] **8. Évoque le diagnostic d'embolie pulmonaire *(1 grille sur 3)***
> - [ ] **9. Évoque un diagnostic différentiel cohérent *(1 grille sur 3)***
> 	- [ ] Infarctus du myocarde
> 	- [ ] Pneumothorax
> 	- [ ] Œdème aigu pulmonaire
> 	- [ ] Pneumonie/bronchite

> [!success] 💊 Management — si Infarctus du myocarde / SCA
> - [ ] **1. Examens biologiques et toxicologiques**
> 	- [ ] Toxicologie urinaire
> 	- [ ] Troponine T, CK-MB
> - [ ] **2. Examens invasifs si indiqués**
> 	- [ ] Coronarographie
> - [ ] **3. Conseil et prévention**
> 	- [ ] Conseil sur l'arrêt des drogues illicites
> 	- [ ] Conseil sur l'arrêt du tabac
> 	- [ ] Réaction appropriée au défi concernant les médicaments
> 	- [ ] Éducation sur les facteurs de risque cardiovasculaires

> [!success] 💊 Management — si Péricardite / Myopéricardite
> - [ ] **1. Examens complémentaires demandés**
> 	- [ ] Laboratoires
> 	- [ ] ECG
> 	- [ ] Radiographie du thorax
> - [ ] **2. Réponse à la demande d'hospitalisation**
> 	- [ ] A répondu positivement à la demande du patient concernant l'hospitalisation

> [!success] 💊 Management — si Pneumothorax
> - [ ] **1. Laboratoire de base *(1 grille sur 3)***
> - [ ] **2. Gazométrie artérielle *(1 grille sur 3)***
> - [ ] **3. Radiographie thoracique (2 incidences) *(1 grille sur 3)***
> - [ ] **4. Échographie thoracique *(1 grille sur 3)***
> - [ ] **5. ECG *(1 grille sur 3)***
> - [ ] **6. Diagnostic de travail *(1 grille sur 3)***
> - [ ] **7. Oxygénothérapie *(1 grille sur 3)***
> - [ ] **8. Drainage thoracique *(1 grille sur 3)***
> - [ ] **9. Analgésie *(1 grille sur 3)***
> - [ ] **10. Position semi-assise *(1 grille sur 3)***
> - [ ] **11. Monitoring *(1 grille sur 3)***
> - [ ] **12. Hospitalisation *(1 grille sur 3)***
> - [ ] **13. Arrêt du tabac *(1 grille sur 3)***
> - [ ] **14. Radiographie de contrôle *(1 grille sur 3)***
> - [ ] **15. Prophylaxie des récidives *(1 grille sur 3)***
> - [ ] **16. Critères d'hospitalisation *(1 grille sur 3)***
> 	- [ ] Pneumothorax > 20%
> 	- [ ] Pneumothorax symptomatique
> 	- [ ] Pneumothorax bilatéral
> 	- [ ] Pneumothorax sous tension
> 	- [ ] Comorbidités pulmonaires

> [!success] 💊 Management — si Reflux gastro-œsophagien
> - [ ] **1. Suivi et surveillance**
> 	- [ ] Réévaluation à 4-8 semaines
> 	- [ ] Si amélioration : traitement à la demande
> 	- [ ] Si échec : endoscopie digestive haute
> 	- [ ] Surveillance au long cours si œsophagite
