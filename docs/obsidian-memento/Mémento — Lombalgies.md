---
aliases:
  - "Mémento Lombalgies"
type: memento-ecos-ssp
ssp: "Lombalgies"
specialite: "Musculo-Squelettique"
cas: 8
diagnostics: 6
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

# Lombalgies ⭐️

*Musculo-Squelettique · 8 grilles · 6 diagnostics documentés · 2 attendus absents du corpus* — [[SSP — Lombalgies]]

> [!abstract] Les 8 grilles fusionnées
> - **AMBOSS-9** — Hernie discale `premier-dd` · [grille](<file:///Users/damienfulliquet/Developer/GitHub/grilles-ecos/cases/amboss/AMBOSS-9_-_Douleurs_dorsales_-_Homme_71_ans_-_Grille_ECOS.html>)
> - **AMBOSS-10** — Spondylarthrite ankylosante `premier-dd` · [grille](<file:///Users/damienfulliquet/Developer/GitHub/grilles-ecos/cases/amboss/AMBOSS-10_-_Douleurs_dorsales_et_raideur_-_Homme_26_ans_-_Grille_ECOS.html>)
> - **AZYGOS-20** — Suspicion de myélome multiple (confirmation par ponction médullaire) `diagnostic-travail` · [grille](<file:///Users/damienfulliquet/Developer/GitHub/grilles-ecos/docs/azygos-grilles/41ad9d6e-557b-49f5-a3a7-0ce3e57d1ba2.json>)
> - **German-57** — Fracture vertébrale `corrige` · [grille](<file:///Users/damienfulliquet/Developer/GitHub/grilles-ecos/cases/german/German-57_-_Lombalgie_-_Grille_ECOS.html>)
> - **German-58** — Hernie discale `corrige` · [grille](<file:///Users/damienfulliquet/Developer/GitHub/grilles-ecos/cases/german/German-58_-_Lombalgie_-_Grille_ECOS.html>)
> - **German-59** — Colique néphrétique sur lithiase `corrige` · [grille](<file:///Users/damienfulliquet/Developer/GitHub/grilles-ecos/cases/german/German-59_-_Lombalgie_-_Grille_ECOS.html>)
> - **RESCOS-31** — Colique néphrétique sur lithiase `dd-principal` · [grille](<file:///Users/damienfulliquet/Developer/GitHub/grilles-ecos/cases/rescos/RESCOS-31_-_Douleur_lombaire_-_Grille_ECOS.html>)
> - **RESCOS-48** — Cancer prostatique métastatique `explicite` · [grille](<file:///Users/damienfulliquet/Developer/GitHub/grilles-ecos/cases/rescos/RESCOS-48%20-%20Lombalgie%20-%20Grille%20ECOS.html>)

> [!note] 📋 Anamnèse
> - [ ] **1. Motif de consultation principal *(4 grilles sur 8)***
> - [ ] **2. Caractérisation de la douleur dorsale *(5 diagnostics)***
> 	- [ ] Localisation *(5 grilles sur 8)*
> 	- [ ] Intensité (échelle 0-10) *(2 grilles sur 8)*
> 	- [ ] Qualité *(3 grilles sur 8)*
> 	- [ ] Début *(3 grilles sur 8)*
> 	- [ ] Événements précipitants *(2 grilles sur 8)*
> 	- [ ] Progression/constant/intermittent *(2 grilles sur 8)*
> 	- [ ] Épisodes antérieurs *(2 grilles sur 8)*
> 	- [ ] Irradiation *(5 grilles sur 8)*
> 	- [ ] Facteurs améliorants *(2 grilles sur 8)*
> 	- [ ] Facteurs aggravants *(2 grilles sur 8)*
> 	- [ ] Type *(1 grille sur 8)*
> 	- [ ] Intensité *(2 grilles sur 8)*
> 	- [ ] Évolution *(1 grille sur 8)*
> 	- [ ] Chronologie *(Cancer prostatique métastatique)*
> 	- [ ] Facteurs atténuants/aggravants *(Cancer prostatique métastatique)*
> - [ ] **3. Symptômes urinaires associés *(6 grilles sur 8)***
> 	- [ ] Hématurie macroscopique *(1 grille sur 8)*
> 	- [ ] Dysurie *(1 grille sur 8)*
> 	- [ ] Incontinence *(1 grille sur 8)*
> 	- [ ] Pollakiurie *(1 grille sur 8)*
> 	- [ ] Urgences mictionnelles *(1 grille sur 8)*
> 	- [ ] Besoin impérieux d'uriner *(1 grille sur 8)*
> 	- [ ] Difficultés mictionnelles *(1 grille sur 8)*
> 	- [ ] Urines troubles ou hématuriques *(1 grille sur 8)*
> 	- [ ] Sensation de vidange incomplète *(1 grille sur 8)*
> 	- [ ] Brûlures mictionnelles possibles *(1 grille sur 8)*
> - [ ] **4. Recherche de symptômes spécifiques - Drapeaux rouges *(1 grille sur 8)***
> 	- [ ] Traumatisme
> 	- [ ] Fièvre/frissons
> 	- [ ] Sueurs nocturnes
> 	- [ ] Fatigue
> 	- [ ] Éruption/changements cutanés (sur le dos)
> 	- [ ] Toux
> 	- [ ] Douleurs articulaires
> 	- [ ] Problèmes urinaires
> 	- [ ] Problèmes intestinaux
> 	- [ ] Appétit
> 	- [ ] Variations pondérales
> 	- [ ] Infections récentes
> - [ ] **5. Recherche de symptômes neurologiques *(6 grilles sur 8)***
> 	- [ ] Sensation de picotements *(2 grilles sur 8)*
> 	- [ ] Faiblesse musculaire *(4 grilles sur 8)*
> 	- [ ] Engourdissement (particulièrement membres inférieurs) *(2 grilles sur 8)*
> 	- [ ] Dysfonction érectile *(2 grilles sur 8)*
> 	- [ ] Traumatisme *(Spondylarthrite ankylosante)*
> 	- [ ] Fièvre/frissons *(Spondylarthrite ankylosante)*
> 	- [ ] Sueurs nocturnes *(Spondylarthrite ankylosante)*
> 	- [ ] Fatigue *(Spondylarthrite ankylosante)*
> 	- [ ] Éruption/changements cutanés et unguéaux *(Spondylarthrite ankylosante)*
> 	- [ ] Dyspnée *(Spondylarthrite ankylosante)*
> 	- [ ] Problèmes urinaires *(Spondylarthrite ankylosante)*
> 	- [ ] Problèmes intestinaux *(Spondylarthrite ankylosante)*
> 	- [ ] Appétit *(Spondylarthrite ankylosante)*
> 	- [ ] Variations pondérales *(Spondylarthrite ankylosante)*
> 	- [ ] Infections récentes *(Spondylarthrite ankylosante)*
> 	- [ ] Problèmes oculaires *(Spondylarthrite ankylosante)*
> 	- [ ] Localisation *(1 grille sur 8)*
> 	- [ ] Troubles sensitifs *(1 grille sur 8)*
> 	- [ ] Déficit moteur *(Cancer prostatique métastatique)*
> 	- [ ] Déficit sensitif *(Cancer prostatique métastatique)*
> 	- [ ] Troubles du transit *(Cancer prostatique métastatique)*
> 	- [ ] Incontinence fécale *(Cancer prostatique métastatique)*
> 	- [ ] Anesthésie en selle *(Cancer prostatique métastatique)*
> - [ ] **6. Antécédents médicaux personnels *(6 grilles sur 8)***
> 	- [ ] Néoplasie *(Fracture vertébrale)*
> 	- [ ] Autres pathologies *(Fracture vertébrale)*
> 	- [ ] Pathologies connues *(2 grilles sur 8)*
> 	- [ ] Immunosuppression *(1 grille sur 8)*
> 	- [ ] Cancer *(1 grille sur 8)*
> 	- [ ] Antécédents de lombalgies *(1 grille sur 8)*
> - [ ] **7. Antécédents chirurgicaux *(5 grilles sur 8)***
> - [ ] **8. Allergies *(6 grilles sur 8)***
> - [ ] **9. Médicaments *(3 grilles sur 8)***
> 	- [ ] Médicaments actuels *(1 grille sur 8)*
> 	- [ ] Quantité de Dafalgan® *(1 grille sur 8)*
> - [ ] **10. Hospitalisations *(2 grilles sur 8)***
> - [ ] **11. Antécédents familiaux *(6 grilles sur 8)***
> 	- [ ] Ostéoporose familiale *(Fracture vertébrale)*
> 	- [ ] Fractures familiales *(Fracture vertébrale)*
> 	- [ ] Néoplasies familiales *(Fracture vertébrale)*
> 	- [ ] Ostéoporose *(1 grille sur 8)*
> 	- [ ] Pathologies cardiovasculaires *(1 grille sur 8)*
> 	- [ ] Autres pathologies pertinentes *(1 grille sur 8)*
> - [ ] **12. Habitudes et mode de vie *(2 grilles sur 8)***
> 	- [ ] Occupation
> 	- [ ] Domicile
> 	- [ ] Alcool
> 	- [ ] Drogues illicites
> 	- [ ] Tabac
> 	- [ ] Exercice
> 	- [ ] Alimentation *(1 grille sur 8)*
> 	- [ ] Consommation de marijuana (durée, fréquence, dernière utilisation) *(Spondylarthrite ankylosante)*
> - [ ] **13. Histoire sexuelle *(Spondylarthrite ankylosante)***
> 	- [ ] Activité sexuelle
> 	- [ ] Avec qui
> 	- [ ] Nombre de partenaires dans l'année
> 	- [ ] Protection
> 	- [ ] IST antérieures
> - [ ] **14. Questions de clôture *(4 grilles sur 8)***
> 	- [ ] Avez-vous quelque chose à ajouter ? *(3 grilles sur 8)*
> 	- [ ] Avez-vous des questions ? *(3 grilles sur 8)*
> - [ ] **15. Dimension temporelle *(Suspicion de myélome multiple (confirmation par ponction médullaire))***
> - [ ] **16. Début / durée *(Suspicion de myélome multiple (confirmation par ponction médullaire))***
> - [ ] **17. Évolution *(Suspicion de myélome multiple (confirmation par ponction médullaire))***
> - [ ] **18. Déclencheur / traumatisme *(Suspicion de myélome multiple (confirmation par ponction médullaire))***
> - [ ] **19. Localisation *(Suspicion de myélome multiple (confirmation par ponction médullaire))***
> - [ ] **20. Irradiation *(3 grilles sur 8)***
> - [ ] **21. Qualité *(Suspicion de myélome multiple (confirmation par ponction médullaire))***
> - [ ] **22. Intensité / gravité *(Suspicion de myélome multiple (confirmation par ponction médullaire))***
> - [ ] **23. Facteurs aggravants *(Suspicion de myélome multiple (confirmation par ponction médullaire))***
> - [ ] **24. Facteurs soulageants *(4 grilles sur 8)***
> 	- [ ] Amélioration *(2 grilles sur 8)*
> 	- [ ] Aggravation *(2 grilles sur 8)*
> - [ ] **25. Mesures déjà entreprises *(Suspicion de myélome multiple (confirmation par ponction médullaire))***
> - [ ] **26. Retentissement des symptômes *(Suspicion de myélome multiple (confirmation par ponction médullaire))***
> - [ ] **27. Douleur nocturne *(Suspicion de myélome multiple (confirmation par ponction médullaire))***
> - [ ] **28. Raideur matinale *(Suspicion de myélome multiple (confirmation par ponction médullaire))***
> - [ ] **29. Sensibilité *(Suspicion de myélome multiple (confirmation par ponction médullaire))***
> - [ ] **30. Motricité *(Suspicion de myélome multiple (confirmation par ponction médullaire))***
> - [ ] **31. Troubles vésico-sphinctériens *(Suspicion de myélome multiple (confirmation par ponction médullaire))***
> - [ ] **32. Troubles de l’érection *(Suspicion de myélome multiple (confirmation par ponction médullaire))***
> - [ ] **33. Démarche instable *(Suspicion de myélome multiple (confirmation par ponction médullaire))***
> - [ ] **34. Symptomatologie B *(Suspicion de myélome multiple (confirmation par ponction médullaire))***
> - [ ] **35. Fièvre *(Suspicion de myélome multiple (confirmation par ponction médullaire))***
> - [ ] **36. Perte de poids *(Suspicion de myélome multiple (confirmation par ponction médullaire))***
> - [ ] **37. Sueurs nocturnes *(Suspicion de myélome multiple (confirmation par ponction médullaire))***
> - [ ] **38. Anamnèse systématique *(Suspicion de myélome multiple (confirmation par ponction médullaire))***
> - [ ] **39. Général *(Suspicion de myélome multiple (confirmation par ponction médullaire))***
> - [ ] **40. Infections passées *(Suspicion de myélome multiple (confirmation par ponction médullaire))***
> - [ ] **41. Tête *(Suspicion de myélome multiple (confirmation par ponction médullaire))***
> - [ ] **42. Yeux *(Suspicion de myélome multiple (confirmation par ponction médullaire))***
> - [ ] **43. Gorge / Nez / Oreilles / Bouche *(Suspicion de myélome multiple (confirmation par ponction médullaire))***
> - [ ] **44. Thorax *(Suspicion de myélome multiple (confirmation par ponction médullaire))***
> - [ ] **45. Abdomen *(Suspicion de myélome multiple (confirmation par ponction médullaire))***
> - [ ] **46. Urogénital *(Suspicion de myélome multiple (confirmation par ponction médullaire))***
> - [ ] **47. Peau *(Suspicion de myélome multiple (confirmation par ponction médullaire))***
> - [ ] **48. Extrémités *(Suspicion de myélome multiple (confirmation par ponction médullaire))***
> - [ ] **49. Maladies osseuses ou tumorales *(Suspicion de myélome multiple (confirmation par ponction médullaire))***
> - [ ] **50. Examens de dépistage *(Suspicion de myélome multiple (confirmation par ponction médullaire))***
> - [ ] **51. Dépistage par coloscopie *(Suspicion de myélome multiple (confirmation par ponction médullaire))***
> - [ ] **52. Contrôle urologique *(Suspicion de myélome multiple (confirmation par ponction médullaire))***
> - [ ] **53. CT thoracique basse dose *(Suspicion de myélome multiple (confirmation par ponction médullaire))***
> - [ ] **54. Antécédents de fractures *(2 grilles sur 8)***
> - [ ] **55. Noxes *(Suspicion de myélome multiple (confirmation par ponction médullaire))***
> - [ ] **56. Alcool *(Suspicion de myélome multiple (confirmation par ponction médullaire))***
> - [ ] **57. Tabac *(Suspicion de myélome multiple (confirmation par ponction médullaire))***
> - [ ] **58. Drogues i.v. *(Suspicion de myélome multiple (confirmation par ponction médullaire))***
> - [ ] **59. Maladies tumorales *(Suspicion de myélome multiple (confirmation par ponction médullaire))***
> - [ ] **60. Profession *(Suspicion de myélome multiple (confirmation par ponction médullaire))***
> - [ ] **61. Anamnèse sociale *(4 grilles sur 8)***
> 	- [ ] Profession *(2 grilles sur 8)*
> 	- [ ] Activité physique *(2 grilles sur 8)*
> 	- [ ] Autonomie *(Fracture vertébrale)*
> 	- [ ] Situation familiale *(1 grille sur 8)*
> 	- [ ] Troubles de la vidange *(Cancer prostatique métastatique)*
> 	- [ ] Temps de latence *(Cancer prostatique métastatique)*
> 	- [ ] Jet faible *(Cancer prostatique métastatique)*
> 	- [ ] Gouttes terminales *(Cancer prostatique métastatique)*
> 	- [ ] Nycturie *(Cancer prostatique métastatique)*
> 	- [ ] Brûlures mictionnelles *(Cancer prostatique métastatique)*
> 	- [ ] Hématurie *(Cancer prostatique métastatique)*
> 	- [ ] Urgences/incontinence *(Cancer prostatique métastatique)*
> - [ ] **62. Présentation avec nom, fonction et tâche *(3 grilles sur 8)***
> - [ ] **63. Caractéristiques temporelles *(3 grilles sur 8)***
> 	- [ ] Début
> 	- [ ] Facteur déclenchant *(Fracture vertébrale)*
> 	- [ ] Durée *(2 grilles sur 8)*
> 	- [ ] Évolution *(1 grille sur 8)*
> - [ ] **64. Type et intensité de la douleur *(3 grilles sur 8)***
> 	- [ ] Type *(Fracture vertébrale)*
> 	- [ ] Intensité *(Fracture vertébrale)*
> - [ ] **65. Recherche des drapeaux rouges (red flags) *(Cancer prostatique métastatique · Fracture vertébrale)***
> 	- [ ] Signes infectieux *(Fracture vertébrale)*
> 	- [ ] Syndrome de la queue de cheval *(Fracture vertébrale)*
> 	- [ ] Déficits neurologiques *(Fracture vertébrale)*
> 	- [ ] Incontinence urinaire ou fécale *(Fracture vertébrale)*
> 	- [ ] Anesthésie en selle *(Fracture vertébrale)*
> 	- [ ] Âge *(Cancer prostatique métastatique)*
> 	- [ ] Traumatisme *(Cancer prostatique métastatique)*
> 	- [ ] Perte de poids *(Cancer prostatique métastatique)*
> 	- [ ] Sudations nocturnes *(Cancer prostatique métastatique)*
> 	- [ ] Fièvre *(Cancer prostatique métastatique)*
> 	- [ ] Antécédents néoplasiques *(Cancer prostatique métastatique)*
> - [ ] **66. Symptômes généraux (symptômes B) *(2 grilles sur 8)***
> 	- [ ] Fièvre
> 	- [ ] Perte de poids non intentionnelle *(Fracture vertébrale)*
> 	- [ ] Sueurs nocturnes
> 	- [ ] Asthénie *(Fracture vertébrale)*
> 	- [ ] Perte de poids *(1 grille sur 8)*
> - [ ] **67. Traitements actuels *(3 grilles sur 8)***
> 	- [ ] Médicaments réguliers *(1 grille sur 8)*
> 	- [ ] Antalgiques à la demande *(1 grille sur 8)*
> - [ ] **68. Habitudes de vie et toxiques *(3 grilles sur 8)***
> 	- [ ] Tabac
> 	- [ ] Alcool
> 	- [ ] Drogues
> - [ ] **69. Statut hormonal *(2 grilles sur 8)***
> - [ ] **70. Facteurs de risque d'ostéoporose *(Fracture vertébrale)***
> 	- [ ] Ménopause précoce
> 	- [ ] Tabagisme important
> 	- [ ] Antécédent de fracture
> 	- [ ] Corticothérapie prolongée
> 	- [ ] Faible poids corporel
> - [ ] **71. Question ouverte d'introduction *(2 grilles sur 8)***
> - [ ] **72. Pattern de la douleur *(1 grille sur 8)***
> 	- [ ] Type
> 	- [ ] Épisodes antérieurs
> 	- [ ] Douleurs nocturnes
> - [ ] **73. Qualité de la douleur *(2 grilles sur 8)***
> - [ ] **74. Événement déclenchant ou traumatisme *(2 grilles sur 8)***
> 	- [ ] Circonstances *(1 grille sur 8)*
> 	- [ ] Port de charge lourde *(1 grille sur 8)*
> 	- [ ] Traumatisme *(1 grille sur 8)*
> - [ ] **75. Symptômes neurologiques - Sensibilité *(1 grille sur 8)***
> - [ ] **76. Recherche syndrome de la queue de cheval *(1 grille sur 8)***
> 	- [ ] Incontinence urinaire
> 	- [ ] Rétention urinaire
> 	- [ ] Incontinence fécale
> 	- [ ] Anesthésie en selle
> - [ ] **77. Antécédents de lombalgies *(2 grilles sur 8)***
> 	- [ ] Épisodes similaires antérieurs *(1 grille sur 8)*
> 	- [ ] Antécédents de lithiase urinaire *(1 grille sur 8)*
> 	- [ ] Infections urinaires récurrentes *(1 grille sur 8)*
> 	- [ ] Malformations urologiques connues *(1 grille sur 8)*
> 	- [ ] Antécédents familiaux de lithiase *(1 grille sur 8)*
> - [ ] **78. Anamnèse sociale et professionnelle *(1 grille sur 8)***
> 	- [ ] Profession
> 	- [ ] Stress, situation de charge
> 	- [ ] Capacité de travail actuelle
> - [ ] **79. Pattern et évolution *(1 grille sur 8)***
> 	- [ ] Type
> 	- [ ] Au repos et en mouvement
> 	- [ ] Épisodes antérieurs
> - [ ] **80. Symptômes digestifs *(1 grille sur 8)***
> 	- [ ] Transit intestinal
> 	- [ ] Nausées/vomissements
> - [ ] **81. Symptômes généraux *(Colique néphrétique sur lithiase)***
> 	- [ ] Fièvre *(1 grille sur 8)*
> 	- [ ] Frissons *(1 grille sur 8)*
> 	- [ ] Perte de poids *(1 grille sur 8)*
> 	- [ ] Sueurs nocturnes *(1 grille sur 8)*
> 	- [ ] Agitation motrice *(1 grille sur 8)*
> 	- [ ] Nausées *(1 grille sur 8)*
> 	- [ ] Vomissements *(1 grille sur 8)*
> 	- [ ] Sueurs froides *(1 grille sur 8)*
> - [ ] **82. Antécédents de lithiase *(1 grille sur 8)***
> 	- [ ] Dépistage pour ostéoporose
> 	- [ ] Fractures antérieures
> 	- [ ] Calculs rénaux antérieurs
> - [ ] **83. Hydratation et habitudes alimentaires *(1 grille sur 8)***
> 	- [ ] Apports hydriques quotidiens
> 	- [ ] Alimentation riche en oxalates
> 	- [ ] Consommation de sel
> - [ ] **84. Facteurs déclenchants et contexte *(1 grille sur 8)***
> 	- [ ] Activité sportive récente
> 	- [ ] Déshydratation relative
> 	- [ ] Consommation de bière
> - [ ] **85. Facteurs de risque lithiasique *(1 grille sur 8)***
> 	- [ ] Hydratation habituelle insuffisante
> 	- [ ] Alimentation riche en protéines
> 	- [ ] Consommation de sel importante
> 	- [ ] Supplémentation vitaminique
> 	- [ ] Climat chaud, transpiration importante
> 	- [ ] Sédentarité alternant avec sport intense
> - [ ] **86. Médicaments et habitudes *(1 grille sur 8)***
> 	- [ ] Prise d'antalgiques
> 	- [ ] Suppléments protéinés
> 	- [ ] Consommation d'alcool
> 	- [ ] Tabagisme
> 	- [ ] Allergies médicamenteuses
> - [ ] **87. Impact fonctionnel *(Cancer prostatique métastatique)***
> 	- [ ] Mobilité réduite
> 	- [ ] Autonomie affectée
> 	- [ ] Qualité du sommeil
> - [ ] **88. Habitudes et antécédents *(Cancer prostatique métastatique)***
> 	- [ ] Médicaments
> 	- [ ] Tabac
> 	- [ ] Alcool
> 	- [ ] Activité physique
> 	- [ ] Antécédents médicaux personnels

> [!tip] 🩺 Status
> - [ ] **1. Mesures d'hygiène *(2 grilles sur 8)***
> 	- [ ] Lavage des mains
> 	- [ ] Respect de la pudeur avec drap
> - [ ] **2. Examen des hanches *(5 grilles sur 8)***
> 	- [ ] Inspection du dos *(3 grilles sur 8)*
> 	- [ ] Examen de la colonne vertébrale *(2 grilles sur 8)*
> 	- [ ] Test d'élévation jambe tendue (signe de Lasègue) *(Spondylarthrite ankylosante)*
> 	- [ ] Signe de Mennell *(Spondylarthrite ankylosante)*
> 	- [ ] Mobilité passive *(2 grilles sur 8)*
> 	- [ ] Douleur à la mobilisation *(Fracture vertébrale)*
> 	- [ ] Recherche de douleur *(1 grille sur 8)*
> 	- [ ] Palpation des processus épineux *(1 grille sur 8)*
> 	- [ ] Recherche de contracture paravertébrale *(1 grille sur 8)*
> - [ ] **3. Test de Lasègue (élévation jambe tendue) *(1 grille sur 8)***
> - [ ] **4. Examen des extrémités *(2 grilles sur 8)***
> 	- [ ] Inspection des membres inférieurs
> 	- [ ] Inspection des membres supérieurs *(Spondylarthrite ankylosante)*
> 	- [ ] Inspection des mains *(Spondylarthrite ankylosante)*
> 	- [ ] Examen du genou *(Spondylarthrite ankylosante)*
> 	- [ ] Examen de la cheville *(Spondylarthrite ankylosante)*
> - [ ] **5. Examen neurologique complet *(3 grilles sur 8)***
> 	- [ ] Examen ciblé des mouvements passifs et actifs *(2 grilles sur 8)*
> 	- [ ] Examen ciblé de la sensibilité *(1 grille sur 8)*
> 	- [ ] Réflexes ostéo-tendineux *(2 grilles sur 8)*
> 	- [ ] Examen ciblé de la marche *(2 grilles sur 8)*
> 	- [ ] Signe de Babinski *(1 grille sur 8)*
> 	- [ ] Sensibilité (tact, douleur, vibration) *(Fracture vertébrale)*
> 	- [ ] Force musculaire segmentaire *(Fracture vertébrale)*
> 	- [ ] Réflexe cutané plantaire *(Fracture vertébrale)*
> - [ ] **6. Examen tête et cou *(Spondylarthrite ankylosante)***
> 	- [ ] Inspection des conjonctives
> 	- [ ] Inspection de l'oropharynx
> - [ ] **7. Examen thoracique *(Spondylarthrite ankylosante)***
> 	- [ ] Inspection du thorax
> 	- [ ] Palpation du thorax
> 	- [ ] Percussion des champs pulmonaires
> 	- [ ] Auscultation des poumons
> - [ ] **8. Examen cutané *(Spondylarthrite ankylosante)***
> - [ ] **9. Inspection du dos *(Suspicion de myélome multiple (confirmation par ponction médullaire))***
> - [ ] **10. Douleur à la percussion et à la palpation *(Suspicion de myélome multiple (confirmation par ponction médullaire))***
> - [ ] **11. Mobilité *(Suspicion de myélome multiple (confirmation par ponction médullaire))***
> - [ ] **12. Inclinaison *(Suspicion de myélome multiple (confirmation par ponction médullaire))***
> - [ ] **13. Rétroversion *(Suspicion de myélome multiple (confirmation par ponction médullaire))***
> - [ ] **14. Rotation *(Suspicion de myélome multiple (confirmation par ponction médullaire))***
> - [ ] **15. Marche et station *(Suspicion de myélome multiple (confirmation par ponction médullaire))***
> - [ ] **16. Allure de la marche *(Suspicion de myélome multiple (confirmation par ponction médullaire))***
> - [ ] **17. Marche sur la pointe des pieds *(Suspicion de myélome multiple (confirmation par ponction médullaire))***
> - [ ] **18. Marche sur les talons *(Suspicion de myélome multiple (confirmation par ponction médullaire))***
> - [ ] **19. Test de Romberg *(Suspicion de myélome multiple (confirmation par ponction médullaire))***
> - [ ] **20. Motricité *(Suspicion de myélome multiple (confirmation par ponction médullaire))***
> - [ ] **21. Flexion de hanche (L1-L2) *(Suspicion de myélome multiple (confirmation par ponction médullaire))***
> - [ ] **22. Extension du genou (L3-L4) *(Suspicion de myélome multiple (confirmation par ponction médullaire))***
> - [ ] **23. Extension dorsale du pied (L4-L5) *(Suspicion de myélome multiple (confirmation par ponction médullaire))***
> - [ ] **24. Extension de l’hallux (L5) *(Suspicion de myélome multiple (confirmation par ponction médullaire))***
> - [ ] **25. Flexion plantaire du pied (S1) *(Suspicion de myélome multiple (confirmation par ponction médullaire))***
> - [ ] **26. Coordination *(Suspicion de myélome multiple (confirmation par ponction médullaire))***
> - [ ] **27. Épreuve talon-genou *(Suspicion de myélome multiple (confirmation par ponction médullaire))***
> - [ ] **28. Sensibilité *(Suspicion de myélome multiple (confirmation par ponction médullaire))***
> - [ ] **29. Réflexes *(Suspicion de myélome multiple (confirmation par ponction médullaire))***
> - [ ] **30. Signes radiculaires *(Suspicion de myélome multiple (confirmation par ponction médullaire))***
> - [ ] **31. Signe de Lasègue *(2 grilles sur 8)***
> - [ ] **32. Statut interniste *(Suspicion de myélome multiple (confirmation par ponction médullaire))***
> - [ ] **33. Inspection du rachis *(Fracture vertébrale)***
> - [ ] **34. Palpation du rachis *(Fracture vertébrale)***
> 	- [ ] Palpation des processus épineux
> 	- [ ] Douleur à la percussion
> 	- [ ] Recherche de contracture paravertébrale
> - [ ] **35. Tests de mobilité rachidienne *(2 grilles sur 8)***
> 	- [ ] Flexion antérieure *(Fracture vertébrale)*
> 	- [ ] Extension *(Fracture vertébrale)*
> 	- [ ] Inclinaisons latérales *(Fracture vertébrale)*
> 	- [ ] Rotations *(Fracture vertébrale)*
> 	- [ ] Résultat *(Fracture vertébrale)*
> 	- [ ] Test de Schober *(1 grille sur 8)*
> 	- [ ] Test d'Ott *(1 grille sur 8)*
> 	- [ ] Distance doigts-sol *(1 grille sur 8)*
> - [ ] **36. Test de compression axiale *(Fracture vertébrale)***
> - [ ] **37. Tests spécifiques *(Fracture vertébrale)***
> 	- [ ] Signe de Lasègue
> 	- [ ] Test de Lasègue controlatéral
> 	- [ ] Test de Bragard
> - [ ] **38. Pouls périphériques *(Fracture vertébrale)***
> 	- [ ] Pouls fémoraux
> 	- [ ] Pouls poplités
> 	- [ ] Pouls pédieux
> - [ ] **39. Observation de la marche *(1 grille sur 8)***
> 	- [ ] Schéma de marche
> 	- [ ] Marche sur la pointe des pieds
> 	- [ ] Marche sur les talons
> - [ ] **40. Examen en position debout *(1 grille sur 8)***
> 	- [ ] Statique (alignement, symétrie)
> 	- [ ] Dynamique (mouvements actifs)
> 	- [ ] Recherche de scoliose
> 	- [ ] Recherche de déformation étagée
> - [ ] **41. Examen en position assise *(1 grille sur 8)***
> 	- [ ] Palpation des processus épineux
> 	- [ ] Percussion vertébrale
> 	- [ ] Recherche de points douloureux
> - [ ] **42. Testing des réflexes *(1 grille sur 8)***
> 	- [ ] Réflexe rotulien (L3-L4)
> 	- [ ] Réflexe achilléen (S1)
> - [ ] **43. Testing musculaire segmentaire *(1 grille sur 8)***
> 	- [ ] L3/L4 : Quadriceps fémoral
> 	- [ ] L5 : Extenseur propre du gros orteil
> 	- [ ] S1 : Triceps sural
> - [ ] **44. Testing sensitif par dermatomes *(1 grille sur 8)***
> 	- [ ] L3 : Face interne de la cuisse
> 	- [ ] L4 : Face interne du mollet
> 	- [ ] L5 : Face dorsale du pied
> 	- [ ] S1 : Face latérale du pied
> - [ ] **45. Examen en décubitus *(1 grille sur 8)***
> 	- [ ] Recherche de contracture musculaire
> 	- [ ] Signe de Lasègue
> 	- [ ] Test de Lasègue controlatéral
> 	- [ ] Test de Bragard
> - [ ] **46. Examen vasculaire périphérique *(1 grille sur 8)***
> 	- [ ] Palpation des pouls périphériques (si irradiation dans les jambes)
> - [ ] **47. Toucher rectal *(3 grilles sur 8)***
> 	- [ ] Tonus sphinctérien *(2 grilles sur 8)*
> 	- [ ] Sensibilité péri-anale *(1 grille sur 8)*
> 	- [ ] Palpation de la prostate *(Cancer prostatique métastatique)*
> 	- [ ] Recherche de sang *(Cancer prostatique métastatique)*
> - [ ] **48. Inspection générale *(1 grille sur 8)***
> 	- [ ] État général
> 	- [ ] Faciès douloureux
> 	- [ ] Position antalgique
> - [ ] **49. Recherche du signe de Giordano *(1 grille sur 8)***
> 	- [ ] Percussion des fosses lombaires
> 	- [ ] Résultat
> - [ ] **50. Examen abdominal *(Colique néphrétique sur lithiase)***
> 	- [ ] Inspection du dos *(1 grille sur 8)*
> 	- [ ] Auscultation *(1 grille sur 8)*
> 	- [ ] Palpation superficielle et profonde *(1 grille sur 8)*
> 	- [ ] Recherche d'un globe vésical *(1 grille sur 8)*
> 	- [ ] Inspection: pas de distension *(1 grille sur 8)*
> 	- [ ] Palpation: sensibilité flanc gauche *(1 grille sur 8)*
> 	- [ ] Défense absente *(1 grille sur 8)*
> 	- [ ] Pas de masse palpable *(1 grille sur 8)*
> 	- [ ] Bruits hydroaériques présents *(1 grille sur 8)*
> 	- [ ] Pas de globe vésical *(1 grille sur 8)*
> - [ ] **51. Palpation des points urétéraux *(Colique néphrétique sur lithiase)***
> 	- [ ] Point urétéral supérieur
> 	- [ ] Point urétéral moyen
> 	- [ ] Point urétéral inférieur
> 	- [ ] Douleur provoquée le long du trajet urétéral *(1 grille sur 8)*
> 	- [ ] Comparaison bilatérale *(1 grille sur 8)*
> - [ ] **52. Examen des organes génitaux externes *(Colique néphrétique sur lithiase)***
> 	- [ ] Inspection vulvaire *(1 grille sur 8)*
> 	- [ ] Recherche d'écoulement *(1 grille sur 8)*
> 	- [ ] Inspection: testicules symétriques *(1 grille sur 8)*
> 	- [ ] Palpation testiculaire: indolore, pas de masse *(1 grille sur 8)*
> 	- [ ] Cordons spermatiques sans anomalie *(1 grille sur 8)*
> 	- [ ] Réflexe crémastérien présent *(1 grille sur 8)*
> - [ ] **53. Signes vitaux complémentaires *(1 grille sur 8)***
> 	- [ ] Température
> 	- [ ] État d'hydratation
> - [ ] **54. État général et comportement *(1 grille sur 8)***
> 	- [ ] Patient agité, ne trouve pas de position antalgique
> 	- [ ] Faciès douloureux
> 	- [ ] Pâleur, sueurs
> 	- [ ] Déambulation incessante
> 	- [ ] Anxiété manifeste
> - [ ] **55. Signes vitaux *(1 grille sur 8)***
> 	- [ ] Tension artérielle
> 	- [ ] Fréquence cardiaque
> 	- [ ] Température
> 	- [ ] Fréquence respiratoire
> - [ ] **56. Examen des fosses lombaires *(1 grille sur 8)***
> 	- [ ] Inspection: pas d'ecchymose, pas de tuméfaction
> 	- [ ] Palpation douce: sensibilité
> 	- [ ] Percussion: douleur à l'ébranlement lombaire gauche
> 	- [ ] Comparaison avec côté controlatéral
> 	- [ ] Recherche d'un contact lombaire
> - [ ] **57. Recherche de complications *(1 grille sur 8)***
> 	- [ ] Signes de pyélonéphrite
> 	- [ ] Signes de sepsis
> 	- [ ] Anurie
> 	- [ ] Rétention aiguë d'urine
> 	- [ ] État de choc
> - [ ] **58. Examens différentiels *(1 grille sur 8)***
> 	- [ ] Recherche appendicite
> 	- [ ] Éliminer anévrisme aorte
> 	- [ ] Examen vasculaire périphérique
> 	- [ ] Examen neurologique sommaire
> 	- [ ] Auscultation cardio-pulmonaire
> - [ ] **59. Examen ostéo-articulaire *(Cancer prostatique métastatique)***
> 	- [ ] Inspection du rachis
> 	- [ ] Palpation/percussion du rachis
> 	- [ ] Palpation muscles paravertébraux
> 	- [ ] Mobilité rachidienne (flexion/extension/rotation)
> 	- [ ] Signe de Lasègue
> - [ ] **60. Examen neurologique des membres inférieurs *(Cancer prostatique métastatique)***
> 	- [ ] Force motrice
> 	- [ ] Sensibilité
> 	- [ ] Réflexes ostéo-tendineux
> 	- [ ] Signe de Babinski
> 	- [ ] Marche

> [!success] 💊 Management — partagé par plusieurs diagnostics
> - [ ] **1. Communication avec le patient *(2 grilles sur 8)* — *Hernie discale · Spondylarthrite ankylosante***
> 	- [ ] Explications au patient des impressions diagnostiques préliminaires
> 	- [ ] Explication du plan de prise en charge
> 	- [ ] Utilisation d'un langage non médical et clarification des termes médicaux
> 	- [ ] Évaluation de l'accord du patient avec le plan diagnostique
> 	- [ ] Recherche des préoccupations et questions du patient
> - [ ] **2. Diagnostic principal *(3 grilles sur 8)* — *Colique néphrétique sur lithiase · Fracture vertébrale · Hernie discale***
> - [ ] **3. Prise en charge thérapeutique ambulatoire *(3 grilles sur 8)* — *Colique néphrétique sur lithiase · Fracture vertébrale · Hernie discale***

> [!success] 💊 Management — si Cancer prostatique métastatique
> - [ ] **1. Hypothèse diagnostique principale**
> 	- [ ] Cancer prostatique métastatique
> 	- [ ] Justification basée sur l'anamnèse et l'examen
> - [ ] **2. Examens d'imagerie**
> 	- [ ] Échographie résidu post-mictionnel
> 	- [ ] Échographie rénale
> 	- [ ] Imagerie selon PSA (CT TAP, scintigraphie osseuse, PET-PSMA)
> - [ ] **3. Résultats de laboratoire**
> 	- [ ] FSC
> 	- [ ] Fonction rénale
> 	- [ ] PSA
> 	- [ ] Phosphatases alcalines
> 	- [ ] Calcium
> - [ ] **4. Diagnostics différentiels**
> 	- [ ] Syndrome de la queue de cheval
> 	- [ ] Métastases osseuses d'autre origine
> 	- [ ] Myélome multiple
> 	- [ ] Sténose spinale
> 	- [ ] Infection (ostéomyélite, abcès épidural)
> - [ ] **5. Prise en charge proposée**
> 	- [ ] Référer à l'urologue
> 	- [ ] Antalgie adaptée
> 	- [ ] Évaluation urgence relative

> [!success] 💊 Management — si Colique néphrétique sur lithiase
> - [ ] **1. Examens complémentaires urgents**
> 	- [ ] Bandelette urinaire (confirmer hématurie) *(1 grille sur 2)*
> 	- [ ] ECBU avec recherche de cristaux *(1 grille sur 2)*
> 	- [ ] Créatinine, urée (fonction rénale)
> 	- [ ] Ionogramme sanguin, calcémie
> 	- [ ] FSC, CRP (éliminer infection) *(1 grille sur 2)*
> 	- [ ] Échographie rénale et vésicale en urgence *(1 grille sur 2)*
> 	- [ ] CT abdomen sans contraste (gold standard) si doute *(1 grille sur 2)*
> 	- [ ] Bandelette urinaire: hématurie dans 90% des cas *(1 grille sur 2)*
> 	- [ ] ECBU: hématurie microscopique, cristallurie, pH urinaire *(1 grille sur 2)*
> 	- [ ] FSC, CRP: syndrome inflammatoire si complication *(1 grille sur 2)*
> 	- [ ] Échographie rénale et vésicale: dilatation des cavités pyélocalicielles *(1 grille sur 2)*
> - [ ] **2. Diagnostics différentiels *(1 grille sur 2)***
> 	- [ ] Fracture vertébrale ostéoporotique
> 	- [ ] Pyélonéphrite aiguë
> 	- [ ] Lombalgie musculaire
> 	- [ ] Pathologie gynécologique (kyste ovarien tordu)
> 	- [ ] Anévrisme de l'aorte abdominale
> 	- [ ] Appendicite rétrocæcale (si à droite)
> 	- [ ] Diverticulite sigmoïdienne
> - [ ] **3. Prévention des récidives**
> 	- [ ] Hydratation abondante (> 2L/jour) *(1 grille sur 2)*
> 	- [ ] Régime adapté selon composition du calcul
> 	- [ ] Réduction apports sodés *(1 grille sur 2)*
> 	- [ ] Normalisation apports calciques *(1 grille sur 2)*
> 	- [ ] Traitement spécifique selon lithiase *(1 grille sur 2)*
> 	- [ ] Analyse spectrophotométrique du calcul expulsé *(1 grille sur 2)*
> 	- [ ] Bilan métabolique à distance (calcémie, uricémie, oxalurie) *(1 grille sur 2)*
> 	- [ ] Hyperhydratation: 2-3L/jour à vie *(1 grille sur 2)*
> 	- [ ] Oxalate de calcium: limiter oxalates (chocolat, thé) *(1 grille sur 2)*
> 	- [ ] Acide urique: alcalinisation urines, allopurinol *(1 grille sur 2)*
> 	- [ ] Phosphate de calcium: acidification urines *(1 grille sur 2)*
> 	- [ ] Surveillance régulière: échographie annuelle *(1 grille sur 2)*
> - [ ] **4. Indications d'hospitalisation**
> 	- [ ] Signes infectieux associés (urgence) *(1 grille sur 2)*
> 	- [ ] Rein unique fonctionnel *(1 grille sur 2)*
> 	- [ ] Insuffisance rénale aiguë
> 	- [ ] Douleur réfractaire au traitement *(1 grille sur 2)*
> 	- [ ] Calcul > 10 mm *(1 grille sur 2)*
> 	- [ ] Obstruction bilatérale *(1 grille sur 2)*
> 	- [ ] Colique néphrétique fébrile (urgence urologique) *(1 grille sur 2)*
> 	- [ ] Anurie (obstruction bilatérale ou rein unique) *(1 grille sur 2)*
> 	- [ ] Colique néphrétique hyperalgique résistante *(1 grille sur 2)*
> 	- [ ] Terrain particulier: grossesse, rein unique, transplanté *(1 grille sur 2)*
> 	- [ ] Impossibilité de prise en charge ambulatoire *(1 grille sur 2)*
> - [ ] **5. Prise en charge à distance *(1 grille sur 2)***
> 	- [ ] Analyse du calcul si récupéré
> 	- [ ] Bilan métabolique à 6 semaines
> 	- [ ] Calcium, phosphate, acide urique sanguins
> 	- [ ] Calciurie, phosphaturie, uraturie des 24h
> 	- [ ] PH urinaire, densité urinaire
> - [ ] **6. Information et éducation *(1 grille sur 2)***
> 	- [ ] Expliquer l'évolution naturelle
> 	- [ ] Calcul 90%
> 	- [ ] Importance de filtrer les urines
> 	- [ ] Signes d'alerte nécessitant reconsultation
> 	- [ ] Remise de documentation écrite
> - [ ] **7. Diagnostics différentiels de la colique néphrétique *(1 grille sur 2)***
> - [ ] **8. Imagerie pour confirmation diagnostique *(1 grille sur 2)***
> 	- [ ] TDM abdomino-pelvien sans injection (examen de référence)
> 	- [ ] Visualise 95% des calculs radio-opaques et radio-transparents
> 	- [ ] Localise précisément le calcul
> 	- [ ] Évalue le retentissement (dilatation)
> 	- [ ] Mesure la taille du calcul
> 	- [ ] ASP (Abdomen Sans Préparation): calculs radio-opaques seulement (80%)
> 	- [ ] Échographie: alternative si contre-indication TDM (grossesse)
> - [ ] **9. Traitement symptomatique de la crise *(1 grille sur 2)***
> - [ ] **10. Traitement urologique spécifique *(1 grille sur 2)***
> 	- [ ] Calculs < 5mm: expulsion spontanée dans 70% des cas
> 	- [ ] Calculs 5-10mm: expulsion dans 50% des cas
> 	- [ ] Lithotripsie extracorporelle (LEC) si calcul < 20mm
> 	- [ ] Urétéroscopie avec extraction ou fragmentation laser
> 	- [ ] Néphrostomie percutanée si infection + obstruction
> 	- [ ] Chirurgie ouverte exceptionnelle
> - [ ] **11. Complications à rechercher *(1 grille sur 2)***

> [!success] 💊 Management — si Fracture vertébrale
> - [ ] **1. Examens complémentaires urgents**
> 	- [ ] FSC, CRP, VS (exclusion processus inflammatoire)
> 	- [ ] Phosphatases alcalines (PAL), Gamma-GT (si PAL élevées)
> 	- [ ] Calcémie, phosphatémie
> 	- [ ] 25-OH vitamine D
> 	- [ ] TSH
> 	- [ ] Créatinine (fonction rénale, ostéopathie rénale)
> 	- [ ] Électrophorèse des protéines sériques (si suspicion myélome)
> - [ ] **2. Examens d'imagerie**
> 	- [ ] Radiographie du rachis lombaire (face et profil)
> 	- [ ] Densitométrie osseuse (DMO)
> 	- [ ] IRM rachidienne si doute diagnostique
> 	- [ ] Scintigraphie osseuse si suspicion métastases multiples
> - [ ] **3. Diagnostics différentiels**
> 	- [ ] Fracture vertébrale ostéoporotique
> 	- [ ] Métastase vertébrale (antécédent de cancer du sein)
> 	- [ ] Fracture pathologique sur autre cause (myélome, hyperparathyroïdie)
> 	- [ ] Spondylodiscite infectieuse
> 	- [ ] Lombalgie mécanique commune
> - [ ] **4. Suivi et surveillance**
> 	- [ ] Contrôle clinique à 4-6 semaines
> 	- [ ] Contrôle radiologique si aggravation
> 	- [ ] DMO de contrôle à 2 ans
> 	- [ ] Surveillance observance traitement
> 	- [ ] Dépistage nouvelles fractures

> [!success] 💊 Management — si Hernie discale
> - [ ] **1. Hypothèse diagnostique principale *(1 grille sur 2)***
> - [ ] **2. Examens complémentaires urgents**
> 	- [ ] Examen génital *(1 grille sur 2)*
> 	- [ ] Examens biologiques pour exclure processus inflammatoire (FSC, CRP, VS) *(1 grille sur 2)*
> 	- [ ] IRM lombaire selon évolution clinique et déficit neurologique *(1 grille sur 2)*
> 	- [ ] Radiographie lombaire si suspicion de spondylolisthésis *(1 grille sur 2)*
> 	- [ ] EMG si doute diagnostique après 6 semaines *(1 grille sur 2)*
> - [ ] **3. Examens d'imagerie *(1 grille sur 2)***
> 	- [ ] IRM du rachis
> 	- [ ] Radiographie du rachis
> 	- [ ] CT du rachis
> - [ ] **4. Examens spécialisés *(1 grille sur 2)***
> 	- [ ] Absorptiométrie biphotonique (DEXA)
> - [ ] **5. Conseil et prévention *(1 grille sur 2)***
> 	- [ ] Conseil sur l'arrêt du tabac
> 	- [ ] Réaction appropriée au défi concernant la dépendance aux antalgiques
> - [ ] **6. Diagnostics différentiels *(1 grille sur 2)***
> 	- [ ] Fracture vertébrale ostéoporotique
> 	- [ ] Protrusion discale sans hernie franche
> 	- [ ] Canal lombaire étroit
> 	- [ ] Spondylolisthésis
> 	- [ ] Contracture musculaire paravertébrale
> 	- [ ] Processus inflammatoire/infectieux (spondylodiscite)
> 	- [ ] Processus tumoral (métastase, tumeur primitive)
> - [ ] **7. Orientation et suivi *(1 grille sur 2)***
> 	- [ ] Orientation orthopédie/neurochirurgie selon évolution
> 	- [ ] Contrôle à 2 semaines
> 	- [ ] IRM si pas d'amélioration à 4-6 semaines
> 	- [ ] Arrêt de travail selon profession
> 	- [ ] Éducation sur l'évolution naturelle favorable (90% à 6 semaines)
> - [ ] **8. Prévention des récidives *(1 grille sur 2)***
> 	- [ ] École du dos
> 	- [ ] Renforcement musculaire après phase aiguë
> 	- [ ] Ergonomie au travail
> 	- [ ] Perte de poids si surcharge pondérale
> 	- [ ] Activité physique régulière

> [!success] 💊 Management — si Métastases osseuses
> *Aucune grille du corpus ne documente ce diagnostic* — il est pourtant attendu de cette SSP. **Trou de révision à combler ailleurs.**

> [!success] 💊 Management — si Ostéoporose
> *Aucune grille du corpus ne documente ce diagnostic* — il est pourtant attendu de cette SSP. **Trou de révision à combler ailleurs.**

> [!success] 💊 Management — si Spondylarthrite ankylosante
> - [ ] **1. Hypothèse diagnostique principale**
> - [ ] **2. Examens complémentaires urgents**
> 	- [ ] Examen génital
> 	- [ ] FSC, VS
> - [ ] **3. Examens d'imagerie**
> 	- [ ] Radiographie du rachis et des articulations sacro-iliaques
> 	- [ ] Radiographie des mains et du genou droit
> - [ ] **4. Conseil et prévention**
> 	- [ ] Réaction appropriée au défi concernant la dépendance aux antalgiques
> 	- [ ] Conseil sur les drogues récréatives
> 	- [ ] Conseil sur les pratiques sexuelles sûres
> - [ ] **5. Examens immunologiques**
> 	- [ ] Facteur rhumatoïde, anticorps anti-nucléaires, HLA-B27
> - [ ] **6. Examens microbiologiques**
> 	- [ ] Tests d'amplification des acides nucléiques pour chlamydia et gonocoque
> 	- [ ] Cultures de selles et d'urine
> 	- [ ] Test VIH

> [!success] 💊 Management — si Suspicion de myélome multiple (confirmation par ponction médullaire)
> - [ ] **1. Radiographie conventionnelle**
> - [ ] **2. Fracture atraumatique**
> - [ ] **3. Indice de maladie osseuse**
> - [ ] **4. Bilan complémentaire nécessaire**
> - [ ] **5. Résultats de laboratoire**
> - [ ] **6. Protéines sériques**
> - [ ] **7. Résultat du CT**
> - [ ] **8. Commentaire des résultats**
> - [ ] **9. Constellation CRAB**
> - [ ] **10. Gammapathie monoclonale (IgG) avec restriction des chaînes légères**
> - [ ] **11. Diagnostic de travail**
> - [ ] **12. Affections ostéométaboliques**
> - [ ] **13. Ostéoporose primaire**
> - [ ] **14. Endocriniennes**
> - [ ] **15. Métaboliques / nutritionnelles**
> - [ ] **16. Médicamenteuses**
> - [ ] **17. Systémiques / inflammatoires**
> - [ ] **18. Autres**
> - [ ] **19. Causes infectieuses**
> - [ ] **20. Spondylodiscite / ostéomyélite**
> - [ ] **21. Causes néoplasiques**
> - [ ] **22. Myélome multiple**
> - [ ] **23. Métastases osseuses**
> - [ ] **24. Tumeurs osseuses primitives**
> - [ ] **25. Autres néoplasies hématologiques**
