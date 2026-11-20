"""Schémas explicatifs des articles « Conseils » (SVG dessinés en code, légendes en FR / EN / AR).

Chaque schéma est une fonction qui reçoit les textes de la langue et renvoie le SVG. Les valeurs dessinées sont
celles de l'article (aucune cote inventée). Sortie : images/schemas/<langue>/<nom>.svg
Usage : python3 tools/schemas.py
"""
import html, os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
JAUNE, ENCRE, GRIS, TRAIT, FOND = "#f5b400", "#1f2328", "#5b6470", "#c9ced6", "#ffffff"
POLICE = "'Source Sans 3','Segoe UI',Arial,sans-serif"


def t(x, y, s, taille=15, poids=400, couleur=ENCRE, ancre="start", rtl=False, extra=""):
    """Texte SVG (en arabe, l'ancrage est inversé pour garder la même mise en page)."""
    if rtl and ancre in ("start", "end"):
        ancre = "end" if ancre == "start" else "start"
    d = ' direction="rtl"' if rtl else ""
    return (f'<text x="{x}" y="{y}" font-size="{taille}" font-weight="{poids}" fill="{couleur}" '
            f'text-anchor="{ancre}"{d} {extra}>{html.escape(s)}</text>')


def cadre(w, h, titre, note, rtl, corps):
    xt = w - 24 if rtl else 24
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}" role="img" '
            f'aria-label="{html.escape(titre)}" font-family="{POLICE}">'
            f'<rect width="{w}" height="{h}" rx="14" fill="{FOND}"/>'
            + t(xt, 38, titre, 21, 700, ENCRE, "start", rtl)
            + corps
            + t(xt, h - 16, note, 13, 400, GRIS, "start", rtl)
            + "</svg>")


# ---------------------------------------------------------------------------------------------------
TXT = {
 "fr": {
  "sdb_titre": "Les volumes de sécurité d'une salle de bain (vue en coupe)",
  "sdb_note": "Repères NF C 15-100 (édition 2002 amendée). Tous les circuits de la salle de bain : différentiel 30 mA.",
  "v0": "Volume 0", "v0a": "Intérieur de la baignoire", "v0b": "TBTS 12 V, IPX7",
  "v1": "Volume 1", "v1a": "TBTS 12 V, IPX4 (IPX5 si jets)", "v1b": "Interrupteurs interdits",
  "v2": "Volume 2", "v2a": "Classe II", "v2b": "IPX4 min.",
  "hv": "Hors volume", "hva": "Prises 16 A, interrupteurs,", "hvb": "lave-linge, appareils de classe I",
  "prise": "Prise 16 A", "inter": "Interrupteur",
  "semelle_titre": "Semelle isolée, poteau et longrine (vue en coupe)",
  "semelle_note": "Exemple de l'article : poteau de 300 kN sur un sol à 2 bars. Dimensions et ferraillage à déterminer par l'ingénieur.",
  "tn": "Terrain naturel", "poteau": "Poteau b = 25 cm", "amorces": "Attentes du poteau",
  "largeur": "B = 1,25 m (surface = charge ÷ contrainte du sol)", "hauteur": "Hauteur utile ≥ (B − b) / 4",
  "nappe": "Nappe inférieure (2 sens)", "proprete": "Béton de propreté",
  "longrine": "Longrine : relie les semelles (RPS 2000 version 2011)", "enrobage": "Enrobage renforcé (béton coulé contre terre)",
  "assise": "Niveau d'assise donné par l'étude de sol",
 },
}


def salle_de_bain(x, rtl=False):
    w, h = 900, 560
    sol, h225 = 480, 143            # 150 px par mètre : 2,25 m au-dessus du sol
    mur, bain_fin, v2_fin = 60, 315, 405
    b = []
    # pièce : mur, sol, plafond
    b.append(f'<rect x="{mur}" y="60" width="{w - 60 - mur}" height="{sol - 60}" fill="#f7f8fa" stroke="{TRAIT}"/>')
    # zones
    b.append(f'<rect x="{mur}" y="{h225}" width="{bain_fin - mur}" height="{398 - h225}" fill="#cfe3f7"/>')      # volume 1
    b.append(f'<rect x="{bain_fin}" y="{h225}" width="{v2_fin - bain_fin}" height="{sol - h225}" fill="#e6f0fb"/>')  # volume 2
    b.append(f'<rect x="{v2_fin}" y="60" width="{w - 60 - v2_fin}" height="{sol - 60}" fill="#fbf7ea"/>')         # hors volume
    # baignoire et volume 0
    b.append(f'<path d="M{mur} 398 H{bain_fin} V470 Q{bain_fin} {sol} {bain_fin - 12} {sol} H{mur} Z" fill="#ffffff" stroke="{ENCRE}" stroke-width="2"/>')
    b.append(f'<rect x="{mur + 10}" y="404" width="{bain_fin - mur - 22}" height="62" rx="10" fill="#2f6fb3"/>')
    # douche murale
    b.append(f'<path d="M{mur} 190 H{mur + 38} V205" stroke="{GRIS}" stroke-width="5" fill="none"/><circle cx="{mur + 38}" cy="212" r="9" fill="{GRIS}"/>')
    # sol et limites
    b.append(f'<line x1="40" y1="{sol}" x2="{w - 40}" y2="{sol}" stroke="{ENCRE}" stroke-width="3"/>')
    b.append(f'<line x1="{mur}" y1="{h225}" x2="{v2_fin}" y2="{h225}" stroke="#2f6fb3" stroke-width="1.5" stroke-dasharray="6 4"/>')
    b.append(f'<line x1="{v2_fin}" y1="{h225}" x2="{v2_fin}" y2="{sol}" stroke="#2f6fb3" stroke-width="1.5" stroke-dasharray="6 4"/>')
    # cotes
    b.append(f'<line x1="38" y1="{h225}" x2="38" y2="{sol}" stroke="{ENCRE}" stroke-width="1.5" marker-start="url(#f)" marker-end="url(#f)"/>')
    b.append(t(30, 320, "2,25 m", 15, 700, ENCRE, "middle", False, 'transform="rotate(-90 30 320)"'))
    b.append(f'<line x1="{bain_fin}" y1="126" x2="{v2_fin}" y2="126" stroke="{ENCRE}" stroke-width="1.5" marker-start="url(#f)" marker-end="url(#f)"/>')
    b.append(t((bain_fin + v2_fin) // 2, 118, "0,60 m", 15, 700, ENCRE, "middle"))
    # textes des zones
    b.append(t(188, 446, x["v0"], 16, 700, "#ffffff", "middle") + t(188, 462, x["v0b"], 13, 400, "#ffffff", "middle"))
    b.append(t(188, 260, x["v1"], 18, 700, ENCRE, "middle") + t(188, 282, x["v1a"], 13, 400, ENCRE, "middle")
             + t(188, 300, x["v1b"], 13, 700, "#b3261e", "middle"))
    b.append(t(360, 250, x["v2"], 15, 700, ENCRE, "middle") + t(360, 272, x["v2a"], 13, 400, ENCRE, "middle")
             + t(360, 290, x["v2b"], 13, 400, ENCRE, "middle"))
    b.append(t(620, 120, x["hv"], 18, 700, ENCRE, "middle") + t(620, 142, x["hva"], 13, 400, ENCRE, "middle")
             + t(620, 160, x["hvb"], 13, 400, ENCRE, "middle"))
    # prise et interrupteur hors volume
    b.append(f'<rect x="560" y="360" width="34" height="34" rx="6" fill="#fff" stroke="{ENCRE}" stroke-width="2"/>'
             f'<circle cx="571" cy="377" r="3" fill="{ENCRE}"/><circle cx="583" cy="377" r="3" fill="{ENCRE}"/>')
    b.append(t(604, 382, x["prise"], 13, 600, ENCRE))
    b.append(f'<rect x="700" y="290" width="30" height="40" rx="5" fill="#fff" stroke="{ENCRE}" stroke-width="2"/>'
             f'<rect x="709" y="300" width="12" height="20" rx="2" fill="{JAUNE}"/>')
    b.append(t(740, 315, x["inter"], 13, 600, ENCRE))
    defs = f'<defs><marker id="f" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0 0 L10 5 L0 10 z" fill="{ENCRE}"/></marker></defs>'
    corps = defs + "".join(b)
    if rtl:  # en arabe, on garde le dessin et on ne retourne que les textes (ancrage)
        pass
    return cadre(w, h, x["sdb_titre"], x["sdb_note"], rtl, corps)


def semelle(x, rtl=False):
    w, h = 900, 600
    tn = 150                                   # terrain naturel
    s_haut, s_bas, prop = 400, 470, 486        # semelle et béton de propreté
    b = []
    # terre et fouille
    b.append(f'<rect x="0" y="{tn}" width="{w}" height="{h - tn - 40}" fill="#efe3cf"/>')
    b.append(f'<path d="M60 {tn} L60 {prop} L350 {prop} L350 {tn} Z M600 {tn} L600 {prop} L890 {prop} L890 {tn} Z" fill="#f6efe2"/>')
    b.append(f'<line x1="0" y1="{tn}" x2="{w}" y2="{tn}" stroke="#8a6d3b" stroke-width="2.5"/>')
    b.append(t(20 if not rtl else w - 20, tn - 10, x["tn"], 14, 600, "#8a6d3b", "start", rtl))
    for x0, x1 in ((80, 330), (620, 870)):
        # béton de propreté
        b.append(f'<rect x="{x0 - 8}" y="{s_bas}" width="{x1 - x0 + 16}" height="{prop - s_bas}" fill="#c8cbd0"/>')
        # semelle
        b.append(f'<rect x="{x0}" y="{s_haut}" width="{x1 - x0}" height="{s_bas - s_haut}" fill="#d9dce1" stroke="{ENCRE}" stroke-width="2"/>')
        # nappe inférieure : barres longitudinales (ligne) et transversales (points)
        b.append(f'<path d="M{x0 + 10} {s_haut + 30} V{s_bas - 12} H{x1 - 10} V{s_haut + 30}" fill="none" stroke="#b3261e" stroke-width="3"/>')
        for xx in range(x0 + 22, x1 - 10, 22):
            b.append(f'<circle cx="{xx}" cy="{s_bas - 17}" r="3.5" fill="#b3261e"/>')
        # poteau et attentes
        pc = (x0 + x1) // 2
        b.append(f'<rect x="{pc - 25}" y="70" width="50" height="{s_haut - 70}" fill="#d9dce1" stroke="{ENCRE}" stroke-width="2"/>')
        for xx in (pc - 15, pc + 15):
            b.append(f'<path d="M{xx} 80 V{s_bas - 14} H{xx + (-22 if xx < pc else 22)}" fill="none" stroke="#b3261e" stroke-width="3"/>')
    # longrine entre les deux poteaux
    b.append(f'<rect x="230" y="320" width="415" height="70" fill="#d9dce1" stroke="{ENCRE}" stroke-width="2"/>')
    b.append(f'<line x1="215" y1="332" x2="660" y2="332" stroke="#b3261e" stroke-width="3"/><line x1="215" y1="378" x2="660" y2="378" stroke="#b3261e" stroke-width="3"/>')
    for xx in range(250, 640, 28):
        b.append(f'<rect x="{xx}" y="327" width="6" height="56" fill="none" stroke="#b3261e" stroke-width="1.6"/>')
    # cotes : largeur B et hauteur
    b.append(f'<line x1="80" y1="505" x2="330" y2="505" stroke="{ENCRE}" stroke-width="1.5" marker-start="url(#f)" marker-end="url(#f)"/>')
    b.append(t(80, 527, x["largeur"], 14, 700, ENCRE, "start"))
    b.append(f'<line x1="345" y1="{s_haut}" x2="345" y2="{s_bas}" stroke="{ENCRE}" stroke-width="1.5" marker-start="url(#f)" marker-end="url(#f)"/>')
    # étiquettes avec traits de rappel
    def etiquette(px, py, lx, ly, texte, ancre="start"):
        return (f'<line x1="{px}" y1="{py}" x2="{lx}" y2="{ly}" stroke="{GRIS}" stroke-width="1.2"/><circle cx="{px}" cy="{py}" r="3" fill="{GRIS}"/>'
                + t(lx + (6 if ancre == "start" else -6), ly + 5, texte, 14, 600, ENCRE, ancre))
    b.append(etiquette(230, 120, 290, 100, x["poteau"]))
    b.append(etiquette(190, 250, 300, 230, x["amorces"]))
    b.append(etiquette(352, 435, 392, 425, x["hauteur"]))
    b.append(etiquette(300, 453, 392, 458, x["nappe"]))
    b.append(etiquette(330, 480, 400, 560, x["proprete"]))
    b.append(etiquette(440, 355, 470, 290, x["longrine"]))
    b.append(etiquette(864, 452, 874, 522, x["enrobage"], "end"))
    b.append(etiquette(890, prop, 890, 572, x["assise"], "end"))
    defs = f'<defs><marker id="f" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0 0 L10 5 L0 10 z" fill="{ENCRE}"/></marker></defs>'
    return cadre(w, h + 30, x["semelle_titre"], x["semelle_note"], rtl, defs + "".join(b))


SCHEMAS = {"volumes-salle-de-bain": salle_de_bain, "semelle-longrine": semelle}


def main():
    for lang, x in TXT.items():
        d = os.path.join(ROOT, "images", "schemas", lang)
        os.makedirs(d, exist_ok=True)
        for nom, f in SCHEMAS.items():
            open(os.path.join(d, nom + ".svg"), "w", encoding="utf-8").write(f(x, rtl=(lang == "ar")))
    print("schémas :", ", ".join(SCHEMAS))


if __name__ == "__main__":
    main()
