/* SIGMA ICC – outil de chiffrage (estimation rapide et chiffrage détaillé)
   Calculs : assets/js/moteur.js (mêmes formules que le fichier de calcul Excel du bureau).
   Prix : assets/js/donnees-prix.js (Maroc, MAD, fourniture et pose). */
(function () {
  "use strict";
  var E = window.Engine, REF = window.SIGMA_PRIX;
  var $ = function (s) { return document.querySelector(s); };
  var esc = function (s) { return String(s == null ? "" : s).replace(/[&<>"']/g, function (c) { return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c]; }); };
  function fmt(n, d) {
    if (n == null || isNaN(n)) return "–";
    d = d || 0;
    var s = Math.abs(n).toFixed(d).split(".");
    s[0] = s[0].replace(/\B(?=(\d{3})+(?!\d))/g, " ");
    return (n < 0 ? "-" : "") + s[0] + (s[1] ? "," + s[1] : "");
  }
  var dh = function (n, d) { return fmt(n, d) + " DH"; };
  function mdh(n) { return n >= 1e6 ? fmt(n / 1e6, 2) + " M DH" : dh(Math.round(n / 1000) * 1000); }
  var parseNum = function (v) { var s = String(v == null ? "" : v).replace(/\s/g, "").replace(",", "."); if (s === "") return null; var n = Number(s); return isNaN(n) ? null : n; };

  // ------------------------------------------------------------ données
  var LOTS = REF.lots, BLOCS = {}, ART = {}, PAR_LOT = {};
  REF.blocs.forEach(function (b) { BLOCS[b.code] = b; });
  LOTS.forEach(function (l) { PAR_LOT[l.code] = []; });
  REF.articles.forEach(function (a) { ART[a.ref] = a; var b = BLOCS[a.bloc]; if (b && PAR_LOT[b.lot]) PAR_LOT[b.lot].push(a); });
  var LIB_LOT = {}; LOTS.forEach(function (l) { LIB_LOT[l.code] = l.lib; });

  var CLE = "sigma-chiffrage-v1";
  var etat = { type: "Villa", ville: "Marrakech", surface: 250, gamme: "Standard", q: {}, onglet: "rapide" };
  try { var sv = JSON.parse(localStorage.getItem(CLE) || "null"); if (sv) Object.assign(etat, sv); } catch (e) { }
  function sauver() { try { localStorage.setItem(CLE, JSON.stringify(etat)); } catch (e) { } }

  function projet(lignes) {
    return { pays: "Maroc", gamme: etat.gamme, surface: etat.surface, lines: lignes };
  }
  function lignesSaisies() {
    return Object.keys(etat.q).filter(function (r) { return etat.q[r] > 0 && ART[r]; })
      .map(function (r) { return { bloc: ART[r].bloc, ref: r, q: etat.q[r] }; });
  }

  // ------------------------------------------------------------ formulaire projet
  $("#ch-type").value = etat.type; $("#ch-ville").value = etat.ville; $("#ch-surface").value = etat.surface;
  document.querySelectorAll('input[name="gamme"]').forEach(function (r) { r.checked = r.value === etat.gamme; });
  $("#ch-projet").addEventListener("input", function () {
    etat.type = $("#ch-type").value; etat.ville = $("#ch-ville").value.trim();
    var s = parseNum($("#ch-surface").value); etat.surface = s && s > 0 ? s : 0;
    var g = document.querySelector('input[name="gamme"]:checked'); etat.gamme = g ? g.value : "Standard";
    sauver(); toutRendre();
  });

  // ------------------------------------------------------------ onglets
  function onglet(n) {
    etat.onglet = n; sauver();
    ["rapide", "detail"].forEach(function (k) {
      $("#tab-" + k).setAttribute("aria-selected", k === n ? "true" : "false");
      $("#pan-" + k).hidden = k !== n;
    });
  }
  $("#tab-rapide").addEventListener("click", function () { onglet("rapide"); });
  $("#tab-detail").addEventListener("click", function () { onglet("detail"); });
  $(".ch-onglets").addEventListener("keydown", function (ev) {
    if (ev.key === "ArrowRight" || ev.key === "ArrowLeft") { var n = etat.onglet === "rapide" ? "detail" : "rapide"; onglet(n); $("#tab-" + n).focus(); }
  });

  // ------------------------------------------------------------ estimation rapide
  function partsExemple() {
    var p = projet(REF.exemple.lines), ctx = E.context(REF, {}, p), res = E.computeProject(ctx, p);
    var parts = [];
    Object.keys(res.byLot).forEach(function (k) { if (res.byLot[k].ht > 0) parts.push({ lot: k, part: res.byLot[k].ht / res.T.ht }); });
    parts.sort(function (a, b) { return b.part - a.part; });
    return { parts: parts, ctx: ctx };
  }
  function rendreRapide() {
    var x = partsExemple(), ctx = x.ctx, r = E.ratioRange(ctx), s = etat.surface || 0;
    var bas = r[0] * s, haut = r[1] * s, mil = (bas + haut) / 2;
    $("#r-tuiles").innerHTML =
      '<div><b>Coût au m² TTC</b><strong>' + fmt(r[0]) + ' – ' + fmt(r[1]) + '</strong><span>DH/m², gamme ' + esc(etat.gamme.toLowerCase()) + '</span></div>' +
      '<div><b>Fourchette basse</b><strong>' + mdh(bas) + '</strong><span>TTC</span></div>' +
      '<div class="fort"><b>Valeur médiane</b><strong>' + mdh(mil) + '</strong><span>TTC, dont TVA 20 % : ' + mdh(mil - mil / 1.2) + '</span></div>' +
      '<div><b>Fourchette haute</b><strong>' + mdh(haut) + '</strong><span>TTC</span></div>';
    $("#r-note").textContent = fmt(s) + " m² · " + (etat.type || "Projet") + (etat.ville ? " · " + etat.ville : "") + " · montants TTC";
    var max = x.parts[0] ? x.parts[0].part : 1;
    $("#r-lots").innerHTML = x.parts.map(function (p) {
      return '<div class="ch-barre"><span>' + esc(LIB_LOT[p.lot]) + '</span><span class="piste"><i style="width:' + (p.part / max * 100).toFixed(1) + '%"></i></span>' +
        '<span class="val">' + mdh(mil * p.part) + '<small>' + fmt(p.part * 100, 1) + ' %</small></span></div>';
    }).join("");
  }

  // ------------------------------------------------------------ chiffrage détaillé
  var ouverts = {};
  function calcul() {
    var p = projet(lignesSaisies()), ctx = E.context(REF, {}, p);
    return { ctx: ctx, res: E.computeProject(ctx, p) };
  }
  function pvUnitaire(ctx, a) { return E.computeLine(ctx, { bloc: a.bloc, ref: a.ref, q: 1 }).pv; }

  function lignesTable(ctx, arts) {
    var h = "", blocCour = null;
    arts.forEach(function (a) {
      if (a.bloc !== blocCour) { blocCour = a.bloc; var b = BLOCS[a.bloc]; h += '<tr class="bloc"><td colspan="5">' + esc(b ? b.lib : a.bloc) + '<span>' + esc(a.bloc) + '</span></td></tr>'; }
      var q = etat.q[a.ref] || "", pv = pvUnitaire(ctx, a), id = "q-" + a.ref.replace(/[^A-Za-z0-9-]/g, "_");
      h += '<tr' + (q > 0 ? ' class="saisi"' : '') + ' data-ref="' + esc(a.ref) + '"><td><label for="' + id + '" style="font-weight:400;display:block">' + esc(a.des) + '</label></td><td class="u">' + esc(a.u) + '</td>' +
        '<td class="n">' + fmt(pv, 2) + '</td><td class="n"><input id="' + id + '" inputmode="decimal" value="' + (q === "" ? "" : String(q).replace(".", ",")) + '" aria-label="Quantité"></td>' +
        '<td class="n t">' + (q > 0 ? fmt(q * pv, 2) : "–") + '</td></tr>';
    });
    return '<div class="ch-table-zone"><table class="ch-table"><thead><tr><th>Ouvrage</th><th>Unité</th><th class="n">PU HT (DH)</th><th class="n">Quantité</th><th class="n">Total HT</th></tr></thead><tbody>' + h + '</tbody></table></div>';
  }

  function rendreDetail() {
    var c = calcul(), ctx = c.ctx, res = c.res;
    var qry = $("#d-recherche").value.trim().toLowerCase(), seules = $("#d-seules").checked;
    var mots = qry ? qry.normalize("NFD").replace(/[̀-ͯ]/g, "").split(/\s+/) : [];
    var norm = function (s) { return s.toLowerCase().normalize("NFD").replace(/[̀-ͯ]/g, ""); };
    var html = "";
    LOTS.forEach(function (l) {
      var arts = PAR_LOT[l.code].filter(function (a) {
        if (seules && !(etat.q[a.ref] > 0)) return false;
        if (!mots.length) return true;
        var t = norm(a.des + " " + (BLOCS[a.bloc] ? BLOCS[a.bloc].lib : ""));
        return mots.every(function (m) { return t.indexOf(m) >= 0; });
      });
      if ((qry || seules) && !arts.length) return;
      var tot = res.byLot[l.code] ? res.byLot[l.code].ht : 0;
      var ouvert = ouverts[l.code] || (qry && arts.length <= 60) || (seules && arts.length);
      html += '<details class="ch-lot" data-lot="' + l.code + '"' + (ouvert ? " open" : "") + '><summary><span class="code">' + l.code + '</span><span class="lib">' + esc(l.lib) +
        '</span><span class="tot num' + (tot > 0 ? " plein" : "") + '">' + (tot > 0 ? dh(tot) + " HT" : arts.length + " ouvrages") + '</span></summary>' +
        (ouvert ? lignesTable(ctx, arts) : "") + '</details>';
    });
    $("#d-lots").innerHTML = html || '<p class="ch-vide">Aucun ouvrage ne correspond. Essayez un autre mot, ou décochez « Lignes chiffrées seulement ».</p>';
    rendreTotaux(c);
  }

  function rendreTotaux(c) {
    c = c || calcul();
    var T = c.res.T, n = lignesSaisies().length, s = etat.surface || 0;
    $("#d-totaux").innerHTML =
      '<dt>Lignes chiffrées</dt><dd>' + n + '</dd>' +
      '<dt>Total HT</dt><dd>' + dh(T.ht, 2) + '</dd>' +
      '<dt>TVA 20 %</dt><dd>' + dh(T.tva, 2) + '</dd>' +
      '<dt class="ttc">Total TTC</dt><dd class="ttc">' + dh(T.ttc) + '</dd>' +
      '<dt>Coût TTC au m²</dt><dd>' + (s > 0 && T.ttc > 0 ? dh(T.ttcM2) : "–") + '</dd>';
    var r = E.ratioRange(c.ctx), ctrl = "";
    if (n && s > 0) {
      var v = T.ttcM2, dans = v >= r[0] && v <= r[1];
      ctrl = '<div class="ch-pastille' + (dans ? "" : " attention") + '">' + (dans
        ? "Le coût au m² est dans la fourchette habituelle de la gamme " + esc(etat.gamme.toLowerCase()) + " (" + fmt(r[0]) + " à " + fmt(r[1]) + " DH/m² TTC)."
        : "Le coût au m² est " + (v < r[0] ? "sous" : "au-dessus de") + " la fourchette habituelle de la gamme " + esc(etat.gamme.toLowerCase()) + " (" + fmt(r[0]) + " à " + fmt(r[1]) + " DH/m² TTC)" + (v < r[0] ? " : des lots manquent peut-être." : ".")) + '</div>';
    } else ctrl = '<div class="ch-pastille attention">Saisissez des quantités dans les lots, ou chargez l\'exemple de villa pour voir un chiffrage complet.</div>';
    $("#d-controle").innerHTML = ctrl;
    var lots = Object.keys(c.res.byLot).filter(function (k) { return c.res.byLot[k].ht > 0; }).sort(function (a, b) { return c.res.byLot[b].ht - c.res.byLot[a].ht; });
    var max = lots.length ? c.res.byLot[lots[0]].ht : 1;
    $("#d-lots-barres").innerHTML = lots.slice(0, 8).map(function (k) {
      var v = c.res.byLot[k].ht;
      return '<div class="ch-barre"><span>' + esc(LIB_LOT[k]) + '</span><span class="piste"><i style="width:' + (v / max * 100).toFixed(1) + '%"></i></span><span class="val">' + fmt(v / T.ht * 100, 0) + ' %</span></div>';
    }).join("");
  }

  $("#d-lots").addEventListener("toggle", function (ev) {
    var d = ev.target; if (!d.classList || !d.classList.contains("ch-lot")) return;
    var code = d.getAttribute("data-lot"); ouverts[code] = d.open;
    if (d.open && !d.querySelector(".ch-table")) rendreDetail();
  }, true);

  $("#d-lots").addEventListener("change", function (ev) {
    var inp = ev.target; if (inp.tagName !== "INPUT") return;
    var tr = inp.closest("tr"), ref = tr.getAttribute("data-ref"), v = parseNum(inp.value);
    if (v != null && v > 0) etat.q[ref] = v; else delete etat.q[ref];
    sauver();
    var c = calcul(), a = ART[ref], pv = pvUnitaire(c.ctx, a);
    tr.classList.toggle("saisi", v > 0);
    tr.querySelector("td.t").textContent = v > 0 ? fmt(v * pv, 2) : "–";
    var det = tr.closest("details"), tot = c.res.byLot[det.getAttribute("data-lot")];
    var span = det.querySelector("summary .tot");
    if (tot && tot.ht > 0) { span.textContent = dh(tot.ht) + " HT"; span.classList.add("plein"); }
    else { span.textContent = PAR_LOT[det.getAttribute("data-lot")].length + " ouvrages"; span.classList.remove("plein"); }
    rendreTotaux(c);
  });

  var minuterie;
  $("#d-recherche").addEventListener("input", function () { clearTimeout(minuterie); minuterie = setTimeout(rendreDetail, 180); });
  $("#d-seules").addEventListener("change", rendreDetail);
  $("#d-exemple").addEventListener("click", function () {
    etat.q = {}; REF.exemple.lines.forEach(function (l) { etat.q[l.ref] = l.q; });
    etat.surface = REF.exemple.surface; etat.type = "Villa"; $("#ch-surface").value = etat.surface; $("#ch-type").value = "Villa";
    sauver(); toutRendre(); $("#d-etat").textContent = "Exemple chargé : villa R+1 de 250 m².";
  });
  $("#d-vider").addEventListener("click", function () {
    if (!lignesSaisies().length) return;
    etat.q = {}; ouverts = {}; sauver(); toutRendre(); $("#d-etat").textContent = "Toutes les quantités ont été effacées.";
  });

  // ------------------------------------------------------------ récapitulatif
  function recap() {
    var c = calcul(), T = c.res.T, L = [];
    L.push("Estimation SIGMA ICC – " + (etat.type || "Projet") + (etat.ville ? ", " + etat.ville : "") + ", " + fmt(etat.surface) + " m², gamme " + etat.gamme.toLowerCase());
    if (lignesSaisies().length) {
      Object.keys(c.res.byLot).sort().forEach(function (k) { var v = c.res.byLot[k].ht; if (v > 0) L.push("  " + k + " " + LIB_LOT[k] + " : " + dh(v) + " HT"); });
      L.push("Total HT : " + dh(T.ht, 2)); L.push("TVA 20 % : " + dh(T.tva, 2)); L.push("Total TTC : " + dh(T.ttc, 2));
      if (etat.surface > 0) L.push("Soit " + dh(T.ttcM2) + " TTC/m²");
    } else {
      var r = E.ratioRange(c.ctx);
      L.push("Fourchette rapide : " + mdh(r[0] * etat.surface) + " à " + mdh(r[1] * etat.surface) + " TTC (" + fmt(r[0]) + " à " + fmt(r[1]) + " DH/m²)");
    }
    return L.join("\n");
  }
  $("#d-copier").addEventListener("click", function () {
    var t = recap();
    if (navigator.clipboard && navigator.clipboard.writeText) navigator.clipboard.writeText(t)
      .then(function () { $("#d-etat").textContent = "Récapitulatif copié."; })
      .catch(function () { $("#d-etat").textContent = "Copie impossible ici : utilisez le bouton « Joindre à ma demande »."; });
    else $("#d-etat").textContent = "Copie impossible ici : utilisez le bouton « Joindre à ma demande ».";
  });
  $("#d-demande").addEventListener("click", function () {
    var msg = document.getElementById("f-msg"), sujet = document.getElementById("f-sujet");
    if (msg) msg.value = recap() + "\n\nPrécisions sur mon projet : ";
    if (sujet) sujet.value = "Chiffrage des travaux";
    document.getElementById("demande").scrollIntoView({ behavior: "smooth" });
    if (msg) setTimeout(function () { msg.focus(); }, 400);
  });

  function toutRendre() { rendreRapide(); rendreDetail(); }
  onglet(etat.onglet === "detail" ? "detail" : "rapide");
  toutRendre();
})();
