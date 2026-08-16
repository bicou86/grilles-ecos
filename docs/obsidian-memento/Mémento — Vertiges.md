---
aliases:
  - "Mémento Vertiges"
type: memento-ecos-ssp
ssp: "Vertiges"
specialite: "Neurologie"
cas: 2
diagnostics: 2
attendus_documentes_ailleurs: 1
attendus_absents_du_corpus: 1
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

# Vertiges ⭐️

*Neurologie · 2 grilles · 2 diagnostics documentés · 1 attendu documenté ailleurs · 1 attendu absent du corpus* — [[SSP — Vertiges]]

> [!abstract] Les 2 grilles fusionnées
> - **AMBOSS-40** — Zona auriculaire (syndrome de Ramsay Hunt) `premier-dd` · [grille](<file:///Users/damienfulliquet/Developer/GitHub/grilles-ecos/cases/amboss/AMBOSS-40_-_Vertiges_-_Homme_25_ans_-_Grille_ECOS.html>)
> - **RESCOS-66** — Maladie de Parkinson `premier-dd` · [grille](<file:///Users/damienfulliquet/Developer/GitHub/grilles-ecos/cases/rescos/RESCOS-66%20-%20Troubles%20de%20l'équilibre%20-%20ECC%20Neurologie%20-%20Grille%20ECOS.html>)

> [!note] 📋 Anamnèse
> - [ ] **1. Motif principal *(Zona auriculaire (syndrome de Ramsay Hunt))***
> - [ ] **2. Caractérisation des vertiges *(Zona auriculaire (syndrome de Ramsay Hunt))***
> 	- [ ] Description des vertiges
> 	- [ ] Début
> 	- [ ] Constant/intermittent
> 	- [ ] Événements précipitants
> 	- [ ] Progression
> 	- [ ] Épisodes antérieurs
> 	- [ ] Facteurs améliorants
> 	- [ ] Facteurs aggravants
> 	- [ ] Symptômes associés
> - [ ] **3. Recherche de symptômes spécifiques pour vertiges *(Zona auriculaire (syndrome de Ramsay Hunt))***
> 	- [ ] Traumatisme
> 	- [ ] Céphalée
> 	- [ ] Fièvre/frissons
> 	- [ ] Éruption cutanée/changements cutanés
> 	- [ ] Toux
> 	- [ ] Infections récentes
> 	- [ ] Acouphènes
> 	- [ ] Plénitude auriculaire
> 	- [ ] Perte auditive
> 	- [ ] Changements de vision
> 	- [ ] Engourdissement/faiblesse/picotements
> 	- [ ] Prurit
> - [ ] **4. Antécédents médicaux *(Zona auriculaire (syndrome de Ramsay Hunt))***
> 	- [ ] Antécédents médicaux
> 	- [ ] Varicelle dans le passé
> - [ ] **5. Allergies *(Zona auriculaire (syndrome de Ramsay Hunt))***
> - [ ] **6. Médicaments *(Zona auriculaire (syndrome de Ramsay Hunt))***
> - [ ] **7. Hospitalisations et antécédents chirurgicaux *(Zona auriculaire (syndrome de Ramsay Hunt))***
> 	- [ ] Hospitalisations
> 	- [ ] Antécédents chirurgicaux
> - [ ] **8. Contacts malades et antécédents familiaux *(Zona auriculaire (syndrome de Ramsay Hunt))***
> 	- [ ] Contacts malades
> 	- [ ] Antécédents familiaux
> - [ ] **9. Habitudes et mode de vie *(Zona auriculaire (syndrome de Ramsay Hunt))***
> 	- [ ] Travail
> 	- [ ] Domicile
> 	- [ ] Alcool
> 	- [ ] Drogues récréatives
> 	- [ ] Tabac
> - [ ] **10. Caractérisation des troubles de l'équilibre *(Maladie de Parkinson)***
> 	- [ ] Type de déséquilibre
> 	- [ ] Circonstances d'apparition
> 	- [ ] Évolution temporelle
> 	- [ ] Facteurs aggravants
> 	- [ ] Retentissement fonctionnel
> - [ ] **11. Analyse de l'amaigrissement *(Maladie de Parkinson)***
> 	- [ ] Perte de poids chiffrée
> 	- [ ] Modification de l'appétit
> 	- [ ] Troubles de la déglutition
> 	- [ ] Troubles digestifs
> 	- [ ] Contexte psychologique
> - [ ] **12. Symptômes neurologiques associés *(Maladie de Parkinson)***
> 	- [ ] Troubles cognitifs
> 	- [ ] Troubles moteurs
> 	- [ ] Troubles sensitifs
> 	- [ ] Troubles visuels
> 	- [ ] Troubles de la parole
> - [ ] **13. Recherche de signes d'alarme oncologique *(Maladie de Parkinson)***
> 	- [ ] Altération état général
> 	- [ ] Douleurs
> 	- [ ] Antécédents néoplasiques
> 	- [ ] Symptômes spécifiques d'organe
> 	- [ ] Facteurs de risque
> - [ ] **14. Antécédents et comorbidités *(Maladie de Parkinson)***
> 	- [ ] Maladies neurodégénératives
> 	- [ ] Pathologies cardiovasculaires
> 	- [ ] Troubles métaboliques
> 	- [ ] Maladies auto-immunes
> 	- [ ] Chirurgies antérieures
> - [ ] **15. Médicaments et toxiques *(Maladie de Parkinson)***
> 	- [ ] Psychotropes
> 	- [ ] Antiépileptiques
> 	- [ ] Antihypertenseurs
> 	- [ ] Oto-toxiques
> 	- [ ] Alcoolisme

> [!tip] 🩺 Status
> - [ ] **1. Mesures d'hygiène *(Zona auriculaire (syndrome de Ramsay Hunt))***
> 	- [ ] Lavage des mains
> 	- [ ] Respect de la pudeur avec drap
> - [ ] **2. Examen de la tête, yeux, oreilles, nez et gorge *(Zona auriculaire (syndrome de Ramsay Hunt))***
> 	- [ ] Inspection de la tête
> 	- [ ] Palpation de la tête
> 	- [ ] Inspection des oreilles
> 	- [ ] Palpation des oreilles
> 	- [ ] Otoscopie
> - [ ] **3. Tests auditifs *(Zona auriculaire (syndrome de Ramsay Hunt))***
> 	- [ ] Test de Rinne et test de Weber
> 	- [ ] Test de Dix-Hallpike
> - [ ] **4. Examen neurologique général**
> 	- [ ] Examen ciblé des nerfs crâniens *(Zona auriculaire (syndrome de Ramsay Hunt))*
> 	- [ ] Examen ciblé de l'audition *(Zona auriculaire (syndrome de Ramsay Hunt))*
> 	- [ ] Examen ciblé des mouvements passifs et actifs *(Zona auriculaire (syndrome de Ramsay Hunt))*
> 	- [ ] Examen ciblé de la sensibilité *(Zona auriculaire (syndrome de Ramsay Hunt))*
> 	- [ ] Examen ciblé des réflexes ostéotendineux *(Zona auriculaire (syndrome de Ramsay Hunt))*
> 	- [ ] Examen ciblé de la marche *(Zona auriculaire (syndrome de Ramsay Hunt))*
> 	- [ ] Test d'alternance rapide des mouvements *(Zona auriculaire (syndrome de Ramsay Hunt))*
> 	- [ ] Test doigt-nez *(Zona auriculaire (syndrome de Ramsay Hunt))*
> 	- [ ] Test de Romberg *(Zona auriculaire (syndrome de Ramsay Hunt))*
> 	- [ ] Fonctions supérieures *(Maladie de Parkinson)*
> 	- [ ] Nerfs crâniens *(Maladie de Parkinson)*
> 	- [ ] Force musculaire *(Maladie de Parkinson)*
> 	- [ ] Réflexes ostéotendineux *(Maladie de Parkinson)*
> 	- [ ] Signes pyramidaux *(Maladie de Parkinson)*
> - [ ] **5. Évaluation de l'état général et nutritionnel *(Maladie de Parkinson)***
> 	- [ ] Poids et taille
> 	- [ ] État d'hydratation
> 	- [ ] Pâleur
> 	- [ ] Adénopathies
> 	- [ ] Signes vitaux
> - [ ] **6. Examen de la statique et de la marche *(Maladie de Parkinson)***
> 	- [ ] Station debout
> 	- [ ] Marche spontanée
> 	- [ ] Demi-tour
> 	- [ ] Marche sur ligne droite
> 	- [ ] Marche yeux fermés
> - [ ] **7. Examen de la coordination cérébelleuse *(Maladie de Parkinson)***
> 	- [ ] Épreuves index-nez
> 	- [ ] Épreuves talon-genou
> 	- [ ] Mouvements alternés rapides
> 	- [ ] Écriture
> 	- [ ] Dysarthrie cérébelleuse
> - [ ] **8. Examen du système extrapyramidal *(Maladie de Parkinson)***
> 	- [ ] Tonus musculaire
> 	- [ ] Tremblements
> 	- [ ] Bradykinésie
> 	- [ ] Réflexes posturaux
> 	- [ ] Micrographie, hypomimie faciale
> - [ ] **9. Examen de la sensibilité proprioceptive *(Maladie de Parkinson)***
> 	- [ ] Sensibilité positionnelle
> 	- [ ] Sensibilité vibratoire
> 	- [ ] Romberg
> 	- [ ] Marche aveugle
> 	- [ ] Pseudo-athétose
> - [ ] **10. Examen vestibulaire et oculomoteur *(Maladie de Parkinson)***
> 	- [ ] Nystagmus
> 	- [ ] Mouvements oculaires
> 	- [ ] Manœuvre de Dix-Hallpike
> 	- [ ] Head impulse test
> 	- [ ] Coordination œil-tête

> [!success] 💊 Management — si HypoTA orthostatique
> *Aucune grille de cette SSP ne documente ce diagnostic* — mais le corpus le documente ailleurs : [[Mémento — Syncope & Perte de Connaissance]] (2 grilles) · [[Mémento — Chute & Évaluation Gériatrique]] (1 grille).

> [!success] 💊 Management — si Maladie de Parkinson
> - [ ] **1. Diagnostic syndromique des troubles de l'équilibre**
> 	- [ ] Ataxie cérébelleuse
> 	- [ ] Ataxie sensitive
> 	- [ ] Syndrome extrapyramidal
> 	- [ ] Atteinte vestibulaire
> - [ ] **2. Diagnostic étiologique - causes des troubles de l'équilibre**
> - [ ] **3. Bilan étiologique de l'amaigrissement**
> 	- [ ] Recherche néoplasique
> 	- [ ] Bilan inflammatoire
> 	- [ ] Endoscopies digestives
> 	- [ ] Bilan thyroïdien
> - [ ] **4. Examens complémentaires neurologiques**
> 	- [ ] IRM cérébrale
> 	- [ ] Électromyogramme
> 	- [ ] Ponction lombaire
> 	- [ ] Anticorps paranéoplasiques
> - [ ] **5. Prise en charge symptomatique**
> 	- [ ] Rééducation équilibre
> 	- [ ] Aides techniques
> 	- [ ] Aménagement domicile
> 	- [ ] Support nutritionnel
> - [ ] **6. Traitement étiologique selon la cause**
> - [ ] **7. Prévention des chutes et sécurité**
> 	- [ ] Évaluation risque de chute
> 	- [ ] Révision médicamenteuse
> 	- [ ] Correction déficits sensoriels
> 	- [ ] Programme d'exercices adaptés
> - [ ] **8. Surveillance et orientation**
> 	- [ ] Suivi neurologique spécialisé
> 	- [ ] Oncologie
> 	- [ ] Gériatrie
> 	- [ ] Rééducation fonctionnelle

> [!success] 💊 Management — si Névrite vestibulaire / Ménière
> *Aucune grille du corpus ne documente ce diagnostic* — il est pourtant attendu de cette SSP. **Trou de révision à combler ailleurs.**

> [!success] 💊 Management — si Zona auriculaire (syndrome de Ramsay Hunt)
> - [ ] **1. Hypothèses diagnostiques**
> - [ ] **2. Examens complémentaires**
> 	- [ ] Audiométrie tonale
> 	- [ ] Potentiels évoqués auditifs du tronc cérébral
> - [ ] **3. Communication avec le patient**
> 	- [ ] Explications au patient des impressions diagnostiques préliminaires
> 	- [ ] Explication du plan de prise en charge
> 	- [ ] Utilisation d'un langage non médical et clarification des termes médicaux
> 	- [ ] Évaluation de l'accord du patient avec le plan diagnostique
> 	- [ ] Recherche des préoccupations et questions du patient
> - [ ] **4. Conseil et soutien**
> 	- [ ] Conseil sur les drogues récréatives
> 	- [ ] Conseil sur l'arrêt du tabac
> 	- [ ] Réaction appropriée au défi concernant le départ
