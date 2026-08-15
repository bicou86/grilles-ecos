---
aliases:
  - "Mémento Diarrhée"
type: memento-ecos-ssp
ssp: "Diarrhée"
specialite: "Gastro-Hépatologie"
cas: 5
diagnostics: 5
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
> diagnostic : l'encadré 💊 se scinde en un bloc **commun** — ce que tous les
> diagnostics de la SSP partagent — puis un bloc **par diagnostic**. Un item
> porté par deux diagnostics sur cinq figure donc dans **deux** sous-blocs.
> À l'intérieur d'un sous-bloc, `*(n grilles sur m)*` compte les grilles **de
> ce diagnostic-là**, pas celles de la SSP.
>
> Un sous-bloc existe pour **chacun des diagnostics attendus de la SSP**
> (docs/ecos-priorites-2026.yaml), y compris ceux qu'aucune grille du corpus
> ne documente : ce sous-bloc vide est un **trou de révision** à combler
> ailleurs, pas un défaut du mémento.
>
> ⚠️ **Le suffixe parle des formulations, pas du contenu clinique.** Le
> rapprochement entre grilles est encore purement lexical : deux grilles qui
> disent la même chose autrement (« Motif de consultation » et « Motif de
> consultation principal », « Allergies » et « Allergies connues ») donnent
> **deux items distincts**, chacun marqué comme partiel. Un `*(1 grille sur 2)*`
> ne veut donc pas dire que l'autre grille néglige la question — seulement
> qu'elle l'écrit autrement. Tant que le vocabulaire canonique n'est pas
> rempli, lisez les libellés voisins ensemble.

# Diarrhée ⭐️

*Gastro-Hépatologie · 5 grilles · 5 diagnostics distincts* — [[SSP — Diarrhée]]

> [!abstract] Les 5 grilles fusionnées
> - **AMBOSS-8** — MICI (Crohn / RCUH) `premier-dd` · [grille](<file:///Users/damienfulliquet/Developer/GitHub/grilles-ecos/cases/amboss/AMBOSS-8_-_Troubles_du_transit_-_Homme_32_ans_-_Grille_ECOS.html>)
> - **German-13** — Diarrhée chronique par malabsorption `corrige` · [grille](<file:///Users/damienfulliquet/Developer/GitHub/grilles-ecos/cases/german/German-13_-_Diarrhe_e_-_Grille_ECOS.html>)
> - **German-85** — Déshydratation `corrige` · [grille](<file:///Users/damienfulliquet/Developer/GitHub/grilles-ecos/cases/german/German-85_-_Vomissements_et_diarrhe_e_-_Pe_diatrie_-_Grille_ECOS.html>)
> - **RESCOS-14** — Rectocolite ulcéro-hémorragique (RCUH) `explicite` · [grille](<file:///Users/damienfulliquet/Developer/GitHub/grilles-ecos/cases/rescos/RESCOS-14_-_Diarrhe_es_-_Grille_ECOS.html>)
> - **RESCOS-15** — Cancer colorectal `premier-dd` · [grille](<file:///Users/damienfulliquet/Developer/GitHub/grilles-ecos/cases/rescos/RESCOS-15_-_Diarrhe_es_et_constipation_-_Grille_ECOS.html>)

> [!note] 📋 Anamnèse
> - [ ] **1. Motif principal *(MICI (Crohn / RCUH))***
> - [ ] **2. Caractérisation des troubles du transit *(MICI (Crohn / RCUH))***
> 	- [ ] Début
> 	- [ ] Constant/intermittent
> 	- [ ] Événements précipitants
> 	- [ ] Progression
> 	- [ ] Épisodes antérieurs
> 	- [ ] Fréquence
> 	- [ ] Facteurs améliorants
> 	- [ ] Facteurs aggravants
> - [ ] **3. Caractéristiques des selles *(Diarrhée chronique par malabsorption · MICI (Crohn / RCUH))***
> 	- [ ] Diarrhée (couleur/consistance) *(MICI (Crohn / RCUH))*
> 	- [ ] Sang dans les selles *(MICI (Crohn / RCUH))*
> 	- [ ] Couleur du sang *(MICI (Crohn / RCUH))*
> 	- [ ] Quantité (mélangé, en surface) *(MICI (Crohn / RCUH))*
> 	- [ ] Constant/intermittent *(MICI (Crohn / RCUH))*
> 	- [ ] Début du saignement *(MICI (Crohn / RCUH))*
> 	- [ ] Fréquence *(Diarrhée chronique par malabsorption)*
> 	- [ ] Consistance : liquide - pâteuse - moulée - dure *(Diarrhée chronique par malabsorption)*
> 	- [ ] Volume *(Diarrhée chronique par malabsorption)*
> - [ ] **4. Symptômes associés - Douleurs abdominales *(MICI (Crohn / RCUH))***
> 	- [ ] Présence
> 	- [ ] Localisation
> 	- [ ] Intensité (échelle 0-10)
> 	- [ ] Qualité
> 	- [ ] Début
> 	- [ ] Événements précipitants
> 	- [ ] Progression/constant/intermittent
> 	- [ ] Épisodes antérieurs
> 	- [ ] Irradiation
> 	- [ ] Facteurs améliorants
> 	- [ ] Facteurs aggravants
> - [ ] **5. Recherche de symptômes spécifiques *(MICI (Crohn / RCUH))***
> 	- [ ] Voyage récent
> 	- [ ] Eau non purifiée, randonnée
> 	- [ ] Nausées/vomissements
> 	- [ ] Fièvre/frissons
> 	- [ ] Sueurs nocturnes/fatigue
> 	- [ ] Éruption/changements cutanés
> 	- [ ] Douleurs articulaires
> 	- [ ] Problèmes urinaires
> 	- [ ] Changements d'appétit
> 	- [ ] Variations pondérales
> 	- [ ] Infection récente
> 	- [ ] Vision floue
> - [ ] **6. Antécédents médicaux *(MICI (Crohn / RCUH))***
> - [ ] **7. Antécédents chirurgicaux *(MICI (Crohn / RCUH))***
> - [ ] **8. Allergies *(MICI (Crohn / RCUH))***
> - [ ] **9. Médicaments *(MICI (Crohn / RCUH))***
> - [ ] **10. Hospitalisations et contacts malades *(MICI (Crohn / RCUH))***
> 	- [ ] Hospitalisations
> 	- [ ] Contacts malades
> - [ ] **11. Antécédents familiaux *(MICI (Crohn / RCUH))***
> - [ ] **12. Habitudes et mode de vie *(MICI (Crohn / RCUH))***
> 	- [ ] Occupation
> 	- [ ] Domicile
> 	- [ ] Alcool
> 	- [ ] Drogues illicites
> 	- [ ] Tabac
> 	- [ ] Exercice
> 	- [ ] Alimentation
> - [ ] **13. Présentation avec nom, fonction et objectif de la consultation *(Diarrhée chronique par malabsorption · Déshydratation)***
> - [ ] **14. Question ouverte pour identifier le symptôme principal *(Diarrhée chronique par malabsorption)***
> - [ ] **15. Question de clarification : "Que comprenez-vous par diarrhée ?" *(Diarrhée chronique par malabsorption)***
> - [ ] **16. Caractérisation temporelle de la diarrhée *(Diarrhée chronique par malabsorption)***
> 	- [ ] Durée
> 	- [ ] Évolution : intermittente - continue - croissante
> 	- [ ] Épisodes antérieurs
> - [ ] **17. Aspect des selles *(Diarrhée chronique par malabsorption)***
> 	- [ ] Couleur : grise (acholique) - noire (méléna) - rouge (hématochézie)
> 	- [ ] Odeur : normale - très malodorante
> 	- [ ] Présence de sang/méléna
> 	- [ ] Présence de mucus/pus
> - [ ] **18. Facteurs influençants *(Diarrhée chronique par malabsorption)***
> 	- [ ] Alimentation, gluten
> 	- [ ] Changements alimentaires récents
> - [ ] **19. Symptômes associés généraux *(Diarrhée chronique par malabsorption)***
> 	- [ ] Fièvre
> 	- [ ] Céphalées
> 	- [ ] Douleurs musculaires/articulaires
> 	- [ ] Éruption cutanée
> - [ ] **20. Signes de déshydratation *(Diarrhée chronique par malabsorption)***
> 	- [ ] Production/couleur urinaire
> 	- [ ] Vertiges/hypotension orthostatique
> - [ ] **21. Symptômes constitutionnels *(Diarrhée chronique par malabsorption)***
> 	- [ ] Symptômes B (sueurs nocturnes, perte de poids)
> 	- [ ] Intolérance à la chaleur/transpiration excessive/tremblements
> - [ ] **22. Symptômes gastro-intestinaux associés *(Diarrhée chronique par malabsorption)***
> 	- [ ] Nausées/vomissements
> 	- [ ] Ballonnements/flatulences
> 	- [ ] Constipation paradoxale
> 	- [ ] Douleurs abdominales
> 	- [ ] Douleurs rectales
> 	- [ ] Incontinence fécale
> - [ ] **23. Antécédents médicaux pertinents *(Diarrhée chronique par malabsorption)***
> 	- [ ] Maladies préexistantes
> 	- [ ] Diabète
> 	- [ ] Chirurgies abdominales
> 	- [ ] Pathologie thyroïdienne
> 	- [ ] Radiothérapie abdominale
> - [ ] **24. Médicaments et allergies *(Diarrhée chronique par malabsorption)***
> 	- [ ] Médicaments actuels
> 	- [ ] Antibiotiques récents
> 	- [ ] Laxatifs
> 	- [ ] Autres médicaments pertinents
> 	- [ ] Allergies
> - [ ] **25. Habitudes de vie *(Diarrhée chronique par malabsorption)***
> 	- [ ] Alcool
> 	- [ ] Tabac
> 	- [ ] Drogues
> - [ ] **26. Antécédents familiaux digestifs *(Diarrhée chronique par malabsorption)***
> 	- [ ] Cancer colorectal
> 	- [ ] Maladie cœliaque
> 	- [ ] Maladies inflammatoires intestinales (MICI)
> - [ ] **27. Contexte épidémiologique *(Diarrhée chronique par malabsorption)***
> 	- [ ] Restauration collective
> 	- [ ] Consommation de viande crue
> 	- [ ] Eau non potable
> 	- [ ] Entourage affecté
> 	- [ ] Voyages récents
> - [ ] **28. Contexte social et professionnel *(Diarrhée chronique par malabsorption)***
> - [ ] **29. Question ouverte pour identifier le motif de consultation *(Déshydratation)***
> - [ ] **30. Signes cliniques de déshydratation *(Déshydratation)***
> 	- [ ] Pli cutané persistant
> 	- [ ] Muqueuses sèches
> 	- [ ] Oligurie
> - [ ] **31. Symptômes digestifs *(Déshydratation)***
> 	- [ ] Vomissements (fréquence, aspect)
> 	- [ ] Diarrhée (fréquence, consistance)
> - [ ] **32. Bilan des entrées et sorties *(Déshydratation)***
> 	- [ ] Quantité de boissons ingérées
> 	- [ ] Fréquence et volume des urines
> 	- [ ] Présence de larmes lors des pleurs
> - [ ] **33. État neurologique *(Déshydratation)***
> 	- [ ] Confusion
> 	- [ ] Somnolence
> 	- [ ] Sopor
> - [ ] **34. Recherche de causes infectieuses *(Déshydratation)***
> 	- [ ] Signes d'infection urinaire
> 	- [ ] Fièvre associée
> 	- [ ] Environnement épidémique
> - [ ] **35. Recherche de causes métaboliques - Diabète sucré *(Déshydratation)***
> 	- [ ] Polyurie-polydipsie
> 	- [ ] Perte de poids récente
> 	- [ ] Antécédents familiaux de diabète
> - [ ] **36. Recherche de causes endocriniennes - Insuffisance surrénalienne *(Déshydratation)***
> 	- [ ] Asthénie chronique
> 	- [ ] Hypotension
> 	- [ ] Hyperpigmentation cutanée
> - [ ] **37. Antécédents personnels *(Déshydratation)***
> 	- [ ] Maladies rénales
> 	- [ ] Maladies digestives chroniques
> 	- [ ] Hospitalisations récentes
> - [ ] **38. Habitudes alimentaires et hydratation habituelle *(Déshydratation)***
> - [ ] **39. Toxiques et médicaments *(Déshydratation)***
> 	- [ ] Diurétiques
> 	- [ ] Laxatifs
> 	- [ ] Autres médicaments
> - [ ] **40. Anamnèse de l'entourage *(Déshydratation)***
> 	- [ ] Cas similaires dans l'entourage
> 	- [ ] Voyage récent
> 	- [ ] Consommation d'aliments suspects
> - [ ] **41. Antécédents familiaux pertinents *(Déshydratation)***
> - [ ] **42. Anamnèse sociale *(Déshydratation)***
> 	- [ ] Conditions de vie
> 	- [ ] Autonomie (personne âgée)
> 	- [ ] Garde d'enfant/crèche
> - [ ] **43. Caractérisation de la plainte principale *(Rectocolite ulcéro-hémorragique (RCUH))***
> 	- [ ] Localisation de la douleur
> 	- [ ] Type de douleur
> 	- [ ] Intensité
> 	- [ ] Durée et fréquence
> 	- [ ] Facteurs aggravants
> - [ ] **44. Caractérisation des rectorragies *(Rectocolite ulcéro-hémorragique (RCUH))***
> 	- [ ] Présence de sang frais
> 	- [ ] Quantité et fréquence
> 	- [ ] Glaires
> 	- [ ] Diarrhées nocturnes
> 	- [ ] Ténesmes et urgences fécales
> - [ ] **45. Symptômes associés *(Rectocolite ulcéro-hémorragique (RCUH))***
> 	- [ ] Perte de poids
> 	- [ ] Inappétence
> 	- [ ] Nausées et vomissements
> 	- [ ] Fatigue
> 	- [ ] Palpitations
> - [ ] **46. Retentissement fonctionnel *(Rectocolite ulcéro-hémorragique (RCUH))***
> 	- [ ] Impact socioprofessionnel
> 	- [ ] Isolement social
> 	- [ ] Adaptation comportementale
> - [ ] **47. Antécédents et facteurs de risque *(Rectocolite ulcéro-hémorragique (RCUH))***
> 	- [ ] Voyage récent
> 	- [ ] Relations sexuelles non protégées
> 	- [ ] Consommation d'aliments à risque
> 	- [ ] Tabagisme
> 	- [ ] Médicaments gastrotoxiques
> - [ ] **48. Anamnèse systémique *(Rectocolite ulcéro-hémorragique (RCUH))***
> 	- [ ] Pas de symptômes urinaires
> 	- [ ] Pas de douleurs articulaires
> 	- [ ] Pas d'atteinte cutanée
> 	- [ ] Pas d'atteinte oculaire
> 	- [ ] Pas de notion de contage
> - [ ] **49. Anamnèse médicale et chirurgicale *(Rectocolite ulcéro-hémorragique (RCUH))***
> 	- [ ] Reflux gastro-œsophagien
> 	- [ ] Lombalgies chroniques
> 	- [ ] Appendicectomie
> 	- [ ] Cure de tunnel carpien
> - [ ] **50. Motif de consultation *(Cancer colorectal)***
> - [ ] **51. Caractérisation de la modification du transit *(Cancer colorectal)***
> 	- [ ] Évolution générale
> 	- [ ] Nombre de selles par 24h
> 	- [ ] Modification récente du transit
> 	- [ ] Selles noires déféquées
> 	- [ ] Selles nauséabondes
> - [ ] **52. Caractéristiques des selles - Aspect anormal *(Cancer colorectal)***
> 	- [ ] Selles de couleur habituelle mélée à du sang rouge
> 	- [ ] Selles rouges avec caillots
> 	- [ ] Selles noires luisantes
> 	- [ ] Selles couleur mastic
> 	- [ ] Selles jaunes-grisâtres, pâteuses
> 	- [ ] Selles en pétoles, dures
> 	- [ ] Selles rubanées de calibre diminué
> - [ ] **53. Symptômes digestifs associés *(Cancer colorectal)***
> 	- [ ] Distension abdominale douloureuse
> 	- [ ] Difficultés à s'alimenter
> 	- [ ] Ténesme
> 	- [ ] Épreintes
> 	- [ ] Douleurs abdominales
> 	- [ ] Ballonnements
> 	- [ ] Flatulences
> - [ ] **54. Éléments anormaux dans les selles *(Cancer colorectal)***
> 	- [ ] Glaires
> 	- [ ] Pus
> 	- [ ] Sang noir
> 	- [ ] Sang rouge
> 	- [ ] Graisses
> 	- [ ] Aliments non digérés
> - [ ] **55. Retentissement général *(Cancer colorectal)***
> 	- [ ] Asthénie
> 	- [ ] Perte de poids
> 	- [ ] Anorexie
> 	- [ ] Fièvre
> 	- [ ] Sueurs nocturnes
> 	- [ ] Altération de l'état général
> - [ ] **56. Définitions des troubles du transit *(Cancer colorectal)***
> 	- [ ] Diarrhée aiguë
> 	- [ ] Diarrhée chronique
> 	- [ ] Diarrhée
> 	- [ ] Constipation
> 	- [ ] Syndrome dysentérique
> 	- [ ] Syndrome cholérique
> - [ ] **57. Facteurs favorisants et antécédents *(Cancer colorectal)***
> 	- [ ] Alimentation récente
> 	- [ ] Voyage récent
> 	- [ ] Prise médicamenteuse
> 	- [ ] Stress psychosocial
> 	- [ ] Antécédents familiaux de cancer colorectal
> 	- [ ] Antécédents personnels de polypes
> 	- [ ] Maladies inflammatoires intestinales

> [!tip] 🩺 Status
> - [ ] **1. Mesures d'hygiène *(MICI (Crohn / RCUH))***
> 	- [ ] Lavage des mains
> 	- [ ] Respect de la pudeur avec drap
> - [ ] **2. Examen tête et cou *(MICI (Crohn / RCUH))***
> 	- [ ] Inspection des conjonctives
> 	- [ ] Examen des pupilles
> 	- [ ] Inspection de l'oropharynx
> - [ ] **3. Examen cardiovasculaire *(MICI (Crohn / RCUH))***
> - [ ] **4. Examen pulmonaire *(MICI (Crohn / RCUH))***
> - [ ] **5. Examen abdominal *(MICI (Crohn / RCUH) · Rectocolite ulcéro-hémorragique (RCUH))***
> 	- [ ] Inspection de l'abdomen
> 	- [ ] Auscultation de l'abdomen *(MICI (Crohn / RCUH))*
> 	- [ ] Percussion de l'abdomen *(MICI (Crohn / RCUH))*
> 	- [ ] Palpation de l'abdomen *(MICI (Crohn / RCUH))*
> 	- [ ] Auscultation des bruits intestinaux *(Rectocolite ulcéro-hémorragique (RCUH))*
> 	- [ ] Palpation des 4 quadrants *(Rectocolite ulcéro-hémorragique (RCUH))*
> 	- [ ] Recherche de défense ou détente *(Rectocolite ulcéro-hémorragique (RCUH))*
> 	- [ ] Recherche de masses *(Rectocolite ulcéro-hémorragique (RCUH))*
> - [ ] **6. Examen cutané *(MICI (Crohn / RCUH))***
> - [ ] **7. Examen abdominal complet *(Diarrhée chronique par malabsorption)***
> 	- [ ] Inspection (distension, cicatrices)
> 	- [ ] Auscultation (bruits hydroaériques)
> 	- [ ] Palpation (masses, douleur, défense)
> 	- [ ] Percussion (matité, tympanisme)
> - [ ] **8. Évaluation de l'état d'hydratation *(Diarrhée chronique par malabsorption)***
> 	- [ ] Turgor cutané
> 	- [ ] État des muqueuses
> - [ ] **9. Recherche de signes cutanés *(Diarrhée chronique par malabsorption)***
> 	- [ ] Érythème noueux
> 	- [ ] Pyoderma gangrenosum
> 	- [ ] Autres manifestations extra-intestinales
> - [ ] **10. Toucher rectal *(Cancer colorectal · Diarrhée chronique par malabsorption · Rectocolite ulcéro-hémorragique (RCUH))***
> 	- [ ] Tonus sphinctérien *(Cancer colorectal · Diarrhée chronique par malabsorption)*
> 	- [ ] Présence de sang *(Diarrhée chronique par malabsorption)*
> 	- [ ] Masses rectales *(Diarrhée chronique par malabsorption)*
> 	- [ ] Fécalome *(Diarrhée chronique par malabsorption)*
> 	- [ ] Inspection de la marge anale *(Rectocolite ulcéro-hémorragique (RCUH))*
> 	- [ ] Recherche de sang frais *(Rectocolite ulcéro-hémorragique (RCUH))*
> 	- [ ] Évaluation du tonus sphinctérien *(Rectocolite ulcéro-hémorragique (RCUH))*
> 	- [ ] Palpation rectale *(Rectocolite ulcéro-hémorragique (RCUH))*
> 	- [ ] Position genu-pectorale ou décubitus latéral *(Cancer colorectal)*
> 	- [ ] Ampoule rectale *(Cancer colorectal)*
> 	- [ ] Masses rectales palpables *(Cancer colorectal)*
> 	- [ ] Sang au doigtier *(Cancer colorectal)*
> 	- [ ] Douleur provoquée *(Cancer colorectal)*
> - [ ] **11. Examen thyroïdien *(Diarrhée chronique par malabsorption)***
> 	- [ ] Palpation de la thyroïde
> 	- [ ] Recherche de nodules
> - [ ] **12. Auscultation cardiopulmonaire *(Diarrhée chronique par malabsorption)***
> - [ ] **13. Évaluation clinique de l'état d'hydratation *(Déshydratation)***
> 	- [ ] Pli cutané (temps de recoloration)
> 	- [ ] État des muqueuses (sèches/humides)
> 	- [ ] Yeux enfoncés
> 	- [ ] Fontanelle déprimée (nourrisson)
> - [ ] **14. Palpation vésicale *(Déshydratation)***
> 	- [ ] Globe vésical
> 	- [ ] Douleur sus-pubienne
> - [ ] **15. Examen rénal *(Déshydratation)***
> 	- [ ] Palpation des fosses lombaires
> 	- [ ] Recherche de douleur à l'ébranlement
> - [ ] **16. Mesure de la tension artérielle *(Déshydratation)***
> 	- [ ] Recherche d'hypotension orthostatique
> - [ ] **17. Évaluation de l'état général *(Déshydratation)***
> 	- [ ] Poids actuel (si possible)
> 	- [ ] État de conscience
> 	- [ ] Température
> - [ ] **18. Signes vitaux et état général *(Rectocolite ulcéro-hémorragique (RCUH))***
> 	- [ ] Prise des signes vitaux
> 	- [ ] Évaluation de l'état général
> 	- [ ] Recherche de signes de déshydratation
> - [ ] **19. Recherche de complications *(Rectocolite ulcéro-hémorragique (RCUH))***
> 	- [ ] Signes de péritonite
> 	- [ ] Signes de mégacôlon toxique
> 	- [ ] État hémodynamique
> - [ ] **20. Recherche de manifestations extra-intestinales *(Rectocolite ulcéro-hémorragique (RCUH))***
> 	- [ ] Examen cutané
> 	- [ ] Examen articulaire
> 	- [ ] Examen oculaire si indiqué
> - [ ] **21. Inspection générale *(Cancer colorectal)***
> 	- [ ] Ambiance générale
> 	- [ ] Faciès
> 	- [ ] Pâleur cutanéo-muqueuse
> 	- [ ] Ictère
> 	- [ ] État d'hydratation
> 	- [ ] Signes de carences
> - [ ] **22. Signes vitaux *(Cancer colorectal)***
> 	- [ ] Pulsations, tension artérielle
> 	- [ ] Rythme et amplitude respiratoires
> 	- [ ] Température
> 	- [ ] Poids actuel et évolution
> - [ ] **23. Inspection abdominale *(Cancer colorectal)***
> 	- [ ] Morphologie
> 	- [ ] Symétrie vs asymétrie
> 	- [ ] Cicatrices
> 	- [ ] Hernies
> 	- [ ] Veines superficielles
> 	- [ ] Mouvements respiratoires
> - [ ] **24. Auscultation abdominale *(Cancer colorectal)***
> 	- [ ] Patience
> 	- [ ] Fréquence des bruits
> 	- [ ] Tonalité
> 	- [ ] Silence abdominal
> 	- [ ] Hyperactivité
> - [ ] **25. Percussion abdominale *(Cancer colorectal)***
> 	- [ ] Patient allongé
> 	- [ ] Tympanisme
> 	- [ ] Distension gazeuse
> 	- [ ] Matité
> 	- [ ] Mesure de la taille du foie, de la rate
> - [ ] **26. Palpation superficielle *(Cancer colorectal)***
> 	- [ ] Main à plat, doigts serrés
> 	- [ ] Tonus pariétal spontané et en réponse
> 	- [ ] Douleur localisée
> 	- [ ] Défense ou contracture
> 	- [ ] Extension
> 	- [ ] Douleur à l'ébranlement
> - [ ] **27. Palpation profonde *(Cancer colorectal)***
> 	- [ ] Recherche masse abdominale
> 	- [ ] Mobilité de la masse
> 	- [ ] Pulsations
> 	- [ ] Aorte
> 	- [ ] Taille des organes
> 	- [ ] Points douloureux spécifiques
> - [ ] **28. Palpation spécifique du côlon *(Cancer colorectal)***
> 	- [ ] Cadre colique
> 	- [ ] Sigmoïde
> 	- [ ] Cordon induré douloureux
> 	- [ ] Masses palpables
> 	- [ ] Sensibilité à la palpation

> [!success] 💊 Management — si Cancer colorectal
> - [ ] **1. Diagnostics différentiels des troubles du transit**
> - [ ] **2. Signes d'alarme (Red Flags)**
> - [ ] **3. Examens complémentaires de première intention**
> 	- [ ] FSC: recherche anémie ferriprive (saignement chronique)
> 	- [ ] Ferritine, fer sérique, transferrine
> 	- [ ] CRP, VS: syndrome inflammatoire
> 	- [ ] Ionogramme, urée, créatinine: déshydratation
> 	- [ ] Bilan hépatique: pathologie associée
> 	- [ ] TSH: dysthyroïdie cause de troubles du transit
> 	- [ ] Albumine: dénutrition, malabsorption
> - [ ] **4. Imagerie et endoscopie**
> 	- [ ] ASP debout face et profil: niveaux hydro-aériques si occlusion
> 	- [ ] CT abdomino-pelvien avec injection: bilan d'extension si tumeur
> 	- [ ] Coloscopie totale: examen de référence pour la pathologie colique
> 	- [ ] Visualisation directe des lésions
> 	- [ ] Biopsies multiples
> 	- [ ] Polypectomie thérapeutique
> 	- [ ] Gastroscopie si méléna: recherche saignement haut
> 	- [ ] Entéro-IRM ou vidéocapsule si suspicion grêle
> - [ ] **5. Marqueurs tumoraux et examens spécialisés**
> 	- [ ] ACE (antigène carcino-embryonnaire): cancer colorectal
> 	- [ ] CA 19-9: tumeurs digestives
> 	- [ ] Calprotectine fécale: inflammation intestinale
> 	- [ ] Test immunologique fécal (recherche de sang occulte dans les selles)
> 	- [ ] Coproculture si diarrhée fébrile
> 	- [ ] Recherche parasites si contexte évocateur
> 	- [ ] Test respiratoire lactose/fructose si malabsorption
> - [ ] **6. Traitement symptomatique des troubles du transit**
> - [ ] **7. Surveillance et suivi**
> 	- [ ] Contrôle biologique après traitement martial
> 	- [ ] Coloscopie de contrôle selon findings initiaux
> 	- [ ] Surveillance post-polypectomie selon recommandations
> 	- [ ] Dépistage famille si cancer colorectal
> 	- [ ] Éducation signes d'alarme
> 	- [ ] Suivi nutritionnel si dénutrition

> [!success] 💊 Management — si Colite à Clostridium
> *Aucune grille du corpus ne documente ce diagnostic* — il est pourtant attendu de cette SSP. **Trou de révision à combler ailleurs.**

> [!success] 💊 Management — si Diarrhée chronique par malabsorption
> - [ ] **1. Énonce le diagnostic principal**
> 	- [ ] Insuffisance pancréatique exocrine (sur pancréatites chroniques)
> - [ ] **2. Évoque les diagnostics différentiels pertinents**
> - [ ] **3. Propose les examens complémentaires de première intention**
> 	- [ ] Biologie : FSC, CRP, ionogramme (Na, K, Ca)
> 	- [ ] Fonction rénale : créatinine, urée
> 	- [ ] Fonction hépatique : transaminases, GGT, phosphatases alcalines (PAL), albumine
> 	- [ ] Bilan de coagulation : TP/INR, TCA
> 	- [ ] Fonction thyroïdienne : TSH
> - [ ] **4. Propose les examens complémentaires spécifiques**
> 	- [ ] Élastase fécale (insuffisance pancréatique)
> 	- [ ] Calprotectine fécale (inflammation intestinale)
> 	- [ ] Coproculture et recherche de parasites
> 	- [ ] US abdominal ou CT abdominal
> 	- [ ] Coloscopie avec biopsies
> - [ ] **5. Propose une prise en charge thérapeutique adaptée**
> - [ ] **6. Organise le suivi et reconnaît les complications**
> 	- [ ] Surveillance de l'état nutritionnel
> 	- [ ] Dépistage du cancer colorectal si indiqué
> 	- [ ] Orientation spécialisée si nécessaire (gastro-entérologie)
> 	- [ ] Hospitalisation si déshydratation sévère

> [!success] 💊 Management — si Diarrhée du voyageur
> *Aucune grille du corpus ne documente ce diagnostic* — il est pourtant attendu de cette SSP. **Trou de révision à combler ailleurs.**

> [!success] 💊 Management — si Déshydratation
> - [ ] **1. Énonce le diagnostic principal**
> 	- [ ] Déshydratation aiguë
> - [ ] **2. Évoque les diagnostics différentiels pertinents**
> - [ ] **3. Propose une prise en charge thérapeutique adaptée**
> - [ ] **4. Propose les examens complémentaires appropriés**
> 	- [ ] Ionogramme sanguin (Na, K, Cl)
> 	- [ ] Fonction rénale (créatinine, urée)
> 	- [ ] FSC (hémoconcentration : Hb, Ht)
> 	- [ ] Glycémie
> 	- [ ] Analyse d'urine si suspicion d'infection
> - [ ] **5. Organise le suivi et l'orientation**
> 	- [ ] Critères d'hospitalisation définis
> 	- [ ] Transfert à l'hôpital si nécessaire
> 	- [ ] Surveillance de la réhydratation
> 	- [ ] Éducation des parents/soignants

> [!success] 💊 Management — si MICI (Crohn / RCUH)
> - [ ] **1. Hypothèses diagnostiques**
> - [ ] **2. Examens complémentaires urgents**
> 	- [ ] Examen rectal
> 	- [ ] Recherche de sang occulte dans les selles
> 	- [ ] FSC, électrolytes
> 	- [ ] VS, CRP
> - [ ] **3. Examens microbiologiques**
> 	- [ ] Coproculture; microscopie des selles pour œufs et parasites
> - [ ] **4. Examens d'imagerie et endoscopie**
> 	- [ ] US abdominale
> 	- [ ] Radiographie abdominale simple
> 	- [ ] Coloscopie
> - [ ] **5. Communication avec le patient**
> 	- [ ] Explications au patient des impressions diagnostiques préliminaires
> 	- [ ] Explication du plan de prise en charge
> 	- [ ] Utilisation d'un langage non médical et clarification des termes médicaux
> 	- [ ] Évaluation de l'accord du patient avec le plan diagnostique
> 	- [ ] Recherche des préoccupations et questions du patient
> - [ ] **6. Conseil et prévention**
> 	- [ ] Conseil sur l'arrêt du tabac
> 	- [ ] Réaction appropriée au défi concernant le travail
> 	- [ ] Discussion sur l'importance du dépistage familial (cancer colorectal)

> [!success] 💊 Management — si Rectocolite ulcéro-hémorragique (RCUH)
> - [ ] **1. Hypothèse diagnostique principale**
> 	- [ ] Rectocolite ulcéro-hémorragique (RCUH)
> 	- [ ] Justification basée sur les symptômes
> 	- [ ] Explication adaptée à la patiente
> - [ ] **2. Diagnostics différentiels évoqués**
> 	- [ ] Maladie de Crohn
> 	- [ ] Colite infectieuse (bactérienne, parasitaire)
> 	- [ ] Colite médicamenteuse (AINS)
> 	- [ ] Carcinome colorectal
> - [ ] **3. Examens complémentaires**
> 	- [ ] Bilan biologique (FSC, CRP, électrolytes, fonction rénale)
> 	- [ ] Cultures de selles et parasitologie
> 	- [ ] Calprotectine fécale
> 	- [ ] Colonoscopie avec biopsies
> - [ ] **4. Prise en charge immédiate**
> 	- [ ] Critères d'hospitalisation évalués
> 	- [ ] Réhydratation IV
> 	- [ ] Corticothérapie IV si colite sévère
> 	- [ ] Arrêt des AINS
> - [ ] **5. Plan de suivi**
> 	- [ ] Consultation gastro-entérologie
> 	- [ ] Surveillance des complications
> 	- [ ] Protocole de dépistage du cancer colorectal
> 	- [ ] Soutien psychologique
> - [ ] **6. Communication avec la patiente**
> 	- [ ] Réponse à la question sur le cancer
> 	- [ ] Explication du caractère chronique de la maladie
> 	- [ ] Rassurance sur les options thérapeutiques
> 	- [ ] Information sur les groupes de soutien
