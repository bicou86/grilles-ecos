---
aliases:
  - "Mémento Fièvre"
type: memento-ecos-ssp
ssp: "Fièvre"
specialite: "Médecine Interne"
cas: 3
diagnostics: 3
attendus: "non déclarés"
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
> ⚠️ **Le suffixe parle des formulations, pas du contenu clinique.** Le
> rapprochement entre grilles est encore purement lexical : deux grilles qui
> disent la même chose autrement (« Motif de consultation » et « Motif de
> consultation principal », « Allergies » et « Allergies connues ») donnent
> **deux items distincts**, chacun marqué comme partiel. Un `*(1 grille sur 2)*`
> ne veut donc pas dire que l'autre grille néglige la question — seulement
> qu'elle l'écrit autrement. Tant que le vocabulaire canonique n'est pas
> rempli, lisez les libellés voisins ensemble.

# Fièvre ⭐️

*Médecine Interne · 3 grilles · 3 diagnostics documentés · aucun diagnostic attendu déclaré* — [[SSP — Fièvre]]

> [!abstract] Les 3 grilles fusionnées
> - **AZYGOS-31** — Pyélonéphrite `diagnostic-travail` · [grille](<file:///Users/damienfulliquet/Developer/GitHub/grilles-ecos/docs/azygos-grilles/f9c82847-69cb-4a1a-aa41-6a246165b62a.json>)
> - **AZYGOS-32** — Fuite anastomotique `confirme` · [grille](<file:///Users/damienfulliquet/Developer/GitHub/grilles-ecos/docs/azygos-grilles/4be4b3cf-70a5-4b07-a07b-3d125310420d.json>)
> - **RESCOS-46** — Endocardite infectieuse `confirme` · [grille](<file:///Users/damienfulliquet/Developer/GitHub/grilles-ecos/cases/rescos/RESCOS-46%20-%20Fièvre%20-%20Grille%20ECOS.html>)

> [!question] Plaintes voisines
> La même plainte, ou une forme voisine, est documentée ailleurs :
> - [[Mémento — Fièvre au Retour de Voyage]] (2 grilles) — contexte de voyage, diagnostic différentiel distinct
> - [[Mémento — Fièvre du Nourrisson]] (3 grilles) — forme du nourrisson, diagnostic différentiel distinct

> [!note] 📋 Anamnèse
> - [ ] **1. Question ouverte d’entrée *(Fuite anastomotique · Pyélonéphrite)***
> - [ ] **2. Dimension temporelle *(Fuite anastomotique · Pyélonéphrite)***
> - [ ] **3. Début / Durée *(Fuite anastomotique · Pyélonéphrite)***
> - [ ] **4. Évolution *(Fuite anastomotique · Pyélonéphrite)***
> - [ ] **5. Épisode antérieur *(Pyélonéphrite)***
> - [ ] **6. Intensité / Sévérité *(Pyélonéphrite)***
> - [ ] **7. Facteurs atténuants *(Pyélonéphrite)***
> - [ ] **8. Symptômes associés à la fièvre**
> 	- [ ] Frissons *(Endocardite infectieuse)*
> 	- [ ] Transpiration *(Endocardite infectieuse)*
> 	- [ ] Toux *(Endocardite infectieuse)*
> 	- [ ] Dyspnée *(Endocardite infectieuse)*
> 	- [ ] Disparition du goût et/ou odorat COVID-19 *(Endocardite infectieuse)*
> - [ ] **9. Vigilance *(Pyélonéphrite)***
> - [ ] **10. Comportement de boisson *(Pyélonéphrite)***
> - [ ] **11. Miction *(Pyélonéphrite)***
> - [ ] **12. Couches *(Pyélonéphrite)***
> - [ ] **13. Voies respiratoires *(Pyélonéphrite)***
> - [ ] **14. Oreilles *(Pyélonéphrite)***
> - [ ] **15. Gastro-intestinal *(Pyélonéphrite)***
> - [ ] **16. Peau *(Pyélonéphrite)***
> - [ ] **17. Convulsion *(Pyélonéphrite)***
> - [ ] **18. Antécédents médicaux *(Endocardite infectieuse · Pyélonéphrite)***
> 	- [ ] Maladies *(Endocardite infectieuse)*
> 	- [ ] Opérations/hospitalisations *(Endocardite infectieuse)*
> 	- [ ] Vaccins *(Endocardite infectieuse)*
> 	- [ ] Perte de poids récente *(Endocardite infectieuse)*
> - [ ] **19. Antécédents chirurgicaux *(Pyélonéphrite)***
> - [ ] **20. Médicaments *(Pyélonéphrite)***
> - [ ] **21. Allergies *(Pyélonéphrite)***
> - [ ] **22. Naissance et développement *(Pyélonéphrite)***
> - [ ] **23. Grossesse / Accouchement *(Pyélonéphrite)***
> - [ ] **24. Développement *(Pyélonéphrite)***
> - [ ] **25. Vaccinations *(Pyélonéphrite)***
> - [ ] **26. Alimentation *(Pyélonéphrite)***
> - [ ] **27. Antécédents familiaux *(Pyélonéphrite)***
> - [ ] **28. Général *(Pyélonéphrite)***
> - [ ] **29. Reins et voies urinaires *(Pyélonéphrite)***
> - [ ] **30. Situation sociale *(Pyélonéphrite)***
> - [ ] **31. Mode d’apparition *(Fuite anastomotique)***
> - [ ] **32. Localisation de la douleur *(Fuite anastomotique)***
> - [ ] **33. Type de douleur *(Fuite anastomotique)***
> - [ ] **34. Intensité de la douleur *(Fuite anastomotique)***
> - [ ] **35. Facteurs soulageants *(Fuite anastomotique)***
> - [ ] **36. Mesures déjà prises *(Fuite anastomotique)***
> - [ ] **37. Facteurs aggravants *(Fuite anastomotique)***
> - [ ] **38. Frissons / sensation de fièvre *(Fuite anastomotique)***
> - [ ] **39. Nausées / vomissements *(Fuite anastomotique)***
> - [ ] **40. Sensation de tension / ballonnement *(Fuite anastomotique)***
> - [ ] **41. Selles *(Fuite anastomotique)***
> - [ ] **42. Flatulences *(Fuite anastomotique)***
> - [ ] **43. DD Wind | Poumon *(Fuite anastomotique)***
> - [ ] **44. Toux *(Fuite anastomotique)***
> - [ ] **45. Dyspnée *(Fuite anastomotique)***
> - [ ] **46. DD Water | Voies urinaires *(Fuite anastomotique)***
> - [ ] **47. Troubles mictionnels *(Fuite anastomotique)***
> - [ ] **48. DD Walking | Thrombose / embolie *(Fuite anastomotique)***
> - [ ] **49. Symptômes des membres / œdème de jambe *(Fuite anastomotique)***
> - [ ] **50. Douleurs thoraciques *(Fuite anastomotique)***
> - [ ] **51. DD Wound | Plaie *(Fuite anastomotique)***
> - [ ] **52. Anomalies plaie OP (douleur, rougeur, écoulement) *(Fuite anastomotique)***
> - [ ] **53. DD « What did we do? » | Dispositifs, médicaments, etc. *(Fuite anastomotique)***
> - [ ] **54. Douleur / rougeur à la voie veineuse *(Fuite anastomotique)***
> - [ ] **55. Niveau fonctionnel antérieur *(Fuite anastomotique)***
> - [ ] **56. Caractérisation de la fièvre *(Endocardite infectieuse)***
> 	- [ ] Début/durée
> 	- [ ] Intensité
> 	- [ ] Évolution
> 	- [ ] Fluctuation
> 	- [ ] Facteurs soulageants
> - [ ] **57. Présence de douleurs (tous types) *(Endocardite infectieuse)***
> 	- [ ] Pas de douleur thoracique, pas de céphalée, pas de douleur nucale
> - [ ] **58. Caractérisation de la toux *(Endocardite infectieuse)***
> 	- [ ] Chronologie (durée)
> 	- [ ] Fréquence
> 	- [ ] Qualité (sèche/grasse)
> 	- [ ] Expectorations
> 	- [ ] Couleur des expectorations
> 	- [ ] Présence de sang dans les expectorations
> - [ ] **59. Anamnèse par système *(Endocardite infectieuse)***
> 	- [ ] Éruptions cutanées
> 	- [ ] Douleurs articulaires
> 	- [ ] Symptômes digestifs
> 	- [ ] Symptômes urinaires
> - [ ] **60. Habitudes *(Endocardite infectieuse)***
> 	- [ ] Médicaments
> 	- [ ] Tabac
> 	- [ ] Voyages
> 	- [ ] Drogues
> 	- [ ] Sexualité (type, préservatif)

> [!tip] 🩺 Status
> - [ ] **1. État général *(Pyélonéphrite)***
> - [ ] **2. Temps de recoloration capillaire *(Fuite anastomotique · Pyélonéphrite)***
> - [ ] **3. Inspection cutanée *(Endocardite infectieuse · Pyélonéphrite)***
> 	- [ ] Recherche d'affection/éruption cutanées (point d'entrée infectieux) *(Endocardite infectieuse)*
> 	- [ ] Recherche systématique sur tout le corps (sauf zones intimes) *(Endocardite infectieuse)*
> - [ ] **4. Hydratation *(Pyélonéphrite)***
> - [ ] **5. Muqueuses *(Pyélonéphrite)***
> - [ ] **6. Turgescence cutanée *(Pyélonéphrite)***
> - [ ] **7. Larmes *(Pyélonéphrite)***
> - [ ] **8. Inspection *(Pyélonéphrite)***
> - [ ] **9. Auscultation *(Pyélonéphrite)***
> - [ ] **10. Palpation *(Fuite anastomotique · Pyélonéphrite)***
> - [ ] **11. Fosses lombaires *(Pyélonéphrite)***
> - [ ] **12. Statut ORL *(Pyélonéphrite)***
> - [ ] **13. Oreilles *(Pyélonéphrite)***
> - [ ] **14. Nez *(Pyélonéphrite)***
> - [ ] **15. Pharynx *(Pyélonéphrite)***
> - [ ] **16. Méningisme *(Pyélonéphrite)***
> - [ ] **17. Motricité spontanée *(Pyélonéphrite)***
> - [ ] **18. Paramètres vitaux *(Fuite anastomotique)***
> - [ ] **19. Situation circulatoire *(Fuite anastomotique)***
> - [ ] **20. Température des extrémités *(Fuite anastomotique)***
> - [ ] **21. Inspection des plaies opératoires *(Fuite anastomotique)***
> - [ ] **22. Inspection du drain de Douglas *(Fuite anastomotique)***
> - [ ] **23. Inspection / palpation VVP *(Fuite anastomotique)***
> - [ ] **24. Inspection de l’abdomen *(Fuite anastomotique)***
> - [ ] **25. Auscultation des bruits intestinaux *(Fuite anastomotique)***
> - [ ] **26. Percussion de l’abdomen *(Fuite anastomotique)***
> - [ ] **27. Palpation douce *(Fuite anastomotique)***
> - [ ] **28. Douleur au relâchement direct *(Fuite anastomotique)***
> - [ ] **29. Douleur au relâchement croisée *(Fuite anastomotique)***
> - [ ] **30. Douleur à la secousse / à l’ébranlement *(Fuite anastomotique)***
> - [ ] **31. Toucher rectal *(Fuite anastomotique)***
> - [ ] **32. Auscultation pulmonaire *(Fuite anastomotique)***
> - [ ] **33. Douleur à la percussion des fosses rénales *(Fuite anastomotique)***
> - [ ] **34. Examen des jambes *(Fuite anastomotique)***
> - [ ] **35. Auscultation cardiaque *(Endocardite infectieuse)***
> 	- [ ] Foyer aortique
> 	- [ ] Foyer pulmonaire
> 	- [ ] Foyer mitral
> 	- [ ] Foyer tricuspidien
> - [ ] **36. Status vasculaire *(Endocardite infectieuse)***
> 	- [ ] Palpation des pouls périphériques
> 	- [ ] Temps de recoloration des extrémités
> 	- [ ] Présence d'œdème/angiœdème
> 	- [ ] Auscultation des carotides
> - [ ] **37. Pulmonaire *(Endocardite infectieuse)***
> 	- [ ] Auscultation postérieure (min 6 foyers, 3 de chaque côté)
> 	- [ ] En auscultant, compare systématiquement gauche et droite
> 	- [ ] Auscultation latérale (des deux côtés)
> 	- [ ] Auscultation antérieure
> 	- [ ] Percussion
> 	- [ ] Amplitude
> - [ ] **38. Inspection de la cavité buccale *(Endocardite infectieuse)***
> - [ ] **39. Rigidité nucale (méningisme) *(Endocardite infectieuse)***
> - [ ] **40. Palpations des aires ganglionnaires *(Endocardite infectieuse)***
> 	- [ ] Cervicales
> 	- [ ] Axillaires
> 	- [ ] Inguinales

> [!success] 💊 Management — si Endocardite infectieuse
> - [ ] **1. Évoque un diagnostic différentiel cohérent**
> 	- [ ] Endocardite (extraction dentaire récente)
> 	- [ ] Pneumonie
> 	- [ ] Méningite
> 	- [ ] Sepsis
> 	- [ ] Maladies inflammatoires (Still, Horton)
> 	- [ ] Néoplasies
> 	- [ ] Fièvre médicamenteuse
> - [ ] **2. Propose un examen paraclinique pertinent**
> 	- [ ] Chimie sanguine et formule sanguine
> 	- [ ] Hémocultures
> 	- [ ] Stix urinaire/ECBU
> 	- [ ] Radiographie thoracique
> 	- [ ] ECG
> - [ ] **3. Évoque la nécessité d'hospitalisation et de surveillance**

> [!success] 💊 Management — si Fuite anastomotique
> *La ou les grilles de ce diagnostic ne cotent aucun item de management* — elles s'arrêtent à l'anamnèse et au status.

> [!success] 💊 Management — si Pyélonéphrite
> - [ ] **1. Statut urinaire**
> - [ ] **2. Laboratoire**
> - [ ] **3. CRP**
> - [ ] **4. Formule sanguine**
> - [ ] **5. Échographie**
> - [ ] **6. Uroculture**
> - [ ] **7. Hémoculture**
> - [ ] **8. Diagnostic de travail**
> - [ ] **9. Classification**
> - [ ] **10. Antibiothérapie**
> - [ ] **11. Substitution liquidienne**
> - [ ] **12. Antipyrèse**
> - [ ] **13. Hospitalisation**
> - [ ] **14. Liaison néphrologique**
> - [ ] **15. Bilan complémentaire**
> - [ ] **16. MCUG**
> - [ ] **17. Scintigraphie fonctionnelle**
