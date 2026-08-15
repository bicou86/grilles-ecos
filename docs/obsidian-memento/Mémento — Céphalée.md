---
aliases:
  - "Mémento Céphalée"
type: memento-ecos-ssp
ssp: "Céphalée"
specialite: "Neurologie"
cas: 6
diagnostics: 5
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

# Céphalée ⭐️

*Neurologie · 6 grilles · 5 diagnostics documentés · 2 attendus absents du corpus* — [[SSP — Céphalée]]

> [!abstract] Les 6 grilles fusionnées
> - **AMBOSS-26** — Migraine `premier-dd` · [grille](<file:///Users/damienfulliquet/Developer/GitHub/grilles-ecos/cases/amboss/AMBOSS-26_-_Ce_phale_e_-_Homme_29_ans_-_Grille_ECOS.html>)
> - **AMBOSS-33** — Hémorragie sous-arachnoïdienne `premier-dd` · [grille](<file:///Users/damienfulliquet/Developer/GitHub/grilles-ecos/cases/amboss/AMBOSS-33_-_Ce_phale_e_-_Femme_55_ans_-_Grille_ECOS.html>)
> - **AZYGOS-3** — Migraine `diagnostic-travail` · [grille](<file:///Users/damienfulliquet/Developer/GitHub/grilles-ecos/.azygos-extraction/74108006-36f7-4056-8383-2346f553295e.json>)
> - **German-8** — Céphalée du restaurant chinois `corrige` · [grille](<file:///Users/damienfulliquet/Developer/GitHub/grilles-ecos/cases/german/German-8_-_Ce_phale_es_-_Grille_ECOS.html>)
> - **German-9** — Méningite `corrige` · [grille](<file:///Users/damienfulliquet/Developer/GitHub/grilles-ecos/cases/german/German-9_-_Ce_phale_es_-_Grille_ECOS.html>)
> - **RESCOS-10** — Thrombose veineuse cérébrale `explicite` · [grille](<file:///Users/damienfulliquet/Developer/GitHub/grilles-ecos/cases/rescos/RESCOS-10_-_Ce_phale_e_-_Grille_ECOS.html>)

> [!note] 📋 Anamnèse
> - [ ] **1. Motif principal *(2 grilles sur 6)***
> - [ ] **2. Caractérisation de la céphalée *(3 grilles sur 6)***
> 	- [ ] Localisation
> 	- [ ] Intensité (échelle 0-10) *(2 grilles sur 6)*
> 	- [ ] Qualité
> 	- [ ] Début
> 	- [ ] Événements précipitants *(2 grilles sur 6)*
> 	- [ ] Progression/constant/intermittent *(2 grilles sur 6)*
> 	- [ ] Épisodes antérieurs *(2 grilles sur 6)*
> 	- [ ] Irradiation *(2 grilles sur 6)*
> 	- [ ] Facteurs améliorants *(2 grilles sur 6)*
> 	- [ ] Facteurs aggravants *(2 grilles sur 6)*
> 	- [ ] Symptômes associés *(2 grilles sur 6)*
> 	- [ ] Intensité *(Thrombose veineuse cérébrale)*
> 	- [ ] Évolution *(Thrombose veineuse cérébrale)*
> 	- [ ] Durée *(Thrombose veineuse cérébrale)*
> - [ ] **3. Recherche de symptômes spécifiques *(1 grille sur 6)***
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
> - [ ] **4. Antécédents médicaux *(Hémorragie sous-arachnoïdienne · Migraine · Méningite)***
> - [ ] **5. Allergies *(4 diagnostics)***
> 	- [ ] Allergies *(1 grille sur 6)*
> 	- [ ] Type de réaction *(1 grille sur 6)*
> - [ ] **6. Médicaments *(4 diagnostics)***
> 	- [ ] Antihypertenseurs *(Céphalée du restaurant chinois)*
> 	- [ ] Antalgiques *(Céphalée du restaurant chinois)*
> - [ ] **7. Hospitalisations et antécédents chirurgicaux *(2 grilles sur 6)***
> 	- [ ] Hospitalisations
> 	- [ ] Antécédents chirurgicaux
> - [ ] **8. Antécédents familiaux *(Céphalée du restaurant chinois · Migraine)***
> - [ ] **9. Habitudes et mode de vie *(2 grilles sur 6)***
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
> - [ ] **12. Question d'ouverture *(1 grille sur 6)***
> - [ ] **13. Dimension temporelle *(1 grille sur 6)***
> - [ ] **14. Épisode actuel *(1 grille sur 6)***
> - [ ] **15. Début *(1 grille sur 6)***
> - [ ] **16. Durée des crises *(1 grille sur 6)***
> - [ ] **17. Fréquence et évolution *(1 grille sur 6)***
> - [ ] **18. Localisation *(1 grille sur 6)***
> - [ ] **19. Irradiation *(2 grilles sur 6)***
> - [ ] **20. Qualité *(1 grille sur 6)***
> - [ ] **21. Intensité de la douleur *(2 grilles sur 6)***
> - [ ] **22. Facteurs aggravants *(2 grilles sur 6)***
> - [ ] **23. Facteurs soulageants *(1 grille sur 6)***
> - [ ] **24. Bilans neurologiques antérieurs *(1 grille sur 6)***
> - [ ] **25. Retentissement des symptômes *(1 grille sur 6)***
> - [ ] **26. Symptômes associés *(2 grilles sur 6)***
> 	- [ ] Nausées/vomissements *(Thrombose veineuse cérébrale)*
> 	- [ ] Photophobie/phonophobie *(Thrombose veineuse cérébrale)*
> 	- [ ] Symptômes neurologiques *(Thrombose veineuse cérébrale)*
> 	- [ ] Fièvre *(Thrombose veineuse cérébrale)*
> 	- [ ] Éruption cutanée *(Thrombose veineuse cérébrale)*
> - [ ] **27. Nausées / vomissements *(1 grille sur 6)***
> - [ ] **28. Photophobie *(1 grille sur 6)***
> - [ ] **29. Phonophobie *(1 grille sur 6)***
> - [ ] **30. Symptômes d'aura *(1 grille sur 6)***
> - [ ] **31. Symptômes autonomes *(1 grille sur 6)***
> - [ ] **32. Anamnèse des déclencheurs *(1 grille sur 6)***
> - [ ] **33. Sommeil *(1 grille sur 6)***
> - [ ] **34. Stress *(1 grille sur 6)***
> - [ ] **35. Menstruation *(1 grille sur 6)***
> - [ ] **36. Alimentation / caféine / alcool *(1 grille sur 6)***
> - [ ] **37. Signes d'alarme des céphalées *(1 grille sur 6)***
> - [ ] **38. Début en coup de tonnerre *(1 grille sur 6)***
> - [ ] **39. Céphalée maximale *(1 grille sur 6)***
> - [ ] **40. Fièvre *(2 grilles sur 6)***
> - [ ] **41. Raideur de nuque *(2 grilles sur 6)***
> - [ ] **42. Trouble de la conscience *(1 grille sur 6)***
> - [ ] **43. Déficit neurologique focal *(1 grille sur 6)***
> - [ ] **44. Grossesse *(1 grille sur 6)***
> - [ ] **45. Traumatisme *(2 grilles sur 6)***
> - [ ] **46. Abus médicamenteux *(1 grille sur 6)***
> - [ ] **47. Dépistage de l'artérite à cellules géantes *(1 grille sur 6)***
> - [ ] **48. Diagnostic antérieur de céphalées *(1 grille sur 6)***
> - [ ] **49. Antécédents chirurgicaux *(1 grille sur 6)***
> - [ ] **50. Désir de grossesse *(1 grille sur 6)***
> - [ ] **51. Noxes *(1 grille sur 6)***
> - [ ] **52. Tabagisme *(1 grille sur 6)***
> - [ ] **53. Drogues *(1 grille sur 6)***
> - [ ] **54. Migraine dans la famille *(1 grille sur 6)***
> - [ ] **55. Profession *(1 grille sur 6)***
> - [ ] **56. Facteurs de stress psychosociaux *(1 grille sur 6)***
> - [ ] **57. Situation sociale *(1 grille sur 6)***
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
> - [ ] **1. Mesures d'hygiène *(2 grilles sur 6)***
> 	- [ ] Lavage des mains
> 	- [ ] Respect de la pudeur avec drap
> - [ ] **2. Examen de la tête, yeux, oreilles, nez et gorge *(2 grilles sur 6)***
> 	- [ ] Inspection de la tête
> 	- [ ] Palpation de la tête
> 	- [ ] Inspection des conjonctives *(1 grille sur 6)*
> 	- [ ] Évaluation de l'acuité visuelle (échelle de Snellen) *(1 grille sur 6)*
> 	- [ ] Fond d'œil direct
> - [ ] **3. Examen du cou *(1 grille sur 6)***
> 	- [ ] Inspection du cou
> 	- [ ] Palpation du cou
> - [ ] **4. Examen neurologique *(2 grilles sur 6)***
> 	- [ ] Évaluation de l'orientation dans le temps, l'espace et les personnes
> 	- [ ] Examen ciblé des nerfs crâniens
> 	- [ ] Recherche de méningisme *(1 grille sur 6)*
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
> - [ ] **6. Méningisme *(2 grilles sur 6)***
> - [ ] **7. Pupilles *(1 grille sur 6)***
> - [ ] **8. Oculomotricité *(1 grille sur 6)***
> - [ ] **9. Mouvements oculaires *(1 grille sur 6)***
> - [ ] **10. Acuité visuelle / champ visuel *(1 grille sur 6)***
> - [ ] **11. Nerfs crâniens *(1 grille sur 6)***
> - [ ] **12. Nerf VII | Facial *(1 grille sur 6)***
> - [ ] **13. Nerfs IX-XII | Tronc cérébral *(1 grille sur 6)***
> - [ ] **14. Nerf V | Trijumeau *(1 grille sur 6)***
> - [ ] **15. Motricité *(1 grille sur 6)***
> - [ ] **16. Sensibilité *(1 grille sur 6)***
> - [ ] **17. Réflexes *(1 grille sur 6)***
> - [ ] **18. Coordination *(1 grille sur 6)***
> - [ ] **19. Démarche *(1 grille sur 6)***
> - [ ] **20. Tête *(1 grille sur 6)***
> - [ ] **21. Examen des sinus *(1 grille sur 6)***
> - [ ] **22. Inspection *(1 grille sur 6)***
> - [ ] **23. Palpation de la voûte crânienne *(1 grille sur 6)***
> - [ ] **24. Colonne cervicale *(1 grille sur 6)***
> - [ ] **25. Articulation temporo-mandibulaire *(1 grille sur 6)***
> - [ ] **26. Artère temporale *(1 grille sur 6)***
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

> [!success] 💊 Management — partagé par plusieurs diagnostics
> - [ ] **1. Hypothèses diagnostiques *(2 grilles sur 6)* — *Hémorragie sous-arachnoïdienne · Migraine***
> - [ ] **2. Diagnostic de suspicion *(2 grilles sur 6)* — *Céphalée du restaurant chinois · Méningite***

> [!success] 💊 Management — si Algie vasculaire (cluster)
> *Aucune grille du corpus ne documente ce diagnostic* — il est pourtant attendu de cette SSP. **Trou de révision à combler ailleurs.**

> [!success] 💊 Management — si Céphalée du restaurant chinois
> - [ ] **1. Diagnostics différentiels**
> - [ ] **2. Examens diagnostiques**
> 	- [ ] VS (CRP)
> 	- [ ] FSC
> - [ ] **3. CT cérébral**
> - [ ] **4. Traitement/Prise en charge**
> 	- [ ] Si maladie de Horton : corticoïdes et référence
> 	- [ ] Sinon : antalgiques et contrôle

> [!success] 💊 Management — si Hémorragie sous-arachnoïdienne
> - [ ] **1. Conseil et soutien**
> 	- [ ] Proposer d'aider la patiente à s'allonger
> 	- [ ] Proposer de diminuer l'éclairage dans la salle d'examen
> 	- [ ] Réaction appropriée au défi concernant le mari
> 	- [ ] Soutien émotionnel face à la gravité
> 	- [ ] Information sur l'urgence de la situation
> - [ ] **2. Examens complémentaires urgents**
> 	- [ ] CT cérébral sans contraste
> 	- [ ] FSC
> 	- [ ] Glucose, électrolytes
> - [ ] **3. Examens complémentaires biologiques et microbiologiques**
> 	- [ ] TP, TCA
> 	- [ ] Hémocultures
> - [ ] **4. Ponction lombaire et imagerie spécialisée**
> 	- [ ] Ponction lombaire avec analyse du LCR
> 	- [ ] Angiographie
> - [ ] **5. Communication avec la patiente**
> 	- [ ] Explications à la patiente des impressions diagnostiques préliminaires
> 	- [ ] Explication du plan de prise en charge
> 	- [ ] Utilisation d'un langage non médical et clarification des termes médicaux
> 	- [ ] Évaluation de l'accord de la patiente avec le plan diagnostique
> 	- [ ] Recherche des préoccupations et questions de la patiente
> 	- [ ] Ne pas répéter les manœuvres douloureuses pendant l'examen physique

> [!success] 💊 Management — si Méningite
> - [ ] **1. Diagnostics différentiels**
> - [ ] **2. Examens de laboratoire**
> 	- [ ] FSC
> 	- [ ] CRP
> 	- [ ] Électrolytes
> 	- [ ] Glucose
> - [ ] **3. Diagnostic du liquide céphalo-rachidien**
> 	- [ ] Liquide clair
> 	- [ ] Lymphocytose
> 	- [ ] Glucose normale
> 	- [ ] Protéines
> 	- [ ] Lactate
> - [ ] **4. Traitement**

> [!success] 💊 Management — si Migraine
> - [ ] **1. Drapeaux rouges à rechercher *(1 grille sur 2)***
> 	- [ ] Céphalée sévère implacable
> 	- [ ] Fièvre
> 	- [ ] Déficits neurologiques focaux
> 	- [ ] Convulsions
> 	- [ ] Troubles de conscience
> 	- [ ] Signes d'hypertension intracrânienne (ex: perte de connaissance, œdème papillaire)
> 	- [ ] Signes de méningisme
> 	- [ ] Symptômes psychiatriques
> 	- [ ] Douleur oculaire
> - [ ] **2. Prise en charge *(1 grille sur 2)***
> 	- [ ] Migraine, céphalée de tension et algie vasculaire = diagnostics cliniques basés sur l'histoire et l'examen physique
> 	- [ ] Ne pas faire d'examens diagnostiques sauf si drapeaux rouges présents
> 	- [ ] Proposer au patient de s'allonger et tamiser la lumière
> - [ ] **3. Communication avec le patient *(1 grille sur 2)***
> 	- [ ] Explications au patient des impressions diagnostiques préliminaires
> 	- [ ] Explication du plan de prise en charge
> 	- [ ] Utilisation d'un langage non médical et clarification des termes médicaux
> 	- [ ] Évaluation de l'accord du patient avec le plan diagnostique
> 	- [ ] Recherche des préoccupations et questions du patient
> - [ ] **4. Conseil et soutien *(1 grille sur 2)***
> 	- [ ] Conseil sur l'arrêt du tabac
> 	- [ ] Donner l'option de s'allonger et proposer de tamiser la lumière
> 	- [ ] Réaction appropriée au défi concernant l'entretien d'embauche
> 	- [ ] Éducation sur les facteurs déclenchants
> 	- [ ] Conseils hygiène de vie
> - [ ] **5. Pas d'imagerie *(1 grille sur 2)***
> - [ ] **6. Diagnostic de travail *(1 grille sur 2)***
> - [ ] **7. Information sur le diagnostic *(1 grille sur 2)***
> - [ ] **8. Traitement de la crise par AINS *(1 grille sur 2)***
> - [ ] **9. Traitement de la crise par triptan *(1 grille sur 2)***
> - [ ] **10. Mesures non médicamenteuses *(1 grille sur 2)***
> - [ ] **11. Filet de sécurité *(1 grille sur 2)***
> - [ ] **12. Journal des migraines *(1 grille sur 2)***
> - [ ] **13. Conseils sur le mode de vie *(1 grille sur 2)***
> - [ ] **14. Information sur la contraception *(1 grille sur 2)***
> - [ ] **15. Contrôle de suivi *(1 grille sur 2)***
> - [ ] **16. Évaluer l'indication à une prophylaxie *(1 grille sur 2)***
> - [ ] **17. Orientation vers la neurologie *(1 grille sur 2)***

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
