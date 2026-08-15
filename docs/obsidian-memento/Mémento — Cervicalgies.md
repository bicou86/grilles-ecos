---
aliases:
  - "Mémento Cervicalgies"
type: memento-ecos-ssp
ssp: "Cervicalgies"
specialite: "Musculo-Squelettique"
cas: 1
diagnostics: 1
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

# Cervicalgies

*Musculo-Squelettique · 1 grille · 1 diagnostic documenté · 1 attendu documenté ailleurs · 1 attendu absent du corpus* — [[SSP — Cervicalgies]]

> [!abstract] La seule grille de cette SSP
> - **AZYGOS-18** — Radiculopathie cervicale C6 `diagnostic-travail` · [grille](<file:///Users/damienfulliquet/Developer/GitHub/grilles-ecos/.azygos-extraction/9eb8cf72-3d4f-427a-82f1-d538d46c91d0.json>)

> [!note] 📋 Anamnèse
> - [ ] **1. Question initiale sur l’évolution**
> - [ ] **2. Degré de sévérité de l’évolution de la douleur**
> - [ ] **3. Localisation et irradiation de la douleur**
> - [ ] **4. Qualité de la douleur**
> - [ ] **5. Facteurs déclenchants**
> - [ ] **6. Mesures prises jusqu’ici**
> - [ ] **7. Progression des symptômes neurologiques**
> - [ ] **8. Trouble de la sensibilité – évolution**
> - [ ] **9. Trouble de la sensibilité – localisation**
> - [ ] **10. Symptômes moteurs**
> - [ ] **11. Limitation fonctionnelle**
> - [ ] **12. Trouble vésico-sphinctérien**
> - [ ] **13. Trouble de la marche**
> - [ ] **14. Symptômes bilatéraux**
> - [ ] **15. Antécédents**
> - [ ] **16. Opérations antérieures**
> - [ ] **17. Médication actuelle**
> - [ ] **18. Noxes**
> - [ ] **19. Tabagisme**
> - [ ] **20. Alcool**
> - [ ] **21. Anamnèse familiale**
> - [ ] **22. Profession / charge**
> - [ ] **23. Situation de logement et au quotidien**

> [!tip] 🩺 Status
> - [ ] **1. Inspection du rachis cervical**
> - [ ] **2. Mobilité du rachis cervical évaluée**
> - [ ] **3. Test de Spurling**
> - [ ] **4. Motricité**
> - [ ] **5. C5 Abduction de l’épaule, des deux côtés**
> - [ ] **6. C6 Flexion du coude, des deux côtés**
> - [ ] **7. C6 Extension du poignet, des deux côtés**
> - [ ] **8. C7 Extension du coude, des deux côtés**
> - [ ] **9. C8–Th1 Écartement des doigts et abduction de l’auriculaire**
> - [ ] **10. Test de sensibilité selon les dermatomes**
> - [ ] **11. C5**
> - [ ] **12. C6 Sensibilité au niveau de l’avant-bras radial**
> - [ ] **13. C6 Sensibilité au niveau du pouce et du bord radial de l’index**
> - [ ] **14. C7**
> - [ ] **15. C8**
> - [ ] **16. Th1**
> - [ ] **17. Réflexe bicipital (BSR) des deux côtés**
> - [ ] **18. Réflexe brachioradial (BRR) des deux côtés**
> - [ ] **19. Réflexe tricipital (TSR) des deux côtés**
> - [ ] **20. Signes pyramidaux (Babinski) des deux côtés**
> - [ ] **21. Démarche**
> - [ ] **22. Anomalies bilatérales exclues**

> [!success] 💊 Management — si Cervicalgie
> *Aucune grille du corpus ne documente ce diagnostic* — il est pourtant attendu de cette SSP. **Trou de révision à combler ailleurs.**

> [!success] 💊 Management — si Hernie discale
> *Aucune grille de cette SSP ne documente ce diagnostic* — mais le corpus le documente ailleurs : [[Mémento — Lombalgies]] (2 grilles) · « Neuropathie Périphérique » (1 grille, hors lot).

> [!success] 💊 Management — si Radiculopathie cervicale C6
> - [ ] **1. Diagnostic de travail**
> - [ ] **2. Progression neurologique**
> - [ ] **3. Degré d’urgence**
> - [ ] **4. Information sur le diagnostic de travail**
> - [ ] **5. Analgésie de soutien**
> - [ ] **6. IRM du rachis cervical**
> - [ ] **7. Orientation neurochirurgicale**
> - [ ] **8. Filet de sécurité**
