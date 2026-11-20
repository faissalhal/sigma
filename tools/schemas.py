"""Schémas explicatifs des articles « Conseils » : illustrations techniques en SVG, légendes en FR / EN / AR.

Style « illustration technique » : matières (carrelage, béton, terre, acier), ombres douces, pastilles numérotées
sur le dessin et panneau de légende à côté. Les valeurs dessinées sont celles de l'article (aucune cote inventée).
Sortie : images/schemas/<langue>/<nom>.svg — Usage : python3 tools/schemas.py
"""
import html, os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
JAUNE, ENCRE, GRIS, TRAIT = "#f5b400", "#1f2328", "#5b6470", "#d5dae1"
BLEU, BLEU_F, ROUGE = "#2f6fb3", "#1d4f86", "#c0392b"
POLICE = "'Source Sans 3','Segoe UI',Arial,sans-serif"
W, H = 1200, 760
PANNEAU_X = 812          # début du panneau de légende (à droite ; à gauche en arabe)


def esc(s):
    return html.escape(s)


def t(x, y, s, taille=17, poids=400, couleur=ENCRE, ancre="start", rtl=False, extra=""):
    if rtl and ancre in ("start", "end"):
        ancre = "end" if ancre == "start" else "start"
    d = ' direction="rtl"' if rtl else ""
    return (f'<text x="{x}" y="{y}" font-size="{taille}" font-weight="{poids}" fill="{couleur}" '
            f'text-anchor="{ancre}"{d} {extra}>{esc(s)}</text>')


DEFS = f"""<defs>
<filter id="ombre" x="-10%" y="-10%" width="130%" height="140%"><feDropShadow dx="0" dy="6" stdDeviation="7" flood-color="#0b1a2b" flood-opacity=".16"/></filter>
<filter id="ombre2" x="-5%" y="-5%" width="110%" height="120%"><feDropShadow dx="0" dy="2" stdDeviation="2" flood-color="#000" flood-opacity=".18"/></filter>
<marker id="fl" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="8" markerHeight="8" orient="auto-start-reverse"><path d="M0 1 L10 5 L0 9 z" fill="{ENCRE}"/></marker>
<pattern id="carreaux" width="40" height="40" patternUnits="userSpaceOnUse"><rect width="40" height="40" fill="#f4f6f8"/><path d="M40 0H0V40" fill="none" stroke="#dde2e8" stroke-width="2"/></pattern>
<pattern id="sol" width="60" height="22" patternUnits="userSpaceOnUse"><rect width="60" height="22" fill="#cfc6b8"/><path d="M60 0H0V22" fill="none" stroke="#b9ae9d" stroke-width="2"/></pattern>
<pattern id="beton" width="26" height="26" patternUnits="userSpaceOnUse"><rect width="26" height="26" fill="#dfe2e6"/><circle cx="4" cy="5" r="1.3" fill="#b4b9c1"/><circle cx="17" cy="9" r="1" fill="#a9afb8"/><circle cx="9" cy="19" r="1.6" fill="#bfc4cb"/><circle cx="21" cy="21" r="1" fill="#a9afb8"/><path d="M12 3 l3 2 -2 2z" fill="#c4c8ce"/></pattern>
<pattern id="maigre" width="18" height="18" patternUnits="userSpaceOnUse"><rect width="18" height="18" fill="#b9bdc3"/><circle cx="4" cy="4" r="1.6" fill="#8f949c"/><circle cx="13" cy="11" r="2" fill="#9ea3aa"/></pattern>
<pattern id="terre" width="22" height="22" patternUnits="userSpaceOnUse" patternTransform="rotate(45)"><rect width="22" height="22" fill="#e8d6b8"/><line x1="0" y1="0" x2="0" y2="22" stroke="#d6bf98" stroke-width="5"/></pattern>
<linearGradient id="emaille" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#ffffff"/><stop offset="1" stop-color="#dfe6ee"/></linearGradient>
<linearGradient id="eau" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#5b9ad8"/><stop offset="1" stop-color="#2f6fb3"/></linearGradient>
<linearGradient id="acier" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#e2574c"/><stop offset=".5" stop-color="#c0392b"/><stop offset="1" stop-color="#8e2a20"/></linearGradient>
<linearGradient id="ciel" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#eef4fb"/><stop offset="1" stop-color="#ffffff"/></linearGradient>
</defs>"""


def pastille(x, y, n, couleur=JAUNE, texte=ENCRE):
    return (f'<g filter="url(#ombre2)"><circle cx="{x}" cy="{y}" r="17" fill="{couleur}" stroke="#fff" stroke-width="3"/></g>'
            f'<text x="{x}" y="{y + 6}" font-size="17" font-weight="800" fill="{texte}" text-anchor="middle">{esc(str(n))}</text>')


def cote(x1, y1, x2, y2, texte, tx, ty, rot=0):
    r = f' transform="rotate({rot} {tx} {ty})"' if rot else ""
    return (f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{ENCRE}" stroke-width="1.8" marker-start="url(#fl)" marker-end="url(#fl)"/>'
            f'<g{r}><rect x="{tx - 38}" y="{ty - 15}" width="76" height="24" rx="12" fill="#fff" stroke="{ENCRE}" stroke-width="1.2"/>'
            f'<text x="{tx}" y="{ty + 3}" font-size="15" font-weight="700" fill="{ENCRE}" text-anchor="middle">{esc(texte)}</text></g>')


def panneau(items, rtl, y0=112, titre_panneau=None, pas_serre=False):
    """Panneau de légende : [(pastille ou couleur, titre, ligne 1, ligne 2, couleur de ligne 2)]."""
    x0 = 24 if rtl else PANNEAU_X
    w = W - PANNEAU_X - 24
    out = [f'<g filter="url(#ombre)"><rect x="{x0}" y="{y0 - 22}" width="{w}" height="{H - y0 - 70}" rx="16" fill="#fff" stroke="{TRAIT}"/></g>']
    y = y0 + 16
    if titre_panneau:
        out.append(t(x0 + w - 22 if rtl else x0 + 22, y, titre_panneau, 15, 800, GRIS, "start", False, 'letter-spacing="1.5"' if not rtl else ""))
        y += 26
    for marque, titre, l1, l2, c2 in items:
        cx = x0 + w - 36 if rtl else x0 + 36
        if isinstance(marque, str) and marque.startswith("#"):
            out.append(f'<rect x="{cx - 15}" y="{y - 15}" width="30" height="30" rx="8" fill="{marque}" stroke="#fff" stroke-width="2" filter="url(#ombre2)"/>')
        else:
            out.append(pastille(cx, y, marque))
        tx = cx - 30 if rtl else cx + 30
        a = "end" if rtl else "start"
        out.append(f'<text x="{tx}" y="{y + 6}" font-size="18" font-weight="700" fill="{ENCRE}" text-anchor="{a}"{" direction=\"rtl\"" if rtl else ""}>{esc(titre)}</text>')
        if l1:
            out.append(f'<text x="{tx}" y="{y + 30}" font-size="15.5" fill="{GRIS}" text-anchor="{a}"{" direction=\"rtl\"" if rtl else ""}>{esc(l1)}</text>')
        if l2:
            out.append(f'<text x="{tx}" y="{y + 52}" font-size="15.5" font-weight="{700 if c2 else 400}" fill="{c2 or GRIS}" text-anchor="{a}"{" direction=\"rtl\"" if rtl else ""}>{esc(l2)}</text>')
        y += 90 if l2 else (64 if pas_serre else 72)
    return "".join(out)


def cadre(titre, sous_titre, note, rtl, corps):
    xt = W - 32 if rtl else 32
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" role="img" '
            f'aria-label="{esc(titre)}" font-family="{POLICE}">{DEFS}'
            f'<rect width="{W}" height="{H}" rx="18" fill="#f7f8fa"/>'
            f'<rect x="{W - 32 - 64 if rtl else 32}" y="26" width="64" height="6" rx="3" fill="{JAUNE}"/>'
            + t(xt, 66, titre, 27, 800, ENCRE, "start", rtl)
            + (t(xt, 92, sous_titre, 16, 400, GRIS, "start", rtl) if sous_titre else "")
            + corps
            + f'<line x1="32" y1="{H - 44}" x2="{W - 32}" y2="{H - 44}" stroke="{TRAIT}"/>'
            + t(xt, H - 18, note, 14, 400, GRIS, "start", rtl)
            + t(W - 32 if not rtl else 32, H - 18, "SIGMA ICC · sigma-icc.ma", 14, 700, ENCRE, "end", rtl)
            + "</svg>")


# ---------------------------------------------------------------------------------------------------
TXT = {
 "fr": {
  "sdb_titre": "Les volumes de sécurité d'une salle de bain",
  "sdb_sous": "Vue en coupe : ce que la norme admet dans chaque zone",
  "sdb_note": "Repères NF C 15-100 (édition 2002 amendée)",
  "leg": "LÉGENDE",
  "v0": "Volume 0", "v0a": "Intérieur de la baignoire", "v0b": "TBTS 12 V, IPX7 uniquement",
  "v1": "Volume 1", "v1a": "Au-dessus, jusqu'à 2,25 m", "v1b": "TBTS 12 V, IPX5 uniquement",
  "v2": "Volume 2", "v2a": "Bande de 60 cm autour du volume 1", "v2b": "Classe II, IPX4 minimum",
  "hv": "Hors volume", "hva": "Le reste de la pièce", "hvb": "Prises 16 A, interrupteurs, lave-linge",
  "ddr": "Tous les circuits : différentiel 30 mA",
  "cache": "Volume caché (sous la baignoire) : aucun appareil",
  "dch_titre": "Les volumes d'une douche à l'italienne",
  "dch_sous": "Sans receveur ni paroi fixe : les volumes se mesurent depuis la pomme de douche",
  "dch_note": "Repères NF C 15-100 · d'après l'infographie Legrand « Les points clés de la norme NF C 15-100 »",
  "coupe": "Vue en coupe", "plan": "Vue de dessus",
  "d0": "Volume 0", "d0a": "Couche de 10 cm au-dessus du sol,", "d0b": "sur 1,20 m autour de la douche · IPX7",
  "d1": "Volume 1", "d1a": "Rayon de 1,20 m, jusqu'à 2,25 m", "d1b": "TBTS 12 V, IPX5",
  "d2": "Volume 2", "d2a": "60 cm de plus autour du volume 1", "d2b": "Classe II, IPX4 minimum",
  "dhv": "Hors volume", "dhva": "Au-delà de 1,80 m de la douche", "dhvb": "Prises 16 A, interrupteurs",
  "drec": "Avec receveur : volume 0 = intérieur du receveur",
  "semelle_titre": "Semelle isolée, poteau et longrine",
  "semelle_sous": "Vue en coupe d'une fondation de villa et de ses aciers",
  "semelle_note": "Exemple : poteau de 300 kN sur un sol à 2 bars. Dimensions et ferraillage à déterminer par l'ingénieur.",
  "tn": "Terrain naturel",
  "s1": "Poteau (b = 25 cm)", "s1a": "et ses attentes ancrées dans la semelle",
  "s2": "Semelle : B = 1,25 m", "s2a": "Surface = charge ÷ contrainte du sol",
  "s3": "Hauteur utile ≥ (B − b) / 4", "s3a": "Ici au moins 25 cm, plus l'enrobage",
  "s4": "Nappe inférieure", "s4a": "Aciers dans les deux sens",
  "s5": "Béton de propreté", "s5a": "Quelques cm de béton maigre",
  "s6": "Longrine", "s6a": "Relie les semelles (exigée par le RPS)",
  "s7": "Enrobage renforcé", "s7a": "Béton coulé contre la terre",
  "s8": "Niveau d'assise", "s8a": "Donné par l'étude de sol",
 },
}


# ---------------------------------------------------------------------------------------------------
def salle_de_bain(x, rtl=False):
    ox = 432 if rtl else 40          # décalage du dessin (à droite du panneau en arabe)
    sol, m = 640, 160                 # niveau du sol, pixels par mètre
    h225 = sol - int(2.25 * m)        # 280
    plafond = 150
    mur, bain = ox + 50, ox + 50 + int(1.70 * m)          # baignoire 1,70 m
    v2 = bain + int(0.60 * m)                              # bande de 60 cm
    fin = ox + 740
    b = []
    # pièce : mur carrelé, plafond, sol carrelé
    b.append(f'<g filter="url(#ombre)"><rect x="{mur}" y="{plafond}" width="{fin - mur}" height="{sol - plafond}" fill="url(#carreaux)"/></g>')
    b.append(f'<rect x="{mur}" y="{plafond}" width="{fin - mur}" height="10" fill="#e3e7ec"/>')
    b.append(f'<rect x="{mur - 10}" y="{sol}" width="{fin - mur + 20}" height="22" fill="url(#sol)"/>')
    b.append(f'<rect x="{mur - 14}" y="{plafond}" width="14" height="{sol - plafond + 22}" fill="#c9ced6"/>')
    # zones (calques translucides)
    b.append(f'<rect x="{mur}" y="{h225}" width="{bain - mur}" height="{sol - 88 - h225}" fill="{BLEU}" fill-opacity=".22"/>')
    b.append(f'<rect x="{bain}" y="{h225}" width="{v2 - bain}" height="{sol - h225}" fill="{BLEU}" fill-opacity=".10"/>')
    b.append(f'<path d="M{mur} {h225} H{v2} V{sol}" fill="none" stroke="{BLEU_F}" stroke-width="2.2" stroke-dasharray="9 6"/>')
    b.append(f'<line x1="{bain}" y1="{h225}" x2="{bain}" y2="{sol - 88}" stroke="{BLEU_F}" stroke-width="1.6" stroke-dasharray="5 5"/>')
    # douche : barre, flexible et pomme
    b.append(f'<rect x="{mur + 26}" y="{h225 + 30}" width="6" height="150" rx="3" fill="#9aa3ad"/>')
    b.append(f'<path d="M{mur + 29} {h225 + 52} q 26 6 30 26" fill="none" stroke="#9aa3ad" stroke-width="5" stroke-linecap="round"/>')
    b.append(f'<ellipse cx="{mur + 62}" cy="{h225 + 84}" rx="16" ry="7" fill="#7d8792"/>')
    b.append(f'<path d="M{mur + 32} {h225 + 180} q 40 30 20 80" fill="none" stroke="#9aa3ad" stroke-width="4"/>')
    # baignoire (0,55 m) avec eau = volume 0
    ht = 88
    b.append(f'<g filter="url(#ombre)"><path d="M{mur} {sol - ht} H{bain} V{sol - 18} Q{bain} {sol} {bain - 20} {sol} H{mur + 20} Q{mur} {sol} {mur} {sol - 18} Z" fill="url(#emaille)" stroke="#aeb7c2" stroke-width="2"/></g>')
    b.append(f'<rect x="{mur - 4}" y="{sol - ht - 8}" width="{bain - mur + 8}" height="12" rx="6" fill="#ffffff" stroke="#aeb7c2" stroke-width="2"/>')
    b.append(f'<path d="M{mur + 14} {sol - ht + 18} q 30 -8 60 0 t 60 0 t 60 0 t 60 0 V{sol - 14} H{mur + 14} Z" fill="url(#eau)" opacity=".92"/>')
    b.append(f'<rect x="{bain - 40}" y="{sol - ht - 34}" width="10" height="28" rx="4" fill="#9aa3ad"/><rect x="{bain - 60}" y="{sol - ht - 38}" width="34" height="8" rx="4" fill="#9aa3ad"/>')
    # volume 2 : sèche-serviettes (classe II) et applique étanche
    rx0 = bain + 22
    for i in range(7):
        b.append(f'<rect x="{rx0}" y="{430 + i * 22}" width="52" height="8" rx="4" fill="#ffffff" stroke="#aeb7c2"/>')
    b.append(f'<rect x="{rx0 - 4}" y="422" width="6" height="160" rx="3" fill="#aeb7c2"/><rect x="{rx0 + 50}" y="422" width="6" height="160" rx="3" fill="#aeb7c2"/>')
    b.append(f'<rect x="{bain + 30}" y="{h225 + 26}" width="36" height="22" rx="11" fill="#fff8d6" stroke="#d9b64a" stroke-width="2"/>')
    # hors volume : lave-linge, prise, interrupteur, porte
    lx = v2 + 120
    b.append(f'<g filter="url(#ombre)"><rect x="{lx}" y="{sol - 120}" width="110" height="120" rx="10" fill="#ffffff" stroke="#aeb7c2" stroke-width="2"/></g>'
             f'<rect x="{lx}" y="{sol - 120}" width="110" height="22" rx="10" fill="#eef1f4"/>'
             f'<circle cx="{lx + 55}" cy="{sol - 52}" r="32" fill="#dfe6ee" stroke="#9aa3ad" stroke-width="4"/><circle cx="{lx + 55}" cy="{sol - 52}" r="18" fill="#b7c9dc"/>')
    px, py = v2 + 60, 470
    b.append(f'<g filter="url(#ombre2)"><rect x="{px}" y="{py}" width="40" height="40" rx="8" fill="#fff" stroke="{ENCRE}" stroke-width="2"/></g>'
             f'<circle cx="{px + 13}" cy="{py + 20}" r="3.5" fill="{ENCRE}"/><circle cx="{px + 27}" cy="{py + 20}" r="3.5" fill="{ENCRE}"/>')
    dx = fin - 92
    b.append(f'<rect x="{dx}" y="{plafond + 120}" width="82" height="{sol - plafond - 120}" fill="#e9e1d3" stroke="#bfb29c" stroke-width="2"/><circle cx="{dx + 14}" cy="{sol - 150}" r="5" fill="#8f7f63"/>')
    b.append(f'<g filter="url(#ombre2)"><rect x="{dx - 52}" y="{sol - 230}" width="32" height="44" rx="6" fill="#fff" stroke="{ENCRE}" stroke-width="2"/></g><rect x="{dx - 42}" y="{sol - 220}" width="12" height="24" rx="3" fill="{JAUNE}"/>')
    # cotes
    b.append(cote(mur - 30, h225, mur - 30, sol, "2,25 m", mur - 30, (h225 + sol) // 2, -90))
    b.append(cote(bain, h225 - 24, v2, h225 - 24, "0,60 m", (bain + v2) // 2, h225 - 24))
    # pastilles
    b.append(pastille((mur + bain) // 2, sol - 44, 0, BLEU_F, "#fff"))
    b.append(pastille((mur + bain) // 2 + 30, (h225 + sol - 88) // 2, 1, BLEU, "#fff"))
    b.append(pastille((bain + v2) // 2, h225 + 70, 2, "#7fb0e0", ENCRE))
    b.append(pastille(v2 + 150, h225 + 20, "HV", JAUNE, ENCRE))
    items = [(BLEU_F, x["v0"], x["v0a"], x["v0b"], None), (BLEU, x["v1"], x["v1a"], x["v1b"], ROUGE),
             ("#9cc3ea", x["v2"], x["v2a"], x["v2b"], None), (JAUNE, x["hv"], x["hva"], x["hvb"], None)]
    leg = panneau(items, rtl, 140, x["leg"])
    # bandeau différentiel
    bx = 24 if rtl else PANNEAU_X
    leg += (f'<rect x="{bx + 18}" y="{H - 176}" width="{W - PANNEAU_X - 60}" height="40" rx="10" fill="#eef1f4" stroke="{TRAIT}"/>'
            + t(bx + (W - PANNEAU_X - 24) // 2, H - 150, x["cache"], 14.5, 600, ENCRE, "middle")
            + f'<rect x="{bx + 18}" y="{H - 128}" width="{W - PANNEAU_X - 60}" height="40" rx="10" fill="#fff6d6" stroke="{JAUNE}"/>'
            + t(bx + (W - PANNEAU_X - 24) // 2, H - 102, x["ddr"], 15.5, 700, ENCRE, "middle"))
    return cadre(x["sdb_titre"], x["sdb_sous"], x["sdb_note"], rtl, "".join(b) + leg)


def semelle(x, rtl=False):
    ox = 432 if rtl else 40
    tn = 230                                   # terrain naturel
    m = 320                                    # pixels par mètre
    s_g = ox + 90                              # semelle B = 1,25 m
    s_d = s_g + int(1.25 * m)
    s_h, s_b = 470, 470 + int(0.35 * m)        # 0,35 m d'épaisseur (illustratif)
    prop = s_b + 18
    pc = (s_g + s_d) // 2
    p_g, p_d = pc - int(0.125 * m), pc + int(0.125 * m)   # poteau 25 cm
    fin = ox + 750
    b = []
    # terre, fouille, terrain naturel
    b.append(f'<rect x="{ox}" y="{tn}" width="{fin - ox}" height="{prop + 60 - tn}" fill="url(#terre)"/>')
    b.append(f'<rect x="{ox}" y="120" width="{fin - ox}" height="{tn - 120}" fill="url(#ciel)"/>')
    b.append(f'<path d="M{s_g - 40} {tn} L{s_g - 40} {prop} L{s_d + 40} {prop} L{s_d + 40} {tn} Z" fill="#f2e6d0"/>')
    b.append(f'<path d="M{ox} {tn} H{fin}" stroke="#7a5c2e" stroke-width="3"/>')
    for i in range(0, fin - ox, 34):
        b.append(f'<path d="M{ox + i} {tn} l8 -9 l6 9" fill="#7fa65a"/>')
    b.append(t(ox + 8 if not rtl else fin - 8, tn - 16, x["tn"], 15, 700, "#6d5226", "start", rtl))
    # béton de propreté
    b.append(f'<rect x="{s_g - 16}" y="{s_b}" width="{s_d - s_g + 32}" height="{prop - s_b}" fill="url(#maigre)"/>')
    # semelle, poteau, longrine
    b.append(f'<g filter="url(#ombre)"><rect x="{s_g}" y="{s_h}" width="{s_d - s_g}" height="{s_b - s_h}" fill="url(#beton)" stroke="#8f959e" stroke-width="2"/></g>')
    b.append(f'<g filter="url(#ombre)"><rect x="{p_g}" y="140" width="{p_d - p_g}" height="{s_h - 140}" fill="url(#beton)" stroke="#8f959e" stroke-width="2"/></g>')
    lo_h, lo_b = 380, 462
    b.append(f'<g filter="url(#ombre)"><path d="M{p_d} {lo_h} H{fin - 20} l10 12 l-14 14 l14 14 l-14 14 l14 14 l-10 14 H{p_d} Z" fill="url(#beton)" stroke="#8f959e" stroke-width="2"/></g>')
    # aciers : nappe inférieure, attentes du poteau, longrine
    ac = 'stroke="#b8352a" stroke-width="7" stroke-linecap="round" fill="none"'
    b.append(f'<path d="M{s_g + 18} {s_h + 40} V{s_b - 20} H{s_d - 18} V{s_h + 40}" {ac}/>')
    for xx in range(s_g + 38, s_d - 20, 30):
        b.append(f'<circle cx="{xx}" cy="{s_b - 30}" r="6" fill="url(#acier)"/>')
    for xx, sens in ((p_g + 16, -1), (p_d - 16, 1)):
        b.append(f'<path d="M{xx} 150 V{s_b - 28} h{sens * 46}" {ac}/>')
    for yy in range(170, s_h, 34):
        b.append(f'<rect x="{p_g + 10}" y="{yy}" width="{p_d - p_g - 20}" height="4" rx="2" fill="#a83226"/>')
    b.append(f'<path d="M{p_g + 30} {lo_h + 14} H{fin - 30}" {ac}/><path d="M{p_g + 30} {lo_b - 14} H{fin - 30}" {ac}/>')
    b.append(f'<path d="M{p_g + 30} {lo_h + 12} H{fin - 30}" stroke="#ec7c70" stroke-width="2" fill="none"/><path d="M{p_g + 30} {lo_b - 16} H{fin - 30}" stroke="#ec7c70" stroke-width="2" fill="none"/>')
    for xx in range(p_d + 20, fin - 40, 32):
        b.append(f'<rect x="{xx}" y="{lo_h + 8}" width="8" height="{lo_b - lo_h - 16}" rx="3" fill="none" stroke="#a83226" stroke-width="3"/>')
    # cotes
    b.append(cote(s_g, prop + 34, s_d, prop + 34, "1,25 m", pc, prop + 34))
    b.append(cote(p_g, 160, p_d, 160, "25 cm", pc, 128))
    b.append(cote(s_g - 34, s_h, s_g - 34, s_b - 22, "h", s_g - 34, (s_h + s_b) // 2 - 10))
    b.append(f'<path d="M{s_d + 60} {prop} H{fin}" stroke="{ENCRE}" stroke-width="1.6" stroke-dasharray="8 6"/>')
    # pastilles
    b.append(pastille(p_d + 22, 220, 1))
    b.append(pastille(s_d - 40, s_h + 26, 2))
    b.append(pastille(s_g - 34, s_h - 30, 3))
    b.append(pastille(s_g + 60, s_b - 54, 4))
    b.append(pastille(s_d + 6, s_b + 12, 5))
    b.append(pastille(fin - 90, lo_h - 24, 6))
    b.append(pastille(s_g + 18, s_b + 2, 7))
    b.append(pastille(fin - 40, prop - 24, 8))
    items = [(1, x["s1"], x["s1a"], None, None), (2, x["s2"], x["s2a"], None, None), (3, x["s3"], x["s3a"], None, None),
             (4, x["s4"], x["s4a"], None, None), (5, x["s5"], x["s5a"], None, None), (6, x["s6"], x["s6a"], None, None),
             (7, x["s7"], x["s7a"], None, None), (8, x["s8"], x["s8a"], None, None)]
    return cadre(x["semelle_titre"], x["semelle_sous"], x["semelle_note"], rtl, "".join(b) + panneau(items, rtl, 128, None, True))


def douche(x, rtl=False):
    ox = 432 if rtl else 40
    sol, m = 650, 160
    h225 = sol - int(2.25 * m)
    mur = ox + 40
    r1, r2 = mur + int(1.20 * m), mur + int(1.80 * m)        # 1,20 m et 1,80 m depuis la douche
    fin = ox + 430
    b = []
    b.append(t(mur, 150, x["coupe"], 16, 800, GRIS, "start", False, 'letter-spacing="1"'))
    b.append(f'<g filter="url(#ombre)"><rect x="{mur}" y="170" width="{fin - mur}" height="{sol - 170}" fill="url(#carreaux)"/></g>')
    b.append(f'<rect x="{mur - 10}" y="{sol}" width="{fin - mur + 20}" height="20" fill="url(#sol)"/>')
    b.append(f'<rect x="{mur - 12}" y="170" width="12" height="{sol - 150}" fill="#c9ced6"/>')
    # zones
    b.append(f'<rect x="{mur}" y="{h225}" width="{r1 - mur}" height="{sol - h225}" fill="{BLEU}" fill-opacity=".20"/>')
    b.append(f'<rect x="{r1}" y="{h225}" width="{r2 - r1}" height="{sol - h225}" fill="{BLEU}" fill-opacity=".09"/>')
    b.append(f'<rect x="{mur}" y="{sol - 16}" width="{r1 - mur}" height="16" fill="{BLEU_F}" fill-opacity=".85"/>')
    b.append(f'<path d="M{mur} {h225} H{r2} V{sol}" fill="none" stroke="{BLEU_F}" stroke-width="2.2" stroke-dasharray="9 6"/>')
    b.append(f'<line x1="{r1}" y1="{h225}" x2="{r1}" y2="{sol}" stroke="{BLEU_F}" stroke-width="1.6" stroke-dasharray="5 5"/>')
    # pomme de douche fixe au plafond / mur, jet d'eau, caniveau
    b.append(f'<path d="M{mur} {h225 + 26} H{mur + 46} V{h225 + 40}" stroke="#7d8792" stroke-width="6" fill="none"/>')
    b.append(f'<ellipse cx="{mur + 46}" cy="{h225 + 44}" rx="20" ry="6" fill="#6b7580"/>')
    for i in range(-3, 4):
        b.append(f'<line x1="{mur + 46 + i * 5}" y1="{h225 + 52}" x2="{mur + 46 + i * 12}" y2="{sol - 24}" stroke="#7fb3e6" stroke-width="1.6" stroke-dasharray="2 7" opacity=".9"/>')
    b.append(f'<rect x="{mur + 120}" y="{sol - 3}" width="60" height="6" rx="3" fill="#7d8792"/>')
    b.append(f'<g filter="url(#ombre2)"><rect x="{r2 + 20}" y="470" width="36" height="36" rx="7" fill="#fff" stroke="{ENCRE}" stroke-width="2"/></g>'
             f'<circle cx="{r2 + 32}" cy="488" r="3.2" fill="{ENCRE}"/><circle cx="{r2 + 44}" cy="488" r="3.2" fill="{ENCRE}"/>')
    # cotes
    b.append(cote(mur - 26, h225, mur - 26, sol, "2,25 m", mur - 26, (h225 + sol) // 2 - 30, -90))
    b.append(cote(mur, h225 - 22, r1, h225 - 22, "1,20 m", (mur + r1) // 2, h225 - 22))
    b.append(cote(r1, h225 - 22, r2, h225 - 22, "0,60 m", (r1 + r2) // 2, h225 - 52))
    b.append(f'<line x1="{r1 + 8}" y1="{sol - 16}" x2="{r1 + 8}" y2="{sol}" stroke="{ENCRE}" stroke-width="1.6"/>'
             f'<path d="M{r1 + 8} {sol - 8} H{r1 + 30}" stroke="{ENCRE}" stroke-width="1.2"/>'
             f'<rect x="{r1 + 30}" y="{sol - 40}" width="66" height="24" rx="12" fill="#fff" stroke="{ENCRE}" stroke-width="1.2"/>'
             f'<text x="{r1 + 63}" y="{sol - 23}" font-size="15" font-weight="700" fill="{ENCRE}" text-anchor="middle">0,10 m</text>')
    b.append(pastille(mur + 70, sol - 40, 0, BLEU_F, "#fff"))
    b.append(pastille(mur + 120, h225 + 150, 1, BLEU, "#fff"))
    b.append(pastille((r1 + r2) // 2, h225 + 150, 2, "#7fb0e0", ENCRE))
    b.append(pastille(r2 + 38, 440, "HV", JAUNE, ENCRE))
    # vue de dessus
    px, py, mp = ox + 480, 420, 120
    b.append(t(px, 150, x["plan"], 16, 800, GRIS, "start", False, 'letter-spacing="1"'))
    b.append(f'<g filter="url(#ombre)"><rect x="{px}" y="170" width="280" height="500" rx="4" fill="url(#carreaux)"/></g>')
    b.append(f'<path d="M{px} {py - int(1.8 * mp)} A{int(1.8 * mp)} {int(1.8 * mp)} 0 0 1 {px} {py + int(1.8 * mp)} Z" fill="{BLEU}" fill-opacity=".10" stroke="{BLEU_F}" stroke-width="2" stroke-dasharray="8 6"/>')
    b.append(f'<path d="M{px} {py - int(1.2 * mp)} A{int(1.2 * mp)} {int(1.2 * mp)} 0 0 1 {px} {py + int(1.2 * mp)} Z" fill="{BLEU}" fill-opacity=".26" stroke="{BLEU_F}" stroke-width="2"/>')
    b.append(f'<rect x="{px - 10}" y="170" width="10" height="500" fill="#9aa3ad"/>')
    b.append(f'<circle cx="{px + 6}" cy="{py}" r="9" fill="#6b7580" stroke="#fff" stroke-width="3"/>')
    b.append(f'<line x1="{px + 6}" y1="{py}" x2="{px + int(1.2 * mp * 0.71)}" y2="{py + int(1.2 * mp * 0.71)}" stroke="{ENCRE}" stroke-width="1.6" marker-end="url(#fl)"/>')
    b.append(t(px + 40, py + 54, "1,20 m", 15, 800, ENCRE))
    b.append(f'<line x1="{px + int(1.2 * mp * 0.71)}" y1="{py - int(1.2 * mp * 0.71)}" x2="{px + int(1.8 * mp * 0.71)}" y2="{py - int(1.8 * mp * 0.71)}" stroke="{ENCRE}" stroke-width="1.6" marker-start="url(#fl)" marker-end="url(#fl)"/>')
    b.append(t(px + 150, py - 130, "0,60 m", 15, 800, ENCRE))
    items = [(BLEU_F, x["d0"], x["d0a"], x["d0b"], None), (BLEU, x["d1"], x["d1a"], x["d1b"], None),
             ("#9cc3ea", x["d2"], x["d2a"], x["d2b"], None), (JAUNE, x["dhv"], x["dhva"], x["dhvb"], None)]
    leg = panneau(items, rtl, 140, x["leg"])
    bx = 24 if rtl else PANNEAU_X
    leg += (f'<rect x="{bx + 18}" y="{H - 176}" width="{W - PANNEAU_X - 60}" height="40" rx="10" fill="#eef1f4" stroke="{TRAIT}"/>'
            + t(bx + (W - PANNEAU_X - 24) // 2, H - 150, x["drec"], 13.5, 600, ENCRE, "middle")
            + f'<rect x="{bx + 18}" y="{H - 128}" width="{W - PANNEAU_X - 60}" height="40" rx="10" fill="#fff6d6" stroke="{JAUNE}"/>'
            + t(bx + (W - PANNEAU_X - 24) // 2, H - 102, x["ddr"], 15.5, 700, ENCRE, "middle"))
    return cadre(x["dch_titre"], x["dch_sous"], x["dch_note"], rtl, "".join(b) + leg)


SCHEMAS = {"volumes-salle-de-bain": salle_de_bain, "volumes-douche": douche, "semelle-longrine": semelle}


def main():
    for lang, x in TXT.items():
        d = os.path.join(ROOT, "images", "schemas", lang)
        os.makedirs(d, exist_ok=True)
        for nom, f in SCHEMAS.items():
            open(os.path.join(d, nom + ".svg"), "w", encoding="utf-8").write(f(x, rtl=(lang == "ar")))
    print("schémas :", ", ".join(SCHEMAS))


if __name__ == "__main__":
    main()
