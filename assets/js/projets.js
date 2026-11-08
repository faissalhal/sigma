/* SIGMA ICC – projets chargés depuis data/projets.json (géré depuis admin.html).
   La page contient déjà une version statique des projets : si le fichier se charge, elle est remplacée. */
(function () {
  "use strict";
  var liste = document.getElementById("liste-projets"), galerie = document.getElementById("galerie-accueil");
  var filtres = document.querySelectorAll(".filtres[data-projets]");
  if (!liste && !galerie) return;
  var esc = function (s) { return String(s == null ? "" : s).replace(/[&<>"']/g, function (c) { return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c]; }); };

  function carte(p) {
    var imgs = (p.img || []).map(function (src, n) { return '<img src="' + esc(src) + '" alt="' + esc(p.titre) + ", photo " + (n + 1) + '" loading="lazy" width="750" height="600">'; }).join("");
    var champs = [["Client", p.client], ["Localisation", p.lieu], ["Surface", p.surface ? p.surface + " m²" : ""], ["Année complétée", p.annee], ["Maîtrise d'œuvre", p.moe]];
    var dl = champs.filter(function (c) { return c[1]; }).map(function (c) { return "<dt>" + c[0] + "</dt><dd>" + esc(c[1]) + "</dd>"; }).join("");
    return '<article class="projet" data-cat="' + esc(p.cat) + '" id="' + esc(p.id) + '"><div class="galerie">' + imgs + '</div><div class="infos">' +
      '<span class="etiquette">' + esc(p.catlib) + "</span><h3>" + esc(p.titre) + "</h3><p>" + esc(p.texte) + "</p><dl>" + dl + "</dl></div></article>";
  }
  function vignettes(p) {
    return (p.img || []).map(function (src) {
      return '<figure class="vignette" data-cat="' + esc(p.cat) + '"><img src="' + esc(src) + '" alt="' + esc(p.titre) + '" loading="lazy" width="750" height="600">' +
        '<figcaption><b>' + esc(p.catlib) + '</b><a href="projects.html#' + esc(p.id) + '">Plus d\'info</a></figcaption></figure>';
    }).join("");
  }
  function boutons(P) {
    var vus = {}, h = '<button type="button" data-f="tous" aria-pressed="true">Afficher tout</button>';
    P.forEach(function (p) { if (!vus[p.cat]) { vus[p.cat] = 1; h += '<button type="button" data-f="' + esc(p.cat) + '" aria-pressed="false">' + esc(p.catlib) + "</button>"; } });
    return h;
  }

  fetch("data/projets.json?v=" + Date.now(), { cache: "no-store" })
    .then(function (r) { if (!r.ok) throw new Error(r.status); return r.json(); })
    .then(function (P) {
      if (!Array.isArray(P) || !P.length) return;
      P = P.filter(function (p) { return !p.masque; });
      if (liste) liste.innerHTML = P.map(carte).join("");
      if (galerie) galerie.innerHTML = P.map(vignettes).join("");
      filtres.forEach(function (f) { f.innerHTML = boutons(P); });
      document.dispatchEvent(new Event("projets-charges"));
      if (location.hash) { var c = document.getElementById(location.hash.slice(1)); if (c) c.scrollIntoView(); }
    })
    .catch(function () { /* la version statique reste affichée */ });
})();
