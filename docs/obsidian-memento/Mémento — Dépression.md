---
aliases:
  - "Mémento Dépression"
type: memento-ecos-ssp
ssp: "Dépression"
specialite: "Psychiatrie"
cas: 1
diagnostics: 1
attendus_documentes_ailleurs: 0
attendus_absents_du_corpus: 0
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

# Dépression ⭐️

*Psychiatrie · 1 grille · 1 diagnostic documenté* — [[SSP — Dépression]]

> [!abstract] La seule grille de cette SSP
> - **RESCOS-13** — Dépression `explicite` · [grille](<file:///Users/damienfulliquet/Developer/GitHub/grilles-ecos/cases/rescos/RESCOS-13_-_De_pression_-_Grille_ECOS.html>)

> [!note] 📋 Anamnèse
> - [ ] **1. Exploration des symptômes dépressifs**
> 	- [ ] Humeur triste
> 	- [ ] Anhédonie
> 	- [ ] Fatigue/perte d'énergie
> 	- [ ] Troubles du sommeil
> 	- [ ] Troubles de l'appétit
> 	- [ ] Isolement social
> - [ ] **2. Facteurs déclenchants**
> 	- [ ] Rupture amoureuse
> 	- [ ] Déménagement récent
> 	- [ ] Difficultés scolaires
> 	- [ ] Isolement social
> - [ ] **3. Évaluation du risque suicidaire - Idéation**
> 	- [ ] Présence d'idées suicidaires
> 	- [ ] Fréquence des pensées suicidaires
> 	- [ ] Intensité du désir de mort
> 	- [ ] Ambivalence face à la mort
> - [ ] **4. Évaluation du risque suicidaire - Planification**
> 	- [ ] Scénario établi
> 	- [ ] Moyen choisi
> 	- [ ] Date prévue
> 	- [ ] Accessibilité des moyens
> 	- [ ] Préparatifs effectués
> - [ ] **5. Antécédents psychiatriques**
> 	- [ ] Tentative de suicide antérieure
> 	- [ ] Diagnostic antérieur
> 	- [ ] Suivis psychiatriques antérieurs
> 	- [ ] Hospitalisations psychiatriques
> - [ ] **6. Antécédents familiaux**
> 	- [ ] Suicide dans la famille
> 	- [ ] Troubles psychiatriques familiaux
> 	- [ ] Antécédents médicaux
> - [ ] **7. Habitudes et consommations**
> 	- [ ] Alcool
> 	- [ ] Drogues
> 	- [ ] Tabac
> 	- [ ] Changements récents dans les habitudes
> - [ ] **8. Symptômes associés**
> 	- [ ] Douleur thoracique
> 	- [ ] Anxiété
> 	- [ ] Autres symptômes somatiques
> - [ ] **9. Évaluation du fonctionnement**
> 	- [ ] Fonctionnement social
> 	- [ ] Fonctionnement scolaire
> 	- [ ] Activités quotidiennes

> [!success] 💊 Management — si Dépression
> - [ ] **1. Hypothèse diagnostique principale**
> 	- [ ] Épisode dépressif majeur avec risque suicidaire élevé
> - [ ] **2. Diagnostics différentiels évoqués**
> 	- [ ] Trouble de la personnalité borderline
> 	- [ ] Trouble bipolaire
> 	- [ ] Trouble de l'adaptation
> 	- [ ] Trouble lié aux substances
> - [ ] **3. Évaluation du risque suicidaire selon RUD**
> 	- [ ] Risque
> 	- [ ] Urgence
> 	- [ ] Dangerosité
> 	- [ ] Conclusion: risque élevé
> - [ ] **4. Prise en charge immédiate**
> 	- [ ] Hospitalisation en psychiatrie
> 	- [ ] Mesures de protection
> 	- [ ] Retrait des moyens létaux
> 	- [ ] Surveillance rapprochée
> - [ ] **5. Plan thérapeutique**
> 	- [ ] Traitement antidépresseur
> 	- [ ] Psychothérapie
> 	- [ ] Soutien psychosocial
> 	- [ ] Implication de la famille
> - [ ] **6. Communication avec le patient**
> 	- [ ] Explication du diagnostic
> 	- [ ] Validation de la souffrance
> 	- [ ] Explication de la nécessité d'hospitalisation
> 	- [ ] Alliance thérapeutique
