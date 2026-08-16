---
aliases:
  - "Mémento Syndrome Néphrotique"
type: memento-ecos-ssp
ssp: "Syndrome Néphrotique"
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

# Syndrome Néphrotique

*Néphro-Urologie · 1 grille · 1 diagnostic documenté* — [[SSP — Syndrome Néphrotique]]

> [!abstract] La seule grille de cette SSP
> - **German-50** — Syndrome néphrotique `corrige` · [grille](<file:///Users/damienfulliquet/Developer/GitHub/grilles-ecos/cases/german/German-50_-_Gonflement_du_visage_-_Grille_ECOS.html>)

> [!note] 📋 Anamnèse
> - [ ] **1. Présentation avec nom, fonction et tâche**
> - [ ] **2. Symptômes principaux**
> 	- [ ] Œdèmes palpébraux
> 	- [ ] Fatigue
> 	- [ ] Œdèmes des jambes
> - [ ] **3. Chronologie des symptômes**
> 	- [ ] Œdèmes palpébraux
> 	- [ ] Fatigue
> 	- [ ] Progression
> - [ ] **4. Premier épisode**
> - [ ] **5. Symptômes associés - Douleur**
> 	- [ ] Douleurs faciales
> 	- [ ] Douleurs abdominales
> 	- [ ] Douleurs lombaires
> - [ ] **6. Symptômes urinaires**
> 	- [ ] Problèmes mictionnels
> 	- [ ] Dysurie
> 	- [ ] Pollakiurie
> 	- [ ] Hématurie
> 	- [ ] Mousseuse
> - [ ] **7. Signes généraux**
> 	- [ ] Fièvre
> 	- [ ] Prise de poids récente
> 	- [ ] Perte d'appétit
> - [ ] **8. Antécédents récents importants**
> 	- [ ] Hospitalisation récente
> 	- [ ] Complications
> - [ ] **9. Antécédents médicaux - Oncologiques**
> 	- [ ] Cancer actuel
> 	- [ ] Antécédent de cancer
> 	- [ ] Dépistages à jour
> - [ ] **10. Antécédents médicaux - Infectieux**
> 	- [ ] Hépatite B ou C
> 	- [ ] VIH
> 	- [ ] Autres infections chroniques
> - [ ] **11. Antécédents médicaux - Auto-immuns**
> 	- [ ] Traitement actuel
> 	- [ ] Suivi
> 	- [ ] Dernière poussée
> - [ ] **12. Autres antécédents médicaux**
> 	- [ ] Diabète
> 	- [ ] Hypertension
> 	- [ ] Maladies rénales antérieures
> 	- [ ] Maladies cardiaques
> - [ ] **13. Médicaments actuels**
> 	- [ ] Posologie
> 	- [ ] Observance
> 	- [ ] INR récent
> - [ ] **14. Allergies médicamenteuses**
> - [ ] **15. Habitudes de vie**
> 	- [ ] Alcool
> 	- [ ] Tabac
> 	- [ ] Drogues
> 	- [ ] Régime alimentaire
> - [ ] **16. Antécédents familiaux**
> 	- [ ] Type de maladie rénale
> 	- [ ] Autres maladies familiales
> - [ ] **17. Anamnèse sociale**
> 	- [ ] Situation familiale
> 	- [ ] Logement
> 	- [ ] Profession
> 	- [ ] Stress/soucis actuels
> - [ ] **18. Origine et statut migratoire**
> 	- [ ] Pays d'origine
> 	- [ ] Durée en Suisse

> [!tip] 🩺 Status
> - [ ] **1. Signes vitaux**
> 	- [ ] Tension artérielle
> 	- [ ] Fréquence cardiaque
> 	- [ ] Température
> - [ ] **2. Inspection et palpation du visage**
> 	- [ ] Œdèmes palpébraux
> 	- [ ] Consistance
> 	- [ ] Couleur cutanée
> 	- [ ] Autres signes faciaux
> - [ ] **3. Examen abdominal**
> 	- [ ] Inspection
> 	- [ ] Palpation
> 	- [ ] Ascite
> 	- [ ] Hépatomégalie
> - [ ] **4. Palpation rénale**
> 	- [ ] Fosses lombaires
> 	- [ ] Reins palpables
> 	- [ ] Contact lombaire
> - [ ] **5. Auscultation cardio-pulmonaire**
> 	- [ ] Auscultation pulmonaire
> 	- [ ] Auscultation cardiaque
> 	- [ ] Signes de surcharge
> - [ ] **6. Inspection des veines jugulaires**
> 	- [ ] Turgescence jugulaire
> 	- [ ] Reflux hépato-jugulaire
> - [ ] **7. Examen des membres inférieurs**
> 	- [ ] Bilatéraux
> 	- [ ] Prenant le godet
> 	- [ ] Signes de TVP
> - [ ] **8. Examen cutané**
> 	- [ ] Éruption cutanée
> 	- [ ] Lésions de lupus
> 	- [ ] Purpura

> [!success] 💊 Management — si Syndrome néphrotique
> - [ ] **1. Diagnostic principal évoqué**
> - [ ] **2. Diagnostics différentiels**
> 	- [ ] Syndrome néphrotique
> 	- [ ] Néphrite lupique
> 	- [ ] Glomérulonéphrite post-infectieuse
> 	- [ ] Insuffisance cardiaque
> 	- [ ] Hypoprotidémie d'autre origine
> 	- [ ] Angioœdème
> 	- [ ] Hypothyroïdie
> - [ ] **3. Examens complémentaires urgents**
> 	- [ ] Bandelette urinaire
> 	- [ ] Sédiment urinaire
> 	- [ ] Rapport protéine/créatinine urinaire
> - [ ] **4. Bilan biologique complémentaire**
> 	- [ ] Fonction rénale (créatinine, urée, DFG)
> 	- [ ] Protidémie et albuminémie
> 	- [ ] Bilan lipidique
> 	- [ ] FSC, VS, CRP
> - [ ] **5. Reconnaissance du syndrome néphrotique**
> 	- [ ] Protéinurie > 3.5 g/24h
> 	- [ ] Hypoalbuminémie < 30 g/L
> 	- [ ] Œdèmes
> 	- [ ] Hyperlipidémie fréquente
> - [ ] **6. Traitement initial**
> 	- [ ] Restriction sodée
> 	- [ ] Restriction hydrique si hyponatrémie
> 	- [ ] Diurétiques de l'anse si œdèmes importants
> - [ ] **7. Surveillance de l'anticoagulation**
> 	- [ ] Vérifier l'INR (patient sous Marcoumar)
> 	- [ ] Risque thrombotique augmenté dans le syndrome néphrotique
> 	- [ ] Adapter la posologie si nécessaire
> - [ ] **8. Orientation spécialisée**
> 	- [ ] Suivi conjoint avec rhumatologue (lupus)
> - [ ] **9. Information et éducation du patient**
> 	- [ ] Explication du diagnostic suspecté
> 	- [ ] Importance du suivi néphrologique
> 	- [ ] Surveillance du poids et des œdèmes
> 	- [ ] Signes d'alerte à surveiller
> - [ ] **10. Plan de suivi**
> 	- [ ] Consultation néphrologie dans les 24-48h
> 	- [ ] Contrôle biologique rapproché
> 	- [ ] Surveillance de la fonction rénale
> 	- [ ] Ajustement thérapeutique selon résultats
