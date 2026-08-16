---
aliases:
  - "Mémento Pollakiurie"
type: memento-ecos-ssp
ssp: "Pollakiurie"
specialite: "Néphro-Urologie"
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

# Pollakiurie

*Néphro-Urologie · 1 grille · 1 diagnostic documenté* — [[SSP — Pollakiurie]]

> [!abstract] La seule grille de cette SSP
> - **German-71** — Diabète de type 2 `corrige` · [grille](<file:///Users/damienfulliquet/Developer/GitHub/grilles-ecos/cases/german/German-71_-_Pollakiurie_-_Grille_ECOS.html>)

> [!note] 📋 Anamnèse
> - [ ] **1. Présentation du médecin**
> 	- [ ] Se présenter avec nom, fonction et tâche
> - [ ] **2. Problème actuel**
> 	- [ ] Identifier le motif de consultation
> - [ ] **3. Caractérisation des symptômes urinaires**
> 	- [ ] Urgence mictionnelle
> 	- [ ] Dysurie
> 	- [ ] Couleur de l'urine
> 	- [ ] Début précis des symptômes
> - [ ] **4. Polydipsie et appétit**
> 	- [ ] Habitudes de boisson
> 	- [ ] Appétit
> - [ ] **5. Évolution du poids**
> - [ ] **6. Autres symptômes urogénitaux**
> 	- [ ] Incontinence
> 	- [ ] Troubles de l'érection
> - [ ] **7. Symptômes généraux**
> 	- [ ] Vertiges
> 	- [ ] Douleurs
> 	- [ ] Douleur thoracique/angine de poitrine
> - [ ] **8. Symptômes neurologiques**
> 	- [ ] Troubles sensitifs
> 	- [ ] Engourdissement des mains ou des pieds
> - [ ] **9. Antécédents médicaux personnels**
> 	- [ ] Maladies antérieures
> 	- [ ] Hospitalisations
> 	- [ ] Chirurgies
> - [ ] **10. Mode de vie et habitudes**
> 	- [ ] Habitudes alimentaires
> 	- [ ] Activités sportives
> 	- [ ] Loisirs
> - [ ] **11. Substances et médicaments**
> 	- [ ] Tabac
> 	- [ ] Alcool
> 	- [ ] Drogues
> 	- [ ] Médicaments actuels
> - [ ] **12. Anamnèse familiale**
> 	- [ ] Diabète sucré
> 	- [ ] Maladies cardiovasculaires
> 	- [ ] Autres maladies héréditaires
> - [ ] **13. Anamnèse sociale**
> 	- [ ] Situation professionnelle
> 	- [ ] Situation familiale

> [!tip] 🩺 Status
> - [ ] **1. Examen cardiovasculaire**
> 	- [ ] Auscultation cardiaque
> 	- [ ] Recherche de souffles
> 	- [ ] Rythme et fréquence
> - [ ] **2. Examen pulmonaire**
> 	- [ ] Auscultation pulmonaire
> 	- [ ] Recherche de râles
> 	- [ ] Symétrie auscultatoire
> - [ ] **3. Examen ophtalmologique**
> 	- [ ] Fond d'œil
> 	- [ ] Recherche de rétinopathie diabétique
> - [ ] **4. Examen vasculaire périphérique**
> 	- [ ] Palpation des pouls périphériques
> 	- [ ] Recherche de signes d'artériopathie
> - [ ] **5. Examen neurologique**
> 	- [ ] Test de la sensibilité
> 	- [ ] Sens vibratoire au diapason
> 	- [ ] Test au monofilament
> 	- [ ] Réflexes ostéo-tendineux
> - [ ] **6. Mesure de la tension artérielle**
> 	- [ ] Prise de tension

> [!success] 💊 Management — si Diabète de type 2
> - [ ] **1. Diagnostic principal suspecté**
> 	- [ ] Diabète sucré de type 2
> - [ ] **2. Diagnostics différentiels**
> - [ ] **3. Examens complémentaires - Biologie**
> 	- [ ] Formule sanguine complète (FSC)
> 	- [ ] Glycémie à jeun
> 	- [ ] CRP
> 	- [ ] Nouvelle glycémie à jeun le lendemain
> - [ ] **4. Examens complémentaires - Analyses urinaires**
> 	- [ ] Recherche de corps cétoniques
> 	- [ ] Recherche de glucose
> 	- [ ] Recherche de signes d'infection
> 	- [ ] Bandelette urinaire complète
> - [ ] **5. Prise en charge thérapeutique**
> 	- [ ] Changement de régime alimentaire
> 	- [ ] Contrôle du poids
> 	- [ ] Si échec : antidiabétiques oraux
> 	- [ ] Contrôle de la tension artérielle
> - [ ] **6. Gestion des complications potentielles**
> 	- [ ] Évaluer la nécessité d'un transfert hospitalier
> 	- [ ] Suspicion de coma diabétique
> 	- [ ] Organiser le transfert si nécessaire
> - [ ] **7. Suivi et accompagnement**
> 	- [ ] Rassurer le patient
> 	- [ ] Planifier des consultations régulières
> 	- [ ] Proposer un soutien continu
> 	- [ ] Éducation thérapeutique
