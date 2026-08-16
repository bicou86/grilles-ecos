---
aliases:
  - "Mémento Dysphonie"
type: memento-ecos-ssp
ssp: "Dysphonie"
specialite: "ORL"
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

# Dysphonie

*ORL · 1 grille · 1 diagnostic documenté* — [[SSP — Dysphonie]]

> [!abstract] La seule grille de cette SSP
> - **AZYGOS-24** — Suspicion de carcinome glottique `diagnostic-travail` · [grille](<file:///Users/damienfulliquet/Developer/GitHub/grilles-ecos/docs/azygos-grilles/95e8b791-ccf9-4b76-aacc-cd67d1ed3ea9.json>)

> [!note] 📋 Anamnèse
> - [ ] **1. Question d’ouverture**
> - [ ] **2. Dimension temporelle**
> - [ ] **3. Début / durée**
> - [ ] **4. Déclencheur**
> - [ ] **5. Évolution**
> - [ ] **6. Intensité / gravité**
> - [ ] **7. Facteurs aggravants**
> - [ ] **8. Facteurs soulageants**
> - [ ] **9. Mesures prises jusqu’ici**
> - [ ] **10. Retentissement des symptômes**
> - [ ] **11. Symptômes associés**
> - [ ] **12. Charge vocale**
> - [ ] **13. Sensation de globe**
> - [ ] **14. Troubles de la déglutition**
> - [ ] **15. Dysphagie**
> - [ ] **16. Odynophagie**
> - [ ] **17. Fausses routes répétées**
> - [ ] **18. Dyspnée**
> - [ ] **19. Hémoptysie**
> - [ ] **20. Otalgie**
> - [ ] **21. Tuméfaction cervicale**
> - [ ] **22. Symptômes généraux**
> - [ ] **23. Symptômes B**
> - [ ] **24. Reflux**
> - [ ] **25. Goutte post-nasale**
> - [ ] **26. Antécédents**
> - [ ] **27. Anamnèse tumorale**
> - [ ] **28. Antécédents chirurgicaux**
> - [ ] **29. Médicaments**
> - [ ] **30. Noxes**
> - [ ] **31. Tabac**
> - [ ] **32. Alcool**
> - [ ] **33. Drogues**
> - [ ] **34. Allergies**
> - [ ] **35. Antécédents familiaux**
> - [ ] **36. Profession**
> - [ ] **37. Situation sociale**

> [!tip] 🩺 Status
> - [ ] **1. Inspection**
> - [ ] **2. Auscultation**
> - [ ] **3. Larynx / trachée**
> - [ ] **4. Poumons**
> - [ ] **5. Cavité buccale / vestibule**
> - [ ] **6. Oropharynx**
> - [ ] **7. Nerfs crâniens**
> - [ ] **8. Glossopharyngien / vague (IX, X)**
> - [ ] **9. Hypoglosse (XII)**
> - [ ] **10. Palpation**
> - [ ] **11. Plancher buccal / base de la langue**
> - [ ] **12. Réalisation de la laryngoscopie au miroir**
> - [ ] **13. Information du patient et positionnement**
> - [ ] **14. Lampe frontale**
> - [ ] **15. Chauffer le miroir**
> - [ ] **16. Saisir la langue**
> - [ ] **17. Introduire le miroir**
> - [ ] **18. Test de phonation**
> - [ ] **19. Résultat de la laryngoscopie**
> - [ ] **20. Ganglions lymphatiques**
> - [ ] **21. Thyroïde**
> - [ ] **22. Larynx**

> [!success] 💊 Management — si Suspicion de carcinome glottique
> - [ ] **1. Diagnostic présumé**
> - [ ] **2. Classement DD**
> - [ ] **3. Orientation en clinique ORL**
> - [ ] **4. Examens complémentaires**
> - [ ] **5. Vidéolaryngoscopie**
> - [ ] **6. Biopsie**
> - [ ] **7. Arrêt du tabac**
> - [ ] **8. Filet de sécurité**
