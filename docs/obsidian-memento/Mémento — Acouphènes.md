---
aliases:
  - "Mémento Acouphènes"
type: memento-ecos-ssp
ssp: "Acouphènes"
specialite: "ORL"
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

# Acouphènes

*ORL · 1 grille · 1 diagnostic documenté* — [[SSP — Acouphènes]]

> [!abstract] La seule grille de cette SSP
> - **German-2** — Acouphène subjectif bilatéral `corrige` · [grille](<file:///Users/damienfulliquet/Developer/GitHub/grilles-ecos/cases/german/German-2_-_Acouphe_nes_-_Grille_ECOS.html>)

> [!note] 📋 Anamnèse
> - [ ] **1. Présentation avec nom, fonction et tâche**
> - [ ] **2. Problème actuel**
> - [ ] **3. Caractérisation des acouphènes**
> 	- [ ] Apparition temporelle
> 	- [ ] Évolution
> 	- [ ] Facteurs modulateurs
> 	- [ ] Type de son
> 	- [ ] Latéralisation
> - [ ] **4. Symptômes ORL associés**
> 	- [ ] Troubles auditifs
> 	- [ ] Sécrétions auriculaires (cérumen, sang, pus)
> 	- [ ] Otalgie
> 	- [ ] Vertiges
> 	- [ ] Sensation de plénitude auriculaire
> - [ ] **5. Symptômes généraux d'accompagnement**
> 	- [ ] Fièvre
> 	- [ ] Toux
> 	- [ ] Rhinite
> 	- [ ] Nausées/vomissements
> 	- [ ] Céphalées
> - [ ] **6. Recherche de facteurs déclenchants**
> 	- [ ] Traumatisme acoustique récent
> 	- [ ] Exposition au bruit
> 	- [ ] Situations particulières
> - [ ] **7. Antécédents ORL**
> 	- [ ] Otites à répétition
> 	- [ ] Chirurgie ORL
> 	- [ ] Surdité familiale
> - [ ] **8. Antécédents médicaux généraux**
> 	- [ ] Hypertension artérielle
> 	- [ ] Diabète
> 	- [ ] Maladies cardiovasculaires
> 	- [ ] Troubles neurologiques
> 	- [ ] Antécédents psychiatriques
> - [ ] **9. Traumatismes**
> 	- [ ] Traumatisme crânien
> 	- [ ] Barotraumatisme
> 	- [ ] Traumatisme cervical
> - [ ] **10. Anamnèse médicamenteuse**
> 	- [ ] Recherche de médicaments ototoxiques (aminosides, diurétiques de l'anse, aspirine haute dose)
> 	- [ ] Chimiothérapie
> 	- [ ] Médicaments actuels
> - [ ] **11. Anamnèse sociale et professionnelle**
> 	- [ ] Situation familiale
> 	- [ ] Profession
> 	- [ ] Exposition professionnelle au bruit
> 	- [ ] Consommation de substances (tabac, alcool, café)
> - [ ] **12. Anamnèse systémique**
> 	- [ ] Revue des systèmes cardiovasculaire
> 	- [ ] Revue du système neurologique
> 	- [ ] Recherche de signes d'alerte
> - [ ] **13. Impact sur la qualité de vie**
> 	- [ ] Troubles du sommeil
> 	- [ ] Difficultés de concentration
> 	- [ ] Retentissement professionnel
> 	- [ ] Anxiété liée aux acouphènes

> [!tip] 🩺 Status
> - [ ] **1. Inspection**
> 	- [ ] Inspection du pavillon auriculaire
> 	- [ ] Recherche de cicatrices ou malformations
> 	- [ ] Inspection du conduit auditif externe
> - [ ] **2. Palpation**
> 	- [ ] Pression du tragus
> 	- [ ] Traction du pavillon
> 	- [ ] Palpation mastoïdienne
> 	- [ ] Palpation des ganglions cervicaux
> - [ ] **3. Otoscopie bilatérale**
> 	- [ ] Aspect du tympan
> 	- [ ] Présence de cérumen
> 	- [ ] Signes inflammatoires
> 	- [ ] Perforations
> - [ ] **4. Tests auditifs au diapason**
> 	- [ ] Test de Weber
> 	- [ ] Test de Rinne bilatéral
> - [ ] **5. Examen vestibulaire et de l'équilibre**
> 	- [ ] Test de Romberg
> 	- [ ] Recherche de nystagmus
> 	- [ ] Test de marche aveugle
> 	- [ ] Épreuve des index
> - [ ] **6. Examen neurologique ciblé**
> 	- [ ] Nerfs crâniens (notamment V, VII, VIII)
> 	- [ ] Réflexes
> 	- [ ] Sensibilité faciale
> 	- [ ] Force musculaire
> - [ ] **7. Examen cardiovasculaire**
> 	- [ ] Auscultation cardiaque
> 	- [ ] Auscultation carotidienne (souffle)
> 	- [ ] Mesure de la tension artérielle
> 	- [ ] Pouls périphériques
> - [ ] **8. Examen de la cavité buccale et du pharynx**
> 	- [ ] Inspection de l'oropharynx
> 	- [ ] Palpation de l'articulation temporo-mandibulaire
> 	- [ ] Dentition

> [!success] 💊 Management — si Acouphène subjectif bilatéral
> - [ ] **1. Diagnostic principal**
> - [ ] **2. Diagnostics différentiels**
> - [ ] **3. Examens complémentaires**
> 	- [ ] Audiométrie tonale et vocale
> 	- [ ] Tympanométrie
> 	- [ ] Potentiels évoqués auditifs
> 	- [ ] Acouphénométrie
> 	- [ ] IRM cérébrale avec séquences du rocher (si suspicion de neurinome)
> 	- [ ] Bilan biologique (FSC, TSH, glycémie)
> 	- [ ] Bilan cardiovasculaire si indiqué
> - [ ] **4. Prise en charge thérapeutique**
> - [ ] **5. Information et éducation du patient**
> 	- [ ] Expliquer la nature bénigne dans la majorité des cas
> 	- [ ] Informer sur la complexité du traitement
> 	- [ ] Rassurer sur l'absence de gravité habituelle
> 	- [ ] Expliquer l'importance de la prise en charge globale
> - [ ] **6. Suivi et orientation**
> 	- [ ] Contrôle audiométrique régulier
> 	- [ ] Suivi ORL spécialisé
> 	- [ ] Orientation psychologique si retentissement important
> 	- [ ] Groupe de soutien pour patients acouphéniques
> - [ ] **7. Signes d'alerte nécessitant une prise en charge urgente**
