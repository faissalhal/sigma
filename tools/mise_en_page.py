"""Mise en page des pages Service et FAQ (FR, EN, AR) : plus de colonnes vides sur ordinateur.

- Pages service : le menu « Solutions » et une carte contact forment une colonne latérale collante,
  le contenu occupe toute la largeur restante, les galeries reçoivent les nouvelles photos.
- FAQ : questions à gauche, colonne latérale à droite (contact, services, conseils).
Le script est idempotent : on peut le relancer après chaque modification. Usage : python3 tools/mise_en_page.py
"""
import html, os, re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

TXT = {
    "": {"h": "Besoin d'une étude ?", "p": "Devis gratuit sous 48 h, études et suivi de chantier à Marrakech et partout au Maroc.",
         "b1": "Demander un devis", "b2": "Écrire sur WhatsApp", "serv": "Nos services", "cons": "Conseils et guides",
         "cons_p": "Normes, prix et bonnes pratiques expliqués simplement.", "cons_l": "Lire les conseils →",
         "faq_h": "Une question sur votre projet ?", "faq_p": "Un ingénieur vous répond, 7 jours sur 7 pour les urgences."},
    "en": {"h": "Need an engineering study?", "p": "Free quote within 48 hours, studies and site supervision in Marrakech and across Morocco.",
           "b1": "Request a quote", "b2": "Message us on WhatsApp", "serv": "Our services", "cons": "Advice and guides",
           "cons_p": "Standards, prices and best practice, explained simply.", "cons_l": "Read the advice →",
           "faq_h": "A question about your project?", "faq_p": "An engineer answers you, 7 days a week for emergencies."},
    "ar": {"h": "هل تحتاج إلى دراسة تقنية؟", "p": "عرض سعر مجاني خلال 48 ساعة، دراسات وتتبع الأوراش في مراكش وفي جميع أنحاء المغرب.",
           "b1": "اطلب عرض سعر", "b2": "راسلنا على واتساب", "serv": "خدماتنا", "cons": "نصائح وأدلة",
           "cons_p": "المعايير والأسعار والممارسات الجيدة بشرح مبسط.", "cons_l": "اقرأ النصائح ←",
           "faq_h": "سؤال حول مشروعك؟", "faq_p": "يجيبك مهندس، طيلة أيام الأسبوع للحالات المستعجلة."},
}

# nouvelles galeries : (fichier, largeur, hauteur, {langue: texte alternatif})
GAL = {
 "STRUCTURE": [("maison-beton.jpg", 1400, 933, {"": "Chantier de bâtiment en béton armé : poteaux, voiles et coffrages", "en": "Reinforced concrete building site: columns, walls and formwork", "ar": "ورش بناء بالخرسانة المسلحة: أعمدة وجدران وقوالب"}),
               ("beton-poutre.jpg", 1400, 1050, {"": "Ferraillage d'une poutre en béton armé ligaturé sur chantier", "en": "Rebar cage of a reinforced concrete beam on site", "ar": "تسليح عارضة من الخرسانة المسلحة في الورش"}),
               ("1.jpg", 750, 600, {"": "Montage d'éléments en béton à la grue", "en": "Concrete elements lifted by crane", "ar": "تركيب عناصر خرسانية بالرافعة"}),
               ("3.jpg", 750, 600, {"": "Villa contemporaine en béton livrée", "en": "Completed contemporary concrete villa", "ar": "فيلا عصرية منجزة بالخرسانة"})],
 "CFA": [("elec-tableau.jpg", 1400, 933, {"": "Électricien raccordant un tableau électrique", "en": "Electrician wiring a distribution board", "ar": "كهربائي يوصل لوحة التوزيع الكهربائي"}),
         ("elec-disjoncteurs.jpg", 1400, 933, {"": "Tableau électrique avec disjoncteurs et interrupteurs différentiels", "en": "Distribution board with circuit breakers and RCDs", "ar": "لوحة كهربائية بقواطع وقواطع تفاضلية"}),
         ("elec-prises.jpg", 1400, 933, {"": "Pose de prises et de boîtes d'encastrement", "en": "Installing sockets and flush boxes", "ar": "تركيب المآخذ وعلب التثبيت"}),
         ("ele1.jpg", 750, 600, {"": "Éclairage extérieur d'une villa avec piscine", "en": "Outdoor lighting of a villa with a pool", "ar": "إنارة خارجية لفيلا بمسبح"})],
 "FD": [("clim-exterieur.jpg", 1400, 933, {"": "Techniciens contrôlant les pressions d'une unité de climatisation", "en": "Technicians checking the pressures of an air-conditioning unit", "ar": "تقنيون يقيسون ضغط وحدة التكييف"}),
        ("ventilation.jpg", 1400, 913, {"": "Gaines de ventilation et de désenfumage en acier galvanisé", "en": "Galvanised steel ventilation and smoke-extraction ducts", "ar": "قنوات التهوية وسحب الدخان من الفولاذ المجلفن"}),
        ("plombier.jpg", 1400, 933, {"": "Plombier installant des réseaux d'eau", "en": "Plumber installing water pipes", "ar": "سباك يركب شبكات الماء"}),
        ("cvc1.jpg", 750, 600, {"": "Réseaux de plomberie eau froide et eau chaude", "en": "Cold and hot water pipework", "ar": "شبكات الماء البارد والساخن"})],
 "CSSI": [("incendie-alarme.jpg", 1400, 933, {"": "Déclencheur manuel d'alarme incendie", "en": "Manual fire alarm call point", "ar": "زر إنذار الحريق اليدوي"}),
          ("cssi2.jpg", 750, 600, {"": "Détecteur de fumée", "en": "Smoke detector", "ar": "كاشف الدخان"}),
          ("cssi1.jpg", 750, 600, {"": "Local technique équipé d'un système de sécurité incendie", "en": "Technical room fitted with a fire safety system", "ar": "غرفة تقنية مجهزة بنظام السلامة من الحريق"})],
}


def contact_card(t, h=None, p=None, court=False):
    para = "" if court else f'<p>{html.escape(p or t["p"])}</p>'
    return (f'<div class="cote-carte cote-contact"><h3>{html.escape(h or t["h"])}</h3>{para}'
            f'<a class="btn" href="contact.html#formulaire">{t["b1"]}</a>'
            f'<a class="btn secondaire" href="https://wa.me/212620897660" rel="noopener">{t["b2"]}</a>'
            f'<a class="cote-tel" href="tel:+212661057455" dir="ltr">+212 6 61 05 74 55</a></div>')


def service_pages(lang):
    t, d = TXT[lang], os.path.join(ROOT, lang)
    pre = "../" if lang else ""
    for f in sorted(os.listdir(d)):
        if not (f.startswith("service-") and f.endswith(".html")):
            continue
        p = os.path.join(d, f)
        h = open(p, encoding="utf-8").read()
        # colonne latérale : retirer l'ancienne enveloppe, puis envelopper le menu
        h = re.sub(r'<aside class="service-cote">(?:<div class="service-cote-colle">)?(<nav class="sommaire".*?</nav>).*?</aside>', r"\1", h, flags=re.S)
        h, n = re.subn(r'(<nav class="sommaire" aria-label="[^"]*">.*?</nav>)',
                       lambda m: f'<aside class="service-cote"><div class="service-cote-colle">{m.group(1)}{contact_card(t, court=True)}</div></aside>', h, count=1, flags=re.S)
        assert n == 1, p
        key = f[len("service-"):-len(".html")]
        if key in GAL:
            tags = "".join(f'<img src="{pre}images/services/{im}" alt="{html.escape(alt[lang])}" loading="{"eager" if i == 0 else "lazy"}" width="{w}" height="{hh}">'
                           for i, (im, w, hh, alt) in enumerate(GAL[key]))
            h, n = re.subn(r'<div class="visuels galerie">.*?</div>', f'<div class="visuels galerie">{tags}</div>', h, count=1, flags=re.S)
            assert n == 1, p
        open(p, "w", encoding="utf-8").write(h)


def faq_page(lang):
    t = TXT[lang]
    p = os.path.join(ROOT, lang, "faq.html")
    h = open(p, encoding="utf-8").read()
    # liens des services, repris du menu « Services » du pied de page
    serv = re.search(r'<h2>[^<]*</h2>\s*((?:<a href="service-[^"]+\.html">[^<]+</a>\s*)+)', h)
    liens = re.findall(r'<a href="(service-[^"]+\.html)">([^<]+)</a>', serv.group(1)) if serv else []
    if not liens:
        liens = re.findall(r'<a href="(service-[^"]+\.html)">([^<]+)</a>', h)[:7]
    vus, uniques = set(), []
    for a, b in liens:
        if a not in vus:
            vus.add(a); uniques.append((a, b))
    cote = ('<aside class="faq-cote">'
            + f'<div class="cote-carte autres"><h3>{t["serv"]}</h3><ul>'
            + "".join(f'<li><a href="{a}">{b}</a></li>' for a, b in uniques) + "</ul></div>"
            + (f'<div class="cote-carte"><h3>{t["cons"]}</h3><p>{t["cons_p"]}</p><a class="lien-fleche" href="{"../" if lang else ""}conseils.html">{t["cons_l"]}</a></div>')
            + contact_card(t, t["faq_h"], t["faq_p"]) + "</aside>")
    if '<div class="faq-grille">' in h:
        h = re.sub(r'<aside class="faq-cote">.*?</aside>', cote, h, count=1, flags=re.S)
    else:
        h, n = re.subn(r'(<section><div class="conteneur">)(<div class="faq">.*?)(\n</div></section>)',
                       lambda m: f'{m.group(1)}<div class="faq-grille"><div class="faq-principal">{m.group(2)}</div>{cote}</div>{m.group(3)}', h, count=1, flags=re.S)
        assert n == 1, p
    open(p, "w", encoding="utf-8").write(h)


if __name__ == "__main__":
    for lg in ("", "en", "ar"):
        service_pages(lg)
        faq_page(lg)
    print("ok")
