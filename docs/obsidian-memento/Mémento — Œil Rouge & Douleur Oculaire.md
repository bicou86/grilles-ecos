---
aliases:
  - "Mémento Œil Rouge & Douleur Oculaire"
type: memento-ecos-ssp
ssp: "Œil Rouge & Douleur Oculaire"
cas: 4
diagnostics: 4
attendus_sans_grille: 2
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

# Œil Rouge & Douleur Oculaire

*4 grilles · 4 diagnostics documentés · 2 attendus sans grille* — [[SSP — Œil Rouge & Douleur Oculaire]]

> [!abstract] Les 4 grilles fusionnées
> - **AZYGOS-10** — Glaucome aigu `diagnostic-travail` · [grille](<file:///Users/damienfulliquet/Developer/GitHub/grilles-ecos/.azygos-extraction/8d674409-0b72-4e3f-bcd2-4507b3d27a1e.json>)
> - **AZYGOS-45** — Sécheresse oculaire évaporative (dysfonction des glandes de Meibom) `diagnostic-travail` · [grille](<file:///Users/damienfulliquet/Developer/GitHub/grilles-ecos/.azygos-extraction/7aa130b4-975d-44fa-9dbb-6a83e36aa6d0.json>)
> - **German-88** — Conjonctivite allergique `corrige` · [grille](<file:///Users/damienfulliquet/Developer/GitHub/grilles-ecos/cases/german/German-88_-_Yeux_rouges_-_Grille_ECOS.html>)
> - **RESCOS-32** — Kératite herpétique `confirme` · [grille](<file:///Users/damienfulliquet/Developer/GitHub/grilles-ecos/cases/rescos/RESCOS-32_-_Douleur_oculaire_-_Grille_ECOS.html>)

> [!note] 📋 Anamnèse
> - [ ] **1. Question d’entrée *(Glaucome aigu · Sécheresse oculaire évaporative (dysfonction des glandes de Meibom))***
> - [ ] **2. Dimension temporelle *(Glaucome aigu · Sécheresse oculaire évaporative (dysfonction des glandes de Meibom))***
> - [ ] **3. Début / durée *(Glaucome aigu · Sécheresse oculaire évaporative (dysfonction des glandes de Meibom))***
> - [ ] **4. Mode d’apparition *(Glaucome aigu)***
> - [ ] **5. Évolution *(Glaucome aigu · Sécheresse oculaire évaporative (dysfonction des glandes de Meibom))***
> - [ ] **6. Déclencheurs *(Glaucome aigu)***
> - [ ] **7. Traumatisme oculaire *(Glaucome aigu)***
> - [ ] **8. Localisation *(Glaucome aigu)***
> - [ ] **9. Irradiation *(Glaucome aigu)***
> - [ ] **10. Qualité *(Glaucome aigu)***
> - [ ] **11. Intensité *(Glaucome aigu)***
> - [ ] **12. Facteurs aggravants *(Glaucome aigu · Sécheresse oculaire évaporative (dysfonction des glandes de Meibom))***
> - [ ] **13. Facteurs soulageants *(Glaucome aigu · Sécheresse oculaire évaporative (dysfonction des glandes de Meibom))***
> - [ ] **14. Symptômes associés *(Glaucome aigu)***
> - [ ] **15. Acuité visuelle *(Glaucome aigu)***
> - [ ] **16. Baisse du visus unilatérale *(Glaucome aigu)***
> - [ ] **17. Caractère de la baisse de vision *(Glaucome aigu)***
> - [ ] **18. Halos / couronnes lumineuses *(Glaucome aigu)***
> - [ ] **19. Céphalée *(Glaucome aigu)***
> - [ ] **20. Nausées / vomissements *(Glaucome aigu)***
> - [ ] **21. Segment antérieur de l’œil *(Glaucome aigu)***
> - [ ] **22. Rougeur *(Glaucome aigu)***
> - [ ] **23. Photophobie *(Glaucome aigu)***
> - [ ] **24. Sécrétions / larmoiement *(Conjonctivite allergique · Glaucome aigu)***
> 	- [ ] Larmoiement *(Conjonctivite allergique)*
> 	- [ ] Type de sécrétions (claires, purulentes) *(Conjonctivite allergique)*
> 	- [ ] Paupières collées le matin *(Conjonctivite allergique)*
> 	- [ ] Croûtes sur les cils *(Conjonctivite allergique)*
> - [ ] **25. Sensation de corps étranger *(Glaucome aigu)***
> - [ ] **26. Prurit *(Glaucome aigu · Sécheresse oculaire évaporative (dysfonction des glandes de Meibom))***
> - [ ] **27. Segment postérieur de l’œil *(Glaucome aigu)***
> - [ ] **28. Mouches volantes / éclairs lumineux *(Glaucome aigu)***
> - [ ] **29. Scotomes / déficits du champ visuel *(Glaucome aigu)***
> - [ ] **30. Métamorphopsies *(Glaucome aigu)***
> - [ ] **31. Neuro-ophtalmologie / orbite *(Glaucome aigu)***
> - [ ] **32. Diplopie *(Glaucome aigu)***
> - [ ] **33. Dyschromatopsie *(Glaucome aigu)***
> - [ ] **34. DD-céphalée *(Glaucome aigu)***
> - [ ] **35. Céphalée « coup de tonnerre » *(Glaucome aigu)***
> - [ ] **36. Migraine / algie vasculaire de la face *(Glaucome aigu)***
> - [ ] **37. Déficits neurologiques focaux *(Glaucome aigu)***
> - [ ] **38. Artérite à cellules géantes *(Glaucome aigu)***
> - [ ] **39. A. temporalis *(Glaucome aigu)***
> - [ ] **40. Douleurs à la mastication *(Glaucome aigu)***
> - [ ] **41. Amaurosis fugax *(Glaucome aigu)***
> - [ ] **42. Symptômes B *(Glaucome aigu)***
> - [ ] **43. Antécédents *(Glaucome aigu · Sécheresse oculaire évaporative (dysfonction des glandes de Meibom))***
> - [ ] **44. Antécédents généraux *(Glaucome aigu)***
> - [ ] **45. Antécédents ophtalmologiques *(Glaucome aigu)***
> - [ ] **46. Antécédents chirurgicaux oculaires *(Glaucome aigu)***
> - [ ] **47. Aides visuelles *(Glaucome aigu)***
> - [ ] **48. Médicaments *(Glaucome aigu · Sécheresse oculaire évaporative (dysfonction des glandes de Meibom))***
> - [ ] **49. Médicaments généraux *(Glaucome aigu)***
> - [ ] **50. Médicaments à risque de glaucome *(Glaucome aigu)***
> - [ ] **51. Collyres *(Glaucome aigu)***
> - [ ] **52. Allergies *(Glaucome aigu · Sécheresse oculaire évaporative (dysfonction des glandes de Meibom))***
> - [ ] **53. Noxes *(Glaucome aigu · Sécheresse oculaire évaporative (dysfonction des glandes de Meibom))***
> - [ ] **54. Alcool *(Glaucome aigu · Sécheresse oculaire évaporative (dysfonction des glandes de Meibom))***
> - [ ] **55. Tabagisme *(Glaucome aigu · Sécheresse oculaire évaporative (dysfonction des glandes de Meibom))***
> - [ ] **56. Anamnèse familiale de glaucome *(Glaucome aigu)***
> - [ ] **57. Profession *(Glaucome aigu)***
> - [ ] **58. Situation sociale *(Glaucome aigu · Sécheresse oculaire évaporative (dysfonction des glandes de Meibom))***
> - [ ] **59. Dynamique journalière *(Sécheresse oculaire évaporative (dysfonction des glandes de Meibom))***
> - [ ] **60. Localisation / latéralisation *(Sécheresse oculaire évaporative (dysfonction des glandes de Meibom))***
> - [ ] **61. Mesures prises jusqu’ici *(Sécheresse oculaire évaporative (dysfonction des glandes de Meibom))***
> - [ ] **62. Plaintes des bords palpébraux *(Sécheresse oculaire évaporative (dysfonction des glandes de Meibom))***
> - [ ] **63. Lentilles de contact *(Sécheresse oculaire évaporative (dysfonction des glandes de Meibom))***
> - [ ] **64. Larmoiement associé *(Sécheresse oculaire évaporative (dysfonction des glandes de Meibom))***
> - [ ] **65. Baisse d’acuité visuelle *(Sécheresse oculaire évaporative (dysfonction des glandes de Meibom))***
> - [ ] **66. Fortes douleurs / photophobie *(Sécheresse oculaire évaporative (dysfonction des glandes de Meibom))***
> - [ ] **67. Sécrétions / paupières collées *(Sécheresse oculaire évaporative (dysfonction des glandes de Meibom))***
> - [ ] **68. Traumatisme / corps étranger *(Sécheresse oculaire évaporative (dysfonction des glandes de Meibom))***
> - [ ] **69. Herpès *(Sécheresse oculaire évaporative (dysfonction des glandes de Meibom))***
> - [ ] **70. Bilan du Sjögren *(Sécheresse oculaire évaporative (dysfonction des glandes de Meibom))***
> - [ ] **71. Xérostomie *(Sécheresse oculaire évaporative (dysfonction des glandes de Meibom))***
> - [ ] **72. Douleurs articulaires *(Sécheresse oculaire évaporative (dysfonction des glandes de Meibom))***
> - [ ] **73. Autres signes de sicca *(Sécheresse oculaire évaporative (dysfonction des glandes de Meibom))***
> - [ ] **74. Opérations antérieures *(Sécheresse oculaire évaporative (dysfonction des glandes de Meibom))***
> - [ ] **75. Drogues *(Sécheresse oculaire évaporative (dysfonction des glandes de Meibom))***
> - [ ] **76. Antécédents familiaux *(Sécheresse oculaire évaporative (dysfonction des glandes de Meibom))***
> - [ ] **77. Profession et environnement de travail *(Sécheresse oculaire évaporative (dysfonction des glandes de Meibom))***
> - [ ] **78. Présentation avec nom, fonction et objectif de la consultation *(Conjonctivite allergique)***
> - [ ] **79. Caractérisation du symptôme principal *(Conjonctivite allergique)***
> 	- [ ] Yeux rouges bilatéraux
> 	- [ ] Démangeaisons importantes
> 	- [ ] Latéralité et symétrie
> - [ ] **80. Symptômes oculaires associés *(Conjonctivite allergique)***
> 	- [ ] Sensation de corps étranger
> 	- [ ] Douleurs oculaires
> 	- [ ] Baisse d'acuité visuelle
> 	- [ ] Photophobie
> 	- [ ] Vision floue
> 	- [ ] Halos lumineux
> - [ ] **81. Chronologie et évolution *(Conjonctivite allergique)***
> 	- [ ] Début des symptômes
> 	- [ ] Mode d'installation (brutal/progressif)
> 	- [ ] Évolution
> 	- [ ] Variations journalières
> 	- [ ] Facteurs déclenchants ou améliorants
> - [ ] **82. Symptômes ORL et respiratoires associés *(Conjonctivite allergique)***
> 	- [ ] Rhinorrhée
> 	- [ ] Éternuements fréquents
> 	- [ ] Obstruction nasale
> 	- [ ] Prurit nasal
> 	- [ ] Symptômes de sinusite
> - [ ] **83. Contexte environnemental et saisonnier *(Conjonctivite allergique)***
> 	- [ ] Période de l'année (printemps/été)
> 	- [ ] Exposition à des allergènes
> 	- [ ] Animaux domestiques
> 	- [ ] Changements récents d'environnement
> 	- [ ] Exposition professionnelle/scolaire
> - [ ] **84. Port et entretien des lentilles de contact *(Conjonctivite allergique)***
> 	- [ ] Port de lentilles
> 	- [ ] Type de lentilles (souples/rigides)
> 	- [ ] Port aujourd'hui
> 	- [ ] Durée de port quotidien
> 	- [ ] Hygiène et entretien
> 	- [ ] Changements récents de produits
> - [ ] **85. Anamnèse familiale d'allergie *(Conjonctivite allergique)***
> 	- [ ] Allergies dans la famille
> 	- [ ] Asthme familial
> 	- [ ] Eczéma/dermatite atopique
> 	- [ ] Rhinite allergique familiale
> - [ ] **86. Antécédents personnels d'atopie *(Conjonctivite allergique)***
> 	- [ ] Asthme personnel
> 	- [ ] Eczéma/dermatite atopique
> 	- [ ] Rhinite allergique
> 	- [ ] Allergies alimentaires
> 	- [ ] Allergies aux animaux
> 	- [ ] Autres allergies
> - [ ] **87. Correction optique et réfraction *(Conjonctivite allergique)***
> 	- [ ] Port de lunettes/lentilles
> 	- [ ] Degré de myopie
> 	- [ ] Dernière consultation ophtalmologique
> - [ ] **88. Médicaments et traitements *(Conjonctivite allergique)***
> 	- [ ] Bronchodilatateurs
> 	- [ ] Corticoïdes inhalés
> 	- [ ] Antihistaminiques
> 	- [ ] Collyres utilisés
> 	- [ ] Automédication
> - [ ] **89. Habitudes et toxiques *(Conjonctivite allergique)***
> 	- [ ] Tabagisme
> 	- [ ] Consommation d'alcool
> 	- [ ] Cannabis
> 	- [ ] Autres substances
> - [ ] **90. Contexte social et activités *(Conjonctivite allergique)***
> 	- [ ] Scolarité
> 	- [ ] Intégration sociale
> 	- [ ] Sports et loisirs
> 	- [ ] Stress/examens
> - [ ] **91. Anamnèse sexuelle et IST *(Conjonctivite allergique)***
> 	- [ ] Activité sexuelle récente
> 	- [ ] Protection utilisée
> 	- [ ] Symptômes urogénitaux
> 	- [ ] Antécédents d'IST
> - [ ] **92. Symptômes généraux *(Conjonctivite allergique)***
> 	- [ ] État général
> 	- [ ] Fièvre
> 	- [ ] Asthénie
> 	- [ ] Arthralgies
> - [ ] **93. Caractéristiques de la douleur : Début / Durée / Fréquence *(Kératite herpétique)***
> - [ ] **94. Caractéristiques de la douleur : Évolution / Qualité / Intensité / Localisation / Irradiation *(Kératite herpétique)***
> - [ ] **95. Douleur : Facteurs aggravants / Facteurs atténuants *(Kératite herpétique)***
> - [ ] **96. Symptômes associés : Vision floue / Photophobie *(Kératite herpétique)***
> - [ ] **97. Caractéristiques troubles de la vision *(Kératite herpétique)***
> 	- [ ] Mono-binoculaire
> 	- [ ] Diplopie
> 	- [ ] Myodésopsies (mouches volantes)
> - [ ] **98. Altération du champ visuel *(Kératite herpétique)***
> - [ ] **99. Antécédent similaire par le passé *(Kératite herpétique)***
> - [ ] **100. Notion de *(Kératite herpétique)***
> 	- [ ] Contage dans l'entourage
> 	- [ ] Port de lentilles
> 	- [ ] Traumatisme
> 	- [ ] Exposition agent irritant/UV
> - [ ] **101. Histoire médicale *(Kératite herpétique)***
> 	- [ ] ATCD médico-chirurgicaux
> 	- [ ] Allergies
> - [ ] **102. Traitement en cours *(Kératite herpétique)***

> [!tip] 🩺 Status
> - [ ] **1. Évaluation du visus *(Glaucome aigu)***
> - [ ] **2. Visus droit *(Glaucome aigu)***
> - [ ] **3. Visus gauche *(Glaucome aigu)***
> - [ ] **4. Aide visuelle utilisée *(Glaucome aigu)***
> - [ ] **5. Inspection *(Glaucome aigu · Sécheresse oculaire évaporative (dysfonction des glandes de Meibom))***
> - [ ] **6. Évaluation des pupilles *(Glaucome aigu)***
> - [ ] **7. Réaction directe à la lumière *(Glaucome aigu)***
> - [ ] **8. Réaction consensuelle à la lumière *(Glaucome aigu)***
> - [ ] **9. Test au faisceau lumineux oscillant *(Glaucome aigu)***
> - [ ] **10. Réaction de convergence *(Glaucome aigu)***
> - [ ] **11. Motilité oculaire *(Glaucome aigu)***
> - [ ] **12. Champ visuel par confrontation *(Glaucome aigu)***
> - [ ] **13. Central *(Glaucome aigu)***
> - [ ] **14. Médio-périphérique *(Glaucome aigu)***
> - [ ] **15. Périphérique *(Glaucome aigu)***
> - [ ] **16. Examen monoculaire *(Glaucome aigu)***
> - [ ] **17. Test des quadrants *(Glaucome aigu)***
> - [ ] **18. Palpation du globe *(Glaucome aigu)***
> - [ ] **19. Ophthalmoscope manuel *(Glaucome aigu)***
> - [ ] **20. Réflexe du fond (lumière rétrodiffusée) *(Glaucome aigu)***
> - [ ] **21. Lumière incidente (éclairage direct) *(Glaucome aigu)***
> - [ ] **22. Cornée (fente focalisée) *(Glaucome aigu)***
> - [ ] **23. Profondeur de la chambre antérieure (fente focalisée) *(Glaucome aigu)***
> - [ ] **24. Fond d’œil *(Glaucome aigu)***
> - [ ] **25. Méningisme *(Glaucome aigu)***
> - [ ] **26. Examen neurologique orientant *(Glaucome aigu)***
> - [ ] **27. Acuité visuelle *(Sécheresse oculaire évaporative (dysfonction des glandes de Meibom))***
> - [ ] **28. Fermeture palpébrale *(Sécheresse oculaire évaporative (dysfonction des glandes de Meibom))***
> - [ ] **29. Œil externe *(Sécheresse oculaire évaporative (dysfonction des glandes de Meibom))***
> - [ ] **30. Pression oculaire *(Sécheresse oculaire évaporative (dysfonction des glandes de Meibom))***
> - [ ] **31. Glandes de Meibom *(Sécheresse oculaire évaporative (dysfonction des glandes de Meibom))***
> - [ ] **32. Expression *(Sécheresse oculaire évaporative (dysfonction des glandes de Meibom))***
> - [ ] **33. Ménisque lacrymal *(Sécheresse oculaire évaporative (dysfonction des glandes de Meibom))***
> - [ ] **34. Conjonctive *(Sécheresse oculaire évaporative (dysfonction des glandes de Meibom))***
> - [ ] **35. Pupilles et chambre antérieure *(Sécheresse oculaire évaporative (dysfonction des glandes de Meibom))***
> - [ ] **36. Temps de rupture du film lacrymal *(Sécheresse oculaire évaporative (dysfonction des glandes de Meibom))***
> - [ ] **37. Coloration de la cornée *(Sécheresse oculaire évaporative (dysfonction des glandes de Meibom))***
> - [ ] **38. Inspection générale des yeux et annexes *(Conjonctivite allergique)***
> 	- [ ] Hyperhémie conjonctivale bilatérale
> 	- [ ] Type d'injection (diffuse, localisée, péricornéenne)
> 	- [ ] Chémosis
> 	- [ ] Aspect des paupières
> 	- [ ] Position des cils
> 	- [ ] Sourcil latéral manquant
> - [ ] **39. Examen des paupières *(Conjonctivite allergique)***
> 	- [ ] Œdème palpébral
> 	- [ ] Érythème
> 	- [ ] Croûtes, squames
> 	- [ ] Éversion des paupières (recherche corps étranger)
> 	- [ ] Papilles tarsales
> 	- [ ] Follicules
> - [ ] **40. Examen des sécrétions *(Conjonctivite allergique)***
> 	- [ ] Nature des sécrétions (muqueuses, purulentes, aqueuses)
> 	- [ ] Quantité
> 	- [ ] Localisation (angle interne/externe)
> - [ ] **41. Examen pupillaire *(Conjonctivite allergique)***
> 	- [ ] Taille et symétrie des pupilles
> 	- [ ] Réflexe photomoteur direct
> 	- [ ] Réflexe consensuel
> 	- [ ] Déficit pupillaire afférent relatif
> - [ ] **42. Mesure de l'acuité visuelle *(Conjonctivite allergique)***
> 	- [ ] Sans correction
> 	- [ ] Avec correction
> 	- [ ] Vision de près
> 	- [ ] Champ visuel par confrontation
> - [ ] **43. Examen à la lampe à fente *(Conjonctivite allergique)***
> 	- [ ] Examen des paupières et cils
> 	- [ ] Film lacrymal
> 	- [ ] Conjonctive bulbaire et tarsale
> 	- [ ] Cornée (transparence, épithélium)
> 	- [ ] Chambre antérieure (profondeur, Tyndall)
> 	- [ ] Iris et cristallin
> - [ ] **44. Test à la fluorescéine *(Conjonctivite allergique)***
> 	- [ ] Recherche d'érosion cornéenne
> 	- [ ] Recherche d'ulcère
> 	- [ ] Temps de rupture du film lacrymal
> 	- [ ] Pattern de coloration
> - [ ] **45. Pression intraoculaire *(Conjonctivite allergique)***
> 	- [ ] Palpation comparative
> 	- [ ] Mesure si disponible
> 	- [ ] Signes de glaucome aigu
> - [ ] **46. Examen ORL complémentaire *(Conjonctivite allergique)***
> 	- [ ] Rhinoscopie antérieure
> 	- [ ] Muqueuse nasale (pâle, œdématiée)
> 	- [ ] Cornets
> 	- [ ] Sécrétions
> - [ ] **47. Auscultation pulmonaire *(Conjonctivite allergique)***
> 	- [ ] Auscultation systématique antérieure
> 	- [ ] Auscultation systématique postérieure
> 	- [ ] Recherche de sibilants
> 	- [ ] Recherche de signes d'exacerbation asthmatique
> - [ ] **48. Examen cutané *(Conjonctivite allergique)***
> 	- [ ] Recherche de lésions eczémateuses
> 	- [ ] Dermographisme
> 	- [ ] Signes de dermatite atopique
> - [ ] **49. Observation des yeux *(Kératite herpétique)***
> 	- [ ] Sous paupière supérieure
> 	- [ ] Sous paupière inférieure
> - [ ] **50. Palpation oculaire *(Kératite herpétique)***
> - [ ] **51. Champ visuel *(Kératite herpétique)***
> 	- [ ] Les 4 quadrants
> 	- [ ] La périphérie
> - [ ] **52. Oculomotricité *(Kératite herpétique)***
> 	- [ ] Convergence
> 	- [ ] 6 directions
> - [ ] **53. Réflexe pupillaire *(Kératite herpétique)***
> 	- [ ] Direct
> 	- [ ] Consensuel
> 	- [ ] À la convergence
> - [ ] **54. Nerfs crâniens *(Kératite herpétique)***
> 	- [ ] Sensibilité de la face (V)
> 	- [ ] Mobilité de la face (VII)
> - [ ] **55. Acuité visuelle de loin OU de près *(Kératite herpétique)***
> - [ ] **56. Propose une ophtalmoscopie directe *(Kératite herpétique)***
> - [ ] **57. Propose un examen à la lampe à fente *(Kératite herpétique)***

> [!success] 💊 Management — partagé par plusieurs diagnostics
> - [ ] **1. Diagnostic de travail *(Glaucome aigu · Sécheresse oculaire évaporative (dysfonction des glandes de Meibom) — 2 grilles sur 4)***

> [!success] 💊 Management — si Conjonctivite allergique
> - [ ] **1. Diagnostic principal évoqué**
> 	- [ ] Conjonctivite allergique saisonnière
> 	- [ ] Arguments en faveur du diagnostic
> 	- [ ] Corrélation avec le terrain atopique
> - [ ] **2. Diagnostics différentiels pertinents**
> - [ ] **3. Examens complémentaires proposés**
> 	- [ ] Prélèvement conjonctival pour bactériologie
> 	- [ ] Recherche de Chlamydia si indiqué
> 	- [ ] Tests allergologiques cutanés (prick tests)
> 	- [ ] IgE spécifiques si nécessaire
> 	- [ ] Frottis conjonctival (éosinophiles)
> - [ ] **4. Traitement antiallergique local**
> 	- [ ] Antihistaminiques topiques (lévocabastine, azélastine)
> 	- [ ] Stabilisateurs de mastocytes (cromoglycate, nédocromil)
> 	- [ ] Associations antihistaminique/stabilisateur
> 	- [ ] Collyres corticoïdes en cure courte si sévère
> 	- [ ] Larmes artificielles
> 	- [ ] Compresses froides
> - [ ] **5. Traitement systémique**
> 	- [ ] Antihistaminiques oraux (cétirizine, loratadine)
> 	- [ ] Optimisation du traitement de l'asthme
> 	- [ ] Corticoïdes nasaux si rhinite associée
> - [ ] **6. Mesures préventives et conseils**
> 	- [ ] Éviction des allergènes identifiés
> 	- [ ] Port de lunettes de soleil
> 	- [ ] Lavage des cheveux le soir
> 	- [ ] Fenêtres fermées en période pollinique
> 	- [ ] Arrêt temporaire des lentilles
> 	- [ ] Hygiène palpébrale
> 	- [ ] Sevrage tabagique conseillé
> - [ ] **7. Éducation sur les IST**
> 	- [ ] Information sur les risques
> 	- [ ] Importance de la protection
> 	- [ ] Proposition de dépistage IST
> 	- [ ] Conseils de prévention
> - [ ] **8. Planification du suivi**
> 	- [ ] Réévaluation si persistance des symptômes
> 	- [ ] Consultation ophtalmologique si aggravation
> 	- [ ] Suivi allergologique
> 	- [ ] Contrôle de l'observance
> - [ ] **9. Critères de référence spécialisée**
> 	- [ ] Baisse d'acuité visuelle
> 	- [ ] Douleur oculaire importante
> 	- [ ] Photophobie marquée
> 	- [ ] Échec du traitement
> 	- [ ] Suspicion de complication

> [!success] 💊 Management — si Glaucome aigu
> - [ ] **1. Laboratoire de routine**
> - [ ] **2. Baisse médicamenteuse de la pression intraoculaire**
> - [ ] **3. Analgésie**
> - [ ] **4. Antiemèse**
> - [ ] **5. Avis d’ophtalmologue**
> - [ ] **6. Transfert en clinique ophtalmologique**
> - [ ] **7. Information sur le risque de cécité**
> - [ ] **8. Clinique ophtalmologique**
> - [ ] **9. Collyres locaux**
> - [ ] **10. Tonométrie de Goldmann**
> - [ ] **11. Répéter le fond d’œil**
> - [ ] **12. Gonioscopie**
> - [ ] **13. Iridotomie au laser**

> [!success] 💊 Management — si Kératite herpétique
> - [ ] **1. Diagnostic de suspicion**
> - [ ] **2. Origine**
> - [ ] **3. Propose un traitement topique**
> - [ ] **4. Propose un avis ophtalmologique**

> [!success] 💊 Management — si Kératite photoélectrique
> *Aucune grille du corpus ne documente ce diagnostic* — il est pourtant attendu de cette SSP. **Trou de révision à combler ailleurs.**

> [!success] 💊 Management — si Sécheresse oculaire évaporative (dysfonction des glandes de Meibom)
> - [ ] **1. Laboratoire uniquement en cas de suspicion systémique**
> - [ ] **2. Pas d’imagerie**
> - [ ] **3. Test de Schirmer**
> - [ ] **4. Information du patient**
> - [ ] **5. Hygiène des bords palpébraux**
> - [ ] **6. Larmes artificielles**
> - [ ] **7. Déclencheurs et hygiène de vie**
> - [ ] **8. Adapter le traitement de l’allergie**
> - [ ] **9. Contrôle évolutif**
> - [ ] **10. Examens complémentaires**
> - [ ] **11. Filet de sécurité**

> [!success] 💊 Management — si Zona
> *Aucune grille de cette SSP ne documente ce diagnostic* — mais le corpus le documente ailleurs : [[Mémento — Éruption Cutanée]] (2 grilles).
