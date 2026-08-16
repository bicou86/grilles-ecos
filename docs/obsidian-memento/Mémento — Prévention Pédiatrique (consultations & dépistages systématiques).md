---
aliases:
  - "Mémento Prévention Pédiatrique (consultations & dépistages systématiques)"
type: memento-ecos-ssp
ssp: "Prévention Pédiatrique (consultations & dépistages systématiques)"
specialite: "Pédiatrie"
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

# Prévention Pédiatrique (consultations & dépistages systématiques)

*Pédiatrie · 1 grille · 1 diagnostic documenté* — [[SSP — Prévention Pédiatrique (consultations & dépistages systématiques)]]

> [!abstract] La seule grille de cette SSP
> - **German-3** — Difficultés alimentaires avec prise insuffisante `corrige` · [grille](<file:///Users/damienfulliquet/Developer/GitHub/grilles-ecos/cases/german/German-3_-_Allaitement_-_Pe_diatrie_-_Grille_ECOS.html>)

> [!note] 📋 Anamnèse
> - [ ] **1. Présentation avec nom, fonction et tâche**
> - [ ] **2. Motif de consultation - plaintes de la mère**
> - [ ] **3. Caractérisation du problème alimentaire**
> 	- [ ] Début des symptômes
> 	- [ ] Évolution dans le temps
> 	- [ ] Mode d'alimentation
> 	- [ ] Comportement alimentaire global
> - [ ] **4. Quantification des prises alimentaires**
> 	- [ ] Quantité par tétée
> 	- [ ] Quantité totale par jour
> 	- [ ] Nombre de tétées par jour
> 	- [ ] Durée des tétées
> - [ ] **5. Comportement de l'enfant pendant l'allaitement**
> 	- [ ] Demande spontanée de nourriture
> 	- [ ] Comportement lors de la prise
> 	- [ ] Réaction pendant/après l'allaitement
> 	- [ ] Signes de satiété précoce
> - [ ] **6. Symptômes digestifs associés**
> 	- [ ] Régurgitations/rots
> 	- [ ] Vomissements
> 	- [ ] Transit intestinal
> 	- [ ] Ballonnements ou distension abdominale
> - [ ] **7. Signes de douleur ou d'inconfort**
> 	- [ ] Pleurs inexpliqués
> 	- [ ] Signes de douleur pendant/après les tétées
> 	- [ ] Coliques du nourrisson
> 	- [ ] Irritabilité générale
> - [ ] **8. Recherche de signes généraux**
> 	- [ ] Fièvre
> 	- [ ] Signes d'infection
> 	- [ ] Fatigue excessive
> 	- [ ] Autres symptômes associés
> - [ ] **9. Évaluation de l'allaitement maternel**
> 	- [ ] Temps disponible pour allaiter
> 	- [ ] Technique d'allaitement
> 	- [ ] Production lactée
> 	- [ ] État des mamelons
> 	- [ ] Douleurs lors de l'allaitement
> - [ ] **10. Antécédents périnataux**
> 	- [ ] Terme de naissance
> 	- [ ] Poids de naissance
> 	- [ ] Taille de naissance
> 	- [ ] Périmètre crânien de naissance
> 	- [ ] Adaptation néonatale
> - [ ] **11. Croissance actuelle**
> 	- [ ] Poids actuel
> 	- [ ] Taille actuelle
> 	- [ ] Périmètre crânien actuel
> 	- [ ] Évolution des courbes de croissance
> - [ ] **12. Antécédents obstétricaux**
> 	- [ ] Déroulement de la grossesse
> 	- [ ] Complications gravidiques
> 	- [ ] Exposition à des toxiques
> 	- [ ] Médications pendant la grossesse
> - [ ] **13. Antécédents médicaux de l'enfant**
> 	- [ ] Hospitalisations antérieures
> 	- [ ] Maladies chroniques
> 	- [ ] Médications actuelles
> 	- [ ] Vaccinations
> - [ ] **14. Contexte familial et psychosocial**
> 	- [ ] Configuration familiale
> 	- [ ] Dynamique familiale
> 	- [ ] Fratrie
> 	- [ ] Soutien familial disponible
> - [ ] **15. Antécédents familiaux**
> 	- [ ] Troubles digestifs familiaux
> 	- [ ] Allergies alimentaires
> 	- [ ] Troubles de croissance
> 	- [ ] Maladies métaboliques
> - [ ] **16. Facteurs de risque psychosociaux**
> 	- [ ] Stress maternel
> 	- [ ] Anxiété parentale concernant l'alimentation
> 	- [ ] Dépression post-partum
> 	- [ ] Difficultés d'attachement

> [!tip] 🩺 Status
> - [ ] **1. État général et signes vitaux**
> 	- [ ] Aspect général
> 	- [ ] Coloration cutanée
> 	- [ ] Température
> 	- [ ] Fréquence cardiaque
> 	- [ ] Fréquence respiratoire
> - [ ] **2. Évaluation de l'hydratation**
> 	- [ ] Turgor cutané
> 	- [ ] Temps de recoloration capillaire
> 	- [ ] Muqueuses
> 	- [ ] Production d'urine
> 	- [ ] Larmes présentes
> - [ ] **3. Examen neurologique du nourrisson**
> 	- [ ] État de conscience
> 	- [ ] Tonus musculaire
> 	- [ ] Réflexe de succion
> 	- [ ] Réflexe de préhension
> 	- [ ] Fontanelles
> - [ ] **4. Examen de la cavité buccale**
> 	- [ ] Inspection de la bouche
> 	- [ ] Recherche de muguet
> 	- [ ] Frein de langue
> 	- [ ] Palais
> 	- [ ] Pharynx
> - [ ] **5. Examen ORL**
> 	- [ ] Inspection du nez
> 	- [ ] Otoscopie bilatérale
> 	- [ ] Recherche d'obstruction nasale
> - [ ] **6. Examen cardio-pulmonaire**
> 	- [ ] Auscultation cardiaque
> 	- [ ] Auscultation pulmonaire
> 	- [ ] Recherche de signes de détresse respiratoire
> - [ ] **7. Examen abdominal**
> 	- [ ] Inspection
> 	- [ ] Palpation
> 	- [ ] Recherche d'organomégalie
> 	- [ ] Bruits hydroaériques
> 	- [ ] Orifices herniaires
> - [ ] **8. Évaluation anthropométrique**
> 	- [ ] Poids actuel et percentile
> 	- [ ] Rapport poids/taille
> 	- [ ] Évolution sur les courbes
> 	- [ ] Signes de malnutrition
> - [ ] **9. Observation d'une tétée**
> 	- [ ] Position du bébé
> 	- [ ] Prise du sein
> 	- [ ] Efficacité de la succion
> 	- [ ] Comportement pendant la tétée
> 	- [ ] Signes de fatigue

> [!success] 💊 Management — si Difficultés alimentaires avec prise insuffisante
> - [ ] **1. Diagnostic principal**
> - [ ] **2. Diagnostics différentiels**
> - [ ] **3. Examens complémentaires**
> 	- [ ] FSC (recherche d'anémie)
> 	- [ ] Ionogramme, urée, créatinine
> 	- [ ] Bilan hépatique si indiqué
> 	- [ ] TSH si suspicion d'hypothyroïdie
> 	- [ ] Analyse d'urine (ECBU)
> 	- [ ] US abdominale si suspicion de pathologie digestive
> 	- [ ] PH-métrie si suspicion de RGO sévère
> 	- [ ] Test d'élimination-réintroduction si suspicion d'APLV
> - [ ] **4. Prise en charge immédiate**
> - [ ] **5. Plan de suivi**
> 	- [ ] Contrôle pondéral dans 1 semaine
> 	- [ ] Réévaluation de l'efficacité de l'allaitement
> 	- [ ] Suivi des courbes de croissance
> 	- [ ] Ajustement du plan selon l'évolution
> 	- [ ] Orientation vers consultant en lactation si pas d'amélioration
> - [ ] **6. Éducation et conseils aux parents**
> 	- [ ] Signes de bonne prise alimentaire
> 	- [ ] Signes d'alarme nécessitant une consultation
> 	- [ ] Importance de la surveillance pondérale
> 	- [ ] Normalité des variations individuelles
> 	- [ ] Ressources disponibles (consultante en lactation, groupes de soutien)
> - [ ] **7. Critères d'hospitalisation**
> - [ ] **8. Alternatives si échec de l'allaitement**
> 	- [ ] Compléments au lait maternel tiré
> 	- [ ] Utilisation du DAL (dispositif d'aide à la lactation)
> 	- [ ] Introduction progressive de préparation pour nourrissons
> 	- [ ] Maintien de l'allaitement mixte si souhaité
