---
aliases:
  - "Mémento Nausées, Vomissements & Hématémèse"
type: memento-ecos-ssp
ssp: "Nausées, Vomissements & Hématémèse"
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

# Nausées, Vomissements & Hématémèse

*1 grille · 1 diagnostic documenté* — [[SSP — Nausées, Vomissements & Hématémèse]]

> [!abstract] La seule grille de cette SSP
> - **AMBOSS-5** — Grossesse (suivi/conseils) `premier-dd` · [grille](<file:///Users/damienfulliquet/Developer/GitHub/grilles-ecos/cases/amboss/AMBOSS-5_-_Nause_es_-_Femme_19_ans_-_Grille_ECOS.html>)

> [!note] 📋 Anamnèse
> - [ ] **1. Motif principal**
> - [ ] **2. Caractérisation des nausées et vomissements**
> 	- [ ] Vomissements
> 	- [ ] Couleur
> 	- [ ] Sang
> 	- [ ] Début
> 	- [ ] Constant/intermittent
> 	- [ ] Événements précipitants
> 	- [ ] Progression
> 	- [ ] Épisodes antérieurs
> 	- [ ] Facteurs améliorants
> 	- [ ] Facteurs aggravants
> - [ ] **3. Symptômes associés**
> - [ ] **4. Recherche de symptômes spécifiques**
> 	- [ ] Gêne urinaire
> 	- [ ] Voyage récent
> 	- [ ] Œdème des chevilles
> 	- [ ] Fièvre/frissons
> 	- [ ] Fatigue
> 	- [ ] Éruption/changements cutanés
> 	- [ ] Douleurs articulaires
> 	- [ ] Troubles du transit
> 	- [ ] Appétit
> 	- [ ] Variations pondérales
> 	- [ ] Infections récentes
> 	- [ ] Douleurs abdominales
> 	- [ ] Douleurs dorsales
> 	- [ ] Augmentation/sensibilité des seins
> - [ ] **5. Antécédents médicaux**
> - [ ] **6. Antécédents chirurgicaux**
> - [ ] **7. Allergies**
> - [ ] **8. Médicaments**
> - [ ] **9. Hospitalisations**
> - [ ] **10. Antécédents familiaux**
> 	- [ ] Parents
> 	- [ ] Fratrie
> - [ ] **11. Habitudes et mode de vie**
> 	- [ ] Occupation
> 	- [ ] Domicile
> 	- [ ] Alcool
> 	- [ ] Drogues illicites
> 	- [ ] Tabac
> 	- [ ] Alimentation
> 	- [ ] Contacts malades
> - [ ] **12. Histoire sexuelle et gynécologique**
> 	- [ ] Activité sexuelle
> 	- [ ] Avec qui
> 	- [ ] Hommes ou femmes
> 	- [ ] Nombre de partenaires dans l'année
> 	- [ ] Protection
> 	- [ ] Quand l'implant a-t-il été posé
> 	- [ ] IST antérieures
> 	- [ ] Douleurs pendant les rapports
> 	- [ ] Dernières règles
> 	- [ ] Ménarche
> 	- [ ] Durée des règles
> 	- [ ] Règles régulières
> 	- [ ] Combien de tampons par jour
> 	- [ ] Pertes vaginales
> 	- [ ] Démangeaisons vaginales
> 	- [ ] Grossesses

> [!tip] 🩺 Status
> - [ ] **1. Mesures d'hygiène**
> 	- [ ] Lavage des mains
> 	- [ ] Respect de la pudeur avec drap
> - [ ] **2. Examen du dos**
> 	- [ ] Examen de la sensibilité de l'angle costo-vertébral
> - [ ] **3. Examen cardiovasculaire**
> - [ ] **4. Examen pulmonaire**
> - [ ] **5. Examen abdominal**
> 	- [ ] Inspection de l'abdomen
> 	- [ ] Auscultation de l'abdomen
> 	- [ ] Percussion de l'abdomen
> 	- [ ] Palpation de l'abdomen
> - [ ] **6. Signes d'appendicite**
> - [ ] **7. Examen cutané**

> [!success] 💊 Management — si Grossesse (suivi/conseils)
> - [ ] **1. Hypothèses diagnostiques**
> - [ ] **2. Examens complémentaires urgents**
> 	- [ ] Examen pelvien
> 	- [ ] Prélèvements cervicaux et urétraux pour PCR gonocoque et chlamydia
> 	- [ ] Analyse d'urine
> 	- [ ] Β-hCG sérique
> 	- [ ] FSC, VS, électrolytes
> - [ ] **3. Examens d'imagerie**
> 	- [ ] US abdominale
> 	- [ ] US transvaginale
> - [ ] **4. Communication avec la patiente**
> 	- [ ] Explications au patient des impressions diagnostiques préliminaires
> 	- [ ] Explication du plan de prise en charge
> 	- [ ] Utilisation d'un langage non médical et clarification des termes médicaux
> 	- [ ] Évaluation de l'accord du patient avec le plan diagnostique
> 	- [ ] Recherche des préoccupations et questions du patient
> - [ ] **5. Conseil et prévention**
> 	- [ ] Conseil sur les pratiques sexuelles sûres
> 	- [ ] Réaction appropriée au défi concernant la grossesse
