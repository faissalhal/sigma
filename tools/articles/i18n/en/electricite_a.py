# -*- coding: utf-8 -*-
T = {
 "conseil-combien-prises-par-circuit": {
   "title": "How many sockets per circuit? The NF C 15-100 rules explained",
   "crumb": "Sockets per circuit",
   "desc": "Sockets per circuit: max 8 outlets on 1.5 mm² with a 16 A breaker, 12 on 2.5 mm² with a 20 A breaker, 6 in the kitchen. Counting rules and a villa example.",
   "lead": "The number of sockets allowed on a circuit depends on the wire cross-section and the circuit breaker rating. Here are the NF C 15-100 benchmarks, the reference used by engineering firms in Morocco.",
   "body": """
<p>Under the NF C 15-100 rules (2002 edition as amended, still very widely applied), a 16 A socket-outlet circuit can supply <b>a maximum of 8 outlets if it is wired in 1.5 mm² and protected by a 16 A circuit breaker</b>, and <b>a maximum of 12 outlets if it is wired in 2.5 mm² and protected by a 20 A circuit breaker</b>. These limits prevent a single cable from being overloaded by too many appliances plugged in at the same time.</p>
<h2>The table to remember</h2>
<div class="tableau"><table><thead><tr><th>Conductor cross-section (copper)</th><th>Protection</th><th>Maximum number of outlets</th></tr></thead><tbody>
<tr><td>1.5 mm²</td><td>16 A circuit breaker</td><td>8</td></tr>
<tr><td>2.5 mm²</td><td>20 A circuit breaker</td><td>12</td></tr>
<tr><td>2.5 mm² (kitchen worktop sockets)</td><td>20 A circuit breaker</td><td>6, on a circuit dedicated to the kitchen</td></tr>
</tbody></table></div>
<p>A fuse is not an alternative to the circuit breaker for the 1.5 mm² circuit: in new installations, protection is provided by a miniature circuit breaker. Like every circuit, the socket circuit is also placed downstream of a 30 mA residual current device.</p>
<h2>How to count sockets</h2>
<ul>
<li><b>One outlet = one socket</b>: since the 2015 amendment, a double or triple socket block counts as 2 or 3 outlets. The old rules of counting per box no longer apply.</li>
<li><b>Dedicated sockets do not count</b>: the washing machine, oven, dishwasher or air conditioner have their own circuit (see <a href="conseil-circuits-specialises-nf-c-15-100.html">dedicated circuits</a>).</li>
<li><b>Switched sockets</b> (turned on by a light switch) count as sockets if they are on the socket circuit.</li>
</ul>
<h2>What this means in a villa</h2>
<p>A 200 m² villa in Marrakech easily has 40 to 60 socket outlets. With 2.5 mm² / 20 A circuits, you therefore need at least 4 to 5 socket circuits, not counting the kitchen circuits and the dedicated circuits. In practice, the engineering firm groups the sockets by zone (living room, bedrooms, outdoors, office) so that a fault does not cut power to the whole house, and to balance the loads between the residual current devices, or even between the phases in a three-phase supply.</p>
<p>Two tips from the field: avoid putting the sockets of an office with computer equipment on the same circuit as those of a room where a portable heater or an iron is plugged in during winter, and provide a dedicated circuit for outdoor sockets (garden, terrace, pool), which are more exposed to moisture.</p>
<h2>What about the Moroccan standard?</h2>
<p>In Morocco, standards NM 06.1.100 to 06.1.106 published by IMANOR govern low-voltage installations; NM 06.1.100 was approved in 2025. In specifications (CPS) and design studies, NF C 15-100 remains the most cited technical reference. Its 2024 edition replaced the 2002 edition and reorganises the standard into several parts: the engineering firm checks which edition applies to your contract and what the inspection body requires.</p>
<h2>The role of the engineering firm</h2>
<p>An electrical engineering firm draws up the single-line diagram, the number of circuits, the cross-sections and the ratings, taking into account cable lengths (voltage drop) and the power actually contracted with Radeema or ONEE. This file is what allows you to compare electricians' quotes on a clear basis. For the general framework, see also our article on <a href="conseil-norme-electrique-nf-c-15-100-maroc.html">the NF C 15-100 standard in Morocco</a>.</p>
""",
   "faq": [
     ("How many sockets on a 16 A circuit breaker?", "Under NF C 15-100, a 1.5 mm² circuit protected by a 16 A circuit breaker can supply a maximum of 8 socket outlets."),
     ("How many sockets on a 20 A circuit breaker?", "A 2.5 mm² circuit protected by a 20 A circuit breaker can supply up to 12 outlets, except in the kitchen where the worktop circuit is limited to 6 outlets."),
     ("Does a double socket count as one or two sockets?", "It counts as two: since the 2015 amendment to NF C 15-100, each outlet of a multiple block is counted separately."),
   ],
 },
 "conseil-circuits-specialises-nf-c-15-100": {
   "title": "Mandatory dedicated circuits: oven, washing machine, A/C and more",
   "crumb": "Dedicated circuits",
   "desc": "NF C 15-100 dedicated circuits: at least 4, incl. the hob on 6 mm² / 32 A and three 2.5 mm² / 20 A circuits (oven, washing machine…). A/C in Morocco.",
   "lead": "Some appliances must have their own line from the distribution board. Which ones, with what cross-section and which circuit breaker, and what to plan for an air-conditioned villa in Marrakech.",
   "body": """
<p>A dedicated circuit is a line running from the distribution board to supply <b>a single high-power appliance</b>. NF C 15-100 requires <b>at least 4 dedicated circuits</b> in a dwelling: one circuit for the cooker or hob (6 mm², 32 A circuit breaker in single-phase) and at least three circuits for appliances such as the washing machine, dishwasher, oven or tumble dryer, usually in 2.5 mm² protected by a 20 A circuit breaker.</p>
<h2>The list of dedicated circuits</h2>
<div class="tableau"><table><thead><tr><th>Appliance</th><th>Usual cross-section</th><th>Usual protection</th></tr></thead><tbody>
<tr><td>Hob or cooker (single-phase)</td><td>6 mm²</td><td>32 A circuit breaker</td></tr>
<tr><td>Hob (three-phase)</td><td>2.5 mm²</td><td>20 A circuit breaker</td></tr>
<tr><td>Oven, washing machine, dishwasher, tumble dryer</td><td>2.5 mm²</td><td>20 A circuit breaker</td></tr>
<tr><td>Single-phase electric water heater</td><td>2.5 mm²</td><td>20 A circuit breaker</td></tr>
<tr><td>Freezer</td><td>2.5 mm²</td><td>20 A circuit breaker (dedicated circuit recommended)</td></tr>
<tr><td>Air conditioner, heat pump, pool pump</td><td>Depending on power and manual</td><td>According to the manufacturer's instructions</td></tr>
</tbody></table></div>
<p>These values are the usual NF C 15-100 benchmarks (table of cross-sections and ratings reproduced by cable manufacturers). For powerful appliances or those far from the board, the cross-section is recalculated according to the length to limit voltage drop.</p>
<h2>Why one line per appliance</h2>
<ul>
<li><b>Avoid overloads</b>: an oven (2 to 3.5 kW) and a washing machine heating water on the same line quickly exceed 16 A.</li>
<li><b>Limit outages</b>: a fault on the washing machine must not cut off the refrigerator or the lighting.</li>
<li><b>Choose the right residual current device</b>: the washing machine and the hob must be downstream of a 30 mA type A residual current switch, see <a href="conseil-differentiel-30ma-type-ac-a-f.html">types AC, A and F</a>.</li>
</ul>
<h2>Air conditioning, a special case in Morocco</h2>
<p>In Marrakech, where summer temperatures regularly exceed 40 °C, air conditioning is often the largest consumption item. Each outdoor unit, each ducted unit and each VRV system must have its own dedicated circuit, sized according to the current stated by the manufacturer, with an isolating device nearby for maintenance. "Inverter" air conditioners contain variable-speed electronics: equipment manufacturers recommend a type F residual current device for them (or type A depending on the appliance). The villa's other equipment follows the same logic: pool pump, booster pump, motorised gate, charging point.</p>
<h2>Plan them at the design stage</h2>
<p>Adding a dedicated circuit afterwards means running a new line and often cutting new wall chases. The engineering firm prepares the power balance, lists all appliances (including those that will be bought later), sets the cross-sections and ratings, and checks that the board keeps sufficient spare capacity. For the kitchen in particular, read our article on <a href="conseil-four-plaque-cuisson-cable-disjoncteur.html">the cable and circuit breaker for the oven and hob</a>.</p>
""",
   "faq": [
     ("How many dedicated circuits does a house need?", "NF C 15-100 requires at least 4: a 32 A circuit for the hob or cooker and three circuits for appliances such as the washing machine, dishwasher and oven."),
     ("Must an electric water heater have its own circuit?", "Yes, the electric water heater is supplied by a dedicated circuit, commonly 2.5 mm² protected by a 20 A circuit breaker for a standard single-phase appliance."),
     ("Should an air conditioner be on a dedicated circuit?", "Yes, each air conditioner or outdoor unit must have its own line, sized according to the current given by the manufacturer and protected by a suitable residual current device, often type F for inverter models."),
   ],
 },
 "conseil-four-plaque-cuisson-cable-disjoncteur": {
   "title": "Oven and hob: which cable and which circuit breaker to choose?",
   "crumb": "Oven and hob",
   "desc": "Single-phase hob: 6 mm² cable and 32 A breaker under a type A RCD. Three-phase: 2.5 mm² and 20 A. Oven: dedicated 2.5 mm² / 20 A circuit. Mistakes to avoid.",
   "lead": "The kitchen concentrates the most powerful appliances in the house. Here are the usual cable cross-sections and circuit breaker ratings for the oven and hob, and frequent mistakes on site.",
   "body": """
<p>In single-phase, the hob (or cooker) is supplied by a <b>dedicated 6 mm² circuit protected by a 32 A circuit breaker</b>, placed downstream of a 30 mA type A residual current switch. The oven also has its own circuit, commonly <b>2.5 mm² protected by a 20 A circuit breaker</b>. In three-phase, the hob can be supplied in 2.5 mm² with a 20 A four-pole circuit breaker. These are the NF C 15-100 benchmarks, the reference most used by engineering firms in Morocco.</p>
<h2>The usual values</h2>
<div class="tableau"><table><thead><tr><th>Appliance</th><th>Supply</th><th>Cable cross-section</th><th>Circuit breaker</th></tr></thead><tbody>
<tr><td>Hob or cooker</td><td>Single-phase 230 V</td><td>6 mm²</td><td>32 A</td></tr>
<tr><td>Hob</td><td>Three-phase 400 V</td><td>2.5 mm² (5 conductors)</td><td>20 A</td></tr>
<tr><td>Built-in oven</td><td>Single-phase 230 V</td><td>2.5 mm²</td><td>20 A</td></tr>
<tr><td>Hood, microwave, small appliances</td><td>Single-phase 230 V</td><td>Kitchen socket circuit 2.5 mm²</td><td>20 A</td></tr>
</tbody></table></div>
<p>Some hob manufacturers or certain manuals specify other ratings for three-phase or two-phase connection: the appliance manual and the engineering firm's calculation note take precedence over generic tables.</p>
<h2>Connection: cable outlet or socket</h2>
<ul>
<li><b>Hob</b>: connection via a connection box (cable outlet) or a dedicated 32 A socket, placed so that it remains accessible under the worktop.</li>
<li><b>Oven</b>: dedicated 16 A or 20 A socket, or cable outlet depending on the model. A socket placed behind the oven must be possible to disconnect by pulling the appliance out.</li>
<li><b>Residual current device</b>: the hob circuit must be under a 30 mA type A residual current switch, because induction hobs generate leakage currents that type AC does not detect correctly.</li>
</ul>
<h2>Mistakes to avoid</h2>
<ol>
<li><b>Plugging the hob into a 16 A socket</b> with an extension lead or adapter: risk of overheating and fire.</li>
<li><b>Putting the oven and the hob on the same 32 A circuit</b>: each appliance must have its own circuit, except an all-in-one cooker.</li>
<li><b>Undersizing a long cable</b>: if the kitchen is far from the board (single-storey villa, summer kitchen near the pool), voltage drop may require a larger cross-section.</li>
<li><b>Forgetting three-phase</b>: in a villa with a three-phase connection, supplying the hob in three-phase spreads the load better between the phases.</li>
</ol>
<h2>The engineering firm's view</h2>
<p>In a villa or a high-end apartment, the kitchen may include an induction hob, two ovens, a dishwasher, an American-style refrigerator and a wine cooler. The engineering firm includes these loads in the electrical power balance, chooses the cross-sections, distributes the circuits between the residual current devices and checks the power to be contracted with the distributor. See also <a href="conseil-circuits-specialises-nf-c-15-100.html">mandatory dedicated circuits</a> and <a href="conseil-section-cable-calibre-disjoncteur.html">the cable cross-section / rating table</a>.</p>
""",
   "faq": [
     ("What cable size for an induction hob?", "In single-phase, the hob is supplied in 6 mm² with a 32 A circuit breaker, under a 30 mA type A residual current device; in three-phase, 2.5 mm² with a 20 A circuit breaker is the usual value."),
     ("Which circuit breaker for an electric oven?", "The oven has a dedicated circuit, commonly 2.5 mm² protected by a 20 A circuit breaker, unless the manufacturer's manual states otherwise."),
     ("Can the oven and hob be on the same circuit breaker?", "No, except for an all-in-one cooker: NF C 15-100 provides for one dedicated circuit for the hob and another for the oven."),
   ],
 },
 "conseil-disjoncteur-ou-differentiel-difference": {
   "title": "Circuit breaker or residual current switch: what is the difference?",
   "crumb": "Breaker or RCD",
   "desc": "The circuit breaker protects cables from overloads and short circuits; the 30 mA residual current device protects people from current leaks. Roles and choice.",
   "lead": "Three devices with similar names, three different roles in the distribution board. Understanding the difference helps you read a quote and know why a device \"trips\".",
   "body": """
<p>The <b>circuit breaker</b> protects cables and appliances against overloads and short circuits. The <b>residual current switch</b> protects people: it cuts the power as soon as it detects a leak to earth, for example when someone touches a live part. The <b>residual current circuit breaker</b> combines both functions in a single device. In a home distribution board, you generally find 30 mA residual current switches at the head of each row and miniature circuit breakers below them, one per circuit.</p>
<h2>The three devices side by side</h2>
<div class="tableau"><table><thead><tr><th>Device</th><th>What it detects</th><th>What it protects</th><th>Where it is found</th></tr></thead><tbody>
<tr><td>Miniature circuit breaker (10, 16, 20, 32 A…)</td><td>Overload, short circuit</td><td>The cables of one circuit</td><td>One per circuit</td></tr>
<tr><td>30 mA residual current switch</td><td>Earth leakage current</td><td>People</td><td>At the head of a group of circuits</td></tr>
<tr><td>Residual current circuit breaker</td><td>Both</td><td>Cables and people</td><td>Main incoming breaker, or a single circuit</td></tr>
</tbody></table></div>
<h2>The circuit breaker: protecting cables</h2>
<p>Each cable can carry a maximum current: 1.5 mm² for 16 A, 2.5 mm² for 20 A, 6 mm² for 32 A, according to the NF C 15-100 benchmarks. If too many appliances are plugged in, the cable heats up; the circuit breaker trips before the insulation deteriorates. In the event of a short circuit, it trips within a few milliseconds. Its rating is therefore chosen according to the cable cross-section, never according to the appliance alone (see <a href="conseil-section-cable-calibre-disjoncteur.html">the cross-section / rating table</a>).</p>
<h2>The residual current switch: protecting people</h2>
<p>It compares the current leaving through the phase with the current returning through the neutral. If more than 30 mA is missing, current is escaping elsewhere, through the earth or through a human body: it trips. It does not protect against overloads, hence the requirement for circuit breakers downstream. Its rating (25, 40 or 63 A) indicates the current it can carry, not its sensitivity. It comes in several types (AC, A, F) depending on the appliances protected: see <a href="conseil-differentiel-30ma-type-ac-a-f.html">which type of residual current device to choose</a>.</p>
<h2>The main incoming circuit breaker</h2>
<p>At the head of the installation, after the meter, is the main circuit breaker. Depending on the distributor and the type of connection, it is a residual current type (with a sensitivity of a few hundred milliamps, for example 500 mA): it then provides overall protection and cuts the whole dwelling. It does not replace the 30 mA residual current devices, which alone protect people against direct contact.</p>
<h2>What to do when it trips?</h2>
<ul>
<li><b>A miniature circuit breaker trips</b>: overload or short circuit on that circuit. Unplug the appliances and reset; if it trips again with nothing connected, there is a wiring fault.</li>
<li><b>A residual current switch trips</b>: current leakage on one of the circuits it protects, often a damp appliance or an outdoor socket. Switch off the circuit breakers one by one to find the faulty circuit.</li>
</ul>
<p>The engineering firm sets out the protection scheme in the single-line diagram: number and type of residual current devices, circuit breaker ratings, discrimination between protection levels. This is the document the electrician follows and the inspection body checks.</p>
""",
   "faq": [
     ("What is the difference between a circuit breaker and an RCD?", "The circuit breaker trips in the event of an overload or short circuit to protect the cables; the residual current device trips as soon as a current leak exceeds its sensitivity (30 mA) to protect people."),
     ("Is a residual current switch enough without a circuit breaker?", "No, the residual current switch does not protect against overloads: each circuit downstream must have its own circuit breaker suited to the cable cross-section."),
     ("What does 40 A mean on a 30 mA residual current switch?", "40 A is the maximum current it can carry; 30 mA is its sensitivity, i.e. the leakage current at which it trips."),
   ],
 },
 "conseil-differentiel-30ma-type-ac-a-f": {
   "title": "30 mA RCD type AC, A or F: which one for which circuit?",
   "crumb": "RCD type AC, A, F",
   "desc": "30 mA RCD: type AC for standard circuits, type A for the hob and washing machine, type F for inverter air conditioning and heat pumps. Selection table and tips.",
   "lead": "Not all 30 mA residual current switches detect the same leaks. The right type depends on the appliances connected, and the question matters in a Moroccan villa heavily equipped with air conditioning.",
   "body": """
<p><b>Type AC</b> detects standard alternating current leaks: it is suitable for lighting circuits, sockets and simple heaters. <b>Type A</b> also detects leaks with a DC component produced by electronics: NF C 15-100 requires it for the hob, the washing machine and the electric vehicle charging point. <b>Type F</b> adds detection of currents from single-phase frequency converters: it is recommended for inverter air conditioners, heat pumps and variable-speed pumps.</p>
<h2>The selection table</h2>
<div class="tableau"><table><thead><tr><th>Type</th><th>What it detects</th><th>Circuits concerned</th></tr></thead><tbody>
<tr><td>AC</td><td>Sinusoidal alternating leaks</td><td>Lighting, sockets, water heater, simple heaters</td></tr>
<tr><td>A</td><td>AC + pulsating DC leaks</td><td>Hob, washing machine, charging point, and any circuit where you want more margin</td></tr>
<tr><td>F</td><td>A + multi-frequency currents (single-phase drives)</td><td>Inverter air conditioner and heat pump, variable-speed pool pump, freezer (fewer nuisance trips)</td></tr>
<tr><td>B</td><td>F + smooth DC leaks</td><td>Three-phase equipment with drive or rectifier, some charging points</td></tr>
</tbody></table></div>
<p>Simple rule: a type A can always replace a type AC, and a type F a type A, but never the reverse where the higher type is required. Type A costs on average around 20% more than type AC, depending on the manufacturer.</p>
<h2>What the standard says</h2>
<ul>
<li><b>In the 2002 edition of NF C 15-100 as amended</b>, still widely applied: all circuits are protected by 30 mA residual current devices, and at least one type A residual current switch protects the hob and the washing machine.</li>
<li><b>In the 2024 edition</b>, in force in France since September 2025, manufacturers state that type F is required at the head of circuits supplying equipment with single-phase variable-speed drives. The details depend on the text applied: to be confirmed by the inspection body for your project.</li>
<li><b>In Morocco</b>, the NM 06.1.100 to 06.1.106 series of standards governs low-voltage installations; in specifications (CPS), NF C 15-100 remains the most cited reference.</li>
</ul>
<h2>The case of air-conditioned villas in Marrakech</h2>
<p>A villa may have six to ten inverter air conditioning units, a variable-speed pool pump and a booster pump. All these machines produce leakage currents that type AC detects poorly: either it does not trip when it should, or it trips for no apparent reason. Grouping this equipment under one or more type F residual current devices, while limiting the number of appliances per device, reduces nuisance tripping in the middle of summer. The freezer also benefits from a separate residual current device (type F or "high immunity") to avoid losing its contents after an unnoticed power cut.</p>
<h2>Distributing the residual current devices properly</h2>
<p>The choice of type goes hand in hand with the distribution of circuits: how many residual current devices, and which circuits under each. See <a href="conseil-nombre-interrupteurs-differentiels-maison.html">the number of residual current switches according to floor area</a> and <a href="conseil-disjoncteur-ou-differentiel-difference.html">the difference between a circuit breaker and a residual current device</a>. In a project overseen by an engineering firm, this choice appears on the single-line diagram, which prevents substitution with cheaper equipment on site.</p>
""",
   "faq": [
     ("Which RCD for a washing machine?", "The washing machine must be placed downstream of a 30 mA type A residual current switch, like the hob, according to NF C 15-100."),
     ("Which RCD for inverter air conditioning?", "Manufacturers recommend a 30 mA type F residual current device for single-phase inverter air conditioners and heat pumps, as it detects the currents produced by their variable-speed drive."),
     ("Can a type AC RCD be replaced with a type A?", "Yes, a type A performs all the functions of type AC and more; the reverse is prohibited where type A is required."),
   ],
 },
 "conseil-nombre-interrupteurs-differentiels-maison": {
   "title": "How many residual current switches for your home's floor area?",
   "crumb": "Number of RCDs",
   "desc": "Number of 30 mA residual current switches: 2 up to 35 m², 3 from 35 to 100 m², 4 above under NF C 15-100 (2002), incl. one type A. Ratings and distribution.",
   "lead": "The number of residual current switches depends on the floor area of the dwelling and the number of circuits. Here is the reference table and how to distribute the circuits in a villa.",
   "body": """
<p>According to the NF C 15-100 table (2002 edition as amended, still widely applied), a dwelling of <b>35 m² or less</b> has at least <b>2 30 mA residual current switches</b>, a dwelling of <b>35 to 100 m²</b> has <b>3</b>, and a dwelling of <b>more than 100 m²</b> has <b>4</b>, each time including one type A for the hob and the washing machine. For a villa, this minimum is almost always exceeded, because the number of circuits is what decides.</p>
<h2>The reference table</h2>
<div class="tableau"><table><thead><tr><th>Floor area of the dwelling</th><th>Type AC residual current switches</th><th>Type A residual current switch</th></tr></thead><tbody>
<tr><td>35 m² or less</td><td>1 × 25 A</td><td>1 × 40 A</td></tr>
<tr><td>From 35 to 100 m²</td><td>2 × 40 A</td><td>1 × 40 A</td></tr>
<tr><td>More than 100 m²</td><td>3 × 40 A</td><td>1 × 40 A</td></tr>
</tbody></table></div>
<p>These values are minimums for a standard dwelling. The 2024 edition of the standard reorganised these rules: depending on the edition applied to your project, the engineering firm or the inspection body specifies the exact requirements, particularly regarding types A and F.</p>
<h2>Why several residual current devices</h2>
<ul>
<li><b>Avoid cutting everything</b>: if a single residual current device protects the whole house, a leak on a garden socket plunges the villa into darkness.</li>
<li><b>Limit cumulative leakage</b>: each appliance leaks a few milliamps. Too many appliances under the same 30 mA device cause nuisance tripping.</li>
<li><b>Split lighting and sockets</b>: the lighting circuits of a given zone are placed under different residual current devices from the sockets, so that some light remains in the event of a fault.</li>
</ul>
<p>Manufacturers advise not to exceed about 8 circuits per residual current switch. In a heavily equipped villa (air conditioning, IT, LED lighting with electronic drivers), it is prudent to stay below that, as each piece of electronic equipment adds a small permanent leakage current.</p>
<h2>Example for a 250 m² villa in Marrakech</h2>
<ol>
<li><b>Type A residual current device no. 1</b>: hob, washing machine, dishwasher.</li>
<li><b>Type F residual current devices</b> (one or two): inverter air conditioners, variable-speed pool pump.</li>
<li><b>Type AC or A residual current devices</b> (three or four): lighting and sockets, distributed by floor or by zone (day, night, outdoors).</li>
<li><b>Separate residual current device</b> for the freezer and, if needed, for the IT network and video surveillance.</li>
</ol>
<p>This often results in 6 or 8 residual current devices, well beyond the minimum of 4. In three-phase, the residual current devices are also used to balance the load between the three phases.</p>
<h2>The role of the engineering firm</h2>
<p>The engineering firm counts the circuits, chooses the type and rating of each residual current device, checks that the sum of the downstream circuits remains compatible with its rating, and provides spare capacity in the board (see <a href="conseil-tableau-electrique-gtl-maison.html">distribution board and GTL</a>). For choosing the type, read <a href="conseil-differentiel-30ma-type-ac-a-f.html">30 mA RCD type AC, A or F</a>.</p>
""",
   "faq": [
     ("How many RCDs for a 120 m² house?", "The NF C 15-100 table (2002 edition) requires at least 4 30 mA residual current switches above 100 m²: three type AC rated 40 A and one type A rated 40 A."),
     ("How many circuits under one residual current switch?", "Manufacturers advise a maximum of about 8 circuits per residual current switch, to limit cumulative leakage currents and nuisance tripping."),
     ("Is a type A residual current device mandatory?", "Yes, at least one 30 mA type A residual current switch is required to protect the hob and the washing machine."),
   ],
 },
 "conseil-section-cable-calibre-disjoncteur": {
   "title": "Cable cross-section and circuit breaker rating: the reference table",
   "crumb": "Cross-section and rating",
   "desc": "NF C 15-100 cross-section / rating table: 1.5 mm² at 16 A, 2.5 mm² at 20 A, 4 mm² at 25 A, 6 mm² at 32 A, 10 mm² at 40 A. Long distances and villas.",
   "lead": "The circuit breaker rating is chosen according to the cross-section of the cable it protects. Here is the usual table for domestic installations, and the cases where you need to go beyond a table.",
   "body": """
<p>In a domestic copper installation, the NF C 15-100 benchmarks are as follows: <b>1.5 mm² protected by a 16 A circuit breaker</b>, <b>2.5 mm² by 20 A</b>, <b>4 mm² by 25 A</b>, <b>6 mm² by 32 A</b> and <b>10 mm² by 40 A</b> for certain high-power circuits. The principle is simple: the circuit breaker must trip before the cable heats up, so its rating must never exceed what the cross-section can carry.</p>
<h2>The usual table (copper, dwelling)</h2>
<div class="tableau"><table><thead><tr><th>Cross-section</th><th>Maximum circuit breaker</th><th>Common uses</th></tr></thead><tbody>
<tr><td>1.5 mm²</td><td>16 A (10 A or 16 A for lighting)</td><td>Lighting (8 points maximum), sockets (8 outlets maximum), roller shutters</td></tr>
<tr><td>2.5 mm²</td><td>20 A</td><td>Sockets (12 outlets maximum), oven, washing machine, dishwasher, tumble dryer, water heater, three-phase hob</td></tr>
<tr><td>4 mm²</td><td>25 A</td><td>Supply to a sub-distribution board, appliances of 4 to 5 kW</td></tr>
<tr><td>6 mm²</td><td>32 A</td><td>Single-phase hob or cooker, sub-distribution board</td></tr>
<tr><td>10 mm²</td><td>40 A</td><td>Large heating appliances, supply to a sub-distribution board</td></tr>
</tbody></table></div>
<p>These correspondences are those of the NF C 15-100 table reproduced by cable manufacturers. They apply to standard lengths and usual installation methods (embedded conduits). They do not replace a calculation when conditions differ from these assumptions.</p>
<h2>When the table is no longer enough</h2>
<ul>
<li><b>Long distances</b>: on a sprawling villa, a pool house or a gate 60 m from the board, voltage drop may require a larger cross-section than in the table.</li>
<li><b>High ambient temperature</b>: a cable laid on a flat roof or in roof spaces that exceed 50 °C in summer in Marrakech carries less current than at 30 °C; correction factors are then applied.</li>
<li><b>Grouped cables</b>: several cables packed in the same conduit or cable tray heat up more; the cross-section must be corrected.</li>
<li><b>Main supply and risers</b>: the cable between the meter and the board, or the risers of a building, are always calculated according to the contracted power and the length.</li>
</ul>
<h2>Common mistakes</h2>
<ol>
<li><b>Replacing a 16 A circuit breaker with a 20 A one</b> because it "trips": if the cable is 1.5 mm², it is no longer protected.</li>
<li><b>Mixing cross-sections on the same circuit</b>: a 1.5 mm² section on a 20 A circuit becomes the weak link.</li>
<li><b>Using cable of dubious quality</b>: an actual cross-section smaller than the stated one invalidates the whole calculation. Insist on cable that complies with Moroccan standards and is inspected.</li>
</ol>
<h2>The role of the engineering firm</h2>
<p>For a villa, a building or commercial premises, the engineering firm calculates each line: operating current, installation method, temperature, length, voltage drop and breaking capacity. The result appears in the calculation note and on the single-line diagram. See also <a href="conseil-combien-prises-par-circuit.html">how many sockets per circuit</a> and <a href="conseil-four-plaque-cuisson-cable-disjoncteur.html">the oven and hob cable</a>.</p>
""",
   "faq": [
     ("Which circuit breaker for 2.5 mm² cable?", "A 2.5 mm² copper cable is protected by a circuit breaker of 20 A maximum according to the NF C 15-100 benchmarks."),
     ("What cable size for a 32 A circuit breaker?", "A 32 A circuit breaker protects a 6 mm² copper cable, for example for a single-phase hob."),
     ("Can a 20 A circuit breaker be used on 1.5 mm² cable?", "No, 1.5 mm² is protected by a 16 A circuit breaker at most; a 20 A one would let the cable overheat without tripping."),
   ],
 },
 "conseil-mise-a-la-terre-maison-maroc": {
   "title": "Earthing a house: earth rod, foundation loop, resistance",
   "crumb": "Earthing",
   "desc": "Earthing a house in Morocco: foundation loop in 25 mm² bare copper, earth rods, 16 or 25 mm² earthing conductor, target resistance and testing.",
   "lead": "The earth electrode carries away fault currents and allows residual current devices to do their job. The best solution is decided when the foundations are laid.",
   "body": """
<p>For a new house, the best earth electrode is a <b>foundation earth loop</b>: a <b>bare copper cable of at least 25 mm²</b> laid at the bottom of the foundation trenches, around the entire perimeter of the building, before the concrete is poured. It is connected to the board by an <b>earthing conductor</b> (16 mm² copper if insulated and protected, 25 mm² if bare). In renovation work, earth rods driven into the ground are used. The resistance obtained must be measured and remain compatible with the residual current devices.</p>
<h2>Earth electrode solutions</h2>
<div class="tableau"><table><thead><tr><th>Solution</th><th>When</th><th>Key points</th></tr></thead><tbody>
<tr><td>Foundation earth loop</td><td>New construction, when the foundations are laid</td><td>Bare copper 25 mm² minimum, in contact with the soil, under the blinding concrete or at the bottom of the trench, both ends accessible for testing</td></tr>
<tr><td>Earth rods</td><td>Renovation, supplement</td><td>Vertical rod, generally 1.5 to 2 m long; several spaced rods connected together if the resistance is too high</td></tr>
<tr><td>Ring or conductor in a trench</td><td>Rocky ground, extension</td><td>Cable buried in a dedicated trench around the building</td></tr>
</tbody></table></div>
<h2>What resistance value should you aim for?</h2>
<p>The protection rule is that the touch voltage in the event of a fault must remain below 50 V. The maximum allowable value therefore depends on the sensitivity of the residual current device at the head of the installation: with a 500 mA device, you get 100 Ω, the value often cited as the limit. With more sensitive residual current devices, the theoretical limit is higher, but good practice is to aim for a much lower value, a few tens of ohms. A well-executed foundation earth loop generally gives low values.</p>
<p>In Marrakech, soils that are dry and stony in summer can push up the resistance of earth rods. Measure during the dry season and plan for several rods if necessary.</p>
<h2>From the ground to the sockets</h2>
<ol>
<li><b>The earth electrode</b> (loop or rods).</li>
<li><b>The earthing conductor</b> up to the test link (removable, to measure the resistance).</li>
<li><b>The main earthing terminal</b> of the board, from which the green-yellow protective conductors of each circuit run.</li>
<li><b>The main equipotential bonding</b>, which connects metal pipework and structures, see <a href="conseil-liaison-equipotentielle-principale-lep.html">the LEP</a>.</li>
</ol>
<p>The earthing system (generally TT for dwellings connected to the low-voltage network) must be confirmed with the distributor (Radeema in Marrakech, ONEE or another utility depending on the city).</p>
<h2>Coordinating with the structural work</h2>
<p>The foundation earth loop must be laid by the electrician or the mason at the right time: once the concrete is poured, it is too late. The engineering firm includes it in the drawings and the specifications (CPS), and checks its installation during site visits, before pouring. A resistance measurement is taken at handover. In a building, the loop is supplemented by connections to the reinforcement and the earth risers. See also <a href="conseil-role-bureau-etudes-techniques.html">the role of the engineering firm</a>.</p>
""",
   "faq": [
     ("What cross-section for a foundation earth loop?", "The foundation earth loop is made of bare copper of at least 25 mm², laid in contact with the soil at the bottom of the foundations."),
     ("What earth resistance should be achieved?", "With a 500 mA residual current device at the head of the installation, 100 Ω is the limit often cited; in practice the aim is much lower, a few tens of ohms at most."),
     ("Can an earth electrode be installed after construction?", "Yes, with one or more earth rods connected together; the foundation earth loop, which performs better, can only be laid when the foundations are built."),
   ],
 },
 "conseil-liaison-equipotentielle-principale-lep": {
   "title": "Main equipotential bonding (LEP): role and installation",
   "crumb": "Main equipotential bonding",
   "desc": "Main equipotential bonding (LEP) connects metal water and gas pipes and structures to earth. Copper cross-section from 6 mm² to 25 mm², connection.",
   "lead": "Main equipotential bonding brings all the metal parts entering the building to the same potential. A discreet wire, but essential for safety.",
   "body": """
<p><b>Main equipotential bonding (LEP)</b> connects all the metal pipes and structures entering the building to the main earthing terminal: water supply, gas, heating, metal ducts, accessible structural elements. Its purpose is to prevent a dangerous voltage difference from appearing between two metal parts that can be touched at the same time, for example a tap and the casing of a faulty appliance.</p>
<h2>What must be connected</h2>
<ul>
<li><b>Metal water pipes</b> where they enter the building (after the meter).</li>
<li><b>The gas pipe</b> if it is metal (mains network or pipework from a cylinder store).</li>
<li><b>Metal heating and hot water pipes</b>.</li>
<li><b>Accessible metal structural elements</b> and metal ducts or conduits.</li>
<li><b>In an apartment building</b>: the concrete reinforcement where accessible, metal risers, ventilation ducts.</li>
</ul>
<p>With PEX, multilayer or PPR pipework, very common today, the LEP mainly concerns the metal sections (copper or galvanised steel water inlet, fittings and manifolds).</p>
<h2>Conductor cross-sections</h2>
<div class="tableau"><table><thead><tr><th>Conductor</th><th>Usual cross-section (copper)</th></tr></thead><tbody>
<tr><td>Main equipotential bonding</td><td>Half the cross-section of the largest protective conductor in the installation, with a minimum of 6 mm² and not exceeding 25 mm²</td></tr>
<tr><td>Earthing conductor (earth electrode to test link)</td><td>16 mm² insulated and protected, 25 mm² bare</td></tr>
<tr><td>Circuit protective conductors</td><td>Same cross-section as the circuit's live conductors</td></tr>
</tbody></table></div>
<p>Example: with a 16 mm² main protective conductor, the LEP is made in 10 mm². For a standard house, 6 mm² is the most common value. The conductor is green-yellow, attached with earthing clamps suited to each pipe.</p>
<h2>How to install it</h2>
<ol>
<li>Provide a <b>main earthing terminal</b> (or bar) near the board or in the service duct.</li>
<li>Fit a clamp on each metal pipe, as close as possible to where it enters the building.</li>
<li>Connect each clamp to the main terminal with a green-yellow conductor of suitable cross-section, without cutting it along the way.</li>
<li>Label the connections and leave them accessible for inspection.</li>
</ol>
<h2>LEP and LES: do not confuse them</h2>
<p>The LEP is general and starts from the main earthing terminal. <b>Supplementary equipotential bonding</b> (LES) is local: it mainly concerns the bathroom, see <a href="conseil-liaison-equipotentielle-supplementaire-les-salle-de-bain.html">LES in the bathroom</a>. Both complement the earth electrode described in <a href="conseil-mise-a-la-terre-maison-maroc.html">earthing a house</a>.</p>
<p>The engineering firm shows the LEP on the electrical and plumbing drawings, which allows it to be coordinated between the two trades. It is a point the inspection body systematically checks before the installation is energised. In renovation work, the absence of an LEP is one of the most common defects in older houses: installing one is inexpensive and significantly improves safety, provided the earth electrode itself is sound.</p>
""",
   "faq": [
     ("What cross-section for main equipotential bonding?", "The LEP is half the cross-section of the largest protective conductor in the installation, with a minimum of 6 mm² and a maximum of 25 mm² in copper."),
     ("Do PEX pipes need to be connected to earth?", "No, synthetic pipes are not conductive; equipotential bonding concerns metal parts, such as a copper or steel water inlet."),
     ("Where is the main equipotential bonding connected?", "It starts from the main earthing terminal, near the board or in the service duct, to which the earthing conductor and the protective conductors are also connected."),
   ],
 },
 "conseil-liaison-equipotentielle-supplementaire-les-salle-de-bain": {
   "title": "Supplementary equipotential bonding (LES) in the bathroom",
   "crumb": "Bathroom LES",
   "desc": "LES bonding links the bathroom's metal parts (pipes, bathtub, shower tray): green-yellow 2.5 mm² if protected or 4 mm² if unprotected. When it is needed.",
   "lead": "In the bathroom, water and wet skin make an electric shock far more dangerous. Supplementary equipotential bonding brings everything metal in the room to the same potential.",
   "body": """
<p><b>Supplementary equipotential bonding (LES)</b> is a green-yellow conductor that connects together, and to the protective conductor, all the accessible metal parts of the bathroom: metal water pipes, metal bathtub or shower tray, metal waste outlet, metal door frames. It is commonly made in <b>2.5 mm² if the conductor is mechanically protected</b> (in conduit, embedded) and in <b>4 mm² if it is not</b>. Its purpose: to ensure that no dangerous voltage can appear between two parts touched at the same time with wet hands and feet.</p>
<h2>The parts to connect</h2>
<ul>
<li><b>Metal pipes</b> for cold water, hot water and drainage.</li>
<li><b>Metal bathtub or shower tray</b> (enamelled steel, cast iron): a connection lug is often provided under the fixture.</li>
<li><b>Accessible metal door frames and structural elements</b> in the room.</li>
<li><b>The exposed conductive parts of class I appliances</b> (towel radiator, water heater) via their protective conductor.</li>
</ul>
<p>Acrylic or ceramic bathtubs and shower trays, and PEX or multilayer pipes, are not conductive and do not need to be connected.</p>
<h2>Is it always mandatory?</h2>
<p>The LES was long systematic in bathrooms. Amendment 5 of NF C 15-100 (2015) clarified the cases where it can be carried out differently, or is no longer necessary, notably when the installation has main equipotential bonding and the circuits are protected by a 30 mA residual current device, subject to conditions. These conditions are precise and vary according to the edition of the standard applied: in practice, in a new build in Morocco with partly metal pipework, installing it remains the safest solution, and the inspection body decides in case of doubt.</p>
<h2>How to install it</h2>
<ol>
<li>Fit an earthing clamp on each metal pipe and on the lug of the bathtub or shower tray.</li>
<li>Connect these points together with a continuous green-yellow conductor, without inaccessible intermediate connectors.</li>
<li>Connect the bonding to the protective conductor of a bathroom circuit (earth terminal of an appliance or connection box) or to the earth bar of the board if it is close by.</li>
<li>Leave the connections visible or accessible for inspection by the inspection body.</li>
</ol>
<h2>In a riad or a renovation</h2>
<p>In riads and older houses in the medina, you still find galvanised steel or copper pipes embedded in the walls, and sometimes no earth electrode at all. Before redoing the bathroom, you must check the earthing of the entire installation (see <a href="conseil-mise-a-la-terre-maison-maroc.html">earthing</a>) and the presence of 30 mA residual current devices. The LES is useless if the protective conductor is not connected to any earth.</p>
<p>The engineering firm includes the LES in the bathroom drawings, in compliance with <a href="conseil-volumes-salle-de-bain-electricite.html">zones 0, 1 and 2</a>, and coordinates the plumber and the electrician so that the clamps are fitted before the walls and ducts are closed up.</p>
""",
   "faq": [
     ("What cross-section for bathroom equipotential bonding?", "A green-yellow conductor of 2.5 mm² is commonly used if it is mechanically protected, in conduit or embedded, and 4 mm² if it is not."),
     ("Does an acrylic bathtub need to be earthed?", "No, an acrylic or ceramic bathtub or shower tray is not conductive; only accessible metal parts are connected."),
     ("Is the LES still mandatory?", "Since amendment 5 of 2015, NF C 15-100 accepts cases where it is no longer necessary, under precise conditions; in the absence of certainty, installing it remains the safest solution."),
   ],
 },
 "conseil-volumes-salle-de-bain-electricite": {
   "title": "Bathroom zones 0, 1, 2: what electrical equipment is allowed?",
   "crumb": "Bathroom zones",
   "desc": "Bathroom zones: zone 0 limited to 12 V SELV IPX7, SELV in zone 1, class II IPX4 in zone 2 (60 cm, 2.25 m high). Where to put sockets and the water heater.",
   "lead": "NF C 15-100 divides the bathroom into zones around the bathtub and shower. The closer you get to water, the stricter the rules.",
   "body": """
<p>The bathroom is divided into three zones: <b>zone 0</b> (inside the bathtub or shower tray), where almost nothing is allowed except watertight IPX7 12 V safety extra-low voltage (SELV) lighting; <b>zone 1</b> (above it, up to 2.25 m high), limited to 12 V SELV and certain water heaters; <b>zone 2</b> (a 60 cm strip around zone 1, up to 2.25 m), where class II light fittings and appliances, IPX4 minimum, are allowed. Beyond that, you are <b>outside the zones</b> and socket outlets are possible.</p>
<h2>What is allowed in each zone</h2>
<div class="tableau"><table><thead><tr><th>Zone</th><th>Extent</th><th>What is allowed</th></tr></thead><tbody>
<tr><td>Zone 0</td><td>Inside the bathtub or shower tray</td><td>Only 12 V SELV equipment, IPX7 (submersible lighting)</td></tr>
<tr><td>Zone 1</td><td>Above zone 0, up to 2.25 m from the floor</td><td>12 V SELV equipment (at least IPX4, IPX5 where there are water jets); electric water heater under conditions</td></tr>
<tr><td>Zone 2</td><td>60 cm around zone 1, up to 2.25 m</td><td>Class II light fittings and appliances, IPX4 minimum; shaver socket with isolating transformer</td></tr>
<tr><td>Outside the zones</td><td>The rest of the room</td><td>16 A socket outlets, washing machine, switches, earthed class I appliances</td></tr>
</tbody></table></div>
<p>All bathroom circuits are protected by a 30 mA residual current device. Switches are prohibited in zones 0 and 1.</p>
<h2>Practical cases</h2>
<ul>
<li><b>Walk-in shower</b> without a fixed screen: zone 1 is no longer limited by the shower tray: it extends over a 1.20 m radius around the fixed shower head, according to the rules of the 2002 edition as amended. So place sockets and switches further away than with a conventional shower tray.</li>
<li><b>Vanity unit with a socket</b>: the socket must be outside the zones, or be limited to a shaver socket in zone 2.</li>
<li><b>Washing machine in the bathroom</b>: outside the zones only.</li>
<li><b>Towel radiator</b>: class II in zone 2, or outside the zones.</li>
<li><b>Electric water heater</b>: preferably outside the zones; in zone 1, only a horizontal appliance placed as high as possible, under the conditions of the standard.</li>
</ul>
<h2>A fixed screen changes everything</h2>
<p>A fixed screen, a partition or a ceiling limits the zones: behind a solid screen, you may find yourself outside the zones. This is often the solution for installing a socket near a bathtub in a small bathroom. The space under the bathtub, closed by a panel removable only with a tool, also has its own rules (IPX4 for the equipment allowed there).</p>
<h2>Riads, hammams and hotel suites</h2>
<p>In the riads and guest houses of Marrakech, tadelakt bathrooms, open showers and private hammams raise specific cases: floor-level mood lighting, illuminated mirrors, hammams with steam generators. A hammam is subject to specific rules. The engineering firm marks out the zones on the plan of each bathroom, chooses the protection ratings and coordinates with the <a href="conseil-liaison-equipotentielle-supplementaire-les-salle-de-bain.html">supplementary equipotential bonding</a>. The dimensions given here are those of the 2002 edition of NF C 15-100 as amended; the 2024 edition must be checked for projects that apply it.</p>
""",
   "faq": [
     ("Can you have an electrical socket in a bathroom?", "Yes, outside the zones, i.e. more than 60 cm from the bathtub or shower (or behind a fixed screen); in zone 2, only a shaver socket with an isolating transformer is allowed."),
     ("How wide is zone 2?", "Zone 2 forms a 60 cm strip around zone 1, up to a height of 2.25 m, according to the rules of NF C 15-100, 2002 edition as amended."),
     ("What lighting can be used in a shower?", "In zone 0, only watertight IPX7 12 V SELV lighting is allowed; above, in zone 1, 12 V SELV lighting with at least IPX4, IPX5 where there are water jets."),
   ],
 },
 "conseil-tableau-electrique-gtl-maison": {
   "title": "Distribution board and GTL: location, number of rows, spare capacity",
   "crumb": "Distribution board and GTL",
   "desc": "Distribution board: controls between 0.90 and 1.80 m, 20% spare capacity, 600 mm wide GTL above 35 m². Where to place it in a villa and what the GTL contains.",
   "lead": "The distribution board and the dwelling technical duct (GTL) bring together the power supply and the protective devices. Their location and size are decided on the drawings, not on site.",
   "body": """
<p>The distribution board must be placed <b>inside the dwelling</b> or in a directly accessible annex room, with its controls <b>between 0.90 m and 1.80 m above the floor</b> (board without a door), and must keep <b>at least 20% free slots</b> for future additions. Under NF C 15-100, it is integrated into a <b>dwelling technical duct (GTL)</b>, a column that also houses the communications enclosure and the incoming networks: 600 mm wide in a dwelling of more than 35 m², 450 mm below that.</p>
<h2>Key benchmarks</h2>
<div class="tableau"><table><thead><tr><th>Item</th><th>Usual benchmark (NF C 15-100)</th></tr></thead><tbody>
<tr><td>Height of controls</td><td>Between 0.90 m and 1.80 m from the floor; with a door, between 0.50 m and 1.80 m</td></tr>
<tr><td>Spare capacity</td><td>At least 20% free slots in a detached house, with no empty row</td></tr>
<tr><td>GTL, dwelling of more than 35 m²</td><td>600 mm wide, about 200 mm deep</td></tr>
<tr><td>GTL, dwelling of 35 m² or less</td><td>450 mm wide, about 150 mm deep</td></tr>
<tr><td>Location</td><td>In the dwelling or a directly accessible annex room, generally near the entrance or the garage</td></tr>
</tbody></table></div>
<p>For a dwelling adapted to people with reduced mobility, the height range is lower (Legrand cites 0.75 m to 1.30 m for the isolating device). These values are those of the 2002 edition as amended; the 2024 edition must be checked for projects that apply it.</p>
<h2>How many rows?</h2>
<p>The number of rows follows from the number of circuits: each miniature circuit breaker generally takes up one module, each residual current switch two or four modules, and a standard row has 13 or 18 modules. For a villa of 200 to 300 m², with 25 to 40 circuits, 6 to 8 residual current devices, a surge protector and contactors, a 4-row board is commonly needed, or even a main board plus sub-distribution boards per floor or for the pool. Add 20% spare capacity and wiring space: a board that is too small quickly becomes impossible to extend.</p>
<h2>Where to place it in a villa?</h2>
<ul>
<li><b>Near the entrance or the garage</b>, accessible without going through a bedroom, and not in a bathroom or above a sink.</li>
<li><b>Away from heat</b>: in Marrakech, a board in an unventilated, west-facing room can exceed 40 °C in summer, which makes the devices heat up and causes tripping.</li>
<li><b>Close to the centre of gravity of the loads</b> to limit cable length and voltage drop, particularly towards the kitchen and the air conditioning units.</li>
<li><b>In a riad</b>: provide a ventilated plant room and one sub-distribution board per floor rather than dozens of cables running through the old walls.</li>
</ul>
<h2>What the GTL contains</h2>
<ol>
<li>The main incoming circuit breaker and the distribution board.</li>
<li>The communications enclosure (telephone, fibre, RJ45, television).</li>
<li>The incoming networks from the meter (Radeema, ONEE or another distributor).</li>
<li>Socket outlets to power the internet box and the equipment in the enclosure.</li>
</ol>
<p>The engineering firm draws the board on the single-line diagram, counts the modules and places the GTL on the architect's drawings from the design stage, to avoid squeezing it into a cupboard that is too narrow later on. See also <a href="conseil-nombre-interrupteurs-differentiels-maison.html">the number of residual current devices</a> and <a href="conseil-circuits-specialises-nf-c-15-100.html">dedicated circuits</a>.</p>
""",
   "faq": [
     ("At what height should a distribution board be installed?", "Under NF C 15-100, the controls of a board without a door are between 0.90 m and 1.80 m from the floor; with a door, the range is 0.50 m to 1.80 m."),
     ("How much spare capacity should a distribution board have?", "At least 20% free slots in a detached house, without leaving any row completely empty, so that circuits can be added later."),
     ("How wide should a GTL be?", "600 mm wide and about 200 mm deep for a dwelling of more than 35 m², 450 mm wide for a dwelling of 35 m² or less."),
   ],
 },
 "conseil-nombre-prises-par-piece": {
   "title": "Minimum number of sockets and light points per room (NF C 15-100)",
   "crumb": "Sockets per room",
   "desc": "Sockets per room under NF C 15-100: living room 5 minimum (7 above 28 m²), bedroom 3, kitchen 6 incl. 4 above the worktop, at least one light point per room.",
   "lead": "The standard sets a minimum number of sockets and light points per room. These are floors, not targets: in a villa, you almost always plan for more.",
   "body": """
<p>Under the NF C 15-100 rules (2002 edition as amended, still widely applied), you need at least <b>5 sockets in a living room of less than 28 m²</b> (7 above that according to most guides), <b>3 sockets per bedroom</b> and <b>6 sockets in a kitchen of more than 4 m²</b>, including 4 above the worktop. Each main room also has at least one lighting point, on the ceiling or as a switched wall light. These minimums do not include the sockets on dedicated circuits (oven, washing machine, dishwasher).</p>
<h2>The table by room</h2>
<div class="tableau"><table><thead><tr><th>Room</th><th>Minimum 16 A sockets</th><th>Lighting</th></tr></thead><tbody>
<tr><td>Living room of less than 28 m²</td><td>5</td><td>At least one light point</td></tr>
<tr><td>Living room of 28 m² or more</td><td>7 (some manufacturers' guides state more)</td><td>At least one light point</td></tr>
<tr><td>Bedroom</td><td>3</td><td>At least one light point</td></tr>
<tr><td>Kitchen of more than 4 m²</td><td>6, including 4 above the worktop</td><td>At least one light point</td></tr>
<tr><td>Kitchen of 4 m² or less</td><td>3</td><td>At least one light point</td></tr>
<tr><td>Bathroom</td><td>Outside the zones only</td><td>At least one light point, according to the zones</td></tr>
</tbody></table></div>
<p>As for circuits, remember that a 1.5 mm² lighting circuit supplies a maximum of 8 light points, and a 2.5 mm² socket circuit a maximum of 12 outlets (see <a href="conseil-combien-prises-par-circuit.html">how many sockets per circuit</a>).</p>
<h2>What is really planned in a villa</h2>
<ul>
<li><b>Living room</b>: 8 to 12 sockets, including sockets near the television, the sofa and charging points; floor sockets if the living room is large and open-plan.</li>
<li><b>Bedrooms</b>: 2 sockets on each side of the bed (lamps, chargers), one near the desk, one for the air conditioner if it is not on a dedicated circuit.</li>
<li><b>Kitchen</b>: in addition to the 4 worktop sockets, sockets for the refrigerator, hood, microwave and small appliances, plus the dedicated circuits.</li>
<li><b>Outdoors</b>: watertight sockets on the terrace, in the garden and near the pool, on a dedicated circuit protected by a 30 mA residual current device.</li>
<li><b>Corridors and hallways</b>: a socket for the vacuum cleaner, lighting controlled from several places (two-way switching or impulse relay).</li>
</ul>
<h2>Heights and locations</h2>
<p>Sockets are installed at a sufficient height above the finished floor (in practice at least 5 cm for a 16 A socket), and worktop sockets are not placed above the sink or the hob. Remember to put switches at the entrance to each room, on the door-opening side.</p>
<h2>Draw the plan before cutting chases</h2>
<p>The most economical approach is to place sockets, switches and light points on the layout plan, including furniture, before work begins. The engineering firm draws up this layout plan, groups the points into circuits and checks consistency with the board. For the regulatory framework in Morocco, see <a href="conseil-norme-electrique-nf-c-15-100-maroc.html">NF C 15-100 and Moroccan standards</a>.</p>
""",
   "faq": [
     ("How many sockets in a bedroom?", "NF C 15-100 requires at least 3 socket outlets per bedroom, whatever its size; in practice 5 or 6 are often planned."),
     ("How many sockets in a living room?", "At least 5 sockets in a living room of less than 28 m², and 7 above that according to most NF C 15-100 guides."),
     ("How many sockets in a kitchen?", "At least 6 sockets in a kitchen of more than 4 m², including 4 above the worktop, not counting the sockets on dedicated circuits."),
   ],
 },
}
