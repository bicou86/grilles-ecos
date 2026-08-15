---
aliases:
  - "Mémento HTA (Suivi & Crise Hypertensive)"
type: memento-ecos-ssp
ssp: "HTA (Suivi & Crise Hypertensive)"
specialite: "Cardiologie & Vasculaire"
cas: 2
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

# HTA (Suivi & Crise Hypertensive) ⭐️

*Cardiologie & Vasculaire · 2 grilles · 1 diagnostic documenté* — [[SSP — HTA (Suivi & Crise Hypertensive)]]

> [!abstract] Les 2 grilles fusionnées
> - **German-53** — HTA `corrige` · [grille](<file:///Users/damienfulliquet/Developer/GitHub/grilles-ecos/cases/german/German-53_-_Hypertension_-_Grille_ECOS.html>)
> - **German-54** — HTA `corrige` · [grille](<file:///Users/damienfulliquet/Developer/GitHub/grilles-ecos/cases/german/German-54_-_Hypertension_-_Grille_ECOS.html>)

> [!note] 📋 Anamnèse
> - [ ] **1. Présentation avec nom, fonction et objectif**
> - [ ] **2. Motif de consultation principal**
> - [ ] **3. Circonstances de découverte *(1 grille sur 2)***
> 	- [ ] Contexte de la mesure
> 	- [ ] Appareil utilisé
> 	- [ ] Valeurs relevées
> 	- [ ] Fréquence des mesures
> 	- [ ] Depuis quand
> - [ ] **4. Symptômes associés**
> 	- [ ] Céphalées
> 	- [ ] Acouphènes *(1 grille sur 2)*
> 	- [ ] Vertiges
> 	- [ ] Épistaxis *(1 grille sur 2)*
> 	- [ ] Douleurs thoraciques
> 	- [ ] Dyspnée *(1 grille sur 2)*
> 	- [ ] Palpitations
> 	- [ ] Troubles visuels
> 	- [ ] Dyspnée d'effort *(1 grille sur 2)*
> 	- [ ] Œdèmes *(1 grille sur 2)*
> - [ ] **5. Antécédents cardiovasculaires *(1 grille sur 2)***
> 	- [ ] Maladies cardiaques
> 	- [ ] Angine de poitrine
> 	- [ ] Infarctus
> 	- [ ] AVC/AIT
> 	- [ ] Claudication intermittente
> - [ ] **6. Antécédents métaboliques et rénaux *(1 grille sur 2)***
> 	- [ ] Diabète
> 	- [ ] Dyslipidémie
> 	- [ ] Maladies rénales
> 	- [ ] Hyperuricémie
> - [ ] **7. Statut hormonal *(1 grille sur 2)***
> 	- [ ] Statut ménopausique
> 	- [ ] Traitement hormonal substitutif
> 	- [ ] Contraception antérieure
> - [ ] **8. Médicaments actuels**
> 	- [ ] Antihypertenseurs prescrits
> 	- [ ] Autres médicaments réguliers *(1 grille sur 2)*
> 	- [ ] Médicaments pouvant augmenter la TA *(1 grille sur 2)*
> 	- [ ] Posologie *(1 grille sur 2)*
> 	- [ ] Observance thérapeutique *(1 grille sur 2)*
> 	- [ ] Effets secondaires *(1 grille sur 2)*
> - [ ] **9. Habitudes de vie**
> 	- [ ] Alimentation
> 	- [ ] Consommation d'alcool
> 	- [ ] Tabagisme
> 	- [ ] Activité physique
> 	- [ ] Gestion du stress *(1 grille sur 2)*
> - [ ] **10. Antécédents familiaux cardiovasculaires**
> 	- [ ] Hypertension familiale
> 	- [ ] Maladies cardiovasculaires *(1 grille sur 2)*
> 	- [ ] Diabète
> 	- [ ] Maladies rénales *(1 grille sur 2)*
> 	- [ ] AVC
> 	- [ ] Infarctus du myocarde *(1 grille sur 2)*
> 	- [ ] Néphropathie *(1 grille sur 2)*
> - [ ] **11. Anamnèse sociale**
> 	- [ ] Profession *(1 grille sur 2)*
> 	- [ ] Situation familiale *(1 grille sur 2)*
> 	- [ ] Niveau de stress *(1 grille sur 2)*
> - [ ] **12. Évolution de l'hypertension *(1 grille sur 2)***
> 	- [ ] Hypertension connue depuis quand
> 	- [ ] Valeurs tensionnelles habituelles
> 	- [ ] Contrôle régulier
> 	- [ ] Compliance au traitement
> - [ ] **13. Facteurs d'aggravation *(1 grille sur 2)***
> 	- [ ] Stress récent
> 	- [ ] Modification du régime alimentaire
> 	- [ ] Prise de poids
> 	- [ ] Consommation de sel
> 	- [ ] Autres médicaments
> - [ ] **14. Complications cardiovasculaires *(1 grille sur 2)***
> 	- [ ] Antécédents d'AVC/AIT
> 	- [ ] Cardiopathie ischémique
> 	- [ ] Insuffisance cardiaque
> 	- [ ] Artériopathie périphérique
> 	- [ ] Néphropathie
> - [ ] **15. Comorbidités *(1 grille sur 2)***
> 	- [ ] Diabète
> 	- [ ] Dyslipidémie
> 	- [ ] Obésité
> 	- [ ] Syndrome d'apnée du sommeil
> 	- [ ] Insuffisance rénale

> [!tip] 🩺 Status
> - [ ] **1. Mesure correcte de la tension artérielle**
> 	- [ ] Position assise, repos 5 minutes *(1 grille sur 2)*
> 	- [ ] Bras à hauteur du cœur *(1 grille sur 2)*
> 	- [ ] Brassard adapté
> 	- [ ] Mesure aux deux bras
> 	- [ ] Au moins 2 mesures
> 	- [ ] Repos 5 minutes avant mesure *(1 grille sur 2)*
> 	- [ ] Position assise correcte *(1 grille sur 2)*
> - [ ] **2. Examen cardiovasculaire**
> 	- [ ] Auscultation cardiaque (rythme, souffles)
> 	- [ ] Recherche de souffles vasculaires (carotides, abdomen) *(1 grille sur 2)*
> 	- [ ] Palpation des pouls périphériques
> 	- [ ] Recherche d'œdèmes des membres inférieurs *(1 grille sur 2)*
> 	- [ ] Recherche de souffle *(1 grille sur 2)*
> 	- [ ] Recherche de B3/B4 *(1 grille sur 2)*
> - [ ] **3. Recherche de signes d'HTA secondaire *(1 grille sur 2)***
> 	- [ ] Inspection (faciès cushingoïde)
> 	- [ ] Palpation abdominale (masses, souffle rénal)
> 	- [ ] Recherche de signes d'hyperthyroïdie
> 	- [ ] Examen de la thyroïde
> - [ ] **4. Évaluation du retentissement *(1 grille sur 2)***
> 	- [ ] Auscultation pulmonaire
> 	- [ ] Fond d'œil (ou mentionner la nécessité)
> 	- [ ] Examen neurologique sommaire
> 	- [ ] Recherche de protéinurie (bandelette)
> - [ ] **5. Données anthropométriques *(1 grille sur 2)***
> 	- [ ] Poids et taille
> 	- [ ] Calcul de l'IMC
> 	- [ ] Tour de taille
> 	- [ ] Évaluation de l'obésité abdominale
> - [ ] **6. Hygiène et préparation *(1 grille sur 2)***
> 	- [ ] Désinfection des mains
> 	- [ ] Installation correcte du patient
> - [ ] **7. Évaluation générale *(1 grille sur 2)***
> 	- [ ] État général
> 	- [ ] Poids et taille (IMC)
> 	- [ ] Tour de taille
> - [ ] **8. Examen pulmonaire *(1 grille sur 2)***
> 	- [ ] Auscultation pulmonaire
> 	- [ ] Recherche de râles
> 	- [ ] Signes d'insuffisance cardiaque
> - [ ] **9. Recherche d'œdèmes *(1 grille sur 2)***
> 	- [ ] Œdèmes des membres inférieurs
> 	- [ ] Signe du godet
> 	- [ ] Bilatéralité
> - [ ] **10. Examen des organes cibles *(1 grille sur 2)***
> 	- [ ] Fond d'œil (ou mention)
> 	- [ ] Examen neurologique sommaire
> 	- [ ] Palpation rénale
> 	- [ ] Recherche de souffles vasculaires

> [!success] 💊 Management — si HTA
> - [ ] **1. Diagnostic principal**
> - [ ] **2. Diagnostics différentiels d'HTA secondaire *(1 grille sur 2)***
> - [ ] **3. Facteurs de risque cardiovasculaire identifiés *(1 grille sur 2)***
> 	- [ ] Âge (femme > 55 ans)
> 	- [ ] Antécédents familiaux cardiovasculaires
> 	- [ ] Surpoids
> 	- [ ] Sédentarité
> 	- [ ] Consommation de sel élevée
> 	- [ ] Stress
> - [ ] **4. Examens complémentaires *(1 grille sur 2)***
> 	- [ ] Bilan biologique (FSC, ionogramme, créatinine, glycémie)
> 	- [ ] Bilan lipidique complet
> 	- [ ] TSH
> 	- [ ] Analyse d'urine (protéinurie, hématurie)
> 	- [ ] ECG de repos
> 	- [ ] MAPA ou automesure tensionnelle
> - [ ] **5. Examens de retentissement *(1 grille sur 2)***
> 	- [ ] Échocardiographie
> 	- [ ] Fond d'œil
> 	- [ ] Écho-Doppler des artères rénales si suspicion
> 	- [ ] Radiographie thoracique
> - [ ] **6. Mesures hygiéno-diététiques**
> 	- [ ] Régime sans sel strict *(1 grille sur 2)*
> 	- [ ] Réduction pondérale progressive *(1 grille sur 2)*
> 	- [ ] Activité physique adaptée *(1 grille sur 2)*
> 	- [ ] Gestion du stress *(1 grille sur 2)*
> 	- [ ] Éviter les médicaments néphrotoxiques *(1 grille sur 2)*
> - [ ] **7. Stratégie médicamenteuse *(1 grille sur 2)***
> 	- [ ] Confirmation par MAPA avant traitement
> 	- [ ] Si confirmé : IEC ou ARA2 en première intention
> 	- [ ] Alternative : diurétique thiazidique ou inhibiteur calcique
> 	- [ ] Bithérapie si objectif non atteint
> 	- [ ] Surveillance de la fonction rénale et kaliémie
> - [ ] **8. Objectifs thérapeutiques *(1 grille sur 2)***
> 	- [ ] TA < 140/90 mmHg en consultation
> 	- [ ] TA < 135/85 mmHg en automesure
> 	- [ ] Réduction du risque cardiovasculaire global
> - [ ] **9. Suivi et éducation *(1 grille sur 2)***
> 	- [ ] Contrôle dans 1 mois
> 	- [ ] Éducation à l'automesure
> 	- [ ] Importance de l'observance
> 	- [ ] Carnet de suivi tensionnel
> 	- [ ] Consultation annuelle systématique
> - [ ] **10. Facteurs de décompensation identifiés *(1 grille sur 2)***
> 	- [ ] Mauvaise observance thérapeutique
> 	- [ ] Prise d'AINS
> 	- [ ] Augmentation de la consommation de sel
> 	- [ ] Stress psychosocial
> 	- [ ] Prise de poids
> - [ ] **11. Examens complémentaires urgents *(1 grille sur 2)***
> 	- [ ] ECG
> 	- [ ] Bilan biologique (ionogramme, créatinine)
> 	- [ ] BNP ou NT-proBNP
> 	- [ ] Radiographie thoracique
> 	- [ ] Échocardiographie
> - [ ] **12. Adaptation thérapeutique immédiate *(1 grille sur 2)***
> - [ ] **13. Éducation thérapeutique renforcée *(1 grille sur 2)***
> 	- [ ] Importance de l'observance
> 	- [ ] Utilisation d'un pilulier
> 	- [ ] Reconnaissance des signes d'alarme
> 	- [ ] Automesure tensionnelle
> 	- [ ] Carnet de suivi
> - [ ] **14. Critères d'hospitalisation *(1 grille sur 2)***
> 	- [ ] TA > 180/110 avec signes de souffrance
> 	- [ ] Insuffisance cardiaque décompensée
> 	- [ ] Suspicion d'urgence hypertensive
> 	- [ ] Mauvaise réponse au traitement
> - [ ] **15. Plan de suivi *(1 grille sur 2)***
> 	- [ ] Contrôle dans 1 semaine
> 	- [ ] Puis tous les 15 jours jusqu'à stabilisation
> 	- [ ] Surveillance fonction rénale et ionogramme
> 	- [ ] Ajustement thérapeutique selon évolution
> 	- [ ] Référence cardiologue si nécessaire
> - [ ] **16. Information et motivation du patient *(1 grille sur 2)***
> 	- [ ] Expliquer les risques de l'HTA non contrôlée
> 	- [ ] Importance du traitement à vie
> 	- [ ] Bénéfices attendus
> 	- [ ] Impliquer l'entourage
> 	- [ ] Groupe de soutien si nécessaire
