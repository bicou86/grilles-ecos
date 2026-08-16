---
aliases:
  - "Mémento Masse Mammaire"
type: memento-ecos-ssp
ssp: "Masse Mammaire"
specialite: "Gynéco-Obstétrique"
cas: 2
diagnostics: 2
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

# Masse Mammaire ⭐️

*Gynéco-Obstétrique · 2 grilles · 2 diagnostics documentés* — [[SSP — Masse Mammaire]]

> [!abstract] Les 2 grilles fusionnées
> - **AZYGOS-37** — Nodule suspect de malignité dans le sein droit `diagnostic-travail` · [grille](<file:///Users/damienfulliquet/Developer/GitHub/grilles-ecos/docs/azygos-grilles/8b69fbb3-93d0-4ecc-aa93-f1fcdee0c6e0.json>)
> - **German-62** — Masse mammaire suspecte de carcinome `corrige` · [grille](<file:///Users/damienfulliquet/Developer/GitHub/grilles-ecos/cases/german/German-62_-_Masse_mammaire_-_Grille_ECOS.html>)

> [!note] 📋 Anamnèse
> - [ ] **1. Question d’entrée *(Nodule suspect de malignité dans le sein droit)***
> - [ ] **2. Nodule *(Nodule suspect de malignité dans le sein droit)***
> - [ ] **3. Découverte *(Nodule suspect de malignité dans le sein droit)***
> - [ ] **4. Localisation *(Nodule suspect de malignité dans le sein droit)***
> - [ ] **5. Évolution de la taille *(Nodule suspect de malignité dans le sein droit)***
> - [ ] **6. Description *(Nodule suspect de malignité dans le sein droit)***
> - [ ] **7. Nombre et côté *(Nodule suspect de malignité dans le sein droit)***
> - [ ] **8. Douleurs mammaires *(Nodule suspect de malignité dans le sein droit)***
> - [ ] **9. Modifications cutanées et des mamelons *(Nodule suspect de malignité dans le sein droit)***
> - [ ] **10. Sécrétion mamelonnaire *(Nodule suspect de malignité dans le sein droit)***
> - [ ] **11. Anciens résultats mammaires *(Nodule suspect de malignité dans le sein droit)***
> - [ ] **12. Anamnèse reproductive *(Nodule suspect de malignité dans le sein droit)***
> - [ ] **13. Ménarche *(Nodule suspect de malignité dans le sein droit)***
> - [ ] **14. Ménopause *(Nodule suspect de malignité dans le sein droit)***
> - [ ] **15. Grossesses et allaitement *(Nodule suspect de malignité dans le sein droit)***
> - [ ] **16. Hormonothérapie *(Nodule suspect de malignité dans le sein droit)***
> - [ ] **17. Prévention et auto-examen *(Nodule suspect de malignité dans le sein droit)***
> - [ ] **18. Dernière mammographie *(Nodule suspect de malignité dans le sein droit)***
> - [ ] **19. Dernier contrôle gynécologique *(Nodule suspect de malignité dans le sein droit)***
> - [ ] **20. Auto-examen des seins *(Nodule suspect de malignité dans le sein droit)***
> - [ ] **21. Symptômes B *(Nodule suspect de malignité dans le sein droit)***
> - [ ] **22. Dépistage par système d’organes *(Nodule suspect de malignité dans le sein droit)***
> - [ ] **23. Douleurs osseuses *(Nodule suspect de malignité dans le sein droit)***
> - [ ] **24. Symptômes pulmonaires *(Nodule suspect de malignité dans le sein droit)***
> - [ ] **25. Symptômes neurologiques *(Nodule suspect de malignité dans le sein droit)***
> - [ ] **26. Symptômes abdominaux *(Nodule suspect de malignité dans le sein droit)***
> - [ ] **27. Antécédents *(Nodule suspect de malignité dans le sein droit)***
> - [ ] **28. Hypertension artérielle *(Nodule suspect de malignité dans le sein droit)***
> - [ ] **29. Antécédents oncologiques *(Nodule suspect de malignité dans le sein droit)***
> - [ ] **30. Médicaments *(Nodule suspect de malignité dans le sein droit)***
> - [ ] **31. Noxes *(Nodule suspect de malignité dans le sein droit)***
> - [ ] **32. Alcool *(Nodule suspect de malignité dans le sein droit)***
> - [ ] **33. Nicotine *(Nodule suspect de malignité dans le sein droit)***
> - [ ] **34. Allergies *(Nodule suspect de malignité dans le sein droit)***
> - [ ] **35. Cancers familiaux *(Nodule suspect de malignité dans le sein droit)***
> - [ ] **36. Carcinome mammaire *(Nodule suspect de malignité dans le sein droit)***
> - [ ] **37. Carcinome de l’ovaire *(Nodule suspect de malignité dans le sein droit)***
> - [ ] **38. Test génétique *(Nodule suspect de malignité dans le sein droit)***
> - [ ] **39. Autres maladies *(Nodule suspect de malignité dans le sein droit)***
> - [ ] **40. Anamnèse sociale**
> - [ ] **41. Profession *(Nodule suspect de malignité dans le sein droit)***
> - [ ] **42. Situation de logement *(Nodule suspect de malignité dans le sein droit)***
> - [ ] **43. Soutien *(Nodule suspect de malignité dans le sein droit)***
> - [ ] **44. Charge psychosociale *(Nodule suspect de malignité dans le sein droit)***
> - [ ] **45. Présentation avec nom, fonction et objectif *(Masse mammaire suspecte de carcinome)***
> - [ ] **46. Motif de consultation principal *(Masse mammaire suspecte de carcinome)***
> - [ ] **47. Caractéristiques du nodule *(Masse mammaire suspecte de carcinome)***
> 	- [ ] Date de découverte
> 	- [ ] Localisation précise
> 	- [ ] Taille
> 	- [ ] Consistance
> 	- [ ] Mobilité
> - [ ] **48. Symptômes associés *(Masse mammaire suspecte de carcinome)***
> 	- [ ] Douleurs mammaires
> 	- [ ] Écoulement mamelonnaire
> 	- [ ] Rougeur/chaleur locale
> 	- [ ] Infection récente
> 	- [ ] Symptômes B
> - [ ] **49. Anamnèse gynécologique *(Masse mammaire suspecte de carcinome)***
> 	- [ ] Ménarche
> 	- [ ] Statut ménopausique
> 	- [ ] Bouffées de chaleur
> 	- [ ] Troubles du sommeil
> 	- [ ] Évolution pondérale
> - [ ] **50. Anamnèse obstétricale *(Masse mammaire suspecte de carcinome)***
> 	- [ ] Nombre de grossesses
> 	- [ ] Nombre d'enfants
> 	- [ ] Fausses couches
> - [ ] **51. Activité sexuelle et contraception *(Masse mammaire suspecte de carcinome)***
> 	- [ ] Activité sexuelle actuelle
> 	- [ ] Contraception antérieure
> 	- [ ] Contraception actuelle
> - [ ] **52. Antécédents médicaux *(Masse mammaire suspecte de carcinome)***
> 	- [ ] Maladies mammaires antérieures
> 	- [ ] Maladies gynécologiques
> 	- [ ] Interventions chirurgicales
> - [ ] **53. Médication actuelle *(Masse mammaire suspecte de carcinome)***
> - [ ] **54. Habitudes de vie et allergies *(Masse mammaire suspecte de carcinome)***
> 	- [ ] Consommation de substances
> 	- [ ] Allergies connues
> 	- [ ] Habitudes alimentaires
> - [ ] **55. Antécédents familiaux *(Masse mammaire suspecte de carcinome)***
> 	- [ ] Antécédents parentaux
> 	- [ ] Cancer du sein familial
> 	- [ ] Mutation génétique connue

> [!tip] 🩺 Status
> - [ ] **1. Réalisation *(Nodule suspect de malignité dans le sein droit)***
> - [ ] **2. Bras le long du corps *(Nodule suspect de malignité dans le sein droit)***
> - [ ] **3. Mains derrière la tête *(Nodule suspect de malignité dans le sein droit)***
> - [ ] **4. Résultat de l’inspection *(Nodule suspect de malignité dans le sein droit)***
> - [ ] **5. Technique de palpation *(Nodule suspect de malignité dans le sein droit)***
> - [ ] **6. Palpation superficielle *(Nodule suspect de malignité dans le sein droit)***
> - [ ] **7. Palpation profonde *(Nodule suspect de malignité dans le sein droit)***
> - [ ] **8. Expression des mamelons *(Nodule suspect de malignité dans le sein droit)***
> - [ ] **9. Palpation du côté opposé *(Nodule suspect de malignité dans le sein droit)***
> - [ ] **10. Résultat concernant le nodule *(Nodule suspect de malignité dans le sein droit)***
> - [ ] **11. Palpation des ganglions *(Nodule suspect de malignité dans le sein droit)***
> - [ ] **12. Axillaires des deux côtés *(Nodule suspect de malignité dans le sein droit)***
> - [ ] **13. Sus-claviculaires des deux côtés *(Nodule suspect de malignité dans le sein droit)***
> - [ ] **14. Sous-claviculaires des deux côtés *(Nodule suspect de malignité dans le sein droit)***
> - [ ] **15. Résultat ganglionnaire *(Nodule suspect de malignité dans le sein droit)***
> - [ ] **16. Signes vitaux *(Masse mammaire suspecte de carcinome)***
> - [ ] **17. Examen des seins *(Masse mammaire suspecte de carcinome)***
> 	- [ ] Inspection en différentes positions
> 	- [ ] Palpation systématique des deux seins
> 	- [ ] Expression des mamelons
> - [ ] **18. Examen gynécologique mentionné *(Masse mammaire suspecte de carcinome)***
> - [ ] **19. Palpation des ganglions lymphatiques *(Masse mammaire suspecte de carcinome)***
> 	- [ ] Ganglions axillaires
> 	- [ ] Ganglions sus-claviculaires
> 	- [ ] Ganglions sous-claviculaires

> [!success] 💊 Management — si Masse mammaire suspecte de carcinome
> - [ ] **1. Diagnostic de suspicion**
> - [ ] **2. Diagnostics différentiels**
> - [ ] **3. Examens diagnostiques proposés**
> 	- [ ] Mammographie bilatérale
> 	- [ ] Échographie mammaire (US)
> 	- [ ] Biopsie sous contrôle échographique (US)
> - [ ] **4. Traitement en cas de cancer confirmé**
> - [ ] **5. Explications complémentaires sur demande de la patiente**
> 	- [ ] Méthode du ganglion sentinelle
> 	- [ ] Complications du curage axillaire (lymphœdème)
> 	- [ ] Justification de la radiothérapie adjuvante
> 	- [ ] Durée et organisation du traitement
> - [ ] **6. Orientation spécialisée**
> - [ ] **7. Soutien psychologique**
> 	- [ ] Reconnaître l'anxiété de la patiente
> 	- [ ] Proposer un soutien psycho-oncologique
> 	- [ ] Informer sur les groupes de soutien

> [!success] 💊 Management — si Nodule suspect de malignité dans le sein droit
> - [ ] **1. Échographie mammaire**
> - [ ] **2. Diagnostic présumé**
> - [ ] **3. À clarifier**
> - [ ] **4. Pas de pré-diagnostic**
> - [ ] **5. Triple diagnostic**
> - [ ] **6. Orientation centre du sein**
> - [ ] **7. Conseil génétique**
> - [ ] **8. Auto-examen des seins**
> - [ ] **9. Prévention**
> - [ ] **10. Reconsultation**
