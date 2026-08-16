---
aliases:
  - "Mémento Dyspnée"
type: memento-ecos-ssp
ssp: "Dyspnée"
specialite: "Pneumologie"
cas: 5
diagnostics: 3
attendus_documentes_ailleurs: 1
attendus_absents_du_corpus: 2
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

# Dyspnée ⭐️

*Pneumologie · 5 grilles · 3 diagnostics documentés · 1 attendu documenté ailleurs · 2 attendus absents du corpus* — [[SSP — Dyspnée]]

> [!abstract] Les 5 grilles fusionnées
> - **AZYGOS-23** — Insuffisance cardiaque (décompensée) `diagnostic-travail` · [grille](<file:///Users/damienfulliquet/Developer/GitHub/grilles-ecos/docs/azygos-grilles/60e62ee5-98b7-4679-91e1-6f82bb0678fe.json>)
> - **German-35** — Asthme `corrige` · [grille](<file:///Users/damienfulliquet/Developer/GitHub/grilles-ecos/cases/german/German-35_-_Dyspne_e_-_Grille_ECOS.html>)
> - **German-36** — BPCO `explicite` · [grille](<file:///Users/damienfulliquet/Developer/GitHub/grilles-ecos/cases/german/German-36_-_Dyspne_e_-_Grille_ECOS.html>)
> - **RESCOS-39** — Insuffisance cardiaque (décompensée) `dd-principal` · [grille](<file:///Users/damienfulliquet/Developer/GitHub/grilles-ecos/cases/rescos/RESCOS-39_-_Dyspne_e_-_Grille_ECOS.html>)
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
> - [ ] **29. Facteurs d'amélioration et d'aggravation *(Asthme · BPCO)***
> 	- [ ] Ce qui améliore *(Asthme)*
> 	- [ ] Ce qui aggrave *(Asthme)*
> 	- [ ] Position particulière *(Asthme)*
> 	- [ ] Influence de l'environnement *(Asthme)*
> 	- [ ] Position assise/debout *(BPCO)*
> 	- [ ] Air frais *(BPCO)*
> 	- [ ] Repos *(BPCO)*
> 	- [ ] Médicaments éventuels *(BPCO)*
> - [ ] **30. Caractéristiques de l'expectoration *(Asthme · BPCO)***
> 	- [ ] Type de toux *(Asthme)*
> 	- [ ] Hémoptysie
> 	- [ ] Moment de survenue *(Asthme)*
> 	- [ ] Association avec la dyspnée *(Asthme)*
> 	- [ ] Aspect *(BPCO)*
> 	- [ ] Quantité *(BPCO)*
> 	- [ ] Odeur *(BPCO)*
> - [ ] **31. Symptômes nocturnes et sommeil *(Asthme)***
> 	- [ ] Réveils nocturnes
> 	- [ ] Dyspnée nocturne
> 	- [ ] Orthopnée
> 	- [ ] Qualité du sommeil
> - [ ] **32. Symptômes associés - ORL et respiratoires *(2 grilles sur 5)***
> 	- [ ] Infections ORL récentes *(Asthme)*
> 	- [ ] Fréquence des infections *(Asthme)*
> 	- [ ] Fièvre *(Asthme)*
> 	- [ ] Rhinorrhée postérieure *(Asthme)*
> 	- [ ] Toux chronique *(1 grille sur 5)*
> 	- [ ] Expectorations *(1 grille sur 5)*
> 	- [ ] Hémoptysie *(1 grille sur 5)*
> 	- [ ] Sifflements respiratoires *(1 grille sur 5)*
> 	- [ ] Infections respiratoires récurrentes *(1 grille sur 5)*
> - [ ] **33. Symptômes associés - État général *(Asthme)***
> 	- [ ] Performance physique
> 	- [ ] Appétit
> 	- [ ] Évolution pondérale
> 	- [ ] Fatigue inhabituelle
> - [ ] **34. Symptômes associés cardiovasculaires *(3 grilles sur 5)***
> 	- [ ] Sensation de corps étranger *(Asthme)*
> 	- [ ] Dysphagie *(Asthme)*
> 	- [ ] Ronflement *(Asthme)*
> 	- [ ] Douleurs thoraciques *(2 grilles sur 5)*
> 	- [ ] Bruits respiratoires *(Asthme)*
> 	- [ ] Fatigue importante *(1 grille sur 5)*
> 	- [ ] Toux sèche nocturne *(1 grille sur 5)*
> 	- [ ] Palpitations *(2 grilles sur 5)*
> 	- [ ] Nycturie *(1 grille sur 5)*
> 	- [ ] Syncopes ou lipothymies *(1 grille sur 5)*
> 	- [ ] Claudication intermittente *(1 grille sur 5)*
> 	- [ ] Œdèmes membres inférieurs *(1 grille sur 5)*
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
> - [ ] **37. Antécédents médicaux personnels *(3 grilles sur 5)***
> 	- [ ] Maladies antérieures *(Asthme)*
> 	- [ ] Problèmes respiratoires antérieurs *(Asthme)*
> 	- [ ] Hospitalisations *(2 grilles sur 5)*
> 	- [ ] Interventions chirurgicales *(2 grilles sur 5)*
> 	- [ ] Maladies chroniques connues *(BPCO)*
> 	- [ ] Pathologies cardiovasculaires *(BPCO)*
> 	- [ ] Autres problèmes de santé *(BPCO)*
> 	- [ ] Chirurgies antérieures *(BPCO)*
> 	- [ ] Pathologies cardiaques préexistantes *(1 grille sur 5)*
> 	- [ ] Pathologies respiratoires *(1 grille sur 5)*
> 	- [ ] Allergies médicamenteuses *(1 grille sur 5)*
> - [ ] **38. Traitements et habitudes *(2 grilles sur 5)***
> 	- [ ] Médicaments actuels *(Asthme)*
> 	- [ ] Tabagisme *(Asthme)*
> 	- [ ] Alcool *(Asthme)*
> 	- [ ] Drogues *(Asthme)*
> 	- [ ] IEC (ramipril 5mg/j) *(1 grille sur 5)*
> 	- [ ] Bêtabloquant (bisoprolol 5mg/j) *(1 grille sur 5)*
> 	- [ ] Statine (atorvastatine 40mg/j) *(1 grille sur 5)*
> - [ ] **39. Allergies détaillées *(Asthme)***
> 	- [ ] Allergies respiratoires
> 	- [ ] Allergies alimentaires
> 	- [ ] Manifestations cutanées
> 	- [ ] Croûtes de lait
> 	- [ ] Diagnostic d'asthme antérieur
> - [ ] **40. Antécédents familiaux *(Asthme · BPCO)***
> 	- [ ] Allergies familiales
> 	- [ ] Maladies respiratoires familiales
> 	- [ ] Asthme familial *(Asthme)*
> 	- [ ] Autres maladies héréditaires *(Asthme)*
> 	- [ ] Cancer bronchique *(BPCO)*
> 	- [ ] Pathologies cardiovasculaires *(BPCO)*
> - [ ] **41. Contexte social et environnemental *(Asthme · BPCO)***
> 	- [ ] Situation familiale
> 	- [ ] Profession *(Asthme)*
> 	- [ ] Projets *(Asthme)*
> 	- [ ] Animaux domestiques *(Asthme)*
> 	- [ ] Activité professionnelle actuelle *(BPCO)*
> 	- [ ] Conditions de vie *(BPCO)*
> 	- [ ] Antécédents judiciaires *(BPCO)*
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
> - [ ] **46. Facteurs déclenchants et aggravants *(BPCO)***
> 	- [ ] Temps froid
> 	- [ ] Tabagisme passif
> 	- [ ] Après refroidissements
> 	- [ ] Effort physique
> 	- [ ] Position couchée
> - [ ] **47. Impact fonctionnel *(BPCO)***
> 	- [ ] Performance physique
> 	- [ ] Activités quotidiennes limitées
> 	- [ ] Qualité de vie
> 	- [ ] Activités abandonnées
> - [ ] **48. Exacerbations et hospitalisations *(BPCO)***
> 	- [ ] Épisodes de bronchite
> 	- [ ] Prise d'antibiotiques
> 	- [ ] Hospitalisations
> 	- [ ] Recours aux urgences
> - [ ] **49. Activités physiques et loisirs *(BPCO)***
> 	- [ ] Sport actuel
> 	- [ ] Activités antérieures
> 	- [ ] Limitations progressives
> 	- [ ] Sédentarité
> - [ ] **50. Habitudes et toxiques *(BPCO)***
> 	- [ ] Tabagisme actif
> 	- [ ] Tentatives d'arrêt
> 	- [ ] Consommation d'alcool
> 	- [ ] Toxicomanie
> - [ ] **51. Allergies et traitements actuels *(BPCO)***
> 	- [ ] Allergies médicamenteuses
> 	- [ ] Intolérances
> 	- [ ] Médicaments actuels
> 	- [ ] Observance thérapeutique
> - [ ] **52. Facteurs de risque cardiovasculaire *(3 grilles sur 5)***
> 	- [ ] Hypertension artérielle *(2 grilles sur 5)*
> 	- [ ] Diabète *(2 grilles sur 5)*
> 	- [ ] Dyslipidémie *(2 grilles sur 5)*
> 	- [ ] Antécédents familiaux cardiovasculaires *(2 grilles sur 5)*
> 	- [ ] Tabagisme *(2 grilles sur 5)*
> 	- [ ] Sédentarité *(1 grille sur 5)*
> 	- [ ] Surpoids *(1 grille sur 5)*
> 	- [ ] Stress professionnel *(1 grille sur 5)*
> 	- [ ] Antécédents familiaux *(1 grille sur 5)*
> - [ ] **53. Symptômes d'insuffisance cardiaque *(BPCO)***
> 	- [ ] Œdèmes des membres inférieurs
> 	- [ ] Prise de poids récente
> 	- [ ] Nycturie
> 	- [ ] Fatigue inhabituelle
> - [ ] **54. Motif de consultation *(1 grille sur 5)***
> - [ ] **55. Œdèmes des membres inférieurs *(1 grille sur 5)***
> 	- [ ] Apparition progressive
> 	- [ ] Bilatéraux et symétriques
> 	- [ ] Prennent le godet
> 	- [ ] Plus importants le soir
> 	- [ ] Diminution le matin
> 	- [ ] Prise de poids
> - [ ] **56. Classification NYHA *(1 grille sur 5)***
> 	- [ ] Classe I: Pas de limitation
> 	- [ ] Classe II: Limitation légère
> 	- [ ] Classe III: Limitation marquée
> 	- [ ] Classe IV: Symptômes au repos
> - [ ] **57. Antécédents cardiovasculaires *(1 grille sur 5)***
> 	- [ ] Hypertension artérielle
> 	- [ ] Infarctus du myocarde
> 	- [ ] Angioplastie coronaire
> 	- [ ] Dyslipidémie
> 	- [ ] Diabète type 2
> - [ ] **58. Recherche d'éléments discriminants cardiaques vs respiratoires *(1 grille sur 5)***
> 	- [ ] Éléments cardiaques
> 	- [ ] Éléments respiratoires
> 	- [ ] Prise de poids récente
> 	- [ ] Position de sommeil
> 	- [ ] Tolérance à l'effort antérieure
> - [ ] **59. Habitudes et mode de vie *(1 grille sur 5)***
> 	- [ ] Tabac
> 	- [ ] Alcool
> 	- [ ] Activité physique
> 	- [ ] Médicaments actuels
> 	- [ ] Expositions professionnelles
> - [ ] **60. Contexte psychosocial *(1 grille sur 5)***
> 	- [ ] Situation professionnelle
> 	- [ ] Situation financière
> 	- [ ] Isolement social
> 	- [ ] Stress et anxiété
> 	- [ ] Observance thérapeutique potentielle
> - [ ] **61. Intégration anamnèse cardio-respiratoire *(1 grille sur 5)***

> [!tip] 🩺 Status
> - [ ] **1. Palpation *(1 grille sur 5)***
> - [ ] **2. Inspection *(1 grille sur 5)***
> - [ ] **3. Inspection (Membres inférieurs) *(1 grille sur 5)***
> - [ ] **4. Palpation (Membres inférieurs) *(1 grille sur 5)***
> - [ ] **5. Comparaison de la circonférence *(1 grille sur 5)***
> - [ ] **6. Inspection du thorax *(1 grille sur 5)***
> - [ ] **7. Vibrations vocales *(1 grille sur 5)***
> - [ ] **8. Percussion du thorax *(1 grille sur 5)***
> - [ ] **9. Auscultation pulmonaire**
> 	- [ ] Auscultation antérieure systématique *(Asthme · BPCO)*
> 	- [ ] Auscultation postérieure systématique *(Asthme · BPCO)*
> 	- [ ] Identification de sibilants *(Asthme)*
> 	- [ ] Bronchophonie *(Asthme)*
> 	- [ ] Bruits surajoutés *(BPCO)*
> 	- [ ] Murmure vésiculaire *(3 grilles sur 5)*
> 	- [ ] Râles crépitants *(2 grilles sur 5)*
> 	- [ ] Matité des bases *(1 grille sur 5)*
> 	- [ ] Pas de sibilants *(1 grille sur 5)*
> 	- [ ] Sibilances expiratoires *(1 grille sur 5)*
> 	- [ ] Ronchi *(1 grille sur 5)*
> 	- [ ] Expiration prolongée *(1 grille sur 5)*
> - [ ] **10. Auscultation cardiaque *(2 grilles sur 5)***
> 	- [ ] Bruits du cœur assourdis *(1 grille sur 5)*
> 	- [ ] Galop (B3) *(1 grille sur 5)*
> 	- [ ] Souffle systolique d'insuffisance mitrale *(1 grille sur 5)*
> 	- [ ] Pas de frottement péricardique *(1 grille sur 5)*
> - [ ] **11. Palpation du pouls *(1 grille sur 5)***
> - [ ] **12. Veines jugulaires *(1 grille sur 5)***
> - [ ] **13. Reflux hépato-jugulaire *(1 grille sur 5)***
> - [ ] **14. Contrôle de la plaie *(1 grille sur 5)***
> - [ ] **15. Contrôle d'hématome *(1 grille sur 5)***
> - [ ] **16. Examen cardiovasculaire *(Asthme · BPCO)***
> 	- [ ] Palpation du choc de pointe *(Asthme)*
> 	- [ ] Auscultation cardiaque
> 	- [ ] Recherche de souffles *(Asthme)*
> 	- [ ] Rythme et fréquence *(Asthme)*
> 	- [ ] Recherche de signes d'HTAP *(BPCO)*
> 	- [ ] Pouls périphériques *(BPCO)*
> 	- [ ] Pression artérielle *(BPCO)*
> - [ ] **17. Examen pulmonaire - Inspection *(Asthme)***
> 	- [ ] Symétrie des mouvements respiratoires
> 	- [ ] Utilisation des muscles accessoires
> 	- [ ] Type de respiration
> 	- [ ] Déformations thoraciques
> - [ ] **18. Examen pulmonaire - Palpation *(Asthme)***
> 	- [ ] Vibrations vocales (frémitus)
> 	- [ ] Points douloureux
> 	- [ ] Ampliation thoracique
> 	- [ ] Adénopathies sus-claviculaires
> - [ ] **19. Examen pulmonaire - Percussion *(Asthme)***
> 	- [ ] Percussion systématique
> 	- [ ] Détermination des bases pulmonaires
> 	- [ ] Recherche de matité
> 	- [ ] Comparaison bilatérale
> - [ ] **20. Examen des extrémités *(Asthme)***
> 	- [ ] Recherche d'hippocratisme digital
> 	- [ ] Recherche de cyanose
> 	- [ ] État des ongles
> 	- [ ] Temps de recoloration capillaire
> - [ ] **21. Examen ORL succinct *(Asthme)***
> 	- [ ] Inspection de la gorge
> 	- [ ] Examen des oreilles
> 	- [ ] Examen du nez
> 	- [ ] État de la muqueuse
> - [ ] **22. Palpation des aires ganglionnaires *(Asthme)***
> 	- [ ] Ganglions cervicaux
> 	- [ ] Ganglions sous-mandibulaires
> 	- [ ] Ganglions sus-claviculaires
> 	- [ ] Ganglions axillaires
> - [ ] **23. Inspection générale et pulmonaire *(3 grilles sur 5)***
> 	- [ ] État général du patient *(BPCO)*
> 	- [ ] Coloration cutanée *(2 grilles sur 5)*
> 	- [ ] Morphologie thoracique *(BPCO)*
> 	- [ ] Type de respiration *(BPCO)*
> 	- [ ] Fréquence respiratoire *(2 grilles sur 5)*
> 	- [ ] Patient en position semi-assise *(1 grille sur 5)*
> 	- [ ] Dyspnée de repos modérée *(1 grille sur 5)*
> 	- [ ] Cyanose légère des extrémités *(1 grille sur 5)*
> 	- [ ] Turgescence jugulaire *(1 grille sur 5)*
> 	- [ ] Reflux hépato-jugulaire *(1 grille sur 5)*
> 	- [ ] État général *(1 grille sur 5)*
> 	- [ ] Pouls jugulaire *(1 grille sur 5)*
> 	- [ ] Tirage sus-sternal *(1 grille sur 5)*
> 	- [ ] Extrémités *(1 grille sur 5)*
> - [ ] **24. Palpation thoracique *(BPCO)***
> 	- [ ] Vibrations vocales
> 	- [ ] Ampliation thoracique
> 	- [ ] Points douloureux
> 	- [ ] Déformations
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
> - [ ] **28. Signes vitaux *(1 grille sur 5)***
> 	- [ ] SpO2 94% en air ambiant
> - [ ] **29. Examen abdominal *(1 grille sur 5)***
> 	- [ ] Hépatomégalie
> 	- [ ] Sensibilité hépatique
> 	- [ ] Ascite modérée
> 	- [ ] Pas de splénomégalie
> - [ ] **30. Examen des membres inférieurs *(1 grille sur 5)***
> 	- [ ] Œdèmes bilatéraux prenant le godet
> 	- [ ] Symétriques et blancs
> 	- [ ] Mous et indolores
> 	- [ ] Pouls périphériques présents
> 	- [ ] Pas de signes de phlébite
> - [ ] **31. Examen cardiovasculaire - position couchée 45° *(1 grille sur 5)***
> 	- [ ] Inspection aire cardiaque et pouls jugulaire
> 	- [ ] Palpation précordiale et choc de pointe
> 	- [ ] Palpation pouls carotidien
> 	- [ ] Auscultation 4 foyers en décubitus dorsal
> 	- [ ] Recherche B3/B4 en décubitus latéral gauche
> - [ ] **32. Auscultation cardiaque - bruits pathologiques *(1 grille sur 5)***
> 	- [ ] B1 et B2
> 	- [ ] Souffle systolique aortique
> 	- [ ] Souffle systolique mitral
> 	- [ ] Galop B3 ou B4
> 	- [ ] Frottement péricardique
> - [ ] **33. Examen respiratoire - position assise *(1 grille sur 5)***
> 	- [ ] Inspection mouvements respiratoires
> 	- [ ] Inspection forme thorax
> 	- [ ] Palpation ampliation thoracique
> 	- [ ] Palpation vibrations vocales
> 	- [ ] Percussion postérieure et antérieure
> - [ ] **34. Signes périphériques d'insuffisance cardiaque *(1 grille sur 5)***
> 	- [ ] Œdèmes membres inférieurs
> 	- [ ] Reflux hépato-jugulaire
> 	- [ ] Hépatomégalie
> 	- [ ] Ascite
> 	- [ ] Pouls périphériques
> - [ ] **35. Intégration de l'examen physique *(1 grille sur 5)***
> 	- [ ] Séquence optimale pour confort patient
> 	- [ ] Passage fluide entre positions
> 	- [ ] Examen complet sans répétitions inutiles
> 	- [ ] Éléments prioritaires selon contexte
> - [ ] **36. Technique d'examen intégré cardio-respiratoire *(1 grille sur 5)***

> [!success] 💊 Management — partagé par plusieurs diagnostics
> - [ ] **1. Diagnostics différentiels *(3 grilles sur 5)* — *Asthme · BPCO · Insuffisance cardiaque (décompensée)***

> [!success] 💊 Management — si Asthme
> - [ ] **1. Diagnostic principal**
> 	- [ ] Asthme d'effort / asthme induit par l'exercice
> 	- [ ] Justification du diagnostic
> 	- [ ] Éléments cliniques en faveur
> 	- [ ] Terrain atopique
> - [ ] **2. Examens complémentaires - Fonction respiratoire**
> 	- [ ] Spirométrie
> 	- [ ] Test de réversibilité aux bêta-2 mimétiques
> 	- [ ] Test de provocation si nécessaire
> 	- [ ] Peak-flow en ambulatoire
> - [ ] **3. Examens complémentaires - Imagerie et biologie**
> 	- [ ] Radiographie thoracique
> 	- [ ] FSC avec éosinophiles
> 	- [ ] IgE totales et spécifiques
> 	- [ ] Tests cutanés allergologiques
> - [ ] **4. Traitement médicamenteux proposé**
> 	- [ ] Bêta-2 mimétiques à courte durée d'action à la demande
> 	- [ ] Technique d'inhalation
> 	- [ ] Utilisation avant l'effort
> 	- [ ] Plan d'action en cas de crise
> - [ ] **5. Traitement de fond éventuel**
> 	- [ ] Corticoïdes inhalés si symptômes fréquents
> 	- [ ] Association fixe si besoin
> 	- [ ] Adaptation selon contrôle
> 	- [ ] Réévaluation régulière
> - [ ] **6. Mesures non médicamenteuses**
> 	- [ ] Éviction des allergènes identifiés
> 	- [ ] Arrêt du tabac (accompagnement)
> 	- [ ] Échauffement avant l'effort
> 	- [ ] Éducation thérapeutique
> - [ ] **7. Planification du suivi**
> 	- [ ] Rendez-vous de contrôle
> 	- [ ] Surveillance de l'efficacité
> 	- [ ] Ajustement thérapeutique
> 	- [ ] Orientation pneumologique si besoin

> [!success] 💊 Management — si BPCO
> - [ ] **1. Diagnostic principal**
> 	- [ ] BPCO légère (GOLD stade I)
> 	- [ ] Justification clinique
> 	- [ ] Facteurs de risque identifiés
> 	- [ ] Présentation typique
> - [ ] **2. Examens complémentaires - Fonction respiratoire**
> 	- [ ] Test de réversibilité aux bêta-2 mimétiques
> 	- [ ] Spirométrie complète
> 	- [ ] Gazométrie artérielle
> 	- [ ] Test de marche de 6 minutes
> - [ ] **3. Traitement médicamenteux proposé**
> 	- [ ] Technique d'inhalation
> 	- [ ] Bêta-2 agoniste de courte durée d'action (SABA)
> 	- [ ] Anticholinergique de courte durée d'action (SAMA)
> 	- [ ] Association éventuelle
> - [ ] **4. Mesures non médicamenteuses**
> 	- [ ] Sevrage tabagique (priorité absolue)
> 	- [ ] Vaccination antigrippale et antipneumococcique
> 	- [ ] Réhabilitation respiratoire
> 	- [ ] Activité physique adaptée
> - [ ] **5. Planification du suivi**
> 	- [ ] Consultation de contrôle
> 	- [ ] Surveillance spirométrique
> 	- [ ] Éducation thérapeutique
> 	- [ ] Plan d'action en cas d'exacerbation
> - [ ] **6. Examens complémentaires - Microbiologie et imagerie**
> 	- [ ] Culture des crachats (ECBC)
> 	- [ ] Radiographie thoracique
> 	- [ ] Scanner thoracique si indiqué
> 	- [ ] ECG
> - [ ] **7. Interprétation correcte de la spirométrie**
> 	- [ ] Classification GOLD stade I
> 	- [ ] VEMS < 80% de la valeur prédite
> 	- [ ] VEMS/CVF < 70%
> 	- [ ] Absence de réversibilité significative
> - [ ] **8. Prise en charge des comorbidités**
> 	- [ ] Suivi du programme méthadone
> 	- [ ] Dépistage des complications
> 	- [ ] Support psychosocial
> 	- [ ] Prévention des exacerbations

> [!success] 💊 Management — si Bronchiolite
> *Aucune grille du corpus ne documente ce diagnostic* — il est pourtant attendu de cette SSP. **Trou de révision à combler ailleurs.**

> [!success] 💊 Management — si Embolie pulmonaire
> *Aucune grille de cette SSP ne documente ce diagnostic* — mais le corpus le documente ailleurs : [[Mémento — Douleur Thoracique]] (3 grilles) · [[Mémento — Douleur du Membre Inférieur]] (1 grille).

> [!success] 💊 Management — si Insuffisance cardiaque (décompensée)
> - [ ] **1. Laboratoire *(1 grille sur 3)***
> - [ ] **2. Formule sanguine *(1 grille sur 3)***
> - [ ] **3. GSA *(1 grille sur 3)***
> - [ ] **4. Radiographie du thorax AP au lit *(1 grille sur 3)***
> - [ ] **5. Résultat *(1 grille sur 3)***
> - [ ] **6. Hypothèse diagnostique *(1 grille sur 3)***
> - [ ] **7. Oxygénothérapie *(1 grille sur 3)***
> - [ ] **8. Traitement diurétique *(1 grille sur 3)***
> - [ ] **9. Diminution de la précharge *(1 grille sur 3)***
> - [ ] **10. Bilan hydrique *(1 grille sur 3)***
> - [ ] **11. Suivi de l'évolution *(1 grille sur 3)***
> - [ ] **12. Réévaluation *(1 grille sur 3)***
> - [ ] **13. Contrôle biologique *(1 grille sur 3)***
> - [ ] **14. Relais *(1 grille sur 3)***
> - [ ] **15. Diagnostic principal *(1 grille sur 3)***
> 	- [ ] Insuffisance cardiaque décompensée
> 	- [ ] Sténose aortique sévère
> 	- [ ] Insuffisance mitrale modérée
> 	- [ ] Dysfonction VG sévère
> 	- [ ] Possible syndrome obstructif associé
> - [ ] **16. Examens complémentaires - Fonction respiratoire *(1 grille sur 3)***
> 	- [ ] Spirométrie
> 	- [ ] Gazométrie artérielle
> 	- [ ] Test de marche de 6 minutes
> 	- [ ] Scanner thoracique si indication
> 	- [ ] Polysomnographie si suspicion SAOS
> - [ ] **17. Examens complémentaires cardiaques *(2 grilles sur 3)***
> 	- [ ] ECG 12 dérivations *(1 grille sur 3)*
> 	- [ ] Radiographie thoracique
> 	- [ ] BNP ou NT-proBNP
> 	- [ ] Échocardiographie transthoracique *(1 grille sur 3)*
> 	- [ ] Bilan biologique: FSC, ionogramme, créatinine, BNP *(1 grille sur 3)*
> 	- [ ] Troponines si suspicion de SCA *(1 grille sur 3)*
> 	- [ ] Gazométrie artérielle si dyspnée sévère *(1 grille sur 3)*
> 	- [ ] ECG *(1 grille sur 3)*
> 	- [ ] Échocardiographie *(1 grille sur 3)*
> 	- [ ] Coronarographie si chirurgie envisagée *(1 grille sur 3)*
> - [ ] **18. Critères diagnostiques d'insuffisance cardiaque *(1 grille sur 3)***
> 	- [ ] Critères de Framingham majeurs
> 	- [ ] Dyspnée paroxystique nocturne
> 	- [ ] Turgescence jugulaire
> 	- [ ] Râles crépitants
> 	- [ ] Cardiomégalie radiologique
> 	- [ ] Œdème aigu du poumon
> 	- [ ] Galop B3
> 	- [ ] Reflux hépato-jugulaire
> - [ ] **19. Prise en charge de l'insuffisance cardiaque *(2 grilles sur 3)***
> - [ ] **20. Signes d'alarme (red flags) *(1 grille sur 3)***
> 	- [ ] Œdème aigu du poumon
> 	- [ ] Choc cardiogénique
> 	- [ ] Syndrome coronarien aigu
> 	- [ ] Arythmie ventriculaire
> 	- [ ] Insuffisance rénale aiguë
> - [ ] **21. Éducation thérapeutique *(1 grille sur 3)***
> 	- [ ] Reconnaissance des signes d'alarme
> 	- [ ] Importance de l'observance thérapeutique
> 	- [ ] Auto-surveillance du poids
> 	- [ ] Régime pauvre en sel
> 	- [ ] Limitation des apports hydriques
> 	- [ ] Activité physique régulière adaptée
> - [ ] **22. Diagnostic différentiel dyspnée cardio-pulmonaire *(1 grille sur 3)***
> - [ ] **23. Prise en charge respiratoire *(1 grille sur 3)***
> 	- [ ] Oxygénothérapie si hypoxémie
> 	- [ ] Bronchodilatateurs si obstruction
> 	- [ ] Sevrage tabagique impératif
> 	- [ ] Kinésithérapie respiratoire
> 	- [ ] Vaccination grippe/pneumocoque
> - [ ] **24. Surveillance et critères d'hospitalisation *(1 grille sur 3)***
> 	- [ ] Hospitalisation pour décompensation aiguë
> 	- [ ] Monitoring poids quotidien
> 	- [ ] Surveillance diurèse et ionogramme
> 	- [ ] Évaluation pré-opératoire si chirurgie
> 	- [ ] Suivi multidisciplinaire cardio-pneumo
> - [ ] **25. Aspects psychosociaux et éducation *(1 grille sur 3)***
> 	- [ ] Soutien psychologique
> 	- [ ] Aide sociale
> 	- [ ] Éducation thérapeutique
> 	- [ ] Aménagement domicile si besoin
> 	- [ ] Coordination avec médecin traitant
> - [ ] **26. Management intégré cardio-respiratoire *(1 grille sur 3)***

> [!success] 💊 Management — si Tachycardie supraventriculaire (TSV/WPW)
> *Aucune grille du corpus ne documente ce diagnostic* — il est pourtant attendu de cette SSP. **Trou de révision à combler ailleurs.**
