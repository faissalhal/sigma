# Cahier des charges des articles « Conseils » de SIGMA ICC

SIGMA ICC est un bureau d'études techniques (BET) à Marrakech : études structure béton armé, électricité CFO/CFA,
plomberie, CVC, thermique RTCM, sécurité incendie (CSSI), VRD, BIM, suivi de chantier. Les articles servent à
apparaître sur Google pour les questions que se posent les particuliers, promoteurs et professionnels AU MAROC,
et à donner envie de contacter SIGMA ICC. Public : propriétaires de villa ou riad, acheteurs, promoteurs, artisans.

## Format (Python)
Chaque fichier `tools/articles/<lot>.py` contient une liste `ARTICLES` de dictionnaires :

```python
ARTICLES = [
{
 "slug": "conseil-combien-prises-par-circuit",        # imposé par la liste de sujets, commence par "conseil-"
 "cat": "electricite",                                 # imposé (voir lots plus bas)
 "title": "Combien de prises sur un même circuit ? Les règles de la NF C 15-100",   # 50-70 caractères, la requête Google en tête
 "crumb": "Prises par circuit",                        # 2 à 4 mots
 "desc": "…",                                          # meta description 140-160 caractères, concrète, avec les chiffres clés
 "lead": "…",                                          # chapeau 1 à 2 phrases
 "img": "images/services/cfo1.jpg",                    # une image de la liste du lot
 "min": 5,                                             # minutes de lecture (≈ mots / 200)
 "body": """
<p>…</p>
<h2>…</h2>
<div class="tableau"><table><thead><tr><th>…</th></tr></thead><tbody><tr><td>…</td></tr></tbody></table></div>
<ul><li><b>…</b> : …</li></ul>
""",
 "faq": [("Question ?", "Réponse en 1 à 3 phrases, autonome, avec le chiffre clé."), ...],   # exactement 3
 "sources": [("https://…", "Éditeur, titre court"), ...],   # 0 à 4, UNIQUEMENT des URL réellement trouvées
},
]
```

## Rédaction
- Français clair et direct, vouvoiement OU tutoiement : utiliser le **vous**. Pas de jargon non expliqué.
- 450 à 700 mots de corps. 3 à 5 intertitres `<h2>`. Au moins un tableau OU une liste chiffrée quand le sujet s'y prête.
- Commencer par la réponse : le premier paragraphe répond à la question du titre.
- Contexte marocain : climat de Marrakech (étés > 40 °C), distributeurs (ONEE, Radeema à Marrakech, Lydec,
  Redal, Amendis selon la ville), règlement parasismique RPS 2000 version 2011, règlement thermique RTCM
  (décret 2-13-874), sécurité incendie (décret 2-14-499), permis via Rokhas, loi 12-90.
- Électricité : au Maroc, la série de normes marocaines NM 06.1.100 à 06.1.106 (IMANOR) encadre les installations
  basse tension ; la NM 06.1.100 a été homologuée en mai 2025 et des projets de normes complémentaires ont été
  soumis à enquête publique. Dans la pratique des bureaux d'études et des CPS, la NF C 15-100 (France, issue de la
  CEI 60364) reste la référence technique la plus citée ; son édition 2024 a remplacé le document de 2002.
  Sources : https://leseco.ma/business/installations-electriques-huit-nouvelles-normes-soumises-a-lenquete-publique.html
  et https://www.imanor.gov.ma/normes/page/62/
- Terminer le corps par un paragraphe ou une `<h2>` qui montre le rôle du bureau d'études (sans publicité lourde :
  l'encadré « Un projet en préparation ? » est ajouté automatiquement après l'article).
- Pas d'emoji. Pas de « En conclusion ». Pas de remplissage.

## Exactitude (règle absolue)
- Ne JAMAIS inventer un chiffre réglementaire, un numéro de décret, d'article de loi ou une URL.
- Vérifier par WebSearch (plusieurs sources si possible) chaque valeur normative ou prix. Si les sources divergent,
  donner une fourchette et dire que c'est indicatif ; si un point n'est pas sûr, le formuler prudemment
  (« selon l'édition de la norme appliquée », « à confirmer par le bureau de contrôle ») ou ne pas le dire.
- Prix en DH, présentés comme indicatifs, avec la source.
- Repères NF C 15-100 (règles connues de l'édition 2002 amendée, encore largement appliquées) — à présenter comme
  tels et à recouper : circuit prises 16 A en 1,5 mm² protégé 16 A : 8 socles max ; en 2,5 mm² protégé 20 A :
  12 socles max ; éclairage : 8 points lumineux max par circuit en 1,5 mm² ; circuits spécialisés en 2,5 mm² / 20 A
  pour four, lave-linge, lave-vaisselle, sèche-linge, chauffe-eau ; plaque de cuisson monophasée 6 mm² / 32 A ;
  dispositifs différentiels 30 mA en tête de tous les circuits ; liaison équipotentielle principale (LEP) ;
  salle d'eau : volumes 0, 1, 2. Signaler que l'édition 2024 a fait évoluer certaines règles quand c'est pertinent.
- Les URL de `sources` doivent provenir de résultats WebSearch réels de cette session. Sinon : `"sources": []`.

## Liens internes
Vous pouvez lier d'autres articles avec `<a href="SLUG.html">…</a>` UNIQUEMENT si le slug figure dans la liste
complète des sujets (fichier `tools/articles/SUJETS.md`) ou parmi les articles existants :
conseil-permis-de-construire-maroc-rokhas, conseil-etude-de-sol-maroc-prix, conseil-prix-bureau-etudes-techniques-maroc,
conseil-reglement-parasismique-rps-2011-maroc, conseil-prix-construction-m2-maroc, conseil-dosage-beton-fondation-dalle,
conseil-prix-piscine-maroc, conseil-fissures-maison-causes-gravite, conseil-surelevation-ajouter-etage-maroc,
conseil-etancheite-toiture-terrasse-maroc, conseil-climatisation-puissance-btu-m2, conseil-isolation-thermique-rtcm-maroc,
conseil-prix-construction-villa-marrakech, conseil-role-bureau-etudes-techniques, conseil-norme-electrique-nf-c-15-100-maroc.
Maximum 3 liens internes par article.

## HTML autorisé dans body
<p>, <h2>, <ul>, <ol>, <li>, <b>, <a href="…">, et les tableaux sous la forme
<div class="tableau"><table><thead>…</thead><tbody>…</tbody></table></div>. Les apostrophes typographiques ou droites
sont libres ; ne pas mettre de guillemets triples """ dans le texte.

## Images par lot (choisir dans la liste, varier)
- structure : images/services/maison-beton.jpg, images/services/beton-poutre.jpg, images/services/1.jpg, images/services/3.jpg, images/projects/project1.jpg … project6.jpg, images/projects/villa1.jpg, images/projects/villa2.jpg
- electricite : images/services/elec-tableau.jpg, images/services/elec-disjoncteurs.jpg, images/services/elec-prises.jpg, images/services/ele1.jpg, images/services/ele2.jpg, images/projects/magasin2.jpg, images/villa-technique.jpg
- plomberie : images/services/plombier.jpg, images/services/cvc1.jpg, images/projects/pompage1.jpeg, pompage2.jpeg, pompage3.jpeg, images/projects/riad1.jpg … riad4.jpg
- cvc : images/services/clim-exterieur.jpg, images/services/ventilation.jpg, images/services/cvc1.jpg, images/projects/riad2.jpg, images/projects/magasin3.jpg
- vrd : images/services/vrd3.jpg, vrd4.jpg, vrd5.jpg, images/service_img1.jpg
- incendie : images/services/incendie-alarme.jpg, images/services/cssi1.jpg, images/services/cssi2.jpg, images/services/ventilation.jpg
- thermique : images/services/ener.jpg, images/villa-finie.jpg, images/projects/villa1.jpg, images/projects/villa2.jpg
- achat / reglementation : images/projects/*.jpg, images/projects/riad1.jpg … riad4.jpg, images/villa-finie.jpg, images/villa-technique.jpg, images/services/BIM1.jpg (BIM)

## Validation avant de rendre la main
`cd /home/user/sigma && python3 -c "import importlib.util,sys;s=importlib.util.spec_from_file_location('m','tools/articles/<lot>.py');m=importlib.util.module_from_spec(s);s.loader.exec_module(m);print(len(m.ARTICLES))"`
doit afficher le nombre d'articles sans erreur. Vérifier : 3 FAQ par article, slugs uniques et conformes à la liste,
images existantes. NE PAS lancer de git commit/push, NE PAS modifier d'autres fichiers que le vôtre.
