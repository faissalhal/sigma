/* SIGMA ICC – administration des projets.
   Le site est publié par GitHub Pages : cette page lit et enregistre data/projets.json et les photos
   directement dans le dépôt GitHub, avec un jeton personnel saisi par l'administrateur.
   Le jeton n'est jamais écrit dans le code du site. */
(function () {
  "use strict";
  var DEPOT = "faissalhal/sigma", BRANCHE = "main", FICHIER = "data/projets.json", DOSSIER_PHOTOS = "images/projects/";
  var API = "https://api.github.com/repos/" + DEPOT + "/contents/";
  var CLE_JETON = "sigma-admin-jeton";
  var $ = function (s) { return document.querySelector(s); };
  var esc = function (s) { return String(s == null ? "" : s).replace(/[&<>"']/g, function (c) { return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c]; }); };
  var slug = function (s) { return String(s || "").toLowerCase().normalize("NFD").replace(/[̀-ͯ]/g, "").replace(/[^a-z0-9]+/g, "-").replace(/^-|-$/g, "").slice(0, 40) || "projet"; };

  var jeton = "", projets = [], sha = null, edition = null, nouvellesPhotos = [], photosGardees = [];

  function etat(msg, type) { var e = $("#a-etat"); e.textContent = msg; e.className = "a-etat " + (type || ""); }
  function b64DepuisTexte(t) { var o = new TextEncoder().encode(t), s = ""; for (var i = 0; i < o.length; i += 0x8000) s += String.fromCharCode.apply(null, o.subarray(i, i + 0x8000)); return btoa(s); }
  function texteDepuisB64(b) { var s = atob(b.replace(/\n/g, "")), o = new Uint8Array(s.length); for (var i = 0; i < s.length; i++) o[i] = s.charCodeAt(i); return new TextDecoder().decode(o); }
  function gh(chemin, opts) {
    opts = opts || {};
    return fetch(chemin.indexOf("http") === 0 ? chemin : API + chemin, {
      method: opts.method || "GET",
      headers: { "Authorization": "Bearer " + jeton, "Accept": "application/vnd.github+json", "X-GitHub-Api-Version": "2022-11-28" },
      body: opts.body ? JSON.stringify(opts.body) : undefined, cache: "no-store"
    }).then(function (r) {
      return r.json().catch(function () { return {}; }).then(function (j) {
        if (!r.ok) { var e = new Error(j.message || ("Erreur " + r.status)); e.status = r.status; throw e; }
        return j;
      });
    });
  }

  // ------------------------------------------------------------ connexion
  try { var j0 = localStorage.getItem(CLE_JETON); if (j0) { $("#a-jeton").value = j0; $("#a-retenir").checked = true; } } catch (e) { }
  $("#a-connexion").addEventListener("submit", function (ev) {
    ev.preventDefault();
    jeton = $("#a-jeton").value.trim();
    if (!jeton) return;
    etat("Connexion à GitHub…");
    gh("https://api.github.com/repos/" + DEPOT).then(function (r) {
      if (!r.permissions || !r.permissions.push) throw new Error("Ce jeton peut lire le dépôt mais pas y écrire. Donnez-lui la permission « Contents : Read and write ».");
      try { if ($("#a-retenir").checked) localStorage.setItem(CLE_JETON, jeton); else localStorage.removeItem(CLE_JETON); } catch (e) { }
      return charger();
    }).then(function () {
      $("#a-connexion").hidden = true; $("#a-espace").hidden = false; $("#a-deconnexion").hidden = false;
      etat("Connecté au dépôt " + DEPOT + ".", "ok");
    }).catch(function (e) {
      etat(e.status === 401 ? "Jeton refusé par GitHub : vérifiez-le ou créez-en un nouveau." : e.status === 404 ? "Dépôt introuvable avec ce jeton : il doit donner accès à " + DEPOT + "." : e.message, "err");
    });
  });
  $("#a-deconnexion").addEventListener("click", function () {
    jeton = ""; try { localStorage.removeItem(CLE_JETON); } catch (e) { }
    $("#a-jeton").value = ""; $("#a-retenir").checked = false;
    $("#a-espace").hidden = true; $("#a-connexion").hidden = false; this.hidden = true; etat("Déconnecté. Le jeton a été effacé de cet appareil.");
  });

  function charger() {
    return gh(FICHIER + "?ref=" + BRANCHE).then(function (f) {
      sha = f.sha; projets = JSON.parse(texteDepuisB64(f.content)); rendreListe(); remplirCategories();
    }).catch(function (e) {
      if (e.status === 404) { sha = null; projets = []; rendreListe(); remplirCategories(); return; }
      throw e;
    });
  }

  // ------------------------------------------------------------ liste
  function rendreListe() {
    $("#a-nb").textContent = projets.length + " projet" + (projets.length > 1 ? "s" : "");
    $("#a-liste").innerHTML = projets.map(function (p, i) {
      var img = p.img && p.img[0] ? '<img src="' + esc(p.img[0]) + '?v=' + Date.now() + '" alt="">' : '<span class="a-sans">Pas de photo</span>';
      return '<li class="a-projet' + (p.masque ? " masque" : "") + '" data-i="' + i + '">' + img +
        '<div><b>' + esc(p.titre) + '</b><span>' + esc(p.catlib) + (p.lieu ? " · " + esc(p.lieu) : "") + (p.annee ? " · " + esc(p.annee) : "") + (p.masque ? " · <em>masqué</em>" : "") + " · " + (p.img ? p.img.length : 0) + " photo(s)</span></div>" +
        '<div class="a-btns">' +
        '<button type="button" class="ic" data-a="haut" aria-label="Monter"' + (i === 0 ? " disabled" : "") + '>↑</button>' +
        '<button type="button" class="ic" data-a="bas" aria-label="Descendre"' + (i === projets.length - 1 ? " disabled" : "") + '>↓</button>' +
        '<button type="button" class="btn petit secondaire" data-a="modifier">Modifier</button>' +
        '<button type="button" class="btn petit secondaire" data-a="masquer">' + (p.masque ? "Afficher" : "Masquer") + '</button>' +
        '<button type="button" class="btn petit secondaire danger" data-a="supprimer">Supprimer</button></div></li>';
    }).join("") || '<li class="a-vide">Aucun projet pour l\'instant.</li>';
  }
  var aConfirmer = null;
  $("#a-liste").addEventListener("click", function (ev) {
    var b = ev.target.closest("button[data-a]"); if (!b) return;
    var i = +b.closest("li").getAttribute("data-i"), a = b.getAttribute("data-a"), p = projets[i];
    if (a === "modifier") return ouvrirFormulaire(i);
    if (a === "haut" || a === "bas") {
      var j = a === "haut" ? i - 1 : i + 1; projets.splice(j, 0, projets.splice(i, 1)[0]);
      return publier("Ordre des projets modifié");
    }
    if (a === "masquer") { p.masque = !p.masque; return publier((p.masque ? "Projet masqué : " : "Projet affiché : ") + p.titre); }
    if (a === "supprimer") {
      if (aConfirmer !== b) { aConfirmer = b; b.textContent = "Confirmer ?"; setTimeout(function () { if (aConfirmer === b) { aConfirmer = null; b.textContent = "Supprimer"; } }, 4000); return; }
      aConfirmer = null; projets.splice(i, 1); return publier("Projet supprimé : " + p.titre);
    }
  });

  // ------------------------------------------------------------ formulaire
  function remplirCategories() {
    var vus = {}, opts = [];
    projets.forEach(function (p) { if (!vus[p.cat]) { vus[p.cat] = 1; opts.push('<option value="' + esc(p.cat) + '">' + esc(p.catlib) + "</option>"); } });
    $("#f-cat").innerHTML = opts.join("") + '<option value="__nouvelle">Nouvelle catégorie…</option>';
    majCat();
  }
  function majCat() { $("#f-cat-nouvelle-zone").hidden = $("#f-cat").value !== "__nouvelle"; }
  $("#f-cat").addEventListener("change", majCat);

  function ouvrirFormulaire(i) {
    edition = i == null ? null : i;
    var p = edition == null ? {} : projets[edition];
    $("#a-form-titre").textContent = edition == null ? "Ajouter un projet" : "Modifier : " + p.titre;
    ["titre", "texte", "client", "lieu", "surface", "annee", "moe"].forEach(function (k) { $("#f-" + k).value = p[k] || ""; });
    if (p.cat) $("#f-cat").value = p.cat; else if ($("#f-cat").options.length > 1) $("#f-cat").selectedIndex = 0;
    $("#f-cat-nouvelle").value = ""; majCat();
    photosGardees = (p.img || []).slice(); nouvellesPhotos = []; $("#f-photos").value = "";
    rendrePhotos();
    $("#a-formulaire").hidden = false; $("#a-formulaire").scrollIntoView({ behavior: "smooth" }); $("#f-titre").focus();
  }
  $("#a-ajouter").addEventListener("click", function () { ouvrirFormulaire(null); });
  $("#f-annuler").addEventListener("click", function () { $("#a-formulaire").hidden = true; edition = null; });

  function rendrePhotos() {
    var h = photosGardees.map(function (src, k) { return '<figure data-g="' + k + '"><img src="' + esc(src) + '" alt=""><button type="button" class="ic" aria-label="Retirer la photo">✕</button></figure>'; }).join("");
    h += nouvellesPhotos.map(function (ph, k) { return '<figure data-n="' + k + '" class="nouvelle"><img src="' + ph.url + '" alt=""><button type="button" class="ic" aria-label="Retirer la photo">✕</button><span>nouvelle</span></figure>'; }).join("");
    $("#f-apercu").innerHTML = h || '<p class="ch-note">Aucune photo. Ajoutez-en au moins une.</p>';
  }
  $("#f-apercu").addEventListener("click", function (ev) {
    var b = ev.target.closest("button"); if (!b) return;
    var f = b.closest("figure");
    if (f.hasAttribute("data-g")) photosGardees.splice(+f.getAttribute("data-g"), 1);
    else nouvellesPhotos.splice(+f.getAttribute("data-n"), 1);
    rendrePhotos();
  });
  // Les photos sont réduites dans le navigateur (1600 px max, JPEG) avant l'envoi
  $("#f-photos").addEventListener("change", function () {
    var fichiers = Array.prototype.slice.call(this.files || []);
    Promise.all(fichiers.map(reduire)).then(function (res) { nouvellesPhotos = nouvellesPhotos.concat(res.filter(Boolean)); rendrePhotos(); });
    this.value = "";
  });
  function reduire(f) {
    return new Promise(function (ok) {
      if (!/^image\//.test(f.type)) return ok(null);
      var url = URL.createObjectURL(f), img = new Image();
      img.onload = function () {
        var k = Math.min(1, 1600 / Math.max(img.naturalWidth, img.naturalHeight)), cv = document.createElement("canvas");
        cv.width = Math.round(img.naturalWidth * k); cv.height = Math.round(img.naturalHeight * k);
        var g = cv.getContext("2d"); g.fillStyle = "#fff"; g.fillRect(0, 0, cv.width, cv.height); g.drawImage(img, 0, 0, cv.width, cv.height);
        var d = cv.toDataURL("image/jpeg", 0.84); URL.revokeObjectURL(url);
        ok({ url: d, b64: d.split(",")[1] });
      };
      img.onerror = function () { ok(null); };
      img.src = url;
    });
  }

  $("#a-formulaire").addEventListener("submit", function (ev) {
    ev.preventDefault();
    var titre = $("#f-titre").value.trim(), texte = $("#f-texte").value.trim();
    var cat = $("#f-cat").value, catlib;
    if (cat === "__nouvelle") { catlib = $("#f-cat-nouvelle").value.trim(); if (!catlib) { etat("Donnez un nom à la nouvelle catégorie.", "err"); return; } cat = slug(catlib); }
    else catlib = $("#f-cat").selectedOptions[0].textContent;
    if (!titre || !texte) { etat("Le titre et la description sont obligatoires.", "err"); return; }
    if (!photosGardees.length && !nouvellesPhotos.length) { etat("Ajoutez au moins une photo.", "err"); return; }
    var p = edition == null ? { id: slug(titre) + "-" + Date.now().toString(36) } : projets[edition];
    Object.assign(p, { cat: cat, catlib: catlib, titre: titre, texte: texte,
      client: $("#f-client").value.trim(), lieu: $("#f-lieu").value.trim(), surface: $("#f-surface").value.trim(),
      annee: $("#f-annee").value.trim(), moe: $("#f-moe").value.trim() });
    var bouton = $("#f-enregistrer"); bouton.disabled = true;
    var base = slug(titre).slice(0, 30) + "-" + Date.now().toString(36), chemins = [];
    var envoi = nouvellesPhotos.reduce(function (pr, ph, k) {
      return pr.then(function () {
        var chemin = DOSSIER_PHOTOS + base + "-" + (k + 1) + ".jpg";
        etat("Envoi de la photo " + (k + 1) + " sur " + nouvellesPhotos.length + "…");
        return gh(chemin, { method: "PUT", body: { message: "Admin : photo du projet " + titre, content: ph.b64, branch: BRANCHE } }).then(function () { chemins.push(chemin); });
      });
    }, Promise.resolve());
    envoi.then(function () {
      p.img = photosGardees.concat(chemins);
      if (edition == null) projets.unshift(p);
      return publier((edition == null ? "Projet ajouté : " : "Projet modifié : ") + titre);
    }).then(function (ok) {
      bouton.disabled = false;
      if (ok) { $("#a-formulaire").hidden = true; edition = null; nouvellesPhotos = []; }
    }).catch(function (e) { bouton.disabled = false; etat("Échec de l'envoi des photos : " + e.message, "err"); });
  });

  // ------------------------------------------------------------ publication de data/projets.json
  function publier(message) {
    etat("Publication sur GitHub…");
    var corps = { message: "Admin : " + message, content: b64DepuisTexte(JSON.stringify(projets, null, 2) + "\n"), branch: BRANCHE };
    if (sha) corps.sha = sha;
    return gh(FICHIER, { method: "PUT", body: corps }).then(function (r) {
      sha = r.content.sha; rendreListe(); remplirCategories();
      etat(message + ". Publié : le site sera à jour dans 1 à 2 minutes.", "ok");
      return true;
    }).catch(function (e) {
      if (e.status === 409) { etat("Le fichier a changé ailleurs entre-temps. Rechargement de la liste : refaites votre modification.", "err"); return charger().then(function () { return false; }); }
      etat("Publication impossible : " + e.message, "err"); return charger().then(function () { return false; });
    });
  }
})();
