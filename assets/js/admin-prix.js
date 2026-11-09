/* SIGMA ICC – administration des prix du chiffrage (assets/js/donnees-prix.js).
   Lit le fichier sur GitHub, permet de modifier désignations, unités, prix d'achat par devise, temps de pose,
   fourchettes au m² par pays et coefficients par type de projet, puis publie le fichier. */
(function () {
  "use strict";
  var FICHIER = "assets/js/donnees-prix.js";
  var $ = function (s) { return document.querySelector(s); };
  var esc = function (s) { return String(s == null ? "" : s).replace(/[&<>"']/g, function (c) { return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c]; }); };
  var num = function (v) { var t = String(v == null ? "" : v).replace(/\s/g, "").replace(",", "."); if (t === "") return null; var n = Number(t); return isNaN(n) ? NaN : n; };
  var fmt = function (n) { return n == null ? "" : String(n).replace(".", ","); };
  var A, REF = null, ORIG = null, sha = null, entete = "", modifs = [];

  // onglets Projets / Prix
  function onglet(n) {
    ["projets", "prix"].forEach(function (k) { $("#t-" + k).setAttribute("aria-selected", k === n ? "true" : "false"); $("#a-tab-" + k).hidden = k !== n; });
    if (n === "prix" && !REF) charger();
  }
  $("#t-projets").addEventListener("click", function () { onglet("projets"); });
  $("#t-prix").addEventListener("click", function () { onglet("prix"); });
  document.addEventListener("admin-connecte", function () { A = window.SigmaAdmin; });

  function charger() {
    A = window.SigmaAdmin; if (!A) return;
    A.etat("Chargement des prix…");
    return A.gh(FICHIER + "?ref=" + A.BRANCHE).then(function (f) {
      sha = f.sha;
      var t = A.texte(f.content), i = t.indexOf("window.SIGMA_PRIX");
      entete = t.slice(0, i);
      var json = t.slice(t.indexOf("{", i), t.lastIndexOf("}") + 1);
      REF = JSON.parse(json); ORIG = JSON.parse(json); modifs = [];
      remplirFiltres(); rendre(); rendreAvance(); majModifs();
      A.etat("Prix chargés : " + REF.articles.length + " ouvrages, " + REF.devises.length + " devises.", "ok");
    }).catch(function (e) { A.etat("Impossible de charger les prix : " + e.message, "err"); });
  }

  var LIBLOT = {};
  function remplirFiltres() {
    REF.lots.forEach(function (l) { LIBLOT[l.code] = l.lib; });
    var dv = $("#p-devise").value;
    $("#p-devise").innerHTML = REF.devises.map(function (d) { return '<option value="' + d.code + '">' + d.code + " – " + esc(d.nom) + "</option>"; }).join("");
    $("#p-devise").value = dv || "MAD";
    var lt = $("#p-lot").value;
    $("#p-lot").innerHTML = REF.lots.map(function (l) { return '<option value="' + l.code + '">' + l.code + " " + esc(l.lib) + "</option>"; }).join("");
    $("#p-lot").value = lt || "L15";
    remplirBlocs();
  }
  function remplirBlocs() {
    var lot = $("#p-lot").value;
    $("#pa-bloc").innerHTML = REF.blocs.filter(function (b) { return b.lot === lot; }).map(function (b) { return '<option value="' + b.code + '">' + b.code + " " + esc(b.lib) + "</option>"; }).join("");
  }
  function blocsDuLot(lot) { var s = {}; REF.blocs.forEach(function (b) { if (b.lot === lot) s[b.code] = b; }); return s; }

  function rendre() {
    var dv = $("#p-devise").value, lot = $("#p-lot").value, q = $("#p-cherche").value.trim().toLowerCase();
    var B = blocsDuLot(lot), h = "", bloc = null, n = 0;
    REF.articles.forEach(function (a) {
      if (q) { if ((a.des + " " + a.ref).toLowerCase().indexOf(q) < 0) return; }
      else if (!B[a.bloc]) return;
      if (a.bloc !== bloc) { bloc = a.bloc; var bi = REF.blocs.find(function (x) { return x.code === bloc; }); h += '<tr class="bloc"><td colspan="6">' + esc(bi ? bi.lib : bloc) + "<span>" + esc(bloc) + "</span></td></tr>"; }
      var o = ORIG.articles.find(function (x) { return x.ref === a.ref; });
      var change = !o || o.des !== a.des || o.u !== a.u || o.h !== a.h || o.p[dv] !== a.p[dv];
      h += '<tr data-ref="' + esc(a.ref) + '"' + (change ? ' class="saisi"' : "") + '><td class="u" data-l="Réf.">' + esc(a.ref) + "</td>" +
        '<td data-l="Désignation"><input class="p-des" value="' + esc(a.des) + '" aria-label="Désignation"></td>' +
        '<td data-l="Unité"><input class="p-u" value="' + esc(a.u) + '" aria-label="Unité"></td>' +
        '<td class="n" data-l="Prix d\'achat HT"><input class="p-pu" value="' + fmt(a.p[dv]) + '" inputmode="decimal" aria-label="Prix d\'achat HT"></td>' +
        '<td class="n" data-l="Temps (h)"><input class="p-h" value="' + fmt(a.h) + '" inputmode="decimal" aria-label="Temps de pose"></td>' +
        '<td class="act"><button type="button" class="ic" data-a="suppr" title="Supprimer l\'ouvrage" aria-label="Supprimer l\'ouvrage">✕</button></td></tr>';
      n++;
    });
    $("#p-lignes").innerHTML = h || '<tr><td colspan="6" class="ch-vide">Aucun ouvrage.</td></tr>';
    $("#p-info").textContent = n + " ouvrage" + (n > 1 ? "s" : "") + (q ? " trouvés" : " dans ce lot") + " · prix en " + dv;
  }
  ["#p-devise", "#p-lot"].forEach(function (s) { $(s).addEventListener("change", function () { if (s === "#p-lot") remplirBlocs(); rendre(); }); });
  var minut; $("#p-cherche").addEventListener("input", function () { clearTimeout(minut); minut = setTimeout(rendre, 200); });

  function noter(texte) { modifs.push(texte); majModifs(); }
  function majModifs() {
    $("#p-publier").disabled = !modifs.length; $("#p-annuler").disabled = !modifs.length;
    $("#p-modifs").innerHTML = modifs.length ? "<h3>" + modifs.length + " modification(s) en attente</h3><ul>" + modifs.slice(-30).map(function (m) { return "<li>" + esc(m) + "</li>"; }).join("") + "</ul>" : "";
  }

  $("#p-lignes").addEventListener("change", function (ev) {
    var inp = ev.target, tr = inp.closest("tr"); if (!tr || !tr.dataset.ref) return;
    var a = REF.articles.find(function (x) { return x.ref === tr.dataset.ref; }), dv = $("#p-devise").value;
    if (inp.classList.contains("p-des")) { var v = inp.value.trim(); if (!v) { inp.value = a.des; return; } a.des = v; noter(a.ref + " : désignation modifiée"); }
    if (inp.classList.contains("p-u")) { a.u = inp.value.trim() || a.u; noter(a.ref + " : unité " + a.u); }
    if (inp.classList.contains("p-pu")) {
      var n = num(inp.value);
      if (n === null) { delete a.p[dv]; noter(a.ref + " : prix " + dv + " retiré"); }
      else if (isNaN(n) || n < 0) { A.etat("Prix invalide pour " + a.ref + ".", "err"); inp.value = fmt(a.p[dv]); return; }
      else { var av = a.p[dv]; a.p[dv] = n; noter(a.ref + " : prix " + dv + " " + (av == null ? "–" : fmt(av)) + " → " + fmt(n)); }
    }
    if (inp.classList.contains("p-h")) { var hh = num(inp.value); if (hh == null || isNaN(hh) || hh < 0) { inp.value = fmt(a.h); return; } a.h = hh; noter(a.ref + " : temps " + fmt(hh) + " h"); }
    tr.classList.add("saisi");
  });
  var aConfirmer = null;
  $("#p-lignes").addEventListener("click", function (ev) {
    var b = ev.target.closest("button[data-a=suppr]"); if (!b) return;
    if (aConfirmer !== b) { aConfirmer = b; b.textContent = "?"; b.title = "Cliquer encore pour confirmer"; setTimeout(function () { if (aConfirmer === b) { aConfirmer = null; b.textContent = "✕"; } }, 4000); return; }
    var ref = b.closest("tr").dataset.ref;
    REF.articles = REF.articles.filter(function (x) { return x.ref !== ref; });
    REF.exemple.lines = REF.exemple.lines.filter(function (l) { return l.ref !== ref; });
    noter(ref + " : ouvrage supprimé"); rendre();
  });

  $("#p-ajout").addEventListener("submit", function (ev) {
    ev.preventDefault();
    var bloc = $("#pa-bloc").value, dv = $("#p-devise").value, pu = num($("#pa-pu").value), h = num($("#pa-h").value) || 0;
    if (pu == null || isNaN(pu) || pu < 0) { A.etat("Indiquez un prix d'achat valide.", "err"); return; }
    var prefixe = bloc.replace(/[^A-Z0-9]/gi, "").toUpperCase(), max = 0;
    REF.articles.forEach(function (a) { if (a.bloc === bloc) { var m = a.ref.match(/-(\d+)$/); if (m) max = Math.max(max, +m[1]); } });
    var ref = prefixe + "-" + String(max + 1).padStart(2, "0");
    while (REF.articles.some(function (a) { return a.ref === ref; })) ref += "b";
    var art = { ref: ref, des: $("#pa-des").value.trim(), bloc: bloc, u: $("#pa-u").value.trim() || "U", p: {}, h: h };
    art.p[dv] = pu;
    var dernier = -1; REF.articles.forEach(function (a, i) { if (a.bloc === bloc) dernier = i; });
    REF.articles.splice(dernier + 1, 0, art);
    noter(ref + " : ouvrage ajouté (" + art.des + ", " + fmt(pu) + " " + dv + ")");
    $("#pa-des").value = ""; $("#pa-pu").value = ""; $("#pa-h").value = "0";
    rendre();
    A.etat("Ouvrage " + ref + " ajouté. Pensez à saisir son prix dans les autres devises si besoin.", "ok");
  });

  // fourchettes au m² par pays, coefficients par type
  var CHAMPS = ["taux", "eMin", "eMax", "mMin", "mMax", "hMin", "hMax"];
  function rendreAvance() {
    $("#p-pays").innerHTML = REF.pays.map(function (p, i) {
      return '<tr data-i="' + i + '"><td>' + esc(p.pays) + "</td><td>" + p.devise + "</td>" + CHAMPS.map(function (c) { return '<td class="n"><input data-c="' + c + '" value="' + fmt(p[c]) + '" inputmode="decimal" aria-label="' + c + " " + esc(p.pays) + '"></td>'; }).join("") + "</tr>";
    }).join("");
    $("#p-types").innerHTML = (REF.typesProjet || []).map(function (t, i) {
      return '<tr data-t="' + i + '"><td>' + esc(t.nom) + '</td><td class="n"><input value="' + fmt(t.k) + '" inputmode="decimal" aria-label="Coefficient ' + esc(t.nom) + '"></td></tr>';
    }).join("");
  }
  $("#p-pays").addEventListener("change", function (ev) {
    var inp = ev.target, i = +inp.closest("tr").dataset.i, c = inp.dataset.c, n = num(inp.value);
    if (n == null || isNaN(n) || n < 0) { inp.value = fmt(REF.pays[i][c]); return; }
    REF.pays[i][c] = n; noter(REF.pays[i].pays + " : " + c + " = " + fmt(n));
  });
  $("#p-types").addEventListener("change", function (ev) {
    var inp = ev.target, i = +inp.closest("tr").dataset.t, n = num(inp.value);
    if (n == null || isNaN(n) || n <= 0) { inp.value = fmt(REF.typesProjet[i].k); return; }
    REF.typesProjet[i].k = n; noter(REF.typesProjet[i].nom + " : coefficient " + fmt(n));
  });

  $("#p-annuler").addEventListener("click", function () { REF = JSON.parse(JSON.stringify(ORIG)); modifs = []; rendre(); rendreAvance(); majModifs(); A.etat("Modifications annulées."); });
  $("#p-publier").addEventListener("click", function () {
    var b = this; b.disabled = true; A.etat("Publication des prix…");
    var contenu = entete + "window.SIGMA_PRIX = " + JSON.stringify(REF) + ";\n";
    var msg = "Admin : prix du chiffrage (" + modifs.length + " modification" + (modifs.length > 1 ? "s" : "") + ")\n\n" + modifs.slice(0, 40).join("\n");
    A.gh(FICHIER, { method: "PUT", body: { message: msg, content: A.b64(contenu), sha: sha, branch: A.BRANCHE } }).then(function (r) {
      sha = r.content.sha; ORIG = JSON.parse(JSON.stringify(REF)); modifs = []; majModifs(); rendre();
      A.etat("Prix publiés. L'outil de chiffrage sera à jour dans 1 à 2 minutes.", "ok");
    }).catch(function (e) {
      b.disabled = false;
      A.etat(e.status === 409 ? "Le fichier des prix a changé ailleurs entre-temps. Rechargez la page avant de recommencer (vos modifications non publiées seront perdues)." : "Publication impossible : " + e.message, "err");
    });
  });
})();
