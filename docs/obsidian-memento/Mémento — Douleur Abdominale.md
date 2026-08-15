---
aliases:
  - "Mémento Douleur Abdominale"
type: memento-ecos-ssp
ssp: "Douleur Abdominale"
specialite: "Gastro-Hépatologie"
cas: 20
diagnostics: 18
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
> - 🔬 = Management : examens complémentaires
> - 💊 = Management : prise en charge attendue
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
> ⚠️ **Le suffixe parle des formulations, pas du contenu clinique.** Le
> rapprochement entre grilles est encore purement lexical : deux grilles qui
> disent la même chose autrement (« Motif de consultation » et « Motif de
> consultation principal », « Allergies » et « Allergies connues ») donnent
> **deux items distincts**, chacun marqué comme partiel. Un `*(1 grille sur 2)*`
> ne veut donc pas dire que l'autre grille néglige la question — seulement
> qu'elle l'écrit autrement. Tant que le vocabulaire canonique n'est pas
> rempli, lisez les libellés voisins ensemble.

# Douleur Abdominale ⭐️

*Gastro-Hépatologie · 20 grilles · 18 diagnostics distincts* — [[SSP — Douleur Abdominale]]

> [!abstract] Les 20 grilles fusionnées
> - **AMBOSS-1** — Cholécystite aiguë `premier-dd` · [grille](<file:///Users/damienfulliquet/Developer/GitHub/grilles-ecos/cases/amboss/AMBOSS-1_-_Douleurs_abdominales_-_Femme_47_ans_-_Grille_ECOS.html>)
> - **AMBOSS-2** — Appendicite aiguë `premier-dd` · [grille](<file:///Users/damienfulliquet/Developer/GitHub/grilles-ecos/cases/amboss/AMBOSS-2_-_Douleurs_abdominales_-_Femme_23_ans_-_Grille_ECOS.html>)
> - **AMBOSS-3** — Cancer de l'ovaire `premier-dd` · [grille](<file:///Users/damienfulliquet/Developer/GitHub/grilles-ecos/cases/amboss/AMBOSS-3_-_Douleurs_abdominales_-_Femme_34_ans_-_Grille_ECOS.html>)
> - **AMBOSS-15** — Maladie cœliaque `premier-dd` · [grille](<file:///Users/damienfulliquet/Developer/GitHub/grilles-ecos/cases/amboss/AMBOSS-15_-_Douleur_abdominale_chronique_-_Garc_on_6_ans_-_Grille_ECOS.html>)
> - **AZYGOS-14** — Cholécystite aiguë `diagnostic-travail` · [grille](<file:///Users/damienfulliquet/Developer/GitHub/grilles-ecos/.azygos-extraction/85052041-2d60-4b4f-b865-642bec286e27.json>)
> - **AZYGOS-16** — Purpura de Schönlein-Henoch (vascularite à IgA) `diagnostic-travail` · [grille](<file:///Users/damienfulliquet/Developer/GitHub/grilles-ecos/.azygos-extraction/e9e0065d-8071-4a0c-bf41-f041635274fa.json>)
> - **German-15** — Diverticulite sigmoïdienne non compliquée `corrige` · [grille](<file:///Users/damienfulliquet/Developer/GitHub/grilles-ecos/cases/german/German-15_-_Douleur_abdominale_-_Grille_ECOS.html>)
> - **German-16** — Douleurs abdominales non spécifiques `premier-dd` · [grille](<file:///Users/damienfulliquet/Developer/GitHub/grilles-ecos/cases/german/German-16_-_Douleur_abdominale_-_Grille_ECOS.html>)
> - **German-17** — Endométriose pelvienne `corrige` · [grille](<file:///Users/damienfulliquet/Developer/GitHub/grilles-ecos/cases/german/German-17_-_Douleur_abdominale_-_Grille_ECOS.html>)
> - **German-18** — Infection génitale haute `corrige` · [grille](<file:///Users/damienfulliquet/Developer/GitHub/grilles-ecos/cases/german/German-18_-_Douleur_abdominale_-_Grille_ECOS.html>)
> - **German-19** — Rectocolite ulcéro-hémorragique `corrige` · [grille](<file:///Users/damienfulliquet/Developer/GitHub/grilles-ecos/cases/german/German-19_-_Douleur_abdominale_-_Grille_ECOS.html>)
> - **German-20** — Ischémie mésentérique aiguë `corrige` · [grille](<file:///Users/damienfulliquet/Developer/GitHub/grilles-ecos/cases/german/German-20_-_Douleur_abdominale_-_Grille_ECOS.html>)
> - **German-21** — Reflux gastro-œsophagien (RGO) `explicite` · [grille](<file:///Users/damienfulliquet/Developer/GitHub/grilles-ecos/cases/german/German-21_-_Douleur_abdominale_-_Grille_ECOS.html>)
> - **RESCOS-17** — Pyélonéphrite `premier-dd` · [grille](<file:///Users/damienfulliquet/Developer/GitHub/grilles-ecos/cases/rescos/RESCOS-17_-_Douleur_abdominale_-_Grille_ECOS.html>)
> - **RESCOS-18** — Cholangite `premier-dd` · [grille](<file:///Users/damienfulliquet/Developer/GitHub/grilles-ecos/cases/rescos/RESCOS-18_-_Douleur_abdominale_-_Grille_ECOS.html>)
> - **RESCOS-19** — Cholécystite `premier-dd` · [grille](<file:///Users/damienfulliquet/Developer/GitHub/grilles-ecos/cases/rescos/RESCOS-19_-_Douleur_abdominale_-_Grille_ECOS.html>)
> - **RESCOS-20** — Torsion ovarienne `explicite` · [grille](<file:///Users/damienfulliquet/Developer/GitHub/grilles-ecos/cases/rescos/RESCOS-20_-_Douleur_abdominale_-_Grille_ECOS.html>)
> - **RESCOS-21** — Perforation d'ulcère gastro-duodénal `premier-dd` · [grille](<file:///Users/damienfulliquet/Developer/GitHub/grilles-ecos/cases/rescos/RESCOS-21_-_Douleur_abdominale_-_Grille_ECOS.html>)
> - **RESCOS-22** — Gastroentérite `explicite` · [grille](<file:///Users/damienfulliquet/Developer/GitHub/grilles-ecos/cases/rescos/RESCOS-22_-_Douleur_abdominale_-_ECC_Digestion_-_Grille_ECOS.html>)
> - **RESCOS-23** — Cholécystite `explicite` · [grille](<file:///Users/damienfulliquet/Developer/GitHub/grilles-ecos/cases/rescos/RESCOS-23_-_Douleur_abdominale_-_ECC_Digestion_-_Grille_ECOS.html>)

> [!note] 📋 Anamnèse
> - [ ] **1. Motif principal *(4 grilles sur 20)***
> - [ ] **2. Caractérisation de la douleur *(7 grilles sur 20)***
> 	- [ ] Localisation *(6 grilles sur 20)*
> 	- [ ] Intensité *(6 grilles sur 20)*
> 	- [ ] Qualité
> 	- [ ] Début *(3 grilles sur 20)*
> 	- [ ] Évolution temporelle *(3 grilles sur 20)*
> 	- [ ] Irradiation
> 	- [ ] Facteurs améliorants *(3 grilles sur 20)*
> 	- [ ] Facteurs aggravants *(5 grilles sur 20)*
> 	- [ ] Épisodes antérieurs similaires *(3 grilles sur 20)*
> 	- [ ] Événements précipitants *(Appendicite aiguë · Cancer de l'ovaire)*
> 	- [ ] Facteurs aggravant/soulageant *(Cholangite · Pyélonéphrite)*
> 	- [ ] Quantité *(Cholangite)*
> 	- [ ] Chronologie *(Cholangite)*
> 	- [ ] Facteurs soulageants *(2 grilles sur 20)*
> 	- [ ] Localisation précise *(Torsion ovarienne)*
> - [ ] **3. Symptômes associés *(7 grilles sur 20)***
> 	- [ ] Nausées *(4 grilles sur 20)*
> 	- [ ] Vomissements *(5 grilles sur 20)*
> 	- [ ] Caractéristiques des vomissements *(1 grille sur 20)*
> 	- [ ] Fièvre *(3 grilles sur 20)*
> 	- [ ] Fièvre/frissons *(Appendicite aiguë)*
> 	- [ ] Appétit *(Appendicite aiguë · Cancer de l'ovaire)*
> 	- [ ] Ballonnements *(Cancer de l'ovaire)*
> 	- [ ] Prise de poids *(Cancer de l'ovaire)*
> 	- [ ] Diarrhée *(Douleurs abdominales non spécifiques)*
> 	- [ ] Troubles du transit *(Perforation d'ulcère gastro-duodénal)*
> 	- [ ] Frissons *(Perforation d'ulcère gastro-duodénal)*
> 	- [ ] Arrêt des matières et des gaz *(Perforation d'ulcère gastro-duodénal)*
> - [ ] **4. Recherche de symptômes spécifiques *(3 grilles sur 20)***
> 	- [ ] Voyage récent
> 	- [ ] Fatigue *(2 grilles sur 20)*
> 	- [ ] Éruption cutanée *(2 grilles sur 20)*
> 	- [ ] Ictère *(1 grille sur 20)*
> 	- [ ] Troubles urinaires
> 	- [ ] Modifications de la couleur des urines *(1 grille sur 20)*
> 	- [ ] Troubles du transit
> 	- [ ] Modifications de la couleur des selles *(1 grille sur 20)*
> 	- [ ] Sang dans les selles *(1 grille sur 20)*
> 	- [ ] Appétit *(1 grille sur 20)*
> 	- [ ] Variations pondérales *(2 grilles sur 20)*
> 	- [ ] Infections récentes
> 	- [ ] Douleurs articulaires *(Appendicite aiguë)*
> 	- [ ] Traumatisme *(Cancer de l'ovaire)*
> 	- [ ] Fièvre/frissons *(Cancer de l'ovaire)*
> 	- [ ] Sueurs nocturnes *(Cancer de l'ovaire)*
> 	- [ ] Dyspnée *(Cancer de l'ovaire)*
> - [ ] **5. Antécédents médicaux *(Appendicite aiguë · Cancer de l'ovaire · Cholécystite aiguë)***
> - [ ] **6. Antécédents chirurgicaux *(Appendicite aiguë · Cancer de l'ovaire · Cholécystite aiguë)***
> - [ ] **7. Allergies *(9 diagnostics)***
> - [ ] **8. Médicaments *(5 diagnostics)***
> 	- [ ] Antiacides *(1 grille sur 20)*
> 	- [ ] Fréquence *(1 grille sur 20)*
> - [ ] **9. Hospitalisations *(3 grilles sur 20)***
> - [ ] **10. Contacts malades *(3 grilles sur 20)***
> - [ ] **11. Antécédents familiaux *(4 diagnostics)***
> 	- [ ] Père *(2 grilles sur 20)*
> 	- [ ] Mère *(2 grilles sur 20)*
> 	- [ ] Sœur *(Cancer de l'ovaire)*
> 	- [ ] Grand-mère *(Cancer de l'ovaire)*
> - [ ] **12. Habitudes et mode de vie *(3 grilles sur 20)***
> 	- [ ] Occupation
> 	- [ ] Domicile
> 	- [ ] Tabac
> 	- [ ] Alcool
> 	- [ ] Questions CAGE - Besoin de réduire *(1 grille sur 20)*
> 	- [ ] Questions CAGE - Agacée par les critiques *(1 grille sur 20)*
> 	- [ ] Questions CAGE - Culpabilité *(1 grille sur 20)*
> 	- [ ] Questions CAGE - Besoin de boire le matin *(1 grille sur 20)*
> 	- [ ] Drogues illicites
> 	- [ ] Exercice physique *(1 grille sur 20)*
> 	- [ ] Régime alimentaire *(2 grilles sur 20)*
> - [ ] **13. Histoire sexuelle et gynécologique *(Appendicite aiguë · Cancer de l'ovaire)***
> 	- [ ] Activité sexuelle
> 	- [ ] Partenaire *(Appendicite aiguë)*
> 	- [ ] Douleur pendant les rapports *(Appendicite aiguë)*
> 	- [ ] Nombre de partenaires dans l'année
> 	- [ ] Protection
> 	- [ ] Dernières règles
> 	- [ ] Ménarche
> 	- [ ] Durée des règles
> 	- [ ] Régularité
> 	- [ ] Nombre de tampons par jour
> 	- [ ] Pertes vaginales
> 	- [ ] Démangeaisons vaginales
> 	- [ ] Sécheresse vaginale *(Appendicite aiguë)*
> 	- [ ] Grossesses
> 	- [ ] Dernier frottis
> - [ ] **14. Caractérisation de la douleur abdominale *(Gastroentérite · Maladie cœliaque · Perforation d'ulcère gastro-duodénal)***
> 	- [ ] Localisation
> 	- [ ] Intensité (échelle 0-10) *(Maladie cœliaque)*
> 	- [ ] Qualité *(Maladie cœliaque)*
> 	- [ ] Début *(Maladie cœliaque · Perforation d'ulcère gastro-duodénal)*
> 	- [ ] Événements précipitants *(Maladie cœliaque)*
> 	- [ ] Symptômes associés à la consommation de certains aliments *(Maladie cœliaque)*
> 	- [ ] Progression/constant/intermittent *(Maladie cœliaque)*
> 	- [ ] Épisodes antérieurs *(Maladie cœliaque)*
> 	- [ ] Irradiation *(Gastroentérite · Maladie cœliaque)*
> 	- [ ] Facteurs améliorants *(Maladie cœliaque)*
> 	- [ ] Facteurs aggravants *(Maladie cœliaque)*
> 	- [ ] Horaire *(Perforation d'ulcère gastro-duodénal)*
> 	- [ ] Type *(Perforation d'ulcère gastro-duodénal)*
> 	- [ ] Intensité *(Gastroentérite · Perforation d'ulcère gastro-duodénal)*
> 	- [ ] Évolution *(Perforation d'ulcère gastro-duodénal)*
> 	- [ ] Début et progression *(Gastroentérite)*
> 	- [ ] Caractère *(Gastroentérite)*
> - [ ] **15. Symptômes associés - Souillures *(Maladie cœliaque)***
> 	- [ ] Présence
> 	- [ ] Fréquence
> 	- [ ] Diarrhée
> 	- [ ] Constipation
> 	- [ ] Couleur
> 	- [ ] Sang
> - [ ] **16. Recherche de symptômes spécifiques pédiatriques *(Maladie cœliaque)***
> 	- [ ] Fièvre
> 	- [ ] Vomissements
> 	- [ ] Éruption/changements cutanés
> 	- [ ] Pleurs/irritabilité
> 	- [ ] Problèmes urinaires/énurésie
> 	- [ ] Problèmes de sommeil
> 	- [ ] Activité (enjoué)
> 	- [ ] Comment le problème affecte l'enfant
> 	- [ ] Comment le problème affecte le parent
> 	- [ ] Punition pour les symptômes
> 	- [ ] Récompense pour les symptômes
> - [ ] **17. Antécédents médicaux et chirurgicaux *(Maladie cœliaque)***
> 	- [ ] Antécédents médicaux
> 	- [ ] Antécédents chirurgicaux
> 	- [ ] Hospitalisations antérieures
> 	- [ ] Histoire prénatale
> - [ ] **18. Allergies et médicaments *(Maladie cœliaque)***
> 	- [ ] Allergies
> 	- [ ] Médicaments
> - [ ] **19. Vaccinations *(Maladie cœliaque)***
> - [ ] **20. Croissance et développement *(Maladie cœliaque)***
> 	- [ ] Croissance et développement
> 	- [ ] Garderie/école
> 	- [ ] Problèmes à l'école/notes
> - [ ] **21. Habitudes alimentaires *(Maladie cœliaque · Reflux gastro-œsophagien (RGO))***
> 	- [ ] Habitudes alimentaires *(Maladie cœliaque)*
> 	- [ ] Appétit *(Maladie cœliaque)*
> 	- [ ] Dernier contrôle *(Maladie cœliaque)*
> - [ ] **22. Question initiale *(1 grille sur 20)***
> - [ ] **23. Dimension temporelle *(1 grille sur 20)***
> - [ ] **24. Début / Durée *(1 grille sur 20)***
> - [ ] **25. Évolution *(2 grilles sur 20)***
> - [ ] **26. Épisode *(1 grille sur 20)***
> - [ ] **27. Facteur déclenchant *(1 grille sur 20)***
> - [ ] **28. Localisation *(6 grilles sur 20)***
> - [ ] **29. Qualité *(2 grilles sur 20)***
> - [ ] **30. Irradiation *(7 grilles sur 20)***
> - [ ] **31. Intensité / Sévérité *(1 grille sur 20)***
> - [ ] **32. Factors aggravants *(1 grille sur 20)***
> - [ ] **33. Facteurs soulageants *(2 grilles sur 20)***
> - [ ] **34. Retentissement des symptômes *(1 grille sur 20)***
> - [ ] **35. Mesures déjà prises *(1 grille sur 20)***
> - [ ] **36. Fièvre aiguë *(1 grille sur 20)***
> - [ ] **37. Anamnèse de l'entourage *(5 grilles sur 20)***
> - [ ] **38. Nausées *(1 grille sur 20)***
> - [ ] **39. Vomissements *(2 grilles sur 20)***
> - [ ] **40. Qualité (bilieux/sanglant/en marc de café) *(1 grille sur 20)***
> - [ ] **41. Selles *(2 grilles sur 20)***
> - [ ] **42. Dernières selles *(1 grille sur 20)***
> - [ ] **43. Qualité (sang/méléna/acholique) *(1 grille sur 20)***
> - [ ] **44. Symptômes B *(2 grilles sur 20)***
> - [ ] **45. Troubles de la miction *(1 grille sur 20)***
> - [ ] **46. Dysurie *(2 grilles sur 20)***
> - [ ] **47. Pollakiurie *(1 grille sur 20)***
> - [ ] **48. Gynécologique *(1 grille sur 20)***
> - [ ] **49. Dernier contrôle *(1 grille sur 20)***
> - [ ] **50. Anamnèse du cycle / des saignements *(1 grille sur 20)***
> - [ ] **51. Symptômes vaginaux *(1 grille sur 20)***
> - [ ] **52. Grossesse possible *(1 grille sur 20)***
> - [ ] **53. Thorax *(1 grille sur 20)***
> - [ ] **54. Douleurs *(1 grille sur 20)***
> - [ ] **55. Dyspnée *(1 grille sur 20)***
> - [ ] **56. Toux *(1 grille sur 20)***
> - [ ] **57. Dernier repas *(1 grille sur 20)***
> - [ ] **58. Toxiques *(1 grille sur 20)***
> - [ ] **59. Alcool *(1 grille sur 20)***
> - [ ] **60. Tabagisme *(1 grille sur 20)***
> - [ ] **61. Drogues *(1 grille sur 20)***
> - [ ] **62. Anamnèse de voyage *(5 grilles sur 20)***
> 	- [ ] Voyage récent *(Infection génitale haute)*
> - [ ] **63. Profession *(1 grille sur 20)***
> - [ ] **64. Situation sociale *(1 grille sur 20)***
> - [ ] **65. Facteurs de stress psychosociaux *(1 grille sur 20)***
> - [ ] **66. Question d’entrée *(Purpura de Schönlein-Henoch (vascularite à IgA))***
> - [ ] **67. Dynamique temporelle *(Purpura de Schönlein-Henoch (vascularite à IgA))***
> - [ ] **68. Début *(Purpura de Schönlein-Henoch (vascularite à IgA))***
> - [ ] **69. Intensité *(5 diagnostics)***
> - [ ] **70. Facteurs aggravants *(Purpura de Schönlein-Henoch (vascularite à IgA))***
> - [ ] **71. Retentissement *(Purpura de Schönlein-Henoch (vascularite à IgA))***
> - [ ] **72. Estomac *(Purpura de Schönlein-Henoch (vascularite à IgA))***
> - [ ] **73. Aspect des vomissements *(Purpura de Schönlein-Henoch (vascularite à IgA))***
> - [ ] **74. Intestin *(Purpura de Schönlein-Henoch (vascularite à IgA))***
> - [ ] **75. Caractéristiques des selles *(Purpura de Schönlein-Henoch (vascularite à IgA))***
> - [ ] **76. Peau *(Purpura de Schönlein-Henoch (vascularite à IgA))***
> - [ ] **77. Caractéristiques du résultat cutané *(Purpura de Schönlein-Henoch (vascularite à IgA))***
> - [ ] **78. Éruption *(Purpura de Schönlein-Henoch (vascularite à IgA))***
> - [ ] **79. Urines *(Purpura de Schönlein-Henoch (vascularite à IgA))***
> - [ ] **80. Miction *(Endométriose pelvienne · Purpura de Schönlein-Henoch (vascularite à IgA))***
> - [ ] **81. Caractéristiques du résultat urinaire *(Purpura de Schönlein-Henoch (vascularite à IgA))***
> - [ ] **82. Comportement d’hydratation *(Purpura de Schönlein-Henoch (vascularite à IgA))***
> - [ ] **83. Articulations *(Purpura de Schönlein-Henoch (vascularite à IgA))***
> - [ ] **84. Infection préalable *(Purpura de Schönlein-Henoch (vascularite à IgA))***
> - [ ] **85. DD hématologiques *(Purpura de Schönlein-Henoch (vascularite à IgA))***
> - [ ] **86. Tendance aux saignements *(Purpura de Schönlein-Henoch (vascularite à IgA))***
> - [ ] **87. Asthénie *(Purpura de Schönlein-Henoch (vascularite à IgA))***
> - [ ] **88. Douleurs osseuses *(Purpura de Schönlein-Henoch (vascularite à IgA))***
> - [ ] **89. Fièvre / EG *(Purpura de Schönlein-Henoch (vascularite à IgA))***
> - [ ] **90. Traumatisme *(Purpura de Schönlein-Henoch (vascularite à IgA))***
> - [ ] **91. Antécédents *(Cholangite · Purpura de Schönlein-Henoch (vascularite à IgA))***
> 	- [ ] Médicaux (maladies) *(Cholangite)*
> 	- [ ] Hospitalisations *(Cholangite)*
> 	- [ ] Opérations *(Cholangite)*
> - [ ] **92. Statut vaccinal *(Purpura de Schönlein-Henoch (vascularite à IgA))***
> - [ ] **93. Anamnèse familiale *(8 diagnostics)***
> 	- [ ] Cancer colorectal familial *(Diverticulite sigmoïdienne non compliquée)*
> 	- [ ] Maladies inflammatoires intestinales *(Diverticulite sigmoïdienne non compliquée)*
> 	- [ ] Diverticulose familiale *(Diverticulite sigmoïdienne non compliquée)*
> 	- [ ] Hypertension artérielle *(Douleurs abdominales non spécifiques)*
> 	- [ ] Diabète *(Douleurs abdominales non spécifiques)*
> 	- [ ] Maladies rénales *(Douleurs abdominales non spécifiques)*
> 	- [ ] Infarctus du myocarde *(Douleurs abdominales non spécifiques)*
> 	- [ ] Troubles de la coagulation *(Douleurs abdominales non spécifiques)*
> 	- [ ] Embolies *(Douleurs abdominales non spécifiques)*
> 	- [ ] Cancers *(Reflux gastro-œsophagien (RGO))*
> 	- [ ] Maladies cardiovasculaires *(Reflux gastro-œsophagien (RGO))*
> - [ ] **94. Prise en charge *(Purpura de Schönlein-Henoch (vascularite à IgA))***
> - [ ] **95. Présentation avec nom, fonction et tâche *(7 diagnostics)***
> - [ ] **96. Identification du symptôme principal *(4 diagnostics)***
> - [ ] **97. Caractérisation de la douleur (OPQRST) *(Diverticulite sigmoïdienne non compliquée)***
> 	- [ ] Localisation précise
> 	- [ ] Type/caractère
> 	- [ ] Intensité
> 	- [ ] Irradiation
> - [ ] **98. Évolution temporelle *(Diverticulite sigmoïdienne non compliquée)***
> 	- [ ] Début
> 	- [ ] Mode d'apparition
> 	- [ ] Évolution
> 	- [ ] Périodicité
> - [ ] **99. Facteurs modulateurs *(Diverticulite sigmoïdienne non compliquée)***
> 	- [ ] Facteurs aggravants
> 	- [ ] Facteurs améliorants
> 	- [ ] Position antalgique
> 	- [ ] Relation avec l'alimentation
> - [ ] **100. Symptômes digestifs associés *(4 grilles sur 20)***
> 	- [ ] Nausées *(3 grilles sur 20)*
> 	- [ ] Vomissements
> 	- [ ] Transit intestinal - diarrhée *(Diverticulite sigmoïdienne non compliquée)*
> 	- [ ] Flatulences *(Diverticulite sigmoïdienne non compliquée)*
> 	- [ ] Constipation *(Diverticulite sigmoïdienne non compliquée)*
> 	- [ ] Habitudes intestinales *(Reflux gastro-œsophagien (RGO))*
> 	- [ ] Ictère *(Reflux gastro-œsophagien (RGO))*
> 	- [ ] Perte d'appétit *(2 grilles sur 20)*
> 	- [ ] Perte de poids *(Gastroentérite)*
> 	- [ ] Hoquet, éructations *(2 grilles sur 20)*
> 	- [ ] Dégoût pour la nourriture *(1 grille sur 20)*
> - [ ] **101. Recherche de signes d'alarme *(Diverticulite sigmoïdienne non compliquée)***
> 	- [ ] Fièvre
> 	- [ ] Perte de poids inexpliquée
> 	- [ ] Symptômes B (sueurs nocturnes)
> 	- [ ] Sang dans les selles
> 	- [ ] Masse palpable
> - [ ] **102. Anamnèse urogynécologique *(Diverticulite sigmoïdienne non compliquée)***
> 	- [ ] Modifications mictionnelles
> 	- [ ] Dysurie, pollakiurie
> 	- [ ] Hématurie
> 	- [ ] Pertes vaginales anormales
> 	- [ ] Métrorragies post-ménopausiques
> - [ ] **103. Antécédents obstétricaux et gynécologiques *(Diverticulite sigmoïdienne non compliquée)***
> 	- [ ] Parité
> 	- [ ] Ménopause
> 	- [ ] Antécédents gynécologiques
> 	- [ ] Hystérectomie
> - [ ] **104. Antécédents médicaux personnels *(Diverticulite sigmoïdienne non compliquée)***
> 	- [ ] Pathologies chroniques
> 	- [ ] Chirurgies abdominales antérieures
> 	- [ ] Coloscopie de dépistage
> 	- [ ] Antécédents de diverticulose
> - [ ] **105. Traitement actuel et allergies *(Diverticulite sigmoïdienne non compliquée)***
> 	- [ ] Médicaments actuels
> 	- [ ] Allergies médicamenteuses
> 	- [ ] Automédication récente
> - [ ] **106. Habitudes de vie et facteurs de risque *(Diverticulite sigmoïdienne non compliquée)***
> 	- [ ] Tabagisme
> 	- [ ] Consommation d'alcool
> 	- [ ] Toxicomanie
> 	- [ ] Activité physique
> 	- [ ] Régime alimentaire (fibres)
> - [ ] **107. Contexte psychosocial *(Diverticulite sigmoïdienne non compliquée)***
> 	- [ ] Situation familiale
> 	- [ ] Autonomie
> 	- [ ] Stress récent
> 	- [ ] Support social
> - [ ] **108. Anamnèse par systèmes *(Diverticulite sigmoïdienne non compliquée)***
> 	- [ ] Symptômes cardiovasculaires
> 	- [ ] Symptômes respiratoires
> 	- [ ] Symptômes neurologiques
> 	- [ ] Symptômes articulaires
> - [ ] **109. Qualité de la douleur *(Douleurs abdominales non spécifiques)***
> - [ ] **110. Sévérité (échelle 1-10) *(Douleurs abdominales non spécifiques)***
> - [ ] **111. Facteurs d'amélioration ou d'aggravation *(Douleurs abdominales non spécifiques)***
> - [ ] **112. Localisation et durée *(Douleurs abdominales non spécifiques)***
> - [ ] **113. Vertiges *(Douleurs abdominales non spécifiques)***
> - [ ] **114. Menstruation *(Douleurs abdominales non spécifiques)***
> - [ ] **115. Revue des systèmes *(Douleurs abdominales non spécifiques)***
> 	- [ ] Migraine
> 	- [ ] Épilepsie
> - [ ] **116. Anamnèse médicamenteuse *(Douleurs abdominales non spécifiques)***
> - [ ] **117. Consommation de substances *(6 diagnostics)***
> 	- [ ] Alcool *(Reflux gastro-œsophagien (RGO))*
> 	- [ ] Tabac *(Reflux gastro-œsophagien (RGO))*
> - [ ] **118. Activités sportives et loisirs *(Douleurs abdominales non spécifiques · Reflux gastro-œsophagien (RGO))***
> - [ ] **119. Anamnèse sociale *(6 diagnostics)***
> - [ ] **120. Identification des symptômes principaux *(Endométriose pelvienne · Rectocolite ulcéro-hémorragique)***
> - [ ] **121. Début des symptômes *(4 diagnostics)***
> - [ ] **122. Fréquence et périodicité *(4 diagnostics)***
> - [ ] **123. Caractère de la douleur *(5 diagnostics)***
> - [ ] **124. Facteurs aggravants ou soulageants *(4 diagnostics)***
> - [ ] **125. Douleurs liées à l'alimentation *(Endométriose pelvienne · Ischémie mésentérique aiguë · Rectocolite ulcéro-hémorragique)***
> - [ ] **126. Symptômes généraux *(Endométriose pelvienne · Infection génitale haute · Rectocolite ulcéro-hémorragique)***
> 	- [ ] Fièvre *(Endométriose pelvienne · Rectocolite ulcéro-hémorragique)*
> 	- [ ] Perte de poids
> 	- [ ] Sueurs nocturnes
> 	- [ ] Fièvre prolongée *(Infection génitale haute)*
> - [ ] **127. Symptômes digestifs *(Endométriose pelvienne · Infection génitale haute · Rectocolite ulcéro-hémorragique)***
> 	- [ ] Transit intestinal *(Endométriose pelvienne)*
> 	- [ ] Gaz *(Endométriose pelvienne)*
> 	- [ ] Nausées/Vomissements
> 	- [ ] Sang dans les vomissements
> 	- [ ] Constipation *(Endométriose pelvienne · Rectocolite ulcéro-hémorragique)*
> 	- [ ] Diarrhée *(Endométriose pelvienne · Rectocolite ulcéro-hémorragique)*
> 	- [ ] Sang dans les selles *(Endométriose pelvienne · Infection génitale haute)*
> 	- [ ] Transit intestinal et gaz *(Infection génitale haute · Rectocolite ulcéro-hémorragique)*
> 	- [ ] Diarrhée/Constipation *(Infection génitale haute)*
> 	- [ ] Aspect des selles *(Rectocolite ulcéro-hémorragique)*
> - [ ] **128. Antécédent de chirurgie abdominale *(4 diagnostics)***
> - [ ] **129. Anamnèse gynécologique *(Endométriose pelvienne · Infection génitale haute)***
> 	- [ ] Dernières règles *(Endométriose pelvienne)*
> 	- [ ] Durée du cycle *(Endométriose pelvienne)*
> 	- [ ] Durée des menstruations *(Endométriose pelvienne)*
> 	- [ ] Intensité des saignements *(Endométriose pelvienne)*
> 	- [ ] Symptômes vaginaux
> 	- [ ] Pertes vaginales *(Endométriose pelvienne)*
> 	- [ ] Partenaire stable *(Endométriose pelvienne)*
> 	- [ ] Dyspareunie *(Endométriose pelvienne)*
> 	- [ ] Contraception *(Endométriose pelvienne)*
> 	- [ ] Enfants *(Endométriose pelvienne)*
> 	- [ ] Grossesse actuelle *(Endométriose pelvienne)*
> 	- [ ] Antécédent de chirurgie gynécologique *(Endométriose pelvienne)*
> 	- [ ] Grossesse *(Infection génitale haute)*
> 	- [ ] Nouveau partenaire sexuel *(Infection génitale haute)*
> - [ ] **130. Anamnèse personnelle *(4 diagnostics)***
> - [ ] **131. Médication actuelle *(5 diagnostics)***
> - [ ] **132. Migration de la douleur *(Infection génitale haute · Ischémie mésentérique aiguë · Rectocolite ulcéro-hémorragique)***
> - [ ] **133. Mode de début *(Infection génitale haute · Ischémie mésentérique aiguë · Rectocolite ulcéro-hémorragique)***
> - [ ] **134. Fièvre *(Infection génitale haute)***
> - [ ] **135. Symptômes extra-intestinaux *(Rectocolite ulcéro-hémorragique)***
> 	- [ ] Aphtes
> 	- [ ] Inflammation oculaire
> 	- [ ] Troubles articulaires
> - [ ] **136. Antécédents de douleurs similaires *(Ischémie mésentérique aiguë)***
> - [ ] **137. Symptômes généraux et digestifs *(Ischémie mésentérique aiguë)***
> 	- [ ] Fièvre
> 	- [ ] Transit intestinal et gaz
> 	- [ ] Nausées/Vomissements
> 	- [ ] Sang dans les vomissements
> 	- [ ] Diarrhée/Constipation
> 	- [ ] Sang dans les selles
> - [ ] **138. Symptômes constitutionnels *(Ischémie mésentérique aiguë)***
> 	- [ ] Perte de poids
> 	- [ ] Sueurs nocturnes
> 	- [ ] Fièvre prolongée
> - [ ] **139. Facteurs de risque cardiovasculaire *(Ischémie mésentérique aiguë)***
> 	- [ ] Hypertension artérielle
> 	- [ ] Dyslipidémie
> 	- [ ] Diabète
> 	- [ ] Tabagisme
> 	- [ ] Antécédent familial de maladie coronarienne < 55 ans
> - [ ] **140. Localisation de la douleur *(Reflux gastro-œsophagien (RGO))***
> - [ ] **141. Fréquence *(Reflux gastro-œsophagien (RGO))***
> - [ ] **142. Durée et évolution *(Reflux gastro-œsophagien (RGO))***
> 	- [ ] Durée totale
> 	- [ ] Durée des épisodes
> 	- [ ] Évolution
> - [ ] **143. Événements récents *(Reflux gastro-œsophagien (RGO))***
> - [ ] **144. Facteurs d'influence et dépendance alimentaire *(Reflux gastro-œsophagien (RGO))***
> 	- [ ] Facteurs soulageants
> 	- [ ] Facteurs déclenchants
> 	- [ ] Relation temporelle avec les repas
> - [ ] **145. Réveil matinal avec goût acide *(Reflux gastro-œsophagien (RGO))***
> - [ ] **146. Dysphagie ou odynophagie *(Reflux gastro-œsophagien (RGO))***
> - [ ] **147. Appétit *(Reflux gastro-œsophagien (RGO))***
> - [ ] **148. Changements de poids et symptômes B *(Reflux gastro-œsophagien (RGO))***
> - [ ] **149. Anamnèse systémique *(Reflux gastro-œsophagien (RGO))***
> 	- [ ] De la tête aux pieds incluant fièvre et symptômes B
> - [ ] **150. Chronologie de la douleur *(3 grilles sur 20)***
> 	- [ ] Début/durée *(Pyélonéphrite)*
> 	- [ ] Fluctuation *(Pyélonéphrite)*
> 	- [ ] Circonstances de survenue
> 	- [ ] Début *(2 grilles sur 20)*
> 	- [ ] Progression *(2 grilles sur 20)*
> - [ ] **151. Anamnèse actuelle - présence de *(Pyélonéphrite)***
> 	- [ ] Fièvre
> 	- [ ] Frissons
> - [ ] **152. Par système - urinaire *(2 grilles sur 20)***
> 	- [ ] Quantité d'urine
> 	- [ ] Fréquence mictionnelle *(Pyélonéphrite)*
> 	- [ ] Couleur de l'urine
> 	- [ ] Présence de sang *(Pyélonéphrite)*
> 	- [ ] Douleur à la miction *(Pyélonéphrite)*
> 	- [ ] Hématurie *(1 grille sur 20)*
> 	- [ ] Dysurie *(1 grille sur 20)*
> 	- [ ] Algurie *(1 grille sur 20)*
> 	- [ ] Pollakiurie *(1 grille sur 20)*
> - [ ] **153. Par système - digestif *(2 grilles sur 20)***
> 	- [ ] Nausées
> 	- [ ] Vomissements
> 	- [ ] Consistance des selles
> 	- [ ] Fréquence du transit *(Pyélonéphrite)*
> 	- [ ] Couleur des selles
> 	- [ ] Présence de sang dans les selles *(Pyélonéphrite)*
> 	- [ ] Dernier transit *(1 grille sur 20)*
> 	- [ ] Sang dans les selles *(1 grille sur 20)*
> - [ ] **154. Antécédents personnels *(2 grilles sur 20)***
> 	- [ ] Maladies / comorbidités *(Pyélonéphrite)*
> 	- [ ] Hospitalisations / opérations
> 	- [ ] Diète *(1 grille sur 20)*
> 	- [ ] Médicaments *(1 grille sur 20)*
> 	- [ ] Alcool *(1 grille sur 20)*
> 	- [ ] Tabac *(1 grille sur 20)*
> 	- [ ] Drogues *(1 grille sur 20)*
> 	- [ ] Comorbidités *(1 grille sur 20)*
> - [ ] **155. Habitudes *(Pyélonéphrite)***
> 	- [ ] Alcool
> 	- [ ] Tabac
> 	- [ ] Diète
> 	- [ ] Médicaments
> 	- [ ] Drogues
> - [ ] **156. Symptômes associés - fièvre *(Cholangite)***
> 	- [ ] Début/chronologie
> 	- [ ] Intensité
> 	- [ ] Fluctuation
> 	- [ ] Présence de frissons
> 	- [ ] Présence de transpiration
> - [ ] **157. Symptômes associés - nausées *(Cholangite)***
> 	- [ ] Présence de nausée
> 	- [ ] Présence de vomissement
> 	- [ ] Début/durée des nausées
> - [ ] **158. Symptômes similaires par le passé *(Cholangite)***
> - [ ] **159. Anamnèse par système - digestives (selles) *(Cholangite)***
> 	- [ ] Quantité
> 	- [ ] Fréquence
> 	- [ ] Couleur
> 	- [ ] Présence de sang
> - [ ] **160. Habitudes - alimentation *(Cholangite)***
> 	- [ ] Alimentation habituelle
> 	- [ ] Contenu du dernier repas
> 	- [ ] Consommation d'alcool
> 	- [ ] Allergies
> - [ ] **161. État général *(2 grilles sur 20)***
> 	- [ ] Fièvre et frissons *(1 grille sur 20)*
> 	- [ ] Fatigue
> 	- [ ] Forme (perte de poids) *(1 grille sur 20)*
> 	- [ ] Fièvre *(Torsion ovarienne)*
> 	- [ ] Perte/prise de poids récente *(Torsion ovarienne)*
> - [ ] **162. Système reproducteur (DD: grossesse extra-utérine, torsion ovarienne) *(Torsion ovarienne)***
> 	- [ ] Test de grossesse (la patiente en a-t-elle fait un ?)
> 	- [ ] Contraception
> 	- [ ] Antécédent de césarienne/de grossesse
> 	- [ ] Aménorrhée
> 	- [ ] Métrorragie/ménorragie
> 	- [ ] Pertes vaginales
> - [ ] **163. Système digestif (DD: colite, appendicite, diverticulite) *(Torsion ovarienne)***
> 	- [ ] Nausées
> 	- [ ] Vomissements
> 	- [ ] Dernier transit
> 	- [ ] Diarrhées
> 	- [ ] Constipation
> 	- [ ] Sang dans les selles
> - [ ] **164. Système urinaire: (DD: lithiase rénale, cystite, pyélonéphrite) *(Torsion ovarienne)***
> 	- [ ] Dysurie/algurie
> 	- [ ] Urgenturie
> 	- [ ] Couleur des urines
> 	- [ ] Hématurie
> - [ ] **165. Habitudes et antécédents personnels *(Torsion ovarienne)***
> 	- [ ] Médicaments
> 	- [ ] Maladies connues
> 	- [ ] Antécédents chirurgicaux
> - [ ] **166. Motif de consultation *(Perforation d'ulcère gastro-duodénal)***
> - [ ] **167. Caractéristiques spécifiques de la douleur *(Perforation d'ulcère gastro-duodénal)***
> 	- [ ] Coliques
> 	- [ ] Continues
> 	- [ ] Irradiation
> 	- [ ] Sans irradiation actuellement
> 	- [ ] Exacerbée par
> 	- [ ] Non calmée par
> - [ ] **168. Antécédents de maladie ulcéreuse *(Perforation d'ulcère gastro-duodénal)***
> 	- [ ] Maladie ulcéreuse connue
> 	- [ ] Sensation de faim douloureuse
> 	- [ ] Brûlure épigastrique
> 	- [ ] Rythmée par les repas
> 	- [ ] Réveils nocturnes à 02h
> 	- [ ] Calmée par alimentation ou lait
> 	- [ ] Printemps et automne
> - [ ] **169. Traitement antérieur *(Perforation d'ulcère gastro-duodénal)***
> 	- [ ] Ranitidine prescrite
> 	- [ ] Prise irrégulière
> 	- [ ] Interruption du traitement antibiotique d'éradication
> 	- [ ] Intolérance après 48 heures
> 	- [ ] Automédication fréquente
> - [ ] **170. Facteurs de risque ulcéreux *(Perforation d'ulcère gastro-duodénal)***
> 	- [ ] Calculs biliaires ou urinaires
> 	- [ ] Ulcère gastro-duodénal connu
> 	- [ ] Stress professionnel
> 	- [ ] Tabagisme
> 	- [ ] Consommation d'AINS
> 	- [ ] Consommation d'alcool
> 	- [ ] Antécédents familiaux d'ulcère
> - [ ] **171. Troubles urinaires associés *(Perforation d'ulcère gastro-duodénal)***
> 	- [ ] Dysurie
> 	- [ ] Pollakiurie
> 	- [ ] Hématurie
> 	- [ ] Volume des urines
> 	- [ ] Fréquence mictionnelle
> 	- [ ] Odeur anormale
> - [ ] **172. Facteurs déclenchants, aggravants et calmants *(Gastroentérite)***
> 	- [ ] Facteurs déclenchants
> 	- [ ] Facteurs aggravants
> 	- [ ] Facteurs calmants
> 	- [ ] Position antalgique
> 	- [ ] Évolution temporelle
> - [ ] **173. Anamnèse du transit intestinal et aspect des selles *(Gastroentérite)***
> 	- [ ] Fréquence des selles
> 	- [ ] Aspect des selles
> 	- [ ] Odeur
> 	- [ ] Présence de glaires, sang, pus
> 	- [ ] Horaire
> - [ ] **174. Symptômes généraux et signes de déshydratation *(Gastroentérite)***
> 	- [ ] Fièvre
> 	- [ ] Asthénie
> 	- [ ] Troubles du sommeil
> 	- [ ] Soif et apports hydriques
> 	- [ ] État général
> - [ ] **175. Recherche de complications et symptômes d'alarme *(Gastroentérite)***
> 	- [ ] Troubles urinaires
> 	- [ ] Signes d'occlusion
> 	- [ ] Douleur à la détente
> 	- [ ] Signes de péritonisme
> - [ ] **176. Antécédents et contexte épidémiologique *(Gastroentérite)***
> 	- [ ] Antécédents similaires
> 	- [ ] Voyage récent
> 	- [ ] Contage
> 	- [ ] Antécédents familiaux
> 	- [ ] Médicaments et habitudes
> - [ ] **177. Anamnèse gynécologique (si applicable) *(Gastroentérite)***
> 	- [ ] Dernières règles
> 	- [ ] Contraception
> 	- [ ] Risque de grossesse
> - [ ] **178. Caractérisation de la douleur biliaire *(1 grille sur 20)***
> 	- [ ] Localisation
> 	- [ ] Irradiation
> 	- [ ] Début et progression
> 	- [ ] Caractère
> 	- [ ] Intensité
> - [ ] **179. Facteurs aggravants et déclenchants *(1 grille sur 20)***
> 	- [ ] Facteurs aggravants
> 	- [ ] Facteurs déclenchants
> 	- [ ] Position antalgique
> 	- [ ] Effet du traitement
> 	- [ ] Évolution temporelle
> - [ ] **180. Symptômes généraux et signes d'alarme *(1 grille sur 20)***
> 	- [ ] Fièvre
> 	- [ ] Frissons
> 	- [ ] Impact fonctionnel
> 	- [ ] Ictère
> 	- [ ] Altération état général
> - [ ] **181. Transit et fonction digestive *(1 grille sur 20)***
> 	- [ ] Transit conservé
> 	- [ ] Aspect des selles
> 	- [ ] Troubles urinaires
> 	- [ ] Dernière prise alimentaire
> - [ ] **182. Antécédents personnels et facteurs de risque *(1 grille sur 20)***
> 	- [ ] Épisodes similaires antérieurs
> 	- [ ] Surpoids
> 	- [ ] Régime en cours
> 	- [ ] Bonne santé habituelle
> - [ ] **183. Antécédents familiaux et habitudes *(1 grille sur 20)***
> 	- [ ] Antécédents familiaux
> 	- [ ] Père avec cholestérol élevé
> 	- [ ] Tabagisme
> 	- [ ] Alcool
> 	- [ ] Activité physique
> - [ ] **184. Anamnèse socioprofessionnelle et impact *(1 grille sur 20)***
> 	- [ ] Profession
> 	- [ ] Situation familiale
> 	- [ ] Impact professionnel
> 	- [ ] Contexte psychosocial

> [!tip] 🩺 Status
> - [ ] **1. Mesures d'hygiène *(3 grilles sur 20)***
> 	- [ ] Lavage des mains
> 	- [ ] Respect de la pudeur avec drap
> - [ ] **2. Examen de la tête et du cou *(2 grilles sur 20)***
> 	- [ ] Inspection des sclérotiques *(1 grille sur 20)*
> 	- [ ] Inspection des conjonctives *(Cancer de l'ovaire)*
> - [ ] **3. Examen cardiovasculaire *(3 grilles sur 20)***
> - [ ] **4. Examen pulmonaire *(3 grilles sur 20)***
> 	- [ ] Percussion des champs pulmonaires *(Cancer de l'ovaire)*
> 	- [ ] Auscultation pulmonaire *(Cancer de l'ovaire)*
> - [ ] **5. Examen abdominal *(5 grilles sur 20)***
> 	- [ ] Inspection de l'abdomen *(3 grilles sur 20)*
> 	- [ ] Auscultation de l'abdomen *(3 grilles sur 20)*
> 	- [ ] Percussion de l'abdomen *(3 grilles sur 20)*
> 	- [ ] Palpation de l'abdomen *(3 grilles sur 20)*
> - [ ] **6. Signe de Murphy *(3 grilles sur 20)***
> - [ ] **7. Examen cutané *(1 grille sur 20)***
> - [ ] **8. Signe de McBurney *(Appendicite aiguë)***
> - [ ] **9. Signe de Blumberg *(Appendicite aiguë)***
> - [ ] **10. Signe du psoas *(Appendicite aiguë)***
> - [ ] **11. Signe de Rovsing *(Appendicite aiguë)***
> - [ ] **12. Éviter de répéter les manœuvres douloureuses *(Cancer de l'ovaire)***
> - [ ] **13. Non disponible dans les cas téléphoniques *(Maladie cœliaque)***
> - [ ] **14. Paramètres vitaux *(1 grille sur 20)***
> - [ ] **15. Inspection *(5 grilles sur 20)***
> 	- [ ] Teint *(Infection génitale haute · Rectocolite ulcéro-hémorragique)*
> 	- [ ] État général *(Infection génitale haute · Reflux gastro-œsophagien (RGO))*
> 	- [ ] Abdomen *(Infection génitale haute)*
> 	- [ ] Cavité buccale *(Rectocolite ulcéro-hémorragique)*
> 	- [ ] Peau *(Rectocolite ulcéro-hémorragique)*
> 	- [ ] Recherche de signes d'alarme *(Reflux gastro-œsophagien (RGO))*
> - [ ] **16. Sclérotiques *(1 grille sur 20)***
> - [ ] **17. Peau / Abdomen *(1 grille sur 20)***
> - [ ] **18. Auscultation *(4 grilles sur 20)***
> 	- [ ] Auscultation abdominale *(Reflux gastro-œsophagien (RGO))*
> 	- [ ] Auscultation cardio-pulmonaire *(Reflux gastro-œsophagien (RGO))*
> 	- [ ] Les 4 quadrants *(1 grille sur 20)*
> 	- [ ] Auscultation avant toute autre partie du status *(1 grille sur 20)*
> - [ ] **19. Percussion *(5 grilles sur 20)***
> 	- [ ] Percussion abdominale *(Reflux gastro-œsophagien (RGO))*
> 	- [ ] Des 4 quadrants *(2 grilles sur 20)*
> 	- [ ] Délimitation de la taille du foie à la percussion (ou autre technique appropriée) *(Cholangite)*
> 	- [ ] Délimite la taille du foie en percutant (ou autre technique appropriée) *(1 grille sur 20)*
> - [ ] **20. Palpation *(4 grilles sur 20)***
> 	- [ ] Superficielle *(2 grilles sur 20)*
> 	- [ ] Profonde (à deux mains) *(Cholangite)*
> 	- [ ] Teste la détente *(Cholangite)*
> 	- [ ] Commence par le côté non douloureux *(Cholangite)*
> 	- [ ] Profonde *(1 grille sur 20)*
> 	- [ ] Détente *(1 grille sur 20)*
> - [ ] **21. Douleur directe à la décompression *(1 grille sur 20)***
> - [ ] **22. Douleur à la décompression controlatérale *(1 grille sur 20)***
> - [ ] **23. Douleur à l'ébranlement *(1 grille sur 20)***
> - [ ] **24. Loges rénales *(3 grilles sur 20)***
> 	- [ ] Palpation *(2 grilles sur 20)*
> 	- [ ] Percussion *(2 grilles sur 20)*
> - [ ] **25. État général *(Purpura de Schönlein-Henoch (vascularite à IgA))***
> - [ ] **26. Examen de base *(Purpura de Schönlein-Henoch (vascularite à IgA))***
> - [ ] **27. Signes de péritonisme *(Purpura de Schönlein-Henoch (vascularite à IgA))***
> - [ ] **28. McBurney *(Purpura de Schönlein-Henoch (vascularite à IgA))***
> - [ ] **29. Douleur à la décompression *(Purpura de Schönlein-Henoch (vascularite à IgA))***
> - [ ] **30. Douleur à la secousse *(Purpura de Schönlein-Henoch (vascularite à IgA))***
> - [ ] **31. Palpation du foie *(Purpura de Schönlein-Henoch (vascularite à IgA) · Reflux gastro-œsophagien (RGO))***
> 	- [ ] Taille et consistance du foie *(Reflux gastro-œsophagien (RGO))*
> - [ ] **32. Inspection cutanée *(Purpura de Schönlein-Henoch (vascularite à IgA))***
> - [ ] **33. Endobuccal / muqueuses *(Purpura de Schönlein-Henoch (vascularite à IgA))***
> - [ ] **34. Statut articulaire *(Purpura de Schönlein-Henoch (vascularite à IgA))***
> - [ ] **35. Douleur à la percussion rénale *(Purpura de Schönlein-Henoch (vascularite à IgA))***
> - [ ] **36. Méningisme *(Purpura de Schönlein-Henoch (vascularite à IgA))***
> - [ ] **37. Examen neurologique *(Purpura de Schönlein-Henoch (vascularite à IgA))***
> - [ ] **38. Inspection générale et signes vitaux *(Diverticulite sigmoïdienne non compliquée · Gastroentérite)***
> 	- [ ] État général
> 	- [ ] Position antalgique *(Diverticulite sigmoïdienne non compliquée)*
> 	- [ ] Faciès douloureux *(Diverticulite sigmoïdienne non compliquée)*
> 	- [ ] Signes vitaux *(Diverticulite sigmoïdienne non compliquée)*
> 	- [ ] Signes vitaux complets *(Gastroentérite)*
> 	- [ ] Signes de déshydratation *(Gastroentérite)*
> 	- [ ] Recherche d'ictère *(Gastroentérite)*
> - [ ] **39. Inspection abdominale *(Diverticulite sigmoïdienne non compliquée · Perforation d'ulcère gastro-duodénal)***
> 	- [ ] Distension abdominale *(Diverticulite sigmoïdienne non compliquée)*
> 	- [ ] Asymétrie *(Diverticulite sigmoïdienne non compliquée)*
> 	- [ ] Cicatrices
> 	- [ ] Péristaltisme visible *(Diverticulite sigmoïdienne non compliquée)*
> 	- [ ] Circulation collatérale *(Diverticulite sigmoïdienne non compliquée)*
> 	- [ ] Morphologie *(Perforation d'ulcère gastro-duodénal)*
> 	- [ ] Symétrie vs asymétrie *(Perforation d'ulcère gastro-duodénal)*
> 	- [ ] Hernies *(Perforation d'ulcère gastro-duodénal)*
> 	- [ ] Veines superficielles *(Perforation d'ulcère gastro-duodénal)*
> 	- [ ] Respiration abdominale *(Perforation d'ulcère gastro-duodénal)*
> - [ ] **40. Auscultation abdominale *(7 diagnostics)***
> 	- [ ] Bruits hydroaériques *(Diverticulite sigmoïdienne non compliquée)*
> 	- [ ] Qualité (gargouillis, cliquetis) *(Diverticulite sigmoïdienne non compliquée)*
> 	- [ ] Quantité (5-34/min) *(Diverticulite sigmoïdienne non compliquée)*
> 	- [ ] Souffles vasculaires *(Diverticulite sigmoïdienne non compliquée)*
> 	- [ ] Ausculte les 4 quadrants *(Cholangite)*
> 	- [ ] Auscultation avant toute autre partie de l'examen clinique *(Cholangite)*
> 	- [ ] Patience *(Perforation d'ulcère gastro-duodénal)*
> 	- [ ] Silence abdominal *(Perforation d'ulcère gastro-duodénal)*
> 	- [ ] Bruits intestinaux *(Perforation d'ulcère gastro-duodénal)*
> 	- [ ] Tonalité *(Perforation d'ulcère gastro-duodénal)*
> 	- [ ] Auscultation pendant au moins 1 minute *(Gastroentérite)*
> 	- [ ] Auscultation de part et d'autre de l'ombilic *(Gastroentérite)*
> 	- [ ] Évaluation de la fréquence des bruits intestinaux *(Gastroentérite)*
> 	- [ ] Tonalité des bruits *(Gastroentérite)*
> 	- [ ] Intensité des bruits intestinaux *(Gastroentérite)*
> - [ ] **41. Percussion abdominale *(Diverticulite sigmoïdienne non compliquée · Gastroentérite · Perforation d'ulcère gastro-duodénal)***
> 	- [ ] Tympanisme généralisé *(Diverticulite sigmoïdienne non compliquée)*
> 	- [ ] Matité déclive *(Diverticulite sigmoïdienne non compliquée · Perforation d'ulcère gastro-duodénal)*
> 	- [ ] Douleur à la percussion *(Diverticulite sigmoïdienne non compliquée · Perforation d'ulcère gastro-duodénal)*
> 	- [ ] Signe du flot *(Diverticulite sigmoïdienne non compliquée)*
> 	- [ ] Tympanisme diffus *(Perforation d'ulcère gastro-duodénal)*
> 	- [ ] Disparition de la matité pré-hépatique *(Perforation d'ulcère gastro-duodénal)*
> 	- [ ] Technique correcte *(Gastroentérite)*
> 	- [ ] Tympanisme *(Gastroentérite)*
> 	- [ ] Matité *(Gastroentérite)*
> 	- [ ] Flèche hépatique *(Gastroentérite)*
> - [ ] **42. Palpation superficielle et profonde *(Diverticulite sigmoïdienne non compliquée)***
> 	- [ ] Douleur à la pression
> 	- [ ] Résistance/masse palpable
> 	- [ ] Défense musculaire
> 	- [ ] Contracture abdominale
> - [ ] **43. Recherche de signes péritonéaux *(Diverticulite sigmoïdienne non compliquée)***
> 	- [ ] Douleur à la décompression (Blumberg)
> 	- [ ] Signe de Murphy
> 	- [ ] Signe du psoas
> 	- [ ] Signe de l'obturateur
> 	- [ ] Signe de Rovsing
> - [ ] **44. Palpation des organes *(Diverticulite sigmoïdienne non compliquée)***
> 	- [ ] Foie
> 	- [ ] Rate
> 	- [ ] Reins
> 	- [ ] Vessie
> - [ ] **45. Examen des orifices herniaires *(Diverticulite sigmoïdienne non compliquée)***
> 	- [ ] Hernies inguinales
> 	- [ ] Hernie crurale
> 	- [ ] Hernie ombilicale
> - [ ] **46. Toucher rectal *(Diverticulite sigmoïdienne non compliquée · Infection génitale haute · Ischémie mésentérique aiguë)***
> 	- [ ] Tonus sphinctérien *(Diverticulite sigmoïdienne non compliquée)*
> 	- [ ] Masses rectales *(Diverticulite sigmoïdienne non compliquée)*
> 	- [ ] Sang au doigtier *(Diverticulite sigmoïdienne non compliquée)*
> 	- [ ] Douglas douloureux *(Diverticulite sigmoïdienne non compliquée)*
> - [ ] **47. Examen gynécologique si indiqué *(Diverticulite sigmoïdienne non compliquée)***
> 	- [ ] Toucher vaginal
> 	- [ ] Mobilité utérine douloureuse
> 	- [ ] Masses annexielles
> - [ ] **48. Désinfection des mains *(Douleurs abdominales non spécifiques)***
> - [ ] **49. Prise de la tension artérielle *(Douleurs abdominales non spécifiques)***
> - [ ] **50. Inspection générale *(Douleurs abdominales non spécifiques)***
> - [ ] **51. Auscultation cardiaque et prise du pouls *(Douleurs abdominales non spécifiques)***
> - [ ] **52. Auscultation pulmonaire *(Douleurs abdominales non spécifiques)***
> - [ ] **53. Évaluation de la capacité de discernement *(Douleurs abdominales non spécifiques)***
> 	- [ ] Évaluation pendant l'entretien
> - [ ] **54. Inspection de la vulve, du vagin et du col *(Endométriose pelvienne)***
> - [ ] **55. Examen bimanuel recto-vaginal *(Endométriose pelvienne)***
> 	- [ ] Utérus
> 	- [ ] Cul-de-sac de Douglas
> - [ ] **56. Palpation des ganglions lymphatiques *(4 diagnostics)***
> - [ ] **57. Palpation abdominale *(4 diagnostics)***
> 	- [ ] Palpation superficielle et profonde *(Reflux gastro-œsophagien (RGO))*
> 	- [ ] Recherche de masse *(Reflux gastro-œsophagien (RGO))*
> 	- [ ] Recherche de douleur épigastrique *(Reflux gastro-œsophagien (RGO))*
> - [ ] **58. Signes péritonéaux *(Infection génitale haute · Ischémie mésentérique aiguë · Rectocolite ulcéro-hémorragique)***
> - [ ] **59. Recherche de signes hémorragiques *(Infection génitale haute)***
> - [ ] **60. Toucher rectal avec inspection de l'anus *(Rectocolite ulcéro-hémorragique)***
> - [ ] **61. Inspection de l'abdomen et de la peau *(Ischémie mésentérique aiguë)***
> 	- [ ] État général
> - [ ] **62. Status cardio-pulmonaire *(Ischémie mésentérique aiguë)***
> 	- [ ] Examen cardiovasculaire
> 	- [ ] Examen pulmonaire
> - [ ] **63. Status vasculaire *(Ischémie mésentérique aiguë)***
> 	- [ ] Recherche de pouls périphériques
> 	- [ ] Recherche d'anévrisme de l'aorte abdominale
> - [ ] **64. Palpation de la rate *(2 grilles sur 20)***
> 	- [ ] Recherche de splénomégalie *(Reflux gastro-œsophagien (RGO))*
> 	- [ ] Décubitus dorsal *(1 grille sur 20)*
> 	- [ ] Décubitus latéral droit *(1 grille sur 20)*
> 	- [ ] Technique bimanuelle correcte *(1 grille sur 20)*
> 	- [ ] Évaluation taille et consistance si palpable *(1 grille sur 20)*
> - [ ] **65. Palpation des reins *(2 grilles sur 20)***
> 	- [ ] Recherche de douleur rénale *(Reflux gastro-œsophagien (RGO))*
> 	- [ ] Palpation bimanuelle *(1 grille sur 20)*
> 	- [ ] Main antérieure sous rebord costal *(1 grille sur 20)*
> 	- [ ] Palpation lors inspiration profonde *(1 grille sur 20)*
> 	- [ ] Évaluation pôle inférieur rein droit *(1 grille sur 20)*
> - [ ] **66. Inspection buccale *(Reflux gastro-œsophagien (RGO))***
> 	- [ ] Recherche de signes d'œsophagite
> 	- [ ] État dentaire
> - [ ] **67. Status abdominal - installation *(2 grilles sur 20)***
> 	- [ ] Bras & jambes décroisées
> 	- [ ] Tête légèrement surélevée
> 	- [ ] Abdomen entièrement visible (premier bouton du pantalon déboutonné ou patient en sous-vêtements)
> 	- [ ] Se place à droite du patient
> - [ ] **68. Status abdominal - auscultation *(Pyélonéphrite)***
> 	- [ ] Les 4 quadrants
> 	- [ ] Auscultation avant toute autre partie du status
> - [ ] **69. Status abdominal - percussion *(Pyélonéphrite)***
> 	- [ ] Les 4 quadrants
> 	- [ ] Délimite la taille du foie en percutant (ou autre technique appropriée)
> - [ ] **70. Status abdominal - palpation *(Pyélonéphrite)***
> 	- [ ] Superficielle
> 	- [ ] Profonde
> 	- [ ] Détente
> - [ ] **71. Status abdominal - tests spécifiques *(Pyélonéphrite)***
> 	- [ ] Palpation du point de McBurney
> 	- [ ] Signe du Psoas
> 	- [ ] Signe de Murphy
> - [ ] **72. Evoque un toucher rectal *(3 grilles sur 20)***
> - [ ] **73. Installation du patient *(Cholangite)***
> 	- [ ] Jambes décroisées
> 	- [ ] Bras le long du corps
> 	- [ ] Tête légèrement surélevée
> 	- [ ] Abdomen visible en entier (si nécessaire, premier bouton du pantalon enlevé)
> 	- [ ] Se positionne à droite de la patiente
> - [ ] **74. Tests spécifiques *(Cholangite)***
> 	- [ ] Signe de Murphy
> 	- [ ] Palpation du point de McBurney
> 	- [ ] Signe du Psoas
> - [ ] **75. DD : appendicite *(1 grille sur 20)***
> 	- [ ] Palpation du point de McBurney
> 	- [ ] Signe du Psoas
> - [ ] **76. S'assure du confort d'installation de la patiente *(Torsion ovarienne)***
> - [ ] **77. Status abdominal *(Torsion ovarienne)***
> 	- [ ] Observation
> 	- [ ] Auscultation
> 	- [ ] Palpation superficielle
> 	- [ ] Palpation profonde
> 	- [ ] Percussion foie et rate
> - [ ] **78. Status urinaire - percussion des loges rénales *(Torsion ovarienne)***
> - [ ] **79. Status gynécologique - 1 *(Torsion ovarienne)***
> 	- [ ] Met des gants
> 	- [ ] Observation du périnée, vestibule
> 	- [ ] Lubrification correcte du spéculum
> - [ ] **80. Status gynécologique - 2 *(Torsion ovarienne)***
> 	- [ ] Insertion du spéculum avec angle de 45°
> 	- [ ] Observation du col
> 	- [ ] Palpation bi-manuelle
> 	- [ ] Mobilisation du col à une main
> 	- [ ] Retire le spéculum sans le fermer
> - [ ] **81. Inspection générale - Ambiance *(Perforation d'ulcère gastro-duodénal)***
> 	- [ ] Agitation ou prostration
> 	- [ ] Position antalgique
> 	- [ ] Faciès douloureux, crispé
> 	- [ ] Pâleur, sueurs froides
> 	- [ ] État de choc
> - [ ] **82. Signes vitaux *(Perforation d'ulcère gastro-duodénal)***
> 	- [ ] Pulsations
> 	- [ ] Tension artérielle
> 	- [ ] Rythme respiratoire
> 	- [ ] Amplitude respiratoire
> 	- [ ] Température
> - [ ] **83. Examen cutané et muqueux *(Perforation d'ulcère gastro-duodénal)***
> 	- [ ] Peau
> 	- [ ] Langue
> 	- [ ] Signes de dénutrition
> 	- [ ] Signes de déshydratation
> - [ ] **84. Palpation superficielle *(Perforation d'ulcère gastro-duodénal)***
> 	- [ ] Défense généralisée
> 	- [ ] Contracture abdominale
> 	- [ ] Hyperesthésie cutanée
> 	- [ ] Douleur maximale épigastrique
> 	- [ ] Extension de la contracture
> - [ ] **85. Palpation profonde *(Perforation d'ulcère gastro-duodénal)***
> 	- [ ] Impossible si contracture
> 	- [ ] Recherche masse si possible
> 	- [ ] Foie et rate
> 	- [ ] Points douloureux spécifiques
> 	- [ ] Douleur à l'ébranlement
> - [ ] **86. Signes péritonéaux spécifiques *(Perforation d'ulcère gastro-duodénal)***
> 	- [ ] Contracture abdominale généralisée
> 	- [ ] Signe du rebond positif
> 	- [ ] Douleur à la décompression brutale
> 	- [ ] Douleur à la toux
> 	- [ ] Douleur à la percussion du talon
> 	- [ ] Position antalgique en chien de fusil
> - [ ] **87. Touchers pelviens *(Perforation d'ulcère gastro-duodénal)***
> 	- [ ] Toucher rectal
> 	- [ ] Bombement douloureux
> 	- [ ] Recherche de sang
> 	- [ ] Toucher vaginal
> - [ ] **88. Inspection abdominale systématique *(Gastroentérite)***
> 	- [ ] Identification des 4 quadrants et 9 régions
> 	- [ ] Abdomen plat vs distendu, symétrique vs asymétrique
> 	- [ ] Recherche de cicatrices chirurgicales
> 	- [ ] Observation lors de la respiration
> 	- [ ] Réaction à la toux
> - [ ] **89. Palpation superficielle de l'abdomen *(Gastroentérite)***
> 	- [ ] Commencer à l'opposé de la zone douloureuse
> 	- [ ] Palpation avec main à plat dans chaque région
> 	- [ ] Évaluation du tonus pariétal spontané
> 	- [ ] Recherche de douleur localisée
> 	- [ ] Recherche de défense ou contracture
> - [ ] **90. Palpation profonde et recherche de masses *(Gastroentérite)***
> 	- [ ] Recherche de masses
> 	- [ ] Palpation de l'aorte abdominale
> 	- [ ] Douleur à l'ébranlement et à la détente
> 	- [ ] Évaluation de la douleur provoquée
> - [ ] **91. Palpation des organes (foie, rate, reins) *(Gastroentérite)***
> 	- [ ] Palpation du bord inférieur du foie
> 	- [ ] Palpation de la rate
> 	- [ ] Palpation bimanuelle des loges rénales
> 	- [ ] Mention du toucher rectal si indiqué
> - [ ] **92. Inspection générale et recherche d'ictère *(1 grille sur 20)***
> 	- [ ] Inspection de la peau
> 	- [ ] Examen des sclères
> 	- [ ] État général
> 	- [ ] Signes vitaux complets
> - [ ] **93. Recherche des signes d'insuffisance hépatocellulaire *(1 grille sur 20)***
> 	- [ ] Angiomes stellaires
> 	- [ ] Erythrose palmaire
> 	- [ ] Gynécomastie
> 	- [ ] Ongles blancs
> 	- [ ] Ecchymoses
> - [ ] **94. Recherche des signes d'hypertension portale *(1 grille sur 20)***
> 	- [ ] Collatérales porto-systémiques
> 	- [ ] Splénomégalie
> 	- [ ] Ascite
> - [ ] **95. Recherche des signes de cholestase chronique *(1 grille sur 20)***
> 	- [ ] Lésions de grattage
> 	- [ ] Xanthélasma
> 	- [ ] Hyperpigmentation cutanée
> - [ ] **96. Examen spécialisé du foie *(1 grille sur 20)***
> 	- [ ] Flèche hépatique
> 	- [ ] Palpation du bord inférieur du foie
> 	- [ ] Signe de Murphy
> 	- [ ] Caractéristiques du foie palpé
> - [ ] **97. Recherche d'ascite *(1 grille sur 20)***
> 	- [ ] Matité déclive à la percussion
> 	- [ ] Patient couché : percussion ligne horizontale ombilic
> 	- [ ] Patient tourné 30-45° : recherche déplacement limite
> 	- [ ] Technique de matité déclive correcte
> - [ ] **98. Examen abdominal général *(1 grille sur 20)***
> 	- [ ] Séquence inspection-auscultation-percussion-palpation
> 	- [ ] 4 quadrants et 9 régions de l'abdomen
> 	- [ ] Technique de percussion et palpation correcte
