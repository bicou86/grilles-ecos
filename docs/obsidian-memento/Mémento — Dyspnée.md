---
aliases:
  - "Mémento Dyspnée"
type: memento-ecos-ssp
ssp: "Dyspnée"
specialite: "Pneumologie"
cas: 5
diagnostics: 3
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
> - 🔬 = Management : examens complémentaires
> - 💊 = Management : prise en charge attendue
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
> ⚠️ **Le suffixe parle des formulations, pas du contenu clinique.** Le
> rapprochement entre grilles est encore purement lexical : deux grilles qui
> disent la même chose autrement (« Motif de consultation » et « Motif de
> consultation principal », « Allergies » et « Allergies connues ») donnent
> **deux items distincts**, chacun marqué comme partiel. Un `*(1 grille sur 2)*`
> ne veut donc pas dire que l'autre grille néglige la question — seulement
> qu'elle l'écrit autrement. Tant que le vocabulaire canonique n'est pas
> rempli, lisez les libellés voisins ensemble.

# Dyspnée ⭐️

*Pneumologie · 5 grilles · 3 diagnostics distincts* — [[SSP — Dyspnée]]

> [!abstract] Les 5 grilles fusionnées
> - **AZYGOS-23** — Insuffisance cardiaque (décompensée) `diagnostic-travail` · [grille](<file:///Users/damienfulliquet/Developer/GitHub/grilles-ecos/.azygos-extraction/60e62ee5-98b7-4679-91e1-6f82bb0678fe.json>)
> - **German-35** — Asthme `corrige` · [grille](<file:///Users/damienfulliquet/Developer/GitHub/grilles-ecos/cases/german/German-35_-_Dyspne_e_-_Grille_ECOS.html>)
> - **German-36** — BPCO `explicite` · [grille](<file:///Users/damienfulliquet/Developer/GitHub/grilles-ecos/cases/german/German-36_-_Dyspne_e_-_Grille_ECOS.html>)
> - **RESCOS-39** — Insuffisance cardiaque (décompensée) `premier-dd` · [grille](<file:///Users/damienfulliquet/Developer/GitHub/grilles-ecos/cases/rescos/RESCOS-39_-_Dyspne_e_-_Grille_ECOS.html>)
> - **RESCOS-40** — Insuffisance cardiaque (décompensée) `premier-dd` · [grille](<file:///Users/damienfulliquet/Developer/GitHub/grilles-ecos/cases/rescos/RESCOS-40_-_Dyspne_e_-_ECC_Cardio-pulmonaire_-_Grille_ECOS.html>)

> [!note] 📋 Anamnèse
> - [ ] **1. Stable / Instable *(1 grille sur 5)***
> - [ ] **2. Question d'introduction *(1 grille sur 5)***
> - [ ] **3. Dynamique temporelle *(1 grille sur 5)***
> - [ ] **4. Début *(1 grille sur 5)***
> - [ ] **5. Évolution *(1 grille sur 5)***
> - [ ] **6. Gravité *(1 grille sur 5)***
> - [ ] **7. Influence de la position *(1 grille sur 5)***
> - [ ] **8. Toux *(1 grille sur 5)***
> - [ ] **9. Expectoration *(1 grille sur 5)***
> - [ ] **10. Gonflement des jambes *(1 grille sur 5)***
> - [ ] **11. Nycturie *(1 grille sur 5)***
> - [ ] **12. DD Embolie pulmonaire *(1 grille sur 5)***
> - [ ] **13. Douleurs dépendantes de la respiration *(1 grille sur 5)***
> - [ ] **14. Syncope *(1 grille sur 5)***
> - [ ] **15. Anamnèse de thrombose *(1 grille sur 5)***
> - [ ] **16. DD SCA *(1 grille sur 5)***
> - [ ] **17. Douleurs thoraciques *(1 grille sur 5)***
> - [ ] **18. Irradiation bras/mâchoire/dos *(1 grille sur 5)***
> - [ ] **19. Palpitations *(1 grille sur 5)***
> - [ ] **20. DD Pneumonie *(1 grille sur 5)***
> - [ ] **21. Événement d'aspiration (fausse route) *(1 grille sur 5)***
> - [ ] **22. Fièvre *(1 grille sur 5)***
> - [ ] **23. Expectoration purulente *(1 grille sur 5)***
> - [ ] **24. Présentation avec nom, fonction et tâche *(Asthme · BPCO)***
> - [ ] **25. Question d'entrée ouverte - Symptômes principaux *(Asthme)***
> - [ ] **26. Circonstances de survenue et facteurs déclenchants *(Asthme)***
> 	- [ ] Moment de survenue
> 	- [ ] Type d'apparition
> 	- [ ] Facteurs déclenchants identifiés
> 	- [ ] Lien avec l'effort physique
> - [ ] **27. Évolution temporelle des symptômes *(Asthme · BPCO)***
> 	- [ ] Durée des épisodes *(Asthme)*
> 	- [ ] Évolution pendant la crise *(Asthme)*
> 	- [ ] Amélioration *(Asthme)*
> 	- [ ] Temps de récupération *(Asthme)*
> 	- [ ] Durée totale *(BPCO)*
> 	- [ ] Saisonnalité *(BPCO)*
> 	- [ ] Progression *(BPCO)*
> 	- [ ] Périodes d'amélioration *(BPCO)*
> - [ ] **28. Fréquence et récurrence *(Asthme)***
> 	- [ ] Épisodes antérieurs
> 	- [ ] Fréquence
> 	- [ ] Évolution dans le temps
> 	- [ ] Saisonnalité éventuelle
> - [ ] **29. Facteurs d'amélioration et d'aggravation *(Asthme)***
> 	- [ ] Ce qui améliore
> 	- [ ] Ce qui aggrave
> 	- [ ] Position particulière
> 	- [ ] Influence de l'environnement
> - [ ] **30. Caractéristiques de la toux *(Asthme)***
> 	- [ ] Type de toux
> 	- [ ] Hémoptysie
> 	- [ ] Moment de survenue
> 	- [ ] Association avec la dyspnée
> - [ ] **31. Symptômes nocturnes et sommeil *(Asthme)***
> 	- [ ] Réveils nocturnes
> 	- [ ] Dyspnée nocturne
> 	- [ ] Orthopnée
> 	- [ ] Qualité du sommeil
> - [ ] **32. Symptômes associés - ORL et respiratoires *(Asthme)***
> 	- [ ] Infections ORL récentes
> 	- [ ] Fréquence des infections
> 	- [ ] Fièvre
> 	- [ ] Rhinorrhée postérieure
> - [ ] **33. Symptômes associés - État général *(Asthme)***
> 	- [ ] Performance physique
> 	- [ ] Appétit
> 	- [ ] Évolution pondérale
> 	- [ ] Fatigue inhabituelle
> - [ ] **34. Symptômes associés - Autres *(Asthme)***
> 	- [ ] Sensation de corps étranger
> 	- [ ] Dysphagie
> 	- [ ] Ronflement
> 	- [ ] Douleurs thoraciques
> 	- [ ] Bruits respiratoires
> - [ ] **35. Facteurs de risque thromboemboliques *(Asthme)***
> 	- [ ] Vol long récent
> 	- [ ] Immobilisation prolongée
> 	- [ ] Douleur au mollet
> 	- [ ] Contraception orale
> - [ ] **36. Exposition et voyages *(Asthme)***
> 	- [ ] Exposition tuberculose
> 	- [ ] Voyages récents
> 	- [ ] Contact avec malades
> 	- [ ] Exposition professionnelle
> - [ ] **37. Antécédents médicaux personnels *(Asthme · BPCO)***
> 	- [ ] Maladies antérieures *(Asthme)*
> 	- [ ] Problèmes respiratoires antérieurs *(Asthme)*
> 	- [ ] Hospitalisations *(Asthme)*
> 	- [ ] Interventions chirurgicales *(Asthme)*
> 	- [ ] Maladies chroniques connues *(BPCO)*
> 	- [ ] Pathologies cardiovasculaires *(BPCO)*
> 	- [ ] Autres problèmes de santé *(BPCO)*
> 	- [ ] Chirurgies antérieures *(BPCO)*
> - [ ] **38. Traitements et habitudes *(Asthme)***
> 	- [ ] Médicaments actuels
> 	- [ ] Tabagisme
> 	- [ ] Alcool
> 	- [ ] Drogues
> - [ ] **39. Allergies détaillées *(Asthme)***
> 	- [ ] Allergies respiratoires
> 	- [ ] Allergies alimentaires
> 	- [ ] Manifestations cutanées
> 	- [ ] Croûtes de lait
> 	- [ ] Diagnostic d'asthme antérieur
> - [ ] **40. Antécédents familiaux *(Asthme · BPCO)***
> 	- [ ] Allergies familiales
> 	- [ ] Maladies respiratoires *(Asthme)*
> 	- [ ] Asthme familial *(Asthme)*
> 	- [ ] Autres maladies héréditaires *(Asthme)*
> 	- [ ] Cancer bronchique *(BPCO)*
> 	- [ ] Maladies respiratoires familiales *(BPCO)*
> 	- [ ] Pathologies cardiovasculaires *(BPCO)*
> - [ ] **41. Contexte social et environnemental *(Asthme)***
> 	- [ ] Situation familiale
> 	- [ ] Profession
> 	- [ ] Projets
> 	- [ ] Animaux domestiques
> - [ ] **42. Questions finales et résumé *(Asthme)***
> 	- [ ] Autres informations importantes
> 	- [ ] Questions du patient
> 	- [ ] Résumé de l'anamnèse
> - [ ] **43. Question d'entrée ouverte - Motif de consultation *(BPCO)***
> - [ ] **44. Caractérisation de la dyspnée *(3 grilles sur 5)***
> 	- [ ] Effort déclenchant *(BPCO)*
> 	- [ ] Orthopnée
> 	- [ ] Dyspnée paroxystique nocturne
> 	- [ ] Évolution dans le temps *(BPCO)*
> 	- [ ] Début progressif *(1 grille sur 5)*
> 	- [ ] Dyspnée d'effort initialement *(1 grille sur 5)*
> 	- [ ] Aggravation progressive *(1 grille sur 5)*
> 	- [ ] Amélioration en position assise *(1 grille sur 5)*
> 	- [ ] Évolution temporelle *(1 grille sur 5)*
> 	- [ ] Circonstances *(1 grille sur 5)*
> 	- [ ] Quantification *(1 grille sur 5)*
> - [ ] **45. Symptômes respiratoires associés - Toux *(BPCO)***
> 	- [ ] Type de toux
> 	- [ ] Caractère
> 	- [ ] Moment privilégié
> 	- [ ] Évolution récente
> - [ ] **46. Caractéristiques de l'expectoration *(BPCO)***
> 	- [ ] Aspect
> 	- [ ] Quantité
> 	- [ ] Odeur
> 	- [ ] Hémoptysie
> - [ ] **47. Facteurs déclenchants et aggravants *(BPCO)***
> 	- [ ] Temps froid
> 	- [ ] Tabagisme passif
> 	- [ ] Après refroidissements
> 	- [ ] Effort physique
> 	- [ ] Position couchée
> - [ ] **48. Facteurs d'amélioration *(BPCO)***
> 	- [ ] Position assise/debout
> 	- [ ] Air frais
> 	- [ ] Repos
> 	- [ ] Médicaments éventuels
> - [ ] **49. Impact fonctionnel *(BPCO)***
> 	- [ ] Performance physique
> 	- [ ] Activités quotidiennes limitées
> 	- [ ] Qualité de vie
> 	- [ ] Activités abandonnées
> - [ ] **50. Exacerbations et hospitalisations *(BPCO)***
> 	- [ ] Épisodes de bronchite
> 	- [ ] Prise d'antibiotiques
> 	- [ ] Hospitalisations
> 	- [ ] Recours aux urgences
> - [ ] **51. Activités physiques et loisirs *(BPCO)***
> 	- [ ] Sport actuel
> 	- [ ] Activités antérieures
> 	- [ ] Limitations progressives
> 	- [ ] Sédentarité
> - [ ] **52. Habitudes et toxiques *(BPCO)***
> 	- [ ] Tabagisme actif
> 	- [ ] Tentatives d'arrêt
> 	- [ ] Consommation d'alcool
> 	- [ ] Toxicomanie
> - [ ] **53. Allergies et traitements actuels *(BPCO)***
> 	- [ ] Allergies médicamenteuses
> 	- [ ] Intolérances
> 	- [ ] Médicaments actuels
> 	- [ ] Observance thérapeutique
> - [ ] **54. Contexte social et professionnel *(BPCO)***
> 	- [ ] Situation familiale
> 	- [ ] Activité professionnelle actuelle
> 	- [ ] Conditions de vie
> 	- [ ] Antécédents judiciaires
> - [ ] **55. Facteurs de risque cardiovasculaire *(3 grilles sur 5)***
> 	- [ ] Hypertension artérielle *(2 grilles sur 5)*
> 	- [ ] Diabète *(2 grilles sur 5)*
> 	- [ ] Dyslipidémie *(2 grilles sur 5)*
> 	- [ ] Antécédents familiaux cardiovasculaires *(2 grilles sur 5)*
> 	- [ ] Tabagisme *(2 grilles sur 5)*
> 	- [ ] Sédentarité *(1 grille sur 5)*
> 	- [ ] Surpoids *(1 grille sur 5)*
> 	- [ ] Stress professionnel *(1 grille sur 5)*
> 	- [ ] Antécédents familiaux *(1 grille sur 5)*
> - [ ] **56. Symptômes d'insuffisance cardiaque *(BPCO)***
> 	- [ ] Œdèmes des membres inférieurs
> 	- [ ] Prise de poids récente
> 	- [ ] Nycturie
> 	- [ ] Fatigue inhabituelle
> - [ ] **57. Motif de consultation *(1 grille sur 5)***
> - [ ] **58. Œdèmes des membres inférieurs *(1 grille sur 5)***
> 	- [ ] Apparition progressive
> 	- [ ] Bilatéraux et symétriques
> 	- [ ] Prennent le godet
> 	- [ ] Plus importants le soir
> 	- [ ] Diminution le matin
> 	- [ ] Prise de poids
> - [ ] **59. Symptômes associés *(1 grille sur 5)***
> 	- [ ] Fatigue importante
> 	- [ ] Toux sèche nocturne
> 	- [ ] Palpitations
> 	- [ ] Nycturie
> - [ ] **60. Classification NYHA *(1 grille sur 5)***
> 	- [ ] Classe I: Pas de limitation
> 	- [ ] Classe II: Limitation légère
> 	- [ ] Classe III: Limitation marquée
> 	- [ ] Classe IV: Symptômes au repos
> - [ ] **61. Antécédents cardiovasculaires *(1 grille sur 5)***
> 	- [ ] Hypertension artérielle
> 	- [ ] Infarctus du myocarde
> 	- [ ] Angioplastie coronaire
> 	- [ ] Dyslipidémie
> 	- [ ] Diabète type 2
> - [ ] **62. Traitement actuel *(1 grille sur 5)***
> 	- [ ] IEC (ramipril 5mg/j)
> 	- [ ] Bêtabloquant (bisoprolol 5mg/j)
> 	- [ ] Statine (atorvastatine 40mg/j)
> - [ ] **63. Recherche d'éléments discriminants cardiaques vs respiratoires *(1 grille sur 5)***
> 	- [ ] Éléments cardiaques
> 	- [ ] Éléments respiratoires
> 	- [ ] Prise de poids récente
> 	- [ ] Position de sommeil
> 	- [ ] Tolérance à l'effort antérieure
> - [ ] **64. Symptômes associés cardiovasculaires *(1 grille sur 5)***
> 	- [ ] Douleurs thoraciques
> 	- [ ] Palpitations
> 	- [ ] Syncopes ou lipothymies
> 	- [ ] Claudication intermittente
> 	- [ ] Œdèmes membres inférieurs
> - [ ] **65. Symptômes associés respiratoires *(1 grille sur 5)***
> 	- [ ] Toux chronique
> 	- [ ] Expectorations
> 	- [ ] Hémoptysie
> 	- [ ] Sifflements respiratoires
> 	- [ ] Infections respiratoires récurrentes
> - [ ] **66. Antécédents médicaux pertinents *(1 grille sur 5)***
> 	- [ ] Pathologies cardiaques préexistantes
> 	- [ ] Pathologies respiratoires
> 	- [ ] Hospitalisations antérieures
> 	- [ ] Interventions chirurgicales
> 	- [ ] Allergies médicamenteuses
> - [ ] **67. Habitudes et mode de vie *(1 grille sur 5)***
> 	- [ ] Tabac
> 	- [ ] Alcool
> 	- [ ] Activité physique
> 	- [ ] Médicaments actuels
> 	- [ ] Expositions professionnelles
> - [ ] **68. Contexte psychosocial *(1 grille sur 5)***
> 	- [ ] Situation professionnelle
> 	- [ ] Situation financière
> 	- [ ] Isolement social
> 	- [ ] Stress et anxiété
> 	- [ ] Observance thérapeutique potentielle
> - [ ] **69. Intégration anamnèse cardio-respiratoire *(1 grille sur 5)***

> [!tip] 🩺 Status
> - [ ] **1. Palpation *(1 grille sur 5)***
> - [ ] **2. Inspection *(1 grille sur 5)***
> - [ ] **3. Comparaison de la circonférence *(1 grille sur 5)***
> - [ ] **4. Inspection du thorax *(1 grille sur 5)***
> - [ ] **5. Vibrations vocales *(1 grille sur 5)***
> - [ ] **6. Percussion du thorax *(1 grille sur 5)***
> - [ ] **7. Auscultation pulmonaire *(2 grilles sur 5)***
> 	- [ ] Râles crépitants bilatéraux *(1 grille sur 5)*
> 	- [ ] Diminution du murmure vésiculaire *(1 grille sur 5)*
> 	- [ ] Matité des bases *(1 grille sur 5)*
> - [ ] **8. Auscultation cardiaque *(2 grilles sur 5)***
> 	- [ ] Bruits du cœur assourdis *(1 grille sur 5)*
> 	- [ ] Galop (B3) *(1 grille sur 5)*
> 	- [ ] Souffle systolique d'insuffisance mitrale *(1 grille sur 5)*
> - [ ] **9. Palpation du pouls *(1 grille sur 5)***
> - [ ] **10. Veines jugulaires *(1 grille sur 5)***
> - [ ] **11. Reflux hépato-jugulaire *(1 grille sur 5)***
> - [ ] **12. Contrôle de la plaie *(1 grille sur 5)***
> - [ ] **13. Contrôle d'hématome *(1 grille sur 5)***
> - [ ] **14. Examen cardiaque *(Asthme)***
> 	- [ ] Palpation du choc de pointe
> 	- [ ] Auscultation cardiaque systématique
> 	- [ ] Recherche de souffles
> 	- [ ] Rythme et fréquence
> - [ ] **15. Examen pulmonaire - Inspection *(Asthme)***
> 	- [ ] Symétrie des mouvements respiratoires
> 	- [ ] Utilisation des muscles accessoires
> 	- [ ] Type de respiration
> 	- [ ] Déformations thoraciques
> - [ ] **16. Examen pulmonaire - Palpation *(Asthme)***
> 	- [ ] Vibrations vocales (frémitus)
> 	- [ ] Points douloureux
> 	- [ ] Ampliation thoracique
> 	- [ ] Adénopathies sus-claviculaires
> - [ ] **17. Examen pulmonaire - Percussion *(Asthme)***
> 	- [ ] Percussion systématique
> 	- [ ] Détermination des bases pulmonaires
> 	- [ ] Recherche de matité
> 	- [ ] Comparaison bilatérale
> - [ ] **18. Examen pulmonaire - Auscultation *(Asthme)***
> 	- [ ] Auscultation antérieure systématique
> 	- [ ] Auscultation postérieure systématique
> 	- [ ] Identification de sibilants
> 	- [ ] Bronchophonie
> - [ ] **19. Examen des extrémités *(Asthme)***
> 	- [ ] Recherche d'hippocratisme digital
> 	- [ ] Recherche de cyanose
> 	- [ ] État des ongles
> 	- [ ] Temps de recoloration capillaire
> - [ ] **20. Examen ORL succinct *(Asthme)***
> 	- [ ] Inspection de la gorge
> 	- [ ] Examen des oreilles
> 	- [ ] Examen du nez
> 	- [ ] État de la muqueuse
> - [ ] **21. Palpation des aires ganglionnaires *(Asthme)***
> 	- [ ] Ganglions cervicaux
> 	- [ ] Ganglions sous-mandibulaires
> 	- [ ] Ganglions sus-claviculaires
> 	- [ ] Ganglions axillaires
> - [ ] **22. Inspection générale et pulmonaire *(BPCO)***
> 	- [ ] État général du patient
> 	- [ ] Coloration cutanée
> 	- [ ] Morphologie thoracique
> 	- [ ] Type de respiration
> 	- [ ] Fréquence respiratoire
> - [ ] **23. Palpation thoracique *(BPCO)***
> 	- [ ] Vibrations vocales
> 	- [ ] Ampliation thoracique
> 	- [ ] Points douloureux
> 	- [ ] Déformations
> - [ ] **24. Auscultation pulmonaire systématique *(BPCO)***
> 	- [ ] Auscultation antérieure complète
> 	- [ ] Auscultation postérieure complète
> 	- [ ] Bruits surajoutés
> 	- [ ] Murmure vésiculaire
> - [ ] **25. Évaluation des muscles respiratoires accessoires *(BPCO)***
> 	- [ ] Utilisation des scalènes
> 	- [ ] Utilisation des sterno-cléido-mastoïdiens
> 	- [ ] Respiration abdominale paradoxale
> 	- [ ] Tirage
> - [ ] **26. Recherche de signes d'insuffisance cardiaque droite *(BPCO)***
> 	- [ ] Œdèmes des membres inférieurs
> 	- [ ] Turgescence jugulaire
> 	- [ ] Reflux hépato-jugulaire
> 	- [ ] Hépatomégalie
> - [ ] **27. Recherche de cyanose et modifications des extrémités *(BPCO)***
> 	- [ ] Cyanose péribuccale
> 	- [ ] Cyanose des extrémités
> 	- [ ] Hippocratisme digital
> 	- [ ] Température des extrémités
> - [ ] **28. Examen cardiovasculaire *(BPCO)***
> 	- [ ] Auscultation cardiaque
> 	- [ ] Recherche de signes d'HTAP
> 	- [ ] Pouls périphériques
> 	- [ ] Pression artérielle
> - [ ] **29. Signes vitaux *(1 grille sur 5)***
> 	- [ ] SpO2 94% en air ambiant
> - [ ] **30. Inspection générale *(1 grille sur 5)***
> 	- [ ] Patient en position semi-assise
> 	- [ ] Dyspnée de repos modérée
> 	- [ ] Cyanose légère des extrémités
> 	- [ ] Turgescence jugulaire
> 	- [ ] Reflux hépato-jugulaire
> - [ ] **31. Examen abdominal *(1 grille sur 5)***
> 	- [ ] Hépatomégalie
> 	- [ ] Sensibilité hépatique
> 	- [ ] Ascite modérée
> - [ ] **32. Examen des membres inférieurs *(1 grille sur 5)***
> 	- [ ] Œdèmes bilatéraux prenant le godet
> 	- [ ] Symétriques et blancs
> 	- [ ] Mous et indolores
> 	- [ ] Pouls périphériques présents
> - [ ] **33. Inspection générale intégrée *(1 grille sur 5)***
> 	- [ ] État général
> 	- [ ] Fréquence respiratoire
> 	- [ ] Coloration cutanée
> 	- [ ] Pouls jugulaire
> 	- [ ] Tirage sus-sternal
> 	- [ ] Extrémités
> - [ ] **34. Examen cardiovasculaire - position couchée 45° *(1 grille sur 5)***
> 	- [ ] Inspection aire cardiaque et pouls jugulaire
> 	- [ ] Palpation précordiale et choc de pointe
> 	- [ ] Palpation pouls carotidien
> 	- [ ] Auscultation 4 foyers en décubitus dorsal
> 	- [ ] Recherche B3/B4 en décubitus latéral gauche
> - [ ] **35. Auscultation cardiaque - bruits pathologiques *(1 grille sur 5)***
> 	- [ ] B1 et B2
> 	- [ ] Souffle systolique aortique
> 	- [ ] Souffle systolique mitral
> 	- [ ] Galop B3 ou B4
> 	- [ ] Frottement péricardique
> - [ ] **36. Examen respiratoire - position assise *(1 grille sur 5)***
> 	- [ ] Inspection mouvements respiratoires
> 	- [ ] Inspection forme thorax
> 	- [ ] Palpation ampliation thoracique
> 	- [ ] Palpation vibrations vocales
> 	- [ ] Percussion postérieure et antérieure
> - [ ] **37. Auscultation pulmonaire - bruits pathologiques *(1 grille sur 5)***
> 	- [ ] Murmure vésiculaire
> 	- [ ] Sibilances expiratoires
> 	- [ ] Râles crépitants
> 	- [ ] Ronchi
> 	- [ ] Expiration prolongée
> - [ ] **38. Signes périphériques d'insuffisance cardiaque *(1 grille sur 5)***
> 	- [ ] Œdèmes membres inférieurs
> 	- [ ] Reflux hépato-jugulaire
> 	- [ ] Hépatomégalie
> 	- [ ] Ascite
> 	- [ ] Pouls périphériques
> - [ ] **39. Intégration de l'examen physique *(1 grille sur 5)***
> 	- [ ] Séquence optimale pour confort patient
> 	- [ ] Passage fluide entre positions
> 	- [ ] Examen complet sans répétitions inutiles
> 	- [ ] Éléments prioritaires selon contexte
> - [ ] **40. Technique d'examen intégré cardio-respiratoire *(1 grille sur 5)***
