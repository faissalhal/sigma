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
{
 "slug": "conseil-prix-piscine-maroc",
 "title": "Prix d'une piscine en béton au Maroc en 2026",
 "crumb": "Prix d'une piscine",
 "desc": "Combien coûte une piscine en béton au Maroc en 2026 : prix au m² de bassin, exemples 6×4 et 8×4 m, postes souvent oubliés (filtration, local technique, plages) et étude structure du bassin.",
 "lead": "Prix au m² de bassin, exemples chiffrés, ce que les devis n'incluent pas toujours et pourquoi un bassin en béton armé se calcule comme une structure.",
 "img": "images/projects/villa1.jpg", "min": 6,
 "body": """
<p>La piscine est devenue un standard des villas autour de Marrakech. Son prix varie pourtant du simple au triple selon la taille, le revêtement et surtout ce que comprend le devis. Voici les ordres de grandeur du marché et les points à vérifier avant de signer.</p>
<h2>Les prix constatés</h2>
<div class="tableau"><table>
<thead><tr><th>Projet</th><th>Prix indicatif</th></tr></thead>
<tbody>
<tr><td>Bassin en béton, finition standard, au m² de plan d'eau</td><td>environ 4 000 à 9 500 DH</td></tr>
<tr><td>Finition haut de gamme (carrelage, pierre, débordement), au m²</td><td>10 000 à 15 000 DH et plus</td></tr>
<tr><td>Piscine 6 × 4 m (24 m²)</td><td>à partir d'environ 85 000 à 135 000 DH</td></tr>
<tr><td>Piscine 8 × 4 m (32 m²) avec carrelage</td><td>environ 120 000 à 220 000 DH</td></tr>
</tbody></table></div>
<p>Ces fourchettes, relevées auprès de pisciniers marocains, sont très larges : c'est le contenu du devis qui explique l'écart.</p>
<h2>Les postes souvent oubliés</h2>
<ul>
<li><b>La filtration</b> : pompe, filtre, skimmers, refoulements, et le local technique qui les abrite.</li>
<li><b>Le revêtement</b> : enduit, liner, mosaïque ou carrelage, qui fait varier fortement le prix au m².</li>
<li><b>Les plages et margelles</b> autour du bassin.</li>
<li><b>Le terrassement et l'évacuation des terres</b>, plus coûteux sur un terrain rocheux.</li>
<li><b>Les options</b> : chauffage, éclairage, électrolyse au sel, couverture de sécurité.</li>
</ul>
<h2>Un bassin est une structure</h2>
<p>Une piscine enterrée subit la poussée des terres quand elle est vide et la poussée de l'eau quand elle est pleine. Ses parois et son radier en béton armé doivent donc être calculés et ferraillés comme n'importe quel ouvrage : épaisseurs, armatures, joints et étanchéité. Un bassin mal calculé fissure, fuit, et se répare difficilement.</p>
<p>Le bureau d'études dimensionne le radier et les voiles, vérifie le sol (une piscine posée sur un remblai mal compacté peut tasser) et coordonne les réservations pour les canalisations et l'éclairage.</p>
<h2>Les étapes d'un projet de piscine</h2>
<ol>
<li>Implantation et vérification du sol.</li>
<li>Plans et calcul de la structure du bassin.</li>
<li>Terrassement, béton de propreté, radier puis voiles.</li>
<li>Pose des réseaux hydrauliques et test d'étanchéité.</li>
<li>Revêtement, plages, mise en eau et réglages de la filtration.</li>
</ol>
""",
 "faq": [("Combien coûte une piscine 8 × 4 au Maroc ?", "Une piscine en béton de 8 × 4 m avec carrelage coûte en ordre de grandeur 120 000 à 220 000 DH, selon les finitions et ce qu'inclut le devis."),
         ("Quel est le prix au m² d'une piscine en béton ?", "Comptez environ 4 000 à 9 500 DH par m² de bassin en finition standard, et 10 000 à 15 000 DH et plus en haut de gamme."),
         ("Faut-il un bureau d'études pour une piscine ?", "C'est recommandé : le radier et les parois en béton armé doivent être calculés pour résister à la poussée des terres et de l'eau, et adaptés au sol.")],
 "sources": [("https://piscinenordmaroc.com/prix-construction-piscine-maroc-devis/", "Piscine Nord Maroc, prix construction piscine 2025"),
             ("https://lepisciniste.ma/shop/piscine-enterree-en-beton/travaux-de-construction-piscine-24-m2/", "Le Pisciniste, piscine béton 6×4"),
             ("https://www.full-piscine.com/prix-construction-piscine-maroc/", "Full Piscine, prix construction piscine au Maroc")],
},
{
 "slug": "conseil-fissures-maison-causes-gravite",
 "title": "Fissures dans une maison : causes, gravité et quand s'inquiéter",
 "crumb": "Fissures dans une maison",
 "desc": "Fissure fine, en escalier, à 45° ou traversante : comment reconnaître une fissure grave dans une maison au Maroc, ses causes (tassement, retrait, structure) et que faire avant de reboucher.",
 "lead": "Comment lire une fissure (largeur, tracé, évolution), distinguer le superficiel du structurel, et les bons réflexes avant de reboucher.",
 "img": "images/projects/riad2.jpg", "min": 6,
 "body": """
<p>Presque toutes les maisons finissent par présenter des fissures. La plupart sont sans gravité ; quelques-unes signalent un problème de fondations ou de structure qu'il faut traiter vite. La largeur compte, mais le tracé, l'élément touché et surtout l'évolution dans le temps comptent tout autant.</p>
<h2>Les repères de largeur</h2>
<div class="tableau"><table>
<thead><tr><th>Largeur</th><th>Ce que c'est en général</th></tr></thead>
<tbody>
<tr><td>Moins de 0,2 mm (« faïençage », microfissure)</td><td>Le plus souvent superficielle : retrait de l'enduit ou de la peinture</td></tr>
<tr><td>De 0,2 à 2 mm</td><td>À surveiller : retrait, dilatation, léger tassement</td></tr>
<tr><td>Plus de 2 mm (lézarde)</td><td>À faire examiner, surtout si elle traverse le mur ou s'élargit</td></tr>
</tbody></table></div>
<p>Ces seuils sont des repères, pas une règle : une fissure fine peut être active, une plus large peut être ancienne et stabilisée.</p>
<h2>Ce que révèle le tracé</h2>
<ul>
<li><b>En escalier</b>, le long des joints de briques ou de parpaings : signe typique d'un tassement différentiel des fondations.</li>
<li><b>À 45° partant d'un angle de porte ou de fenêtre</b> : mouvement du mur ou linteau insuffisant.</li>
<li><b>Horizontale sous une dalle ou en haut de mur</b> : dilatation de la toiture-terrasse, fréquente sous le soleil marocain.</li>
<li><b>Sur un poteau ou une poutre</b>, avec des traces de rouille : armatures qui corrodent, à traiter rapidement.</li>
<li><b>Traversante</b>, visible des deux côtés du mur : toujours à faire diagnostiquer.</li>
</ul>
<h2>Les causes les plus fréquentes au Maroc</h2>
<ul>
<li>Des fondations posées sans étude de sol, sur un remblai ou un sol hétérogène.</li>
<li>Des fuites d'eau (canalisations, terrasse) qui détrempent le sol sous les fondations.</li>
<li>L'absence de chaînages ou de longrines, que le règlement parasismique impose pourtant.</li>
<li>Un béton trop arrosé, mal vibré, ou une cure négligée par forte chaleur.</li>
<li>Les écarts de température sur les terrasses non isolées.</li>
</ul>
<h2>Les bons réflexes</h2>
<ol>
<li><b>Ne pas reboucher tout de suite</b> : un enduit masque le problème sans le régler.</li>
<li><b>Photographier et dater</b>, mesurer la largeur, et poser un témoin (repère) pour voir si la fissure évolue.</li>
<li><b>Chercher une fuite</b> si la fissure apparaît près d'une salle d'eau ou d'une terrasse.</li>
<li><b>Faire appel à un bureau d'études</b> si la fissure dépasse 2 mm, traverse le mur, touche un élément porteur ou s'élargit : il en recherche la cause et définit la réparation (reprise en sous-œuvre, agrafage, renforcement).</li>
</ol>
""",
 "faq": [("Quand faut-il s'inquiéter d'une fissure dans une maison ?", "Quand elle dépasse environ 2 mm, traverse le mur, touche un poteau ou une poutre, suit les joints en escalier ou s'élargit avec le temps."),
         ("Une fissure en escalier est-elle grave ?", "Elle est souvent le signe d'un tassement différentiel des fondations : il faut la faire examiner et en rechercher la cause."),
         ("Faut-il reboucher une fissure tout de suite ?", "Non : il faut d'abord comprendre sa cause et vérifier qu'elle est stabilisée, sinon elle réapparaîtra.")],
 "sources": [("https://reaconsult.ma/tendances-et-conseils-en-immobilier/fissures-batiment-maroc-diagnostic-gravite-expertise", "Reaconsult, fissures et diagnostic au Maroc"),
             ("https://www.habitatpresto.com/mag/maconnerie/fissure-horizontale-maison", "Habitatpresto, fissures horizontales"),
             ("https://www.construires.fr/expertise-batiment/expertise-fissures/", "Construires, savoir si une fissure est grave")],
},
{
 "slug": "conseil-surelevation-ajouter-etage-maroc",
 "title": "Ajouter un étage à sa maison au Maroc : faisabilité et démarches",
 "crumb": "Ajouter un étage",
 "desc": "Surélévation au Maroc : vérifier que le plan d'aménagement l'autorise, faire étudier la structure existante (fondations, poteaux), obtenir le permis et les solutions de renforcement.",
 "lead": "Avant d'ajouter un étage : ce qu'autorise l'urbanisme, ce que la structure existante peut porter, le permis, et les renforcements possibles.",
 "img": "images/projects/project6.jpg", "min": 6,
 "body": """
<p>Ajouter un étage est souvent moins cher qu'acheter un nouveau terrain. Mais une maison n'a pas été calculée pour porter un niveau de plus : avant tout projet, il faut vérifier deux choses, ce que l'urbanisme autorise et ce que la structure peut supporter.</p>
<h2>1. Ce que l'urbanisme autorise</h2>
<p>Le plan d'aménagement fixe, pour chaque zone, la hauteur et le nombre de niveaux autorisés. Une note de renseignements urbanistiques indique ce qui est permis sur votre parcelle. En copropriété, l'accord des copropriétaires est aussi nécessaire. Une surélévation demande, comme une construction neuve, une <b>autorisation de construire</b> déposée avec des plans d'architecte et des études techniques.</p>
<h2>2. Ce que la structure peut porter</h2>
<p>C'est la question décisive, et elle ne se règle pas « à l'œil » : des armatures en attente qui dépassent du toit ne prouvent pas qu'un étage est possible. Le bureau d'études vérifie :</p>
<ul>
<li><b>Les fondations</b> : leurs dimensions et la capacité du sol, parfois avec une étude de sol et des sondages au pied des semelles.</li>
<li><b>Les poteaux et les poutres</b> : sections, ferraillage, état du béton (une carotte ou un relevé d'armatures peut être nécessaire).</li>
<li><b>La dalle de toiture</b>, qui deviendra un plancher et devra porter de nouvelles charges.</li>
<li><b>Le comportement parasismique</b> de l'ensemble, car un niveau de plus augmente les efforts en cas de séisme.</li>
</ul>
<h2>3. Les solutions si la structure ne suffit pas</h2>
<ul>
<li>Renforcer les poteaux (chemisage en béton armé ou en matériaux composites).</li>
<li>Reprendre ou élargir les fondations (reprise en sous-œuvre).</li>
<li>Alléger le nouvel étage : structure métallique ou bois, cloisons légères.</li>
</ul>
<p>Le diagnostic du bureau d'études chiffre ces options et permet de décider si la surélévation reste intéressante.</p>
<h2>Les étapes</h2>
<ol>
<li>Note de renseignements et esquisse de l'architecte.</li>
<li>Diagnostic de la structure existante par le bureau d'études.</li>
<li>Études de renforcement et du nouvel étage, puis dépôt du permis.</li>
<li>Travaux de renforcement, puis construction de l'étage, avec contrôle des ferraillages.</li>
</ol>
""",
 "faq": [("Faut-il un permis pour ajouter un étage au Maroc ?", "Oui : une surélévation nécessite une autorisation de construire, avec des plans d'architecte et des études techniques, et elle doit respecter le plan d'aménagement."),
         ("Ma maison peut-elle supporter un étage de plus ?", "Seul un diagnostic de la structure par un bureau d'études permet de le dire : fondations, poteaux, poutres et dalle doivent être vérifiés."),
         ("Que faire si la structure ne suffit pas ?", "On peut renforcer les poteaux et les fondations, ou alléger le nouvel étage (structure métallique, cloisons légères), selon le diagnostic.")],
 "sources": [("https://bati.ma/guide/surelevation-maison-maroc", "Bati.ma, surélévation de maison au Maroc"),
             ("https://guatbimmo.ma/surelever-son-appartement-au-maroc-autorisations-et-budget-a/", "Guatbi Immo, surélever au Maroc"),
             ("https://francobat.ma/permis-de-construire-au-maroc/", "Francobat, permis de construire au Maroc")],
},
{
 "slug": "conseil-etancheite-toiture-terrasse-maroc",
 "title": "Étanchéité d'une toiture-terrasse au Maroc : solutions et prix au m²",
 "crumb": "Étanchéité de terrasse",
 "desc": "Étanchéité de toiture-terrasse au Maroc : bitume monocouche ou bicouche, étanchéité liquide, PVC, prix au m² (de 45 à 350 DH), forme de pente, relevés et erreurs à l'origine des infiltrations.",
 "lead": "Bitume, liquide ou membrane PVC : comparer les solutions d'étanchéité, leurs prix au m², et les détails qui évitent les infiltrations.",
 "img": "images/projects/riad3.jpg", "min": 6,
 "body": """
<p>Au Maroc, la plupart des maisons sont couvertes d'une toiture-terrasse. Quand l'étanchéité est mal faite, l'eau finit par passer : taches au plafond, peinture qui cloque, et à terme des armatures qui rouillent dans la dalle. Le choix du système compte, mais les détails d'exécution comptent encore plus.</p>
<h2>Les solutions et leurs prix</h2>
<div class="tableau"><table>
<thead><tr><th>Système</th><th>Prix indicatif fourni-posé</th></tr></thead>
<tbody>
<tr><td>Bitume monocouche ou feutre soudé (une couche)</td><td>environ 45 à 90 DH/m²</td></tr>
<tr><td>Membrane bitumineuse bicouche (SBS)</td><td>environ 100 à 160 DH/m²</td></tr>
<tr><td>Bicouche avec protection (dallage, gravillons)</td><td>environ 120 à 250 DH/m²</td></tr>
<tr><td>Étanchéité liquide (résine)</td><td>environ 120 à 250 DH/m²</td></tr>
<tr><td>Membrane PVC, TPO ou EPDM</td><td>environ 160 à 350 DH/m²</td></tr>
</tbody></table></div>
<p>Ces fourchettes ne comprennent pas toujours la dépose de l'ancienne étanchéité ni la reprise de la forme de pente : vérifiez-le sur le devis.</p>
<h2>Les détails qui font la différence</h2>
<ul>
<li><b>La forme de pente</b> : l'eau doit s'écouler vers les évacuations, sans flaques stagnantes.</li>
<li><b>Les relevés</b> sur les acrotères, d'une hauteur suffisante et bien protégés en tête.</li>
<li><b>Les points singuliers</b> : évacuations, sorties de gaines, pieds de garde-corps, joints de dilatation.</li>
<li><b>Une protection</b> contre le soleil et le passage : sur une terrasse accessible, une membrane nue s'abîme vite.</li>
<li><b>L'isolation thermique</b> : la poser avec l'étanchéité améliore le confort d'été et limite les fissures dues aux écarts de température.</li>
</ul>
<h2>Accessible ou non ?</h2>
<p>Une terrasse accessible (on y marche, on y installe du mobilier) demande une étanchéité protégée par un revêtement. Une terrasse non accessible peut recevoir une membrane autoprotégée. Ce choix se fait dès la conception, car il change les charges que la dalle doit porter.</p>
<h2>Le rôle du bureau d'études</h2>
<p>Le BET intègre la terrasse dans le calcul de la dalle (poids des formes de pente, de l'isolant et de la protection), prévoit les joints de dilatation et les évacuations, et décrit le système d'étanchéité dans le dossier de consultation des entreprises.</p>
""",
 "faq": [("Quel est le prix de l'étanchéité d'une terrasse au m² au Maroc ?", "De 45 à 90 DH/m² pour un bitume monocouche, 100 à 160 DH/m² pour une bicouche SBS, et jusqu'à 250 à 350 DH/m² pour une étanchéité protégée ou une membrane PVC/EPDM."),
         ("Quelle est la meilleure étanchéité pour une terrasse ?", "Pour une terrasse accessible, une membrane bicouche protégée par un revêtement est une solution éprouvée ; le bon choix dépend de l'usage et du support."),
         ("Pourquoi ma terrasse fuit-elle malgré l'étanchéité ?", "Le plus souvent à cause d'un détail : relevé trop bas, évacuation mal raccordée, pente insuffisante ou membrane abîmée par le soleil.")],
 "sources": [("https://lechantier.ma/en/blog/etancheite-terrasse-maroc", "Le Chantier, étanchéité de terrasse au Maroc"),
             ("https://enginloc.ma/blog/materiaux-etancheite-maroc-sika", "Enginloc, matériaux d'étanchéité au Maroc"),
             ("https://tachrone.ma/blog/entreprise-etancheite-maroc-prix-m2-choisir/", "Tachrone, entreprise d'étanchéité : prix au m²")],
},
{
 "slug": "conseil-climatisation-puissance-btu-m2",
 "title": "Climatisation : quelle puissance (BTU) selon la surface de la pièce ?",
 "crumb": "Puissance de climatisation",
 "desc": "Quelle puissance de climatiseur choisir : tableau BTU par m² (9 000, 12 000, 18 000, 24 000 BTU), facteurs qui changent le calcul à Marrakech, et quand faire un bilan thermique par un bureau d'études.",
 "lead": "Le tableau des puissances selon la surface, les facteurs qui changent tout sous le climat de Marrakech, et quand un vrai calcul devient indispensable.",
 "img": "images/services/cvc1.jpg", "min": 5,
 "body": """
<p>Un climatiseur trop faible tourne en permanence sans jamais rafraîchir ; un appareil trop puissant fait des cycles courts, déshumidifie mal et coûte plus cher. Pour une pièce courante, une règle simple donne un bon point de départ ; pour une villa entière, un bilan thermique s'impose.</p>
<h2>Le tableau de départ</h2>
<div class="tableau"><table>
<thead><tr><th>Puissance du climatiseur</th><th>Puissance froid approximative</th><th>Surface indicative</th></tr></thead>
<tbody>
<tr><td>9 000 BTU</td><td>environ 2,6 kW</td><td>jusqu'à 20 à 25 m²</td></tr>
<tr><td>12 000 BTU</td><td>environ 3,5 kW</td><td>25 à 35 m²</td></tr>
<tr><td>18 000 BTU</td><td>environ 5,3 kW</td><td>35 à 50 m²</td></tr>
<tr><td>24 000 BTU</td><td>environ 7 kW</td><td>50 à 70 m²</td></tr>
</tbody></table></div>
<p>Ces surfaces correspondent à une pièce de hauteur courante (environ 2,7 m), correctement isolée. Repère de conversion : 1 kW vaut environ 3 412 BTU/h.</p>
<h2>Ce qui fait monter le besoin</h2>
<ul>
<li><b>Le climat</b> : à Marrakech, les étés dépassent souvent 40 °C ; prévoyez une marge par rapport aux tableaux établis pour des climats tempérés.</li>
<li><b>Le dernier étage</b> sous une terrasse non isolée, qui chauffe toute la journée.</li>
<li><b>Les grandes baies vitrées</b> exposées au sud ou à l'ouest.</li>
<li><b>La hauteur sous plafond</b> : un séjour en double hauteur ou un riad avec patio couvert.</li>
<li><b>L'occupation et les équipements</b> : cuisine ouverte, nombreux occupants, matériel informatique.</li>
</ul>
<h2>Split, gainable ou VRV ?</h2>
<ul>
<li><b>Split mural</b> : simple et économique pour quelques pièces.</li>
<li><b>Gainable</b> : un appareil caché dans un faux plafond qui distribue l'air par des bouches, plus discret pour une villa.</li>
<li><b>VRV / DRV</b> : un groupe extérieur et plusieurs unités intérieures réglées séparément, adapté aux grandes villas, hôtels et bureaux.</li>
</ul>
<h2>Quand faire un bilan thermique</h2>
<p>Pour une villa, un riad, un hôtel ou un commerce, le bureau d'études calcule les apports de chaleur pièce par pièce (murs, vitrages, toiture, occupants, équipements). Il choisit le système, dimensionne les réseaux et les alimentations électriques, et évite d'acheter des appareils surdimensionnés. Bien isoler la toiture et protéger les vitrages du soleil réduit souvent la puissance nécessaire davantage que n'importe quel appareil.</p>
""",
 "faq": [("Quelle puissance de climatiseur pour 20 m² ?", "Un appareil de 9 000 BTU (environ 2,6 kW) convient en général à une pièce de 20 m² bien isolée ; prévoyez plus sous une terrasse ou avec de grandes baies au soleil."),
         ("Combien de BTU pour 30 m² ?", "Pour 30 m², on part en général sur 12 000 BTU (environ 3,5 kW), à ajuster selon l'isolation et l'exposition."),
         ("Faut-il un bilan thermique pour climatiser une villa ?", "C'est recommandé : un calcul pièce par pièce évite les appareils sous- ou surdimensionnés et permet de choisir entre split, gainable et VRV.")],
 "sources": [],
},
{
 "slug": "conseil-isolation-thermique-rtcm-maroc",
 "title": "Isolation thermique d'une maison au Maroc : ce que demande le RTCM",
 "crumb": "Isolation et RTCM",
 "desc": "Isolation thermique au Maroc : le règlement thermique de construction (RTCM), les 6 zones climatiques (Marrakech en zone 5), isolation de la toiture, des murs et des dalles sur sol, vitrages et confort d'été.",
 "lead": "Le règlement thermique marocain expliqué simplement : zones climatiques, parois à isoler en priorité, et ce que cela change pour le confort et la facture de climatisation.",
 "img": "images/villa-finie.jpg", "min": 6,
 "body": """
<p>Une maison bien isolée reste fraîche plus longtemps l'été et consomme beaucoup moins en climatisation. Au Maroc, ces performances sont encadrées par le <b>règlement thermique de construction (RTCM)</b>, approuvé par le décret n° 2-13-874 du 15 octobre 2014, qui fixe des exigences minimales pour les bâtiments neufs.</p>
<h2>Six zones climatiques</h2>
<p>Le RTCM découpe le Maroc en six zones climatiques. Les exigences dépendent de la zone : plus le climat est chaud ou froid, plus l'enveloppe doit être performante. <b>Marrakech est classée en zone 5</b>, l'une des zones les plus exigeantes pour le confort d'été.</p>
<h2>Ce que le règlement vise</h2>
<ul>
<li><b>La toiture</b> : c'est la paroi la plus exposée au soleil, et la première à isoler. Sous une terrasse non isolée, le dernier étage devient une étuve.</li>
<li><b>Les murs extérieurs</b> : double cloison avec isolant, ou blocs isolants, selon le niveau de performance visé.</li>
<li><b>Les dalles sur sol</b> : dans les zones 5 et 6, le RTCM demande d'isoler les dalles au sol des espaces climatisés ou chauffés.</li>
<li><b>Les vitrages</b> : leur surface, leur orientation et leurs protections solaires (casquettes, brise-soleil, volets).</li>
</ul>
<p>Le règlement propose deux façons de s'y conformer : respecter des valeurs minimales d'isolation paroi par paroi, ou démontrer par le calcul que le bâtiment ne dépasse pas des besoins de chauffage et de climatisation maximaux.</p>
<h2>À qui il s'applique</h2>
<p>Le RTCM vise les bâtiments neufs résidentiels et tertiaires (hôtels, bureaux, écoles, hôpitaux), hors habitat individuel rural. Même quand il n'est pas imposé, l'appliquer à une villa reste l'un des meilleurs investissements de confort.</p>
<h2>Les bons choix pour une villa à Marrakech</h2>
<ol>
<li>Isoler en priorité la toiture-terrasse, avec l'étanchéité.</li>
<li>Protéger les vitrages au sud et à l'ouest du soleil d'été.</li>
<li>Isoler les murs les plus exposés et traiter les ponts thermiques (poteaux, abouts de dalles).</li>
<li>Dimensionner ensuite la climatisation sur la maison isolée : la puissance nécessaire baisse sensiblement.</li>
</ol>
<h2>Le rôle du bureau d'études</h2>
<p>Le BET conseille l'architecte dans le choix des matériaux et des épaisseurs pour atteindre les performances du RTCM, vérifie la conformité par le calcul quand c'est nécessaire, puis dimensionne la climatisation en conséquence.</p>
""",
 "faq": [("Dans quelle zone thermique se trouve Marrakech ?", "Marrakech est classée en zone climatique 5 du règlement thermique de construction marocain (RTCM), l'une des plus exigeantes pour le confort d'été."),
         ("Le RTCM s'applique-t-il à ma villa ?", "Il vise les bâtiments neufs résidentiels et tertiaires, hors habitat individuel rural ; même quand il n'est pas imposé, l'appliquer améliore nettement le confort."),
         ("Quelle partie de la maison isoler en priorité ?", "La toiture-terrasse, la paroi la plus exposée au soleil, puis les vitrages et les murs les plus exposés.")],
 "sources": [("https://energetique.uae.ma/textes_energ/decret_%202_13_874%20_construction.pdf", "Décret n° 2-13-874 (RTCM)"),
             ("https://ordrearchicentre.org/wp-content/uploads/2020/05/R%C3%A8glement-thermique-de-construction-au-Maroc-.pdf", "RTCM, version simplifiée"),
             ("https://cnoa.ma/s/a/library/2025-01-28/61a97566-1453-4d87-b737-56da14a67f7d.pdf", "Conseil national de l'Ordre des architectes, RTCM")],
},

]


# Lots (familles d'articles) : ordre d'affichage sur la page Conseils et dans la FAQ
LOTS = [("structure", "Structure et béton armé"), ("electricite", "Électricité"), ("plomberie", "Plomberie et sanitaire"),
        ("cvc", "Climatisation et ventilation"), ("thermique", "Thermique et énergie"), ("incendie", "Sécurité incendie"),
        ("vrd", "VRD et réseaux"), ("achat", "Achat et expertise"), ("reglementation", "Démarches, prix et chantier")]
LOT_NOM = dict(LOTS)
# catégorie des articles écrits avant les lots (y compris ceux faits à la main, hors de ce script)
CAT = {"conseil-permis-de-construire-maroc-rokhas": "reglementation", "conseil-etude-de-sol-maroc-prix": "structure",
       "conseil-prix-bureau-etudes-techniques-maroc": "reglementation", "conseil-reglement-parasismique-rps-2011-maroc": "structure",
       "conseil-prix-construction-m2-maroc": "reglementation", "conseil-dosage-beton-fondation-dalle": "structure",
       "conseil-prix-piscine-maroc": "structure", "conseil-fissures-maison-causes-gravite": "structure",
       "conseil-surelevation-ajouter-etage-maroc": "structure", "conseil-etancheite-toiture-terrasse-maroc": "structure",
       "conseil-climatisation-puissance-btu-m2": "cvc", "conseil-isolation-thermique-rtcm-maroc": "thermique",
       "conseil-prix-construction-villa-marrakech": "reglementation", "conseil-role-bureau-etudes-techniques": "reglementation",
       "conseil-norme-electrique-nf-c-15-100-maroc": "electricite"}
for _a in ARTICLES:
    _a.setdefault("cat", CAT.get(_a["slug"], "reglementation"))


# photos du site réservées à un seul article (les autres articles ont leur image dans images/conseils/)
IMG_CHOISIE = {"conseil-prix-piscine-maroc": "images/projects/villa2.jpg",
               "conseil-controle-ferraillage-avant-coulage": "images/service_img3.jpg",
               "conseil-poutre-portee-retombee": "images/services/beton-poutre.jpg",
               "conseil-surelevation-ajouter-etage-maroc": "images/projects/riad4.jpg",
               "conseil-delai-decoffrage-dalle-poteaux": "images/services/maison-beton.jpg",
               "conseil-prix-construction-m2-maroc": "images/villa-finie.jpg",
               "conseil-tableau-electrique-gtl-maison": "images/services/elec-tableau.jpg",
               "conseil-disjoncteur-ou-differentiel-difference": "images/services/elec-disjoncteurs.jpg",
               "conseil-combien-prises-par-circuit": "images/services/elec-prises.jpg",
               "conseil-electricite-piscine-securite": "images/services/ele1.jpg",
               "conseil-section-cable-calibre-disjoncteur": "images/services/ele2.jpg",
               "conseil-prix-installation-electrique-villa-maroc": "images/villa-technique.jpg"}
# lots dont chaque article a déjà son image unique (contrôlé à chaque génération)
LOTS_IMAGES_UNIQUES = {"structure", "electricite"}


def charger_lots():
    """Ajoute les articles des fichiers tools/articles/<lot>.py (une liste ARTICLES par fichier)."""
    import glob, importlib.util
    vus = {a["slug"] for a in ARTICLES}
    for f in sorted(glob.glob(os.path.join(ROOT, "tools", "articles", "*.py"))):
        spec = importlib.util.spec_from_file_location(os.path.basename(f)[:-3], f)
        m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
        for a in m.ARTICLES:
            if a["slug"] in vus:
                continue
            assert a["cat"] in LOT_NOM, (f, a["slug"], a["cat"])
            assert len(a["faq"]) >= 1 and os.path.exists(os.path.join(ROOT, a["img"])), (f, a["slug"])
            vus.add(a["slug"]); ARTICLES.append(a); CAT[a["slug"]] = a["cat"]
    for a in ARTICLES:
        CAT[a["slug"]] = a["cat"]
        # une image propre à chaque article : images/conseils/<slug>.jpg, sinon une photo du site choisie pour lui
        propre = f"images/conseils/{a['slug']}.jpg"
        if os.path.exists(os.path.join(ROOT, propre)):
            a["img"] = propre
        elif a["slug"] in IMG_CHOISIE:
            a["img"] = IMG_CHOISIE[a["slug"]]
    import collections
    # les images réservées aux lots déjà traités ne doivent apparaître nulle part ailleurs : les autres articles
    # (lots pas encore illustrés un par un) prennent provisoirement une photo générique non réservée
    reservees = {a["img"] for a in ARTICLES if a["cat"] in LOTS_IMAGES_UNIQUES}
    secours = [x for x in ["images/projects/project1.jpg", "images/projects/project2.jpg", "images/projects/project3.jpg",
               "images/projects/project4.jpg", "images/projects/project5.jpg", "images/projects/project6.jpg",
               "images/projects/villa1.jpg", "images/projects/riad1.jpg", "images/projects/riad2.jpg", "images/projects/riad3.jpg",
               "images/villa-finie.jpg"] if x not in reservees]
    k = 0
    for a in ARTICLES:
        if a["cat"] not in LOTS_IMAGES_UNIQUES and a["img"] in reservees:
            a["img"] = secours[k % len(secours)]; k += 1
    usage = collections.Counter(a["img"] for a in ARTICLES)
    for a in ARTICLES:
        if a["cat"] in LOTS_IMAGES_UNIQUES and usage[a["img"]] > 1:
            raise SystemExit(f"image en double : {a['img']} ({[b['slug'] for b in ARTICLES if b['img'] == a['img']]})")


def esc(s):
    return html.escape(s, quote=True)


def build():
    tpl = open(os.path.join(ROOT, TEMPLATE), encoding="utf-8").read()
    # le modèle a peut-être déjà sa colonne latérale : on la retire, apply_layout() la recrée pour chaque article
    tpl = re.sub(r'<aside class="article-cote">.*?</aside>', "", tpl, flags=re.S).replace('<div class="conteneur article-grille">', '<div class="conteneur">')
    # le modèle porte peut-être les liens vers ses propres traductions : on les retire (articles_i18n les recrée pour chaque article)
    tpl = re.sub(r'<link rel="alternate" hreflang="[^"]+" href="[^"]*">\n', "", tpl)
    tpl = re.sub(r'<nav class="langues"[^>]*>.*?</nav>', '<nav class="langues" aria-label="Langue"><a href="index.html" hreflang="fr" lang="fr" aria-current="true">FR</a><a href="en/index.html" hreflang="en" lang="en">EN</a><a href="ar/index.html" hreflang="ar" lang="ar">ع</a></nav>', tpl, count=1, flags=re.S)
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
        h = re.sub(r'(<div class="fil"><a href="index.html">Accueil</a> / <a href="conseils.html">Conseils</a> / )[^<]*(</div>)', lambda m: m.group(1) + f'<a href="conseils-{a["cat"]}.html">{esc(LOT_NOM[a["cat"]])}</a> / ' + esc(a["crumb"]) + m.group(2), h, count=1)
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
    page_conseils()
    # plan du site
    sp = os.path.join(ROOT, "sitemap.xml"); s = open(sp, encoding="utf-8").read()
    add = "".join(f"  <url><loc>{DOMAIN}/{a['slug']}.html</loc><lastmod>{DATE}</lastmod><priority>0.7</priority></url>\n" for a in ARTICLES if a["slug"] not in s)
    s = s.replace(f"  <url><loc>{DOMAIN}/conseils.html</loc>", add + f"  <url><loc>{DOMAIN}/conseils.html</loc>", 1)
    s = re.sub(r"(<url><loc>https://sigma-icc.ma/conseils.html</loc><lastmod>)[^<]*", r"\g<1>" + DATE, s)
    open(sp, "w", encoding="utf-8").write(s)
    print(len(ARTICLES), "articles")


def cartes_conseils():
    """{slug: carte HTML} pour tous les articles : ceux du script, plus les articles faits à la main déjà présents sur conseils.html."""
    c = open(os.path.join(ROOT, "conseils.html"), encoding="utf-8").read()
    cartes = {m.group(1): m.group(0).replace(' en-plus"', '"', 1) for m in re.finditer(r'<a class="service(?: en-plus)?" href="(conseil-[^"]+)\.html">.*?</a>', c, re.S)}
    for a in ARTICLES:
        cartes[a["slug"]] = (f'<a class="service" href="{a["slug"]}.html"><img src="{a["img"]}" alt="" loading="lazy" width="750" height="600">\n'
                             f'  <div><span class="code">{esc(LOT_NOM[a["cat"]])} · {a["min"]} min</span><h3>{esc(a["title"])}</h3><p>{esc(a["lead"])}</p><span class="lire">Lire l\'article →</span></div></a>')
    return cartes


# présentation de chaque thème (pages conseils-<lot>.html) et service lié
LOT_INFO = {
 "electricite": ("Normes NF C 15-100 et NM 06.1.100, tableau électrique, différentiels, prises, mise à la terre, photovoltaïque : les règles d'une installation électrique sûre au Maroc.", "service-CFA.html"),
 "structure": ("Fondations, poteaux, poutres, planchers, béton et acier, règlement parasismique : comprendre la structure de votre maison avant et pendant le chantier.", "service-STRUCTURE.html"),
 "plomberie": ("Diamètres, évacuations, chauffe-eau solaire, pression, fuites, assainissement : bien concevoir la plomberie d'une villa ou d'un riad.", "service-FD.html"),
 "cvc": ("Climatisation, ventilation, chauffage et humidité : choisir et dimensionner les bons équipements pour le climat de Marrakech.", "service-FD.html"),
 "thermique": ("Isolation, vitrages, orientation, protections solaires et facture d'électricité : construire une maison confortable en été comme en hiver.", "service-EGT.html"),
 "incendie": ("Établissements recevant du public, hôtels, riads, parkings : détection, désenfumage, issues de secours et équipements de sécurité incendie.", "service-CSSI.html"),
 "vrd": ("Lotissements, assainissement, branchements, voirie et eaux pluviales : les réseaux qui desservent un terrain ou un projet.", "service-VRD.html"),
 "achat": ("Avant d'acheter une maison, un riad, un appartement neuf ou un terrain : ce qu'il faut vérifier, lot par lot, et ce que coûte une expertise.", "contact.html#formulaire"),
 "reglementation": ("Permis de construire, bureau de contrôle, garanties, réception des travaux, contrats et prix : les démarches d'un projet de construction au Maroc.", "contact.html#formulaire"),
}
# parcours « Par où commencer ? » : (situation, phrase, article)
PARCOURS = [("Je construis", "Budget, études et étapes d'une villa", "conseil-prix-construction-m2-maroc"),
            ("J'achète", "La checklist avant de signer", "conseil-expertise-avant-achat-maison-checklist"),
            ("Je rénove", "Par où commencer une rénovation", "conseil-renovation-maison-ancienne-par-ou-commencer"),
            ("Mon électricité", "Les règles clés de la NF C 15-100", "conseil-norme-electrique-nf-c-15-100-maroc")]
PAR_LOT = 6  # articles montrés par thème sur la page Conseils


def _ordre_cartes():
    cartes = cartes_conseils()
    ordre = [a["slug"] for a in ARTICLES] + [k for k in cartes if k not in {a["slug"] for a in ARTICLES}]
    par_lot = {k: [x for x in ordre if x in cartes and CAT.get(x, "reglementation") == k] for k, _ in LOTS}
    return cartes, par_lot


def page_conseils():
    cp = os.path.join(ROOT, "conseils.html"); c = open(cp, encoding="utf-8").read()
    cartes, par_lot = _ordre_cartes()
    total = sum(len(v) for v in par_lot.values())
    titres = {a["slug"]: a["title"] for a in ARTICLES}
    parcours = "".join(f'<a class="parcours" href="{slug}.html"><span>{esc(sit)}</span><b>{esc(txt)}</b></a>'
                       for sit, txt, slug in PARCOURS if os.path.exists(os.path.join(ROOT, slug + ".html")))
    nav = "".join(f'<a href="conseils-{k}.html" data-lot="{k}">{esc(nom)} <span>{len(par_lot[k])}</span></a>' for k, nom in LOTS if par_lot[k])
    blocs = []
    for k, nom in LOTS:
        lot = par_lot[k]
        if not lot:
            continue
        cards = "".join(cartes[x].replace('<a class="service"', '<a class="service en-plus"', 1) if i >= PAR_LOT else cartes[x] for i, x in enumerate(lot))
        plus = f'<a class="voir-lot" href="conseils-{k}.html">Voir les {len(lot)} articles « {esc(nom)} » →</a>' if len(lot) > PAR_LOT else ""
        blocs.append(f'<div class="lot-conseils" id="lot-{k}"><div class="lot-tete"><h2>{esc(nom)}</h2><a href="conseils-{k}.html">Tout le thème →</a></div>'
                     f'<div class="grille-services">{cards}</div>{plus}</div>')
    bloc = ('<section><div class="conteneur"><!--lots-->'
            f'<div class="recherche-conseils"><label for="q-conseils">Rechercher parmi les {total} conseils</label>'
            '<input id="q-conseils" type="search" placeholder="Ex. : prises, fondation, climatisation, achat riad…" autocomplete="off" data-recherche="#lots-conseils .service">'
            '<p class="recherche-vide" hidden>Aucun article ne correspond. Essayez un autre mot, ou <a href="contact.html#formulaire">posez-nous la question</a>.</p></div>'
            f'<h2 class="titre-parcours">Par où commencer ?</h2><div class="parcours-grille">{parcours}</div>'
            f'<nav class="lots-nav" aria-label="Thèmes">{nav}</nav>'
            f'<div id="lots-conseils">{"".join(blocs)}</div><!--/lots--></div></section>\n')
    if "<!--lots-->" in c:
        c = re.sub(r'<section><div class="conteneur"><!--lots-->.*?<!--/lots--></div></section>\n', lambda m: bloc, c, count=1, flags=re.S)
    else:
        c, n = re.subn(r'<section><div class="conteneur"><div class="grille-services">.*?</div></div></section>\n(?=</main>)', lambda m: bloc, c, count=1, flags=re.S)
        assert n == 1
    open(cp, "w", encoding="utf-8").write(c)
    pages_themes(c, cartes, par_lot)


def pages_themes(base, cartes, par_lot):
    """Une page par thème (conseils-<lot>.html), construite sur le modèle de conseils.html."""
    sp = os.path.join(ROOT, "sitemap.xml"); smap = open(sp, encoding="utf-8").read()
    for k, nom in LOTS:
        lot = par_lot[k]
        if not lot:
            continue
        intro, service = LOT_INFO[k]
        url = f"{DOMAIN}/conseils-{k}.html"
        titre = f"Conseils {nom} : {len(lot)} guides pour votre projet au Maroc"
        h = base
        h = re.sub(r"<title>.*?</title>", f"<title>{esc(titre)} | SIGMA ICC</title>", h, count=1)
        for prop in ("og:title",):
            h = re.sub(rf'<meta property="{prop}" content="[^"]*">', f'<meta property="{prop}" content="{esc(titre)} | SIGMA ICC">', h, count=1)
        h = re.sub(r'<meta name="description" content="[^"]*">', f'<meta name="description" content="{esc(intro)}">', h, count=1)
        h = re.sub(r'<meta property="og:description" content="[^"]*">', f'<meta property="og:description" content="{esc(intro)}">', h, count=1)
        h = re.sub(r'<link rel="canonical" href="[^"]*">', f'<link rel="canonical" href="{url}">', h, count=1)
        h = re.sub(r'<meta property="og:url" content="[^"]*">', f'<meta property="og:url" content="{url}">', h, count=1)
        h = re.sub(r'<div class="fil">.*?</div>', f'<div class="fil"><a href="index.html">Accueil</a> / <a href="conseils.html">Conseils</a> / {esc(nom)}</div>', h, count=1, flags=re.S)
        h = re.sub(r"<h1>.*?</h1><p>.*?</p>", lambda m: f"<h1>{esc(nom)}</h1><p>{esc(intro)}</p>", h, count=1, flags=re.S)
        nav = "".join(f'<a href="conseils-{x}.html"{" aria-current=\"page\"" if x == k else ""}>{esc(n)} <span>{len(par_lot[x])}</span></a>' for x, n in LOTS if par_lot[x])
        lien_service = (f'<div class="encadre"><h3>Besoin d\'une étude pour votre projet ?</h3><p>SIGMA ICC réalise les études et le suivi de chantier, à Marrakech et partout au Maroc.</p>'
                        f'<div class="actions"><a class="btn" href="contact.html#formulaire">Demander un devis</a><a class="btn secondaire" href="{service}">Voir le service</a></div></div>')
        bloc = ('<section><div class="conteneur"><!--lots-->'
                f'<div class="recherche-conseils"><label for="q-conseils">Rechercher dans « {esc(nom)} »</label>'
                '<input id="q-conseils" type="search" placeholder="Tapez un mot-clé…" autocomplete="off" data-recherche="#lots-conseils .service">'
                '<p class="recherche-vide" hidden>Aucun article ne correspond. <a href="conseils.html">Voir tous les thèmes</a>.</p></div>'
                f'<nav class="lots-nav" aria-label="Thèmes">{nav}</nav>'
                f'<div id="lots-conseils"><div class="lot-conseils"><div class="grille-services">{"".join(cartes[x] for x in lot)}</div></div></div>'
                f'{lien_service}<!--/lots--></div></section>\n')
        h = re.sub(r'<section><div class="conteneur"><!--lots-->.*?<!--/lots--></div></section>\n', lambda m: bloc, h, count=1, flags=re.S)
        open(os.path.join(ROOT, f"conseils-{k}.html"), "w", encoding="utf-8").write(h)
        if f"/conseils-{k}.html" not in smap:
            smap = smap.replace(f"  <url><loc>{DOMAIN}/conseils.html</loc>", f"  <url><loc>{url}</loc><lastmod>{DATE}</lastmod><priority>0.8</priority></url>\n  <url><loc>{DOMAIN}/conseils.html</loc>", 1)
    open(sp, "w", encoding="utf-8").write(smap)


def page_faq():
    """FAQ par lot : une question (et sa réponse) de chaque article, regroupées par thème, avec le lien vers l'article."""
    fp = os.path.join(ROOT, "faq.html"); h = open(fp, encoding="utf-8").read()
    parts, nav, qs = [], [], []
    for k, nom in LOTS:
        arts = [a for a in ARTICLES if a["cat"] == k]
        if not arts:
            continue
        items = "".join(f'<details><summary>{esc(a["faq"][0][0])}</summary><p>{esc(a["faq"][0][1])} <a href="{a["slug"]}.html">Lire l\'article : {esc(a["crumb"])} →</a></p></details>' for a in arts)
        qs += [a["faq"][0] for a in arts]
        nav.append(f'<a href="#faq-{k}">{esc(nom)}</a>')
        parts.append(f'<h2 class="faq-lot" id="faq-{k}">{esc(nom)}</h2><div class="faq">{items}</div>')
    bloc = ('<!--faq-lots--><div class="recherche-conseils"><label for="q-faq">Rechercher une question</label>'
            '<input id="q-faq" type="search" placeholder="Ex. : différentiel, fosse septique, permis…" autocomplete="off" data-recherche=".faq-principal details">'
            '<p class="recherche-vide" hidden>Aucune question ne correspond. <a href="contact.html#formulaire">Posez-nous la vôtre</a>.</p></div>'
            f'<nav class="lots-nav" aria-label="Thèmes de la FAQ"><a href="#faq-general">Questions générales</a>{"".join(nav)}</nav>'
            '<h2 class="faq-lot" id="faq-general">Questions générales</h2><!--/faq-lots-->')
    suite = "<!--faq-lots-suite-->" + "".join(parts) + "<!--/faq-lots-suite-->"
    h = re.sub(r"<!--faq-lots-->.*?<!--/faq-lots-->", "", h, flags=re.S)
    h = re.sub(r"<!--faq-lots-suite-->.*?<!--/faq-lots-suite-->", "", h, flags=re.S)
    h = h.replace('<div class="faq-principal"><div class="faq">', '<div class="faq-principal">' + bloc + '<div class="faq">', 1)
    i = h.index('<div class="encadre" style="margin-top:32px;max-width:860px">')
    h = h[:i] + suite + h[i:]
    # données structurées : questions générales d'origine + questions par lot
    m = re.search(r'<script type="application/ld\+json">(.*?)</script>', h, re.S)
    ld = json.loads(m.group(1))
    base = [q for q in ld["mainEntity"] if not q.get("_lot")]
    ld["mainEntity"] = [q for q in base if q["name"] not in {x for x, _ in qs}] + [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": r}} for q, r in qs]
    h = h[:m.start(1)] + json.dumps(ld, ensure_ascii=False) + h[m.end(1):]
    open(fp, "w", encoding="utf-8").write(h)


SERVICE_LOTS = {"STRUCTURE": ["structure"], "CFA": ["electricite"], "FD": ["plomberie", "cvc"], "CSSI": ["incendie"],
                "VRD": ["vrd"], "EGT": ["thermique"], "BIM": []}


def liens_services():
    """Sur chaque page service (FR) : les conseils du même lot, juste avant l'encadré « Intéressé par ce service ? »."""
    for k, lots in SERVICE_LOTS.items():
        p = os.path.join(ROOT, f"service-{k}.html"); h = open(p, encoding="utf-8").read()
        h = re.sub(r"<!--conseils-lies-->.*?<!--/conseils-lies-->", "", h, flags=re.S)
        arts = [a for a in ARTICLES if a["cat"] in lots] + ([a for a in ARTICLES if a["slug"] == "conseil-bim-avantages-projet"] if k == "BIM" else [])
        if arts:
            li = "".join(f'<li><a href="{a["slug"]}.html">{esc(a["title"])}</a></li>' for a in arts[:12])
            bloc = f'<!--conseils-lies--><div class="conseils-lies"><h2>Nos conseils sur ce sujet</h2><ul>{li}</ul><a class="lien-fleche" href="conseils-{lots[0] if lots else "reglementation"}.html">Tous les conseils du thème →</a></div><!--/conseils-lies-->'
            i = h.index('<div class="encadre"><h3>Intéressé par ce service ?</h3>')
            h = h[:i] + bloc + h[i:]
        open(p, "w", encoding="utf-8").write(h)


def apply_layout():
    """Mise en page en deux colonnes sur ordinateur : l'article (largeur lisible) et une colonne latérale qui reste visible
    (sommaire, contact, autres articles). Sur téléphone, la colonne passe sous l'article. S'applique à tous les articles
    « Conseils », anciens et nouveaux ; la colonne est reconstruite à chaque passage (liste des articles à jour)."""
    import glob
    cards = re.findall(r'<a class="service(?: en-plus)?" href="(conseil-[^"]+)">.*?<h3>(.*?)</h3>', open(os.path.join(ROOT, "conseils.html"), encoding="utf-8").read(), re.S)
    for f in sorted(glob.glob(os.path.join(ROOT, "conseil-*.html"))):
        h = open(f, encoding="utf-8").read()
        # page déjà mise en page : on retire l'ancienne colonne pour la reconstruire (liste des articles à jour)
        h = re.sub(r'<aside class="article-cote">.*?</aside>', "", h, flags=re.S).replace('<div class="conteneur article-grille">', '<div class="conteneur">')
        h = re.sub(r'<h2 id="partie-\d+">', "<h2>", h)
        name = os.path.basename(f)
        # ancres sur les intertitres pour le sommaire
        n = [0]
        def anchor(m):
            n[0] += 1
            return f'<h2 id="partie-{n[0]}">{m.group(1)}</h2>'
        start, end = h.index('<article class="contenu article">'), h.index("</article>")
        art = re.sub(r"<h2>(.*?)</h2>", anchor, h[start:end])
        titres = re.findall(r'<h2 id="(partie-\d+)">(.*?)</h2>', art)
        sommaire = "".join(f'<li><a href="#{i}">{t}</a></li>' for i, t in titres)
        moi = CAT.get(name[:-5], "reglementation")
        cands = [c for c in cards if c[0] != name]
        cands = [c for c in cands if CAT.get(c[0][:-5]) == moi] + [c for c in cands if CAT.get(c[0][:-5]) != moi]
        autres = "".join(f'<li><a href="{u}">{t}</a></li>' for u, t in cands[:6]) + f'<li class="tous"><a href="conseils-{moi}.html">Tous les conseils « {esc(LOT_NOM[moi])} » →</a></li>'
        aside = (f'<aside class="article-cote">'
                 f'<div class="cote-carte"><h3>Sommaire</h3><ol class="sommaire">{sommaire}</ol></div>'
                 f'<div class="cote-carte"><h3>Autres conseils</h3><ul class="autres">{autres}</ul></div>'
                                  '<div class="cote-carte cote-contact"><h3>Besoin d\'un bureau d\'études ?</h3><p>Études béton armé, électricité, plomberie et CVC, suivi de chantier à Marrakech et partout au Maroc.</p>'
                 '<a class="btn" href="contact.html#formulaire">Demander une étude</a>'
                 '<a class="btn secondaire" href="https://wa.me/212620897660" rel="noopener">Écrire sur WhatsApp</a>'
                 '<a class="cote-tel" href="tel:+212661057455" dir="ltr">+212 6 61 05 74 55</a></div>'
"</aside>")
        h = h[:start] + art + h[end:]
        h = h.replace('<section><div class="conteneur"><article class="contenu article">', '<section><div class="conteneur article-grille"><article class="contenu article">', 1)
        h = h.replace("</article></div></section>", "</article>" + aside + "</div></section>", 1)
        open(f, "w", encoding="utf-8").write(h)


if __name__ == "__main__":
    charger_lots()
    build()
    apply_layout()
    page_faq()
    liens_services()
    import articles_i18n  # versions anglaise et arabe (si les traductions existent)
    articles_i18n.main()
