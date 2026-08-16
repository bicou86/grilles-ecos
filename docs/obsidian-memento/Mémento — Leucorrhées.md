---
aliases:
  - "Mémento Leucorrhées"
type: memento-ecos-ssp
ssp: "Leucorrhées"
specialite: "Gynéco-Obstétrique"
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

# Leucorrhées

*Gynéco-Obstétrique · 1 grille · 1 diagnostic documenté* — [[SSP — Leucorrhées]]

> [!abstract] La seule grille de cette SSP
> - **AMBOSS-32** — Infection au papillomavirus humain (VPH) `premier-dd` · [grille](<file:///Users/damienfulliquet/Developer/GitHub/grilles-ecos/cases/amboss/AMBOSS-32_-_Le_sion_ge_nitale_-_Femme_17_ans_-_Grille_ECOS.html>)

> [!note] 📋 Anamnèse
> - [ ] **1. Motif principal**
> - [ ] **2. Caractérisation de la lésion génitale**
> 	- [ ] Description du changement cutané
> 	- [ ] Lésion douloureuse
> 	- [ ] Début
> 	- [ ] Évolution temporelle
> 	- [ ] Événements précipitants
> 	- [ ] Progression
> 	- [ ] Épisodes antérieurs
> 	- [ ] Facteurs améliorants
> 	- [ ] Facteurs aggravants
> 	- [ ] Symptômes associés
> 	- [ ] Fréquence
> 	- [ ] Autres symptômes urinaires (ex: sang dans les urines)
> - [ ] **3. Recherche de symptômes spécifiques pour lésions génitales et dysurie**
> 	- [ ] Voyage récent
> 	- [ ] Fièvre/frissons
> 	- [ ] Éruption cutanée/changements cutanés
> 	- [ ] Problèmes intestinaux
> 	- [ ] Appétit
> 	- [ ] Variations pondérales
> 	- [ ] Infections récentes
> 	- [ ] Gonflement dans l'aine
> 	- [ ] Douleur dans l'aine
> - [ ] **4. Antécédents médicaux**
> - [ ] **5. Allergies**
> - [ ] **6. Médicaments**
> - [ ] **7. Hospitalisations et antécédents chirurgicaux**
> 	- [ ] Hospitalisations
> 	- [ ] Antécédents chirurgicaux
> - [ ] **8. Contacts malades et antécédents familiaux**
> 	- [ ] Contacts malades
> 	- [ ] Antécédents familiaux
> - [ ] **9. Habitudes et mode de vie**
> 	- [ ] Travail
> 	- [ ] Domicile
> 	- [ ] Alcool
> 	- [ ] Drogues récréatives
> 	- [ ] Tabac
> 	- [ ] Tabac dans le passé
> - [ ] **10. Antécédents sexuels**
> 	- [ ] Activité sexuelle
> 	- [ ] Avec qui
> 	- [ ] Hommes ou femmes
> 	- [ ] Nombre de partenaires au cours de la dernière année
> 	- [ ] Protection
> 	- [ ] Antécédents d'infections sexuellement transmissibles
> - [ ] **11. Antécédents gynécologiques**
> 	- [ ] Dernières règles
> 	- [ ] Ménarche
> 	- [ ] Durée des règles
> 	- [ ] Règles régulières
> 	- [ ] Combien de tampons par jour
> 	- [ ] Pertes vaginales
> 	- [ ] Apparence des pertes vaginales
> 	- [ ] Odeur des pertes vaginales
> 	- [ ] Démangeaisons vaginales
> 	- [ ] Sécheresse vaginale
> 	- [ ] Grossesses
> 	- [ ] Avortements/fausses couches
> 	- [ ] Vaccination contre le VPH
> 	- [ ] Série de vaccination complétée

> [!tip] 🩺 Status
> - [ ] **1. Mesures d'hygiène**
> 	- [ ] Lavage des mains
> 	- [ ] Respect de la pudeur avec drap
> - [ ] **2. Examen de la tête, yeux, oreilles, nez et gorge**
> 	- [ ] Inspection de l'oropharynx
> - [ ] **3. Examen du cou**
> 	- [ ] Palpation des ganglions lymphatiques de la tête et du cou
> - [ ] **4. Examen du dos**
> 	- [ ] Examen de la sensibilité de l'angle costo-vertébral
> - [ ] **5. Examen abdominal**
> 	- [ ] Inspection de l'abdomen
> 	- [ ] Auscultation de l'abdomen
> 	- [ ] Percussion de l'abdomen
> 	- [ ] Palpation de l'abdomen
> 	- [ ] Palpation des ganglions lymphatiques inguinaux
> - [ ] **6. Examen cutané**

> [!success] 💊 Management — si Infection au papillomavirus humain (VPH)
> - [ ] **1. Hypothèses diagnostiques**
> - [ ] **2. Examens complémentaires de première intention**
> 	- [ ] Examen pelvien
> 	- [ ] Examen rectal
> 	- [ ] Test VIH
> - [ ] **3. Tests diagnostiques IST**
> 	- [ ] Test rapide de la réagine plasmatique
> 	- [ ] Microscopie à fond noir
> 	- [ ] Tests d'amplification des acides nucléiques pour chlamydia et gonorrhée
> - [ ] **4. Autres examens**
> 	- [ ] Bandelette urinaire, analyse d'urine
> 	- [ ] Préparation à l'état frais avec test KOH
> - [ ] **5. Communication avec la patiente**
> 	- [ ] Explications à la patiente des impressions diagnostiques préliminaires
> 	- [ ] Explication du plan de prise en charge
> 	- [ ] Utilisation d'un langage non médical et clarification des termes médicaux
> 	- [ ] Évaluation de l'accord de la patiente avec le plan diagnostique
> 	- [ ] Demande de consentement pour effectuer le test VIH
> 	- [ ] Recherche des préoccupations et questions de la patiente
> - [ ] **6. Conseil et soutien**
> 	- [ ] Conseil sur les pratiques sexuelles plus sûres
> 	- [ ] Conseil sur l'utilisation de préservatifs sans latex
> 	- [ ] Recommandation de compléter la série de vaccination VPH
> 	- [ ] Réaction appropriée au défi sur la confidentialité
> 	- [ ] Éducation sur la prévention des IST
