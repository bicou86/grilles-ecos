---
aliases:
  - "Mémento Douleur Abdominale"
type: memento-ecos-ssp
ssp: "Douleur Abdominale"
specialite: "Gastro-Hépatologie"
cas: 20
diagnostics: 17
attendus_sans_grille: 5
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

# Douleur Abdominale ⭐️

*Gastro-Hépatologie · 20 grilles · 17 diagnostics documentés · 5 attendus sans grille* — [[SSP — Douleur Abdominale]]

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
> - **German-19** — MICI (Crohn / RCUH) `corrige` · [grille](<file:///Users/damienfulliquet/Developer/GitHub/grilles-ecos/cases/german/German-19_-_Douleur_abdominale_-_Grille_ECOS.html>)
> - **German-20** — Ischémie mésentérique aiguë `corrige` · [grille](<file:///Users/damienfulliquet/Developer/GitHub/grilles-ecos/cases/german/German-20_-_Douleur_abdominale_-_Grille_ECOS.html>)
> - **German-21** — Reflux gastro-œsophagien (RGO) `explicite` · [grille](<file:///Users/damienfulliquet/Developer/GitHub/grilles-ecos/cases/german/German-21_-_Douleur_abdominale_-_Grille_ECOS.html>)
> - **RESCOS-17** — Pyélonéphrite `premier-dd` · [grille](<file:///Users/damienfulliquet/Developer/GitHub/grilles-ecos/cases/rescos/RESCOS-17_-_Douleur_abdominale_-_Grille_ECOS.html>)
> - **RESCOS-18** — Cholangite `premier-dd` · [grille](<file:///Users/damienfulliquet/Developer/GitHub/grilles-ecos/cases/rescos/RESCOS-18_-_Douleur_abdominale_-_Grille_ECOS.html>)
> - **RESCOS-19** — Cholécystite aiguë `premier-dd` · [grille](<file:///Users/damienfulliquet/Developer/GitHub/grilles-ecos/cases/rescos/RESCOS-19_-_Douleur_abdominale_-_Grille_ECOS.html>)
> - **RESCOS-20** — Torsion ovarienne `explicite` · [grille](<file:///Users/damienfulliquet/Developer/GitHub/grilles-ecos/cases/rescos/RESCOS-20_-_Douleur_abdominale_-_Grille_ECOS.html>)
> - **RESCOS-21** — Perforation d'ulcère gastro-duodénal `premier-dd` · [grille](<file:///Users/damienfulliquet/Developer/GitHub/grilles-ecos/cases/rescos/RESCOS-21_-_Douleur_abdominale_-_Grille_ECOS.html>)
> - **RESCOS-22** — Gastroentérite `explicite` · [grille](<file:///Users/damienfulliquet/Developer/GitHub/grilles-ecos/cases/rescos/RESCOS-22_-_Douleur_abdominale_-_ECC_Digestion_-_Grille_ECOS.html>)
> - **RESCOS-23** — Cholécystite aiguë `explicite` · [grille](<file:///Users/damienfulliquet/Developer/GitHub/grilles-ecos/cases/rescos/RESCOS-23_-_Douleur_abdominale_-_ECC_Digestion_-_Grille_ECOS.html>)

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
> - [ ] **5. Antécédents médicaux *(4 grilles sur 20)***
> - [ ] **6. Antécédents chirurgicaux *(4 grilles sur 20)***
> - [ ] **7. Allergies *(10 grilles sur 20)***
> - [ ] **8. Médicaments *(6 grilles sur 20)***
> 	- [ ] Antiacides *(1 grille sur 20)*
> 	- [ ] Fréquence *(1 grille sur 20)*
> - [ ] **9. Hospitalisations *(3 grilles sur 20)***
> - [ ] **10. Contacts malades *(3 grilles sur 20)***
> - [ ] **11. Antécédents familiaux *(5 grilles sur 20)***
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
> - [ ] **120. Identification des symptômes principaux *(Endométriose pelvienne · MICI (Crohn / RCUH))***
> - [ ] **121. Début des symptômes *(4 diagnostics)***
> - [ ] **122. Fréquence et périodicité *(4 diagnostics)***
> - [ ] **123. Caractère de la douleur *(5 diagnostics)***
> - [ ] **124. Facteurs aggravants ou soulageants *(4 diagnostics)***
> - [ ] **125. Douleurs liées à l'alimentation *(Endométriose pelvienne · Ischémie mésentérique aiguë · MICI (Crohn / RCUH))***
> - [ ] **126. Symptômes généraux *(Endométriose pelvienne · Infection génitale haute · MICI (Crohn / RCUH))***
> 	- [ ] Fièvre *(Endométriose pelvienne · MICI (Crohn / RCUH))*
> 	- [ ] Perte de poids
> 	- [ ] Sueurs nocturnes
> 	- [ ] Fièvre prolongée *(Infection génitale haute)*
> - [ ] **127. Symptômes digestifs *(Endométriose pelvienne · Infection génitale haute · MICI (Crohn / RCUH))***
> 	- [ ] Transit intestinal *(Endométriose pelvienne)*
> 	- [ ] Gaz *(Endométriose pelvienne)*
> 	- [ ] Nausées/Vomissements
> 	- [ ] Sang dans les vomissements
> 	- [ ] Constipation *(Endométriose pelvienne · MICI (Crohn / RCUH))*
> 	- [ ] Diarrhée *(Endométriose pelvienne · MICI (Crohn / RCUH))*
> 	- [ ] Sang dans les selles *(Endométriose pelvienne · Infection génitale haute)*
> 	- [ ] Transit intestinal et gaz *(Infection génitale haute · MICI (Crohn / RCUH))*
> 	- [ ] Diarrhée/Constipation *(Infection génitale haute)*
> 	- [ ] Aspect des selles *(MICI (Crohn / RCUH))*
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
> - [ ] **132. Migration de la douleur *(Infection génitale haute · Ischémie mésentérique aiguë · MICI (Crohn / RCUH))***
> - [ ] **133. Mode de début *(Infection génitale haute · Ischémie mésentérique aiguë · MICI (Crohn / RCUH))***
> - [ ] **134. Fièvre *(Infection génitale haute)***
> - [ ] **135. Symptômes extra-intestinaux *(MICI (Crohn / RCUH))***
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
> 	- [ ] Teint *(Infection génitale haute · MICI (Crohn / RCUH))*
> 	- [ ] État général *(Infection génitale haute · Reflux gastro-œsophagien (RGO))*
> 	- [ ] Abdomen *(Infection génitale haute)*
> 	- [ ] Cavité buccale *(MICI (Crohn / RCUH))*
> 	- [ ] Peau *(MICI (Crohn / RCUH))*
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
> - [ ] **58. Signes péritonéaux *(Infection génitale haute · Ischémie mésentérique aiguë · MICI (Crohn / RCUH))***
> - [ ] **59. Recherche de signes hémorragiques *(Infection génitale haute)***
> - [ ] **60. Toucher rectal avec inspection de l'anus *(MICI (Crohn / RCUH))***
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

> [!success] 💊 Management — partagé par plusieurs diagnostics
> - [ ] **1. Hypothèses diagnostiques *(Appendicite aiguë · Cancer de l'ovaire · Cholécystite aiguë · Maladie cœliaque — 4 grilles sur 20)***
> - [ ] **2. Communication avec la patiente *(Appendicite aiguë · Cancer de l'ovaire · Cholécystite aiguë — 3 grilles sur 20)***
> 	- [ ] Explications au patient des impressions diagnostiques préliminaires
> 	- [ ] Explication du plan de prise en charge
> 	- [ ] Utilisation d'un langage non médical et clarification des termes médicaux
> 	- [ ] Évaluation de l'accord du patient avec le plan diagnostique
> 	- [ ] Recherche des préoccupations et questions du patient
> - [ ] **3. Examens complémentaires urgents *(Appendicite aiguë · Cancer de l'ovaire — 2 grilles sur 20)***
> 	- [ ] Test de grossesse urinaire *(Appendicite aiguë — 1 grille sur 20)*
> 	- [ ] FSC avec différentielle *(Appendicite aiguë — 1 grille sur 20)*
> 	- [ ] VS, CRP *(Appendicite aiguë — 1 grille sur 20)*
> 	- [ ] Analyse d'urine et ECBU *(Appendicite aiguë — 1 grille sur 20)*
> 	- [ ] US abdominale et pelvienne *(Appendicite aiguë — 1 grille sur 20)*
> 	- [ ] Examen pelvien *(Cancer de l'ovaire — 1 grille sur 20)*
> 	- [ ] Β-hCG sérique *(Cancer de l'ovaire — 1 grille sur 20)*
> 	- [ ] FSC *(Cancer de l'ovaire — 1 grille sur 20)*
> - [ ] **4. Examens complémentaires secondaires *(Appendicite aiguë · Cancer de l'ovaire — 2 grilles sur 20)***
> 	- [ ] Examen pelvien *(Appendicite aiguë — 1 grille sur 20)*
> 	- [ ] Prélèvements cervicaux et urétraux *(Appendicite aiguë — 1 grille sur 20)*
> 	- [ ] CT abdominal *(Appendicite aiguë — 1 grille sur 20)*
> 	- [ ] CA-125 *(Cancer de l'ovaire — 1 grille sur 20)*
> 	- [ ] Laparoscopie *(Cancer de l'ovaire — 1 grille sur 20)*
> 	- [ ] Test génétique BRCA *(Cancer de l'ovaire — 1 grille sur 20)*
> - [ ] **5. Conseil et prévention *(Appendicite aiguë · Cancer de l'ovaire — 2 grilles sur 20)***
> 	- [ ] Conseil sur les pratiques sexuelles sûres *(Appendicite aiguë — 1 grille sur 20)*
> 	- [ ] Réaction appropriée au défi concernant la grossesse *(Appendicite aiguë — 1 grille sur 20)*
> 	- [ ] Conseil sur les options de contraception *(Cancer de l'ovaire — 1 grille sur 20)*
> 	- [ ] Réaction appropriée au défi concernant la chirurgie *(Cancer de l'ovaire — 1 grille sur 20)*
> - [ ] **6. Examens d'imagerie *(Cancer de l'ovaire · Diverticulite sigmoïdienne non compliquée — 2 grilles sur 20)***
> 	- [ ] US transvaginale *(Cancer de l'ovaire — 1 grille sur 20)*
> 	- [ ] US transabdominale *(Cancer de l'ovaire — 1 grille sur 20)*
> 	- [ ] Échographie abdominale *(Diverticulite sigmoïdienne non compliquée — 1 grille sur 20)*
> 	- [ ] CT abdominal avec contraste (gold standard) *(Diverticulite sigmoïdienne non compliquée — 1 grille sur 20)*
> 	- [ ] Radiographie abdominale si suspicion de perforation *(Diverticulite sigmoïdienne non compliquée — 1 grille sur 20)*
> 	- [ ] IRM si contre-indication au CT *(Diverticulite sigmoïdienne non compliquée — 1 grille sur 20)*
> - [ ] **7. Examens biologiques *(Diverticulite sigmoïdienne non compliquée · Maladie cœliaque — 2 grilles sur 20)***
> 	- [ ] FSC, VGM, TCMH *(Maladie cœliaque — 1 grille sur 20)*
> 	- [ ] Panel IgE allergies pédiatriques *(Maladie cœliaque — 1 grille sur 20)*
> 	- [ ] FSC avec formule *(Diverticulite sigmoïdienne non compliquée — 1 grille sur 20)*
> 	- [ ] CRP *(Diverticulite sigmoïdienne non compliquée — 1 grille sur 20)*
> 	- [ ] VS si disponible *(Diverticulite sigmoïdienne non compliquée — 1 grille sur 20)*
> 	- [ ] Ionogramme, urée, créatinine *(Diverticulite sigmoïdienne non compliquée — 1 grille sur 20)*
> 	- [ ] Analyse d'urine (ECBU) *(Diverticulite sigmoïdienne non compliquée — 1 grille sur 20)*
> 	- [ ] Test de grossesse si approprié *(Diverticulite sigmoïdienne non compliquée — 1 grille sur 20)*
> - [ ] **8. Laboratoire *(Cholécystite aiguë · Purpura de Schönlein-Henoch (vascularite à IgA) — 2 grilles sur 20)***
> - [ ] **9. Échographie *(Cholécystite aiguë · Purpura de Schönlein-Henoch (vascularite à IgA) — 2 grilles sur 20)***
> - [ ] **10. Diagnostic principal *(Diverticulite sigmoïdienne non compliquée · Reflux gastro-œsophagien (RGO) — 2 grilles sur 20)***
> 	- [ ] Reflux gastro-œsophagien (RGO) *(Reflux gastro-œsophagien (RGO) — 1 grille sur 20)*
> - [ ] **11. Diagnostics différentiels *(Diverticulite sigmoïdienne non compliquée · Douleurs abdominales non spécifiques · Endométriose pelvienne · Infection génitale haute · Ischémie mésentérique aiguë · MICI (Crohn / RCUH) · Pyélonéphrite · Reflux gastro-œsophagien (RGO) — 8 grilles sur 20)***
> - [ ] **12. Prise en charge thérapeutique *(Diverticulite sigmoïdienne non compliquée · Endométriose pelvienne · Infection génitale haute · MICI (Crohn / RCUH) · Reflux gastro-œsophagien (RGO) — 5 grilles sur 20)***
> 	- [ ] Analgésiques *(Endométriose pelvienne — 1 grille sur 20)*
> 	- [ ] Contraceptifs oraux (inhibiteurs de l'ovulation) *(Endométriose pelvienne — 1 grille sur 20)*
> 	- [ ] Thérapie endocrinienne *(Endométriose pelvienne — 1 grille sur 20)*
> 	- [ ] Ablation chirurgicale en cas de complications ou stades très avancés *(Endométriose pelvienne — 1 grille sur 20)*
> 	- [ ] Doxycycline / Azithromycine *(Infection génitale haute — 1 grille sur 20)*
> 	- [ ] Traitement du partenaire *(Infection génitale haute — 1 grille sur 20)*
> 	- [ ] Chirurgie en cas d'abcès ou autres complications *(Infection génitale haute — 1 grille sur 20)*
> 	- [ ] Conseils nutritionnels pour prévenir les carences *(MICI (Crohn / RCUH) — 1 grille sur 20)*
> 	- [ ] Induction de rémission *(MICI (Crohn / RCUH) — 1 grille sur 20)*
> 	- [ ] Maintien de rémission *(MICI (Crohn / RCUH) — 1 grille sur 20)*
> 	- [ ] Coloscopies de contrôle régulières *(MICI (Crohn / RCUH) — 1 grille sur 20)*
> 	- [ ] Mesures hygiéno-diététiques *(Reflux gastro-œsophagien (RGO) — 1 grille sur 20)*
> 	- [ ] Lit : surélévation de la tête de lit *(Reflux gastro-œsophagien (RGO) — 1 grille sur 20)*
> 	- [ ] Restriction de la consommation de café et d'alcool *(Reflux gastro-œsophagien (RGO) — 1 grille sur 20)*
> 	- [ ] Éviter les aliments acides *(Reflux gastro-œsophagien (RGO) — 1 grille sur 20)*
> 	- [ ] Éviter les repas tardifs *(Reflux gastro-œsophagien (RGO) — 1 grille sur 20)*
> 	- [ ] Perte de poids *(Reflux gastro-œsophagien (RGO) — 1 grille sur 20)*
> 	- [ ] Éviter les médicaments diminuant la pression du sphincter *(Reflux gastro-œsophagien (RGO) — 1 grille sur 20)*
> 	- [ ] Traitement médicamenteux *(Reflux gastro-œsophagien (RGO) — 1 grille sur 20)*
> 	- [ ] Inhibiteurs de la pompe à protons (IPP) *(Reflux gastro-œsophagien (RGO) — 1 grille sur 20)*
> 	- [ ] Éventuellement antagonistes des récepteurs H2 *(Reflux gastro-œsophagien (RGO) — 1 grille sur 20)*
> 	- [ ] En cas de résistance thérapeutique *(Reflux gastro-œsophagien (RGO) — 1 grille sur 20)*
> 	- [ ] Fundoplicature *(Reflux gastro-œsophagien (RGO) — 1 grille sur 20)*
> 	- [ ] En cas d'œsophage de Barrett *(Reflux gastro-œsophagien (RGO) — 1 grille sur 20)*
> 	- [ ] Contrôles endoscopiques réguliers *(Reflux gastro-œsophagien (RGO) — 1 grille sur 20)*
> - [ ] **13. Diagnostic suspecté *(Douleurs abdominales non spécifiques · Endométriose pelvienne · Infection génitale haute · Ischémie mésentérique aiguë · MICI (Crohn / RCUH) — 5 grilles sur 20)***
> 	- [ ] Hidden agenda (demande cachée) *(Douleurs abdominales non spécifiques — 1 grille sur 20)*
> 	- [ ] Endométriose *(Endométriose pelvienne — 1 grille sur 20)*
> 	- [ ] Annexite aiguë (salpingite) *(Infection génitale haute — 1 grille sur 20)*
> 	- [ ] Colite ulcéreuse (diagnostic primaire) *(MICI (Crohn / RCUH) — 1 grille sur 20)*
> 	- [ ] Infarctus mésentérique aigu *(Ischémie mésentérique aiguë — 1 grille sur 20)*
> - [ ] **14. Examens diagnostiques *(Endométriose pelvienne · Infection génitale haute · Ischémie mésentérique aiguë · MICI (Crohn / RCUH) · Reflux gastro-œsophagien (RGO) — 5 grilles sur 20)***
> 	- [ ] Analyses sanguines
> 	- [ ] Test de grossesse *(Endométriose pelvienne · Infection génitale haute — 2 grilles sur 20)*
> 	- [ ] Prélèvement vaginal et cervical *(Endométriose pelvienne — 1 grille sur 20)*
> 	- [ ] Échographie vaginale *(Endométriose pelvienne — 1 grille sur 20)*
> 	- [ ] Laparoscopie diagnostique *(Endométriose pelvienne — 1 grille sur 20)*
> 	- [ ] Échographie abdominale/vaginale *(Infection génitale haute — 1 grille sur 20)*
> 	- [ ] Consultation gynécologique pour examen au spéculum avec prélèvement *(Infection génitale haute — 1 grille sur 20)*
> 	- [ ] Recherche de Chlamydia/Gonocoque *(Infection génitale haute — 1 grille sur 20)*
> 	- [ ] Examen bimanuel *(Infection génitale haute — 1 grille sur 20)*
> 	- [ ] Examen bactériologique des selles *(MICI (Crohn / RCUH) — 1 grille sur 20)*
> 	- [ ] Échographie abdominale *(Ischémie mésentérique aiguë · MICI (Crohn / RCUH) — 2 grilles sur 20)*
> 	- [ ] Iléo-coloscopie avec biopsies *(MICI (Crohn / RCUH) — 1 grille sur 20)*
> 	- [ ] Radiographie thoracique *(Ischémie mésentérique aiguë — 1 grille sur 20)*
> 	- [ ] ECG *(Ischémie mésentérique aiguë — 1 grille sur 20)*
> 	- [ ] Radiographie abdominale *(Ischémie mésentérique aiguë — 1 grille sur 20)*
> 	- [ ] Doppler couleur, angio-IRM *(Ischémie mésentérique aiguë — 1 grille sur 20)*
> 	- [ ] Coloscopie *(Ischémie mésentérique aiguë — 1 grille sur 20)*
> 	- [ ] Gastroscopie *(Reflux gastro-œsophagien (RGO) — 1 grille sur 20)*
> 	- [ ] PH-métrie œsophagienne *(Reflux gastro-œsophagien (RGO) — 1 grille sur 20)*
> 	- [ ] Test à l'uréase avec biopsie *(Reflux gastro-œsophagien (RGO) — 1 grille sur 20)*
> 	- [ ] Radiographie ou CT *(Reflux gastro-œsophagien (RGO) — 1 grille sur 20)*
> - [ ] **15. Evoque un diagnostic différentiel plausible *(Cholangite · Cholécystite aiguë — 2 grilles sur 20)***
> 	- [ ] Cholangite
> 	- [ ] Pancréatite *(Cholangite — 1 grille sur 20)*
> 	- [ ] Appendicite *(Cholangite — 1 grille sur 20)*
> 	- [ ] Hépatite
> 	- [ ] Pyélonéphrite *(Cholangite — 1 grille sur 20)*
> 	- [ ] Trouble gynécologique *(Cholangite — 1 grille sur 20)*
> 	- [ ] Cholécystite *(Cholécystite aiguë — 1 grille sur 20)*
> 	- [ ] Néoplasie *(Cholécystite aiguë — 1 grille sur 20)*
> 	- [ ] Gastrite / inflammation du tube digestif *(Cholécystite aiguë — 1 grille sur 20)*
> 	- [ ] Stase biliaire sur compression néoplasique (p.ex. cancer pancréatique) *(Cholécystite aiguë — 1 grille sur 20)*
> - [ ] **16. Évaluation de la sévérité et des complications *(Cholécystite aiguë · Gastroentérite — 2 grilles sur 20)***
> 	- [ ] Évaluation du degré de déshydratation *(Gastroentérite — 1 grille sur 20)*
> 	- [ ] Recherche de signes de choc *(Gastroentérite — 1 grille sur 20)*
> 	- [ ] Évaluation de la perte pondérale *(Gastroentérite — 1 grille sur 20)*
> 	- [ ] Exclusion de complications *(Gastroentérite — 1 grille sur 20)*
> 	- [ ] Recherche signes de cholécystite *(Cholécystite aiguë — 1 grille sur 20)*
> 	- [ ] Exclusion angiocholite *(Cholécystite aiguë — 1 grille sur 20)*
> 	- [ ] Évaluation retentissement général *(Cholécystite aiguë — 1 grille sur 20)*
> 	- [ ] Recherche signes de péritonite *(Cholécystite aiguë — 1 grille sur 20)*
> - [ ] **17. Proposition d'examens complémentaires *(Cholécystite aiguë · Gastroentérite — 2 grilles sur 20)***
> 	- [ ] Bilan biologique
> 	- [ ] Coproculture et recherche de parasites *(Gastroentérite — 1 grille sur 20)*
> 	- [ ] Bandelette urinaire *(Gastroentérite — 1 grille sur 20)*
> 	- [ ] Imagerie abdominale si doute diagnostique *(Gastroentérite — 1 grille sur 20)*
> 	- [ ] Échographie abdominale *(Cholécystite aiguë — 1 grille sur 20)*
> 	- [ ] FSC, CRP *(Cholécystite aiguë — 1 grille sur 20)*
> 	- [ ] Lipasémie *(Cholécystite aiguë — 1 grille sur 20)*
> - [ ] **18. Prise en charge thérapeutique immédiate *(Cholécystite aiguë · Gastroentérite — 2 grilles sur 20)***
> 	- [ ] Réhydratation *(Gastroentérite — 1 grille sur 20)*
> 	- [ ] Correction des pertes électrolytiques *(Gastroentérite — 1 grille sur 20)*
> 	- [ ] Traitement symptomatique *(Gastroentérite — 1 grille sur 20)*
> 	- [ ] Repos digestif initial puis réalimentation progressive *(Gastroentérite — 1 grille sur 20)*
> 	- [ ] Antalgiques *(Cholécystite aiguë — 1 grille sur 20)*
> 	- [ ] Antispasmodiques *(Cholécystite aiguë — 1 grille sur 20)*
> 	- [ ] Antiémétiques si vomissements *(Cholécystite aiguë — 1 grille sur 20)*
> 	- [ ] Mise à jeun initiale *(Cholécystite aiguë — 1 grille sur 20)*
> - [ ] **19. Surveillance et critères d'hospitalisation *(Cholécystite aiguë · Gastroentérite — 2 grilles sur 20)***
> 	- [ ] Critères d'hospitalisation
> 	- [ ] Surveillance clinique
> 	- [ ] Critères d'amélioration *(Gastroentérite — 1 grille sur 20)*
> 	- [ ] Planification du suivi ambulatoire *(Gastroentérite — 1 grille sur 20)*
> 	- [ ] Signes d'alarme *(Cholécystite aiguë — 1 grille sur 20)*
> 	- [ ] Suivi ambulatoire programmé *(Cholécystite aiguë — 1 grille sur 20)*

> [!success] 💊 Management — si Appendicite aiguë
> *Aucun item propre à ce diagnostic* — tout son management figure dans l'encadré partagé ci-dessus.

> [!success] 💊 Management — si Cancer de l'ovaire
> *Aucun item propre à ce diagnostic* — tout son management figure dans l'encadré partagé ci-dessus.

> [!success] 💊 Management — si Cholangite
> - [ ] **1. Mentionne une cholécystite comme hypothèse diagnostique principale**

> [!success] 💊 Management — si Cholécystite aiguë
> - [ ] **1. Examens complémentaires initiaux *(1 grille sur 4)***
> 	- [ ] US abdominale
> 	- [ ] Bilan hépatique complet
> 	- [ ] Transaminases
> 	- [ ] Enzymes pancréatiques
> 	- [ ] FSC
> 	- [ ] Ionogramme et calcium
> - [ ] **2. Examens complémentaires de seconde ligne *(1 grille sur 4)***
> 	- [ ] CT abdominal
> 	- [ ] ERCP
> - [ ] **3. Conseil et défis *(1 grille sur 4)***
> 	- [ ] Conseil sur les options de soutien pour les changements de poids et d'alimentation
> 	- [ ] Réaction appropriée au défi concernant le poids
> - [ ] **4. Formule sanguine *(1 grille sur 4)***
> - [ ] **5. Status urinaire *(1 grille sur 4)***
> - [ ] **6. ECG *(1 grille sur 4)***
> - [ ] **7. Diagnostic de travail *(1 grille sur 4)***
> - [ ] **8. Cholécysectomie laparoscopique *(1 grille sur 4)***
> - [ ] **9. Antibiothérapie i.v. *(1 grille sur 4)***
> - [ ] **10. Réhydratation i.v. *(1 grille sur 4)***
> - [ ] **11. Analgésie *(1 grille sur 4)***
> - [ ] **12. Hospitalisation *(1 grille sur 4)***
> - [ ] **13. Laisser à jeun *(1 grille sur 4)***
> - [ ] **14. Mentionne l'hypothèse diagnostique cholélithiase / cholédocholithiase *(1 grille sur 4)***
> - [ ] **15. Diagnostic principal et classification *(1 grille sur 4)***
> 	- [ ] Évoque colique hépatique/cholécystite
> 	- [ ] Classification selon durée
> 	- [ ] Différenciation avec angiocholite
> 	- [ ] Facteurs de risque
> - [ ] **16. Traitement spécifique selon diagnostic *(1 grille sur 4)***
> 	- [ ] Cholécystectomie
> 	- [ ] Timing chirurgical
> 	- [ ] Antibiothérapie si cholécystite
> 	- [ ] CPRE si angiocholite
> - [ ] **17. Conseils diététiques et préventifs *(1 grille sur 4)***
> 	- [ ] Régime pauvre en graisses
> 	- [ ] Perte de poids progressive
> 	- [ ] Repas fractionnés
> 	- [ ] Éviter jeûne prolongé
> - [ ] **18. Information du patient et planification *(1 grille sur 4)***
> 	- [ ] Explication du diagnostic probable
> 	- [ ] Information sur évolution et traitement
> 	- [ ] Conseils pour récidive
> 	- [ ] Planification chirurgicale si indiquée

> [!success] 💊 Management — si Diverticulite sigmoïdienne non compliquée
> - [ ] **1. Classification de la diverticulite**
> 	- [ ] Classification de Hinchey
> 	- [ ] Diverticulite non compliquée
> 	- [ ] Diverticulite compliquée (abcès, perforation, péritonite)
> - [ ] **2. Suivi et surveillance**
> 	- [ ] Contrôle clinique à 48-72h si ambulatoire
> 	- [ ] Contrôle biologique si pas d'amélioration
> 	- [ ] Coloscopie 6-8 semaines après l'épisode
> 	- [ ] Éducation sur les signes d'alarme
> - [ ] **3. Critères d'hospitalisation**
> - [ ] **4. Complications potentielles**
> 	- [ ] Abcès péricolique
> 	- [ ] Perforation avec péritonite
> 	- [ ] Fistules (colovésicale, colovaginale)
> 	- [ ] Sténose colique
> 	- [ ] Hémorragie diverticulaire
> - [ ] **5. Éducation du patient**
> 	- [ ] Explication de la pathologie diverticulaire
> 	- [ ] Importance de l'observance thérapeutique
> 	- [ ] Modifications du mode de vie
> 	- [ ] Signes nécessitant une reconsultation urgente
> 	- [ ] Prévention des récidives

> [!success] 💊 Management — si Douleurs abdominales non spécifiques
> - [ ] **1. Prescription médicamenteuse**
> 	- [ ] Pilule contraceptive combinée
> 	- [ ] Explication sur la prise : 1ère pilule le 1er jour des règles
> 	- [ ] Puis 3 semaines chaque jour
> 	- [ ] Puis 1 semaine de pause
> - [ ] **2. Information sur les effets secondaires**
> 	- [ ] Effets secondaires bénins
> 	- [ ] Situations d'urgence
> - [ ] **3. Conseils et éducation**
> 	- [ ] Protection contre les infections sexuellement transmissibles non assurée par la pilule
> 	- [ ] Contraception post-coïtale mentionnée en cas de grossesse possible
> 	- [ ] Recommandation de contrôle chez le gynécologue
> 	- [ ] Promesse de secret médical, mais encouragement à parler avec les parents
> 	- [ ] Si pilule oubliée 1x : préservatif pendant 7-14 jours
> 	- [ ] Attention en cas de diarrhée/vomissements, antibiotiques, millepertuis, pamplemousse

> [!success] 💊 Management — si Endométriose pelvienne
> - [ ] **1. Information et éducation de la patiente**
> 	- [ ] Explication que les symptômes disparaissent souvent lors de l'aménorrhée ou de la grossesse
> 	- [ ] Information sur les complications possibles
> 	- [ ] Information sur les récidives possibles après traitement

> [!success] 💊 Management — si Gastroentérite
> - [ ] **1. Diagnostic principal et différentiel**
> 	- [ ] Évoque gastro-entérite aiguë
> 	- [ ] Probablement d'origine infectieuse
> 	- [ ] Contexte de voyage en zone tropicale
> 	- [ ] Diagnostic différentiel
> - [ ] **2. Traitement spécifique et antibiotiques**
> 	- [ ] Indication d'antibiothérapie
> 	- [ ] Choix antibiotique adapté
> 	- [ ] Traitement antiparasitaire si indiqué
> 	- [ ] Probiotiques pour restaurer flore intestinale
> - [ ] **3. Conseils diététiques et de prévention**
> 	- [ ] Réalimentation progressive
> 	- [ ] Conseils d'hygiène
> 	- [ ] Éviction professionnelle si nécessaire
> 	- [ ] Prévention pour futurs voyages
> - [ ] **4. Information du patient et éducation**
> 	- [ ] Explication du diagnostic et évolution probable
> 	- [ ] Signes d'alarme nécessitant reconsultation
> 	- [ ] Importance de la compliance thérapeutique
> 	- [ ] Conseils pour la reprise du travail

> [!success] 💊 Management — si Hépatite (virale/alcoolique)
> *Aucune grille de cette SSP ne documente ce diagnostic* — mais le corpus le documente ailleurs : [[Mémento — Ictère]] (1 grille).

> [!success] 💊 Management — si Infarctus du myocarde / SCA
> *Aucune grille de cette SSP ne documente ce diagnostic* — mais le corpus le documente ailleurs : [[Mémento — Douleur Thoracique]] (1 grille).

> [!success] 💊 Management — si Infection génitale haute
> - [ ] **1. Information de la patiente**
> 	- [ ] Information sur les complications possibles
> 	- [ ] Douleurs pelviennes chroniques possibles
> 	- [ ] Risque accru de grossesse extra-utérine

> [!success] 💊 Management — si Ischémie mésentérique aiguë
> - [ ] **1. Prise en charge thérapeutique urgente**
> 	- [ ] Tolérance à l'ischémie intestinale maximale 6 heures !
> 	- [ ] Dès la suspicion clinique
> 	- [ ] Angiographie et laparotomie exploratrice
> 	- [ ] Selon les constatations : embolectomie, désobstruction, pontage
> 	- [ ] Réévaluation du traitement médicamenteux

> [!success] 💊 Management — si Maladie cœliaque
> - [ ] **1. Examens complémentaires de première intention**
> 	- [ ] Examen physique
> 	- [ ] Anticorps anti-transglutaminase tissulaire IgA (tTG)
> 	- [ ] IgA quantitatives
> - [ ] **2. Communication avec le parent**
> 	- [ ] Explications au parent des impressions diagnostiques préliminaires
> 	- [ ] Explication du plan de prise en charge
> 	- [ ] Utilisation d'un langage non médical et clarification des termes médicaux
> 	- [ ] Évaluation de l'accord du parent avec le plan diagnostique
> 	- [ ] Recherche des préoccupations et questions du parent
> - [ ] **3. Soutien et conseils parentaux**
> 	- [ ] Réaction appropriée au défi concernant la frustration parentale
> 	- [ ] Conseils pour rester calme lors des épisodes
> 	- [ ] Éviter punitions et récompenses liées aux symptômes
> 	- [ ] Importance du suivi médical
> 	- [ ] Rassurer sur la démarche diagnostique

> [!success] 💊 Management — si MICI (Crohn / RCUH)
> - [ ] **1. Information sur les complications**
> 	- [ ] Mégacôlon toxique
> 	- [ ] Perforation
> 	- [ ] Hémorragie sévère
> 	- [ ] Cancer du côlon

> [!success] 💊 Management — si Pancréatite aiguë
> *Aucune grille du corpus ne documente ce diagnostic* — il est pourtant attendu de cette SSP. **Trou de révision à combler ailleurs.**

> [!success] 💊 Management — si Perforation d'ulcère gastro-duodénal
> - [ ] **1. Diagnostics différentiels de l'abdomen aigu**
> - [ ] **2. Examens complémentaires en urgence**
> 	- [ ] ASP debout face (ou thorax debout): croissant gazeux sous-diaphragmatique
> 	- [ ] CT abdominal sans et avec injection: pneumopéritoine, liquide libre
> 	- [ ] FSC: hyperleucocytose, hémoconcentration
> 	- [ ] Ionogramme, urée, créatinine: déshydratation, insuffisance rénale
> 	- [ ] Bilan préopératoire: groupe sanguin, RAI, TP, TCA
> 	- [ ] Gazométrie artérielle: acidose métabolique si choc
> - [ ] **3. Signes radiologiques de pneumopéritoine**
> 	- [ ] ASP/Thorax debout: croissant gazeux sous les coupoles
> 	- [ ] Signe de Rigler: double contour des anses (air des deux côtés)
> 	- [ ] Ligament falciforme visible
> 	- [ ] Air péri-hépatique
> 	- [ ] CT: sensibilité maximale pour air libre
> 	- [ ] Recherche du site de perforation
> - [ ] **4. Prise en charge initiale d'urgence**
> - [ ] **5. Traitement chirurgical en urgence**
> 	- [ ] Indication formelle: péritonite généralisée
> 	- [ ] Laparotomie ou laparoscopie selon expertise
> 	- [ ] Suture simple de la perforation
> 	- [ ] Épiplooplastie (patch épiploïque)
> 	- [ ] Toilette péritonéale abondante
> 	- [ ] Drainage de la cavité péritonéale
> 	- [ ] Biopsie des berges (éliminer cancer)
> - [ ] **6. Complications et surveillance**
> - [ ] **7. Traitement post-opératoire et prévention**
> 	- [ ] IPP per os 8 semaines minimum
> 	- [ ] Éradication H. pylori si positive
> 	- [ ] Trithérapie: IPP + amoxicilline + clarithromycine 14j
> 	- [ ] Quadrithérapie si échec: IPP + bismuth + tétracycline + métronidazole
> 	- [ ] Arrêt AINS, aspirine si possible
> 	- [ ] Sevrage tabagique impératif
> 	- [ ] Contrôle endoscopique à 6-8 semaines
> 	- [ ] Surveillance cicatrisation et biopsies

> [!success] 💊 Management — si Péritonite
> *Aucune grille du corpus ne documente ce diagnostic* — il est pourtant attendu de cette SSP. **Trou de révision à combler ailleurs.**

> [!success] 💊 Management — si Purpura de Schönlein-Henoch (vascularite à IgA)
> - [ ] **1. Créatinine**
> - [ ] **2. CRP**
> - [ ] **3. Hémogramme**
> - [ ] **4. Urine**
> - [ ] **5. Diagnostic présumé**
> - [ ] **6. Atteinte rénale**
> - [ ] **7. Antalgie**
> - [ ] **8. Instruction**
> - [ ] **9. Glucocorticoïdes**
> - [ ] **10. Surveillance hospitalière**
> - [ ] **11. Contrôle rénal**
> - [ ] **12. Avis néphrologique**

> [!success] 💊 Management — si Pyélonéphrite
> - [ ] **1. Hypothèse diagnostique principale**
> - [ ] **2. Examens complémentaires proposés**
> 	- [ ] Imagerie (US/CT) pour déterminer la meilleure prise en charge
> 	- [ ] Bandelette urinaire / analyse d'urine
> 	- [ ] Bilan sanguin (formule sanguine, fonction rénale, CRP)
> - [ ] **3. Antalgie proposée**

> [!success] 💊 Management — si Reflux gastro-œsophagien (RGO)
> *Aucun item propre à ce diagnostic* — tout son management figure dans l'encadré partagé ci-dessus.

> [!success] 💊 Management — si Torsion ovarienne
> - [ ] **1. Demande un test de grossesse**
> - [ ] **2. Demande un examen de laboratoire**
> 	- [ ] FSC
> 	- [ ] CRP
> - [ ] **3. Demande un US ou un CT**
> - [ ] **4. Évoque le diagnostic de torsion ovarienne**
> - [ ] **5. Propose une consultation immédiate aux urgences de gynécologie**

> [!success] 💊 Management — si Ulcère gastro-duodénal
> *Aucune grille de cette SSP ne documente ce diagnostic* — mais le corpus le documente ailleurs : « Rectorragies & Hémorragie Digestive Basse » (1 grille, hors lot).
