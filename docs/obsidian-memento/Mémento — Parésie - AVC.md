---
aliases:
  - "Mémento Parésie - AVC"
type: memento-ecos-ssp
ssp: "Parésie - AVC"
specialite: "Neurologie"
cas: 4
diagnostics: 3
attendus_documentes_ailleurs: 0
attendus_absents_du_corpus: 1
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

> [!warning] Mémento mixte — 1 grille officielle, 3 non officielles
> **RESCOS-70b** fait partie des **neuf grilles officielles** et fait donc
> autorité ; elle est signalée ⭐️ dans l'encadré ci-dessous. Les 3
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

# Parésie - AVC ⭐️

*Neurologie · 4 grilles · 3 diagnostics documentés · 1 attendu absent du corpus* — [[SSP — Parésie - AVC]]

> [!abstract] Les 4 grilles fusionnées
> - **RESCOS-52** — AIT `explicite` · [grille](<file:///Users/damienfulliquet/Developer/GitHub/grilles-ecos/cases/rescos/RESCOS-52%20-%20Paralysie%20-%20Grille%20ECOS.html>)
> - **RESCOS-53** — AVC `premier-dd` · [grille](<file:///Users/damienfulliquet/Developer/GitHub/grilles-ecos/cases/rescos/RESCOS-53%20-%20Parésie%20facio-brachiale%20-%20ECC%20Neurologie%20-%20Grille%20ECOS.html>)
> - **RESCOS-70** — Paralysie de Bell `dd-principal` · [grille](<file:///Users/damienfulliquet/Developer/GitHub/grilles-ecos/cases/rescos/RESCOS-70%20-%20Paralysie%20faciale%20-%20Grille%20ECOS.html>)
> - **RESCOS-70b** ⭐️ **officielle** — Paralysie de Bell `explicite` · [grille](<file:///Users/damienfulliquet/Developer/GitHub/grilles-ecos/cases/rescos/RESCOS-70b%20-%20Paralysie%20faciale%20-%20Grille%20ECOS.html>)

> [!note] 📋 Anamnèse
> - [ ] **1. Paralysie *(AIT)***
> 	- [ ] Localisation
> 	- [ ] Circonstance de survenue
> 	- [ ] Développement
> 	- [ ] Chronologie/résolution
> - [ ] **2. Anamnèse actuelle par système - neurologique *(AIT)***
> 	- [ ] Perte de force
> 	- [ ] Perte de sensibilité
> 	- [ ] Céphalées
> 	- [ ] Vertiges
> 	- [ ] Troubles visuels
> 	- [ ] Troubles auditifs
> - [ ] **3. Présence de douleurs *(AIT)***
> 	- [ ] Pas de douleur associée aux symptômes neurologiques
> - [ ] **4. Épisodes similaires par le passé *(2 grilles sur 4)***
> 	- [ ] Premier épisode, jamais eu de symptômes similaires *(AIT)*
> - [ ] **5. Antécédents médicaux et comorbidités *(AIT)***
> 	- [ ] Maladies
> 	- [ ] Hospitalisations
> 	- [ ] Opérations
> - [ ] **6. Médicaments *(AIT)***
> 	- [ ] Amlodipine 5mg 1x/jour pour hypertension
> 	- [ ] Pas d'autre médicament, pas d'allergie
> - [ ] **7. Habitudes *(AIT)***
> 	- [ ] Tabac
> 	- [ ] Alcool
> 	- [ ] Drogues
> - [ ] **8. Antécédents familiaux *(AIT)***
> 	- [ ] Père décédé d'une tumeur cérébrale il y a 2 ans
> 	- [ ] Très inquiet d'avoir la même chose que son père
> - [ ] **9. Caractérisation de l'épisode neurologique aigu *(AVC)***
> 	- [ ] Mode d'installation
> 	- [ ] Heure précise de début
> 	- [ ] Circonstances de découverte
> 	- [ ] Évolution depuis le début
> 	- [ ] Premiers symptômes remarqués
> - [ ] **10. Analyse sémiologique détaillée *(AVC)***
> 	- [ ] Troubles moteurs
> 	- [ ] Troubles de la parole
> 	- [ ] Troubles sensitifs associés
> 	- [ ] Troubles visuels
> 	- [ ] Autres déficits neurologiques
> - [ ] **11. Recherche de facteurs de risque cardiovasculaire *(AVC)***
> 	- [ ] Hypertension artérielle
> 	- [ ] Diabète
> 	- [ ] Hypercholestérolémie
> 	- [ ] Tabagisme
> 	- [ ] Fibrillation auriculaire
> - [ ] **12. Antécédents neurologiques et vasculaires *(AVC)***
> 	- [ ] AVC ou AIT antérieurs
> 	- [ ] Pathologies carotidiennes
> 	- [ ] Cardiopathies emboligènes
> 	- [ ] Maladies hémorragiques
> 	- [ ] Traumatismes crâniens récents
> - [ ] **13. Médicaments et traitements en cours *(AVC)***
> 	- [ ] Anticoagulants
> 	- [ ] Antiagrégants plaquettaires
> 	- [ ] Antihypertenseurs
> 	- [ ] Antidiabétiques
> 	- [ ] Autres traitements
> - [ ] **14. Signes fonctionnels associés et état antérieur *(AVC)***
> 	- [ ] Céphalées
> 	- [ ] Nausées, vomissements
> 	- [ ] Troubles de la conscience
> 	- [ ] État fonctionnel antérieur
> 	- [ ] Qualité de vie et projet thérapeutique
> - [ ] **15. Caractérisation du déficit facial *(1 grille sur 4)***
> 	- [ ] Début
> 	- [ ] Mode d'installation
> 	- [ ] Évolution depuis le début
> 	- [ ] Latéralité
> 	- [ ] Territoires atteints (front, œil, bouche)
> - [ ] **16. Douleur rétro-auriculaire *(1 grille sur 4)***
> 	- [ ] Présence de la douleur
> 	- [ ] Antériorité par rapport au déficit
> - [ ] **17. Symptômes oculaires *(1 grille sur 4)***
> 	- [ ] Occlusion palpébrale incomplète
> 	- [ ] Sécheresse / sensation de grain de sable
> 	- [ ] Larmoiement
> 	- [ ] Acuité visuelle et douleur oculaire
> - [ ] **18. Signes d'atteinte du nerf facial en amont *(1 grille sur 4)***
> 	- [ ] Hyperacousie
> 	- [ ] Trouble du goût
> - [ ] **19. Dépistage des signes d'atteinte centrale *(1 grille sur 4)***
> 	- [ ] Déficit moteur ou sensitif d'un membre
> 	- [ ] Trouble du langage
> 	- [ ] Diplopie
> 	- [ ] Trouble de l'équilibre ou de la marche
> 	- [ ] Céphalée inhabituelle ou perte de connaissance
> - [ ] **20. Dépistage d'un syndrome de Ramsay-Hunt *(1 grille sur 4)***
> 	- [ ] Vésicules du pavillon ou du conduit auditif
> 	- [ ] Otalgie ou otorrhée
> 	- [ ] Baisse d'audition
> 	- [ ] Vertige rotatoire
> - [ ] **21. Dépistage d'une borréliose de Lyme *(1 grille sur 4)***
> 	- [ ] Morsure de tique
> 	- [ ] Érythème migrant
> 	- [ ] Exposition (forêt, randonnée)
> - [ ] **22. Terrain et facteurs de risque *(1 grille sur 4)***
> 	- [ ] Diabète ou hypertension artérielle
> 	- [ ] Immunosuppression, VIH, IST
> 	- [ ] Épisode similaire antérieur
> - [ ] **23. Anamnèse générale, antécédents et habitudes *(1 grille sur 4)***
> 	- [ ] État fébrile récent · Traitements et allergies · Alcool, tabac, drogues · Antécédents familiaux
> - [ ] **24. Explore les préoccupations et représentations *(1 grille sur 4)***
> - [ ] **25. Caractérisation de l'épisode *(1 grille sur 4)***
> 	- [ ] Circonstances de survenue
> 	- [ ] Localisation
> 	- [ ] Type de symptômes
> 	- [ ] Symptômes associés
> - [ ] **26. Précise si les symptômes touchent TOUTE l'hémiface (front compris) ou seulement une partie *(1 grille sur 4)***
> - [ ] **27. Chronologie *(1 grille sur 4)***
> 	- [ ] Cinétique d'installation
> 	- [ ] Durée / évolution
> 	- [ ] Réponse aux symptômes (ce qui a été fait)
> - [ ] **28. Recherche d'un état fébrile avant ou après l'épisode *(1 grille sur 4)***
> - [ ] **29. Recherche des signes d'alerte neurologiques (exclusion atteinte centrale) *(1 grille sur 4)***
> 	- [ ] Déficit d'un membre
> 	- [ ] Trouble du langage
> 	- [ ] Diplopie
> 	- [ ] Trouble de la marche / équilibre
> 	- [ ] Céphalée inhabituelle
> - [ ] **30. Évalue le risque de complication oculaire par défaut de fermeture palpébrale *(1 grille sur 4)***
> 	- [ ] Recherche de symptômes oculaires (larmoiement, sécheresse, rougeur, douleur)
> 	- [ ] Intention de protéger l'œil
> - [ ] **31. État de santé *(1 grille sur 4)***
> 	- [ ] Maladies actuelles
> 	- [ ] Antécédents médico-chirurgicaux
> 	- [ ] Médicaments
> - [ ] **32. Investigue les facteurs de risque / causes possibles *(1 grille sur 4)***
> 	- [ ] Herpès Zoster
> 	- [ ] Maladie de Lyme
> 	- [ ] IST (VIH, syphilis)
> 	- [ ] Diabète ou autre maladie systémique

> [!tip] 🩺 Status
> - [ ] **1. État de vigilance - orientation *(AIT)***
> 	- [ ] Spatiale
> 	- [ ] Temporelle
> 	- [ ] Sur sa personne
> - [ ] **2. Motricité des membres supérieurs *(AIT)***
> 	- [ ] Flexion
> 	- [ ] Extension
> 	- [ ] Abduction
> - [ ] **3. Sensibilité des membres supérieurs - évalue globalement la sensibilité sur tous les dermatomes *(AIT)***
> - [ ] **4. Réflexes ostéo-tendineux des membres supérieurs *(AIT)***
> 	- [ ] Réflexe bicipital des deux côtés
> 	- [ ] Réflexe stylo-radial des deux côtés
> 	- [ ] Réflexe tricipital des deux côtés
> - [ ] **5. Motricité des membres inférieurs *(AIT)***
> 	- [ ] Abduction
> 	- [ ] Adduction
> 	- [ ] Flexion
> 	- [ ] Extension
> - [ ] **6. Sensibilité des membres inférieurs - évalue globalement la sensibilité sur tous les dermatomes *(AIT)***
> - [ ] **7. Réflexes ostéo-tendineux des membres inférieurs (des deux côtés) *(AIT)***
> 	- [ ] Rotulien
> 	- [ ] Achilléen
> - [ ] **8. Réflexe cutané plantaire (Babinski) des deux côtés *(AIT)***
> - [ ] **9. Évaluation de l'état de conscience et fonctions supérieures *(AVC)***
> 	- [ ] Score de Glasgow
> 	- [ ] Orientation temporo-spatiale
> 	- [ ] Attention et concentration
> 	- [ ] Langage
> 	- [ ] Reconnaissance visuelle et négligence
> - [ ] **10. Examen des nerfs crâniens *(AVC)***
> 	- [ ] Nerf facial (VII)
> 	- [ ] Nerfs oculomoteurs (III, IV, VI)
> 	- [ ] Nerf trijumeau (V)
> 	- [ ] Nerfs bulbaires (IX, X, XII)
> 	- [ ] Champ visuel
> - [ ] **11. Examen de la motricité *(AVC)***
> 	- [ ] Testing musculaire analytique
> 	- [ ] Manœuvre de Barré
> 	- [ ] Tonus musculaire
> 	- [ ] Réflexes ostéotendineux
> 	- [ ] Réflexes cutanés
> - [ ] **12. Examen de la sensibilité *(AVC)***
> 	- [ ] Sensibilité tactile superficielle
> 	- [ ] Sensibilité douloureuse
> 	- [ ] Sensibilité proprioceptive
> 	- [ ] Sensibilité vibratoire
> 	- [ ] Discrimination tactile
> - [ ] **13. Examen de la coordination et équilibre *(AVC)***
> 	- [ ] Épreuves index-nez et talon-genou
> 	- [ ] Mouvements alternés rapides
> 	- [ ] Station debout
> 	- [ ] Marche et demi-tour
> 	- [ ] Dystonie, mouvements anormaux
> - [ ] **14. Recherche de signes méningés et d'HTIC *(AVC)***
> 	- [ ] Raideur de nuque
> 	- [ ] Signes de Kernig et Brudzinski
> 	- [ ] Photophobie et phonophobie
> 	- [ ] Œdème papillaire
> 	- [ ] Signes végétatifs
> - [ ] **15. Examen cardiovasculaire orienté *(AVC)***
> 	- [ ] Auscultation cardiaque
> 	- [ ] Auscultation carotidienne
> 	- [ ] Pouls périphériques
> 	- [ ] Signes d'insuffisance cardiaque
> - [ ] **16. Inspection du visage au repos *(1 grille sur 4)***
> - [ ] **17. Testing du territoire facial supérieur *(1 grille sur 4)***
> 	- [ ] Plisser le front · Lever les sourcils · Fermer les yeux avec force
> - [ ] **18. Occlusion palpébrale et signe de Charles Bell *(1 grille sur 4)***
> - [ ] **19. Testing du territoire facial inférieur *(1 grille sur 4)***
> 	- [ ] Sourire / montrer les dents
> 	- [ ] Gonfler les joues
> 	- [ ] Plisser les lèvres (siffler)
> - [ ] **20. Examen des autres paires crâniennes *(1 grille sur 4)***
> 	- [ ] II — acuité visuelle et champ visuel par confrontation
> 	- [ ] III, IV, VI — oculomotricité et réflexe photomoteur
> 	- [ ] V — sensibilité faciale et masséters
> 	- [ ] VIII à XII — audition, voile, déglutition, langue
> - [ ] **21. Examen ophtalmologique ciblé *(1 grille sur 4)***
> 	- [ ] Acuité visuelle
> 	- [ ] Inspection de la cornée et de la conjonctive
> 	- [ ] Réflexe cornéen
> 	- [ ] Recherche de kératite (fluorescéine)
> - [ ] **22. Otoscopie et inspection du pavillon *(1 grille sur 4)***
> - [ ] **23. Palpation de la loge parotidienne et des aires ganglionnaires *(1 grille sur 4)***
> - [ ] **24. Examen neurologique des membres et de la coordination *(1 grille sur 4)***
> 	- [ ] Force segmentaire des quatre membres
> 	- [ ] Sensibilité
> 	- [ ] Coordination et marche
> - [ ] **25. Paramètres vitaux et état général *(1 grille sur 4)***
> - [ ] **26. Envisage examen de l'acuité visuelle *(1 grille sur 4)***
> - [ ] **27. Inspection des paupières et de la fermeture palpébrale (lagophtalmie, signe de Charles Bell) *(1 grille sur 4)***
> - [ ] **28. Inspection de la conjonctive et de la cornée (signes d'exposition : rougeur, sécheresse) et évaluation du larmoiement *(1 grille sur 4)***
> 	- [ ] Inspection de la conjonctive et de la cornée
> 	- [ ] Évaluation du larmoiement
> - [ ] **29. Réaction pupillaire *(1 grille sur 4)***
> - [ ] **30. Champs visuels par confrontation *(1 grille sur 4)***
> - [ ] **31. Motilité oculaire (6 directions) *(1 grille sur 4)***
> 	- [ ] Horizontal
> 	- [ ] Vertical
> - [ ] **32. Fond d'œil à l'ophtalmoscope (intention) *(1 grille sur 4)***
> - [ ] **33. Réflexe cornéen (intention) *(1 grille sur 4)***
> - [ ] **34. Sensibilité des territoires du V DES DEUX CÔTÉS *(1 grille sur 4)***
> 	- [ ] Front
> 	- [ ] Joues
> 	- [ ] Mandibules
> - [ ] **35. NC VII — inspection du visage (recherche d'asymétrie) *(1 grille sur 4)***
> - [ ] **36. NC VII — motilité des sourcils *(1 grille sur 4)***
> 	- [ ] Lever les sourcils
> 	- [ ] Froncer les sourcils
> - [ ] **37. NC VII — yeux *(1 grille sur 4)***
> 	- [ ] Fermer fortement
> 	- [ ] Ouverture contre résistance
> - [ ] **38. NC VII — bouche *(1 grille sur 4)***
> 	- [ ] Découvrir les dents / sourire
> 	- [ ] Gonfler les joues
> - [ ] **39. Envisage de tester la force ou les réflexes aux extrémités (exclusion atteinte centrale) *(1 grille sur 4)***
> - [ ] **40. Envisage de tester la sensibilité aux extrémités *(1 grille sur 4)***

> [!success] 💊 Management — si AIT
> - [ ] **1. Évoque le diagnostic principal d'accident ischémique transitoire (AIT)**
> - [ ] **2. Évoque un diagnostic différentiel cohérent**
> 	- [ ] AVC ischémique
> 	- [ ] Saignement intracrânien
> 	- [ ] Abus d'alcool/drogues/médicaments
> 	- [ ] Vasoconstriction cérébrale
> 	- [ ] Syndrome psychiatrique (trouble de conversion)
> - [ ] **3. Propose des examens complémentaires appropriés**
> 	- [ ] IRM cérébrale (examen de référence)
> 	- [ ] CT scan cérébral
> 	- [ ] Bilan sanguin complet
> 	- [ ] ECG
> 	- [ ] Échographie carotidienne
> - [ ] **4. Évoque la nécessité d'une prise en charge urgente**
> 	- [ ] AIT doit être traité avec autant d'importance qu'un AVC
> 	- [ ] Hospitalisation pour bilan et surveillance
> - [ ] **5. Rassure le patient concernant l'inquiétude liée au père**
> 	- [ ] Explique que tumeur cérébrale très peu probable avec apparition aussi brusque
> 	- [ ] Différencie AIT des tumeurs cérébrales

> [!success] 💊 Management — si AVC
> - [ ] **1. Diagnostic topographique et syndromique**
> 	- [ ] Syndrome facio-brachial droit
> 	- [ ] Localisation : territoire sylvien superficiel gauche
> 	- [ ] Différenciation centrale vs périphérique
> 	- [ ] Évaluation sévérité
> - [ ] **2. Diagnostic étiologique - AVC ischémique vs hémorragique**
> - [ ] **3. Urgence thérapeutique - thrombolyse**
> 	- [ ] Fenêtre thérapeutique
> 	- [ ] Critères d'inclusion thrombolyse
> 	- [ ] Critères d'exclusion
> 	- [ ] Score NIHSS et évaluation bénéfice/risque
> - [ ] **4. Examens complémentaires en urgence**
> 	- [ ] CT cérébral sans contraste
> 	- [ ] Bilan biologique
> 	- [ ] ECG
> 	- [ ] IRM cérébrale avec diffusion
> - [ ] **5. Prise en charge aiguë et surveillance**
> 	- [ ] Monitoring neurologique
> 	- [ ] Surveillance cardiorespiratoire
> 	- [ ] Position demi-assise
> 	- [ ] Contrôle glycémique
> 	- [ ] Contrôle tensionnel
> - [ ] **6. Recherche étiologique de l'AVC ischémique**
> 	- [ ] Écho-Doppler des troncs supra-aortiques
> 	- [ ] Échocardiographie
> 	- [ ] Holter ECG
> 	- [ ] Bilan thrombophilie si sujet jeune
> - [ ] **7. Prévention secondaire**
> 	- [ ] Antiagrégation plaquettaire
> 	- [ ] Statine
> 	- [ ] Contrôle facteurs de risque
> 	- [ ] Rééducation précoce
> - [ ] **8. Pronostic et planification de sortie**
> 	- [ ] Évaluation fonctionnelle
> 	- [ ] Orientation
> 	- [ ] Information famille
> 	- [ ] Suivi spécialisé

> [!success] 💊 Management — si Paralysie de Bell
> - [ ] **1. Présentation du cas *(1 grille sur 2)***
> 	- [ ] Synthétique
> 	- [ ] Éléments pertinents de l'anamnèse et du status
> - [ ] **2. Hypothèse diagnostique**
> 	- [ ] Paralysie de Bell *(1 grille sur 2)*
> 	- [ ] AVC *(1 grille sur 2)*
> 	- [ ] Ramsay-Hunt *(1 grille sur 2)*
> 	- [ ] Lyme *(1 grille sur 2)*
> 	- [ ] Cause otologique / parotidienne *(1 grille sur 2)*
> - [ ] **3. Argumente le caractère périphérique *(1 grille sur 2)***
> - [ ] **4. Diagnostics différentiels et argumentation *(1 grille sur 2)***
> - [ ] **5. Examens complémentaires *(1 grille sur 2)***
> 	- [ ] Sérologie de Lyme selon l'exposition
> 	- [ ] Sérologies VIH et syphilis selon l'anamnèse
> 	- [ ] Glycémie
> 	- [ ] Pas d'imagerie en urgence si le tableau est typique
> - [ ] **6. Traitement *(1 grille sur 2)***
> 	- [ ] Corticothérapie précoce (dans les 72 h)
> 	- [ ] Antiviral seulement si suspicion de zona ou forme sévère
> 	- [ ] Antalgie
> - [ ] **7. Protection oculaire *(1 grille sur 2)***
> 	- [ ] Larmes artificielles la journée
> 	- [ ] Pommade et occlusion palpébrale nocturne
> 	- [ ] Consigne de consulter en urgence si douleur, rougeur ou baisse de vue
> - [ ] **8. Information, pronostic et suivi *(1 grille sur 2)***
> - [ ] **9. Reconnaît une paralysie faciale PÉRIPHÉRIQUE et la distingue d'une atteinte centrale (atteinte du front) *(1 grille sur 2)***
> - [ ] **10. Propose la paralysie de Bell comme hypothèse principale (diagnostic clinique d'exclusion) *(1 grille sur 2)***
> - [ ] **11. Reconnaît qu'aucune imagerie / laboratoire de routine n'est nécessaire dans la forme typique (examens ciblés seulement si atypie) *(1 grille sur 2)***
> - [ ] **12. Corticothérapie orale précoce (moins de 72 h) *(1 grille sur 2)***
> - [ ] **13. Protection oculaire (larmes artificielles / occlusion nocturne) pour prévenir la kératite d'exposition *(1 grille sur 2)***

> [!success] 💊 Management — si Sclérose en plaques
> *Aucune grille du corpus ne documente ce diagnostic* — il est pourtant attendu de cette SSP. **Trou de révision à combler ailleurs.**
