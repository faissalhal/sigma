/* SIGMA ICC – menu, animations (diaporama, apparitions, compteurs), visionneuse photo, formulaire */
(function () {
  "use strict";
  var calme = window.matchMedia && window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  // Menu mobile
  var btn = document.getElementById("menu-btn"), nav = document.getElementById("nav");
  if (btn && nav) btn.addEventListener("click", function () {
    var o = nav.classList.toggle("ouvert");
    btn.setAttribute("aria-expanded", o ? "true" : "false");
  });

  // En-tête réduit et bouton « haut » au défilement
  var entete = document.querySelector(".entete"), haut = document.getElementById("haut");
  function surDefilement() {
    var y = window.scrollY || 0;
    if (entete) entete.classList.toggle("reduit", y > 40);
    if (haut) haut.classList.toggle("visible", y > 700);
  }
  window.addEventListener("scroll", surDefilement, { passive: true }); surDefilement();
  if (haut) haut.addEventListener("click", function () { window.scrollTo({ top: 0, behavior: calme ? "auto" : "smooth" }); });

  // Carrousel de l'accueil (diapositives de l'ancien site, textes animés)
  var car = document.getElementById("carrousel");
  if (car) {
    var slides = car.querySelectorAll(".slide"), pts = car.querySelectorAll(".points button");
    var barre = car.querySelector(".carrousel-barre i"), k = 0, minut = null;
    var aller = function (n) {
      slides[k].classList.remove("actif"); slides[k].setAttribute("aria-hidden", "true"); pts[k].removeAttribute("aria-current");
      k = (n + slides.length) % slides.length;
      slides[k].classList.add("actif"); slides[k].setAttribute("aria-hidden", "false"); pts[k].setAttribute("aria-current", "true");
      relancer();
    };
    var relancer = function () {
      clearTimeout(minut);
      if (calme) return;
      barre.classList.remove("court"); void barre.offsetWidth; barre.classList.add("court");
      minut = setTimeout(function () { aller(k + 1); }, 7000);
    };
    pts.forEach(function (p, n) { p.addEventListener("click", function () { if (n !== k) aller(n); }); });
    car.querySelector(".prec").addEventListener("click", function () { aller(k - 1); });
    car.querySelector(".suiv").addEventListener("click", function () { aller(k + 1); });
    car.addEventListener("keydown", function (ev) { if (ev.key === "ArrowLeft") aller(k - 1); if (ev.key === "ArrowRight") aller(k + 1); });
    var x0 = null;
    car.addEventListener("touchstart", function (ev) { x0 = ev.touches[0].clientX; }, { passive: true });
    car.addEventListener("touchend", function (ev) { if (x0 === null) return; var dx = ev.changedTouches[0].clientX - x0; if (Math.abs(dx) > 50) aller(k + (dx < 0 ? 1 : -1)); x0 = null; });
    relancer();
  }

  // Compteurs animés
  function compter(el) {
    var fin = +el.getAttribute("data-compte"), t0 = null, d = 1200;
    if (calme || !fin) return;
    var pas = function (t) { if (!t0) t0 = t; var k = Math.min(1, (t - t0) / d); el.textContent = Math.round(fin * (1 - Math.pow(1 - k, 3))); if (k < 1) requestAnimationFrame(pas); };
    el.textContent = "0"; requestAnimationFrame(pas);
  }

  // Apparitions au défilement : seuls les éléments hors écran au chargement sont masqués
  var cibles = document.querySelectorAll(".titre-section, .coupe, .service, .etapes li, .apercu-projets a, .projet, .vignette, .temoin, .clients li, .engagements li, .cartes-contact > div, .valeur, .faq details, .chiffres > div, .encadre, .extrait, .contenu > *, .coordonnees > div, .formulaire, .deux-col > *");
  if ("IntersectionObserver" in window && !calme) {
    var obs = new IntersectionObserver(function (entrees) {
      entrees.forEach(function (en) {
        if (!en.isIntersecting) return;
        var el = en.target; obs.unobserve(el);
        el.classList.add("rv-vu"); el.classList.remove("rv-cache");
        if (el.classList.contains("extrait")) el.classList.add("vu");
        if (el.classList.contains("coupe")) el.classList.add("anime");
        el.querySelectorAll("[data-compte]").forEach(compter);
        if (el.hasAttribute("data-compte")) compter(el);
      });
    }, { rootMargin: "0px 0px -8% 0px" });
    var h = window.innerHeight;
    cibles.forEach(function (el) {
      var r = el.getBoundingClientRect();
      if (r.top > h) {
        var freres = el.parentElement ? Array.prototype.indexOf.call(el.parentElement.children, el) : 0;
        el.style.setProperty("--rv-delai", (Math.min(freres, 6) * 0.07) + "s");
        el.classList.add("rv-cache");
      } else {
        if (el.classList.contains("extrait")) el.classList.add("vu");
      }
      obs.observe(el);
    });
  } else {
    document.querySelectorAll(".extrait").forEach(function (x) { x.classList.add("vu"); });
  }

  // Filtres des projets (délégation : marche aussi pour les projets chargés depuis data/projets.json)
  document.addEventListener("click", function (ev) {
    var b = ev.target.closest(".filtres button"); if (!b) return;
    var grp = b.closest(".filtres"), f = b.getAttribute("data-f");
    grp.querySelectorAll("button").forEach(function (x) { x.setAttribute("aria-pressed", x === b ? "true" : "false"); });
    document.querySelectorAll(".projet, .vignette").forEach(function (p) {
      var ok = f === "tous" || p.getAttribute("data-cat") === f;
      p.hidden = !ok;
      if (ok && !calme) { p.classList.remove("rv-vu"); p.classList.add("rv-cache"); requestAnimationFrame(function () { requestAnimationFrame(function () { p.classList.add("rv-vu"); p.classList.remove("rv-cache"); }); }); }
    });
  });

  // Visionneuse des photos (la liste des photos est relue à chaque ouverture)
  var SEL_PHOTOS = ".projet .galerie img, .vignette img, .contenu .visuels img, .coupe-vue > img:first-child";
  var v = document.createElement("div");
  v.className = "visionneuse"; v.hidden = true; v.setAttribute("role", "dialog"); v.setAttribute("aria-modal", "true"); v.setAttribute("aria-label", "Photo");
  v.innerHTML = '<img alt=""><p></p><button class="fermer" type="button" aria-label="Fermer">×</button><button class="prec" type="button" aria-label="Photo précédente">‹</button><button class="suiv" type="button" aria-label="Photo suivante">›</button>';
  document.body.appendChild(v);
  var vi = v.querySelector("img"), vp = v.querySelector("p"), photos = [], cour = 0, retour = null;
  var ouvrir = function (n) {
    cour = (n + photos.length) % photos.length;
    vi.src = photos[cour].currentSrc || photos[cour].src; vi.alt = photos[cour].alt; vp.textContent = photos[cour].alt;
    vi.style.animation = "none"; void vi.offsetWidth; vi.style.animation = "";
    if (v.hidden) { retour = document.activeElement; v.hidden = false; v.querySelector(".fermer").focus(); }
  };
  var fermer = function () { v.hidden = true; if (retour) retour.focus(); };
  var depuis = function (img) {
    photos = Array.prototype.filter.call(document.querySelectorAll(SEL_PHOTOS), function (p) { return !p.closest("[hidden]"); });
    var n = photos.indexOf(img); if (n >= 0) ouvrir(n);
  };
  document.addEventListener("click", function (e) { var img = e.target.closest && e.target.closest(SEL_PHOTOS); if (img && !img.closest(".visionneuse")) depuis(img); });
  document.addEventListener("keydown", function (e) {
    if (!v.hidden) { if (e.key === "Escape") fermer(); else if (e.key === "ArrowLeft") ouvrir(cour - 1); else if (e.key === "ArrowRight") ouvrir(cour + 1); return; }
    if (e.key === "Enter" && e.target.matches && e.target.matches(SEL_PHOTOS)) depuis(e.target);
  });
  var rendreFocusables = function () { document.querySelectorAll(SEL_PHOTOS).forEach(function (p) { p.tabIndex = 0; }); };
  rendreFocusables(); document.addEventListener("projets-charges", rendreFocusables);
  v.querySelector(".fermer").addEventListener("click", fermer);
  v.querySelector(".prec").addEventListener("click", function () { ouvrir(cour - 1); });
  v.querySelector(".suiv").addEventListener("click", function () { ouvrir(cour + 1); });
  v.addEventListener("click", function (e) { if (e.target === v) fermer(); });

  // Newsletter
  var lettre = document.getElementById("lettre");
  if (lettre) lettre.addEventListener("submit", function (ev) {
    ev.preventDefault();
    var etat = lettre.querySelector(".message-etat");
    etat.textContent = "Inscription en cours…";
    fetch(lettre.getAttribute("data-url"), { method: "POST", body: new FormData(lettre) })
      .then(function () { etat.textContent = "Merci, votre inscription est enregistrée."; lettre.reset(); })
      .catch(function () { etat.textContent = "L'inscription a échoué. Écrivez-nous à sigma.icc@gmail.com."; });
  });

  // Formulaire de devis : envoi vers la feuille Google existante, puis page de confirmation
  document.querySelectorAll("form.formulaire[data-url]").forEach(function (form) {
    form.addEventListener("submit", function (ev) {
      ev.preventDefault();
      var etat = form.querySelector(".message-etat"), bouton = form.querySelector("button[type=submit]");
      if (bouton) bouton.disabled = true;
      if (etat) etat.textContent = "Envoi en cours…";
      fetch(form.getAttribute("data-url"), { method: "POST", body: new FormData(form) })
        .then(function () { window.location.href = "demande-envoye.html"; })
        .catch(function () {
          if (bouton) bouton.disabled = false;
          if (etat) etat.textContent = "L'envoi a échoué. Écrivez-nous à sigma.icc@gmail.com ou appelez le +212 6 61 05 74 55.";
        });
    });
  });
})();
