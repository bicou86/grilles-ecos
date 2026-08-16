---
aliases:
  - "Mémento Perte de Poids Involontaire"
type: memento-ecos-ssp
ssp: "Perte de Poids Involontaire"
specialite: "Médecine Interne"
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

# Perte de Poids Involontaire ⭐️

*Médecine Interne · 1 grille · 1 diagnostic documenté* — [[SSP — Perte de Poids Involontaire]]

> [!abstract] La seule grille de cette SSP
> - **AZYGOS-39** — Anorexie mentale, type restrictif (DSM-5 / CIM-11) `diagnostic-travail` · [grille](<file:///Users/damienfulliquet/Developer/GitHub/grilles-ecos/docs/azygos-grilles/66feb4ea-b8a5-4251-9eab-5d90ec80a1cd.json>)

> [!note] 📋 Anamnèse
> - [ ] **1. Question initiale**
> - [ ] **2. Dimension temporelle**
> - [ ] **3. Début / durée**
> - [ ] **4. Évolution / dynamique du trouble alimentaire**
> - [ ] **5. Déclencheurs**
> - [ ] **6. Changement de vie**
> - [ ] **7. Réseaux sociaux**
> - [ ] **8. Mesures antérieures**
> - [ ] **9. Symptômes associés**
> - [ ] **10. Comportement alimentaire**
> - [ ] **11. Évolution pondérale**
> - [ ] **12. Ampleur / dynamique**
> - [ ] **13. Volontaire vs. involontaire**
> - [ ] **14. Image corporelle / dysmorphophobie corporelle**
> - [ ] **15. Dysmorphophobie corporelle**
> - [ ] **16. Peur de prendre du poids**
> - [ ] **17. Estime de soi dépendante du poids**
> - [ ] **18. Insight de la maladie / motivation thérapeutique**
> - [ ] **19. Anamnèse menstruelle**
> - [ ] **20. Instabilité circulatoire (vertiges / syncope)**
> - [ ] **21. Accès hyperphagiques (binge-eating)**
> - [ ] **22. Mesures compensatoires / purge**
> - [ ] **23. Vomissements auto-induits**
> - [ ] **24. Abus de laxatifs / diurétiques**
> - [ ] **25. Sport excessif / besoin de bouger**
> - [ ] **26. DD somatiques de la perte pondérale**
> - [ ] **27. Hyperthyroïdie**
> - [ ] **28. Diabète sucré**
> - [ ] **29. Maladie inflammatoire chronique de l’intestin / malabsorption**
> - [ ] **30. Malignité / infection chronique**
> - [ ] **31. Complications / conséquences de la dénutrition**
> - [ ] **32. Frilosité / sensation de froid**
> - [ ] **33. Fatigue / capacité réduite à l’effort**
> - [ ] **34. Altérations cutanées trophiques**
> - [ ] **35. Constipation**
> - [ ] **36. Plaintes cognitives**
> - [ ] **37. Antécédents**
> - [ ] **38. Antécédents somatiques**
> - [ ] **39. Antécédents psychiatriques**
> - [ ] **40. Médicaments**
> - [ ] **41. Noxes**
> - [ ] **42. Alcool**
> - [ ] **43. Tabagisme**
> - [ ] **44. Drogues**
> - [ ] **45. Antécédents familiaux**
> - [ ] **46. Troubles alimentaires dans la famille**
> - [ ] **47. Maladies psychiatriques dans la famille**
> - [ ] **48. Maladies somatiques dans la famille**
> - [ ] **49. Profession**
> - [ ] **50. Situation sociale**
> - [ ] **51. Facteurs de maintien**

> [!tip] 🩺 Status
> - [ ] **1. Énergie / psychomotricité**
> - [ ] **2. Affect / humeur**
> - [ ] **3. Symptômes obsessionnels**
> - [ ] **4. Suicidalité / automutilation**
> - [ ] **5. Paramètres vitaux**
> - [ ] **6. IMC / morphotype**
> - [ ] **7. Inspection peau & cheveux**
> - [ ] **8. Statut interniste**
> - [ ] **9. Cardiaque**
> - [ ] **10. Pulmonaire**
> - [ ] **11. Abdomen**
> - [ ] **12. Neurologique orientant**

> [!success] 💊 Management — si Anorexie mentale, type restrictif (DSM-5 / CIM-11)
> - [ ] **1. Laboratoire de base**
> - [ ] **2. Hémogramme**
> - [ ] **3. Électrolytes (incl. phosphate, magnésium)**
> - [ ] **4. Glycémie**
> - [ ] **5. Fonctions hépatiques (ALT, AST)**
> - [ ] **6. Endocrinologie**
> - [ ] **7. Bilan thyroïdien (TSH, fT3)**
> - [ ] **8. Bilan hormonal (LH, FSH, œstradiol)**
> - [ ] **9. Test de grossesse**
> - [ ] **10. Β-hCG**
> - [ ] **11. ECG**
> - [ ] **12. Test de Schellong**
> - [ ] **13. Diagnostic présumé**
> - [ ] **14. Raisonnement clinique**
> - [ ] **15. Consignes / information du patient**
> - [ ] **16. Thérapie multimodale**
> - [ ] **17. Prophylaxie du refeeding**
> - [ ] **18. Hospitalisation**
> - [ ] **19. Orientation vers un spécialiste**
> - [ ] **20. Filet de sécurité**
> - [ ] **21. Suivi**
