/* SIGMA ICC – outil de chiffrage
   Calculs : assets/js/moteur.js (mêmes formules que le fichier de calcul Excel du bureau).
   Prix : assets/js/donnees-prix.js (15 pays, 9 devises, prix d'achat par devise sans conversion).
   Le visiteur choisit le pays et la devise, saisit quantités et prix d'achat, ajoute ou copie des lignes,
   crée des blocs, et télécharge le devis en PDF (mention « Généré par SIGMA ICC B.E.T »). */
(function () {
  "use strict";
  var E = window.Engine, REF = window.SIGMA_PRIX;
  var $ = function (s) { return document.querySelector(s); };
  var esc = function (s) { return String(s == null ? "" : s).replace(/[&<>"']/g, function (c) { return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c]; }); };
  var parseNum = function (v) { var s = String(v == null ? "" : v).replace(/\s/g, "").replace(",", "."); if (s === "") return null; var n = Number(s); return isNaN(n) ? null : n; };
  var uid = function () { return "x" + Date.now().toString(36) + Math.random().toString(36).slice(2, 6); };
  function fmt(n, d, sep) {
    if (n == null || isNaN(n)) return "–";
    d = d == null ? 0 : d;
    var s = Math.abs(n).toFixed(d).split(".");
    s[0] = s[0].replace(/\B(?=(\d{3})+(?!\d))/g, sep || " ");
    return (n < 0 ? "-" : "") + s[0] + (s[1] ? "," + s[1] : "");
  }
  var numIn = function (n) { return n == null || n === "" ? "" : String(n).replace(".", ","); };

  // ------------------------------------------------------------ référentiel
  var LOTS = REF.lots, LIB_LOT = {}, BLOCS_REF = {}, ART = {}, ART_BLOC = {};
  LOTS.forEach(function (l) { LIB_LOT[l.code] = l.lib; });
  REF.blocs.forEach(function (b) { BLOCS_REF[b.code] = b; });
  REF.articles.forEach(function (a) { ART[a.ref] = a; (ART_BLOC[a.bloc] = ART_BLOC[a.bloc] || []).push(a); });
  var DEV = {}; REF.devises.forEach(function (d) { DEV[d.code] = d; });

  // ------------------------------------------------------------ état
  var CLE = "sigma-chiffrage-v2";
  var etat = { pays: "Maroc", devise: "", type: "Villa", ville: "Marrakech", surface: 250, gamme: "Standard", onglet: "detail",
    q: {}, pu: {}, extra: [], blocsPerso: [] };
  try { var sv = JSON.parse(localStorage.getItem(CLE) || "null"); if (sv) Object.assign(etat, sv); } catch (e) { }
  function sauver() { try { localStorage.setItem(CLE, JSON.stringify(etat)); } catch (e) { } }

  // Type de projet : coefficient sur la fourchette au m² (base villa) et répartition type par lot
  var TYPES = REF.typesProjet || [];
  function typeProjet() { return TYPES.find(function (t) { return t.nom === etat.type; }) || TYPES[0] || { nom: "Villa", k: 1, rep: {} }; }
  function fourchette(ctx) { var r = E.ratioRange(ctx), k = typeProjet().k; return [r[0] * k, r[1] * k]; }
  function pays() { return REF.pays.find(function (p) { return p.pays === etat.pays; }) || REF.pays[0]; }
  function devise() { return etat.devise || pays().devise; }
  function blocsDuLot(code) {
    return REF.blocs.filter(function (b) { return b.lot === code; }).concat(etat.blocsPerso.filter(function (b) { return b.lot === code; }));
  }
  function blocInfo(code) { return BLOCS_REF[code] || etat.blocsPerso.find(function (b) { return b.code === code; }); }

  // Lignes transmises au moteur
  function lignes() {
    var L = [];
    Object.keys(etat.q).forEach(function (r) {
      if (etat.q[r] > 0 && ART[r]) L.push({ bloc: ART[r].bloc, ref: r, q: etat.q[r], puForce: etat.pu[r] != null ? etat.pu[r] : undefined });
    });
    etat.extra.forEach(function (x) {
      if (x.q > 0) L.push({ bloc: x.bloc, q: x.q, libre: { des: x.des || "Ligne ajoutée", u: x.u || "U", pu: x.pu, h: x.h || 0 } });
    });
    return L;
  }
  function projet(L) {
    var f = { devise: devise() };
    // devise différente de celle du pays : taux horaire d'un pays qui utilise cette devise
    if (f.devise !== pays().devise) { var pp = REF.pays.find(function (x) { return x.devise === f.devise; }); if (pp) f.taux = pp.taux; }
    return { pays: etat.pays, gamme: etat.gamme, surface: etat.surface, lines: L || lignes(), forcages: f, blocsPerso: etat.blocsPerso };
  }
  function calcul() {
    var p = projet(), ctx = E.context(REF, {}, p);
    return { p: p, ctx: ctx, res: E.computeProject(ctx, p), autre: E.computeProject(ctx, p, ctx.methode === "COEF" ? "DS" : "COEF") };
  }
  var sym = function (ctx) { return ctx.sym; };
  function mt(n, ctx, d) { return fmt(n, d == null ? ctx.dec : d) + " " + sym(ctx); }
  function court(n, ctx) {
    if (Math.abs(n) >= 1e9) return fmt(n / 1e9, 2) + " Md " + sym(ctx);
    if (Math.abs(n) >= 1e6) return fmt(n / 1e6, 2) + " M " + sym(ctx);
    return fmt(n, 0) + " " + sym(ctx);
  }

  // ------------------------------------------------------------ formulaire projet
  $("#ch-pays").innerHTML = REF.pays.map(function (p) { return '<option value="' + esc(p.pays) + '">' + esc(p.pays) + " (" + p.devise + ")</option>"; }).join("");
  function remplirDevises() {
    var pd = pays().devise;
    $("#ch-devise").innerHTML = REF.devises.filter(function (d) { return REF.articles[0].p[d.code] != null; }).map(function (d) {
      return '<option value="' + d.code + '">' + d.code + " – " + esc(d.nom) + (d.code === pd ? " (devise du pays)" : "") + "</option>";
    }).join("");
    $("#ch-devise").value = devise();
  }
  if (TYPES.length) {
    $("#ch-type").innerHTML = TYPES.map(function (t) { return '<option value="' + esc(t.nom) + '">' + esc(t.nom) + "</option>"; }).join("");
    if (!TYPES.some(function (t) { return t.nom === etat.type; })) etat.type = TYPES[0].nom;
  }
  $("#ch-pays").value = etat.pays; remplirDevises();
  $("#ch-type").value = etat.type; $("#ch-ville").value = etat.ville; $("#ch-surface").value = etat.surface;
  document.querySelectorAll('input[name="gamme"]').forEach(function (r) { r.checked = r.value === etat.gamme; });
  $("#ch-projet").addEventListener("change", function (ev) {
    if (ev.target.id === "ch-pays") { etat.pays = ev.target.value; etat.devise = ""; remplirDevises(); }
    if (ev.target.id === "ch-devise") etat.devise = ev.target.value === pays().devise ? "" : ev.target.value;
  });
  $("#ch-projet").addEventListener("input", function () {
    etat.type = $("#ch-type").value; etat.ville = $("#ch-ville").value.trim();
    var s = parseNum($("#ch-surface").value); etat.surface = s && s > 0 ? s : 0;
    // les études techniques au m² suivent la surface du projet
    ["IC12-10", "IC12-11", "IC12-12"].forEach(function (r) { if (etat.q[r] > 0 && etat.surface > 0) etat.q[r] = etat.surface; });
    var g = document.querySelector('input[name="gamme"]:checked'); etat.gamme = g ? g.value : "Standard";
    sauver(); toutRendre();
  });
  $("#ch-projet").addEventListener("change", function (ev) { if (ev.target.tagName === "SELECT") { sauver(); toutRendre(); } });

  // ------------------------------------------------------------ onglets
  function onglet(n) {
    etat.onglet = n; sauver();
    document.body.classList.toggle("ch-detail-actif", n === "detail");
    ["rapide", "detail"].forEach(function (k) { $("#tab-" + k).setAttribute("aria-selected", k === n ? "true" : "false"); $("#pan-" + k).hidden = k !== n; });
  }
  $("#tab-rapide").addEventListener("click", function () { onglet("rapide"); });
  $("#tab-detail").addEventListener("click", function () { onglet("detail"); });

  // ------------------------------------------------------------ estimation rapide
  function rendreRapide() {
    var ctx = E.context(REF, {}, projet([])), t = typeProjet(), r = fourchette(ctx), s = etat.surface || 0, p = pays();
    // part du gros œuvre plus forte en économique, plus faible en haut de gamme (sources 2025-2026)
    var fGO = { "Économique": 1.35, "Standard": 1, "Haut de gamme": 0.78 }[etat.gamme] || 1, GO = { L03: 1, L04: 1, L05: 1 };
    var poids = Object.keys(t.rep).map(function (k) { return { lot: k, w: t.rep[k] * (GO[k] ? fGO : 1) }; });
    var somme = poids.reduce(function (a, x) { return a + x.w; }, 0);
    var parts = poids.map(function (x) { return { lot: x.lot, part: x.w / somme }; }).sort(function (a, b) { return b.part - a.part; });
    if (ctx.devise !== p.devise) {
      $("#r-tuiles").innerHTML = '<div style="grid-column:1/-1"><b>Fourchette indisponible</b><span>Les coûts au m² sont connus dans la devise du pays (' + p.devise + "). Revenez à cette devise pour l'estimation rapide, ou utilisez le devis détaillé.</span></div>";
      $("#r-lots").innerHTML = ""; $("#r-note").textContent = ""; return;
    }
    var bas = r[0] * s, haut = r[1] * s, mil = (bas + haut) / 2;
    var coef = t.k === 1 ? "base villa" : "× " + fmt(t.k, 2).replace(/0$/, "") + " par rapport à une villa";
    $("#r-tuiles").innerHTML =
      '<div><b>Coût au m² TTC</b><strong>' + fmt(r[0]) + " – " + fmt(r[1]) + "</strong><span>" + sym(ctx) + "/m², " + esc(t.nom.toLowerCase()) + ", gamme " + esc(etat.gamme.toLowerCase()) + " (" + coef + ")</span></div>" +
      "<div><b>Fourchette basse</b><strong>" + court(bas, ctx) + "</strong><span>TTC</span></div>" +
      '<div class="fort"><b>Valeur médiane</b><strong>' + court(mil, ctx) + "</strong><span>TTC, dont TVA " + fmt(ctx.tva * 100, 2).replace(/,00$/, "") + " % : " + court(mil - mil / (1 + ctx.tva), ctx) + "</span></div>" +
      "<div><b>Fourchette haute</b><strong>" + court(haut, ctx) + "</strong><span>TTC</span></div>";
    $("#r-note").textContent = fmt(s) + " m² · " + t.nom + (etat.ville ? " · " + etat.ville : "") + " · montants TTC";
    var max = parts[0] ? parts[0].part : 1;
    $("#r-lots").innerHTML = parts.map(function (q) {
      return '<div class="ch-barre"><span>' + esc(LIB_LOT[q.lot]) + '</span><span class="piste"><i style="width:' + (q.part / max * 100).toFixed(1) + '%"></i></span><span class="val">' + court(mil * q.part, ctx) + "<small>" + fmt(q.part * 100, 1) + " %</small></span></div>";
    }).join("");
  }

  // ------------------------------------------------------------ devis détaillé
  var ouverts = {};
  function puSuggere(ctx, a) { var v = a.p[ctx.devise]; return v == null ? null : v * ctx.gammeK; }
  function ligneLib(ctx, a) {
    var line = { bloc: a.bloc, ref: a.ref, q: 1, puForce: etat.pu[a.ref] != null ? etat.pu[a.ref] : undefined };
    return E.computeLine(ctx, line);
  }
  function ligneExtra(ctx, x) { return E.computeLine(ctx, { bloc: x.bloc, q: 1, libre: { des: x.des, u: x.u, pu: x.pu, h: x.h || 0 } }); }

  function trLib(ctx, a) {
    var q = etat.q[a.ref], r = ligneLib(ctx, a), sug = puSuggere(ctx, a), id = "q-" + a.ref.replace(/[^A-Za-z0-9-]/g, "_");
    var manque = ctx.prixMode === "saisie" || sug == null;
    return '<tr class="' + (q > 0 ? "saisi" : "") + '" data-ref="' + esc(a.ref) + '">' +
      '<td><label for="' + id + '" class="des">' + esc(a.des) + "</label></td><td class=\"u\" data-l=\"Unité\">" + esc(a.u) + "</td>" +
      '<td class="n" data-l="Prix d\'achat HT"><input class="pu" value="' + numIn(etat.pu[a.ref]) + '" placeholder="' + (sug == null ? "à saisir" : fmt(sug, ctx.dec, " ")) + '" inputmode="decimal" aria-label="Prix d\'achat HT"></td>' +
      '<td class="n h" data-l="Temps (h)">' + fmt(a.h, 2) + '</td><td class="n pv" data-l="PV unitaire HT">' + (r.pv > 0 ? fmt(r.pv, ctx.dec) : (manque ? "–" : fmt(0, ctx.dec))) + "</td>" +
      '<td class="n" data-l="Quantité"><input id="' + id + '" class="qte" value="' + numIn(q) + '" inputmode="decimal" aria-label="Quantité"></td>' +
      '<td class="n t" data-l="Total HT">' + (q > 0 ? fmt(q * r.pv, ctx.dec) : "–") + "</td>" +
      '<td class="act"><button type="button" class="ic" data-act="copier" title="Copier la ligne en dessous" aria-label="Copier la ligne en dessous">⧉</button></td></tr>';
  }
  function trExtra(ctx, x) {
    var r = ligneExtra(ctx, x);
    return '<tr class="ajout' + (x.q > 0 ? " saisi" : "") + '" data-x="' + x.id + '">' +
      '<td><input class="des-in" value="' + esc(x.des) + '" placeholder="Désignation de l\'ouvrage" aria-label="Désignation"></td>' +
      '<td class="u" data-l="Unité"><input class="u-in" value="' + esc(x.u) + '" aria-label="Unité"></td>' +
      '<td class="n" data-l="Prix d\'achat HT"><input class="pu" value="' + numIn(x.pu) + '" placeholder="à saisir" inputmode="decimal" aria-label="Prix d\'achat HT"></td>' +
      '<td class="n" data-l="Temps (h)"><input class="h-in" value="' + numIn(x.h) + '" placeholder="0" inputmode="decimal" aria-label="Temps de pose (h)"></td>' +
      '<td class="n pv" data-l="PV unitaire HT">' + fmt(r.pv, ctx.dec) + "</td>" +
      '<td class="n" data-l="Quantité"><input class="qte" value="' + numIn(x.q) + '" inputmode="decimal" aria-label="Quantité"></td>' +
      '<td class="n t" data-l="Total HT">' + (x.q > 0 ? fmt(x.q * r.pv, ctx.dec) : "–") + "</td>" +
      '<td class="act"><button type="button" class="ic" data-act="copier" title="Copier la ligne en dessous" aria-label="Copier la ligne en dessous">⧉</button><button type="button" class="ic" data-act="suppr" title="Supprimer la ligne" aria-label="Supprimer la ligne">✕</button></td></tr>';
  }
  // Les lignes ajoutées s'insèrent juste après leur ligne d'origine (« apres »), ou en fin de bloc
  function apres(cle, bloc) { return etat.extra.filter(function (x) { return x.bloc === bloc && x.apres === cle; }); }
  function rendreSuite(ctx, cle, bloc, filtre) {
    return apres(cle, bloc).map(function (x) { return (filtre(x) ? trExtra(ctx, x) : "") + rendreSuite(ctx, x.id, bloc, filtre); }).join("");
  }

  function rendreDetail() {
    var c = calcul(), ctx = c.ctx;
    var qry = $("#d-recherche").value.trim(), seules = $("#d-seules").checked;
    var norm = function (s) { return String(s || "").toLowerCase().normalize("NFD").replace(/[̀-ͯ]/g, ""); };
    var mots = qry ? norm(qry).split(/\s+/) : [];
    var okTexte = function (t) { t = norm(t); return mots.every(function (m) { return t.indexOf(m) >= 0; }); };
    var html = "";
    LOTS.forEach(function (l) {
      var corps = "", n = 0;
      blocsDuLot(l.code).forEach(function (b) {
        var filtreA = function (a) { return (!seules || etat.q[a.ref] > 0) && (!mots.length || okTexte(a.des + " " + b.lib)); };
        var filtreX = function (x) { return (!seules || x.q > 0) && (!mots.length || okTexte(x.des + " " + b.lib)); };
        var rows = rendreSuite(ctx, null, b.code, filtreX);
        var arts = ART_BLOC[b.code] || [];
        var lignesB = arts.map(function (a) { var ok = filtreA(a); if (ok) n++; return (ok ? trLib(ctx, a) : "") + rendreSuite(ctx, a.ref, b.code, filtreX); }).join("") + rows;
        n += (lignesB.match(/data-x=/g) || []).length;
        if ((qry || seules) && !lignesB) return;
        corps += '<tr class="bloc"><td colspan="8">' + esc(b.lib) + "<span>" + esc(b.code) + (b.perso ? " · bloc personnalisé" : "") + "</span></td></tr>" + lignesB +
          '<tr class="ajouter"><td colspan="8"><button type="button" class="lien" data-act="ajouter" data-bloc="' + esc(b.code) + '">+ Ajouter une ligne dans ce bloc</button></td></tr>';
      });
      if ((qry || seules) && !n) return;
      var tot = c.res.byLot[l.code] ? c.res.byLot[l.code].ht : 0;
      var ouvert = ouverts[l.code] || ((qry || seules) && n <= 80);
      html += '<details class="ch-lot" data-lot="' + l.code + '"' + (ouvert ? " open" : "") + '><summary><span class="code">' + l.code + '</span><span class="lib">' + esc(l.lib) +
        '</span><span class="tot num' + (tot > 0 ? " plein" : "") + '">' + (tot > 0 ? mt(tot, ctx, 0) + " HT" : "") + "</span></summary>" +
        (ouvert ? '<div class="ch-table-zone"><table class="ch-table"><thead><tr><th>Ouvrage</th><th>Unité</th><th class="n">Prix d\'achat HT</th><th class="n">Temps (h)</th><th class="n">PV unitaire HT</th><th class="n">Quantité</th><th class="n">Total HT</th><th></th></tr></thead><tbody>' + corps + "</tbody></table></div>" +
          '<form class="ch-nouveau-bloc" data-lot="' + l.code + '"><label>Nouveau bloc dans ce lot<input name="nom" placeholder="Ex. : Éclairage du jardin" required></label><button class="btn petit secondaire" type="submit">+ Créer le bloc</button></form>' : "") + "</details>";
    });
    $("#d-lots").innerHTML = html || '<p class="ch-vide">Aucun ouvrage ne correspond. Essayez un autre mot, ou décochez « Lignes chiffrées seulement ».</p>';
    rendreTotaux(c);
  }

  function rendreTotaux(c) {
    c = c || calcul();
    var ctx = c.ctx, T = c.res.T, A = c.autre.T, n = lignes().length, s = etat.surface || 0;
    var nomM = function (m) { return m === "COEF" ? "Coefficients" : "Déboursé sec"; };
    $("#d-totaux").innerHTML =
      "<dt>Lignes chiffrées</dt><dd>" + n + "</dd>" +
      "<dt>Total HT</dt><dd>" + mt(T.ht, ctx) + "</dd>" +
      "<dt>TVA " + fmt(ctx.tva * 100, 2).replace(/,00$/, "") + " %</dt><dd>" + mt(T.tva, ctx) + "</dd>" +
      '<dt class="ttc">Total TTC</dt><dd class="ttc">' + mt(T.ttc, ctx, 0) + "</dd>" +
      "<dt>Coût TTC au m²</dt><dd>" + (s > 0 && T.ttc > 0 ? mt(T.ttcM2, ctx, 0) : "–") + "</dd>" +
      "<dt>Retenue de garantie " + fmt(ctx.rg * 100, 0) + " %</dt><dd>" + mt(T.rg, ctx) + "</dd>" +
      "<dt>Cautionnement " + fmt(ctx.caution * 100, 0) + " %</dt><dd>" + mt(T.caution, ctx) + "</dd>";
    var bm = document.getElementById("ch-barre-mobile");
    if (bm) { bm.querySelector("strong").textContent = mt(T.ttc, ctx, 0); bm.querySelector("span").textContent = n + " ligne" + (n > 1 ? "s" : "") + " · TTC" + (s > 0 && T.ttc > 0 ? " · " + mt(T.ttcM2, ctx, 0) + "/m²" : ""); }
    $("#d-methodes").innerHTML = n ? '<div class="m actif"><b>' + nomM(ctx.methode) + "</b> (méthode du pays)<span>" + mt(T.ht, ctx, 0) + " HT</span></div>" +
      '<div class="m"><b>' + nomM(ctx.methode === "COEF" ? "DS" : "COEF") + "</b> pour comparaison<span>" + mt(A.ht, ctx, 0) + " HT · écart " + (T.ht > 0 ? fmt((A.ht / T.ht - 1) * 100, 1) : "0") + " %</span></div>" : "";
    var ctrl = E.controls(ctx, c.p, c.res).filter(function (k) { return k.s !== "ok" && !k.range && k.k !== "Lignes sans quantité" && k.k !== "Références inconnues" && k.k !== "Blocs inconnus"; });
    var h = "";
    if (!n) h = '<div class="ch-pastille attention">Saisissez des quantités dans les lots, ou chargez l\'exemple de villa pour voir un devis complet.</div>';
    else {
      ctrl.forEach(function (k) { if (!k.range) h += '<div class="ch-pastille attention">' + esc(k.k) + " : " + k.v + "</div>"; });
      var fr = fourchette(ctx), v = T.ttcM2;
      if (s > 0 && ctx.devise === pays().devise && (v < fr[0] || v > fr[1]))
        h += '<div class="ch-pastille attention">Le coût au m² (' + mt(v, ctx, 0) + ") sort de la fourchette habituelle pour un projet « " + esc(typeProjet().nom.toLowerCase()) + " », gamme " + esc(etat.gamme.toLowerCase()) + " (" + fmt(fr[0]) + " à " + fmt(fr[1]) + " " + sym(ctx) + "/m² TTC).</div>";
      if (!h) h = '<div class="ch-pastille">Contrôles du devis : aucune anomalie.</div>';
    }
    $("#d-controle").innerHTML = h;
    var lots = Object.keys(c.res.byLot).filter(function (k) { return c.res.byLot[k].ht > 0; }).sort(function (a, b) { return c.res.byLot[b].ht - c.res.byLot[a].ht; });
    var max = lots.length ? c.res.byLot[lots[0]].ht : 1;
    $("#d-lots-barres").innerHTML = lots.slice(0, 8).map(function (k) {
      var v = c.res.byLot[k].ht;
      return '<div class="ch-barre"><span>' + esc(LIB_LOT[k]) + '</span><span class="piste"><i style="width:' + (v / max * 100).toFixed(1) + '%"></i></span><span class="val">' + fmt(v / T.ht * 100, 0) + " %</span></div>";
    }).join("");
  }

  // Mise à jour d'une ligne sans tout redessiner
  function majLigne(tr) {
    var c = calcul(), ctx = c.ctx, r, q;
    if (tr.hasAttribute("data-ref")) { var a = ART[tr.getAttribute("data-ref")]; r = ligneLib(ctx, a); q = etat.q[a.ref]; }
    else { var x = etat.extra.find(function (z) { return z.id === tr.getAttribute("data-x"); }); r = ligneExtra(ctx, x); q = x.q; }
    tr.classList.toggle("saisi", q > 0);
    tr.querySelector("td.pv").textContent = r.pv > 0 ? fmt(r.pv, ctx.dec) : "–";
    tr.querySelector("td.t").textContent = q > 0 ? fmt(q * r.pv, ctx.dec) : "–";
    var det = tr.closest("details"), tot = c.res.byLot[det.getAttribute("data-lot")], span = det.querySelector("summary .tot");
    span.textContent = tot && tot.ht > 0 ? mt(tot.ht, ctx, 0) + " HT" : ""; span.classList.toggle("plein", !!(tot && tot.ht > 0));
    rendreTotaux(c);
  }

  var zone = $("#d-lots");
  zone.addEventListener("toggle", function (ev) {
    var d = ev.target; if (!d.classList || !d.classList.contains("ch-lot")) return;
    ouverts[d.getAttribute("data-lot")] = d.open;
    if (d.open && !d.querySelector(".ch-table")) rendreDetail();
  }, true);
  zone.addEventListener("change", function (ev) {
    var inp = ev.target; if (inp.tagName !== "INPUT" || inp.closest(".ch-nouveau-bloc")) return;
    var tr = inp.closest("tr"), v = parseNum(inp.value);
    if (tr.hasAttribute("data-ref")) {
      var ref = tr.getAttribute("data-ref");
      if (inp.classList.contains("qte")) { if (v > 0) etat.q[ref] = v; else delete etat.q[ref]; }
      if (inp.classList.contains("pu")) { if (v != null && v >= 0) etat.pu[ref] = v; else delete etat.pu[ref]; }
    } else {
      var x = etat.extra.find(function (z) { return z.id === tr.getAttribute("data-x"); });
      if (inp.classList.contains("qte")) x.q = v > 0 ? v : null;
      if (inp.classList.contains("pu")) x.pu = v != null && v >= 0 ? v : null;
      if (inp.classList.contains("h-in")) x.h = v != null && v >= 0 ? v : 0;
      if (inp.classList.contains("des-in")) x.des = inp.value.trim();
      if (inp.classList.contains("u-in")) x.u = inp.value.trim();
    }
    sauver(); majLigne(tr);
  });
  zone.addEventListener("click", function (ev) {
    var b = ev.target.closest("button[data-act]"); if (!b) return;
    var act = b.getAttribute("data-act"), tr = b.closest("tr"), ctx = calcul().ctx, nx;
    if (act === "ajouter") {
      nx = { id: uid(), bloc: b.getAttribute("data-bloc"), apres: dernier(b.getAttribute("data-bloc")), des: "", u: "U", pu: null, h: 0, q: null };
    } else if (act === "copier") {
      if (tr.hasAttribute("data-ref")) {
        var a = ART[tr.getAttribute("data-ref")];
        nx = { id: uid(), bloc: a.bloc, apres: a.ref, des: a.des, u: a.u, pu: etat.pu[a.ref] != null ? etat.pu[a.ref] : puSuggere(ctx, a), h: a.h, q: null };
      } else {
        var x = etat.extra.find(function (z) { return z.id === tr.getAttribute("data-x"); });
        nx = Object.assign({}, x, { id: uid(), apres: x.id, q: null });
      }
    } else if (act === "suppr") {
      var id = tr.getAttribute("data-x"), cible = etat.extra.find(function (z) { return z.id === id; });
      etat.extra.forEach(function (z) { if (z.apres === id) z.apres = cible.apres; });
      etat.extra = etat.extra.filter(function (z) { return z.id !== id; });
      sauver(); rendreDetail(); $("#d-etat").textContent = "Ligne supprimée."; return;
    }
    if (nx) {
      if (nx.pu != null) nx.pu = Math.round(nx.pu * 1000) / 1000;
      etat.extra.push(nx); sauver(); rendreDetail();
      var nouv = zone.querySelector('tr[data-x="' + nx.id + '"] ' + (act === "ajouter" ? ".des-in" : ".qte"));
      if (nouv) nouv.focus();
    }
  });
  // Dernière ligne d'un bloc (pour ajouter en fin de bloc)
  function dernier(bloc) {
    var arts = ART_BLOC[bloc] || [], cle = arts.length ? arts[arts.length - 1].ref : null;
    for (;;) { var s = apres(cle, bloc); if (!s.length) return cle; cle = s[s.length - 1].id; }
  }
  zone.addEventListener("submit", function (ev) {
    var f = ev.target; if (!f.classList.contains("ch-nouveau-bloc")) return;
    ev.preventDefault();
    var nom = f.querySelector("input").value.trim(); if (!nom) return;
    var lot = f.getAttribute("data-lot"), n = etat.blocsPerso.filter(function (b) { return b.lot === lot; }).length + 1;
    var code = lot + "-P" + n;
    etat.blocsPerso.push({ code: code, lib: nom, lot: lot, perso: true });
    etat.extra.push({ id: uid(), bloc: code, apres: null, des: "", u: "U", pu: null, h: 0, q: null });
    sauver(); rendreDetail(); $("#d-etat").textContent = "Bloc « " + nom + " » créé.";
  });

  var minuterie;
  $("#d-recherche").addEventListener("input", function () { clearTimeout(minuterie); minuterie = setTimeout(rendreDetail, 200); });
  $("#d-seules").addEventListener("change", rendreDetail);
  $("#d-tout-ouvrir").addEventListener("click", function () {
    var tous = LOTS.every(function (l) { return ouverts[l.code]; });
    LOTS.forEach(function (l) { ouverts[l.code] = !tous; });
    this.textContent = tous ? "Tout déplier" : "Tout replier"; rendreDetail();
  });
  $("#d-exemple").addEventListener("click", function () {
    etat.q = {}; etat.pu = {}; etat.extra = []; etat.blocsPerso = [];
    REF.exemple.lines.forEach(function (l) { etat.q[l.ref] = l.q; });
    etat.surface = REF.exemple.surface; etat.type = "Villa"; $("#ch-surface").value = etat.surface; $("#ch-type").value = "Villa";
    sauver(); toutRendre(); $("#d-etat").textContent = "Exemple chargé : villa R+1 de 250 m².";
  });
  var confirmerVider = false;
  $("#d-vider").addEventListener("click", function () {
    if (!confirmerVider) { confirmerVider = true; this.textContent = "Confirmer l'effacement"; var b = this; setTimeout(function () { confirmerVider = false; b.textContent = "Tout effacer"; }, 4000); return; }
    confirmerVider = false; this.textContent = "Tout effacer";
    etat.q = {}; etat.pu = {}; etat.extra = []; etat.blocsPerso = []; ouverts = {};
    sauver(); toutRendre(); $("#d-etat").textContent = "Le devis a été effacé.";
  });

  // ------------------------------------------------------------ récapitulatif et PDF
  function recap() {
    var c = calcul(), T = c.res.T, ctx = c.ctx, L = [];
    L.push("Estimation SIGMA ICC – " + (etat.type || "Projet") + (etat.ville ? ", " + etat.ville : "") + ", " + etat.pays + ", " + fmt(etat.surface) + " m², gamme " + etat.gamme.toLowerCase() + ", devise " + ctx.devise);
    if (lignes().length) {
      Object.keys(c.res.byLot).sort().forEach(function (k) { var v = c.res.byLot[k].ht; if (v > 0) L.push("  " + k + " " + (LIB_LOT[k] || k) + " : " + mt(v, ctx, 0) + " HT"); });
      L.push("Total HT : " + mt(T.ht, ctx)); L.push("TVA : " + mt(T.tva, ctx)); L.push("Total TTC : " + mt(T.ttc, ctx));
    } else {
      var r = E.ratioRange(c.ctx);
      L.push("Fourchette rapide : " + court(r[0] * etat.surface, ctx) + " à " + court(r[1] * etat.surface, ctx) + " TTC");
    }
    return L.join("\n").replace(/ /g, " ");
  }
  $("#d-demande").addEventListener("click", function () {
    var msg = document.getElementById("f-msg"), sujet = document.getElementById("f-sujet");
    if (msg) msg.value = recap() + "\n\nPrécisions sur mon projet : ";
    if (sujet) sujet.value = "Chiffrage des travaux";
    document.getElementById("demande").scrollIntoView({ behavior: "smooth" });
    if (msg) setTimeout(function () { msg.focus(); }, 400);
  });

  var logoPng = null;
  (function () { // logo SVG converti en image pour le PDF
    var img = new Image();
    img.onload = function () { try { var cv = document.createElement("canvas"); cv.width = img.naturalWidth * 3; cv.height = img.naturalHeight * 3; var g = cv.getContext("2d"); g.drawImage(img, 0, 0, cv.width, cv.height); logoPng = { d: cv.toDataURL("image/png"), r: img.naturalWidth / img.naturalHeight }; } catch (e) { } };
    img.src = "images/logo-sigma.svg";
  })();
  function chargerPdf() {
    return new Promise(function (ok, ko) {
      if (window.jspdf && window.jspdf.jsPDF && window.jspdf.jsPDF.API.autoTable) return ok();
      var a = document.createElement("script"); a.src = "https://cdnjs.cloudflare.com/ajax/libs/jspdf/2.5.1/jspdf.umd.min.js";
      a.onload = function () { var b = document.createElement("script"); b.src = "https://cdnjs.cloudflare.com/ajax/libs/jspdf-autotable/3.8.2/jspdf.plugin.autotable.min.js"; b.onload = ok; b.onerror = ko; document.head.appendChild(b); };
      a.onerror = ko; document.head.appendChild(a);
    });
  }
  $("#d-pdf").addEventListener("click", function () {
    var c = calcul(), ctx = c.ctx, T = c.res.T;
    if (!lignes().length) { $("#d-etat").textContent = "Le devis est vide : saisissez au moins une quantité."; return; }
    $("#d-etat").textContent = "Préparation du PDF…";
    chargerPdf().then(function () {
      var J = window.jspdf.jsPDF, doc = new J({ unit: "mm", format: "a4" }), W = 210, H = 297;
      var S = function (n, d) { return fmt(n, d == null ? ctx.dec : d, " "); };
      var symP = ctx.sym === "€" ? "EUR" : ctx.sym;
      var jaune = [255, 182, 0], graph = [48, 48, 48];
      // en-tête
      if (logoPng) doc.addImage(logoPng.d, "PNG", 14, 10, 18 * logoPng.r, 18);
      doc.setFont("helvetica", "bold"); doc.setFontSize(16); doc.setTextColor.apply(doc, graph);
      doc.text("Estimation des travaux", W - 14, 17, { align: "right" });
      doc.setFont("helvetica", "normal"); doc.setFontSize(9); doc.setTextColor(100);
      var d = new Date(), dt = ("0" + d.getDate()).slice(-2) + "/" + ("0" + (d.getMonth() + 1)).slice(-2) + "/" + d.getFullYear();
      doc.text("Établie le " + dt + " · " + etat.pays + " · devise " + ctx.devise, W - 14, 23, { align: "right" });
      doc.setFillColor.apply(doc, jaune); doc.rect(14, 31, W - 28, 1.2, "F");
      doc.setFontSize(10); doc.setTextColor.apply(doc, graph);
      var infos = [["Projet", etat.type || "–"], ["Ville", etat.ville || "–"], ["Surface", S(etat.surface, 0) + " m²"], ["Gamme", etat.gamme], ["Méthode", ctx.methode === "COEF" ? "Coefficients" : "Déboursé sec"]];
      infos.forEach(function (it, i) { var x = 14 + i * 36.4; doc.setFont("helvetica", "bold"); doc.text(it[0].toUpperCase(), x, 38); doc.setFont("helvetica", "normal"); doc.text(String(it[1]), x, 43); });
      // lignes par lot / bloc
      var rows = [], rowsMeta = [];
      var parLot = {};
      c.res.rows.forEach(function (r) { if (!(r.q > 0)) return; (parLot[r.lot] = parLot[r.lot] || []).push(r); });
      Object.keys(parLot).sort().forEach(function (lot) {
        rows.push([{ content: lot + "  " + (LIB_LOT[lot] || lot), colSpan: 4, styles: { fillColor: [33, 33, 33], textColor: 255, fontStyle: "bold" } }, { content: S(c.res.byLot[lot].ht), styles: { fillColor: [33, 33, 33], textColor: [255, 182, 0], fontStyle: "bold", halign: "right" } }]);
        var bloc = null;
        parLot[lot].forEach(function (r) {
          if (r.line.bloc !== bloc) { bloc = r.line.bloc; var bi = blocInfo(bloc); rows.push([{ content: bi ? bi.lib : bloc, colSpan: 5, styles: { fillColor: [245, 245, 242], fontStyle: "bold", textColor: graph } }]); }
          rows.push([r.des, r.u, S(r.q, 2).replace(/,00$/, ""), S(r.pv), S(r.total)]);
        });
      });
      doc.autoTable({
        startY: 50, head: [["Désignation", "Unité", "Quantité", "PU HT (" + symP + ")", "Total HT (" + symP + ")"]], body: rows,
        styles: { font: "helvetica", fontSize: 8.2, cellPadding: 1.6, textColor: graph, lineColor: [218, 218, 218], lineWidth: .1 },
        headStyles: { fillColor: jaune, textColor: [33, 33, 33], fontStyle: "bold" },
        columnStyles: { 0: { cellWidth: 98 }, 1: { cellWidth: 14, halign: "center" }, 2: { cellWidth: 20, halign: "right" }, 3: { cellWidth: 24, halign: "right" }, 4: { cellWidth: 26, halign: "right" } },
        margin: { top: 16, bottom: 20, left: 14, right: 14 }
      });
      // totaux
      var y = doc.lastAutoTable.finalY + 6; if (y > H - 70) { doc.addPage(); y = 20; }
      var tot = [["Total HT", S(T.ht)], ["TVA " + fmt(ctx.tva * 100, 2, " ").replace(/,00$/, "") + " %", S(T.tva)], ["Total TTC", S(T.ttc)],
        ["Coût TTC au m²", etat.surface > 0 ? S(T.ttcM2, 0) : "–"], ["Retenue de garantie " + S(ctx.rg * 100, 0) + " % (pour information)", S(T.rg)], ["Cautionnement " + S(ctx.caution * 100, 0) + " % (pour information)", S(T.caution)]];
      doc.autoTable({ startY: y, body: tot, theme: "plain", margin: { left: W - 14 - 110, right: 14 },
        styles: { fontSize: 9.5, cellPadding: 1.8, textColor: graph }, columnStyles: { 0: { cellWidth: 70 }, 1: { cellWidth: 40, halign: "right" } },
        didParseCell: function (h) { if (h.row.index === 2) { h.cell.styles.fontStyle = "bold"; h.cell.styles.fontSize = 11.5; h.cell.styles.fillColor = jaune; } } });
      y = doc.lastAutoTable.finalY + 6;
      doc.setFontSize(8); doc.setTextColor(110);
      doc.text(doc.splitTextToSize("Montants en " + symP + ". Prix indicatifs (novembre 2026), fourniture et pose, calculés par la méthode " + (ctx.methode === "COEF" ? "des coefficients" : "du déboursé sec") + ". Cette estimation ne remplace pas un chiffrage établi sur plans.", W - 28), 14, y);
      // pied de page sur chaque page : mention obligatoire
      var n = doc.getNumberOfPages();
      for (var i = 1; i <= n; i++) {
        doc.setPage(i);
        doc.setDrawColor(218); doc.line(14, H - 14, W - 14, H - 14);
        doc.setFontSize(8.5); doc.setTextColor.apply(doc, graph); doc.setFont("helvetica", "bold");
        doc.text("Généré par SIGMA ICC B.E.T", 14, H - 9);
        doc.setFont("helvetica", "normal"); doc.setTextColor(110);
        doc.text("sigma-icc.ma · +212 6 61 05 74 55 · sigma.icc@gmail.com", W / 2, H - 9, { align: "center" });
        doc.text("Page " + i + " / " + n, W - 14, H - 9, { align: "right" });
      }
      var nom = "Devis-SIGMA-ICC-" + (etat.type || "projet").replace(/[^A-Za-z0-9]+/g, "-") + "-" + d.toISOString().slice(0, 10) + ".pdf";
      try { doc.save(nom); $("#d-etat").textContent = "PDF téléchargé : " + nom; }
      catch (e) { $("#d-etat").textContent = "Ce navigateur bloque le téléchargement. Essayez depuis le site en ligne."; }
    }).catch(function () { $("#d-etat").textContent = "Impossible de charger le module PDF. Vérifiez votre connexion internet."; });
  });

  var barre = document.getElementById("ch-barre-mobile");
  if (barre) barre.querySelector("button").addEventListener("click", function () { document.querySelector(".ch-synthese").scrollIntoView({ behavior: "smooth", block: "start" }); });

  function toutRendre() { rendreRapide(); rendreDetail(); }
  onglet(etat.onglet === "rapide" ? "rapide" : "detail");
  toutRendre();
})();
