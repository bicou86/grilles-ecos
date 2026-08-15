---
aliases:
  - "Mémento Ictère"
type: memento-ecos-ssp
ssp: "Ictère"
specialite: "Gastro-Hépatologie"
cas: 2
diagnostics: 2
attendus_documentes_ailleurs: 0
attendus_absents_du_corpus: 2
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

# Ictère ⭐️

*Gastro-Hépatologie · 2 grilles · 2 diagnostics documentés · 2 attendus absents du corpus* — [[SSP — Ictère]]

> [!abstract] Les 2 grilles fusionnées
> - **German-55** — Hépatite (virale/alcoolique) `corrige` · [grille](<file:///Users/damienfulliquet/Developer/GitHub/grilles-ecos/cases/german/German-55_-_Icte_re_-_Grille_ECOS.html>)
> - **RESCOS-47** — Néoplasie des voies biliaires/pancréatique `explicite` · [grille](<file:///Users/damienfulliquet/Developer/GitHub/grilles-ecos/cases/rescos/RESCOS-47%20-%20Ictère%20-%20Grille%20ECOS.html>)

> [!note] 📋 Anamnèse
> - [ ] **1. Présentation avec nom, fonction et objectif *(Hépatite (virale/alcoolique))***
> - [ ] **2. Motif de consultation principal *(Hépatite (virale/alcoolique))***
> - [ ] **3. Caractéristiques de l'ictère *(Hépatite (virale/alcoolique))***
> 	- [ ] Début et évolution
> 	- [ ] Localisation
> 	- [ ] Progression
> 	- [ ] Coloration des sclérotiques
> - [ ] **4. Symptômes digestifs**
> 	- [ ] Douleurs abdominales
> 	- [ ] Nausées/vomissements
> 	- [ ] Troubles du transit *(Hépatite (virale/alcoolique))*
> 	- [ ] Ballonnements *(Hépatite (virale/alcoolique))*
> 	- [ ] Fréquence des selles *(Néoplasie des voies biliaires/pancréatique)*
> 	- [ ] Sang dans les selles *(Néoplasie des voies biliaires/pancréatique)*
> 	- [ ] Couleur des selles *(Néoplasie des voies biliaires/pancréatique)*
> 	- [ ] Dysphagie *(Néoplasie des voies biliaires/pancréatique)*
> - [ ] **5. Caractéristiques des selles et urines *(Hépatite (virale/alcoolique))***
> 	- [ ] Couleur des selles
> 	- [ ] Consistance des selles
> 	- [ ] Couleur des urines
> 	- [ ] Fréquence urinaire
> - [ ] **6. Symptômes généraux**
> 	- [ ] Fièvre/frissons *(Hépatite (virale/alcoolique))*
> 	- [ ] Asthénie *(Hépatite (virale/alcoolique))*
> 	- [ ] Perte de poids
> 	- [ ] Sueurs nocturnes *(Hépatite (virale/alcoolique))*
> 	- [ ] Anorexie *(Hépatite (virale/alcoolique))*
> 	- [ ] Fièvre *(Néoplasie des voies biliaires/pancréatique)*
> 	- [ ] Sudations nocturnes *(Néoplasie des voies biliaires/pancréatique)*
> 	- [ ] Frissons *(Néoplasie des voies biliaires/pancréatique)*
> - [ ] **7. Événements récents *(Hépatite (virale/alcoolique))***
> 	- [ ] Maladie récente
> 	- [ ] Prise médicamenteuse
> 	- [ ] Traumatisme
> 	- [ ] Stress particulier
> - [ ] **8. Prurit *(Hépatite (virale/alcoolique))***
> - [ ] **9. Signes d'hépatopathie chronique *(Hépatite (virale/alcoolique))***
> 	- [ ] Ascite
> 	- [ ] Œdèmes des membres inférieurs
> 	- [ ] Circulation collatérale
> 	- [ ] Gynécomastie
> - [ ] **10. Facteurs de risque hépatiques *(Hépatite (virale/alcoolique))***
> 	- [ ] Consommation d'alcool
> 	- [ ] Toxicomanie IV
> 	- [ ] Tatouages/piercings
> 	- [ ] Transfusions
> 	- [ ] Rapports sexuels à risque
> - [ ] **11. Antécédents médicaux**
> 	- [ ] Diabète *(Hépatite (virale/alcoolique))*
> 	- [ ] Maladies hépatiques *(Hépatite (virale/alcoolique))*
> 	- [ ] Chirurgies abdominales *(Hépatite (virale/alcoolique))*
> 	- [ ] Lithiase biliaire *(Hépatite (virale/alcoolique))*
> 	- [ ] Médicaux *(Néoplasie des voies biliaires/pancréatique)*
> 	- [ ] Chirurgicaux *(Néoplasie des voies biliaires/pancréatique)*
> 	- [ ] Allergies *(Néoplasie des voies biliaires/pancréatique)*
> - [ ] **12. Médicaments et allergies *(Hépatite (virale/alcoolique))***
> 	- [ ] Traitements en cours
> 	- [ ] Allergies médicamenteuses
> 	- [ ] Phytothérapie
> 	- [ ] Compléments alimentaires
> - [ ] **13. Statut vaccinal *(Hépatite (virale/alcoolique))***
> 	- [ ] Vaccination hépatite A
> 	- [ ] Vaccination hépatite B
> - [ ] **14. Voyages récents *(Hépatite (virale/alcoolique))***
> 	- [ ] Destination
> 	- [ ] Durée du séjour
> 	- [ ] Conditions sanitaires
> 	- [ ] Alimentation sur place
> - [ ] **15. Antécédents familiaux**
> 	- [ ] Maladies hépatiques familiales *(Hépatite (virale/alcoolique))*
> 	- [ ] Cancers digestifs *(Hépatite (virale/alcoolique))*
> 	- [ ] Maladies génétiques *(Hépatite (virale/alcoolique))*
> 	- [ ] Père décédé d'un cancer du pancréas diagnostiqué après ictère *(Néoplasie des voies biliaires/pancréatique)*
> 	- [ ] Mère décédée d'un AVC *(Néoplasie des voies biliaires/pancréatique)*
> - [ ] **16. Anamnèse sociale *(Hépatite (virale/alcoolique))***
> 	- [ ] Profession
> 	- [ ] Conditions de vie
> 	- [ ] Statut en Suisse
> - [ ] **17. Ictère *(Néoplasie des voies biliaires/pancréatique)***
> 	- [ ] Début
> 	- [ ] Localisation
> 	- [ ] Facteurs aggravants
> 	- [ ] Facteurs atténuants
> 	- [ ] Constant vs Fluctuant
> 	- [ ] Contexte d'apparition
> - [ ] **18. Ictère - précisions *(Néoplasie des voies biliaires/pancréatique)***
> 	- [ ] Symptômes associés
> 	- [ ] Premier épisode vs récurrent
> - [ ] **19. Anamnèse uro-génitale *(Néoplasie des voies biliaires/pancréatique)***
> 	- [ ] Couleur des urines
> 	- [ ] Sang dans les urines
> 	- [ ] Dernières règles
> - [ ] **20. DD : hépatites *(Néoplasie des voies biliaires/pancréatique)***
> 	- [ ] Vaccins hépatites A et B
> 	- [ ] Drogues IV
> 	- [ ] Rapports sexuels à risque
> 	- [ ] Voyages dans des zones endémiques
> - [ ] **21. Habitudes *(Néoplasie des voies biliaires/pancréatique)***
> 	- [ ] Alimentaires
> 	- [ ] Médicaments

> [!tip] 🩺 Status
> - [ ] **1. État général et signes vitaux *(Hépatite (virale/alcoolique))***
> 	- [ ] État général
> 	- [ ] Température
> 	- [ ] Tension artérielle
> 	- [ ] Fréquence cardiaque
> - [ ] **2. Examen cutanéo-muqueux *(Hépatite (virale/alcoolique))***
> 	- [ ] Ictère conjonctival
> 	- [ ] Ictère cutané (localisation)
> 	- [ ] Signes cutanés d'hépatopathie (angiomes stellaires, érythrose palmaire)
> 	- [ ] Traces de grattage
> - [ ] **3. Examen abdominal complet *(Hépatite (virale/alcoolique))***
> 	- [ ] Inspection (distension, circulation collatérale)
> 	- [ ] Palpation hépatique (taille, consistance, bord)
> 	- [ ] Palpation splénique
> 	- [ ] Recherche d'ascite (matité déclive)
> 	- [ ] Douleur à la palpation (Murphy)
> - [ ] **4. Examen ganglionnaire *(Hépatite (virale/alcoolique))***
> 	- [ ] Aires cervicales
> 	- [ ] Aires axillaires
> 	- [ ] Aires inguinales
> 	- [ ] Ganglion de Troisier
> - [ ] **5. Examen cardio-pulmonaire *(Hépatite (virale/alcoolique))***
> 	- [ ] Auscultation cardiaque
> 	- [ ] Auscultation pulmonaire
> 	- [ ] Recherche d'œdèmes périphériques
> - [ ] **6. Examen neurologique sommaire *(Hépatite (virale/alcoolique))***
> 	- [ ] État de conscience
> 	- [ ] Astérixis (flapping tremor)
> 	- [ ] Réflexes ostéo-tendineux
> - [ ] **7. Préparation du status *(Néoplasie des voies biliaires/pancréatique)***
> 	- [ ] Position de l'étudiant à droite du patient
> 	- [ ] Jambes du patient décroisées et bras le long du corps
> 	- [ ] Tête du patient légèrement surélevée
> - [ ] **8. Auscultation *(Néoplasie des voies biliaires/pancréatique)***
> 	- [ ] Auscultation avant palpation
> 	- [ ] 4 quadrants
> - [ ] **9. Percussion *(Néoplasie des voies biliaires/pancréatique)***
> 	- [ ] 4 quadrants
> 	- [ ] Percussion du foie afin d'en délimiter la hauteur
> - [ ] **10. Palpation superficielle *(Néoplasie des voies biliaires/pancréatique)***
> 	- [ ] 4 quadrants
> 	- [ ] Contact visuel maintenu
> - [ ] **11. Évoque le toucher rectal *(Néoplasie des voies biliaires/pancréatique)***
> - [ ] **12. Palpation profonde *(Néoplasie des voies biliaires/pancréatique)***
> 	- [ ] 4 quadrants
> 	- [ ] Rate
> 	- [ ] Reins
> 	- [ ] Contact visuel maintenu
> 	- [ ] Foie
> - [ ] **13. Tests spécifiques *(Néoplasie des voies biliaires/pancréatique)***
> 	- [ ] Défense ET détente
> 	- [ ] Signe de Murphy

> [!success] 💊 Management — si Carcinome hépatocellulaire
> *Aucune grille du corpus ne documente ce diagnostic* — il est pourtant attendu de cette SSP. **Trou de révision à combler ailleurs.**

> [!success] 💊 Management — si Hépatite (virale/alcoolique)
> - [ ] **1. Diagnostic principal suspecté**
> - [ ] **2. Diagnostics différentiels**
> - [ ] **3. Examens biologiques de première intention**
> 	- [ ] Bilan hépatique complet (ASAT, ALAT, GGT, PAL, bilirubine totale/conjuguée)
> 	- [ ] FSC, plaquettes
> 	- [ ] TP, TCA (fonction hépatique)
> 	- [ ] Créatinine, ionogramme
> - [ ] **4. Sérologies virales**
> 	- [ ] IgM anti-VHA
> 	- [ ] Ag HBs, Ac anti-HBc IgM
> 	- [ ] Ac anti-VHC
> 	- [ ] Ac anti-VHE si indiqué
> - [ ] **5. Examens d'imagerie**
> 	- [ ] Échographie abdominale
> 	- [ ] Recherche de lithiase
> 	- [ ] Évaluation du parenchyme hépatique
> 	- [ ] Voies biliaires
> - [ ] **6. Prise en charge thérapeutique**
> - [ ] **7. Critères d'hospitalisation**
> 	- [ ] TP < 50%
> 	- [ ] Encéphalopathie hépatique
> 	- [ ] Vomissements incoercibles
> 	- [ ] Contexte social défavorable
> 	- [ ] Doute diagnostique
> - [ ] **8. Suivi et pronostic**
> 	- [ ] Contrôle biologique à 1 semaine
> 	- [ ] Normalisation attendue en 4-6 semaines
> 	- [ ] Guérison complète habituelle pour hépatite A
> 	- [ ] Vaccination ultérieure hépatites A et B
> - [ ] **9. Information du patient**
> 	- [ ] Explication du diagnostic probable
> 	- [ ] Évolution favorable habituelle
> 	- [ ] Mesures d'hygiène
> 	- [ ] Arrêt de travail nécessaire
> 	- [ ] Signes d'alarme à surveiller

> [!success] 💊 Management — si Ictère du nouveau-né
> *Aucune grille du corpus ne documente ce diagnostic* — il est pourtant attendu de cette SSP. **Trou de révision à combler ailleurs.**

> [!success] 💊 Management — si Néoplasie des voies biliaires/pancréatique
> - [ ] **1. Évoque le diagnostic principal de néoplasie des voies biliaires/pancréatique**
> - [ ] **2. Évoque un diagnostic différentiel cohérent**
> 	- [ ] Néoplasie pancréatique
> 	- [ ] Cholangite/cholecystite
> 	- [ ] Pancréatite
> 	- [ ] Hépatite
> 	- [ ] Hémolyse
> - [ ] **3. Propose des examens complémentaires appropriés**
> 	- [ ] Laboratoire (bilirubine totale et directe, transaminases, PAL, GGT)
> 	- [ ] Échographie abdominale
> 	- [ ] CT abdominale avec contraste
> 	- [ ] CPRE/cholangio-IRM si indiqué
> - [ ] **4. Informe la patiente de l'hypothèse diagnostique**
> 	- [ ] Explique la suspicion de problème au niveau du foie/voies biliaires
> 	- [ ] Mentionne la nécessité d'examens complémentaires
