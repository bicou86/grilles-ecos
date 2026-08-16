---
aliases:
  - "Mémento Toux"
type: memento-ecos-ssp
ssp: "Toux"
cas: 13
diagnostics: 8
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

> [!warning] Mémento mixte — 1 grille officielle, 12 non officielles
> **RESCOS-63b** fait partie des **neuf grilles officielles** et fait donc
> autorité ; elle est signalée ⭐️ dans l'encadré ci-dessous. Les 12
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

# Toux

*13 grilles · 8 diagnostics documentés · 1 attendu documenté ailleurs · 1 attendu absent du corpus* — [[SSP — Toux]]

> [!abstract] Les 13 grilles fusionnées
> - **AMBOSS-18** — Asthme `premier-dd` · [grille](<file:///Users/damienfulliquet/Developer/GitHub/grilles-ecos/cases/amboss/AMBOSS-18_-_Toux_chronique_-_Femme_21_ans_-_Grille_ECOS.html>)
> - **AMBOSS-19** — BPCO `premier-dd` · [grille](<file:///Users/damienfulliquet/Developer/GitHub/grilles-ecos/cases/amboss/AMBOSS-19_-_Toux_chronique_-_Femme_53_ans_-_Grille_ECOS.html>)
> - **AMBOSS-31** — Cancer pulmonaire `premier-dd` · [grille](<file:///Users/damienfulliquet/Developer/GitHub/grilles-ecos/cases/amboss/AMBOSS-31_-_Toux_-_Homme_58_ans_-_Grille_ECOS.html>)
> - **AZYGOS-47** — Pneumonie `diagnostic-travail` · [grille](<file:///Users/damienfulliquet/Developer/GitHub/grilles-ecos/.azygos-extraction/ccef5f83-9402-4ac8-ac18-913d834bc565.json>)
> - **German-75** — Tuberculose `corrige` · [grille](<file:///Users/damienfulliquet/Developer/GitHub/grilles-ecos/cases/german/German-75_-_Toux_-_Grille_ECOS.html>)
> - **German-76** — Insuffisance cardiaque (décompensée) `corrige` · [grille](<file:///Users/damienfulliquet/Developer/GitHub/grilles-ecos/cases/german/German-76_-_Toux_-_Grille_ECOS.html>)
> - **German-77** — Pneumonie `corrige` · [grille](<file:///Users/damienfulliquet/Developer/GitHub/grilles-ecos/cases/german/German-77_-_Toux_-_Grille_ECOS.html>)
> - **German-78** — Asthme `corrige` · [grille](<file:///Users/damienfulliquet/Developer/GitHub/grilles-ecos/cases/german/German-78_-_Toux_-_Grille_ECOS.html>)
> - **German-79** — Faux-croup `corrige` · [grille](<file:///Users/damienfulliquet/Developer/GitHub/grilles-ecos/cases/german/German-79_-_Toux_-_Consultation_te_le_phonique_-_Pe_diatrie_-_Grille_ECOS.html>)
> - **RESCOS-62** — Pneumonie `premier-dd` · [grille](<file:///Users/damienfulliquet/Developer/GitHub/grilles-ecos/cases/rescos/RESCOS-62%20-%20Toux%20-%20ECC%20Poumon%20-%20Grille%20ECOS.html>)
> - **RESCOS-63** — Coqueluche `explicite` · [grille](<file:///Users/damienfulliquet/Developer/GitHub/grilles-ecos/cases/rescos/RESCOS-63%20-%20Toux%20-%20Pédiatrie%20-%20Grille%20ECOS.html>)
> - **RESCOS-63b** ⭐️ **officielle** — Coqueluche `explicite` · [grille](<file:///Users/damienfulliquet/Developer/GitHub/grilles-ecos/cases/rescos/RESCOS-63b%20-%20Toux%20-%20Pédiatrie%20-%20Grille%20ECOS.html>)
> - **RESCOS-64-1** — Cancer pulmonaire `explicite` · [grille](<file:///Users/damienfulliquet/Developer/GitHub/grilles-ecos/cases/rescos/RESCOS-64%20-%20Toux%20-%20Station%20double%201%20-%20Grille%20ECOS.html>)

> [!note] 📋 Anamnèse
> - [ ] **1. Motif principal *(3 grilles sur 13)***
> - [ ] **2. Caractérisation de la toux *(6 grilles sur 13)***
> 	- [ ] Toux productive d'expectorations *(1 grille sur 13)*
> 	- [ ] Couleur des expectorations *(3 grilles sur 13)*
> 	- [ ] Volume des expectorations *(2 grilles sur 13)*
> 	- [ ] Sang dans les expectorations *(2 grilles sur 13)*
> 	- [ ] Début *(2 grilles sur 13)*
> 	- [ ] Constant/intermittent *(2 grilles sur 13)*
> 	- [ ] Événements précipitants *(2 grilles sur 13)*
> 	- [ ] Progression *(2 grilles sur 13)*
> 	- [ ] Épisodes antérieurs *(2 grilles sur 13)*
> 	- [ ] Fréquence *(2 grilles sur 13)*
> 	- [ ] Facteurs améliorants *(2 grilles sur 13)*
> 	- [ ] Facteurs aggravants *(2 grilles sur 13)*
> 	- [ ] Toux productive *(BPCO)*
> 	- [ ] Productive ou sèche *(1 grille sur 13)*
> 	- [ ] Début et fréquence *(1 grille sur 13)*
> 	- [ ] Antécédents similaires *(1 grille sur 13)*
> 	- [ ] Son *(Faux-croup)*
> 	- [ ] Type *(Faux-croup)*
> 	- [ ] Productive ou non *(Faux-croup)*
> 	- [ ] Type de toux *(1 grille sur 13)*
> 	- [ ] Horaire *(1 grille sur 13)*
> 	- [ ] Facteurs déclenchants *(1 grille sur 13)*
> 	- [ ] Durée et évolution *(1 grille sur 13)*
> 	- [ ] Efficacité de la toux *(1 grille sur 13)*
> - [ ] **3. Symptômes associés *(4 grilles sur 13)***
> 	- [ ] Anxiété *(1 grille sur 13)*
> 	- [ ] Nervosité *(1 grille sur 13)*
> 	- [ ] Sueurs *(1 grille sur 13)*
> - [ ] **4. Recherche de symptômes spécifiques *(2 grilles sur 13)***
> 	- [ ] Voyage récent
> 	- [ ] Céphalées *(1 grille sur 13)*
> 	- [ ] Nausées/vomissements *(1 grille sur 13)*
> 	- [ ] Fièvre/frissons
> 	- [ ] Sueurs nocturnes
> 	- [ ] Fatigue
> 	- [ ] Palpitations
> 	- [ ] Douleur thoracique
> 	- [ ] Problèmes urinaires
> 	- [ ] Problèmes intestinaux
> 	- [ ] Problèmes de sommeil *(1 grille sur 13)*
> 	- [ ] Appétit
> 	- [ ] Variations pondérales
> 	- [ ] Infections récentes
> 	- [ ] Symptômes d'infection respiratoire haute
> 	- [ ] Exposition à la tuberculose *(1 grille sur 13)*
> 	- [ ] Exposition aux fumées/poussières *(1 grille sur 13)*
> 	- [ ] Exposition aux animaux/animaux domestiques *(1 grille sur 13)*
> 	- [ ] Œdème des chevilles *(BPCO)*
> 	- [ ] Essoufflement *(BPCO)*
> 	- [ ] Problèmes de sommeil, plusieurs oreillers *(BPCO)*
> 	- [ ] Exposition à la tuberculose, dernier test cutané *(BPCO)*
> - [ ] **5. Antécédents médicaux personnels *(6 grilles sur 13)***
> 	- [ ] Maladies chroniques *(Tuberculose)*
> 	- [ ] Immunosuppression *(Tuberculose)*
> 	- [ ] Hospitalisations *(Tuberculose)*
> 	- [ ] Chirurgies *(Tuberculose)*
> 	- [ ] Hypertension artérielle *(1 grille sur 13)*
> 	- [ ] Toux chronique *(1 grille sur 13)*
> - [ ] **6. Allergies *(6 grilles sur 13)***
> 	- [ ] Allergies connues *(Tuberculose)*
> 	- [ ] Manifestations allergiques *(Tuberculose)*
> 	- [ ] Traitements antiallergiques *(Tuberculose)*
> 	- [ ] Tests allergologiques antérieurs *(Tuberculose)*
> - [ ] **7. Médicaments *(4 grilles sur 13)***
> 	- [ ] Médicaments actuels *(1 grille sur 13)*
> 	- [ ] Efficacité contre symptômes actuels *(1 grille sur 13)*
> - [ ] **8. Hospitalisations et antécédents chirurgicaux *(3 grilles sur 13)***
> 	- [ ] Hospitalisations
> 	- [ ] Antécédents chirurgicaux
> - [ ] **9. Contacts malades *(2 grilles sur 13)***
> - [ ] **10. Antécédents familiaux *(5 diagnostics)***
> 	- [ ] Maladies pulmonaires familiales *(Tuberculose)*
> 	- [ ] Tuberculose familiale *(Tuberculose)*
> 	- [ ] Allergies familiales *(2 grilles sur 13)*
> 	- [ ] Maladies génétiques *(Tuberculose)*
> 	- [ ] Maladies cardiovasculaires *(Insuffisance cardiaque (décompensée))*
> 	- [ ] Diabète *(Insuffisance cardiaque (décompensée))*
> 	- [ ] Hypertension *(Insuffisance cardiaque (décompensée))*
> 	- [ ] Mort subite *(Insuffisance cardiaque (décompensée))*
> 	- [ ] Mère *(1 grille sur 13)*
> 	- [ ] Père *(1 grille sur 13)*
> 	- [ ] Pathologies pulmonaires *(1 grille sur 13)*
> 	- [ ] Pathologies cardiovasculaires *(1 grille sur 13)*
> 	- [ ] Cancers *(1 grille sur 13)*
> 	- [ ] Maladies héréditaires *(1 grille sur 13)*
> - [ ] **11. Habitudes et mode de vie *(5 grilles sur 13)***
> 	- [ ] Occupation *(1 grille sur 13)*
> 	- [ ] Domicile *(3 grilles sur 13)*
> 	- [ ] Alcool
> 	- [ ] Drogues illicites *(1 grille sur 13)*
> 	- [ ] Tabac
> 	- [ ] Exercice *(2 grilles sur 13)*
> 	- [ ] Travail *(2 grilles sur 13)*
> 	- [ ] Drogues récréatives *(2 grilles sur 13)*
> 	- [ ] Drogues *(2 grilles sur 13)*
> - [ ] **12. Caractérisation de la toux et des expectorations *(1 grille sur 13)***
> 	- [ ] Productive
> 	- [ ] Couleur
> 	- [ ] Sang
> 	- [ ] Volume
> 	- [ ] Début
> 	- [ ] Évolution temporelle
> 	- [ ] Événements précipitants
> 	- [ ] Progression
> 	- [ ] Épisodes antérieurs
> 	- [ ] Fréquence
> 	- [ ] Facteurs améliorants
> 	- [ ] Facteurs aggravants
> 	- [ ] Symptômes associés
> - [ ] **13. Recherche de symptômes spécifiques pour toux chronique et hémoptysie *(1 grille sur 13)***
> 	- [ ] Voyage récent
> 	- [ ] Fièvre/frissons
> 	- [ ] Sueurs nocturnes
> 	- [ ] Fatigue
> 	- [ ] Éruption cutanée/changements cutanés
> 	- [ ] Douleur thoracique
> 	- [ ] Douleur aggravée par respiration profonde
> 	- [ ] Dyspnée
> 	- [ ] Troubles du sommeil
> 	- [ ] Appétit
> 	- [ ] Variations pondérales
> 	- [ ] Perte de poids intentionnelle
> 	- [ ] Infections récentes
> 	- [ ] Symptômes d'infection respiratoire haute
> - [ ] **14. Exposition à la tuberculose et dépistage *(1 grille sur 13)***
> 	- [ ] Exposition à la tuberculose
> 	- [ ] Dernier test tuberculinique
> - [ ] **15. Expositions environnementales et symptômes neurologiques *(1 grille sur 13)***
> 	- [ ] Exposition aux animaux
> 	- [ ] Exposition aux moisissures
> 	- [ ] Faiblesse musculaire
> 	- [ ] Picotements/engourdissements
> - [ ] **16. Contacts malades et antécédents familiaux *(1 grille sur 13)***
> 	- [ ] Contacts malades
> 	- [ ] Antécédents familiaux
> - [ ] **17. Question d’introduction *(1 grille sur 13)***
> - [ ] **18. Dimension temporelle *(1 grille sur 13)***
> - [ ] **19. Début / durée *(1 grille sur 13)***
> - [ ] **20. Apparition *(1 grille sur 13)***
> - [ ] **21. Évolution *(1 grille sur 13)***
> - [ ] **22. Déclencheurs *(1 grille sur 13)***
> - [ ] **23. Facteurs aggravants / survenue situationnelle *(1 grille sur 13)***
> - [ ] **24. Facteurs soulageants / mesures prises jusqu’ici *(1 grille sur 13)***
> - [ ] **25. Retentissement des symptômes *(1 grille sur 13)***
> - [ ] **26. Dyspnée *(2 grilles sur 13)***
> 	- [ ] Présence *(1 grille sur 13)*
> 	- [ ] Circonstances *(1 grille sur 13)*
> - [ ] **27. Survenue situationnelle *(1 grille sur 13)***
> - [ ] **28. Expectoration *(2 grilles sur 13)***
> - [ ] **29. Aspect / couleur / hémoptysie *(1 grille sur 13)***
> - [ ] **30. Signes d’infection *(1 grille sur 13)***
> - [ ] **31. Fièvre *(3 grilles sur 13)***
> 	- [ ] Début *(Coqueluche)*
> 	- [ ] Évolution *(Coqueluche)*
> 	- [ ] Température précisée *(Coqueluche)*
> 	- [ ] Réponse aux fébrifuges *(Coqueluche)*
> 	- [ ] Frissons/marbrures *(Coqueluche)*
> - [ ] **32. Frissons *(1 grille sur 13)***
> - [ ] **33. Anamnèse d’exposition / contacts *(1 grille sur 13)***
> - [ ] **34. Infections passées *(1 grille sur 13)***
> - [ ] **35. Symptômes B *(2 grilles sur 13)***
> 	- [ ] Perte de poids *(1 grille sur 13)*
> 	- [ ] Fièvre *(1 grille sur 13)*
> 	- [ ] Sueurs nocturnes *(1 grille sur 13)*
> - [ ] **36. Diagnostic différentiel douleur thoracique *(1 grille sur 13)***
> - [ ] **37. Douleur thoracique *(1 grille sur 13)***
> - [ ] **38. Dépendance respiratoire *(1 grille sur 13)***
> - [ ] **39. Irradiation *(1 grille sur 13)***
> - [ ] **40. Caractère de pression/serrements *(1 grille sur 13)***
> - [ ] **41. Symptômes végétatifs associés *(1 grille sur 13)***
> - [ ] **42. Diagnostic différentiel facteurs de risque de thrombo-embolie *(1 grille sur 13)***
> - [ ] **43. ATCD de MTEV *(1 grille sur 13)***
> - [ ] **44. Immobilisation / opération *(1 grille sur 13)***
> - [ ] **45. Voyage longue distance *(1 grille sur 13)***
> - [ ] **46. Gonflement/douleur unilatéral(e) de jambe *(1 grille sur 13)***
> - [ ] **47. Opérations antérieures *(1 grille sur 13)***
> - [ ] **48. Noxes *(1 grille sur 13)***
> - [ ] **49. Alcool *(1 grille sur 13)***
> - [ ] **50. Tabac *(1 grille sur 13)***
> - [ ] **51. Drogues *(1 grille sur 13)***
> - [ ] **52. Ancienne profession *(1 grille sur 13)***
> - [ ] **53. Environnement / contexte social *(1 grille sur 13)***
> - [ ] **54. Présentation avec nom, fonction et tâche *(4 grilles sur 13)***
> - [ ] **55. Question d'entrée ouverte - Symptôme principal *(Tuberculose)***
> - [ ] **56. Épisodes antérieurs de toux ou problèmes respiratoires *(Tuberculose)***
> 	- [ ] Bronchites récurrentes
> 	- [ ] Fréquence des épisodes
> 	- [ ] Sévérité antérieure
> 	- [ ] Traitements utilisés
> - [ ] **57. Caractérisation temporelle de la toux actuelle *(Tuberculose)***
> 	- [ ] Début
> 	- [ ] Évolution
> 	- [ ] Prédominance horaire
> 	- [ ] Caractère continu ou paroxystique
> - [ ] **58. Caractéristiques de la toux et des expectorations *(Insuffisance cardiaque (décompensée) · Tuberculose)***
> 	- [ ] Type de toux
> 	- [ ] Aspect des expectorations *(Tuberculose)*
> 	- [ ] Quantité
> 	- [ ] Odeur *(Tuberculose)*
> 	- [ ] Couleur des expectorations *(Insuffisance cardiaque (décompensée))*
> 	- [ ] Aspect (mousseux, rosé) *(Insuffisance cardiaque (décompensée))*
> - [ ] **59. Hémoptysie *(3 grilles sur 13)***
> 	- [ ] Présence de sang *(Tuberculose)*
> 	- [ ] Quantité si présente *(Tuberculose)*
> 	- [ ] Aspect (strié, franc) *(Tuberculose)*
> 	- [ ] Fréquence *(Tuberculose)*
> 	- [ ] Présence de sang franc *(Insuffisance cardiaque (décompensée))*
> 	- [ ] Expectorations rosées *(Insuffisance cardiaque (décompensée))*
> 	- [ ] Quantification *(Insuffisance cardiaque (décompensée))*
> - [ ] **60. Symptômes respiratoires associés *(2 grilles sur 13)***
> 	- [ ] Dyspnée *(Tuberculose)*
> 	- [ ] Sifflements respiratoires *(Tuberculose)*
> 	- [ ] Douleurs thoraciques
> 	- [ ] Sensation d'oppression *(Tuberculose)*
> 	- [ ] Dyspnée d'effort *(1 grille sur 13)*
> 	- [ ] Sibilances *(1 grille sur 13)*
> 	- [ ] Caractère de la douleur *(1 grille sur 13)*
> - [ ] **61. Facteurs modulateurs *(Tuberculose)***
> 	- [ ] Facteurs aggravants
> 	- [ ] Facteurs améliorants
> 	- [ ] Position
> 	- [ ] Activité physique
> - [ ] **62. Symptômes ORL associés *(Tuberculose)***
> 	- [ ] Rhinite
> 	- [ ] Pharyngite
> 	- [ ] Écoulement post-nasal
> 	- [ ] Douleurs sinusiennes
> - [ ] **63. Symptômes généraux - Performance *(Tuberculose)***
> 	- [ ] Baisse de performance
> 	- [ ] Fatigue inhabituelle
> 	- [ ] Tolérance à l'effort diminuée
> 	- [ ] Impact sur le travail
> - [ ] **64. Symptômes généraux - Signes B *(Tuberculose)***
> 	- [ ] Perte de poids
> 	- [ ] Fièvre
> 	- [ ] Sueurs nocturnes
> 	- [ ] Anorexie
> - [ ] **65. Symptômes cardiovasculaires *(Insuffisance cardiaque (décompensée) · Tuberculose)***
> 	- [ ] Palpitations
> 	- [ ] Œdèmes *(Tuberculose)*
> 	- [ ] Orthopnée *(Tuberculose)*
> 	- [ ] Dyspnée paroxystique nocturne *(Tuberculose)*
> 	- [ ] Douleurs thoraciques *(Insuffisance cardiaque (décompensée))*
> 	- [ ] Syncopes ou malaises *(Insuffisance cardiaque (décompensée))*
> 	- [ ] Claudication intermittente *(Insuffisance cardiaque (décompensée))*
> - [ ] **66. Symptômes gastro-œsophagiens *(Insuffisance cardiaque (décompensée) · Tuberculose)***
> 	- [ ] Reflux gastro-œsophagien
> 	- [ ] Pyrosis
> 	- [ ] Régurgitations
> 	- [ ] Dysphagie
> - [ ] **67. Exposition professionnelle et contages *(Tuberculose)***
> 	- [ ] Contact avec patients tuberculeux
> 	- [ ] Autres expositions antérieures
> 	- [ ] Protection utilisée
> 	- [ ] Dépistages antérieurs
> - [ ] **68. Exposition environnementale *(Insuffisance cardiaque (décompensée) · Tuberculose)***
> 	- [ ] Poussières/irritants *(Tuberculose)*
> 	- [ ] Animaux
> 	- [ ] Moisissures *(Tuberculose)*
> 	- [ ] Tabagisme passif
> 	- [ ] Professionnelle (peintre) *(Insuffisance cardiaque (décompensée))*
> 	- [ ] Amiante, solvants *(Insuffisance cardiaque (décompensée))*
> - [ ] **69. Traitements médicamenteux *(Tuberculose)***
> 	- [ ] Médicaments actuels
> 	- [ ] IEC (toux médicamenteuse)
> 	- [ ] Immunosuppresseurs
> 	- [ ] Antibiotiques récents
> - [ ] **70. Habitudes et toxiques *(Tuberculose)***
> 	- [ ] Tabagisme
> 	- [ ] Alcool
> 	- [ ] Drogues
> 	- [ ] Exposition professionnelle aux toxiques
> - [ ] **71. Contexte social *(Tuberculose)***
> 	- [ ] Situation familiale
> 	- [ ] Profession
> 	- [ ] Conditions de logement
> 	- [ ] Voyages récents
> - [ ] **72. Question d'entrée ouverte - Plainte principale *(Insuffisance cardiaque (décompensée))***
> - [ ] **73. Épisodes antérieurs similaires *(Insuffisance cardiaque (décompensée))***
> 	- [ ] Première fois avec ces caractéristiques
> 	- [ ] Problèmes respiratoires antérieurs
> 	- [ ] Hospitalisations pour dyspnée
> - [ ] **74. Caractérisation temporelle de la toux *(Insuffisance cardiaque (décompensée))***
> 	- [ ] Début
> 	- [ ] Évolution
> 	- [ ] Installation
> 	- [ ] Prédominance horaire
> - [ ] **75. Dyspnée - Caractérisation détaillée *(Insuffisance cardiaque (décompensée))***
> 	- [ ] Présence
> 	- [ ] Type
> 	- [ ] Classe NYHA
> 	- [ ] Progression récente
> - [ ] **76. Facteurs positionnels *(Insuffisance cardiaque (décompensée))***
> 	- [ ] Aggravation en décubitus
> 	- [ ] Aggravation nocturne
> 	- [ ] Aggravation à l'effort
> 	- [ ] Nombre d'oreillers utilisés
> - [ ] **77. Facteurs d'amélioration *(Insuffisance cardiaque (décompensée))***
> 	- [ ] Position assise
> 	- [ ] Repos
> 	- [ ] Fenêtre ouverte
> 	- [ ] Autres positions
> - [ ] **78. Orthopnée et dyspnée paroxystique nocturne *(Insuffisance cardiaque (décompensée))***
> 	- [ ] Orthopnée (nombre d'oreillers)
> 	- [ ] Réveils nocturnes avec dyspnée
> 	- [ ] Besoin de se lever la nuit
> 	- [ ] Amélioration en position assise
> - [ ] **79. Symptômes ORL et infectieux *(Insuffisance cardiaque (décompensée))***
> 	- [ ] Infection ORL récente
> 	- [ ] Rhinite
> 	- [ ] Pharyngite
> 	- [ ] Fièvre
> - [ ] **80. Performance physique et fatigue *(Insuffisance cardiaque (décompensée))***
> 	- [ ] Baisse de performance
> 	- [ ] Fatigue inhabituelle
> 	- [ ] Limitation des activités quotidiennes
> 	- [ ] Autonomie actuelle
> - [ ] **81. Autres symptômes respiratoires *(Insuffisance cardiaque (décompensée))***
> 	- [ ] Écoulement post-nasal
> 	- [ ] Sifflements respiratoires
> 	- [ ] Sensation d'oppression
> 	- [ ] Toux nocturne
> - [ ] **82. Œdèmes et prise de poids *(Insuffisance cardiaque (décompensée))***
> 	- [ ] Œdèmes des membres inférieurs
> 	- [ ] Prise de poids récente
> 	- [ ] Abdomen gonflé
> 	- [ ] Dyspnée après les repas
> - [ ] **83. Symptômes généraux *(Insuffisance cardiaque (décompensée))***
> 	- [ ] Perte de poids
> 	- [ ] Fièvre
> 	- [ ] Sueurs nocturnes
> 	- [ ] Anorexie
> - [ ] **84. Antécédents cardiovasculaires *(Insuffisance cardiaque (décompensée))***
> 	- [ ] Pathologie cardiaque connue
> 	- [ ] Valvulopathie
> 	- [ ] Infarctus du myocarde
> 	- [ ] Chirurgie cardiaque
> - [ ] **85. Traitements cardiovasculaires actuels *(Insuffisance cardiaque (décompensée))***
> 	- [ ] IEC
> 	- [ ] Bêtabloquant
> 	- [ ] Antiagrégant
> 	- [ ] Statine
> 	- [ ] Observance thérapeutique
> - [ ] **86. Habitudes et facteurs de risque *(2 grilles sur 13)***
> 	- [ ] Tabagisme *(Insuffisance cardiaque (décompensée))*
> 	- [ ] Alcool *(Insuffisance cardiaque (décompensée))*
> 	- [ ] Drogues *(Insuffisance cardiaque (décompensée))*
> 	- [ ] Activité physique actuelle *(Insuffisance cardiaque (décompensée))*
> 	- [ ] Tabagisme actif *(1 grille sur 13)*
> 	- [ ] Profession *(1 grille sur 13)*
> 	- [ ] Consommation d'alcool *(1 grille sur 13)*
> - [ ] **87. Allergies et intolérances *(Insuffisance cardiaque (décompensée))***
> 	- [ ] Allergies médicamenteuses
> 	- [ ] Allergies environnementales
> 	- [ ] Intolérances alimentaires
> - [ ] **88. Contexte social et autonomie *(Insuffisance cardiaque (décompensée))***
> 	- [ ] Situation familiale
> 	- [ ] Vit avec
> 	- [ ] Aide à domicile
> 	- [ ] Autonomie pour les AVQ
> - [ ] **89. Symptômes principaux *(2 grilles sur 13)***
> - [ ] **90. Épisodes antérieurs de symptômes similaires *(1 grille sur 13)***
> - [ ] **91. Début et mode d'apparition *(1 grille sur 13)***
> 	- [ ] Quand
> 	- [ ] Comment
> - [ ] **92. Facteurs aggravants *(1 grille sur 13)***
> - [ ] **93. Facteurs améliorants *(1 grille sur 13)***
> - [ ] **94. Anamnèse de l'entourage (contagion) *(1 grille sur 13)***
> - [ ] **95. Symptômes associés - Infection ORL *(1 grille sur 13)***
> 	- [ ] Rhinorrhée
> 	- [ ] Mal de gorge
> - [ ] **96. Symptômes associés - Baisse de performance *(1 grille sur 13)***
> - [ ] **97. Symptômes associés - Écoulement postnasal *(1 grille sur 13)***
> - [ ] **98. Symptômes associés - Douleurs thoraciques *(1 grille sur 13)***
> 	- [ ] Présence
> 	- [ ] Caractéristiques
> - [ ] **99. Symptômes associés - Symptômes cardiaques *(1 grille sur 13)***
> - [ ] **100. Symptômes associés - Sibilances *(1 grille sur 13)***
> - [ ] **101. Symptômes associés - Reflux gastro-œsophagien *(1 grille sur 13)***
> - [ ] **102. Symptômes associés - Œdèmes des membres inférieurs *(1 grille sur 13)***
> - [ ] **103. Exposition (professionnelle, environnementale) *(1 grille sur 13)***
> - [ ] **104. Médicaments actuels *(2 grilles sur 13)***
> - [ ] **105. Anamnèse sociale *(2 grilles sur 13)***
> 	- [ ] État civil
> 	- [ ] Enfants
> 	- [ ] Situation professionnelle *(1 grille sur 13)*
> 	- [ ] Profession *(1 grille sur 13)*
> - [ ] **106. État actuel *(1 grille sur 13)***
> - [ ] **107. Type de dyspnée *(1 grille sur 13)***
> 	- [ ] Repos ou effort
> 	- [ ] Circonstances de début
> - [ ] **108. Douleurs *(1 grille sur 13)***
> 	- [ ] Douleurs à la toux
> 	- [ ] Autres douleurs
> - [ ] **109. Infection préalable ou concomitante *(1 grille sur 13)***
> - [ ] **110. Symptômes infectieux *(1 grille sur 13)***
> 	- [ ] Fièvre
> 	- [ ] Rhinorrhée
> - [ ] **111. Allergies connues *(1 grille sur 13)***
> - [ ] **112. Antécédents cardiaques *(1 grille sur 13)***
> - [ ] **113. Autres antécédents médicaux *(1 grille sur 13)***
> - [ ] **114. Activités sportives et loisirs *(1 grille sur 13)***
> - [ ] **115. Présentation avec nom et fonction *(Faux-croup)***
> - [ ] **116. Identification complète *(Faux-croup)***
> 	- [ ] Nom, âge et sexe de l'enfant
> 	- [ ] Numéro de téléphone de l'appelant pour rappel
> - [ ] **117. Question ouverte initiale *(Faux-croup)***
> - [ ] **118. Début et circonstances *(Faux-croup)***
> 	- [ ] Début
> 	- [ ] Activités précédentes
> 	- [ ] État actuel
> - [ ] **119. État général actuel de l'enfant *(Faux-croup)***
> 	- [ ] Léthargie
> 	- [ ] Réactivité
> - [ ] **120. Signes de détresse respiratoire *(Faux-croup)***
> 	- [ ] Tirage intercostal
> 	- [ ] Tirage sus-sternal
> 	- [ ] Respiration rapide et superficielle
> - [ ] **121. Température *(Faux-croup)***
> 	- [ ] Fièvre mesurée
> 	- [ ] Sensation thermique
> 	- [ ] Site de mesure si mesuré
> - [ ] **122. Signes d'infection ORL *(Faux-croup)***
> 	- [ ] Nez
> 	- [ ] Gorge
> 	- [ ] Cou
> 	- [ ] Trachée
> - [ ] **123. Caractéristiques de la respiration *(Faux-croup)***
> - [ ] **124. Possibilité d'aspiration de corps étranger *(Faux-croup)***
> - [ ] **125. Coloration cutanée *(Faux-croup)***
> - [ ] **126. Tentatives thérapeutiques *(Faux-croup)***
> - [ ] **127. Recherche de drapeaux rouges (RED FLAGS) *(Faux-croup)***
> 	- [ ] État général, troubles de conscience
> 	- [ ] Foyers fébriles ORL (troubles déglutition, otalgie)
> 	- [ ] Méningisme
> 	- [ ] Signes urinaires
> 	- [ ] Éruption cutanée
> 	- [ ] Traumatisme crânien récent
> - [ ] **128. Antécédents similaires *(Faux-croup)***
> - [ ] **129. Maladies de base *(Faux-croup)***
> - [ ] **130. Hospitalisations antérieures *(Faux-croup)***
> - [ ] **131. Médicaments et allergies *(2 grilles sur 13)***
> - [ ] **132. Anamnèse de l'entourage *(Faux-croup)***
> - [ ] **133. Résumé et confirmation *(Faux-croup)***
> 	- [ ] Fait un bref résumé de la situation
> 	- [ ] Demande confirmation de l'exactitude
> - [ ] **134. Caractérisation des expectorations *(1 grille sur 13)***
> 	- [ ] Couleur des crachats
> 	- [ ] Quantité
> 	- [ ] Odeur
> 	- [ ] Présence de sang
> 	- [ ] Évolution dans le temps
> - [ ] **135. Caractérisation de la douleur thoracique *(1 grille sur 13)***
> 	- [ ] Localisation
> 	- [ ] Reproductible à la palpation
> 	- [ ] Variation avec la respiration
> 	- [ ] Irradiation
> 	- [ ] Intensité
> 	- [ ] Durée et circonstances
> - [ ] **136. Évaluation de la dyspnée *(1 grille sur 13)***
> 	- [ ] Circonstances
> 	- [ ] Classification NYHA ou mMRC
> 	- [ ] Orthopnée
> 	- [ ] Dyspnée paroxystique nocturne
> 	- [ ] Évolution dans le temps
> 	- [ ] Sifflements ou bruits associés
> - [ ] **137. Signes généraux et symptômes associés *(1 grille sur 13)***
> 	- [ ] Fièvre
> 	- [ ] Asthénie et perte de poids
> 	- [ ] Sueurs nocturnes
> 	- [ ] Signes d'insuffisance cardiaque
> 	- [ ] Autres symptômes respiratoires
> - [ ] **138. Antécédents personnels et facteurs de risque *(1 grille sur 13)***
> 	- [ ] Pathologies chroniques
> 	- [ ] Antécédents pulmonaires
> 	- [ ] Hospitalisations antérieures
> 	- [ ] Allergies médicamenteuses
> 	- [ ] Vaccinations
> - [ ] **139. Habitudes et expositions *(1 grille sur 13)***
> 	- [ ] Tabac
> 	- [ ] Alcool
> 	- [ ] Activité physique
> 	- [ ] Exposition professionnelle
> 	- [ ] Exposition infectieuse
> - [ ] **140. Toux *(Coqueluche)***
> 	- [ ] Début
> 	- [ ] Évolution
> 	- [ ] Qualité
> 	- [ ] Fréquence
> 	- [ ] Cyanose
> - [ ] **141. Vomissements *(Coqueluche)***
> 	- [ ] Début
> 	- [ ] Évolution
> 	- [ ] Association avec toux
> 	- [ ] Contenu
> - [ ] **142. Alimentation/Hydratation *(Coqueluche)***
> 	- [ ] Allaitement
> 	- [ ] Couches mouillées
> - [ ] **143. État général *(Coqueluche)***
> 	- [ ] Apathie et/ou fatigue
> - [ ] **144. Anamnèse personnelle *(Coqueluche)***
> 	- [ ] Grossesse
> 	- [ ] Accouchement
> 	- [ ] Néonatale
> 	- [ ] Croissance
> 	- [ ] Développement
> - [ ] **145. Vaccins/Médicaments *(Coqueluche)***
> 	- [ ] Vaccins
> 	- [ ] Médicaments
> - [ ] **146. Contage *(Coqueluche)***
> - [ ] **147. Caractérisation de l'hémoptysie *(1 grille sur 13)***
> 	- [ ] Début et durée
> 	- [ ] Quantité
> 	- [ ] Aspect du sang
> 	- [ ] Évolution
> - [ ] **148. Histoire de la toux chronique *(1 grille sur 13)***
> 	- [ ] Ancienneté
> 	- [ ] Horaire habituel
> 	- [ ] Évolution récente
> 	- [ ] Caractère des expectorations habituelles
> - [ ] **149. Antécédents respiratoires *(1 grille sur 13)***
> 	- [ ] BPCO suspectée par médecin traitant
> 	- [ ] Épisodes de bronchite
> 	- [ ] Participation aux campagnes de dépistage
> - [ ] **150. Symptômes généraux et signes d'alarme *(1 grille sur 13)***
> 	- [ ] Perte de poids
> - [ ] **151. Signes négatifs importants *(1 grille sur 13)***
> 	- [ ] Pas d'œdèmes des membres inférieurs
> 	- [ ] Pas de troubles du sommeil respiratoires
> 	- [ ] Pas de voyage récent
> 	- [ ] Pas d'immobilisation ou antécédent thromboembolique
> - [ ] **152. Antécédents personnels et familiaux *(1 grille sur 13)***
> 	- [ ] Antécédents familiaux
> 	- [ ] Suivi gynécologique régulier
> - [ ] **153. Contexte social et professionnel *(1 grille sur 13)***
> 	- [ ] Situation familiale
> 	- [ ] Profession
> 	- [ ] Impact sur la qualité de vie

> [!tip] 🩺 Status
> - [ ] **1. Mesures d'hygiène *(3 grilles sur 13)***
> 	- [ ] Lavage des mains
> 	- [ ] Respect de la pudeur avec drap
> - [ ] **2. Examen de la tête, yeux, oreilles, nez et gorge *(2 grilles sur 13)***
> 	- [ ] Inspection de l'oropharynx
> - [ ] **3. Examen du cou *(3 grilles sur 13)***
> 	- [ ] Palpation des ganglions lymphatiques de la tête et du cou
> 	- [ ] Évaluation de la distension veineuse jugulaire *(BPCO)*
> - [ ] **4. Examen cardiovasculaire *(4 grilles sur 13)***
> 	- [ ] Auscultation cardiaque *(3 grilles sur 13)*
> 	- [ ] Palpation du pouls radial *(BPCO)*
> 	- [ ] Palpation du choc apexien *(BPCO)*
> 	- [ ] Recherche du reflux hépato-jugulaire *(BPCO)*
> 	- [ ] Auscultation cardiaque systématique *(1 grille sur 13)*
> 	- [ ] Recherche de signes d'insuffisance cardiaque droite *(1 grille sur 13)*
> 	- [ ] Évaluation des pouls périphériques *(1 grille sur 13)*
> 	- [ ] Recherche d'œdèmes des membres inférieurs *(1 grille sur 13)*
> - [ ] **5. Examen thoracique *(3 grilles sur 13)***
> 	- [ ] Inspection du thorax
> 	- [ ] Palpation du thorax
> 	- [ ] Percussion des champs pulmonaires
> 	- [ ] Auscultation pulmonaire
> 	- [ ] Recherche de frémitus *(1 grille sur 13)*
> 	- [ ] Recherche de frémitus vocal *(BPCO)*
> 	- [ ] Examen du frémissement *(1 grille sur 13)*
> 	- [ ] Inspection du mouchoir du patient *(1 grille sur 13)*
> - [ ] **6. Examen des extrémités *(6 grilles sur 13)***
> 	- [ ] Inspection des mains *(3 grilles sur 13)*
> 	- [ ] Recherche d'œdème déclive *(BPCO)*
> 	- [ ] Recherche d'hippocratisme digital *(2 grilles sur 13)*
> 	- [ ] Recherche de cyanose *(2 grilles sur 13)*
> 	- [ ] État des ongles *(Tuberculose)*
> 	- [ ] Température des extrémités *(Tuberculose)*
> 	- [ ] Hippocratisme digital *(Insuffisance cardiaque (décompensée))*
> 	- [ ] Cyanose périphérique *(Insuffisance cardiaque (décompensée))*
> 	- [ ] Température *(Insuffisance cardiaque (décompensée))*
> 	- [ ] Temps de recoloration capillaire *(Insuffisance cardiaque (décompensée))*
> - [ ] **7. Examen du dos *(1 grille sur 13)***
> 	- [ ] Examen de la colonne vertébrale
> - [ ] **8. Signes vitaux *(3 grilles sur 13)***
> 	- [ ] Pression artérielle *(Insuffisance cardiaque (décompensée) · Tuberculose)*
> 	- [ ] Fréquence cardiaque *(Insuffisance cardiaque (décompensée) · Tuberculose)*
> 	- [ ] Température *(Insuffisance cardiaque (décompensée) · Tuberculose)*
> 	- [ ] Fréquence respiratoire *(Insuffisance cardiaque (décompensée) · Tuberculose)*
> 	- [ ] Saturation en oxygène *(Insuffisance cardiaque (décompensée))*
> - [ ] **9. Orientation *(1 grille sur 13)***
> - [ ] **10. Inspection *(1 grille sur 13)***
> - [ ] **11. Pattern respiratoire *(1 grille sur 13)***
> - [ ] **12. Forme du thorax *(1 grille sur 13)***
> - [ ] **13. Signes de cyanose *(1 grille sur 13)***
> - [ ] **14. Palpation *(1 grille sur 13)***
> - [ ] **15. Percussion *(1 grille sur 13)***
> - [ ] **16. Fremitus vocal augmenté *(1 grille sur 13)***
> - [ ] **17. Bronchophonie *(1 grille sur 13)***
> - [ ] **18. Auscultation *(1 grille sur 13)***
> - [ ] **19. Auscultation cardiaque *(1 grille sur 13)***
> - [ ] **20. Veines jugulaires *(1 grille sur 13)***
> - [ ] **21. Inspection et palpation périphérie *(1 grille sur 13)***
> - [ ] **22. Examen cardiaque *(3 grilles sur 13)***
> 	- [ ] Palpation du précordium *(2 grilles sur 13)*
> 	- [ ] Auscultation cardiaque *(2 grilles sur 13)*
> 	- [ ] Recherche de signes d'insuffisance cardiaque droite *(Tuberculose)*
> 	- [ ] Pouls périphériques *(Tuberculose)*
> 	- [ ] Auscultation *(1 grille sur 13)*
> 	- [ ] Pouls *(1 grille sur 13)*
> - [ ] **23. Examen pulmonaire - Inspection *(Insuffisance cardiaque (décompensée) · Tuberculose)***
> 	- [ ] Symétrie thoracique
> 	- [ ] Utilisation des muscles accessoires *(Tuberculose)*
> 	- [ ] Type de respiration
> 	- [ ] Déformations
> 	- [ ] Tirage *(Insuffisance cardiaque (décompensée))*
> - [ ] **24. Examen pulmonaire - Palpation *(Insuffisance cardiaque (décompensée) · Tuberculose)***
> 	- [ ] Vibrations vocales (frémitus) *(Tuberculose)*
> 	- [ ] Points douloureux
> 	- [ ] Adénopathies sus-claviculaires *(Tuberculose)*
> 	- [ ] Ampliation thoracique
> 	- [ ] Vibrations vocales *(Insuffisance cardiaque (décompensée))*
> - [ ] **25. Examen pulmonaire - Percussion *(Insuffisance cardiaque (décompensée) · Tuberculose)***
> 	- [ ] Percussion systématique *(Tuberculose)*
> 	- [ ] Recherche de matité *(Tuberculose)*
> 	- [ ] Comparaison bilatérale
> 	- [ ] Limites pulmonaires *(Tuberculose)*
> 	- [ ] Matité des bases *(Insuffisance cardiaque (décompensée))*
> 	- [ ] Épanchement pleural *(Insuffisance cardiaque (décompensée))*
> - [ ] **26. Auscultation pulmonaire *(5 grilles sur 13)***
> 	- [ ] Auscultation antérieure systématique *(Insuffisance cardiaque (décompensée) · Tuberculose)*
> 	- [ ] Auscultation postérieure systématique *(Insuffisance cardiaque (décompensée) · Tuberculose)*
> 	- [ ] Bruits surajoutés *(Tuberculose)*
> 	- [ ] Modifications du murmure vésiculaire *(Tuberculose)*
> 	- [ ] Râles crépitants des bases *(Insuffisance cardiaque (décompensée))*
> 	- [ ] Diminution du murmure vésiculaire *(Insuffisance cardiaque (décompensée))*
> 	- [ ] Demande respiration bouche ouverte *(1 grille sur 13)*
> 	- [ ] Points d'auscultation *(1 grille sur 13)*
> 	- [ ] Comparaison symétrique G/D systématique *(1 grille sur 13)*
> 	- [ ] Murmure vésiculaire *(1 grille sur 13)*
> 	- [ ] Souffle tubaire *(1 grille sur 13)*
> 	- [ ] Auscultation systématique des deux champs pulmonaires *(1 grille sur 13)*
> 	- [ ] Identification des sibilances *(1 grille sur 13)*
> 	- [ ] Recherche de râles crépitants ou sous-crépitants *(1 grille sur 13)*
> 	- [ ] Évaluation du murmure vésiculaire *(1 grille sur 13)*
> - [ ] **27. Inspection veineuse *(Tuberculose)***
> 	- [ ] Turgescence des veines jugulaires
> 	- [ ] Reflux hépato-jugulaire
> 	- [ ] Circulation collatérale
> - [ ] **28. Recherche d'œdèmes *(Insuffisance cardiaque (décompensée) · Tuberculose)***
> 	- [ ] Œdèmes des membres inférieurs
> 	- [ ] Signe du godet
> 	- [ ] Symétrie *(Tuberculose)*
> 	- [ ] Ascension *(Tuberculose)*
> 	- [ ] Bilatéralité et symétrie *(Insuffisance cardiaque (décompensée))*
> 	- [ ] Œdème sacré *(Insuffisance cardiaque (décompensée))*
> - [ ] **29. Examen ORL *(2 grilles sur 13)***
> 	- [ ] Inspection de la gorge *(Tuberculose)*
> 	- [ ] Otoscopie *(Tuberculose)*
> 	- [ ] Rhinoscopie antérieure *(Tuberculose)*
> 	- [ ] Palpation sinusienne *(Tuberculose)*
> 	- [ ] Gorge *(1 grille sur 13)*
> 	- [ ] Oreilles *(1 grille sur 13)*
> 	- [ ] Nez *(1 grille sur 13)*
> - [ ] **30. Palpation des ganglions lymphatiques *(2 grilles sur 13)***
> 	- [ ] Ganglions cervicaux *(Tuberculose)*
> 	- [ ] Ganglions sus-claviculaires *(Tuberculose)*
> 	- [ ] Ganglions axillaires *(Tuberculose)*
> 	- [ ] Autres territoires *(Tuberculose)*
> - [ ] **31. Examen abdominal *(3 grilles sur 13)***
> 	- [ ] Inspection *(Tuberculose)*
> 	- [ ] Auscultation *(Tuberculose)*
> 	- [ ] Palpation (hépatomégalie, splénomégalie) *(Tuberculose)*
> 	- [ ] Percussion *(Tuberculose)*
> 	- [ ] Hépatomégalie de stase *(Insuffisance cardiaque (décompensée))*
> 	- [ ] Ascite *(Insuffisance cardiaque (décompensée))*
> 	- [ ] Circulation collatérale *(Insuffisance cardiaque (décompensée))*
> 	- [ ] Masses *(Insuffisance cardiaque (décompensée))*
> - [ ] **32. Inspection générale *(Insuffisance cardiaque (décompensée))***
> 	- [ ] État général
> 	- [ ] Coloration (cyanose, pâleur)
> 	- [ ] Position de confort
> 	- [ ] Utilisation des muscles accessoires
> - [ ] **33. Examen cardiaque - Palpation *(Insuffisance cardiaque (décompensée))***
> 	- [ ] Palpation du précordium
> 	- [ ] Choc de pointe (déplacé?)
> 	- [ ] Frémissements
> 	- [ ] Soulèvement parasternal
> - [ ] **34. Examen cardiaque - Auscultation *(Insuffisance cardiaque (décompensée))***
> 	- [ ] B1 et B2
> 	- [ ] Bruits surajoutés (B3, B4)
> 	- [ ] Souffles (sténose aortique?)
> 	- [ ] Frottement péricardique
> - [ ] **35. Signes d'insuffisance cardiaque droite *(Insuffisance cardiaque (décompensée))***
> 	- [ ] Turgescence des veines jugulaires
> 	- [ ] Reflux hépato-jugulaire
> 	- [ ] Hépatomégalie
> 	- [ ] Ascite
> - [ ] **36. Examen ORL rapide *(Insuffisance cardiaque (décompensée))***
> 	- [ ] Gorge
> 	- [ ] Oreilles
> 	- [ ] Nez
> 	- [ ] Absence de foyer infectieux
> - [ ] **37. Palpation ganglionnaire *(Insuffisance cardiaque (décompensée))***
> 	- [ ] Aires cervicales
> 	- [ ] Aires axillaires
> 	- [ ] Autres territoires
> - [ ] **38. Signes vitaux mesurés *(1 grille sur 13)***
> - [ ] **39. Examen pulmonaire *(1 grille sur 13)***
> 	- [ ] Palpation (frémissement vocal)
> 	- [ ] Percussion thoracique
> 	- [ ] Auscultation systématique antérieure et postérieure
> - [ ] **40. Inspection des veines jugulaires *(1 grille sur 13)***
> - [ ] **41. Recherche d'œdèmes des membres inférieurs *(1 grille sur 13)***
> - [ ] **42. Hygiène des mains *(1 grille sur 13)***
> - [ ] **43. Inspection thoracique *(2 grilles sur 13)***
> 	- [ ] Inspection statique du thorax *(1 grille sur 13)*
> 	- [ ] Évaluation de la symétrie respiratoire *(1 grille sur 13)*
> 	- [ ] Recherche de déformation thoracique *(1 grille sur 13)*
> 	- [ ] Évaluation du tirage et de l'ampliation *(1 grille sur 13)*
> - [ ] **44. Examen des extrémités (recherche d'embolie pulmonaire) *(1 grille sur 13)***
> - [ ] **45. Examens complémentaires si pertinents *(1 grille sur 13)***
> 	- [ ] Peau
> 	- [ ] Gorge
> 	- [ ] Ganglions lymphatiques
> - [ ] **46. Note: Examen clinique non réalisable par téléphone *(Faux-croup)***
> 	- [ ] Évaluation indirecte basée sur les observations parentales
> - [ ] **47. Inspection générale - patient couché *(1 grille sur 13)***
> 	- [ ] Aspect général
> 	- [ ] Fréquence respiratoire
> 	- [ ] Cycle respiratoire
> 	- [ ] Détresse respiratoire
> 	- [ ] Cyanose centrale et périphérique
> 	- [ ] Hippocratisme digital
> - [ ] **48. Inspection thoracique - patient assis *(1 grille sur 13)***
> 	- [ ] Forme du thorax
> 	- [ ] Asymétrie thoracique
> 	- [ ] Déformations rachidiennes
> 	- [ ] Cicatrices
> 	- [ ] Respiration paradoxale
> - [ ] **49. Palpation thoracique *(2 grilles sur 13)***
> 	- [ ] Ampliation thoracique *(1 grille sur 13)*
> 	- [ ] Localisation précise de la douleur *(1 grille sur 13)*
> 	- [ ] Vibrations vocales *(1 grille sur 13)*
> 	- [ ] Technique correcte *(1 grille sur 13)*
> 	- [ ] Recherche d'emphysème sous-cutané *(1 grille sur 13)*
> 	- [ ] Palpation des vibrations vocales *(1 grille sur 13)*
> 	- [ ] Recherche de douleur à la palpation *(1 grille sur 13)*
> 	- [ ] Évaluation de l'ampliation thoracique *(1 grille sur 13)*
> 	- [ ] Palpation des aires ganglionnaires (sus-claviculaires, axillaires) *(1 grille sur 13)*
> - [ ] **50. Percussion thoracique *(1 grille sur 13)***
> 	- [ ] Limite inférieure poumons
> 	- [ ] Comparaison sonorité G/D
> 	- [ ] Reconnaissance des sons
> 	- [ ] Technique correcte
> 	- [ ] Interprétation
> - [ ] **51. Identification des bruits pathologiques *(1 grille sur 13)***
> 	- [ ] Sibilances
> 	- [ ] Ronchi
> 	- [ ] Râles fins
> 	- [ ] Râles grossiers
> 	- [ ] Frottement pleural
> 	- [ ] Stridor
> - [ ] **52. Examen cardiovasculaire complémentaire *(1 grille sur 13)***
> 	- [ ] Palpation choc de pointe
> 	- [ ] Auscultation cardiaque
> 	- [ ] Œdèmes membres inférieurs
> 	- [ ] Turgescence jugulaire
> 	- [ ] Reflux hépato-jugulaire
> - [ ] **53. Examen général et signes vitaux *(1 grille sur 13)***
> 	- [ ] Évaluation de l'état général
> 	- [ ] Mesure de la fréquence respiratoire
> 	- [ ] Évaluation des signes de détresse respiratoire
> 	- [ ] Recherche de cyanose
> - [ ] **54. Percussion pulmonaire *(1 grille sur 13)***
> 	- [ ] Percussion systématique des deux champs pulmonaires
> 	- [ ] Recherche de matité
> 	- [ ] Évaluation de la sonorité pulmonaire
> 	- [ ] Délimitation des bases pulmonaires
> - [ ] **55. Examen ORL et recherche d'adénopathies *(1 grille sur 13)***
> 	- [ ] Palpation des aires ganglionnaires cervicales
> 	- [ ] Examen de la cavité buccale
> 	- [ ] Palpation des aires ganglionnaires sus-claviculaires
> 	- [ ] Recherche d'adénopathies axillaires
> - [ ] **56. Recherche de signes extrarespiratoires *(1 grille sur 13)***
> 	- [ ] Recherche d'hippocratisme digital
> 	- [ ] Examen cutané (recherche de métastases)
> 	- [ ] Palpation abdominale (hépatomégalie)
> 	- [ ] Évaluation neurologique de base

> [!success] 💊 Management — partagé par plusieurs diagnostics
> - [ ] **1. Hypothèses diagnostiques *(3 grilles sur 13)* — *Asthme · BPCO · Cancer pulmonaire***
> - [ ] **2. Communication avec la patiente *(2 grilles sur 13)* — *Asthme · BPCO***
> 	- [ ] Explications à la patiente des impressions diagnostiques préliminaires
> 	- [ ] Explication du plan de prise en charge
> 	- [ ] Utilisation d'un langage non médical et clarification des termes médicaux
> 	- [ ] Évaluation de l'accord de la patiente avec le plan diagnostique
> 	- [ ] Recherche des préoccupations et questions de la patiente

> [!success] 💊 Management — si Asthme
> - [ ] **1. Examens complémentaires de première intention *(1 grille sur 2)***
> 	- [ ] Gaz du sang artériel, oxymétrie de pouls
> 	- [ ] FSC avec différentielle
> - [ ] **2. Examens de fonction respiratoire *(1 grille sur 2)***
> 	- [ ] Mesure du débit de pointe
> 	- [ ] Tests de fonction pulmonaire (EFR)
> 	- [ ] Test de provocation à la méthacholine
> - [ ] **3. Examens d'imagerie *(1 grille sur 2)***
> 	- [ ] Radiographie thoracique
> - [ ] **4. Conseil et soutien *(1 grille sur 2)***
> 	- [ ] Conseil sur les drogues récréatives
> 	- [ ] Offrir mouchoir et/ou eau pendant la crise de toux de la patiente
> 	- [ ] Réaction appropriée au défi concernant la guérison
> 	- [ ] Rassurer sur les options thérapeutiques
> 	- [ ] Éducation sur l'asthme si confirmé
> - [ ] **5. Diagnostic principal évoqué *(1 grille sur 2)***
> - [ ] **6. Examens complémentaires *(1 grille sur 2)***
> 	- [ ] Radiographie thoracique
> 	- [ ] Gazométrie artérielle
> 	- [ ] Bilan sanguin (FSC, CRP, CK, troponines, D-dimères)
> 	- [ ] Épreuves fonctionnelles respiratoires avec test de provocation bronchique
> 	- [ ] ECG/Échocardiographie
> 	- [ ] Tests d'allergie
> - [ ] **7. Traitement proposé *(1 grille sur 2)***
> 	- [ ] Bêta-2-mimétiques (salbutamol) en inhalation
> 	- [ ] Éducation thérapeutique
> 	- [ ] Éviction des facteurs déclenchants
> - [ ] **8. Diagnostics différentiels cardiaques *(1 grille sur 2)***
> - [ ] **9. Diagnostics différentiels pulmonaires *(1 grille sur 2)***
> - [ ] **10. Interprétation des épreuves fonctionnelles respiratoires *(1 grille sur 2)***
> 	- [ ] Syndrome obstructif
> 	- [ ] Résistances centrales augmentées
> 	- [ ] Volume résiduel augmenté
> 	- [ ] Test de réversibilité

> [!success] 💊 Management — si BPCO
> - [ ] **1. Examens complémentaires de première intention**
> 	- [ ] Gaz du sang artériel, oxymétrie de pouls
> 	- [ ] ECG
> 	- [ ] Échocardiographie transthoracique
> 	- [ ] BNP, NT-pro BNP
> 	- [ ] Radiographie thoracique
> - [ ] **2. Conseil et soutien**
> 	- [ ] Offrir mouchoir et eau lors de la crise de toux
> 	- [ ] Conseil sur l'arrêt du tabac
> 	- [ ] Conseil sur les options de soutien pour l'exercice régulier
> 	- [ ] Réaction appropriée au défi concernant l'arrêt du tabac
> 	- [ ] Éducation sur les risques du tabagisme
> - [ ] **3. Tests de fonction pulmonaire**
> 	- [ ] Spirométrie avec test de réversibilité

> [!success] 💊 Management — si Bronchiolite
> *Aucune grille du corpus ne documente ce diagnostic* — il est pourtant attendu de cette SSP. **Trou de révision à combler ailleurs.**

> [!success] 💊 Management — si Cancer pulmonaire
> - [ ] **1. Examens complémentaires de première intention *(1 grille sur 2)***
> 	- [ ] Radiographie thoracique
> 	- [ ] Oxymétrie de pouls
> 	- [ ] Gazométrie artérielle
> - [ ] **2. Conseil et soutien *(1 grille sur 2)***
> 	- [ ] Conseil sur l'arrêt du tabac
> 	- [ ] Réaction appropriée au défi sur les coûts
> 	- [ ] Orientation vers services sociaux
> 	- [ ] Soutien émotionnel face à l'inquiétude
> 	- [ ] Information sur l'urgence du diagnostic
> - [ ] **3. Examens microbiologiques *(1 grille sur 2)***
> 	- [ ] Coloration de Gram des expectorations, microscopie avec coloration acido-résistante, cytologie, et culture de routine et mycobactérienne
> - [ ] **4. Examens biologiques et imagerie avancée *(1 grille sur 2)***
> 	- [ ] FSC avec formule
> 	- [ ] CT thoracique
> - [ ] **5. Communication avec le patient *(1 grille sur 2)***
> 	- [ ] Explications au patient des impressions diagnostiques préliminaires
> 	- [ ] Explication du plan de prise en charge
> 	- [ ] Utilisation d'un langage non médical et clarification des termes médicaux
> 	- [ ] Évaluation de l'accord du patient avec le plan diagnostique
> 	- [ ] Recherche des préoccupations et questions du patient
> - [ ] **6. Prise en charge immédiate *(1 grille sur 2)***
> 	- [ ] Arrêt du tabac immédiat et accompagnement
> 	- [ ] Consultation pneumologique urgente
> 	- [ ] Surveillance clinique (quantité hémoptysie, état respiratoire)
> 	- [ ] Information et rassurance de la patiente
> - [ ] **7. Diagnostic principal et diagnostics différentiels *(1 grille sur 2)***
> 	- [ ] Cancer pulmonaire (forte suspicion)
> 	- [ ] BPCO avec exacerbation
> 	- [ ] Tuberculose pulmonaire
> 	- [ ] Bronchectasies
> - [ ] **8. Examens de première intention *(1 grille sur 2)***
> 	- [ ] Radiographie thoracique (face et profil)
> 	- [ ] FSC avec plaquettes
> 	- [ ] Bilan de coagulation (TP, TCA)
> 	- [ ] Ionogramme, créatinine, urée
> - [ ] **9. Examens de seconde intention *(1 grille sur 2)***
> 	- [ ] CT thoracique avec injection
> 	- [ ] Fibroscopie bronchique avec lavage et biopsie
> 	- [ ] Recherche de BK dans les expectorations (3 prélèvements)
> 	- [ ] Spirométrie complète
> - [ ] **10. Examens complémentaires selon orientation *(1 grille sur 2)***
> 	- [ ] CT thoraco-abdomino-pelvien (si suspicion néoplasique)
> 	- [ ] PET scan (bilan d'extension)
> 	- [ ] Échocardiographie (si suspicion cardiaque)
> 	- [ ] Angio-CT pulmonaire (si suspicion d'embolie)
> - [ ] **11. Surveillance et suivi *(1 grille sur 2)***
> 	- [ ] Surveillance de l'abondance de l'hémoptysie
> 	- [ ] Réévaluation rapide si aggravation
> 	- [ ] Coordination avec le pneumologue
> 	- [ ] Planification des examens complémentaires

> [!success] 💊 Management — si Coqueluche
> - [ ] **1. Diagnostics différentiels**
> 	- [ ] Bronchiolite
> 	- [ ] Pneumonie
> 	- [ ] Faux croup
> 	- [ ] Infection virale des voies respiratoires supérieures
> - [ ] **2. Examens complémentaires**
> 	- [ ] Prise de sang (FSC, CRP, Hémoculture)
> 	- [ ] Recherche bactério dans les expectorations
> 	- [ ] Radiographie/Ultrason thoracique
> - [ ] **3. Hypothèse diagnostique : Coqueluche**
> - [ ] **4. Prise en charge immédiate**
> 	- [ ] Hospitalisation
> 	- [ ] Hydratation
> 	- [ ] Alimentation
> 	- [ ] Antibiotiques

> [!success] 💊 Management — si Faux-croup
> - [ ] **1. Diagnostic principal évoqué**
> - [ ] **2. Diagnostics différentiels**
> - [ ] **3. Évaluation de l'urgence**
> 	- [ ] Mentionne la possibilité d'une consultation urgente
> 	- [ ] Reconnaît l'impossibilité de déplacement immédiat
> 	- [ ] Propose surveillance et rappel dans 1 heure
> - [ ] **4. Conseils thérapeutiques**
> 	- [ ] Mesurer la fièvre, si présente donner paracétamol/Algifor sirop
> 	- [ ] Assurer une bonne humidification de l'air
> 	- [ ] Remèdes maison : lait au miel, tisanes, compresses de pommes de terre
> 	- [ ] Installer l'enfant dans la salle de bain avec eau chaude qui coule
> 	- [ ] Calmer l'enfant
> - [ ] **5. Signes d'alarme à surveiller**
> 	- [ ] Tirage intercostal ou sus-sternal
> 	- [ ] Peau bleutée (cyanose)
> 	- [ ] Pas d'amélioration malgré les mesures
> 	- [ ] Refus de boire
> 	- [ ] Dégradation de l'état général
> 	- [ ] Expectorations sanglantes
> - [ ] **6. Organisation du suivi**
> 	- [ ] Proposer rappel dans 1 heure
> 	- [ ] Si aggravation, envoyer ambulance pour chercher l'enfant
> 	- [ ] Disponibilité pour nouveau contact si besoin
> - [ ] **7. Vérification de la compréhension**
> 	- [ ] Fait répéter les recommandations par l'appelant
> 	- [ ] Demande accord avec les recommandations
> 	- [ ] Demande s'il y a des questions ou points peu clairs
> - [ ] **8. Clôture appropriée**
> 	- [ ] Encourage à rappeler en cas d'incertitude
> 	- [ ] Encourage à se présenter si nécessaire
> 	- [ ] Attitude rassurante et professionnelle

> [!success] 💊 Management — si Insuffisance cardiaque (décompensée)
> - [ ] **1. Examens d'imagerie**
> 	- [ ] Radiographie thoracique
> 	- [ ] Signes de surcharge (cardiomégalie, redistribution vasculaire)
> 	- [ ] Lignes de Kerley
> 	- [ ] Épanchement pleural
> - [ ] **2. Examens biologiques**
> 	- [ ] BNP ou NT-proBNP
> 	- [ ] Troponine
> 	- [ ] Marqueurs inflammatoires (CRP)
> 	- [ ] Fonction rénale et ionogramme
> 	- [ ] FSC
> - [ ] **3. Diagnostic principal évoqué**
> 	- [ ] Insuffisance cardiaque congestive
> 	- [ ] Type (gauche, droite, globale)
> 	- [ ] Étiologie probable (valvulaire)
> 	- [ ] Classification NYHA
> - [ ] **4. Diagnostics différentiels**
> - [ ] **5. Examens cardiologiques**
> 	- [ ] ECG (troubles du rythme, HVG)
> 	- [ ] Échocardiographie
> 	- [ ] Évaluation de la FEVG
> 	- [ ] Évaluation valvulaire (sténose aortique?)
> - [ ] **6. Traitement médicamenteux de l'IC**
> 	- [ ] Optimisation IEC (déjà sous Lisinopril)
> 	- [ ] Diurétiques de l'anse (furosémide)
> 	- [ ] Bêtabloquant (déjà sous métoprolol)
> 	- [ ] Antagoniste de l'aldostérone si indiqué
> - [ ] **7. Traitement symptomatique**
> 	- [ ] Restriction hydrosodée
> 	- [ ] Oxygénothérapie si hypoxémie
> 	- [ ] Position semi-assise
> 	- [ ] Surveillance du poids quotidien
> - [ ] **8. Évaluation de la sévérité**
> 	- [ ] Critères d'hospitalisation
> 	- [ ] Signes de décompensation aiguë
> 	- [ ] Stabilité hémodynamique
> 	- [ ] Compliance thérapeutique
> - [ ] **9. Prise en charge étiologique**
> 	- [ ] Évaluation chirurgicale si sténose aortique sévère
> 	- [ ] Remplacement valvulaire aortique
> 	- [ ] TAVI si risque chirurgical élevé
> 	- [ ] Optimisation du traitement médical
> - [ ] **10. Organisation du transfert si nécessaire**
> 	- [ ] Indication d'hospitalisation
> 	- [ ] Service de cardiologie
> 	- [ ] Transport médicalisé
> 	- [ ] Information du patient et de la famille
> - [ ] **11. Suivi et éducation thérapeutique**
> 	- [ ] Surveillance des symptômes
> 	- [ ] Pesée quotidienne
> 	- [ ] Signes d'alarme
> 	- [ ] Observance médicamenteuse

> [!success] 💊 Management — si Pneumonie
> - [ ] **1. Examens complémentaires de première intention *(1 grille sur 3)***
> 	- [ ] Radiographie thorax
> 	- [ ] FSC
> 	- [ ] CRP
> 	- [ ] Saturation O2
> 	- [ ] Bandelette urinaire
> - [ ] **2. Examens biologiques *(1 grille sur 3)***
> - [ ] **3. Hémogramme *(1 grille sur 3)***
> - [ ] **4. Valeurs inflammatoires (CRP) *(1 grille sur 3)***
> - [ ] **5. Fonction rénale *(1 grille sur 3)***
> - [ ] **6. Gazométrie artérielle *(1 grille sur 3)***
> - [ ] **7. Radiographie *(1 grille sur 3)***
> - [ ] **8. ECG *(1 grille sur 3)***
> - [ ] **9. Diagnostic de travail *(1 grille sur 3)***
> - [ ] **10. Antibiothérapie intraveineuse *(1 grille sur 3)***
> - [ ] **11. Oxygénothérapie *(1 grille sur 3)***
> - [ ] **12. Apport hydrique *(1 grille sur 3)***
> - [ ] **13. Analgésie et antipyrèse *(1 grille sur 3)***
> - [ ] **14. Hospitalisation *(1 grille sur 3)***
> - [ ] **15. Suivi évolutif *(1 grille sur 3)***
> - [ ] **16. Recommandation vaccinale *(1 grille sur 3)***
> - [ ] **17. Diagnostic étiologique *(1 grille sur 3)***
> - [ ] **18. Hémocultures *(1 grille sur 3)***
> - [ ] **19. Prélèvement Covid/Influenza *(1 grille sur 3)***
> - [ ] **20. Diagnostic des expectorations *(1 grille sur 3)***
> - [ ] **21. Diagnostic principal évoqué *(1 grille sur 3)***
> - [ ] **22. Diagnostics différentiels *(1 grille sur 3)***
> - [ ] **23. Examens complémentaires *(1 grille sur 3)***
> 	- [ ] Radiographie thoracique
> 	- [ ] Bilan biologique (FSC, marqueurs inflammatoires)
> 	- [ ] Hémocultures
> - [ ] **24. Traitement proposé *(1 grille sur 3)***
> 	- [ ] Antibiothérapie (amoxicilline, Augmentin ou macrolide)
> 	- [ ] Traitement symptomatique (antipyrétique, hydratation)
> - [ ] **25. Évaluation du score CURB-65 *(1 grille sur 3)***
> 	- [ ] C - Confusion
> 	- [ ] U - Urée > 7 mmol/L
> 	- [ ] R - Fréquence respiratoire ≥ 30/min
> 	- [ ] B - TA < 90/60 mmHg
> 	- [ ] 65 - Âge ≥ 65 ans
> - [ ] **26. Organisation de la prise en charge *(1 grille sur 3)***
> 	- [ ] Traitement ambulatoire vs hospitalisation
> 	- [ ] Arrêt de travail
> 	- [ ] Contrôle à prévoir (48-72h)
> - [ ] **27. Orientation diagnostique principale *(1 grille sur 3)***
> 	- [ ] Pneumonie communautaire
> 	- [ ] Évaluation de la gravité
> 	- [ ] Scores de gravité
> 	- [ ] Indication d'hospitalisation
> - [ ] **28. Diagnostic différentiel respiratoire *(1 grille sur 3)***
> - [ ] **29. Examens complémentaires selon gravité *(1 grille sur 3)***
> 	- [ ] Hémocultures
> 	- [ ] Gazométrie artérielle
> 	- [ ] PCT
> 	- [ ] PCR respiratoire
> 	- [ ] ECBC
> - [ ] **30. Traitement antibiotique ambulatoire *(1 grille sur 3)***
> - [ ] **31. Traitements symptomatiques et mesures générales *(1 grille sur 3)***
> 	- [ ] Antipyrétiques
> 	- [ ] Hydratation
> 	- [ ] Repos et arrêt de travail
> 	- [ ] Oxygénothérapie si SpO2 < 92%
> 	- [ ] Kinésithérapie respiratoire si encombrement
> - [ ] **32. Surveillance et critères d'hospitalisation *(1 grille sur 3)***
> 	- [ ] Réévaluation clinique à 48-72h
> 	- [ ] Critères CURB-65 ≥ 2
> 	- [ ] Désaturation < 90% en air ambiant
> 	- [ ] Comorbidités décompensées
> 	- [ ] Échec traitement ambulatoire
> - [ ] **33. Prévention et conseils *(1 grille sur 3)***
> 	- [ ] Sevrage tabagique
> 	- [ ] Vaccination antigrippale annuelle
> 	- [ ] Vaccination antipneumococcique
> 	- [ ] Mesures hygiéno-diététiques
> 	- [ ] Consultation de suivi post-infection

> [!success] 💊 Management — si Scarlatine / Angine streptococcique
> *Aucune grille de cette SSP ne documente ce diagnostic* — mais le corpus le documente ailleurs : [[Mémento — Éruption Cutanée]] (1 grille).

> [!success] 💊 Management — si Tuberculose
> - [ ] **1. Diagnostic principal évoqué**
> 	- [ ] Tuberculose pulmonaire
> 	- [ ] Justification épidémiologique
> 	- [ ] Justification clinique
> 	- [ ] Degré de contagiosité
> - [ ] **2. Diagnostics différentiels**
> - [ ] **3. Examens diagnostiques pour la tuberculose**
> 	- [ ] Radiographie thoracique
> 	- [ ] Test de Mantoux/IGRA
> 	- [ ] Culture des expectorations (3 échantillons)
> 	- [ ] PCR tuberculose
> - [ ] **4. Reconnaissance radiologique**
> 	- [ ] Identification des lésions tuberculeuses
> 	- [ ] Localisation (apex)
> 	- [ ] Cavernes
> 	- [ ] Infiltrats
> - [ ] **5. Autres examens complémentaires**
> 	- [ ] FSC, CRP
> 	- [ ] Fonction hépatique et rénale (pré-thérapeutique)
> 	- [ ] Sérologie VIH
> 	- [ ] Test de grossesse si femme en âge de procréer
> - [ ] **6. Traitement antituberculeux**
> 	- [ ] Quadrithérapie initiale (RHEZ)
> 	- [ ] Durée du traitement (6 mois minimum)
> 	- [ ] Surveillance des effets secondaires
> 	- [ ] DOT (Directly Observed Therapy)
> - [ ] **7. Mesures d'isolement et de santé publique**
> 	- [ ] Hospitalisation en chambre d'isolement respiratoire
> 	- [ ] Port du masque FFP2
> 	- [ ] Déclaration obligatoire
> 	- [ ] Enquête d'entourage
> - [ ] **8. Information et éducation du patient**
> 	- [ ] Explication de la maladie
> 	- [ ] Importance de l'observance
> 	- [ ] Durée du traitement
> 	- [ ] Mesures de protection de l'entourage
> - [ ] **9. Suivi prévu**
> 	- [ ] Contrôles réguliers
> 	- [ ] Surveillance de l'efficacité
> 	- [ ] Dépistage des effets secondaires
> 	- [ ] Suivi de l'observance
