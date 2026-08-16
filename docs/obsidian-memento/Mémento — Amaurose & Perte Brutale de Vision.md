---
aliases:
  - "Mémento Amaurose & Perte Brutale de Vision"
type: memento-ecos-ssp
ssp: "Amaurose & Perte Brutale de Vision"
cas: 5
diagnostics: 5
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

# Amaurose & Perte Brutale de Vision

*5 grilles · 5 diagnostics documentés · 1 attendu absent du corpus* — [[SSP — Amaurose & Perte Brutale de Vision]]

> [!abstract] Les 5 grilles fusionnées
> - **AMBOSS-34** — AVC `premier-dd` · [grille](<file:///Users/damienfulliquet/Developer/GitHub/grilles-ecos/cases/amboss/AMBOSS-34_-_Perte_de_vision_-_Homme_66_ans_-_Grille_ECOS.html>)
> - **AZYGOS-40** — OACR / Occlusion rétinienne `diagnostic-travail` · [grille](<file:///Users/damienfulliquet/Developer/GitHub/grilles-ecos/docs/azygos-grilles/f0f3ec7f-0c04-4307-a694-3f4a12c6eb9c.json>)
> - **AZYGOS-48** — Décollement de rétine `diagnostic-travail` · [grille](<file:///Users/damienfulliquet/Developer/GitHub/grilles-ecos/docs/azygos-grilles/68e9d154-8aea-43fd-a9fe-29bb5f8335f6.json>)
> - **German-69** — Cataracte `explicite` · [grille](<file:///Users/damienfulliquet/Developer/GitHub/grilles-ecos/cases/german/German-69_-_Perte_de_vision_-_Grille_ECOS.html>)
> - **RESCOS-3** — Horton (artérite à cellules géantes) `explicite` · [grille](<file:///Users/damienfulliquet/Developer/GitHub/grilles-ecos/cases/rescos/RESCOS-3_-_Amaurose_-_Grille_ECOS.html>)

> [!note] 📋 Anamnèse
> - [ ] **1. Motif principal *(AVC)***
> - [ ] **2. Caractérisation de la perte de vision *(AVC)***
> 	- [ ] Début
> 	- [ ] Constante/intermittente
> 	- [ ] Événements précipitants
> 	- [ ] Progression
> 	- [ ] Épisodes antérieurs
> 	- [ ] Fréquence
> 	- [ ] Facteurs améliorants
> 	- [ ] Facteurs aggravants
> 	- [ ] Symptômes associés
> - [ ] **3. Caractérisation de la céphalée associée *(AVC)***
> 	- [ ] Localisation
> 	- [ ] Intensité (sur une échelle de 0-10)
> 	- [ ] Qualité
> 	- [ ] Début
> 	- [ ] Événements précipitants
> 	- [ ] Progression/constante/intermittente
> 	- [ ] Irradiation
> 	- [ ] Facteurs améliorants
> 	- [ ] Facteurs aggravants
> - [ ] **4. Recherche de symptômes spécifiques pour perte de vision récurrente et céphalée *(AVC)***
> 	- [ ] Traumatisme
> 	- [ ] Nausées/vomissements
> 	- [ ] Fièvre/frissons
> 	- [ ] Sueurs nocturnes
> 	- [ ] Fatigue
> 	- [ ] Palpitations
> 	- [ ] Éruption cutanée/changements cutanés
> 	- [ ] Toux
> 	- [ ] Essoufflement
> 	- [ ] Problèmes urinaires
> 	- [ ] Problèmes intestinaux
> 	- [ ] Problèmes de sommeil
> 	- [ ] Appétit
> 	- [ ] Changements de poids
> 	- [ ] Infections récentes
> 	- [ ] Vertiges
> 	- [ ] Chutes
> 	- [ ] Faiblesse
> 	- [ ] Engourdissement
> 	- [ ] Picotements
> 	- [ ] Convulsion
> 	- [ ] Problèmes d'élocution
> - [ ] **5. Antécédents médicaux personnels *(AVC · Cataracte · Décollement de rétine)***
> 	- [ ] Diabète *(Cataracte)*
> 	- [ ] Pathologies systémiques *(Cataracte)*
> 	- [ ] Chirurgies antérieures *(Cataracte)*
> - [ ] **6. Allergies *(4 diagnostics)***
> 	- [ ] Allergies médicamenteuses *(Cataracte)*
> 	- [ ] Autres allergies *(Cataracte)*
> - [ ] **7. Médicaments *(AVC · Décollement de rétine · OACR / Occlusion rétinienne)***
> - [ ] **8. Hospitalisations et antécédents chirurgicaux *(AVC)***
> 	- [ ] Hospitalisations
> 	- [ ] Antécédents chirurgicaux
> - [ ] **9. Contacts malades et antécédents familiaux *(AVC)***
> 	- [ ] Contacts malades
> 	- [ ] Antécédents familiaux
> - [ ] **10. Habitudes et mode de vie *(AVC · Horton (artérite à cellules géantes))***
> 	- [ ] Travail *(AVC)*
> 	- [ ] Domicile *(AVC)*
> 	- [ ] Alcool *(AVC)*
> 	- [ ] Drogues récréatives *(AVC)*
> 	- [ ] Tabagisme
> 	- [ ] Exercice *(AVC)*
> 	- [ ] Alimentation *(AVC)*
> 	- [ ] Drogues *(Horton (artérite à cellules géantes))*
> 	- [ ] Médicaments *(Horton (artérite à cellules géantes))*
> - [ ] **11. Question d’entrée *(OACR / Occlusion rétinienne)***
> - [ ] **12. Dimension temporelle *(Décollement de rétine · OACR / Occlusion rétinienne)***
> - [ ] **13. Début / Durée *(Décollement de rétine · OACR / Occlusion rétinienne)***
> - [ ] **14. Mode de survenue *(OACR / Occlusion rétinienne)***
> - [ ] **15. Évolution *(Décollement de rétine · OACR / Occlusion rétinienne)***
> - [ ] **16. Épisodes antérieurs *(OACR / Occlusion rétinienne)***
> - [ ] **17. Déclencheur *(OACR / Occlusion rétinienne)***
> - [ ] **18. Localisation *(Décollement de rétine · OACR / Occlusion rétinienne)***
> - [ ] **19. Intensité / Sévérité *(OACR / Occlusion rétinienne)***
> - [ ] **20. Qualité *(OACR / Occlusion rétinienne)***
> - [ ] **21. Mesures déjà prises *(OACR / Occlusion rétinienne)***
> - [ ] **22. Symptômes associés *(Décollement de rétine · OACR / Occlusion rétinienne)***
> - [ ] **23. Douleur *(OACR / Occlusion rétinienne)***
> - [ ] **24. Lunettes / Lentilles de contact *(OACR / Occlusion rétinienne)***
> - [ ] **25. Segments antérieurs *(OACR / Occlusion rétinienne)***
> - [ ] **26. Rougeur *(OACR / Occlusion rétinienne)***
> - [ ] **27. Photophobie *(OACR / Occlusion rétinienne)***
> - [ ] **28. Sensation de corps étranger *(OACR / Occlusion rétinienne)***
> - [ ] **29. Décollement de rétine *(OACR / Occlusion rétinienne)***
> - [ ] **30. Éclairs lumineux *(OACR / Occlusion rétinienne)***
> - [ ] **31. Rideau *(OACR / Occlusion rétinienne)***
> - [ ] **32. Pluie de suie *(OACR / Occlusion rétinienne)***
> - [ ] **33. Mouches volantes *(OACR / Occlusion rétinienne)***
> - [ ] **34. Artérite à cellules géantes *(OACR / Occlusion rétinienne)***
> - [ ] **35. Céphalées *(OACR / Occlusion rétinienne)***
> - [ ] **36. Douleurs à la mastication *(OACR / Occlusion rétinienne)***
> - [ ] **37. Douleurs ceintures scapulaire / pelvienne *(OACR / Occlusion rétinienne)***
> - [ ] **38. Symptômes généraux *(OACR / Occlusion rétinienne)***
> - [ ] **39. Neurologique *(OACR / Occlusion rétinienne)***
> - [ ] **40. Trouble du langage *(OACR / Occlusion rétinienne)***
> - [ ] **41. Paralysie *(OACR / Occlusion rétinienne)***
> - [ ] **42. Trouble de la sensibilité *(Décollement de rétine · OACR / Occlusion rétinienne)***
> - [ ] **43. Vertiges *(OACR / Occlusion rétinienne)***
> - [ ] **44. Antécédents *(OACR / Occlusion rétinienne)***
> - [ ] **45. Yeux / Cœur *(OACR / Occlusion rétinienne)***
> - [ ] **46. Antécédents chirurgicaux *(Décollement de rétine · OACR / Occlusion rétinienne)***
> - [ ] **47. Noxes *(OACR / Occlusion rétinienne)***
> - [ ] **48. Alcool *(Décollement de rétine · OACR / Occlusion rétinienne)***
> - [ ] **49. Tabagisme *(Décollement de rétine · OACR / Occlusion rétinienne)***
> - [ ] **50. Drogues *(Décollement de rétine · OACR / Occlusion rétinienne)***
> - [ ] **51. Antécédents familiaux *(Cataracte · Décollement de rétine · OACR / Occlusion rétinienne)***
> 	- [ ] Pathologies oculaires familiales *(Cataracte)*
> 	- [ ] Inquiétude du patient *(Cataracte)*
> 	- [ ] Cataracte familiale *(Cataracte)*
> - [ ] **52. Profession *(Décollement de rétine · OACR / Occlusion rétinienne)***
> - [ ] **53. Situation sociale *(Décollement de rétine · OACR / Occlusion rétinienne)***
> - [ ] **54. Question initiale *(Décollement de rétine)***
> - [ ] **55. Apparition *(Décollement de rétine)***
> - [ ] **56. Facteur déclenchant / Traumatisme *(Décollement de rétine)***
> - [ ] **57. Retentissement des symptômes *(Décollement de rétine)***
> - [ ] **58. Symptômes de décollement de rétine *(Décollement de rétine)***
> - [ ] **59. Corps flottants / Pluie de suie *(Décollement de rétine)***
> - [ ] **60. Déficit du champ visuel *(Décollement de rétine)***
> - [ ] **61. Vision centrale *(Décollement de rétine)***
> - [ ] **62. Douleurs / Signes d'inflammation *(Décollement de rétine)***
> - [ ] **63. Symptômes neurologiques *(Décollement de rétine)***
> - [ ] **64. Trouble de la parole *(Décollement de rétine)***
> - [ ] **65. Déficits moteurs *(Décollement de rétine)***
> - [ ] **66. Maux de tête / Vertiges *(Décollement de rétine)***
> - [ ] **67. Ophtalmologiques *(Décollement de rétine)***
> - [ ] **68. Non ophtalmologiques *(Décollement de rétine)***
> - [ ] **69. Correction visuelle *(Décollement de rétine)***
> - [ ] **70. Toxiques *(Décollement de rétine)***
> - [ ] **71. Facteurs de stress psychosociaux *(Décollement de rétine)***
> - [ ] **72. Présentation avec nom, fonction et tâche *(Cataracte)***
> - [ ] **73. Question d'entrée ouverte *(Cataracte)***
> 	- [ ] Qu'est-ce qui vous amène aujourd'hui ?
> - [ ] **74. Caractérisation de la baisse de vision *(Cataracte)***
> 	- [ ] Apparition
> 	- [ ] Évolution
> 	- [ ] Unilatérale ou bilatérale
> 	- [ ] Prédominance vision de loin ou de près
> - [ ] **75. Symptômes visuels associés *(Cataracte)***
> 	- [ ] Photosensibilité
> 	- [ ] Amélioration paradoxale vision de près
> 	- [ ] Vision des couleurs
> 	- [ ] Halos lumineux
> 	- [ ] Vision double
> 	- [ ] Vision trouble/voilée
> - [ ] **76. Symptômes oculaires associés *(Cataracte)***
> 	- [ ] Douleurs oculaires
> 	- [ ] Rougeur oculaire
> 	- [ ] Larmoiement
> 	- [ ] Sécrétions
> 	- [ ] Sensation de corps étranger
> - [ ] **77. Symptômes généraux et drapeaux rouges *(Cataracte)***
> 	- [ ] Céphalées
> 	- [ ] Claudication de la mâchoire
> 	- [ ] Douleurs temporales
> 	- [ ] Symptômes B (fièvre, sueurs nocturnes, perte de poids)
> - [ ] **78. Facteurs de risque cardiovasculaire *(Cataracte)***
> 	- [ ] Hypertension artérielle
> 	- [ ] Diabète
> 	- [ ] Dyslipidémie
> 	- [ ] Tabagisme
> 	- [ ] Consommation d'alcool
> - [ ] **79. Anamnèse médicamenteuse *(Cataracte)***
> 	- [ ] Corticothérapie systémique
> 	- [ ] Collyre myotique
> 	- [ ] Autres médicaments
> - [ ] **80. Antécédents ophtalmologiques *(Cataracte)***
> 	- [ ] Chirurgie oculaire antérieure
> 	- [ ] Traumatisme oculaire
> 	- [ ] Glaucome
> 	- [ ] Myopie/hypermétropie
> - [ ] **81. Anamnèse sociale et impact fonctionnel *(Cataracte)***
> 	- [ ] Situation de vie
> 	- [ ] Autonomie
> 	- [ ] Activités quotidiennes
> 	- [ ] Conduite automobile
> - [ ] **82. Caractérisation cécité *(Horton (artérite à cellules géantes))***
> 	- [ ] Localisation
> 	- [ ] Chronologie
> 	- [ ] Développement (subit / progressif)
> 	- [ ] Circonstance de survenue
> 	- [ ] Perte de connaissance associée
> - [ ] **83. Caractérisation céphalées *(Horton (artérite à cellules géantes))***
> 	- [ ] Localisation
> 	- [ ] Irradiation
> 	- [ ] Qualité
> 	- [ ] Quantité
> 	- [ ] Chronologie
> 	- [ ] Développement
> - [ ] **84. Anamnèse par système - générale *(Horton (artérite à cellules géantes))***
> 	- [ ] Fièvre
> 	- [ ] Sudation nocturne
> 	- [ ] Perte de poids
> - [ ] **85. Anamnèse par système - neurologique *(Horton (artérite à cellules géantes))***
> 	- [ ] Diplopie
> 	- [ ] Perte de force
> 	- [ ] Perte de sensibilité
> 	- [ ] Paresthésies
> 	- [ ] Vertiges
> - [ ] **86. Antécédents et comorbidités *(Horton (artérite à cellules géantes))***
> 	- [ ] Maladies actuelles
> 	- [ ] Antécédents médico-chirurgicaux
> 	- [ ] Allergies

> [!tip] 🩺 Status
> - [ ] **1. Mesures d'hygiène *(AVC)***
> 	- [ ] Lavage des mains
> 	- [ ] Respect de la pudeur avec drap
> - [ ] **2. Examen de la tête, yeux, oreilles, nez et gorge *(AVC)***
> 	- [ ] Inspection de la tête
> 	- [ ] Palpation de la tête
> 	- [ ] Évaluation de l'acuité visuelle (échelle de Snellen)
> 	- [ ] Fundoscopie directe
> 	- [ ] Examen du champ visuel
> - [ ] **3. Examen du cou *(AVC)***
> 	- [ ] Auscultation des artères carotides
> - [ ] **4. Examen cardiovasculaire *(AVC)***
> 	- [ ] Palpation du pouls radial
> 	- [ ] Auscultation du cœur
> - [ ] **5. Examen thoracique *(AVC)***
> 	- [ ] Auscultation des poumons
> - [ ] **6. Examen neurologique *(AVC)***
> 	- [ ] Évaluation du niveau de conscience
> 	- [ ] Examen de l'orientation dans le temps, l'espace et les personnes
> 	- [ ] Évaluation du langage
> 	- [ ] Examen ciblé des nerfs crâniens
> 	- [ ] Signe de Kernig
> 	- [ ] Signe de Brudzinski
> 	- [ ] Méningisme
> 	- [ ] Examen ciblé des mouvements passifs et actifs
> 	- [ ] Examen ciblé de la sensibilité
> 	- [ ] Examen ciblé des réflexes ostéotendineux
> 	- [ ] Examen ciblé de la marche
> 	- [ ] Test d'alternance rapide des mouvements
> 	- [ ] Test doigt-nez
> 	- [ ] Signe de Babinski
> 	- [ ] Test de Romberg
> - [ ] **7. Status neuro orientant *(OACR / Occlusion rétinienne)***
> - [ ] **8. Acuité visuelle *(Cataracte · OACR / Occlusion rétinienne)***
> 	- [ ] Vision de loin avec correction *(Cataracte)*
> 	- [ ] Vision de près avec correction *(Cataracte)*
> 	- [ ] Test du trou sténopéique *(Cataracte)*
> - [ ] **9. Réflexe pupillaire *(OACR / Occlusion rétinienne)***
> - [ ] **10. Champ visuel *(Décollement de rétine · OACR / Occlusion rétinienne)***
> - [ ] **11. Motilité oculaire *(OACR / Occlusion rétinienne)***
> - [ ] **12. Segments antérieurs *(OACR / Occlusion rétinienne)***
> - [ ] **13. Pression intraoculaire *(Décollement de rétine · OACR / Occlusion rétinienne)***
> - [ ] **14. Fundoscopie *(OACR / Occlusion rétinienne)***
> - [ ] **15. Artères temporales *(OACR / Occlusion rétinienne)***
> - [ ] **16. Auscultation cardiaque *(OACR / Occlusion rétinienne)***
> - [ ] **17. Auscultation des carotides *(OACR / Occlusion rétinienne)***
> - [ ] **18. Examen de l'acuité visuelle *(Décollement de rétine)***
> - [ ] **19. Acuité visuelle de loin à droite *(Décollement de rétine)***
> - [ ] **20. Acuité visuelle de loin à gauche *(Décollement de rétine)***
> - [ ] **21. Correction lors de l'examen de l'acuité visuelle *(Décollement de rétine)***
> - [ ] **22. Central *(Décollement de rétine)***
> - [ ] **23. Moyennement périphérique *(Décollement de rétine)***
> - [ ] **24. Périphérique *(Décollement de rétine)***
> - [ ] **25. Examen monoculaire *(Décollement de rétine)***
> - [ ] **26. Examen par quadrants *(Décollement de rétine)***
> - [ ] **27. Évaluation de la pupille *(Décollement de rétine)***
> - [ ] **28. Réaction pupillaire à la lumière *(Décollement de rétine)***
> - [ ] **29. Test de l'éclairement alterné (Swinging-flashlight test) *(Décollement de rétine)***
> - [ ] **30. Motilité *(Décollement de rétine)***
> - [ ] **31. Segments externes de l'œil *(Décollement de rétine)***
> - [ ] **32. Segments antérieurs de l'œil *(Décollement de rétine)***
> - [ ] **33. Vitré antérieur *(Décollement de rétine)***
> - [ ] **34. Fond d'œil droit *(Décollement de rétine)***
> - [ ] **35. Fond d'œil gauche *(Décollement de rétine)***
> - [ ] **36. Examen des annexes et segment antérieur *(Cataracte)***
> 	- [ ] Paupières
> 	- [ ] Conjonctive
> 	- [ ] Cornée
> 	- [ ] Chambre antérieure
> - [ ] **37. Examen à la lampe à fente *(Cataracte)***
> 	- [ ] Cristallin
> 	- [ ] Type d'opacité
> 	- [ ] Densité
> - [ ] **38. Test du reflet rouge rétinien *(Cataracte)***
> 	- [ ] Reflet rouge
> 	- [ ] Symétrie
> - [ ] **39. Pupilles et réflexes pupillaires *(Cataracte)***
> 	- [ ] Taille et symétrie
> 	- [ ] Réflexe photomoteur direct
> 	- [ ] Réflexe consensuel
> 	- [ ] Défaut pupillaire afférent relatif
> - [ ] **40. Tonus oculaire *(Cataracte)***
> 	- [ ] Palpation bidigitale
> 	- [ ] Mesure si disponible
> - [ ] **41. Fond d'œil *(Cataracte)***
> 	- [ ] Visualisation
> 	- [ ] Ce qui est visible
> 	- [ ] Exclusion de pathologie rétinienne évidente
> - [ ] **42. Examen neurologique de base *(Cataracte)***
> 	- [ ] Champs visuels par confrontation
> 	- [ ] Oculomotricité
> 	- [ ] Nerfs crâniens
> - [ ] **43. Ophtalmologique - observation *(Horton (artérite à cellules géantes))***
> 	- [ ] Sclère
> 	- [ ] Paupière
> - [ ] **44. Ophtalmologique - acuité visuelle *(Horton (artérite à cellules géantes))***
> 	- [ ] Œil droit
> 	- [ ] Œil gauche
> - [ ] **45. Ophtalmologique - fond d'œil *(Horton (artérite à cellules géantes))***
> - [ ] **46. Neuro-ophtalmologique *(Horton (artérite à cellules géantes))***
> 	- [ ] Champs visuels
> 	- [ ] Poursuite oculaire / oculomotricité
> - [ ] **47. Neuro-ophtalmologique - réflexes pupillaires *(Horton (artérite à cellules géantes))***
> 	- [ ] Direct
> 	- [ ] Croisé
> - [ ] **48. Neurologique - orientation aux 4 modes *(Horton (artérite à cellules géantes))***
> 	- [ ] Temps
> 	- [ ] Localisation
> 	- [ ] Personne
> 	- [ ] Situation
> - [ ] **49. Neurologique - motricité & sensibilité grossière *(Horton (artérite à cellules géantes))***
> 	- [ ] Motricité
> 	- [ ] Sensibilité
> - [ ] **50. DD AVC - Test de Cincinnati (Stroke Scale) *(Horton (artérite à cellules géantes))***
> 	- [ ] Motricité de la face (NC VII)
> 	- [ ] Épreuve des bras tendus
> 	- [ ] Répétition d'une phrase
> - [ ] **51. DD artérite de Horton *(Horton (artérite à cellules géantes))***
> 	- [ ] Percussion de l'artère temporale
> 	- [ ] Palpation de la mâchoire
> - [ ] **52. Cardiaque *(Horton (artérite à cellules géantes))***
> 	- [ ] Auscultation des 4 foyers
> 	- [ ] Auscultation des carotides des deux côtés

> [!success] 💊 Management — partagé par plusieurs diagnostics
> - [ ] **1. Diagnostic de travail *(2 grilles sur 5)* — *Décollement de rétine · OACR / Occlusion rétinienne***

> [!success] 💊 Management — si AVC
> - [ ] **1. Hypothèses diagnostiques**
> - [ ] **2. Examens complémentaires urgents**
> 	- [ ] Oxymétrie de pouls
> 	- [ ] ECG et monitoring cardiaque
> 	- [ ] FSC
> 	- [ ] TP, TCA
> 	- [ ] Électrolytes, glucose sérique
> 	- [ ] Troponine
> - [ ] **3. Imagerie cérébrale**
> 	- [ ] CT cérébral sans contraste
> 	- [ ] IRM cérébrale
> - [ ] **4. Communication avec le patient**
> 	- [ ] Explications au patient des impressions diagnostiques préliminaires
> 	- [ ] Explication du plan de prise en charge
> 	- [ ] Utilisation d'un langage non médical et clarification des termes médicaux
> 	- [ ] Évaluation de l'accord du patient avec le plan diagnostique
> 	- [ ] Recherche des préoccupations et questions du patient
> - [ ] **5. Conseil et soutien**
> 	- [ ] Réaction appropriée au défi concernant la peur de mourir

> [!success] 💊 Management — si Cataracte
> - [ ] **1. Diagnostic principal**
> 	- [ ] Cataracte sénile bilatérale
> 	- [ ] Type nucléaire prédominant
> - [ ] **2. Diagnostics différentiels**
> - [ ] **3. Examens complémentaires**
> 	- [ ] Biométrie oculaire (si chirurgie envisagée)
> 	- [ ] Échographie oculaire mode B (si fond d'œil non visible)
> 	- [ ] OCT maculaire (pour exclure pathologie maculaire associée)
> 	- [ ] Glycémie (dépistage diabète)
> 	- [ ] Bilan préopératoire si chirurgie planifiée
> - [ ] **4. Traitement**
> - [ ] **5. Information du patient**
> 	- [ ] Explication de la nature de la cataracte
> 	- [ ] Rassurer : pas la même pathologie que son père (DMLA)
> 	- [ ] Excellent pronostic avec la chirurgie (>95% de succès)
> 	- [ ] Risques chirurgicaux faibles mais existants
> 	- [ ] Récupération visuelle habituelle en quelques semaines
> - [ ] **6. Suivi et orientation**
> 	- [ ] Référence en ophtalmologie pour évaluation chirurgicale
> 	- [ ] Suivi régulier en attendant la chirurgie
> 	- [ ] Surveillance de la progression
> 	- [ ] Contrôle postopératoire après chirurgie

> [!success] 💊 Management — si Décollement de rétine
> - [ ] **1. OCT**
> - [ ] **2. Échographie oculaire**
> - [ ] **3. Information sur le diagnostic de travail**
> - [ ] **4. Contacter la chirurgie vitréo-rétinienne**
> - [ ] **5. Examens diagnostiques complémentaires**
> - [ ] **6. Consignes préopératoires**

> [!success] 💊 Management — si DMLA
> *Aucune grille du corpus ne documente ce diagnostic* — il est pourtant attendu de cette SSP. **Trou de révision à combler ailleurs.**

> [!success] 💊 Management — si Horton (artérite à cellules géantes)
> - [ ] **1. Demande de laboratoire**
> 	- [ ] Formule sanguine simple (FSS)
> 	- [ ] Vitesse de sédimentation (VS)
> 	- [ ] CRP
> - [ ] **2. Demande de biopsie de l'artère temporale**
> - [ ] **3. Évoque la nécessité d'exclure une dissection aortique en proposant**
> 	- [ ] Imagerie
> 	- [ ] Prise de tension aux 2 bras
> - [ ] **4. Évoque le diagnostic d'artérite de Horton / maladie de Horton / artérite temporale**
> - [ ] **5. Propose l'introduction immédiate d'une corticothérapie**
> - [ ] **6. Propose en parallèle l'introduction de**
> 	- [ ] Calcium / vitamine D
> 	- [ ] Protection gastrique
> - [ ] **7. Propose une hospitalisation**

> [!success] 💊 Management — si OACR / Occlusion rétinienne
> - [ ] **1. Imagerie cérébrale**
> - [ ] **2. Laboratoire**
> - [ ] **3. Hémogramme**
> - [ ] **4. Paramètres inflammatoires**
> - [ ] **5. ECG**
> - [ ] **6. Pas de thérapie fondée sur des preuves**
> - [ ] **7. Adressage Stroke Center**
> - [ ] **8. Investigations complémentaires**
> - [ ] **9. Échocardiographie**
> - [ ] **10. Doppler des carotides**
> - [ ] **11. ECG de longue durée**
> - [ ] **12. Prévention secondaire**
> - [ ] **13. Anticoagulation orale**
> - [ ] **14. Statine**
> - [ ] **15. Contrôle de la tension artérielle**
> - [ ] **16. Arrêt du tabac**
