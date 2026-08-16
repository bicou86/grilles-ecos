---
aliases:
  - "Mémento Vaccination & Prévention Pédiatrique"
type: memento-ecos-ssp
ssp: "Vaccination & Prévention Pédiatrique"
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

# Vaccination & Prévention Pédiatrique

*Pédiatrie · 1 grille · 1 diagnostic documenté* — [[SSP — Vaccination & Prévention Pédiatrique]]

> [!abstract] La seule grille de cette SSP
> - **German-39** — Conseil en vaccination du nourrisson `confirme` · [grille](<file:///Users/damienfulliquet/Developer/GitHub/grilles-ecos/cases/german/German-39_-_EM_Vaccinations_-_Pe_diatrie_-_Grille_ECOS.html>)

> [!note] 📋 Anamnèse
> - [ ] **1. Présentation avec nom, fonction et objectif de la consultation**
> - [ ] **2. Explorer les questions de la mère**
> - [ ] **3. Antécédents vaccinaux et expériences**
> 	- [ ] Statut vaccinal de la mère
> 	- [ ] Profession des parents
> 	- [ ] Niveau de connaissances sur les vaccinations
> - [ ] **4. Explorer les craintes et l'environnement social**
> 	- [ ] Angoisses spécifiques concernant les vaccinations
> 	- [ ] Influence de l'entourage (famille, amis, groupe de parents)
> - [ ] **5. Gestion des questions sur les effets secondaires**
> 	- [ ] Effets secondaires courants (douleur locale, rougeur, fièvre légère)
> 	- [ ] Effets secondaires graves très rares
> 	- [ ] Balance bénéfice-risque favorable
> 	- [ ] Comparaison avec les risques des maladies évitées
> - [ ] **6. Réponse aux préoccupations sur l'autisme**
> 	- [ ] Coïncidence temporelle uniquement
> 	- [ ] Études nombreuses confirmant la sécurité
> - [ ] **7. Explication de l'âge de vaccination précoce**
> 	- [ ] Vaccination dès 8 semaines car système immunitaire encore immature
> 	- [ ] Protection nécessaire justement parce que les bébés sont vulnérables
> 	- [ ] Anticorps maternels diminuent après quelques mois
> - [ ] **8. Gestion de la pression sociale négative**
> 	- [ ] Explication du concept d'immunité collective
> 	- [ ] Responsabilité collective pour protéger les plus vulnérables
> 	- [ ] Approche empathique face aux critiques
> - [ ] **9. Sensibilisation aux maladies évitables par vaccination**
> 	- [ ] Nous sommes privilégiés grâce aux vaccinations
> 	- [ ] Maladies graves devenues rares donc méconnues
> 	- [ ] Conséquences potentiellement dramatiques des maladies
> - [ ] **10. Information sur le caractère non obligatoire**
> 	- [ ] Décision parentale mais avec responsabilité des conséquences
> 	- [ ] Certaines structures peuvent exiger des vaccinations
> - [ ] **11. Explication des échecs vaccinaux possibles**
> 	- [ ] Nécessité de doses multiples pour une protection optimale
> 	- [ ] Échecs vaccinaux rares mais possibles
> 	- [ ] Importance du respect du calendrier vaccinal
> - [ ] **12. Information sur la prise en charge financière**
> 	- [ ] Vaccinations de base remboursées par l'assurance maladie
> 	- [ ] Vaccinations recommandées prises en charge

> [!tip] 🩺 Status
> - [ ] **1. Explication du plan vaccinal DTPa-IPV-Hib-HBV**
> 	- [ ] Schéma: 2, 4, 6, 15-24 mois, 4-7 ans, 11-15 ans, 25-29 ans
> 	- [ ] Diphtérie: croup, obstruction des voies respiratoires, myocardite, polyneuropathie
> 	- [ ] Tétanos: contractions musculaires graves, potentiellement mortel
> 	- [ ] Coqueluche: attention particulière chez les nourrissons (risque d'apnée)
> 	- [ ] Poliomyélite: paralysie, encore présente dans certains pays
> 	- [ ] Haemophilus influenzae b: méningite, épiglottite, pneumonie
> 	- [ ] Hépatite B: protection précoce importante
> - [ ] **2. Explication vaccination pneumocoques**
> 	- [ ] Schéma: 2, 4 et 12 mois
> 	- [ ] Protection contre méningite, pneumonie, septicémie
> 	- [ ] Particulièrement dangereux pour les nourrissons
> - [ ] **3. Explication vaccination ROR**
> 	- [ ] Schéma: 12 mois et 15-24 mois
> 	- [ ] Rougeole: >1 million décès/an dans le monde, complications: otite, pneumonie, encéphalite (1/1000, létalité 30%)
> 	- [ ] Oreillons: méningite, surdité, orchite avec risque de stérilité
> 	- [ ] Rubéole: dangereux pendant la grossesse, encéphalite rubéoleuse
> - [ ] **4. Explication vaccination méningocoques**
> 	- [ ] Schéma: 12-15 mois et 11-15 ans
> 	- [ ] Méningite fulminante avec létalité de 10%
> 	- [ ] Septicémie méningococcique
> - [ ] **5. Information sur les autres vaccinations**
> 	- [ ] HPV: 11-14 ans (2 doses)
> 	- [ ] Varicelle: si pas contractée naturellement, vaccination à 11-14 ans
> 	- [ ] Hépatite A: selon voyages et exposition
> 	- [ ] FSME: selon région et activités
> 	- [ ] Grippe: annuelle pour groupes à risque
> - [ ] **6. Utilisation du carnet de vaccination**
> 	- [ ] Importance du suivi vaccinal
> 	- [ ] Conservation des dates et lots
> 	- [ ] Document officiel pour voyages et inscriptions

> [!success] 💊 Management — si Conseil en vaccination du nourrisson
> - [ ] **1. Remise de documentation officielle**
> 	- [ ] Guide de vaccination de l'OFSP
> 	- [ ] Brochures d'information adaptées
> 	- [ ] Site web de référence pour informations fiables
> - [ ] **2. Planification concrète du suivi vaccinal**
> 	- [ ] Proposition de premier rendez-vous à 2 mois
> 	- [ ] Explication du calendrier complet
> 	- [ ] Convenir que la mère recontacte pour fixer le rendez-vous
> - [ ] **3. Disponibilité pour questions supplémentaires**
> 	- [ ] Offrir un nouvel entretien si nécessaire
> 	- [ ] Possibilité de contact téléphonique
> 	- [ ] Porte ouverte pour toute inquiétude
> - [ ] **4. Mise en garde sur les sources d'information**
> 	- [ ] Prudence vis-à-vis des informations Internet non vérifiées
> 	- [ ] Privilégier les sources officielles (OFSP, pédiatre)
> 	- [ ] Éviter les forums et réseaux sociaux pour information médicale
> - [ ] **5. Encouragement bienveillant à la vaccination**
> 	- [ ] Renforcement positif de la démarche de s'informer
> 	- [ ] Rappel des bénéfices pour les enfants
> 	- [ ] Respect du processus décisionnel parental
