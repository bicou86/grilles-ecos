---
aliases:
  - "Mémento Hypoacousie"
type: memento-ecos-ssp
ssp: "Hypoacousie"
cas: 4
diagnostics: 2
attendus_documentes_ailleurs: 0
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

# Hypoacousie

*4 grilles · 2 diagnostics documentés · 1 attendu absent du corpus* — [[SSP — Hypoacousie]]

> [!abstract] Les 4 grilles fusionnées
> - **AMBOSS-23** — Presbyacousie `premier-dd` · [grille](<file:///Users/damienfulliquet/Developer/GitHub/grilles-ecos/cases/amboss/AMBOSS-23_-_Perte_auditive_-_Homme_65_ans_-_Grille_ECOS.html>)
> - **AZYGOS-33** — Presbyacousie `diagnostic-travail` · [grille](<file:///Users/damienfulliquet/Developer/GitHub/grilles-ecos/docs/azygos-grilles/8fdeb650-3127-4f13-9ec7-1d50b1a6af35.json>)
> - **German-67** — Surdité brusque idiopathique gauche `explicite` · [grille](<file:///Users/damienfulliquet/Developer/GitHub/grilles-ecos/cases/german/German-67_-_Perte_auditive_-_Grille_ECOS.html>)
> - **German-68** — Presbyacousie `explicite` · [grille](<file:///Users/damienfulliquet/Developer/GitHub/grilles-ecos/cases/german/German-68_-_Perte_auditive_-_Grille_ECOS.html>)

> [!note] 📋 Anamnèse
> - [ ] **1. Motif de consultation *(2 grilles sur 4)***
> 	- [ ] Qu'est-ce qui vous amène aujourd'hui ? *(1 grille sur 4)*
> 	- [ ] Avez-vous des problèmes particuliers ? *(1 grille sur 4)*
> - [ ] **2. Caractérisation de la perte auditive *(3 grilles sur 4)***
> 	- [ ] Oreilles affectées *(1 grille sur 4)*
> 	- [ ] Tous les sons/sons spécifiques *(1 grille sur 4)*
> 	- [ ] Début *(1 grille sur 4)*
> 	- [ ] Constant/intermittent *(1 grille sur 4)*
> 	- [ ] Événements précipitants *(1 grille sur 4)*
> 	- [ ] Progression *(1 grille sur 4)*
> 	- [ ] Épisodes antérieurs *(1 grille sur 4)*
> 	- [ ] Facteurs améliorants *(1 grille sur 4)*
> 	- [ ] Facteurs aggravants *(1 grille sur 4)*
> 	- [ ] Symptômes associés *(1 grille sur 4)*
> 	- [ ] Apparition temporelle *(2 grilles sur 4)*
> 	- [ ] Évolution temporelle *(Surdité brusque idiopathique gauche)*
> 	- [ ] Latéralisation *(2 grilles sur 4)*
> 	- [ ] Intensité de la perte auditive *(Surdité brusque idiopathique gauche)*
> 	- [ ] Évolution *(1 grille sur 4)*
> 	- [ ] Sévérité *(1 grille sur 4)*
> - [ ] **3. Recherche de symptômes spécifiques *(1 grille sur 4)***
> 	- [ ] Traumatisme
> 	- [ ] Céphalées
> 	- [ ] Nausées/vomissements
> 	- [ ] Éruption cutanée/changements cutanés
> 	- [ ] Infections récentes
> 	- [ ] Vertiges
> 	- [ ] Exposition récente à un bruit fort soudain
> 	- [ ] Acouphènes
> 	- [ ] Douleur auriculaire
> 	- [ ] Écoulement auriculaire
> 	- [ ] Faiblesse
> 	- [ ] Engourdissement
> 	- [ ] Picotements
> - [ ] **4. Antécédents médicaux *(1 grille sur 4)***
> 	- [ ] Antécédents médicaux
> 	- [ ] Type de chimiothérapie
> - [ ] **5. Allergies *(3 grilles sur 4)***
> 	- [ ] Allergies *(1 grille sur 4)*
> 	- [ ] Description de la réaction allergique *(1 grille sur 4)*
> 	- [ ] Allergies connues *(Surdité brusque idiopathique gauche)*
> - [ ] **6. Médicaments *(2 grilles sur 4)***
> - [ ] **7. Hospitalisations et antécédents chirurgicaux *(1 grille sur 4)***
> 	- [ ] Hospitalisations
> 	- [ ] Antécédents chirurgicaux
> - [ ] **8. Antécédents familiaux *(2 grilles sur 4)***
> 	- [ ] Surdité familiale *(Surdité brusque idiopathique gauche)*
> 	- [ ] Autres pathologies ORL familiales *(Surdité brusque idiopathique gauche)*
> - [ ] **9. Habitudes et mode de vie *(1 grille sur 4)***
> 	- [ ] Travail
> 	- [ ] Niveau sonore au travail, protection auditive
> 	- [ ] Domicile
> 	- [ ] Alcool
> 	- [ ] Drogues récréatives
> 	- [ ] Tabac
> - [ ] **10. Question d'entrée ouverte *(2 grilles sur 4)***
> 	- [ ] Qu'est-ce qui vous amène aujourd'hui ? *(Surdité brusque idiopathique gauche)*
> - [ ] **11. Localisation (unilatérale / bilatérale) *(1 grille sur 4)***
> - [ ] **12. Dimension temporelle *(1 grille sur 4)***
> - [ ] **13. Durée (depuis quand ?) *(1 grille sur 4)***
> - [ ] **14. Début (soudain / insidieux) *(1 grille sur 4)***
> - [ ] **15. Évolution (stable / progressive / intermittente) *(1 grille sur 4)***
> - [ ] **16. Déclencheurs *(1 grille sur 4)***
> - [ ] **17. Qualité de l’hypoacousie *(1 grille sur 4)***
> - [ ] **18. Intensité / retentissement de l’hypoacousie *(1 grille sur 4)***
> - [ ] **19. Facteurs améliorants *(1 grille sur 4)***
> - [ ] **20. Facteurs aggravants *(1 grille sur 4)***
> - [ ] **21. Symptômes associés *(1 grille sur 4)***
> - [ ] **22. Otalgies *(1 grille sur 4)***
> - [ ] **23. Otorrhée *(1 grille sur 4)***
> - [ ] **24. Vertiges *(1 grille sur 4)***
> - [ ] **25. Acouphènes / bourdonnements *(1 grille sur 4)***
> - [ ] **26. Exposition au bruit *(2 grilles sur 4)***
> 	- [ ] Exposition professionnelle antérieure *(1 grille sur 4)*
> 	- [ ] Loisirs bruyants *(1 grille sur 4)*
> 	- [ ] Traumatismes acoustiques *(1 grille sur 4)*
> - [ ] **27. Céphalées *(1 grille sur 4)***
> - [ ] **28. Symptômes neurologiques focaux *(1 grille sur 4)***
> - [ ] **29. Infections passées *(1 grille sur 4)***
> - [ ] **30. Antécédents *(1 grille sur 4)***
> - [ ] **31. Problèmes auditifs/oreilles antérieurs, appareils auditifs *(1 grille sur 4)***
> - [ ] **32. Opérations ORL antérieures *(1 grille sur 4)***
> - [ ] **33. Noxes *(1 grille sur 4)***
> - [ ] **34. Alcool *(1 grille sur 4)***
> - [ ] **35. Tabac *(1 grille sur 4)***
> - [ ] **36. Drogues *(1 grille sur 4)***
> - [ ] **37. Hypoacousie familiale *(1 grille sur 4)***
> - [ ] **38. Profession *(1 grille sur 4)***
> - [ ] **39. Situation sociale *(1 grille sur 4)***
> - [ ] **40. Présentation avec nom, fonction et tâche *(2 grilles sur 4)***
> - [ ] **41. Symptômes associés ORL *(2 grilles sur 4)***
> 	- [ ] Sécrétions auriculaires (cérumen, sang, pus)
> 	- [ ] Douleurs auriculaires
> 	- [ ] Acouphènes
> 	- [ ] Vertiges
> - [ ] **42. Symptômes généraux *(2 grilles sur 4)***
> 	- [ ] Fièvre
> 	- [ ] Toux
> 	- [ ] Rhinite *(Surdité brusque idiopathique gauche)*
> 	- [ ] Vomissements
> 	- [ ] Rhinorrhée *(1 grille sur 4)*
> - [ ] **43. Facteurs déclenchants et traumatismes *(Surdité brusque idiopathique gauche)***
> 	- [ ] Facteur déclenchant identifiable
> 	- [ ] Traumatisme récent
> 	- [ ] Situation particulière
> - [ ] **44. Antécédents ORL et exposition *(Surdité brusque idiopathique gauche)***
> 	- [ ] Antécédents de maladies auriculaires
> 	- [ ] Exposition professionnelle au bruit
> 	- [ ] Traumatismes auditifs antérieurs
> - [ ] **45. Anamnèse médicamenteuse *(2 grilles sur 4)***
> 	- [ ] Médicaments actuels
> 	- [ ] Médicaments ototoxiques
> 	- [ ] Automédication récente *(Surdité brusque idiopathique gauche)*
> 	- [ ] Traitement cardiovasculaire *(1 grille sur 4)*
> - [ ] **46. Anamnèse systémique *(2 grilles sur 4)***
> 	- [ ] Hypertension artérielle
> 	- [ ] Diabète
> 	- [ ] Troubles neurologiques
> 	- [ ] Facteurs psychosociaux *(Surdité brusque idiopathique gauche)*
> - [ ] **47. Anamnèse sociale et professionnelle *(Surdité brusque idiopathique gauche)***
> 	- [ ] Profession
> 	- [ ] Situation familiale
> 	- [ ] Stress professionnel
> - [ ] **48. Antécédents médicaux et ORL *(1 grille sur 4)***
> 	- [ ] Otite moyenne dans l'enfance
> 	- [ ] Méningite
> 	- [ ] Cardiopathie ischémique
> 	- [ ] Autres antécédents ORL
> - [ ] **49. Impact fonctionnel sur la communication *(1 grille sur 4)***
> 	- [ ] Capacité à téléphoner
> 	- [ ] Volume de la télévision/radio
> 	- [ ] Compréhension en groupe
> - [ ] **50. Anamnèse sociale et impact psychosocial *(1 grille sur 4)***
> 	- [ ] Situation de vie
> 	- [ ] Animaux de compagnie
> 	- [ ] Condition physique
> - [ ] **51. Activités sociales et loisirs *(1 grille sur 4)***
> 	- [ ] Participation sociale actuelle
> 	- [ ] Activités abandonnées
> 	- [ ] Isolement social

> [!tip] 🩺 Status
> - [ ] **1. Mesures d'hygiène *(1 grille sur 4)***
> 	- [ ] Lavage des mains
> 	- [ ] Respect de la pudeur avec drap
> - [ ] **2. Examen de la tête, yeux, oreilles, nez et gorge *(1 grille sur 4)***
> 	- [ ] Palpation de la tête
> 	- [ ] Inspection des oreilles
> 	- [ ] Palpation des oreilles
> 	- [ ] Otoscopie
> 	- [ ] Tests de Rinne et Weber
> - [ ] **3. Examen neurologique de base *(2 grilles sur 4)***
> 	- [ ] Examen ciblé des nerfs crâniens *(1 grille sur 4)*
> 	- [ ] Examen ciblé de l'audition *(1 grille sur 4)*
> 	- [ ] Nerfs crâniens *(1 grille sur 4)*
> 	- [ ] Équilibre *(1 grille sur 4)*
> 	- [ ] Coordination *(1 grille sur 4)*
> - [ ] **4. Tension artérielle *(1 grille sur 4)***
> - [ ] **5. Inspection *(1 grille sur 4)***
> - [ ] **6. Palpation (tragus / helix) *(1 grille sur 4)***
> - [ ] **7. Otoscopie incl. manœuvre de Valsalva *(1 grille sur 4)***
> - [ ] **8. Tests auditifs *(1 grille sur 4)***
> - [ ] **9. Épreuve d’orientation auditive (test des nombres chuchotés) *(1 grille sur 4)***
> - [ ] **10. Test de Weber *(1 grille sur 4)***
> - [ ] **11. Test de Rinne *(1 grille sur 4)***
> - [ ] **12. Status neurologique orientant *(1 grille sur 4)***
> - [ ] **13. Examen du facial *(1 grille sur 4)***
> - [ ] **14. Status complet des nerfs crâniens *(1 grille sur 4)***
> - [ ] **15. Motricité / sensibilité / coordination *(1 grille sur 4)***
> - [ ] **16. Inspection de l'oreille *(2 grilles sur 4)***
> 	- [ ] Inspection du pavillon auriculaire *(Surdité brusque idiopathique gauche)*
> 	- [ ] Inspection du conduit auditif externe visible
> 	- [ ] Pavillon auriculaire droit *(1 grille sur 4)*
> 	- [ ] Pavillon auriculaire gauche *(1 grille sur 4)*
> - [ ] **17. Palpation de l'oreille et recherche d'adénopathies *(Surdité brusque idiopathique gauche)***
> 	- [ ] Palpation du tragus
> 	- [ ] Traction du pavillon auriculaire
> 	- [ ] Palpation mastoïdienne
> 	- [ ] Recherche d'adénopathies cervicales
> - [ ] **18. Otoscopie bilatérale *(2 grilles sur 4)***
> 	- [ ] Conduit auditif externe droit
> 	- [ ] Tympan droit
> 	- [ ] Conduit auditif externe gauche
> 	- [ ] Tympan gauche
> - [ ] **19. Tests auditifs au diapason *(2 grilles sur 4)***
> 	- [ ] Test de Weber
> 	- [ ] Test de Rinne à droite
> 	- [ ] Test de Rinne à gauche
> - [ ] **20. Test de la voix chuchotée *(2 grilles sur 4)***
> 	- [ ] Oreille droite *(Surdité brusque idiopathique gauche)*
> 	- [ ] Oreille gauche *(Surdité brusque idiopathique gauche)*
> 	- [ ] Compréhension à droite *(1 grille sur 4)*
> 	- [ ] Compréhension à gauche *(1 grille sur 4)*
> 	- [ ] Nécessité de répéter fort *(1 grille sur 4)*
> - [ ] **21. Examen de l'équilibre et coordination *(Surdité brusque idiopathique gauche)***
> 	- [ ] Équilibre statique
> 	- [ ] Marche
> 	- [ ] Recherche de nystagmus
> - [ ] **22. Palpation auriculaire *(1 grille sur 4)***
> 	- [ ] Pression du tragus
> 	- [ ] Traction du pavillon
> 	- [ ] Palpation mastoïdienne

> [!success] 💊 Management — partagé par plusieurs diagnostics
> - [ ] **1. Diagnostics différentiels *(2 grilles sur 4)* — *Presbyacousie · Surdité brusque idiopathique gauche***

> [!success] 💊 Management — si Otosclérose
> *Aucune grille du corpus ne documente ce diagnostic* — il est pourtant attendu de cette SSP. **Trou de révision à combler ailleurs.**

> [!success] 💊 Management — si Presbyacousie
> - [ ] **1. Hypothèses diagnostiques *(1 grille sur 3)***
> - [ ] **2. Examens complémentaires *(2 grilles sur 3)***
> 	- [ ] Audiométrie *(1 grille sur 3)*
> 	- [ ] Tympanométrie *(1 grille sur 3)*
> 	- [ ] Audiométrie tonale (courbe typique avec chute dans les aigus) *(1 grille sur 3)*
> 	- [ ] Audiométrie vocale (mauvaise discrimination) *(1 grille sur 3)*
> 	- [ ] Potentiels évoqués auditifs si doute diagnostique *(1 grille sur 3)*
> - [ ] **3. Communication avec le patient *(1 grille sur 3)***
> 	- [ ] Explications au patient des impressions diagnostiques préliminaires
> 	- [ ] Explication du plan de prise en charge
> 	- [ ] Utilisation d'un langage non médical et clarification des termes médicaux
> 	- [ ] Évaluation de l'accord du patient avec le plan diagnostique
> 	- [ ] Recherche des préoccupations et questions du patient
> - [ ] **4. Conseil et soutien *(1 grille sur 3)***
> 	- [ ] Conseil sur l'arrêt du tabac
> 	- [ ] Conseil pour réduire la prise d'aspirine
> 	- [ ] Réaction appropriée au défi : articuler clairement, parler fort
> 	- [ ] Éducation sur les aides auditives
> 	- [ ] Stratégies de communication
> - [ ] **5. Audiométrie *(1 grille sur 3)***
> - [ ] **6. Presbyacousie *(1 grille sur 3)***
> - [ ] **7. Orientation vers une spécialiste ORL / un spécialiste ORL pour l’appareillage auditif *(1 grille sur 3)***
> - [ ] **8. Filet de sécurité *(1 grille sur 3)***
> - [ ] **9. Diagnostic principal *(1 grille sur 3)***
> 	- [ ] Presbyacousie bilatérale
> - [ ] **10. Information du patient et pronostic *(1 grille sur 3)***
> 	- [ ] Évolution progressive mais appareillage efficace
> 	- [ ] Importance de l'observance pour éviter l'isolement social
> 	- [ ] Réévaluation audiométrique annuelle
> 	- [ ] Adaptation possible des réglages de l'appareil
> - [ ] **11. Caractéristiques diagnostiques de la presbyacousie *(1 grille sur 3)***
> 	- [ ] Surdité de perception symétrique bilatérale
> 	- [ ] Atteinte prédominante des fréquences aiguës
> 	- [ ] Limitation de la compréhension de la parole
> 	- [ ] Difficultés accrues en environnement bruyant
> 	- [ ] Évolution progressive avec l'âge
> 	- [ ] Possible association avec des acouphènes
> - [ ] **12. Traitement et prise en charge *(1 grille sur 3)***

> [!success] 💊 Management — si Surdité brusque idiopathique gauche
> - [ ] **1. Examens complémentaires**
> 	- [ ] Audiométrie tonale en urgence
> 	- [ ] Audiométrie vocale
> 	- [ ] Tympanométrie
> 	- [ ] Diagnostic vestibulaire (nystagmus, épreuve calorique)
> 	- [ ] Bilan biologique (FSC, CRP, VS, glycémie)
> 	- [ ] Recherche d'hypertension artérielle
> 	- [ ] Recherche d'hyperlipidémie
> 	- [ ] IRM cérébrale et du conduit auditif interne si pas d'amélioration
> - [ ] **2. Diagnostic principal**
> 	- [ ] Surdité brusque idiopathique gauche
> 	- [ ] Surdité de perception unilatérale gauche
> - [ ] **3. Traitement**
> - [ ] **4. Information du patient et pronostic**
> 	- [ ] Récupération complète dans 60% des cas
> 	- [ ] Récupération partielle dans 20% des cas
> 	- [ ] Possibilité de récidive
> 	- [ ] Importance du traitement précoce
> 	- [ ] Nécessité d'un suivi audiométrique
