---
aliases:
  - "Mémento Diplopie"
type: memento-ecos-ssp
ssp: "Diplopie"
specialite: "Ophtalmologie"
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

# Diplopie

*Ophtalmologie · 1 grille · 1 diagnostic documenté* — [[SSP — Diplopie]]

> [!abstract] La seule grille de cette SSP
> - **RESCOS-16** — Myasthénie grave `explicite` · [grille](<file:///Users/damienfulliquet/Developer/GitHub/grilles-ecos/cases/rescos/RESCOS-16_-_Diplopie_-_Grille_ECOS.html>)

> [!note] 📋 Anamnèse
> - [ ] **1. Caractérisation des symptômes**
> 	- [ ] Faiblesse
> 	- [ ] Ptose
> 	- [ ] Diplopie
> 	- [ ] Trouble respiratoire
> - [ ] **2. Exploration d'autres symptômes neurologiques**
> 	- [ ] Troubles sensitifs
> 	- [ ] Baisse d'acuité visuelle
> 	- [ ] Céphalées
> 	- [ ] Trouble du langage (dysarthrie ou aphasie)
> 	- [ ] Vertiges
> 	- [ ] Fasciculations
> - [ ] **3. Cinétique d'évolution**
> 	- [ ] Début
> 	- [ ] Évolution
> 	- [ ] Dégradation récente
> 	- [ ] Horaire spécifique
> - [ ] **4. Anamnèse systémique**
> 	- [ ] Fièvre
> 	- [ ] Infection récente
> 	- [ ] Atteinte d'autres systèmes (digestif, cutané, perte de poids récente etc)
> 	- [ ] Consommation de conserves artisanales
> 	- [ ] Plaie/blessure récente
> - [ ] **5. Contexte**
> 	- [ ] Antécédents médico-chirurgicaux
> 	- [ ] Médicaments
> 	- [ ] Anamnèse familiale
> 	- [ ] Allergies
> 	- [ ] Habitus

> [!tip] 🩺 Status
> - [ ] **1. NC III IV VI**
> 	- [ ] Observation de ptose
> 	- [ ] Constate la ptose à bascule
> 	- [ ] Oculomotricité
> - [ ] **2. NC II III**
> 	- [ ] Champs visuels
> 	- [ ] Acuité visuelle
> 	- [ ] Réflexes photomoteurs directs ET croisés
> - [ ] **3. NC V VII VIII**
> 	- [ ] Sensibilité de la face aux territoires V1, V2 & V3
> 	- [ ] Motricité de la face
> 	- [ ] Test auditif
> - [ ] **4. NC XI - motricité de la tête & du cou**
> - [ ] **5. NC IX XII**
> 	- [ ] Évaluation de la motricité de la langue
> 	- [ ] Inspection de la luette
> - [ ] **6. Tests spécifiques à la myasthénie**
> 	- [ ] Ice Pack Test
> 	- [ ] Simpson
> - [ ] **7. Force**
> 	- [ ] Épreuves de stabilisation
> 	- [ ] Force segmentaire aux 4 membres
> 	- [ ] Recherche fatigabilité
> - [ ] **8. Réflexes**
> 	- [ ] Réflexes ostéotendineux
> 	- [ ] Réflexes cutanés plantaires
> - [ ] **9. Dépistage trouble sensitif**

> [!success] 💊 Management — si Myasthénie grave
> - [ ] **1. Hypothèse diagnostique principale - myasthénie grave**
> - [ ] **2. Diagnostics différentiels**
> 	- [ ] Botulisme
> 	- [ ] Syndrome de Lambert Eaton
> 	- [ ] Sclérose latérale amyotrophique (SLA - Maladie de Charcot)
> 	- [ ] Syndrome de Guillain-Barré
> 	- [ ] Atteinte du tronc cérébral
> - [ ] **3. Examens complémentaires**
> 	- [ ] Dosage anticorps anti RAch
> 	- [ ] ENMG
> 	- [ ] CT à la recherche Thymome
> - [ ] **4. Mise en route d'un traitement**
> 	- [ ] Pyridostigmine
> 	- [ ] Corticothérapie
> 	- [ ] Échanges plasmatiques
> - [ ] **5. Suite de prise en charge - propose**
> 	- [ ] Hospitalisation
> 	- [ ] Contrôle et monitoring de l'atteinte respiratoire
