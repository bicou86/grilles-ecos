---
aliases:
  - "Mémento Prurit"
type: memento-ecos-ssp
ssp: "Prurit"
specialite: "Médecine Interne"
cas: 1
diagnostics: 1
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

# Prurit

*Médecine Interne · 1 grille · 1 diagnostic documenté · 2 attendus absents du corpus* — [[SSP — Prurit]]

> [!abstract] La seule grille de cette SSP
> - **RESCOS-56** — Ictère obstructif `confirme` · [grille](<file:///Users/damienfulliquet/Developer/GitHub/grilles-ecos/cases/rescos/RESCOS-56%20-%20Prurit%20-%20Grille%20ECOS.html>)

> [!note] 📋 Anamnèse
> - [ ] **1. Motif de consultation**
> - [ ] **2. Caractérisation de l'ictère**
> 	- [ ] Début
> 	- [ ] Prurit généralisé
> 	- [ ] Urines foncées
> 	- [ ] Selles décolorées
> 	- [ ] Coloration jaune
> 	- [ ] Évolution progressive
> - [ ] **3. Symptômes associés**
> 	- [ ] Prurit intense
> 	- [ ] Perte pondérale
> 	- [ ] Anorexie
> 	- [ ] Vagues douleurs épigastriques
> - [ ] **4. Antécédents personnels**
> 	- [ ] Cholécystectomie
> 	- [ ] Calculs biliaires antérieurs
> - [ ] **5. Habitudes et toxiques**
> 	- [ ] Consommation d'alcool
> 	- [ ] Tabagisme
> 	- [ ] Médicaments hépatotoxiques
> 	- [ ] Compléments alimentaires
> 	- [ ] Drogues illicites
> - [ ] **6. Antécédents familiaux**
> 	- [ ] Cancer digestif dans la famille
> 	- [ ] Pathologies hépatiques héréditaires
> 	- [ ] Maladies auto-immunes
> - [ ] **7. Revue des systèmes**
> 	- [ ] Pas de méléna
> 	- [ ] Pas d'hématémèse
> 	- [ ] Pas de rectorragies
> 	- [ ] Transit intestinal normal
> 	- [ ] Pas de troubles urinaires
> 	- [ ] Pas de dyspnée

> [!tip] 🩺 Status
> - [ ] **1. Inspection générale**
> 	- [ ] Ictère cutanéo-muqueux franc
> 	- [ ] Sclérotiques ictériques
> 	- [ ] Excoriations cutanées
> 	- [ ] État général
> 	- [ ] Pas d'angiomes stellaires
> 	- [ ] Pas d'érythrose palmaire
> - [ ] **2. Signes vitaux**
> 	- [ ] Tension artérielle
> 	- [ ] Fréquence cardiaque
> 	- [ ] Température
> 	- [ ] Fréquence respiratoire
> 	- [ ] Saturation O2
> 	- [ ] Poids actuel et évolution
> - [ ] **3. Examen abdominal - Inspection**
> 	- [ ] Morphologie générale
> 	- [ ] Symétrie
> 	- [ ] Cicatrices
> 	- [ ] Hernies visibles
> 	- [ ] Veines superficielles
> 	- [ ] Mouvements respiratoires
> - [ ] **4. Auscultation abdominale**
> 	- [ ] Patience avant de conclure
> 	- [ ] Bruits intestinaux
> 	- [ ] Tonalité
> 	- [ ] Souffle vasculaire
> - [ ] **5. Percussion abdominale**
> 	- [ ] Matité hépatique
> 	- [ ] Flèche hépatique
> 	- [ ] Recherche d'ascite
> 	- [ ] Rate
> - [ ] **6. Palpation superficielle**
> 	- [ ] Main à plat, doigts serrés
> 	- [ ] Tonus pariétal spontané et en réponse à la pression
> 	- [ ] Douleur localisée
> 	- [ ] Défense
> 	- [ ] Contracture
> 	- [ ] Douleur à l'ébranlement
> - [ ] **7. Palpation profonde - Foie**
> 	- [ ] Position décubitus dorsal
> 	- [ ] Technique main postérieure loge rénale, main antérieure sous rebord costal
> 	- [ ] Inspiration profonde pour faire descendre le foie
> 	- [ ] Consistance
> 	- [ ] Surface
> 	- [ ] Bord inférieur
> - [ ] **8. Palpation profonde - Rate et autres**
> 	- [ ] Rate non palpable
> 	- [ ] Recherche de masse abdominale
> 	- [ ] Aorte
> 	- [ ] Vésicule biliaire
> 	- [ ] Points douloureux épigastriques
> - [ ] **9. Recherche de signes d'insuffisance hépatocellulaire**
> 	- [ ] Absence d'ascite
> 	- [ ] Pas d'angiomes stellaires
> 	- [ ] Pas d'érythrose palmaire
> 	- [ ] Pas d'ongles blancs
> 	- [ ] Pas de foetor hépatique
> 	- [ ] Pas d'encéphalopathie
> - [ ] **10. Recherche de signes d'hypertension portale**
> 	- [ ] Pas de splénomégalie
> 	- [ ] Pas de circulation collatérale abdominale
> 	- [ ] Pas d'ascite
> 	- [ ] Pas de gynécomastie
> 	- [ ] Pas d'atrophie testiculaire

> [!success] 💊 Management — si Eczéma / Dermatite
> *Aucune grille du corpus ne documente ce diagnostic* — il est pourtant attendu de cette SSP. **Trou de révision à combler ailleurs.**

> [!success] 💊 Management — si Ictère obstructif
> - [ ] **1. Diagnostics différentiels de l'ictère**
> - [ ] **2. Examens complémentaires de première intention**
> 	- [ ] Bilan hépatique complet: bilirubine totale et conjuguée
> 	- [ ] Transaminases (ALAT/ASAT)
> 	- [ ] Phosphatases alcalines (PAL) et Gamma-GT
> 	- [ ] Albumine, TP/INR
> 	- [ ] FSC: recherche anémie, hyperleucocytose
> 	- [ ] Lipase
> - [ ] **3. Imagerie biliaire**
> 	- [ ] Échographie abdominale en première intention
> 	- [ ] Dilatation des voies biliaires intra et extra-hépatiques
> 	- [ ] Recherche de calcul résiduel dans le cholédoque
> 	- [ ] Masse pancréatique ou péri-hilaire
> 	- [ ] État du parenchyme hépatique
> 	- [ ] CT abdominal avec injection
> 	- [ ] Meilleure visualisation des masses
> 	- [ ] Staging si néoplasie
> 	- [ ] Cholangio-IRM (cholangio-pancréatographie par résonance magnétique)
> 	- [ ] Visualisation non invasive de l'arbre biliaire
> 	- [ ] Localisation précise de l'obstacle
> - [ ] **4. Marqueurs tumoraux et examens spécialisés**
> 	- [ ] CA 19-9
> 	- [ ] ACE
> 	- [ ] Alpha-foetoprotéine
> 	- [ ] IgG4
> 	- [ ] CPRE diagnostique et thérapeutique
> 	- [ ] Sphinctérotomie si calcul
> 	- [ ] Pose de prothèse biliaire si sténose
> 	- [ ] Biopsies/brossage cytologique
> - [ ] **5. Traitement symptomatique du prurit**
> - [ ] **6. Surveillance et complications**
> - [ ] **7. Orientation et prise en charge**
> 	- [ ] Hospitalisation si angiocholite ou altération état général
> 	- [ ] Référence gastro-entérologie pour CPRE
> 	- [ ] Référence chirurgie si tumeur résécable
> 	- [ ] Référence oncologie si tumeur non résécable
> 	- [ ] Suivi rapproché si traitement ambulatoire
> 	- [ ] Supplémentation vitamines liposolubles (A,D,E,K)

> [!success] 💊 Management — si Urticaire
> *Aucune grille du corpus ne documente ce diagnostic* — il est pourtant attendu de cette SSP. **Trou de révision à combler ailleurs.**
