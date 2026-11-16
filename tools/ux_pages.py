"""Améliorations de navigation et de contenu (FR, EN, AR), idempotentes : python3 tools/ux_pages.py

1. Menu EN/AR : lien vers les conseils (en français).
2. Accueil : barre d'accès rapide sous le diaporama (Appeler, Devis, Services), sur téléphone.
3. Textes concrets : « Qui sommes-nous » (À propos), engagements de l'accueil, encadré « En bref » en tête de chaque service.
   Seuls des faits présents sur le site sont utilisés (projets de data/projets.json, chiffres de l'accueil).
(4. Le bouton « Obtenir un devis » sur ordinateur est réglé dans assets/css/sigma.css.)
"""
import os, re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LANGS = ("", "en", "ar")


def lire(p):
    return open(os.path.join(ROOT, p), encoding="utf-8").read()


def ecrire(p, h):
    open(os.path.join(ROOT, p), "w", encoding="utf-8").write(h)


def entre(h, nom, contenu, avant=None, remplace=None):
    """Remplace le bloc <!--nom-->…<!--/nom--> ; sinon l'insère avant `avant` ou à la place de la regex `remplace`."""
    bloc = f"<!--{nom}-->{contenu}<!--/{nom}-->"
    if f"<!--{nom}-->" in h:
        return re.sub(rf"<!--{nom}-->.*?<!--/{nom}-->", lambda m: bloc, h, count=1, flags=re.S)
    if remplace:
        h2, n = re.subn(remplace, lambda m: bloc, h, count=1, flags=re.S)
        assert n == 1, (nom, remplace[:60])
        return h2
    assert avant in h, (nom, avant[:60])
    return h.replace(avant, bloc + avant, 1)


# 1. menu EN/AR -------------------------------------------------------------------------------------
CONSEILS_NAV = {"en": "Advice (FR)", "ar": "نصائح (بالفرنسية)"}


def menu_conseils():
    for lg, txt in CONSEILS_NAV.items():
        for f in sorted(os.listdir(os.path.join(ROOT, lg))):
            if not f.endswith(".html"):
                continue
            p = f"{lg}/{f}"; h = lire(p)
            if 'id="nav"' not in h or "../conseils.html" in h.split('id="nav"', 1)[1].split("</nav>", 1)[0]:
                continue
            h, n = re.subn(r'(<nav class="nav" id="nav"[^>]*>.*?<a href="faq.html"[^>]*>[^<]*</a>)',
                           lambda m: m.group(1) + f'<a href="../conseils.html" hreflang="fr">{txt}</a>', h, count=1, flags=re.S)
            if n:
                ecrire(p, h)


# 2. accès rapide sur l'accueil -----------------------------------------------------------------------
RAPIDE = {"": ("Appeler", "Demander un devis", "Nos services", "Accès rapide"),
          "en": ("Call us", "Get a quote", "Our services", "Quick access"),
          "ar": ("اتصل بنا", "اطلب عرض سعر", "خدماتنا", "وصول سريع")}


def acces_rapide():
    for lg in LANGS:
        p = os.path.join(lg, "index.html"); h = lire(p)
        a, b, c, lab = RAPIDE[lg]
        html = (f'<nav class="acces-rapide" aria-label="{lab}"><div class="conteneur">'
                f'<a href="tel:+212661057455"><span aria-hidden="true">☎</span>{a}</a>'
                f'<a class="principal" href="contact.html#formulaire">{b}</a>'
                f'<a href="services.html">{c}</a></div></nav>')
        h = entre(h, "acces-rapide", html, avant='<section class="bande-action">')
        ecrire(p, h)


# 3a. engagements de l'accueil et texte « Qui sommes-nous » -----------------------------------------------
ENGAGEMENTS = {
    "": ["7 domaines d'études sous un même toit", "Villas, immeubles, hôtels, restaurants, usines et projets agricoles",
         "Références à Marrakech, Rabat, Fès, El Jadida et Settat", "Un ingénieur joignable 7 j/7"],
    "en": ["7 engineering disciplines under one roof", "Villas, apartment buildings, hotels, restaurants, factories and farms",
           "References in Marrakech, Rabat, Fès, El Jadida and Settat", "An engineer on call 7 days a week"],
    "ar": ["7 مجالات دراسات تحت سقف واحد", "فيلات وعمارات وفنادق ومطاعم ومصانع ومشاريع فلاحية",
           "مراجع في مراكش والرباط وفاس والجديدة وسطات", "مهندس متاح طيلة أيام الأسبوع"],
}
APROPOS = {
    "": ["SIGMA ICC est un bureau d'études techniques installé à Guéliz, Marrakech. Nous réalisons les études de tous les lots techniques d'un bâtiment : structure en béton armé, électricité courants forts et courants faibles, plomberie, climatisation et ventilation, thermique et énergie solaire, sécurité incendie et VRD. Nous suivons ensuite le chantier jusqu'à la réception.",
         "Nous intervenons sur des villas et des riads, des immeubles, des hôtels, des restaurants, des commerces, des usines et des projets agricoles. Nos clients sont des particuliers, des promoteurs, des exploitants, des industriels, des agriculteurs et des collectivités. Nous travaillons avec leur architecte, du dossier de permis de construire jusqu'aux plans d'exécution.",
         "Quelques réalisations : des villas R+1 avec sous-sol à Marrakech, Rabat et El Jadida ; les études électricité, CVC et sécurité incendie de 9 magasins à Marrakech, Rabat et Fès ; des études de stabilité et la réhabilitation de riads à Marrakech ; le pompage solaire de bornes fontaines près de Settat.",
         "Notre façon de travailler : des notes de calcul et des plans clairs, des quantités justes pour ne pas surdimensionner, et un ingénieur joignable 7 jours sur 7 pendant le chantier."],
    "en": ["SIGMA ICC is a technical engineering consultancy based in Guéliz, Marrakech. We design every technical package of a building: reinforced concrete structure, high- and low-voltage electrical systems, plumbing, air conditioning and ventilation, thermal and solar energy, fire safety, roads and utilities. We then supervise the site through to handover.",
           "We work on villas and riads, apartment buildings, hotels, restaurants, shops, factories and agricultural projects. Our clients are private owners, developers, operators, manufacturers, farmers and local authorities. We work alongside their architect, from the building permit application to the construction drawings.",
           "Selected projects: two-storey villas with basements in Marrakech, Rabat and El Jadida; electrical, HVAC and fire safety design for 9 shops in Marrakech, Rabat and Fès; structural assessment and rehabilitation of riads in Marrakech; solar pumping for public water points near Settat.",
           "How we work: clear calculations and drawings, accurate quantities with no over-design, and an engineer you can reach 7 days a week during the works."],
    "ar": ["SIGMA ICC مكتب دراسات تقنية مقره بحي جيليز في مراكش. ننجز دراسات جميع الأشغال التقنية للبناية: الهيكل بالخرسانة المسلحة، والكهرباء بالتيارات القوية والضعيفة، والترصيص الصحي، والتكييف والتهوية، والحرارة والطاقة الشمسية، والسلامة من الحريق، والطرق والشبكات المختلفة. ثم نتابع الورش حتى التسليم.",
           "نشتغل على الفيلات والرياضات، والعمارات، والفنادق، والمطاعم، والمحلات التجارية، والمصانع، والمشاريع الفلاحية. زبناؤنا خواص، ومنعشون عقاريون، ومسيرو مؤسسات، وصناعيون، وفلاحون، وجماعات. نعمل إلى جانب المهندس المعماري، من ملف رخصة البناء إلى تصاميم التنفيذ.",
           "من إنجازاتنا: فيلات من طابقين مع طابق تحت أرضي في مراكش والرباط والجديدة؛ ودراسات الكهرباء والتكييف والسلامة من الحريق لتسعة محلات تجارية في مراكش والرباط وفاس؛ ودراسات الاستقرار وإعادة تأهيل رياضات في مراكش؛ والضخ بالطاقة الشمسية لسقايات قرب سطات.",
           "طريقة عملنا: مذكرات حساب وتصاميم واضحة، وكميات مضبوطة دون مبالغة في الأبعاد، ومهندس يمكن التواصل معه طيلة أيام الأسبوع خلال الأشغال."],
}


def textes_concrets():
    for lg in LANGS:
        p = os.path.join(lg, "index.html"); h = lire(p)
        lis = "".join(f"<li>{t}</li>" for t in ENGAGEMENTS[lg])
        h, n = re.subn(r'<ul class="engagements">.*?</ul>', f'<ul class="engagements">{lis}</ul>', h, count=1, flags=re.S)
        assert n == 1, p
        ecrire(p, h)
        p = os.path.join(lg, "about.html"); h = lire(p)
        ps = "".join(f"<p>{t}</p>" for t in APROPOS[lg])
        # paragraphes du premier bloc .texte (après le titre h2), jusqu'à la fin de ce bloc
        h, n = re.subn(r'(<div class="texte"><span class="repere">[^<]*</span><h2>[^<]*</h2>)(?:<!--apropos-->)?(?:<p>.*?</p>)+(?:<!--/apropos-->)?',
                       lambda m: m.group(1) + "<!--apropos-->" + ps + "<!--/apropos-->", h, count=1, flags=re.S)
        assert n == 1, p
        ecrire(p, h)


# 3b. encadré « En bref » des pages service ------------------------------------------------------------
LIB = {"": ("En bref", "Demander un devis", "Nos conseils sur ce thème"),
       "en": ("At a glance", "Get a quote", "Our advice (in French)"),
       "ar": ("باختصار", "اطلب عرض سعر", "نصائحنا (بالفرنسية)")}
LOT = {"STRUCTURE": "structure", "CFA": "electricite", "FD": "cvc", "CSSI": "incendie", "EGT": "thermique", "VRD": "vrd", "BIM": "reglementation"}
BREF = {
 "STRUCTURE": {
  "": [("Ce que nous livrons", "notes de calcul, plans de coffrage et de ferraillage, nomenclatures d'aciers, selon le règlement parasismique RPS 2000 (version 2011)."),
       ("Pour quels projets", "villas, immeubles, riads, hôtels, restaurants, commerces, usines, bâtiments agricoles et équipements publics."),
       ("Sur le chantier", "contrôle du ferraillage avant coulage, réponses aux entreprises, coordination avec le bureau de contrôle."),
       ("Déjà réalisé", "villas R+1 avec sous-sol à Marrakech, Rabat et El Jadida ; études de stabilité et réhabilitation de riads à Marrakech.")],
  "en": [("What we deliver", "structural calculations, formwork and reinforcement drawings and rebar schedules, in line with the Moroccan seismic code RPS 2000 (2011 version)."),
         ("For which projects", "villas, apartment buildings, riads, hotels, restaurants, shops, factories, farm buildings and public facilities."),
         ("On site", "rebar inspection before pouring, answers to contractors, coordination with the inspection body."),
         ("Already delivered", "two-storey villas with basements in Marrakech, Rabat and El Jadida; structural assessment and rehabilitation of riads in Marrakech.")],
  "ar": [("ما نسلمه", "مذكرات الحساب وتصاميم القوالب والتسليح وجداول الحديد، وفق ضابط البناء المضاد للزلازل RPS 2000 (صيغة 2011)."),
         ("لأي مشاريع", "الفيلات والعمارات والرياضات والفنادق والمطاعم والمحلات التجارية والمصانع والبنايات الفلاحية والمرافق العمومية."),
         ("في الورش", "مراقبة التسليح قبل الصب، والإجابة على أسئلة المقاولات، والتنسيق مع مكتب المراقبة."),
         ("أنجزنا", "فيلات من طابقين مع طابق تحت أرضي في مراكش والرباط والجديدة؛ ودراسات الاستقرار وإعادة تأهيل رياضات في مراكش.")]},
 "CFA": {
  "": [("Ce que nous livrons", "bilan de puissance, schémas unifilaires des tableaux, plans d'éclairage et de prises, calcul des sections de câbles, CCTP et métrés."),
       ("Courants faibles", "réseau informatique et fibre, téléphonie, vidéosurveillance, contrôle d'accès, sonorisation, détection incendie."),
       ("Références techniques", "NF C 15-100, la norme la plus utilisée au Maroc, et la série de normes marocaines NM 06.1.100."),
       ("Déjà réalisé", "études électricité de 9 magasins à Marrakech, Rabat et Fès, de villas, d'immeubles, d'hôtels, de restaurants, d'usines et d'exploitations agricoles.")],
  "en": [("What we deliver", "power demand assessment, single-line diagrams of the boards, lighting and socket layouts, cable sizing, specifications and bills of quantities."),
         ("Low-voltage systems", "data network and fibre, telephony, CCTV, access control, public address, fire detection."),
         ("Technical references", "NF C 15-100, the standard most used in Morocco, and the Moroccan NM 06.1.100 series."),
         ("Already delivered", "electrical design for 9 shops in Marrakech, Rabat and Fès, and for villas, apartment buildings, hotels, restaurants, factories and farms.")],
  "ar": [("ما نسلمه", "حصيلة القدرة، والمخططات الأحادية للوحات، وتصاميم الإنارة والمآخذ، وحساب مقاطع الكابلات، ودفتر الشروط التقنية والكميات."),
         ("التيارات الضعيفة", "شبكة المعلوميات والألياف البصرية، والهاتف، والمراقبة بالكاميرات، ومراقبة الولوج، والصوتيات، وكشف الحريق."),
         ("المرجعيات التقنية", "معيار NF C 15-100 الأكثر استعمالا في المغرب، وسلسلة المعايير المغربية NM 06.1.100."),
         ("أنجزنا", "دراسات الكهرباء لتسعة محلات تجارية في مراكش والرباط وفاس، ولفيلات وعمارات وفنادق ومطاعم ومصانع وضيعات فلاحية.")]},
 "FD": {
  "": [("Ce que nous livrons", "bilan thermique, choix et dimensionnement des équipements (split, gainable, VRV, VMC), plans des réseaux, plomberie et évacuations, désenfumage."),
       ("Pour quels projets", "villas, immeubles, riads, hôtels, restaurants (extraction de cuisine), commerces, bureaux, usines et parkings."),
       ("Climat de Marrakech", "des étés au-delà de 40 °C : les puissances sont calculées pièce par pièce, sans surdimensionner."),
       ("Déjà réalisé", "études CVC de 9 magasins à Marrakech, Rabat et Fès ; plomberie et climatisation de villas.")],
  "en": [("What we deliver", "heat load calculation, equipment selection and sizing (split, ducted, VRF, mechanical ventilation), duct and pipe layouts, plumbing and drainage, smoke control."),
         ("For which projects", "villas, apartment buildings, riads, hotels, restaurants (kitchen extraction), shops, offices, factories and car parks."),
         ("Marrakech climate", "summers above 40 °C: capacities are calculated room by room, without over-sizing."),
         ("Already delivered", "HVAC design for 9 shops in Marrakech, Rabat and Fès; plumbing and air conditioning for villas.")],
  "ar": [("ما نسلمه", "الحصيلة الحرارية، واختيار التجهيزات وتحديد قدرتها (سبليت، قنوات، VRV، تهوية ميكانيكية)، وتصاميم الشبكات، والترصيص الصحي وصرف المياه، وسحب الدخان."),
         ("لأي مشاريع", "الفيلات والعمارات والرياضات والفنادق والمطاعم (شفط المطابخ) والمحلات التجارية والمكاتب والمصانع والمرائب."),
         ("مناخ مراكش", "صيف تتجاوز حرارته 40 درجة: تحسب القدرات غرفة بغرفة دون مبالغة."),
         ("أنجزنا", "دراسات التكييف لتسعة محلات تجارية في مراكش والرباط وفاس؛ والترصيص والتكييف لفيلات.")]},
 "CSSI": {
  "": [("Notre rôle", "coordonner le système de sécurité incendie (SSI) de la conception à la réception, pour qu'alarme, détection, désenfumage et portes fonctionnent ensemble."),
       ("Ce que nous livrons", "analyse du projet, cahier des charges SSI, suivi des essais et dossier d'identité du SSI."),
       ("Pour quels projets", "établissements recevant du public, hôtels, restaurants, riads et maisons d'hôtes, immeubles, commerces, usines et parkings, au regard du décret 2-14-499."),
       ("Déjà réalisé", "études de détection et de protection incendie de 9 magasins à Marrakech, Rabat et Fès.")],
  "en": [("Our role", "coordinating the fire safety system (SSI) from design to handover, so that alarm, detection, smoke control and doors work together."),
         ("What we deliver", "project analysis, SSI specifications, test supervision and the SSI identity file."),
         ("For which projects", "buildings open to the public, hotels, restaurants, riads and guesthouses, apartment buildings, shops, factories and car parks, under decree 2-14-499."),
         ("Already delivered", "fire detection and protection design for 9 shops in Marrakech, Rabat and Fès.")],
  "ar": [("دورنا", "تنسيق نظام السلامة من الحريق من التصميم إلى التسليم، حتى يعمل الإنذار والكشف وسحب الدخان والأبواب معا."),
         ("ما نسلمه", "تحليل المشروع، ودفتر شروط نظام السلامة، وتتبع التجارب، وملف تعريف النظام."),
         ("لأي مشاريع", "المؤسسات المستقبلة للعموم، والفنادق، والمطاعم، والرياضات ودور الضيافة، والعمارات، والمحلات التجارية، والمصانع والمرائب، طبقا للمرسوم 2-14-499."),
         ("أنجزنا", "دراسات الكشف والحماية من الحريق لتسعة محلات تجارية في مراكش والرباط وفاس.")]},
 "EGT": {
  "": [("Ce que nous livrons", "étude thermique selon le règlement RTCM, choix des isolants et des vitrages, protections solaires, dimensionnement solaire (eau chaude, photovoltaïque, pompage)."),
       ("L'objectif", "une maison fraîche l'été à Marrakech, chaude l'hiver, avec une facture d'électricité réduite."),
       ("Pour quels projets", "villas, immeubles, hôtels, restaurants, bâtiments tertiaires, usines et exploitations agricoles (pompage solaire, irrigation)."),
       ("Déjà réalisé", "étude et dimensionnement de systèmes de pompage solaire pour des bornes fontaines près de Settat.")],
  "en": [("What we deliver", "thermal study under the Moroccan RTCM code, insulation and glazing choices, solar shading, solar sizing (hot water, photovoltaics, pumping)."),
         ("The goal", "a house that stays cool in a Marrakech summer and warm in winter, with a lower electricity bill."),
         ("For which projects", "villas, apartment buildings, hotels, restaurants, offices, factories and farms (solar pumping, irrigation)."),
         ("Already delivered", "design and sizing of solar pumping systems for public water points near Settat.")],
  "ar": [("ما نسلمه", "الدراسة الحرارية وفق النظام الحراري للبناء بالمغرب RTCM، واختيار العوازل والزجاج، والحماية من الشمس، وتحديد أنظمة الطاقة الشمسية (الماء الساخن، الكهروضوئية، الضخ)."),
         ("الهدف", "منزل منعش في صيف مراكش ودافئ في الشتاء، بفاتورة كهرباء أقل."),
         ("لأي مشاريع", "الفيلات والعمارات والفنادق والمطاعم وبنايات الخدمات والمصانع والضيعات الفلاحية (الضخ الشمسي، السقي)."),
         ("أنجزنا", "دراسة وتحديد أنظمة الضخ بالطاقة الشمسية لسقايات قرب سطات.")]},
 "VRD": {
  "": [("Ce que nous livrons", "études de faisabilité, plans de voirie, réseaux d'eau potable, d'assainissement et d'eaux pluviales, électricité et éclairage public, métrés."),
       ("Pour quels projets", "lotissements, ensembles résidentiels, zones d'activité, équipements et projets des collectivités."),
       ("Coordination", "avec les distributeurs d'eau et d'électricité et les services techniques de la commune."),
       ("Pourquoi c'est important", "des réseaux bien conçus dès le départ évitent de rouvrir les voies après la réception.")],
  "en": [("What we deliver", "feasibility studies, road layouts, drinking water, sewerage and stormwater networks, power and street lighting, bills of quantities."),
         ("For which projects", "housing estates, residential complexes, business parks, public facilities and local authority projects."),
         ("Coordination", "with the water and electricity distributors and the municipality's technical services."),
         ("Why it matters", "networks designed right from the start avoid digging up roads after handover.")],
  "ar": [("ما نسلمه", "دراسات الجدوى، وتصاميم الطرق، وشبكات الماء الصالح للشرب والتطهير ومياه الأمطار، والكهرباء والإنارة العمومية، والكميات."),
         ("لأي مشاريع", "التجزئات والمجمعات السكنية ومناطق الأنشطة والمرافق ومشاريع الجماعات."),
         ("التنسيق", "مع موزعي الماء والكهرباء والمصالح التقنية للجماعة."),
         ("لماذا هذا مهم", "شبكات مصممة جيدا منذ البداية تجنب إعادة حفر الطرق بعد التسليم.")]},
 "BIM": {
  "": [("Ce que nous livrons", "maquette numérique 3D du bâtiment, synthèse des lots techniques avec détection des conflits, plans et métrés extraits de la maquette."),
       ("L'intérêt", "les conflits entre structure, gaines et réseaux sont réglés à l'écran, pas sur le chantier ; les quantités sont fiables."),
       ("Pour quels projets", "immeubles, hôtels, usines et bâtiments neufs, et relevés de bâtiments existants."),
       ("Avec qui", "l'architecte, les entreprises et le maître d'ouvrage partagent la même maquette.")],
  "en": [("What we deliver", "a 3D digital model of the building, clash detection across technical packages, drawings and quantities taken from the model."),
         ("The benefit", "clashes between structure, ducts and pipes are solved on screen, not on site; quantities are reliable."),
         ("For which projects", "apartment buildings, hotels, factories and other new buildings, and surveys of existing buildings."),
         ("With whom", "the architect, contractors and client share the same model.")],
  "ar": [("ما نسلمه", "مجسم رقمي ثلاثي الأبعاد للبناية، وتركيب الأشغال التقنية مع كشف التعارضات، وتصاميم وكميات مستخرجة من المجسم."),
         ("الفائدة", "تحل التعارضات بين الهيكل والقنوات والشبكات على الشاشة لا في الورش، والكميات موثوقة."),
         ("لأي مشاريع", "العمارات والفنادق والمصانع وغيرها من البنايات الجديدة، ورفع البنايات القائمة."),
         ("مع من", "يتقاسم المهندس المعماري والمقاولات وصاحب المشروع نفس المجسم.")]},
}


def en_bref():
    for lg in LANGS:
        titre, devis, cons = LIB[lg]
        pre = "../" if lg else ""
        for k, items in BREF.items():
            p = os.path.join(lg, f"service-{k}.html"); h = lire(p)
            lis = "".join(f"<li><b>{a}</b> : {b}</li>" if not lg == "ar" else f"<li><b>{a}</b>: {b}</li>" for a, b in items[lg])
            html = (f'<div class="en-bref"><h2>{titre}</h2><ul>{lis}</ul><div class="actions">'
                    f'<a class="btn" href="contact.html#formulaire">{devis}</a>'
                    f'<a class="btn secondaire" href="{pre}conseils-{LOT[k]}.html">{cons}</a></div></div>')
            # remplace les paragraphes d'introduction génériques (entre le début du contenu et la galerie)
            if "<!--en-bref-->" in h:
                h = entre(h, "en-bref", html)
            else:
                h, n = re.subn(r'(<div class="contenu">)\s*(?:<p>.*?</p>\s*)*(?=<div class="visuels galerie">)',
                               lambda m: m.group(1) + "\n    <!--en-bref-->" + html + "<!--/en-bref-->\n    ", h, count=1, flags=re.S)
                assert n == 1, p
            ecrire(p, h)


if __name__ == "__main__":
    menu_conseils()
    acces_rapide()
    textes_concrets()
    en_bref()
    print("ok")
