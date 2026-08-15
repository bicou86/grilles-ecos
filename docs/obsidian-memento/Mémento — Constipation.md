---
aliases:
  - "Mémento Constipation"
type: memento-ecos-ssp
ssp: "Constipation"
specialite: "Gastro-Hépatologie"
cas: 1
diagnostics: 1
attendus_documentes_ailleurs: 0
attendus_absents_du_corpus: 3
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

# Constipation

*Gastro-Hépatologie · 1 grille · 1 diagnostic documenté · 3 attendus absents du corpus* — [[SSP — Constipation]]

> [!abstract] La seule grille de cette SSP
> - **German-12** — Obstacle colique `corrige` · [grille](<file:///Users/damienfulliquet/Developer/GitHub/grilles-ecos/cases/german/German-12_-_Constipation_-_Grille_ECOS.html>)

> [!note] 📋 Anamnèse
> - [ ] **1. Présentation avec nom, fonction et tâche**
> - [ ] **2. Question d'entrée ouverte → Symptôme principal**
> - [ ] **3. Question de clarification : "Qu'entendez-vous par constipation ?"**
> - [ ] **4. Évolution temporelle**
> 	- [ ] Durée
> 	- [ ] Évolution : intermittente – continue – progressive
> 	- [ ] Fréquence des selles < 3/semaine = pathologique
> - [ ] **5. Caractéristiques des selles**
> 	- [ ] Consistance : liquide – pâteuse – moulée – fragments durs
> 	- [ ] Effort de poussée important
> 	- [ ] Sensation d'évacuation incomplète
> 	- [ ] Sensation de blocage
> 	- [ ] Évacuation digitale
> - [ ] **6. Douleurs lors de la défécation**
> - [ ] **7. Aspect des selles**
> 	- [ ] Couleur : grise (acholique) – noire (méléna) – rouge (hématochézie)
> 	- [ ] Odeur : normale – très malodorante
> 	- [ ] Sang dans/sur les selles
> 	- [ ] Mucus/pus dans les selles
> - [ ] **8. Épisodes antérieurs**
> - [ ] **9. Volume des selles par rapport à l'habitude**
> - [ ] **10. Facteurs d'influence**
> 	- [ ] Régime alimentaire
> 	- [ ] Gluten
> 	- [ ] Coloscopie antérieure
> - [ ] **11. Symptômes d'accompagnement**
> 	- [ ] Fièvre
> 	- [ ] Céphalées
> 	- [ ] Douleurs musculaires/articulaires
> 	- [ ] Éruption cutanée
> 	- [ ] Production/couleur urinaire
> 	- [ ] Vertiges/hypotension orthostatique
> - [ ] **12. Symptômes B**
> - [ ] **13. Symptômes thyroïdiens**
> 	- [ ] Intolérance au froid
> 	- [ ] Prise de poids
> 	- [ ] Chute de cheveux
> 	- [ ] Modifications cutanées
> - [ ] **14. Symptômes gastro-intestinaux**
> 	- [ ] Nausées/vomissements
> 	- [ ] Ballonnements/flatulences
> 	- [ ] Diarrhée paradoxale
> 	- [ ] Douleurs abdominales
> 	- [ ] Douleurs rectales
> 	- [ ] Incontinence fécale
> - [ ] **15. Antécédents personnels**
> 	- [ ] Maladies antérieures
> 	- [ ] Opérations/accouchements
> 	- [ ] Cancer actif
> 	- [ ] Diabète
> 	- [ ] Thyroïde
> - [ ] **16. Allergies**
> - [ ] **17. Médicaments**
> 	- [ ] Vitamine D + Ca2+
> 	- [ ] Euthyrox 50 μg/j
> 	- [ ] Antiacides
> 	- [ ] Anticholinergiques
> 	- [ ] Diurétiques
> 	- [ ] Opiacés
> - [ ] **18. Toxiques**
> - [ ] **19. Anamnèse familiale**
> 	- [ ] Cancer du côlon
> 	- [ ] Autres cancers
> 	- [ ] Maladies thyroïdiennes
> - [ ] **20. Anamnèse sociale**
> 	- [ ] Alimentation
> 	- [ ] Modification de l'alimentation
> 	- [ ] Quantité de boisson
> 	- [ ] Profession
> 	- [ ] Loisirs/activité physique
> - [ ] **21. Anamnèse systémique**

> [!tip] 🩺 Status
> - [ ] **1. Examen abdominal**
> 	- [ ] Inspection
> 	- [ ] Auscultation
> 	- [ ] Percussion
> 	- [ ] Palpation
> 	- [ ] Évaluation du turgor cutané et recherche d'efflorescences
> - [ ] **2. Toucher rectal**
> - [ ] **3. Examen thyroïdien**
> - [ ] **4. Examen cardio-pulmonaire**
> 	- [ ] Auscultation cardiaque
> 	- [ ] Auscultation pulmonaire

> [!success] 💊 Management — si Fécalome
> *Aucune grille du corpus ne documente ce diagnostic* — il est pourtant attendu de cette SSP. **Trou de révision à combler ailleurs.**

> [!success] 💊 Management — si Mucoviscidose
> *Aucune grille du corpus ne documente ce diagnostic* — il est pourtant attendu de cette SSP. **Trou de révision à combler ailleurs.**

> [!success] 💊 Management — si Obstacle colique
> - [ ] **1. Diagnostic de suspicion**
> - [ ] **2. Diagnostics différentiels**
> - [ ] **3. Red flags - Signaux d'alarme**
> - [ ] **4. Examens diagnostiques**
> 	- [ ] Laboratoire : FSC, CRP, leucocytes, créatinine, électrolytes (Na, K, Ca), TSH, glucose
> 	- [ ] Transaminases, Gamma-GT, phosphatases alcalines (PAL), albumine, Quick/aPTT
> 	- [ ] Test FIT (recherche de sang occulte dans les selles)
> 	- [ ] US abdominale ou CT abdomen
> 	- [ ] Coloscopie
> - [ ] **5. Reconnaissance de pathologie sur imagerie/coloscopie**
> - [ ] **6. Traitement proposé (médicaments/chirurgie)**
> - [ ] **7. Organisation si nécessaire d'un transfert hospitalier**

> [!success] 💊 Management — si Péritonite
> *Aucune grille du corpus ne documente ce diagnostic* — il est pourtant attendu de cette SSP. **Trou de révision à combler ailleurs.**
