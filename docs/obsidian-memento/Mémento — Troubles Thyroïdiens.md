---
aliases:
  - "Mémento Troubles Thyroïdiens"
type: memento-ecos-ssp
ssp: "Troubles Thyroïdiens"
specialite: "Endocrinologie"
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

# Troubles Thyroïdiens

*Endocrinologie · 1 grille · 1 diagnostic documenté* — [[SSP — Troubles Thyroïdiens]]

> [!abstract] La seule grille de cette SSP
> - **AZYGOS-13** — Thyroïdite de De Quervain (thyroïdite granulomateuse subaiguë) `diagnostic-travail` · [grille](<file:///Users/damienfulliquet/Developer/GitHub/grilles-ecos/docs/azygos-grilles/fb6aa38c-15da-406b-becf-dff6a82912ab.json>)

> [!note] 📋 Anamnèse
> - [ ] **1. Question d’entrée**
> - [ ] **2. Dimension temporelle**
> - [ ] **3. Début / durée**
> - [ ] **4. Mode d’apparition**
> - [ ] **5. Évolution**
> - [ ] **6. Déclencheurs**
> - [ ] **7. Localisation**
> - [ ] **8. Irradiation**
> - [ ] **9. Qualité**
> - [ ] **10. Intensité / sévérité**
> - [ ] **11. Facteurs aggravants**
> - [ ] **12. Facteurs soulageants**
> - [ ] **13. Mesures antérieures**
> - [ ] **14. Retentissement des symptômes**
> - [ ] **15. Symptômes associés**
> - [ ] **16. Gonflement cervical / nodule**
> - [ ] **17. Cavité buccale / pharynx**
> - [ ] **18. Dysphagie**
> - [ ] **19. Ouverture buccale**
> - [ ] **20. Altération de la voix**
> - [ ] **21. Hypersalivation**
> - [ ] **22. Fièvre**
> - [ ] **23. Douleurs diffuses / myalgies**
> - [ ] **24. Fatigue / asthénie**
> - [ ] **25. Infection antérieure**
> - [ ] **26. Symptômes d’hyperthyroïdie**
> - [ ] **27. Palpitations**
> - [ ] **28. Sueurs / intolérance à la chaleur**
> - [ ] **29. Tremor**
> - [ ] **30. Nervosité / agitation intérieure**
> - [ ] **31. Perte de poids**
> - [ ] **32. Diarrhée**
> - [ ] **33. Symptômes d’hypothyroïdie**
> - [ ] **34. Intolérance au froid**
> - [ ] **35. Prise de poids**
> - [ ] **36. Constipation**
> - [ ] **37. Peau sèche / chute de cheveux**
> - [ ] **38. Apathie / humeur dépressive**
> - [ ] **39. Symptômes B**
> - [ ] **40. Troubles respiratoires**
> - [ ] **41. Dyspnée**
> - [ ] **42. Toux**
> - [ ] **43. Antécédents**
> - [ ] **44. Maladies de la thyroïde**
> - [ ] **45. Opérations antérieures**
> - [ ] **46. Médicaments**
> - [ ] **47. Allergies**
> - [ ] **48. Noxes**
> - [ ] **49. Alcool**
> - [ ] **50. Tabac**
> - [ ] **51. Drogues**
> - [ ] **52. Maladies thyroïdiennes familiales**
> - [ ] **53. Profession**
> - [ ] **54. Situation sociale**
> - [ ] **55. Facteurs de stress psychosociaux**

> [!tip] 🩺 Status
> - [ ] **1. Paramètres vitaux**
> - [ ] **2. Inspection du cou**
> - [ ] **3. Palpation du cou**
> - [ ] **4. Thyroïde**
> - [ ] **5. Mobilité à la déglutition**
> - [ ] **6. Ganglions cervicaux**
> - [ ] **7. Auscultation de la thyroïde**
> - [ ] **8. Cavité buccale / pharynx**
> - [ ] **9. Signes d’hyperthyroïdie**
> - [ ] **10. Inspection des mains**
> - [ ] **11. Aspect cutané**
> - [ ] **12. Réflexes**
> - [ ] **13. Cœur**
> - [ ] **14. Poumons**

> [!success] 💊 Management — si Thyroïdite de De Quervain (thyroïdite granulomateuse subaiguë)
> - [ ] **1. Laboratoire**
> - [ ] **2. Hémogramme**
> - [ ] **3. Fonction thyroïdienne**
> - [ ] **4. Paramètres inflammatoires**
> - [ ] **5. Anticorps thyroïdiens**
> - [ ] **6. Échographie de la thyroïde**
> - [ ] **7. ECG**
> - [ ] **8. Diagnostic de travail**
> - [ ] **9. Traitement symptomatique de la douleur**
> - [ ] **10. Traitement symptomatique de l’hyperthyroïdie**
> - [ ] **11. Pas d’antithyroïdiens de synthèse**
> - [ ] **12. Glucocorticoïdes**
> - [ ] **13. Instructions**
> - [ ] **14. Hydratation suffisante**
> - [ ] **15. Éviter la caféine**
> - [ ] **16. Pas de suppléments iodés**
> - [ ] **17. Suivi**
> - [ ] **18. Filet de sécurité**
