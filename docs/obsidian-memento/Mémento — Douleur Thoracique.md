---
aliases:
  - "Mémento Douleur Thoracique"
type: memento-ecos-ssp
ssp: "Douleur Thoracique"
specialite: "Cardiologie & Vasculaire"
cas: 12
diagnostics: 7
attendus_documentes_ailleurs: 0
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

# Douleur Thoracique ⭐️

*Cardiologie & Vasculaire · 12 grilles · 7 diagnostics documentés · 1 attendu absent du corpus* — [[SSP — Douleur Thoracique]]

> [!abstract] Les 12 grilles fusionnées
> - **AMBOSS-12** — Embolie pulmonaire `premier-dd` · [grille](<file:///Users/damienfulliquet/Developer/GitHub/grilles-ecos/cases/amboss/AMBOSS-12_-_Douleur_thoracique_-_Femme_35_ans_-_Grille_ECOS.html>)
> - **AMBOSS-13** — Pneumothorax `premier-dd` · [grille](<file:///Users/damienfulliquet/Developer/GitHub/grilles-ecos/cases/amboss/AMBOSS-13_-_Douleur_thoracique_-_Homme_35_ans_-_Grille_ECOS.html>)
> - **AMBOSS-14** — Infarctus du myocarde / SCA `premier-dd` · [grille](<file:///Users/damienfulliquet/Developer/GitHub/grilles-ecos/cases/amboss/AMBOSS-14_-_Douleur_thoracique_-_Homme_45_ans_-_Grille_ECOS.html>)
> - **AZYGOS-22** — Pneumothorax `diagnostic-travail` · [grille](<file:///Users/damienfulliquet/Developer/GitHub/grilles-ecos/docs/azygos-grilles/36c2f5c1-90b6-4677-9a14-9d758632e1df.json>)
> - **German-30** — Contusion costale `corrige` · [grille](<file:///Users/damienfulliquet/Developer/GitHub/grilles-ecos/cases/german/German-30_-_Douleur_thoracique_-_Grille_ECOS.html>)
> - **German-31** — Embolie pulmonaire `corrige` · [grille](<file:///Users/damienfulliquet/Developer/GitHub/grilles-ecos/cases/german/German-31_-_Douleur_thoracique_-_Grille_ECOS.html>)
> - **German-32** — Pneumothorax `corrige` · [grille](<file:///Users/damienfulliquet/Developer/GitHub/grilles-ecos/cases/german/German-32_-_Douleur_thoracique_-_Grille_ECOS.html>)
> - **German-33** — Reflux gastro-œsophagien `corrige` · [grille](<file:///Users/damienfulliquet/Developer/GitHub/grilles-ecos/cases/german/German-33_-_Douleur_thoracique_-_Grille_ECOS.html>)
> - **RESCOS-34** — Péricardite / Myopéricardite `explicite` · [grille](<file:///Users/damienfulliquet/Developer/GitHub/grilles-ecos/cases/rescos/RESCOS-34_-_Douleur_thoracique_-_Grille_ECOS.html>)
> - **RESCOS-35** — Embolie pulmonaire `explicite` · [grille](<file:///Users/damienfulliquet/Developer/GitHub/grilles-ecos/cases/rescos/RESCOS-35_-_Douleur_thoracique_-_Grille_ECOS.html>)
> - **RESCOS-36** — Angor stable / Maladie coronarienne `premier-dd` · [grille](<file:///Users/damienfulliquet/Developer/GitHub/grilles-ecos/cases/rescos/RESCOS-36_-_Douleur_thoracique_-_Grille_ECOS.html>)
> - **RESCOS-37** — Angor stable / Maladie coronarienne `explicite` · [grille](<file:///Users/damienfulliquet/Developer/GitHub/grilles-ecos/cases/rescos/RESCOS-37_-_Douleur_thoracique_-_ECC_Cardiologie_-_Grille_ECOS.html>)

> [!note] 📋 Anamnèse
> - [ ] **1. Motif de consultation *(4 grilles sur 12)***
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
> - [ ] **5. Antécédents médicaux *(8 grilles sur 12)***
> - [ ] **6. Antécédents chirurgicaux *(4 grilles sur 12)***
> - [ ] **7. Allergies *(8 grilles sur 12)***
> - [ ] **8. Médicaments actuels *(8 grilles sur 12)***
> - [ ] **9. Hospitalisations et contacts malades *(1 grille sur 12)***
> 	- [ ] Hospitalisations
> 	- [ ] Contacts malades
> - [ ] **10. Antécédents familiaux *(8 grilles sur 12)***
> - [ ] **11. Habitudes et mode de vie *(7 grilles sur 12)***
> 	- [ ] Occupation *(3 grilles sur 12)*
> 	- [ ] Domicile *(3 grilles sur 12)*
> 	- [ ] Alcool *(4 grilles sur 12)*
> 	- [ ] Drogues illicites *(3 grilles sur 12)*
> 	- [ ] Tabac *(4 grilles sur 12)*
> 	- [ ] Exercice *(2 grilles sur 12)*
> 	- [ ] Alimentation *(1 grille sur 12)*
> 	- [ ] Consommation d'amphétamines (durée, fréquence, dernière prise) *(Infarctus du myocarde / SCA)*
> 	- [ ] Médicaments actuels *(Péricardite / Myopéricardite)*
> 	- [ ] Cannabis *(Péricardite / Myopéricardite)*
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
> - [ ] **61. Activités sportives, loisirs *(Contusion costale)***
> - [ ] **62. Anamnèse sociale *(4 grilles sur 12)***
> - [ ] **63. Identification des symptômes *(3 grilles sur 12)***
> - [ ] **64. Début et évolution des symptômes *(1 grille sur 12)***
> - [ ] **65. Intensité de la douleur *(3 grilles sur 12)***
> - [ ] **66. Caractère de la douleur *(3 grilles sur 12)***
> - [ ] **67. Douleur liée à la respiration *(3 grilles sur 12)***
> - [ ] **68. Irradiation de la douleur *(3 grilles sur 12)***
> - [ ] **69. Facteurs modulateurs *(3 grilles sur 12)***
> 	- [ ] Facteur atténuant *(Péricardite / Myopéricardite)*
> 	- [ ] Facteur aggravant *(Péricardite / Myopéricardite)*
> - [ ] **70. Traumatisme thoracique *(3 grilles sur 12)***
> - [ ] **71. Facteurs de risque cardiovasculaire *(4 grilles sur 12)***
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
> 	- [ ] Médicaments actuels *(1 grille sur 12)*
> 	- [ ] Alcool *(1 grille sur 12)*
> - [ ] **72. Facteurs de risque d'embolie pulmonaire (Score de Wells) *(2 grilles sur 12)***
> 	- [ ] Œdème/douleur du mollet
> 	- [ ] Voyage récent
> 	- [ ] Chirurgie récente
> 	- [ ] Cancer actif
> 	- [ ] Antécédents familiaux de thrombophilie
> 	- [ ] Contraceptifs oraux *(1 grille sur 12)*
> 	- [ ] Grossesse *(1 grille sur 12)*
> - [ ] **73. Signes généraux *(3 grilles sur 12)***
> - [ ] **74. Début et évolution *(1 grille sur 12)***
> - [ ] **75. Événement déclenchant *(1 grille sur 12)***
> - [ ] **76. Antécédents cardiaques *(1 grille sur 12)***
> - [ ] **77. Asthme *(1 grille sur 12)***
> - [ ] **78. Antécédents de TVP/EP *(1 grille sur 12)***
> - [ ] **79. Durée des symptômes *(Reflux gastro-œsophagien)***
> - [ ] **80. Facteurs déclenchants et modulateurs *(Reflux gastro-œsophagien)***
> - [ ] **81. Lien avec l'effort physique *(Reflux gastro-œsophagien)***
> - [ ] **82. Raison de la visite *(Péricardite / Myopéricardite)***
> 	- [ ] Douleur à la poitrine
> - [ ] **83. Circonstances de survenue *(Péricardite / Myopéricardite)***
> 	- [ ] Circonstances
> - [ ] **84. Antécédents médicaux récents *(Péricardite / Myopéricardite)***
> 	- [ ] État grippal
> 	- [ ] Pneumonie
> - [ ] **85. Voyages récents *(Péricardite / Myopéricardite)***
> 	- [ ] Voyages récents
> - [ ] **86. Douleur thoracique - évolution temporelle *(1 grille sur 12)***
> 	- [ ] Chronologie
> 	- [ ] Évolution
> - [ ] **87. Antécédents et comorbidités *(1 grille sur 12)***
> 	- [ ] Maladies
> 	- [ ] Hospitalisations
> 	- [ ] Médicaments actuels
> 	- [ ] Allergies
> - [ ] **88. Facteurs de risque *(1 grille sur 12)***
> 	- [ ] Tabagisme
> 	- [ ] Voyages récents
> 	- [ ] Chirurgie/immobilisation récente
> 	- [ ] Médicaments actuels
> 	- [ ] Antécédents d'embolie pulmonaire/angine de poitrine/AVC
> - [ ] **89. Représentation de la maladie *(1 grille sur 12)***
> 	- [ ] Peur d'un cancer pulmonaire comme son mari
> - [ ] **90. Circonstances déclenchantes *(1 grille sur 12)***
> 	- [ ] Effort physique
> 	- [ ] Stress émotionnel
> 	- [ ] Froid
> 	- [ ] Repas copieux
> 	- [ ] Jamais au repos
> 	- [ ] Pas la nuit
> - [ ] **91. Évolution dans le temps *(1 grille sur 12)***
> 	- [ ] Début
> 	- [ ] Fréquence croissante
> 	- [ ] Seuil d'effort diminué
> 	- [ ] Caractéristiques stables
> - [ ] **92. Classification CCS de l'angor *(1 grille sur 12)***
> 	- [ ] Classe I: Activités quotidiennes normales
> 	- [ ] Classe II: Limitation légère
> 	- [ ] Classe III: Limitation marquée
> 	- [ ] Classe IV: Angor au moindre effort ou repos
> - [ ] **93. Antécédents et traitements *(1 grille sur 12)***
> 	- [ ] Cholestérol élevé
> 	- [ ] Automédication aspirine
> - [ ] **94. Facteurs déclenchants et circonstances d'apparition *(1 grille sur 12)***
> 	- [ ] Facteur déclenchant 1er épisode
> 	- [ ] Facteur déclenchant 2ème épisode
> 	- [ ] Relation à l'effort
> 	- [ ] Facteurs soulageants
> 	- [ ] Évolution des crises
> - [ ] **95. Symptômes associés et recherche d'insuffisance cardiaque *(1 grille sur 12)***
> 	- [ ] Dyspnée d'effort
> 	- [ ] Dyspnée à la fin des escaliers
> 	- [ ] Orthopnée
> 	- [ ] Dyspnée paroxystique nocturne
> 	- [ ] Œdèmes membres inférieurs
> 	- [ ] Palpitations
> - [ ] **96. Classification de la sévérité (classes d'angine) *(1 grille sur 12)***
> 	- [ ] Impact fonctionnel
> 	- [ ] Limitation des activités
> 	- [ ] Angor au repos
> 	- [ ] Classification probable
> - [ ] **97. Antécédents personnels cardiovasculaires *(1 grille sur 12)***
> 	- [ ] Diabète
> 	- [ ] Hypertension artérielle
> 	- [ ] Hypercholestérolémie
> 	- [ ] Affections cardiaques
> 	- [ ] Hospitalisations
> - [ ] **98. Antécédents familiaux cardiovasculaires *(1 grille sur 12)***
> 	- [ ] Mère
> 	- [ ] Père
> 	- [ ] Frère
> 	- [ ] Oncle maternel
> 	- [ ] Recherche mort subite
> - [ ] **99. Anamnèse socioprofessionnelle et impact *(1 grille sur 12)***
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
> - [ ] **9. Signes vitaux *(2 grilles sur 12)***
> 	- [ ] SpO2 98% en air ambiant *(1 grille sur 12)*
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
> - [ ] **23. Palpation des pouls périphériques *(2 grilles sur 12)***
> 	- [ ] Pouls carotidiens symétriques *(1 grille sur 12)*
> 	- [ ] Pouls fémoraux présents *(1 grille sur 12)*
> 	- [ ] Pouls pédieux présents *(1 grille sur 12)*
> 	- [ ] Pouls tibiaux postérieurs présents *(1 grille sur 12)*
> 	- [ ] Pas de souffle abdominal *(1 grille sur 12)*
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
> - [ ] **46. Auscultation pulmonaire *(1 grille sur 12)***
> 	- [ ] Pas de râles
> 	- [ ] Pas de sibilants
> 	- [ ] Symétrique bilatéralement
> - [ ] **47. Signes vitaux et mesures anthropométriques *(1 grille sur 12)***
> 	- [ ] Fréquence cardiaque
> 	- [ ] Tension artérielle
> 	- [ ] Fréquence respiratoire
> 	- [ ] Poids et taille
> - [ ] **48. Inspection générale et recherche de signes cardiovasculaires *(1 grille sur 12)***
> 	- [ ] Cyanose centrale
> 	- [ ] Cyanose périphérique
> 	- [ ] Signes cutanés
> 	- [ ] Inspection thoracique
> 	- [ ] Température des extrémités
> - [ ] **49. Évaluation du pouls veineux jugulaire *(1 grille sur 12)***
> 	- [ ] Positionnement du patient
> 	- [ ] Respiration par la bouche
> 	- [ ] Niveau du collapsus veineux
> 	- [ ] Réflux hépato-jugulaire
> - [ ] **50. Palpation cardiovasculaire *(1 grille sur 12)***
> 	- [ ] Pouls artériels
> 	- [ ] Choc de pointe
> 	- [ ] Aire précordiale
> 	- [ ] 2ème espace intercostal droit
> 	- [ ] Creux épigastrique
> - [ ] **51. Auscultation cardiaque systématique *(1 grille sur 12)***
> 	- [ ] 5 foyers d'auscultation
> 	- [ ] Identification B1 et B2
> 	- [ ] Utilisation cloche et membrane
> 	- [ ] Position du patient
> 	- [ ] Recherche de souffles et bruits surajoutés
> - [ ] **52. Auscultation des carotides *(1 grille sur 12)***
> 	- [ ] Auscultation bilatérale des carotides
> 	- [ ] Recherche de souffles carotidiens
> 	- [ ] Corrélation avec examen cardiaque

> [!success] 💊 Management — partagé par plusieurs diagnostics
> - [ ] **1. Communication avec le patient *(2 grilles sur 12)* — *Infarctus du myocarde / SCA · Pneumothorax***
> 	- [ ] Explications au patient des impressions diagnostiques préliminaires
> 	- [ ] Explication du plan de prise en charge
> 	- [ ] Utilisation d'un langage non médical et clarification des termes médicaux
> 	- [ ] Évaluation de l'accord du patient avec le plan diagnostique
> 	- [ ] Recherche des préoccupations et questions du patient
> - [ ] **2. Énonce le diagnostic de suspicion principal *(3 grilles sur 12)* — *Embolie pulmonaire · Pneumothorax · Reflux gastro-œsophagien***

> [!success] 💊 Management — si Angor stable / Maladie coronarienne
> - [ ] **1. Diagnostics différentiels *(1 grille sur 2)***
> - [ ] **2. Stratification du risque cardiovasculaire**
> 	- [ ] Score de risque SCORE2 ou Framingham *(1 grille sur 2)*
> 	- [ ] Évaluation du risque à 10 ans *(1 grille sur 2)*
> 	- [ ] Patient à haut risque (> 20%) *(1 grille sur 2)*
> 	- [ ] Nécessité d'une prise en charge agressive *(1 grille sur 2)*
> 	- [ ] Recherche de lésions d'organes cibles *(1 grille sur 2)*
> 	- [ ] Évaluation du risque global *(1 grille sur 2)*
> 	- [ ] Urgence de la prise en charge *(1 grille sur 2)*
> 	- [ ] Nécessité d'explorations rapides *(1 grille sur 2)*
> 	- [ ] Évaluation pronostic à court et long terme *(1 grille sur 2)*
> - [ ] **3. Examens complémentaires *(1 grille sur 2)***
> 	- [ ] ECG de repos 12 dérivations
> 	- [ ] Test d'effort sur tapis ou vélo
> 	- [ ] Échocardiographie de repos
> 	- [ ] Score calcique coronaire si doute
> 	- [ ] Coroscanner si test d'effort non concluant
> 	- [ ] Coronarographie si test positif
> 	- [ ] Bilan lipidique complet
> 	- [ ] Glycémie à jeun, HbA1c
> 	- [ ] Créatinine, microalbuminurie
> - [ ] **4. Traitement médical de l'angor stable *(1 grille sur 2)***
> - [ ] **5. Indications de revascularisation *(1 grille sur 2)***
> 	- [ ] Angor réfractaire au traitement médical optimal
> 	- [ ] Test d'ischémie fortement positif
> 	- [ ] Sténose du tronc commun > 50%
> 	- [ ] Sténose tritronculaire avec dysfonction VG
> 	- [ ] Sténose IVA proximale > 70%
> 	- [ ] Score SYNTAX pour choisir entre angioplastie et pontage
> - [ ] **6. Signes d'alarme nécessitant une prise en charge urgente *(1 grille sur 2)***
> - [ ] **7. Interprétation des symptômes et diagnostic principal *(1 grille sur 2)***
> 	- [ ] Évoque angor d'effort stable
> 	- [ ] Classe II selon classification CCS
> 	- [ ] Corrélation symptômes-effort
> 	- [ ] Élimination angor instable (pas de repos)
> - [ ] **8. Identification des facteurs de risque cardiovasculaire *(1 grille sur 2)***
> 	- [ ] Diabète non traité
> 	- [ ] Hypertension probable
> 	- [ ] Dyslipidémie
> 	- [ ] Tabagisme ancien
> 	- [ ] Surpoids
> 	- [ ] Sédentarité
> - [ ] **9. Proposition d'examens complémentaires appropriés *(1 grille sur 2)***
> 	- [ ] ECG de repos 12 dérivations
> 	- [ ] Test d'effort ou imagerie de stress
> 	- [ ] Bilan biologique
> 	- [ ] Échocardiographie de repos
> 	- [ ] Radiographie thoracique
> - [ ] **10. Initiation du traitement médical optimal *(1 grille sur 2)***
> 	- [ ] Antiagrégation plaquettaire
> 	- [ ] Bêta-bloquant
> 	- [ ] Statine
> 	- [ ] Dérivés nitrés
> 	- [ ] Traitement des facteurs de risque
> - [ ] **11. Conseils de prévention et modification du mode de vie *(1 grille sur 2)***
> 	- [ ] Arrêt tabac définitif
> 	- [ ] Activité physique régulière
> 	- [ ] Contrôle pondéral
> 	- [ ] Régime méditerranéen
> 	- [ ] Éducation thérapeutique
> - [ ] **12. Information du patient et planification du suivi *(1 grille sur 2)***
> 	- [ ] Explication du diagnostic d'angor stable
> 	- [ ] Information sur l'évolution et le pronostic
> 	- [ ] Conseils pour la vie quotidienne
> 	- [ ] Conduite à tenir en cas de crise
> 	- [ ] Suivi cardiologique régulier programmé

> [!success] 💊 Management — si Contusion costale
> - [ ] **1. Énonce le diagnostic de suspicion**
> - [ ] **2. Diagnostics différentiels**
> 	- [ ] Contusion costale
> 	- [ ] Fracture de côte
> 	- [ ] Pneumothorax
> - [ ] **3. Nomme les examens diagnostiques**
> - [ ] **4. Thérapie**
> 	- [ ] Analgésie adaptée (paracétamol, AINS, opioïdes si nécessaire)
> 	- [ ] Immobilisation relative
> 	- [ ] Physiothérapie respiratoire pour prévenir les complications
> - [ ] **5. Explique l'évolution naturelle et le pronostic**
> 	- [ ] Pas d'autre thérapie spécifique nécessaire
> 	- [ ] Guérison spontanée en 3-6 semaines
> 	- [ ] Pronostic excellent
> - [ ] **6. Rédige un certificat d'incapacité de travail**
> 	- [ ] 1 semaine d'arrêt initial
> 	- [ ] Contrôle prévu pour réévaluation
> 	- [ ] Adaptation selon l'évolution clinique

> [!success] 💊 Management — si Dissection aortique
> *Aucune grille du corpus ne documente ce diagnostic* — il est pourtant attendu de cette SSP. **Trou de révision à combler ailleurs.**

> [!success] 💊 Management — si Embolie pulmonaire
> - [ ] **1. Hypothèses diagnostiques *(1 grille sur 3)***
> - [ ] **2. Examens complémentaires urgents *(1 grille sur 3)***
> 	- [ ] ECG
> 	- [ ] Troponine T, CK-MB
> - [ ] **3. Examens d'imagerie *(1 grille sur 3)***
> 	- [ ] Échographie Doppler de compression des jambes
> 	- [ ] Échocardiographie transthoracique
> 	- [ ] Radiographie thoracique
> 	- [ ] Angiographie pulmonaire par CT
> - [ ] **4. Examens biologiques *(1 grille sur 3)***
> 	- [ ] FSC, VS, hémocultures
> 	- [ ] Gaz du sang artériel
> - [ ] **5. Communication avec la patiente *(1 grille sur 3)***
> 	- [ ] Explications à la patiente des impressions diagnostiques préliminaires
> 	- [ ] Explication du plan de prise en charge
> 	- [ ] Utilisation d'un langage non médical et clarification des termes médicaux
> 	- [ ] Évaluation de l'accord de la patiente avec le plan diagnostique
> 	- [ ] Recherche des préoccupations et questions de la patiente
> - [ ] **6. Conseil et soutien *(1 grille sur 3)***
> 	- [ ] Conseil sur l'arrêt du tabac
> 	- [ ] Réaction appropriée au défi concernant l'anxiété
> 	- [ ] Rassurer la patiente sur la prise en charge
> 	- [ ] Proposer présence famille/amis pour soutien
> - [ ] **7. Diagnostics différentiels *(2 grilles sur 3)***
> 	- [ ] Pneumothorax
> 	- [ ] Embolie pulmonaire *(1 grille sur 3)*
> 	- [ ] Syndrome coronarien aigu *(1 grille sur 3)*
> 	- [ ] Pneumonie *(1 grille sur 3)*
> 	- [ ] Douleur musculosquelettique *(1 grille sur 3)*
> 	- [ ] Reflux gastro-œsophagien *(1 grille sur 3)*
> 	- [ ] Infarctus du myocarde *(1 grille sur 3)*
> 	- [ ] Œdème aigu pulmonaire *(1 grille sur 3)*
> 	- [ ] Pneumonie/bronchite *(1 grille sur 3)*
> - [ ] **8. Examens diagnostiques urgents *(1 grille sur 3)***
> 	- [ ] ECG (éliminer SCA)
> 	- [ ] Radiographie thoracique
> 	- [ ] D-dimères (si probabilité faible/intermédiaire)
> 	- [ ] Gazométrie artérielle
> 	- [ ] FSC, CRP, troponine
> 	- [ ] Angio-CT thoracique si D-dimères positifs ou haute probabilité
> - [ ] **9. Prise en charge thérapeutique initiale *(1 grille sur 3)***
> 	- [ ] Oxygénothérapie si SpO2 < 94%
> 	- [ ] Analgésie adaptée
> 	- [ ] Anticoagulation si forte suspicion d'EP
> 	- [ ] Surveillance monitoring
> - [ ] **10. Information et suivi *(1 grille sur 3)***
> 	- [ ] Expliquer la gravité potentielle
> 	- [ ] Nécessité d'hospitalisation pour surveillance
> 	- [ ] Importance de l'observance thérapeutique
> 	- [ ] Contrôle INR si AVK, surveillance hémorragique
> - [ ] **11. Prévention secondaire *(1 grille sur 3)***
> 	- [ ] Arrêt du tabac impératif
> 	- [ ] Contrôle des facteurs de risque cardiovasculaire
> 	- [ ] Éviter immobilisation prolongée
> 	- [ ] Prophylaxie lors de voyages prolongés
> - [ ] **12. Indique à la patiente qu'elle devrait se rendre rapidement à l'hôpital *(1 grille sur 3)***
> - [ ] **13. Évoque le diagnostic d'embolie pulmonaire *(1 grille sur 3)***

> [!success] 💊 Management — si Infarctus du myocarde / SCA
> - [ ] **1. Hypothèses diagnostiques**
> - [ ] **2. Examens complémentaires urgents**
> 	- [ ] ECG
> 	- [ ] FSC
> 	- [ ] Échocardiographie
> - [ ] **3. Examens biologiques et toxicologiques**
> 	- [ ] Toxicologie urinaire
> 	- [ ] Troponine T, CK-MB
> - [ ] **4. Examens invasifs si indiqués**
> 	- [ ] Coronarographie
> - [ ] **5. Conseil et prévention**
> 	- [ ] Conseil sur l'arrêt des drogues illicites
> 	- [ ] Conseil sur l'arrêt du tabac
> 	- [ ] Réaction appropriée au défi concernant les médicaments
> 	- [ ] Éducation sur les facteurs de risque cardiovasculaires

> [!success] 💊 Management — si Péricardite / Myopéricardite
> - [ ] **1. Hypothèses diagnostiques**
> 	- [ ] Péricardite aiguë
> - [ ] **2. Examens complémentaires demandés**
> 	- [ ] Laboratoires
> 	- [ ] ECG
> 	- [ ] Radiographie du thorax
> - [ ] **3. Réponse à la demande d'hospitalisation**
> 	- [ ] A répondu positivement à la demande du patient concernant l'hospitalisation

> [!success] 💊 Management — si Pneumothorax
> - [ ] **1. Hypothèses diagnostiques *(1 grille sur 3)***
> - [ ] **2. Examens complémentaires urgents *(1 grille sur 3)***
> 	- [ ] ECG
> 	- [ ] Gaz du sang artériel, oxymétrie de pouls
> - [ ] **3. Examens d'imagerie *(1 grille sur 3)***
> 	- [ ] CT thoracique
> - [ ] **4. Conseil et soutien *(1 grille sur 3)***
> 	- [ ] Conseil sur l'arrêt du tabac
> 	- [ ] Réaction appropriée au défi de la radiographie
> 	- [ ] Rassurer le patient sur la prise en charge
> 	- [ ] Expliquer les prochaines étapes du traitement
> - [ ] **5. Laboratoire de base *(1 grille sur 3)***
> - [ ] **6. Gazométrie artérielle *(1 grille sur 3)***
> - [ ] **7. Radiographie thoracique (2 incidences) *(1 grille sur 3)***
> - [ ] **8. Échographie thoracique *(1 grille sur 3)***
> - [ ] **9. ECG *(1 grille sur 3)***
> - [ ] **10. Diagnostic de travail *(1 grille sur 3)***
> - [ ] **11. Oxygénothérapie *(1 grille sur 3)***
> - [ ] **12. Drainage thoracique *(1 grille sur 3)***
> - [ ] **13. Analgésie *(1 grille sur 3)***
> - [ ] **14. Position semi-assise *(1 grille sur 3)***
> - [ ] **15. Monitoring *(1 grille sur 3)***
> - [ ] **16. Hospitalisation *(1 grille sur 3)***
> - [ ] **17. Arrêt du tabac *(1 grille sur 3)***
> - [ ] **18. Radiographie de contrôle *(1 grille sur 3)***
> - [ ] **19. Prophylaxie des récidives *(1 grille sur 3)***
> - [ ] **20. Diagnostics différentiels *(1 grille sur 3)***
> 	- [ ] Embolie pulmonaire
> 	- [ ] Douleur musculosquelettique
> 	- [ ] Pneumothorax spontané primaire
> 	- [ ] Crise d'asthme
> 	- [ ] Cardiomyopathie/myocardite
> - [ ] **21. Examens diagnostiques *(1 grille sur 3)***
> 	- [ ] Radiographie thoracique (image typique de pneumothorax)
> 	- [ ] Biologie : FSC, CRP, troponine, CK
> 	- [ ] Gazométrie artérielle
> 	- [ ] ECG
> 	- [ ] US thoracique si doute diagnostique
> - [ ] **22. Prise en charge thérapeutique *(1 grille sur 3)***
> 	- [ ] Oxygénothérapie haut débit
> 	- [ ] Analgésie adaptée
> 	- [ ] Surveillance monitoring cardio-respiratoire
> 	- [ ] Si pneumothorax < 2cm : observation
> 	- [ ] Si pneumothorax > 2cm ou symptomatique : drainage thoracique
> - [ ] **23. Critères d'hospitalisation *(1 grille sur 3)***
> 	- [ ] Pneumothorax > 20%
> 	- [ ] Pneumothorax symptomatique
> 	- [ ] Pneumothorax bilatéral
> 	- [ ] Pneumothorax sous tension
> 	- [ ] Comorbidités pulmonaires
> - [ ] **24. Information du patient *(1 grille sur 3)***
> 	- [ ] Expliquer le diagnostic et le mécanisme
> 	- [ ] Risque de récidive (30% à 2 ans)
> 	- [ ] Importance de l'arrêt du tabac
> 	- [ ] Signes d'alarme nécessitant une reconsultation urgente

> [!success] 💊 Management — si Reflux gastro-œsophagien
> - [ ] **1. Diagnostics différentiels**
> 	- [ ] Œsophagite peptique
> 	- [ ] Hernie hiatale
> 	- [ ] Angor stable
> 	- [ ] Pathologie œsophagienne (sténose, cancer)
> - [ ] **2. Examens diagnostiques**
> 	- [ ] Biologie : FSC, CRP, troponine, CK
> 	- [ ] ECG (éliminer cause cardiaque)
> 	- [ ] Radiographie thoracique
> 	- [ ] PH-métrie des 24 heures
> 	- [ ] Endoscopie digestive haute (si signes d'alarme ou échec du traitement)
> - [ ] **3. Prise en charge thérapeutique**
> 	- [ ] Mesures hygiéno-diététiques
> 	- [ ] Inhibiteurs de la pompe à protons (IPP)
> - [ ] **4. Information du patient**
> 	- [ ] Expliquer la nature bénigne du RGO
> 	- [ ] Importance des mesures hygiéno-diététiques
> 	- [ ] Observance du traitement IPP
> 	- [ ] Consulter si apparition de signes d'alarme
> - [ ] **5. Suivi et surveillance**
> 	- [ ] Réévaluation à 4-8 semaines
> 	- [ ] Si amélioration : traitement à la demande
> 	- [ ] Si échec : endoscopie digestive haute
> 	- [ ] Surveillance au long cours si œsophagite
