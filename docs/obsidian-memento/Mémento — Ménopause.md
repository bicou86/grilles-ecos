---
aliases:
  - "Mémento Ménopause"
type: memento-ecos-ssp
ssp: "Ménopause"
specialite: "Gynéco-Obstétrique"
cas: 2
diagnostics: 2
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

# Ménopause

*Gynéco-Obstétrique · 2 grilles · 2 diagnostics documentés* — [[SSP — Ménopause]]

> [!abstract] Les 2 grilles fusionnées
> - **German-6** — Phéochromocytome `premier-dd` · [grille](<file:///Users/damienfulliquet/Developer/GitHub/grilles-ecos/cases/german/German-6_-_Bouffe_es_de_chaleur_-_Grille_ECOS.html>)
> - **German-63** — Ménopause physiologique confirmée `corrige` · [grille](<file:///Users/damienfulliquet/Developer/GitHub/grilles-ecos/cases/german/German-63_-_Me_nopause_-_Grille_ECOS.html>)

> [!note] 📋 Anamnèse
> - [ ] **1. Présentation avec nom, fonction et tâche**
> - [ ] **2. Caractéristiques temporelles des symptômes *(Phéochromocytome)***
> 	- [ ] Depuis quand
> 	- [ ] Fréquence
> 	- [ ] Durée des épisodes
> - [ ] **3. Facteurs déclenchants *(Phéochromocytome)***
> 	- [ ] Stress/excitation
> 	- [ ] Alcool
> 	- [ ] Aliments épicés
> 	- [ ] Chaleur ambiante
> - [ ] **4. Modifications cutanées lors des épisodes *(Phéochromocytome)***
> 	- [ ] Coloration
> 	- [ ] Reste du corps
> 	- [ ] Extrémités
> 	- [ ] Prurit/démangeaisons
> - [ ] **5. Symptômes végétatifs *(Phéochromocytome)***
> 	- [ ] Transpiration
> 	- [ ] Bouffées de chaleur
> 	- [ ] Frissons
> - [ ] **6. Symptômes généraux *(Phéochromocytome)***
> 	- [ ] Faiblesse physique
> 	- [ ] Fatigue
> 	- [ ] Malaise
> - [ ] **7. Symptômes neuropsychiatriques *(Phéochromocytome)***
> 	- [ ] Agitation interne
> 	- [ ] Tremblements
> 	- [ ] Troubles du sommeil
> 	- [ ] Irritabilité
> - [ ] **8. Symptômes gastro-intestinaux *(Phéochromocytome)***
> 	- [ ] Diarrhée
> 	- [ ] Constipation
> 	- [ ] Nausées
> 	- [ ] Vomissements
> 	- [ ] Crampes abdominales
> - [ ] **9. Symptômes respiratoires *(Phéochromocytome)***
> 	- [ ] Dyspnée
> 	- [ ] Toux
> 	- [ ] Wheezing
> - [ ] **10. Symptômes cardiovasculaires *(Phéochromocytome)***
> 	- [ ] Palpitations
> 	- [ ] Douleurs thoraciques
> 	- [ ] Œdèmes
> - [ ] **11. Symptômes neurologiques *(Phéochromocytome)***
> 	- [ ] Céphalées
> 	- [ ] Vertiges
> 	- [ ] Paresthésies
> - [ ] **12. Symptômes B *(Phéochromocytome)***
> 	- [ ] Perte de poids
> 	- [ ] Sueurs nocturnes
> 	- [ ] Fièvre
> - [ ] **13. Symptômes urogénitaux *(Phéochromocytome)***
> 	- [ ] Nycturie
> 	- [ ] Polyurie
> 	- [ ] Troubles mictionnels
> - [ ] **14. Symptômes thyroïdiens *(Phéochromocytome)***
> 	- [ ] Intolérance à la chaleur
> 	- [ ] Modifications oculaires
> 	- [ ] Tremblements fins
> 	- [ ] Goitre
> - [ ] **15. Statut gynécologique *(Phéochromocytome)***
> 	- [ ] Statut menstruel
> 	- [ ] Âge
> 	- [ ] Contraception
> - [ ] **16. Antécédents médicaux personnels**
> 	- [ ] Maladies cardiovasculaires *(Phéochromocytome)*
> 	- [ ] Maladies thyroïdiennes *(Phéochromocytome)*
> 	- [ ] Maladies rénales *(Phéochromocytome)*
> 	- [ ] Diabète *(Phéochromocytome)*
> 	- [ ] Cancer *(Phéochromocytome)*
> 	- [ ] Interventions chirurgicales
> 	- [ ] Pathologies chroniques *(Ménopause physiologique confirmée)*
> 	- [ ] Traitements actuels *(Ménopause physiologique confirmée)*
> - [ ] **17. Médicaments actuels *(Phéochromocytome)***
> - [ ] **18. Allergies *(Phéochromocytome)***
> - [ ] **19. Habitudes de vie**
> 	- [ ] Alcool
> 	- [ ] Tabac
> 	- [ ] Drogues
> 	- [ ] Activité physique
> 	- [ ] Alimentation *(Ménopause physiologique confirmée)*
> - [ ] **20. Antécédents familiaux**
> 	- [ ] Autres cancers familiaux *(Phéochromocytome)*
> 	- [ ] Maladies cardiovasculaires
> 	- [ ] Maladies endocriniennes *(Phéochromocytome)*
> 	- [ ] Cancers familiaux *(Ménopause physiologique confirmée)*
> 	- [ ] Ostéoporose familiale *(Ménopause physiologique confirmée)*
> - [ ] **21. Anamnèse sociale**
> 	- [ ] Profession *(Phéochromocytome)*
> 	- [ ] Situation familiale *(Phéochromocytome)*
> 	- [ ] Stress psychosocial *(Phéochromocytome)*
> - [ ] **22. Motif de consultation *(Ménopause physiologique confirmée)***
> - [ ] **23. Anamnèse menstruelle *(Ménopause physiologique confirmée)***
> 	- [ ] Date des dernières règles
> 	- [ ] Régularité antérieure
> 	- [ ] Autres saignements vaginaux
> - [ ] **24. Symptômes vasomoteurs *(Ménopause physiologique confirmée)***
> 	- [ ] Bouffées de chaleur
> 	- [ ] Sueurs
> 	- [ ] Fréquence et moment
> 	- [ ] Durée
> - [ ] **25. Palpitations *(Ménopause physiologique confirmée)***
> - [ ] **26. Symptômes uro-génitaux *(Ménopause physiologique confirmée)***
> 	- [ ] Sécheresse vaginale
> 	- [ ] Dyspareunie
> 	- [ ] Troubles mictionnels
> 	- [ ] Incontinence urinaire
> - [ ] **27. Sexualité *(Ménopause physiologique confirmée)***
> 	- [ ] Libido
> 	- [ ] Qualité des rapports
> - [ ] **28. Symptômes psychologiques *(Ménopause physiologique confirmée)***
> 	- [ ] Humeur
> 	- [ ] Tension intérieure
> 	- [ ] Agressivité
> 	- [ ] Anxiété
> - [ ] **29. Fonction cognitive *(Ménopause physiologique confirmée)***
> 	- [ ] Concentration
> 	- [ ] Mémoire
> 	- [ ] Performance générale
> - [ ] **30. Troubles du sommeil *(Ménopause physiologique confirmée)***
> - [ ] **31. Symptômes ostéo-articulaires *(Ménopause physiologique confirmée)***
> 	- [ ] Douleurs articulaires
> 	- [ ] Antécédents de fractures
> - [ ] **32. Anamnèse gynéco-obstétricale *(Ménopause physiologique confirmée)***
> 	- [ ] Parité
> 	- [ ] Ménarche
> 	- [ ] Cycles antérieurs
> 	- [ ] Contraception
> - [ ] **33. Revue des systèmes *(Ménopause physiologique confirmée)***
> 	- [ ] Symptômes B (fièvre, perte de poids, sueurs nocturnes)
> 	- [ ] Autres symptômes
> - [ ] **34. Questions de clôture *(Ménopause physiologique confirmée)***
> 	- [ ] Avez-vous quelque chose à ajouter ?
> 	- [ ] Avez-vous des questions ?

> [!tip] 🩺 Status
> - [ ] **1. Signes vitaux *(Phéochromocytome)***
> 	- [ ] Tension artérielle
> 	- [ ] Fréquence cardiaque
> 	- [ ] Température
> - [ ] **2. Examen cardiovasculaire *(Phéochromocytome)***
> 	- [ ] Auscultation cardiaque
> 	- [ ] Pouls périphériques
> 	- [ ] Signes d'insuffisance cardiaque
> - [ ] **3. Examen pulmonaire *(Phéochromocytome)***
> 	- [ ] Auscultation pulmonaire
> 	- [ ] Signes de détresse respiratoire
> - [ ] **4. Examen cutané *(Phéochromocytome)***
> 	- [ ] Modifications cutanées actuelles
> 	- [ ] Télangiectasies
> 	- [ ] Érythème
> 	- [ ] Flush observable
> - [ ] **5. Examen abdominal *(Phéochromocytome)***
> 	- [ ] Hépatomégalie
> 	- [ ] Splénomégalie
> 	- [ ] Masses abdominales
> 	- [ ] Douleur/défense
> - [ ] **6. Examen thyroïdien *(Phéochromocytome)***
> 	- [ ] Palpation thyroïdienne
> 	- [ ] Signes d'hyperthyroïdie
> - [ ] **7. Examen neurologique *(Phéochromocytome)***
> 	- [ ] État de conscience
> 	- [ ] Tremblements
> 	- [ ] Réflexes
> - [ ] **8. Examen général *(Ménopause physiologique confirmée)***
> 	- [ ] État général
> 	- [ ] Poids et taille
> 	- [ ] IMC
> - [ ] **9. Examen de l'appareil locomoteur *(Ménopause physiologique confirmée)***
> 	- [ ] Examen de la colonne vertébrale
> 	- [ ] Recherche de diminution de taille
> 	- [ ] Recherche de cyphose dorsale
> 	- [ ] Évaluation du risque d'ostéoporose
> - [ ] **10. Examen mammaire *(Ménopause physiologique confirmée)***
> 	- [ ] Inspection des seins
> 	- [ ] Palpation mammaire bilatérale
> 	- [ ] Palpation des aires ganglionnaires axillaires
> - [ ] **11. Examen gynécologique *(Ménopause physiologique confirmée)***
> 	- [ ] Examen vulvaire (atrophie, sécheresse)
> 	- [ ] Examen au spéculum
> 	- [ ] Inspection du col utérin
> 	- [ ] Palpation bimanuelle
> - [ ] **12. Prélèvements *(Ménopause physiologique confirmée)***
> 	- [ ] Frottis cervico-vaginal
> 	- [ ] Prélèvements microbiologiques si indiqués

> [!success] 💊 Management — si Ménopause physiologique confirmée
> - [ ] **1. Examens complémentaires**
> 	- [ ] Dosage FSH (> 30 UI/L)
> 	- [ ] Dosage œstradiol (< 184 pmol/L)
> 	- [ ] Bilan lipidique
> 	- [ ] Glycémie à jeun
> 	- [ ] TSH
> 	- [ ] Mammographie de dépistage
> 	- [ ] Densitométrie osseuse (DMO)
> - [ ] **2. Utilisation correcte de la terminologie**
> 	- [ ] Ménopause : arrêt définitif des règles depuis 12 mois
> 	- [ ] Périménopause : période de transition avant la ménopause
> 	- [ ] Climatère : ensemble de la période de transition
> - [ ] **3. Traitement hormonal de la ménopause (THM)**
> - [ ] **4. Alternatives non hormonales**
> 	- [ ] ISRS/IRSN pour bouffées de chaleur
> 	- [ ] Gabapentine, clonidine
> 	- [ ] Phyto-œstrogènes (efficacité limitée)
> 	- [ ] Acupuncture, yoga, méditation
> 	- [ ] Lubrifiants et hydratants vaginaux
> - [ ] **5. Prévention et prise en charge de l'ostéoporose**
> 	- [ ] Calcium 1000-1200 mg/jour
> 	- [ ] Vitamine D 800-1000 UI/jour
> 	- [ ] Activité physique régulière avec mise en charge
> 	- [ ] Arrêt du tabac
> 	- [ ] Limitation de l'alcool
> 	- [ ] Prévention des chutes
> 	- [ ] Bisphosphonates si ostéoporose avérée
> - [ ] **6. Conseils pour la gestion des symptômes**
> 	- [ ] Bouffées de chaleur : vêtements légers, éviter déclencheurs
> 	- [ ] Sécheresse vaginale : lubrifiants, hydratants locaux
> 	- [ ] Troubles psychologiques : soutien, thérapie si besoin
> 	- [ ] Hygiène de vie : alimentation équilibrée, exercice
> - [ ] **7. Suivi et surveillance**
> 	- [ ] Réévaluation annuelle du rapport bénéfice/risque du THM
> 	- [ ] Mammographie tous les 2 ans
> 	- [ ] Frottis selon recommandations
> 	- [ ] DMO selon facteurs de risque
> 	- [ ] Surveillance tensionnelle et métabolique

> [!success] 💊 Management — si Phéochromocytome
> - [ ] **1. Diagnostic principal évoqué**
> - [ ] **2. Diagnostics différentiels**
> 	- [ ] Ménopause/périménopause
> 	- [ ] Causes médicamenteuses
> 	- [ ] Phéochromocytome
> 	- [ ] Syndrome carcinoïde
> 	- [ ] Polyglobulie vraie
> 	- [ ] Abus d'alcool chronique
> 	- [ ] Syndrome de Cushing
> 	- [ ] Diabète sucré
> 	- [ ] Hypertension artérielle essentielle
> 	- [ ] Rosacée
> 	- [ ] Lupus érythémateux systémique
> 	- [ ] Dermatomyosite
> 	- [ ] Sténose/insuffisance mitrale
> 	- [ ] Œdème pulmonaire
> 	- [ ] État fébrile
> - [ ] **3. Examens complémentaires**
> 	- [ ] Biologie sanguine
> 	- [ ] Dosages hormonaux spécifiques
> 	- [ ] Examens urinaires
> 	- [ ] Imagerie
> - [ ] **4. Prise en charge de l'anxiété**
> 	- [ ] Écoute empathique des inquiétudes
> 	- [ ] Rassurer sur l'antécédent familial de cancer rénal
> 	- [ ] Expliquer la démarche diagnostique
> 	- [ ] Proposer un suivi rapproché
> - [ ] **5. Prise en charge immédiate**
> 	- [ ] Surveillance tensionnelle rapprochée
> 	- [ ] Traitement antihypertenseur si nécessaire
> 	- [ ] Éviter les facteurs déclenchants
> 	- [ ] Conseils hygiéno-diététiques
> - [ ] **6. Orientation spécialisée**
> 	- [ ] Endocrinologue si suspicion endocrinienne
> 	- [ ] Gynécologue pour bilan ménopause
> 	- [ ] Hospitalisation si urgence hypertensive
> 	- [ ] Cardiologue si HTA sévère
> - [ ] **7. Planification du suivi**
> 	- [ ] Consultation de contrôle avec résultats
> 	- [ ] Carnet de surveillance tensionnelle
> 	- [ ] Journal des symptômes
> 	- [ ] Numéro d'urgence si aggravation
