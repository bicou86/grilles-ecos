---
aliases:
  - "Mémento Douleur du Genou"
type: memento-ecos-ssp
ssp: "Douleur du Genou"
cas: 3
diagnostics: 2
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

# Douleur du Genou

*3 grilles · 2 diagnostics documentés · 1 attendu documenté ailleurs · 1 attendu absent du corpus* — [[SSP — Douleur du Genou]]

> [!abstract] Les 3 grilles fusionnées
> - **AMBOSS-25** — Thrombose veineuse profonde (TVP) `premier-dd` · [grille](<file:///Users/damienfulliquet/Developer/GitHub/grilles-ecos/cases/amboss/AMBOSS-25_-_Douleur_au_genou_-_Femme_47_ans_-_Grille_ECOS.html>)
> - **AZYGOS-17** — Déchirure méniscale / ligamentaire `diagnostic-travail` · [grille](<file:///Users/damienfulliquet/Developer/GitHub/grilles-ecos/docs/azygos-grilles/03534eb4-8ba8-409e-a9c2-6b04c555a00b.json>)
> - **German-23** — Déchirure méniscale / ligamentaire `corrige` · [grille](<file:///Users/damienfulliquet/Developer/GitHub/grilles-ecos/cases/german/German-23_-_Douleur_au_genou_-_Grille_ECOS.html>)

> [!note] 📋 Anamnèse
> - [ ] **1. Motif principal *(Thrombose veineuse profonde (TVP))***
> - [ ] **2. Caractérisation de la douleur *(2 grilles sur 3)***
> 	- [ ] Localisation *(Thrombose veineuse profonde (TVP))*
> 	- [ ] Intensité (échelle 0-10) *(Thrombose veineuse profonde (TVP))*
> 	- [ ] Qualité *(Thrombose veineuse profonde (TVP))*
> 	- [ ] Début *(Thrombose veineuse profonde (TVP))*
> 	- [ ] Événements précipitants *(Thrombose veineuse profonde (TVP))*
> 	- [ ] Autres blessures lors de la chute *(Thrombose veineuse profonde (TVP))*
> 	- [ ] Perte de connaissance *(Thrombose veineuse profonde (TVP))*
> 	- [ ] Progression/constant/intermittent *(Thrombose veineuse profonde (TVP))*
> 	- [ ] Épisodes antérieurs *(Thrombose veineuse profonde (TVP))*
> 	- [ ] Irradiation *(Thrombose veineuse profonde (TVP))*
> 	- [ ] Facteurs améliorants *(Thrombose veineuse profonde (TVP))*
> 	- [ ] Facteurs aggravants *(Thrombose veineuse profonde (TVP))*
> 	- [ ] Symptômes associés *(Thrombose veineuse profonde (TVP))*
> - [ ] **3. Recherche de symptômes spécifiques *(Thrombose veineuse profonde (TVP))***
> 	- [ ] Voyage récent
> 	- [ ] Fièvre/frissons
> 	- [ ] Éruption cutanée/changements cutanés
> 	- [ ] Douleur thoracique
> 	- [ ] Toux
> 	- [ ] Dyspnée
> 	- [ ] Douleurs articulaires
> 	- [ ] Problèmes urinaires
> 	- [ ] Variations pondérales
> 	- [ ] Infections récentes
> 	- [ ] Vertiges
> 	- [ ] Chaleur du membre inférieur
> 	- [ ] Faiblesse/engourdissement/picotements
> - [ ] **4. Antécédents médicaux**
> 	- [ ] Antécédents médicaux *(Thrombose veineuse profonde (TVP))*
> 	- [ ] Thrombose dans le passé *(Thrombose veineuse profonde (TVP))*
> - [ ] **5. Allergies *(2 grilles sur 3)***
> - [ ] **6. Médicaments actuels**
> - [ ] **7. Hospitalisations et antécédents chirurgicaux *(Thrombose veineuse profonde (TVP))***
> 	- [ ] Hospitalisations
> 	- [ ] Grossesses antérieures/fausses couches
> 	- [ ] Antécédents chirurgicaux
> - [ ] **8. Antécédents familiaux**
> - [ ] **9. Habitudes et mode de vie *(2 grilles sur 3)***
> 	- [ ] Travail *(Thrombose veineuse profonde (TVP))*
> 	- [ ] Domicile *(Thrombose veineuse profonde (TVP))*
> 	- [ ] Alcool *(Thrombose veineuse profonde (TVP))*
> 	- [ ] Drogues récréatives *(Thrombose veineuse profonde (TVP))*
> 	- [ ] Tabac *(Thrombose veineuse profonde (TVP))*
> 	- [ ] Exercice *(Thrombose veineuse profonde (TVP))*
> 	- [ ] Alimentation *(Thrombose veineuse profonde (TVP))*
> - [ ] **10. Question initiale *(1 grille sur 3)***
> - [ ] **11. Dimension temporelle *(1 grille sur 3)***
> - [ ] **12. Début *(1 grille sur 3)***
> - [ ] **13. Évolution *(1 grille sur 3)***
> - [ ] **14. Déclencheur *(1 grille sur 3)***
> - [ ] **15. Localisation *(1 grille sur 3)***
> - [ ] **16. Irradiation *(1 grille sur 3)***
> - [ ] **17. Qualité *(1 grille sur 3)***
> - [ ] **18. Intensité / sévérité *(1 grille sur 3)***
> - [ ] **19. Facteurs aggravants *(1 grille sur 3)***
> - [ ] **20. Facteurs soulageants *(1 grille sur 3)***
> - [ ] **21. Mesures déjà prises *(1 grille sur 3)***
> - [ ] **22. Retentissement au quotidien *(1 grille sur 3)***
> - [ ] **23. Symptômes associés *(1 grille sur 3)***
> - [ ] **24. Blessures antérieures *(1 grille sur 3)***
> - [ ] **25. Activité sportive *(1 grille sur 3)***
> - [ ] **26. Mécanisme de la blessure *(1 grille sur 3)***
> - [ ] **27. Symptômes mécaniques *(Déchirure méniscale / ligamentaire)***
> - [ ] **28. Clic / phénomène de ressaut *(1 grille sur 3)***
> - [ ] **29. Blocage / sensation de coincement *(1 grille sur 3)***
> - [ ] **30. Limitation de l’extension *(1 grille sur 3)***
> - [ ] **31. Dynamique du gonflement *(1 grille sur 3)***
> - [ ] **32. DD lésion ligamentaire *(1 grille sur 3)***
> - [ ] **33. Giving-way / dérobement *(1 grille sur 3)***
> - [ ] **34. Pop / claquement sonore *(1 grille sur 3)***
> - [ ] **35. Sensation d’instabilité *(1 grille sur 3)***
> - [ ] **36. DD fracture, Règles d’Ottawa pour le genou *(1 grille sur 3)***
> - [ ] **37. Capacité de charge après le traumatisme *(1 grille sur 3)***
> - [ ] **38. Flexion au-delà de 90° *(1 grille sur 3)***
> - [ ] **39. Antécédents chirurgicaux *(1 grille sur 3)***
> - [ ] **40. Noxes *(1 grille sur 3)***
> - [ ] **41. Tabac *(1 grille sur 3)***
> - [ ] **42. Alcool *(1 grille sur 3)***
> - [ ] **43. Drogues *(1 grille sur 3)***
> - [ ] **44. Anamnèse psychosociale *(1 grille sur 3)***
> - [ ] **45. Profession / loisirs *(1 grille sur 3)***
> - [ ] **46. Charge psychosociale *(1 grille sur 3)***
> - [ ] **47. Situation sociale *(1 grille sur 3)***
> - [ ] **48. Présentation avec nom, fonction et tâche *(1 grille sur 3)***
> - [ ] **49. Début et évolution temporelle *(1 grille sur 3)***
> - [ ] **50. Facteur déclenchant/circonstances *(1 grille sur 3)***
> - [ ] **51. Évolution depuis le début *(1 grille sur 3)***
> - [ ] **52. Localisation précise de la douleur *(1 grille sur 3)***
> - [ ] **53. Intensité de la douleur (échelle 0-10) *(1 grille sur 3)***
> - [ ] **54. Caractère de la douleur *(1 grille sur 3)***
> - [ ] **55. Présence de gonflement *(1 grille sur 3)***
> - [ ] **56. Douleur au repos *(1 grille sur 3)***
> - [ ] **57. Capacité de marche/mobilité *(1 grille sur 3)***
> - [ ] **58. Limitation des mouvements *(1 grille sur 3)***
> - [ ] **59. Auto-traitement déjà entrepris *(1 grille sur 3)***
> - [ ] **60. Symptômes associés (fièvre, signes d'infection) *(1 grille sur 3)***
> - [ ] **61. Morsure de tique *(1 grille sur 3)***
> - [ ] **62. Douleurs dans d'autres articulations *(1 grille sur 3)***
> - [ ] **63. Antécédents de pathologie du genou *(1 grille sur 3)***
> - [ ] **64. Anamnèse sociale et professionnelle *(1 grille sur 3)***

> [!tip] 🩺 Status
> - [ ] **1. Mesures d'hygiène *(Thrombose veineuse profonde (TVP))***
> 	- [ ] Lavage des mains
> 	- [ ] Respect de la pudeur avec drap
> - [ ] **2. Examen cardiovasculaire *(Thrombose veineuse profonde (TVP))***
> 	- [ ] Palpation du pouls radial
> 	- [ ] Auscultation cardiaque
> 	- [ ] Évaluation de la distension veineuse jugulaire
> - [ ] **3. Examen thoracique *(Thrombose veineuse profonde (TVP))***
> 	- [ ] Auscultation pulmonaire
> - [ ] **4. Examen des extrémités *(Thrombose veineuse profonde (TVP))***
> 	- [ ] Retrait du bandage de la patiente
> 	- [ ] Inspection des membres inférieurs
> 	- [ ] Recherche d'œdème déclive
> 	- [ ] Palpation des membres inférieurs
> 	- [ ] Examen ciblé des mouvements passifs et actifs des membres inférieurs
> 	- [ ] Test de Lachman
> 	- [ ] Test du tiroir postérieur
> 	- [ ] Test de stress en valgus
> 	- [ ] Test de stress en varus
> 	- [ ] Examen ciblé de la sensibilité des membres inférieurs
> 	- [ ] Palpation des pouls pédieux
> 	- [ ] Signe de Homans
> - [ ] **5. Démarche *(1 grille sur 3)***
> - [ ] **6. Tests globaux *(1 grille sur 3)***
> - [ ] **7. Test d’extension *(1 grille sur 3)***
> - [ ] **8. Test d’accroupissement *(1 grille sur 3)***
> - [ ] **9. Inspection générale *(Déchirure méniscale / ligamentaire)***
> 	- [ ] Axes des membres inférieurs *(1 grille sur 3)*
> 	- [ ] Longueur des jambes et position du bassin *(1 grille sur 3)*
> 	- [ ] Analyse de la marche *(1 grille sur 3)*
> 	- [ ] Recherche de gonflement et rotule dansante *(1 grille sur 3)*
> - [ ] **10. Inspection *(1 grille sur 3)***
> - [ ] **11. PDMS *(1 grille sur 3)***
> - [ ] **12. Palpation *(1 grille sur 3)***
> - [ ] **13. Phénomène de ballottement rotulien *(1 grille sur 3)***
> - [ ] **14. Mobilité *(1 grille sur 3)***
> - [ ] **15. Flexion / extension *(1 grille sur 3)***
> - [ ] **16. Rotation *(1 grille sur 3)***
> - [ ] **17. Tests méniscaux *(Déchirure méniscale / ligamentaire)***
> 	- [ ] Test de Steinmann I *(1 grille sur 3)*
> 	- [ ] Test de McMurray *(1 grille sur 3)*
> 	- [ ] Test d'Apley (Grinding test) *(1 grille sur 3)*
> - [ ] **18. Test de McMurray *(1 grille sur 3)***
> - [ ] **19. Test de Steinmann I *(1 grille sur 3)***
> - [ ] **20. Tests des ligaments croisés *(Déchirure méniscale / ligamentaire)***
> 	- [ ] Ligament croisé antérieur - Test de Lachman *(1 grille sur 3)*
> 	- [ ] Ligament croisé postérieur - Test du tiroir postérieur, Gravity-Sign *(1 grille sur 3)*
> - [ ] **21. Lachman *(1 grille sur 3)***
> - [ ] **22. Tiroir antérieur *(1 grille sur 3)***
> - [ ] **23. Tiroir postérieur *(1 grille sur 3)***
> - [ ] **24. Ligaments latéraux *(1 grille sur 3)***
> - [ ] **25. Stress en valgus *(1 grille sur 3)***
> - [ ] **26. Stress en varus *(1 grille sur 3)***
> - [ ] **27. Palpation systématique *(1 grille sur 3)***
> 	- [ ] Structures osseuses (tubérosité tibiale antérieure, rotule, condyles fémoraux)
> 	- [ ] Interligne articulaire
> 	- [ ] Ligaments collatéraux
> 	- [ ] Tendon rotulien
> 	- [ ] Recherche d'épanchement (signe du glaçon)
> - [ ] **28. Examen fonctionnel - Mobilité articulaire *(1 grille sur 3)***
> 	- [ ] Flexion-extension active et passive
> 	- [ ] Méthode Neutre-Zéro
> - [ ] **29. Test de stabilité ligamentaire collatérale *(1 grille sur 3)***
> 	- [ ] Stress varus-valgus en extension complète
> 	- [ ] Stress varus-valgus en flexion 20-30°
> - [ ] **30. Examen de l'appareil extenseur *(1 grille sur 3)***
> 	- [ ] Palpation du tubercule des adducteurs
> 	- [ ] Test d'appréhension pour luxation patellaire en flexion 30°
> 	- [ ] Mobilité de la rotule
> - [ ] **31. Test de force musculaire *(1 grille sur 3)***
> 	- [ ] Flexion/extension contre résistance
> 	- [ ] Quadriceps et ischio-jambiers
> - [ ] **32. Évaluation vasculo-nerveuse périphérique *(1 grille sur 3)***
> 	- [ ] Pouls pédieux et tibial postérieur
> 	- [ ] Sensibilité
> 	- [ ] Motricité distale

> [!success] 💊 Management — si Arthrite septique
> *Aucune grille de cette SSP ne documente ce diagnostic* — mais le corpus le documente ailleurs : [[Mémento — Boiterie de l'Enfant]] (2 grilles).

> [!success] 💊 Management — si Déchirure méniscale / ligamentaire
> - [ ] **1. Radiographie du genou *(1 grille sur 2)***
> - [ ] **2. IRM du genou *(1 grille sur 2)***
> - [ ] **3. Diagnostic de travail *(1 grille sur 2)***
> - [ ] **4. Information sur le diagnostic *(1 grille sur 2)***
> - [ ] **5. Analgésie *(1 grille sur 2)***
> - [ ] **6. Refroidissement *(1 grille sur 2)***
> - [ ] **7. Décharge *(1 grille sur 2)***
> - [ ] **8. Orthèse de genou *(1 grille sur 2)***
> - [ ] **9. Indication opératoire *(1 grille sur 2)***
> - [ ] **10. Technique opératoire *(1 grille sur 2)***
> - [ ] **11. Avis orthopédique *(1 grille sur 2)***
> - [ ] **12. Filet de sécurité *(1 grille sur 2)***
> - [ ] **13. Contrôle d’évolution *(1 grille sur 2)***
> - [ ] **14. Diagnostic principal *(1 grille sur 2)***
> - [ ] **15. Diagnostics différentiels (au moins 2) *(1 grille sur 2)***
> - [ ] **16. Examens complémentaires *(1 grille sur 2)***
> 	- [ ] Radiographie du genou (face/profil) pour exclure une lésion osseuse
> 	- [ ] IRM du genou pour confirmation diagnostique
> 	- [ ] Éventuellement arthroscopie diagnostique et thérapeutique
> - [ ] **17. Traitement aigu *(1 grille sur 2)***
> 	- [ ] Protocole RICE (repos, glace, compression, élévation)
> 	- [ ] AINS (ex: ibuprofène 600mg 3x/jour)
> 	- [ ] Antalgiques si nécessaire
> 	- [ ] Décharge partielle avec cannes anglaises
> 	- [ ] Immobilisation relative (attelle articulée si nécessaire)
> - [ ] **18. Prise en charge à moyen terme *(1 grille sur 2)***
> 	- [ ] Référence à l'orthopédiste
> 	- [ ] Physiothérapie pour renforcement musculaire et proprioception
> 	- [ ] Décision thérapeutique selon IRM: conservateur vs chirurgical
> 	- [ ] Si chirurgie: suture méniscale, résection partielle ou remplacement selon lésion
> - [ ] **19. Information du patient *(1 grille sur 2)***
> 	- [ ] Explication du diagnostic probable
> 	- [ ] Évolution attendue
> 	- [ ] Importance du repos sportif temporaire
> 	- [ ] Plan de traitement proposé
> - [ ] **20. Suivi *(1 grille sur 2)***
> 	- [ ] Contrôle clinique dans 1-2 semaines
> 	- [ ] Adaptation du traitement selon évolution
> 	- [ ] Certificat médical pour arrêt sportif

> [!success] 💊 Management — si Ostéomyélite
> *Aucune grille du corpus ne documente ce diagnostic* — il est pourtant attendu de cette SSP. **Trou de révision à combler ailleurs.**

> [!success] 💊 Management — si Thrombose veineuse profonde (TVP)
> - [ ] **1. Hypothèses diagnostiques**
> - [ ] **2. Examens complémentaires de première intention**
> 	- [ ] D-dimères
> 	- [ ] Échographie de compression avec Doppler jambe droite
> 	- [ ] Échographie mollet droit
> - [ ] **3. Examens d'imagerie ostéo-articulaire**
> 	- [ ] Radiographie genou droit
> 	- [ ] IRM genou droit
> - [ ] **4. Communication avec la patiente**
> 	- [ ] Explications à la patiente des impressions diagnostiques préliminaires
> 	- [ ] Explication du plan de prise en charge
> 	- [ ] Utilisation d'un langage non médical et clarification des termes médicaux
> 	- [ ] Évaluation de l'accord de la patiente avec le plan diagnostique
> 	- [ ] Recherche des préoccupations et questions de la patiente
> 	- [ ] Ne pas répéter les manœuvres douloureuses pendant l'examen physique
> 	- [ ] Remettre le bandage de la patiente
> - [ ] **5. Conseil et soutien**
> 	- [ ] Conseil sur les options de soutien pour les changements de poids et de régime
> 	- [ ] Conseil sur l'arrêt du tabac
> 	- [ ] Réaction appropriée au défi
> 	- [ ] Éducation sur l'importance de la mobilisation précoce
> 	- [ ] Information sur la prévention des TVP
