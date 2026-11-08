/* Moteur de calcul SIGMA ICC – reprise exacte des formules du fichier de calcul de chiffrage (méthode des coefficients / déboursé sec). */
(function (root) {
  function roundTo(x, d) {
    const f = Math.pow(10, d);
    // arrondi « Excel » (moitié vers l'extérieur), robuste aux erreurs binaires
    const v = Math.abs(x) * f;
    const r = Math.round(v + 1e-9 * Math.max(1, v));
    return Math.sign(x) * r / f;
  }
  const num = (v, d) => (v === null || v === undefined || v === "" || isNaN(v)) ? d : Number(v);

  // Construit le contexte de calcul d'un projet (pays, devise, coefficients retenus)
  function context(ref, settings, project) {
    settings = settings || {};
    const paysOv = (settings.pays || {})[project.pays] || {};
    const p0 = ref.pays.find(p => p.pays === project.pays) || ref.pays[0];
    const pays = Object.assign({}, p0, paysOv);
    const forc = project.forcages || {};
    const devise = forc.devise || pays.devise;
    const dv = ref.devises.find(d => d.code === devise) || { code: devise, sym: devise, dec: 2 };
    const g = ref.gammes.find(x => x.nom === project.gamme) || ref.gammes[1];
    const ctx = {
      pays, devise, sym: dv.sym, dec: num(dv.dec, 2), gammeK: num(g.k, 1), gamme: g.nom,
      tva: num(forc.tva, pays.tva),
      methode: forc.methode || project.methode || pays.methode,
      kmat: num(forc.kmat, pays.kmat), kmo: num(forc.kmo, pays.kmo),
      taux: num(forc.taux, pays.taux),
      fc: num(forc.fc, pays.fc), fg: num(forc.fg, pays.fg), b: num(forc.b, pays.b),
      rg: num(pays.rg, 0), caution: num(pays.caution, 0),
      tauxForceManquant: devise !== pays.devise && (forc.taux === undefined || forc.taux === null || forc.taux === "")
    };
    ctx.kglob = (1 + ctx.fc) * (1 + ctx.fg) * (1 + ctx.b);
    // lots retenus
    const lotOv = settings.lots || {};
    ctx.lots = {};
    ref.lots.concat(settings.extraLots || []).forEach(l0 => {
      const l = Object.assign({}, l0, lotOv[l0.code] || {});
      const kmat = num(l.kmat, ctx.kmat);
      const r = {
        code: l.code, lib: l.lib,
        kmat, kmatGE: num(l.kmatGE, kmat), kmo: num(l.kmo, ctx.kmo),
        K: (1 + num(l.fc, ctx.fc)) * (1 + num(l.fg, ctx.fg)) * (1 + num(l.b, ctx.b)),
        taux: ctx.taux * num(l.metier, 1)
      };
      ctx.lots[l.code] = r;
    });
    ctx.blocs = {};
    ref.blocs.concat(settings.extraBlocs || [], project.blocsPerso || []).forEach(b => { ctx.blocs[b.code] = b; });
    ctx.prixMode = project.prixMode === "saisie" ? "saisie" : "auto";
    // articles (référence + surcharges + articles ajoutés)
    const artOv = settings.articles || {};
    ctx.articles = {};
    ref.articles.concat(settings.extraArticles || []).forEach(a0 => {
      const ov = artOv[a0.ref];
      const a = Object.assign({}, a0, ov || {});
      a.p = Object.assign({}, a0.p || {}, (ov && ov.p) || {});
      ctx.articles[a.ref] = a;
    });
    return ctx;
  }

  // Calcule une ligne. line = {bloc, ref, q, puForce, libre:{des,u,pu,h,ge}}
  function computeLine(ctx, line, methodeOverride) {
    const meth = methodeOverride || ctx.methode;
    const art = line.libre ? Object.assign({ ref: "", p: {} }, line.libre) : ctx.articles[line.ref];
    const out = { line, ok: true, errors: [] };
    if (!art) { out.ok = false; out.errors.push("ref"); }
    const bloc = ctx.blocs[line.bloc];
    const lotCode = bloc ? bloc.lot : null;
    const lot = lotCode ? ctx.lots[lotCode] : null;
    if (!bloc) out.errors.push("bloc");
    out.lot = lotCode;
    out.des = line.des || (art ? art.des : "Référence inconnue");
    out.u = (line.u !== undefined && line.u !== null && line.u !== "") ? line.u : (art ? art.u : "");
    const q = num(line.q, 0);
    let pu, found = true;
    out.puSaisi = line.puForce !== undefined && line.puForce !== null && line.puForce !== "";
    out.puManquant = false;
    if (out.puSaisi) pu = Number(line.puForce);
    else if (line.libre) { pu = num(line.libre.pu, 0); out.puSaisi = line.libre.pu !== undefined && line.libre.pu !== null && line.libre.pu !== ""; }
    else if (ctx.prixMode === "saisie") { pu = 0; out.puManquant = true; }
    else {
      const raw = art ? art.p[ctx.devise] : undefined;
      if (raw === undefined || raw === null || raw === "") { found = false; pu = 0; }
      else pu = Number(raw) * ctx.gammeK;
    }
    out.prixTrouve = found;
    const h = art ? num(art.h, 0) : 0;
    const ge = art ? !!art.ge : false;
    const L = lot || { kmat: ctx.kmat, kmatGE: ctx.kmat, kmo: ctx.kmo, K: ctx.kglob, taux: ctx.taux };
    const coefMat = meth === "COEF" ? (ge ? L.kmatGE : L.kmat) : L.K;
    const coefMO = meth === "COEF" ? L.kmo : L.K;
    const taux = L.taux;
    out.q = q; out.pu = pu; out.h = h; out.taux = taux; out.coefMat = coefMat; out.coefMO = coefMO; out.ge = ge;
    out.totalMat = q * pu * coefMat;
    out.heures = q * h;
    out.totalMO = out.heures * taux * coefMO;
    out.pvCalc = roundTo(pu * coefMat + h * taux * coefMO, ctx.dec);
    const forced = line.pvForce !== undefined && line.pvForce !== null && line.pvForce !== "";
    out.pvSaisi = forced;
    out.pvManquant = false;
    out.pv = forced ? Number(line.pvForce) : out.pvCalc;
    if (forced) {
      // répartition fournitures / M.O. au prorata du prix calculé
      const ratio = out.pvCalc > 0 ? out.pv / out.pvCalc : 0;
      if (out.pvCalc > 0) { out.totalMat *= ratio; out.totalMO *= ratio; }
      else { out.totalMat = q * out.pv; out.totalMO = 0; }
    }
    if (!found && forced) out.prixTrouve = true;
    out.total = q * out.pv;
    out.dsU = pu + h * taux;
    out.ds = q * out.dsU;
    return out;
  }

  function computeProject(ctx, project, methodeOverride) {
    const rows = (project.lines || []).map(l => computeLine(ctx, l, methodeOverride));
    const byLot = {}, byBloc = {};
    const T = { mat: 0, heures: 0, mo: 0, ds: 0, ht: 0 };
    rows.forEach(r => {
      [[byLot, r.lot || "?"], [byBloc, r.line.bloc || "?"]].forEach(([m, k]) => {
        const o = m[k] || (m[k] = { mat: 0, heures: 0, mo: 0, ds: 0, ht: 0, n: 0 });
        o.mat += r.totalMat; o.heures += r.heures; o.mo += r.totalMO; o.ds += r.ds; o.ht += r.total; o.n++;
      });
      T.mat += r.totalMat; T.heures += r.heures; T.mo += r.totalMO; T.ds += r.ds; T.ht += r.total;
    });
    T.tva = roundTo(T.ht * ctx.tva, ctx.dec);
    T.ttc = T.ht + T.tva;
    const s = num(project.surface, 0);
    T.htM2 = s > 0 ? T.ht / s : 0;
    T.ttcM2 = s > 0 ? T.ttc / s : 0;
    T.coefMoyen = T.ds > 0 ? T.ht / T.ds : 0;
    T.partMO = T.ht > 0 ? T.mo / T.ht : 0;
    T.rg = roundTo(T.ttc * ctx.rg, ctx.dec);
    T.caution = roundTo(T.ttc * ctx.caution, ctx.dec);
    return { rows, byLot, byBloc, T };
  }

  function ratioRange(ctx) {
    const p = ctx.pays, g = ctx.gamme;
    if (g === "Économique") return [p.eMin, p.eMax];
    if (g === "Haut de gamme") return [p.hMin, p.hMax];
    return [p.mMin, p.mMax];
  }

  function controls(ctx, project, res) {
    const c = [];
    const q = res.rows.filter(r => r.q > 0);
    const noPrice = q.filter(r => !r.prixTrouve).length;
    const unknown = res.rows.filter(r => r.errors.includes("ref")).length;
    const badBloc = res.rows.filter(r => r.errors.includes("bloc")).length;
    const zeroQ = res.rows.filter(r => !(r.q > 0)).length;
    c.push({ k: "Références inconnues", v: unknown, s: unknown ? "err" : "ok" });
    c.push({ k: "Blocs inconnus", v: badBloc, s: badBloc ? "err" : "ok" });
    c.push({ k: "Lignes sans prix dans la devise " + ctx.devise, v: noPrice, s: noPrice ? "err" : "ok" });
    c.push({ k: "Lignes sans quantité", v: zeroQ, s: zeroQ ? "info" : "ok" });
    const puMiss = q.filter(r => r.puManquant).length;
    if (ctx.prixMode === "saisie") c.push({ k: "Lignes quantifiées sans prix d'achat saisi", v: puMiss, s: puMiss ? "err" : "ok" });
    if (ctx.tauxForceManquant) c.push({ k: "Devise différente du pays : forcer le taux horaire", v: 1, s: "warn" });
    const [mn, mx] = ratioRange(ctx);
    if (ctx.devise === ctx.pays.devise && mn && mx && num(project.surface, 0) > 0) {
      const v = res.T.ttcM2;
      c.push({ k: "TTC/m² dans la fourchette " + ctx.gamme.toLowerCase() + " du pays", v, range: [mn, mx], s: (v >= mn && v <= mx) ? "ok" : "warn" });
    }
    return c;
  }

  const api = { roundTo, context, computeLine, computeProject, controls, ratioRange };
  if (typeof module !== "undefined") module.exports = api; else root.Engine = api;
})(this);
