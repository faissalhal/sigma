# -*- coding: utf-8 -*-
# English translation of the "Conseils" articles: structure batch (SIGMA ICC)

T = {
 "conseil-type-fondation-semelle-radier": {
   "title": "Which foundation type to choose: footings, raft or piles?",
   "crumb": "Foundation type",
   "desc": "Pad or strip footings, raft or piles: how the soil investigation and the building loads determine the foundation type for a house in Morocco.",
   "lead": "You do not pick a foundation type from a catalogue: it follows from the bearing capacity of the soil, the depth of the good soil and the loads of your building.",
   "body": """
<p>For a villa or a small building on reasonable soil, <b>footings</b> (pad footings under the columns, strip footings under the walls) connected by tie beams remain the most common and most economical solution. A <b>raft</b> becomes worthwhile when the soil is weak or heterogeneous, and <b>piles</b> when the good soil lies too deep. The soil investigation decides, then the structural engineer does the design.</p>
<h2>The three main families</h2>
<div class="tableau"><table><thead><tr><th>Foundation</th><th>Principle</th><th>Typical case</th></tr></thead><tbody>
<tr><td>Pad and strip footings</td><td>Shallow foundation: each column or wall rests on a widened reinforced concrete footing</td><td>Bearing soil at shallow depth, moderate loads (villa with one or two upper floors)</td></tr>
<tr><td>Raft foundation</td><td>Thick reinforced concrete slab under the whole footprint, which spreads the loads</td><td>Low-bearing soil, risk of differential settlement, basement with groundwater</td></tr>
<tr><td>Piles or micropiles</td><td>Deep foundation that reaches a strong soil at depth</td><td>Thick fill, compressible soil, heavy loads, underpinning</td></tr>
</tbody></table></div>
<h2>What the soil investigation must give you</h2>
<p>The geotechnical report provides the data that drive the choice:</p>
<ul>
<li><b>The allowable bearing pressure of the soil</b> (in bars or MPa) and the depth at which it is reached.</li>
<li><b>The settlement risks</b>, in particular differential settlement between two parts of the building, which causes many cracks.</li>
<li><b>The presence of water</b> (water table, seepage), swelling clays, fill or cavities.</li>
<li><b>A recommended foundation type</b> and founding level.</li>
</ul>
<p>Without this information, the engineer has to make cautious assumptions, which often costs more in concrete and steel than the investigation itself. See our article on the <a href="conseil-etude-de-sol-maroc-prix.html">cost of a soil investigation in Morocco</a>.</p>
<h2>When to switch from footings to a raft?</h2>
<p>When the calculated footings become so large that they almost touch, or would cover a large part of the building footprint, a raft often becomes simpler and not necessarily more expensive. A raft is also preferred when differential settlement must be limited or a watertight basement is required. Conversely, on good soil, a raft under a light villa is generally oversized.</p>
<h2>Seismic requirements</h2>
<p>In Morocco, the seismic code RPS 2000 (2011 version) also applies to foundations: pad footings must be tied together by tie beams so that they do not move relative to one another during an earthquake. A single building block should in principle rest on a single foundation type and at a consistent level, unless justified. To learn more, see our article on the <a href="conseil-reglement-parasismique-rps-2011-maroc.html">RPS 2011 seismic code</a>.</p>
<h2>The role of the engineering firm</h2>
<p>The engineering firm combines the soil report, the building load take-down and the RPS requirements to choose the foundation and produce its formwork and reinforcement drawings. On site, it checks that the bottom of the excavation matches the soil described by the geotechnical engineer before the blinding concrete is poured: this is when a bad surprise costs the least.</p>
""",
   "faq": [
    ("Which foundation for a two-storey villa in Morocco?", "On soil with good bearing capacity, pad footings under columns and strip footings under walls, connected by tie beams, are generally sufficient. The final choice depends on the soil investigation and the engineer's calculations."),
    ("Is a raft stronger than footings?", "Not necessarily: a raft suits weak soils or basements, but on good soil properly designed footings are just as safe and more economical."),
    ("When are piles needed?", "When the strong soil lies too deep for shallow foundations, for example under thick fill or compressible soils. The geotechnical investigation determines this."),
   ],
 },
 "conseil-semelle-isolee-filante-dimension": {
   "title": "Pad or strip footing dimensions: how to calculate them",
   "crumb": "Footing dimensions",
   "desc": "Footing area = load / allowable soil pressure: 30 t on a 2-bar soil gives about 1.25 × 1.25 m. Depth, blinding concrete and common mistakes explained.",
   "lead": "The size of a footing follows from a calculation that is simple in principle: the load it receives divided by what the soil can bear. The rest is a matter of reinforcement and detailing.",
   "body": """
<p>The area of a footing is calculated by dividing the load transmitted by the column or wall by the <b>allowable bearing pressure of the soil</b> given by the geotechnical investigation. There is therefore no "standard size": the same villa may need footings 1 m wide on rocky soil and nearly 2 m wide on poor soil.</p>
<h2>The principle of the calculation</h2>
<p>Take a column bringing down 300 kN (about 30 tonnes) onto a soil with an allowable bearing pressure of 2 bars (0.2 MPa, i.e. 200 kN/m²):</p>
<ul>
<li><b>Required area</b>: 300 / 200 = 1.5 m².</li>
<li><b>Square footing</b>: square root of 1.5 ≈ 1.22 m, rounded up to 1.25 × 1.25 m.</li>
<li><b>On a 1-bar soil</b>, the same load would require 3 m², i.e. about 1.75 × 1.75 m.</li>
</ul>
<p>For a strip footing, the reasoning is the same per linear metre of wall: the load per metre divided by the allowable pressure gives the width. The engineer adds the self-weight of the footing and the soil above, and the load combinations, including earthquake according to RPS 2000 (2011 version).</p>
<h2>The depth of the footing</h2>
<p>A footing must be thick enough to transmit the column force to its whole area without failing. In the classic "strut" method of the BAEL, the effective depth is at least a quarter of the projection, i.e. (B - b) / 4, B being the width of the footing and b that of the column. With a 1.25 m footing under a 25 cm column, this gives at least 25 cm of effective depth, plus the concrete cover. The exact values and the reinforcement (bottom mesh in both directions, column starter bars) are <b>to be determined by the engineer</b>.</p>
<h2>Points to respect on site</h2>
<ul>
<li><b>The founding level</b> given by the soil investigation: you dig down to the good soil, even if it is deeper than expected.</li>
<li><b>The blinding concrete</b>, a layer of a few centimetres of lean concrete that protects the bottom of the excavation and supports the reinforcement.</li>
<li><b>The concrete cover</b> of the bars, greater for concrete cast against the ground (see <a href="conseil-enrobage-armatures-beton.html">reinforcement cover</a>).</li>
<li><b>The tie beams</b> connecting the footings to each other, required by the seismic code.</li>
<li><b>Centring</b> the column on the footing: an eccentric footing (on a property boundary, for example) is designed differently.</li>
</ul>
<h2>Common mistakes</h2>
<p>Copying the footing sizes from a neighbour, reducing their size to save concrete, or placing a footing on uncompacted fill are the classic causes of settlement and <a href="conseil-fissures-maison-causes-gravite.html">cracks</a>. An undersized footing can only be fixed by costly underpinning.</p>
<h2>The role of the engineering firm</h2>
<p>The engineering firm establishes the load take-down column by column, sizes each footing according to the actual soil and provides a dimensioned foundation plan with reinforcement. It then inspects the bottom of the excavation and the reinforcement before pouring.</p>
""",
   "faq": [
    ("How do you calculate the area of a footing?", "Divide the load transmitted by the column by the allowable bearing pressure of the soil: 300 kN on a 2-bar soil (200 kN/m²) requires 1.5 m², i.e. a footing of about 1.25 × 1.25 m."),
    ("How thick should a pad footing be?", "According to the strut method, the effective depth is at least a quarter of the projection, (B - b) / 4. The exact value and the reinforcement are set by the engineer."),
    ("Can footings be built without a soil investigation?", "It is not advisable: without a measured allowable bearing pressure, the engineer must use a cautious assumption, and an error about the soil is the leading cause of settlement."),
   ],
 },
 "conseil-longrines-role-dimension": {
   "title": "Tie beams: what are they for and how are they sized?",
   "crumb": "Tie beams",
   "desc": "Tie beams connect footings to stop them moving apart in an earthquake and carry the ground-floor walls. Their role, RPS 2011, cross-section and reinforcement.",
   "lead": "Invisible once the ground slab is poured, tie beams are nevertheless a key element of a house's seismic resistance: they stop the foundations from moving independently of one another.",
   "body": """
<p>A tie beam is a reinforced concrete beam that connects the footings to each other at foundation level. It has two roles: <b>tying the foundations together</b> so that they move as one in an earthquake or under settlement, and often <b>carrying the walls</b> of the ground floor. In Morocco, the seismic code RPS 2000 (2011 version) requires pad footings to be tied together.</p>
<h2>Why tie beams are essential in seismic areas</h2>
<p>During an earthquake, the ground does not move the same way everywhere. Unconnected pad footings can move closer together or further apart, tearing the columns away at their base. The tie beam then works as a <b>tie</b> (in tension) or a <b>strut</b> (in compression) between the supports. It also limits the effects of differential settlement by sharing the loads better between neighbouring foundations.</p>
<h2>The two types of tie beam</h2>
<ul>
<li><b>Connecting tie beam</b>: it connects the footings and carries little load. Its cross-section remains modest and its reinforcement is symmetrical (top and bottom), as it may be in tension or compression.</li>
<li><b>Load-bearing tie beam</b>: it receives the weight of a wall or heavy partition and also works in bending. It is designed as a beam resting on the footings.</li>
</ul>
<h2>What cross-section and reinforcement?</h2>
<p>The cross-section of a tie beam depends on the span between footings, the wall loads and the seismic force to be transmitted. Seismic codes set a minimum tie force and minimum cross-sections; these values vary between texts (Moroccan RPS, Algerian RPA, Eurocode 8) and must not be transposed from one country to another. On a villa, typical tie beams have cross-sections of a few tens of centimetres per side, with regular stirrups, but <b>the exact cross-section is to be determined by the engineer</b> from the design calculations.</p>
<div class="tableau"><table><thead><tr><th>Checkpoint</th><th>What to check</th></tr></thead><tbody>
<tr><td>Continuity</td><td>Bars anchored in the footings or columns, sufficient lap lengths</td></tr>
<tr><td>Reinforcement</td><td>Top and bottom bars as per the drawing, stirrups at the specified spacing</td></tr>
<tr><td>Bedding</td><td>Tie beam cast on blinding concrete or compacted soil, never on loose fill</td></tr>
<tr><td>Concrete cover</td><td>Spacers in place, increased cover for concrete cast against the ground</td></tr>
</tbody></table></div>
<h2>Tie beams and ground slab</h2>
<p>The ground-floor slab does not replace the tie beams, unless the engineer has designed a suspended slab or a raft that plays this role. A slab laid on hardcore is an independent element, which may crack without compromising the structure. Tie beams also support the façade walls and limit rising damp when a damp-proof course is provided above them (see <a href="conseil-remontees-capillaires-murs.html">rising damp</a>).</p>
<h2>The role of the engineering firm</h2>
<p>The engineering firm draws the foundation plan with all the tie beams, their cross-sections and their reinforcement, in accordance with RPS 2011. During site visits, it checks that the tie beams have not been omitted or reduced to save money, a practice still common on small sites and with serious consequences in an earthquake.</p>
""",
   "faq": [
    ("Are tie beams mandatory in Morocco?", "The seismic code RPS 2000 (2011 version) requires pad footings to be tied together; tie beams are the usual way of doing so."),
    ("What is the difference between a tie beam and a strip footing?", "A strip footing transmits the load of a wall directly to the soil, whereas a tie beam is a beam that connects footings and can carry a wall between two supports."),
    ("What cross-section for a tie beam?", "It depends on the span, the walls carried and the seismic force: the cross-section and reinforcement are set by the engineer in the foundation drawings."),
   ],
 },
 "conseil-chainage-horizontal-vertical": {
   "title": "Horizontal and vertical ring beams: role and rules in Morocco",
   "crumb": "Ring beams and ties",
   "desc": "Vertical ties at corners, horizontal ring beams at each floor: seismic role and RPS rules (4 T10, 3 cm², 15 cm depth, at most 5 m between vertical ties).",
   "lead": "Ring beams and ties encircle masonry walls and connect them to the floors. In a seismic region like Marrakech, they make the difference between a wall that cracks and a wall that collapses.",
   "body": """
<p>A ring beam or tie is a reinforced concrete element built into the masonry: <b>horizontal</b> at each floor level and at the top of walls, <b>vertical</b> at corners, wall intersections and the edges of large openings. Together, they form a cage that stops the walls from breaking apart under an earthquake or settlement.</p>
<h2>Why ring beams and ties are essential</h2>
<p>Brick or block masonry resists compression well, but tension and shear very poorly. During an earthquake, unconfined walls separate at the corners and topple. The 2023 Al Haouz earthquake showed the gap between confined buildings and traditional masonry without ties. Ring beams and ties also transmit floor forces to the walls and limit cracking due to shrinkage or thermal movement.</p>
<h2>The RPS rules for confined masonry</h2>
<p>The Moroccan seismic code devotes a chapter to confined masonry buildings. The RPS 2000 text notably provides for the following, to be checked in the 2011 version applied to your project:</p>
<div class="tableau"><table><thead><tr><th>Element</th><th>RPS 2000 provision</th></tr></thead><tbody>
<tr><td>End vertical ties</td><td>At least 4 T10 bars, with stirrups spaced at 10 cm</td></tr>
<tr><td>Horizontal ring beams</td><td>Minimum steel area of 3 cm²</td></tr>
<tr><td>Concrete section</td><td>Minimum depth of 15 cm for vertical ties and horizontal ring beams</td></tr>
<tr><td>Spacing</td><td>5 m maximum between two vertical ties</td></tr>
</tbody></table></div>
<p>Some presentation documents on RPS 2011 quote other minimum values; if in doubt, the official text and the engineering firm's design calculations prevail.</p>
<h2>Where to place ring beams and ties</h2>
<ul>
<li><b>Horizontal</b>: at each floor level, at the top of walls (including parapets) and, on tall walls, at mid-height if the calculation requires it.</li>
<li><b>Vertical</b>: at all corners, at wall junctions, on both sides of large openings, and at regular intervals along long walls.</li>
<li><b>Frames</b>: large openings are bordered by reinforced concrete stiffeners.</li>
</ul>
<h2>Mistakes to avoid</h2>
<ul>
<li>Horizontal ring beams interrupted at corners, with no return or lapping of the bars.</li>
<li>Vertical ties not anchored into the tie beams at the bottom or into the top ring beam.</li>
<li>Stirrups spaced too far apart or closed without hooks, bars placed directly against the brick with no cover.</li>
<li>Masonry built with no connection to the ties cast afterwards.</li>
</ul>
<h2>Ring beams and column-beam frames</h2>
<p>In a villa with a reinforced concrete frame (columns, beams, floors), infill walls are not load-bearing, but they must be held so that they do not collapse: the tying or stiffening rules also apply to large panels. The engineering firm specifies on its drawings which structural system is adopted and where to place the stiffeners. See also our article on <a href="conseil-reglement-parasismique-rps-2011-maroc.html">RPS 2011</a>. During site visits, it checks the continuity of the ring beams at corners and their anchorage into the tie beams and floors.</p>
""",
   "faq": [
    ("What reinforcement for a vertical tie?", "RPS 2000 provides for at least 4 T10 bars with stirrups spaced at 10 cm for end vertical ties in confined masonry; the engineer may require more."),
    ("How many metres apart should vertical ties be?", "RPS 2000 limits the distance between two vertical ties to 5 m, in addition to those placed at corners and wall intersections."),
    ("Is a horizontal ring beam mandatory at every storey?", "Yes, in confined masonry a horizontal ring beam encircles the walls at each floor level and at the top of the wall, to connect walls and floors."),
   ],
 },
 "conseil-poteau-section-minimale-rps": {
   "title": "Minimum size of a reinforced concrete column under the RPS",
   "crumb": "Column size",
   "desc": "In Morocco, the RPS sets a minimum column dimension of 25 cm (30 cm for ductility class ND3). Reinforcement, closer stirrups at the ends and mistakes to avoid.",
   "lead": "The 20 × 20 cm column still seen on some sites does not comply with the seismic code. Here is what the RPS requires and what remains to be calculated.",
   "body": """
<p>Under the Moroccan seismic code (RPS 2000, 2011 version), the smallest dimension of a reinforced concrete column must be at least <b>25 cm</b> for ductility levels ND1 and ND2, and at least <b>30 cm</b> for level ND3. A 20 × 20 cm column is therefore not compliant, whatever load it carries.</p>
<h2>What the code sets</h2>
<div class="tableau"><table><thead><tr><th>Requirement</th><th>Value or principle</th></tr></thead><tbody>
<tr><td>Smallest dimension (ND1, ND2)</td><td>25 cm minimum</td></tr>
<tr><td>Smallest dimension (ND3)</td><td>30 cm minimum</td></tr>
<tr><td>Slenderness</td><td>Limited: a column that is too tall relative to its width must be widened</td></tr>
<tr><td>Critical zones</td><td>Closer stirrups at the ends of the column, at the bottom and top</td></tr>
<tr><td>Transverse reinforcement</td><td>Minimum diameter of 6 mm, closed stirrups</td></tr>
</tbody></table></div>
<p>The ductility level (ND1 to ND3) depends on the seismic zone, the building class and the structural system adopted by the engineer; the engineer states it in the design calculations.</p>
<h2>Reinforcement: to be calculated, not copied</h2>
<p>The number and diameter of the longitudinal bars depend on the calculated forces (vertical loads and earthquake). The code sets minimum and maximum steel percentages, and closer stirrups in the critical zones, near the floors, where plastic hinges form during an earthquake. In these zones, stirrup spacing is limited to roughly the smallest of three values: 8 times the diameter of the longitudinal bars, a quarter of the smallest column dimension, and 15 cm. The exact spacing and the length of the critical zones are <b>to be determined by the engineer</b>.</p>
<h2>Mistakes seen on site</h2>
<ul>
<li><b>20 cm columns</b> to "save space" in the walls: not compliant with the RPS.</li>
<li><b>Stirrups spaced 20 to 25 cm apart</b> over the full height, with no tighter spacing at the ends.</li>
<li><b>Unclosed stirrups</b> or poorly hooked ones, which open up during an earthquake.</li>
<li><b>Bar laps</b> all at the same level, just above the floor, in the most heavily loaded zone.</li>
<li><b>Short columns</b> created by a spandrel or partial wall: they concentrate forces and fail first.</li>
<li><b>Column-beam joints</b> without stirrups, because they are difficult to reinforce.</li>
</ul>
<h2>Interior, corner or façade column</h2>
<p>A corner or façade column does not carry the same load as a central column, but it undergoes more bending. Columns in the same row may therefore have different reinforcement. On a serious structural drawing, each column has a reference and specific reinforcement. To understand the regulatory context, read our article on <a href="conseil-reglement-parasismique-rps-2011-maroc.html">RPS 2011</a>.</p>
<h2>The role of the engineering firm</h2>
<p>The engineering firm calculates the forces in each column, sets its cross-section and reinforcement, and draws the stirrup details in the critical zones. <a href="conseil-controle-ferraillage-avant-coulage.html">Checking the reinforcement before pouring</a> makes it possible to verify that these provisions are actually in place before it is too late.</p>
""",
   "faq": [
    ("What is the minimum column size in Morocco?", "RPS 2000 (2011 version) requires a smallest dimension of at least 25 cm for ductility levels ND1 and ND2, and 30 cm for level ND3."),
    ("Is a 20 × 20 cm column allowed?", "No: it is below the 25 cm minimum dimension set by the Moroccan seismic code for reinforced concrete columns."),
    ("Why tighten the stirrups at the top and bottom of columns?", "These are the critical zones where forces concentrate during an earthquake: closely spaced stirrups confine the concrete and stop the bars from buckling."),
   ],
 },
 "conseil-plancher-hourdis-ou-dalle-pleine": {
   "title": "Hollow-block floor or solid slab: which one for your house?",
   "crumb": "Hollow-block or solid slab",
   "desc": "Beam-and-hollow-block floor (16+4, 20+5) or solid reinforced concrete slab: spans, weight, acoustics, cost and when each solution is needed in Morocco.",
   "lead": "The hollow-block floor is the most widespread solution for villas in Morocco, but the solid slab remains essential in certain cases. Here are the criteria to decide.",
   "body": """
<p>For a villa with typical spans (up to about 5 m), the <b>beam-and-hollow-block floor</b> is generally the most economical and the fastest to build. The <b>solid slab</b> is required for irregular shapes, cantilevers, heavy loads, wet areas or when you want a smooth soffit with no downstand beams. The choice lies with the engineer, in agreement with the architect.</p>
<h2>The hollow-block floor (hourdis)</h2>
<p>It consists of joists (precast or cast in place), hollow concrete or clay blocks (the hourdis) and a topping slab reinforced with welded mesh. It is designated by two figures: a <b>16+4</b> floor has 16 cm blocks and a 4 cm topping, i.e. about 20 cm in total; a <b>20+5</b> is about 25 cm.</p>
<div class="tableau"><table><thead><tr><th>Type</th><th>Total thickness</th><th>Typical use (indicative)</th></tr></thead><tbody>
<tr><td>16+4</td><td>≈ 20 cm</td><td>Typical residential spans, often up to about 5 m</td></tr>
<tr><td>20+5</td><td>≈ 25 cm</td><td>Longer spans or heavier loads</td></tr>
<tr><td>Solid slab</td><td>As per calculation</td><td>Complex shapes, cantilevers, bathrooms, accessible roof terraces</td></tr>
</tbody></table></div>
<p>Allowable spans depend on the joists used, the loads and the reinforcement: they are read from the manufacturer's tables or calculated. The values above are orders of magnitude, <b>to be confirmed by calculation</b>.</p>
<h2>The solid reinforced concrete slab</h2>
<p>It is a reinforced concrete plate cast on formwork, supported on beams or walls. It can span in one or two directions, which makes it suitable for irregular shapes, cantilevered balconies and openings. It is heavier and uses more concrete and steel, but offers better acoustic insulation against airborne noise and great freedom for routing services.</p>
<h2>Quick comparison</h2>
<ul>
<li><b>Cost</b>: advantage to the hollow-block floor on typical spans, with less concrete and formwork.</li>
<li><b>Weight</b>: the hollow-block floor is lighter, which reduces the loads on the columns, the foundations and the seismic force.</li>
<li><b>Shapes</b>: advantage to the solid slab for corners, cantilevers and large openings.</li>
<li><b>Acoustics</b>: the solid slab, being more massive, insulates better against airborne noise.</li>
<li><b>Fixings</b>: drilling into a hollow block requires suitable anchors for suspended loads.</li>
</ul>
<h2>Seismic requirements</h2>
<p>In both cases, the floor must act as a rigid <b>diaphragm</b> connecting the columns and walls. This requires a continuous topping slab, properly reinforced and connected to the ring beams and beams. A topping slab that is too thin or has no mesh compromises this role. On roof terraces, also think about <a href="conseil-etancheite-toiture-terrasse-maroc.html">waterproofing</a> and insulation.</p>
<h2>The role of the engineering firm</h2>
<p>The engineering firm chooses the floor type room by room, calculates spans and loads, defines the direction of the joists, the reinforcement around openings and the solid slab zones. The formwork drawings it provides prevent improvisation on site, such as a joist doubled "by eye" under a heavy partition.</p>
""",
   "faq": [
    ("What does a 16+4 floor mean?", "It is a joist floor with 16 cm high hollow blocks and a 4 cm topping slab, i.e. a total thickness of about 20 cm."),
    ("What span for a 16+4 hollow-block floor?", "It is commonly used for residential spans of up to about 5 m, but the allowable span depends on the joists and loads and must be checked by calculation."),
    ("Is a solid slab stronger than a hollow-block floor?", "Both are safe if they are designed. The solid slab is better suited to irregular shapes, cantilevers and heavy loads; the hollow-block floor is lighter and more economical on typical spans."),
   ],
 },
 "conseil-poutre-portee-retombee": {
   "title": "Reinforced concrete beam: what downstand for what span?",
   "crumb": "Beam spans",
   "desc": "Preliminary beam sizing: depth of L/15 to L/10 of the span, i.e. 35 to 50 cm for 5 m. Width, RPS (b ≥ 20 cm) and ways of reducing the downstand.",
   "lead": "The downstand of a beam is often a topic of discussion between architect, client and engineer. Here are the orders of magnitude and the real room for manoeuvre.",
   "body": """
<p>For preliminary sizing, the total depth of a reinforced concrete beam is between <b>1/15 and 1/10 of its span</b>. A beam spanning 5 m between supports will therefore be about 35 to 50 cm deep, part of which projects below the floor: this is the <b>downstand</b>. These ratios are used to start the project; the final cross-section is <b>set by calculation</b>.</p>
<h2>Preliminary sizing orders of magnitude</h2>
<div class="tableau"><table><thead><tr><th>Span between supports</th><th>Depth L/15</th><th>Depth L/10</th></tr></thead><tbody>
<tr><td>3 m</td><td>20 cm</td><td>30 cm</td></tr>
<tr><td>4 m</td><td>27 cm</td><td>40 cm</td></tr>
<tr><td>5 m</td><td>33 cm</td><td>50 cm</td></tr>
<tr><td>6 m</td><td>40 cm</td><td>60 cm</td></tr>
</tbody></table></div>
<p>The width is commonly between 0.4 and 0.7 times the depth. The heavier the load (wall above, column resting on the beam), the closer you get to L/10, or even beyond. A cantilever beam is designed differently and generally requires a much greater depth relative to its length.</p>
<h2>RPS rules for beams</h2>
<p>The Moroccan seismic code sets minimum dimensions for beams forming part of the bracing system: a <b>width of at least 20 cm</b>, a width-to-depth ratio of at least 0.25, and a width limited relative to that of the supporting column. It also requires longitudinal bars of at least 10 mm and closer stirrups near the supports, in the critical zones.</p>
<h2>How to reduce the downstand?</h2>
<ul>
<li><b>Add a support</b> (column or wall) to divide the span: this is the most effective solution.</li>
<li><b>Widen the beam</b> and reduce its depth (flat beam or beam embedded in the floor), at the cost of more steel and a deflection to be checked.</li>
<li><b>Use a solid slab</b> spanning in two directions rather than a single beam.</li>
<li><b>Switch to a steel beam</b> or prestressed concrete for very long spans.</li>
<li><b>Place the beam as an upstand</b>, above the floor, when the use allows it (terrace, parapet).</li>
</ul>
<p>Each option has consequences on cost, deflection and seismic behaviour; they are discussed at the preliminary design stage, not on site.</p>
<h2>Deflection, often overlooked</h2>
<p>A beam that is too thin may resist without breaking but deform excessively: tiles coming loose, cracked partitions, jammed doors and windows. It is often deflection, more than strength, that governs the depth of a long-span beam. If you notice cracks, our article on <a href="conseil-fissures-maison-causes-gravite.html">cracks in a house</a> will help you interpret them.</p>
<h2>The role of the engineering firm</h2>
<p>The engineering firm balances architectural requirements and structural constraints: it calculates each beam, checks deflection and RPS compliance, and proposes alternatives if a downstand is a problem. Any removal of a column or increase in span during construction must be submitted to it (see <a href="conseil-supprimer-mur-porteur-ouverture.html">opening a load-bearing wall</a>).</p>
""",
   "faq": [
    ("What beam depth for a 5 m span?", "For preliminary sizing, between L/15 and L/10, i.e. about 35 to 50 cm for 5 m. The final depth depends on the loads and deflection and must be calculated."),
    ("What is the minimum beam width under the RPS?", "The Moroccan seismic code requires a width of at least 20 cm and a width-to-depth ratio of at least 0.25 for beams."),
    ("Can the downstand of a beam be eliminated?", "It can be reduced with a wider flat beam, an additional support or a solid slab, but each solution must be calculated by the engineer."),
   ],
 },
 "conseil-enrobage-armatures-beton": {
   "title": "Concrete cover to reinforcement: what values should you respect?",
   "crumb": "Reinforcement cover",
   "desc": "Concrete cover to steel: 1 to 5 cm under the BAEL, about 25 to 45 mm under Eurocode 2 depending on exposure. Its role against corrosion and how to check it.",
   "lead": "Cover is the thickness of concrete between the steel and the surface. A few millimetres less are enough to make the reinforcement rust and the concrete spall within a few years.",
   "body": """
<p>Cover is the distance between the concrete surface and the nearest reinforcement, stirrups included. The values depend on the exposure of the structure: with the <b>BAEL 91</b>, still widely used in Morocco, the values are 1 cm inside closed, dry premises, 3 cm for surfaces exposed to the weather or condensation, and 5 cm in marine or highly aggressive environments. With <b>Eurocode 2</b>, the nominal cover is generally between 25 and 45 mm depending on the exposure class.</p>
<h2>Why cover is vital</h2>
<p>Concrete naturally protects steel from corrosion thanks to its alkalinity. Over time, carbon dioxide from the air penetrates the concrete (carbonation) and eventually reaches the reinforcement if the cover is too thin. The steel rusts, swells and makes the concrete burst: this is the classic defect of balconies, parapets and façade columns that spall. Cover also ensures the bond between steel and concrete and provides protection in case of fire.</p>
<h2>Reference values</h2>
<div class="tableau"><table><thead><tr><th>Situation</th><th>BAEL 91 (art. A.7.1)</th><th>Eurocode 2 (indicative, class S4)</th></tr></thead><tbody>
<tr><td>Dry interior, closed premises</td><td>1 cm</td><td>≈ 25 mm (XC1)</td></tr>
<tr><td>Exterior, weather, condensation</td><td>3 cm (2 cm if concrete > 40 MPa)</td><td>≈ 35 to 40 mm (XC3, XC4)</td></tr>
<tr><td>Marine or highly aggressive environment</td><td>5 cm</td><td>≈ 45 mm and more (XS)</td></tr>
<tr><td>Concrete cast against the ground</td><td>Increased value</td><td>40 mm on blinding concrete, 75 mm against bare soil</td></tr>
</tbody></table></div>
<p>With Eurocode 2, the nominal cover equals the minimum cover plus a construction tolerance, generally 10 mm. The exact values depend on the structural class, the concrete class and the national annex applied: they are <b>set by the engineer</b> on the drawings. The diameter of the largest bar is also a minimum.</p>
<h2>How to guarantee cover on site</h2>
<ul>
<li><b>Spacers</b> in concrete or plastic, of the right thickness, in sufficient numbers (not pieces of brick or stone).</li>
<li><b>Chairs</b> for the top mesh of slabs, so that it is not crushed under the workers' feet.</li>
<li><b>Clean and stable formwork</b>, so that the reinforcement does not move during pouring.</li>
<li><b>Proper vibration</b>, without touching the reinforcement, to avoid honeycombing.</li>
</ul>
<h2>The Marrakech climate</h2>
<p>High temperatures and dry air speed up the drying of surface concrete, which becomes more porous if curing is neglected: the protection provided by the cover decreases. Proper <a href="conseil-cure-beton-chaleur-marrakech.html">concrete curing</a> is therefore the essential complement to correct cover. Swimming pools, buried structures and tanks deserve higher values.</p>
<h2>The role of the engineering firm</h2>
<p>The engineering firm specifies the cover of each element on the drawings and checks it during the <a href="conseil-controle-ferraillage-avant-coulage.html">reinforcement inspection before pouring</a>. Insufficient cover is one of the most frequent defects found, and one of the most expensive to repair later.</p>
""",
   "faq": [
    ("What cover for an exterior column?", "Under BAEL 91, 3 cm for a surface exposed to the weather; under Eurocode 2, about 35 to 40 mm depending on the exposure class. The exact value is shown on the engineer's drawings."),
    ("What cover for a foundation footing?", "Concrete cast against the ground requires increased cover: Eurocode 2, for example, uses 40 mm on blinding concrete and 75 mm directly against the soil."),
    ("What happens if the cover is insufficient?", "The reinforcement eventually rusts, swells and makes the concrete burst: this is the origin of much spalling on balconies, parapets and façade columns."),
   ],
 },
 "conseil-controle-ferraillage-avant-coulage": {
   "title": "Checking reinforcement before pouring: the site checklist",
   "crumb": "Reinforcement inspection",
   "desc": "Before each pour, check bar diameters and numbers, stirrups, laps, anchorages, cover and cleanliness: the inspection checklist used by an engineering firm.",
   "lead": "Once the concrete is poured, it is too late: the reinforcement becomes invisible. The inspection before pouring is when the real strength of your structure is decided.",
   "body": """
<p>Before each pour of footings, columns, beams or slabs, the reinforcement must be compared point by point with the construction drawings: <b>bar diameters and numbers, stirrup spacing, laps, anchorages, cover and cleanliness</b>. This inspection, carried out by the engineering firm or the technical inspection body, often takes less than an hour and prevents irreparable defects.</p>
<h2>The inspection checklist</h2>
<div class="tableau"><table><thead><tr><th>Item</th><th>What is checked</th></tr></thead><tbody>
<tr><td>Main bars</td><td>Number, diameter (HA10, HA12, HA14…) and position as per the drawing</td></tr>
<tr><td>Stirrups and links</td><td>Diameter, spacing, closer spacing in critical zones, closed stirrups</td></tr>
<tr><td>Laps</td><td>Sufficient length, staggered and not all at the same place</td></tr>
<tr><td>Anchorages</td><td>Beam bars anchored into the columns, starter bars in place for the next floor</td></tr>
<tr><td>Column-beam joints</td><td>Stirrups present in the joint, despite the difficulty of placing them</td></tr>
<tr><td>Cover</td><td>Spacers and chairs of the right thickness, in sufficient numbers</td></tr>
<tr><td>Cleanliness</td><td>Bars free of soil, oil and loose rust; formwork cleaned</td></tr>
<tr><td>Openings and sleeves</td><td>Ducts and sleeves provided, without cutting or moving the reinforcement</td></tr>
</tbody></table></div>
<h2>The most frequent defects</h2>
<ul>
<li><b>Substituted diameters</b>: an HA12 instead of an HA14, due to lack of stock. The steel area drops by nearly 27%.</li>
<li><b>Stirrups too far apart</b> at the ends of columns and beams, where the seismic code requires them to be closer.</li>
<li><b>Poorly formed hooks</b>: seismic rules require stirrups closed by hooks bent into the concrete core, which do not open in an earthquake.</li>
<li><b>Laps too short</b>. When the drawings give no indication, the BAEL gives a standard length of about 50 diameters for FeE500 steel (40 diameters for FeE400).</li>
<li><b>Crushed top mesh</b> in slabs, which loses all effectiveness over supports and cantilevers.</li>
<li><b>Forgotten top bars</b> over beams and slab supports.</li>
</ul>
<h2>How to organise the inspection</h2>
<p>Stipulate in the contractor's contract that each pour of a structural element is preceded by acceptance of the reinforcement, with a notice period (for example 24 to 48 hours). The inspector writes a report with photos, and the corrections are checked before the pour is authorised. Dated photos then form a useful archive for handover and in case of dispute. See also our article on <a href="conseil-suivi-de-chantier-bet-visites.html">site supervision by the engineering firm</a>.</p>
<h2>After the inspection: the pour</h2>
<p>Inspecting the reinforcement is pointless if the concrete is then poorly placed: added water, no vibration, pouring in high heat without precautions. The inspector also checks the mix or the delivery note of the ready-mixed concrete, and has test cubes or cylinders taken on important elements. On mix design, read our article on <a href="conseil-dosage-beton-fondation-dalle.html">concrete mix proportions</a>.</p>
<h2>The role of the engineering firm</h2>
<p>The engineering firm that designed the structure is best placed to inspect its reinforcement: it knows which details are critical and why. Its visits before pouring turn drawings on paper into a structure that genuinely complies with RPS 2011.</p>
""",
   "faq": [
    ("Who should inspect the reinforcement before pouring?", "The engineering firm that designed the structure or the appointed technical inspection body. The contractor must notify it in advance of each pour of a load-bearing element."),
    ("What lap length for reinforcing bars?", "It is shown on the drawings; without a calculation, the BAEL gives a standard value of about 50 diameters for FeE500 steel and 40 diameters for FeE400."),
    ("Can an HA14 be replaced by an HA12?", "Not without the engineer's approval: the steel area drops from 1.54 to 1.13 cm² per bar, i.e. about 27% less."),
   ],
 },
 "conseil-cure-beton-chaleur-marrakech": {
   "title": "Curing concrete in hot weather: best practice in Marrakech",
   "crumb": "Concrete curing",
   "desc": "Above 25 °C, concrete needs precautions: pour early in the morning, water it, cover it, use a curing compound. Best practice for summer concreting in Marrakech.",
   "lead": "When it is over 40 °C in Marrakech, poorly protected concrete can lose a significant part of its strength and become covered in cracks within a few hours.",
   "body": """
<p>In hot weather, concrete must be <b>poured during the cool hours</b> and <b>kept moist for several days</b>: regular watering, wet sheets or hessian, or a sprayed curing compound. Cement manufacturers' guides recommend special measures as soon as the temperature exceeds 25 °C. In Marrakech, where summer temperatures often exceed 40 °C, these precautions are not optional.</p>
<h2>Why heat damages concrete</h2>
<p>Concrete hardens through a chemical reaction between cement and water, called hydration. If the water evaporates too quickly, this reaction stops at the surface: the concrete becomes porous, weaker and less protective for the reinforcement. Heat also speeds up setting, which makes placing and vibration harder. The result: plastic shrinkage cracks on the surface of slabs, crazing, loss of strength. According to technical sources, concrete cured in a dry environment can lose a significant part of its strength compared with concrete kept moist.</p>
<h2>Before and during pouring</h2>
<ul>
<li><b>Pour early in the morning</b> (or late in the day), never during the hottest hours.</li>
<li><b>Dampen the formwork</b> and the substrate (blinding concrete, hollow blocks) without leaving standing water.</li>
<li><b>Protect aggregates and water</b> from the sun for site-mixed concrete; for ready-mixed concrete, ask for a suitable mix (set retarder).</li>
<li><b>Never add water</b> to the concrete to make up for its stiffness: this is the leading cause of weak concrete.</li>
<li><b>Pour quickly</b>, with a pump if possible, and vibrate properly.</li>
<li><b>Postpone the pour</b> if conditions (hot wind, extreme heat) do not allow proper work.</li>
</ul>
<h2>After pouring: curing</h2>
<div class="tableau"><table><thead><tr><th>Method</th><th>How to apply it</th></tr></thead><tbody>
<tr><td>Watering</td><td>Misting or fine watering several times a day, without letting it dry between passes</td></tr>
<tr><td>Sheets, wet hessian</td><td>Laid as soon as the surface allows, kept moist; light-coloured mats facing the sun</td></tr>
<tr><td>Curing compound</td><td>Sprayed just after finishing, it forms a film that limits evaporation</td></tr>
<tr><td>Leaving formwork in place</td><td>Formed faces dry more slowly as long as the formwork remains in place</td></tr>
</tbody></table></div>
<p>The curing period depends on the cement, the temperature and the element; several days are a minimum in hot weather, and the specifications or the engineering firm may set a precise duration.</p>
<h2>The most sensitive elements</h2>
<p>Slabs and roof terraces, highly exposed to sun and wind, are the most vulnerable: their large surface area encourages evaporation. Swimming pool walls and tanks, which must remain watertight, deserve particularly careful curing. Neglected curing also reduces the effectiveness of the <a href="conseil-enrobage-armatures-beton.html">reinforcement cover</a>.</p>
<h2>The role of the engineering firm</h2>
<p>The engineering firm includes hot-weather concreting requirements in the specifications and checks compliance during site visits. It can also have test specimens taken to check the actual strength of the concrete before approving <a href="conseil-delai-decoffrage-dalle-poteaux.html">formwork removal</a>.</p>
""",
   "faq": [
    ("Above what temperature are precautions needed when pouring concrete?", "Cement manufacturers' guides recommend special measures as soon as the temperature exceeds 25 °C: pouring during the cool hours, protection and enhanced curing."),
    ("How long should a concrete slab be watered in summer?", "Several days at least in hot weather, keeping the surface constantly moist; the exact duration may be set by the specifications or the engineering firm."),
    ("Can water be added to concrete when it is hot?", "No: added water reduces strength and increases porosity. Use a retarding admixture instead, or pour during cooler hours."),
   ],
 },
 "conseil-delai-decoffrage-dalle-poteaux": {
   "title": "Formwork striking times for slabs, beams and columns",
   "crumb": "Striking times",
   "desc": "Column sides and beam sides: 1 to 3 days. Slab soffits and props: often 21 to 28 days, or back-propping. Indicative striking times and precautions to take.",
   "lead": "Striking formwork too early is one of the classic causes of excessive deflection, cracking and even collapse. Here are the times to respect depending on the element and conditions.",
   "body": """
<p>Vertical formwork (column sides, walls, beam sides) can generally be removed after <b>1 to 3 days</b>, as it carries no load. Soffit formwork and props under slabs and beams must stay in place much longer, commonly <b>21 to 28 days</b>, or be replaced by back-propping. These times are indicative: the rule is to strike only once the concrete has reached sufficient strength.</p>
<h2>Indicative times by element</h2>
<div class="tableau"><table><thead><tr><th>Element</th><th>Usual time (indicative)</th><th>Remark</th></tr></thead><tbody>
<tr><td>Column and wall sides</td><td>1 to 3 days</td><td>Wait until the edges no longer tear off when striking</td></tr>
<tr><td>Beam sides</td><td>1 to 3 days</td><td>The beam soffit and its props stay in place</td></tr>
<tr><td>Slab and beam soffits</td><td>Often 21 to 28 days</td><td>Earlier striking possible with back-propping</td></tr>
<tr><td>Cantilevers, balconies</td><td>Longer, as specified by the engineer</td><td>Elements very sensitive to premature striking</td></tr>
</tbody></table></div>
<p>Concrete only reaches its design strength at 28 days, but it develops a large part of it in the first week, especially in hot weather. This is why some formwork can be removed earlier, provided props are left to carry the slab.</p>
<h2>What makes the times vary</h2>
<ul>
<li><b>Temperature</b>: concrete hardens faster in the heat and more slowly in cold weather (Atlas winters).</li>
<li><b>The type of cement</b> and the concrete mix.</li>
<li><b>The span</b>: a large slab or a long beam needs more time.</li>
<li><b>Construction loads</b>: a floor that is already carrying the formwork and concrete of the floor above must remain propped.</li>
<li><b>Curing</b>: concrete that has dried too quickly does not have the expected strength.</li>
</ul>
<h2>Back-propping</h2>
<p>To reuse formwork faster, contractors use back-propping: the floor is struck and props are immediately put back to relieve it until it has reached its strength. This method is safe if it is organised bay by bay, without leaving the floor unsupported. In a multi-storey building, props over several floors often add up: a propping plan is needed.</p>
<h2>Signs of premature striking</h2>
<p>Visible deflection of the slab, cracks on the soffit or near the supports, chipped column edges, or honeycombing revealed too early. Excessive deflection is often irreversible. If in doubt, have the <a href="conseil-fissures-maison-causes-gravite.html">cracks</a> examined by an engineer.</p>
<h2>The role of the engineering firm</h2>
<p>The engineering firm sets the minimum striking times and conditions in the specifications, taking the season into account. For sensitive elements, it may require tests on specimens before authorising removal of the props. Proper <a href="conseil-cure-beton-chaleur-marrakech.html">concrete curing</a> also determines the strength at the time of striking.</p>
""",
   "faq": [
    ("When can a concrete slab be struck?", "The soffit formwork and props generally stay in place for 21 to 28 days, unless organised back-propping is used. The exact time depends on the span, the temperature and the strength reached."),
    ("How long before striking a column?", "Column sides can generally be removed after 1 to 3 days, when the concrete is hard enough for the edges not to tear off."),
    ("What is back-propping?", "It means putting props back under a slab just after striking, to relieve it until it reaches its strength while allowing the formwork to be reused."),
   ],
 },
 "conseil-supprimer-mur-porteur-ouverture": {
   "title": "Opening or removing a load-bearing wall: steps, risks and design",
   "crumb": "Load-bearing wall",
   "desc": "Opening a load-bearing wall requires a structural study, propping, a designed beam (concrete or steel) and sometimes a permit. Steps and pitfalls in Morocco.",
   "lead": "Enlarging a living room or creating a wide opening by removing a load-bearing wall is possible, provided the loads are transferred correctly. What you need to know before demolishing.",
   "body": """
<p>Yes, a load-bearing wall can be opened up or removed, but only after a <b>structural study</b> that calculates the loads to be carried, sizes the <b>replacement beam</b> (reinforced concrete or steel) and checks its supports down to the foundations. The work is carried out under <b>propping</b>, by a qualified contractor. In Morocco, a structural alteration may also require a permit and, in a co-owned building, the agreement of the co-owners.</p>
<h2>How do you know if a wall is load-bearing?</h2>
<p>A wall is load-bearing if it supports a floor, a roof or another wall. In a recent villa with a concrete frame (columns and beams), most walls are simple infill; in an old house, a riad or a confined masonry building, thick walls are almost always load-bearing. The clues: thickness, central position, joists resting on it. Only the structural drawings or a survey can settle the matter.</p>
<h2>The steps of an opening</h2>
<ol>
<li><b>Survey and design</b>: survey of the existing building, load take-down, choice of beam and supports, check of the foundations under the new support points.</li>
<li><b>Permits</b>: depending on the nature of the work and the municipality, application via the Rokhas platform; agreement of the co-owners in an apartment building.</li>
<li><b>Propping</b>: props and timber beams on both sides of the wall to relieve the floor during the work.</li>
<li><b>Creating the supports</b>: reinforced concrete columns or padstones at the ends of the opening.</li>
<li><b>Installing the beam</b>: reinforced concrete beam cast in place or steel section, packed and grouted onto its supports.</li>
<li><b>Demolition</b> of the wall under the beam, then removal of the props once the grout has hardened.</li>
</ol>
<h2>The risks of an improvised opening</h2>
<ul>
<li><b>Cracking and sagging</b> of the floor above if the beam is too weak or poorly packed.</li>
<li><b>Bearing failure</b> at the supports: a well-sized beam resting on fragile masonry crushes its support.</li>
<li><b>Reduced seismic resistance</b>: a load-bearing wall often contributes to bracing; removing it can make the building vulnerable to earthquakes, as the damage in Al Haouz showed.</li>
<li><b>Inadequate foundations</b> under the new columns, which concentrate the loads.</li>
</ul>
<h2>Concrete or steel?</h2>
<p>A steel beam (IPN, IPE, HEA) is quick to install and limits the downstand, but must be protected against corrosion and sometimes against fire. A reinforced concrete beam, cast in place, requires formwork and a hardening period but integrates well into a concrete structure. The choice depends on the span, the acceptable downstand and site access.</p>
<h2>The role of the engineering firm</h2>
<p>The engineering firm carries out the survey, the design calculations and the construction drawings, then inspects the propping and the installation of the beam. It also checks the impact on the overall seismic stability, particularly in a <a href="conseil-surelevation-ajouter-etage-maroc.html">vertical extension</a> or a major renovation. Before buying a property to convert, a <a href="conseil-verifier-structure-maison-avant-achat.html">structural check</a> avoids unpleasant surprises.</p>
""",
   "faq": [
    ("Can a load-bearing wall be removed in a house?", "Yes, provided a replacement beam and its supports are designed by a structural engineer and the work is carried out under propping."),
    ("Is a permit needed to open a load-bearing wall in Morocco?", "A structural alteration may require a permit from the municipality, to be checked depending on the work, and the agreement of the co-owners in an apartment building."),
    ("What beam should replace a load-bearing wall?", "A reinforced concrete beam or a steel section (IPN, IPE, HEA), whose size depends on the span and loads and must be set by the design calculations."),
   ],
 },
 "conseil-joint-de-dilatation-batiment": {
   "title": "Building expansion joints: when are they needed and how often?",
   "crumb": "Expansion joint",
   "desc": "In a hot, dry climate like Marrakech, an expansion joint is often provided about every 25 m, plus a seismic joint at least 5 cm wide as required by the RPS.",
   "lead": "A concrete building expands in the heat and contracts in the cold. Beyond a certain length, it must be split into independent blocks to avoid cracking.",
   "body": """
<p>An expansion joint splits the building into independent blocks to absorb changes in length due to temperature and concrete shrinkage. The French BAEL rules, often used in Morocco, recommend a joint about every <b>25 m in dry, hot regions</b> with large temperature swings (close to the Mediterranean climate), and up to 50 m in humid, temperate regions. In Marrakech, a block length of around 25 m is therefore most often adopted, unless justified by calculation.</p>
<h2>Why joints are necessary</h2>
<p>Concrete expands by about 1 mm per 10 m of length for a 10 °C difference. Between a winter night and a sunny summer day, a roof terrace in Marrakech can undergo several tens of degrees of variation. If it cannot move freely, a long building accumulates forces that crack the walls, slabs and parapets. Concrete shrinkage on drying has the same effect.</p>
<h2>Orders of magnitude</h2>
<div class="tableau"><table><thead><tr><th>Structure</th><th>Distance between joints (indicative)</th></tr></thead><tbody>
<tr><td>Reinforced concrete structure, hot and dry climate</td><td>About 25 m (BAEL rules, Mediterranean regions)</td></tr>
<tr><td>Reinforced concrete structure, humid and temperate climate</td><td>Up to 40 to 50 m</td></tr>
<tr><td>Masonry façade walls</td><td>Lower values, around 20 m in a Mediterranean climate</td></tr>
<tr><td>Ground slabs, terraces, parapets</td><td>Closer jointing, depending on the finish</td></tr>
</tbody></table></div>
<p>These distances are benchmarks: the engineer may increase them by calculating the thermal effects, or reduce them for an irregular shape.</p>
<h2>Expansion joint and seismic joint</h2>
<p>In Morocco, the seismic code RPS 2000 (2011 version) adds a requirement: two adjacent blocks must be separated by a <b>seismic joint</b> wide enough to stop them from pounding against each other during an earthquake. The texts set a minimum width of <b>5 cm</b>, to be increased according to the height of the blocks and the calculated displacements. In practice, the expansion joint is sized to serve as the seismic joint as well. A joint is also recommended between two parts with very different heights or shapes (L-shaped block, a four-storey part adjoining a two-storey part).</p>
<h2>Building a joint properly</h2>
<ul>
<li><b>Complete separation</b> of the structure from ground to roof (columns and beams doubled on each side); the foundations can remain shared, unless the soil is heterogeneous.</li>
<li><b>Empty joint</b>: no rubble or mortar stuck inside, otherwise it no longer works.</li>
<li><b>Joint covers</b> on the façade, roof and floor, which allow the movement to occur.</li>
<li><b>Waterproofing</b> treated with a specific upstand on the roof terrace (see <a href="conseil-etancheite-toiture-terrasse-maroc.html">roof terrace waterproofing</a>).</li>
<li><b>Services</b> (pipes, cables) fitted with flexible sleeves where they cross the joint.</li>
</ul>
<h2>The role of the engineering firm</h2>
<p>The engineering firm divides the building into blocks from the design stage, taking into account the climate, the shape and the RPS, and sizes the width of the joints. Regular <a href="conseil-fissures-maison-causes-gravite.html">cracks</a> along a long building without joints are often a sign that this step was forgotten.</p>
""",
   "faq": [
    ("How many metres apart should expansion joints be?", "In a hot, dry climate like Marrakech, the BAEL rules lead to about 25 m between joints for a reinforced concrete structure; up to 50 m in a humid, temperate climate."),
    ("How wide should a seismic joint be in Morocco?", "RPS 2000 (2011 version) sets a minimum width of 5 cm between blocks, to be increased according to the building height and the calculated displacements."),
    ("Does a villa need an expansion joint?", "A compact villa less than 25 m long generally does not need one, unless it has a very irregular shape or parts of different heights, to be assessed by the engineer."),
   ],
 },
 "conseil-mur-de-soutenement-calcul": {
   "title": "Retaining wall: design, drainage and mistakes to avoid",
   "crumb": "Retaining wall",
   "desc": "A retaining wall is checked for overturning, sliding and soil bearing capacity. Earth pressure, drainage, weep holes: have it designed from 1.50 m upwards.",
   "lead": "A retaining wall holds back tonnes of soil and often water. Poorly designed or poorly drained, it tips over or cracks: it is a structure that must be designed by calculation.",
   "body": """
<p>A retaining wall is designed on the basis of the <b>earth pressure</b> it retains, the surcharges (cars, buildings upslope) and the presence of water. The checks ensure that it does not <b>overturn</b>, does not <b>slide</b>, that the soil under its footing <b>bears</b> it and that the concrete and steel are strong enough. Insurers recommend a study by an engineering firm beyond 1.50 m of retained height, and drainage is as important as the calculation.</p>
<h2>The forces involved</h2>
<p>Earth pressure increases with depth: it is zero at the top of the wall and maximum at its base. It depends on the nature of the soil (density, friction angle, cohesion). A car parked at the top, a neighbouring house or a swimming pool add a surcharge. Above all, water building up behind an undrained wall adds hydrostatic pressure that can double the forces. In a seismic zone like Marrakech, earthquakes also increase the pressure.</p>
<h2>The four checks</h2>
<div class="tableau"><table><thead><tr><th>Check</th><th>Risk avoided</th><th>Means</th></tr></thead><tbody>
<tr><td>Overturning</td><td>The wall tips over downslope</td><td>Wider footing, heel under the retained soil</td></tr>
<tr><td>Sliding</td><td>The wall slides on its base</td><td>Shear key under the footing, wider footing</td></tr>
<tr><td>Soil bearing capacity</td><td>The soil gives way under the toe of the footing</td><td>Footing sized from the soil investigation</td></tr>
<tr><td>Wall strength</td><td>The stem cracks or fails</td><td>Calculated thickness and reinforcement</td></tr>
</tbody></table></div>
<h2>Types of wall</h2>
<ul>
<li><b>Reinforced concrete "inverted T" wall</b>: a stem fixed to a footing with a toe at the front and a heel under the retained soil. This is the most common solution for a villa.</li>
<li><b>Gravity wall</b> in masonry, stone or unreinforced concrete: it resists through its mass, suitable for low heights.</li>
<li><b>Gabion or block walls</b>: free-draining by nature, suitable for landscaping.</li>
</ul>
<h2>Drainage, the weak point of failed walls</h2>
<p>A large share of retaining wall failures comes from poor water drainage. A well-designed wall includes:</p>
<ul>
<li><b>A drainage layer</b> of gravel behind the wall, separated from the soil by a geotextile.</li>
<li><b>A drain</b> at the base, connected to an outlet.</li>
<li><b>Weep holes</b>: pipes passing through the wall, sloping slightly downslope, which let the water out.</li>
<li><b>Waterproofing or a bituminous coating</b> on the face against the soil if the wall borders a room.</li>
</ul>
<p>Weep holes and drains must be maintained: when blocked, they leave the wall as vulnerable as if it had none.</p>
<h2>The role of the engineering firm</h2>
<p>The engineering firm relies on the <a href="conseil-etude-de-sol-maroc-prix.html">soil investigation</a> to design the wall, and provides the formwork and reinforcement drawings and the drainage details. For a basement, the retaining wall is also the wall of the room: see our article on <a href="conseil-sous-sol-cuvelage-infiltrations.html">basement tanking</a>.</p>
""",
   "faq": [
    ("From what height should a retaining wall be designed by an engineer?", "Insurers recommend a study by an engineering firm beyond 1.50 m of retained soil, and whenever there is a surcharge upslope or water."),
    ("What are weep holes for?", "They are pipes passing through the wall that drain the water building up behind it; without them, the water pressure adds to the earth pressure."),
    ("Why does a retaining wall tip over?", "Most often because of a footing that is too narrow, an unforeseen surcharge, or missing or blocked drainage that lets water push on the wall."),
   ],
 },
}
