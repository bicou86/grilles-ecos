---
aliases:
  - "Mémento Rhinosinusite"
type: memento-ecos-ssp
ssp: "Rhinosinusite"
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

# Rhinosinusite

*1 grille · 1 diagnostic documenté* — [[SSP — Rhinosinusite]]

> [!abstract] La seule grille de cette SSP
> - **AZYGOS-36** — Rhinosinusite post-virale `diagnostic-travail` · [grille](<file:///Users/damienfulliquet/Developer/GitHub/grilles-ecos/docs/azygos-grilles/f0fbf3ec-d0b2-4c9b-ae46-56ddbfb96c24.json>)

> [!note] 📋 Anamnèse
> - [ ] **1. Question initiale**
> - [ ] **2. Dimension temporelle**
> - [ ] **3. Début / Durée**
> - [ ] **4. Apparition / Facteur déclenchant**
> - [ ] **5. Évolution**
> - [ ] **6. Épisodes**
> - [ ] **7. Localisation**
> - [ ] **8. Facteurs soulageants**
> - [ ] **9. Mesures déjà prises**
> - [ ] **10. Facteurs aggravants**
> - [ ] **11. Retentissement des symptômes**
> - [ ] **12. Symptômes d'accompagnement**
> - [ ] **13. Trouble de l'odorat**
> - [ ] **14. Rhinorrhée**
> - [ ] **15. Qualité (aqueuse / muqueuse / sanglante)**
> - [ ] **16. Antécédent de traumatisme nasal**
> - [ ] **17. Douleur faciale**
> - [ ] **18. Aggravation lors de la flexion**
> - [ ] **19. Rhinorrhée postérieure**
> - [ ] **20. Symptômes B**
> - [ ] **21. Fièvre**
> - [ ] **22. Signes de méningisme**
> - [ ] **23. Maux de tête / Raideur de la nuque**
> - [ ] **24. Photophobie**
> - [ ] **25. Déficits neurologiques**
> - [ ] **26. Troubles de la parole**
> - [ ] **27. Paralysies**
> - [ ] **28. Troubles de la sensibilité**
> - [ ] **29. Troubles de la marche**
> - [ ] **30. Symptômes oculaires**
> - [ ] **31. Diplopie**
> - [ ] **32. Baisse de l'acuité visuelle**
> - [ ] **33. Perception du rouge**
> - [ ] **34. Symptômes auriculaires / auditifs**
> - [ ] **35. Voies respiratoires**
> - [ ] **36. Maux de gorge**
> - [ ] **37. Toux**
> - [ ] **38. Dyspnée**
> - [ ] **39. Antécédents médicaux**
> - [ ] **40. Antécédents chirurgicaux**
> - [ ] **41. Anamnèse médicamenteuse**
> - [ ] **42. Toxiques**
> - [ ] **43. Alcool**
> - [ ] **44. Tabagisme**
> - [ ] **45. Drogues**
> - [ ] **46. Allergies**
> - [ ] **47. Antécédents familiaux**
> - [ ] **48. Profession**

> [!tip] 🩺 Status
> - [ ] **1. Inspection**
> - [ ] **2. Forme externe**
> - [ ] **3. Soulever la pointe du nez**
> - [ ] **4. Respiration nasale**
> - [ ] **5. Palpation**
> - [ ] **6. Nez**
> - [ ] **7. Sinus paranasaux**
> - [ ] **8. Rhinoscopie**
> - [ ] **9. Rhinoscopie antérieure**
> - [ ] **10. Rhinoscopie postérieure**
> - [ ] **11. Otoscopie y compris manœuvre de Valsalva**
> - [ ] **12. Palpation des ganglions lymphatiques**
> - [ ] **13. Statut oculaire**
> - [ ] **14. Réflexe pupillaire**
> - [ ] **15. Acuité visuelle**
> - [ ] **16. Saturation du rouge**
> - [ ] **17. Oculomotricité**
> - [ ] **18. Nerf trijumeau**
> - [ ] **19. Sensibilité**
> - [ ] **20. Points d'émergence**
> - [ ] **21. Examen du nerf facial**

> [!success] 💊 Management — si Rhinosinusite post-virale
> - [ ] **1. Diagnostic de travail**
> - [ ] **2. Spray nasal de glucocorticoïde**
> - [ ] **3. Sécrétolytique d'origine végétale**
> - [ ] **4. Mesures adjuvantes**
> - [ ] **5. Lavage nasal**
> - [ ] **6. Inhalation**
> - [ ] **7. Housses anti-acariens**
> - [ ] **8. Contrôle d'évolution**
> - [ ] **9. Filet de sécurité**
