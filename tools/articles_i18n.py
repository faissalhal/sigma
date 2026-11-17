"""Articles « Conseils » en anglais (en/) et en arabe (ar/), à partir des traductions de tools/articles/i18n/<langue>/*.py.

Pour chaque langue : une page par article (en/<slug>.html), la page Conseils (en/conseils.html) et une page par thème
(en/conseils-<lot>.html). En-tête, menu et pied de page sont repris de la page FAQ de la langue. Les versions FR, EN et AR
d'un même article sont reliées (hreflang, sélecteur de langue). Les images, catégories, durées et sources viennent de
l'article français. Usage (après tools/articles_seo.py) : python3 tools/articles_i18n.py
"""
import glob, html, importlib.util, json, os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "tools"))
import articles_seo as A  # noqa: E402

DOMAIN = A.DOMAIN
LANGS = ("en", "ar")
MOIS = {"en": ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"],
        "ar": ["يناير", "فبراير", "مارس", "أبريل", "ماي", "يونيو", "يوليوز", "غشت", "شتنبر", "أكتوبر", "نونبر", "دجنبر"]}

TX = {
 "en": {
  "home": "Home", "advice": "Advice", "hub_title": "Advice and guides", "hub_meta": "Construction advice for Morocco",
  "hub_lead": "Building costs, permits, structure, electrical, plumbing, air conditioning: practical guides from our engineers to prepare your project in Morocco.",
  "search": "Search the {n} articles", "search_lot": "Search in “{lot}”", "ph": "E.g. sockets, foundations, air conditioning, buying a riad…",
  "ph_lot": "Type a keyword…", "empty": 'No article matches. Try another word, or <a href="contact.html#formulaire">ask us your question</a>.',
  "empty_lot": 'No article matches. <a href="conseils.html">See all topics</a>.',
  "start": "Where to start?", "see_all": "See all {n} articles on “{lot}” →", "whole": "Whole topic →", "read": "Read the article →",
  "min": "{n} min read", "published": "Published {d}", "by": "SIGMA ICC, engineering consultancy",
  "contents": "Contents", "others": "Other advice", "all_lot": "All advice on “{lot}” →",
  "c_h": "Need an engineering consultancy?", "c_p": "Reinforced concrete, electrical, plumbing and HVAC design, site supervision in Marrakech and across Morocco.",
  "c_b1": "Request a study", "c_b2": "Message us on WhatsApp",
  "cta_h": "A project in the pipeline?", "cta_p": "SIGMA ICC designs reinforced concrete, electrical, plumbing and HVAC systems and supervises sites for villas, riads, hotels and shops.",
  "cta_b1": "Request a study", "cta_b2": "Estimate my works", "sources": "Sources", "faq": "Frequently asked questions",
  "lot_cta_h": "Need a study for your project?", "lot_cta_p": "SIGMA ICC carries out engineering studies and site supervision in Marrakech and across Morocco.",
  "lot_cta_b1": "Request a quote", "lot_cta_b2": "See the service", "themes": "Topics", "lot_title": "{lot} advice: {n} guides for your project in Morocco",
  "parcours": [("I'm building", "Budget, studies and stages of a villa"), ("I'm buying", "The checklist before you sign"),
               ("I'm renovating", "Where to start a renovation"), ("My electrics", "The key rules of NF C 15-100")],
  "locale": "en_US",
  "lots": {"structure": "Structure and reinforced concrete", "electricite": "Electrical", "plomberie": "Plumbing and sanitation",
           "cvc": "Air conditioning and ventilation", "thermique": "Thermal and energy", "incendie": "Fire safety",
           "vrd": "Roads and utilities (VRD)", "achat": "Buying and inspection", "reglementation": "Procedures, prices and site work"},
  "intros": {
   "structure": "Foundations, columns, beams, floors, concrete and steel, seismic code: understand the structure of your house before and during construction.",
   "electricite": "NF C 15-100 and NM 06.1.100 standards, distribution board, RCDs, sockets, earthing, solar PV: the rules of a safe electrical installation in Morocco.",
   "plomberie": "Pipe sizes, drainage, solar water heaters, water pressure, leaks, sanitation: designing the plumbing of a villa or riad properly.",
   "cvc": "Air conditioning, ventilation, heating and humidity: choosing and sizing the right equipment for the Marrakech climate.",
   "thermique": "Insulation, glazing, orientation, solar shading and electricity bills: building a comfortable house in summer and winter.",
   "incendie": "Buildings open to the public, hotels, riads, car parks: detection, smoke control, emergency exits and fire safety equipment.",
   "vrd": "Housing estates, sewerage, utility connections, roads and stormwater: the networks that serve a plot or a project.",
   "achat": "Before buying a house, a riad, a new apartment or a plot: what to check, system by system, and what an inspection costs.",
   "reglementation": "Building permits, inspection bodies, warranties, handover, contracts and prices: the procedures of a construction project in Morocco."},
 },
 "ar": {
  "home": "الرئيسية", "advice": "نصائح", "hub_title": "نصائح وأدلة", "hub_meta": "نصائح البناء في المغرب",
  "hub_lead": "تكلفة البناء، رخصة البناء، الهيكل، الكهرباء، الترصيص، التكييف: أدلة عملية من مهندسينا لتحضير مشروعك في المغرب.",
  "search": "ابحث في {n} مقالا", "search_lot": "ابحث في «{lot}»", "ph": "مثال: المآخذ، الأساسات، التكييف، شراء رياض…",
  "ph_lot": "اكتب كلمة مفتاحية…", "empty": 'لا يوجد مقال مطابق. جرب كلمة أخرى، أو <a href="contact.html#formulaire">اطرح علينا سؤالك</a>.',
  "empty_lot": 'لا يوجد مقال مطابق. <a href="conseils.html">كل المواضيع</a>.',
  "start": "من أين تبدأ؟", "see_all": "عرض {n} مقالا في «{lot}» ←", "whole": "كل الموضوع ←", "read": "اقرأ المقال ←",
  "min": "مدة القراءة: {n} دقائق", "published": "نُشر في {d}", "by": "SIGMA ICC، مكتب دراسات تقنية",
  "contents": "المحتويات", "others": "نصائح أخرى", "all_lot": "كل نصائح «{lot}» ←",
  "c_h": "هل تحتاج إلى مكتب دراسات؟", "c_p": "دراسات الخرسانة المسلحة والكهرباء والترصيص والتكييف، وتتبع الأوراش في مراكش وفي جميع أنحاء المغرب.",
  "c_b1": "اطلب دراسة", "c_b2": "راسلنا على واتساب",
  "cta_h": "هل لديك مشروع قيد التحضير؟", "cta_p": "تنجز SIGMA ICC دراسات الخرسانة المسلحة والكهرباء والترصيص والتكييف، وتتبع الأوراش للفيلات والرياضات والفنادق والمحلات التجارية.",
  "cta_b1": "اطلب دراسة", "cta_b2": "قدّر تكلفة أشغالي", "sources": "المصادر", "faq": "الأسئلة الشائعة",
  "lot_cta_h": "هل تحتاج إلى دراسة لمشروعك؟", "lot_cta_p": "تنجز SIGMA ICC الدراسات التقنية وتتبع الأوراش في مراكش وفي جميع أنحاء المغرب.",
  "lot_cta_b1": "اطلب عرض سعر", "lot_cta_b2": "اكتشف الخدمة", "themes": "المواضيع", "lot_title": "نصائح {lot}: {n} دليلا لمشروعك في المغرب",
  "parcours": [("أبني", "الميزانية والدراسات ومراحل بناء فيلا"), ("أشتري", "لائحة المراقبة قبل التوقيع"),
               ("أجدد", "من أين تبدأ أشغال التجديد"), ("كهرباء منزلي", "القواعد الأساسية لمعيار NF C 15-100")],
  "locale": "ar_MA",
  "lots": {"structure": "الهيكل والخرسانة المسلحة", "electricite": "الكهرباء", "plomberie": "الترصيص الصحي",
           "cvc": "التكييف والتهوية", "thermique": "العزل الحراري والطاقة", "incendie": "السلامة من الحريق",
           "vrd": "الطرق والشبكات (VRD)", "achat": "الشراء والخبرة التقنية", "reglementation": "الإجراءات والأسعار والأوراش"},
  "intros": {
   "structure": "الأساسات والأعمدة والعوارض والأسقف والخرسانة والحديد وضابط البناء المضاد للزلازل: افهم هيكل منزلك قبل الورش وخلاله.",
   "electricite": "معايير NF C 15-100 وNM 06.1.100، ولوحة التوزيع، والقواطع التفاضلية، والمآخذ، والتأريض، والطاقة الشمسية: قواعد تركيب كهربائي آمن في المغرب.",
   "plomberie": "أقطار الأنابيب، وصرف المياه، والسخانات الشمسية، وضغط الماء، والتسربات، والتطهير: تصميم جيد لترصيص فيلا أو رياض.",
   "cvc": "التكييف والتهوية والتدفئة والرطوبة: اختيار التجهيزات المناسبة لمناخ مراكش وتحديد قدرتها.",
   "thermique": "العزل، والزجاج، والتوجيه، والحماية من الشمس، وفاتورة الكهرباء: بناء منزل مريح صيفا وشتاء.",
   "incendie": "المؤسسات المستقبلة للعموم، والفنادق، والرياضات، والمرائب: الكشف، وسحب الدخان، ومخارج الطوارئ، وتجهيزات السلامة من الحريق.",
   "vrd": "التجزئات، والتطهير، والربط بالشبكات، والطرق، ومياه الأمطار: الشبكات التي تخدم قطعة أرضية أو مشروعا.",
   "achat": "قبل شراء منزل أو رياض أو شقة جديدة أو قطعة أرضية: ما يجب فحصه، جزءا بجزء، وتكلفة الخبرة التقنية.",
   "reglementation": "رخصة البناء، ومكتب المراقبة، والضمانات، وتسلم الأشغال، والعقود والأسعار: إجراءات مشروع بناء في المغرب."},
 },
}
PARCOURS_SLUGS = [p[2] for p in A.PARCOURS]


def esc(s):
    return html.escape(s, quote=True)


def charge(p, nom):
    spec = importlib.util.spec_from_file_location(os.path.basename(p)[:-3] + "_i18n", p)
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
    return getattr(m, nom)


def articles_fr():
    """Métadonnées FR de tous les articles : ceux du script + les 3 faits à la main."""
    A.charger_lots()
    fr = {a["slug"]: dict(a, date=A.DATE) for a in A.ARTICLES}
    for a in charge(os.path.join(ROOT, "tools/articles/i18n/source_core.py"), "ARTICLES"):
        if a["slug"] in fr:
            continue
        h = open(os.path.join(ROOT, a["slug"] + ".html"), encoding="utf-8").read()
        img = re.search(r'<meta property="og:image" content="https://sigma-icc\.ma/([^"]+)"', h).group(1)
        mn = re.search(r"(\d+) min de lecture", h)
        sp = re.search(r'<p class="sources">(.*?)</p>', h, re.S)
        sources = [(u, html.unescape(t)) for u, t in re.findall(r'<a href="([^"]+)"[^>]*>(.*?)</a>', sp.group(1))] if sp else []
        d = re.search(r'"datePublished":\s*"([\d-]+)"', h)
        fr[a["slug"]] = dict(a, img=img, cat=A.CAT.get(a["slug"], "reglementation"), min=int(mn.group(1)) if mn else 6,
                             sources=sources, date=d.group(1) if d else A.DATE)
    return fr


def traductions(lang):
    T = {}
    for f in sorted(glob.glob(os.path.join(ROOT, "tools/articles/i18n", lang, "*.py"))):
        try:
            T.update(charge(f, "T"))
        except Exception as e:  # fichier en cours d'écriture ou invalide : ignoré cette fois
            print("traduction ignorée :", os.path.relpath(f, ROOT), type(e).__name__, file=sys.stderr)
    return T


def date_txt(d, lang):
    y, m, j = d.split("-")
    return f"{int(j)} {MOIS[lang][int(m) - 1]} {y}"


def page(lang, base, *, titre, desc, chemin, image, ld, main, fr_url, actif_conseils=True):
    """Construit une page complète sur le modèle `base` (FAQ de la langue)."""
    url = f"{DOMAIN}/{lang}/{chemin}"
    h = base
    h = re.sub(r"<title>.*?</title>", f"<title>{esc(titre)}</title>", h, count=1)
    h = re.sub(r'<meta name="description" content="[^"]*">', f'<meta name="description" content="{esc(desc)}">', h, count=1)
    h = re.sub(r'<link rel="canonical" href="[^"]*">', f'<link rel="canonical" href="{url}">', h, count=1)
    alt = (f'<link rel="alternate" hreflang="fr" href="{DOMAIN}/{fr_url}">\n<link rel="alternate" hreflang="en" href="{DOMAIN}/en/{chemin}">\n'
           f'<link rel="alternate" hreflang="ar" href="{DOMAIN}/ar/{chemin}">\n<link rel="alternate" hreflang="x-default" href="{DOMAIN}/{fr_url}">')
    h = re.sub(r'(<link rel="alternate" hreflang="[^"]+" href="[^"]*">\n?)+', alt + "\n", h, count=1)
    h = re.sub(r'<meta property="og:type" content="[^"]*">', '<meta property="og:type" content="article">' if ld and "Article" in ld else '<meta property="og:type" content="website">', h, count=1)
    for prop, val in (("og:title", titre), ("og:description", desc), ("og:url", url), ("og:image", f"{DOMAIN}/{image}")):
        h = re.sub(rf'<meta property="{prop}" content="[^"]*">', f'<meta property="{prop}" content="{esc(val)}">', h, count=1)
    h = re.sub(r'<script type="application/ld\+json">.*?</script>\n?', "", h, flags=re.S)
    if ld:
        h = h.replace("</head>", f'<script type="application/ld+json">{ld}</script>\n</head>', 1)
    # sélecteur de langue : même page dans les autres langues
    h = re.sub(r'<nav class="langues"[^>]*>.*?</nav>', lambda m: (
        f'<nav class="langues" aria-label="{"Language" if lang == "en" else "اللغة"}">'
        f'<a href="../{fr_url}" hreflang="fr" lang="fr">FR</a>'
        f'<a href="../en/{chemin}" hreflang="en" lang="en"{" aria-current=\"true\"" if lang == "en" else ""}>EN</a>'
        f'<a href="../ar/{chemin}" hreflang="ar" lang="ar"{" aria-current=\"true\"" if lang == "ar" else ""}>ع</a></nav>'), h, count=1, flags=re.S)
    # menu : rubrique Conseils active
    h = re.sub(r'(<nav class="nav" id="nav"[^>]*>.*?</nav>)', lambda m: m.group(1).replace(' aria-current="page"', "").replace(
        'href="conseils.html">', 'href="conseils.html" aria-current="page">' if actif_conseils else 'href="conseils.html">'), h, count=1, flags=re.S)
    h = re.sub(r"<main>.*?</main>", lambda m: "<main>\n" + main + "\n</main>", h, count=1, flags=re.S)
    return h


def carte(lang, a, t, x):
    return (f'<a class="service" href="{a["slug"]}.html"><img src="../{a["img"]}" alt="" loading="lazy" width="750" height="600">\n'
            f'  <div><span class="code">{esc(x["lots"][a["cat"]])} · {a["min"]} min</span><h3>{esc(t["title"])}</h3><p>{esc(t["lead"])}</p>'
            f'<span class="lire">{x["read"]}</span></div></a>')


def construire(lang):
    x = TX[lang]
    base = open(os.path.join(ROOT, lang, "faq.html"), encoding="utf-8").read()
    fr, T = articles_fr(), traductions(lang)
    ordre = [a["slug"] for a in A.ARTICLES] + [s for s in fr if s not in {a["slug"] for a in A.ARTICLES}]
    dispo = [s for s in ordre if s in T]
    par_lot = {k: [s for s in dispo if fr[s]["cat"] == k] for k, _ in A.LOTS}
    # ---- articles
    for s in dispo:
        a, t = fr[s], T[s]
        lotn = x["lots"][a["cat"]]
        n = [0]
        def ancre(m):
            n[0] += 1
            return f'<h2 id="partie-{n[0]}">{m.group(1)}</h2>'
        body = re.sub(r"<h2>(.*?)</h2>", ancre, t["body"])
        faq = ""
        if t["faq"]:
            n[0] += 1
            faq = f'<h2 id="partie-{n[0]}">{x["faq"]}</h2><div class="faq">' + "".join(f"<details><summary>{esc(q)}</summary><p>{esc(r)}</p></details>" for q, r in t["faq"]) + "</div>"
        titres = re.findall(r'<h2 id="(partie-\d+)">(.*?)</h2>', body + faq)
        src = (f'<p class="sources"><b>{x["sources"]} :</b> ' if lang == "en" else f'<p class="sources"><b>{x["sources"]}:</b> ') + \
              " · ".join(f'<a href="{u}" target="_blank" rel="noopener">{esc(tt)}</a>' for u, tt in a["sources"]) + ".</p>" if a["sources"] else ""
        cta = (f'<div class="encadre"><h3>{x["cta_h"]}</h3><p>{x["cta_p"]}</p>\n    <div class="actions"><a class="btn" href="contact.html#formulaire">{x["cta_b1"]}</a>'
               f'<a class="btn secondaire" href="../chiffrage.html">{x["cta_b2"]}</a></div></div>')
        meta = f'<p class="meta">{x["published"].format(d=date_txt(a["date"], lang))} · {x["min"].format(n=a["min"])} · {x["by"]}</p>'
        autres = [o for o in par_lot[a["cat"]] if o != s][:6]
        if len(autres) < 6:
            autres += [o for o in dispo if o != s and o not in autres][:6 - len(autres)]
        aside = (f'<aside class="article-cote"><div class="cote-carte"><h3>{x["contents"]}</h3><ol class="sommaire">'
                 + "".join(f'<li><a href="#{i}">{tt}</a></li>' for i, tt in titres) + "</ol></div>"
                 f'<div class="cote-carte"><h3>{x["others"]}</h3><ul class="autres">'
                 + "".join(f'<li><a href="{o}.html">{esc(T[o]["title"])}</a></li>' for o in autres)
                 + f'<li class="tous"><a href="conseils-{a["cat"]}.html">{x["all_lot"].format(lot=esc(lotn))}</a></li></ul></div>'
                 f'<div class="cote-carte cote-contact"><h3>{x["c_h"]}</h3><p>{x["c_p"]}</p><a class="btn" href="contact.html#formulaire">{x["c_b1"]}</a>'
                 f'<a class="btn secondaire" href="https://wa.me/212620897660" rel="noopener">{x["c_b2"]}</a>'
                 '<a class="cote-tel" href="tel:+212661057455" dir="ltr">+212 6 61 05 74 55</a></div></aside>')
        main = (f'<div class="entete-page"><div class="conteneur">\n  <div class="fil"><a href="index.html">{x["home"]}</a> / <a href="conseils.html">{x["advice"]}</a> / '
                f'<a href="conseils-{a["cat"]}.html">{esc(lotn)}</a> / {esc(t["crumb"])}</div>\n  <h1>{esc(t["title"])}</h1><p>{esc(t["lead"])}</p>\n</div></div>\n'
                f'<section><div class="conteneur article-grille"><article class="contenu article">\n  {meta}\n{body}{faq}\n  {cta}\n  {src}\n</article>{aside}</div></section>')
        url = f"{DOMAIN}/{lang}/{s}.html"
        g = [{"@type": "Article", "headline": t["title"], "description": t["desc"], "datePublished": a["date"], "dateModified": A.DATE, "inLanguage": lang,
              "author": {"@type": "Organization", "name": "SIGMA ICC"},
              "publisher": {"@type": "Organization", "name": "SIGMA ICC", "logo": {"@type": "ImageObject", "url": f"{DOMAIN}/images/logo-sigma.svg"}},
              "image": f"{DOMAIN}/{a['img']}", "mainEntityOfPage": url}]
        if t["faq"]:
            g.append({"@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": r}} for q, r in t["faq"]]})
        ld = json.dumps({"@context": "https://schema.org", "@graph": g}, ensure_ascii=False)
        h = page(lang, base, titre=t["title"] + " | SIGMA ICC", desc=t["desc"], chemin=s + ".html", image=a["img"], ld=ld, main=main, fr_url=s + ".html")
        open(os.path.join(ROOT, lang, s + ".html"), "w", encoding="utf-8").write(h)
    # ---- page Conseils de la langue
    total = len(dispo)
    nav = "".join(f'<a href="conseils-{k}.html">{esc(x["lots"][k])} <span>{len(par_lot[k])}</span></a>' for k, _ in A.LOTS if par_lot[k])
    parcours = "".join(f'<a class="parcours" href="{slug}.html"><span>{esc(sit)}</span><b>{esc(txt)}</b></a>'
                       for (sit, txt), slug in zip(x["parcours"], PARCOURS_SLUGS) if slug in T)
    blocs = []
    for k, _ in A.LOTS:
        lot = par_lot[k]
        if not lot:
            continue
        cards = "".join(carte(lang, fr[s], T[s], x).replace('<a class="service"', '<a class="service en-plus"', 1) if i >= A.PAR_LOT else carte(lang, fr[s], T[s], x) for i, s in enumerate(lot))
        plus = f'<a class="voir-lot" href="conseils-{k}.html">{x["see_all"].format(n=len(lot), lot=esc(x["lots"][k]))}</a>' if len(lot) > A.PAR_LOT else ""
        blocs.append(f'<div class="lot-conseils" id="lot-{k}"><div class="lot-tete"><h2>{esc(x["lots"][k])}</h2><a href="conseils-{k}.html">{x["whole"]}</a></div>'
                     f'<div class="grille-services">{cards}</div>{plus}</div>')
    recherche = lambda lab, ph, vide: (f'<div class="recherche-conseils"><label for="q-conseils">{lab}</label>'
                                       f'<input id="q-conseils" type="search" placeholder="{esc(ph)}" autocomplete="off" data-recherche="#lots-conseils .service">'
                                       f'<p class="recherche-vide" hidden>{vide}</p></div>')
    main = (f'<div class="entete-page"><div class="conteneur">\n  <div class="fil"><a href="index.html">{x["home"]}</a> / {x["advice"]}</div>\n'
            f'  <h1>{x["hub_title"]}</h1><p>{x["hub_lead"]}</p>\n</div></div>\n'
            f'<section><div class="conteneur">{recherche(x["search"].format(n=total), x["ph"], x["empty"])}'
            f'<h2 class="titre-parcours">{x["start"]}</h2><div class="parcours-grille">{parcours}</div>'
            f'<nav class="lots-nav" aria-label="{x["themes"]}">{nav}</nav><div id="lots-conseils">{"".join(blocs)}</div></div></section>')
    h = page(lang, base, titre=f'{x["hub_title"]} | SIGMA ICC', desc=x["hub_lead"], chemin="conseils.html", image="images/villa-finie.jpg", ld="", main=main, fr_url="conseils.html")
    open(os.path.join(ROOT, lang, "conseils.html"), "w", encoding="utf-8").write(h)
    # ---- pages par thème
    for k, _ in A.LOTS:
        lot = par_lot[k]
        if not lot:
            continue
        nom, intro = x["lots"][k], x["intros"][k]
        service = A.LOT_INFO[k][1]
        navk = "".join(f'<a href="conseils-{j}.html"{" aria-current=\"page\"" if j == k else ""}>{esc(x["lots"][j])} <span>{len(par_lot[j])}</span></a>' for j, _ in A.LOTS if par_lot[j])
        main = (f'<div class="entete-page"><div class="conteneur">\n  <div class="fil"><a href="index.html">{x["home"]}</a> / <a href="conseils.html">{x["advice"]}</a> / {esc(nom)}</div>\n'
                f'  <h1>{esc(nom)}</h1><p>{esc(intro)}</p>\n</div></div>\n'
                f'<section><div class="conteneur">{recherche(x["search_lot"].format(lot=esc(nom)), x["ph_lot"], x["empty_lot"])}'
                f'<nav class="lots-nav" aria-label="{x["themes"]}">{navk}</nav>'
                f'<div id="lots-conseils"><div class="lot-conseils"><div class="grille-services">{"".join(carte(lang, fr[s], T[s], x) for s in lot)}</div></div></div>'
                f'<div class="encadre"><h3>{x["lot_cta_h"]}</h3><p>{x["lot_cta_p"]}</p><div class="actions"><a class="btn" href="contact.html#formulaire">{x["lot_cta_b1"]}</a>'
                f'<a class="btn secondaire" href="{service}">{x["lot_cta_b2"]}</a></div></div></div></section>')
        h = page(lang, base, titre=x["lot_title"].format(lot=nom, n=len(lot)) + " | SIGMA ICC", desc=intro, chemin=f"conseils-{k}.html",
                 image="images/villa-finie.jpg", ld="", main=main, fr_url=f"conseils-{k}.html")
        open(os.path.join(ROOT, lang, f"conseils-{k}.html"), "w", encoding="utf-8").write(h)
    return dispo, [k for k, _ in A.LOTS if par_lot[k]]


def liens_fr(dispo_par_langue, lots):
    """Pages FR : hreflang et sélecteur de langue vers la version traduite quand elle existe."""
    pages = [s + ".html" for s in set.intersection(*[set(d) for d in dispo_par_langue.values()])] + ["conseils.html"] + [f"conseils-{k}.html" for k in lots]
    for p in pages:
        f = os.path.join(ROOT, p); h = open(f, encoding="utf-8").read()
        h = re.sub(r'<link rel="alternate" hreflang="[^"]+" href="[^"]*">\n', "", h)
        alt = "".join(f'<link rel="alternate" hreflang="{l}" href="{DOMAIN}/{"" if l in ("fr", "x-default") else l + "/"}{p}">\n' for l in ("fr", "en", "ar", "x-default"))
        h = re.sub(r'(<link rel="canonical" href="[^"]*">\n)', lambda m: m.group(1) + alt, h, count=1)
        h = re.sub(r'<nav class="langues"[^>]*>.*?</nav>', lambda m: (
            f'<nav class="langues" aria-label="Langue"><a href="{p}" hreflang="fr" lang="fr" aria-current="true">FR</a>'
            f'<a href="en/{p}" hreflang="en" lang="en">EN</a><a href="ar/{p}" hreflang="ar" lang="ar">ع</a></nav>'), h, count=1, flags=re.S)
        open(f, "w", encoding="utf-8").write(h)


def plan_du_site(dispo_par_langue, lots):
    sp = os.path.join(ROOT, "sitemap.xml"); s = open(sp, encoding="utf-8").read()
    s = re.sub(r"  <url><loc>https://sigma-icc\.ma/(?:en|ar)/conseils?[^<]*</loc>.*?</url>\n", "", s)
    add = ""
    for lang, dispo in dispo_par_langue.items():
        for p in ["conseils.html"] + [f"conseils-{k}.html" for k in lots] + [d + ".html" for d in dispo]:
            add += f"  <url><loc>{DOMAIN}/{lang}/{p}</loc><lastmod>{A.DATE}</lastmod><priority>0.6</priority></url>\n"
    s = s.replace("</urlset>", add + "</urlset>", 1)
    open(sp, "w", encoding="utf-8").write(s)


def main():
    dispo = {}
    lots = set()
    for lg in LANGS:
        d, l = construire(lg)
        dispo[lg] = d; lots |= set(l)
        print(lg, len(d), "articles traduits")
    lots = [k for k, _ in A.LOTS if k in lots]
    liens_fr(dispo, lots)
    plan_du_site(dispo, lots)


if __name__ == "__main__":
    main()
