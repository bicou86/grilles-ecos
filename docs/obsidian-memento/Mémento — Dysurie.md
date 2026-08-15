---
aliases:
  - "Mémento Dysurie"
type: memento-ecos-ssp
ssp: "Dysurie"
specialite: "Néphro-Urologie"
cas: 4
diagnostics: 4
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

# Dysurie

*Néphro-Urologie · 4 grilles · 4 diagnostics documentés · 1 attendu documenté ailleurs · 1 attendu absent du corpus* — [[SSP — Dysurie]]

> [!abstract] Les 4 grilles fusionnées
> - **AZYGOS-8** — Suspicion d'hyperplasie bénigne de la prostate `diagnostic-travail` · [grille](<file:///Users/damienfulliquet/Developer/GitHub/grilles-ecos/.azygos-extraction/f5e3b513-caf4-4300-ad3e-bde97d0d54ab.json>)
> - **German-37** — Urétrite sexuellement transmissible `corrige` · [grille](<file:///Users/damienfulliquet/Developer/GitHub/grilles-ecos/cases/german/German-37_-_Dysurie_-_Grille_ECOS.html>)
> - **RESCOS-41** — Infection à Chlamydia trachomatis `explicite` · [grille](<file:///Users/damienfulliquet/Developer/GitHub/grilles-ecos/cases/rescos/RESCOS-41%20-%20Dysurie%20-%20Grille%20ECOS.html>)
> - **RESCOS-42** — Infection urinaire (cystite) `explicite` · [grille](<file:///Users/damienfulliquet/Developer/GitHub/grilles-ecos/cases/rescos/RESCOS-42%20-%20Dysurie%20-%20Grille%20ECOS.html>)

> [!note] 📋 Anamnèse
> - [ ] **1. Question initiale *(Suspicion d'hyperplasie bénigne de la prostate)***
> - [ ] **2. Dimension temporelle *(Suspicion d'hyperplasie bénigne de la prostate)***
> - [ ] **3. Début / Durée *(Suspicion d'hyperplasie bénigne de la prostate)***
> - [ ] **4. Apparition *(Suspicion d'hyperplasie bénigne de la prostate)***
> - [ ] **5. Évolution *(Suspicion d'hyperplasie bénigne de la prostate)***
> - [ ] **6. Facteurs soulageants *(Suspicion d'hyperplasie bénigne de la prostate)***
> - [ ] **7. Facteurs aggravants *(Suspicion d'hyperplasie bénigne de la prostate)***
> - [ ] **8. Retentissement des symptômes *(Suspicion d'hyperplasie bénigne de la prostate)***
> - [ ] **9. Symptômes associés *(Infection à Chlamydia trachomatis · Suspicion d'hyperplasie bénigne de la prostate)***
> 	- [ ] Spotting/métrorragies *(Infection à Chlamydia trachomatis)*
> 	- [ ] Dyspareunie *(Infection à Chlamydia trachomatis)*
> 	- [ ] Écoulements vaginaux *(Infection à Chlamydia trachomatis)*
> 	- [ ] Prurit vulvaire *(Infection à Chlamydia trachomatis)*
> - [ ] **10. Symptômes obstructifs *(Suspicion d'hyperplasie bénigne de la prostate)***
> - [ ] **11. Difficultés à démarrer *(Suspicion d'hyperplasie bénigne de la prostate)***
> - [ ] **12. Jet urinaire affaibli *(Suspicion d'hyperplasie bénigne de la prostate)***
> - [ ] **13. Jet interrompu *(Suspicion d'hyperplasie bénigne de la prostate)***
> - [ ] **14. Gouttes retardataires *(Suspicion d'hyperplasie bénigne de la prostate)***
> - [ ] **15. Miction prolongée *(Suspicion d'hyperplasie bénigne de la prostate)***
> - [ ] **16. Résidu post-mictionnel *(Suspicion d'hyperplasie bénigne de la prostate)***
> - [ ] **17. Symptômes de stockage *(Suspicion d'hyperplasie bénigne de la prostate)***
> - [ ] **18. Urgenturie *(Suspicion d'hyperplasie bénigne de la prostate)***
> - [ ] **19. Pollakiurie *(Suspicion d'hyperplasie bénigne de la prostate)***
> - [ ] **20. Nycturie *(Suspicion d'hyperplasie bénigne de la prostate)***
> - [ ] **21. Dysurie *(Suspicion d'hyperplasie bénigne de la prostate)***
> - [ ] **22. Rétention d'urine *(Suspicion d'hyperplasie bénigne de la prostate)***
> - [ ] **23. Incontinence urinaire *(Suspicion d'hyperplasie bénigne de la prostate)***
> - [ ] **24. Signes d'infection *(Suspicion d'hyperplasie bénigne de la prostate)***
> - [ ] **25. Hématurie *(Suspicion d'hyperplasie bénigne de la prostate)***
> - [ ] **26. Symptômes B *(Suspicion d'hyperplasie bénigne de la prostate)***
> - [ ] **27. Quantité de boisson *(Suspicion d'hyperplasie bénigne de la prostate)***
> - [ ] **28. Troubles de l'érection *(Suspicion d'hyperplasie bénigne de la prostate)***
> - [ ] **29. Transit / Constipation *(Suspicion d'hyperplasie bénigne de la prostate)***
> - [ ] **30. Symptômes neurologiques *(Suspicion d'hyperplasie bénigne de la prostate)***
> - [ ] **31. Antécédents médicaux *(Infection urinaire (cystite) · Suspicion d'hyperplasie bénigne de la prostate · Urétrite sexuellement transmissible)***
> 	- [ ] Maladies/comorbidités *(Infection urinaire (cystite))*
> 	- [ ] Interventions ou hospitalisations *(Infection urinaire (cystite))*
> 	- [ ] Allergies *(Infection urinaire (cystite))*
> 	- [ ] Médicaments *(Infection urinaire (cystite))*
> - [ ] **32. Antécédents chirurgicaux *(Suspicion d'hyperplasie bénigne de la prostate)***
> - [ ] **33. Anamnèse médicamenteuse *(Suspicion d'hyperplasie bénigne de la prostate)***
> - [ ] **34. Toxiques *(Suspicion d'hyperplasie bénigne de la prostate)***
> - [ ] **35. Alcool *(Suspicion d'hyperplasie bénigne de la prostate)***
> - [ ] **36. Tabac *(Suspicion d'hyperplasie bénigne de la prostate)***
> - [ ] **37. Drogues *(Suspicion d'hyperplasie bénigne de la prostate)***
> - [ ] **38. Allergies *(Suspicion d'hyperplasie bénigne de la prostate · Urétrite sexuellement transmissible)***
> - [ ] **39. Antécédents familiaux *(Suspicion d'hyperplasie bénigne de la prostate · Urétrite sexuellement transmissible)***
> - [ ] **40. Profession *(Suspicion d'hyperplasie bénigne de la prostate)***
> - [ ] **41. Anamnèse sociale *(Suspicion d'hyperplasie bénigne de la prostate · Urétrite sexuellement transmissible)***
> - [ ] **42. Présentation avec nom, fonction et tâche *(Urétrite sexuellement transmissible)***
> - [ ] **43. Question ouverte d'entrée - Symptôme principal *(Urétrite sexuellement transmissible)***
> - [ ] **44. Caractérisation de la dysurie *(Urétrite sexuellement transmissible)***
> 	- [ ] Douleurs mictionnelles
> 	- [ ] Jet faible/goutte à goutte
> 	- [ ] Durée des symptômes
> - [ ] **45. Fréquence et volume mictionnel *(Urétrite sexuellement transmissible)***
> 	- [ ] Fréquence
> 	- [ ] Volume
> 	- [ ] Nycturie
> - [ ] **46. Aspect des urines *(Urétrite sexuellement transmissible)***
> 	- [ ] Couleur
> 	- [ ] Présence de sang
> - [ ] **47. Écoulement urétral *(Urétrite sexuellement transmissible)***
> 	- [ ] Présence
> 	- [ ] Moment d'apparition
> 	- [ ] Aspect
> - [ ] **48. Douleurs associées *(Urétrite sexuellement transmissible)***
> 	- [ ] Douleurs hypogastriques
> 	- [ ] Douleurs lombaires
> 	- [ ] Douleurs lors de l'éjaculation
> - [ ] **49. Symptômes généraux *(Urétrite sexuellement transmissible)***
> 	- [ ] Fièvre
> 	- [ ] Éruption cutanée
> 	- [ ] Symptômes B (sueurs nocturnes, perte de poids)
> - [ ] **50. Recherche étiologique - Comportements à risque *(Urétrite sexuellement transmissible)***
> 	- [ ] Hydratation
> 	- [ ] Rapports sexuels non protégés
> 	- [ ] Partenaires
> 	- [ ] Dernier rapport à risque
> - [ ] **51. Antécédents urologiques *(Urétrite sexuellement transmissible)***
> 	- [ ] Dépistage prostatique
> 	- [ ] Sondage vésical
> 	- [ ] Épisodes similaires antérieurs
> 	- [ ] Anomalies congénitales
> - [ ] **52. Médicaments actuels *(Urétrite sexuellement transmissible)***
> - [ ] **53. Habitudes de vie *(Infection à Chlamydia trachomatis · Urétrite sexuellement transmissible)***
> 	- [ ] Alcool
> 	- [ ] Tabac
> 	- [ ] Drogues
> 	- [ ] Activité physique *(Infection à Chlamydia trachomatis)*
> - [ ] **54. Caractérisation du symptôme principal *(Infection à Chlamydia trachomatis)***
> 	- [ ] Douleurs à la miction
> 	- [ ] Intensité
> 	- [ ] Évolution
> 	- [ ] Développement
> - [ ] **55. Anamnèse sexuelle *(Infection urinaire (cystite) · Infection à Chlamydia trachomatis)***
> 	- [ ] Nouveau partenaire *(Infection à Chlamydia trachomatis)*
> 	- [ ] Fréquence des rapports *(Infection à Chlamydia trachomatis)*
> 	- [ ] Protection *(Infection à Chlamydia trachomatis)*
> 	- [ ] Partenaires multiples du copain *(Infection à Chlamydia trachomatis)*
> 	- [ ] Derniers rapports avant nouvelle relation *(Infection à Chlamydia trachomatis)*
> 	- [ ] Pratiques *(Infection urinaire (cystite))*
> 	- [ ] Partenaires *(Infection urinaire (cystite))*
> 	- [ ] Type de protection *(Infection urinaire (cystite))*
> 	- [ ] Antécédents d'IST *(Infection urinaire (cystite))*
> 	- [ ] Moyens contraceptifs *(Infection urinaire (cystite))*
> - [ ] **56. Anamnèse gynécologique *(Infection à Chlamydia trachomatis)***
> 	- [ ] Dernières règles
> 	- [ ] Contraception
> 	- [ ] Antécédents d'IST
> 	- [ ] Grossesses antérieures
> - [ ] **57. Symptômes urinaires *(Infection à Chlamydia trachomatis)***
> 	- [ ] Pollakiurie
> 	- [ ] Urgenturie
> 	- [ ] Hématurie
> 	- [ ] Douleurs lombaires
> - [ ] **58. Réponse aux symptômes *(Infection à Chlamydia trachomatis)***
> 	- [ ] Automédication
> 	- [ ] Consultation médicale antérieure
> - [ ] **59. Allergies et médicaments *(Infection à Chlamydia trachomatis)***
> 	- [ ] Allergies
> 	- [ ] Médicaments actuels
> - [ ] **60. Caractérisation de la douleur mictionnelle *(Infection urinaire (cystite))***
> 	- [ ] Qualité
> 	- [ ] Intensité
> 	- [ ] Irradiation
> 	- [ ] Facteurs aggravants ET soulageants
> 	- [ ] Symptômes associés
> - [ ] **61. Chronologie de la douleur *(Infection urinaire (cystite))***
> 	- [ ] Début
> 	- [ ] Circonstance de survenue
> 	- [ ] Évolution
> - [ ] **62. Anamnèse urologique *(Infection urinaire (cystite))***
> 	- [ ] Fréquence mictionnelle
> 	- [ ] Quantité d'urine
> 	- [ ] Couleur des urines
> 	- [ ] Présence de sang
> - [ ] **63. Anamnèse génitale *(Infection urinaire (cystite))***
> 	- [ ] Pertes vaginales
> 	- [ ] Prurit vaginal
> 	- [ ] Dates des dernières règles
> - [ ] **64. Anamnèse générale, présence de *(Infection urinaire (cystite))***
> 	- [ ] Fièvre
> 	- [ ] Transpiration
> 	- [ ] Perte de poids involontaire

> [!tip] 🩺 Status
> - [ ] **1. Paramètres vitaux *(Suspicion d'hyperplasie bénigne de la prostate)***
> - [ ] **2. Palpation sus-pubienne *(Suspicion d'hyperplasie bénigne de la prostate)***
> - [ ] **3. Examen abdominal d'orientation *(Suspicion d'hyperplasie bénigne de la prostate)***
> - [ ] **4. Indication, information et consentement *(Suspicion d'hyperplasie bénigne de la prostate)***
> - [ ] **5. Indication *(Suspicion d'hyperplasie bénigne de la prostate)***
> - [ ] **6. Explication du déroulement *(Suspicion d'hyperplasie bénigne de la prostate)***
> - [ ] **7. Consentement *(Suspicion d'hyperplasie bénigne de la prostate)***
> - [ ] **8. Préparation et positionnement *(Suspicion d'hyperplasie bénigne de la prostate)***
> - [ ] **9. Positionnement *(Suspicion d'hyperplasie bénigne de la prostate)***
> - [ ] **10. Gants et lubrifiant *(Suspicion d'hyperplasie bénigne de la prostate)***
> - [ ] **11. Annonce de l'introduction *(Suspicion d'hyperplasie bénigne de la prostate)***
> - [ ] **12. TR systématique et résultat de la palpation *(Suspicion d'hyperplasie bénigne de la prostate)***
> - [ ] **13. Tonus sphinctérien *(Suspicion d'hyperplasie bénigne de la prostate)***
> - [ ] **14. Rectum *(Suspicion d'hyperplasie bénigne de la prostate)***
> - [ ] **15. Douleur à la palpation *(Suspicion d'hyperplasie bénigne de la prostate)***
> - [ ] **16. Taille de la prostate *(Suspicion d'hyperplasie bénigne de la prostate)***
> - [ ] **17. Consistance et surface de la prostate *(Suspicion d'hyperplasie bénigne de la prostate)***
> - [ ] **18. Mobilité de la muqueuse / Sillon *(Suspicion d'hyperplasie bénigne de la prostate)***
> - [ ] **19. Examen du doigtier *(Suspicion d'hyperplasie bénigne de la prostate)***
> - [ ] **20. Organes génitaux externes / Périnée *(Suspicion d'hyperplasie bénigne de la prostate)***
> - [ ] **21. Organes génitaux externes *(Suspicion d'hyperplasie bénigne de la prostate)***
> - [ ] **22. Périnée / Région périanale *(Suspicion d'hyperplasie bénigne de la prostate)***
> - [ ] **23. Réflexe anal *(Suspicion d'hyperplasie bénigne de la prostate)***
> - [ ] **24. Examen abdominal *(Infection à Chlamydia trachomatis · Urétrite sexuellement transmissible)***
> 	- [ ] Palpation abdominale
> 	- [ ] Palpation vésicale *(Urétrite sexuellement transmissible)*
> 	- [ ] Percussion vésicale *(Urétrite sexuellement transmissible)*
> 	- [ ] Recherche d'un globe vésical *(Urétrite sexuellement transmissible)*
> 	- [ ] Recherche de sensibilité sus-pubienne *(Infection à Chlamydia trachomatis)*
> 	- [ ] Palpation du foie *(Infection à Chlamydia trachomatis)*
> - [ ] **25. Examen des fosses lombaires *(Urétrite sexuellement transmissible)***
> 	- [ ] Palpation bilatérale
> 	- [ ] Signe de Giordano (douleur à la percussion)
> - [ ] **26. Examen génital externe *(Urétrite sexuellement transmissible)***
> 	- [ ] Inspection du méat urétral
> 	- [ ] Recherche d'écoulement
> 	- [ ] Examen du gland et du prépuce
> 	- [ ] Palpation testiculaire
> 	- [ ] Recherche d'adénopathies inguinales
> - [ ] **27. Toucher rectal *(Urétrite sexuellement transmissible)***
> 	- [ ] Évaluation du volume prostatique
> 	- [ ] Consistance de la prostate
> 	- [ ] Douleur prostatique
> 	- [ ] Recherche de nodules
> - [ ] **28. Installation et confort de la patiente *(Infection à Chlamydia trachomatis)***
> 	- [ ] Vérifier le confort
> 	- [ ] Expliquer l'examen
> 	- [ ] Respecter l'intimité
> - [ ] **29. Préparation examen gynécologique *(Infection à Chlamydia trachomatis)***
> 	- [ ] Port de gants
> 	- [ ] Inspection du périnée et de la vulve
> 	- [ ] Lubrification du spéculum
> - [ ] **30. Examen au spéculum *(Infection à Chlamydia trachomatis)***
> 	- [ ] Introduction correcte du spéculum
> 	- [ ] Visualisation du col
> 	- [ ] Observation des parois vaginales
> 	- [ ] Retrait correct du spéculum
> - [ ] **31. Toucher vaginal *(Infection à Chlamydia trachomatis)***
> 	- [ ] Palpation bimanuelle
> 	- [ ] Mobilisation du col
> 	- [ ] Recherche de masses annexielles
> - [ ] **32. Prélèvements *(Infection à Chlamydia trachomatis)***
> 	- [ ] Prélèvement cervical pour PCR
> 	- [ ] Frottis si indiqué
> 	- [ ] Technique de prélèvement correcte
> - [ ] **33. Évoque la nécessité d'effectuer un examen abdominal *(Infection urinaire (cystite))***
> 	- [ ] Propose un examen abdominal complet
> 	- [ ] Recherche douleur lombaire/flancs (pyélonéphrite)
> - [ ] **34. Évoque la possibilité d'un examen gynécologique *(Infection urinaire (cystite))***
> 	- [ ] Propose examen gynécologique pour IST
> - [ ] **35. Simulation - palpation vésicale *(Infection urinaire (cystite))***
> 	- [ ] Réaction appropriée si palpation vessie

> [!success] 💊 Management — si Infection à Chlamydia trachomatis
> - [ ] **1. Prévention et conseils**
> 	- [ ] Utilisation du préservatif
> 	- [ ] Dépistage régulier si partenaires multiples
> 	- [ ] Notification des partenaires
> 	- [ ] Suivi après traitement
> - [ ] **2. Hypothèse diagnostique principale**
> 	- [ ] Infection à Chlamydia trachomatis
> 	- [ ] Explication adaptée à la patiente
> - [ ] **3. Diagnostics différentiels évoqués**
> 	- [ ] Infection à Neisseria gonorrhoeae
> 	- [ ] Infection à Trichomonas vaginalis
> 	- [ ] Infection à Mycoplasma
> 	- [ ] Cystite simple
> - [ ] **4. Examens complémentaires**
> 	- [ ] PCR Chlamydia/Gonocoque
> 	- [ ] Analyse d'urine
> 	- [ ] Test de grossesse si indiqué
> 	- [ ] Dépistage IST complet
> - [ ] **5. Traitement proposé**
> 	- [ ] Azithromycine 1g dose unique
> 	- [ ] ± Ceftriaxone 250mg IM
> 	- [ ] Traitement du partenaire
> 	- [ ] Abstinence/protection pendant traitement
> - [ ] **6. Réponse aux inquiétudes**
> 	- [ ] Rassurer sur la gravité
> 	- [ ] Expliquer les complications possibles si non traité
> 	- [ ] Importance du traitement du partenaire

> [!success] 💊 Management — si Infection urinaire (cystite)
> - [ ] **1. Diagnostics différentiels évoqués**
> 	- [ ] Pyélonéphrite
> 	- [ ] Infections sexuellement transmissibles (gonorrhée, chlamydia, syphilis, VIH)
> - [ ] **2. Traitement proposé**
> 	- [ ] Antibiothérapie pour infection urinaire
> - [ ] **3. Évoque le diagnostic d'infection urinaire basse**
> - [ ] **4. Propose des investigations paracliniques**
> 	- [ ] Analyse d'urine/ECBU
> 	- [ ] Dépistage IST (gonorrhée, chlamydia, syphilis, VIH)

> [!success] 💊 Management — si Prostatite
> *Aucune grille du corpus ne documente ce diagnostic* — il est pourtant attendu de cette SSP. **Trou de révision à combler ailleurs.**

> [!success] 💊 Management — si Pyélonéphrite
> *Aucune grille de cette SSP ne documente ce diagnostic* — mais le corpus le documente ailleurs : « Colique Néphrétique » (2 grilles, hors lot) · [[Mémento — Douleur Abdominale]] (1 grille) · « Fièvre » (1 grille, hors lot).

> [!success] 💊 Management — si Suspicion d'hyperplasie bénigne de la prostate
> - [ ] **1. Prise de sang**
> - [ ] **2. Valeurs de rétention rénale**
> - [ ] **3. Formule sanguine et paramètres inflammatoires**
> - [ ] **4. Analyse d'urine**
> - [ ] **5. Status urinaire**
> - [ ] **6. Échographie vésicale avec mesure du résidu post-mictionnel**
> - [ ] **7. Échographie des reins / des voies urinaires supérieures**
> - [ ] **8. Hypothèse diagnostique**
> - [ ] **9. Information du patient**
> - [ ] **10. Instructions**
> - [ ] **11. Traitement médicamenteux**
> - [ ] **12. Alpha-bloquants**
> - [ ] **13. Inhibiteurs de la 5-alpha-réductase**
> - [ ] **14. Calendrier mictionnel**
> - [ ] **15. Examens diagnostiques complémentaires**
> - [ ] **16. Orientation vers un spécialiste**
> - [ ] **17. Contrôle d'évolution**
> - [ ] **18. Filet de sécurité**

> [!success] 💊 Management — si Urétrite sexuellement transmissible
> - [ ] **1. Énonce le diagnostic principal**
> - [ ] **2. Diagnostics différentiels**
> 	- [ ] Cystite
> 	- [ ] Prostatite
> 	- [ ] Urétrite non gonococcique
> 	- [ ] Infection urinaire haute
> - [ ] **3. Examens diagnostiques**
> 	- [ ] Bandelette urinaire et ECBU
> 	- [ ] Test des 3 ou 4 verres si nécessaire
> 	- [ ] Prélèvement de l'écoulement urétral (gonocoques et Chlamydia)
> 	- [ ] Biologie : FSC, CRP, créatinine
> 	- [ ] Test VIH obligatoire !
> 	- [ ] Sérologies IST (syphilis, hépatites B et C)
> - [ ] **4. Traitement antibiotique**
> 	- [ ] Ceftriaxone 500mg IM dose unique (gonocoque)
> 	- [ ] + Azithromycine 1g PO dose unique (Chlamydia)
> 	- [ ] Alternative : doxycycline 100mg 2x/j pendant 7 jours
> - [ ] **5. Notification des partenaires**
> 	- [ ] Information obligatoire des partenaires
> 	- [ ] Traitement empirique des partenaires
> 	- [ ] Période de notification : 60 jours
> 	- [ ] Anonymat respecté si souhaité
> - [ ] **6. Prévention et conseils**
> 	- [ ] Utilisation systématique du préservatif
> 	- [ ] Dépistage régulier si comportements à risque
> 	- [ ] Information sur les IST
> 	- [ ] Vaccination hépatite B si non fait
> - [ ] **7. Suivi**
> 	- [ ] Contrôle clinique à 1 semaine
> 	- [ ] Test de guérison à 3-4 semaines
> 	- [ ] Contrôle VIH à 3 mois (fenêtre sérologique)
> 	- [ ] Support psychologique si nécessaire (contexte de séparation)
