---
aliases:
  - "Mémento Chute & Évaluation Gériatrique"
type: memento-ecos-ssp
ssp: "Chute & Évaluation Gériatrique"
specialite: "Musculo-Squelettique"
cas: 5
diagnostics: 5
attendus_documentes_ailleurs: 4
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

# Chute & Évaluation Gériatrique ⭐️

*Musculo-Squelettique · 5 grilles · 5 diagnostics documentés · 4 attendus documentés ailleurs · 1 attendu absent du corpus* — [[SSP — Chute & Évaluation Gériatrique]]

> [!abstract] Les 5 grilles fusionnées
> - **AMBOSS-24** — Violence domestique `dd-principal` · [grille](<file:///Users/damienfulliquet/Developer/GitHub/grilles-ecos/cases/amboss/AMBOSS-24_-_E_valuation_apre_s_chute_-_Femme_30_ans_-_Grille_ECOS.html>)
> - **AZYGOS-4** — HypoTA orthostatique `confirme` · [grille](<file:///Users/damienfulliquet/Developer/GitHub/grilles-ecos/docs/azygos-grilles/a8012490-bf2d-48f1-85c0-35662fd010b5.json>)
> - **German-10** — Accident vasculaire cérébral `corrige` · [grille](<file:///Users/damienfulliquet/Developer/GitHub/grilles-ecos/cases/german/German-10_-_Chute_-_Grille_ECOS.html>)
> - **German-11** — Chute multifactorielle `corrige` · [grille](<file:///Users/damienfulliquet/Developer/GitHub/grilles-ecos/cases/german/German-11_-_Chute_-_Grille_ECOS.html>)
> - **RESCOS-11** — Fracture du membre supérieur (humérus, tête radiale) `confirme` · [grille](<file:///Users/damienfulliquet/Developer/GitHub/grilles-ecos/cases/rescos/RESCOS-11_-_Chute_-_Grille_ECOS.html>)

> [!note] 📋 Anamnèse
> - [ ] **1. Motif principal *(Fracture du membre supérieur (humérus, tête radiale) · Violence domestique)***
> - [ ] **2. Caractérisation du traumatisme *(Violence domestique)***
> 	- [ ] Début/moment de l'événement
> 	- [ ] Événements précipitants/mécanisme de la chute
> 	- [ ] Perte de connaissance
> 	- [ ] Progression
> 	- [ ] Épisodes antérieurs
> 	- [ ] Fréquence
> 	- [ ] Facteurs améliorants
> 	- [ ] Facteurs aggravants
> 	- [ ] Symptômes associés
> - [ ] **3. Recherche de symptômes spécifiques *(Violence domestique)***
> 	- [ ] Céphalées
> 	- [ ] Nausées/vomissements
> 	- [ ] Fièvre/frissons
> 	- [ ] Sueurs nocturnes
> 	- [ ] Fatigue
> 	- [ ] Éruption cutanée/changements cutanés
> 	- [ ] Douleurs articulaires
> 	- [ ] Problèmes urinaires
> 	- [ ] Problèmes intestinaux
> 	- [ ] Problèmes de sommeil
> 	- [ ] Appétit
> 	- [ ] Variations pondérales
> 	- [ ] Vertiges
> - [ ] **4. Antécédents hémorragiques *(Violence domestique)***
> 	- [ ] Saignements accrus après blessures mineures
> 	- [ ] Saignements accrus pendant l'accouchement
> 	- [ ] Saignements accrus pendant les règles
> 	- [ ] Saignements de nez
> 	- [ ] Saignements des gencives après brossage
> 	- [ ] Saignements dans muscles, articulations ou tissus profonds
> - [ ] **5. Antécédents médicaux *(4 diagnostics)***
> 	- [ ] AVC antérieurs *(Accident vasculaire cérébral)*
> 	- [ ] Autres pathologies *(Accident vasculaire cérébral)*
> 	- [ ] Diabète *(Chute multifactorielle)*
> 	- [ ] Gonarthrose bilatérale *(Chute multifactorielle)*
> 	- [ ] Hypertension artérielle *(Chute multifactorielle)*
> 	- [ ] Problème cardiaque *(Chute multifactorielle)*
> - [ ] **6. Allergies *(Chute multifactorielle · Violence domestique)***
> - [ ] **7. Médicaments *(4 diagnostics)***
> - [ ] **8. Hospitalisations et antécédents chirurgicaux *(Violence domestique)***
> 	- [ ] Hospitalisations
> 	- [ ] Antécédents chirurgicaux
> - [ ] **9. Antécédents familiaux *(Accident vasculaire cérébral · Chute multifactorielle · Violence domestique)***
> 	- [ ] AVC *(Accident vasculaire cérébral)*
> 	- [ ] Maladies cardiaques *(Accident vasculaire cérébral)*
> 	- [ ] Hypertension *(Accident vasculaire cérébral)*
> 	- [ ] Diabète *(Accident vasculaire cérébral)*
> - [ ] **10. Habitudes et mode de vie *(Violence domestique)***
> 	- [ ] Travail
> 	- [ ] Domicile
> 	- [ ] Alcool
> 	- [ ] Drogues récréatives
> 	- [ ] Tabac
> - [ ] **11. Histoire spécifique de violence domestique *(Violence domestique)***
> 	- [ ] Relation avec le conjoint
> 	- [ ] Peur pour sa sécurité/celle des enfants
> 	- [ ] Arme à feu à la maison
> 	- [ ] Plan d'urgence
> 	- [ ] Système de soutien
> 	- [ ] Consommation alcool/drogues du conjoint
> 	- [ ] Dépression
> 	- [ ] Régularité des abus
> - [ ] **12. Déroulement de la chute *(HypoTA orthostatique)***
> - [ ] **13. Vertiges *(HypoTA orthostatique)***
> - [ ] **14. Perte de connaissance *(Chute multifactorielle · HypoTA orthostatique)***
> - [ ] **15. Symptômes cardiaques *(HypoTA orthostatique)***
> - [ ] **16. Impact crânien *(HypoTA orthostatique)***
> - [ ] **17. Aide après la chute *(HypoTA orthostatique)***
> - [ ] **18. Chutes antérieures *(HypoTA orthostatique)***
> - [ ] **19. Peur de chuter *(HypoTA orthostatique)***
> - [ ] **20. Mobilité et habitat *(HypoTA orthostatique)***
> - [ ] **21. Aides techniques *(HypoTA orthostatique)***
> - [ ] **22. Distance de marche *(HypoTA orthostatique)***
> - [ ] **23. Situation de logement *(HypoTA orthostatique)***
> - [ ] **24. Escaliers *(HypoTA orthostatique)***
> - [ ] **25. Seuils *(HypoTA orthostatique)***
> - [ ] **26. BADL *(HypoTA orthostatique)***
> - [ ] **27. Transferts *(HypoTA orthostatique)***
> - [ ] **28. Toilette et douche *(HypoTA orthostatique)***
> - [ ] **29. Habillage *(HypoTA orthostatique)***
> - [ ] **30. Aller aux toilettes *(HypoTA orthostatique)***
> - [ ] **31. Alimentation *(HypoTA orthostatique)***
> - [ ] **32. IADL *(HypoTA orthostatique)***
> - [ ] **33. Courses *(HypoTA orthostatique)***
> - [ ] **34. Cuisine *(HypoTA orthostatique)***
> - [ ] **35. Ménage *(HypoTA orthostatique)***
> - [ ] **36. Finances *(HypoTA orthostatique)***
> - [ ] **37. Transports *(HypoTA orthostatique)***
> - [ ] **38. Rendez-vous *(HypoTA orthostatique)***
> - [ ] **39. Anamnèse sociale *(Accident vasculaire cérébral · Chute multifactorielle · HypoTA orthostatique)***
> - [ ] **40. État civil *(HypoTA orthostatique)***
> - [ ] **41. Profession *(HypoTA orthostatique)***
> - [ ] **42. Loisirs *(HypoTA orthostatique)***
> - [ ] **43. Proches *(HypoTA orthostatique)***
> - [ ] **44. Cognition, psychisme et sommeil *(HypoTA orthostatique)***
> - [ ] **45. Cognition *(HypoTA orthostatique)***
> - [ ] **46. Humeur *(HypoTA orthostatique)***
> - [ ] **47. Sommeil *(HypoTA orthostatique)***
> - [ ] **48. Nutrition, poids et appareil locomoteur *(HypoTA orthostatique)***
> - [ ] **49. Nutrition *(HypoTA orthostatique)***
> - [ ] **50. Évolution pondérale *(HypoTA orthostatique)***
> - [ ] **51. Douleurs articulaires et squelettiques *(HypoTA orthostatique)***
> - [ ] **52. Élimination et continence *(HypoTA orthostatique)***
> - [ ] **53. Selles *(HypoTA orthostatique)***
> - [ ] **54. Miction *(HypoTA orthostatique)***
> - [ ] **55. Continence *(HypoTA orthostatique)***
> - [ ] **56. Vertiges et sensorialité *(HypoTA orthostatique)***
> - [ ] **57. Vision *(Accident vasculaire cérébral · Chute multifactorielle · HypoTA orthostatique)***
> - [ ] **58. Audition *(Accident vasculaire cérébral · HypoTA orthostatique)***
> - [ ] **59. Présentation avec nom, fonction et tâche *(Accident vasculaire cérébral · Chute multifactorielle)***
> - [ ] **60. Moment de l'événement *(Accident vasculaire cérébral)***
> - [ ] **61. Dernier moment où la patiente était normale *(Accident vasculaire cérébral)***
> - [ ] **62. Circonstances de la chute *(Accident vasculaire cérébral)***
> - [ ] **63. Force musculaire *(Accident vasculaire cérébral)***
> - [ ] **64. Sensibilité *(Accident vasculaire cérébral)***
> - [ ] **65. Motricité fine *(Accident vasculaire cérébral)***
> - [ ] **66. Langage *(Accident vasculaire cérébral)***
> - [ ] **67. Toxiques *(Accident vasculaire cérébral · Chute multifactorielle)***
> - [ ] **68. Facteurs de risque cardiovasculaire *(Accident vasculaire cérébral)***
> 	- [ ] Hypertension
> 	- [ ] Hyperlipidémie
> - [ ] **69. Activités sportives, loisirs *(Accident vasculaire cérébral)***
> - [ ] **70. Événement *(Chute multifactorielle)***
> - [ ] **71. Temporalité *(Chute multifactorielle)***
> - [ ] **72. Premier épisode *(Chute multifactorielle)***
> - [ ] **73. Douleurs *(Chute multifactorielle)***
> - [ ] **74. Fièvre *(Chute multifactorielle)***
> - [ ] **75. Sensation de malaise *(Chute multifactorielle)***
> - [ ] **76. Autres symptômes *(Chute multifactorielle)***
> 	- [ ] Faiblesse
> 	- [ ] Troubles sensitifs
> 	- [ ] Céphalées
> 	- [ ] Vertiges
> 	- [ ] Palpitations
> 	- [ ] Dyspnée
> - [ ] **77. Médicaments actuels *(Chute multifactorielle)***
> 	- [ ] Tramadol
> 	- [ ] Somnifère
> 	- [ ] Sulfonylurée
> 	- [ ] Aspirine
> - [ ] **78. Maladies récentes/Hospitalisations *(Chute multifactorielle)***
> - [ ] **79. Habitudes alimentaires *(Chute multifactorielle)***
> - [ ] **80. Condition physique *(Chute multifactorielle)***
> - [ ] **81. Mécanisme du traumatisme *(Fracture du membre supérieur (humérus, tête radiale))***
> 	- [ ] Circonstance
> 	- [ ] Énergie
> 	- [ ] Position lors de la réception
> 	- [ ] Autres blessures que coude
> - [ ] **82. Caractérisation de la douleur *(Fracture du membre supérieur (humérus, tête radiale))***
> 	- [ ] Localisation
> 	- [ ] Intensité
> 	- [ ] Qualité
> 	- [ ] Évolution
> 	- [ ] Irradiation
> 	- [ ] Facteurs atténuants/aggravants
> - [ ] **83. Présence de symptômes neuro-vasculaires associés au trauma *(Fracture du membre supérieur (humérus, tête radiale))***
> 	- [ ] Impotence
> 	- [ ] Symptômes neuro-vasculaires
> - [ ] **84. Antécédents chirurgicaux *(Fracture du membre supérieur (humérus, tête radiale))***
> - [ ] **85. Santé actuelle *(Fracture du membre supérieur (humérus, tête radiale))***
> 	- [ ] Maladies actuelles
> 	- [ ] Médicaments
> 	- [ ] Allergies
> - [ ] **86. Impact du traumatisme sur le quotidien de la patiente *(Fracture du membre supérieur (humérus, tête radiale))***
> 	- [ ] Membre dominant
> 	- [ ] Activités quotidiennes affectées

> [!tip] 🩺 Status
> - [ ] **1. Mesures d'hygiène *(Violence domestique)***
> 	- [ ] Lavage des mains
> 	- [ ] Respect de la pudeur avec drap
> - [ ] **2. Vérification corporelle complète *(Violence domestique)***
> - [ ] **3. Examen de la tête, yeux, oreilles, nez et gorge *(Violence domestique)***
> 	- [ ] Inspection de la tête
> 	- [ ] Palpation de la tête
> 	- [ ] Inspection des conjonctives
> 	- [ ] Inspection des sclères
> 	- [ ] Examen des pupilles
> 	- [ ] Examen des muscles oculomoteurs
> - [ ] **4. Examen des extrémités *(Violence domestique)***
> 	- [ ] Inspection des membres supérieurs
> 	- [ ] Inspection des mains
> 	- [ ] Inspection des membres inférieurs
> - [ ] **5. Examen cutané *(Violence domestique)***
> - [ ] **6. MMS *(HypoTA orthostatique)***
> - [ ] **7. Nerfs crâniens *(Accident vasculaire cérébral · HypoTA orthostatique)***
> - [ ] **8. Acuité visuelle *(HypoTA orthostatique)***
> - [ ] **9. Audition *(HypoTA orthostatique)***
> - [ ] **10. Motricité *(HypoTA orthostatique)***
> - [ ] **11. Sensibilité *(HypoTA orthostatique)***
> - [ ] **12. Épreuve des bras tendus *(HypoTA orthostatique)***
> - [ ] **13. Doigt-nez *(HypoTA orthostatique)***
> - [ ] **14. Diadococinésie *(HypoTA orthostatique)***
> - [ ] **15. Vibrations *(HypoTA orthostatique)***
> - [ ] **16. Auscultation cardiaque *(HypoTA orthostatique)***
> - [ ] **17. Auscultation pulmonaire *(HypoTA orthostatique)***
> - [ ] **18. Veines jugulaires *(HypoTA orthostatique)***
> - [ ] **19. Recherche d’œdèmes *(HypoTA orthostatique)***
> - [ ] **20. TA couché-debout (Schellong) *(HypoTA orthostatique)***
> - [ ] **21. Pouls radial *(HypoTA orthostatique)***
> - [ ] **22. Pouls des pieds *(HypoTA orthostatique)***
> - [ ] **23. Voie orale *(HypoTA orthostatique)***
> - [ ] **24. Inspection *(HypoTA orthostatique)***
> - [ ] **25. Auscultation *(Accident vasculaire cérébral · HypoTA orthostatique)***
> 	- [ ] Auscultation cardiaque *(Accident vasculaire cérébral)*
> 	- [ ] Auscultation des carotides *(Accident vasculaire cérébral)*
> - [ ] **26. Palpation *(HypoTA orthostatique)***
> - [ ] **27. Redressement *(HypoTA orthostatique)***
> - [ ] **28. Transfert *(HypoTA orthostatique)***
> - [ ] **29. Station debout *(HypoTA orthostatique)***
> - [ ] **30. Analyse de la marche *(HypoTA orthostatique)***
> - [ ] **31. Orientation et état de conscience *(Accident vasculaire cérébral)***
> - [ ] **32. Examen de la marche *(Accident vasculaire cérébral)***
> 	- [ ] Marche en tandem
> - [ ] **33. Tests de coordination *(Accident vasculaire cérébral)***
> 	- [ ] Test de Romberg
> 	- [ ] Test d'Unterberger
> 	- [ ] Diadococinésie
> 	- [ ] Test de préhension des bras
> 	- [ ] Épreuve doigt-nez
> 	- [ ] Épreuve talon-genou
> - [ ] **34. Examen moteur *(Accident vasculaire cérébral)***
> - [ ] **35. Examen sensitif *(Accident vasculaire cérébral)***
> - [ ] **36. Recherche d'apraxie *(Accident vasculaire cérébral)***
> - [ ] **37. Réflexes *(Accident vasculaire cérébral)***
> 	- [ ] Réflexes ostéo-tendineux
> 	- [ ] Signe de Babinski
> - [ ] **38. Signes méningés *(Accident vasculaire cérébral)***
> - [ ] **39. Status cardiaque et pulmonaire *(Chute multifactorielle)***
> - [ ] **40. Neurostatus *(Chute multifactorielle)***
> 	- [ ] Ataxie
> 	- [ ] Tests cérébelleux
> 	- [ ] Sensibilité
> 	- [ ] Motricité
> - [ ] **41. Test de vision *(Chute multifactorielle)***
> - [ ] **42. Observation avec comparaison des deux membres supérieurs *(Fracture du membre supérieur (humérus, tête radiale))***
> - [ ] **43. Palpation des deux membres supérieurs *(Fracture du membre supérieur (humérus, tête radiale))***
> 	- [ ] Coudes
> 	- [ ] Bras et épaules
> 	- [ ] Avant-bras et poignets
> - [ ] **44. Perfusion distale des 2 membres supérieurs, avec comparaison *(Fracture du membre supérieur (humérus, tête radiale))***
> 	- [ ] Pouls périphériques
> 	- [ ] Temps de recoloration ou gradient thermique
> - [ ] **45. Sensibilité sur les terrains des nerfs *(Fracture du membre supérieur (humérus, tête radiale))***
> 	- [ ] Radial
> 	- [ ] Médian
> 	- [ ] Ulnaire
> - [ ] **46. Motricité sur les terrains des nerfs *(Fracture du membre supérieur (humérus, tête radiale))***
> 	- [ ] Radial
> 	- [ ] Médian
> 	- [ ] Ulnaire

> [!success] 💊 Management — si Accident vasculaire cérébral
> - [ ] **1. Diagnostic de suspicion**
> - [ ] **2. Diagnostics différentiels**
> - [ ] **3. Examens diagnostiques**
> 	- [ ] Laboratoire
> 	- [ ] ECG
> 	- [ ] Imagerie cérébrale / CT
> - [ ] **4. Traitement d'urgence**
> 	- [ ] Position allongée
> 	- [ ] Oxygénothérapie
> 	- [ ] Thrombolyse
> 	- [ ] Contrôle glycémique
> 	- [ ] Ne pas trop abaisser la tension artérielle
> - [ ] **5. Information du neurologue**

> [!success] 💊 Management — si Chute multifactorielle
> - [ ] **1. Examens complémentaires**
> 	- [ ] ECG
> 	- [ ] Radiographie thoracique
> - [ ] **2. Diagnostics différentiels - Chute chez patient âgé**
> - [ ] **3. Examens de laboratoire**
> 	- [ ] FSC
> 	- [ ] Marqueurs inflammatoires
> 	- [ ] Vitamine B12
> 	- [ ] Glycémie
> - [ ] **4. Bilan urinaire**
> - [ ] **5. Imagerie cérébrale**
> - [ ] **6. Échographie des carotides**

> [!success] 💊 Management — si Fracture du bassin (hémorragique)
> *Aucune grille de cette SSP ne documente ce diagnostic* — mais le corpus le documente ailleurs : [[Mémento — AVP (Accident de la Voie Publique)]] (2 grilles).

> [!success] 💊 Management — si Fracture du membre supérieur (humérus, tête radiale)
> - [ ] **1. Demande une radiographie du coude gauche avec les incidences**
> 	- [ ] Face
> 	- [ ] Profil
> - [ ] **2. Demande un examen CT-scan ou l'a évoqué dans la suite de la prise en charge**
> - [ ] **3. Évalue le risque de grossesse avant de proposer des examens radiologiques**
> - [ ] **4. Analyse de la radiographie, identifie**
> 	- [ ] Luxation
> 	- [ ] Fracture de la tête radiale
> 	- [ ] Fracture du processus coronoïde
> - [ ] **5. Propose une antalgie**
> - [ ] **6. Prise en charge immédiate**
> 	- [ ] Référer au spécialiste
> 	- [ ] Immobilisation du membre
> - [ ] **7. Évoque une possible prise en charge chirurgicale**

> [!success] 💊 Management — si Fracture du scaphoïde
> *Aucune grille de cette SSP ne documente ce diagnostic* — mais le corpus le documente ailleurs : [[Mémento — Douleur au Poignet]] (1 grille).

> [!success] 💊 Management — si Hématome sous-dural
> *Aucune grille du corpus ne documente ce diagnostic* — il est pourtant attendu de cette SSP. **Trou de révision à combler ailleurs.**

> [!success] 💊 Management — si Hémorragie sous-arachnoïdienne
> *Aucune grille de cette SSP ne documente ce diagnostic* — mais le corpus le documente ailleurs : [[Mémento — Céphalée]] (1 grille).

> [!success] 💊 Management — si HypoTA orthostatique
> *La ou les grilles de ce diagnostic ne cotent aucun item de management* — elles s'arrêtent à l'anamnèse et au status.

> [!success] 💊 Management — si Pneumothorax
> *Aucune grille de cette SSP ne documente ce diagnostic* — mais le corpus le documente ailleurs : [[Mémento — Douleur Thoracique]] (3 grilles).

> [!success] 💊 Management — si Violence domestique
> - [ ] **1. Hypothèses diagnostiques**
> - [ ] **2. Examens complémentaires**
> 	- [ ] FSC
> 	- [ ] Frottis sanguin périphérique
> 	- [ ] Temps de saignement, TP, TCA
> - [ ] **3. Tests spécifiques maladie de von Willebrand**
> 	- [ ] Dosage de l'activité du facteur VIII
> 	- [ ] Dosage de l'antigène du facteur von Willebrand
> 	- [ ] Dosage du cofacteur de la ristocétine
> - [ ] **4. Communication avec la patiente**
> 	- [ ] Explications à la patiente des impressions diagnostiques préliminaires
> 	- [ ] Explication du plan de prise en charge
> 	- [ ] Utilisation d'un langage non médical et clarification des termes médicaux
> 	- [ ] Évaluation de l'accord de la patiente avec le plan diagnostique
> 	- [ ] Recherche des préoccupations et questions de la patiente
> 	- [ ] Ne pas répéter les manœuvres douloureuses pendant l'examen physique
> - [ ] **5. Conseil et soutien**
> 	- [ ] Conseil sur les options de soutien pour la violence domestique
> 	- [ ] Réaction appropriée au défi
> 	- [ ] Approche empathique et non-jugeante
> 	- [ ] Information sur la confidentialité
> 	- [ ] Évaluation du plan de sécurité
> 	- [ ] Documentation appropriée
