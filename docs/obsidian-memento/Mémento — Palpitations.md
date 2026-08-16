---
aliases:
  - "Mémento Palpitations"
type: memento-ecos-ssp
ssp: "Palpitations"
specialite: "Cardiologie & Vasculaire"
cas: 3
diagnostics: 3
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

# Palpitations ⭐️

*Cardiologie & Vasculaire · 3 grilles · 3 diagnostics documentés · 1 attendu documenté ailleurs · 1 attendu absent du corpus* — [[SSP — Palpitations]]

> [!abstract] Les 3 grilles fusionnées
> - **German-7** — Insuffisance cardiaque (décompensée) `corrige` · [grille](<file:///Users/damienfulliquet/Developer/GitHub/grilles-ecos/cases/german/German-7_-_Bradycardie_-_Grille_ECOS.html>)
> - **German-66** — Palpitations liées au stress et aux stimulants `corrige` · [grille](<file:///Users/damienfulliquet/Developer/GitHub/grilles-ecos/cases/german/German-66_-_Palpitations_-_Grille_ECOS.html>)
> - **German-74** — Fibrillation auriculaire `corrige` · [grille](<file:///Users/damienfulliquet/Developer/GitHub/grilles-ecos/cases/german/German-74_-_Tachycardie_-_Grille_ECOS.html>)

> [!note] 📋 Anamnèse
> - [ ] **1. Présentation avec nom, fonction et tâche**
> - [ ] **2. Question d'entrée ouverte → Symptôme principal *(Fibrillation auriculaire · Insuffisance cardiaque (décompensée))***
> - [ ] **3. Apparition temporelle *(Insuffisance cardiaque (décompensée))***
> 	- [ ] Début soudain – insidieux
> 	- [ ] Durée
> 	- [ ] Évolution paroxystique – persistante – permanente
> 	- [ ] Épisodes antérieurs
> - [ ] **4. Fréquence cardiaque *(Insuffisance cardiaque (décompensée))***
> - [ ] **5. Rythme cardiaque *(Insuffisance cardiaque (décompensée))***
> - [ ] **6. Palpitations ou extrasystoles *(Insuffisance cardiaque (décompensée))***
> - [ ] **7. Facteurs influençants *(Insuffisance cardiaque (décompensée))***
> - [ ] **8. Symptômes d'accompagnement *(Insuffisance cardiaque (décompensée))***
> 	- [ ] Douleurs thoraciques
> 	- [ ] Vertiges/Collapsus
> 	- [ ] Fatigue
> 	- [ ] Dyspnée
> 	- [ ] Œdèmes
> 	- [ ] Évolution pondérale
> 	- [ ] Diurèse augmentée
> - [ ] **9. Signes d'hypothyroïdie *(Insuffisance cardiaque (décompensée))***
> 	- [ ] Intolérance au froid
> 	- [ ] Prise de poids
> 	- [ ] Constipation
> 	- [ ] Peau/cheveux
> - [ ] **10. Facteurs de risque cardiovasculaire *(Fibrillation auriculaire · Insuffisance cardiaque (décompensée))***
> 	- [ ] Hypertension *(Insuffisance cardiaque (décompensée))*
> 	- [ ] Tabagisme *(Insuffisance cardiaque (décompensée))*
> 	- [ ] Diabète
> 	- [ ] Dyslipidémie
> 	- [ ] Antécédents familiaux d'infarctus du myocarde *(Insuffisance cardiaque (décompensée))*
> 	- [ ] Hypertension artérielle *(Fibrillation auriculaire)*
> 	- [ ] Obésité (IMC) *(Fibrillation auriculaire)*
> - [ ] **11. Résumé avec retour au patient *(Insuffisance cardiaque (décompensée))***
> - [ ] **12. Antécédents médicaux personnels *(Insuffisance cardiaque (décompensée) · Palpitations liées au stress et aux stimulants)***
> 	- [ ] Maladies cardiaques (coronaropathie, infarctus du myocarde)/chirurgie cardiaque *(Insuffisance cardiaque (décompensée))*
> 	- [ ] Maladies cérébrovasculaires (AIT, AVC) *(Insuffisance cardiaque (décompensée))*
> 	- [ ] Artériopathie périphérique *(Insuffisance cardiaque (décompensée))*
> 	- [ ] Thyroïde *(Insuffisance cardiaque (décompensée))*
> 	- [ ] Chirurgies *(Insuffisance cardiaque (décompensée))*
> 	- [ ] Pathologies connues *(Palpitations liées au stress et aux stimulants)*
> 	- [ ] Hospitalisations *(Palpitations liées au stress et aux stimulants)*
> 	- [ ] Interventions chirurgicales *(Palpitations liées au stress et aux stimulants)*
> - [ ] **13. Allergies *(Insuffisance cardiaque (décompensée))***
> - [ ] **14. Traitements actuels**
> 	- [ ] Euthyrox 50 μg *(Insuffisance cardiaque (décompensée))*
> 	- [ ] Antihypertenseurs *(Fibrillation auriculaire)*
> 	- [ ] Hypolipémiants *(Fibrillation auriculaire)*
> 	- [ ] Anticoagulants/antiagrégants *(Fibrillation auriculaire)*
> 	- [ ] Autres médicaments *(Fibrillation auriculaire)*
> 	- [ ] Observance *(Fibrillation auriculaire)*
> - [ ] **15. Toxiques *(Insuffisance cardiaque (décompensée))***
> 	- [ ] Alcool
> 	- [ ] Tabac
> 	- [ ] Drogues
> - [ ] **16. Anamnèse familiale *(Insuffisance cardiaque (décompensée) · Palpitations liées au stress et aux stimulants)***
> 	- [ ] Maladies cardiovasculaires (coronaropathie, artériopathie, cérébrovasculaire, infarctus du myocarde) *(Insuffisance cardiaque (décompensée))*
> 	- [ ] Diabète, hypertension *(Insuffisance cardiaque (décompensée))*
> 	- [ ] Maladies thyroïdiennes *(Insuffisance cardiaque (décompensée))*
> 	- [ ] Morts subites *(Insuffisance cardiaque (décompensée))*
> 	- [ ] Maladies cardiaques familiales *(Palpitations liées au stress et aux stimulants)*
> 	- [ ] Situation familiale *(Palpitations liées au stress et aux stimulants)*
> 	- [ ] Mère *(Palpitations liées au stress et aux stimulants)*
> 	- [ ] Fratrie *(Palpitations liées au stress et aux stimulants)*
> - [ ] **17. Anamnèse sociale *(Insuffisance cardiaque (décompensée) · Palpitations liées au stress et aux stimulants)***
> 	- [ ] Famille *(Insuffisance cardiaque (décompensée))*
> 	- [ ] Profession *(Insuffisance cardiaque (décompensée))*
> 	- [ ] Habitudes alimentaires *(Insuffisance cardiaque (décompensée))*
> 	- [ ] Loisirs (activités sportives) *(Insuffisance cardiaque (décompensée))*
> 	- [ ] Logement *(Palpitations liées au stress et aux stimulants)*
> 	- [ ] Études *(Palpitations liées au stress et aux stimulants)*
> 	- [ ] Support social *(Palpitations liées au stress et aux stimulants)*
> - [ ] **18. Anamnèse par systèmes *(Insuffisance cardiaque (décompensée) · Palpitations liées au stress et aux stimulants)***
> 	- [ ] Neurologique (AIT, troubles sensitifs, langage) *(Palpitations liées au stress et aux stimulants)*
> 	- [ ] Psychiatrique *(Palpitations liées au stress et aux stimulants)*
> 	- [ ] Cardiaque *(Palpitations liées au stress et aux stimulants)*
> 	- [ ] Thyroïdien *(Palpitations liées au stress et aux stimulants)*
> 	- [ ] Digestif *(Palpitations liées au stress et aux stimulants)*
> 	- [ ] Uro-génital *(Palpitations liées au stress et aux stimulants)*
> - [ ] **19. Motif de consultation *(Palpitations liées au stress et aux stimulants)***
> - [ ] **20. Caractéristiques temporelles *(Palpitations liées au stress et aux stimulants)***
> 	- [ ] Début
> 	- [ ] Moment d'apparition
> 	- [ ] Durée des épisodes
> 	- [ ] Fréquence
> - [ ] **21. Caractéristiques du rythme cardiaque *(Fibrillation auriculaire · Palpitations liées au stress et aux stimulants)***
> 	- [ ] Faire taper le rythme par la patiente *(Palpitations liées au stress et aux stimulants)*
> 	- [ ] Fréquence *(Palpitations liées au stress et aux stimulants)*
> 	- [ ] Régularité *(Palpitations liées au stress et aux stimulants)*
> 	- [ ] Fréquence estimée *(Fibrillation auriculaire)*
> 	- [ ] Régularité du rythme *(Fibrillation auriculaire)*
> 	- [ ] Sensations de pauses *(Fibrillation auriculaire)*
> 	- [ ] Battements manqués ou supplémentaires *(Fibrillation auriculaire)*
> - [ ] **22. Irradiation *(Palpitations liées au stress et aux stimulants)***
> - [ ] **23. Symptômes cardiovasculaires associés *(Fibrillation auriculaire · Palpitations liées au stress et aux stimulants)***
> 	- [ ] Vertiges *(Palpitations liées au stress et aux stimulants)*
> 	- [ ] Syncope/malaise *(Palpitations liées au stress et aux stimulants)*
> 	- [ ] Dyspnée *(Palpitations liées au stress et aux stimulants)*
> 	- [ ] Douleurs thoraciques
> 	- [ ] Oppression thoracique *(Fibrillation auriculaire)*
> 	- [ ] Irradiation éventuelle *(Fibrillation auriculaire)*
> 	- [ ] Lien avec l'effort *(Fibrillation auriculaire)*
> - [ ] **24. Symptômes neurovégétatifs *(Fibrillation auriculaire · Palpitations liées au stress et aux stimulants)***
> 	- [ ] Transpiration *(Palpitations liées au stress et aux stimulants)*
> 	- [ ] Sensation de chaleur *(Palpitations liées au stress et aux stimulants)*
> 	- [ ] Tremblements *(Palpitations liées au stress et aux stimulants)*
> 	- [ ] Nausées
> 	- [ ] Vertiges/malaises *(Fibrillation auriculaire)*
> 	- [ ] Syncope ou présyncope *(Fibrillation auriculaire)*
> 	- [ ] Sueurs *(Fibrillation auriculaire)*
> - [ ] **25. Habitudes alimentaires et hydratation *(Palpitations liées au stress et aux stimulants)***
> 	- [ ] Hydratation
> 	- [ ] Café
> 	- [ ] Appétit
> 	- [ ] Alimentation
> 	- [ ] Poids et taille
> - [ ] **26. Habitudes de vie et toxiques *(Palpitations liées au stress et aux stimulants)***
> 	- [ ] Tabac
> 	- [ ] Alcool
> 	- [ ] Drogues
> - [ ] **27. Activité physique et loisirs *(Palpitations liées au stress et aux stimulants)***
> - [ ] **28. État psychologique et stress *(Palpitations liées au stress et aux stimulants)***
> 	- [ ] Niveau de stress
> 	- [ ] Charge de travail
> 	- [ ] Sentiment de surcharge
> - [ ] **29. Questions de clôture et résumé *(Fibrillation auriculaire · Palpitations liées au stress et aux stimulants)***
> 	- [ ] Résumer les points importants *(Palpitations liées au stress et aux stimulants)*
> 	- [ ] Avez-vous des questions ? *(Palpitations liées au stress et aux stimulants)*
> 	- [ ] Autres informations importantes *(Fibrillation auriculaire)*
> 	- [ ] Questions du patient *(Fibrillation auriculaire)*
> 	- [ ] Résumé de l'anamnèse *(Fibrillation auriculaire)*
> - [ ] **30. Caractérisation temporelle de l'épisode actuel *(Fibrillation auriculaire)***
> 	- [ ] Début
> 	- [ ] Durée actuelle
> 	- [ ] Évolution
> 	- [ ] Fin de l'épisode (spontanée ou provoquée)
> - [ ] **31. Récurrence et historique *(Fibrillation auriculaire)***
> 	- [ ] Épisodes antérieurs
> 	- [ ] Fréquence des épisodes
> 	- [ ] Durée habituelle
> 	- [ ] Évolution dans le temps
> - [ ] **32. Facteurs déclenchants et modulateurs *(Fibrillation auriculaire)***
> 	- [ ] Stress
> 	- [ ] Caféine
> 	- [ ] Alcool
> 	- [ ] Effort physique
> 	- [ ] Position
> 	- [ ] Repas copieux
> - [ ] **33. Symptômes respiratoires *(Fibrillation auriculaire)***
> 	- [ ] Dyspnée
> 	- [ ] Orthopnée
> 	- [ ] Dyspnée paroxystique nocturne
> 	- [ ] Toux
> - [ ] **34. Signes d'insuffisance cardiaque *(Fibrillation auriculaire)***
> 	- [ ] Œdèmes des membres inférieurs
> 	- [ ] Prise de poids récente
> 	- [ ] Fatigue inhabituelle
> 	- [ ] Diminution de la tolérance à l'effort
> - [ ] **35. Symptôme spécifique post-critique *(Fibrillation auriculaire)***
> 	- [ ] Polyurie post-paroxystique
> 	- [ ] Fatigue après l'épisode
> 	- [ ] Durée de récupération
> - [ ] **36. Signes d'hyperthyroïdie *(Fibrillation auriculaire)***
> 	- [ ] Intolérance à la chaleur
> 	- [ ] Perte de poids
> 	- [ ] Diarrhée
> 	- [ ] Tremblements
> - [ ] **37. Symptômes généraux *(Fibrillation auriculaire)***
> 	- [ ] Fièvre
> 	- [ ] Asthénie
> 	- [ ] Anorexie
> 	- [ ] Modifications récentes
> - [ ] **38. Statut ménopausique et hormonal *(Fibrillation auriculaire)***
> 	- [ ] Dernières menstruations
> 	- [ ] Symptômes de ménopause
> 	- [ ] Traitement hormonal substitutif
> 	- [ ] Bouffées de chaleur
> - [ ] **39. Contexte psychosocial *(Fibrillation auriculaire)***
> 	- [ ] Stress aigu récent
> 	- [ ] Charge mentale
> 	- [ ] Anxiété associée
> 	- [ ] Qualité du sommeil
> - [ ] **40. Tabagisme détaillé *(Fibrillation auriculaire)***
> 	- [ ] Consommation actuelle
> 	- [ ] Durée
> 	- [ ] Paquets-années
> 	- [ ] Tentatives d'arrêt
> - [ ] **41. Score de Wells pour embolie pulmonaire *(Fibrillation auriculaire)***
> 	- [ ] Œdème du mollet
> 	- [ ] Immobilisation récente/chirurgie
> 	- [ ] Cancer actif
> 	- [ ] Antécédent de TVP/EP
> 	- [ ] Hémoptysie
> - [ ] **42. Antécédents cardiovasculaires personnels *(Fibrillation auriculaire)***
> 	- [ ] Cardiopathie ischémique
> 	- [ ] Infarctus du myocarde
> 	- [ ] Troubles du rythme connus
> 	- [ ] Valvulopathies
> - [ ] **43. Antécédents neurologiques *(Fibrillation auriculaire)***
> 	- [ ] AVC/AIT
> 	- [ ] Déficit neurologique
> 	- [ ] Céphalées
> 	- [ ] Épilepsie
> - [ ] **44. Autres antécédents médicaux *(Fibrillation auriculaire)***
> 	- [ ] Pathologie thyroïdienne
> 	- [ ] MVTE
> 	- [ ] Pathologies psychiatriques/anxiété
> 	- [ ] Autres maladies chroniques
> - [ ] **45. Antécédents chirurgicaux *(Fibrillation auriculaire)***
> 	- [ ] Interventions antérieures
> 	- [ ] Complications
> 	- [ ] Anesthésies
> - [ ] **46. Allergies médicamenteuses *(Fibrillation auriculaire)***
> 	- [ ] Allergies connues
> 	- [ ] Intolérances
> 	- [ ] Réactions antérieures
> - [ ] **47. Antécédents familiaux cardiovasculaires *(Fibrillation auriculaire)***
> 	- [ ] Infarctus du myocarde
> 	- [ ] Mort subite
> 	- [ ] Troubles du rythme
> 	- [ ] AVC
> - [ ] **48. Habitudes de vie *(Fibrillation auriculaire)***
> 	- [ ] Consommation de café
> 	- [ ] Activité physique
> 	- [ ] Alimentation
> 	- [ ] Consommation d'alcool

> [!tip] 🩺 Status
> - [ ] **1. Auscultation cardiaque *(Fibrillation auriculaire · Insuffisance cardiaque (décompensée))***
> 	- [ ] Inspection *(Insuffisance cardiaque (décompensée))*
> 	- [ ] Palpation *(Insuffisance cardiaque (décompensée))*
> 	- [ ] Percussion *(Insuffisance cardiaque (décompensée))*
> 	- [ ] Auscultation *(Insuffisance cardiaque (décompensée))*
> 	- [ ] Bruits cardiaques *(Fibrillation auriculaire)*
> 	- [ ] Souffles *(Fibrillation auriculaire)*
> 	- [ ] Galop (B3/B4) *(Fibrillation auriculaire)*
> 	- [ ] Frottement péricardique *(Fibrillation auriculaire)*
> - [ ] **2. Status pulmonaire *(Insuffisance cardiaque (décompensée))***
> 	- [ ] Inspection
> 	- [ ] Palpation
> 	- [ ] Percussion
> 	- [ ] Auscultation
> - [ ] **3. Examen thyroïdien *(Insuffisance cardiaque (décompensée) · Palpitations liées au stress et aux stimulants)***
> 	- [ ] Palpation
> 	- [ ] Auscultation *(Insuffisance cardiaque (décompensée))*
> 	- [ ] Inspection *(Palpitations liées au stress et aux stimulants)*
> 	- [ ] Recherche de nodules *(Palpitations liées au stress et aux stimulants)*
> 	- [ ] Recherche de goitre *(Palpitations liées au stress et aux stimulants)*
> - [ ] **4. Examen cutané *(Insuffisance cardiaque (décompensée))***
> - [ ] **5. Signes vitaux *(Palpitations liées au stress et aux stimulants)***
> 	- [ ] Fréquence cardiaque
> 	- [ ] Tension artérielle
> 	- [ ] Fréquence respiratoire
> 	- [ ] Température
> - [ ] **6. Palpation cardiovasculaire *(Fibrillation auriculaire · Palpitations liées au stress et aux stimulants)***
> 	- [ ] Palpation précordiale *(Palpitations liées au stress et aux stimulants)*
> 	- [ ] Auscultation cardiaque en au moins 3 positions *(Palpitations liées au stress et aux stimulants)*
> 	- [ ] Rythme *(Palpitations liées au stress et aux stimulants)*
> 	- [ ] Souffles *(Palpitations liées au stress et aux stimulants)*
> 	- [ ] Bruits surajoutés *(Palpitations liées au stress et aux stimulants)*
> 	- [ ] Pouls périphérique *(Fibrillation auriculaire)*
> 	- [ ] Intensité du pouls *(Fibrillation auriculaire)*
> 	- [ ] Déficit de pouls *(Fibrillation auriculaire)*
> 	- [ ] Choc de pointe *(Fibrillation auriculaire)*
> - [ ] **7. Examen du pouls *(Palpitations liées au stress et aux stimulants)***
> 	- [ ] Pouls radial
> 	- [ ] Régularité
> 	- [ ] Amplitude
> 	- [ ] Symétrie
> - [ ] **8. Examen pulmonaire complet *(Fibrillation auriculaire · Palpitations liées au stress et aux stimulants)***
> 	- [ ] Auscultation antérieure systématique *(Palpitations liées au stress et aux stimulants)*
> 	- [ ] Auscultation postérieure systématique *(Palpitations liées au stress et aux stimulants)*
> 	- [ ] Inspection thoracique *(Fibrillation auriculaire)*
> 	- [ ] Palpation (vibrations vocales) *(Fibrillation auriculaire)*
> 	- [ ] Percussion pulmonaire *(Fibrillation auriculaire)*
> 	- [ ] Auscultation bilatérale *(Fibrillation auriculaire)*
> - [ ] **9. Examen général *(Palpitations liées au stress et aux stimulants)***
> 	- [ ] État général
> 	- [ ] Peau
> 	- [ ] Tremblements
> 	- [ ] Exophtalmie
> - [ ] **10. Examen neurologique sommaire *(Palpitations liées au stress et aux stimulants)***
> 	- [ ] Réflexes ostéo-tendineux
> 	- [ ] Tremblements fins des extrémités
> - [ ] **11. Inspection cardiovasculaire *(Fibrillation auriculaire)***
> 	- [ ] Veines jugulaires
> 	- [ ] Reflux hépato-jugulaire
> 	- [ ] Cyanose
> 	- [ ] Œdèmes périphériques
> - [ ] **12. Percussion cardiaque *(Fibrillation auriculaire)***
> 	- [ ] Matité cardiaque
> 	- [ ] Cardiomégalie
> 	- [ ] Épanchement péricardique
> - [ ] **13. Palpation thyroïdienne *(Fibrillation auriculaire)***
> 	- [ ] Volume thyroïdien
> 	- [ ] Nodules
> 	- [ ] Consistance
> 	- [ ] Mobilité
> - [ ] **14. Auscultation thyroïdienne *(Fibrillation auriculaire)***
> 	- [ ] Souffle thyroïdien
> 	- [ ] Thrill
> - [ ] **15. Examen cutanéo-muqueux *(Fibrillation auriculaire)***
> 	- [ ] Coloration cutanée
> 	- [ ] Conjonctives
> 	- [ ] Muqueuses
> 	- [ ] Temps de recoloration capillaire
> - [ ] **16. Signes périphériques d'insuffisance cardiaque *(Fibrillation auriculaire)***
> 	- [ ] Œdèmes des membres inférieurs
> 	- [ ] Hépatomégalie
> 	- [ ] Ascite
> 	- [ ] Râles pulmonaires

> [!success] 💊 Management — si Fibrillation auriculaire
> - [ ] **1. Diagnostics différentiels**
> - [ ] **2. Traitement médicamenteux au long cours**
> 	- [ ] Bêtabloquants ou inhibiteurs calciques
> 	- [ ] Anticoagulation orale (AOD ou AVK)
> 	- [ ] Antiarythmiques si échec
> 	- [ ] Gestion des facteurs de risque
> - [ ] **3. Diagnostic principal**
> 	- [ ] Fibrillation auriculaire paroxystique
> 	- [ ] Justification clinique
> 	- [ ] Éléments en faveur
> 	- [ ] Score CHA2DS2-VASc à calculer
> - [ ] **4. Prise en charge non médicamenteuse**
> 	- [ ] Surveillance scopée si disponible
> 	- [ ] Contrôle de la fréquence cardiaque
> 	- [ ] Anticoagulation selon score CHA2DS2-VASc
> 	- [ ] Cardioversion si instable
> - [ ] **5. ECG - Réalisation et interprétation**
> 	- [ ] ECG 12 dérivations immédiat
> 	- [ ] Reconnaissance du trouble du rythme
> 	- [ ] Analyse des intervalles
> 	- [ ] Recherche de signes d'ischémie
> - [ ] **6. Examens biologiques - Urgence**
> 	- [ ] Troponine I
> 	- [ ] CK-MB
> 	- [ ] BNP/NT-proBNP
> 	- [ ] D-dimères si suspicion EP
> - [ ] **7. Examens biologiques - Bilan étiologique**
> 	- [ ] FSC (anémie)
> 	- [ ] CRP (inflammation)
> 	- [ ] Ionogramme (Na, K, Ca)
> 	- [ ] Créatinine et DFG
> 	- [ ] TSH (hyperthyroïdie)
> - [ ] **8. Examens biologiques - Bilan pré-thérapeutique**
> 	- [ ] Transaminases (ASAT, ALAT)
> 	- [ ] Gamma-GT, PAL
> 	- [ ] Albumine
> 	- [ ] TP/INR, aPTT
> - [ ] **9. Imagerie et examens complémentaires**
> 	- [ ] Radiographie thoracique
> 	- [ ] Échocardiographie transthoracique
> 	- [ ] Holter ECG 24h si diagnostic incertain
> 	- [ ] Angio-TDM thoracique si suspicion EP
> - [ ] **10. Orientation et suivi**
> 	- [ ] Nécessité d'hospitalisation évaluée
> 	- [ ] Consultation cardiologie
> 	- [ ] Éducation thérapeutique
> 	- [ ] Suivi régulier

> [!success] 💊 Management — si Insuffisance cardiaque (décompensée)
> - [ ] **1. Diagnostic de suspicion**
> - [ ] **2. Diagnostics différentiels**
> - [ ] **3. Examens diagnostiques**
> 	- [ ] Laboratoire : FSC, CRP, Ferritine, Troponine I, CK-MB, LDH
> 	- [ ] Créatinine, électrolytes (Na, K, Ca), TSH, Glucose
> 	- [ ] Transaminases, Gamma-GT, phosphatases alcalines (PAL), Albumine, Quick/aPTT
> 	- [ ] Radiographie thoracique / ECG (24h) / Échocardiographie
> 	- [ ] Éventuellement angio-CT (si suspicion d'embolie pulmonaire)
> 	- [ ] Éventuellement dosage médicamenteux (bêta-bloquants)
> - [ ] **4. Reconnaissance de pathologie**
> - [ ] **5. Traitement médicamenteux au long cours**
> 	- [ ] Parasympatholytiques : Atropine 0,5-1 mg IV
> 	- [ ] Sympathomimétiques : Adrénaline 0,1 mg IV
> - [ ] **6. Traitement par stimulateur cardiaque**
> 	- [ ] Indications absolues : Fibrillation auriculaire, Bloc AV II°/III°
> 	- [ ] Indications relatives : Bradycardie symptomatique
> - [ ] **7. Hospitalisation si nécessaire**

> [!success] 💊 Management — si Palpitations liées au stress et aux stimulants
> - [ ] **1. Diagnostics différentiels**
> 	- [ ] Tachycardie supraventriculaire paroxystique
> 	- [ ] Hyperthyroïdie
> 	- [ ] Trouble anxieux/attaque de panique
> 	- [ ] Arythmie induite par la cocaïne
> 	- [ ] Anémie
> 	- [ ] Phéochromocytome (rare)
> - [ ] **2. Traitement médicamenteux au long cours**
> 	- [ ] Bêta-bloquants si échec des mesures hygiéno-diététiques
> 	- [ ] Anxiolytiques ponctuels si composante anxieuse marquée
> 	- [ ] Traitement spécifique selon résultats (fer si anémie, etc.)
> - [ ] **3. Diagnostic principal**
> - [ ] **4. Examens complémentaires**
> 	- [ ] Biologie : FSC (anémie), TSH (hyperthyroïdie), ionogramme
> 	- [ ] ECG de repos
> 	- [ ] Holter ECG 24h si récidive
> 	- [ ] Échocardiographie si anomalie ECG
> 	- [ ] Test toxicologique urinaire si besoin
> - [ ] **5. Prise en charge non médicamenteuse**
> - [ ] **6. Conseils spécifiques sur les substances**
> 	- [ ] Information sur les risques cardiaques de la cocaïne
> 	- [ ] Orientation vers consultation d'addictologie si besoin
> 	- [ ] Aide au sevrage tabagique
> 	- [ ] Alternatives au café (tisanes, décaféiné)
> - [ ] **7. Suivi**
> 	- [ ] Contrôle à 2-4 semaines
> 	- [ ] Journal des palpitations
> 	- [ ] Réévaluation après modifications du mode de vie
> 	- [ ] ECG de contrôle si persistance
> - [ ] **8. Éducation et prévention**
> 	- [ ] Explication du cercle vicieux stress-palpitations
> 	- [ ] Techniques d'autogestion
> 	- [ ] Signes d'alerte nécessitant une consultation
> 	- [ ] Importance de l'observance des changements

> [!success] 💊 Management — si Tachycardie supraventriculaire (TSV/WPW)
> *Aucune grille du corpus ne documente ce diagnostic* — il est pourtant attendu de cette SSP. **Trou de révision à combler ailleurs.**

> [!success] 💊 Management — si Trouble anxieux
> *Aucune grille de cette SSP ne documente ce diagnostic* — mais le corpus le documente ailleurs : [[Mémento — Trouble Anxieux]] (4 grilles) · [[Mémento — Troubles du Sommeil]] (1 grille).
