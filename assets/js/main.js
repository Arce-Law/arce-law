/* Arce Law — small progressive-enhancement script. Site works without it. */
(function () {
  "use strict";
  var doc = document.documentElement;
  doc.classList.add("js");
  var lang = doc.lang && doc.lang.indexOf("es") === 0 ? "es" : "en";

  /* Mobile menu */
  var menuBtn = document.querySelector(".menu-btn");
  var nav = document.getElementById("primary-nav");
  if (menuBtn && nav) {
    menuBtn.addEventListener("click", function () {
      var open = menuBtn.getAttribute("aria-expanded") === "true";
      menuBtn.setAttribute("aria-expanded", String(!open));
      nav.classList.toggle("is-open", !open);
    });
  }

  /* Services submenu (click/tap + keyboard; Escape closes) */
  var subBtns = document.querySelectorAll(".submenu-btn");
  function closeAll(except) {
    subBtns.forEach(function (b) {
      if (b === except) return;
      b.setAttribute("aria-expanded", "false");
      var m = document.getElementById(b.getAttribute("aria-controls"));
      if (m) m.classList.remove("is-open");
    });
  }
  subBtns.forEach(function (btn) {
    var menu = document.getElementById(btn.getAttribute("aria-controls"));
    btn.addEventListener("click", function (e) {
      e.stopPropagation();
      var open = btn.getAttribute("aria-expanded") === "true";
      closeAll(btn);
      btn.setAttribute("aria-expanded", String(!open));
      menu.classList.toggle("is-open", !open);
    });
  });
  document.addEventListener("click", function (e) {
    if (window.matchMedia("(min-width: 1024px)").matches && !e.target.closest(".has-submenu")) closeAll();
  });
  document.addEventListener("keydown", function (e) {
    if (e.key !== "Escape") return;
    var openBtn = document.querySelector('.submenu-btn[aria-expanded="true"]');
    if (openBtn) { closeAll(); openBtn.focus(); return; }
    if (menuBtn && menuBtn.getAttribute("aria-expanded") === "true") { menuBtn.click(); menuBtn.focus(); }
  });

  /* Remember language choice (used by the root "/" redirect) */
  document.querySelectorAll("[data-set-lang]").forEach(function (a) {
    a.addEventListener("click", function () {
      try { localStorage.setItem("arce-lang", a.getAttribute("data-set-lang")); } catch (err) {}
    });
  });

  /* Footer year */
  var y = document.getElementById("year");
  if (y) y.textContent = String(new Date().getFullYear());

  /* Subtle reveal on scroll */
  var reveals = document.querySelectorAll(".reveal");
  if ("IntersectionObserver" in window && reveals.length) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        if (en.isIntersecting) { en.target.classList.add("is-visible"); io.unobserve(en.target); }
      });
    }, { rootMargin: "0px 0px -8% 0px" });
    reveals.forEach(function (el) { io.observe(el); });
  } else {
    reveals.forEach(function (el) { el.classList.add("is-visible"); });
  }

  /* Contact form: submit to Formspree via fetch, fall back to normal POST */
  var form = document.getElementById("intake-form");
  if (form && window.fetch) {
    var status = document.getElementById("form-status");
    var msgs = {
      en: {
        sending: "Sending…",
        ok: "Thank you. We received your message and will get back to you as soon as possible.",
        err: "Sorry, something went wrong. Please call us or message us on WhatsApp instead.",
        notConfigured: "The form isn't connected yet (Formspree ID missing). Please call or WhatsApp us."
      },
      es: {
        sending: "Enviando…",
        ok: "Gracias. Recibimos su mensaje y nos comunicaremos con usted a la brevedad.",
        err: "Lo sentimos, ocurrió un error. Por favor llámenos o escríbanos por WhatsApp.",
        notConfigured: "El formulario aún no está conectado (falta el ID de Formspree). Por favor llámenos o escríbanos por WhatsApp."
      }
    }[lang];
    form.addEventListener("submit", function (e) {
      e.preventDefault();
      if (!form.checkValidity()) { form.reportValidity(); return; }
      var btn = form.querySelector('button[type="submit"]');
      status.className = "form-status";
      if (form.action.indexOf("YOUR_FORM_ID") !== -1) {
        status.textContent = msgs.notConfigured; status.className = "form-status err"; return;
      }
      var label = btn.textContent;
      btn.disabled = true; btn.textContent = msgs.sending;
      fetch(form.action, { method: "POST", body: new FormData(form), headers: { Accept: "application/json" } })
        .then(function (r) {
          if (!r.ok) throw new Error("bad status");
          form.reset();
          status.textContent = msgs.ok; status.className = "form-status ok";
        })
        .catch(function () { status.textContent = msgs.err; status.className = "form-status err"; })
        .finally(function () { btn.disabled = false; btn.textContent = label; status.focus(); });
    });
  }
})();
