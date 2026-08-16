---
aliases:
  - "Mémento Syncope"
type: memento-ecos-ssp
ssp: "Syncope"
specialite: "Cardiologie & Vasculaire"
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

# Syncope

*Cardiologie & Vasculaire · 1 grille · 1 diagnostic documenté* — [[SSP — Syncope]]

> [!abstract] La seule grille de cette SSP
> - **AZYGOS-46** — Syncope avec suspicion d’origine arythmogène (syndrome de Brugada) `diagnostic-travail` · [grille](<file:///Users/damienfulliquet/Developer/GitHub/grilles-ecos/docs/azygos-grilles/0621c04a-0d48-4b2e-bb2f-7a87487f2115.json>)

> [!note] 📋 Anamnèse
> - [ ] **1. Question initiale**
> - [ ] **2. Moment**
> - [ ] **3. Déroulement (hétéro-anamnèse)**
> - [ ] **4. Mécanisme de chute**
> - [ ] **5. Durée**
> - [ ] **6. Secousses / crampes**
> - [ ] **7. Déviation oculaire**
> - [ ] **8. Réorientation**
> - [ ] **9. Choc cranien**
> - [ ] **10. Activité immédiatement avant la perte de connaissance**
> - [ ] **11. Déclencheurs / triggers**
> - [ ] **12. Orthostatisme / changement de position**
> - [ ] **13. Déclencheurs situationnels (toux / éternuement / déglutition)**
> - [ ] **14. Déclencheurs vasovagaux (émotion / excitation / douleur)**
> - [ ] **15. Temps d’avertissement**
> - [ ] **16. Prodromes**
> - [ ] **17. Vertiges / étourdissements**
> - [ ] **18. Visuel (voile noir / tunnel / scintillement)**
> - [ ] **19. Auditif (sourd / bourdonnement)**
> - [ ] **20. Végétatif (nausées / sueurs / sensation de chaleur)**
> - [ ] **21. Symptômes accompagnants**
> - [ ] **22. Syncopes / présyncopes antérieures**
> - [ ] **23. Symptômes thoraciques (actuels / péri-syncope / à l’effort)**
> - [ ] **24. Douleurs thoraciques / oppression**
> - [ ] **25. Dyspnée**
> - [ ] **26. Palpitations**
> - [ ] **27. Douleurs liées à la chute**
> - [ ] **28. Gonflement / douleur des jambes**
> - [ ] **29. Symptômes infectieux / généraux**
> - [ ] **30. Fièvre / température**
> - [ ] **31. Anamnèse d’infection**
> - [ ] **32. Voies respiratoires supérieures (maux de gorge / rhume)**
> - [ ] **33. Voies respiratoires inférieures (toux / expectoration)**
> - [ ] **34. Céphalées / raideur de nuque**
> - [ ] **35. Myalgies**
> - [ ] **36. Anamnèse environnementale**
> - [ ] **37. DD Symptômes neurologiques**
> - [ ] **38. Morsure de langue**
> - [ ] **39. Perte d’urines / selles**
> - [ ] **40. Symptômes neurologiques focaux**
> - [ ] **41. Longs voyages / immobilisation**
> - [ ] **42. Antécédents médicaux**
> - [ ] **43. Antécédents généraux**
> - [ ] **44. Antécédents cardiaques / troubles du rythme**
> - [ ] **45. Antécédents chirurgicaux**
> - [ ] **46. Médicaments**
> - [ ] **47. Allergies**
> - [ ] **48. Noxes**
> - [ ] **49. Alcool**
> - [ ] **50. Tabagisme**
> - [ ] **51. Drogues / stimulants**
> - [ ] **52. Antécédents familiaux**
> - [ ] **53. Maladies familiales générales**
> - [ ] **54. Mort subite cardiaque dans la famille**
> - [ ] **55. Profession**
> - [ ] **56. Situation sociale**

> [!tip] 🩺 Status
> - [ ] **1. Inspection des conséquences de la chute**
> - [ ] **2. Bouche / pharynx**
> - [ ] **3. Ganglions cervicaux**
> - [ ] **4. Inspection**
> - [ ] **5. Peau / muqueuses**
> - [ ] **6. Mains**
> - [ ] **7. Thorax / travail respiratoire / cicatrices**
> - [ ] **8. Signes de stase**
> - [ ] **9. Turgescence jugulaire**
> - [ ] **10. Œdèmes périphériques**
> - [ ] **11. Reflux hépato-jugulaire**
> - [ ] **12. Perfusion périphérique / pouls**
> - [ ] **13. Auscultation**
> - [ ] **14. Auscultation cardiaque**
> - [ ] **15. Auscultation des carotides**
> - [ ] **16. Test de Schellong**
> - [ ] **17. Auscultation pulmonaire**
> - [ ] **18. Conscience / orientation**
> - [ ] **19. Meningisme**
> - [ ] **20. Nerfs crâniens (orientation)**
> - [ ] **21. Motricité**
> - [ ] **22. Épreuve des bras tendus**
> - [ ] **23. Épreuve des jambes tendues**
> - [ ] **24. Coordination**
> - [ ] **25. Doigt-nez**
> - [ ] **26. Talon-genou**
> - [ ] **27. Romberg**
> - [ ] **28. Sensibilité**

> [!success] 💊 Management — si Syncope avec suspicion d’origine arythmogène (syndrome de Brugada)
> - [ ] **1. Laboratoire**
> - [ ] **2. Troponine (hs)**
> - [ ] **3. ECG 12 dérivations**
> - [ ] **4. Diagnostic de travail**
> - [ ] **5. Antipyrèse**
> - [ ] **6. Hospitalisation**
> - [ ] **7. Monitoring / télémétrie**
> - [ ] **8. Avis de cardiologie**
