---
aliases:
  - "Mémento Boiterie de l'Enfant"
type: memento-ecos-ssp
ssp: "Boiterie de l'Enfant"
specialite: "Pédiatrie"
cas: 2
diagnostics: 1
attendus_documentes_ailleurs: 0
attendus_absents_du_corpus: 0
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

> [!warning] Mémento mixte — 1 grille officielle, 1 non officielles
> **RESCOS-9b** fait partie des **neuf grilles officielles** et fait donc
> autorité ; elle est signalée ⭐️ dans l'encadré ci-dessous. Les 1
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

# Boiterie de l'Enfant

*Pédiatrie · 2 grilles · 1 diagnostic documenté* — [[SSP — Boiterie de l'Enfant]]

> [!abstract] Les 2 grilles fusionnées
> - **RESCOS-9** — Arthrite septique `explicite` · [grille](<file:///Users/damienfulliquet/Developer/GitHub/grilles-ecos/cases/rescos/RESCOS-9_-_Boiterie_pe_diatrique_-_Grille_ECOS.html>)
> - **RESCOS-9b** ⭐️ **officielle** — Arthrite septique `explicite` · [grille](<file:///Users/damienfulliquet/Developer/GitHub/grilles-ecos/cases/rescos/RESCOS-9b_-_Boiterie_pe_diatrique_-_Fillette_de_2_ans_-_Grille_ECOS.html>)

> [!note] 📋 Anamnèse
> - [ ] **1. Caractérisation de la boiterie**
> 	- [ ] Début
> 	- [ ] Durée
> 	- [ ] Évolution
> 	- [ ] Localisation
> - [ ] **2. Caractérisation de la hanche**
> 	- [ ] Rougeur
> 	- [ ] Chaleur
> 	- [ ] Œdèmes
> 	- [ ] Perte de fonction
> - [ ] **3. Atteinte d'une autre articulation**
> 	- [ ] Actuellement
> 	- [ ] Dans le passé
> - [ ] **4. Antécédents de traumatismes des membres inférieurs**
> 	- [ ] Récents
> 	- [ ] Anciens
> - [ ] **5. Caractérisation des douleurs**
> 	- [ ] Durée
> 	- [ ] Intensité
> 	- [ ] Réponse aux antalgiques
> - [ ] **6. Caractérisation de la fièvre**
> 	- [ ] Durée
> 	- [ ] Intensité
> 	- [ ] Réponse au fébrifuges
> - [ ] **7. Caractérisation de la rhinorrhée**
> 	- [ ] Début
> 	- [ ] Couleur/aspect des sécrétions
> 	- [ ] Toux associée
> - [ ] **8. Présence d'éruptions cutanées**
> - [ ] **9. État général**
> 	- [ ] Activités
> 	- [ ] Apathie
> 	- [ ] Comportement
> - [ ] **10. Antécédents similaires**
> 	- [ ] Chez la patiente
> 	- [ ] Dans la famille
> - [ ] **11. Antécédents médicaux**
> 	- [ ] Maladies
> 	- [ ] Chirurgies
> 	- [ ] Hospitalisations
> 	- [ ] Médicaments
> 	- [ ] Vaccins
> - [ ] **12. Antécédents familiaux**
> - [ ] **13. Développement de l'enfant**
> 	- [ ] Grossesse
> 	- [ ] Événements néonataux
> 	- [ ] Croissance
> 	- [ ] Développement psycho-moteur

> [!success] 💊 Management — si Arthrite septique
> - [ ] **1. Diagnostic principal - arthrite septique de la hanche**
> - [ ] **2. Diagnostic différentiel**
> 	- [ ] Ostéomyélite
> 	- [ ] Synovite aiguë transitoire (rhume de hanche)
> 	- [ ] Maladie de Legg-Calvé-Perthes
> - [ ] **3. Investigations complémentaires - bilan sanguin**
> 	- [ ] FSC
> 	- [ ] VS / CRP
> 	- [ ] Hémoculture
> - [ ] **4. Investigations complémentaires - imagerie**
> 	- [ ] Radiographie
> 	- [ ] Échographie
> - [ ] **5. Prise en charge - propose une hospitalisation ou de référer la patiente en orthopédie**
