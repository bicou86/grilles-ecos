---
aliases:
  - "Mémento Claudication Intermittente & AOMI"
type: memento-ecos-ssp
ssp: "Claudication Intermittente & AOMI"
specialite: "Cardiologie & Vasculaire"
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

# Claudication Intermittente & AOMI ⭐️

*Cardiologie & Vasculaire · 1 grille · 1 diagnostic documenté* — [[SSP — Claudication Intermittente & AOMI]]

> [!abstract] La seule grille de cette SSP
> - **German-26** — Occlusion artérielle aiguë du membre inférieur droit `corrige` · [grille](<file:///Users/damienfulliquet/Developer/GitHub/grilles-ecos/cases/german/German-26_-_Douleur_aux_jambes_-_Grille_ECOS.html>)

> [!note] 📋 Anamnèse
> - [ ] **1. Présentation avec nom, fonction et tâche**
> - [ ] **2. Symptômes principaux**
> - [ ] **3. Début des symptômes**
> - [ ] **4. Facteur déclenchant**
> - [ ] **5. Localisation précise**
> - [ ] **6. Intensité de la douleur (échelle 0-10)**
> - [ ] **7. Irradiation**
> - [ ] **8. Début et évolution**
> - [ ] **9. Caractère de la douleur**
> - [ ] **10. Limitation fonctionnelle**
> - [ ] **11. Premier épisode**
> - [ ] **12. Facteurs influençant la douleur**
> - [ ] **13. Activité physique habituelle**
> - [ ] **14. Claudication intermittente**
> - [ ] **15. Angor d'effort**
> - [ ] **16. Traumatisme récent**
> - [ ] **17. Fièvre ou infection**
> - [ ] **18. Facteurs de risque cardiovasculaire**
> 	- [ ] Hypertension artérielle
> 	- [ ] Diabète
> 	- [ ] Dyslipidémie
> 	- [ ] Tabagisme
> 	- [ ] Antécédents familiaux positifs
> - [ ] **19. Signes de thrombose veineuse profonde**
> - [ ] **20. Facteurs de risque de TVP**
> 	- [ ] Immobilisation prolongée
> 	- [ ] Chirurgie récente
> 	- [ ] Antécédent de TVP/EP
> 	- [ ] Thrombophilie familiale
> 	- [ ] Cancer actif
> - [ ] **21. Antécédents personnels**
> - [ ] **22. Allergies**
> - [ ] **23. Médicaments actuels**
> - [ ] **24. Habitudes et toxiques**
> - [ ] **25. Anamnèse familiale**
> - [ ] **26. Anamnèse sociale**

> [!tip] 🩺 Status
> - [ ] **1. Inspection des membres inférieurs**
> - [ ] **2. Évaluation de la sensibilité**
> - [ ] **3. Recherche de signes de TVP**
> - [ ] **4. Palpation des pouls artériels**
> 	- [ ] Pouls fémoral droit
> 	- [ ] Pouls poplité droit
> 	- [ ] Pouls tibial postérieur droit
> 	- [ ] Pouls pédieux droit
> 	- [ ] Comparaison avec le côté controlatéral
> - [ ] **5. Examen cardiovasculaire**
> - [ ] **6. Examen pulmonaire**
> - [ ] **7. Température cutanée**
> 	- [ ] Membre inférieur droit froid
> 	- [ ] Comparaison avec le côté gauche
> - [ ] **8. Examen neurologique**
> 	- [ ] Force musculaire
> 	- [ ] Réflexes ostéo-tendineux
> 	- [ ] Sensibilité profonde
> - [ ] **9. Signes des 6 P de l'ischémie aiguë**
> 	- [ ] Pain (douleur)
> 	- [ ] Pallor (pâleur)
> 	- [ ] Pulselessness (absence de pouls)
> 	- [ ] Paresthésies
> 	- [ ] Paralysis (paralysie)
> 	- [ ] Poikilothermia (membre froid)

> [!success] 💊 Management — si Occlusion artérielle aiguë du membre inférieur droit
> - [ ] **1. Diagnostic principal**
> - [ ] **2. Diagnostics différentiels (au moins 2)**
> - [ ] **3. Examens complémentaires urgents**
> 	- [ ] Échographie Doppler artérielle
> 	- [ ] ECG (recherche de fibrillation auriculaire)
> 	- [ ] Angioscanner des membres inférieurs si disponible
> 	- [ ] Bilan biologique: FSC, CRP, créatinine, CPK, lactates
> 	- [ ] Bilan de coagulation: TP, TCA, INR
> 	- [ ] D-dimères
> - [ ] **4. Prise en charge immédiate**
> 	- [ ] Héparine non fractionnée IV (bolus puis perfusion continue)
> 	- [ ] Analgésie adaptée (morphine si nécessaire)
> 	- [ ] Position déclive du membre
> 	- [ ] Protection thermique du membre
> 	- [ ] Voie veineuse périphérique
> 	- [ ] Monitoring cardiaque continu
> - [ ] **5. Orientation et traitement définitif**
> 	- [ ] Transfert urgent au laboratoire de cathétérisme
> 	- [ ] Embolectomie chirurgicale (technique de Fogarty)
> 	- [ ] Thrombolyse intra-artérielle dirigée
> 	- [ ] Angioplastie percutanée
> 	- [ ] Évaluation par chirurgien vasculaire
> - [ ] **6. Ajustement thérapeutique à long terme**
> 	- [ ] Introduction d'aspirine
> 	- [ ] Clopidogrel selon indication
> 	- [ ] Anticoagulation orale (AOD ou AVK)
> 	- [ ] Optimisation du traitement cardiovasculaire
> 	- [ ] Statine à haute dose
> - [ ] **7. Surveillance et complications**
> 	- [ ] Fenêtre thérapeutique de 6 heures
> 	- [ ] Surveillance horaire des pouls et de la sensibilité
> 	- [ ] Risque de syndrome de reperfusion
> 	- [ ] Risque de rhabdomyolyse
> 	- [ ] Surveillance de la fonction rénale
> 	- [ ] Risque d'amputation si retard thérapeutique
> - [ ] **8. Information du patient et pronostic**
> 	- [ ] Explication de l'urgence de la situation
> 	- [ ] Information sur les procédures à venir
> 	- [ ] Consentement éclairé pour intervention
> 	- [ ] Pronostic dépendant du délai de revascularisation
> - [ ] **9. Prévention secondaire**
> 	- [ ] Recherche étiologique (source embolique)
> 	- [ ] Échocardiographie transthoracique/transoesophagienne
> 	- [ ] Holter ECG si suspicion de FA paroxystique
> 	- [ ] Contrôle strict des facteurs de risque cardiovasculaire
> 	- [ ] Sevrage tabagique impératif
