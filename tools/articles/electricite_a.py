# -*- coding: utf-8 -*-
# Lot electricite_a : articles « Conseils » SIGMA ICC (électricité, partie A)

ARTICLES = [
{
 "slug": "conseil-combien-prises-par-circuit",
 "cat": "electricite",
 "title": "Combien de prises sur un même circuit ? Les règles de la NF C 15-100",
 "crumb": "Prises par circuit",
 "desc": "Combien de prises par circuit : 8 socles maximum en 1,5 mm² protégé 16 A, 12 en 2,5 mm² protégé 20 A, 6 pour la cuisine. Règles de comptage et cas d'une villa.",
 "lead": "Le nombre de prises admis sur un circuit dépend de la section des fils et du calibre du disjoncteur. Voici les repères de la NF C 15-100, référence des bureaux d'études au Maroc.",
 "img": "images/services/elec-prises.jpg",
 "min": 3,
 "body": """
<p>Selon les règles de la NF C 15-100 (édition 2002 amendée, encore très largement appliquée), un circuit de prises de courant 16 A peut alimenter <b>au maximum 8 socles s'il est câblé en 1,5 mm² et protégé par un disjoncteur de 16 A</b>, et <b>au maximum 12 socles s'il est câblé en 2,5 mm² et protégé par un disjoncteur de 20 A</b>. Ces limites évitent qu'un même câble soit surchargé par trop d'appareils branchés en même temps.</p>
<h2>Le tableau à retenir</h2>
<div class="tableau"><table><thead><tr><th>Section des conducteurs (cuivre)</th><th>Protection</th><th>Nombre maximal de socles</th></tr></thead><tbody>
<tr><td>1,5 mm²</td><td>Disjoncteur 16 A</td><td>8</td></tr>
<tr><td>2,5 mm²</td><td>Disjoncteur 20 A</td><td>12</td></tr>
<tr><td>2,5 mm² (prises du plan de travail de la cuisine)</td><td>Disjoncteur 20 A</td><td>6, sur un circuit propre à la cuisine</td></tr>
</tbody></table></div>
<p>Le fusible n'est pas une alternative au disjoncteur pour le circuit 1,5 mm² : dans les installations neuves, la protection se fait par disjoncteur divisionnaire. Le circuit de prises est par ailleurs placé, comme tous les circuits, en aval d'un dispositif différentiel 30 mA.</p>
<h2>Comment compter les prises</h2>
<ul>
<li><b>Un socle = une prise</b> : depuis l'amendement de 2015, un bloc double ou triple compte pour 2 ou 3 socles. Les anciennes règles de décompte par boîtier ne s'appliquent plus.</li>
<li><b>Les prises spécialisées ne comptent pas</b> : lave-linge, four, lave-vaisselle ou climatiseur ont leur propre circuit (voir <a href="conseil-circuits-specialises-nf-c-15-100.html">les circuits spécialisés</a>).</li>
<li><b>Les prises commandées</b> (allumées par un interrupteur) se comptent comme des prises si elles sont sur le circuit de prises.</li>
</ul>
<h2>Ce que cela donne dans une villa</h2>
<p>Une villa de 200 m² à Marrakech compte facilement 40 à 60 prises de courant. Avec des circuits 2,5 mm² / 20 A, il faut donc au moins 4 à 5 circuits de prises, sans compter les circuits de la cuisine et les circuits spécialisés. En pratique, le bureau d'études répartit les prises par zone (séjour, chambres, extérieur, bureau) pour qu'un défaut ne coupe pas toute la maison et pour équilibrer les charges entre les différentiels, voire entre les phases en triphasé.</p>
<p>Deux conseils de terrain : évitez de mettre sur le même circuit les prises d'un bureau avec informatique et celles d'une pièce où l'on branche un radiateur d'appoint ou un fer à repasser l'hiver, et prévoyez un circuit dédié aux prises extérieures (jardin, terrasse, piscine), plus exposées à l'humidité.</p>
<h2>Et la norme marocaine ?</h2>
<p>Au Maroc, les normes NM 06.1.100 à 06.1.106 publiées par l'IMANOR encadrent les installations basse tension ; la NM 06.1.100 a été homologuée en 2025. Dans les CPS et les études, la NF C 15-100 reste la référence technique la plus citée. Son édition 2024 a remplacé celle de 2002 et réorganise la norme en plusieurs parties : le bureau d'études vérifie quelle édition s'applique à votre marché et ce que demande le bureau de contrôle.</p>
<h2>Le rôle du bureau d'études</h2>
<p>Un bureau d'études électricité établit le schéma unifilaire, le nombre de circuits, les sections et les calibres, en tenant compte des longueurs de câble (chute de tension) et de la puissance réellement souscrite auprès de Radeema ou de l'ONEE. C'est ce dossier qui permet de comparer les devis d'électriciens sur une base claire. Pour le cadre général, voir aussi notre article sur <a href="conseil-norme-electrique-nf-c-15-100-maroc.html">la norme NF C 15-100 au Maroc</a>.</p>
""",
 "faq": [
  ("Combien de prises sur un disjoncteur 16 A ?", "Selon la NF C 15-100, un circuit en 1,5 mm² protégé par un disjoncteur 16 A peut alimenter au maximum 8 socles de prise de courant."),
  ("Combien de prises sur un disjoncteur 20 A ?", "Un circuit en 2,5 mm² protégé par un disjoncteur 20 A peut alimenter jusqu'à 12 socles, sauf dans la cuisine où le circuit du plan de travail est limité à 6 socles."),
  ("Une prise double compte-t-elle pour une ou deux prises ?", "Elle compte pour deux : depuis l'amendement de 2015 de la NF C 15-100, chaque socle d'un bloc multiple est compté séparément."),
 ],
 "sources": [
  ("https://www.legrand.fr/questions-frequentes/combien-de-prises-peut-on-mettre-sur-un-disjoncteur-16-a", "Legrand, combien de prises sur un disjoncteur 16 A"),
  ("https://izi-by-edf.fr/blog/electricite-combien-de-prises-par-disjoncteur", "IZI by EDF, nombre de prises par disjoncteur"),
  ("https://www.imanor.gov.ma/normes/page/62/", "IMANOR, catalogue des normes marocaines"),
 ],
},
{
 "slug": "conseil-circuits-specialises-nf-c-15-100",
 "cat": "electricite",
 "title": "Circuits spécialisés obligatoires : four, lave-linge, clim…",
 "crumb": "Circuits spécialisés",
 "desc": "Circuits spécialisés NF C 15-100 : au moins 4, dont la plaque en 6 mm² / 32 A et trois circuits 2,5 mm² / 20 A (four, lave-linge…). Cas de la clim au Maroc.",
 "lead": "Certains appareils doivent avoir leur propre ligne depuis le tableau. Quels sont-ils, avec quelle section et quel disjoncteur, et que prévoir pour une villa climatisée à Marrakech.",
 "img": "images/services/elec-disjoncteurs.jpg",
 "min": 3,
 "body": """
<p>Un circuit spécialisé est une ligne qui part du tableau pour alimenter <b>un seul appareil</b> de forte puissance. La NF C 15-100 impose dans un logement <b>au moins 4 circuits spécialisés</b> : un circuit pour la cuisinière ou la plaque de cuisson (6 mm², disjoncteur 32 A en monophasé) et au moins trois circuits pour des appareils comme le lave-linge, le lave-vaisselle, le four ou le sèche-linge, généralement en 2,5 mm² protégés par un disjoncteur 20 A.</p>
<h2>La liste des circuits spécialisés</h2>
<div class="tableau"><table><thead><tr><th>Appareil</th><th>Section courante</th><th>Protection courante</th></tr></thead><tbody>
<tr><td>Plaque de cuisson ou cuisinière (monophasé)</td><td>6 mm²</td><td>Disjoncteur 32 A</td></tr>
<tr><td>Plaque de cuisson (triphasé)</td><td>2,5 mm²</td><td>Disjoncteur 20 A</td></tr>
<tr><td>Four, lave-linge, lave-vaisselle, sèche-linge</td><td>2,5 mm²</td><td>Disjoncteur 20 A</td></tr>
<tr><td>Chauffe-eau électrique monophasé</td><td>2,5 mm²</td><td>Disjoncteur 20 A</td></tr>
<tr><td>Congélateur</td><td>2,5 mm²</td><td>Disjoncteur 20 A (circuit dédié conseillé)</td></tr>
<tr><td>Climatiseur, pompe à chaleur, pompe de piscine</td><td>Selon la puissance et la notice</td><td>Selon la notice du fabricant</td></tr>
</tbody></table></div>
<p>Ces valeurs sont les repères usuels de la NF C 15-100 (tableau des sections et calibres repris par les fabricants de câbles). Pour les appareils puissants ou éloignés du tableau, la section est recalculée en fonction de la longueur pour limiter la chute de tension.</p>
<h2>Pourquoi une ligne par appareil</h2>
<ul>
<li><b>Éviter les surcharges</b> : un four (2 à 3,5 kW) et un lave-linge en chauffe sur la même ligne dépassent vite 16 A.</li>
<li><b>Limiter les coupures</b> : un défaut sur le lave-linge ne doit pas couper le réfrigérateur ou l'éclairage.</li>
<li><b>Choisir le bon différentiel</b> : le lave-linge et la plaque de cuisson doivent être en aval d'un interrupteur différentiel 30 mA de type A, voir <a href="conseil-differentiel-30ma-type-ac-a-f.html">les types AC, A et F</a>.</li>
</ul>
<h2>La climatisation, un cas à part au Maroc</h2>
<p>À Marrakech, où l'été dépasse régulièrement 40 °C, la climatisation est souvent le premier poste de consommation. Chaque unité extérieure, chaque gainable et chaque groupe VRV doit avoir son circuit dédié, dimensionné selon l'intensité indiquée par le fabricant, avec un dispositif de coupure à proximité pour l'entretien. Les climatiseurs « inverter » comportent une électronique de variation de vitesse : les fabricants de matériel recommandent pour eux un différentiel de type F (ou A selon l'appareil). Les autres équipements de la villa suivent la même logique : pompe de piscine, surpresseur, portail motorisé, borne de recharge.</p>
<h2>Les prévoir dès l'étude</h2>
<p>Ajouter un circuit spécialisé après coup oblige à tirer une nouvelle ligne et souvent à refaire des saignées. Le bureau d'études établit le bilan de puissance, liste tous les appareils (y compris ceux qui seront achetés plus tard), fixe les sections et calibres, et vérifie que le tableau garde une réserve suffisante. Pour la cuisine en particulier, lisez notre article sur <a href="conseil-four-plaque-cuisson-cable-disjoncteur.html">le câble et le disjoncteur du four et de la plaque</a>.</p>
""",
 "faq": [
  ("Combien de circuits spécialisés faut-il dans une maison ?", "La NF C 15-100 en impose au moins 4 : un circuit 32 A pour la plaque ou la cuisinière et trois circuits pour des appareils comme le lave-linge, le lave-vaisselle et le four."),
  ("Le chauffe-eau électrique doit-il avoir son propre circuit ?", "Oui, le chauffe-eau électrique est alimenté par un circuit dédié, couramment en 2,5 mm² protégé par un disjoncteur 20 A pour un appareil monophasé courant."),
  ("Un climatiseur doit-il être sur un circuit dédié ?", "Oui, chaque climatiseur ou groupe extérieur doit avoir sa ligne propre, dimensionnée selon l'intensité donnée par le fabricant et protégée par un différentiel adapté, souvent de type F pour les modèles inverter."),
 ],
 "sources": [
  ("https://home.nexans.fr/app/uploads/2022/03/Tableau-section-et-calibres.pdf", "Nexans, tableau des sections et calibres NF C 15-100"),
  ("https://www.legrand.fr/questions-frequentes/quel-disjoncteur-differentiel-pour-une-climatisation", "Legrand, quel différentiel pour une climatisation"),
  ("https://www.legrand.fr/questions-frequentes/que-doit-on-brancher-sur-un-interrupteur-differentiel-de-type-a", "Legrand, que brancher sur un différentiel de type A"),
 ],
},
{
 "slug": "conseil-four-plaque-cuisson-cable-disjoncteur",
 "cat": "electricite",
 "title": "Four et plaque de cuisson : quel câble et quel disjoncteur ?",
 "crumb": "Four et plaque de cuisson",
 "desc": "Plaque de cuisson en monophasé : câble 6 mm² et disjoncteur 32 A sous différentiel type A. En triphasé : 2,5 mm² et 20 A. Four : circuit dédié 2,5 mm² / 20 A.",
 "lead": "La cuisine concentre les appareils les plus puissants de la maison. Voici les sections de câble et les calibres de disjoncteur usuels pour le four et la plaque, et les erreurs fréquentes sur chantier.",
 "img": "images/services/elec-tableau.jpg",
 "min": 3,
 "body": """
<p>En monophasé, la plaque de cuisson (ou la cuisinière) est alimentée par un <b>circuit spécialisé en 6 mm² protégé par un disjoncteur 32 A</b>, placé en aval d'un interrupteur différentiel 30 mA de type A. Le four a lui aussi son propre circuit, couramment <b>en 2,5 mm² protégé par un disjoncteur 20 A</b>. En triphasé, la plaque peut être alimentée en 2,5 mm² avec un disjoncteur tétrapolaire 20 A. Ce sont les repères de la NF C 15-100, la référence la plus utilisée par les bureaux d'études au Maroc.</p>
<h2>Les valeurs usuelles</h2>
<div class="tableau"><table><thead><tr><th>Appareil</th><th>Alimentation</th><th>Section du câble</th><th>Disjoncteur</th></tr></thead><tbody>
<tr><td>Plaque de cuisson ou cuisinière</td><td>Monophasé 230 V</td><td>6 mm²</td><td>32 A</td></tr>
<tr><td>Plaque de cuisson</td><td>Triphasé 400 V</td><td>2,5 mm² (5 conducteurs)</td><td>20 A</td></tr>
<tr><td>Four encastrable</td><td>Monophasé 230 V</td><td>2,5 mm²</td><td>20 A</td></tr>
<tr><td>Hotte, micro-ondes, petit électroménager</td><td>Monophasé 230 V</td><td>Circuit prises cuisine 2,5 mm²</td><td>20 A</td></tr>
</tbody></table></div>
<p>Quelques fabricants de plaques ou certaines notices indiquent d'autres calibres pour le raccordement triphasé ou bi-phasé : la notice de l'appareil et la note de calcul du bureau d'études priment sur les tableaux génériques.</p>
<h2>Le raccordement : sortie de câble ou prise</h2>
<ul>
<li><b>Plaque de cuisson</b> : raccordement par une boîte de connexion (sortie de câble) ou une prise 32 A dédiée, placée de manière à rester accessible sous le plan de travail.</li>
<li><b>Four</b> : prise 16 A ou 20 A dédiée, ou sortie de câble selon le modèle. Une prise placée derrière le four doit pouvoir être déconnectée en sortant l'appareil.</li>
<li><b>Différentiel</b> : le circuit plaque de cuisson doit être sous un interrupteur différentiel 30 mA de type A, car les plaques à induction génèrent des courants de fuite que le type AC ne détecte pas correctement.</li>
</ul>
<h2>Les erreurs à éviter</h2>
<ol>
<li><b>Brancher la plaque sur une prise 16 A</b> avec une rallonge ou un adaptateur : risque d'échauffement et de départ de feu.</li>
<li><b>Mettre le four et la plaque sur le même circuit 32 A</b> : chaque appareil doit avoir son circuit, sauf cuisinière tout-en-un.</li>
<li><b>Sous-dimensionner un câble long</b> : si la cuisine est loin du tableau (villa de plain-pied, cuisine d'été près de la piscine), la chute de tension peut imposer une section supérieure.</li>
<li><b>Oublier le triphasé</b> : dans une villa raccordée en triphasé, alimenter la plaque en triphasé répartit mieux la charge entre les phases.</li>
</ol>
<h2>L'avis du bureau d'études</h2>
<p>Dans une villa ou un appartement haut de gamme, la cuisine peut compter une plaque à induction, deux fours, un lave-vaisselle, un réfrigérateur américain et une cave à vin. Le bureau d'études intègre ces puissances au bilan électrique, choisit les sections, répartit les circuits entre les différentiels et vérifie la puissance à souscrire auprès du distributeur. Voir aussi <a href="conseil-circuits-specialises-nf-c-15-100.html">les circuits spécialisés obligatoires</a> et <a href="conseil-section-cable-calibre-disjoncteur.html">le tableau section de câble / calibre</a>.</p>
""",
 "faq": [
  ("Quelle section de câble pour une plaque à induction ?", "En monophasé, la plaque est alimentée en 6 mm² avec un disjoncteur 32 A, sous un différentiel 30 mA de type A ; en triphasé, 2,5 mm² avec un disjoncteur 20 A est la valeur usuelle."),
  ("Quel disjoncteur pour un four électrique ?", "Le four a un circuit dédié, couramment en 2,5 mm² protégé par un disjoncteur 20 A, sauf indication différente de la notice du fabricant."),
  ("Peut-on brancher le four et la plaque sur le même disjoncteur ?", "Non, sauf cuisinière tout-en-un : la NF C 15-100 prévoit un circuit spécialisé pour la plaque et un autre pour le four."),
 ],
 "sources": [
  ("https://www.legrand.fr/questions-frequentes/quel-disjoncteur-installer-pour-proteger-des-plaques-a-induction", "Legrand, disjoncteur pour plaque à induction"),
  ("https://home.nexans.fr/app/uploads/2022/03/Tableau-section-et-calibres.pdf", "Nexans, tableau des sections et calibres NF C 15-100"),
 ],
},
{
 "slug": "conseil-disjoncteur-ou-differentiel-difference",
 "cat": "electricite",
 "title": "Disjoncteur ou interrupteur différentiel : quelles différences ?",
 "crumb": "Disjoncteur ou différentiel",
 "desc": "Le disjoncteur protège les câbles des surcharges et courts-circuits, le différentiel 30 mA protège les personnes des fuites de courant. Rôle de chacun et choix.",
 "lead": "Trois appareils aux noms proches, trois rôles différents dans le tableau électrique. Comprendre la différence permet de lire un devis et de savoir pourquoi un appareil « saute ».",
 "img": "images/services/elec-disjoncteurs.jpg",
 "min": 3,
 "body": """
<p>Le <b>disjoncteur</b> protège les câbles et les appareils contre les surcharges et les courts-circuits. L'<b>interrupteur différentiel</b> protège les personnes : il coupe le courant dès qu'il détecte une fuite vers la terre, par exemple quand quelqu'un touche une partie sous tension. Le <b>disjoncteur différentiel</b> réunit les deux fonctions dans un seul appareil. Dans un tableau de logement, on trouve en général des interrupteurs différentiels 30 mA en tête de rangée et des disjoncteurs divisionnaires en dessous, un par circuit.</p>
<h2>Les trois appareils côte à côte</h2>
<div class="tableau"><table><thead><tr><th>Appareil</th><th>Ce qu'il détecte</th><th>Ce qu'il protège</th><th>Où on le trouve</th></tr></thead><tbody>
<tr><td>Disjoncteur divisionnaire (10, 16, 20, 32 A…)</td><td>Surcharge, court-circuit</td><td>Les câbles d'un circuit</td><td>Un par circuit</td></tr>
<tr><td>Interrupteur différentiel 30 mA</td><td>Courant de fuite à la terre</td><td>Les personnes</td><td>En tête d'un groupe de circuits</td></tr>
<tr><td>Disjoncteur différentiel</td><td>Les deux</td><td>Câbles et personnes</td><td>Disjoncteur de branchement, ou circuit isolé</td></tr>
</tbody></table></div>
<h2>Le disjoncteur : protéger les câbles</h2>
<p>Chaque câble supporte une intensité maximale : 1,5 mm² pour 16 A, 2,5 mm² pour 20 A, 6 mm² pour 32 A, selon les repères de la NF C 15-100. Si l'on branche trop d'appareils, le câble chauffe ; le disjoncteur coupe avant que l'isolant ne se dégrade. En cas de court-circuit, il coupe en quelques millisecondes. Son calibre se choisit donc d'après la section du câble, jamais d'après l'appareil seul (voir <a href="conseil-section-cable-calibre-disjoncteur.html">le tableau section / calibre</a>).</p>
<h2>L'interrupteur différentiel : protéger les personnes</h2>
<p>Il compare le courant qui part par la phase et celui qui revient par le neutre. S'il manque plus de 30 mA, c'est que du courant s'échappe ailleurs, par la terre ou par un corps humain : il coupe. Il ne protège pas contre les surcharges, d'où l'obligation d'avoir des disjoncteurs en aval. Son calibre (25, 40 ou 63 A) indique le courant qu'il peut laisser passer, pas sa sensibilité. Il existe en plusieurs types (AC, A, F) selon les appareils protégés : voir <a href="conseil-differentiel-30ma-type-ac-a-f.html">quel type de différentiel choisir</a>.</p>
<h2>Le disjoncteur de branchement</h2>
<p>En tête de l'installation, après le compteur, se trouve le disjoncteur général. Selon le distributeur et le type de raccordement, il est différentiel (avec une sensibilité de quelques centaines de milliampères, par exemple 500 mA) : il sert alors à la protection générale et coupe tout le logement. Il ne remplace pas les différentiels 30 mA, qui sont seuls à assurer la protection des personnes contre les contacts directs.</p>
<h2>Que faire quand ça saute ?</h2>
<ul>
<li><b>Un disjoncteur divisionnaire saute</b> : surcharge ou court-circuit sur ce circuit. Débranchez les appareils et réarmez ; s'il ressaute à vide, il y a un défaut de câblage.</li>
<li><b>Un interrupteur différentiel saute</b> : fuite de courant sur l'un des circuits qu'il protège, souvent un appareil humide ou une prise extérieure. Abaissez les disjoncteurs un par un pour trouver le circuit fautif.</li>
</ul>
<p>Le bureau d'études fixe le schéma de protection dans le schéma unifilaire : nombre et type de différentiels, calibres des disjoncteurs, sélectivité entre étages de protection. C'est ce document que l'électricien suit et que le bureau de contrôle vérifie.</p>
""",
 "faq": [
  ("Quelle est la différence entre un disjoncteur et un différentiel ?", "Le disjoncteur coupe en cas de surcharge ou de court-circuit pour protéger les câbles ; le différentiel coupe dès qu'une fuite de courant dépasse sa sensibilité (30 mA) pour protéger les personnes."),
  ("Un interrupteur différentiel suffit-il sans disjoncteur ?", "Non, l'interrupteur différentiel ne protège pas contre les surcharges : chaque circuit placé en aval doit avoir son propre disjoncteur adapté à la section du câble."),
  ("Que signifie 40 A sur un interrupteur différentiel 30 mA ?", "40 A est l'intensité maximale qu'il peut laisser passer ; 30 mA est sa sensibilité, c'est-à-dire le courant de fuite à partir duquel il coupe."),
 ],
 "sources": [
  ("https://www.legrand.fr/questions-frequentes/quel-est-le-role-du-differentiel", "Legrand, rôle du différentiel"),
  ("https://izi-by-edf.fr/blog/tableau-electrique-disjoncteur-differentiel/", "IZI by EDF, l'interrupteur différentiel du tableau"),
 ],
},
{
 "slug": "conseil-differentiel-30ma-type-ac-a-f",
 "cat": "electricite",
 "title": "Différentiel 30 mA type AC, A ou F : lequel pour quel circuit ?",
 "crumb": "Différentiel AC, A, F",
 "desc": "Différentiel 30 mA : type AC pour les circuits classiques, type A pour plaque et lave-linge, type F pour clim inverter et pompe à chaleur. Tableau et conseils.",
 "lead": "Tous les interrupteurs différentiels 30 mA ne détectent pas les mêmes fuites. Le bon type dépend des appareils branchés, et la question compte dans une villa marocaine très équipée en climatisation.",
 "img": "images/services/elec-tableau.jpg",
 "min": 3,
 "body": """
<p>Le <b>type AC</b> détecte les fuites de courant alternatif classiques : il convient aux circuits d'éclairage, de prises et de radiateurs simples. Le <b>type A</b> détecte en plus les fuites à composante continue produites par l'électronique : il est exigé par la NF C 15-100 pour la plaque de cuisson, le lave-linge et la borne de recharge de véhicule. Le <b>type F</b> ajoute la détection des courants issus des variateurs de fréquence monophasés : il est recommandé pour les climatiseurs inverter, pompes à chaleur et pompes à vitesse variable.</p>
<h2>Le tableau de choix</h2>
<div class="tableau"><table><thead><tr><th>Type</th><th>Ce qu'il détecte</th><th>Circuits concernés</th></tr></thead><tbody>
<tr><td>AC</td><td>Fuites alternatives sinusoïdales</td><td>Éclairage, prises, chauffe-eau, radiateurs simples</td></tr>
<tr><td>A</td><td>AC + fuites continues pulsées</td><td>Plaque de cuisson, lave-linge, borne de recharge, et tout circuit où l'on veut plus de marge</td></tr>
<tr><td>F</td><td>A + courants à fréquences multiples (variateurs monophasés)</td><td>Climatiseur et pompe à chaleur inverter, pompe de piscine à vitesse variable, congélateur (moins de déclenchements intempestifs)</td></tr>
<tr><td>B</td><td>F + fuites continues lisses</td><td>Équipements triphasés à variateur ou redresseur, certaines bornes de recharge</td></tr>
</tbody></table></div>
<p>Règle simple : un type A peut toujours remplacer un type AC, et un type F un type A, mais jamais l'inverse là où le type supérieur est requis. Le type A coûte en moyenne de l'ordre de 20 % de plus qu'un type AC, selon les fabricants.</p>
<h2>Ce que dit la norme</h2>
<ul>
<li><b>Dans l'édition 2002 amendée de la NF C 15-100</b>, encore très appliquée : tous les circuits sont protégés par des différentiels 30 mA, et au moins un interrupteur différentiel de type A protège la plaque de cuisson et le lave-linge.</li>
<li><b>Dans l'édition 2024</b>, en vigueur en France depuis septembre 2025, les fabricants indiquent que le type F est demandé en tête des circuits alimentant des équipements à variateur de vitesse monophasé. Le détail dépend du texte appliqué : à confirmer par le bureau de contrôle pour votre projet.</li>
<li><b>Au Maroc</b>, la série de normes NM 06.1.100 à 06.1.106 encadre les installations basse tension ; dans les CPS, la NF C 15-100 reste la référence la plus citée.</li>
</ul>
<h2>Le cas des villas climatisées à Marrakech</h2>
<p>Une villa peut compter six à dix unités de climatisation inverter, une pompe de piscine à vitesse variable et un surpresseur. Toutes ces machines produisent des courants de fuite que le type AC détecte mal : soit il ne coupe pas quand il le faudrait, soit il saute sans raison apparente. Regrouper ces équipements sous un ou plusieurs différentiels de type F, en limitant le nombre d'appareils par différentiel, réduit les déclenchements intempestifs en plein été. Le congélateur gagne aussi à être sur un différentiel séparé (type F ou « haute immunité ») pour éviter de perdre son contenu après une coupure inaperçue.</p>
<h2>Bien répartir les différentiels</h2>
<p>Le choix du type va de pair avec la répartition des circuits : combien de différentiels, quels circuits sous chacun. Voir <a href="conseil-nombre-interrupteurs-differentiels-maison.html">le nombre d'interrupteurs différentiels selon la surface</a> et <a href="conseil-disjoncteur-ou-differentiel-difference.html">la différence entre disjoncteur et différentiel</a>. Dans un projet suivi par un bureau d'études, ce choix figure sur le schéma unifilaire, ce qui évite les substitutions par du matériel moins cher sur le chantier.</p>
""",
 "faq": [
  ("Quel différentiel pour un lave-linge ?", "Le lave-linge doit être placé en aval d'un interrupteur différentiel 30 mA de type A, comme la plaque de cuisson, selon la NF C 15-100."),
  ("Quel différentiel pour une climatisation inverter ?", "Les fabricants recommandent un différentiel 30 mA de type F pour les climatiseurs et pompes à chaleur inverter monophasés, car il détecte les courants produits par leur variateur de vitesse."),
  ("Peut-on remplacer un différentiel type AC par un type A ?", "Oui, un type A assure toutes les fonctions du type AC et davantage ; l'inverse est interdit là où le type A est exigé."),
 ],
 "sources": [
  ("https://www.legrand.fr/questions-frequentes/que-doit-on-brancher-sur-un-interrupteur-differentiel-de-type-a", "Legrand, que brancher sur un différentiel de type A"),
  ("https://izi-by-edf.fr/blog/interrupteur-differentiel-climatisation", "IZI by EDF, quel interrupteur pour une climatisation"),
  ("https://viox.com/fr/rccb-type-ac-vs-a-vs-f-vs-b/", "VIOX, différentiels type AC, A, F et B"),
 ],
},
{
 "slug": "conseil-nombre-interrupteurs-differentiels-maison",
 "cat": "electricite",
 "title": "Combien d'interrupteurs différentiels selon la surface du logement ?",
 "crumb": "Nombre de différentiels",
 "desc": "Nombre d'interrupteurs différentiels 30 mA : 2 jusqu'à 35 m², 3 de 35 à 100 m², 4 au-delà selon la NF C 15-100 2002, dont un type A. Calibres et répartition.",
 "lead": "Le nombre d'interrupteurs différentiels dépend de la surface du logement et du nombre de circuits. Voici le tableau de référence et la façon de répartir les circuits dans une villa.",
 "img": "images/services/ele1.jpg",
 "min": 3,
 "body": """
<p>Selon le tableau de la NF C 15-100 (édition 2002 amendée, encore très appliquée), un logement de <b>35 m² ou moins</b> compte au minimum <b>2 interrupteurs différentiels 30 mA</b>, un logement de <b>35 à 100 m²</b> en compte <b>3</b>, et un logement de <b>plus de 100 m²</b> en compte <b>4</b>, dont à chaque fois un de type A pour la plaque de cuisson et le lave-linge. Pour une villa, ce minimum est presque toujours dépassé, car c'est le nombre de circuits qui commande.</p>
<h2>Le tableau de référence</h2>
<div class="tableau"><table><thead><tr><th>Surface du logement</th><th>Interrupteurs différentiels type AC</th><th>Interrupteur différentiel type A</th></tr></thead><tbody>
<tr><td>35 m² ou moins</td><td>1 × 25 A</td><td>1 × 40 A</td></tr>
<tr><td>De 35 à 100 m²</td><td>2 × 40 A</td><td>1 × 40 A</td></tr>
<tr><td>Plus de 100 m²</td><td>3 × 40 A</td><td>1 × 40 A</td></tr>
</tbody></table></div>
<p>Ces valeurs sont des minimums pour un logement courant. L'édition 2024 de la norme a réorganisé ces règles : selon l'édition appliquée à votre projet, le bureau d'études ou le bureau de contrôle précise les exigences exactes, notamment sur les types A et F.</p>
<h2>Pourquoi plusieurs différentiels</h2>
<ul>
<li><b>Ne pas tout couper</b> : si un seul différentiel protège toute la maison, une fuite sur une prise de jardin plonge la villa dans le noir.</li>
<li><b>Limiter le cumul des fuites</b> : chaque appareil laisse fuir quelques milliampères. Trop d'appareils sous un même 30 mA provoquent des déclenchements intempestifs.</li>
<li><b>Répartir éclairage et prises</b> : on place les circuits d'éclairage d'une même zone sous des différentiels différents de ceux des prises, pour garder de la lumière en cas de défaut.</li>
</ul>
<p>Les fabricants conseillent de ne pas dépasser environ 8 circuits par interrupteur différentiel. Dans une villa très équipée (climatisation, informatique, éclairage LED avec alimentations électroniques), il est prudent de rester en dessous, car chaque équipement électronique ajoute un petit courant de fuite permanent.</p>
<h2>Exemple pour une villa de 250 m² à Marrakech</h2>
<ol>
<li><b>Différentiel type A n° 1</b> : plaque de cuisson, lave-linge, lave-vaisselle.</li>
<li><b>Différentiels type F</b> (un ou deux) : climatiseurs inverter, pompe de piscine à vitesse variable.</li>
<li><b>Différentiels type AC ou A</b> (trois ou quatre) : éclairage et prises, répartis par niveau ou par zone (jour, nuit, extérieur).</li>
<li><b>Différentiel séparé</b> pour le congélateur et, si besoin, pour le réseau informatique et la vidéosurveillance.</li>
</ol>
<p>On arrive ainsi souvent à 6 ou 8 différentiels, bien au-delà du minimum de 4. En triphasé, les différentiels sont aussi utilisés pour équilibrer la charge entre les trois phases.</p>
<h2>Le rôle du bureau d'études</h2>
<p>Le bureau d'études compte les circuits, choisit le type et le calibre de chaque différentiel, vérifie que la somme des circuits en aval reste compatible avec son calibre et prévoit la réserve dans le tableau (voir <a href="conseil-tableau-electrique-gtl-maison.html">tableau électrique et GTL</a>). Pour le choix du type, lisez <a href="conseil-differentiel-30ma-type-ac-a-f.html">différentiel 30 mA type AC, A ou F</a>.</p>
""",
 "faq": [
  ("Combien de différentiels pour une maison de 120 m² ?", "Le tableau de la NF C 15-100 (édition 2002) prévoit au minimum 4 interrupteurs différentiels 30 mA au-delà de 100 m² : trois de type AC en 40 A et un de type A en 40 A."),
  ("Combien de circuits sous un interrupteur différentiel ?", "Les fabricants conseillent d'environ 8 circuits au maximum par interrupteur différentiel, pour limiter le cumul des courants de fuite et les déclenchements intempestifs."),
  ("Faut-il obligatoirement un différentiel de type A ?", "Oui, au moins un interrupteur différentiel 30 mA de type A est exigé pour protéger la plaque de cuisson et le lave-linge."),
 ],
 "sources": [
  ("https://www.forumconstruire.com/guides/guide-norme-electricite/choisir-differentiels-disjoncteurs.php", "Forumconstruire, guide : choisir différentiels et disjoncteurs"),
  ("https://www.legrand.fr/questions-frequentes/quel-interrupteur-differentiel-choisir-pour-son-tableau-electrique", "Legrand, quel interrupteur différentiel choisir"),
 ],
},
{
 "slug": "conseil-section-cable-calibre-disjoncteur",
 "cat": "electricite",
 "title": "Section de câble et calibre de disjoncteur : le tableau de référence",
 "crumb": "Section et calibre",
 "desc": "Tableau section / calibre NF C 15-100 : 1,5 mm² en 16 A, 2,5 mm² en 20 A, 4 mm² en 25 A, 6 mm² en 32 A, 10 mm² en 40 A. Cas des longues distances et des villas.",
 "lead": "Le calibre du disjoncteur se choisit d'après la section du câble qu'il protège. Voici le tableau usuel des installations domestiques, et les cas où il faut aller plus loin qu'un tableau.",
 "img": "images/services/elec-disjoncteurs.jpg",
 "min": 3,
 "body": """
<p>Dans une installation domestique en cuivre, les repères de la NF C 15-100 sont les suivants : <b>1,5 mm² protégé par un disjoncteur 16 A</b>, <b>2,5 mm² par 20 A</b>, <b>4 mm² par 25 A</b>, <b>6 mm² par 32 A</b> et <b>10 mm² par 40 A</b> pour certains circuits de forte puissance. Le principe est simple : le disjoncteur doit couper avant que le câble ne chauffe, donc son calibre ne doit jamais dépasser ce que la section admet.</p>
<h2>Le tableau usuel (cuivre, logement)</h2>
<div class="tableau"><table><thead><tr><th>Section</th><th>Disjoncteur maximal</th><th>Usages courants</th></tr></thead><tbody>
<tr><td>1,5 mm²</td><td>16 A (10 A ou 16 A pour l'éclairage)</td><td>Éclairage (8 points maximum), prises (8 socles maximum), volets roulants</td></tr>
<tr><td>2,5 mm²</td><td>20 A</td><td>Prises (12 socles maximum), four, lave-linge, lave-vaisselle, sèche-linge, chauffe-eau, plaque en triphasé</td></tr>
<tr><td>4 mm²</td><td>25 A</td><td>Alimentation d'un tableau divisionnaire, appareils de 4 à 5 kW</td></tr>
<tr><td>6 mm²</td><td>32 A</td><td>Plaque de cuisson ou cuisinière en monophasé, tableau divisionnaire</td></tr>
<tr><td>10 mm²</td><td>40 A</td><td>Gros appareils de chauffage, alimentation d'un tableau divisionnaire</td></tr>
</tbody></table></div>
<p>Ces correspondances sont celles du tableau de la NF C 15-100 repris par les fabricants de câbles. Elles valent pour des longueurs courantes et des modes de pose habituels (conduits encastrés). Elles ne remplacent pas un calcul quand les conditions s'écartent de ces hypothèses.</p>
<h2>Quand le tableau ne suffit plus</h2>
<ul>
<li><b>Grande longueur</b> : sur une villa étendue, un abri de piscine ou un portail à 60 m du tableau, la chute de tension peut imposer une section supérieure à celle du tableau.</li>
<li><b>Température ambiante élevée</b> : un câble posé en toiture-terrasse ou dans des combles qui dépassent 50 °C l'été à Marrakech transporte moins de courant qu'à 30 °C ; on applique alors des coefficients de correction.</li>
<li><b>Câbles groupés</b> : plusieurs câbles serrés dans un même fourreau ou chemin de câbles chauffent davantage ; la section doit être corrigée.</li>
<li><b>Alimentation générale et colonnes</b> : le câble entre le compteur et le tableau, ou les colonnes d'un immeuble, se calculent toujours selon la puissance souscrite et la longueur.</li>
</ul>
<h2>Les erreurs fréquentes</h2>
<ol>
<li><b>Remplacer un disjoncteur 16 A par un 20 A</b> parce qu'il « saute » : si le câble est en 1,5 mm², il n'est plus protégé.</li>
<li><b>Mélanger les sections sur un même circuit</b> : un tronçon en 1,5 mm² sur un circuit 20 A devient le maillon faible.</li>
<li><b>Utiliser du câble de qualité douteuse</b> : une section réelle inférieure à la section affichée fausse tout le calcul. Exigez du câble conforme aux normes marocaines et contrôlé.</li>
</ol>
<h2>Le rôle du bureau d'études</h2>
<p>Pour une villa, un immeuble ou un local commercial, le bureau d'études calcule chaque ligne : intensité d'emploi, mode de pose, température, longueur, chute de tension et pouvoir de coupure. Le résultat figure dans la note de calcul et sur le schéma unifilaire. Voir aussi <a href="conseil-combien-prises-par-circuit.html">combien de prises par circuit</a> et <a href="conseil-four-plaque-cuisson-cable-disjoncteur.html">le câble du four et de la plaque</a>.</p>
""",
 "faq": [
  ("Quel disjoncteur pour du câble 2,5 mm² ?", "Un câble cuivre de 2,5 mm² se protège par un disjoncteur de 20 A au maximum selon les repères de la NF C 15-100."),
  ("Quelle section de câble pour un disjoncteur 32 A ?", "Un disjoncteur 32 A protège un câble cuivre de 6 mm², par exemple pour une plaque de cuisson en monophasé."),
  ("Peut-on mettre un disjoncteur 20 A sur du 1,5 mm² ?", "Non, le 1,5 mm² se protège au maximum par un disjoncteur 16 A ; un 20 A laisserait le câble chauffer sans couper."),
 ],
 "sources": [
  ("https://home.nexans.fr/app/uploads/2022/03/Tableau-section-et-calibres.pdf", "Nexans, tableau des sections et calibres NF C 15-100"),
  ("https://www.123elec.com/norme-conducteur-disjoncteur", "123elec, quel disjoncteur selon le conducteur"),
 ],
},
{
 "slug": "conseil-mise-a-la-terre-maison-maroc",
 "cat": "electricite",
 "title": "Mise à la terre d'une maison : piquet, fond de fouille, résistance",
 "crumb": "Mise à la terre",
 "desc": "Mise à la terre d'une maison au Maroc : boucle à fond de fouille en cuivre nu 25 mm², piquets, conducteur de terre 16 ou 25 mm², résistance visée et contrôle.",
 "lead": "La prise de terre évacue les courants de défaut et permet aux différentiels de jouer leur rôle. La meilleure solution se décide au moment des fondations.",
 "img": "images/villa-technique.jpg",
 "min": 3,
 "body": """
<p>Pour une maison neuve, la meilleure prise de terre est une <b>boucle à fond de fouille</b> : un câble de <b>cuivre nu d'au moins 25 mm²</b> posé au fond des tranchées de fondation, sur tout le pourtour du bâtiment, avant le coulage du béton. Elle est reliée au tableau par un <b>conducteur de terre</b> (16 mm² cuivre s'il est isolé et protégé, 25 mm² s'il est nu). En rénovation, on utilise des piquets de terre enfoncés dans le sol. La résistance obtenue doit être mesurée et rester compatible avec les dispositifs différentiels.</p>
<h2>Les solutions de prise de terre</h2>
<div class="tableau"><table><thead><tr><th>Solution</th><th>Quand</th><th>Points clés</th></tr></thead><tbody>
<tr><td>Boucle à fond de fouille</td><td>Construction neuve, au moment des fondations</td><td>Cuivre nu 25 mm² minimum, en contact avec la terre, sous le béton de propreté ou en fond de tranchée, deux extrémités accessibles pour le contrôle</td></tr>
<tr><td>Piquets de terre</td><td>Rénovation, complément</td><td>Piquet vertical, généralement de 1,5 à 2 m ; plusieurs piquets espacés reliés entre eux si la résistance est trop élevée</td></tr>
<tr><td>Ceinture ou conducteur en tranchée</td><td>Terrain rocheux, extension</td><td>Câble enterré dans une tranchée dédiée, autour du bâtiment</td></tr>
</tbody></table></div>
<h2>Quelle valeur de résistance viser ?</h2>
<p>La règle de protection est que la tension de contact en cas de défaut reste inférieure à 50 V. La valeur maximale admissible dépend donc de la sensibilité du différentiel en tête de l'installation : avec un dispositif de 500 mA, on obtient 100 Ω, la valeur souvent citée comme limite. Avec des différentiels plus sensibles, la limite théorique est plus large, mais une bonne pratique est de viser une valeur nettement plus basse, quelques dizaines d'ohms. Une boucle à fond de fouille bien réalisée donne généralement des valeurs faibles.</p>
<p>À Marrakech, les sols secs et caillouteux en été peuvent faire grimper la résistance des piquets. Mesurez en saison sèche et prévoyez plusieurs piquets si nécessaire.</p>
<h2>Du sol jusqu'aux prises</h2>
<ol>
<li><b>La prise de terre</b> (boucle ou piquets).</li>
<li><b>Le conducteur de terre</b> jusqu'à la barrette de mesure (sectionnable, pour mesurer la résistance).</li>
<li><b>La borne principale de terre</b> du tableau, d'où partent les conducteurs de protection vert-jaune de chaque circuit.</li>
<li><b>La liaison équipotentielle principale</b> qui relie les canalisations métalliques et les structures, voir <a href="conseil-liaison-equipotentielle-principale-lep.html">la LEP</a>.</li>
</ol>
<p>Le schéma de liaison à la terre (en général TT pour les logements raccordés au réseau basse tension) est à confirmer auprès du distributeur (Radeema à Marrakech, ONEE ou autre régie selon la ville).</p>
<h2>Coordonner avec le gros œuvre</h2>
<p>La boucle à fond de fouille doit être posée par l'électricien ou le maçon au bon moment : une fois le béton coulé, il est trop tard. Le bureau d'études l'inscrit dans les plans et le CPS, et vérifie sa pose lors des visites de chantier, avant coulage. Une mesure de résistance est faite à la réception. Sur un immeuble, la boucle est complétée par les liaisons aux armatures et aux colonnes de terre. Voir aussi <a href="conseil-role-bureau-etudes-techniques.html">le rôle du bureau d'études</a>.</p>
""",
 "faq": [
  ("Quelle section pour une boucle à fond de fouille ?", "La boucle à fond de fouille est réalisée en cuivre nu d'au moins 25 mm², posée en contact avec la terre au fond des fondations."),
  ("Quelle résistance de terre faut-il obtenir ?", "Avec un différentiel de 500 mA en tête d'installation, 100 Ω est la limite souvent citée ; en pratique on vise beaucoup moins, quelques dizaines d'ohms au plus."),
  ("Peut-on faire une prise de terre après la construction ?", "Oui, avec un ou plusieurs piquets de terre reliés entre eux ; la boucle à fond de fouille, plus performante, ne peut être posée qu'au moment des fondations."),
 ],
 "sources": [
  ("https://izi-by-edf.fr/blog/prise-terre-fond-fouille", "IZI by EDF, réaliser une prise de terre en fond de fouille"),
  ("https://izi-by-edf.fr/blog/electricite-mise-a-la-terre-c-est-quoi", "IZI by EDF, mise à la terre : normes et méthode"),
 ],
},
{
 "slug": "conseil-liaison-equipotentielle-principale-lep",
 "cat": "electricite",
 "title": "Liaison équipotentielle principale (LEP) : rôle et réalisation",
 "crumb": "Liaison équipotentielle principale",
 "desc": "La LEP relie à la terre les canalisations métalliques d'eau, de gaz et les structures. Section cuivre de 6 mm² minimum et 25 mm² au plus, raccordement.",
 "lead": "La liaison équipotentielle principale met au même potentiel toutes les masses métalliques qui entrent dans le bâtiment. Un fil discret, mais indispensable à la sécurité.",
 "img": "images/services/ele2.jpg",
 "min": 3,
 "body": """
<p>La <b>liaison équipotentielle principale (LEP)</b> relie à la borne principale de terre toutes les canalisations et structures métalliques qui entrent dans le bâtiment : arrivée d'eau, gaz, chauffage, gaines métalliques, éléments de structure accessibles. Son but est d'éviter qu'une différence de tension dangereuse apparaisse entre deux parties métalliques que l'on peut toucher en même temps, par exemple un robinet et une carcasse d'appareil en défaut.</p>
<h2>Ce qu'il faut relier</h2>
<ul>
<li><b>Les canalisations métalliques d'eau</b> à leur entrée dans le bâtiment (après le compteur).</li>
<li><b>La canalisation de gaz</b> si elle est métallique (réseau de ville ou tuyauterie depuis un local de bouteilles).</li>
<li><b>Les canalisations de chauffage et d'eau chaude</b> métalliques.</li>
<li><b>Les éléments métalliques de structure</b> accessibles et les gaines ou conduits métalliques.</li>
<li><b>Dans un immeuble</b> : les armatures du béton lorsqu'elles sont accessibles, les colonnes montantes métalliques, les gaines de ventilation.</li>
</ul>
<p>Avec des réseaux en PER, multicouche ou PPR, très répandus aujourd'hui, la LEP concerne surtout les tronçons métalliques (entrée d'eau en cuivre ou en acier galvanisé, raccords et nourrices).</p>
<h2>Section des conducteurs</h2>
<div class="tableau"><table><thead><tr><th>Conducteur</th><th>Section usuelle (cuivre)</th></tr></thead><tbody>
<tr><td>Liaison équipotentielle principale</td><td>La moitié de la section du plus gros conducteur de protection de l'installation, avec un minimum de 6 mm² et sans dépasser 25 mm²</td></tr>
<tr><td>Conducteur de terre (prise de terre vers barrette)</td><td>16 mm² isolé et protégé, 25 mm² nu</td></tr>
<tr><td>Conducteurs de protection des circuits</td><td>Même section que les conducteurs actifs du circuit</td></tr>
</tbody></table></div>
<p>Exemple : avec un conducteur principal de protection de 16 mm², la LEP est réalisée en 10 mm². Pour une maison courante, 6 mm² est la valeur la plus fréquente. Le conducteur est vert-jaune, fixé par des colliers de mise à la terre adaptés à chaque tuyau.</p>
<h2>Comment la réaliser</h2>
<ol>
<li>Prévoir une <b>borne principale de terre</b> (ou barrette) près du tableau ou dans la gaine technique.</li>
<li>Poser un collier sur chaque canalisation métallique, au plus près de son entrée dans le bâtiment.</li>
<li>Relier chaque collier à la borne principale par un conducteur vert-jaune de section adaptée, sans le couper en route.</li>
<li>Repérer les liaisons et les laisser accessibles pour la vérification.</li>
</ol>
<h2>LEP et LES : ne pas confondre</h2>
<p>La LEP est générale et part de la borne principale de terre. La <b>liaison équipotentielle supplémentaire</b> (LES) est locale : elle concerne surtout la salle de bain, voir <a href="conseil-liaison-equipotentielle-supplementaire-les-salle-de-bain.html">la LES en salle de bain</a>. Les deux complètent la prise de terre décrite dans <a href="conseil-mise-a-la-terre-maison-maroc.html">la mise à la terre d'une maison</a>.</p>
<p>Le bureau d'études indique la LEP sur les plans d'électricité et de plomberie, ce qui permet de la coordonner entre les deux corps d'état. C'est un point que le bureau de contrôle vérifie systématiquement avant la mise sous tension. En rénovation, l'absence de LEP est l'un des défauts les plus fréquents dans les maisons anciennes : sa mise en place est peu coûteuse et améliore nettement la sécurité, à condition que la prise de terre elle-même soit correcte.</p>
""",
 "faq": [
  ("Quelle section pour la liaison équipotentielle principale ?", "La LEP fait la moitié de la section du plus gros conducteur de protection de l'installation, avec un minimum de 6 mm² et un maximum de 25 mm² en cuivre."),
  ("Faut-il relier les tuyaux en PER à la terre ?", "Non, les tuyaux en matière synthétique ne sont pas conducteurs ; la liaison équipotentielle concerne les parties métalliques, comme l'entrée d'eau en cuivre ou en acier."),
  ("Où se raccorde la liaison équipotentielle principale ?", "Elle part de la borne principale de terre, près du tableau ou dans la gaine technique, à laquelle sont aussi reliés le conducteur de terre et les conducteurs de protection."),
 ],
 "sources": [
  ("https://izi-by-edf.fr/blog/liaison-equipotentielle-obligatoire", "IZI by EDF, liaison équipotentielle : installation et obligation"),
  ("https://www.futura-sciences.com/maison/definitions/maison-liaison-equipotentielle-10752/", "Futura, définition de la liaison équipotentielle"),
 ],
},
{
 "slug": "conseil-liaison-equipotentielle-supplementaire-les-salle-de-bain",
 "cat": "electricite",
 "title": "Liaison équipotentielle supplémentaire (LES) en salle de bain",
 "crumb": "LES salle de bain",
 "desc": "La LES relie les éléments métalliques de la salle de bain (tuyaux, baignoire, receveur) : vert-jaune 2,5 mm² protégé ou 4 mm² non protégé. Quand la prévoir.",
 "lead": "Dans la salle de bain, l'eau et le corps mouillé rendent un choc électrique beaucoup plus dangereux. La liaison équipotentielle supplémentaire met au même potentiel tout ce qui est métallique dans la pièce.",
 "img": "images/services/ele1.jpg",
 "min": 3,
 "body": """
<p>La <b>liaison équipotentielle supplémentaire (LES)</b> est un conducteur vert-jaune qui relie entre eux, et au conducteur de protection, tous les éléments métalliques accessibles de la salle de bain : canalisations d'eau métalliques, baignoire ou receveur métallique, bonde métallique, huisseries métalliques. Elle se réalise couramment en <b>2,5 mm² si le conducteur est protégé mécaniquement</b> (sous conduit, encastré) et en <b>4 mm² s'il ne l'est pas</b>. Son but : qu'aucune tension dangereuse ne puisse apparaître entre deux éléments que l'on touche en même temps, les mains et les pieds mouillés.</p>
<h2>Les éléments à relier</h2>
<ul>
<li><b>Canalisations métalliques</b> d'eau froide, d'eau chaude et de vidange.</li>
<li><b>Baignoire ou receveur métallique</b> (acier émaillé, fonte) : une patte de raccordement est souvent prévue sous l'appareil.</li>
<li><b>Huisseries et éléments de structure métalliques</b> accessibles dans la pièce.</li>
<li><b>Les masses des appareils de classe I</b> (radiateur sèche-serviettes, chauffe-eau) via leur conducteur de protection.</li>
</ul>
<p>Les baignoires et receveurs en acrylique ou en céramique, les tuyaux en PER ou multicouche ne sont pas conducteurs et n'ont pas à être reliés.</p>
<h2>Est-elle toujours obligatoire ?</h2>
<p>La LES a longtemps été systématique dans les salles d'eau. L'amendement 5 de la NF C 15-100 (2015) a précisé les cas où elle peut être réalisée autrement, ou ne plus être nécessaire, notamment lorsque l'installation est équipée d'une liaison équipotentielle principale et que les circuits sont protégés par un différentiel 30 mA, sous conditions. Ces conditions sont précises et varient selon l'édition de la norme appliquée : en pratique, dans une construction neuve au Maroc avec des réseaux partiellement métalliques, la réaliser reste la solution la plus sûre, et le bureau de contrôle tranche en cas de doute.</p>
<h2>Comment la réaliser</h2>
<ol>
<li>Poser un collier de mise à la terre sur chaque canalisation métallique et sur la patte de la baignoire ou du receveur.</li>
<li>Relier ces points entre eux par un conducteur vert-jaune continu, sans dominos intermédiaires inaccessibles.</li>
<li>Raccorder la liaison au conducteur de protection d'un circuit de la salle de bain (borne de terre d'un appareil ou boîte de connexion) ou à la barrette de terre du tableau si celui-ci est proche.</li>
<li>Laisser les connexions visibles ou accessibles pour la vérification par le bureau de contrôle.</li>
</ol>
<h2>Dans un riad ou une rénovation</h2>
<p>Dans les riads et maisons anciennes de la médina, on trouve encore des canalisations en acier galvanisé ou en cuivre noyées dans les murs, et parfois aucune prise de terre. Avant de refaire la salle de bain, il faut vérifier la mise à la terre de toute l'installation (voir <a href="conseil-mise-a-la-terre-maison-maroc.html">la mise à la terre</a>) et la présence de différentiels 30 mA. La LES ne sert à rien si le conducteur de protection n'est relié à aucune terre.</p>
<p>Le bureau d'études intègre la LES dans les plans de la salle de bain, avec le respect des <a href="conseil-volumes-salle-de-bain-electricite.html">volumes 0, 1 et 2</a>, et coordonne le plombier et l'électricien pour que les colliers soient posés avant la fermeture des murs et des gaines.</p>
""",
 "faq": [
  ("Quelle section pour la liaison équipotentielle de la salle de bain ?", "On utilise couramment un conducteur vert-jaune de 2,5 mm² s'il est protégé mécaniquement, sous conduit ou encastré, et de 4 mm² s'il ne l'est pas."),
  ("Faut-il relier une baignoire acrylique à la terre ?", "Non, une baignoire ou un receveur en acrylique ou en céramique n'est pas conducteur ; seuls les éléments métalliques accessibles sont reliés."),
  ("La LES est-elle encore obligatoire ?", "Depuis l'amendement 5 de 2015, la NF C 15-100 admet des cas où elle n'est plus nécessaire, sous conditions précises ; à défaut de certitude, la réaliser reste la solution la plus sûre."),
 ],
 "sources": [
  ("https://www.ffbatiment.fr/techniques-batiment/equipements-techniques/electricite-courant-fort-courant-faible/dossier-bam/la-norme-nf-c-15-100-demeure-la-reference", "FFB, sécurité électrique dans la salle d'eau"),
  ("https://izi-by-edf.fr/blog/liaison-equipotentielle-obligatoire", "IZI by EDF, liaison équipotentielle : obligation"),
 ],
},
{
 "slug": "conseil-volumes-salle-de-bain-electricite",
 "cat": "electricite",
 "title": "Volumes 0, 1, 2 de la salle de bain : que peut-on installer ?",
 "crumb": "Volumes de la salle de bain",
 "desc": "Volumes de salle de bain : volume 0 limité à la TBTS 12 V IPX7, TBTS en volume 1, classe II IPX4 en volume 2 (60 cm, 2,25 m de haut). Prises et chauffe-eau.",
 "lead": "La NF C 15-100 découpe la salle de bain en volumes autour de la baignoire et de la douche. Plus on est près de l'eau, plus les règles sont strictes.",
 "img": "images/services/elec-prises.jpg",
 "min": 3,
 "body": """
<p>La salle de bain est découpée en trois volumes : le <b>volume 0</b> (l'intérieur de la baignoire ou du receveur), où presque rien n'est admis sauf un éclairage en très basse tension de sécurité 12 V étanche IPX7 ; le <b>volume 1</b> (au-dessus, jusqu'à 2,25 m de hauteur), limité à la TBTS 12 V et à certains chauffe-eau ; le <b>volume 2</b> (une bande de 60 cm autour du volume 1, jusqu'à 2,25 m), où l'on admet des luminaires et appareils de classe II, IPX4 minimum. Au-delà, on est <b>hors volume</b> et les prises de courant sont possibles.</p>
<h2>Ce qui est admis dans chaque volume</h2>
<div class="tableau"><table><thead><tr><th>Volume</th><th>Étendue</th><th>Ce qui est admis</th></tr></thead><tbody>
<tr><td>Volume 0</td><td>Intérieur de la baignoire ou du receveur</td><td>Uniquement du matériel TBTS 12 V, IPX7 (éclairage immergeable)</td></tr>
<tr><td>Volume 1</td><td>Au-dessus du volume 0, jusqu'à 2,25 m du sol</td><td>Matériel TBTS 12 V (IPX4 au moins, IPX5 en cas de jets) ; chauffe-eau électrique sous conditions</td></tr>
<tr><td>Volume 2</td><td>60 cm autour du volume 1, jusqu'à 2,25 m</td><td>Luminaires et appareils de classe II, IPX4 minimum ; prise rasoir avec transformateur de séparation</td></tr>
<tr><td>Hors volume</td><td>Le reste de la pièce</td><td>Prises de courant 16 A, lave-linge, interrupteurs, appareils de classe I reliés à la terre</td></tr>
</tbody></table></div>
<p>Tous les circuits de la salle de bain sont protégés par un différentiel 30 mA. Les interrupteurs sont interdits dans les volumes 0 et 1.</p>
<h2>Les cas pratiques</h2>
<ul>
<li><b>Douche à l'italienne</b> sans paroi fixe : le volume 1 n'est plus limité par le receveur : il s'étend sur un rayon de 1,20 m autour de la pomme de douche fixe, selon les règles de l'édition 2002 amendée. Prévoyez donc les prises et interrupteurs plus loin qu'avec un receveur classique.</li>
<li><b>Meuble vasque avec prise</b> : la prise doit être hors volume, ou se limiter à une prise rasoir dans le volume 2.</li>
<li><b>Lave-linge dans la salle de bain</b> : hors volume uniquement.</li>
<li><b>Sèche-serviettes</b> : classe II en volume 2, ou hors volume.</li>
<li><b>Chauffe-eau électrique</b> : de préférence hors volume ; en volume 1, uniquement un appareil horizontal placé le plus haut possible, selon les conditions de la norme.</li>
</ul>
<h2>Une paroi fixe change tout</h2>
<p>Une paroi fixe, une cloison ou un plafond limitent les volumes : derrière une paroi pleine, on peut se retrouver hors volume. C'est souvent la solution pour installer une prise près d'une baignoire dans une petite salle de bain. Le volume sous la baignoire, fermé par un tablier démontable avec un outil, a aussi ses propres règles (IPX4 pour les équipements qui y sont admis).</p>
<h2>Riads, hammams et suites d'hôtel</h2>
<p>Dans les riads et maisons d'hôtes de Marrakech, les salles de bain en tadelakt, les douches ouvertes et les hammams privés posent des cas particuliers : éclairages d'ambiance au sol, miroirs lumineux, hammam avec générateur de vapeur. Un hammam relève de règles spécifiques. Le bureau d'études trace les volumes sur le plan de chaque salle d'eau, choisit les indices de protection et coordonne avec la <a href="conseil-liaison-equipotentielle-supplementaire-les-salle-de-bain.html">liaison équipotentielle supplémentaire</a>. Les dimensions citées ici sont celles de l'édition 2002 amendée de la NF C 15-100 ; l'édition 2024 doit être vérifiée pour les projets qui l'appliquent.</p>
""",
 "faq": [
  ("Peut-on mettre une prise électrique dans une salle de bain ?", "Oui, hors volume, c'est-à-dire à plus de 60 cm de la baignoire ou de la douche (ou derrière une paroi fixe) ; en volume 2, seule une prise rasoir avec transformateur de séparation est admise."),
  ("Quelle est la largeur du volume 2 ?", "Le volume 2 forme une bande de 60 cm autour du volume 1, jusqu'à 2,25 m de hauteur, selon les règles de la NF C 15-100 édition 2002 amendée."),
  ("Quel éclairage dans une douche ?", "Dans le volume 0, seul un éclairage TBTS 12 V étanche IPX7 est admis ; au-dessus, dans le volume 1, un éclairage TBTS 12 V avec au moins IPX4, IPX5 en cas de jets."),
 ],
 "sources": [
  ("https://www.se.com/fr/fr/work/support/local/reglementation/norme-nfc15-100/salle-de-bain/", "Schneider Electric, NF C 15-100 dans la salle de bain"),
  ("https://sti.eduscol.education.fr/sites/eduscol.education.fr.sti/files/ressources/pedagogiques/9930/9930-salle-de-bain-nfc-15100-2018-05-22.pdf", "Eduscol, fiche salle de bain NF C 15-100"),
  ("https://izi-by-edf.fr/blog/nfc-15-100-salle-de-bain", "IZI by EDF, la NF C 15-100 pour une salle de bain"),
 ],
},
{
 "slug": "conseil-tableau-electrique-gtl-maison",
 "cat": "electricite",
 "title": "Tableau électrique et GTL : emplacement, nombre de rangées, réserve",
 "crumb": "Tableau électrique et GTL",
 "desc": "Tableau électrique : organes de manœuvre entre 0,90 et 1,80 m, 20 % de réserve, GTL de 600 mm de large au-delà de 35 m². Où le placer dans une villa.",
 "lead": "Le tableau électrique et la gaine technique logement (GTL) regroupent l'arrivée d'énergie et les protections. Leur emplacement et leur taille se décident sur plan, pas sur chantier.",
 "img": "images/services/elec-tableau.jpg",
 "min": 3,
 "body": """
<p>Le tableau électrique doit être placé <b>à l'intérieur du logement</b> ou dans un local annexe directement accessible, avec ses organes de manœuvre <b>entre 0,90 m et 1,80 m du sol</b> (tableau sans porte), et garder <b>au moins 20 % d'emplacements libres</b> pour les ajouts futurs. Selon la NF C 15-100, il est intégré à une <b>gaine technique logement (GTL)</b>, colonne qui regroupe aussi le coffret de communication et les arrivées de réseaux : 600 mm de large dans un logement de plus de 35 m², 450 mm en dessous.</p>
<h2>Les repères à retenir</h2>
<div class="tableau"><table><thead><tr><th>Élément</th><th>Repère usuel (NF C 15-100)</th></tr></thead><tbody>
<tr><td>Hauteur des organes de manœuvre</td><td>Entre 0,90 m et 1,80 m du sol ; avec une porte, entre 0,50 m et 1,80 m</td></tr>
<tr><td>Réserve</td><td>20 % d'emplacements libres au minimum en maison individuelle, sans rangée vide</td></tr>
<tr><td>GTL, logement de plus de 35 m²</td><td>600 mm de large, 200 mm de profondeur environ</td></tr>
<tr><td>GTL, logement de 35 m² ou moins</td><td>450 mm de large, 150 mm de profondeur environ</td></tr>
<tr><td>Emplacement</td><td>Dans le logement ou un local annexe directement accessible, en général près de l'entrée ou du garage</td></tr>
</tbody></table></div>
<p>Pour un logement adapté aux personnes à mobilité réduite, la plage de hauteur est plus basse (Legrand cite 0,75 m à 1,30 m pour l'organe de coupure). Ces valeurs sont celles de l'édition 2002 amendée ; l'édition 2024 doit être vérifiée pour les projets qui l'appliquent.</p>
<h2>Combien de rangées ?</h2>
<p>Le nombre de rangées découle du nombre de circuits : chaque disjoncteur divisionnaire occupe en général un module, chaque interrupteur différentiel deux ou quatre modules, et une rangée standard compte 13 ou 18 modules. Pour une villa de 200 à 300 m², avec 25 à 40 circuits, 6 à 8 différentiels, un parafoudre et des contacteurs, il faut couramment un tableau de 4 rangées, voire un tableau principal et des tableaux divisionnaires par niveau ou pour la piscine. Ajoutez 20 % de réserve et l'espace de câblage : un tableau trop petit devient vite impossible à faire évoluer.</p>
<h2>Où le placer dans une villa ?</h2>
<ul>
<li><b>Près de l'entrée ou du garage</b>, accessible sans traverser une chambre, et non dans une salle de bain ou au-dessus d'un évier.</li>
<li><b>À l'abri de la chaleur</b> : à Marrakech, un tableau dans un local non ventilé exposé plein ouest peut dépasser 40 °C l'été, ce qui fait chauffer les appareils et provoque des déclenchements.</li>
<li><b>Proche du centre de gravité des charges</b> pour limiter la longueur des câbles et la chute de tension, en particulier vers la cuisine et les groupes de climatisation.</li>
<li><b>Dans un riad</b> : prévoir un local technique ventilé et un tableau divisionnaire par étage plutôt que des dizaines de câbles qui traversent les murs anciens.</li>
</ul>
<h2>Ce que contient la GTL</h2>
<ol>
<li>Le disjoncteur de branchement et le tableau de répartition.</li>
<li>Le coffret de communication (téléphone, fibre, RJ45, télévision).</li>
<li>Les arrivées des réseaux en provenance du compteur (Radeema, ONEE ou autre distributeur).</li>
<li>Des prises de courant pour alimenter la box et les équipements du coffret.</li>
</ol>
<p>Le bureau d'études dessine le tableau sur le schéma unifilaire, compte les modules et place la GTL sur les plans d'architecte dès la conception, pour éviter de la caser après coup dans un placard trop étroit. Voir aussi <a href="conseil-nombre-interrupteurs-differentiels-maison.html">le nombre de différentiels</a> et <a href="conseil-circuits-specialises-nf-c-15-100.html">les circuits spécialisés</a>.</p>
""",
 "faq": [
  ("À quelle hauteur installer un tableau électrique ?", "Selon la NF C 15-100, les organes de manœuvre d'un tableau sans porte se situent entre 0,90 m et 1,80 m du sol ; avec une porte, la plage va de 0,50 m à 1,80 m."),
  ("Quelle réserve laisser dans un tableau électrique ?", "Au moins 20 % d'emplacements libres en maison individuelle, sans laisser de rangée entièrement vide, pour pouvoir ajouter des circuits plus tard."),
  ("Quelle largeur pour une GTL ?", "600 mm de large et environ 200 mm de profondeur pour un logement de plus de 35 m², 450 mm de large pour un logement de 35 m² ou moins."),
 ],
 "sources": [
  ("https://izi-by-edf.fr/blog/tableau-electrique-a-quelle-hauteur-installer", "IZI by EDF, à quelle hauteur installer un tableau électrique"),
  ("https://www.legrand.fr/questions-frequentes/quelle-hauteur-pour-un-tableau-electrique", "Legrand, quelle hauteur pour un tableau électrique"),
  ("https://eduscol.education.fr/sti/sites/eduscol.education.fr.sti/files/ressources/pedagogiques/9930/9930-etel-et-gtl-2018-05-15.pdf", "Eduscol, fiche ETEL et GTL"),
 ],
},
{
 "slug": "conseil-nombre-prises-par-piece",
 "cat": "electricite",
 "title": "Nombre minimal de prises et de points lumineux par pièce (NF C 15-100)",
 "crumb": "Prises par pièce",
 "desc": "Prises par pièce selon la NF C 15-100 : séjour 5 minimum (7 au-delà de 28 m²), chambre 3, cuisine 6 dont 4 au plan de travail, un point lumineux par pièce.",
 "lead": "La norme fixe un minimum de prises et de points lumineux par pièce. Ce sont des planchers, pas des objectifs : dans une villa, on prévoit presque toujours davantage.",
 "img": "images/services/ele2.jpg",
 "min": 3,
 "body": """
<p>Selon les règles de la NF C 15-100 (édition 2002 amendée, encore très appliquée), il faut au minimum <b>5 prises dans un séjour de moins de 28 m²</b> (7 au-delà selon la plupart des guides), <b>3 prises par chambre</b> et <b>6 prises dans une cuisine de plus de 4 m²</b>, dont 4 au-dessus du plan de travail. Chaque pièce principale reçoit en outre au moins un point d'éclairage, en plafond ou en applique commandée. Ces minimums ne comptent pas les prises des circuits spécialisés (four, lave-linge, lave-vaisselle).</p>
<h2>Le tableau par pièce</h2>
<div class="tableau"><table><thead><tr><th>Pièce</th><th>Prises 16 A minimum</th><th>Éclairage</th></tr></thead><tbody>
<tr><td>Séjour de moins de 28 m²</td><td>5</td><td>Au moins un point lumineux</td></tr>
<tr><td>Séjour de 28 m² et plus</td><td>7 (certains guides de fabricants indiquent davantage)</td><td>Au moins un point lumineux</td></tr>
<tr><td>Chambre</td><td>3</td><td>Au moins un point lumineux</td></tr>
<tr><td>Cuisine de plus de 4 m²</td><td>6, dont 4 au-dessus du plan de travail</td><td>Au moins un point lumineux</td></tr>
<tr><td>Cuisine de 4 m² ou moins</td><td>3</td><td>Au moins un point lumineux</td></tr>
<tr><td>Salle de bain</td><td>Hors volumes uniquement</td><td>Au moins un point lumineux, selon les volumes</td></tr>
</tbody></table></div>
<p>Pour les circuits, rappelons qu'un circuit d'éclairage en 1,5 mm² alimente au maximum 8 points lumineux, et un circuit de prises 12 socles au maximum en 2,5 mm² (voir <a href="conseil-combien-prises-par-circuit.html">combien de prises par circuit</a>).</p>
<h2>Ce que l'on prévoit vraiment dans une villa</h2>
<ul>
<li><b>Séjour</b> : 8 à 12 prises, dont des prises près de la télévision, du canapé et des points de charge ; prises de sol si le séjour est grand et ouvert.</li>
<li><b>Chambres</b> : 2 prises de chaque côté du lit (lampes, chargeurs), une près du bureau, une pour le climatiseur s'il n'est pas sur circuit dédié.</li>
<li><b>Cuisine</b> : au-delà des 4 prises du plan de travail, des prises pour le réfrigérateur, la hotte, le micro-ondes et les petits appareils, plus les circuits spécialisés.</li>
<li><b>Extérieur</b> : prises étanches en terrasse, au jardin et près de la piscine, sur un circuit dédié protégé par un différentiel 30 mA.</li>
<li><b>Couloirs et dégagements</b> : une prise pour l'aspirateur, éclairage commandé de plusieurs endroits (va-et-vient ou télérupteur).</li>
</ul>
<h2>Hauteurs et emplacements</h2>
<p>Les prises sont posées à une hauteur suffisante au-dessus du sol fini (en pratique au moins 5 cm pour une prise 16 A), et les prises du plan de travail ne se placent pas au-dessus de l'évier ni des plaques de cuisson. Pensez aux interrupteurs à l'entrée de chaque pièce, côté ouverture de porte.</p>
<h2>Faire le plan avant les saignées</h2>
<p>Le plus économique est de placer prises, interrupteurs et points lumineux sur le plan d'aménagement, meubles compris, avant le début des travaux. Le bureau d'études établit ce plan d'implantation, regroupe les points en circuits et vérifie la cohérence avec le tableau. Pour le cadre réglementaire au Maroc, voir <a href="conseil-norme-electrique-nf-c-15-100-maroc.html">la NF C 15-100 et les normes marocaines</a>.</p>
""",
 "faq": [
  ("Combien de prises dans une chambre ?", "La NF C 15-100 impose au minimum 3 prises de courant par chambre, quelle que soit sa surface ; en pratique on en prévoit souvent 5 ou 6."),
  ("Combien de prises dans un séjour ?", "Au moins 5 prises dans un séjour de moins de 28 m², et 7 au-delà selon la plupart des guides de la NF C 15-100."),
  ("Combien de prises dans une cuisine ?", "Au moins 6 prises dans une cuisine de plus de 4 m², dont 4 au-dessus du plan de travail, sans compter les prises des circuits spécialisés."),
 ],
 "sources": [
  ("https://www.legrand.fr/questions-frequentes/quelle-est-la-norme-nf-c-15-100-pour-les-prises-de-courant", "Legrand, la NF C 15-100 pour les prises de courant"),
  ("https://selectra.info/energie/actualites/marche/prises-obligatoires-norme-nf-c-15-100", "Selectra, prises obligatoires NF C 15-100"),
  ("https://izi-by-edf.fr/blog/nfc-15-100-cuisine", "IZI by EDF, la NF C 15-100 pour une cuisine"),
 ],
},
]
