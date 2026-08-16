---
aliases:
  - "Mémento Syncope & Perte de Connaissance"
type: memento-ecos-ssp
ssp: "Syncope & Perte de Connaissance"
cas: 7
diagnostics: 6
attendus_documentes_ailleurs: 0
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

# Syncope & Perte de Connaissance

*7 grilles · 6 diagnostics documentés · 2 attendus absents du corpus* — [[SSP — Syncope & Perte de Connaissance]]

> [!abstract] Les 7 grilles fusionnées
> - **AZYGOS-38** — Première crise épileptique focale bilatéralisée `diagnostic-travail` · [grille](<file:///Users/damienfulliquet/Developer/GitHub/grilles-ecos/docs/azygos-grilles/c99ece2f-dc30-4162-815d-060732943dca.json>)
> - **AZYGOS-46** — Syncope avec suspicion d’origine arythmogène (syndrome de Brugada) `diagnostic-travail` · [grille](<file:///Users/damienfulliquet/Developer/GitHub/grilles-ecos/docs/azygos-grilles/0621c04a-0d48-4b2e-bb2f-7a87487f2115.json>)
> - **German-41** — Première crise convulsive tonico-clonique `corrige` · [grille](<file:///Users/damienfulliquet/Developer/GitHub/grilles-ecos/cases/german/German-41_-_Epilepsie_-_Grille_ECOS.html>)
> - **German-60** — HypoTA orthostatique `explicite` · [grille](<file:///Users/damienfulliquet/Developer/GitHub/grilles-ecos/cases/german/German-60_-_Malaise_-_Grille_ECOS.html>)
> - **German-61** — BAV `explicite` · [grille](<file:///Users/damienfulliquet/Developer/GitHub/grilles-ecos/cases/german/German-61_-_Malaise_-_Grille_ECOS.html>)
> - **RESCOS-49** — Hypoglycémie `confirme` · [grille](<file:///Users/damienfulliquet/Developer/GitHub/grilles-ecos/cases/rescos/RESCOS-49%20-%20Malaise%20-%20Grille%20ECOS.html>)
> - **RESCOS-50** — HypoTA orthostatique `explicite` · [grille](<file:///Users/damienfulliquet/Developer/GitHub/grilles-ecos/cases/rescos/RESCOS-50%20-%20Malaise%20-%20Grille%20ECOS.html>)

> [!note] 📋 Anamnèse
> - [ ] **1. Question d’ouverture *(Première crise épileptique focale bilatéralisée)***
> - [ ] **2. Traumatisme de chute *(Première crise épileptique focale bilatéralisée)***
> - [ ] **3. Dimension temporelle *(Première crise épileptique focale bilatéralisée)***
> - [ ] **4. Moment *(Première crise épileptique focale bilatéralisée · Syncope avec suspicion d’origine arythmogène (syndrome de Brugada))***
> - [ ] **5. Durée *(Première crise épileptique focale bilatéralisée · Syncope avec suspicion d’origine arythmogène (syndrome de Brugada))***
> - [ ] **6. Premier événement *(Première crise épileptique focale bilatéralisée)***
> - [ ] **7. Répétition *(Première crise épileptique focale bilatéralisée)***
> - [ ] **8. Déclencheurs *(Première crise épileptique focale bilatéralisée)***
> - [ ] **9. Symptômes associés *(2 grilles sur 7)***
> 	- [ ] Sensations vertigineuses avant la perte de connaissance *(1 grille sur 7)*
> 	- [ ] Voile noir et étoiles avant l'épisode *(1 grille sur 7)*
> 	- [ ] Tremblements pendant l'épisode selon les parents *(1 grille sur 7)*
> 	- [ ] Symptômes disparus au réveil *(1 grille sur 7)*
> - [ ] **10. Aura *(Première crise épileptique focale bilatéralisée)***
> - [ ] **11. Sémiologie de la crise *(Première crise épileptique focale bilatéralisée)***
> - [ ] **12. Secousses *(Première crise épileptique focale bilatéralisée)***
> - [ ] **13. Focalité de la crise *(Première crise épileptique focale bilatéralisée)***
> - [ ] **14. Pattern de la crise *(Première crise épileptique focale bilatéralisée)***
> - [ ] **15. Conscience *(Première crise épileptique focale bilatéralisée)***
> - [ ] **16. Yeux/déviation du regard *(Première crise épileptique focale bilatéralisée)***
> - [ ] **17. Stigmates *(Première crise épileptique focale bilatéralisée)***
> - [ ] **18. Réorientation postictale *(Première crise épileptique focale bilatéralisée)***
> - [ ] **19. Symptômes SNC *(Première crise épileptique focale bilatéralisée)***
> - [ ] **20. Céphalées *(Première crise épileptique focale bilatéralisée)***
> - [ ] **21. Vertiges *(Première crise épileptique focale bilatéralisée)***
> - [ ] **22. Nausées/vomissements *(Première crise épileptique focale bilatéralisée)***
> - [ ] **23. Déficits focaux *(Première crise épileptique focale bilatéralisée)***
> - [ ] **24. Trouble visuel *(Première crise épileptique focale bilatéralisée)***
> - [ ] **25. Trouble sensitif *(Première crise épileptique focale bilatéralisée)***
> - [ ] **26. Paralysies *(Première crise épileptique focale bilatéralisée)***
> - [ ] **27. Bilan de syncope *(Première crise épileptique focale bilatéralisée)***
> - [ ] **28. Symptômes cardiaques *(Première crise épileptique focale bilatéralisée)***
> - [ ] **29. Prodromes de syncope *(Première crise épileptique focale bilatéralisée)***
> - [ ] **30. Fièvre/infection *(Première crise épileptique focale bilatéralisée)***
> - [ ] **31. Symptômes B *(BAV · Première crise convulsive tonico-clonique · Première crise épileptique focale bilatéralisée)***
> 	- [ ] Fièvre *(BAV · Première crise convulsive tonico-clonique)*
> 	- [ ] Sueurs nocturnes *(BAV · Première crise convulsive tonico-clonique)*
> 	- [ ] Perte de poids *(BAV · Première crise convulsive tonico-clonique)*
> 	- [ ] Anorexie *(BAV)*
> - [ ] **32. Antécédents *(Première crise épileptique focale bilatéralisée)***
> - [ ] **33. Antécédents généraux *(Première crise épileptique focale bilatéralisée · Syncope avec suspicion d’origine arythmogène (syndrome de Brugada))***
> - [ ] **34. Antécédents neurologiques *(Première crise épileptique focale bilatéralisée)***
> - [ ] **35. Antécédents chirurgicaux *(BAV · Première crise épileptique focale bilatéralisée · Syncope avec suspicion d’origine arythmogène (syndrome de Brugada))***
> 	- [ ] Interventions antérieures *(BAV)*
> 	- [ ] Complications post-opératoires *(BAV)*
> 	- [ ] Anesthésies antérieures *(BAV)*
> - [ ] **36. Médicaments actuels *(4 diagnostics)***
> 	- [ ] Attention : antidépresseurs, neuroleptiques, tramadol abaissent le seuil épileptogène *(Première crise convulsive tonico-clonique)*
> 	- [ ] Antihypertenseurs *(BAV)*
> 	- [ ] Antidiabétiques *(BAV)*
> 	- [ ] Autres traitements *(BAV)*
> 	- [ ] Observance thérapeutique *(BAV)*
> - [ ] **37. Noxes *(Première crise épileptique focale bilatéralisée · Syncope avec suspicion d’origine arythmogène (syndrome de Brugada))***
> - [ ] **38. Alcool *(Première crise épileptique focale bilatéralisée · Syncope avec suspicion d’origine arythmogène (syndrome de Brugada))***
> - [ ] **39. Tabagisme *(Première crise épileptique focale bilatéralisée · Syncope avec suspicion d’origine arythmogène (syndrome de Brugada))***
> - [ ] **40. Drogues *(Première crise épileptique focale bilatéralisée)***
> - [ ] **41. Allergies *(Première crise convulsive tonico-clonique · Première crise épileptique focale bilatéralisée · Syncope avec suspicion d’origine arythmogène (syndrome de Brugada))***
> - [ ] **42. Antécédents familiaux *(5 diagnostics)***
> 	- [ ] Père *(Première crise convulsive tonico-clonique)*
> 	- [ ] Mère *(Première crise convulsive tonico-clonique)*
> 	- [ ] Fratrie *(Première crise convulsive tonico-clonique)*
> 	- [ ] Épilepsie familiale *(Première crise convulsive tonico-clonique)*
> 	- [ ] Tumeur cérébrale familiale *(Première crise convulsive tonico-clonique)*
> 	- [ ] Maladies cardiovasculaires familiales *(1 grille sur 7)*
> 	- [ ] Hypotension familiale *(1 grille sur 7)*
> 	- [ ] Autres pathologies héréditaires *(1 grille sur 7)*
> 	- [ ] Causes de décès *(1 grille sur 7)*
> 	- [ ] Mort subite familiale *(BAV)*
> 	- [ ] Maladies cardiaques *(BAV)*
> 	- [ ] Troubles du rythme familiaux *(BAV)*
> 	- [ ] État de santé de la mère *(BAV)*
> 	- [ ] Pas d'antécédents familiaux de syncope, épilepsie ou pathologie cardiaque *(1 grille sur 7)*
> - [ ] **43. Épilepsie familiale *(Première crise épileptique focale bilatéralisée)***
> - [ ] **44. Cancers familiaux *(Première crise épileptique focale bilatéralisée)***
> - [ ] **45. Situation de vie *(Première crise épileptique focale bilatéralisée)***
> - [ ] **46. Réseau social *(Première crise épileptique focale bilatéralisée)***
> - [ ] **47. Question initiale *(Syncope avec suspicion d’origine arythmogène (syndrome de Brugada))***
> - [ ] **48. Déroulement (hétéro-anamnèse) *(Syncope avec suspicion d’origine arythmogène (syndrome de Brugada))***
> - [ ] **49. Mécanisme de chute *(Syncope avec suspicion d’origine arythmogène (syndrome de Brugada))***
> - [ ] **50. Secousses / crampes *(Syncope avec suspicion d’origine arythmogène (syndrome de Brugada))***
> - [ ] **51. Déviation oculaire *(Syncope avec suspicion d’origine arythmogène (syndrome de Brugada))***
> - [ ] **52. Réorientation *(Syncope avec suspicion d’origine arythmogène (syndrome de Brugada))***
> - [ ] **53. Choc cranien *(Syncope avec suspicion d’origine arythmogène (syndrome de Brugada))***
> - [ ] **54. Activité immédiatement avant la perte de connaissance *(Syncope avec suspicion d’origine arythmogène (syndrome de Brugada))***
> - [ ] **55. Déclencheurs / triggers *(Syncope avec suspicion d’origine arythmogène (syndrome de Brugada))***
> - [ ] **56. Orthostatisme / changement de position *(Syncope avec suspicion d’origine arythmogène (syndrome de Brugada))***
> - [ ] **57. Déclencheurs situationnels (toux / éternuement / déglutition) *(Syncope avec suspicion d’origine arythmogène (syndrome de Brugada))***
> - [ ] **58. Déclencheurs vasovagaux (émotion / excitation / douleur) *(Syncope avec suspicion d’origine arythmogène (syndrome de Brugada))***
> - [ ] **59. Temps d’avertissement *(Syncope avec suspicion d’origine arythmogène (syndrome de Brugada))***
> - [ ] **60. Prodromes *(Syncope avec suspicion d’origine arythmogène (syndrome de Brugada))***
> - [ ] **61. Vertiges / étourdissements *(Syncope avec suspicion d’origine arythmogène (syndrome de Brugada))***
> - [ ] **62. Visuel (voile noir / tunnel / scintillement) *(Syncope avec suspicion d’origine arythmogène (syndrome de Brugada))***
> - [ ] **63. Auditif (sourd / bourdonnement) *(Syncope avec suspicion d’origine arythmogène (syndrome de Brugada))***
> - [ ] **64. Végétatif (nausées / sueurs / sensation de chaleur) *(Syncope avec suspicion d’origine arythmogène (syndrome de Brugada))***
> - [ ] **65. Symptômes accompagnants *(Syncope avec suspicion d’origine arythmogène (syndrome de Brugada))***
> - [ ] **66. Syncopes / présyncopes antérieures *(Syncope avec suspicion d’origine arythmogène (syndrome de Brugada))***
> - [ ] **67. Symptômes thoraciques (actuels / péri-syncope / à l’effort) *(Syncope avec suspicion d’origine arythmogène (syndrome de Brugada))***
> - [ ] **68. Douleurs thoraciques / oppression *(Syncope avec suspicion d’origine arythmogène (syndrome de Brugada))***
> - [ ] **69. Dyspnée *(Syncope avec suspicion d’origine arythmogène (syndrome de Brugada))***
> - [ ] **70. Palpitations *(Syncope avec suspicion d’origine arythmogène (syndrome de Brugada))***
> - [ ] **71. Douleurs liées à la chute *(Syncope avec suspicion d’origine arythmogène (syndrome de Brugada))***
> - [ ] **72. Gonflement / douleur des jambes *(Syncope avec suspicion d’origine arythmogène (syndrome de Brugada))***
> - [ ] **73. Symptômes infectieux / généraux *(Syncope avec suspicion d’origine arythmogène (syndrome de Brugada))***
> - [ ] **74. Fièvre / température *(Syncope avec suspicion d’origine arythmogène (syndrome de Brugada))***
> - [ ] **75. Anamnèse d’infection *(Syncope avec suspicion d’origine arythmogène (syndrome de Brugada))***
> - [ ] **76. Voies respiratoires supérieures (maux de gorge / rhume) *(Syncope avec suspicion d’origine arythmogène (syndrome de Brugada))***
> - [ ] **77. Voies respiratoires inférieures (toux / expectoration) *(Syncope avec suspicion d’origine arythmogène (syndrome de Brugada))***
> - [ ] **78. Céphalées / raideur de nuque *(Syncope avec suspicion d’origine arythmogène (syndrome de Brugada))***
> - [ ] **79. Myalgies *(Syncope avec suspicion d’origine arythmogène (syndrome de Brugada))***
> - [ ] **80. Anamnèse environnementale *(Syncope avec suspicion d’origine arythmogène (syndrome de Brugada))***
> - [ ] **81. DD Symptômes neurologiques *(Syncope avec suspicion d’origine arythmogène (syndrome de Brugada))***
> - [ ] **82. Morsure de langue *(Syncope avec suspicion d’origine arythmogène (syndrome de Brugada))***
> - [ ] **83. Perte d’urines / selles *(Syncope avec suspicion d’origine arythmogène (syndrome de Brugada))***
> - [ ] **84. Symptômes neurologiques focaux *(Syncope avec suspicion d’origine arythmogène (syndrome de Brugada))***
> - [ ] **85. Longs voyages / immobilisation *(Syncope avec suspicion d’origine arythmogène (syndrome de Brugada))***
> - [ ] **86. Antécédents médicaux *(Syncope avec suspicion d’origine arythmogène (syndrome de Brugada))***
> - [ ] **87. Antécédents cardiaques / troubles du rythme *(Syncope avec suspicion d’origine arythmogène (syndrome de Brugada))***
> - [ ] **88. Drogues / stimulants *(Syncope avec suspicion d’origine arythmogène (syndrome de Brugada))***
> - [ ] **89. Maladies familiales générales *(Syncope avec suspicion d’origine arythmogène (syndrome de Brugada))***
> - [ ] **90. Mort subite cardiaque dans la famille *(Syncope avec suspicion d’origine arythmogène (syndrome de Brugada))***
> - [ ] **91. Profession *(Syncope avec suspicion d’origine arythmogène (syndrome de Brugada))***
> - [ ] **92. Situation sociale *(Syncope avec suspicion d’origine arythmogène (syndrome de Brugada))***
> - [ ] **93. Présentation avec nom, fonction et tâche *(3 grilles sur 7)***
> - [ ] **94. Question ouverte initiale → symptôme principal *(Première crise convulsive tonico-clonique)***
> - [ ] **95. Évolution temporelle de la crise *(Première crise convulsive tonico-clonique)***
> 	- [ ] Début
> 	- [ ] Durée de la crise
> 	- [ ] Fréquence
> - [ ] **96. Caractéristiques de la crise *(Première crise convulsive tonico-clonique)***
> 	- [ ] Localisation
> 	- [ ] Type
> - [ ] **97. Phase post-critique *(Première crise convulsive tonico-clonique)***
> 	- [ ] Désorientation
> 	- [ ] Somnolence
> 	- [ ] Agitation
> 	- [ ] Myalgies
> 	- [ ] Amnésie
> - [ ] **98. Facteurs de provocation *(Première crise convulsive tonico-clonique)***
> 	- [ ] Privation de sommeil
> 	- [ ] Consommation d'alcool/drogues
> 	- [ ] Stress émotionnel
> 	- [ ] Photostimulation
> 	- [ ] Traumatisme crânien
> - [ ] **99. Prodromes et aura *(Première crise convulsive tonico-clonique)***
> 	- [ ] Aura épigastrique
> 	- [ ] Aura olfactive
> 	- [ ] Aura visuelle
> 	- [ ] Aura auditive
> - [ ] **100. Signes accompagnateurs de la crise *(Première crise convulsive tonico-clonique)***
> 	- [ ] Cri initial
> 	- [ ] Morsure de langue
> 	- [ ] Perte d'urine/selles
> - [ ] **101. Chutes ou traumatismes antérieurs *(Première crise convulsive tonico-clonique)***
> - [ ] **102. Symptômes associés - Infectieux *(Première crise convulsive tonico-clonique)***
> 	- [ ] Fièvre
> 	- [ ] Céphalées
> 	- [ ] Photophobie/phonophobie
> 	- [ ] Nausées/vomissements
> - [ ] **103. Symptômes végétatifs *(Première crise convulsive tonico-clonique)***
> - [ ] **104. Symptômes neurologiques et cardiovasculaires *(Première crise convulsive tonico-clonique)***
> 	- [ ] Déficits neurologiques/AIT/AVC
> 	- [ ] Changement de personnalité
> 	- [ ] Cardiopathie connue
> - [ ] **105. Antécédents médicaux personnels *(BAV · Première crise convulsive tonico-clonique)***
> 	- [ ] Diabète
> 	- [ ] Addiction *(Première crise convulsive tonico-clonique)*
> 	- [ ] Cancer actif *(Première crise convulsive tonico-clonique)*
> 	- [ ] Épilepsie *(Première crise convulsive tonico-clonique)*
> 	- [ ] Tumeur cérébrale *(Première crise convulsive tonico-clonique)*
> 	- [ ] Convulsions fébriles enfant *(Première crise convulsive tonico-clonique)*
> 	- [ ] Maladies cardiovasculaires *(BAV)*
> 	- [ ] Maladies respiratoires *(BAV)*
> 	- [ ] Autres pathologies chroniques *(BAV)*
> - [ ] **106. Habitudes de vie *(Première crise convulsive tonico-clonique)***
> 	- [ ] Alcool
> 	- [ ] Tabac
> 	- [ ] Drogues
> - [ ] **107. Anamnèse sociale *(Première crise convulsive tonico-clonique)***
> 	- [ ] Formation
> 	- [ ] Famille
> 	- [ ] Profession
> 	- [ ] Domicile
> 	- [ ] Loisirs
> - [ ] **108. Revue des systèmes *(Première crise convulsive tonico-clonique)***
> - [ ] **109. Question d'entrée ouverte - Motif de consultation *(1 grille sur 7)***
> - [ ] **110. Caractérisation des symptômes principaux *(1 grille sur 7)***
> 	- [ ] Déclenchement par changements de position
> 	- [ ] Amélioration en position allongée
> 	- [ ] Prédominance horaire
> 	- [ ] Durée des symptômes
> - [ ] **111. Symptômes neurovégétatifs associés *(1 grille sur 7)***
> 	- [ ] Vertiges
> 	- [ ] Tachycardie
> 	- [ ] Sueurs
> 	- [ ] Pâleur
> - [ ] **112. Épisodes syncopaux et chutes *(1 grille sur 7)***
> 	- [ ] Nombre de chutes
> 	- [ ] Perte de connaissance complète
> 	- [ ] Gravité des chutes
> 	- [ ] Traumatismes associés
> - [ ] **113. Symptômes cognitifs et généraux *(1 grille sur 7)***
> 	- [ ] Problèmes de concentration
> 	- [ ] Fatigue inhabituelle
> 	- [ ] Céphalées
> 	- [ ] Modifications récentes
> - [ ] **114. Symptômes cardiovasculaires *(1 grille sur 7)***
> 	- [ ] Douleurs thoraciques
> 	- [ ] Dyspnée
> 	- [ ] Palpitations
> 	- [ ] Œdèmes des membres inférieurs
> - [ ] **115. Symptômes évocateurs d'autres causes *(1 grille sur 7)***
> 	- [ ] Intolérance au froid
> 	- [ ] Acrocyanose
> 	- [ ] Signes d'hypothyroïdie
> 	- [ ] Signes d'insuffisance surrénalienne
> - [ ] **116. Antécédents cardiovasculaires *(1 grille sur 7)***
> 	- [ ] Maladies cardiaques connues
> 	- [ ] Hypertension artérielle
> 	- [ ] Insuffisance cardiaque
> 	- [ ] Troubles du rythme
> - [ ] **117. Antécédents médicaux autres *(1 grille sur 7)***
> 	- [ ] Maladies rénales
> 	- [ ] Diabète
> 	- [ ] Maladies neurologiques
> 	- [ ] Autres pathologies chroniques
> - [ ] **118. Traitements médicamenteux *(1 grille sur 7)***
> 	- [ ] Médicaments actuels
> 	- [ ] Antihypertenseurs
> 	- [ ] Diurétiques
> 	- [ ] Psychotropes
> 	- [ ] Observance thérapeutique
> - [ ] **119. Habitudes de vie et hydratation *(1 grille sur 7)***
> 	- [ ] Apports alimentaires
> 	- [ ] Hydratation quotidienne
> 	- [ ] Consommation de sel
> 	- [ ] Modifications récentes
> - [ ] **120. Substances et habitudes *(2 grilles sur 7)***
> 	- [ ] Tabagisme *(1 grille sur 7)*
> 	- [ ] Alcool
> 	- [ ] Café/thé *(1 grille sur 7)*
> 	- [ ] Autres substances *(1 grille sur 7)*
> 	- [ ] Tabac actuel *(BAV)*
> 	- [ ] Café *(BAV)*
> 	- [ ] Drogues illicites *(BAV)*
> - [ ] **121. Activités physiques et mode de vie *(1 grille sur 7)***
> 	- [ ] Activités sportives
> 	- [ ] Loisirs
> 	- [ ] Niveau d'autonomie
> 	- [ ] Mobilité générale
> - [ ] **122. Contexte social *(1 grille sur 7)***
> 	- [ ] Situation familiale
> 	- [ ] Enfants
> 	- [ ] Profession antérieure
> 	- [ ] Conditions de vie actuelles
> - [ ] **123. Question d'entrée ouverte - Symptôme principal *(BAV)***
> - [ ] **124. Caractérisation de l'épisode syncopal *(BAV)***
> 	- [ ] Prodromes
> 	- [ ] Durée de la perte de connaissance
> 	- [ ] Récupération (rapide ou progressive)
> 	- [ ] Confusion post-critique
> - [ ] **125. Fréquence et récurrence *(BAV)***
> 	- [ ] Nombre d'épisodes
> 	- [ ] Premier épisode (date)
> 	- [ ] Augmentation de la fréquence
> 	- [ ] Circonstances similaires
> - [ ] **126. Symptômes cardiovasculaires associés *(BAV)***
> 	- [ ] Palpitations avant/après
> 	- [ ] Douleurs thoraciques
> 	- [ ] Sensation de battements irréguliers
> 	- [ ] Pause cardiaque ressentie
> - [ ] **127. Symptômes généraux récents *(BAV)***
> 	- [ ] Fatigue inhabituelle
> 	- [ ] Faiblesse générale
> 	- [ ] Diminution de la tolérance à l'effort
> 	- [ ] Modifications récentes
> - [ ] **128. Symptômes respiratoires *(BAV)***
> 	- [ ] Dyspnée d'effort
> 	- [ ] Dyspnée de repos
> 	- [ ] Orthopnée
> 	- [ ] Dyspnée paroxystique nocturne
> - [ ] **129. Symptômes neurologiques *(BAV)***
> 	- [ ] Vertiges
> 	- [ ] Troubles visuels avant la syncope
> 	- [ ] Céphalées
> 	- [ ] Déficit neurologique focal
> - [ ] **130. Circonstances déclenchantes *(BAV)***
> 	- [ ] Position lors de la syncope
> 	- [ ] Effort physique
> 	- [ ] Émotion forte
> 	- [ ] Miction, défécation, toux
> - [ ] **131. Facteurs de risque cardiovasculaire *(BAV)***
> 	- [ ] Diabète
> 	- [ ] Hypertension
> 	- [ ] Dyslipidémie
> 	- [ ] Tabagisme
> 	- [ ] Obésité
> - [ ] **132. Allergies médicamenteuses *(BAV)***
> 	- [ ] Allergies connues
> 	- [ ] Intolérances
> 	- [ ] Réactions antérieures
> - [ ] **133. Contexte social et professionnel *(BAV)***
> 	- [ ] Profession
> 	- [ ] Niveau d'activité actuel
> 	- [ ] Stress récent
> 	- [ ] Support social
> - [ ] **134. Orientation du patient *(Hypoglycémie)***
> 	- [ ] Personne
> 	- [ ] Temporalité
> 	- [ ] Espace
> - [ ] **135. Présence de douleur *(Hypoglycémie)***
> - [ ] **136. Notion d'intoxication aiguë ("avez-vous pris ?") *(Hypoglycémie)***
> 	- [ ] Drogue
> 	- [ ] Alcool
> - [ ] **137. Hétéro-anamnèse avec infirmier/-ère - anamnèse actuelle *(Hypoglycémie)***
> 	- [ ] Circonstances du début du malaise
> 	- [ ] Notion de perte de connaissance / syncope
> 	- [ ] Notion de traumatisme crânien
> - [ ] **138. Hétéroanamnèse avec infirmier/-ère - infos sur le/la patient·e *(Hypoglycémie)***
> 	- [ ] Médicaments habituels
> 	- [ ] Antécédents / comorbidités
> - [ ] **139. Anamnèse avec patient·e (post resucrage efficace) *(Hypoglycémie)***
> 	- [ ] Circonstance du malaise
> 	- [ ] Compliance / modalité du traitement anti-diabétique
> - [ ] **140. Caractérisation de la perte de connaissance *(1 grille sur 7)***
> 	- [ ] Chronologie/durée
> 	- [ ] Développement
> 	- [ ] Circonstances de survenue
> 	- [ ] Fréquence
> - [ ] **141. État post-critique *(1 grille sur 7)***
> 	- [ ] Réveil avec famille autour de lui
> 	- [ ] Orientation conservée (sait où il est, reconnaît ses parents)
> 	- [ ] Récupération rapide et complète
> - [ ] **142. Recherche de signes d'hypotension orthostatique *(1 grille sur 7)***
> 	- [ ] Épisode en se levant (changement de position)
> 	- [ ] Vertiges et voile devant les yeux
> - [ ] **143. Antécédents médicaux et facteurs prédisposants *(1 grille sur 7)***
> 	- [ ] Anémie ferriprive en traitement (fer per os et IV)
> 	- [ ] Jamais hospitalisé ni opéré
> 	- [ ] Allergie au pollen
> 	- [ ] Vaccins à jour
> - [ ] **144. Habitudes et facteurs de risque *(1 grille sur 7)***
> 	- [ ] Médicaments actuels
> 	- [ ] Alimentation
> 	- [ ] Activité physique
> 	- [ ] Tabac/alcool/drogues

> [!tip] 🩺 Status
> - [ ] **1. Inspection après chute *(Première crise épileptique focale bilatéralisée)***
> - [ ] **2. Inspection de la langue *(Première crise épileptique focale bilatéralisée)***
> - [ ] **3. Tonus cervical *(Première crise épileptique focale bilatéralisée)***
> - [ ] **4. Examen cardio-pulmonaire *(Première crise convulsive tonico-clonique · Première crise épileptique focale bilatéralisée)***
> 	- [ ] Auscultation cardiaque *(Première crise convulsive tonico-clonique)*
> 	- [ ] Auscultation pulmonaire *(Première crise convulsive tonico-clonique)*
> - [ ] **5. Auscultation cardiaque *(Première crise épileptique focale bilatéralisée · Syncope avec suspicion d’origine arythmogène (syndrome de Brugada))***
> - [ ] **6. Auscultation des carotides *(Première crise épileptique focale bilatéralisée · Syncope avec suspicion d’origine arythmogène (syndrome de Brugada))***
> - [ ] **7. Épreuves de maintien *(Première crise épileptique focale bilatéralisée)***
> - [ ] **8. Épreuve de maintien des bras *(Première crise épileptique focale bilatéralisée)***
> - [ ] **9. Épreuve de maintien des jambes *(Première crise épileptique focale bilatéralisée)***
> - [ ] **10. Test de force comparatif *(Première crise épileptique focale bilatéralisée)***
> - [ ] **11. Membre supérieur *(Première crise épileptique focale bilatéralisée)***
> - [ ] **12. Membre inférieur *(Première crise épileptique focale bilatéralisée)***
> - [ ] **13. Réflexes ostéo-tendineux comparés *(Première crise épileptique focale bilatéralisée)***
> - [ ] **14. Signe de Babinski *(Première crise épileptique focale bilatéralisée)***
> - [ ] **15. Sensibilité *(Première crise épileptique focale bilatéralisée · Syncope avec suspicion d’origine arythmogène (syndrome de Brugada))***
> - [ ] **16. Nerfs crâniens orientation *(Première crise épileptique focale bilatéralisée · Syncope avec suspicion d’origine arythmogène (syndrome de Brugada))***
> - [ ] **17. I. Olfaction *(Première crise épileptique focale bilatéralisée)***
> - [ ] **18. II. Visus *(Première crise épileptique focale bilatéralisée)***
> - [ ] **19. II. Champ visuel *(Première crise épileptique focale bilatéralisée)***
> - [ ] **20. III. Réaction pupillaire *(Première crise épileptique focale bilatéralisée)***
> - [ ] **21. III/IV/VI. Motilité oculaire *(Première crise épileptique focale bilatéralisée)***
> - [ ] **22. V. Sensibilité faciale *(Première crise épileptique focale bilatéralisée)***
> - [ ] **23. VII. Facial *(Première crise épileptique focale bilatéralisée)***
> - [ ] **24. VIII. Audition *(Première crise épileptique focale bilatéralisée)***
> - [ ] **25. IX/X. Déglutition *(Première crise épileptique focale bilatéralisée)***
> - [ ] **26. XI. Accessoire *(Première crise épileptique focale bilatéralisée)***
> - [ ] **27. XII. Déviation linguale *(Première crise épileptique focale bilatéralisée)***
> - [ ] **28. Station et marche *(Première crise épileptique focale bilatéralisée)***
> - [ ] **29. Inspection des conséquences de la chute *(Syncope avec suspicion d’origine arythmogène (syndrome de Brugada))***
> - [ ] **30. Bouche / pharynx *(Syncope avec suspicion d’origine arythmogène (syndrome de Brugada))***
> - [ ] **31. Ganglions cervicaux *(Syncope avec suspicion d’origine arythmogène (syndrome de Brugada))***
> - [ ] **32. Inspection *(Syncope avec suspicion d’origine arythmogène (syndrome de Brugada))***
> - [ ] **33. Peau / muqueuses *(Syncope avec suspicion d’origine arythmogène (syndrome de Brugada))***
> - [ ] **34. Mains *(Syncope avec suspicion d’origine arythmogène (syndrome de Brugada))***
> - [ ] **35. Thorax / travail respiratoire / cicatrices *(Syncope avec suspicion d’origine arythmogène (syndrome de Brugada))***
> - [ ] **36. Signes de stase *(Syncope avec suspicion d’origine arythmogène (syndrome de Brugada))***
> - [ ] **37. Turgescence jugulaire *(Syncope avec suspicion d’origine arythmogène (syndrome de Brugada))***
> - [ ] **38. Œdèmes périphériques *(Syncope avec suspicion d’origine arythmogène (syndrome de Brugada))***
> - [ ] **39. Reflux hépato-jugulaire *(Syncope avec suspicion d’origine arythmogène (syndrome de Brugada))***
> - [ ] **40. Perfusion périphérique / pouls *(Syncope avec suspicion d’origine arythmogène (syndrome de Brugada))***
> - [ ] **41. Auscultation *(Syncope avec suspicion d’origine arythmogène (syndrome de Brugada))***
> - [ ] **42. Test de Schellong *(Syncope avec suspicion d’origine arythmogène (syndrome de Brugada))***
> - [ ] **43. Auscultation pulmonaire *(Syncope avec suspicion d’origine arythmogène (syndrome de Brugada))***
> - [ ] **44. Conscience / orientation *(Syncope avec suspicion d’origine arythmogène (syndrome de Brugada))***
> - [ ] **45. Meningisme *(Syncope avec suspicion d’origine arythmogène (syndrome de Brugada))***
> - [ ] **46. Motricité *(Syncope avec suspicion d’origine arythmogène (syndrome de Brugada))***
> - [ ] **47. Épreuve des bras tendus *(Syncope avec suspicion d’origine arythmogène (syndrome de Brugada))***
> - [ ] **48. Épreuve des jambes tendues *(Syncope avec suspicion d’origine arythmogène (syndrome de Brugada))***
> - [ ] **49. Coordination *(Syncope avec suspicion d’origine arythmogène (syndrome de Brugada))***
> - [ ] **50. Doigt-nez *(Syncope avec suspicion d’origine arythmogène (syndrome de Brugada))***
> - [ ] **51. Talon-genou *(Syncope avec suspicion d’origine arythmogène (syndrome de Brugada))***
> - [ ] **52. Romberg *(Syncope avec suspicion d’origine arythmogène (syndrome de Brugada))***
> - [ ] **53. Examen neurologique (incluant orientation) *(Première crise convulsive tonico-clonique)***
> 	- [ ] État de conscience
> 	- [ ] Force motrice
> 	- [ ] Tonus
> 	- [ ] Réflexes ostéo-tendineux
> - [ ] **54. Auscultation carotidienne *(Première crise convulsive tonico-clonique)***
> - [ ] **55. Hygiène des mains *(1 grille sur 7)***
> 	- [ ] Désinfection des mains avant l'examen
> - [ ] **56. Mesure de la pression artérielle orthostatique *(1 grille sur 7)***
> 	- [ ] Mesure en position couchée (après 5 min de repos)
> 	- [ ] Mesure en position debout (immédiatement)
> 	- [ ] Mesure en position debout (après 3 min)
> 	- [ ] Calcul de la différence
> - [ ] **57. Test de Schellong complet *(1 grille sur 7)***
> 	- [ ] Position couchée 10 minutes
> 	- [ ] Mesures répétées en orthostatisme
> 	- [ ] Documentation des symptômes
> 	- [ ] Interprétation correcte
> - [ ] **58. Examen cardiovasculaire *(HypoTA orthostatique)***
> 	- [ ] Auscultation cardiaque (4 foyers)
> 	- [ ] Palpation du pouls (fréquence et régularité) *(1 grille sur 7)*
> 	- [ ] Recherche de souffles *(1 grille sur 7)*
> 	- [ ] Signes d'insuffisance cardiaque *(1 grille sur 7)*
> 	- [ ] Recherche de souffle ou trouble du rythme *(1 grille sur 7)*
> 	- [ ] Palpation des pouls périphériques *(1 grille sur 7)*
> 	- [ ] Recherche de signes d'insuffisance cardiaque *(1 grille sur 7)*
> - [ ] **59. Examen pulmonaire *(2 grilles sur 7)***
> 	- [ ] Inspection thoracique *(1 grille sur 7)*
> 	- [ ] Auscultation pulmonaire bilatérale *(1 grille sur 7)*
> 	- [ ] Recherche de râles *(1 grille sur 7)*
> 	- [ ] Évaluation de la symétrie *(1 grille sur 7)*
> 	- [ ] Auscultation bilatérale *(BAV)*
> 	- [ ] Recherche de râles crépitants *(BAV)*
> 	- [ ] Signes de congestion *(BAV)*
> 	- [ ] Épanchement pleural *(BAV)*
> - [ ] **60. Inspection cutanée et vasculaire *(1 grille sur 7)***
> 	- [ ] Recherche de pâleur
> 	- [ ] Présence de varices
> 	- [ ] État d'hydratation cutanée
> 	- [ ] Temps de recoloration capillaire
> - [ ] **61. Examen neurologique de dépistage *(2 grilles sur 7)***
> 	- [ ] Orientation temporo-spatiale *(1 grille sur 7)*
> 	- [ ] Équilibre et coordination *(1 grille sur 7)*
> 	- [ ] Réflexes ostéo-tendineux
> 	- [ ] Force musculaire globale *(1 grille sur 7)*
> 	- [ ] État de conscience (score de Glasgow) *(BAV)*
> 	- [ ] Déficit focal *(BAV)*
> 	- [ ] Signes méningés *(BAV)*
> - [ ] **62. Recherche de signes d'hypovolémie *(1 grille sur 7)***
> 	- [ ] Pli cutané
> 	- [ ] Sécheresse des muqueuses
> 	- [ ] Yeux enfoncés
> 	- [ ] Pression veineuse jugulaire
> - [ ] **63. Signes vitaux et état général *(BAV)***
> 	- [ ] État de conscience actuel
> 	- [ ] Pression artérielle
> 	- [ ] Saturation en oxygène
> 	- [ ] Température
> - [ ] **64. Examen cardiaque approfondi *(BAV)***
> 	- [ ] Fréquence cardiaque
> 	- [ ] Régularité du rythme
> 	- [ ] Auscultation des bruits cardiaques
> 	- [ ] Recherche de souffles
> - [ ] **65. Palpation des pouls périphériques *(BAV)***
> 	- [ ] Pouls carotidiens (bilatéral)
> 	- [ ] Pouls radiaux (synchronisme)
> 	- [ ] Pouls fémoraux
> 	- [ ] Pouls pédieux
> - [ ] **66. Recherche de signes d'insuffisance cardiaque *(BAV)***
> 	- [ ] Turgescence jugulaire
> 	- [ ] Reflux hépato-jugulaire
> 	- [ ] Œdèmes des membres inférieurs
> 	- [ ] Hépatomégalie
> - [ ] **67. Examen vasculaire *(BAV)***
> 	- [ ] Auscultation carotidienne (souffles)
> 	- [ ] Palpation aortique
> 	- [ ] Recherche d'anévrisme
> 	- [ ] Signes d'artériopathie
> - [ ] **68. Inspection générale *(BAV)***
> 	- [ ] Coloration cutanée
> 	- [ ] Signes de traumatisme (chute)
> 	- [ ] Morsure de langue
> 	- [ ] Perte d'urines
> - [ ] **69. A - Airways - initie une prise en charge ABCDE *(Hypoglycémie)***
> 	- [ ] Dans les 3 premières minutes après le début station
> 	- [ ] Si patient·e en phase agitée - déclare à voix haute que le A est ok
> 	- [ ] Si patient·e en phase endormie - inspecte l'intérieur de la cavité buccale
> - [ ] **70. B - Breathing *(Hypoglycémie)***
> 	- [ ] Mesure ou demande la fréquence respiratoire
> 	- [ ] Demande la mesure de saturation de l'hémoglobine (SpO2)
> 	- [ ] Auscultation de min 4 plages pulmonaires
> 	- [ ] Thorax visible durant l'examen clinique (pas recouvert)
> - [ ] **71. C - Circulation *(Hypoglycémie)***
> 	- [ ] Mesure ou demande la fréquence cardiaque
> 	- [ ] Demande la mesure de la tension artérielle
> 	- [ ] Palpations des pouls périphériques aux 4 extrémités
> 	- [ ] Recherche des signes d'hémorragie
> 	- [ ] Mesure du temps de recoloration
> - [ ] **72. D - Disability (1) - Glasgow Coma Scale *(Hypoglycémie)***
> 	- [ ] Ouverture des yeux
> 	- [ ] Réponse verbale
> 	- [ ] Réponse motrice
> - [ ] **73. D - Disability (2) - Examen neurologique basique *(Hypoglycémie)***
> 	- [ ] Réflexes pupillaires
> 	- [ ] Observation des pupilles (recherche anisocorie)
> 	- [ ] Motricité globale des 4 membres
> 	- [ ] Signes méningés
> - [ ] **74. D - Disability (3) - mesure du glucose capillaire *(Hypoglycémie)***
> - [ ] **75. E - Exposure *(Hypoglycémie)***
> 	- [ ] Demande mesure T°
> 	- [ ] Examen sommaire "tête aux pieds"
> - [ ] **76. Constantes vitales et état général *(1 grille sur 7)***
> 	- [ ] Mesure de la tension artérielle
> 	- [ ] Fréquence cardiaque et pouls
> 	- [ ] État d'hydratation
> 	- [ ] Évaluation générale
> - [ ] **77. Test d'hypotension orthostatique *(1 grille sur 7)***
> 	- [ ] Mesure TA en position couchée
> 	- [ ] Mesure TA après 3 minutes debout
> 	- [ ] Recherche de symptômes au lever
> 	- [ ] Interprétation du test (chute ≥20/10 mmHg)
> - [ ] **78. Examen neurologique de base *(1 grille sur 7)***
> 	- [ ] État de conscience et orientation
> 	- [ ] Recherche de déficit neurologique focal
> 	- [ ] Reflexes pupillaires
> - [ ] **79. Recherche de signes d'anémie *(1 grille sur 7)***
> 	- [ ] Coloration des conjonctives
> 	- [ ] Coloration des muqueuses
> 	- [ ] Recherche de pâleur cutanée

> [!success] 💊 Management — partagé par plusieurs diagnostics
> - [ ] **1. Diagnostic de travail *(2 grilles sur 7)* — *Première crise épileptique focale bilatéralisée · Syncope avec suspicion d’origine arythmogène (syndrome de Brugada)***
> - [ ] **2. Hospitalisation *(2 grilles sur 7)* — *Première crise épileptique focale bilatéralisée · Syncope avec suspicion d’origine arythmogène (syndrome de Brugada)***

> [!success] 💊 Management — si BAV
> - [ ] **1. Diagnostics différentiels**
> - [ ] **2. Diagnostic principal**
> 	- [ ] Sévérité évaluée
> 	- [ ] Trouble du rythme cardiaque : bloc auriculo-ventriculaire
> 	- [ ] Type de bloc AV suspecté
> 	- [ ] Risque vital immédiat
> - [ ] **3. ECG - Réalisation et interprétation**
> 	- [ ] ECG 12 dérivations en urgence
> 	- [ ] Identification du bloc AV type Mobitz
> 	- [ ] Analyse de l'intervalle PR
> 	- [ ] Recherche d'autres anomalies
> - [ ] **4. Examens biologiques urgents**
> 	- [ ] Troponine
> 	- [ ] BNP/NT-proBNP
> 	- [ ] Ionogramme et fonction rénale
> 	- [ ] FSC
> 	- [ ] TSH si indication
> - [ ] **5. Examens complémentaires cardiologiques**
> 	- [ ] Échocardiographie (exclure infarctus, cardiomyopathie)
> 	- [ ] Monitoring ECG continu
> 	- [ ] Holter ECG 24h si sortie
> 	- [ ] Test d'effort différé
> - [ ] **6. Prise en charge immédiate**
> 	- [ ] Mise sous scope cardiaque
> 	- [ ] Voie veineuse périphérique
> 	- [ ] Oxygénothérapie si besoin
> 	- [ ] Atropine prête si bradycardie symptomatique
> - [ ] **7. Traitement définitif**
> 	- [ ] Indication de stimulateur cardiaque permanent
> 	- [ ] Type de pacemaker approprié
> 	- [ ] Délai d'implantation
> 	- [ ] Pacing temporaire si nécessaire
> - [ ] **8. Révision du traitement médicamenteux**
> 	- [ ] Arrêt des médicaments bradycardisants
> 	- [ ] Adaptation du Valsartan
> 	- [ ] Gestion des antidiabétiques
> 	- [ ] Prévention secondaire cardiovasculaire
> - [ ] **9. Éducation et prévention**
> 	- [ ] Explication de la pathologie
> 	- [ ] Signes d'alarme à reconnaître
> 	- [ ] Conduite automobile temporairement interdite
> 	- [ ] Port de la carte de porteur de pacemaker
> - [ ] **10. Organisation du suivi**
> 	- [ ] Consultation cardiologie urgente
> 	- [ ] Suivi post-implantation
> 	- [ ] Contrôles réguliers du pacemaker
> 	- [ ] Coordination avec le médecin traitant

> [!success] 💊 Management — si Hypoglycémie
> - [ ] **1. Équipement - propose de mettre un accès veineux (voie veineuse périphérique)**
> - [ ] **2. Demande prélèvement sanguin pour test de laboratoire / gazométrie**
> - [ ] **3. Stratégie de resucrage**
> 	- [ ] Propose sucre per os
> 	- [ ] Propose glucose IV
> - [ ] **4. Modalité d'injection du glucose - choisit**
> 	- [ ] Vitesse : bolus
> 	- [ ] Concentration : 40%
> - [ ] **5. Propose une injection de glucagon IM**
> - [ ] **6. Propose un suivi rapproché de la glycémie**

> [!success] 💊 Management — si HypoTA orthostatique
> - [ ] **1. Diagnostics différentiels**
> 	- [ ] Syncope cardiogène (troubles du rythme) *(1 grille sur 2)*
> 	- [ ] Syncope vasovagale *(1 grille sur 2)*
> 	- [ ] Épilepsie *(1 grille sur 2)*
> 	- [ ] AIT (accident ischémique transitoire) *(1 grille sur 2)*
> - [ ] **2. Diagnostic principal *(1 grille sur 2)***
> 	- [ ] Hypotension orthostatique
> 	- [ ] Justification clinique
> 	- [ ] Critères diagnostiques (chute TA >20/10 mmHg)
> 	- [ ] Sévérité évaluée
> - [ ] **3. Examens complémentaires - Monitoring *(1 grille sur 2)***
> 	- [ ] Mesure de la TA sur 3 jours différents
> 	- [ ] Holter tensionnel 24h
> 	- [ ] Test de Schellong standardisé
> 	- [ ] Tilt-test si nécessaire
> - [ ] **4. Examens complémentaires - Biologie *(1 grille sur 2)***
> 	- [ ] FSC (anémie)
> 	- [ ] Ionogramme (déshydratation)
> 	- [ ] Fonction rénale
> 	- [ ] TSH (hypothyroïdie)
> 	- [ ] Cortisol (insuffisance surrénalienne)
> - [ ] **5. Examens complémentaires - Cardiologie *(1 grille sur 2)***
> 	- [ ] ECG de repos
> 	- [ ] Échocardiographie
> 	- [ ] Holter ECG si suspicion de troubles du rythme
> 	- [ ] Test d'effort si indiqué
> - [ ] **6. Mesures non médicamenteuses *(1 grille sur 2)***
> 	- [ ] Hydratation adéquate (>1,5L/jour)
> 	- [ ] Augmentation des apports en sel
> 	- [ ] Lever progressif en 3 temps
> 	- [ ] Éviter la station debout prolongée
> 	- [ ] Bas de contention si varices
> 	- [ ] Surélévation de la tête du lit
> - [ ] **7. Révision médicamenteuse *(1 grille sur 2)***
> 	- [ ] Identification des médicaments hypotenseurs
> 	- [ ] Ajustement posologique
> 	- [ ] Changement d'horaire de prise
> 	- [ ] Substitution si nécessaire
> - [ ] **8. Traitement médicamenteux spécifique *(1 grille sur 2)***
> 	- [ ] Fludrocortisone (Florinef® 0,1mg/jour)
> 	- [ ] Posologie progressive (max 0,5mg/jour)
> 	- [ ] Surveillance des effets secondaires
> 	- [ ] Alternatives (midodrine si échec)
> - [ ] **9. Éducation du patient et prévention *(1 grille sur 2)***
> 	- [ ] Explication de la pathologie
> 	- [ ] Reconnaissance des symptômes d'alerte
> 	- [ ] Prévention des chutes
> 	- [ ] Adaptation de l'environnement
> - [ ] **10. Planification du suivi *(1 grille sur 2)***
> 	- [ ] Rendez-vous de contrôle programmé
> 	- [ ] Surveillance de l'efficacité thérapeutique
> 	- [ ] Ajustement selon l'évolution
> 	- [ ] Coordination avec le médecin traitant
> - [ ] **11. Évoque le diagnostic principal de syncope orthostatique *(1 grille sur 2)***
> - [ ] **12. Propose des examens complémentaires appropriés *(1 grille sur 2)***
> 	- [ ] ECG 12 dérivations
> 	- [ ] Bilan sanguin (FSC, ionogramme, glycémie)
> 	- [ ] Dosage de l'hémoglobine (contrôle anémie)
> 	- [ ] Holter ECG si suspicion cardiaque
> - [ ] **13. Propose une prise en charge adaptée *(1 grille sur 2)***
> 	- [ ] Correction de l'anémie (optimisation traitement martial)
> 	- [ ] Conseils préventifs (lever progressif, hydratation)
> 	- [ ] Éviction des facteurs favorisants
> 	- [ ] Suivi médical rapproché
> - [ ] **14. Rassurance et explication au patient *(1 grille sur 2)***
> 	- [ ] Explique le lien avec l'anémie
> 	- [ ] Rassure sur le caractère bénin probable
> 	- [ ] Explique l'importance du suivi

> [!success] 💊 Management — si Première crise convulsive tonico-clonique
> - [ ] **1. Diagnostics différentiels**
> - [ ] **2. Diagnostic principal**
> - [ ] **3. Examens complémentaires proposés**
> 	- [ ] Biologie : ionogramme, calcium, TSH, CK
> 	- [ ] Bilan hépatique : transaminases, Gamma-GT, phosphatases alcalines, albumine, Quick/aPTT
> 	- [ ] Toxicologie : dépistage drogues, alcoolémie, glycémie
> 	- [ ] Imagerie : échographie carotides, CT/IRM cérébral
> - [ ] **4. Traitement d'urgence du status epilepticus**
> 	- [ ] Lorazépam (Temesta®) 0.1 mg/kg IV
> 	- [ ] Si persistance : Propofol/Thiopental/Phénytoïne
> - [ ] **5. Traitement antiépileptique de fond**
> 	- [ ] Épilepsie focale : Lamotrigine (aussi pendant grossesse)
> 	- [ ] Épilepsie généralisée : Valproate
> 	- [ ] Alternatives : Carbamazépine/Oxcarbazépine
> 	- [ ] Autres : Prégabaline, Gabapentine, Tiagabine/Vigabatrine
> - [ ] **6. Traitements spécifiques selon étiologie**
> 	- [ ] Chirurgie si tumeur
> 	- [ ] Shunt si hydrocéphalie
> 	- [ ] Antibiothérapie/antiviraux si méningite
> - [ ] **7. Orientation et suivi**

> [!success] 💊 Management — si Première crise épileptique focale bilatéralisée
> - [ ] **1. Glycémie capillaire**
> - [ ] **2. Bilan de base**
> - [ ] **3. CT cérébral**
> - [ ] **4. Perfusion CT**
> - [ ] **5. ECG**
> - [ ] **6. Diagnostics différentiels**
> - [ ] **7. AVC cérébral / AIT**
> - [ ] **8. Syncope cardiogène**
> - [ ] **9. Processus expansif cérébral / métastase**
> - [ ] **10. Monitoring**
> - [ ] **11. Accès iv**
> - [ ] **12. Médication de réserve lorazépam**
> - [ ] **13. Demande d’EEG**
> - [ ] **14. Avis neurologique**
> - [ ] **15. IRM cérébrale**
> - [ ] **16. Information sur l’inaptitude à la conduite**
> - [ ] **17. Conseils de sécurité**

> [!success] 💊 Management — si Sténose aortique
> *Aucune grille du corpus ne documente ce diagnostic* — il est pourtant attendu de cette SSP. **Trou de révision à combler ailleurs.**

> [!success] 💊 Management — si Syncope avec suspicion d’origine arythmogène (syndrome de Brugada)
> - [ ] **1. Laboratoire**
> - [ ] **2. Troponine (hs)**
> - [ ] **3. ECG 12 dérivations**
> - [ ] **4. Antipyrèse**
> - [ ] **5. Monitoring / télémétrie**
> - [ ] **6. Avis de cardiologie**

> [!success] 💊 Management — si Syncope vaso-vagale
> *Aucune grille du corpus ne documente ce diagnostic* — il est pourtant attendu de cette SSP. **Trou de révision à combler ailleurs.**
