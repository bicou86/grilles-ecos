---
aliases:
  - "Mémento Détresse Respiratoire (Adulte-Enfant non-néonatal)"
type: memento-ecos-ssp
ssp: "Détresse Respiratoire (Adulte-Enfant non-néonatal)"
specialite: "Urgences Vitales"
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

# Détresse Respiratoire (Adulte-Enfant non-néonatal)

*Urgences Vitales · 1 grille · 1 diagnostic documenté* — [[SSP — Détresse Respiratoire (Adulte-Enfant non-néonatal)]]

> [!abstract] La seule grille de cette SSP
> - **AZYGOS-43** — Pseudo-croup `diagnostic-travail` · [grille](<file:///Users/damienfulliquet/Developer/GitHub/grilles-ecos/docs/azygos-grilles/66bc18ac-f27d-4e48-8fd1-6a685990bc20.json>)

> [!note] 📋 Anamnèse
> - [ ] **1. Identification du/de la patient·e (nom, âge)**
> - [ ] **2. Numéro de rappel**
> - [ ] **3. Question d’entrée**
> - [ ] **4. Dimension temporelle**
> - [ ] **5. Début / durée**
> - [ ] **6. Mode d’apparition**
> - [ ] **7. Évolution**
> - [ ] **8. Déclencheur infectieux / anamnèse de l’environnement**
> - [ ] **9. Facteurs aggravants / contexte de survenue**
> - [ ] **10. Facteurs soulageants**
> - [ ] **11. Mesures prises / tentatives de traitement**
> - [ ] **12. Retentissement des symptômes**
> - [ ] **13. Symptômes associés**
> - [ ] **14. État général**
> - [ ] **15. Évaluation de l’état général par la personne de référence**
> - [ ] **16. Vigilance / capacité d’interaction**
> - [ ] **17. Capacité à boire**
> - [ ] **18. Situation respiratoire**
> - [ ] **19. Tachypnée**
> - [ ] **20. Tirages / travail respiratoire**
> - [ ] **21. Stridor / bruit respiratoire**
> - [ ] **22. Cyanose**
> - [ ] **23. Hypersalivation / trouble de déglutition**
> - [ ] **24. Fortes douleurs pharyngées / à la déglutition**
> - [ ] **25. Modification de la voix**
> - [ ] **26. Fièvre**
> - [ ] **27. Toux**
> - [ ] **28. Caractère aboyant**
> - [ ] **29. Expectoration**
> - [ ] **30. Rhinorrhée**
> - [ ] **31. Événement d’aspiration**
> - [ ] **32. Brûlure chimique / ébouillantement**
> - [ ] **33. Réaction allergique / angio-œdème**
> - [ ] **34. Éruption cutanée**
> - [ ] **35. Gonflement du visage**
> - [ ] **36. Déclencheur allergique**
> - [ ] **37. Maladies respiratoires connues / symptômes respiratoires**
> - [ ] **38. Médicaments**
> - [ ] **39. Noxes**
> - [ ] **40. Fumée passive**
> - [ ] **41. Allergies**
> - [ ] **42. Vaccinations**
> - [ ] **43. Anamnèse pédiatrique complémentaire**
> - [ ] **44. Grossesse**
> - [ ] **45. Accouchement / période néonatale**
> - [ ] **46. Développement**
> - [ ] **47. Antécédents familiaux / maladies respiratoires**
> - [ ] **48. Environnement / circonstances sociales**

> [!success] 💊 Management — si Pseudo-croup
> - [ ] **1. Diagnostic de travail**
> - [ ] **2. Obstruction des voies respiratoires supérieures**
> - [ ] **3. Pseudo-croup**
> - [ ] **4. Triage téléphonique**
> - [ ] **5. Instruction**
> - [ ] **6. Calmer l’enfant, éviter l’agitation**
> - [ ] **7. Antipyrèse au besoin**
> - [ ] **8. Faisabilité**
> - [ ] **9. Évaluation médicale**
> - [ ] **10. Filet de sécurité**
