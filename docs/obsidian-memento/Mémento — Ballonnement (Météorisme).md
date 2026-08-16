---
aliases:
  - "Mémento Ballonnement (Météorisme)"
type: memento-ecos-ssp
ssp: "Ballonnement (Météorisme)"
specialite: "Gastro-Hépatologie"
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

# Ballonnement (Météorisme)

*Gastro-Hépatologie · 1 grille · 1 diagnostic documenté* — [[SSP — Ballonnement (Météorisme)]]

> [!abstract] La seule grille de cette SSP
> - **German-49** — Hernie inguinale droite non réductible `corrige` · [grille](<file:///Users/damienfulliquet/Developer/GitHub/grilles-ecos/cases/german/German-49_-_Gonflement_abdominal_-_Grille_ECOS.html>)

> [!note] 📋 Anamnèse
> - [ ] **1. Présentation avec nom et fonction**
> - [ ] **2. Début par question ouverte**
> - [ ] **3. Localisation précise du gonflement**
> - [ ] **4. Caractéristiques temporelles**
> 	- [ ] Début
> 	- [ ] Évolution
> 	- [ ] Variations journalières
> - [ ] **5. Symptômes douloureux**
> - [ ] **6. Description détaillée du gonflement**
> 	- [ ] Couleur
> 	- [ ] Forme
> 	- [ ] Consistance
> 	- [ ] Mobilité
> 	- [ ] Fluctuation
> - [ ] **7. Latéralité**
> - [ ] **8. Gêne fonctionnelle**
> - [ ] **9. Réductibilité du gonflement**
> - [ ] **10. Facteurs d'amélioration/aggravation**
> 	- [ ] Position debout
> 	- [ ] Position couchée
> 	- [ ] Efforts de poussée
> 	- [ ] Toux/éternuement
> - [ ] **11. Antécédents de hernie**
> - [ ] **12. Symptômes digestifs - Transit**
> 	- [ ] Constipation
> 	- [ ] Consistance des selles
> 	- [ ] Couleur/odeur
> 	- [ ] Sang dans les selles
> - [ ] **13. Symptômes digestifs - Autres**
> 	- [ ] Sensation de plénitude
> 	- [ ] Ballonnements
> 	- [ ] Émission de gaz
> 	- [ ] Nausées/vomissements
> - [ ] **14. Signes généraux**
> 	- [ ] Fièvre
> 	- [ ] Perte de poids
> 	- [ ] Sueurs nocturnes
> 	- [ ] Fatigue
> - [ ] **15. Signes inflammatoires locaux**
> 	- [ ] Jambe rouge
> 	- [ ] Plaie à la jambe
> 	- [ ] Œdème des membres inférieurs
> - [ ] **16. Antécédents médicaux**
> 	- [ ] Cardiovasculaires
> 	- [ ] Métaboliques
> 	- [ ] Diabète
> 	- [ ] Hypertension
> - [ ] **17. Antécédents chirurgicaux**
> 	- [ ] Autres chirurgies abdominales
> 	- [ ] Complications post-opératoires
> - [ ] **18. Médicaments actuels**
> 	- [ ] Observance
> - [ ] **19. Allergies**
> 	- [ ] Médicamenteuses
> 	- [ ] Alimentaires
> - [ ] **20. Habitudes de vie**
> 	- [ ] Alcool
> 	- [ ] Tabac
> 	- [ ] Drogues
> - [ ] **21. Revue des systèmes - Neurologique**
> 	- [ ] Céphalées
> 	- [ ] Vertiges
> 	- [ ] Troubles visuels
> 	- [ ] Troubles auditifs
> - [ ] **22. Revue des systèmes - Cardio-respiratoire**
> 	- [ ] Dyspnée
> 	- [ ] Toux
> 	- [ ] Douleurs thoraciques
> 	- [ ] Palpitations
> - [ ] **23. Revue des systèmes - Urogénital**
> 	- [ ] Jet urinaire
> 	- [ ] Pollakiurie
> 	- [ ] Nycturie
> 	- [ ] Brûlures mictionnelles
> - [ ] **24. Revue des systèmes - Locomoteur**
> 	- [ ] Douleurs articulaires
> 	- [ ] Raideurs
> 	- [ ] Gonflements articulaires
> - [ ] **25. État général et mode de vie**
> 	- [ ] État général
> 	- [ ] Appétit
> 	- [ ] Sommeil
> - [ ] **26. Activité physique**
> - [ ] **27. Habitudes alimentaires**
> - [ ] **28. Anamnèse sociale et professionnelle**
> 	- [ ] Profession
> 	- [ ] Port de charges lourdes
> 	- [ ] Situation familiale
> 	- [ ] Enfants
> - [ ] **29. Anamnèse sexuelle**
> - [ ] **30. Antécédents familiaux**
> 	- [ ] Cancers
> 	- [ ] Lymphomes/leucémies
> - [ ] **31. Inquiétudes du patient**
> - [ ] **32. Résumé et questions du patient**
> 	- [ ] Résumé des points principaux
> 	- [ ] Vérification de la compréhension

> [!tip] 🩺 Status
> - [ ] **1. Inspection des mains**
> 	- [ ] Signes hépatiques (érythème palmaire, Dupuytren)
> 	- [ ] Hippocratisme digital
> 	- [ ] Astérixis
> - [ ] **2. Examen abdominal - Patient debout**
> 	- [ ] Inspection générale de l'abdomen
> 	- [ ] Asymétrie visible
> 	- [ ] Masse évidente
> - [ ] **3. Manœuvres spécifiques debout**
> 	- [ ] Faire tousser le patient
> 	- [ ] Observation de l'augmentation du gonflement
> 	- [ ] Manœuvre de Valsalva
> - [ ] **4. Auscultation abdominale**
> 	- [ ] Auscultation sur le gonflement
> 	- [ ] Recherche de souffle vasculaire
> - [ ] **5. Palpation abdominale générale**
> 	- [ ] Palpation des 9 quadrants
> 	- [ ] Recherche d'hépatomégalie
> 	- [ ] Recherche de splénomégalie
> 	- [ ] Masses abdominales
> - [ ] **6. Palpation inguinale spécifique**
> 	- [ ] Palpation bilatérale des régions inguinales
> 	- [ ] Recherche d'impulsion à la toux
> - [ ] **7. Examen spécifique des orifices herniaires**
> 	- [ ] Orifice inguinal externe
> 	- [ ] Orifice inguinal interne
> 	- [ ] Canal inguinal
> 	- [ ] Distinction hernie directe/indirecte
> - [ ] **8. Examen du scrotum**
> 	- [ ] Inspection du scrotum
> 	- [ ] Palpation testiculaire bilatérale
> 	- [ ] Transillumination si indiquée
> - [ ] **9. Mesure de la tension artérielle**
> - [ ] **10. Toucher rectal si indiqué**
> 	- [ ] Tonus sphinctérien
> 	- [ ] Prostate
> 	- [ ] Masses rectales

> [!success] 💊 Management — si Hernie inguinale droite non réductible
> - [ ] **1. Diagnostic principal communiqué au patient**
> - [ ] **2. Diagnostics différentiels**
> 	- [ ] Hernie inguinale
> 	- [ ] Adénopathie inguinale
> 	- [ ] Lipome
> 	- [ ] Tumeur des tissus mous
> 	- [ ] Hydrocèle
> 	- [ ] Varicocèle
> - [ ] **3. Examens complémentaires proposés**
> 	- [ ] Échographie inguinale pour confirmation
> 	- [ ] Bilan préopératoire si chirurgie envisagée
> - [ ] **4. Options thérapeutiques expliquées**
> 	- [ ] Traitement chirurgical recommandé
> 	- [ ] Techniques : laparoscopique vs ouverte
> 	- [ ] Avantages et inconvénients de chaque technique
> 	- [ ] Délai recommandé
> - [ ] **5. Complications possibles**
> 	- [ ] Risque d'incarcération
> 	- [ ] Risque d'étranglement
> 	- [ ] Complications post-opératoires
> 	- [ ] Récidive possible
> - [ ] **6. Prise en charge des facteurs de risque**
> 	- [ ] Perte de poids recommandée
> 	- [ ] Éviter les efforts de soulèvement
> 	- [ ] Traitement de la constipation
> 	- [ ] Réduction de la consommation d'alcool
> - [ ] **7. Aborder la problématique alcoolique**
> 	- [ ] Évaluation de la consommation
> 	- [ ] Impact sur la santé
> 	- [ ] Proposition d'aide si nécessaire
> - [ ] **8. Référence au chirurgien**
> 	- [ ] Organisation de la consultation chirurgicale
> 	- [ ] Transmission des informations pertinentes
> 	- [ ] Délai de prise en charge
> - [ ] **9. Rassurer le patient**
> 	- [ ] Ce n'est pas une tumeur
> 	- [ ] Pathologie bénigne et fréquente
> 	- [ ] Excellent pronostic après traitement
> - [ ] **10. Plan de suivi**
> 	- [ ] Consultation de contrôle après échographie
> 	- [ ] Suivi post-opératoire
> 	- [ ] Surveillance des facteurs de risque
