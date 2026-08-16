---
aliases:
  - "Mémento Hémoptysie"
type: memento-ecos-ssp
ssp: "Hémoptysie"
specialite: "Pneumologie"
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

# Hémoptysie

*Pneumologie · 1 grille · 1 diagnostic documenté* — [[SSP — Hémoptysie]]

> [!abstract] La seule grille de cette SSP
> - **German-52** — Forte suspicion de cancer broncho-pulmonaire `corrige` · [grille](<file:///Users/damienfulliquet/Developer/GitHub/grilles-ecos/cases/german/German-52_-_He_moptysie_-_Grille_ECOS.html>)

> [!note] 📋 Anamnèse
> - [ ] **1. Présentation avec nom, fonction et objectif**
> - [ ] **2. Motif de consultation principal**
> - [ ] **3. Caractéristiques de l'hémoptysie**
> 	- [ ] Début et évolution
> 	- [ ] Quantité de sang
> 	- [ ] Aspect
> 	- [ ] Fréquence des épisodes
> 	- [ ] Facteurs déclenchants
> - [ ] **4. Symptômes respiratoires associés**
> 	- [ ] Toux
> 	- [ ] Dyspnée
> 	- [ ] Douleurs thoraciques
> 	- [ ] Sifflements respiratoires
> 	- [ ] Expectorations
> - [ ] **5. Symptômes généraux**
> 	- [ ] Fièvre/frissons
> 	- [ ] Sueurs nocturnes
> 	- [ ] Perte de poids
> 	- [ ] Asthénie
> 	- [ ] Anorexie
> - [ ] **6. Antécédents médicaux**
> 	- [ ] BPCO connue
> 	- [ ] Hypertension artérielle
> 	- [ ] Tuberculose antérieure
> 	- [ ] Cancers antérieurs
> 	- [ ] Maladies cardiaques
> - [ ] **7. Habitudes toxiques**
> 	- [ ] Tabagisme
> 	- [ ] Sevrage tabagique
> 	- [ ] Alcool
> 	- [ ] Autres substances
> - [ ] **8. Médicaments actuels**
> 	- [ ] Bronchodilatateurs
> 	- [ ] Antihypertenseurs
> 	- [ ] Anticoagulants/antiagrégants
> 	- [ ] Autres traitements
> - [ ] **9. Exposition et voyages**
> 	- [ ] Exposition professionnelle
> 	- [ ] Voyages récents
> 	- [ ] Contact tuberculeux
> 	- [ ] Animaux domestiques
> - [ ] **10. Antécédents familiaux**
> 	- [ ] Cancer pulmonaire familial
> 	- [ ] Tuberculose familiale
> 	- [ ] Autres cancers
> - [ ] **11. Anamnèse sociale**

> [!tip] 🩺 Status
> - [ ] **1. État général et signes vitaux**
> 	- [ ] État général altéré
> 	- [ ] Coloration cutanéo-muqueuse (pâleur, cyanose)
> 	- [ ] Signes de détresse respiratoire
> 	- [ ] Hippocratisme digital
> - [ ] **2. Examen pulmonaire complet**
> 	- [ ] Inspection du thorax (symétrie, ampliation)
> 	- [ ] Palpation (vibrations vocales)
> 	- [ ] Percussion (matité)
> 	- [ ] Auscultation (murmure vésiculaire, bruits surajoutés)
> - [ ] **3. Examen cardiovasculaire**
> 	- [ ] Auscultation cardiaque
> 	- [ ] Recherche de signes d'insuffisance cardiaque droite
> 	- [ ] Œdèmes des membres inférieurs
> 	- [ ] Pouls périphériques
> - [ ] **4. Examen ORL**
> 	- [ ] Inspection de la cavité buccale
> 	- [ ] Examen du pharynx
> 	- [ ] Recherche d'épistaxis
> 	- [ ] Examen des sinus
> - [ ] **5. Palpation ganglionnaire systématique**
> 	- [ ] Ganglions cervicaux
> 	- [ ] Ganglions sus-claviculaires (Troisier)
> 	- [ ] Ganglions axillaires
> 	- [ ] Ganglions inguinaux
> - [ ] **6. Recherche de signes de gravité**
> 	- [ ] Instabilité hémodynamique
> 	- [ ] Détresse respiratoire aiguë
> 	- [ ] Signes de choc

> [!success] 💊 Management — si Forte suspicion de cancer broncho-pulmonaire
> - [ ] **1. Diagnostics à évoquer en priorité**
> 	- [ ] Cancer broncho-pulmonaire (forte suspicion)
> 	- [ ] Exacerbation de BPCO avec surinfection
> 	- [ ] Tuberculose pulmonaire
> 	- [ ] Embolie pulmonaire
> - [ ] **2. Autres diagnostics différentiels**
> 	- [ ] Bronchiectasies
> 	- [ ] Pneumonie bactérienne
> 	- [ ] Aspergillose
> 	- [ ] Syndrome de Goodpasture
> 	- [ ] Vascularite (Wegener)
> - [ ] **3. Examens biologiques urgents**
> 	- [ ] FSC, plaquettes
> 	- [ ] Coagulation (TP, TCA)
> 	- [ ] Gazométrie artérielle
> 	- [ ] CRP, VS
> 	- [ ] Ionogramme, créatinine
> - [ ] **4. Examens d'imagerie**
> 	- [ ] Radiographie thoracique face + profil
> 	- [ ] CT thoracique avec contraste
> 	- [ ] Angio-CT si suspicion d'EP
> - [ ] **5. Examens microbiologiques**
> 	- [ ] Examen direct et culture des expectorations
> 	- [ ] Recherche de BK (3 échantillons)
> 	- [ ] Recherche de cellules malignes
> 	- [ ] Hémocultures si fièvre
> - [ ] **6. Explorations spécialisées**
> 	- [ ] Bronchoscopie avec LBA
> 	- [ ] Biopsies bronchiques
> 	- [ ] Consultation pneumologique urgente
> - [ ] **7. Prise en charge thérapeutique immédiate**
> - [ ] **8. Critères d'hospitalisation**
> 	- [ ] Hémoptysie abondante (> 100ml/24h)
> 	- [ ] Détresse respiratoire
> 	- [ ] Instabilité hémodynamique
> 	- [ ] Forte suspicion de cancer
> 	- [ ] Contexte social défavorable
> - [ ] **9. Information et soutien au patient**
> 	- [ ] Expliquer la démarche diagnostique
> 	- [ ] Rassurer sans minimiser
> 	- [ ] Proposer un soutien psychologique
> 	- [ ] Impliquer la famille
