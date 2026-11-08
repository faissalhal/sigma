/* SIGMA ICC – menu mobile, filtres des projets, formulaire de contact */
(function () {
  "use strict";
  var btn = document.getElementById("menu-btn"), nav = document.getElementById("nav");
  if (btn && nav) btn.addEventListener("click", function () {
    var o = nav.classList.toggle("ouvert");
    btn.setAttribute("aria-expanded", o ? "true" : "false");
  });

  // Filtres de la page Projets
  var filtres = document.querySelectorAll(".filtres button");
  filtres.forEach(function (b) {
    b.addEventListener("click", function () {
      var f = b.getAttribute("data-f");
      filtres.forEach(function (x) { x.setAttribute("aria-pressed", x === b ? "true" : "false"); });
      document.querySelectorAll(".projet").forEach(function (p) {
        p.hidden = !(f === "tous" || p.getAttribute("data-cat") === f);
      });
    });
  });

  // Formulaire de devis : envoi vers la feuille Google existante, puis page de confirmation
  document.querySelectorAll("form.formulaire").forEach(function (form) {
    form.addEventListener("submit", function (ev) {
      ev.preventDefault();
      var etat = form.querySelector(".message-etat");
      var bouton = form.querySelector("button[type=submit]");
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
