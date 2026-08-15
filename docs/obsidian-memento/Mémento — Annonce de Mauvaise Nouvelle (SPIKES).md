---
aliases:
  - "Mémento Annonce de Mauvaise Nouvelle (SPIKES)"
type: memento-ecos-ssp
ssp: "Annonce de Mauvaise Nouvelle (SPIKES)"
cas: 1
diagnostics: 1
attendus_sans_grille: 1
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
> Quand un item est porté par **deux diagnostics ou plus**, il n'est pas
> recopié dans chaque sous-bloc : il remonte dans un encadré
> `💊 Management — partagé par plusieurs diagnostics`, en tête, où son suffixe
> **nomme les diagnostics concernés** — `*(Angor · STEMI — 3 grilles sur 12)*`
> se lit « au moins une grille d'Angor et une de STEMI le portent, 3 des
> 12 grilles de la SSP au total ». ⚠️ **Cet encadré se lit *avec* le sous-bloc
> de votre diagnostic, pas à sa place.** Il est absent quand aucun item n'est
> partagé, ce qui arrive souvent : le rapprochement entre grilles reste
> purement lexical, et deux grilles qui prescrivent la même chose autrement ne
> se rejoignent pas.
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

# Annonce de Mauvaise Nouvelle (SPIKES)

*1 grille · 1 diagnostic documenté · 1 attendu sans grille* — [[SSP — Annonce de Mauvaise Nouvelle (SPIKES)]]

> [!abstract] La seule grille de cette SSP
> - **RESCOS-8** — Récidive de cancer ovarien `confirme` · [grille](<file:///Users/damienfulliquet/Developer/GitHub/grilles-ecos/cases/rescos/RESCOS-8_-_BBN_-_Re_cidive_cancer_ovarien_-_Grille_ECOS.html>)

> [!note] 📋 Anamnèse
> - [ ] **1. S - Setting up : Préparer le terrain**
> 	- [ ] Choisir un lieu approprié
> 	- [ ] S'assurer d'avoir suffisamment de temps
> 	- [ ] Éteindre téléphone/biper si possible
> 	- [ ] S'asseoir au même niveau que la patiente
> 	- [ ] Demander si elle souhaite être accompagnée
> - [ ] **2. P - Patient perceptions : Représentations de la patiente**
> 	- [ ] Que comprenez-vous de votre situation actuelle?
> 	- [ ] Qu'est-ce qu'on vous a déjà expliqué?
> 	- [ ] Comment interprétez-vous vos symptômes?
> 	- [ ] Quelles sont vos inquiétudes principales?
> 	- [ ] Vérifier compréhension de l'objectif de la rencontre
> - [ ] **3. I - Patient invitation : Avertir la patiente**
> 	- [ ] Malheureusement, j'ai des nouvelles difficiles à vous annoncer
> 	- [ ] Les résultats du scanner montrent quelque chose de préoccupant
> 	- [ ] Souhaitez-vous que je vous explique maintenant?
> 	- [ ] Préférez-vous attendre la présence de quelqu'un?
> 	- [ ] Avertissement progressif

> [!tip] 🩺 Status
> - [ ] **1. K - Knowledge : Annoncer le diagnostic**
> 	- [ ] Le cancer est revenu
> 	- [ ] Métastases au niveau du péritoine
> 	- [ ] Cause de l'iléus
> 	- [ ] Information par segments courts
> 	- [ ] Pauses pour permettre l'assimilation
> - [ ] **2. Vérification de la compréhension**
> 	- [ ] Que comprenez-vous de ce que je viens de dire?
> 	- [ ] Avez-vous des questions sur le diagnostic?
> 	- [ ] Souhaitez-vous plus de détails?
> 	- [ ] Reformulation si nécessaire
> 	- [ ] Adaptation au niveau de compréhension
> - [ ] **3. Information sur les symptômes actuels**
> 	- [ ] Ballonnement depuis 4-6 semaines
> 	- [ ] Douleurs abdominales
> 	- [ ] Vomissements fécaloïdes
> 	- [ ] État général diminué
> 	- [ ] Lien entre symptômes et récidive
> - [ ] **4. Éviter les erreurs de communication**
> 	- [ ] Éviter le jargon médical excessif
> 	- [ ] Ne pas minimiser la gravité
> 	- [ ] Ne pas donner de faux espoirs
> 	- [ ] Éviter les euphémismes confus
> 	- [ ] Être honnête mais empathique

> [!success] 💊 Management — si Diabète inaugural / Acido-cétose
> *Aucune grille du corpus ne documente ce diagnostic* — il est pourtant attendu de cette SSP. **Trou de révision à combler ailleurs.**

> [!success] 💊 Management — si Récidive de cancer ovarien
> - [ ] **1. E - Emotions : Réagir aux émotions**
> 	- [ ] Observer les réactions
> 	- [ ] Respecter le temps et le silence
> 	- [ ] Nommer l'émotion
> 	- [ ] Valider l'émotion
> 	- [ ] Offrir du soutien
> - [ ] **2. Techniques de soutien émotionnel**
> 	- [ ] Empathie verbale
> 	- [ ] Empathie non-verbale
> 	- [ ] Toucher thérapeutique si approprié
> 	- [ ] Offrir des mouchoirs
> 	- [ ] Ne pas précipiter la suite
> - [ ] **3. S - Strategy : Plan thérapeutique immédiat**
> 	- [ ] Avis chirurgical pour lever l'obstacle
> 	- [ ] Sonde naso-gastrique pour soulagement
> 	- [ ] Anti-émétiques
> 	- [ ] Corticoïdes hautes doses
> 	- [ ] Hospitalisation nécessaire
> - [ ] **4. Options oncologiques**
> 	- [ ] Chimiothérapie palliative toutes les 3 semaines
> 	- [ ] But: améliorer qualité de vie
> 	- [ ] Réduction douleurs et ascite
> 	- [ ] Prolongation survie possible
> 	- [ ] Décision à discuter avec oncologie
> - [ ] **5. Discussion du pronostic**
> 	- [ ] Espérance de vie difficile à estimer
> 	- [ ] Médiane 12-18 mois
> 	- [ ] Incertitude inhérente au pronostic
> 	- [ ] Focus sur qualité de vie
> 	- [ ] Accompagnement palliatif disponible
> - [ ] **6. S - Summary : Résumé et prochaines étapes**
> 	- [ ] Récapituler les points principaux
> 	- [ ] Vérifier compréhension globale
> 	- [ ] Plan pour les prochaines 24-48h
> 	- [ ] Rendez-vous de suivi
> 	- [ ] Coordonnées pour questions
