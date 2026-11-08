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

  // Diaporama de l'accueil
  var diapo = document.getElementById("diapo");
  if (diapo) {
    var imgs = diapo.querySelectorAll(".diapo img"), points = diapo.querySelectorAll(".diapo-points button");
    var barre = diapo.querySelector(".diapo-barre i"), cart = diapo.querySelector(".cartouche"), i = 0, minut = null;
    var montrer = function (n) {
      imgs[i].classList.remove("actif"); points[i].removeAttribute("aria-current");
      i = (n + imgs.length) % imgs.length;
      imgs[i].classList.add("actif"); points[i].setAttribute("aria-current", "true");
      var t = (imgs[i].getAttribute("data-cartouche") || "").split("|");
      cart.classList.add("change");
      setTimeout(function () { cart.querySelectorAll("span[data-c]").forEach(function (s) { s.textContent = t[+s.getAttribute("data-c")] || ""; }); cart.classList.remove("change"); }, 300);
      relancer();
    };
    var relancer = function () {
      clearTimeout(minut);
      if (calme) return;
      barre.classList.remove("court"); void barre.offsetWidth; barre.classList.add("court");
      minut = setTimeout(function () { montrer(i + 1); }, 6000);
    };
    points.forEach(function (p, n) { p.addEventListener("click", function () { if (n !== i) montrer(n); }); });
    diapo.addEventListener("mouseenter", function () { clearTimeout(minut); barre.classList.remove("court"); });
    diapo.addEventListener("mouseleave", relancer);
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
  var cibles = document.querySelectorAll(".titre-section, .service, .etapes li, .apercu-projets a, .projet, .valeur, .faq details, .chiffres > div, .encadre, .extrait, .contenu > *, .coordonnees > div, .formulaire, .deux-col > *");
  if ("IntersectionObserver" in window && !calme) {
    var obs = new IntersectionObserver(function (entrees) {
      entrees.forEach(function (en) {
        if (!en.isIntersecting) return;
        var el = en.target; obs.unobserve(el);
        el.classList.add("rv-vu"); el.classList.remove("rv-cache");
        if (el.classList.contains("extrait")) el.classList.add("vu");
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

  // Filtres de la page Projets
  var filtres = document.querySelectorAll(".filtres button");
  filtres.forEach(function (b) {
    b.addEventListener("click", function () {
      var f = b.getAttribute("data-f");
      filtres.forEach(function (x) { x.setAttribute("aria-pressed", x === b ? "true" : "false"); });
      document.querySelectorAll(".projet").forEach(function (p) {
        var ok = f === "tous" || p.getAttribute("data-cat") === f;
        p.hidden = !ok;
        if (ok && !calme) { p.classList.remove("rv-vu"); p.classList.add("rv-cache"); requestAnimationFrame(function () { requestAnimationFrame(function () { p.classList.add("rv-vu"); p.classList.remove("rv-cache"); }); }); }
      });
    });
  });

  // Visionneuse des photos de projets
  var photos = Array.prototype.slice.call(document.querySelectorAll(".projet .galerie img"));
  if (photos.length) {
    var v = document.createElement("div");
    v.className = "visionneuse"; v.hidden = true; v.setAttribute("role", "dialog"); v.setAttribute("aria-modal", "true"); v.setAttribute("aria-label", "Photo du projet");
    v.innerHTML = '<img alt=""><p></p><button class="fermer" type="button" aria-label="Fermer">×</button><button class="prec" type="button" aria-label="Photo précédente">‹</button><button class="suiv" type="button" aria-label="Photo suivante">›</button>';
    document.body.appendChild(v);
    var vi = v.querySelector("img"), vp = v.querySelector("p"), cour = 0, retour = null;
    var ouvrir = function (n) {
      cour = (n + photos.length) % photos.length;
      vi.src = photos[cour].src; vi.alt = photos[cour].alt; vp.textContent = photos[cour].alt;
      vi.style.animation = "none"; void vi.offsetWidth; vi.style.animation = "";
      if (v.hidden) { retour = document.activeElement; v.hidden = false; v.querySelector(".fermer").focus(); }
    };
    var fermer = function () { v.hidden = true; if (retour) retour.focus(); };
    photos.forEach(function (p, n) { p.tabIndex = 0; p.addEventListener("click", function () { ouvrir(n); }); p.addEventListener("keydown", function (e) { if (e.key === "Enter") ouvrir(n); }); });
    v.querySelector(".fermer").addEventListener("click", fermer);
    v.querySelector(".prec").addEventListener("click", function () { ouvrir(cour - 1); });
    v.querySelector(".suiv").addEventListener("click", function () { ouvrir(cour + 1); });
    v.addEventListener("click", function (e) { if (e.target === v) fermer(); });
    document.addEventListener("keydown", function (e) {
      if (v.hidden) return;
      if (e.key === "Escape") fermer(); else if (e.key === "ArrowLeft") ouvrir(cour - 1); else if (e.key === "ArrowRight") ouvrir(cour + 1);
    });
  }

  // Formulaire de devis : envoi vers la feuille Google existante, puis page de confirmation
  document.querySelectorAll("form.formulaire").forEach(function (form) {
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
