---
aliases:
  - "Mémento Céphalée"
type: memento-ecos-ssp
ssp: "Céphalée"
specialite: "Neurologie"
cas: 6
diagnostics: 6
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

# Céphalée ⭐️

*Neurologie · 6 grilles · 6 diagnostics distincts* — [[SSP — Céphalée]]

> [!abstract] Les 6 grilles fusionnées
> - **AMBOSS-26** — Crise migraineuse `premier-dd` · [grille](<file:///Users/damienfulliquet/Developer/GitHub/grilles-ecos/cases/amboss/AMBOSS-26_-_Ce_phale_e_-_Homme_29_ans_-_Grille_ECOS.html>)
> - **AMBOSS-33** — Hémorragie sous-arachnoïdienne `premier-dd` · [grille](<file:///Users/damienfulliquet/Developer/GitHub/grilles-ecos/cases/amboss/AMBOSS-33_-_Ce_phale_e_-_Femme_55_ans_-_Grille_ECOS.html>)
> - **AZYGOS-3** — Migraine `diagnostic-travail` · [grille](<file:///Users/damienfulliquet/Developer/GitHub/grilles-ecos/.azygos-extraction/74108006-36f7-4056-8383-2346f553295e.json>)
> - **German-8** — Céphalée du restaurant chinois `corrige` · [grille](<file:///Users/damienfulliquet/Developer/GitHub/grilles-ecos/cases/german/German-8_-_Ce_phale_es_-_Grille_ECOS.html>)
> - **German-9** — Méningite `corrige` · [grille](<file:///Users/damienfulliquet/Developer/GitHub/grilles-ecos/cases/german/German-9_-_Ce_phale_es_-_Grille_ECOS.html>)
> - **RESCOS-10** — Thrombose veineuse cérébrale `explicite` · [grille](<file:///Users/damienfulliquet/Developer/GitHub/grilles-ecos/cases/rescos/RESCOS-10_-_Ce_phale_e_-_Grille_ECOS.html>)

> [!note] 📋 Anamnèse
> - [ ] **1. Motif principal *(Crise migraineuse · Hémorragie sous-arachnoïdienne)***
> - [ ] **2. Caractérisation de la céphalée *(Crise migraineuse · Hémorragie sous-arachnoïdienne · Thrombose veineuse cérébrale)***
> 	- [ ] Localisation
> 	- [ ] Intensité (échelle 0-10) *(Crise migraineuse · Hémorragie sous-arachnoïdienne)*
> 	- [ ] Qualité
> 	- [ ] Début
> 	- [ ] Événements précipitants *(Crise migraineuse · Hémorragie sous-arachnoïdienne)*
> 	- [ ] Progression/constant/intermittent *(Crise migraineuse · Hémorragie sous-arachnoïdienne)*
> 	- [ ] Épisodes antérieurs *(Crise migraineuse · Hémorragie sous-arachnoïdienne)*
> 	- [ ] Irradiation *(Crise migraineuse · Hémorragie sous-arachnoïdienne)*
> 	- [ ] Facteurs améliorants *(Crise migraineuse · Hémorragie sous-arachnoïdienne)*
> 	- [ ] Facteurs aggravants *(Crise migraineuse · Hémorragie sous-arachnoïdienne)*
> 	- [ ] Symptômes associés *(Crise migraineuse · Hémorragie sous-arachnoïdienne)*
> 	- [ ] Intensité *(Thrombose veineuse cérébrale)*
> 	- [ ] Évolution *(Thrombose veineuse cérébrale)*
> 	- [ ] Durée *(Thrombose veineuse cérébrale)*
> - [ ] **3. Recherche de symptômes spécifiques *(Crise migraineuse)***
> 	- [ ] Traumatisme
> 	- [ ] Fièvre/frissons
> 	- [ ] Problèmes de sommeil
> 	- [ ] Appétit
> 	- [ ] Infections récentes
> 	- [ ] Vertiges
> 	- [ ] Troubles visuels
> 	- [ ] Difficultés à parler
> 	- [ ] Faiblesse
> 	- [ ] Picotements/engourdissements
> 	- [ ] Humeur
> 	- [ ] Larmoiement
> 	- [ ] Congestion nasale/nez qui coule
> 	- [ ] Agitation
> 	- [ ] Transpiration
> - [ ] **4. Antécédents médicaux *(4 diagnostics)***
> - [ ] **5. Allergies *(5 diagnostics)***
> 	- [ ] Allergies *(Crise migraineuse)*
> 	- [ ] Type de réaction *(Crise migraineuse)*
> - [ ] **6. Médicaments *(5 diagnostics)***
> 	- [ ] Antihypertenseurs *(Céphalée du restaurant chinois)*
> 	- [ ] Antalgiques *(Céphalée du restaurant chinois)*
> - [ ] **7. Hospitalisations et antécédents chirurgicaux *(Crise migraineuse · Hémorragie sous-arachnoïdienne)***
> 	- [ ] Hospitalisations
> 	- [ ] Antécédents chirurgicaux
> - [ ] **8. Antécédents familiaux *(Crise migraineuse · Céphalée du restaurant chinois · Migraine)***
> - [ ] **9. Habitudes et mode de vie *(Crise migraineuse · Hémorragie sous-arachnoïdienne)***
> 	- [ ] Travail
> 	- [ ] Domicile
> 	- [ ] Alcool
> 	- [ ] Drogues récréatives
> 	- [ ] Tabac
> 	- [ ] Exercice
> 	- [ ] Alimentation
> 	- [ ] Quantité avant d'arrêter *(Hémorragie sous-arachnoïdienne)*
> - [ ] **10. Recherche de symptômes spécifiques pour céphalée sévère aiguë *(Hémorragie sous-arachnoïdienne)***
> 	- [ ] Fièvre/frissons
> 	- [ ] Palpitations
> 	- [ ] Éruption cutanée/changements cutanés
> 	- [ ] Douleur thoracique
> 	- [ ] Dyspnée
> 	- [ ] Infections récentes
> 	- [ ] Vertiges
> 	- [ ] Engourdissement
> 	- [ ] Picotements
> 	- [ ] Faiblesse
> 	- [ ] Vision altérée
> 	- [ ] Convulsions
> - [ ] **11. Contacts malades et antécédents familiaux *(Hémorragie sous-arachnoïdienne)***
> 	- [ ] Contacts malades
> 	- [ ] Antécédents familiaux
> - [ ] **12. Question d'ouverture *(Migraine)***
> - [ ] **13. Dimension temporelle *(Migraine)***
> - [ ] **14. Épisode actuel *(Migraine)***
> - [ ] **15. Début *(Migraine)***
> - [ ] **16. Durée des crises *(Migraine)***
> - [ ] **17. Fréquence et évolution *(Migraine)***
> - [ ] **18. Localisation *(Migraine)***
> - [ ] **19. Irradiation *(Céphalée du restaurant chinois · Migraine)***
> - [ ] **20. Qualité *(Migraine)***
> - [ ] **21. Intensité de la douleur *(Céphalée du restaurant chinois · Migraine)***
> - [ ] **22. Facteurs aggravants *(Céphalée du restaurant chinois · Migraine)***
> - [ ] **23. Facteurs soulageants *(Migraine)***
> - [ ] **24. Bilans neurologiques antérieurs *(Migraine)***
> - [ ] **25. Retentissement des symptômes *(Migraine)***
> - [ ] **26. Symptômes associés *(Migraine · Thrombose veineuse cérébrale)***
> 	- [ ] Nausées/vomissements *(Thrombose veineuse cérébrale)*
> 	- [ ] Photophobie/phonophobie *(Thrombose veineuse cérébrale)*
> 	- [ ] Symptômes neurologiques *(Thrombose veineuse cérébrale)*
> 	- [ ] Fièvre *(Thrombose veineuse cérébrale)*
> 	- [ ] Éruption cutanée *(Thrombose veineuse cérébrale)*
> - [ ] **27. Nausées / vomissements *(Migraine)***
> - [ ] **28. Photophobie *(Migraine)***
> - [ ] **29. Phonophobie *(Migraine)***
> - [ ] **30. Symptômes d'aura *(Migraine)***
> - [ ] **31. Symptômes autonomes *(Migraine)***
> - [ ] **32. Anamnèse des déclencheurs *(Migraine)***
> - [ ] **33. Sommeil *(Migraine)***
> - [ ] **34. Stress *(Migraine)***
> - [ ] **35. Menstruation *(Migraine)***
> - [ ] **36. Alimentation / caféine / alcool *(Migraine)***
> - [ ] **37. Signes d'alarme des céphalées *(Migraine)***
> - [ ] **38. Début en coup de tonnerre *(Migraine)***
> - [ ] **39. Céphalée maximale *(Migraine)***
> - [ ] **40. Fièvre *(Céphalée du restaurant chinois · Migraine)***
> - [ ] **41. Raideur de nuque *(Céphalée du restaurant chinois · Migraine)***
> - [ ] **42. Trouble de la conscience *(Migraine)***
> - [ ] **43. Déficit neurologique focal *(Migraine)***
> - [ ] **44. Grossesse *(Migraine)***
> - [ ] **45. Traumatisme *(Céphalée du restaurant chinois · Migraine)***
> - [ ] **46. Abus médicamenteux *(Migraine)***
> - [ ] **47. Dépistage de l'artérite à cellules géantes *(Migraine)***
> - [ ] **48. Diagnostic antérieur de céphalées *(Migraine)***
> - [ ] **49. Antécédents chirurgicaux *(Migraine)***
> - [ ] **50. Désir de grossesse *(Migraine)***
> - [ ] **51. Noxes *(Migraine)***
> - [ ] **52. Tabagisme *(Migraine)***
> - [ ] **53. Drogues *(Migraine)***
> - [ ] **54. Migraine dans la famille *(Migraine)***
> - [ ] **55. Profession *(Migraine)***
> - [ ] **56. Facteurs de stress psychosociaux *(Migraine)***
> - [ ] **57. Situation sociale *(Migraine)***
> - [ ] **58. Présentation avec nom, fonction et tâche *(Céphalée du restaurant chinois · Méningite)***
> - [ ] **59. Question ouverte d'introduction → Symptôme principal *(Céphalée du restaurant chinois)***
> - [ ] **60. Localisation des douleurs *(Céphalée du restaurant chinois)***
> 	- [ ] Unilatérale/bilatérale
> 	- [ ] Tête ou visage
> - [ ] **61. Caractéristiques temporelles *(Céphalée du restaurant chinois)***
> 	- [ ] Début de la douleur
> 	- [ ] Durée
> 	- [ ] Constante/intermittente
> - [ ] **62. Variation dans la journée *(Céphalée du restaurant chinois)***
> - [ ] **63. Caractère de la douleur *(Céphalée du restaurant chinois)***
> - [ ] **64. Facteurs de soulagement *(Céphalée du restaurant chinois)***
> - [ ] **65. Symptômes d'accompagnement *(Céphalée du restaurant chinois · Méningite)***
> 	- [ ] Nausées *(Céphalée du restaurant chinois)*
> 	- [ ] Vomissements *(Céphalée du restaurant chinois)*
> 	- [ ] Photophobie
> 	- [ ] Larmoiement *(Céphalée du restaurant chinois)*
> 	- [ ] Douleurs à la mastication *(Céphalée du restaurant chinois)*
> 	- [ ] Troubles visuels *(Céphalée du restaurant chinois)*
> 	- [ ] Transpiration *(Méningite)*
> 	- [ ] Faiblesse générale *(Méningite)*
> 	- [ ] Confusion légère *(Méningite)*
> - [ ] **66. Première fois ou connu *(Céphalée du restaurant chinois)***
> - [ ] **67. Maladies récentes *(Céphalée du restaurant chinois)***
> - [ ] **68. Crises convulsives *(Céphalée du restaurant chinois)***
> - [ ] **69. Douleurs aux épaules et muscles *(Céphalée du restaurant chinois)***
> - [ ] **70. Stress, consommation de caféine *(Céphalée du restaurant chinois)***
> - [ ] **71. Alimentation *(Céphalée du restaurant chinois)***
> - [ ] **72. Piqûre de tique *(Céphalée du restaurant chinois)***
> - [ ] **73. Antécédents personnels *(Céphalée du restaurant chinois)***
> 	- [ ] Néoplasie
> 	- [ ] Hypertension
> - [ ] **74. Contraceptifs oraux (chez la femme) *(Céphalée du restaurant chinois)***
> - [ ] **75. Toxiques *(Céphalée du restaurant chinois)***
> - [ ] **76. Anamnèse sociale, profession *(Céphalée du restaurant chinois)***
> - [ ] **77. Question d'entrée ouverte → Symptôme principal *(Méningite)***
> - [ ] **78. Caractéristiques des céphalées *(Méningite)***
> 	- [ ] Temporalité
> 	- [ ] Caractère
> 	- [ ] Intensité EVA
> 	- [ ] Facteurs aggravants
> 	- [ ] Facteurs améliorants
> - [ ] **79. Anamnèse personnelle *(Méningite)***
> 	- [ ] Alcool
> 	- [ ] Tabac
> 	- [ ] Drogues
> - [ ] **80. Symptômes B *(Méningite)***
> - [ ] **81. Questions sur infections herpétiques *(Méningite)***
> 	- [ ] Herpès
> 	- [ ] Varicelle-zona (VZV)
> - [ ] **82. Anamnèse familiale *(Méningite)***
> - [ ] **83. Anamnèse sociale *(Méningite)***
> 	- [ ] Vit avec sa femme
> 	- [ ] Visite récente chez les petits-enfants il y a 2 semaines
> - [ ] **84. Drapeaux rouges - céphalée *(Thrombose veineuse cérébrale)***
> 	- [ ] Céphalée nouvelle/différente
> 	- [ ] Céphalée décrite comme la pire
> 	- [ ] Céphalée en coup de tonnerre
> 	- [ ] Céphalée déclenchée par effort/exercice/activité sexuelle
> 	- [ ] Céphalée déclenchée/aggravée par Valsalva ou position
> - [ ] **85. Antécédents neurologiques *(Thrombose veineuse cérébrale)***
> 	- [ ] Migraines chroniques
> 	- [ ] Caractéristiques des migraines habituelles
> 	- [ ] Traitement habituel
> 	- [ ] Efficacité du traitement actuel
> - [ ] **86. Facteurs de risque vasculaire *(Thrombose veineuse cérébrale)***
> 	- [ ] Contraception orale
> 	- [ ] Tabagisme
> 	- [ ] Antécédents familiaux vasculaires
> 	- [ ] HTA/diabète/dyslipidémie
> - [ ] **87. Contexte *(Thrombose veineuse cérébrale)***
> 	- [ ] Grossesse/post-partum
> 	- [ ] Immunosuppression/cancer
> 	- [ ] Traumatisme crânien récent
> 	- [ ] Voyage/contage
> 	- [ ] Vaccins
> - [ ] **88. Anamnèse par système *(Thrombose veineuse cérébrale)***
> 	- [ ] État général
> 	- [ ] Système digestif
> 	- [ ] Système gynécologique
> 	- [ ] État psychique

> [!tip] 🩺 Status
> - [ ] **1. Mesures d'hygiène *(Crise migraineuse · Hémorragie sous-arachnoïdienne)***
> 	- [ ] Lavage des mains
> 	- [ ] Respect de la pudeur avec drap
> - [ ] **2. Examen de la tête, yeux, oreilles, nez et gorge *(Crise migraineuse · Hémorragie sous-arachnoïdienne)***
> 	- [ ] Inspection de la tête
> 	- [ ] Palpation de la tête
> 	- [ ] Inspection des conjonctives *(Crise migraineuse)*
> 	- [ ] Évaluation de l'acuité visuelle (échelle de Snellen) *(Crise migraineuse)*
> 	- [ ] Fond d'œil direct
> - [ ] **3. Examen du cou *(Crise migraineuse)***
> 	- [ ] Inspection du cou
> 	- [ ] Palpation du cou
> - [ ] **4. Examen neurologique *(Crise migraineuse · Hémorragie sous-arachnoïdienne)***
> 	- [ ] Évaluation de l'orientation dans le temps, l'espace et les personnes
> 	- [ ] Examen ciblé des nerfs crâniens
> 	- [ ] Recherche de méningisme *(Crise migraineuse)*
> 	- [ ] Examen ciblé des mouvements passifs et actifs
> 	- [ ] Examen ciblé de la sensibilité
> 	- [ ] Examen ciblé des réflexes ostéo-tendineux
> 	- [ ] Examen ciblé de la marche
> 	- [ ] Test des mouvements alternés rapides
> 	- [ ] Test doigt-nez
> 	- [ ] Signe de Babinski
> 	- [ ] Test de Romberg
> 	- [ ] Évaluation du niveau de conscience *(Hémorragie sous-arachnoïdienne)*
> 	- [ ] Méningisme *(Hémorragie sous-arachnoïdienne)*
> 	- [ ] Signe de Kernig *(Hémorragie sous-arachnoïdienne)*
> 	- [ ] Signe de Brudzinski *(Hémorragie sous-arachnoïdienne)*
> - [ ] **5. Examen cardiovasculaire *(Hémorragie sous-arachnoïdienne)***
> 	- [ ] Auscultation cardiaque
> - [ ] **6. Méningisme *(Céphalée du restaurant chinois · Migraine)***
> - [ ] **7. Pupilles *(Migraine)***
> - [ ] **8. Oculomotricité *(Migraine)***
> - [ ] **9. Mouvements oculaires *(Migraine)***
> - [ ] **10. Acuité visuelle / champ visuel *(Migraine)***
> - [ ] **11. Nerfs crâniens *(Migraine)***
> - [ ] **12. Nerf VII | Facial *(Migraine)***
> - [ ] **13. Nerfs IX-XII | Tronc cérébral *(Migraine)***
> - [ ] **14. Nerf V | Trijumeau *(Migraine)***
> - [ ] **15. Motricité *(Migraine)***
> - [ ] **16. Sensibilité *(Migraine)***
> - [ ] **17. Réflexes *(Migraine)***
> - [ ] **18. Coordination *(Migraine)***
> - [ ] **19. Démarche *(Migraine)***
> - [ ] **20. Tête *(Migraine)***
> - [ ] **21. Examen des sinus *(Migraine)***
> - [ ] **22. Inspection *(Migraine)***
> - [ ] **23. Palpation de la voûte crânienne *(Migraine)***
> - [ ] **24. Colonne cervicale *(Migraine)***
> - [ ] **25. Articulation temporo-mandibulaire *(Migraine)***
> - [ ] **26. Artère temporale *(Migraine)***
> - [ ] **27. Signes vitaux *(Céphalée du restaurant chinois)***
> - [ ] **28. Neurostatus *(Céphalée du restaurant chinois)***
> 	- [ ] Pupilles
> 	- [ ] Fond d'œil
> - [ ] **29. Palpation artère temporale *(Céphalée du restaurant chinois)***
> - [ ] **30. Auscultation cardiaque avec artères carotides *(Céphalée du restaurant chinois)***
> - [ ] **31. Signe de Brudzinski *(Méningite)***
> - [ ] **32. Autres signes méningés *(Méningite)***
> 	- [ ] Signe de Kernig
> 	- [ ] Signe de Lasègue
> - [ ] **33. Neurostatus par ailleurs *(Méningite)***
> - [ ] **34. Examen général *(Thrombose veineuse cérébrale)***
> 	- [ ] État de conscience/niveau attentionnel
> 	- [ ] Signes vitaux
> 	- [ ] Aspect général
> - [ ] **35. Examen neurologique - nerfs crâniens *(Thrombose veineuse cérébrale)***
> 	- [ ] Acuité visuelle
> 	- [ ] Champs visuels
> 	- [ ] Réflexes pupillaires
> 	- [ ] Oculomotricité
> 	- [ ] Sensibilité faciale
> 	- [ ] Motricité faciale
> - [ ] **36. Examen neurologique - voies longues *(Thrombose veineuse cérébrale)***
> 	- [ ] Force motrice 4 membres
> 	- [ ] Sensibilité
> 	- [ ] Réflexes ostéotendineux
> 	- [ ] Réflexe cutané plantaire
> - [ ] **37. Recherche de méningisme *(Thrombose veineuse cérébrale)***
> 	- [ ] Raideur de nuque
> 	- [ ] Signe de Kernig
> 	- [ ] Signe de Brudzinski
> - [ ] **38. Examen vasculaire *(Thrombose veineuse cérébrale)***
> 	- [ ] Palpation artères temporales
> 	- [ ] Auscultation carotidienne
> 	- [ ] Recherche de souffle vasculaire
> - [ ] **39. Autres examens pertinents *(Thrombose veineuse cérébrale)***
> 	- [ ] Fond d'œil/œdème papillaire
> 	- [ ] Démarche et épreuves cérébelleuses
> 	- [ ] Recherche d'un rash cutané

> [!success] 💊 Management — si Algie vasculaire (cluster)
> *Aucune grille du corpus ne documente ce diagnostic* — il est pourtant attendu de cette SSP. **Trou de révision à combler ailleurs.**

> [!success] 💊 Management — si Crise migraineuse
> - [ ] **1. Hypothèses diagnostiques**
> - [ ] **2. Drapeaux rouges à rechercher**
> 	- [ ] Céphalée sévère implacable
> 	- [ ] Fièvre
> 	- [ ] Déficits neurologiques focaux
> 	- [ ] Convulsions
> 	- [ ] Troubles de conscience
> 	- [ ] Signes d'hypertension intracrânienne (ex: perte de connaissance, œdème papillaire)
> 	- [ ] Signes de méningisme
> 	- [ ] Symptômes psychiatriques
> 	- [ ] Douleur oculaire
> - [ ] **3. Prise en charge**
> 	- [ ] Migraine, céphalée de tension et algie vasculaire = diagnostics cliniques basés sur l'histoire et l'examen physique
> 	- [ ] Ne pas faire d'examens diagnostiques sauf si drapeaux rouges présents
> 	- [ ] Proposer au patient de s'allonger et tamiser la lumière
> - [ ] **4. Communication avec le patient**
> 	- [ ] Explications au patient des impressions diagnostiques préliminaires
> 	- [ ] Explication du plan de prise en charge
> 	- [ ] Utilisation d'un langage non médical et clarification des termes médicaux
> 	- [ ] Évaluation de l'accord du patient avec le plan diagnostique
> 	- [ ] Recherche des préoccupations et questions du patient
> - [ ] **5. Conseil et soutien**
> 	- [ ] Conseil sur l'arrêt du tabac
> 	- [ ] Donner l'option de s'allonger et proposer de tamiser la lumière
> 	- [ ] Réaction appropriée au défi concernant l'entretien d'embauche
> 	- [ ] Éducation sur les facteurs déclenchants
> 	- [ ] Conseils hygiène de vie

> [!success] 💊 Management — si Céphalée du restaurant chinois
> - [ ] **1. Diagnostic de suspicion**
> - [ ] **2. Diagnostics différentiels**
> - [ ] **3. Examens diagnostiques**
> 	- [ ] VS (CRP)
> 	- [ ] FSC
> - [ ] **4. CT cérébral**
> - [ ] **5. Traitement/Prise en charge**
> 	- [ ] Si maladie de Horton : corticoïdes et référence
> 	- [ ] Sinon : antalgiques et contrôle

> [!success] 💊 Management — si Hémorragie sous-arachnoïdienne
> - [ ] **1. Hypothèses diagnostiques**
> - [ ] **2. Conseil et soutien**
> 	- [ ] Proposer d'aider la patiente à s'allonger
> 	- [ ] Proposer de diminuer l'éclairage dans la salle d'examen
> 	- [ ] Réaction appropriée au défi concernant le mari
> 	- [ ] Soutien émotionnel face à la gravité
> 	- [ ] Information sur l'urgence de la situation
> - [ ] **3. Examens complémentaires urgents**
> 	- [ ] CT cérébral sans contraste
> 	- [ ] FSC
> 	- [ ] Glucose, électrolytes
> - [ ] **4. Examens complémentaires biologiques et microbiologiques**
> 	- [ ] TP, TCA
> 	- [ ] Hémocultures
> - [ ] **5. Ponction lombaire et imagerie spécialisée**
> 	- [ ] Ponction lombaire avec analyse du LCR
> 	- [ ] Angiographie
> - [ ] **6. Communication avec la patiente**
> 	- [ ] Explications à la patiente des impressions diagnostiques préliminaires
> 	- [ ] Explication du plan de prise en charge
> 	- [ ] Utilisation d'un langage non médical et clarification des termes médicaux
> 	- [ ] Évaluation de l'accord de la patiente avec le plan diagnostique
> 	- [ ] Recherche des préoccupations et questions de la patiente
> 	- [ ] Ne pas répéter les manœuvres douloureuses pendant l'examen physique

> [!success] 💊 Management — si Migraine
> - [ ] **1. Pas d'imagerie**
> - [ ] **2. Diagnostic de travail**
> - [ ] **3. Information sur le diagnostic**
> - [ ] **4. Traitement de la crise par AINS**
> - [ ] **5. Traitement de la crise par triptan**
> - [ ] **6. Mesures non médicamenteuses**
> - [ ] **7. Filet de sécurité**
> - [ ] **8. Journal des migraines**
> - [ ] **9. Conseils sur le mode de vie**
> - [ ] **10. Information sur la contraception**
> - [ ] **11. Contrôle de suivi**
> - [ ] **12. Évaluer l'indication à une prophylaxie**
> - [ ] **13. Orientation vers la neurologie**

> [!success] 💊 Management — si Méningite
> - [ ] **1. Diagnostic de suspicion**
> - [ ] **2. Diagnostics différentiels**
> - [ ] **3. Examens de laboratoire**
> 	- [ ] FSC
> 	- [ ] CRP
> 	- [ ] Électrolytes
> 	- [ ] Glucose
> - [ ] **4. Diagnostic du liquide céphalo-rachidien**
> 	- [ ] Liquide clair
> 	- [ ] Lymphocytose
> 	- [ ] Glucose normale
> 	- [ ] Protéines
> 	- [ ] Lactate
> - [ ] **5. Traitement**

> [!success] 💊 Management — si Prééclampsie
> *Aucune grille du corpus ne documente ce diagnostic* — il est pourtant attendu de cette SSP. **Trou de révision à combler ailleurs.**

> [!success] 💊 Management — si Thrombose veineuse cérébrale
> - [ ] **1. Diagnostics différentiels**
> 	- [ ] AVC ischémique/hémorragique
> 	- [ ] Migraine avec aura
> 	- [ ] Méningite/encéphalite
> 	- [ ] Hémorragie sous-arachnoïdienne
> 	- [ ] Dissection artérielle
> 	- [ ] Hypertension intracrânienne
> - [ ] **2. Hypothèse diagnostique principale**
> 	- [ ] Thrombose veineuse cérébrale
> - [ ] **3. Examens complémentaires - laboratoire**
> 	- [ ] FSC, CRP/VS
> 	- [ ] Coagulation (TP, PTT)
> 	- [ ] D-dimères
> 	- [ ] Fonction rénale, ionogramme
> 	- [ ] Test de grossesse si doute
> - [ ] **4. Examens complémentaires - imagerie**
> 	- [ ] CT cérébral en urgence
> 	- [ ] CT avec temps veineux/angio-CT
> 	- [ ] IRM cérébrale si disponible
> 	- [ ] Veinographie par résonance magnétique
> - [ ] **5. Prise en charge immédiate**
> 	- [ ] Voie veineuse périphérique
> 	- [ ] Analgésie adaptée
> 	- [ ] Antiémétiques si nécessaire
> 	- [ ] Surveillance neurologique
> - [ ] **6. Traitement spécifique si thrombose confirmée**
> 	- [ ] Anticoagulation par HBPM dose thérapeutique
> 	- [ ] Même si lésion hémorragique
> 	- [ ] Hospitalisation
> 	- [ ] Arrêt contraception orale
> - [ ] **7. Réponse aux demandes de la patiente**
> 	- [ ] Certificat médical pour examen
> 	- [ ] Explication du diagnostic suspecté
> 	- [ ] Rassurer sur la prise en charge
