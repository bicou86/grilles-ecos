---
aliases:
  - "Mémento Éruption Cutanée"
type: memento-ecos-ssp
ssp: "Éruption Cutanée"
specialite: "Dermatologie"
cas: 8
diagnostics: 7
attendus_documentes_ailleurs: 0
attendus_absents_du_corpus: 4
tags:
  - ecos/memento
  - ecos/grille-officielle
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

> [!warning] Mémento mixte — 1 grille officielle, 7 non officielles
> **RESCOS-68b** fait partie des **neuf grilles officielles** et fait donc
> autorité ; elle est signalée ⭐️ dans l'encadré ci-dessous. Les 7
> autres sont des grilles d'entraînement (RESCOS, AMBOSS, GERMAN, AZYGOS)
> qu'aucun jury n'a validées.
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

# Éruption Cutanée ⭐️

*Dermatologie · 8 grilles · 7 diagnostics documentés · 4 attendus absents du corpus* — [[SSP — Éruption Cutanée]]

> [!abstract] Les 8 grilles fusionnées
> - **AZYGOS-1** — Psoriasis `diagnostic-travail` · [grille](<file:///Users/damienfulliquet/Developer/GitHub/grilles-ecos/docs/azygos-grilles/79a2e44d-a59f-4244-8729-c5a64fedbef0.json>)
> - **AZYGOS-26** — Syphilis `diagnostic-travail` · [grille](<file:///Users/damienfulliquet/Developer/GitHub/grilles-ecos/docs/azygos-grilles/f9ad6e9b-bdf5-4dcc-b66f-b7001601a5d0.json>)
> - **AZYGOS-27** — Dermatite périorale `diagnostic-travail` · [grille](<file:///Users/damienfulliquet/Developer/GitHub/grilles-ecos/docs/azygos-grilles/070f75f5-44ec-46b0-8df3-960bb134d4ee.json>)
> - **German-42** — Tinea corporis `corrige` · [grille](<file:///Users/damienfulliquet/Developer/GitHub/grilles-ecos/cases/german/German-42_-_Eruption_cutane_e_-_Grille_ECOS.html>)
> - **German-43** — Scarlatine / Angine streptococcique `corrige` · [grille](<file:///Users/damienfulliquet/Developer/GitHub/grilles-ecos/cases/german/German-43_-_Eruption_cutane_e_-_Grille_ECOS.html>)
> - **German-44** — Lupus érythémateux cutané `corrige` · [grille](<file:///Users/damienfulliquet/Developer/GitHub/grilles-ecos/cases/german/German-44_-_Erythe_me_-_Grille_ECOS.html>)
> - **RESCOS-68** — Zona `dd-principal` · [grille](<file:///Users/damienfulliquet/Developer/GitHub/grilles-ecos/cases/rescos/RESCOS-68%20-%20Eruption%20cutanée%20-%20Grille%20ECOS.html>)
> - **RESCOS-68b** ⭐️ **officielle** — Zona `explicite` · [grille](<file:///Users/damienfulliquet/Developer/GitHub/grilles-ecos/cases/rescos/RESCOS-68b%20-%20Eruption%20cutanée%20-%20Grille%20ECOS.html>)

> [!note] 📋 Anamnèse
> - [ ] **1. Question d’entrée *(Psoriasis · Syphilis)***
> - [ ] **2. Dimension temporelle *(Dermatite périorale · Psoriasis · Syphilis)***
> - [ ] **3. Début / durée *(Psoriasis · Syphilis)***
> - [ ] **4. Évolution *(Dermatite périorale · Psoriasis · Syphilis)***
> - [ ] **5. Épisodes *(Dermatite périorale · Psoriasis · Syphilis)***
> - [ ] **6. Localisation *(4 diagnostics)***
> - [ ] **7. Facteurs aggravants *(Dermatite périorale · Psoriasis · Syphilis)***
> - [ ] **8. Facteurs soulageants *(Dermatite périorale · Psoriasis · Syphilis)***
> - [ ] **9. Mesures déjà prises *(Psoriasis · Syphilis)***
> - [ ] **10. Symptômes associés *(6 grilles sur 8)***
> 	- [ ] Fièvre et frissons *(Scarlatine / Angine streptococcique)*
> 	- [ ] Mal de gorge *(Scarlatine / Angine streptococcique)*
> 	- [ ] Changements linguaux *(Scarlatine / Angine streptococcique)*
> 	- [ ] Fatigue/asthénie *(Lupus érythémateux cutané)*
> 	- [ ] Arthralgies *(Lupus érythémateux cutané)*
> 	- [ ] Céphalées *(2 grilles sur 8)*
> 	- [ ] Perte de poids *(Lupus érythémateux cutané)*
> 	- [ ] Fièvre *(1 grille sur 8)*
> 	- [ ] Fatigue *(1 grille sur 8)*
> 	- [ ] Toux *(1 grille sur 8)*
> - [ ] **11. Prurit *(4 grilles sur 8)***
> 	- [ ] Début & Évolution *(1 grille sur 8)*
> - [ ] **12. Douleurs *(Psoriasis · Syphilis · Zona)***
> 	- [ ] Début *(Zona)*
> 	- [ ] Précise moment par rapport aux lésions *(Zona)*
> 	- [ ] Caractère *(Zona)*
> 	- [ ] Intensité *(Zona)*
> 	- [ ] Facteurs atténuants/Facteurs aggravants *(1 grille sur 8)*
> 	- [ ] Médicaments pris *(Zona)*
> 	- [ ] Facteurs atténuants *(1 grille sur 8)*
> 	- [ ] Facteurs aggravants *(1 grille sur 8)*
> - [ ] **13. Ongles *(Psoriasis)***
> - [ ] **14. Phénomène de Köbner *(Psoriasis)***
> - [ ] **15. Plaintes articulaires *(Psoriasis)***
> - [ ] **16. Atopie *(Psoriasis)***
> - [ ] **17. Anamnèse personnelle *(4 diagnostics)***
> 	- [ ] Allergie *(Zona)*
> 	- [ ] Vaccins *(Zona)*
> - [ ] **18. Infection préalable *(Psoriasis)***
> - [ ] **19. Antécédents *(Psoriasis · Syphilis)***
> - [ ] **20. Maladies cutanées *(Psoriasis)***
> - [ ] **21. Médicaments actuels *(5 diagnostics)***
> - [ ] **22. Allergies *(Dermatite périorale · Psoriasis · Syphilis)***
> - [ ] **23. Noxes *(Psoriasis · Syphilis)***
> - [ ] **24. Alcool *(Dermatite périorale · Psoriasis · Syphilis)***
> - [ ] **25. Tabac *(Dermatite périorale · Psoriasis · Syphilis)***
> - [ ] **26. Drogues *(Dermatite périorale · Psoriasis · Syphilis)***
> - [ ] **27. Antécédents familiaux *(5 diagnostics)***
> - [ ] **28. Profession *(Dermatite périorale · Psoriasis · Syphilis)***
> - [ ] **29. Facteurs de stress psychosociaux *(Psoriasis)***
> - [ ] **30. Apparition *(Syphilis)***
> - [ ] **31. Déclencheurs *(Syphilis)***
> - [ ] **32. Qualité *(Syphilis)***
> - [ ] **33. Retentissement des symptômes *(Syphilis)***
> - [ ] **34. Dimension temporelle - sentiment de maladie *(Syphilis)***
> - [ ] **35. Fièvre *(Syphilis)***
> - [ ] **36. Symptômes d’infection *(Syphilis)***
> - [ ] **37. Rhinite *(Syphilis)***
> - [ ] **38. Maux de gorge *(Syphilis)***
> - [ ] **39. Toux *(Syphilis)***
> - [ ] **40. Dyspnée *(Syphilis)***
> - [ ] **41. Céphalées *(Syphilis)***
> - [ ] **42. Douleurs des membres *(Syphilis)***
> - [ ] **43. Ganglions lymphatiques *(Syphilis)***
> - [ ] **44. Adénopathie *(Syphilis)***
> - [ ] **45. Douloureux *(Syphilis)***
> - [ ] **46. Anamnèse de l’entourage *(Syphilis)***
> - [ ] **47. Exposition médicamenteuse derniers jours/semaines *(Syphilis)***
> - [ ] **48. Partenaires sexuels multiples *(Syphilis)***
> - [ ] **49. Rapports sexuels non protégés *(Syphilis)***
> - [ ] **50. Symptômes génitaux *(Syphilis)***
> - [ ] **51. Écoulement/Dysurie *(Syphilis)***
> - [ ] **52. Modifications génitales / chancre primaire *(Syphilis)***
> - [ ] **53. Symptômes B *(Syphilis)***
> - [ ] **54. Exposition solaire *(Syphilis)***
> - [ ] **55. Nouveaux produits cosmétiques/d’hygiène *(Syphilis)***
> - [ ] **56. Question initiale *(Dermatite périorale)***
> - [ ] **57. Début *(Dermatite périorale)***
> - [ ] **58. Facteur déclenchant *(Dermatite périorale)***
> - [ ] **59. Gravité *(Dermatite périorale)***
> - [ ] **60. Traitement médical préalable *(Dermatite périorale)***
> - [ ] **61. Stéroïdes topiques *(Dermatite périorale)***
> - [ ] **62. Cosmétiques *(Dermatite périorale)***
> - [ ] **63. Douleurs / Brûlures *(Dermatite périorale)***
> - [ ] **64. Peau *(Dermatite périorale)***
> - [ ] **65. Comédons *(Dermatite périorale)***
> - [ ] **66. Autres plaintes cutanées *(Dermatite périorale)***
> - [ ] **67. Symptômes généraux *(Dermatite périorale)***
> - [ ] **68. Antécédents médicaux personnels *(Dermatite périorale · Scarlatine / Angine streptococcique · Tinea corporis)***
> 	- [ ] Maladies antérieures *(Scarlatine / Angine streptococcique · Tinea corporis)*
> 	- [ ] Interventions chirurgicales *(Scarlatine / Angine streptococcique · Tinea corporis)*
> 	- [ ] Médicaments actuels *(Scarlatine / Angine streptococcique)*
> - [ ] **69. Toxiques *(Dermatite périorale)***
> - [ ] **70. Charge psychosociale *(Dermatite périorale)***
> - [ ] **71. Désinfection des mains, présentation avec nom, fonction et but de la consultation *(Lupus érythémateux cutané · Scarlatine / Angine streptococcique · Tinea corporis)***
> - [ ] **72. Exploration du symptôme principal : éruption cutanée *(Scarlatine / Angine streptococcique · Tinea corporis)***
> - [ ] **73. Évolution temporelle de l'éruption *(Scarlatine / Angine streptococcique · Tinea corporis)***
> - [ ] **74. Évolution et extension des lésions *(Tinea corporis)***
> - [ ] **75. Évolution clinique (amélioration/aggravation) *(Tinea corporis)***
> - [ ] **76. Caractéristiques des lésions *(Tinea corporis)***
> 	- [ ] Aspect (squameux, vésiculeux, etc.)
> 	- [ ] Symptômes associés (prurit, douleur)
> - [ ] **77. Facteurs d'exposition ou déclenchants *(Tinea corporis)***
> - [ ] **78. Symptômes B (fièvre, sueurs nocturnes, perte de poids) *(Tinea corporis)***
> - [ ] **79. Allergies connues *(Scarlatine / Angine streptococcique · Tinea corporis)***
> - [ ] **80. Habitudes de vie *(Lupus érythémateux cutané · Tinea corporis)***
> 	- [ ] Alcool
> 	- [ ] Tabac
> 	- [ ] Drogues
> - [ ] **81. Anamnèse sociale et professionnelle *(Tinea corporis)***
> - [ ] **82. Localisation de l'éruption *(Scarlatine / Angine streptococcique)***
> - [ ] **83. Caractéristiques de l'éruption *(Scarlatine / Angine streptococcique)***
> 	- [ ] Prurit
> 	- [ ] Texture au toucher
> - [ ] **84. État général et symptômes systémiques *(Scarlatine / Angine streptococcique)***
> 	- [ ] Comportement général
> 	- [ ] Céphalées
> 	- [ ] Problèmes respiratoires
> 	- [ ] Autres symptômes systémiques
> - [ ] **85. Statut vaccinal *(Scarlatine / Angine streptococcique)***
> - [ ] **86. Examens préventifs récents *(Scarlatine / Angine streptococcique)***
> - [ ] **87. Anamnèse sociale et exposition *(Scarlatine / Angine streptococcique)***
> 	- [ ] Fréquentation collective
> 	- [ ] Contacts malades
> - [ ] **88. Exploration du symptôme principal *(Lupus érythémateux cutané)***
> - [ ] **89. Caractéristiques de l'érythème *(Lupus érythémateux cutané)***
> 	- [ ] Douleur
> 	- [ ] Sensation de brûlure
> 	- [ ] Prurit
> - [ ] **90. Évolution temporelle et facteurs déclenchants *(Lupus érythémateux cutané)***
> 	- [ ] Durée
> 	- [ ] Facteur déclenchant
> 	- [ ] Évolution
> - [ ] **91. Antécédents d'épisodes similaires *(Lupus érythémateux cutané)***
> - [ ] **92. Revue des systèmes *(Lupus érythémateux cutané)***
> - [ ] **93. Antécédents médicaux et chirurgicaux *(Lupus érythémateux cutané)***
> - [ ] **94. Anamnèse de voyage et exposition solaire *(Lupus érythémateux cutané)***
> 	- [ ] Voyage récent
> 	- [ ] Évolution pendant le voyage
> 	- [ ] Fièvre au retour
> 	- [ ] Exposition solaire
> - [ ] **95. Lésions *(Zona)***
> 	- [ ] Début
> 	- [ ] Évolution en nombre
> 	- [ ] Évolution en caractère
> 	- [ ] Localisation
> - [ ] **96. Premier épisode *(Zona)***
> 	- [ ] A demandé si ATCD similaire *(1 grille sur 8)*
> - [ ] **97. Symptômes associés : Fièvre/fatigue/toux/céphalées *(1 grille sur 8)***
> - [ ] **98. Facteurs de risque *(Zona)***
> 	- [ ] Trauma/stress *(1 grille sur 8)*
> 	- [ ] Traitement immunosuppresseur/infection récente/maladie (cancer, VIH, Immuno) *(1 grille sur 8)*
> 	- [ ] Fatigue importante
> 	- [ ] Trauma *(1 grille sur 8)*
> 	- [ ] Stress *(1 grille sur 8)*
> 	- [ ] Traitement immunosuppresseur *(1 grille sur 8)*
> 	- [ ] Infection récente *(1 grille sur 8)*
> 	- [ ] Maladie (cancer, VIH, immunosuppression) *(1 grille sur 8)*
> - [ ] **99. Anamnèse de varicelle *(Zona)***
> - [ ] **100. Contage *(Zona)***
> - [ ] **101. Douleurs soulagées par cannabis *(1 grille sur 8)***
> - [ ] **102. Prurit — début ET évolution *(1 grille sur 8)***

> [!tip] 🩺 Status
> - [ ] **1. Paramètres vitaux *(Psoriasis · Syphilis)***
> - [ ] **2. Inspection cutanée détaillée *(Psoriasis · Tinea corporis)***
> 	- [ ] Description des lésions *(Tinea corporis)*
> 	- [ ] Distribution et morphologie *(Tinea corporis)*
> 	- [ ] Caractéristiques spécifiques *(Tinea corporis)*
> - [ ] **3. Inspection du cuir chevelu *(Psoriasis)***
> - [ ] **4. Signes de grattage *(Psoriasis)***
> - [ ] **5. Signe de la bougie *(Psoriasis)***
> - [ ] **6. Dernière lamelle *(Psoriasis)***
> - [ ] **7. Signe d’Auspitz *(Psoriasis)***
> - [ ] **8. Inspection des ongles *(Psoriasis)***
> - [ ] **9. Statut articulaire *(Lupus érythémateux cutané · Psoriasis)***
> 	- [ ] Douleur à la palpation *(Lupus érythémateux cutané)*
> 	- [ ] Épanchement articulaire *(Lupus érythémateux cutané)*
> 	- [ ] Limitation des mouvements *(Lupus érythémateux cutané)*
> - [ ] **10. Muqueuses *(Syphilis)***
> - [ ] **11. Peau *(Syphilis)***
> - [ ] **12. Mains *(Syphilis)***
> - [ ] **13. Pieds *(Syphilis)***
> - [ ] **14. Examen anogénital *(Syphilis)***
> - [ ] **15. Cuir chevelu *(Dermatite périorale · Syphilis)***
> - [ ] **16. Ongles des doigts *(Syphilis)***
> - [ ] **17. Ganglions lymphatiques *(Syphilis)***
> - [ ] **18. État général *(Dermatite périorale)***
> - [ ] **19. Observation cutanée du visage *(Dermatite périorale)***
> - [ ] **20. Tronc et membres *(Dermatite périorale)***
> - [ ] **21. Ongles *(Dermatite périorale)***
> - [ ] **22. Conjonctives *(Dermatite périorale)***
> - [ ] **23. Muqueuse buccale *(Dermatite périorale)***
> - [ ] **24. Dermographisme *(Tinea corporis)***
> - [ ] **25. Évaluation du statut cutané général *(Tinea corporis)***
> 	- [ ] Recherche d'autres lésions
> 	- [ ] État de la peau saine
> 	- [ ] Signes de grattage
> - [ ] **26. Palpation des ganglions lymphatiques régionaux *(Tinea corporis)***
> - [ ] **27. Signes d'infection secondaire *(Tinea corporis)***
> - [ ] **28. Évaluation des signes de déshydratation *(Scarlatine / Angine streptococcique)***
> 	- [ ] Diurèse
> 	- [ ] Fontanelle
> 	- [ ] Yeux enfoncés
> 	- [ ] Muqueuses sèches
> 	- [ ] Pli cutané
> - [ ] **29. Examen cutané détaillé *(Lupus érythémateux cutané · Scarlatine / Angine streptococcique)***
> 	- [ ] Description de l'érythème *(Lupus érythémateux cutané)*
> 	- [ ] Localisation *(Lupus érythémateux cutané)*
> 	- [ ] Aspect *(Lupus érythémateux cutané)*
> - [ ] **30. Examen ORL *(Scarlatine / Angine streptococcique)***
> 	- [ ] Aspect de la langue
> 	- [ ] État des amygdales
> - [ ] **31. Auscultation pulmonaire *(Scarlatine / Angine streptococcique)***
> - [ ] **32. Recherche de signes de gravité *(Scarlatine / Angine streptococcique)***
> 	- [ ] État de conscience
> 	- [ ] Signes méningés
> 	- [ ] Signes de choc
> - [ ] **33. Inspection générale *(Lupus érythémateux cutané)***
> 	- [ ] État des yeux
> 	- [ ] Muqueuses
> - [ ] **34. Examen cardio-pulmonaire *(Lupus érythémateux cutané)***
> - [ ] **35. Examen neurologique *(Lupus érythémateux cutané)***
> - [ ] **36. Recherche de signes évocateurs de lupus *(Lupus érythémateux cutané)***
> 	- [ ] Éruption malaire
> 	- [ ] Ulcérations buccales
> 	- [ ] Alopécie
> 	- [ ] Phénomène de Raynaud
> - [ ] **37. Inspection des lésions *(Zona)***
> - [ ] **38. Inspection des paumes des mains/plantes des pieds *(Zona)***
> 	- [ ] Paumes des mains *(1 grille sur 8)*
> 	- [ ] Plantes des pieds *(1 grille sur 8)*
> - [ ] **39. Examen des aires ganglionnaires : Axillaires/Inguinales/Cervicales *(1 grille sur 8)***
> - [ ] **40. Palpation du thorax pour reproduire les douleurs *(Zona)***
> - [ ] **41. Examen des muqueuses : Bouche/Nez/OGE (intention) *(1 grille sur 8)***
> - [ ] **42. Intention de faire un status ORL, pulmonaire ou cardiaque *(Zona)***
> 	- [ ] ORL *(1 grille sur 8)*
> 	- [ ] Pulmonaire *(1 grille sur 8)*
> 	- [ ] Cardiaque *(1 grille sur 8)*
> - [ ] **43. Examen des aires ganglionnaires *(1 grille sur 8)***
> 	- [ ] Axillaires
> 	- [ ] Inguinales
> 	- [ ] Cervicales
> - [ ] **44. Examen des muqueuses (intention) *(1 grille sur 8)***
> 	- [ ] Bouche
> 	- [ ] Nez
> 	- [ ] OGE

> [!success] 💊 Management — partagé par plusieurs diagnostics
> - [ ] **1. Diagnostic clinique *(2 grilles sur 8)* — *Dermatite périorale · Psoriasis***
> - [ ] **2. Diagnostic de travail *(2 grilles sur 8)* — *Psoriasis · Syphilis***
> - [ ] **3. Filet de sécurité *(2 grilles sur 8)* — *Psoriasis · Syphilis***
> - [ ] **4. Diagnostic de suspicion principal *(3 grilles sur 8)* — *Lupus érythémateux cutané · Scarlatine / Angine streptococcique · Tinea corporis***
> - [ ] **5. Traitement proposé *(3 grilles sur 8)* — *Lupus érythémateux cutané · Scarlatine / Angine streptococcique · Tinea corporis***

> [!success] 💊 Management — si Dermatite périorale
> - [ ] **1. Diagnostic de travail : dermatite périorale**
> - [ ] **2. Indices anamnestiques**
> - [ ] **3. Cosmétiques**
> - [ ] **4. Profil de rebond stéroïdien**
> - [ ] **5. Caractère des symptômes**
> - [ ] **6. Résultats cliniques**
> - [ ] **7. Localisation périorale**
> - [ ] **8. Lisière des lèvres respectée**
> - [ ] **9. Papules érythémateuses monomorphes**
> - [ ] **10. DD Acné vulgaire**
> - [ ] **11. Pour**
> - [ ] **12. Contre**
> - [ ] **13. DD Eczéma de contact**
> - [ ] **14. DD Rosacée**
> - [ ] **15. Absence d'examens complémentaires**
> - [ ] **16. Prise en charge de base : thérapie zéro correcte**
> - [ ] **17. Arrêt des stéroïdes**
> - [ ] **18. Réduction des soins**
> - [ ] **19. Éducation de la patiente**
> - [ ] **20. Cause**
> - [ ] **21. Évolution et gestion des attentes**
> - [ ] **22. Contrôle d'évolution**
> - [ ] **23. Traitement élargi**
> - [ ] **24. Traitement topique anti-inflammatoire**
> - [ ] **25. Escalade systémique en cas d'échec thérapeutique**
> - [ ] **26. Complications / Signes d'alarme**
> - [ ] **27. Atteinte oculaire**
> - [ ] **28. Résistance au traitement**
> - [ ] **29. Infection secondaire**
> - [ ] **30. Symptômes généraux**

> [!success] 💊 Management — si Eczéma / Dermatite
> *Aucune grille du corpus ne documente ce diagnostic* — il est pourtant attendu de cette SSP. **Trou de révision à combler ailleurs.**

> [!success] 💊 Management — si Gale
> *Aucune grille du corpus ne documente ce diagnostic* — il est pourtant attendu de cette SSP. **Trou de révision à combler ailleurs.**

> [!success] 💊 Management — si Lupus érythémateux cutané
> - [ ] **1. Diagnostics différentiels**
> - [ ] **2. Examens complémentaires proposés**
> 	- [ ] Biologie sanguine
> 	- [ ] Analyse d'urine
> 	- [ ] Fonction rénale
> - [ ] **3. Justification des examens**
> 	- [ ] Recherche de signes de lupus systémique
> 	- [ ] Évaluation de l'inflammation
> 	- [ ] Dépistage d'atteinte rénale (néphrite lupique)
> - [ ] **4. Information sur l'évolution possible**
> - [ ] **5. Surveillance et suivi recommandés**
> 	- [ ] Contrôle dans 4-6 semaines avec résultats
> 	- [ ] Surveillance biologique régulière si ANA positifs
> 	- [ ] Examen des autres systèmes à chaque consultation
> 	- [ ] Référence en dermatologie si évolution défavorable

> [!success] 💊 Management — si Pityriasis versicolor
> *Aucune grille du corpus ne documente ce diagnostic* — il est pourtant attendu de cette SSP. **Trou de révision à combler ailleurs.**

> [!success] 💊 Management — si Psoriasis
> - [ ] **1. Examen à l’état frais**
> - [ ] **2. Dermatoscopie**
> - [ ] **3. Diagnostics différentiels**
> - [ ] **4. Traitement de base**
> - [ ] **5. Soins cutanés**
> - [ ] **6. Kératolyse**
> - [ ] **7. Éviter les déclencheurs**
> - [ ] **8. Thérapie topique**
> - [ ] **9. Information**
> - [ ] **10. Suivi de l’évolution**
> - [ ] **11. Orientation en dermatologie**
> - [ ] **12. Revue médicamenteuse**

> [!success] 💊 Management — si Scarlatine / Angine streptococcique
> - [ ] **1. Diagnostics différentiels**
> - [ ] **2. Examens complémentaires proposés**
> 	- [ ] Test rapide streptocoque
> 	- [ ] Culture bactériologique
> - [ ] **3. Planification du suivi**
> 	- [ ] Surveillance de l'efficacité du traitement
> 	- [ ] Vérification de la disparition des symptômes
> 	- [ ] Dépistage des complications tardives (glomérulonéphrite, RAA)
> - [ ] **4. Mesures préventives et prophylaxie**
> 	- [ ] Prophylaxie de l'entourage
> 	- [ ] Éviction scolaire
> 	- [ ] Mesures d'hygiène
> - [ ] **5. Information aux parents et surveillance**
> 	- [ ] Explication de la maladie
> 	- [ ] Importance de l'observance du traitement
> 	- [ ] Signes d'alerte (complications)
> 	- [ ] Quand reconsulter

> [!success] 💊 Management — si Syndrome de Stevens-Johnson / Lyell
> *Aucune grille du corpus ne documente ce diagnostic* — il est pourtant attendu de cette SSP. **Trou de révision à combler ailleurs.**

> [!success] 💊 Management — si Syphilis
> - [ ] **1. Bilan de base étendu**
> - [ ] **2. Dépistage IST**
> - [ ] **3. Sérologie syphilis**
> - [ ] **4. TPPA / TPHA comme test de dépistage**
> - [ ] **5. FTA-ABS comme test de confirmation**
> - [ ] **6. VDRL ou RPR pour évaluer l’activité**
> - [ ] **7. Anticorps IgM comme indice d’infection récente**
> - [ ] **8. Pénicilline G i.m.**
> - [ ] **9. Recueillir l’anamnèse des partenaires et recommander un traitement des partenaires**
> - [ ] **10. Information sur la contagion et les mesures de protection**
> - [ ] **11. Planifier des contrôles sérologiques de suivi**
> - [ ] **12. Informer sur une possible réaction de Jarisch-Herxheimer**
> - [ ] **13. Reconsultation immédiate en cas de signes d’alarme**

> [!success] 💊 Management — si Tinea corporis
> - [ ] **1. Diagnostics différentiels**
> - [ ] **2. Examens complémentaires proposés**
> 	- [ ] Prélèvement mycologique
> 	- [ ] Culture mycologique
> - [ ] **3. Interprétation des examens**
> - [ ] **4. Mesures préventives et conseils**
> 	- [ ] Éviter les environnements humides
> 	- [ ] Sécher soigneusement la peau
> 	- [ ] Éviter le partage de serviettes
> 	- [ ] Traiter les contacts si nécessaire
> - [ ] **5. Planification du suivi**
> 	- [ ] Contrôle après 2 semaines de traitement
> 	- [ ] Vérification de la guérison mycologique
> 	- [ ] Adaptation du traitement si nécessaire

> [!success] 💊 Management — si Zona
> - [ ] **1. Diagnostics différentiels *(1 grille sur 2)***
> 	- [ ] Eczéma
> 	- [ ] Impétigo
> 	- [ ] Varicelle
> 	- [ ] Dermatite de contact
> - [ ] **2. Présentation du cas**
> 	- [ ] Synthétique
> 	- [ ] Avec les éléments pertinents de l'anamnèse et du status
> - [ ] **3. Hypothèse Diagnostique *(1 grille sur 2)***
> - [ ] **4. Diagnostic principal et diagnostics différentiels *(1 grille sur 2)***
> - [ ] **5. Argumentation pour les DD *(1 grille sur 2)***
> - [ ] **6. Examens complémentaires indiqués**
> 	- [ ] Frottis des lésions *(1 grille sur 2)*
> - [ ] **7. Dépistage Immunologique (VIH ou autre)**
> - [ ] **8. Hypothèse diagnostique : ZONA *(1 grille sur 2)***
> - [ ] **9. Argumentation *(1 grille sur 2)***
> 	- [ ] Pour le zona : pas de contage, douleurs intenses antérieures aux lésions, antécédent de varicelle, lésions vésiculo-papuleuses limitées à un dermatome ne dépassant pas la ligne médiane. Contre : jeune âge, pas de traitement immunosuppresseur ni de maladie immunologique connue, lésions très croûteuses, pas d'adénopathie.
