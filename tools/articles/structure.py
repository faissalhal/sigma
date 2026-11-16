# -*- coding: utf-8 -*-
# Articles « Conseils » : lot structure (SIGMA ICC)

ARTICLES = [
{
 "slug": "conseil-type-fondation-semelle-radier",
 "cat": "structure",
 "title": "Quel type de fondation choisir : semelles, radier ou pieux ?",
 "crumb": "Type de fondation",
 "desc": "Semelles isolées ou filantes, radier général ou pieux : comment l'étude de sol et les charges du bâtiment décident du type de fondation d'une maison au Maroc.",
 "lead": "Le type de fondation ne se choisit pas sur catalogue : il découle de la portance du sol, de la profondeur du bon sol et des charges de votre bâtiment.",
 "img": "images/projects/project1.jpg",
 "min": 5,
 "body": """
<p>Pour une villa ou un petit immeuble posé sur un sol correct, les <b>semelles</b> (isolées sous les poteaux, filantes sous les murs) reliées par des longrines restent la solution la plus courante et la plus économique. Le <b>radier</b> devient intéressant quand le sol est faible ou hétérogène, et les <b>pieux</b> quand le bon sol se trouve trop profond. C'est l'étude de sol qui tranche, puis l'ingénieur structure qui dimensionne.</p>
<h2>Les trois grandes familles</h2>
<div class="tableau"><table><thead><tr><th>Fondation</th><th>Principe</th><th>Cas typique</th></tr></thead><tbody>
<tr><td>Semelles isolées et filantes</td><td>Fondation superficielle : chaque poteau ou mur repose sur une semelle élargie en béton armé</td><td>Sol porteur à faible profondeur, charges modérées (villa R+1, R+2)</td></tr>
<tr><td>Radier général</td><td>Dalle épaisse en béton armé sous toute l'emprise, qui répartit les charges</td><td>Sol de faible portance, risque de tassements différentiels, sous-sol avec eau</td></tr>
<tr><td>Pieux ou micropieux</td><td>Fondation profonde qui va chercher un sol résistant en profondeur</td><td>Remblais épais, sol compressible, charges importantes, reprise en sous-œuvre</td></tr>
</tbody></table></div>
<h2>Ce que l'étude de sol doit vous donner</h2>
<p>Le rapport géotechnique fournit les données qui conditionnent le choix :</p>
<ul>
<li><b>La contrainte admissible du sol</b> (en bars ou en MPa) et la profondeur à laquelle elle est atteinte.</li>
<li><b>Les risques de tassement</b>, en particulier les tassements différentiels entre deux parties du bâtiment, à l'origine de nombreuses fissures.</li>
<li><b>La présence d'eau</b> (nappe, infiltrations), d'argiles gonflantes, de remblais ou de cavités.</li>
<li><b>Une recommandation de type de fondation</b> et de niveau d'assise.</li>
</ul>
<p>Sans ces informations, l'ingénieur doit faire des hypothèses prudentes, ce qui coûte souvent plus cher en béton et en acier que l'étude elle-même. Voir notre article sur le <a href="conseil-etude-de-sol-maroc-prix.html">prix d'une étude de sol au Maroc</a>.</p>
<h2>Quand passer des semelles au radier ?</h2>
<p>Quand les semelles calculées deviennent si grandes qu'elles se touchent presque, ou qu'elles couvriraient une grande partie de l'emprise du bâtiment, un radier devient souvent plus simple et pas forcément plus cher. Le radier est aussi privilégié lorsqu'il faut limiter les tassements différentiels ou réaliser un sous-sol étanche. À l'inverse, sur un bon sol, un radier sous une villa légère est généralement surdimensionné.</p>
<h2>Les exigences parasismiques</h2>
<p>Au Maroc, le règlement parasismique RPS 2000 version 2011 s'applique aussi aux fondations : les semelles isolées doivent être solidarisées par des longrines pour éviter qu'elles ne se déplacent les unes par rapport aux autres lors d'un séisme. Un même bloc de bâtiment doit en principe reposer sur un seul type de fondation et à un niveau cohérent, sauf justification. Pour en savoir plus, consultez notre article sur le <a href="conseil-reglement-parasismique-rps-2011-maroc.html">règlement parasismique RPS 2011</a>.</p>
<h2>Le rôle du bureau d'études</h2>
<p>Le bureau d'études croise le rapport de sol, la descente de charges du bâtiment et les exigences du RPS pour choisir la fondation et en établir les plans de coffrage et de ferraillage. Sur le chantier, il vérifie que le fond de fouille correspond bien au sol décrit par le géotechnicien avant le coulage du béton de propreté : c'est le moment où une mauvaise surprise coûte le moins cher.</p>
""",
 "faq": [
  ("Quelle fondation pour une villa R+1 au Maroc ?", "Sur un sol de bonne portance, des semelles isolées sous poteaux et filantes sous murs, reliées par des longrines, suffisent généralement. Le choix définitif dépend de l'étude de sol et du calcul de l'ingénieur."),
  ("Un radier est-il plus solide que des semelles ?", "Pas forcément : le radier est adapté aux sols faibles ou aux sous-sols, mais sur un bon sol des semelles bien dimensionnées sont aussi sûres et plus économiques."),
  ("Quand faut-il des pieux ?", "Quand le sol résistant se trouve trop profond pour des fondations superficielles, par exemple sous des remblais épais ou des sols compressibles. C'est l'étude géotechnique qui le détermine."),
 ],
 "sources": [
  ("https://educnet-rec.enpc.fr/pluginfile.php/129256/mod_resource/content/0/enpc_fondations_SH.pdf", "École des Ponts, cours fondations superficielles"),
  ("https://www.techniques-ingenieur.fr/base-documentaire/construction-et-travaux-publics-th3/calcul-et-suivi-d-ouvrages-geotechniques-42219210/fondations-profondes-c248/", "Techniques de l'Ingénieur, fondations profondes"),
 ],
},
{
 "slug": "conseil-semelle-isolee-filante-dimension",
 "cat": "structure",
 "title": "Dimensions d'une semelle isolée ou filante : comment les calculer",
 "crumb": "Dimensions des semelles",
 "desc": "Surface d'une semelle = charge / contrainte admissible du sol : 30 t sur un sol à 2 bars donnent environ 1,25 × 1,25 m. Hauteur, béton de propreté, erreurs.",
 "lead": "La taille d'une semelle découle d'un calcul simple dans son principe : la charge qu'elle reçoit divisée par ce que le sol peut supporter. Le reste est affaire de ferraillage et de détails.",
 "img": "images/services/maison-beton.jpg",
 "min": 5,
 "body": """
<p>La surface d'une semelle se calcule en divisant la charge transmise par le poteau ou le mur par la <b>contrainte admissible du sol</b> donnée par l'étude géotechnique. Il n'existe donc pas de « dimension standard » : une même villa peut nécessiter des semelles de 1 m de côté sur un sol rocheux et de près de 2 m sur un sol médiocre.</p>
<h2>Le principe du calcul</h2>
<p>Prenons un poteau qui descend 300 kN (environ 30 tonnes) sur un sol dont la contrainte admissible est de 2 bars (0,2 MPa, soit 200 kN/m²) :</p>
<ul>
<li><b>Surface nécessaire</b> : 300 / 200 = 1,5 m².</li>
<li><b>Semelle carrée</b> : racine de 1,5 ≈ 1,22 m, arrondie à 1,25 × 1,25 m.</li>
<li><b>Sur un sol à 1 bar</b>, la même charge demanderait 3 m², soit environ 1,75 × 1,75 m.</li>
</ul>
<p>Pour une semelle filante, le raisonnement est le même par mètre linéaire de mur : la charge par mètre divisée par la contrainte admissible donne la largeur. L'ingénieur y ajoute le poids propre de la semelle et des terres, et les combinaisons d'actions, dont le séisme selon le RPS 2000 version 2011.</p>
<h2>La hauteur de la semelle</h2>
<p>Une semelle doit être assez épaisse pour transmettre l'effort du poteau à toute sa surface sans se rompre. Dans la méthode classique dite « des bielles » du BAEL, la hauteur utile est au moins égale au quart du débord, c'est-à-dire (B - b) / 4, B étant la largeur de la semelle et b celle du poteau. Avec une semelle de 1,25 m sous un poteau de 25 cm, cela donne au moins 25 cm de hauteur utile, auxquels s'ajoute l'enrobage. Les valeurs exactes et le ferraillage (nappe inférieure dans les deux sens, attentes du poteau) sont <b>à déterminer par l'ingénieur</b>.</p>
<h2>Les points à respecter sur le chantier</h2>
<ul>
<li><b>Le niveau d'assise</b> indiqué par l'étude de sol : on descend jusqu'au bon sol, même s'il est plus profond que prévu.</li>
<li><b>Le béton de propreté</b>, une couche de quelques centimètres de béton maigre qui protège le fond de fouille et permet de caler les armatures.</li>
<li><b>L'enrobage</b> des aciers, plus important pour un béton coulé contre la terre (voir <a href="conseil-enrobage-armatures-beton.html">l'enrobage des armatures</a>).</li>
<li><b>Les longrines</b> qui relient les semelles entre elles, exigées par le règlement parasismique.</li>
<li><b>Le centrage</b> du poteau sur la semelle : une semelle excentrée (en limite de propriété par exemple) se calcule différemment.</li>
</ul>
<h2>Les erreurs fréquentes</h2>
<p>Reprendre les dimensions des semelles d'un voisin, réduire leur taille pour économiser du béton, ou poser une semelle sur un remblai non compacté sont les causes classiques de tassements et de <a href="conseil-fissures-maison-causes-gravite.html">fissures</a>. Une semelle sous-dimensionnée ne se rattrape qu'au prix d'une reprise en sous-œuvre coûteuse.</p>
<h2>Le rôle du bureau d'études</h2>
<p>Le bureau d'études établit la descente de charges poteau par poteau, dimensionne chaque semelle en fonction du sol réel et fournit un plan de fondations coté et ferraillé. Il contrôle ensuite le fond de fouille et le ferraillage avant coulage.</p>
""",
 "faq": [
  ("Comment calculer la surface d'une semelle ?", "On divise la charge transmise par le poteau par la contrainte admissible du sol : 300 kN sur un sol à 2 bars (200 kN/m²) demandent 1,5 m², soit une semelle d'environ 1,25 × 1,25 m."),
  ("Quelle épaisseur pour une semelle isolée ?", "Selon la méthode des bielles, la hauteur utile vaut au moins le quart du débord, (B - b) / 4. La valeur exacte et le ferraillage sont fixés par l'ingénieur."),
  ("Peut-on faire des semelles sans étude de sol ?", "C'est déconseillé : sans contrainte admissible mesurée, l'ingénieur doit prendre une hypothèse prudente, et une erreur sur le sol est la première cause de tassements."),
 ],
 "sources": [
  ("https://educnet-rec.enpc.fr/pluginfile.php/129256/mod_resource/content/0/enpc_fondations_SH.pdf", "École des Ponts, cours fondations superficielles"),
 ],
},
{
 "slug": "conseil-longrines-role-dimension",
 "cat": "structure",
 "title": "Longrines : à quoi servent-elles et comment les dimensionner ?",
 "crumb": "Longrines",
 "desc": "Les longrines relient les semelles pour éviter leurs déplacements en cas de séisme et portent les murs du rez-de-chaussée. Rôle, RPS 2011, section, ferraillage.",
 "lead": "Invisibles une fois le dallage coulé, les longrines sont pourtant un élément clé de la tenue parasismique d'une maison : elles empêchent les fondations de bouger chacune de leur côté.",
 "img": "images/projects/project2.jpg",
 "min": 4,
 "body": """
<p>Une longrine est une poutre en béton armé qui relie les semelles entre elles au niveau des fondations. Elle a deux rôles : <b>solidariser les fondations</b> pour qu'elles se déplacent ensemble en cas de séisme ou de tassement, et souvent <b>porter les murs</b> du rez-de-chaussée. Au Maroc, le règlement parasismique RPS 2000 version 2011 impose de lier les semelles isolées.</p>
<h2>Pourquoi les longrines sont indispensables en zone sismique</h2>
<p>Lors d'un séisme, le sol ne bouge pas partout de la même façon. Des semelles isolées non reliées peuvent se rapprocher ou s'écarter, ce qui arrache les poteaux à leur base. La longrine travaille alors comme un <b>tirant</b> (en traction) ou une <b>butée</b> (en compression) entre les appuis. Elle limite aussi les effets des tassements différentiels, en répartissant mieux les charges entre fondations voisines.</p>
<h2>Les deux types de longrines</h2>
<ul>
<li><b>Longrine de liaison</b> : elle relie les semelles et porte peu de charge. Sa section reste modeste et son ferraillage est symétrique (haut et bas), car elle peut être tendue ou comprimée.</li>
<li><b>Longrine porteuse</b> : elle reçoit le poids d'un mur ou d'une cloison lourde et travaille aussi en flexion. Elle est calculée comme une poutre posée sur les semelles.</li>
</ul>
<h2>Quelle section et quel ferraillage ?</h2>
<p>La section d'une longrine dépend de la portée entre semelles, des charges de murs et de l'effort sismique à transmettre. Les règlements parasismiques fixent un effort minimal de liaison et des sections minimales ; ces valeurs varient selon les textes (RPS marocain, RPA algérien, Eurocode 8) et ne doivent pas être reprises d'un pays à l'autre. Sur une villa, les longrines courantes ont des sections de l'ordre de quelques dizaines de centimètres de côté, avec des cadres réguliers, mais <b>la section exacte est à déterminer par l'ingénieur</b> à partir de la note de calcul.</p>
<div class="tableau"><table><thead><tr><th>Point de contrôle</th><th>Ce qu'il faut vérifier</th></tr></thead><tbody>
<tr><td>Continuité</td><td>Aciers ancrés dans les semelles ou les poteaux, recouvrements suffisants</td></tr>
<tr><td>Ferraillage</td><td>Barres hautes et basses conformes au plan, cadres à l'espacement prévu</td></tr>
<tr><td>Assise</td><td>Longrine coulée sur béton de propreté ou sol compacté, jamais sur remblai meuble</td></tr>
<tr><td>Enrobage</td><td>Cales en place, béton coulé contre terre avec enrobage renforcé</td></tr>
</tbody></table></div>
<h2>Longrines et dallage</h2>
<p>Le dallage du rez-de-chaussée ne remplace pas les longrines, sauf si l'ingénieur a conçu une dalle portée ou un radier qui joue ce rôle. Un dallage posé sur hérisson est un ouvrage indépendant, qui peut fissurer sans compromettre la structure. Les longrines servent aussi d'appui aux murs de façade et limitent les remontées d'humidité lorsqu'une coupure de capillarité est prévue au-dessus (voir <a href="conseil-remontees-capillaires-murs.html">remontées capillaires</a>).</p>
<h2>Le rôle du bureau d'études</h2>
<p>Le bureau d'études dessine le plan de fondations avec toutes les longrines, leurs sections et leurs ferraillages, conformément au RPS 2011. Lors des visites, il vérifie que les longrines ne sont pas supprimées ou réduites par économie, une pratique encore fréquente sur les petits chantiers et lourde de conséquences en cas de séisme.</p>
""",
 "faq": [
  ("Les longrines sont-elles obligatoires au Maroc ?", "Le règlement parasismique RPS 2000 version 2011 impose de relier les semelles isolées entre elles ; les longrines sont la solution habituelle pour le faire."),
  ("Quelle est la différence entre longrine et semelle filante ?", "La semelle filante transmet directement la charge d'un mur au sol, tandis que la longrine est une poutre qui relie des semelles et peut porter un mur entre deux appuis."),
  ("Quelle section pour une longrine ?", "Elle dépend de la portée, des murs portés et de l'effort sismique : la section et le ferraillage sont fixés par l'ingénieur dans les plans de fondations."),
 ],
 "sources": [
  ("https://www.preventionweb.net/files/21648_13356rps20021.pdf?startDownload=true", "Ministère de l'Habitat, règlement parasismique RPS 2000"),
  ("https://lechantier.ma/en/blog/normes-parasismiques-rps-maroc", "Le Chantier, normes parasismiques RPS au Maroc"),
 ],
},
{
 "slug": "conseil-chainage-horizontal-vertical",
 "cat": "structure",
 "title": "Chaînages horizontaux et verticaux : rôle et règles au Maroc",
 "crumb": "Chaînages",
 "desc": "Chaînages verticaux aux angles, horizontaux à chaque plancher : rôle parasismique et règles du RPS (4 T10, 3 cm², hauteur 15 cm, 5 m au plus entre chaînages).",
 "lead": "Les chaînages ceinturent les murs de maçonnerie et les relient aux planchers. Dans une région sismique comme celle de Marrakech, ils font la différence entre un mur qui fissure et un mur qui s'effondre.",
 "img": "images/services/3.jpg",
 "min": 5,
 "body": """
<p>Un chaînage est un élément en béton armé intégré à la maçonnerie : <b>horizontal</b> au niveau de chaque plancher et en tête de mur, <b>vertical</b> aux angles, aux intersections de murs et aux bords des grandes ouvertures. Ensemble, ils forment une cage qui empêche les murs de se disloquer sous l'effet d'un séisme ou de tassements.</p>
<h2>Pourquoi les chaînages sont essentiels</h2>
<p>Une maçonnerie de briques ou de parpaings résiste bien à la compression, mais très mal à la traction et au cisaillement. Lors d'un séisme, les murs non chaînés se séparent aux angles et basculent. Le séisme d'Al Haouz en 2023 a montré l'écart entre les constructions chaînées et les maçonneries traditionnelles sans chaînage. Les chaînages servent aussi à transmettre les efforts des planchers aux murs et à limiter les fissures dues au retrait ou aux dilatations.</p>
<h2>Les règles de la maçonnerie chaînée du RPS</h2>
<p>Le règlement parasismique marocain consacre un chapitre aux constructions en maçonnerie chaînée. Le texte du RPS 2000 prévoit notamment les dispositions suivantes, à vérifier dans la version 2011 appliquée à votre projet :</p>
<div class="tableau"><table><thead><tr><th>Élément</th><th>Disposition du RPS 2000</th></tr></thead><tbody>
<tr><td>Chaînages verticaux d'extrémité</td><td>Au moins 4 barres T10, avec des cadres espacés de 10 cm</td></tr>
<tr><td>Chaînages horizontaux</td><td>Section d'acier minimale de 3 cm²</td></tr>
<tr><td>Section de béton</td><td>Hauteur minimale de 15 cm pour les chaînages verticaux et horizontaux</td></tr>
<tr><td>Espacement</td><td>5 m au maximum entre deux chaînages verticaux</td></tr>
</tbody></table></div>
<p>Certains documents de présentation du RPS 2011 citent d'autres valeurs minimales ; en cas de doute, c'est le texte officiel et la note de calcul du bureau d'études qui font foi.</p>
<h2>Où placer les chaînages</h2>
<ul>
<li><b>Horizontaux</b> : à chaque niveau de plancher, en tête des murs (acrotères compris) et, sur les murs hauts, à mi-hauteur si le calcul l'exige.</li>
<li><b>Verticaux</b> : à tous les angles, aux jonctions de murs, de part et d'autre des grandes baies, et à intervalles réguliers sur les longs murs.</li>
<li><b>Encadrements</b> : les ouvertures importantes sont bordées de raidisseurs en béton armé.</li>
</ul>
<h2>Les erreurs à éviter</h2>
<ul>
<li>Chaînages horizontaux interrompus aux angles, sans retour ni recouvrement des barres.</li>
<li>Chaînages verticaux non ancrés dans les longrines en bas ou dans le chaînage haut.</li>
<li>Cadres trop espacés ou fermés sans crochets, aciers posés directement contre la brique sans enrobage.</li>
<li>Maçonnerie montée sans liaison avec les chaînages coulés ensuite.</li>
</ul>
<h2>Chaînages et ossature poteaux-poutres</h2>
<p>Dans une villa en ossature béton armé (poteaux, poutres, planchers), les murs de remplissage ne sont pas porteurs, mais ils doivent être tenus pour ne pas s'effondrer : les règles de chaînage ou de raidissage s'appliquent aussi aux grands panneaux. Le bureau d'études précise sur ses plans quel système structurel est retenu et où placer les raidisseurs. Voir aussi notre article sur le <a href="conseil-reglement-parasismique-rps-2011-maroc.html">RPS 2011</a>. Lors des visites de chantier, il vérifie la continuité des chaînages aux angles et leur ancrage dans les longrines et les planchers.</p>
""",
 "faq": [
  ("Quel ferraillage pour un chaînage vertical ?", "Le RPS 2000 prévoit au moins 4 barres T10 avec des cadres espacés de 10 cm pour les chaînages verticaux d'extrémité en maçonnerie chaînée ; l'ingénieur peut demander davantage."),
  ("Tous les combien de mètres faut-il un chaînage vertical ?", "Le RPS 2000 limite à 5 m la distance entre deux chaînages verticaux, en plus de ceux placés aux angles et aux intersections de murs."),
  ("Un chaînage horizontal est-il obligatoire à chaque étage ?", "Oui, en maçonnerie chaînée un chaînage horizontal ceinture les murs au niveau de chaque plancher et en tête de mur, pour relier murs et planchers."),
 ],
 "sources": [
  ("https://www.preventionweb.net/files/21648_13356rps20021.pdf?startDownload=true", "Ministère de l'Habitat, règlement parasismique RPS 2000"),
  ("https://www.abc-maconnerie.com/technologie/mise-oeuvre/construction-parasismique/chainages.html", "ABC Maçonnerie, les chaînages en construction parasismique"),
 ],
},
{
 "slug": "conseil-poteau-section-minimale-rps",
 "cat": "structure",
 "title": "Section minimale d'un poteau en béton armé selon le RPS",
 "crumb": "Section des poteaux",
 "desc": "Au Maroc, le RPS fixe une dimension minimale de 25 cm pour un poteau (30 cm en ductilité ND3). Ferraillage, cadres resserrés aux extrémités et erreurs à éviter.",
 "lead": "Le poteau de 20 × 20 cm encore vu sur certains chantiers ne respecte pas le règlement parasismique. Voici ce que le RPS impose et ce qui reste à calculer.",
 "img": "images/services/beton-poutre.jpg",
 "min": 5,
 "body": """
<p>Selon le règlement parasismique marocain (RPS 2000, version 2011), la plus petite dimension d'un poteau en béton armé doit être d'au moins <b>25 cm</b> pour les niveaux de ductilité ND1 et ND2, et d'au moins <b>30 cm</b> pour le niveau ND3. Un poteau de 20 × 20 cm n'est donc pas conforme, quelle que soit la charge qu'il porte.</p>
<h2>Ce que fixe le règlement</h2>
<div class="tableau"><table><thead><tr><th>Exigence</th><th>Valeur ou principe</th></tr></thead><tbody>
<tr><td>Plus petite dimension (ND1, ND2)</td><td>25 cm minimum</td></tr>
<tr><td>Plus petite dimension (ND3)</td><td>30 cm minimum</td></tr>
<tr><td>Élancement</td><td>Limité : un poteau trop haut par rapport à sa largeur doit être élargi</td></tr>
<tr><td>Zones critiques</td><td>Cadres resserrés aux extrémités du poteau, en pied et en tête</td></tr>
<tr><td>Armatures transversales</td><td>Diamètre minimal de 6 mm, cadres fermés</td></tr>
</tbody></table></div>
<p>Le niveau de ductilité (ND1 à ND3) dépend de la zone sismique, de la classe du bâtiment et du système structurel retenus par l'ingénieur ; c'est lui qui l'indique dans la note de calcul.</p>
<h2>Le ferraillage : à calculer, pas à copier</h2>
<p>Le nombre et le diamètre des barres longitudinales dépendent des efforts calculés (charges verticales et séisme). Le règlement impose des pourcentages minimal et maximal d'acier, et des cadres plus serrés dans les zones critiques, près des planchers, là où se forment les rotules plastiques lors d'un séisme. Dans ces zones, l'espacement des cadres est limité à une valeur de l'ordre de la plus petite des trois grandeurs : 8 fois le diamètre des barres longitudinales, le quart de la plus petite dimension du poteau, et 15 cm. L'espacement exact et la longueur des zones critiques sont <b>à déterminer par l'ingénieur</b>.</p>
<h2>Les erreurs observées sur chantier</h2>
<ul>
<li><b>Poteaux de 20 cm</b> pour « gagner de la place » dans les murs : non conformes au RPS.</li>
<li><b>Cadres espacés de 20 à 25 cm</b> sur toute la hauteur, sans resserrement aux extrémités.</li>
<li><b>Cadres non fermés</b> ou mal crochetés, qui s'ouvrent lors d'un séisme.</li>
<li><b>Recouvrements des barres</b> tous au même niveau, juste au-dessus du plancher, dans la zone la plus sollicitée.</li>
<li><b>Poteaux courts</b> créés par une allège ou un mur partiel : ils concentrent les efforts et cèdent en premier.</li>
<li><b>Nœuds poteau-poutre</b> sans cadres, car difficiles à ferrailler.</li>
</ul>
<h2>Poteau intérieur, d'angle ou de façade</h2>
<p>Un poteau d'angle ou de façade ne porte pas la même charge qu'un poteau central, mais il subit davantage de flexion. Les poteaux d'une même file peuvent donc avoir des ferraillages différents. Sur un plan de structure sérieux, chaque poteau porte une référence et un ferraillage précis. Pour comprendre le contexte réglementaire, lisez notre article sur le <a href="conseil-reglement-parasismique-rps-2011-maroc.html">RPS 2011</a>.</p>
<h2>Le rôle du bureau d'études</h2>
<p>Le bureau d'études calcule les efforts dans chaque poteau, fixe sa section et son ferraillage, et dessine les détails de cadres dans les zones critiques. Le <a href="conseil-controle-ferraillage-avant-coulage.html">contrôle du ferraillage avant coulage</a> permet de vérifier que ces dispositions sont réellement en place avant qu'il ne soit trop tard.</p>
""",
 "faq": [
  ("Quelle est la section minimale d'un poteau au Maroc ?", "Le RPS 2000 version 2011 impose une plus petite dimension d'au moins 25 cm pour les niveaux de ductilité ND1 et ND2, et 30 cm pour le niveau ND3."),
  ("Un poteau de 20 × 20 cm est-il autorisé ?", "Non : il est en dessous de la dimension minimale de 25 cm fixée par le règlement parasismique marocain pour les poteaux en béton armé."),
  ("Pourquoi resserrer les cadres en haut et en bas des poteaux ?", "Ce sont les zones critiques où se concentrent les efforts lors d'un séisme : des cadres rapprochés confinent le béton et empêchent les barres de flamber."),
 ],
 "sources": [
  ("https://www.preventionweb.net/files/21648_13356rps20021.pdf?startDownload=true", "Ministère de l'Habitat, règlement parasismique RPS 2000"),
  ("https://lechantier.ma/en/blog/normes-parasismiques-rps-maroc", "Le Chantier, normes parasismiques RPS au Maroc"),
 ],
},
{
 "slug": "conseil-plancher-hourdis-ou-dalle-pleine",
 "cat": "structure",
 "title": "Plancher hourdis ou dalle pleine : lequel choisir pour votre maison ?",
 "crumb": "Hourdis ou dalle pleine",
 "desc": "Plancher à poutrelles et hourdis (16+4, 20+5) ou dalle pleine en béton armé : portées, poids, acoustique, coût et cas où chaque solution s'impose au Maroc.",
 "lead": "Le plancher à corps creux est la solution la plus répandue au Maroc pour les villas, mais la dalle pleine reste indispensable dans certains cas. Les critères pour trancher.",
 "img": "images/projects/project3.jpg",
 "min": 5,
 "body": """
<p>Pour une villa avec des portées courantes (jusqu'à 5 m environ), le <b>plancher à poutrelles et hourdis</b> est généralement le plus économique et le plus rapide à mettre en œuvre. La <b>dalle pleine</b> s'impose pour les formes irrégulières, les porte-à-faux, les fortes charges, les zones humides ou quand on veut une sous-face lisse sans retombées. Le choix revient à l'ingénieur, en accord avec l'architecte.</p>
<h2>Le plancher à corps creux (hourdis)</h2>
<p>Il se compose de poutrelles (préfabriquées ou coulées en place), de blocs creux en béton ou en terre cuite (les hourdis) et d'une dalle de compression armée d'un treillis soudé. Il se désigne par deux chiffres : un plancher <b>16+4</b> comporte des hourdis de 16 cm et une dalle de compression de 4 cm, soit environ 20 cm au total ; un <b>20+5</b> fait environ 25 cm.</p>
<div class="tableau"><table><thead><tr><th>Type</th><th>Épaisseur totale</th><th>Usage courant (indicatif)</th></tr></thead><tbody>
<tr><td>16+4</td><td>≈ 20 cm</td><td>Portées courantes d'habitation, souvent jusqu'à 5 m environ</td></tr>
<tr><td>20+5</td><td>≈ 25 cm</td><td>Portées plus longues ou charges plus fortes</td></tr>
<tr><td>Dalle pleine</td><td>Selon calcul</td><td>Formes complexes, porte-à-faux, salles d'eau, terrasses accessibles</td></tr>
</tbody></table></div>
<p>Les portées admissibles dépendent des poutrelles utilisées, des charges et du ferraillage : elles se lisent dans les tableaux du fabricant ou se calculent. Les valeurs ci-dessus sont des ordres de grandeur, <b>à confirmer par le calcul</b>.</p>
<h2>La dalle pleine en béton armé</h2>
<p>C'est une plaque de béton armé coulée sur coffrage, appuyée sur des poutres ou des voiles. Elle peut porter dans une ou deux directions, ce qui la rend adaptée aux formes irrégulières, aux balcons en porte-à-faux et aux trémies. Elle est plus lourde et consomme davantage de béton et d'acier, mais offre une meilleure isolation acoustique aux bruits aériens et une grande liberté de passage des réseaux.</p>
<h2>Comparatif rapide</h2>
<ul>
<li><b>Coût</b> : avantage au hourdis sur les portées courantes, moins de béton et de coffrage.</li>
<li><b>Poids</b> : le hourdis est plus léger, ce qui réduit les charges sur les poteaux, les fondations et l'effort sismique.</li>
<li><b>Formes</b> : avantage à la dalle pleine pour les angles, les porte-à-faux et les grandes ouvertures.</li>
<li><b>Acoustique</b> : la dalle pleine, plus massive, isole mieux des bruits aériens.</li>
<li><b>Fixations</b> : percer un hourdis creux demande des chevilles adaptées pour les charges suspendues.</li>
</ul>
<h2>Les exigences parasismiques</h2>
<p>Dans les deux cas, le plancher doit fonctionner comme un <b>diaphragme</b> rigide qui relie les poteaux et les murs. Cela suppose une dalle de compression continue, correctement armée et liée aux chaînages et aux poutres. Une dalle de compression trop mince ou sans treillis compromet ce rôle. Sur les toitures-terrasses, pensez aussi à l'<a href="conseil-etancheite-toiture-terrasse-maroc.html">étanchéité</a> et à l'isolation.</p>
<h2>Le rôle du bureau d'études</h2>
<p>Le bureau d'études choisit le type de plancher pièce par pièce, calcule les portées et charges, définit le sens des poutrelles, les renforts autour des trémies et les zones en dalle pleine. Les plans de coffrage qu'il fournit évitent les improvisations de chantier, comme une poutrelle doublée « au jugé » sous une cloison lourde.</p>
""",
 "faq": [
  ("Que signifie un plancher 16+4 ?", "C'est un plancher à poutrelles avec des hourdis de 16 cm de hauteur et une dalle de compression de 4 cm, soit environ 20 cm d'épaisseur totale."),
  ("Quelle portée pour un plancher hourdis 16+4 ?", "On l'emploie couramment pour des portées d'habitation allant jusqu'à 5 m environ, mais la portée admissible dépend des poutrelles et des charges et doit être vérifiée par le calcul."),
  ("La dalle pleine est-elle plus solide que le hourdis ?", "Les deux sont sûrs s'ils sont calculés. La dalle pleine convient mieux aux formes irrégulières, aux porte-à-faux et aux fortes charges ; le hourdis est plus léger et économique sur les portées courantes."),
 ],
 "sources": [
  ("https://www.habitatpresto.com/mag/renovation/prix-m2-plancher-hourdis", "Habitatpresto, plancher hourdis 16+4 et 20+5"),
 ],
},
{
 "slug": "conseil-poutre-portee-retombee",
 "cat": "structure",
 "title": "Poutre en béton armé : quelle retombée pour quelle portée ?",
 "crumb": "Portée des poutres",
 "desc": "Prédimensionnement d'une poutre : hauteur de L/15 à L/10 de la portée, soit 35 à 50 cm pour 5 m. Largeur, RPS (b ≥ 20 cm) et moyens de réduire la retombée.",
 "lead": "La retombée d'une poutre est souvent un sujet de discussion entre architecte, client et ingénieur. Voici les ordres de grandeur et les marges de manœuvre réelles.",
 "img": "images/services/beton-poutre.jpg",
 "min": 5,
 "body": """
<p>Pour un premier dimensionnement, la hauteur totale d'une poutre en béton armé est comprise entre <b>1/15 et 1/10 de sa portée</b>. Une poutre de 5 m entre appuis aura donc une hauteur d'environ 35 à 50 cm, dont une partie dépasse sous le plancher : c'est la <b>retombée</b>. Ces ratios servent à démarrer le projet ; la section définitive est <b>fixée par le calcul</b>.</p>
<h2>Ordres de grandeur de prédimensionnement</h2>
<div class="tableau"><table><thead><tr><th>Portée entre appuis</th><th>Hauteur L/15</th><th>Hauteur L/10</th></tr></thead><tbody>
<tr><td>3 m</td><td>20 cm</td><td>30 cm</td></tr>
<tr><td>4 m</td><td>27 cm</td><td>40 cm</td></tr>
<tr><td>5 m</td><td>33 cm</td><td>50 cm</td></tr>
<tr><td>6 m</td><td>40 cm</td><td>60 cm</td></tr>
</tbody></table></div>
<p>La largeur se situe couramment entre 0,4 et 0,7 fois la hauteur. Plus la charge est forte (mur au-dessus, poteau qui repose sur la poutre), plus on se rapproche de L/10, voire au-delà. Une poutre en console (porte-à-faux) se dimensionne différemment et demande en général une hauteur bien plus forte par rapport à sa longueur.</p>
<h2>Les règles du RPS pour les poutres</h2>
<p>Le règlement parasismique marocain impose des dimensions minimales aux poutres participant au contreventement : une <b>largeur d'au moins 20 cm</b>, un rapport largeur/hauteur d'au moins 0,25, et une largeur limitée par rapport à celle du poteau d'appui. Il impose aussi des barres longitudinales d'au moins 10 mm et des cadres resserrés près des appuis, dans les zones critiques.</p>
<h2>Comment réduire la retombée ?</h2>
<ul>
<li><b>Ajouter un appui</b> (poteau ou mur) pour diviser la portée : c'est la solution la plus efficace.</li>
<li><b>Élargir la poutre</b> et réduire sa hauteur (poutre plate ou noyée dans le plancher), au prix de plus d'acier et d'une flèche à vérifier.</li>
<li><b>Utiliser une dalle pleine</b> portant dans deux directions plutôt qu'une poutre isolée.</li>
<li><b>Passer à une poutre en acier</b> ou à du béton précontraint pour les très grandes portées.</li>
<li><b>Placer la poutre en relevé</b>, au-dessus du plancher, quand l'usage le permet (terrasse, acrotère).</li>
</ul>
<p>Chaque option a des conséquences sur le coût, la flèche et le comportement sismique ; elles se discutent au stade de l'avant-projet, pas sur le chantier.</p>
<h2>La flèche, souvent oubliée</h2>
<p>Une poutre trop mince peut résister sans casser mais se déformer exagérément : carrelages qui se décollent, cloisons fissurées, menuiseries coincées. C'est souvent la flèche, plus que la résistance, qui impose la hauteur d'une poutre de grande portée. Si vous constatez des fissures, notre article sur les <a href="conseil-fissures-maison-causes-gravite.html">fissures dans une maison</a> vous aidera à les interpréter.</p>
<h2>Le rôle du bureau d'études</h2>
<p>Le bureau d'études arbitre entre exigences architecturales et contraintes structurelles : il calcule chaque poutre, vérifie la flèche et le respect du RPS, et propose des alternatives si une retombée gêne. Toute suppression de poteau ou augmentation de portée en cours de chantier doit lui être soumise (voir <a href="conseil-supprimer-mur-porteur-ouverture.html">ouvrir un mur porteur</a>).</p>
""",
 "faq": [
  ("Quelle hauteur de poutre pour 5 m de portée ?", "En prédimensionnement, entre L/15 et L/10, soit environ 35 à 50 cm pour 5 m. La hauteur définitive dépend des charges et de la flèche et doit être calculée."),
  ("Quelle largeur minimale pour une poutre selon le RPS ?", "Le règlement parasismique marocain impose une largeur d'au moins 20 cm et un rapport largeur/hauteur d'au moins 0,25 pour les poutres."),
  ("Peut-on supprimer la retombée d'une poutre ?", "On peut la réduire avec une poutre plate plus large, un appui supplémentaire ou une dalle pleine, mais chaque solution doit être calculée par l'ingénieur."),
 ],
 "sources": [
  ("https://www.preventionweb.net/files/21648_13356rps20021.pdf?startDownload=true", "Ministère de l'Habitat, règlement parasismique RPS 2000"),
 ],
},
{
 "slug": "conseil-enrobage-armatures-beton",
 "cat": "structure",
 "title": "Enrobage des armatures du béton armé : quelles valeurs respecter ?",
 "crumb": "Enrobage des armatures",
 "desc": "Enrobage des aciers : 1 à 5 cm selon le BAEL, environ 25 à 45 mm selon l'Eurocode 2 et l'exposition. Son rôle contre la corrosion et comment le contrôler.",
 "lead": "L'enrobage, c'est l'épaisseur de béton entre l'acier et la surface. Quelques millimètres en moins suffisent à faire rouiller les armatures et éclater le béton en quelques années.",
 "img": "images/projects/project6.jpg",
 "min": 5,
 "body": """
<p>L'enrobage est la distance entre la surface du béton et l'armature la plus proche, cadres compris. Les valeurs dépendent de l'exposition de l'ouvrage : avec le <b>BAEL 91</b>, encore très utilisé au Maroc, on retient 1 cm à l'intérieur des locaux clos et secs, 3 cm pour les parois exposées aux intempéries ou aux condensations et 5 cm en milieu marin ou très agressif. Avec l'<b>Eurocode 2</b>, l'enrobage nominal se situe généralement entre 25 et 45 mm selon la classe d'exposition.</p>
<h2>Pourquoi l'enrobage est vital</h2>
<p>Le béton protège naturellement l'acier de la corrosion grâce à son alcalinité. Avec le temps, le gaz carbonique de l'air pénètre le béton (carbonatation) et finit par atteindre les armatures si l'enrobage est trop faible. L'acier rouille, gonfle et fait éclater le béton : c'est la pathologie classique des balcons, acrotères et poteaux de façade qui s'épaufrent. L'enrobage assure aussi l'adhérence de l'acier au béton et une protection en cas d'incendie.</p>
<h2>Les valeurs de référence</h2>
<div class="tableau"><table><thead><tr><th>Situation</th><th>BAEL 91 (art. A.7.1)</th><th>Eurocode 2 (indicatif, classe S4)</th></tr></thead><tbody>
<tr><td>Intérieur sec, locaux clos</td><td>1 cm</td><td>≈ 25 mm (XC1)</td></tr>
<tr><td>Extérieur, intempéries, condensation</td><td>3 cm (2 cm si béton > 40 MPa)</td><td>≈ 35 à 40 mm (XC3, XC4)</td></tr>
<tr><td>Milieu marin ou très agressif</td><td>5 cm</td><td>≈ 45 mm et plus (XS)</td></tr>
<tr><td>Béton coulé contre la terre</td><td>Valeur renforcée</td><td>40 mm sur béton de propreté, 75 mm contre le sol brut</td></tr>
</tbody></table></div>
<p>Avec l'Eurocode 2, l'enrobage nominal est égal à l'enrobage minimal augmenté d'une tolérance d'exécution, en général 10 mm. Les valeurs exactes dépendent de la classe structurale, de la classe de béton et de l'annexe nationale appliquée : elles sont <b>fixées par l'ingénieur</b> sur les plans. Le diamètre de la plus grosse barre est aussi un minimum.</p>
<h2>Comment garantir l'enrobage sur chantier</h2>
<ul>
<li><b>Des cales</b> en béton ou en plastique, de la bonne épaisseur, en nombre suffisant (pas des morceaux de brique ou de pierre).</li>
<li><b>Des distanciers</b> pour les nappes supérieures des dalles, afin qu'elles ne s'écrasent pas sous les pas des ouvriers.</li>
<li><b>Un coffrage propre et stable</b>, pour que le ferraillage ne se déplace pas au coulage.</li>
<li><b>Une vibration correcte</b>, sans toucher les armatures, pour éviter les nids de cailloux.</li>
</ul>
<h2>Le climat de Marrakech</h2>
<p>Les fortes chaleurs et l'air sec accélèrent le séchage du béton de surface, qui devient plus poreux si la cure est négligée : la protection apportée par l'enrobage diminue. Une bonne <a href="conseil-cure-beton-chaleur-marrakech.html">cure du béton</a> est donc le complément indispensable d'un enrobage correct. Les piscines, les ouvrages enterrés et les réservoirs méritent des valeurs plus fortes.</p>
<h2>Le rôle du bureau d'études</h2>
<p>Le bureau d'études indique l'enrobage de chaque élément sur les plans et le vérifie lors du <a href="conseil-controle-ferraillage-avant-coulage.html">contrôle du ferraillage avant coulage</a>. Un enrobage insuffisant est l'un des défauts les plus fréquents relevés, et l'un des plus coûteux à réparer plus tard.</p>
""",
 "faq": [
  ("Quel enrobage pour un poteau extérieur ?", "Selon le BAEL 91, 3 cm pour une paroi exposée aux intempéries ; selon l'Eurocode 2, environ 35 à 40 mm selon la classe d'exposition. La valeur exacte figure sur les plans de l'ingénieur."),
  ("Quel enrobage pour une semelle de fondation ?", "Un béton coulé contre la terre demande un enrobage renforcé : l'Eurocode 2 retient par exemple 40 mm sur béton de propreté et 75 mm directement contre le sol."),
  ("Que se passe-t-il si l'enrobage est insuffisant ?", "Les armatures finissent par rouiller, gonflent et font éclater le béton : c'est l'origine de nombreux épaufrements sur les balcons, acrotères et poteaux de façade."),
 ],
 "sources": [
  ("https://www.afgc.asso.fr/app/uploads/2016/10/5_2_NI_Determination_Enrobage_armatutres.pdf", "AFGC, détermination de l'enrobage des armatures"),
  ("https://collections.univ-gustave-eiffel.fr/ouvrages/lcpc/GuideTechnique/GuideTechnique-LCPC-ENROB.pdf", "LCPC, guide technique sur l'enrobage"),
  ("https://qualiteconstruction.com/wp-content/uploads/2024/05/Fiche-Pathologie-Batiment-B05-Corrosion-Armatures-Beton-Arme-Facades-Batiments-AQC.pdf", "AQC, corrosion des armatures en façade"),
 ],
},
{
 "slug": "conseil-controle-ferraillage-avant-coulage",
 "cat": "structure",
 "title": "Contrôle du ferraillage avant coulage : la checklist du chantier",
 "crumb": "Contrôle du ferraillage",
 "desc": "Avant chaque coulage, vérifiez diamètres, nombre de barres, cadres, recouvrements, ancrages, enrobage et propreté : la checklist de contrôle d'un BET.",
 "lead": "Une fois le béton coulé, il est trop tard : le ferraillage devient invisible. Le contrôle avant coulage est le moment où se joue la solidité réelle de votre structure.",
 "img": "images/projects/project4.jpg",
 "min": 5,
 "body": """
<p>Avant chaque coulage de semelles, poteaux, poutres ou dalles, le ferraillage doit être comparé point par point aux plans d'exécution : <b>diamètres et nombre de barres, espacement des cadres, recouvrements, ancrages, enrobage et propreté</b>. Ce contrôle, réalisé par le bureau d'études ou le bureau de contrôle, prend souvent moins d'une heure et évite des défauts irréparables.</p>
<h2>La checklist de contrôle</h2>
<div class="tableau"><table><thead><tr><th>Point</th><th>Ce qu'on vérifie</th></tr></thead><tbody>
<tr><td>Barres principales</td><td>Nombre, diamètre (HA10, HA12, HA14…) et position conformes au plan</td></tr>
<tr><td>Cadres et étriers</td><td>Diamètre, espacement, resserrement dans les zones critiques, cadres fermés</td></tr>
<tr><td>Recouvrements</td><td>Longueur suffisante, décalés et non tous au même endroit</td></tr>
<tr><td>Ancrages</td><td>Barres de poutres ancrées dans les poteaux, attentes en place pour l'étage suivant</td></tr>
<tr><td>Nœuds poteau-poutre</td><td>Cadres présents dans le nœud, malgré la difficulté de mise en place</td></tr>
<tr><td>Enrobage</td><td>Cales et distanciers de la bonne épaisseur, en nombre suffisant</td></tr>
<tr><td>Propreté</td><td>Aciers sans terre, huile ni rouille non adhérente ; coffrage nettoyé</td></tr>
<tr><td>Réservations</td><td>Gaines et fourreaux prévus, sans couper ni déplacer les armatures</td></tr>
</tbody></table></div>
<h2>Les défauts les plus fréquents</h2>
<ul>
<li><b>Diamètres remplacés</b> : un HA12 au lieu d'un HA14, par manque de stock. La section d'acier chute de près de 27 %.</li>
<li><b>Cadres trop espacés</b> aux extrémités des poteaux et des poutres, là où le règlement parasismique les veut resserrés.</li>
<li><b>Crochets mal formés</b> : les règles parasismiques demandent des cadres fermés par des crochets repliés vers l'intérieur du béton, qui ne s'ouvrent pas en cas de séisme.</li>
<li><b>Recouvrements trop courts</b>. Faute d'indication sur les plans, le BAEL donne une longueur forfaitaire de l'ordre de 50 diamètres pour l'acier FeE500 (40 diamètres pour le FeE400).</li>
<li><b>Nappe supérieure écrasée</b> dans les dalles, qui perd toute efficacité sur les appuis et les porte-à-faux.</li>
<li><b>Aciers de chapeaux oubliés</b> au-dessus des poutres et des appuis de dalles.</li>
</ul>
<h2>Comment organiser le contrôle</h2>
<p>Prévoyez dans le contrat de l'entreprise que chaque coulage d'élément structurel soit précédé d'une réception du ferraillage, avec un délai de prévenance (par exemple 24 à 48 heures). Le contrôleur rédige un procès-verbal avec photos, et les corrections sont vérifiées avant d'autoriser le coulage. Les photos datées constituent ensuite une archive utile pour la réception et en cas de litige. Voir aussi notre article sur le <a href="conseil-suivi-de-chantier-bet-visites.html">suivi de chantier par le BET</a>.</p>
<h2>Après le contrôle : le coulage</h2>
<p>Le contrôle du ferraillage ne sert à rien si le béton est ensuite mal mis en œuvre : ajout d'eau, absence de vibration, coulage par forte chaleur sans précaution. Le contrôleur vérifie aussi le dosage ou le bon de livraison du béton prêt à l'emploi, et fait réaliser des éprouvettes sur les ouvrages importants. Sur le dosage, lisez notre article sur le <a href="conseil-dosage-beton-fondation-dalle.html">dosage du béton</a>.</p>
<h2>Le rôle du bureau d'études</h2>
<p>Le bureau d'études qui a calculé la structure est le mieux placé pour contrôler son ferraillage : il sait quels détails sont critiques et pourquoi. Ses visites avant coulage transforment des plans sur papier en une structure réellement conforme au RPS 2011.</p>
""",
 "faq": [
  ("Qui doit contrôler le ferraillage avant coulage ?", "Le bureau d'études qui a conçu la structure ou le bureau de contrôle mandaté. L'entreprise doit le prévenir à l'avance de chaque coulage d'élément porteur."),
  ("Quelle longueur de recouvrement pour les aciers ?", "Elle est indiquée sur les plans ; à défaut de calcul, le BAEL donne une valeur forfaitaire de l'ordre de 50 diamètres pour l'acier FeE500 et 40 diamètres pour le FeE400."),
  ("Peut-on remplacer un HA14 par un HA12 ?", "Pas sans accord de l'ingénieur : la section d'acier passe de 1,54 à 1,13 cm² par barre, soit environ 27 % de moins."),
 ],
 "sources": [
  ("https://piles.cerema.fr/IMG/pdf/Beton_Arme_ferraillage_cle76447d-2.pdf", "Cerema, béton armé et ferraillage"),
 ],
},
{
 "slug": "conseil-cure-beton-chaleur-marrakech",
 "cat": "structure",
 "title": "Cure du béton par forte chaleur : les bons gestes à Marrakech",
 "crumb": "Cure du béton",
 "desc": "Au-delà de 25 °C, le béton exige des précautions : coulage tôt le matin, arrosage, bâches, produit de cure. Les bons gestes l'été à Marrakech.",
 "lead": "Quand il fait plus de 40 °C à Marrakech, un béton mal protégé peut perdre une part importante de sa résistance et se couvrir de fissures en quelques heures.",
 "img": "images/projects/villa1.jpg",
 "min": 5,
 "body": """
<p>Par forte chaleur, le béton doit être <b>coulé aux heures fraîches</b> et <b>maintenu humide pendant plusieurs jours</b> : arrosage régulier, bâches ou toiles humides, ou produit de cure pulvérisé. Les guides des cimentiers recommandent des mesures particulières dès que la température dépasse 25 °C. À Marrakech, où l'été dépasse souvent 40 °C, ces précautions ne sont pas une option.</p>
<h2>Pourquoi la chaleur abîme le béton</h2>
<p>Le béton durcit grâce à une réaction chimique entre le ciment et l'eau, l'hydratation. Si l'eau s'évapore trop vite, cette réaction s'arrête en surface : le béton devient poreux, moins résistant et moins protecteur pour les armatures. La chaleur accélère aussi la prise, ce qui complique la mise en place et la vibration. Résultat : fissures de retrait plastique en surface des dalles, faïençage, perte de résistance. Selon des sources techniques, un béton mûri en ambiance sèche peut perdre une part importante de sa résistance par rapport à un béton conservé humide.</p>
<h2>Avant et pendant le coulage</h2>
<ul>
<li><b>Couler tôt le matin</b> (ou en fin de journée), jamais aux heures les plus chaudes.</li>
<li><b>Humidifier les coffrages</b> et le support (béton de propreté, hourdis) sans laisser d'eau stagnante.</li>
<li><b>Protéger les granulats et l'eau</b> du soleil sur un béton de chantier ; pour un béton de centrale, demander une formulation adaptée (retardateur de prise).</li>
<li><b>Ne jamais ajouter d'eau</b> au béton pour compenser sa raideur : c'est la première cause de béton faible.</li>
<li><b>Couler vite</b>, avec une pompe si possible, et vibrer correctement.</li>
<li><b>Reporter le coulage</b> si les conditions (vent chaud, chaleur extrême) ne permettent pas un travail correct.</li>
</ul>
<h2>Après le coulage : la cure</h2>
<div class="tableau"><table><thead><tr><th>Méthode</th><th>Mise en œuvre</th></tr></thead><tbody>
<tr><td>Arrosage</td><td>Brumisation ou arrosage fin plusieurs fois par jour, sans laisser sécher entre deux passages</td></tr>
<tr><td>Bâches, toiles de jute humides</td><td>Posées dès que la surface le permet, maintenues humides ; nattes à face claire côté soleil</td></tr>
<tr><td>Produit de cure</td><td>Pulvérisé juste après la finition, il forme un film qui limite l'évaporation</td></tr>
<tr><td>Maintien des coffrages</td><td>Les faces coffrées sèchent moins vite tant que le coffrage reste en place</td></tr>
</tbody></table></div>
<p>La durée de cure dépend du ciment, de la température et de l'ouvrage ; plusieurs jours sont un minimum par forte chaleur, et le cahier des charges ou le bureau d'études peut fixer une durée précise.</p>
<h2>Les ouvrages les plus sensibles</h2>
<p>Les dalles et toitures-terrasses, très exposées au soleil et au vent, sont les plus vulnérables : leur grande surface favorise l'évaporation. Les voiles de piscine et les réservoirs, qui doivent rester étanches, méritent une cure particulièrement soignée. Une cure négligée réduit aussi l'efficacité de l'<a href="conseil-enrobage-armatures-beton.html">enrobage des armatures</a>.</p>
<h2>Le rôle du bureau d'études</h2>
<p>Le bureau d'études prévoit les exigences de bétonnage par temps chaud dans le cahier des charges et vérifie leur respect lors des visites. Il peut aussi faire réaliser des éprouvettes pour contrôler la résistance réelle du béton, avant de valider le <a href="conseil-delai-decoffrage-dalle-poteaux.html">décoffrage</a>.</p>
""",
 "faq": [
  ("À partir de quelle température faut-il des précautions pour couler du béton ?", "Les guides des cimentiers recommandent des mesures particulières dès que la température dépasse 25 °C : coulage aux heures fraîches, protection et cure renforcée."),
  ("Combien de temps arroser une dalle en béton en été ?", "Plusieurs jours au minimum par forte chaleur, en gardant la surface constamment humide ; la durée exacte peut être fixée par le cahier des charges ou le bureau d'études."),
  ("Peut-on rajouter de l'eau au béton quand il fait chaud ?", "Non : l'eau ajoutée réduit la résistance et augmente la porosité. Il faut plutôt un adjuvant retardateur ou couler aux heures plus fraîches."),
 ],
 "sources": [
  ("https://www.eqiom.com/sites/default/files/2023-07/eqiom-temps-chaud-site-hd.pdf", "EQIOM, bétonner par temps chaud"),
  ("https://holcim.ch/sites/switzerland/files/docs/pocketguide_betonieren-bei-warmer-witterung_fr.pdf", "Holcim, bétonnage par temps chaud"),
  ("https://www.afgc.asso.fr/app/uploads/2016/10/2_3_RECO_Classe_de_cure.pdf", "AFGC, recommandations sur la cure"),
 ],
},
{
 "slug": "conseil-delai-decoffrage-dalle-poteaux",
 "cat": "structure",
 "title": "Délai de décoffrage d'une dalle, d'une poutre et des poteaux",
 "crumb": "Délais de décoffrage",
 "desc": "Côtés de poteaux et joues de poutres : 1 à 3 jours. Fonds de dalles et étais : souvent 21 à 28 jours, ou sous-étaiement. Délais indicatifs et précautions.",
 "lead": "Décoffrer trop tôt est l'une des causes classiques de flèches excessives, de fissures, voire d'effondrement. Les délais à respecter selon l'élément et les conditions.",
 "img": "images/projects/project5.jpg",
 "min": 5,
 "body": """
<p>Les coffrages verticaux (côtés des poteaux, voiles, joues de poutres) peuvent en général être retirés après <b>1 à 3 jours</b>, car ils ne portent pas de charge. Les fonds de coffrage et les étais des dalles et des poutres doivent rester en place bien plus longtemps, couramment <b>21 à 28 jours</b>, ou être remplacés par un sous-étaiement. Ces délais sont indicatifs : la règle est de ne décoffrer que lorsque le béton a atteint une résistance suffisante.</p>
<h2>Délais indicatifs par élément</h2>
<div class="tableau"><table><thead><tr><th>Élément</th><th>Délai courant (indicatif)</th><th>Remarque</th></tr></thead><tbody>
<tr><td>Côtés de poteaux et voiles</td><td>1 à 3 jours</td><td>Attendre que les arêtes ne s'arrachent pas au décoffrage</td></tr>
<tr><td>Joues de poutres</td><td>1 à 3 jours</td><td>Le fond de poutre et ses étais restent en place</td></tr>
<tr><td>Fonds de dalles et de poutres</td><td>Souvent 21 à 28 jours</td><td>Décoffrage anticipé possible avec sous-étaiement</td></tr>
<tr><td>Porte-à-faux, balcons</td><td>Plus long, selon l'ingénieur</td><td>Éléments très sensibles à un décoffrage prématuré</td></tr>
</tbody></table></div>
<p>Le béton n'atteint sa résistance de calcul qu'à 28 jours, mais il en développe une grande partie dans la première semaine, surtout par temps chaud. C'est pourquoi on peut retirer certains coffrages plus tôt, à condition de laisser des étais pour porter la dalle.</p>
<h2>Ce qui fait varier les délais</h2>
<ul>
<li><b>La température</b> : le béton durcit plus vite à la chaleur, plus lentement par temps froid (hivers de l'Atlas).</li>
<li><b>Le type de ciment</b> et la formulation du béton.</li>
<li><b>La portée</b> : une grande dalle ou une poutre longue demande plus de temps.</li>
<li><b>Les charges de chantier</b> : un plancher qui reçoit déjà le coffrage et le béton de l'étage supérieur doit rester étayé.</li>
<li><b>La cure</b> : un béton qui a séché trop vite n'a pas la résistance attendue.</li>
</ul>
<h2>Le sous-étaiement</h2>
<p>Pour récupérer les coffrages plus vite, les entreprises pratiquent le sous-étaiement : on décoffre le plancher puis on remet immédiatement des étais de séchage qui le soulagent jusqu'à ce qu'il ait atteint sa résistance. Cette méthode est sûre si elle est organisée travée par travée, sans laisser le plancher sans appui. Dans un bâtiment à plusieurs niveaux, les étais de plusieurs étages se cumulent souvent : il faut un plan d'étaiement.</p>
<h2>Les signes d'un décoffrage trop précoce</h2>
<p>Flèche visible de la dalle, fissures en sous-face ou près des appuis, arêtes de poteaux écaillées, ou nids de cailloux révélés trop tôt. Une flèche excessive est souvent irréversible. En cas de doute, faites examiner les <a href="conseil-fissures-maison-causes-gravite.html">fissures</a> par un ingénieur.</p>
<h2>Le rôle du bureau d'études</h2>
<p>Le bureau d'études fixe dans le cahier des charges les délais minimaux et les conditions de décoffrage, en tenant compte de la saison. Pour les ouvrages sensibles, il peut demander des essais sur éprouvettes avant d'autoriser le retrait des étais. Une bonne <a href="conseil-cure-beton-chaleur-marrakech.html">cure du béton</a> conditionne aussi la résistance au moment du décoffrage.</p>
""",
 "faq": [
  ("Quand peut-on décoffrer une dalle en béton ?", "Le fond de coffrage et les étais restent généralement en place 21 à 28 jours, sauf sous-étaiement organisé. Le délai exact dépend de la portée, de la température et de la résistance atteinte."),
  ("Combien de temps avant de décoffrer un poteau ?", "Les côtés d'un poteau peuvent en général être retirés après 1 à 3 jours, quand le béton est assez dur pour que les arêtes ne s'arrachent pas."),
  ("Qu'est-ce que le sous-étaiement ?", "C'est la remise en place d'étais sous une dalle juste après son décoffrage, pour la soulager jusqu'à ce qu'elle atteigne sa résistance tout en récupérant les coffrages."),
 ],
 "sources": [
  ("https://www.ffbatiment.fr/techniques-batiment/gros-oeuvre-structure/echafaudage-levage-coffrage-etaiement/dossier-bam/gagner-du-temps-sans-mettre-en-peril-l-ouvrage", "FFB, sous-étaiement et sécurité de l'ouvrage"),
  ("https://travail-industrie.com/nos-formations/formation-coffreur-bancheur-gros-oeuvre-beton-arme/module/2/chapitre/3", "Travail Industrie, coffrage des poutres et dalles"),
 ],
},
{
 "slug": "conseil-supprimer-mur-porteur-ouverture",
 "cat": "structure",
 "title": "Ouvrir ou supprimer un mur porteur : étapes, risques et étude",
 "crumb": "Mur porteur",
 "desc": "Ouvrir un mur porteur exige une étude de structure, un étaiement, une poutre calculée (béton ou acier) et parfois une autorisation. Étapes et pièges au Maroc.",
 "lead": "Agrandir un séjour ou créer une baie en supprimant un mur porteur est possible, à condition de reporter correctement les charges. Ce qu'il faut savoir avant de casser.",
 "img": "images/projects/villa2.jpg",
 "min": 5,
 "body": """
<p>Oui, on peut ouvrir ou supprimer un mur porteur, mais seulement après une <b>étude de structure</b> qui calcule les charges à reprendre, dimensionne la <b>poutre de remplacement</b> (béton armé ou acier) et vérifie ses appuis jusqu'aux fondations. Les travaux se font sous <b>étaiement</b>, par une entreprise qualifiée. Au Maroc, une modification de structure peut aussi nécessiter une autorisation et, en copropriété, l'accord des copropriétaires.</p>
<h2>Comment savoir si un mur est porteur ?</h2>
<p>Un mur est porteur s'il soutient un plancher, une toiture ou un autre mur. Dans une villa récente en ossature béton (poteaux et poutres), la plupart des murs sont de simples remplissages ; dans une maison ancienne, un riad ou une construction en maçonnerie chaînée, les murs épais sont presque toujours porteurs. Les indices : épaisseur, position centrale, poutrelles qui s'y appuient. Seuls les plans de structure ou un diagnostic permettent de conclure.</p>
<h2>Les étapes d'une ouverture</h2>
<ol>
<li><b>Diagnostic et étude</b> : relevé de l'existant, descente de charges, choix de la poutre et des appuis, vérification des fondations sous les nouveaux points d'appui.</li>
<li><b>Autorisations</b> : selon la nature des travaux et la commune, demande via la plateforme Rokhas ; accord de la copropriété en immeuble.</li>
<li><b>Étaiement</b> : étais et bastaings de part et d'autre du mur pour soulager le plancher pendant les travaux.</li>
<li><b>Création des appuis</b> : poteaux ou sommiers en béton armé aux extrémités de l'ouverture.</li>
<li><b>Pose de la poutre</b> : poutre en béton armé coulée en place ou profilé acier, calée et scellée sur ses appuis.</li>
<li><b>Démolition</b> du mur sous la poutre, puis retrait des étais après durcissement des scellements.</li>
</ol>
<h2>Les risques d'une ouverture improvisée</h2>
<ul>
<li><b>Fissures et affaissement</b> du plancher supérieur si la poutre est trop faible ou mal calée.</li>
<li><b>Poinçonnement</b> des appuis : une poutre bien dimensionnée posée sur une maçonnerie fragile écrase son appui.</li>
<li><b>Affaiblissement parasismique</b> : un mur porteur participe souvent au contreventement ; le supprimer peut rendre le bâtiment vulnérable aux séismes, comme l'ont rappelé les dégâts d'Al Haouz.</li>
<li><b>Fondations insuffisantes</b> sous les nouveaux poteaux, qui concentrent les charges.</li>
</ul>
<h2>Béton ou acier ?</h2>
<p>La poutre en acier (IPN, IPE, HEA) se pose vite et limite la retombée, mais doit être protégée contre la corrosion et parfois contre le feu. La poutre en béton armé, coulée en place, demande un coffrage et un délai de durcissement mais s'intègre bien à une structure béton. Le choix dépend de la portée, de la retombée acceptable et de l'accès au chantier.</p>
<h2>Le rôle du bureau d'études</h2>
<p>Le bureau d'études réalise le diagnostic, la note de calcul et les plans d'exécution, puis contrôle l'étaiement et la pose de la poutre. Il vérifie aussi l'impact sur la stabilité sismique d'ensemble, en particulier dans une <a href="conseil-surelevation-ajouter-etage-maroc.html">surélévation</a> ou une rénovation lourde. Avant d'acheter un bien à transformer, une <a href="conseil-verifier-structure-maison-avant-achat.html">vérification de la structure</a> évite les mauvaises surprises.</p>
""",
 "faq": [
  ("Peut-on supprimer un mur porteur dans une maison ?", "Oui, à condition de faire calculer une poutre de remplacement et ses appuis par un ingénieur structure et de réaliser les travaux sous étaiement."),
  ("Faut-il une autorisation pour ouvrir un mur porteur au Maroc ?", "Une modification de structure peut nécessiter une autorisation de la commune, à vérifier selon les travaux, et l'accord de la copropriété en immeuble."),
  ("Quelle poutre pour remplacer un mur porteur ?", "Une poutre en béton armé ou un profilé acier (IPN, IPE, HEA), dont la section dépend de la portée et des charges et doit être fixée par la note de calcul."),
 ],
 "sources": [
  ("https://www.lamaisonsaintgobain.fr/guides-travaux/renovation-appartement/ouvrir-ou-casser-un-mur-porteur-mode-d-emploi", "La Maison Saint-Gobain, ouvrir un mur porteur"),
  ("https://copeps.fr/actualites/entreprise-ouverture-mur-porteur/", "Copeps, étapes d'une ouverture de mur porteur"),
 ],
},
{
 "slug": "conseil-joint-de-dilatation-batiment",
 "cat": "structure",
 "title": "Joint de dilatation d'un bâtiment : quand et tous les combien ?",
 "crumb": "Joint de dilatation",
 "desc": "En climat chaud et sec comme à Marrakech, on prévoit souvent un joint de dilatation tous les 25 m environ, et un joint sismique d'au moins 5 cm selon le RPS.",
 "lead": "Un bâtiment en béton se dilate à la chaleur et se rétracte au froid. Au-delà d'une certaine longueur, il faut le couper en blocs indépendants pour éviter les fissures.",
 "img": "images/projects/project6.jpg",
 "min": 5,
 "body": """
<p>Un joint de dilatation coupe le bâtiment en blocs indépendants pour absorber les variations de longueur dues à la température et au retrait du béton. Les règles françaises du BAEL, souvent reprises au Maroc, recommandent un joint tous les <b>25 m environ dans les régions sèches et chaudes</b> à forts écarts de température (proches du climat méditerranéen), et jusqu'à 50 m dans les régions humides et tempérées. À Marrakech, on retient donc le plus souvent une longueur de bloc de l'ordre de 25 m, sauf justification par le calcul.</p>
<h2>Pourquoi les joints sont nécessaires</h2>
<p>Le béton se dilate d'environ 1 mm par 10 m de longueur pour 10 °C d'écart. Entre une nuit d'hiver et une journée d'été au soleil, une toiture-terrasse de Marrakech peut subir plusieurs dizaines de degrés de variation. S'il ne peut pas bouger librement, un long bâtiment accumule des efforts qui fissurent les murs, les dalles et les acrotères. Le retrait du béton au séchage produit le même effet.</p>
<h2>Ordres de grandeur</h2>
<div class="tableau"><table><thead><tr><th>Ouvrage</th><th>Distance entre joints (indicative)</th></tr></thead><tbody>
<tr><td>Structure béton armé, climat chaud et sec</td><td>Environ 25 m (règles BAEL, régions méditerranéennes)</td></tr>
<tr><td>Structure béton armé, climat humide et tempéré</td><td>Jusqu'à 40 à 50 m</td></tr>
<tr><td>Murs de façade en maçonnerie</td><td>Valeurs plus faibles, de l'ordre de 20 m en climat méditerranéen</td></tr>
<tr><td>Dallages, terrasses, acrotères</td><td>Fractionnement plus serré, selon le revêtement</td></tr>
</tbody></table></div>
<p>Ces distances sont des repères : l'ingénieur peut les augmenter s'il calcule les effets thermiques, ou les réduire pour une forme irrégulière.</p>
<h2>Joint de dilatation et joint sismique</h2>
<p>Au Maroc, le règlement parasismique RPS 2000 version 2011 ajoute une exigence : deux blocs voisins doivent être séparés par un <b>joint sismique</b> assez large pour qu'ils ne s'entrechoquent pas lors d'un séisme. Les textes fixent une largeur minimale de <b>5 cm</b>, à augmenter en fonction de la hauteur des blocs et des déplacements calculés. En pratique, le joint de dilatation est dimensionné pour servir aussi de joint sismique. Le joint est aussi recommandé entre deux parties de hauteurs ou de formes très différentes (bloc en L, partie R+3 accolée à un R+1).</p>
<h2>Bien réaliser un joint</h2>
<ul>
<li><b>Coupure complète</b> de la structure du sol au toit (poteaux et poutres doublés de part et d'autre) ; les fondations peuvent rester communes, sauf sol hétérogène.</li>
<li><b>Joint vide</b> : pas de gravats ni de mortier coincés dedans, sinon il ne joue plus.</li>
<li><b>Couvre-joints</b> en façade, en toiture et au sol, qui laissent le mouvement se faire.</li>
<li><b>Étanchéité</b> traitée par un relevé spécifique sur la toiture-terrasse (voir <a href="conseil-etancheite-toiture-terrasse-maroc.html">étanchéité de toiture-terrasse</a>).</li>
<li><b>Réseaux</b> (canalisations, câbles) équipés de manchons souples au passage du joint.</li>
</ul>
<h2>Le rôle du bureau d'études</h2>
<p>Le bureau d'études découpe le bâtiment en blocs dès la conception, en tenant compte du climat, de la forme et du RPS, et dimensionne la largeur des joints. Des <a href="conseil-fissures-maison-causes-gravite.html">fissures</a> régulières sur un long bâtiment sans joint sont souvent le signe que cette étape a été oubliée.</p>
""",
 "faq": [
  ("Tous les combien de mètres faut-il un joint de dilatation ?", "En climat chaud et sec comme à Marrakech, les règles BAEL conduisent à environ 25 m entre joints pour une structure en béton armé ; jusqu'à 50 m en climat humide et tempéré."),
  ("Quelle largeur pour un joint sismique au Maroc ?", "Le RPS 2000 version 2011 fixe une largeur minimale de 5 cm entre blocs, à augmenter selon la hauteur des bâtiments et les déplacements calculés."),
  ("Une villa a-t-elle besoin d'un joint de dilatation ?", "Une villa compacte de moins de 25 m de long n'en a généralement pas besoin, sauf forme très irrégulière ou parties de hauteurs différentes, à apprécier par l'ingénieur."),
 ],
 "sources": [
  ("https://www.smabtp.fr/sma/upload/docs/application/pdf/2025-04/b1_mur_facade_maconnerie_blocs_beton.pdf", "SMABTP, murs de façade en maçonnerie de blocs"),
  ("https://www.preventionweb.net/files/21648_13356rps20021.pdf?startDownload=true", "Ministère de l'Habitat, règlement parasismique RPS 2000"),
 ],
},
{
 "slug": "conseil-mur-de-soutenement-calcul",
 "cat": "structure",
 "title": "Mur de soutènement : calcul, drainage et erreurs à éviter",
 "crumb": "Mur de soutènement",
 "desc": "Un mur de soutènement se vérifie au renversement, au glissement et à la portance du sol. Poussée des terres, drainage, barbacanes : à faire calculer dès 1,50 m.",
 "lead": "Un mur de soutènement retient des tonnes de terre et souvent de l'eau. Mal conçu ou mal drainé, il bascule ou se fissure : c'est un ouvrage à faire calculer.",
 "img": "images/projects/project2.jpg",
 "min": 5,
 "body": """
<p>Un mur de soutènement se calcule à partir de la <b>poussée des terres</b> qu'il retient, des surcharges (voitures, construction en amont) et de la présence d'eau. On vérifie qu'il ne <b>bascule pas</b>, ne <b>glisse pas</b>, que le sol sous sa semelle le <b>porte</b> et que le béton et les aciers résistent. Les assureurs recommandent une étude par un bureau d'études au-delà de 1,50 m de hauteur retenue, et le drainage est aussi important que le calcul.</p>
<h2>Les forces en jeu</h2>
<p>La poussée des terres augmente avec la profondeur : elle est nulle en haut du mur et maximale à sa base. Elle dépend de la nature du sol (densité, angle de frottement, cohésion). Une voiture garée en haut, une maison voisine ou une piscine ajoutent une surcharge. Surtout, l'eau accumulée derrière un mur non drainé ajoute une poussée hydrostatique qui peut doubler les efforts. Dans une zone sismique comme Marrakech, le séisme augmente aussi la poussée.</p>
<h2>Les quatre vérifications</h2>
<div class="tableau"><table><thead><tr><th>Vérification</th><th>Risque évité</th><th>Moyens</th></tr></thead><tbody>
<tr><td>Renversement</td><td>Le mur bascule vers l'aval</td><td>Semelle plus large, talon sous les terres</td></tr>
<tr><td>Glissement</td><td>Le mur glisse sur sa base</td><td>Bêche sous la semelle, semelle plus large</td></tr>
<tr><td>Portance du sol</td><td>Le sol cède sous l'avant de la semelle</td><td>Semelle dimensionnée sur l'étude de sol</td></tr>
<tr><td>Résistance du mur</td><td>Le voile se fissure ou se rompt</td><td>Épaisseur et ferraillage calculés</td></tr>
</tbody></table></div>
<h2>Les types de murs</h2>
<ul>
<li><b>Mur en béton armé en « T renversé »</b> : un voile encastré sur une semelle avec un patin à l'avant et un talon sous les terres. C'est la solution la plus courante pour une villa.</li>
<li><b>Mur poids</b> en maçonnerie, pierre ou béton non armé : il résiste par sa masse, adapté aux faibles hauteurs.</li>
<li><b>Murs en gabions ou blocs</b> : drainants par nature, adaptés aux aménagements extérieurs.</li>
</ul>
<h2>Le drainage, point faible des murs sinistrés</h2>
<p>Une part importante des sinistres de murs de soutènement vient d'une mauvaise évacuation de l'eau. Un mur bien conçu comporte :</p>
<ul>
<li><b>Un massif drainant</b> en gravier derrière le mur, séparé de la terre par un géotextile.</li>
<li><b>Un drain</b> en pied, raccordé à un exutoire.</li>
<li><b>Des barbacanes</b> : tubes traversant le mur, légèrement inclinés vers l'aval, qui laissent sortir l'eau.</li>
<li><b>Une étanchéité ou un enduit bitumineux</b> sur la face contre terre si le mur borde un local.</li>
</ul>
<p>Les barbacanes et drains doivent être entretenus : bouchés, ils rendent le mur aussi vulnérable que s'il n'en avait pas.</p>
<h2>Le rôle du bureau d'études</h2>
<p>Le bureau d'études s'appuie sur l'<a href="conseil-etude-de-sol-maroc-prix.html">étude de sol</a> pour calculer le mur, fournit les plans de coffrage et de ferraillage et les détails de drainage. Pour un sous-sol enterré, le mur de soutènement est aussi la paroi du local : voir notre article sur le <a href="conseil-sous-sol-cuvelage-infiltrations.html">cuvelage des sous-sols</a>.</p>
""",
 "faq": [
  ("À partir de quelle hauteur faire calculer un mur de soutènement ?", "Les assureurs recommandent une étude par un bureau d'études au-delà de 1,50 m de terre retenue, et dès qu'il y a une surcharge en amont ou de l'eau."),
  ("À quoi servent les barbacanes ?", "Ce sont des tubes traversant le mur qui évacuent l'eau accumulée derrière lui ; sans elles, la pression de l'eau s'ajoute à la poussée des terres."),
  ("Pourquoi un mur de soutènement bascule-t-il ?", "Le plus souvent à cause d'une semelle trop étroite, d'une surcharge non prévue ou d'un drainage absent ou bouché qui laisse l'eau pousser sur le mur."),
 ],
 "sources": [
  ("https://qualiteconstruction.com/wp-content/uploads/2024/05/Plaquette-Murs-Soutenement-Bonnes-Pratiques-Conception-Execution-AQC.pdf", "AQC, murs de soutènement, bonnes pratiques"),
  ("https://rect.smabtp.fr/sma/upload/docs/application/pdf/2022-10/mur_de_soutenement_fiche_patho_.pdf", "SMABTP, fiche pathologie mur de soutènement"),
  ("https://ft.univ-tlemcen.dz/assets/uploads/pdf/departement/gc/chap3_soutenements.pdf", "Université de Tlemcen, cours sur les soutènements"),
 ],
},
{
 "slug": "conseil-remontees-capillaires-murs",
 "cat": "structure",
 "title": "Remontées capillaires dans les murs : causes et traitements",
 "crumb": "Remontées capillaires",
 "desc": "Salpêtre, enduit qui se décolle en pied de mur : les remontées capillaires se traitent par coupure de capillarité, injection, drainage et enduits à la chaux.",
 "lead": "Humidité en pied de mur, auréoles, salpêtre : les remontées capillaires sont fréquentes dans les maisons anciennes et les riads. Comment les reconnaître et les traiter durablement.",
 "img": "images/services/1.jpg",
 "min": 5,
 "body": """
<p>Les remontées capillaires sont l'humidité du sol qui monte dans les murs par les pores des matériaux, comme dans une mèche. Elles se traitent en <b>coupant le chemin de l'eau</b> : barrière étanche à la base des murs (arase ou injection), réduction de l'eau autour des fondations (drainage, pentes) et enduits qui laissent le mur sécher. Peindre ou enduire au ciment par-dessus ne fait que déplacer le problème.</p>
<h2>Les reconnaître</h2>
<ul>
<li><b>Une bande humide</b> en bas des murs, souvent jusqu'à un mètre de hauteur environ, avec une limite irrégulière.</li>
<li><b>Du salpêtre</b> : dépôts blancs et poudreux de sels qui cristallisent en surface.</li>
<li><b>Des enduits et peintures qui cloquent</b> et se décollent, des plinthes qui pourrissent.</li>
<li><b>Le phénomène persiste</b> en saison sèche, contrairement à la condensation ou aux infiltrations de pluie.</li>
</ul>
<p>Avant tout traitement, il faut écarter les autres causes : fuite de canalisation, infiltration par la façade ou la terrasse, condensation. Un diagnostic avec mesures d'humidité évite de traiter la mauvaise cause.</p>
<h2>Pourquoi les maisons anciennes sont touchées</h2>
<p>Les constructions récentes comportent normalement une <b>coupure de capillarité</b> (arase étanche) au-dessus des fondations ou des longrines. Les maisons anciennes, les riads de la médina et les murs en pisé ou en pierre n'en ont pas. Le problème s'aggrave quand on recouvre ces murs d'enduits ciment ou de carrelage étanches, ou quand le niveau de la rue ou du patio a été rehaussé au fil des années.</p>
<h2>Les solutions</h2>
<div class="tableau"><table><thead><tr><th>Solution</th><th>Principe</th><th>Remarques</th></tr></thead><tbody>
<tr><td>Injection de résine hydrofuge</td><td>Perçages rapprochés à la base du mur, injection d'un produit qui bouche les pores</td><td>Efficacité variable selon le mur ; délicate dans les murs épais hétérogènes</td></tr>
<tr><td>Arase étanche (coupure mécanique)</td><td>Insertion d'une barrière étanche dans le mur, par tronçons</td><td>Efficace mais lourde ; à étudier sur un mur porteur</td></tr>
<tr><td>Drainage périphérique</td><td>Éloigner l'eau des fondations</td><td>Utile si le sol est gorgé d'eau ou mal drainé</td></tr>
<tr><td>Enduits à la chaux</td><td>Laisser le mur sécher et les sels sortir</td><td>Complément indispensable, notamment sur pisé et pierre</td></tr>
</tbody></table></div>
<h2>Les erreurs fréquentes</h2>
<ul>
<li>Appliquer un enduit ciment ou une peinture étanche : l'humidité monte plus haut.</li>
<li>Traiter sans corriger la cause extérieure (gouttière, arrosage contre le mur, sol de patio en contre-pente).</li>
<li>Refaire les enduits tout de suite après une injection : le mur a besoin de temps pour sécher, souvent plusieurs mois selon son épaisseur.</li>
<li>Arroser les jardinières ou les plantations directement au pied des façades, ce qui entretient l'humidité du sol.</li>
</ul>
<h2>Le rôle du bureau d'études</h2>
<p>Le bureau d'études établit le diagnostic et choisit une solution compatible avec la structure : sur un mur porteur ou une maçonnerie traditionnelle, une arase mal exécutée peut fragiliser le mur. En construction neuve, il prévoit la coupure de capillarité au-dessus des <a href="conseil-longrines-role-dimension.html">longrines</a>. Pour un achat, voir aussi <a href="conseil-verifier-plomberie-humidite-avant-achat.html">vérifier l'humidité avant achat</a>.</p>
""",
 "faq": [
  ("Comment savoir si c'est une remontée capillaire ?", "L'humidité forme une bande en bas des murs, souvent avec du salpêtre, et persiste en saison sèche. Un diagnostic doit écarter fuites, infiltrations et condensation."),
  ("L'injection de résine contre l'humidité est-elle efficace ?", "Elle peut l'être sur des murs homogènes, mais son efficacité est variable dans les murs épais et hétérogènes ; elle doit être associée à la suppression des causes extérieures."),
  ("Quel enduit pour un mur humide de riad ?", "Un enduit respirant à la chaux, qui laisse le mur sécher ; les enduits ciment et peintures étanches aggravent les remontées."),
 ],
 "sources": [
  ("https://qualiteconstruction.com/wp-content/uploads/2024/01/fi-pathologie-batiment-b01-remontees-capillaires.pdf", "AQC, fiche pathologie remontées capillaires"),
 ],
},
{
 "slug": "conseil-acier-ha-fe500-diametres",
 "cat": "structure",
 "title": "Acier HA FeE500 : diamètres, sections et poids au mètre",
 "crumb": "Acier HA FeE500",
 "desc": "Tableau des aciers HA : HA6 = 0,222 kg/m, HA8 = 0,395, HA10 = 0,617, HA12 = 0,888, HA14 = 1,21, HA16 = 1,58 kg/m. Sections, usages et calcul du poids d'acier.",
 "lead": "Pour lire un plan de ferraillage, estimer une commande d'acier ou vérifier une facture, il faut connaître la section et le poids au mètre de chaque diamètre de barre.",
 "img": "images/services/beton-poutre.jpg",
 "min": 5,
 "body": """
<p>L'acier HA FeE500 est l'acier à haute adhérence le plus utilisé dans le béton armé au Maroc : « HA » désigne les nervures qui améliorent l'accrochage au béton, et « 500 » sa limite d'élasticité de 500 MPa. Un HA10 pèse <b>0,617 kg par mètre</b>, un HA12 <b>0,888 kg/m</b> et un HA14 <b>1,21 kg/m</b>.</p>
<h2>Tableau des diamètres courants</h2>
<div class="tableau"><table><thead><tr><th>Diamètre</th><th>Section (cm²)</th><th>Poids (kg/m)</th><th>Usages courants</th></tr></thead><tbody>
<tr><td>HA6</td><td>0,28</td><td>0,222</td><td>Cadres et étriers légers</td></tr>
<tr><td>HA8</td><td>0,50</td><td>0,395</td><td>Cadres de poteaux et poutres, dalles</td></tr>
<tr><td>HA10</td><td>0,79</td><td>0,617</td><td>Chaînages, dalles, poutrelles</td></tr>
<tr><td>HA12</td><td>1,13</td><td>0,888</td><td>Poteaux, poutres, semelles</td></tr>
<tr><td>HA14</td><td>1,54</td><td>1,21</td><td>Poteaux et poutres plus chargés</td></tr>
<tr><td>HA16</td><td>2,01</td><td>1,58</td><td>Poutres de grande portée, radiers</td></tr>
<tr><td>HA20</td><td>3,14</td><td>2,47</td><td>Ouvrages lourds</td></tr>
</tbody></table></div>
<p>Le poids se retrouve avec la formule : poids (kg/m) ≈ 0,00617 × d², avec d en millimètres, la masse volumique de l'acier étant de 7 850 kg/m³. Les usages indiqués sont des tendances ; le diamètre de chaque barre est fixé par le calcul.</p>
<h2>Comment lire un plan de ferraillage</h2>
<p>Une indication comme « 4 HA12 » signifie quatre barres de 12 mm, soit 4 × 1,13 = 4,52 cm² d'acier. « Cadres HA8 e = 15 » signifie des cadres en 8 mm espacés de 15 cm. Pour une dalle, « HA10 e = 20 » désigne des barres de 10 mm tous les 20 cm, soit environ 3,9 cm² par mètre de largeur. Ces sections sont celles que l'ingénieur a calculées : remplacer un diamètre par un plus petit réduit fortement la résistance.</p>
<h2>Calculer un poids d'acier</h2>
<ul>
<li><b>Poteau</b> de 3 m avec 4 HA12 : 4 × 3 m × 0,888 = 10,7 kg, plus les recouvrements et les cadres.</li>
<li><b>Cadres HA8</b> de 1 m de développé tous les 15 cm sur 3 m : 20 cadres × 0,395 = 7,9 kg.</li>
<li>Ajoutez une marge pour les chutes et les recouvrements, souvent de quelques pourcents à plus de 10 % selon l'optimisation du façonnage.</li>
</ul>
<h2>Qualité et stockage</h2>
<p>Exigez un acier certifié, avec le marquage du fabricant et de la nuance, et vérifiez sur le bon de livraison qu'il s'agit bien de FeE500 et des diamètres commandés. Sur chantier, stockez l'acier hors du sol ; une fine rouille superficielle n'est pas gênante, mais l'acier qui s'écaille ou perd de la matière doit être refusé. La terre, l'huile de décoffrage et le ciment séché nuisent à l'adhérence.</p>
<h2>Le rôle du bureau d'études</h2>
<p>Le bureau d'études calcule les sections d'acier, les traduit en diamètres et en espacements sur les plans, et peut fournir des nomenclatures d'acier qui permettent de commander au plus juste. Il vérifie ensuite sur place, lors du <a href="conseil-controle-ferraillage-avant-coulage.html">contrôle du ferraillage</a>, que les diamètres posés sont bien ceux des plans. Pour le béton associé, voir les <a href="conseil-classe-beton-b25-c25-30.html">classes de béton</a>.</p>
""",
 "faq": [
  ("Combien pèse un mètre de fer de 12 ?", "Une barre HA12 pèse 0,888 kg par mètre, soit environ 10,7 kg pour une barre de 12 m. Sa section est de 1,13 cm²."),
  ("Que signifie FeE500 ?", "C'est un acier à haute adhérence dont la limite d'élasticité garantie est de 500 MPa ; c'est la nuance la plus courante pour le béton armé."),
  ("Comment calculer le poids d'une barre d'acier ?", "Poids (kg/m) ≈ 0,00617 × d², avec d en millimètres : pour un HA10, 0,00617 × 100 = 0,617 kg/m."),
 ],
 "sources": [
  ("https://travail-industrie.com/blog/article-titre/fer-a-beton-ha-diametres-poids-metre-sections-tableau", "Travail Industrie, fer à béton HA : diamètres, poids, sections"),
  ("https://macalculatriceenligne.com/construction/calcul-poids-acier/", "Ma calculatrice en ligne, calcul du poids d'acier"),
 ],
},
{
 "slug": "conseil-classe-beton-b25-c25-30",
 "cat": "structure",
 "title": "Classes de béton B25, C25/30, C30/37 : que signifient-elles ?",
 "crumb": "Classes de béton",
 "desc": "C25/30 = 25 MPa sur cylindre et 30 MPa sur cube à 28 jours ; B25 (BAEL) = en général 25 MPa sur cylindre. Quelle classe pour une villa et comment la contrôler.",
 "lead": "Sur les plans et dans les cahiers des charges, le béton est désigné par une classe de résistance. Savoir la lire permet de commander le bon béton et de vérifier ce qui est livré.",
 "img": "images/services/maison-beton.jpg",
 "min": 5,
 "body": """
<p>La classe <b>C25/30</b> désigne un béton dont la résistance caractéristique à la compression à 28 jours est de <b>25 MPa mesurée sur cylindre</b> et de <b>30 MPa mesurée sur cube</b> : ce sont deux façons de mesurer la même qualité de béton. L'ancienne désignation <b>B25</b>, encore courante dans les CPS marocains rédigés selon le BAEL, renvoie en général à une résistance de 25 MPa à 28 jours sur cylindre, proche d'un C25/30. Faites toujours préciser la norme de référence.</p>
<h2>Lire une classe de béton</h2>
<p>Dans la désignation européenne (norme EN 206, Eurocode 2), la lettre C signifie « concrete » ; le premier nombre est la résistance sur cylindre de 15 × 30 cm, le second sur cube de 15 cm de côté, tous deux en MPa à 28 jours. Le cube donne une valeur plus élevée que le cylindre pour un même béton, d'où les deux chiffres. Avec le BAEL, la résistance de calcul est notée fc28, mesurée sur cylindre. Attention : dans d'autres systèmes de normes, une lettre B suivie d'un nombre peut désigner une résistance sur cube ; en cas de doute, demandez la précision par écrit.</p>
<div class="tableau"><table><thead><tr><th>Classe</th><th>Cylindre (MPa)</th><th>Cube (MPa)</th><th>Usage courant (indicatif)</th></tr></thead><tbody>
<tr><td>C20/25</td><td>20</td><td>25</td><td>Béton armé peu sollicité, dallages</td></tr>
<tr><td>C25/30</td><td>25</td><td>30</td><td>Structure courante de villa et petit immeuble</td></tr>
<tr><td>C30/37</td><td>30</td><td>37</td><td>Ouvrages plus sollicités ou exposés, piscines, parkings</td></tr>
<tr><td>C35/45</td><td>35</td><td>45</td><td>Ouvrages exigeants, milieux agressifs</td></tr>
</tbody></table></div>
<h2>Classe de résistance et classe d'exposition</h2>
<p>La résistance n'est pas le seul critère. La durabilité dépend de l'environnement : intérieur sec, extérieur, contact avec l'eau, sols agressifs, milieu marin. La norme EN 206 définit des <b>classes d'exposition</b> (XC, XS, XD, XA…) qui imposent un dosage minimal en ciment, un rapport eau/ciment maximal et parfois une résistance minimale. Une piscine, un réservoir ou une fondation en sol agressif peuvent ainsi exiger un béton plus performant que ne l'imposerait le seul calcul de résistance. Le choix de la classe et de l'<a href="conseil-enrobage-armatures-beton.html">enrobage</a> vont de pair.</p>
<h2>Obtenir réellement la classe demandée</h2>
<ul>
<li><b>Béton de centrale</b> : commander la classe de résistance, la classe d'exposition et la consistance, et vérifier le bon de livraison de chaque camion.</li>
<li><b>Béton de chantier</b> : un dosage à 350 kg de ciment par m³ bien exécuté permet couramment d'atteindre une classe de l'ordre de C25/30, mais sans garantie ; la qualité des granulats et la quantité d'eau changent tout (voir le <a href="conseil-dosage-beton-fondation-dalle.html">dosage du béton</a>).</li>
<li><b>Éprouvettes</b> : prélever des éprouvettes lors des coulages importants et les faire écraser par un laboratoire à 7 et 28 jours.</li>
<li><b>Pas d'eau ajoutée</b> sur chantier : c'est la première cause de béton déclassé.</li>
</ul>
<h2>Le rôle du bureau d'études</h2>
<p>Le bureau d'études fixe la classe de résistance et la classe d'exposition de chaque ouvrage dans ses notes de calcul et le cahier des charges. Il peut exiger des essais et interpréter les résultats : un béton qui n'atteint pas sa classe impose de recalculer l'ouvrage, voire de le renforcer.</p>
""",
 "faq": [
  ("Que signifie C25/30 ?", "C'est un béton dont la résistance caractéristique à 28 jours est de 25 MPa sur cylindre et de 30 MPa sur cube, selon la norme EN 206."),
  ("B25 et C25/30, est-ce la même chose ?", "Dans un CPS rédigé selon le BAEL, B25 désigne généralement un béton de 25 MPa sur cylindre à 28 jours, proche d'un C25/30. Faites préciser la norme de référence, car d'autres systèmes mesurent sur cube."),
  ("Quelle classe de béton pour une villa ?", "Une classe C25/30 est courante pour la structure d'une villa ; l'ingénieur peut demander davantage pour les piscines, les ouvrages enterrés ou exposés."),
 ],
 "sources": [
  ("https://travail-industrie.com/blog/article-titre/beton-c25-30-c35-45-c50-60-classe-resistance-comment-choisir", "Travail Industrie, classes de résistance du béton"),
  ("https://www.afgc.asso.fr/app/uploads/2016/10/5_1_NI_Caracteristiques_mecaniques_des_betons.pdf", "AFGC, caractéristiques mécaniques des bétons"),
  ("https://holcim.ch/sites/switzerland/files/docs/betonnorm_sn-en-206_fr.pdf", "Holcim, la norme béton EN 206"),
 ],
},
{
 "slug": "conseil-reprise-en-sous-oeuvre-fondations",
 "cat": "structure",
 "title": "Reprise en sous-œuvre des fondations : quand et comment ?",
 "crumb": "Reprise en sous-œuvre",
 "desc": "Tassement, surélévation, sous-sol à creuser : la reprise en sous-œuvre renforce des fondations existantes par plots alternés, micropieux ou injections.",
 "lead": "Renforcer ou approfondir les fondations d'un bâtiment existant sans le démolir est possible. C'est une opération délicate, qui se conçoit et se surveille avec soin.",
 "img": "images/projects/project3.jpg",
 "min": 5,
 "body": """
<p>La reprise en sous-œuvre consiste à <b>renforcer, élargir ou approfondir les fondations</b> d'un bâtiment existant, sans le démolir. On y recourt quand les fondations tassent, quand on veut ajouter un étage ou creuser un sous-sol, ou quand des travaux voisins déstabilisent le sol. Les techniques principales sont les <b>plots en béton coulés par passes alternées</b>, les <b>micropieux</b> et l'<b>injection</b> du sol.</p>
<h2>Les situations qui l'imposent</h2>
<ul>
<li><b>Tassements différentiels</b> : fissures en escalier ou en biais, portes qui coincent, sols qui penchent.</li>
<li><b>Surélévation</b> : les fondations d'origine ne suffisent plus pour porter un ou deux niveaux de plus (voir <a href="conseil-surelevation-ajouter-etage-maroc.html">ajouter un étage</a>).</li>
<li><b>Creusement d'un sous-sol</b> ou d'une piscine près des murs existants.</li>
<li><b>Fondations dégradées</b> par des fuites d'eau, un sol lessivé ou un terrassement voisin.</li>
</ul>
<h2>Les techniques</h2>
<div class="tableau"><table><thead><tr><th>Technique</th><th>Principe</th><th>Cas d'emploi</th></tr></thead><tbody>
<tr><td>Plots en passes alternées</td><td>On creuse sous la fondation par tronçons courts, non contigus, et on coule du béton jusqu'au bon sol</td><td>Bon sol accessible à faible profondeur</td></tr>
<tr><td>Micropieux</td><td>Pieux de petit diamètre (généralement moins de 25 à 30 cm) forés et armés, reliés à la fondation par une poutre ou des massifs</td><td>Bon sol profond, accès réduit, charges importantes</td></tr>
<tr><td>Injection du sol</td><td>Coulis ou résine injectés pour consolider le sol sous la fondation</td><td>Sols meubles ou décomprimés, selon diagnostic</td></tr>
<tr><td>Élargissement de semelle</td><td>Semelle existante élargie et liaisonnée par des aciers scellés</td><td>Charges en hausse sur un sol correct</td></tr>
</tbody></table></div>
<h2>Pourquoi travailler par passes alternées</h2>
<p>Creuser sous tout un mur d'un coup le laisserait sans appui. On travaille donc par tronçons courts, en sautant un tronçon sur deux ou trois : on reprend d'abord les tronçons 1, 3, 5, puis, une fois le béton durci, les tronçons 2, 4, 6. La longueur des tronçons et l'ordre des passes sont fixés par l'ingénieur selon l'état du mur et du sol. Le clavage, c'est-à-dire le remplissage serré entre l'ancienne fondation et le nouveau béton, est essentiel pour que la charge soit réellement transférée.</p>
<h2>Les précautions indispensables</h2>
<ul>
<li><b>Diagnostic préalable</b> : étude de sol, sondages au pied des fondations existantes, relevé des fissures.</li>
<li><b>Étaiement</b> des planchers si nécessaire et surveillance des fissures (témoins, repères de nivellement).</li>
<li><b>Traitement de la cause</b> : réparer la fuite ou le réseau qui a lessivé le sol, sinon le problème reviendra.</li>
<li><b>Entreprise expérimentée</b> : ce n'est pas un travail de maçonnerie courante.</li>
<li><b>Information des voisins</b> en mitoyenneté : les fondations voisines peuvent être concernées et un constat de l'état de leurs murs avant travaux est prudent.</li>
</ul>
<h2>Le rôle du bureau d'études</h2>
<p>Le bureau d'études analyse la cause des désordres, choisit la technique avec le géotechnicien, calcule les nouveaux appuis et définit le phasage. Il suit ensuite les travaux pour adapter le phasage au sol réellement rencontré. Si des fissures vous inquiètent, notre article sur les <a href="conseil-fissures-maison-causes-gravite.html">fissures dans une maison</a> aide à évaluer leur gravité.</p>
""",
 "faq": [
  ("Qu'est-ce qu'une reprise en sous-œuvre ?", "C'est le renforcement, l'élargissement ou l'approfondissement des fondations d'un bâtiment existant, par plots en béton, micropieux ou injections, sans démolir l'ouvrage."),
  ("Pourquoi creuser par passes alternées ?", "Pour ne jamais laisser un mur sans appui : on reprend des tronçons courts non contigus, puis les tronçons intermédiaires une fois le béton durci."),
  ("Quand utiliser des micropieux ?", "Quand le bon sol est profond, que l'accès est réduit ou que les charges sont importantes ; ce sont des pieux de petit diamètre forés et armés."),
 ],
 "sources": [
  ("https://piles.cerema.fr/IMG/pdf/les_micropieux_guide_technique_1986_cle26d714.pdf", "Cerema (SETRA-LCPC), les micropieux, guide technique"),
  ("https://www.terrasol.fr/wp-content/uploads/2010/11/AFTES00322_Orci_p62.pdf", "Terrasol, reprise en sous-œuvre de bâtiments sensibles"),
 ],
},
{
 "slug": "conseil-sous-sol-cuvelage-infiltrations",
 "cat": "structure",
 "title": "Sous-sol : cuvelage, étanchéité et infiltrations d'eau",
 "crumb": "Sous-sol et cuvelage",
 "desc": "Structure relativement étanche, revêtement d'imperméabilisation ou d'étanchéité (DTU 14.1) : comment protéger un sous-sol des infiltrations dès la conception.",
 "lead": "Un sous-sol qui prend l'eau est l'un des défauts les plus coûteux à reprendre. La protection se décide dès la conception, en fonction de l'eau présente dans le sol.",
 "img": "images/projects/villa1.jpg",
 "min": 5,
 "body": """
<p>Pour protéger un sous-sol, la solution dépend de l'eau qu'il devra affronter : un simple <b>drainage avec enduit d'imperméabilisation</b> peut suffire en sol sec et drainant ; en présence d'une nappe ou d'eau sous pression, il faut un <b>cuvelage</b>, c'est-à-dire une enveloppe étanche capable de résister à la pression de l'eau. La référence technique la plus utilisée est le DTU 14.1 français, révisé en 2020.</p>
<h2>Connaître l'eau du terrain</h2>
<p>Tout commence par l'étude de sol : niveau de la nappe et ses variations, perméabilité du sol, risque d'eau de ruissellement ou de fuites de réseaux. À Marrakech, la nappe est souvent profonde, mais les sous-sols subissent les eaux d'arrosage des jardins, des piscines voisines, des fuites de canalisations et les orages violents. Un sous-sol de villa voisin d'une piscine ou d'un jardin très arrosé doit être traité comme exposé à l'eau.</p>
<h2>Les trois familles de cuvelage</h2>
<div class="tableau"><table><thead><tr><th>Type</th><th>Principe</th><th>Usage</th></tr></thead><tbody>
<tr><td>Structure relativement étanche</td><td>Le béton armé lui-même assure l'étanchéité : épaisseur, ferraillage et fissuration maîtrisés, joints traités</td><td>Parkings, locaux tolérant une légère humidité</td></tr>
<tr><td>Revêtement d'imperméabilisation</td><td>Enduit ou mortier hydrofuge appliqué côté intérieur, adhérent au béton</td><td>Locaux techniques, caves, réhabilitation</td></tr>
<tr><td>Revêtement d'étanchéité</td><td>Membrane continue, généralement côté extérieur, protégée</td><td>Locaux habités exigeant une étanchéité parfaite</td></tr>
</tbody></table></div>
<p>Le choix dépend de l'usage du local : un parking tolère quelques traces d'humidité, une chambre, un home cinéma ou un local technique électrique non.</p>
<h2>Les points faibles à soigner</h2>
<ul>
<li><b>Les reprises de bétonnage</b> entre radier et voiles, et entre levées de voiles : joints waterstop ou bandes d'arrêt d'eau.</li>
<li><b>Les traversées</b> de canalisations et de câbles : fourreaux étanches prévus avant coulage.</li>
<li><b>Les trous de banches</b> et écarteurs de coffrage, à boucher avec soin.</li>
<li><b>La fissuration</b> du béton, limitée par le ferraillage et une bonne <a href="conseil-cure-beton-chaleur-marrakech.html">cure</a>.</li>
<li><b>Le drainage périphérique</b> et l'évacuation des eaux pluviales loin des murs enterrés.</li>
</ul>
<h2>Que faire en cas d'infiltrations ?</h2>
<p>Identifiez d'abord l'origine : remontée de nappe, ruissellement, fuite de réseau, défaut ponctuel (reprise, traversée) ou condensation. Les fuites ponctuelles se traitent souvent par injection de résine dans la fissure ou le joint. Les infiltrations généralisées imposent un cuvelage intérieur résistant à la pression, ou un drainage extérieur si le terrain est accessible. Un simple enduit étanche sur un mur qui reçoit de l'eau sous pression finit généralement par se décoller. Pensez aussi à ventiler le sous-sol : une partie de l'humidité constatée vient souvent de la condensation sur les parois froides.</p>
<h2>Le rôle du bureau d'études</h2>
<p>Le bureau d'études choisit le type de cuvelage avec l'architecte selon l'usage, dimensionne le radier et les voiles pour la poussée des terres et de l'eau, et détaille les joints et traversées. Les voiles enterrés sont aussi des <a href="conseil-mur-de-soutenement-calcul.html">murs de soutènement</a>, et le radier relève du choix de <a href="conseil-type-fondation-semelle-radier.html">fondation</a>.</p>
""",
 "faq": [
  ("Qu'est-ce qu'un cuvelage ?", "C'est une enveloppe étanche qui protège un local enterré contre l'eau, y compris sous pression : béton armé relativement étanche, revêtement d'imperméabilisation ou revêtement d'étanchéité."),
  ("Comment arrêter une infiltration dans un sous-sol ?", "Il faut d'abord en trouver l'origine ; une fuite ponctuelle se traite souvent par injection, une infiltration généralisée par un cuvelage intérieur ou un drainage extérieur."),
  ("Un sous-sol à Marrakech a-t-il besoin d'un cuvelage ?", "Pas toujours, car la nappe est souvent profonde, mais l'eau d'arrosage, des piscines et des fuites peut atteindre les murs enterrés. L'étude de sol et l'usage du local décident."),
 ],
 "sources": [
  ("https://qualiteconstruction.com/wp-content/uploads/2026/01/Fiche-Maitrise-Ouvrage-Professionnelle-Cuvelage-AQC.pdf", "AQC, fiche cuvelage"),
  ("https://www.ffbatiment.fr/actualites-batiment/actualite-bam/coup-de-jeune-pour-les-travaux-de-cuvelage", "FFB, révision du DTU 14.1 cuvelage"),
  ("https://qualiteconstruction.com/wp-content/uploads/2024/05/Plaquette-Prevenir-Humidite-Sous-Sol-AQC.pdf", "AQC, prévenir l'humidité en sous-sol"),
 ],
},
]
