---
aliases:
  - "Mémento Troubles du Développement & Croissance"
type: memento-ecos-ssp
ssp: "Troubles du Développement & Croissance"
specialite: "Pédiatrie"
cas: 1
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

# Troubles du Développement & Croissance

*Pédiatrie · 1 grille · 1 diagnostic documenté* — [[SSP — Troubles du Développement & Croissance]]

> [!abstract] La seule grille de cette SSP
> - **German-14** — Trouble du déficit de l'attention avec hyperactivité `corrige` · [grille](<file:///Users/damienfulliquet/Developer/GitHub/grilles-ecos/cases/german/German-14_-_Difficulte_s_scolaires_-_Pe_diatrie_-_Grille_ECOS.html>)

> [!note] 📋 Anamnèse
> - [ ] **1. Présentation avec nom, fonction et tâche**
> - [ ] **2. Problème principal**
> - [ ] **3. Âge du fils**
> - [ ] **4. Début et évolution de la symptomatologie**
> 	- [ ] Quand ont commencé les difficultés ?
> 	- [ ] Évolution progressive ou soudaine ?
> 	- [ ] Événement déclencheur ?
> - [ ] **5. Sommeil**
> 	- [ ] Heure du coucher et du lever
> 	- [ ] Qualité du sommeil
> 	- [ ] Cauchemars ou terreurs nocturnes
> 	- [ ] Ronflement ou apnées
> - [ ] **6. Comportement à l'école**
> 	- [ ] Résultats scolaires
> 	- [ ] Devoirs
> 	- [ ] Relation avec les enseignants
> 	- [ ] Comportement en classe
> - [ ] **7. Comportement à la maison**
> 	- [ ] Respect des règles
> 	- [ ] Disputes et opposition
> 	- [ ] Relations familiales
> - [ ] **8. Attention et concentration**
> 	- [ ] Capacité à se concentrer sur une tâche
> 	- [ ] Distractibilité
> 	- [ ] Oublis fréquents
> - [ ] **9. Hyperactivité motrice**
> 	- [ ] Agitation
> 	- [ ] Incapacité à rester assis
> 	- [ ] Parle excessivement
> - [ ] **10. Impulsivité**
> 	- [ ] Interrompt les autres
> 	- [ ] Agit sans réfléchir
> 	- [ ] Difficultés à attendre son tour
> - [ ] **11. Relations sociales**
> 	- [ ] Amitiés
> 	- [ ] Jeux avec les autres enfants
> 	- [ ] Comportements agressifs
> - [ ] **12. Activités de loisirs**
> 	- [ ] Sports pratiqués
> 	- [ ] Hobbies
> 	- [ ] Temps d'écran
> - [ ] **13. Fratrie**
> - [ ] **14. Habitudes alimentaires**
> 	- [ ] Boissons sucrées
> 	- [ ] Régime alimentaire
> - [ ] **15. Affect et humeur**
> 	- [ ] Tristesse
> 	- [ ] Anxiété
> 	- [ ] Estime de soi
> - [ ] **16. Développement psychomoteur**
> 	- [ ] Âge de la marche
> 	- [ ] Développement du langage
> 	- [ ] Acquisition de la propreté
> - [ ] **17. Grossesse et accouchement**
> 	- [ ] Déroulement de la grossesse
> 	- [ ] Complications
> 	- [ ] Poids de naissance
> 	- [ ] Terme
> - [ ] **18. Antécédents personnels**
> 	- [ ] Épilepsie
> 	- [ ] Traumatisme crânien
> 	- [ ] Déficit intellectuel
> 	- [ ] Troubles sensoriels
> - [ ] **19. Antécédents familiaux**
> 	- [ ] TDAH dans la famille
> 	- [ ] Troubles de l'apprentissage
> 	- [ ] Troubles psychiatriques
> - [ ] **20. Médicaments et substances**

> [!tip] 🩺 Status
> - [ ] **1. Examen clinique général**
> 	- [ ] État général
> 	- [ ] Paramètres vitaux
> 	- [ ] Poids et taille (courbes de croissance)
> - [ ] **2. Examen neurologique de base**
> 	- [ ] Réflexes
> 	- [ ] Tonus
> 	- [ ] Coordination motrice
> 	- [ ] Mouvements anormaux
> - [ ] **3. Évaluation du comportement pendant la consultation**
> 	- [ ] Agitation
> 	- [ ] Capacité d'attention
> 	- [ ] Interaction avec l'examinateur
> - [ ] **4. Examen sensoriel**
> 	- [ ] Vision
> 	- [ ] Audition
> - [ ] **5. Recherche de signes d'hyperthyroïdie**
> 	- [ ] Thyroïde
> 	- [ ] Tremblements
> 	- [ ] Tachycardie

> [!success] 💊 Management — si Trouble du déficit de l'attention avec hyperactivité
> - [ ] **1. Diagnostic principal évoqué**
> - [ ] **2. Diagnostics différentiels**
> - [ ] **3. Examens complémentaires**
> 	- [ ] Bilan biologique avec TSH
> 	- [ ] Bilan ferrique (ferritine)
> 	- [ ] Glycémie
> 	- [ ] Évaluation psychométrique si indiquée
> - [ ] **4. Prise en charge immédiate**
> 	- [ ] Entretien direct avec l'enfant
> 	- [ ] Contact avec l'enseignant
> 	- [ ] Questionnaires standardisés (Conners, SNAP-IV)
> 	- [ ] Conseils hygiéno-diététiques (réduction Coca-Cola, temps d'écran)
> - [ ] **5. Orientation spécialisée**
> 	- [ ] Pédopsychiatre pour évaluation approfondie
> 	- [ ] Psychologue pour bilan cognitif si nécessaire
> 	- [ ] Orthophoniste si troubles associés
> - [ ] **6. Traitement médicamenteux**
> 	- [ ] Discussion sur méthylphénidate (Ritaline®, Concerta®)
> 	- [ ] Alternative : atomoxétine
> 	- [ ] Après confirmation diagnostique par spécialiste
> - [ ] **7. Question de la mère sur la Ritaline**
> - [ ] **8. Réponse appropriée sur le traitement**
> 	- [ ] Amélioration du développement chez les enfants TDAH traités
> 	- [ ] Normalisation des fonctions cérébrales altérées
> 	- [ ] Meilleurs résultats scolaires et sociaux
> 	- [ ] Surveillance régulière nécessaire
> - [ ] **9. Approches non médicamenteuses**
> 	- [ ] Thérapie comportementale
> 	- [ ] Guidance parentale
> 	- [ ] Aménagements scolaires
> 	- [ ] Activité physique régulière
> - [ ] **10. Suivi proposé**
> 	- [ ] Consultation de contrôle dans 4-6 semaines
> 	- [ ] Coordination avec le pédopsychiatre
> 	- [ ] Réévaluation régulière
