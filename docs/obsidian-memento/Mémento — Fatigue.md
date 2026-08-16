---
aliases:
  - "Mémento Fatigue"
type: memento-ecos-ssp
ssp: "Fatigue"
specialite: "Médecine Interne"
cas: 11
diagnostics: 10
attendus_documentes_ailleurs: 1
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

> [!warning] Mémento mixte — 1 grille officielle, 10 non officielles
> **RESCOS-67b** fait partie des **neuf grilles officielles** et fait donc
> autorité ; elle est signalée ⭐️ dans l'encadré ci-dessous. Les 10
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

# Fatigue

*Médecine Interne · 11 grilles · 10 diagnostics documentés · 1 attendu documenté ailleurs · 1 attendu absent du corpus* — [[SSP — Fatigue]]

> [!abstract] Les 11 grilles fusionnées
> - **AMBOSS-27** — Syndrome de Sheehan (hypopituitarisme post-partum) `premier-dd` · [grille](<file:///Users/damienfulliquet/Developer/GitHub/grilles-ecos/cases/amboss/AMBOSS-27_-_Fatigue_-_Femme_28_ans_-_Grille_ECOS.html>)
> - **AMBOSS-29** — Mononucléose `premier-dd` · [grille](<file:///Users/damienfulliquet/Developer/GitHub/grilles-ecos/cases/amboss/AMBOSS-29_-_Fatigue_-_Femme_18_ans_-_Grille_ECOS.html>)
> - **AMBOSS-36** — Hépatite C aiguë `enonce` · [grille](<file:///Users/damienfulliquet/Developer/GitHub/grilles-ecos/cases/amboss/AMBOSS-36_-_Fatigue_-_Homme_54_ans_-_Grille_ECOS.html>)
> - **AZYGOS-30** — Hémorragie digestive haute sur ulcère peptique `diagnostic-travail` · [grille](<file:///Users/damienfulliquet/Developer/GitHub/grilles-ecos/docs/azygos-grilles/c02797e2-7f49-43bf-bd93-bf93fb65966a.json>)
> - **German-45** — SAOS `corrige` · [grille](<file:///Users/damienfulliquet/Developer/GitHub/grilles-ecos/cases/german/German-45_-_Fatigue_-_Grille_ECOS.html>)
> - **German-46** — Anémie `corrige` · [grille](<file:///Users/damienfulliquet/Developer/GitHub/grilles-ecos/cases/german/German-46_-_Fatigue_-_Grille_ECOS.html>)
> - **German-47** — Dépression `corrige` · [grille](<file:///Users/damienfulliquet/Developer/GitHub/grilles-ecos/cases/german/German-47_-_Fatigue_-_Grille_ECOS.html>)
> - **RESCOS-44** — Diabète de type 2 `explicite` · [grille](<file:///Users/damienfulliquet/Developer/GitHub/grilles-ecos/cases/rescos/RESCOS-44%20-%20Fatigue%20-%20Grille%20ECOS.html>)
> - **RESCOS-45** — Dépression gériatrique `confirme` · [grille](<file:///Users/damienfulliquet/Developer/GitHub/grilles-ecos/cases/rescos/RESCOS-45%20-%20Fatigue%20-%20Grille%20ECOS.html>)
> - **RESCOS-67** — Hypothyroïdie `explicite` · [grille](<file:///Users/damienfulliquet/Developer/GitHub/grilles-ecos/cases/rescos/RESCOS-67%20-%20Fatigue%20-%20Grille%20ECOS.html>)
> - **RESCOS-67b** ⭐️ **officielle** — Hypothyroïdie `explicite` · [grille](<file:///Users/damienfulliquet/Developer/GitHub/grilles-ecos/cases/rescos/RESCOS-67b%20-%20Fatigue%20-%20Grille%20ECOS.html>)

> [!note] 📋 Anamnèse
> - [ ] **1. Motif principal *(Hépatite C aiguë · Mononucléose · Syndrome de Sheehan (hypopituitarisme post-partum))***
> - [ ] **2. Caractérisation de la fatigue *(5 diagnostics)***
> 	- [ ] Début *(Hépatite C aiguë · Mononucléose · Syndrome de Sheehan (hypopituitarisme post-partum))*
> 	- [ ] Évolution temporelle *(Mononucléose · Syndrome de Sheehan (hypopituitarisme post-partum))*
> 	- [ ] Événements précipitants *(Hépatite C aiguë · Mononucléose · Syndrome de Sheehan (hypopituitarisme post-partum))*
> 	- [ ] Progression *(Hépatite C aiguë · Mononucléose · Syndrome de Sheehan (hypopituitarisme post-partum))*
> 	- [ ] Épisodes antérieurs *(Hépatite C aiguë · Mononucléose · Syndrome de Sheehan (hypopituitarisme post-partum))*
> 	- [ ] Facteurs améliorants *(Hépatite C aiguë · Mononucléose · Syndrome de Sheehan (hypopituitarisme post-partum))*
> 	- [ ] Facteurs aggravants *(Hépatite C aiguë · Mononucléose · Syndrome de Sheehan (hypopituitarisme post-partum))*
> 	- [ ] Symptômes associés *(Hépatite C aiguë · Mononucléose · Syndrome de Sheehan (hypopituitarisme post-partum))*
> 	- [ ] Constante/intermittente *(Hépatite C aiguë)*
> 	- [ ] Apparition *(Diabète de type 2)*
> 	- [ ] Intensité *(Diabète de type 2)*
> 	- [ ] Évolution *(Diabète de type 2 · Hypothyroïdie)*
> 	- [ ] Fluctuence *(Diabète de type 2)*
> 	- [ ] Impact sur l'AVQ *(Diabète de type 2)*
> 	- [ ] Premier épisode? *(Diabète de type 2)*
> 	- [ ] Durée *(Hypothyroïdie)*
> 	- [ ] Chronologie sur la journée *(Hypothyroïdie)*
> 	- [ ] Circonstances de survenue *(Hypothyroïdie)*
> - [ ] **3. Recherche de symptômes spécifiques post-partum *(Syndrome de Sheehan (hypopituitarisme post-partum))***
> 	- [ ] Traumatisme
> 	- [ ] Céphalées
> 	- [ ] Nausées/vomissements
> 	- [ ] Fièvre/frissons
> 	- [ ] Palpitations
> 	- [ ] Éruption cutanée/changements cutanés
> 	- [ ] Dyspnée
> 	- [ ] Problèmes urinaires
> 	- [ ] Problèmes intestinaux
> 	- [ ] Troubles du sommeil
> 	- [ ] Appétit
> 	- [ ] Variations pondérales
> 	- [ ] Infections récentes
> 	- [ ] Vertiges
> 	- [ ] Cheveux secs
> 	- [ ] Allaitement
> - [ ] **4. Évaluation de l'humeur et symptômes dépressifs *(Mononucléose · Syndrome de Sheehan (hypopituitarisme post-partum))***
> 	- [ ] Humeur
> 	- [ ] Perte d'intérêt
> 	- [ ] Culpabilité/faible estime de soi
> 	- [ ] Difficultés de concentration
> 	- [ ] Agitation ou ralentissement psychomoteur
> 	- [ ] Idées suicidaires
> 	- [ ] Soutien social
> 	- [ ] Intention de nuire aux enfants *(Syndrome de Sheehan (hypopituitarisme post-partum))*
> 	- [ ] Faible énergie *(Mononucléose)*
> - [ ] **5. Antécédents médicaux *(5 diagnostics)***
> 	- [ ] Médicaux *(SAOS)*
> 	- [ ] Psychiatriques/neurologiques *(SAOS)*
> 	- [ ] Événement marquant récent *(SAOS)*
> - [ ] **6. Allergies *(4 diagnostics)***
> - [ ] **7. Médicaments actuels *(6 diagnostics)***
> - [ ] **8. Hospitalisations et antécédents chirurgicaux *(Hépatite C aiguë · Mononucléose · Syndrome de Sheehan (hypopituitarisme post-partum))***
> 	- [ ] Hospitalisations
> 	- [ ] Antécédents chirurgicaux
> - [ ] **9. Antécédents familiaux *(5 diagnostics)***
> 	- [ ] Anémies héréditaires *(Anémie)*
> 	- [ ] Maladies hématologiques *(Anémie)*
> - [ ] **10. Habitudes et mode de vie *(6 diagnostics)***
> 	- [ ] Travail *(Hépatite C aiguë · Mononucléose · Syndrome de Sheehan (hypopituitarisme post-partum))*
> 	- [ ] Alcool
> 	- [ ] Drogues récréatives *(Hépatite C aiguë · Mononucléose · Syndrome de Sheehan (hypopituitarisme post-partum))*
> 	- [ ] Tabac *(5 diagnostics)*
> 	- [ ] Exercice *(Mononucléose · Syndrome de Sheehan (hypopituitarisme post-partum))*
> 	- [ ] Alimentation *(Diabète de type 2 · Syndrome de Sheehan (hypopituitarisme post-partum))*
> 	- [ ] Domicile *(Hépatite C aiguë · Mononucléose)*
> 	- [ ] Ressenti besoin de réduire votre consommation ? *(Hépatite C aiguë)*
> 	- [ ] Agacé par les critiques sur votre consommation ? *(Hépatite C aiguë)*
> 	- [ ] Culpabilité à propos de la consommation ? *(Hépatite C aiguë)*
> 	- [ ] Besoin de boire dès le matin ? *(Hépatite C aiguë)*
> 	- [ ] Usage de drogues intraveineuses *(Hépatite C aiguë)*
> 	- [ ] Drogues *(Anémie · Diabète de type 2 · Dépression)*
> 	- [ ] Médicaments actuels *(Diabète de type 2)*
> - [ ] **11. Antécédents gynéco-obstétricaux *(Syndrome de Sheehan (hypopituitarisme post-partum))***
> 	- [ ] Activité sexuelle
> 	- [ ] Douleur lors des rapports
> 	- [ ] Libido
> 	- [ ] Dernières règles
> 	- [ ] Ménarche
> 	- [ ] Durée des règles
> 	- [ ] Règles régulières
> 	- [ ] Grossesses
> 	- [ ] Antécédents prénataux
> 	- [ ] Antécédents d'accouchement
> - [ ] **12. Recherche de symptômes spécifiques *(Mononucléose)***
> 	- [ ] Œdème des chevilles
> 	- [ ] Fièvre/frissons
> 	- [ ] Palpitations
> 	- [ ] Éruption cutanée/changements cutanés
> 	- [ ] Douleur thoracique
> 	- [ ] Dyspnée
> 	- [ ] Problèmes intestinaux
> 	- [ ] Troubles du sommeil
> 	- [ ] Appétit
> 	- [ ] Variations pondérales
> 	- [ ] Intolérance au froid
> 	- [ ] Changements capillaires
> 	- [ ] Changements de voix
> 	- [ ] Crampes musculaires
> - [ ] **13. Contacts malades et antécédents familiaux *(Hépatite C aiguë · Mononucléose)***
> 	- [ ] Contacts malades
> 	- [ ] Antécédents familiaux
> - [ ] **14. Antécédents gynécologiques *(Mononucléose)***
> 	- [ ] Activité sexuelle
> 	- [ ] Avec qui
> 	- [ ] Hommes ou femmes
> 	- [ ] Nombre de partenaires au cours de la dernière année
> 	- [ ] Protection
> 	- [ ] Dernières règles
> 	- [ ] Ménarche
> 	- [ ] Durée des règles
> 	- [ ] Règles régulières
> 	- [ ] Combien de tampons par jour
> 	- [ ] Grossesses
> - [ ] **15. Recherche de symptômes spécifiques pour fatigue après fièvre et vomissements *(Hépatite C aiguë)***
> 	- [ ] Voyage récent
> 	- [ ] Nausées/vomissements
> 	- [ ] Fièvre/frissons
> 	- [ ] Sueurs nocturnes
> 	- [ ] Éruption cutanée/changements cutanés
> 	- [ ] Douleurs articulaires
> 	- [ ] Problèmes urinaires/changements de couleur de l'urine
> 	- [ ] Problèmes intestinaux/changements de couleur des selles
> 	- [ ] Douleur abdominale
> 	- [ ] Appétit
> 	- [ ] Changements de poids
> 	- [ ] Prurit
> 	- [ ] Gonflement des seins
> 	- [ ] Diminution de la pilosité corporelle
> 	- [ ] Diminution de la libido
> - [ ] **16. Question d’entrée *(Hémorragie digestive haute sur ulcère peptique)***
> - [ ] **17. Dimension temporelle *(Hémorragie digestive haute sur ulcère peptique)***
> - [ ] **18. Début *(Hémorragie digestive haute sur ulcère peptique)***
> - [ ] **19. Évolution *(Hémorragie digestive haute sur ulcère peptique)***
> - [ ] **20. Vertiges *(Hémorragie digestive haute sur ulcère peptique)***
> - [ ] **21. Dyspnée d’effort *(Hémorragie digestive haute sur ulcère peptique)***
> - [ ] **22. Symptômes associés *(Hémorragie digestive haute sur ulcère peptique · SAOS)***
> 	- [ ] Fièvre, infection *(SAOS)*
> 	- [ ] Perte/prise de poids *(SAOS)*
> 	- [ ] Polyurie/polydipsie *(SAOS)*
> 	- [ ] Troubles digestifs, sang dans les selles *(SAOS)*
> 	- [ ] Troubles mictionnels *(SAOS)*
> - [ ] **23. Douleurs abdominales *(Hémorragie digestive haute sur ulcère peptique)***
> - [ ] **24. Nausées / vomissements *(Hémorragie digestive haute sur ulcère peptique)***
> - [ ] **25. Anamnèse des selles *(Hémorragie digestive haute sur ulcère peptique)***
> - [ ] **26. Modification des selles *(Hémorragie digestive haute sur ulcère peptique)***
> - [ ] **27. Consistance *(Hémorragie digestive haute sur ulcère peptique)***
> - [ ] **28. Couleur *(Hémorragie digestive haute sur ulcère peptique)***
> - [ ] **29. Mélange de sang *(Hémorragie digestive haute sur ulcère peptique)***
> - [ ] **30. DD malignité *(Hémorragie digestive haute sur ulcère peptique)***
> - [ ] **31. Symptômes B *(Hémorragie digestive haute sur ulcère peptique)***
> - [ ] **32. Appétit *(Hémorragie digestive haute sur ulcère peptique)***
> - [ ] **33. Dysphagie *(Hémorragie digestive haute sur ulcère peptique)***
> - [ ] **34. DD fatigue *(Hémorragie digestive haute sur ulcère peptique)***
> - [ ] **35. Thyroïde *(Hémorragie digestive haute sur ulcère peptique)***
> - [ ] **36. Humeur *(Hémorragie digestive haute sur ulcère peptique)***
> - [ ] **37. Sommeil *(Hypothyroïdie · Hémorragie digestive haute sur ulcère peptique)***
> 	- [ ] Durée *(Hypothyroïdie)*
> 	- [ ] Qualité *(Hypothyroïdie)*
> 	- [ ] Impact sur la fatigue *(Hypothyroïdie)*
> - [ ] **38. Polyurie / polydipsie *(Hémorragie digestive haute sur ulcère peptique)***
> - [ ] **39. Antécédents *(Hypothyroïdie · Hémorragie digestive haute sur ulcère peptique)***
> 	- [ ] Antécédents médicaux *(Hypothyroïdie)*
> 	- [ ] Traitement *(Hypothyroïdie)*
> - [ ] **40. Antécédents opératoires *(Hémorragie digestive haute sur ulcère peptique)***
> - [ ] **41. Automédication par AINS *(Hémorragie digestive haute sur ulcère peptique)***
> - [ ] **42. Anticoagulants *(Hémorragie digestive haute sur ulcère peptique)***
> - [ ] **43. Antihypertenseur *(Hémorragie digestive haute sur ulcère peptique)***
> - [ ] **44. Coloscopie de dépistage *(Hémorragie digestive haute sur ulcère peptique)***
> - [ ] **45. Noxes *(Hémorragie digestive haute sur ulcère peptique)***
> - [ ] **46. Alcool *(Hémorragie digestive haute sur ulcère peptique)***
> - [ ] **47. Tabac *(Hémorragie digestive haute sur ulcère peptique)***
> - [ ] **48. Anamnèse sociale *(Anémie · Hémorragie digestive haute sur ulcère peptique)***
> 	- [ ] Situation professionnelle/études *(Anémie)*
> 	- [ ] Conditions de vie *(Anémie)*
> 	- [ ] Stress psychosocial *(Anémie)*
> - [ ] **49. Se présente avec nom, fonction et but de la consultation *(Anémie · Dépression · SAOS)***
> - [ ] **50. Question ouverte d'introduction → Symptôme principal *(SAOS)***
> - [ ] **51. Évolution temporelle *(SAOS)***
> - [ ] **52. Évolution dans la journée *(SAOS)***
> - [ ] **53. Facteurs déclenchants identifiés *(Dépression · SAOS)***
> - [ ] **54. Exploration du sommeil - Qualité *(SAOS)***
> 	- [ ] Qualité subjective
> 	- [ ] Durée de sommeil
> 	- [ ] Problèmes d'endormissement
> 	- [ ] Problèmes de maintien du sommeil
> 	- [ ] Activités avant le coucher
> - [ ] **55. Caractéristiques du sommeil et somnolence *(SAOS)***
> 	- [ ] Sommeil réparateur
> 	- [ ] Somnolence diurne
> 	- [ ] Situations à risque
> - [ ] **56. Signes évocateurs de syndrome d'apnée du sommeil *(SAOS)***
> 	- [ ] Ronflement
> 	- [ ] Pauses respiratoires nocturnes
> 	- [ ] Céphalées matinales
> - [ ] **57. État psychique et humeur *(SAOS)***
> 	- [ ] Changements d'humeur
> 	- [ ] Satisfaction avec la vie actuelle
> 	- [ ] Manque d'élan/motivation
> 	- [ ] Capacité de concentration
> - [ ] **58. Performance et activités quotidiennes *(SAOS)***
> 	- [ ] Performance physique et mentale
> 	- [ ] Déroulement journée type
> 	- [ ] Activité physique régulière
> - [ ] **59. Habitudes alimentaires et consommation *(SAOS)***
> - [ ] **60. Automédication déjà tentée *(SAOS)***
> - [ ] **61. Habitudes de vie (noxes) *(SAOS)***
> 	- [ ] Tabac
> 	- [ ] Alcool
> 	- [ ] Drogues
> - [ ] **62. Anamnèse sociale et professionnelle *(SAOS)***
> - [ ] **63. Problème actuel et plaintes subjectives *(Anémie)***
> - [ ] **64. Symptômes cardiovasculaires *(Anémie)***
> 	- [ ] Dyspnée
> 	- [ ] Palpitations
> - [ ] **65. État général et performance *(Anémie)***
> 	- [ ] Capacité de performance
> 	- [ ] Fatigue
> 	- [ ] État psychique
> - [ ] **66. Symptômes fonctionnels *(Anémie)***
> 	- [ ] Troubles orthostatiques
> 	- [ ] Qualité du sommeil
> 	- [ ] Pâleur remarquée
> - [ ] **67. Épisodes antérieurs similaires et problèmes médicaux passés *(Anémie)***
> - [ ] **68. Recherche de pathologies sous-jacentes *(Anémie)***
> 	- [ ] Infection récente
> 	- [ ] Maladie rénale connue
> - [ ] **69. Anamnèse de pertes sanguines *(Anémie)***
> 	- [ ] Menstruations abondantes
> 	- [ ] Méléna
> 	- [ ] Hématémèse
> 	- [ ] Autres saignements
> - [ ] **70. Habitudes alimentaires et nutritionnelles *(Anémie)***
> 	- [ ] Alimentation équilibrée
> 	- [ ] Régime végétarien/végétalien
> 	- [ ] Consommation de viande rouge
> 	- [ ] Consommation d'alcool
> - [ ] **71. Troubles gastro-intestinaux *(Anémie)***
> 	- [ ] Digestion
> 	- [ ] Dysphagie
> 	- [ ] Maladie ulcéreuse
> 	- [ ] Chirurgie gastrique
> - [ ] **72. Troubles neurologiques *(Anémie)***
> 	- [ ] Troubles de la marche
> 	- [ ] Paresthésies
> 	- [ ] Troubles de la sensibilité profonde
> - [ ] **73. Douleurs osseuses *(Anémie)***
> 	- [ ] Localisation
> 	- [ ] Intensité
> - [ ] **74. Médicaments et exposition à des toxiques *(Anémie)***
> 	- [ ] Médicaments actuels
> 	- [ ] Exposition professionnelle
> - [ ] **75. Évolution temporelle des symptômes *(Dépression)***
> - [ ] **76. Symptômes principaux *(Dépression)***
> 	- [ ] Fatigue
> 	- [ ] Faiblesse
> 	- [ ] Troubles de concentration
> - [ ] **77. Variation diurne des symptômes *(Dépression)***
> 	- [ ] Moment d'amélioration/aggravation
> 	- [ ] Présence d'une baisse matinale
> - [ ] **78. Impact fonctionnel sur la vie quotidienne *(Dépression)***
> - [ ] **79. Qualité du sommeil *(Dépression)***
> - [ ] **80. Appétit et alimentation *(Dépression)***
> - [ ] **81. Autres symptômes ou maladie récente *(Dépression)***
> - [ ] **82. Dépistage de dépression *(Dépression)***
> 	- [ ] Humeur dépressive
> 	- [ ] Anhédonie
> 	- [ ] Épisodes dépressifs antérieurs
> 	- [ ] Troubles du sommeil
> - [ ] **83. Dépistage d'hypothyroïdie *(Dépression)***
> 	- [ ] État de la peau
> 	- [ ] État des cheveux
> 	- [ ] Troubles gastro-intestinaux
> 	- [ ] Transpiration/intolérance au froid
> - [ ] **84. Dépistage d'anémie *(Dépression)***
> 	- [ ] Dyspnée
> 	- [ ] Palpitations
> 	- [ ] Impact du végétarisme
> - [ ] **85. Dépistage de pathologie maligne *(Dépression)***
> 	- [ ] Sueurs nocturnes
> 	- [ ] Fièvre
> 	- [ ] Perte de poids
> 	- [ ] Adénopathies
> - [ ] **86. Dépistage de diabète *(Dépression)***
> 	- [ ] Polydipsie
> 	- [ ] Polyurie
> 	- [ ] Infections récurrentes
> - [ ] **87. Évaluation structurée du risque suicidaire *(Dépression)***
> 	- [ ] Pensées de ne plus vouloir vivre ainsi
> 	- [ ] Désir de changement
> 	- [ ] Pensées de mort
> 	- [ ] Idées suicidaires actives
> 	- [ ] Plans concrets
> 	- [ ] Méthode envisagée
> 	- [ ] Tentatives antérieures
> 	- [ ] Antécédents familiaux de suicide
> - [ ] **88. Symptômes psychiatriques associés *(Dépression)***
> 	- [ ] Anxiété
> 	- [ ] Troubles obsessionnels-compulsifs
> 	- [ ] Troubles de la pensée
> 	- [ ] Idées délirantes
> 	- [ ] Hallucinations
> 	- [ ] Troubles du moi
> - [ ] **89. Antécédents familiaux psychiatriques *(Dépression)***
> - [ ] **90. Anamnèse sociale et réseau de soutien *(Dépression)***
> 	- [ ] Soutien social
> 	- [ ] Situation de logement
> 	- [ ] Situation professionnelle
> - [ ] **91. Caractérisation du sommeil *(Diabète de type 2)***
> 	- [ ] Durée du sommeil
> 	- [ ] Qualité du sommeil
> 	- [ ] Réveils durant la nuit
> 	- [ ] Ronflement
> - [ ] **92. Anamnèse uro-génitale *(Diabète de type 2)***
> 	- [ ] Couleur
> 	- [ ] Quantité
> 	- [ ] Douleur
> 	- [ ] Fréquence
> 	- [ ] Urgence mictionnelle
> - [ ] **93. Anamnèse alimentaire *(Diabète de type 2)***
> 	- [ ] Quels aliments?
> 	- [ ] Plats types
> 	- [ ] Grignotages
> - [ ] **94. DD - dépression *(Diabète de type 2)***
> 	- [ ] Perte de plaisir
> 	- [ ] Tristesse
> 	- [ ] Idées noires
> 	- [ ] Arrêt d'activités
> 	- [ ] Envies suicidaires
> - [ ] **95. DD - cancer *(Diabète de type 2)***
> 	- [ ] Perte de poids
> 	- [ ] Fièvre
> 	- [ ] Sudation nocturne
> - [ ] **96. DD - maladie infectieuse *(Diabète de type 2)***
> 	- [ ] Douleurs abdominales
> 	- [ ] Rapports sexuels à risque
> 	- [ ] Voyage dans un pays à risque
> - [ ] **97. DD - insuffisance cardiovasculaire *(Diabète de type 2)***
> 	- [ ] Dyspnée à l'effort
> 	- [ ] Orthopnée paroxystique nocturne
> 	- [ ] Jambes gonflées
> 	- [ ] Toux sèche
> - [ ] **98. Raison de la visite *(Dépression gériatrique)***
> - [ ] **99. Type d'insomnie : sommeil court, léger *(Dépression gériatrique)***
> - [ ] **100. Chronologie (durée, fréquence) *(Dépression gériatrique)***
> - [ ] **101. Développement : progressif *(Dépression gériatrique)***
> - [ ] **102. Symptômes associés : tristesse, anhédonie *(Dépression gériatrique)***
> - [ ] **103. Situation familiale / statut marital *(Dépression gériatrique)***
> - [ ] **104. Ana. générale : sudation nocturne *(Dépression gériatrique)***
> - [ ] **105. Ana. générale : ronflement *(Dépression gériatrique)***
> - [ ] **106. Ana. générale : prise/perte de poids *(Dépression gériatrique)***
> - [ ] **107. Ana. cardio-vasc : hypertension *(Dépression gériatrique)***
> - [ ] **108. Ana. digestive : mange peu *(Dépression gériatrique)***
> - [ ] **109. Ana. ostéo-articulaire : gonarthrose bilatérale *(Dépression gériatrique)***
> - [ ] **110. Ana. suicide : présence de pensées suicidaires ? *(Dépression gériatrique)***
> - [ ] **111. Histoire médicale : antécédent cancer *(Dépression gériatrique)***
> - [ ] **112. Histoire médicale : opérations *(Dépression gériatrique)***
> - [ ] **113. Habitudes : médicaments *(Dépression gériatrique)***
> - [ ] **114. Habitudes : alcool / drogues *(Dépression gériatrique)***
> - [ ] **115. Conséquences de la fatigue sur le quotidien *(Hypothyroïdie)***
> - [ ] **116. Symptômes B associés *(Hypothyroïdie)***
> 	- [ ] Fièvre
> 	- [ ] Variation de poids
> 	- [ ] Sueurs nocturnes
> - [ ] **117. Symptômes d'hypothyroïdie *(Hypothyroïdie)***
> 	- [ ] Intolérance au froid
> 	- [ ] Transit ralenti
> - [ ] **118. Autres symptômes associés *(Hypothyroïdie)***
> 	- [ ] Toux
> 	- [ ] Douleurs abdominales
> 	- [ ] Modifications de l'appétit
> 	- [ ] Douleurs musculaires ou articulaires
> 	- [ ] Polyurie ou polydipsie
> - [ ] **119. Situation menstruelle *(Hypothyroïdie)***
> 	- [ ] Durée des règles
> 	- [ ] Abondance
> - [ ] **120. Anamnèse psychiatrique *(Hypothyroïdie)***
> 	- [ ] Humeur
> 	- [ ] Stress
> 	- [ ] Perte d'intérêt
> 	- [ ] Troubles de la concentration
> 	- [ ] Anxiété
> - [ ] **121. Alimentation *(1 grille sur 11)***
> 	- [ ] Activité physique
> - [ ] **122. Consommations *(Hypothyroïdie)***
> 	- [ ] Tabac
> 	- [ ] OH
> 	- [ ] Drogues
> - [ ] **123. Alimentation – activité physique *(1 grille sur 11)***
> 	- [ ] Alimentation
> 	- [ ] Activité physique

> [!tip] 🩺 Status
> - [ ] **1. Mesures d'hygiène *(Hépatite C aiguë · Mononucléose · Syndrome de Sheehan (hypopituitarisme post-partum))***
> 	- [ ] Lavage des mains
> 	- [ ] Respect de la pudeur avec drap
> - [ ] **2. Examen de la tête et du cou *(Syndrome de Sheehan (hypopituitarisme post-partum))***
> 	- [ ] Inspection de la tête
> 	- [ ] Inspection des conjonctives
> 	- [ ] Examen de la glande thyroïde
> - [ ] **3. Examen cardiovasculaire *(Syndrome de Sheehan (hypopituitarisme post-partum))***
> 	- [ ] Palpation du pouls radial
> 	- [ ] Auscultation cardiaque
> - [ ] **4. Examen des extrémités et cutané *(Mononucléose · Syndrome de Sheehan (hypopituitarisme post-partum))***
> 	- [ ] Inspection des membres inférieurs
> 	- [ ] Examen cutané
> - [ ] **5. Examen neurologique *(Anémie · Mononucléose · Syndrome de Sheehan (hypopituitarisme post-partum))***
> 	- [ ] Évaluation de l'orientation dans le temps, l'espace et les personnes *(Syndrome de Sheehan (hypopituitarisme post-partum))*
> 	- [ ] Examen ciblé de l'état mental *(Syndrome de Sheehan (hypopituitarisme post-partum))*
> 	- [ ] Examen ciblé des mouvements passifs et actifs *(Syndrome de Sheehan (hypopituitarisme post-partum))*
> 	- [ ] Examen ciblé des réflexes ostéo-tendineux *(Mononucléose · Syndrome de Sheehan (hypopituitarisme post-partum))*
> 	- [ ] Sensibilité profonde *(Anémie)*
> 	- [ ] Réflexes ostéo-tendineux *(Anémie)*
> 	- [ ] Signe de Romberg *(Anémie)*
> - [ ] **6. Examen de la tête, yeux, oreilles, nez et gorge *(Hépatite C aiguë · Mononucléose)***
> 	- [ ] Inspection des conjonctives *(Mononucléose)*
> 	- [ ] Inspection de l'oropharynx *(Mononucléose)*
> 	- [ ] Inspection des sclères *(Hépatite C aiguë)*
> - [ ] **7. Examen du cou *(Mononucléose)***
> 	- [ ] Inspection du cou
> 	- [ ] Palpation des ganglions lymphatiques de la tête et du cou
> 	- [ ] Examen de la glande thyroïde
> - [ ] **8. Examen abdominal *(Hépatite C aiguë · Mononucléose · SAOS)***
> 	- [ ] Palpation du foie *(Hépatite C aiguë · Mononucléose)*
> 	- [ ] Palpation de la rate *(Hépatite C aiguë · Mononucléose)*
> 	- [ ] Inspection de l'abdomen *(Hépatite C aiguë)*
> 	- [ ] Auscultation de l'abdomen *(Hépatite C aiguë)*
> 	- [ ] Percussion de l'abdomen *(Hépatite C aiguë)*
> 	- [ ] Palpation de l'abdomen *(Hépatite C aiguë)*
> 	- [ ] Matité déclive *(Hépatite C aiguë)*
> - [ ] **9. Examen thoracique *(Hépatite C aiguë)***
> 	- [ ] Inspection du thorax
> - [ ] **10. Examen des extrémités *(Hépatite C aiguë)***
> 	- [ ] Inspection des mains
> 	- [ ] Inspection des membres inférieurs
> - [ ] **11. État général *(Hémorragie digestive haute sur ulcère peptique)***
> - [ ] **12. Paramètres vitaux *(Hémorragie digestive haute sur ulcère peptique)***
> - [ ] **13. Statut volémique *(Hémorragie digestive haute sur ulcère peptique)***
> - [ ] **14. Signes d’anémie *(Hémorragie digestive haute sur ulcère peptique)***
> - [ ] **15. Coloration cutanée *(Hémorragie digestive haute sur ulcère peptique)***
> - [ ] **16. Conjonctives *(Hémorragie digestive haute sur ulcère peptique)***
> - [ ] **17. Inspection *(Hémorragie digestive haute sur ulcère peptique)***
> - [ ] **18. Auscultation *(Hémorragie digestive haute sur ulcère peptique)***
> - [ ] **19. Percussion *(Hémorragie digestive haute sur ulcère peptique)***
> - [ ] **20. Palpation *(Hémorragie digestive haute sur ulcère peptique)***
> - [ ] **21. Palpation abdominale *(Anémie · Hémorragie digestive haute sur ulcère peptique)***
> 	- [ ] Hépatomégalie *(Anémie)*
> 	- [ ] Splénomégalie *(Anémie)*
> - [ ] **22. Signes de péritonisme *(Hémorragie digestive haute sur ulcère peptique)***
> - [ ] **23. Foie et rate *(Hémorragie digestive haute sur ulcère peptique)***
> - [ ] **24. Vésicule biliaire *(Hémorragie digestive haute sur ulcère peptique)***
> - [ ] **25. TR *(Hémorragie digestive haute sur ulcère peptique)***
> - [ ] **26. Auscultation cardiopulmonaire *(Hémorragie digestive haute sur ulcère peptique)***
> - [ ] **27. Perfusion périphérique *(Hémorragie digestive haute sur ulcère peptique)***
> - [ ] **28. Examen cardio-pulmonaire *(SAOS)***
> - [ ] **29. Examen neurologique sommaire *(SAOS)***
> - [ ] **30. Mesure de la tension artérielle *(SAOS)***
> - [ ] **31. Inspection ORL *(SAOS)***
> 	- [ ] Évaluation des voies aériennes supérieures
> 	- [ ] Recherche d'hypertrophie amygdalienne
> 	- [ ] Évaluation du palais
> - [ ] **32. Évaluation morphologique *(SAOS)***
> 	- [ ] IMC calculé (29 kg/m² - surpoids)
> 	- [ ] Circonférence cervicale
> 	- [ ] Morphologie faciale
> - [ ] **33. Inspection de la pâleur *(Anémie)***
> 	- [ ] Pâleur cutanée
> 	- [ ] Pâleur des muqueuses
> 	- [ ] Pâleur des plis palmaires
> - [ ] **34. Recherche d'ictère *(Anémie)***
> - [ ] **35. Examen de la cavité buccale *(Anémie)***
> 	- [ ] Chéilite angulaire
> 	- [ ] Aspect de la langue
> 	- [ ] Glossite
> - [ ] **36. Auscultation cardiovasculaire *(Anémie)***
> 	- [ ] Fréquence cardiaque
> 	- [ ] Tension artérielle
> 	- [ ] Souffle cardiaque
> 	- [ ] Bruits vasculaires
> - [ ] **37. Palpation des aires ganglionnaires *(Anémie · Diabète de type 2)***
> 	- [ ] Cervicales *(Diabète de type 2)*
> 	- [ ] Axillaires *(Diabète de type 2)*
> 	- [ ] Inguinales *(Diabète de type 2)*
> - [ ] **38. État mental et présentation *(Dépression)***
> 	- [ ] Contact visuel
> 	- [ ] Hygiène et tenue vestimentaire
> 	- [ ] Attitude générale
> 	- [ ] Collaboration
> - [ ] **39. Humeur et affect *(Dépression)***
> 	- [ ] Humeur subjective
> 	- [ ] Affect observé
> 	- [ ] Congruence humeur-affect
> - [ ] **40. Discours et pensée *(Dépression)***
> 	- [ ] Débit et quantité
> 	- [ ] Organisation de la pensée
> 	- [ ] Contenu (idées suicidaires, délirantes)
> - [ ] **41. Perceptions *(Dépression)***
> 	- [ ] Hallucinations
> 	- [ ] Illusions
> 	- [ ] Déréalisation/dépersonnalisation
> - [ ] **42. Fonctions cognitives *(Dépression)***
> 	- [ ] Orientation temporo-spatiale
> 	- [ ] Attention et concentration
> 	- [ ] Mémoire
> - [ ] **43. Jugement et insight *(Dépression)***
> 	- [ ] Conscience du trouble
> 	- [ ] Capacité de jugement
> - [ ] **44. Examen physique de base *(Dépression)***
> 	- [ ] Signes vitaux
> 	- [ ] Examen neurologique sommaire
> 	- [ ] Recherche de signes d'automutilation
> - [ ] **45. Palpation de la thyroïde *(Diabète de type 2)***
> - [ ] **46. Palpation et percussion des loges rénales *(Diabète de type 2)***
> - [ ] **47. Status cardiaque *(Diabète de type 2)***
> 	- [ ] Auscultation des aires cardiaques (les quatre)
> 	- [ ] Auscultation de la carotide
> 	- [ ] Signe du godet
> 	- [ ] Palpation du choc de pointe
> 	- [ ] Vérification de la présence d'une cyanose périphérique ou centrale
> - [ ] **48. Désinfection des mains *(Dépression gériatrique)***
> - [ ] **49. Posé ≥ 1 question relatif au status psychiatrique *(Dépression gériatrique)***
> - [ ] **50. Palpation thyroïde (médecin derrière le patient) *(Dépression gériatrique)***
> - [ ] **51. Palpation ganglions cervicaux & axillaires *(Dépression gériatrique)***
> - [ ] **52. Général : examen rapide de la peau - examen des sclères *(Hypothyroïdie)***
> 	- [ ] Si réalisé, dire *(1 grille sur 11)*
> 	- [ ] Examen rapide de la peau *(1 grille sur 11)*
> 	- [ ] Examen des sclères *(1 grille sur 11)*
> - [ ] **53. Recherche d'adénopathies cervicales - sus-claviculaires *(Hypothyroïdie)***
> 	- [ ] Cervicales *(1 grille sur 11)*
> 	- [ ] Sus-claviculaires *(1 grille sur 11)*
> - [ ] **54. Palpation de la glande thyroïde *(Hypothyroïdie)***
> - [ ] **55. Auscultation cardiaque correctement réalisé *(Hypothyroïdie)***
> 	- [ ] 4 foyers *(1 grille sur 11)*
> 	- [ ] NON = incomplet ou non réalisé *(1 grille sur 11)*
> 	- [ ] ET postérieur *(1 grille sur 11)*
> 	- [ ] Auscultation des 4 foyers *(1 grille sur 11)*
> - [ ] **56. Auscultation pulmonaire (antérieure et postérieure) *(Hypothyroïdie)***
> - [ ] **57. Examen abdominal : palpation 4 quadrants - recherche d'hépatosplénomégalie *(Hypothyroïdie)***
> 	- [ ] Palpation des 4 quadrants *(1 grille sur 11)*
> 	- [ ] Recherche d'hépatosplénomégalie *(1 grille sur 11)*
> - [ ] **58. Examen des ROT au niveau du genou ou de la cheville ou au moins sur 1 site *(Hypothyroïdie)***
> 	- [ ] Ralentissement de la phase de relaxation des ROT

> [!success] 💊 Management — partagé par plusieurs diagnostics
> - [ ] **1. Hypothèses diagnostiques *(3 grilles sur 11)* — *Hépatite C aiguë · Mononucléose · Syndrome de Sheehan (hypopituitarisme post-partum)***
> - [ ] **2. Communication avec la patiente *(2 grilles sur 11)* — *Mononucléose · Syndrome de Sheehan (hypopituitarisme post-partum)***
> 	- [ ] Explications à la patiente des impressions diagnostiques préliminaires
> 	- [ ] Explication du plan de prise en charge
> 	- [ ] Utilisation d'un langage non médical et clarification des termes médicaux
> 	- [ ] Évaluation de l'accord de la patiente avec le plan diagnostique
> 	- [ ] Recherche des préoccupations et questions de la patiente
> - [ ] **3. Diagnostic de suspicion principal *(2 grilles sur 11)* — *Dépression · SAOS***
> - [ ] **4. Diagnostics différentiels évoqués *(3 grilles sur 11)* — *Anémie · Dépression · SAOS***
> - [ ] **5. Traitement proposé *(2 grilles sur 11)* — *Dépression · SAOS***

> [!success] 💊 Management — si Anémie
> - [ ] **1. Examens complémentaires proposés**
> 	- [ ] FSC complète
> 	- [ ] Bilan martial
> 	- [ ] Bilan inflammatoire
> 	- [ ] Bilan d'hémolyse
> 	- [ ] Frottis sanguin
> 	- [ ] Test de recherche de sang occulte dans les selles
> - [ ] **2. Reconnaissance d'une anémie ferriprive**
> 	- [ ] Caractéristiques biologiques
> 	- [ ] Ferritine basse
> - [ ] **3. Traitement de l'anémie ferriprive**
> - [ ] **4. Reconnaissance d'une carence en vitamine B12/folates**
> 	- [ ] Caractéristiques biologiques
> 	- [ ] Dosages spécifiques
> - [ ] **5. Examens étiologiques selon l'orientation**
> 	- [ ] Si suspicion saignement GI
> 	- [ ] Si suspicion maladie médullaire
> 	- [ ] Si hyperménorrhée
> - [ ] **6. Surveillance et suivi**
> 	- [ ] Contrôle de l'efficacité
> 	- [ ] Contrôle de la ferritine
> 	- [ ] Recherche et traitement de la cause

> [!success] 💊 Management — si Dépression
> - [ ] **1. Examens complémentaires proposés**
> 	- [ ] FSC
> 	- [ ] TSH
> 	- [ ] Bilan métabolique de base
> - [ ] **2. Évaluation de la sévérité et du risque**
> 	- [ ] Risque suicidaire élevé (idées actives, antécédents familiaux)
> 	- [ ] Isolement social important
> 	- [ ] Facteurs de protection limités
> - [ ] **3. Plan de sécurité et suivi**
> 	- [ ] Contrat de non-passage à l'acte
> 	- [ ] Numéros d'urgence fournis
> 	- [ ] Prochain rendez-vous fixé dans 3-7 jours
> 	- [ ] Implication d'un proche si possible
> - [ ] **4. Critères d'hospitalisation**
> 	- [ ] Risque suicidaire imminent
> 	- [ ] Absence de soutien social
> 	- [ ] Incapacité à garantir sa sécurité

> [!success] 💊 Management — si Dépression gériatrique
> - [ ] **1. Un laboratoire (pas besoin de préciser)**
> - [ ] **2. Évoqué à voix haute une dépression / demandé à la patiente si elle se sentait déprimée**
> - [ ] **3. Évoquer l'aide à domicile**
> - [ ] **4. Proposé une prise en charge psycho-gériatrique**
> - [ ] **5. Expliqué qu'il fallait activement rechercher une cause organique à la fatigue**
> - [ ] **6. Refusé de prescrire des somnifères pour le moment**

> [!success] 💊 Management — si Diabète de type 2
> - [ ] **1. L'étudiant/e a-t-elle/il évoqué comme diagnostic principal le diabète?**
> - [ ] **2. Évoquer un diagnostic différentiel plausible**
> 	- [ ] Syndrome d'apnée du sommeil obstructif
> 	- [ ] Hypothyroïdie
> 	- [ ] Psychiatrique (burnout/dépression)
> 	- [ ] Anémie
> 	- [ ] Infection (ex: EBV, CMV, VIH)

> [!success] 💊 Management — si Diabète inaugural / Acido-cétose
> *Aucune grille du corpus ne documente ce diagnostic* — il est pourtant attendu de cette SSP. **Trou de révision à combler ailleurs.**

> [!success] 💊 Management — si Hémorragie digestive haute sur ulcère peptique
> - [ ] **1. Laboratoire**
> - [ ] **2. Hb et hémogramme**
> - [ ] **3. CRP**
> - [ ] **4. Statut martial**
> - [ ] **5. Ferritine**
> - [ ] **6. Diagnostic de travail**
> - [ ] **7. Évaluation du risque**
> - [ ] **8. Adapter la médication**
> - [ ] **9. Arrêt des AINS**
> - [ ] **10. Pause de l’ASA**
> - [ ] **11. Pause de l’anticoagulation**
> - [ ] **12. Laisser à jeun**
> - [ ] **13. Orientation hospitalière**
> - [ ] **14. Mesures hospitalières**
> - [ ] **15. IPP i.v.**
> - [ ] **16. Remplissage i.v.**
> - [ ] **17. Bilan H. pylori**
> - [ ] **18. Œsophagogastroduodénoscopie**

> [!success] 💊 Management — si Hépatite C aiguë
> - [ ] **1. Conseil et soutien**
> 	- [ ] Conseil sur les drogues illicites
> 	- [ ] Conseil sur l'abus d'alcool
> 	- [ ] Conseil sur l'arrêt du tabac
> 	- [ ] Réaction appropriée au défi concernant le test VIH
> - [ ] **2. Examens complémentaires urgents**
> 	- [ ] US abdominal
> 	- [ ] FSC
> 	- [ ] TP, TCA
> 	- [ ] ASAT, ALAT, bilirubine, phosphatases alcalines, Gamma-GT, lipase
> 	- [ ] Albumine
> 	- [ ] Sérologies virales hépatites (HAV, HBV, HCV)
> 	- [ ] Test VIH
> - [ ] **3. Examens complémentaires différés**
> 	- [ ] CT abdominal avec contraste
> - [ ] **4. Communication avec le patient**
> 	- [ ] Explications au patient des impressions diagnostiques préliminaires
> 	- [ ] Explication du plan de prise en charge
> 	- [ ] Utilisation d'un langage non médical et clarification des termes médicaux
> 	- [ ] Évaluation de l'accord du patient avec le plan diagnostique
> 	- [ ] Recherche des préoccupations et questions du patient

> [!success] 💊 Management — si Hypothyroïdie
> - [ ] **1. Demande un laboratoire**
> 	- [ ] FSC
> 	- [ ] Ferritine
> 	- [ ] VS / CRP
> 	- [ ] Fonction rénale
> 	- [ ] Fonction hépatique
> 	- [ ] Électrolytes
> 	- [ ] Glycémie
> - [ ] **2. Demande des tests thyroïdiens (TSH seule ou avec T4 libre)**
> - [ ] **3. Interprète correctement les résultats de laboratoire (TSH augmentée et T4 libre abaissée = hypothyroïdie)**
> - [ ] **4. Diagnostic : hypothyroïdie - primaire OU d'origine autoimmune probable**
> 	- [ ] Hypothyroïdie primaire *(1 grille sur 2)*
> 	- [ ] D'origine auto-immune probable *(1 grille sur 2)*
> - [ ] **5. Cite le diagnostic mentionné au point 4 comme diagnostic plus probable**
> - [ ] **6. Propose un dosage des anticorps anti-TPO**
> - [ ] **7. Traitement : substitution par hormones thyroïdiennes (lévothyroxine)**
> - [ ] **8. Suivi : prévoir un contrôle biologique dans un délai de 6-8 semaines - informations sur symptômes de surdosage**
> 	- [ ] Contrôle biologique dans un délai de 6-8 semaines *(1 grille sur 2)*
> 	- [ ] Informations sur les symptômes de surdosage *(1 grille sur 2)*

> [!success] 💊 Management — si Insuffisance cardiaque (décompensée)
> *Aucune grille de cette SSP ne documente ce diagnostic* — mais le corpus le documente ailleurs : [[Mémento — Dyspnée]] (3 grilles) · [[Mémento — Palpitations]] (1 grille) · [[Mémento — Toux]] (1 grille) · [[Mémento — Œdèmes des Membres Inférieurs]] (1 grille).

> [!success] 💊 Management — si Mononucléose
> - [ ] **1. Examens complémentaires de première intention**
> 	- [ ] Test monospot
> 	- [ ] Sérologie EBV
> 	- [ ] FSC et frottis sanguin
> - [ ] **2. Conseil et soutien**
> 	- [ ] Conseil sur l'évitement des sports de contact en cas de mononucléose suspectée
> 	- [ ] Réaction appropriée au défi sur l'expérience du médecin
> 	- [ ] Éducation sur le repos nécessaire
> 	- [ ] Information sur la durée possible de la fatigue
> 	- [ ] Conseils de prévention transmission
> - [ ] **3. Examens complémentaires biologiques**
> 	- [ ] LDH, ASAT, ALAT
> 	- [ ] Fer sérique, ferritine, transferrine, capacité totale de fixation du fer (TIBC)
> 	- [ ] TSH, T3 libre, T4 libre

> [!success] 💊 Management — si SAOS
> - [ ] **1. Examens complémentaires proposés**
> 	- [ ] Biologie
> 	- [ ] Gazométrie artérielle
> 	- [ ] ECG
> 	- [ ] Radiographie thoracique
> 	- [ ] Polysomnographie
> - [ ] **2. Information sur les risques et complications**
> 	- [ ] Risque cardiovasculaire augmenté
> 	- [ ] Hypertension artérielle
> 	- [ ] Risque d'infarctus du myocarde
> 	- [ ] Risque d'accident vasculaire cérébral
> - [ ] **3. Planification du suivi**
> 	- [ ] Consultation pneumologique pour polysomnographie
> 	- [ ] Suivi tensionnel régulier
> 	- [ ] Réévaluation après mise en place du traitement

> [!success] 💊 Management — si Syndrome de Sheehan (hypopituitarisme post-partum)
> - [ ] **1. Examens complémentaires de première intention**
> 	- [ ] Dosages hormonaux hypophysaires : cortisol sérique, ACTH
> 	- [ ] Dosages hormonaux gonadiques : œstradiol, FSH, LH
> 	- [ ] IGF-1
> 	- [ ] TSH
> 	- [ ] Électrolytes sériques, glucose
> - [ ] **2. Examens complémentaires hématologiques**
> 	- [ ] FSC, VGM, TCMH
> 	- [ ] Fer sérique, ferritine, TIBC
> 	- [ ] Frottis sanguin
> - [ ] **3. Imagerie spécialisée**
> 	- [ ] IRM cérébrale
> - [ ] **4. Conseil et soutien**
> 	- [ ] Conseil sur les modifications du mode de vie pour améliorer l'humeur
> 	- [ ] Réaction appropriée au défi sur la maternité
> 	- [ ] Orientation vers assistance sociale
> 	- [ ] Éducation sur l'importance du soutien familial
> 	- [ ] Information sur les ressources de soutien post-partum
