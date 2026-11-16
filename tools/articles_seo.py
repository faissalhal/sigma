"""Articles « Conseils » de SIGMA ICC sur les sujets de construction les plus recherchés au Maroc.

Chaque article reprend la mise en page d'un article existant (conseil-role-bureau-etudes-techniques.html) :
en-tête, menu, pied de page et styles identiques ; seuls le titre, la description, le contenu, les données
structurées (Article + FAQ) et les sources changent. Le script ajoute aussi les cartes sur conseils.html
et les adresses dans sitemap.xml. Usage : python3 tools/articles_seo.py
"""
import html, json, os, re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DOMAIN = "https://sigma-icc.ma"
TEMPLATE = "conseil-role-bureau-etudes-techniques.html"
DATE, DATE_TXT = "2026-11-16", "16 novembre 2026"

ARTICLES = [
{
 "slug": "conseil-permis-de-construire-maroc-rokhas",
 "title": "Permis de construire au Maroc : étapes, dossier Rokhas et délais",
 "crumb": "Permis de construire",
 "desc": "Obtenir un permis de construire au Maroc en 2026 : note de renseignements, plans de l'architecte, études du BET, dépôt sur Rokhas, pièces à fournir, délais et erreurs qui bloquent le dossier.",
 "lead": "De la note de renseignements à l'affichage sur le chantier : les étapes du permis de construire, les pièces du dossier Rokhas et ce qui fait perdre des semaines.",
 "img": "images/projects/project1.jpg", "min": 7,
 "body": """
<p>Au Maroc, aucune construction neuve ne peut démarrer sans autorisation de construire. Depuis la dématérialisation des procédures d'urbanisme, le dossier se dépose en ligne sur la plateforme nationale <b>Rokhas</b>, mais le travail de fond reste le même : un projet conforme au document d'urbanisme, des plans signés par un architecte et des études techniques cohérentes.</p>
<h2>Les étapes, dans l'ordre</h2>
<ol>
<li><b>Note de renseignements urbanistiques</b> : elle indique ce que le plan d'aménagement autorise sur votre terrain (hauteur, nombre de niveaux, reculs, coefficient d'occupation). C'est le point de départ de l'esquisse.</li>
<li><b>Conception par l'architecte</b> : le recours à un architecte est obligatoire pour le permis. Il établit les plans et constitue le dossier.</li>
<li><b>Études techniques du bureau d'études (BET)</b> : notes de calcul et plans de béton armé, en tenant compte du règlement parasismique et, selon le projet, de l'étude de sol.</li>
<li><b>Dépôt en ligne sur Rokhas</b> : les pièces sont transmises sous forme numérique, les frais réglés et le dossier suivi en ligne. Un accusé de réception daté est délivré.</li>
<li><b>Instruction</b> : la commune et les services concernés (agence urbaine, protection civile selon le projet…) examinent le dossier et peuvent demander des compléments.</li>
<li><b>Délivrance et affichage</b> : une fois l'autorisation obtenue, un panneau de chantier mentionnant ses références doit être affiché.</li>
<li><b>Fin de travaux</b> : le permis d'habiter (ou certificat de conformité) atteste que l'ouvrage réalisé correspond au permis.</li>
</ol>
<h2>Les pièces du dossier</h2>
<div class="tableau"><table>
<thead><tr><th>Pièce</th><th>Qui la fournit</th></tr></thead>
<tbody>
<tr><td>Certificat de propriété (titre foncier) et plan cadastral ou topographique</td><td>Propriétaire, géomètre</td></tr>
<tr><td>Plans architecturaux (situation, masse, niveaux, coupes, façades) et contrat d'architecte</td><td>Architecte</td></tr>
<tr><td>Études et plans béton armé, notes de calcul</td><td>Bureau d'études techniques</td></tr>
<tr><td>Étude de sol, selon la nature et la taille du projet</td><td>Laboratoire géotechnique</td></tr>
<tr><td>Pièces spécifiques (sécurité incendie pour un établissement recevant du public, etc.)</td><td>Architecte et BET</td></tr>
</tbody></table></div>
<p>La liste exacte dépend de la commune et du type de projet : vérifiez-la sur Rokhas avant de déposer, car un dossier incomplet n'est pas instruit.</p>
<h2>Combien de temps faut-il compter ?</h2>
<p>Les délais varient beaucoup d'une commune à l'autre et selon la complexité du projet. En pratique, comptez <b>de quelques semaines à trois ou quatre mois</b> entre le dépôt d'un dossier complet et la délivrance, sans compter le temps de conception et d'études en amont. La loi 12-90 relative à l'urbanisme prévoit qu'en l'absence de réponse dans un délai de deux mois après le dépôt, l'autorisation est réputée accordée ; dans la pratique, mieux vaut une autorisation écrite. Le permis a aussi une durée de validité : si les travaux ne démarrent pas à temps, il faut le renouveler.</p>
<h2>Les erreurs qui bloquent un dossier</h2>
<ul>
<li>Un projet qui dépasse ce que permet la note de renseignements (hauteur, recul, emprise).</li>
<li>Des plans d'architecte et des plans béton armé qui ne correspondent pas (trame de poteaux, niveaux).</li>
<li>Des pièces illisibles ou mal nommées lors du dépôt en ligne.</li>
<li>L'absence d'étude de sol quand la commune ou la taille du projet l'exige.</li>
</ul>
<p>Le bureau d'études intervient tôt pour éviter le deuxième point : une structure pensée dès l'esquisse évite les allers-retours avec la commune.</p>
""",
 "faq": [("Le permis de construire est-il obligatoire pour une villa au Maroc ?", "Oui : toute construction nouvelle doit faire l'objet d'une autorisation de construire, déposée aujourd'hui en ligne sur la plateforme Rokhas avec les plans de l'architecte et les études techniques."),
         ("Combien de temps pour obtenir un permis de construire ?", "Comptez de quelques semaines à trois ou quatre mois après le dépôt d'un dossier complet, selon la commune et la complexité du projet."),
         ("Quelles études techniques faut-il pour le permis ?", "Les études béton armé du bureau d'études (notes de calcul et plans), et selon le projet une étude de sol et des études de sécurité incendie.")],
 "sources": [("https://bati.ma/guide/permis-rokhas-etapes-maroc", "Bati.ma, Rokhas : étapes et documents"),
             ("https://citurbarea.com/guide/rokhas-autorisation-urbanisme-en-ligne", "Citurbarea, Rokhas : pièces et dépôt en ligne"),
             ("https://www.archiplan.ma/post/permis-construire-maroc-guide-complet", "Archiplan, permis de construire au Maroc")],
},
{
 "slug": "conseil-etude-de-sol-maroc-prix",
 "title": "Étude de sol au Maroc : est-elle obligatoire et combien coûte-t-elle ?",
 "crumb": "Étude de sol",
 "desc": "Étude de sol (géotechnique) au Maroc : quand elle est exigée, ce qu'elle apporte pour les fondations, missions G1 et G2, et prix indicatifs pour une villa (5 000 à 10 000 DH).",
 "lead": "Ce que révèle une étude géotechnique, quand la faire, combien elle coûte pour une villa, et pourquoi c'est l'une des dépenses les plus rentables d'un chantier.",
 "img": "images/projects/project3.jpg", "min": 6,
 "body": """
<p>Les fondations sont la seule partie d'un bâtiment qu'on ne peut plus reprendre une fois la maison construite. Les dimensionner sans connaître le sol, c'est choisir entre surdimensionner « par sécurité » et risquer des tassements et des fissures. L'étude de sol, ou étude géotechnique, permet au bureau d'études de trancher sur des données réelles.</p>
<h2>Ce que contient une étude de sol</h2>
<ul>
<li><b>La nature des couches</b> rencontrées (remblais, limons, argiles, roches) grâce à des sondages et essais in situ.</li>
<li><b>La contrainte admissible</b> du sol, c'est-à-dire la charge qu'il peut supporter : c'est la donnée clé pour dimensionner les semelles.</li>
<li><b>Le type de fondation recommandé</b> : semelles isolées ou filantes, radier, ou fondations profondes si le bon sol est trop bas.</li>
<li><b>La présence d'eau</b> (nappe) et l'agressivité éventuelle du sol pour le béton.</li>
<li><b>Les tassements prévisibles</b> et les précautions de terrassement.</li>
</ul>
<h2>G1, G2 : de quelle mission avez-vous besoin ?</h2>
<p>Les laboratoires marocains se réfèrent couramment à la classification de la norme française NF P 94-500. La mission <b>G1</b> est une étude préliminaire du site ; la mission <b>G2</b> (avant-projet, puis projet) fournit les hypothèses précises pour concevoir les fondations. Pour une villa R+1, c'est en pratique une G2 que le bureau d'études demande avant de valider les fondations.</p>
<h2>Est-elle obligatoire ?</h2>
<p>Cela dépend de la commune, de la hauteur du bâtiment et de la zone sismique : elle est systématiquement demandée pour les projets importants, et souvent exigée dans le dossier de permis. Pour une villa, même quand elle n'est pas imposée, elle est fortement recommandée. Demandez à la commune ou à votre bureau d'études la liste des pièces exigées pour votre projet.</p>
<h2>Combien coûte une étude de sol ?</h2>
<div class="tableau"><table>
<thead><tr><th>Projet</th><th>Sondages courants</th><th>Prix indicatif</th></tr></thead>
<tbody>
<tr><td>Villa en rez-de-chaussée (moins de 150 m²)</td><td>2 sondages vers 6 m</td><td>5 000 à 7 000 DH</td></tr>
<tr><td>Villa R+1 (150 à 300 m²)</td><td>2 à 3 sondages vers 8 m</td><td>6 000 à 10 000 DH</td></tr>
<tr><td>Petit immeuble, hôtel, riad avec sous-sol</td><td>Selon le programme</td><td>Sur devis, souvent au-delà de 15 000 DH</td></tr>
</tbody></table></div>
<p>Ces fourchettes, relevées auprès de laboratoires marocains, varient selon l'accès au terrain et le nombre d'essais. Rapportées au coût d'une villa, elles représentent une fraction minime du budget, alors qu'une fondation mal adaptée peut coûter des dizaines de milliers de dirhams en reprises.</p>
<h2>Le bon moment</h2>
<p>Avant les études béton armé, idéalement dès que l'implantation est connue. Le rapport du laboratoire est la première donnée d'entrée du bureau d'études pour la descente de charges et le choix des fondations.</p>
""",
 "faq": [("Combien coûte une étude de sol pour une villa au Maroc ?", "En général entre 5 000 et 10 000 DH pour une villa, selon la surface, le nombre de sondages et l'accès au terrain."),
         ("L'étude de sol est-elle obligatoire au Maroc ?", "Elle est exigée pour les projets importants et souvent dans le dossier de permis ; pour une villa, elle est fortement recommandée même quand elle n'est pas imposée."),
         ("Quelle mission géotechnique pour une maison ?", "Une mission G2 (conception) est généralement celle que demande le bureau d'études pour dimensionner les fondations d'une villa.")],
 "sources": [("https://lechantier.ma/en/blog/etude-sol-maroc-prix", "Le Chantier, étude de sol au Maroc : obligations et prix"),
             ("https://francobat.ma/laboratoire-geotechnique-obligatoire-maroc/", "Francobat, laboratoire géotechnique : obligatoire ?"),
             ("https://geo2mo.com/combien-coute-une-etude-de-sol-guide-des-prix-g1-a-g5", "Geo2mo, missions G1 à G5")],
},
{
 "slug": "conseil-prix-bureau-etudes-techniques-maroc",
 "title": "Prix d'un bureau d'études techniques au Maroc : honoraires et devis",
 "crumb": "Prix d'un bureau d'études",
 "desc": "Combien coûte un bureau d'études techniques (BET) au Maroc : honoraires en pourcentage des travaux, prix pour une villa, ce que comprend la mission et comment comparer les devis.",
 "lead": "Pourcentage des travaux ou forfait, ce qui fait varier le prix, ce qu'un devis sérieux doit contenir : tout pour budgéter les études techniques de votre projet.",
 "img": "images/villa-technique.jpg", "min": 6,
 "body": """
<p>C'est souvent la première question d'un maître d'ouvrage : combien vont coûter les études techniques ? La réponse dépend du projet, mais il existe des ordres de grandeur, et surtout des points à vérifier pour comparer des devis qui ne couvrent pas tous la même chose.</p>
<h2>Les ordres de grandeur</h2>
<div class="tableau"><table>
<thead><tr><th>Mode de calcul</th><th>Ordre de grandeur</th></tr></thead>
<tbody>
<tr><td>Études de structure (béton armé), en pourcentage du coût des travaux</td><td>environ 1 à 3 %</td></tr>
<tr><td>Ensemble des études techniques d'une villa standard (structure, électricité, plomberie, CVC)</td><td>environ 30 000 à 100 000 DH</td></tr>
<tr><td>Villa de standing ou programme plus technique</td><td>davantage, selon les lots et le suivi de chantier</td></tr>
</tbody></table></div>
<p>Ces fourchettes, relevées dans plusieurs guides du marché marocain, sont indicatives : seul un devis établi sur vos plans fait foi.</p>
<h2>Ce qui fait varier le prix</h2>
<ul>
<li><b>Les lots étudiés</b> : béton armé seul, ou aussi électricité (CFO et CFA), plomberie sanitaire, climatisation et ventilation, sécurité incendie.</li>
<li><b>La complexité de la structure</b> : sous-sol, grandes portées, porte-à-faux, piscine, terrain en pente, zone sismique plus exposée.</li>
<li><b>Le suivi de chantier</b> : nombre de visites, contrôle des ferraillages avant chaque coulage, réception.</li>
<li><b>Les livrables</b> : plans d'exécution détaillés, métrés et descriptifs pour consulter les entreprises.</li>
</ul>
<h2>Comment comparer deux devis</h2>
<ol>
<li>Vérifiez que les mêmes lots sont inclus : un devis « béton armé seul » n'est pas comparable à un devis tous corps d'état.</li>
<li>Regardez si le suivi de chantier est compris, et combien de visites.</li>
<li>Demandez si les métrés et l'estimation des travaux sont fournis : ils servent à négocier avec les entreprises.</li>
<li>Méfiez-vous des prix très bas : une structure calculée trop vite se paie en béton et en acier inutiles, ou en reprises.</li>
</ol>
<h2>Un poste qui fait faire des économies</h2>
<p>Une structure optimisée consomme moins de béton et d'acier qu'une structure surdimensionnée « à l'œil » ; un réseau électrique bien calculé évite de refaire des saignées dans des murs finis. Sur une villa, ces économies couvrent souvent une bonne partie des honoraires d'études.</p>
""",
 "faq": [("Combien coûte un bureau d'études pour une villa au Maroc ?", "Pour l'ensemble des études techniques d'une villa standard, comptez généralement entre 30 000 et 100 000 DH ; les études de structure seules représentent souvent 1 à 3 % du coût des travaux."),
         ("Le suivi de chantier est-il compris dans le prix du BET ?", "Pas toujours : vérifiez sur le devis le nombre de visites et le contrôle des ferraillages avant coulage."),
         ("Pourquoi les devis de bureaux d'études sont-ils si différents ?", "Parce qu'ils ne couvrent pas les mêmes lots, le même niveau de détail ni le même suivi de chantier : comparez ligne par ligne.")],
 "sources": [("https://bati.ma/guide/honoraires-architecte-maroc", "Bati.ma, honoraires architecte et études"),
             ("https://www.archiplan.ma/post/guide-complet-du-co%C3%BBt-de-la-construction-au-maroc-2026", "Archiplan, coût de la construction au Maroc 2026"),
             ("https://www.construire-a-marrakech.com/cout-construction-villa-marrakech/", "Construire à Marrakech, coût d'une villa")],
},
{
 "slug": "conseil-reglement-parasismique-rps-2011-maroc",
 "title": "Règlement parasismique RPS 2011 : ce qu'il change pour votre maison",
 "crumb": "Règlement parasismique",
 "desc": "Le règlement de construction parasismique marocain (RPS 2000, version 2011) expliqué : zones sismiques, règles pour une villa (chaînages, longrines, régularité), révision après le séisme d'Al Haouz.",
 "lead": "Zonage sismique, règles de conception, chaînages et ferraillage : ce que le règlement parasismique impose concrètement à une villa ou un riad au Maroc.",
 "img": "images/projects/project4.jpg", "min": 7,
 "body": """
<p>Le séisme d'Al Haouz du 8 septembre 2023 a rappelé que la région de Marrakech est exposée au risque sismique. Au Maroc, la résistance des bâtiments aux séismes est encadrée par le <b>règlement de construction parasismique</b>, le RPS 2000, dont la version révisée de 2011 sert aujourd'hui de référence aux bureaux d'études.</p>
<h2>Un zonage plus fin</h2>
<p>La version 2011 a remplacé l'ancien découpage en trois zones par une carte en cinq zones (numérotées de 0 à 4), établie à partir de l'accélération et de la vitesse maximales du sol. Plus la zone est élevée, plus les efforts sismiques à reprendre sont importants. La zone de votre terrain est l'une des premières données que le bureau d'études fixe dans sa note de calcul.</p>
<h2>À qui il s'applique</h2>
<p>Le règlement concerne les constructions neuves, y compris les maisons individuelles, avec des exigences proportionnées à l'importance du bâtiment : une habitation courante n'est pas traitée comme un hôpital ou une école, qui doivent rester utilisables après un séisme.</p>
<h2>Ce qu'il impose concrètement à une villa</h2>
<ul>
<li><b>Une forme régulière</b> autant que possible : plans compacts, masses bien réparties, pas de décrochements brutaux d'un étage à l'autre.</li>
<li><b>Des fondations solidaires</b> : les semelles sont reliées par des longrines pour éviter les déplacements différentiels.</li>
<li><b>Des chaînages</b> horizontaux et verticaux qui ceinturent les murs et relient planchers et poteaux.</li>
<li><b>Un ferraillage ductile</b> : cadres resserrés aux extrémités des poteaux et des poutres, ancrages et recouvrements suffisants, nœuds bien ferraillés.</li>
<li><b>Pas de « poteaux courts »</b> créés par des allèges ou des murs partiels, qui concentrent les efforts.</li>
</ul>
<h2>Une révision en cours</h2>
<p>Après le séisme d'Al Haouz, les pouvoirs publics ont engagé l'actualisation du règlement : un projet de décret modifiant le RPS 2000 (version 2011) a été préparé, notamment pour revoir le classement sismique de communes, en attendant une étude d'actualisation complète. Votre bureau d'études doit appliquer les textes en vigueur à la date du dépôt de votre permis.</p>
<h2>Le rôle du bureau d'études</h2>
<p>C'est le BET qui traduit le règlement en plans : il calcule les efforts sismiques, dimensionne poteaux, poutres et voiles, et dessine les détails de ferraillage. Sur le chantier, le contrôle des armatures avant chaque coulage est l'étape qui garantit que ces calculs se retrouvent réellement dans le béton.</p>
""",
 "faq": [("Le règlement parasismique s'applique-t-il à une maison individuelle ?", "Oui : les constructions neuves, y compris les villas, doivent respecter le règlement parasismique, avec des exigences adaptées à l'importance du bâtiment."),
         ("Qu'est-ce que le RPS 2011 ?", "C'est la version révisée en 2011 du règlement de construction parasismique marocain RPS 2000 : elle introduit notamment un zonage en cinq zones et sert de référence aux calculs de structure."),
         ("Le règlement parasismique va-t-il changer ?", "Oui : après le séisme d'Al Haouz, un projet de décret modifiant le RPS a été préparé, notamment pour revoir le classement de communes. Le BET applique les textes en vigueur au moment du permis.")],
 "sources": [("https://medias24.com/2024/09/03/le-reglement-parasismique-marocain-sera-actualise-dans-80-communes/", "Médias24, le règlement parasismique sera actualisé (03/09/2024)"),
             ("https://www.lavieeco.com/affaires/de-nouvelles-normes-parasismiques-pour-la-construction-des-ba%C2%A2timents-20044/", "La Vie éco, nouvelles normes parasismiques"),
             ("https://bati.ma/guide/normes-parasismiques-maroc", "Bati.ma, normes parasismiques RPS 2011")],
},
{
 "slug": "conseil-prix-construction-m2-maroc",
 "title": "Prix de construction au m² au Maroc en 2026 : gros œuvre et finitions",
 "crumb": "Prix au m² au Maroc",
 "desc": "Combien coûte la construction au m² au Maroc en 2026 : gros œuvre (1 500 à 2 500 DH/m²), finitions, prix clé en main par gamme, exemple chiffré et postes souvent oubliés.",
 "lead": "Gros œuvre, finitions, clé en main : les prix au m² constatés au Maroc en 2026, un exemple chiffré et les dépenses à ne pas oublier dans votre budget.",
 "img": "images/projects/villa2.jpg", "min": 7,
 "body": """
<p>« Combien coûte le m² ? » est la question qui revient le plus avant un projet. Le chiffre n'a de sens que si l'on sait ce qu'il inclut : la structure seule, ou la maison terminée. Voici les ordres de grandeur constatés sur le marché marocain, à affiner ensuite avec un chiffrage sur plans.</p>
<h2>Les prix au m² par poste</h2>
<div class="tableau"><table>
<thead><tr><th>Poste</th><th>Prix indicatif au m² de plancher</th></tr></thead>
<tbody>
<tr><td>Gros œuvre (fondations, structure béton armé, maçonnerie, dalles)</td><td>environ 1 500 à 2 500 DH, plus pour le haut de gamme</td></tr>
<tr><td>Second œuvre et finitions standard</td><td>environ 1 500 à 2 000 DH et plus</td></tr>
<tr><td>Construction complète, standing correct</td><td>environ 4 500 à 6 000 DH</td></tr>
<tr><td>Construction haut de gamme</td><td>8 000 DH et bien au-delà</td></tr>
</tbody></table></div>
<p>Les écarts entre sources sont importants : ils tiennent à ce que chacun inclut (menuiseries, cuisine, climatisation, aménagements extérieurs) et à la région. Ces prix s'entendent hors terrain.</p>
<h2>Exemple : une maison de 200 m² de plancher</h2>
<ul>
<li>Gros œuvre : environ 300 000 à 500 000 DH.</li>
<li>Maison terminée en standing correct : environ 900 000 à 1 200 000 DH.</li>
<li>À ajouter : honoraires de l'architecte et du bureau d'études, étude de sol, taxes et frais de permis, raccordements eau et électricité, clôture et aménagements extérieurs, piscine le cas échéant.</li>
</ul>
<h2>Ce qui fait monter (ou baisser) le prix</h2>
<ul>
<li><b>Le sol</b> : un mauvais sol impose des fondations plus profondes ou un radier.</li>
<li><b>La forme et le nombre de niveaux</b> : sous-sol, porte-à-faux et grandes portées coûtent plus cher en béton et en acier.</li>
<li><b>Les finitions</b> : c'est le poste qui varie le plus, du simple au triple.</li>
<li><b>La qualité des études</b> : une structure optimisée par le bureau d'études réduit les quantités de béton et d'acier.</li>
</ul>
<h2>Pour un budget fiable</h2>
<p>Partez d'une fourchette au m² pour vérifier la faisabilité, puis faites établir des métrés sur plans : c'est la seule base sérieuse pour consulter les entreprises et éviter les dépassements. Pour Marrakech en particulier, voir aussi notre guide du <a href="conseil-prix-construction-villa-marrakech.html">prix de construction d'une villa à Marrakech</a>.</p>
""",
 "faq": [("Quel est le prix du gros œuvre au m² au Maroc ?", "Le gros œuvre se situe le plus souvent entre 1 500 et 2 500 DH par m² de plancher, davantage pour un projet haut de gamme ou un terrain difficile."),
         ("Combien coûte une maison de 200 m² au Maroc ?", "Pour un standing correct, comptez en ordre de grandeur 900 000 à 1 200 000 DH hors terrain, auxquels s'ajoutent études, permis et raccordements."),
         ("Le prix au m² comprend-il le terrain ?", "Non : les prix de construction au m² s'entendent hors terrain.")],
 "sources": [("https://www.habitatservicesplus.com/prix-gros-oeuvre-m2-au-maroc-en-2025/", "Habitat Service Plus, prix du gros œuvre 2025"),
             ("https://www.forumconstruction.ma/blog/cout-du-gros-oeuvre-prix-m%C2%B2-estimation-travaux-entreprise-de-construction-casablanca-maroc/", "Forum Construction, coût du gros œuvre"),
             ("https://mumtaz.ma/budget-construire-maison-maroc/", "Mumtaz, budget pour construire au Maroc en 2026"),
             ("https://habitorya.com/cout-maison-maroc-2025/", "Habitorya, combien coûte une maison au Maroc")],
},
{
 "slug": "conseil-dosage-beton-fondation-dalle",
 "title": "Dosage du béton : fondations, dalle, poteaux et béton de propreté",
 "crumb": "Dosage du béton",
 "desc": "Quel dosage de béton pour les fondations, une dalle, des poteaux ou un béton de propreté : kg de ciment par m³, quantités de sable, gravier et eau, et erreurs à éviter sur chantier.",
 "lead": "Combien de ciment par m³ selon l'ouvrage, comment se compose un mètre cube de béton, et les erreurs de chantier qui font perdre sa résistance au béton.",
 "img": "images/projects/project5.jpg", "min": 5,
 "body": """
<p>Le béton est le matériau le plus utilisé sur un chantier marocain, et aussi celui qu'on fabrique le plus souvent « à l'œil ». Un béton trop pauvre en ciment ou trop arrosé perd une grande partie de sa résistance. Voici les dosages usuels, à confirmer avec la classe de béton fixée par votre bureau d'études dans ses plans.</p>
<h2>Les dosages usuels selon l'ouvrage</h2>
<div class="tableau"><table>
<thead><tr><th>Ouvrage</th><th>Ciment par m³ de béton</th></tr></thead>
<tbody>
<tr><td>Béton de propreté (sous les semelles)</td><td>150 à 200 kg</td></tr>
<tr><td>Fondations, semelles, longrines en béton armé</td><td>350 kg</td></tr>
<tr><td>Poteaux, poutres, voiles, dalles en béton armé</td><td>350 kg</td></tr>
<tr><td>Dallage, forme de pente, ouvrages non porteurs</td><td>250 à 300 kg</td></tr>
</tbody></table></div>
<h2>La composition d'un mètre cube à 350 kg</h2>
<ul>
<li><b>Ciment</b> : 350 kg, soit 7 sacs de 50 kg.</li>
<li><b>Sable</b> : environ 400 litres.</li>
<li><b>Gravier</b> (gravette) : environ 800 litres.</li>
<li><b>Eau</b> : environ 175 litres, à ajuster selon l'humidité du sable.</li>
</ul>
<p>Ce sont des proportions de chantier courantes ; sur un projet structuré, le bureau d'études indique une classe de résistance (par exemple C25/30) et une centrale à béton fournit un béton formulé et contrôlé.</p>
<h2>Les erreurs qui affaiblissent le béton</h2>
<ul>
<li><b>Ajouter de l'eau</b> pour faciliter la mise en place : c'est la première cause de béton faible et poreux.</li>
<li><b>Ne pas vibrer</b> : les vides autour des armatures favorisent la corrosion.</li>
<li><b>Couler sans contrôle des ferraillages</b> : enrobage insuffisant, cales oubliées, armatures déplacées.</li>
<li><b>Négliger la cure</b> : par forte chaleur, comme souvent à Marrakech, il faut maintenir le béton humide plusieurs jours (arrosage, bâche) pour qu'il ne sèche pas trop vite et ne fissure pas.</li>
<li><b>Décoffrer trop tôt</b> les dalles et les poutres, avant que le béton ait pris assez de résistance.</li>
</ul>
<h2>Béton de centrale ou béton de chantier ?</h2>
<p>Pour les dalles et les gros volumes, le béton prêt à l'emploi (centrale) garantit une composition régulière et une mise en œuvre rapide. Le béton de chantier reste courant pour les petits volumes, à condition de respecter les dosages et de ne pas « allonger » à l'eau.</p>
""",
 "faq": [("Quel dosage de béton pour une fondation ?", "Pour des fondations en béton armé (semelles, longrines), le dosage courant est de 350 kg de ciment par m³ ; le béton de propreté placé dessous est dosé à 150 à 200 kg."),
         ("Combien de sacs de ciment pour 1 m³ de béton ?", "Pour un béton dosé à 350 kg/m³, il faut 7 sacs de ciment de 50 kg, avec environ 400 litres de sable, 800 litres de gravier et 175 litres d'eau."),
         ("Quel dosage pour une dalle en béton armé ?", "Une dalle en béton armé est généralement dosée à 350 kg de ciment par m³, selon la classe de béton fixée par le bureau d'études.")],
 "sources": [],
},
]


def esc(s):
    return html.escape(s, quote=True)


def build():
    tpl = open(os.path.join(ROOT, TEMPLATE), encoding="utf-8").read()
    head_end = tpl.index("</head>")
    for a in ARTICLES:
        url = f"{DOMAIN}/{a['slug']}.html"
        title = a["title"] + " | SIGMA ICC"
        h = tpl
        # en-tête : titre, description, adresse, Open Graph, données structurées (Article + FAQ)
        h = re.sub(r"<title>.*?</title>", f"<title>{esc(title)}</title>", h, count=1)
        h = re.sub(r'<meta name="description" content="[^"]*">', f'<meta name="description" content="{esc(a["desc"])}">', h, count=1)
        h = re.sub(r'<link rel="canonical" href="[^"]*">', f'<link rel="canonical" href="{url}">', h, count=1)
        h = re.sub(r'<meta property="og:title" content="[^"]*">', f'<meta property="og:title" content="{esc(title)}">', h, count=1)
        h = re.sub(r'<meta property="og:description" content="[^"]*">', f'<meta property="og:description" content="{esc(a["desc"])}">', h, count=1)
        h = re.sub(r'<meta property="og:url" content="[^"]*">', f'<meta property="og:url" content="{url}">', h, count=1)
        h = re.sub(r'<meta property="og:image" content="[^"]*">', f'<meta property="og:image" content="{DOMAIN}/{a["img"]}">', h, count=1)
        ld = {"@context": "https://schema.org", "@graph": [
            {"@type": "Article", "headline": a["title"], "description": a["desc"], "datePublished": DATE, "dateModified": DATE, "inLanguage": "fr",
             "author": {"@type": "Organization", "name": "SIGMA ICC"},
             "publisher": {"@type": "Organization", "name": "SIGMA ICC", "logo": {"@type": "ImageObject", "url": f"{DOMAIN}/images/logo-sigma.svg"}},
             "image": f"{DOMAIN}/{a['img']}", "mainEntityOfPage": url},
            {"@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": r}} for q, r in a["faq"]]}]}
        h = re.sub(r'<script type="application/ld\+json">.*?</script>', lambda m: '<script type="application/ld+json">' + json.dumps(ld, ensure_ascii=False) + "</script>", h, count=1, flags=re.S)
        # fil d'Ariane, titre, chapeau
        h = re.sub(r'(<div class="fil"><a href="index.html">Accueil</a> / <a href="conseils.html">Conseils</a> / )[^<]*(</div>)', lambda m: m.group(1) + esc(a["crumb"]) + m.group(2), h, count=1)
        h = re.sub(r"<h1>.*?</h1><p>.*?</p>", lambda m: f"<h1>{esc(a['title'])}</h1><p>{esc(a['lead'])}</p>", h, count=1, flags=re.S)
        # contenu de l'article
        faq = '<h2>Questions fréquentes</h2><div class="faq">' + "".join(f'<details><summary>{esc(q)}</summary><p>{esc(r)}</p></details>' for q, r in a["faq"]) + "</div>"
        src = ("<p class=\"sources\"><b>Sources :</b> " + " · ".join(f'<a href="{u}" target="_blank" rel="noopener">{esc(t)}</a>' for u, t in a["sources"]) + ".</p>") if a["sources"] else ""
        cta = ('<div class="encadre"><h3>Un projet en préparation ?</h3><p>SIGMA ICC réalise les études béton armé, électricité, plomberie et CVC, ainsi que le suivi de chantier, pour les villas, riads, hôtels et commerces.</p>\n'
               '    <div class="actions"><a class="btn" href="contact.html#formulaire">Demander une étude</a><a class="btn secondaire" href="chiffrage.html">Estimer mes travaux</a></div></div>')
        content = (f'<article class="contenu article">\n  <p class="meta">Publié le {DATE_TXT} · {a["min"]} min de lecture · SIGMA ICC, bureau d\'études techniques</p>'
                   + a["body"] + faq + "\n  " + cta + "\n  " + src + "\n</article>")
        h = re.sub(r'<article class="contenu article">.*?</article>', lambda m: content, h, count=1, flags=re.S)
        open(os.path.join(ROOT, a["slug"] + ".html"), "w", encoding="utf-8").write(h)
    # page Conseils : nouvelles cartes en tête de liste
    cp = os.path.join(ROOT, "conseils.html"); c = open(cp, encoding="utf-8").read()
    cards = "".join(
        f'<a class="service" href="{a["slug"]}.html"><img src="{a["img"]}" alt="" loading="lazy" width="750" height="600">\n'
        f'  <div><span class="code">{DATE_TXT} · {a["min"]} min</span><h3>{esc(a["title"])}</h3><p>{esc(a["lead"])}</p><span class="lire">Lire l\'article →</span></div></a>'
        for a in ARTICLES if a["slug"] + ".html" not in c)
    c = c.replace('<div class="grille-services">', '<div class="grille-services">' + cards, 1)
    open(cp, "w", encoding="utf-8").write(c)
    # plan du site
    sp = os.path.join(ROOT, "sitemap.xml"); s = open(sp, encoding="utf-8").read()
    add = "".join(f"  <url><loc>{DOMAIN}/{a['slug']}.html</loc><lastmod>{DATE}</lastmod><priority>0.7</priority></url>\n" for a in ARTICLES if a["slug"] not in s)
    s = s.replace(f"  <url><loc>{DOMAIN}/conseils.html</loc>", add + f"  <url><loc>{DOMAIN}/conseils.html</loc>", 1)
    s = re.sub(r"(<url><loc>https://sigma-icc.ma/conseils.html</loc><lastmod>)[^<]*", r"\g<1>" + DATE, s)
    open(sp, "w", encoding="utf-8").write(s)
    print(len(ARTICLES), "articles")


if __name__ == "__main__":
    build()
