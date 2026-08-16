---
aliases:
  - "Mémento Douleur d'Épaule"
type: memento-ecos-ssp
ssp: "Douleur d'Épaule"
specialite: "Musculo-Squelettique"
cas: 5
diagnostics: 4
attendus_documentes_ailleurs: 0
attendus_absents_du_corpus: 0
tags:
  - ecos/memento
  - ecos/grille-officielle
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

> [!warning] Mémento mixte — 1 grille officielle, 4 non officielles
> **RESCOS-69b** fait partie des **neuf grilles officielles** et fait donc
> autorité ; elle est signalée ⭐️ dans l'encadré ci-dessous. Les 4
> autres sont des grilles d'entraînement (RESCOS, AMBOSS, GERMAN, AZYGOS)
> qu'aucun jury n'a validées.
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

# Douleur d'Épaule

*Musculo-Squelettique · 5 grilles · 4 diagnostics documentés* — [[SSP — Douleur d'Épaule]]

> [!abstract] Les 5 grilles fusionnées
> - **AMBOSS-39** — Rupture de la coiffe des rotateurs `premier-dd` · [grille](<file:///Users/damienfulliquet/Developer/GitHub/grilles-ecos/cases/amboss/AMBOSS-39_-_Douleur_a__l_e_paule_-_Homme_52_ans_-_Grille_ECOS.html>)
> - **AZYGOS-11** — Syndrome sous-acromial droit (tendinopathie du sus-épineux) `diagnostic-travail` · [grille](<file:///Users/damienfulliquet/Developer/GitHub/grilles-ecos/docs/azygos-grilles/372c9d2d-27ec-47f3-b054-fab2f75f3c56.json>)
> - **German-27** — Syndrome de conflit sous-acromial `corrige` · [grille](<file:///Users/damienfulliquet/Developer/GitHub/grilles-ecos/cases/german/German-27_-_Douleur_a__l_e_paule_-_Grille_ECOS.html>)
> - **RESCOS-69** — Fracture du membre supérieur (humérus, tête radiale) `explicite` · [grille](<file:///Users/damienfulliquet/Developer/GitHub/grilles-ecos/cases/rescos/RESCOS-69%20-%20Traumatisme%20MS%20-%20Grille%20ECOS.html>)
> - **RESCOS-69b** ⭐️ **officielle** — Fracture du membre supérieur (humérus, tête radiale) `explicite` · [grille](<file:///Users/damienfulliquet/Developer/GitHub/grilles-ecos/cases/rescos/RESCOS-69b%20-%20Traumatisme%20MS%20-%20Basketteur%2025%20ans%20-%20Grille%20ECOS.html>)

> [!note] 📋 Anamnèse
> - [ ] **1. Motif principal *(Rupture de la coiffe des rotateurs)***
> - [ ] **2. Caractérisation de la douleur à l'épaule *(Rupture de la coiffe des rotateurs)***
> 	- [ ] Localisation
> 	- [ ] Intensité (sur une échelle de 0-10)
> 	- [ ] Qualité
> 	- [ ] Début
> 	- [ ] Événements précipitants
> 	- [ ] Progression/constante/intermittente
> 	- [ ] Épisodes antérieurs
> 	- [ ] Irradiation
> 	- [ ] Facteurs améliorants
> 	- [ ] Facteurs aggravants
> 	- [ ] Symptômes associés
> - [ ] **3. Recherche de symptômes spécifiques pour douleur à l'épaule *(Rupture de la coiffe des rotateurs)***
> 	- [ ] Traumatisme
> 	- [ ] Fièvre/frissons
> 	- [ ] Éruption cutanée/changements cutanés
> 	- [ ] Douleur thoracique
> 	- [ ] Essoufflement
> 	- [ ] Douleurs articulaires
> 	- [ ] Problèmes de sommeil
> 	- [ ] Infections récentes
> 	- [ ] Faiblesse des membres supérieurs
> 	- [ ] Mouvements limités des membres supérieurs
> 	- [ ] Gonflement de l'épaule
> 	- [ ] Altération de la sensation dans les membres supérieurs
> - [ ] **4. Antécédents médicaux *(Rupture de la coiffe des rotateurs · Syndrome de conflit sous-acromial · Syndrome sous-acromial droit (tendinopathie du sus-épineux))***
> 	- [ ] Pathologies rhumatologiques *(Syndrome de conflit sous-acromial)*
> 	- [ ] Autres maladies chroniques *(Syndrome de conflit sous-acromial)*
> - [ ] **5. Allergies *(Rupture de la coiffe des rotateurs · Syndrome sous-acromial droit (tendinopathie du sus-épineux))***
> - [ ] **6. Médicaments actuels *(Rupture de la coiffe des rotateurs · Syndrome de conflit sous-acromial · Syndrome sous-acromial droit (tendinopathie du sus-épineux))***
> - [ ] **7. Hospitalisations et antécédents chirurgicaux *(Rupture de la coiffe des rotateurs)***
> 	- [ ] Hospitalisations
> 	- [ ] Antécédents chirurgicaux
> - [ ] **8. Antécédents familiaux *(Rupture de la coiffe des rotateurs · Syndrome de conflit sous-acromial · Syndrome sous-acromial droit (tendinopathie du sus-épineux))***
> - [ ] **9. Habitudes et mode de vie *(Rupture de la coiffe des rotateurs · Syndrome de conflit sous-acromial)***
> 	- [ ] Travail *(Rupture de la coiffe des rotateurs)*
> 	- [ ] Domicile *(Rupture de la coiffe des rotateurs)*
> 	- [ ] Alcool
> 	- [ ] Drogues récréatives *(Rupture de la coiffe des rotateurs)*
> 	- [ ] Tabac
> 	- [ ] Exercice *(Rupture de la coiffe des rotateurs)*
> 	- [ ] Autres toxiques *(Syndrome de conflit sous-acromial)*
> - [ ] **10. Question d’entrée *(Syndrome sous-acromial droit (tendinopathie du sus-épineux))***
> - [ ] **11. Dynamique temporelle *(Syndrome sous-acromial droit (tendinopathie du sus-épineux))***
> - [ ] **12. Début / durée *(Syndrome sous-acromial droit (tendinopathie du sus-épineux))***
> - [ ] **13. Mode d’apparition *(Syndrome sous-acromial droit (tendinopathie du sus-épineux))***
> - [ ] **14. Évolution *(Syndrome sous-acromial droit (tendinopathie du sus-épineux))***
> - [ ] **15. Déclencheurs *(Syndrome sous-acromial droit (tendinopathie du sus-épineux))***
> - [ ] **16. Charge particulière *(Syndrome sous-acromial droit (tendinopathie du sus-épineux))***
> - [ ] **17. Traumatisme / chute *(Syndrome sous-acromial droit (tendinopathie du sus-épineux))***
> - [ ] **18. Localisation *(Syndrome sous-acromial droit (tendinopathie du sus-épineux))***
> - [ ] **19. Irradiation *(Syndrome sous-acromial droit (tendinopathie du sus-épineux))***
> - [ ] **20. Caractère de la douleur *(Syndrome sous-acromial droit (tendinopathie du sus-épineux))***
> - [ ] **21. Intensité *(Syndrome sous-acromial droit (tendinopathie du sus-épineux))***
> - [ ] **22. Facteurs aggravants *(Syndrome sous-acromial droit (tendinopathie du sus-épineux))***
> - [ ] **23. Mouvements au-dessus de la tête *(Syndrome sous-acromial droit (tendinopathie du sus-épineux))***
> - [ ] **24. Position *(Syndrome sous-acromial droit (tendinopathie du sus-épineux))***
> - [ ] **25. Facteurs soulageants *(Syndrome sous-acromial droit (tendinopathie du sus-épineux))***
> - [ ] **26. Essais de traitement *(Syndrome sous-acromial droit (tendinopathie du sus-épineux))***
> - [ ] **27. Retentissement *(Syndrome sous-acromial droit (tendinopathie du sus-épineux))***
> - [ ] **28. Symptômes associés *(Fracture du membre supérieur (humérus, tête radiale) · Syndrome sous-acromial droit (tendinopathie du sus-épineux))***
> 	- [ ] Perte de sensibilité ou paresthésies du MSD *(Fracture du membre supérieur (humérus, tête radiale))*
> - [ ] **29. Latéralité du membre supérieur *(Syndrome sous-acromial droit (tendinopathie du sus-épineux))***
> - [ ] **30. Fièvre aiguë / frissons *(Syndrome sous-acromial droit (tendinopathie du sus-épineux))***
> - [ ] **31. Signes inflammatoires *(Syndrome sous-acromial droit (tendinopathie du sus-épineux))***
> - [ ] **32. Rougeur *(Syndrome sous-acromial droit (tendinopathie du sus-épineux))***
> - [ ] **33. Gonflement *(Syndrome sous-acromial droit (tendinopathie du sus-épineux))***
> - [ ] **34. Chaleur locale *(Syndrome sous-acromial droit (tendinopathie du sus-épineux))***
> - [ ] **35. Sensibilité *(Syndrome sous-acromial droit (tendinopathie du sus-épineux))***
> - [ ] **36. Motricité / faiblesse *(Syndrome sous-acromial droit (tendinopathie du sus-épineux))***
> - [ ] **37. Raideur matinale *(Syndrome sous-acromial droit (tendinopathie du sus-épineux))***
> - [ ] **38. Douleurs dorsales / cervicales *(Syndrome sous-acromial droit (tendinopathie du sus-épineux))***
> - [ ] **39. Autres douleurs articulaires *(Syndrome sous-acromial droit (tendinopathie du sus-épineux))***
> - [ ] **40. Symptomatologie B *(Syndrome sous-acromial droit (tendinopathie du sus-épineux))***
> - [ ] **41. Lésions antérieures *(Syndrome sous-acromial droit (tendinopathie du sus-épineux))***
> - [ ] **42. Prise en charge antérieure *(Syndrome sous-acromial droit (tendinopathie du sus-épineux))***
> - [ ] **43. Antécédents chirurgicaux *(Syndrome de conflit sous-acromial · Syndrome sous-acromial droit (tendinopathie du sus-épineux))***
> 	- [ ] Chirurgies antérieures *(Syndrome de conflit sous-acromial)*
> 	- [ ] Chirurgie thyroïdienne *(Syndrome de conflit sous-acromial)*
> - [ ] **44. Noxes *(Syndrome sous-acromial droit (tendinopathie du sus-épineux))***
> - [ ] **45. Tabac *(Syndrome sous-acromial droit (tendinopathie du sus-épineux))***
> - [ ] **46. Alcool *(Syndrome sous-acromial droit (tendinopathie du sus-épineux))***
> - [ ] **47. Drogues *(Syndrome sous-acromial droit (tendinopathie du sus-épineux))***
> - [ ] **48. Profession *(Syndrome sous-acromial droit (tendinopathie du sus-épineux))***
> - [ ] **49. Sport / loisir *(Syndrome sous-acromial droit (tendinopathie du sus-épineux))***
> - [ ] **50. Présentation avec nom, fonction et objectif de la consultation *(Syndrome de conflit sous-acromial)***
> - [ ] **51. Question ouverte pour identifier le motif de consultation *(Syndrome de conflit sous-acromial)***
> - [ ] **52. Caractérisation temporelle de la douleur *(Syndrome de conflit sous-acromial)***
> 	- [ ] Début
> 	- [ ] Évolution
> - [ ] **53. Recherche de symptômes inflammatoires *(Syndrome de conflit sous-acromial)***
> 	- [ ] Raideur matinale
> 	- [ ] Paresthésies associées
> - [ ] **54. Impact sur le sommeil *(Syndrome de conflit sous-acromial)***
> 	- [ ] Réveils nocturnes
> 	- [ ] Position de sommeil
> - [ ] **55. Facteurs modulant la douleur *(Syndrome de conflit sous-acromial)***
> 	- [ ] Facteurs aggravants
> 	- [ ] Facteurs améliorants
> 	- [ ] Repos vs mouvement
> - [ ] **56. Recherche d'événements déclenchants *(Syndrome de conflit sous-acromial)***
> 	- [ ] Traumatisme
> 	- [ ] Infection récente
> - [ ] **57. Symptômes généraux *(Syndrome de conflit sous-acromial)***
> 	- [ ] Symptômes B (fièvre, sueurs nocturnes, perte de poids)
> 	- [ ] Fatigue
> 	- [ ] État général
> - [ ] **58. Automédication et traitements essayés *(Syndrome de conflit sous-acromial)***
> - [ ] **59. Contexte social et professionnel *(Syndrome de conflit sous-acromial)***
> 	- [ ] Profession
> 	- [ ] Situation familiale
> 	- [ ] Enfants
> - [ ] **60. Retentissement fonctionnel *(Syndrome de conflit sous-acromial)***
> 	- [ ] Impact professionnel
> 	- [ ] Gêne quotidienne
> 	- [ ] Qualité de vie
> - [ ] **61. Synthèse et questions de la patiente *(Syndrome de conflit sous-acromial)***
> 	- [ ] Résumé des points clés
> 	- [ ] Questions de la patiente
> - [ ] **62. Moment et le lieu *(Fracture du membre supérieur (humérus, tête radiale))***
> 	- [ ] Les deux *(1 grille sur 5)*
> - [ ] **63. Déroulement *(Fracture du membre supérieur (humérus, tête radiale))***
> 	- [ ] Personnes impliquées
> 	- [ ] Mécanisme du traumatisme
> 	- [ ] Les 2 *(1 grille sur 5)*
> - [ ] **64. Demande concernant autre lésion traumatique (coup) *(Fracture du membre supérieur (humérus, tête radiale))***
> 	- [ ] Cérébrale
> 	- [ ] Abdominale
> 	- [ ] Thoracique
> 	- [ ] Autre
> - [ ] **65. Douleurs *(Fracture du membre supérieur (humérus, tête radiale))***
> 	- [ ] Localisation
> 	- [ ] Intensité
> 	- [ ] Évolution
> 	- [ ] Facteurs aggravant/atténuant *(1 grille sur 5)*
> 	- [ ] Médicaments pris ou reçus
> 	- [ ] Caractère
> 	- [ ] Facteurs aggravant *(1 grille sur 5)*
> 	- [ ] Facteurs atténuant *(1 grille sur 5)*
> - [ ] **66. Douleurs ailleurs *(Fracture du membre supérieur (humérus, tête radiale))***
> - [ ] **67. Propose une antalgie *(Fracture du membre supérieur (humérus, tête radiale))***
> - [ ] **68. Prise d'alcool ou drogue ce soir là *(Fracture du membre supérieur (humérus, tête radiale))***
> 	- [ ] Les deux *(1 grille sur 5)*
> - [ ] **69. Antécédents médicaux/chirurgicaux/médicaments/allergie/vaccins *(Fracture du membre supérieur (humérus, tête radiale))***
> 	- [ ] Au moins 3 *(1 grille sur 5)*
> 	- [ ] Un *(1 grille sur 5)*
> - [ ] **70. Contexte d'harcèlement de son équipier/-ère *(Fracture du membre supérieur (humérus, tête radiale))***

> [!tip] 🩺 Status
> - [ ] **1. Mesures d'hygiène *(Rupture de la coiffe des rotateurs)***
> 	- [ ] Lavage des mains
> 	- [ ] Respect de la pudeur avec drap
> - [ ] **2. Examen des extrémités *(Rupture de la coiffe des rotateurs)***
> 	- [ ] Inspection des membres supérieurs
> 	- [ ] Palpation du pouls radial
> 	- [ ] Inspection de la région de l'épaule
> 	- [ ] Palpation de la région de l'épaule
> 	- [ ] Examen ciblé des mouvements passifs et actifs des membres supérieurs
> 	- [ ] Examen ciblé de la sensibilité des membres supérieurs
> 	- [ ] Examen ciblé des réflexes ostéotendineux des membres supérieurs
> - [ ] **3. Tests spécifiques de l'épaule *(Rupture de la coiffe des rotateurs)***
> 	- [ ] Test de l'arc douloureux
> 	- [ ] Test de Neer
> 	- [ ] Test de Jobe
> - [ ] **4. Inspection *(Syndrome sous-acromial droit (tendinopathie du sus-épineux))***
> - [ ] **5. Palpation *(Syndrome sous-acromial droit (tendinopathie du sus-épineux))***
> - [ ] **6. Structures osseuses *(Syndrome sous-acromial droit (tendinopathie du sus-épineux))***
> - [ ] **7. Espace sous-acromial *(Syndrome sous-acromial droit (tendinopathie du sus-épineux))***
> - [ ] **8. Corps musculaires et tendons *(Syndrome sous-acromial droit (tendinopathie du sus-épineux))***
> - [ ] **9. Colonne cervicale et test de Spurling *(Syndrome sous-acromial droit (tendinopathie du sus-épineux))***
> - [ ] **10. Tests globaux *(Syndrome sous-acromial droit (tendinopathie du sus-épineux))***
> - [ ] **11. Prise de la nuque *(Syndrome sous-acromial droit (tendinopathie du sus-épineux))***
> - [ ] **12. Prise du tablier *(Syndrome sous-acromial droit (tendinopathie du sus-épineux))***
> - [ ] **13. Mobilité active *(Syndrome sous-acromial droit (tendinopathie du sus-épineux))***
> - [ ] **14. Antéversion / rétversion *(Syndrome sous-acromial droit (tendinopathie du sus-épineux))***
> - [ ] **15. Abduction / élévation avec arc douloureux *(Syndrome sous-acromial droit (tendinopathie du sus-épineux))***
> - [ ] **16. Adduction le long du corps / adduction horizontale *(Syndrome sous-acromial droit (tendinopathie du sus-épineux))***
> - [ ] **17. Rotation externe le long du corps / en abduction 90° *(Syndrome sous-acromial droit (tendinopathie du sus-épineux))***
> - [ ] **18. Rotation interne selon Apley / en abduction 90° *(Syndrome sous-acromial droit (tendinopathie du sus-épineux))***
> - [ ] **19. Rétraction / protraction de la scapula *(Syndrome sous-acromial droit (tendinopathie du sus-épineux))***
> - [ ] **20. Élévation / abaissement de la scapula *(Syndrome sous-acromial droit (tendinopathie du sus-épineux))***
> - [ ] **21. Mobilité passive *(Syndrome sous-acromial droit (tendinopathie du sus-épineux))***
> - [ ] **22. Abduction / élévation *(Syndrome sous-acromial droit (tendinopathie du sus-épineux))***
> - [ ] **23. Rotation interne le long du corps / en abduction 90° *(Syndrome sous-acromial droit (tendinopathie du sus-épineux))***
> - [ ] **24. Tests sous-acromiaux *(Syndrome sous-acromial droit (tendinopathie du sus-épineux))***
> - [ ] **25. Test de Neer *(Syndrome sous-acromial droit (tendinopathie du sus-épineux))***
> - [ ] **26. Test de Hawkins-Kennedy *(Syndrome sous-acromial droit (tendinopathie du sus-épineux))***
> - [ ] **27. Tests de la coiffe des rotateurs *(Syndrome sous-acromial droit (tendinopathie du sus-épineux))***
> - [ ] **28. Test de Jobe (Empty Can) *(Syndrome sous-acromial droit (tendinopathie du sus-épineux))***
> - [ ] **29. Test de l’infra-épineux *(Syndrome sous-acromial droit (tendinopathie du sus-épineux))***
> - [ ] **30. Lift-off *(Syndrome sous-acromial droit (tendinopathie du sus-épineux))***
> - [ ] **31. Signe du trompettiste (Hornblower) *(Syndrome sous-acromial droit (tendinopathie du sus-épineux))***
> - [ ] **32. Test du bras tombant (Drop Arm) *(Syndrome sous-acromial droit (tendinopathie du sus-épineux))***
> - [ ] **33. Tests de DD *(Syndrome sous-acromial droit (tendinopathie du sus-épineux))***
> - [ ] **34. Cross-Body Adduction *(Syndrome sous-acromial droit (tendinopathie du sus-épineux))***
> - [ ] **35. Test de Speed *(Syndrome sous-acromial droit (tendinopathie du sus-épineux))***
> - [ ] **36. Test d’appréhension *(Syndrome sous-acromial droit (tendinopathie du sus-épineux))***
> - [ ] **37. Statut neurovasculaire *(Syndrome sous-acromial droit (tendinopathie du sus-épineux))***
> - [ ] **38. Nerf axillaire *(Syndrome sous-acromial droit (tendinopathie du sus-épineux))***
> - [ ] **39. Fonctions périphériques distales *(Syndrome sous-acromial droit (tendinopathie du sus-épineux))***
> - [ ] **40. Inspection de l'épaule *(Syndrome de conflit sous-acromial)***
> 	- [ ] Asymétrie
> 	- [ ] Amyotrophie
> 	- [ ] Déformation
> 	- [ ] Signes inflammatoires
> - [ ] **41. Palpation systématique *(Syndrome de conflit sous-acromial)***
> 	- [ ] Processus coracoïde
> 	- [ ] Articulation acromio-claviculaire
> 	- [ ] Coiffe des rotateurs (tubercule majeur et mineur)
> 	- [ ] Tendon du biceps (gouttière bicipitale)
> - [ ] **42. Évaluation des amplitudes articulaires *(Syndrome de conflit sous-acromial)***
> 	- [ ] Abduction (0-180°)
> 	- [ ] Élévation antérieure (flexion)
> 	- [ ] Rétropulsion (extension)
> 	- [ ] Rotation externe
> 	- [ ] Rotation interne
> 	- [ ] Tests fonctionnels (main-nuque, main-dos)
> - [ ] **43. Tests spécifiques de la coiffe des rotateurs *(Syndrome de conflit sous-acromial)***
> 	- [ ] Test de Jobe (supra-épineux)
> 	- [ ] Test lift-off (subscapulaire)
> 	- [ ] Test de Patte (infra-épineux/petit rond) - rotation externe contrariée
> - [ ] **44. Tests de conflit sous-acromial *(Syndrome de conflit sous-acromial)***
> 	- [ ] Test de Neer
> 	- [ ] Test de Hawkins-Kennedy
> 	- [ ] Test de Yocum
> - [ ] **45. Tests d'instabilité *(Syndrome de conflit sous-acromial)***
> 	- [ ] Test d'appréhension antérieur
> 	- [ ] Test d'appréhension postérieur
> 	- [ ] Test du sulcus (instabilité inférieure)
> - [ ] **46. Examen de l'articulation acromio-claviculaire *(Syndrome de conflit sous-acromial)***
> 	- [ ] Palpation directe
> 	- [ ] Test de compression horizontale (cross-arm test)
> - [ ] **47. Examen du tendon du long biceps *(Syndrome de conflit sous-acromial)***
> 	- [ ] Palm-up test (Speed test)
> 	- [ ] Test de Yergason
> - [ ] **48. Examen neurologique et vasculaire *(Syndrome de conflit sous-acromial)***
> 	- [ ] Sensibilité
> 	- [ ] Force musculaire
> 	- [ ] Réflexes
> 	- [ ] Pouls périphériques
> - [ ] **49. Inspection bras D *(Fracture du membre supérieur (humérus, tête radiale))***
> 	- [ ] Importante tuméfaction avec déformation du tiers inférieur au niveau de l'humérus droit *(1 grille sur 5)*
> 	- [ ] Peau intacte *(1 grille sur 5)*
> 	- [ ] Pas de lésion cutanée *(1 grille sur 5)*
> - [ ] **50. Contrôle neurologique et vasculaire distal à la lésion du MSD *(Fracture du membre supérieur (humérus, tête radiale))***
> 	- [ ] Les deux *(1 grille sur 5)*
> 	- [ ] Un *(1 grille sur 5)*
> 	- [ ] Aucun *(1 grille sur 5)*
> - [ ] **51. Vérifie motricité de la main et des doigts du MSD *(Fracture du membre supérieur (humérus, tête radiale))***
> 	- [ ] Les deux *(1 grille sur 5)*
> 	- [ ] Un *(1 grille sur 5)*
> 	- [ ] Aucun *(1 grille sur 5)*
> - [ ] **52. Examen pour d'autres lésions de la peau *(Fracture du membre supérieur (humérus, tête radiale))***
> - [ ] **53. Examen sommaire corps *(Fracture du membre supérieur (humérus, tête radiale))***
> 	- [ ] Abdomen
> 	- [ ] Thorax
> 	- [ ] Bassin
> 	- [ ] 4 membres
> 	- [ ] Crâne/visage/cavité buccale/dents *(1 grille sur 5)*
> 	- [ ] Crâne *(1 grille sur 5)*
> 	- [ ] Visage *(1 grille sur 5)*
> 	- [ ] Cavité buccale *(1 grille sur 5)*
> 	- [ ] Dents *(1 grille sur 5)*
> - [ ] **54. Envisage de faire des photos pour la documentation *(Fracture du membre supérieur (humérus, tête radiale))***

> [!success] 💊 Management — si Fracture du membre supérieur (humérus, tête radiale)
> - [ ] **1. Hypothèses diagnostiques**
> 	- [ ] Fracture de l'humérus
> 	- [ ] Spiroïde
> 	- [ ] De diaphyse
> 	- [ ] Déplacé *(1 grille sur 2)*
> 	- [ ] Distal *(1 grille sur 2)*
> 	- [ ] Multifragmentaire
> 	- [ ] Déplacée *(1 grille sur 2)*
> 	- [ ] Distale *(1 grille sur 2)*
> - [ ] **2. Demande des radiographies du MSD ou CT du MSD**
> 	- [ ] Fracture spiroïde de l'humérus droit (diaphysaire, déplacée, distal, multifragmentaire) *(1 grille sur 2)*
> - [ ] **3. Prise en charge**
> 	- [ ] Réduction fermée, plâtre, consultation et suivi orthopédique *(1 grille sur 2)*
> 	- [ ] Réduction fermée *(1 grille sur 2)*
> 	- [ ] Plâtre *(1 grille sur 2)*
> 	- [ ] Consultation et suivi orthopédique *(1 grille sur 2)*
> - [ ] **4. Informe de la possibilité de porter plainte**
> - [ ] **5. Quittance et prend en charge le trauma psychologique**
> - [ ] **6. Informe des offres de soutien à disposition (organisations aides aux victimes de violence, soutien psychologique)**
> 	- [ ] Les deux types *(1 grille sur 2)*
> 	- [ ] Un type *(1 grille sur 2)*
> 	- [ ] Aucun *(1 grille sur 2)*
> - [ ] **7. Diagnostics différentiels et prise en charge *(1 grille sur 2)***

> [!success] 💊 Management — si Rupture de la coiffe des rotateurs
> - [ ] **1. Hypothèses diagnostiques**
> - [ ] **2. Examens complémentaires**
> 	- [ ] US de l'épaule gauche
> 	- [ ] IRM de l'épaule gauche
> 	- [ ] Radiographie de l'épaule gauche
> 	- [ ] Test d'injection lidocaïne sous-acromiale
> - [ ] **3. Communication avec le patient**
> 	- [ ] Explications au patient des impressions diagnostiques préliminaires
> 	- [ ] Explication du plan de prise en charge
> 	- [ ] Utilisation d'un langage non médical et clarification des termes médicaux
> 	- [ ] Évaluation de l'accord du patient avec le plan diagnostique
> 	- [ ] Recherche des préoccupations et questions du patient
> - [ ] **4. Conseil et soutien**
> 	- [ ] Conseil sur l'utilisation d'opioïdes sur ordonnance
> 	- [ ] Réaction appropriée au défi concernant le retour au sport

> [!success] 💊 Management — si Syndrome de conflit sous-acromial
> - [ ] **1. Énonce le diagnostic principal**
> 	- [ ] Syndrome de conflit sous-acromial (syndrome du supra-épineux)
> - [ ] **2. Évoque les diagnostics différentiels pertinents**
> - [ ] **3. Propose les examens complémentaires appropriés**
> 	- [ ] Radiographie de l'épaule face + profil (première intention)
> 	- [ ] IRM en cas de doute diagnostique ou échec du traitement conservateur
> 	- [ ] Échographie si suspicion de pathologie de la coiffe
> 	- [ ] Bilan biologique si suspicion d'arthrite inflammatoire
> - [ ] **4. Propose une prise en charge thérapeutique adaptée**
> - [ ] **5. Organise le suivi et répond aux inquiétudes**
> 	- [ ] Réévaluation à 4-6 semaines
> 	- [ ] Orientation en rhumatologie/orthopédie si échec du traitement conservateur
> 	- [ ] Rassurer la patiente sur le pronostic généralement favorable
> 	- [ ] Expliquer l'évolution naturelle (amélioration en 3-6 mois dans la plupart des cas)

> [!success] 💊 Management — si Syndrome sous-acromial droit (tendinopathie du sus-épineux)
> - [ ] **1. Diagnostic clinique**
> - [ ] **2. Renoncer à l’IRM**
> - [ ] **3. Échographie**
> - [ ] **4. Radiographie de l’épaule**
> - [ ] **5. Diagnostic de travail**
> - [ ] **6. Adaptation de la charge**
> - [ ] **7. Physiothérapie**
> - [ ] **8. Symptomatique**
> - [ ] **9. Refroidissement**
> - [ ] **10. Analgésie**
> - [ ] **11. Contrôle évolutif**
> - [ ] **12. Infiltration sous-acromiale**
> - [ ] **13. Filet de sécurité**
