---
aliases:
  - "Mémento Otalgie"
type: memento-ecos-ssp
ssp: "Otalgie"
specialite: "ORL"
cas: 2
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

# Otalgie

*ORL · 2 grilles · 1 diagnostic documenté* — [[SSP — Otalgie]]

> [!abstract] Les 2 grilles fusionnées
> - **German-28** — Otite moyenne aiguë `corrige` · [grille](<file:///Users/damienfulliquet/Developer/GitHub/grilles-ecos/cases/german/German-28_-_Douleur_a__l_oreille_-_Pe_diatrie_-_Grille_ECOS.html>)
> - **German-65** — Otite moyenne aiguë `corrige` · [grille](<file:///Users/damienfulliquet/Developer/GitHub/grilles-ecos/cases/german/German-65_-_Otorrhe_e_-_Pe_diatrie_-_Grille_ECOS.html>)

> [!note] 📋 Anamnèse
> - [ ] **1. Présentation avec nom, fonction et objectif de la consultation *(1 grille sur 2)***
> - [ ] **2. Question ouverte pour identifier le problème actuel *(1 grille sur 2)***
> - [ ] **3. Caractérisation temporelle des symptômes *(1 grille sur 2)***
> 	- [ ] Début des symptômes
> 	- [ ] Évolution/aggravation
> - [ ] **4. Symptômes auriculaires spécifiques *(1 grille sur 2)***
> 	- [ ] Hypoacousie
> 	- [ ] Otorrhée (cérumen, sang, pus)
> 	- [ ] Douleur
> 	- [ ] Acouphènes ou vertiges
> - [ ] **5. Symptômes associés *(1 grille sur 2)***
> 	- [ ] Fièvre
> 	- [ ] Toux
> 	- [ ] Rhinorrhée
> 	- [ ] Vomissements
> 	- [ ] Autres symptômes
> - [ ] **6. Antécédents ORL de l'enfant *(1 grille sur 2)***
> 	- [ ] Épisodes antérieurs d'otite
> 	- [ ] Autres maladies ORL
> 	- [ ] Chirurgies ORL
> - [ ] **7. Antécédents médicaux généraux *(1 grille sur 2)***
> 	- [ ] Maladies chroniques
> 	- [ ] Hospitalisations antérieures
> 	- [ ] Allergies connues
> - [ ] **8. Statut vaccinal**
> 	- [ ] Vaccin pneumocoque à jour *(1 grille sur 2)*
> - [ ] **9. Traitements déjà administrés *(1 grille sur 2)***
> 	- [ ] Médicaments donnés
> 	- [ ] Lavage nasal
> 	- [ ] Efficacité
> - [ ] **10. Contexte épidémiologique *(1 grille sur 2)***
> 	- [ ] État de santé de la famille
> 	- [ ] Fréquentation de collectivité
> 	- [ ] Fratrie
> 	- [ ] Cas similaires dans l'entourage
> - [ ] **11. Anamnèse par systèmes**
> 	- [ ] Système respiratoire
> 	- [ ] Système digestif
> 	- [ ] Système cardiovasculaire
> 	- [ ] Système neurologique *(1 grille sur 2)*
> 	- [ ] Hydratation *(1 grille sur 2)*
> - [ ] **12. État général de l'enfant *(1 grille sur 2)***
> 	- [ ] Hydratation
> 	- [ ] Alimentation/appétit
> 	- [ ] Comportement/jeu
> 	- [ ] Sommeil
> - [ ] **13. Antécédents périnataux si pertinents *(1 grille sur 2)***
> 	- [ ] Déroulement de la grossesse
> 	- [ ] Accouchement
> 	- [ ] Période néonatale
> - [ ] **14. Présentation avec nom, fonction et tâche *(1 grille sur 2)***
> - [ ] **15. Problème actuel principal *(1 grille sur 2)***
> - [ ] **16. Caractéristiques temporelles *(1 grille sur 2)***
> 	- [ ] Apparition soudaine
> 	- [ ] Aggravation des symptômes
> - [ ] **17. Caractérisation de l'écoulement *(1 grille sur 2)***
> 	- [ ] Type de sécrétion (cérumen, sang, pus)
> 	- [ ] Aspect
> 	- [ ] Odeur
> 	- [ ] Quantité
> - [ ] **18. Symptômes auriculaires associés *(1 grille sur 2)***
> 	- [ ] Douleur
> 	- [ ] Hypoacousie
> 	- [ ] Acouphènes
> 	- [ ] Vertiges
> - [ ] **19. Symptômes généraux *(1 grille sur 2)***
> 	- [ ] Fièvre
> 	- [ ] Toux
> 	- [ ] Rhinorrhée
> 	- [ ] Vomissements
> 	- [ ] État général
> - [ ] **20. Antécédents médicaux *(1 grille sur 2)***
> 	- [ ] Pathologies antérieures
> 	- [ ] Épisodes d'otite antérieurs
> 	- [ ] Hospitalisations
> - [ ] **21. Traitements en cours *(1 grille sur 2)***
> 	- [ ] Antibiotiques
> 	- [ ] Paracétamol
> 	- [ ] Lavage nasal
> 	- [ ] Amélioration avec traitement
> - [ ] **22. Contexte environnemental *(1 grille sur 2)***
> 	- [ ] État de santé familial
> 	- [ ] Fréquentation de collectivité
> 	- [ ] Fratrie
> - [ ] **23. Questions de clôture *(1 grille sur 2)***
> 	- [ ] Avez-vous des questions ?
> 	- [ ] Y a-t-il autre chose d'important ?

> [!tip] 🩺 Status
> - [ ] **1. Inspection de l'oreille externe**
> 	- [ ] Pavillon auriculaire *(1 grille sur 2)*
> 	- [ ] Région rétro-auriculaire *(1 grille sur 2)*
> 	- [ ] Signes inflammatoires externes *(1 grille sur 2)*
> - [ ] **2. Palpation auriculaire**
> 	- [ ] Douleur à la pression du tragus *(1 grille sur 2)*
> 	- [ ] Douleur à la traction du pavillon *(1 grille sur 2)*
> 	- [ ] Palpation mastoïdienne
> 	- [ ] Pression du tragus *(1 grille sur 2)*
> 	- [ ] Traction du pavillon *(1 grille sur 2)*
> - [ ] **3. Otoscopie bilatérale**
> 	- [ ] Tympan droit *(1 grille sur 2)*
> 	- [ ] Tympan gauche *(1 grille sur 2)*
> 	- [ ] Présence d'épanchement *(1 grille sur 2)*
> 	- [ ] État du conduit auditif externe *(1 grille sur 2)*
> 	- [ ] Oreille droite *(1 grille sur 2)*
> 	- [ ] Oreille gauche *(1 grille sur 2)*
> 	- [ ] Conduit auditif externe *(1 grille sur 2)*
> - [ ] **4. Examen de l'oropharynx *(1 grille sur 2)***
> 	- [ ] Pharynx
> 	- [ ] Amygdales
> 	- [ ] Présence d'exsudat
> - [ ] **5. Palpation des aires ganglionnaires *(1 grille sur 2)***
> 	- [ ] Ganglions cervicaux
> 	- [ ] Ganglions rétro-auriculaires
> 	- [ ] Ganglions sous-mandibulaires
> - [ ] **6. Auscultation cardiopulmonaire *(1 grille sur 2)***
> 	- [ ] Auscultation pulmonaire
> 	- [ ] Auscultation cardiaque
> - [ ] **7. Examen abdominal**
> 	- [ ] Palpation abdominale *(1 grille sur 2)*
> 	- [ ] Recherche d'hépatomégalie *(1 grille sur 2)*
> 	- [ ] Recherche de splénomégalie *(1 grille sur 2)*
> - [ ] **8. Recherche de signes de gravité *(1 grille sur 2)***
> 	- [ ] Douleur à la percussion mastoïdienne
> 	- [ ] Décollement du pavillon
> 	- [ ] Signes méningés
> 	- [ ] État de conscience
> - [ ] **9. Examen ORL complémentaire *(1 grille sur 2)***
> 	- [ ] Oropharynx
> 	- [ ] Rhinoscopie antérieure
> - [ ] **10. Palpation ganglionnaire *(1 grille sur 2)***
> 	- [ ] Ganglions cervicaux
> 	- [ ] Ganglions rétro-auriculaires
> 	- [ ] Ganglions pré-auriculaires
> - [ ] **11. Auscultation cardio-pulmonaire *(1 grille sur 2)***
> 	- [ ] Auscultation pulmonaire
> 	- [ ] Auscultation cardiaque
> - [ ] **12. Recherche de complications *(1 grille sur 2)***
> 	- [ ] Signes de mastoïdite
> 	- [ ] Signes méningés
> 	- [ ] Paralysie faciale

> [!success] 💊 Management — si Otite moyenne aiguë
> - [ ] **1. Énonce le diagnostic principal *(1 grille sur 2)***
> 	- [ ] Otite moyenne aiguë
> - [ ] **2. Évoque les diagnostics différentiels pertinents *(1 grille sur 2)***
> - [ ] **3. Propose les examens complémentaires appropriés *(1 grille sur 2)***
> 	- [ ] En général, pas d'examens nécessaires si clinique claire
> 	- [ ] Bilan biologique si signes de gravité
> 	- [ ] Test rapide streptocoque si suspicion d'angine associée
> 	- [ ] Tympanométrie si doute diagnostique
> - [ ] **4. Propose une stratégie thérapeutique adaptée *(1 grille sur 2)***
> - [ ] **5. Informe sur les complications possibles *(1 grille sur 2)***
> 	- [ ] Mastoïdite
> 	- [ ] Paralysie faciale périphérique (par œdème)
> 	- [ ] Thrombose du sinus latéral
> 	- [ ] Complications intracrâniennes (méningite, abcès cérébral)
> - [ ] **6. Organise le suivi *(1 grille sur 2)***
> 	- [ ] Contrôle à 48-72h si surveillance
> 	- [ ] Contrôle à 1 semaine si antibiotiques
> 	- [ ] Critères de reconsultation urgente
> 	- [ ] Prévention des récidives
> - [ ] **7. Donne des conseils aux parents *(1 grille sur 2)***
> 	- [ ] Surveillance des signes d'alarme
> 	- [ ] Administration correcte des médicaments
> 	- [ ] Importance de l'observance si antibiotiques
> 	- [ ] Mesures de confort
> - [ ] **8. Diagnostic principal *(1 grille sur 2)***
> - [ ] **9. Diagnostics différentiels de l'otorrhée *(1 grille sur 2)***
> 	- [ ] Otite moyenne aiguë purulente perforée
> 	- [ ] Otite externe (mais douleur à la mobilisation)
> 	- [ ] Traumatisme avec fracture du rocher (sang, LCR)
> 	- [ ] Otite moyenne chronique avec cholestéatome (écoulement fétide)
> 	- [ ] Corps étranger surinfecté
> - [ ] **10. Prise en charge thérapeutique *(1 grille sur 2)***
> - [ ] **11. Information sur les complications possibles *(1 grille sur 2)***
> 	- [ ] Mastoïdite (tuméfaction rétro-auriculaire)
> 	- [ ] Paralysie faciale (par œdème du nerf)
> 	- [ ] Thrombose du sinus latéral
> 	- [ ] Complications intracrâniennes (méningite, abcès cérébral)
> 	- [ ] Labyrinthite
> - [ ] **12. Rassurer la mère *(1 grille sur 2)***
> 	- [ ] Perforation tympanique souvent bénéfique (drainage)
> 	- [ ] Cicatrisation spontanée habituelle en 2-3 semaines
> 	- [ ] Amélioration attendue sous antibiotiques
> 	- [ ] Surveillance simple nécessaire
> - [ ] **13. Suivi et surveillance *(1 grille sur 2)***
> 	- [ ] Contrôle clinique dans 48-72h si pas d'amélioration
> 	- [ ] Contrôle ORL à 1 semaine
> 	- [ ] Contrôle de la cicatrisation tympanique à 1 mois
> 	- [ ] Audiométrie si doute sur l'audition
> - [ ] **14. Conseils de prévention *(1 grille sur 2)***
> 	- [ ] Vaccination antipneumococcique à jour
> 	- [ ] Éviter le tabagisme passif
> 	- [ ] Limiter l'usage de la tétine
> 	- [ ] Position semi-assise pour les biberons
> - [ ] **15. Critères de reconsultation urgente *(1 grille sur 2)***
> 	- [ ] Tuméfaction rétro-auriculaire
> 	- [ ] Paralysie faciale
> 	- [ ] Vertiges importants
> 	- [ ] Céphalées intenses
> 	- [ ] Altération de l'état général
