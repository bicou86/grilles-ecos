---
aliases:
  - "Mémento Diarrhée"
type: memento-ecos-ssp
ssp: "Diarrhée"
specialite: "Gastro-Hépatologie"
cas: 5
diagnostics: 4
attendus_documentes_ailleurs: 0
attendus_absents_du_corpus: 2
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

# Diarrhée ⭐️

*Gastro-Hépatologie · 5 grilles · 4 diagnostics documentés · 2 attendus absents du corpus* — [[SSP — Diarrhée]]

> [!abstract] Les 5 grilles fusionnées
> - **AMBOSS-8** — MICI (Crohn / RCUH) `premier-dd` · [grille](<file:///Users/damienfulliquet/Developer/GitHub/grilles-ecos/cases/amboss/AMBOSS-8_-_Troubles_du_transit_-_Homme_32_ans_-_Grille_ECOS.html>)
> - **German-13** — Diarrhée chronique par malabsorption `corrige` · [grille](<file:///Users/damienfulliquet/Developer/GitHub/grilles-ecos/cases/german/German-13_-_Diarrhe_e_-_Grille_ECOS.html>)
> - **German-85** — Déshydratation `corrige` · [grille](<file:///Users/damienfulliquet/Developer/GitHub/grilles-ecos/cases/german/German-85_-_Vomissements_et_diarrhe_e_-_Pe_diatrie_-_Grille_ECOS.html>)
> - **RESCOS-14** — MICI (Crohn / RCUH) `explicite` · [grille](<file:///Users/damienfulliquet/Developer/GitHub/grilles-ecos/cases/rescos/RESCOS-14_-_Diarrhe_es_-_Grille_ECOS.html>)
> - **RESCOS-15** — Cancer colorectal `premier-dd` · [grille](<file:///Users/damienfulliquet/Developer/GitHub/grilles-ecos/cases/rescos/RESCOS-15_-_Diarrhe_es_et_constipation_-_Grille_ECOS.html>)

> [!note] 📋 Anamnèse
> - [ ] **1. Motif de consultation *(2 grilles sur 5)***
> - [ ] **2. Caractérisation des troubles du transit *(Cancer colorectal · MICI (Crohn / RCUH))***
> 	- [ ] Début *(1 grille sur 5)*
> 	- [ ] Constant/intermittent *(1 grille sur 5)*
> 	- [ ] Événements précipitants *(1 grille sur 5)*
> 	- [ ] Progression *(1 grille sur 5)*
> 	- [ ] Épisodes antérieurs *(1 grille sur 5)*
> 	- [ ] Fréquence *(1 grille sur 5)*
> 	- [ ] Facteurs améliorants *(1 grille sur 5)*
> 	- [ ] Facteurs aggravants *(1 grille sur 5)*
> 	- [ ] Présence de sang frais *(1 grille sur 5)*
> 	- [ ] Quantité et fréquence *(1 grille sur 5)*
> 	- [ ] Glaires *(1 grille sur 5)*
> 	- [ ] Diarrhées nocturnes *(1 grille sur 5)*
> 	- [ ] Ténesmes et urgences fécales *(1 grille sur 5)*
> 	- [ ] Diarrhée aiguë *(Cancer colorectal)*
> 	- [ ] Diarrhée chronique *(Cancer colorectal)*
> 	- [ ] Diarrhée *(Cancer colorectal)*
> 	- [ ] Constipation *(Cancer colorectal)*
> 	- [ ] Syndrome dysentérique *(Cancer colorectal)*
> 	- [ ] Syndrome cholérique *(Cancer colorectal)*
> - [ ] **3. Caractéristiques des selles - Aspect anormal *(3 grilles sur 5)***
> 	- [ ] Diarrhée (couleur/consistance) *(1 grille sur 5)*
> 	- [ ] Sang dans les selles *(1 grille sur 5)*
> 	- [ ] Couleur du sang *(1 grille sur 5)*
> 	- [ ] Quantité (mélangé, en surface) *(1 grille sur 5)*
> 	- [ ] Constant/intermittent *(1 grille sur 5)*
> 	- [ ] Début du saignement *(1 grille sur 5)*
> 	- [ ] Fréquence *(Diarrhée chronique par malabsorption)*
> 	- [ ] Consistance : liquide - pâteuse - moulée - dure *(Diarrhée chronique par malabsorption)*
> 	- [ ] Volume *(Diarrhée chronique par malabsorption)*
> 	- [ ] Selles de couleur habituelle mélée à du sang rouge *(Cancer colorectal)*
> 	- [ ] Selles rouges avec caillots *(Cancer colorectal)*
> 	- [ ] Selles noires luisantes *(Cancer colorectal)*
> 	- [ ] Selles couleur mastic *(Cancer colorectal)*
> 	- [ ] Selles jaunes-grisâtres, pâteuses *(Cancer colorectal)*
> 	- [ ] Selles en pétoles, dures *(Cancer colorectal)*
> 	- [ ] Selles rubanées de calibre diminué *(Cancer colorectal)*
> - [ ] **4. Symptômes associés - Douleurs abdominales *(1 grille sur 5)***
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
> - [ ] **5. Recherche de symptômes spécifiques *(1 grille sur 5)***
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
> - [ ] **6. Antécédents médicaux *(2 grilles sur 5)***
> 	- [ ] Maladies rénales *(Déshydratation)*
> 	- [ ] Maladies digestives chroniques *(Déshydratation)*
> 	- [ ] Hospitalisations récentes *(Déshydratation)*
> - [ ] **7. Antécédents chirurgicaux *(1 grille sur 5)***
> - [ ] **8. Allergies *(1 grille sur 5)***
> - [ ] **9. Médicaments *(1 grille sur 5)***
> - [ ] **10. Hospitalisations et contacts malades *(1 grille sur 5)***
> 	- [ ] Hospitalisations
> 	- [ ] Contacts malades
> - [ ] **11. Antécédents familiaux digestifs *(2 grilles sur 5)***
> 	- [ ] Cancer colorectal *(Diarrhée chronique par malabsorption)*
> 	- [ ] Maladie cœliaque *(Diarrhée chronique par malabsorption)*
> 	- [ ] Maladies inflammatoires intestinales (MICI) *(Diarrhée chronique par malabsorption)*
> - [ ] **12. Habitudes et mode de vie *(2 grilles sur 5)***
> 	- [ ] Occupation *(1 grille sur 5)*
> 	- [ ] Domicile *(1 grille sur 5)*
> 	- [ ] Alcool
> 	- [ ] Drogues illicites *(1 grille sur 5)*
> 	- [ ] Tabac
> 	- [ ] Exercice *(1 grille sur 5)*
> 	- [ ] Alimentation *(1 grille sur 5)*
> 	- [ ] Drogues *(Diarrhée chronique par malabsorption)*
> - [ ] **13. Présentation avec nom, fonction et objectif de la consultation *(Diarrhée chronique par malabsorption · Déshydratation)***
> - [ ] **14. Question ouverte pour identifier le motif de consultation *(Diarrhée chronique par malabsorption · Déshydratation)***
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
> - [ ] **19. Symptômes digestifs associés *(4 grilles sur 5)***
> 	- [ ] Fièvre *(Diarrhée chronique par malabsorption)*
> 	- [ ] Céphalées *(Diarrhée chronique par malabsorption)*
> 	- [ ] Douleurs musculaires/articulaires *(Diarrhée chronique par malabsorption)*
> 	- [ ] Éruption cutanée *(Diarrhée chronique par malabsorption)*
> 	- [ ] Vomissements (fréquence, aspect) *(Déshydratation)*
> 	- [ ] Diarrhée (fréquence, consistance) *(Déshydratation)*
> 	- [ ] Perte de poids *(1 grille sur 5)*
> 	- [ ] Inappétence *(1 grille sur 5)*
> 	- [ ] Nausées et vomissements *(1 grille sur 5)*
> 	- [ ] Fatigue *(1 grille sur 5)*
> 	- [ ] Palpitations *(1 grille sur 5)*
> 	- [ ] Distension abdominale douloureuse *(Cancer colorectal)*
> 	- [ ] Difficultés à s'alimenter *(Cancer colorectal)*
> 	- [ ] Ténesme *(Cancer colorectal)*
> 	- [ ] Épreintes *(Cancer colorectal)*
> 	- [ ] Douleurs abdominales *(Cancer colorectal)*
> 	- [ ] Ballonnements *(Cancer colorectal)*
> 	- [ ] Flatulences *(Cancer colorectal)*
> - [ ] **20. Signes cliniques de déshydratation *(Diarrhée chronique par malabsorption · Déshydratation)***
> 	- [ ] Production/couleur urinaire *(Diarrhée chronique par malabsorption)*
> 	- [ ] Vertiges/hypotension orthostatique *(Diarrhée chronique par malabsorption)*
> 	- [ ] Pli cutané persistant *(Déshydratation)*
> 	- [ ] Muqueuses sèches *(Déshydratation)*
> 	- [ ] Oligurie *(Déshydratation)*
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
> - [ ] **23. Antécédents familiaux pertinents *(Diarrhée chronique par malabsorption · Déshydratation)***
> 	- [ ] Maladies préexistantes *(Diarrhée chronique par malabsorption)*
> 	- [ ] Diabète *(Diarrhée chronique par malabsorption)*
> 	- [ ] Chirurgies abdominales *(Diarrhée chronique par malabsorption)*
> 	- [ ] Pathologie thyroïdienne *(Diarrhée chronique par malabsorption)*
> 	- [ ] Radiothérapie abdominale *(Diarrhée chronique par malabsorption)*
> - [ ] **24. Médicaments et allergies *(Diarrhée chronique par malabsorption)***
> 	- [ ] Médicaments actuels
> 	- [ ] Antibiotiques récents
> 	- [ ] Laxatifs
> 	- [ ] Autres médicaments pertinents
> 	- [ ] Allergies
> - [ ] **25. Contexte épidémiologique *(Diarrhée chronique par malabsorption)***
> 	- [ ] Restauration collective
> 	- [ ] Consommation de viande crue
> 	- [ ] Eau non potable
> 	- [ ] Entourage affecté
> 	- [ ] Voyages récents
> - [ ] **26. Contexte social et professionnel *(Diarrhée chronique par malabsorption)***
> - [ ] **27. Bilan des entrées et sorties *(Déshydratation)***
> 	- [ ] Quantité de boissons ingérées
> 	- [ ] Fréquence et volume des urines
> 	- [ ] Présence de larmes lors des pleurs
> - [ ] **28. État neurologique *(Déshydratation)***
> 	- [ ] Confusion
> 	- [ ] Somnolence
> 	- [ ] Sopor
> - [ ] **29. Recherche de causes infectieuses *(Déshydratation)***
> 	- [ ] Signes d'infection urinaire
> 	- [ ] Fièvre associée
> 	- [ ] Environnement épidémique
> - [ ] **30. Recherche de causes métaboliques - Diabète sucré *(Déshydratation)***
> 	- [ ] Polyurie-polydipsie
> 	- [ ] Perte de poids récente
> 	- [ ] Antécédents familiaux de diabète
> - [ ] **31. Recherche de causes endocriniennes - Insuffisance surrénalienne *(Déshydratation)***
> 	- [ ] Asthénie chronique
> 	- [ ] Hypotension
> 	- [ ] Hyperpigmentation cutanée
> - [ ] **32. Habitudes alimentaires et hydratation habituelle *(Déshydratation)***
> - [ ] **33. Toxiques et médicaments *(Déshydratation)***
> 	- [ ] Diurétiques
> 	- [ ] Laxatifs
> 	- [ ] Autres médicaments
> - [ ] **34. Anamnèse de l'entourage *(Déshydratation)***
> 	- [ ] Cas similaires dans l'entourage
> 	- [ ] Voyage récent
> 	- [ ] Consommation d'aliments suspects
> - [ ] **35. Anamnèse sociale *(Déshydratation)***
> 	- [ ] Conditions de vie
> 	- [ ] Autonomie (personne âgée)
> 	- [ ] Garde d'enfant/crèche
> - [ ] **36. Caractérisation de la plainte principale *(1 grille sur 5)***
> 	- [ ] Localisation de la douleur
> 	- [ ] Type de douleur
> 	- [ ] Intensité
> 	- [ ] Durée et fréquence
> 	- [ ] Facteurs aggravants
> - [ ] **37. Retentissement fonctionnel *(1 grille sur 5)***
> 	- [ ] Impact socioprofessionnel
> 	- [ ] Isolement social
> 	- [ ] Adaptation comportementale
> - [ ] **38. Antécédents et facteurs de risque *(1 grille sur 5)***
> 	- [ ] Voyage récent
> 	- [ ] Relations sexuelles non protégées
> 	- [ ] Consommation d'aliments à risque
> 	- [ ] Tabagisme
> 	- [ ] Médicaments gastrotoxiques
> - [ ] **39. Anamnèse systémique *(1 grille sur 5)***
> 	- [ ] Pas de symptômes urinaires
> 	- [ ] Pas de douleurs articulaires
> 	- [ ] Pas d'atteinte cutanée
> 	- [ ] Pas d'atteinte oculaire
> 	- [ ] Pas de notion de contage
> - [ ] **40. Anamnèse médicale et chirurgicale *(1 grille sur 5)***
> 	- [ ] Reflux gastro-œsophagien
> 	- [ ] Lombalgies chroniques
> 	- [ ] Appendicectomie
> 	- [ ] Cure de tunnel carpien
> - [ ] **41. Caractérisation de la modification du transit *(Cancer colorectal)***
> 	- [ ] Évolution générale
> 	- [ ] Nombre de selles par 24h
> 	- [ ] Modification récente du transit
> 	- [ ] Selles noires déféquées
> 	- [ ] Selles nauséabondes
> - [ ] **42. Éléments anormaux dans les selles *(Cancer colorectal)***
> 	- [ ] Glaires
> 	- [ ] Pus
> 	- [ ] Sang noir
> 	- [ ] Sang rouge
> 	- [ ] Graisses
> 	- [ ] Aliments non digérés
> - [ ] **43. Retentissement général *(Cancer colorectal)***
> 	- [ ] Asthénie
> 	- [ ] Perte de poids
> 	- [ ] Anorexie
> 	- [ ] Fièvre
> 	- [ ] Sueurs nocturnes
> 	- [ ] Altération de l'état général
> - [ ] **44. Facteurs favorisants et antécédents *(Cancer colorectal)***
> 	- [ ] Alimentation récente
> 	- [ ] Voyage récent
> 	- [ ] Prise médicamenteuse
> 	- [ ] Stress psychosocial
> 	- [ ] Antécédents familiaux de cancer colorectal
> 	- [ ] Antécédents personnels de polypes
> 	- [ ] Maladies inflammatoires intestinales

> [!tip] 🩺 Status
> - [ ] **1. Mesures d'hygiène *(1 grille sur 5)***
> 	- [ ] Lavage des mains
> 	- [ ] Respect de la pudeur avec drap
> - [ ] **2. Examen tête et cou *(1 grille sur 5)***
> 	- [ ] Inspection des conjonctives
> 	- [ ] Examen des pupilles
> 	- [ ] Inspection de l'oropharynx
> - [ ] **3. Examen cardiovasculaire *(1 grille sur 5)***
> - [ ] **4. Examen pulmonaire *(1 grille sur 5)***
> - [ ] **5. Examen abdominal *(Diarrhée chronique par malabsorption · MICI (Crohn / RCUH))***
> 	- [ ] Inspection de l'abdomen *(MICI (Crohn / RCUH))*
> 	- [ ] Auscultation de l'abdomen *(1 grille sur 5)*
> 	- [ ] Percussion de l'abdomen *(1 grille sur 5)*
> 	- [ ] Palpation de l'abdomen *(1 grille sur 5)*
> 	- [ ] Inspection (distension, cicatrices) *(Diarrhée chronique par malabsorption)*
> 	- [ ] Auscultation (bruits hydroaériques) *(Diarrhée chronique par malabsorption)*
> 	- [ ] Palpation (masses, douleur, défense) *(Diarrhée chronique par malabsorption)*
> 	- [ ] Percussion (matité, tympanisme) *(Diarrhée chronique par malabsorption)*
> 	- [ ] Auscultation des bruits intestinaux *(1 grille sur 5)*
> 	- [ ] Palpation des 4 quadrants *(1 grille sur 5)*
> 	- [ ] Recherche de défense ou détente *(1 grille sur 5)*
> 	- [ ] Recherche de masses *(1 grille sur 5)*
> - [ ] **6. Examen cutané *(1 grille sur 5)***
> - [ ] **7. Évaluation clinique de l'état d'hydratation *(Diarrhée chronique par malabsorption · Déshydratation)***
> 	- [ ] Turgor cutané *(Diarrhée chronique par malabsorption)*
> 	- [ ] État des muqueuses *(Diarrhée chronique par malabsorption)*
> 	- [ ] Pli cutané (temps de recoloration) *(Déshydratation)*
> 	- [ ] État des muqueuses (sèches/humides) *(Déshydratation)*
> 	- [ ] Yeux enfoncés *(Déshydratation)*
> 	- [ ] Fontanelle déprimée (nourrisson) *(Déshydratation)*
> - [ ] **8. Recherche de signes cutanés *(Diarrhée chronique par malabsorption)***
> 	- [ ] Érythème noueux
> 	- [ ] Pyoderma gangrenosum
> 	- [ ] Autres manifestations extra-intestinales
> - [ ] **9. Toucher rectal *(3 grilles sur 5)***
> 	- [ ] Tonus sphinctérien *(Cancer colorectal · Diarrhée chronique par malabsorption)*
> 	- [ ] Présence de sang *(Diarrhée chronique par malabsorption)*
> 	- [ ] Masses rectales palpables *(Cancer colorectal · Diarrhée chronique par malabsorption)*
> 	- [ ] Fécalome *(Diarrhée chronique par malabsorption)*
> 	- [ ] Inspection de la marge anale *(1 grille sur 5)*
> 	- [ ] Recherche de sang frais *(1 grille sur 5)*
> 	- [ ] Évaluation du tonus sphinctérien *(1 grille sur 5)*
> 	- [ ] Palpation rectale *(1 grille sur 5)*
> 	- [ ] Position genu-pectorale ou décubitus latéral *(Cancer colorectal)*
> 	- [ ] Ampoule rectale *(Cancer colorectal)*
> 	- [ ] Sang au doigtier *(Cancer colorectal)*
> 	- [ ] Douleur provoquée *(Cancer colorectal)*
> - [ ] **10. Examen thyroïdien *(Diarrhée chronique par malabsorption)***
> 	- [ ] Palpation de la thyroïde
> 	- [ ] Recherche de nodules
> - [ ] **11. Auscultation cardiopulmonaire *(Cancer colorectal · Diarrhée chronique par malabsorption)***
> 	- [ ] Patience *(Cancer colorectal)*
> 	- [ ] Fréquence des bruits *(Cancer colorectal)*
> 	- [ ] Tonalité *(Cancer colorectal)*
> 	- [ ] Silence abdominal *(Cancer colorectal)*
> 	- [ ] Hyperactivité *(Cancer colorectal)*
> - [ ] **12. Palpation superficielle *(Cancer colorectal · Déshydratation)***
> 	- [ ] Globe vésical *(Déshydratation)*
> 	- [ ] Douleur sus-pubienne *(Déshydratation)*
> 	- [ ] Main à plat, doigts serrés *(Cancer colorectal)*
> 	- [ ] Tonus pariétal spontané et en réponse *(Cancer colorectal)*
> 	- [ ] Douleur localisée *(Cancer colorectal)*
> 	- [ ] Défense ou contracture *(Cancer colorectal)*
> 	- [ ] Extension *(Cancer colorectal)*
> 	- [ ] Douleur à l'ébranlement *(Cancer colorectal)*
> - [ ] **13. Examen rénal *(Déshydratation)***
> 	- [ ] Palpation des fosses lombaires
> 	- [ ] Recherche de douleur à l'ébranlement
> - [ ] **14. Mesure de la tension artérielle *(Déshydratation)***
> 	- [ ] Recherche d'hypotension orthostatique
> - [ ] **15. Évaluation de l'état général *(Déshydratation)***
> 	- [ ] Poids actuel (si possible)
> 	- [ ] État de conscience
> 	- [ ] Température
> - [ ] **16. Signes vitaux et état général *(1 grille sur 5)***
> 	- [ ] Prise des signes vitaux
> 	- [ ] Évaluation de l'état général
> 	- [ ] Recherche de signes de déshydratation
> - [ ] **17. Recherche de complications *(1 grille sur 5)***
> 	- [ ] Signes de péritonite
> 	- [ ] Signes de mégacôlon toxique
> 	- [ ] État hémodynamique
> - [ ] **18. Recherche de manifestations extra-intestinales *(1 grille sur 5)***
> 	- [ ] Examen cutané
> 	- [ ] Examen articulaire
> 	- [ ] Examen oculaire si indiqué
> - [ ] **19. Inspection générale *(Cancer colorectal)***
> 	- [ ] Ambiance générale
> 	- [ ] Faciès
> 	- [ ] Pâleur cutanéo-muqueuse
> 	- [ ] Ictère
> 	- [ ] État d'hydratation
> 	- [ ] Signes de carences
> - [ ] **20. Signes vitaux *(Cancer colorectal)***
> 	- [ ] Pulsations, tension artérielle
> 	- [ ] Rythme et amplitude respiratoires
> 	- [ ] Température
> 	- [ ] Poids actuel et évolution
> - [ ] **21. Inspection abdominale *(Cancer colorectal)***
> 	- [ ] Morphologie
> 	- [ ] Symétrie vs asymétrie
> 	- [ ] Cicatrices
> 	- [ ] Hernies
> 	- [ ] Veines superficielles
> 	- [ ] Mouvements respiratoires
> - [ ] **22. Percussion abdominale *(Cancer colorectal)***
> 	- [ ] Patient allongé
> 	- [ ] Tympanisme
> 	- [ ] Distension gazeuse
> 	- [ ] Matité
> 	- [ ] Mesure de la taille du foie, de la rate
> - [ ] **23. Palpation profonde *(Cancer colorectal)***
> 	- [ ] Recherche masse abdominale
> 	- [ ] Mobilité de la masse
> 	- [ ] Pulsations
> 	- [ ] Aorte
> 	- [ ] Taille des organes
> 	- [ ] Points douloureux spécifiques
> - [ ] **24. Palpation spécifique du côlon *(Cancer colorectal)***
> 	- [ ] Cadre colique
> 	- [ ] Sigmoïde
> 	- [ ] Cordon induré douloureux
> 	- [ ] Masses palpables
> 	- [ ] Sensibilité à la palpation

> [!success] 💊 Management — partagé par plusieurs diagnostics
> - [ ] **1. Évoque les diagnostics différentiels pertinents *(2 grilles sur 5)* — *Diarrhée chronique par malabsorption · Déshydratation***
> - [ ] **2. Propose une prise en charge thérapeutique adaptée *(2 grilles sur 5)* — *Diarrhée chronique par malabsorption · Déshydratation***

> [!success] 💊 Management — si Cancer colorectal
> - [ ] **1. Propose les examens complémentaires de première intention**
> 	- [ ] FSC: recherche anémie ferriprive (saignement chronique)
> 	- [ ] Ferritine, fer sérique, transferrine
> 	- [ ] CRP, VS: syndrome inflammatoire
> 	- [ ] Ionogramme, urée, créatinine: déshydratation
> 	- [ ] Bilan hépatique: pathologie associée
> 	- [ ] TSH: dysthyroïdie cause de troubles du transit
> 	- [ ] Albumine: dénutrition, malabsorption
> - [ ] **2. Examens d'imagerie et endoscopie**
> 	- [ ] ASP debout face et profil: niveaux hydro-aériques si occlusion
> 	- [ ] CT abdomino-pelvien avec injection: bilan d'extension si tumeur
> 	- [ ] Coloscopie totale: examen de référence pour la pathologie colique
> 	- [ ] Visualisation directe des lésions
> 	- [ ] Biopsies multiples
> 	- [ ] Polypectomie thérapeutique
> 	- [ ] Gastroscopie si méléna: recherche saignement haut
> 	- [ ] Entéro-IRM ou vidéocapsule si suspicion grêle
> - [ ] **3. Diagnostics différentiels des troubles du transit**
> - [ ] **4. Signes d'alarme (Red Flags)**
> 	- [ ] Méléna
> 	- [ ] Modification récente du transit après 50 ans
> 	- [ ] Occlusion intestinale
> 	- [ ] Perte de poids inexpliquée
> 	- [ ] Anémie ferriprive
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

> [!success] 💊 Management — si Déshydratation
> - [ ] **1. Énonce le diagnostic principal**
> 	- [ ] Déshydratation aiguë
> - [ ] **2. Propose les examens complémentaires spécifiques**
> 	- [ ] Ionogramme sanguin (Na, K, Cl)
> 	- [ ] Fonction rénale (créatinine, urée)
> 	- [ ] FSC (hémoconcentration : Hb, Ht)
> 	- [ ] Glycémie
> 	- [ ] Analyse d'urine si suspicion d'infection
> - [ ] **3. Organise le suivi et reconnaît les complications**
> 	- [ ] Critères d'hospitalisation définis
> 	- [ ] Transfert à l'hôpital si nécessaire
> 	- [ ] Surveillance de la réhydratation
> 	- [ ] Éducation des parents/soignants

> [!success] 💊 Management — si Diarrhée chronique par malabsorption
> - [ ] **1. Propose les examens complémentaires de première intention**
> 	- [ ] Biologie : FSC, CRP, ionogramme (Na, K, Ca)
> 	- [ ] Fonction rénale : créatinine, urée
> 	- [ ] Fonction hépatique : transaminases, GGT, phosphatases alcalines (PAL), albumine
> 	- [ ] Bilan de coagulation : TP/INR, TCA
> 	- [ ] Fonction thyroïdienne : TSH
> - [ ] **2. Énonce le diagnostic principal**
> 	- [ ] Insuffisance pancréatique exocrine (sur pancréatites chroniques)
> - [ ] **3. Propose les examens complémentaires spécifiques**
> 	- [ ] Élastase fécale (insuffisance pancréatique)
> 	- [ ] Calprotectine fécale (inflammation intestinale)
> 	- [ ] Coproculture et recherche de parasites
> 	- [ ] US abdominal ou CT abdominal
> 	- [ ] Coloscopie avec biopsies
> - [ ] **4. Organise le suivi et reconnaît les complications**
> 	- [ ] Surveillance de l'état nutritionnel
> 	- [ ] Dépistage du cancer colorectal si indiqué
> 	- [ ] Orientation spécialisée si nécessaire (gastro-entérologie)
> 	- [ ] Hospitalisation si déshydratation sévère

> [!success] 💊 Management — si Diarrhée du voyageur
> *Aucune grille du corpus ne documente ce diagnostic* — il est pourtant attendu de cette SSP. **Trou de révision à combler ailleurs.**

> [!success] 💊 Management — si MICI (Crohn / RCUH)
> - [ ] **1. Hypothèse diagnostique principale**
> 	- [ ] Rectocolite ulcéro-hémorragique (RCUH) *(1 grille sur 2)*
> 	- [ ] Justification basée sur les symptômes *(1 grille sur 2)*
> 	- [ ] Explication adaptée à la patiente *(1 grille sur 2)*
> - [ ] **2. Propose les examens complémentaires de première intention**
> 	- [ ] Examen rectal *(1 grille sur 2)*
> 	- [ ] Recherche de sang occulte dans les selles *(1 grille sur 2)*
> 	- [ ] FSC, électrolytes *(1 grille sur 2)*
> 	- [ ] VS, CRP *(1 grille sur 2)*
> 	- [ ] Bilan biologique (FSC, CRP, électrolytes, fonction rénale) *(1 grille sur 2)*
> 	- [ ] Cultures de selles et parasitologie *(1 grille sur 2)*
> 	- [ ] Calprotectine fécale *(1 grille sur 2)*
> 	- [ ] Colonoscopie avec biopsies *(1 grille sur 2)*
> - [ ] **3. Examens microbiologiques *(1 grille sur 2)***
> 	- [ ] Coproculture; microscopie des selles pour œufs et parasites
> - [ ] **4. Examens d'imagerie et endoscopie *(1 grille sur 2)***
> 	- [ ] US abdominale
> 	- [ ] Radiographie abdominale simple
> 	- [ ] Coloscopie
> - [ ] **5. Communication avec la patiente**
> 	- [ ] Explications au patient des impressions diagnostiques préliminaires *(1 grille sur 2)*
> 	- [ ] Explication du plan de prise en charge *(1 grille sur 2)*
> 	- [ ] Utilisation d'un langage non médical et clarification des termes médicaux *(1 grille sur 2)*
> 	- [ ] Évaluation de l'accord du patient avec le plan diagnostique *(1 grille sur 2)*
> 	- [ ] Recherche des préoccupations et questions du patient *(1 grille sur 2)*
> 	- [ ] Réponse à la question sur le cancer *(1 grille sur 2)*
> 	- [ ] Explication du caractère chronique de la maladie *(1 grille sur 2)*
> 	- [ ] Rassurance sur les options thérapeutiques *(1 grille sur 2)*
> 	- [ ] Information sur les groupes de soutien *(1 grille sur 2)*
> - [ ] **6. Conseil et prévention *(1 grille sur 2)***
> 	- [ ] Conseil sur l'arrêt du tabac
> 	- [ ] Réaction appropriée au défi concernant le travail
> 	- [ ] Discussion sur l'importance du dépistage familial (cancer colorectal)
> - [ ] **7. Diagnostics différentiels évoqués *(1 grille sur 2)***
> 	- [ ] Maladie de Crohn
> 	- [ ] Colite infectieuse (bactérienne, parasitaire)
> 	- [ ] Colite médicamenteuse (AINS)
> 	- [ ] Carcinome colorectal
> - [ ] **8. Prise en charge immédiate *(1 grille sur 2)***
> 	- [ ] Critères d'hospitalisation évalués
> 	- [ ] Réhydratation IV
> 	- [ ] Corticothérapie IV si colite sévère
> 	- [ ] Arrêt des AINS
> - [ ] **9. Plan de suivi *(1 grille sur 2)***
> 	- [ ] Consultation gastro-entérologie
> 	- [ ] Surveillance des complications
> 	- [ ] Protocole de dépistage du cancer colorectal
> 	- [ ] Soutien psychologique
