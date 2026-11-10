#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generates the static Arce Law site from tools/content.py.

    python3 tools/build_site.py

Writes /en/**, /es/**, /index.html, /404.html, /sitemap.xml and /robots.txt
in the repository root. Standard library only. GitHub Pages serves the output
as-is; this script never runs on the server.
"""
import json
import os
import sys
from datetime import date
from urllib.parse import quote

sys.path.insert(0, os.path.dirname(__file__))
from content import *  # noqa: E402,F403

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
TODAY = date.today().isoformat()

# ---------------------------------------------------------------- icons (inline SVG, stroke style)
ICONS = {
    "home": '<path d="M3 10.5 12 3l9 7.5"/><path d="M5 9.5V21h14V9.5"/><path d="M10 21v-6h4v6"/>',
    "family": '<circle cx="9" cy="7" r="3.5"/><path d="M2.5 21v-1.5A5.5 5.5 0 0 1 8 14h2a5.5 5.5 0 0 1 5.5 5.5V21"/><circle cx="17.5" cy="9" r="2.5"/><path d="M17 14.2a4.5 4.5 0 0 1 4.5 4.3V21"/>',
    "stamp": '<path d="M14 3H6a1 1 0 0 0-1 1v16a1 1 0 0 0 1 1h12a1 1 0 0 0 1-1V8z"/><path d="M14 3v5h5"/><circle cx="12" cy="13.5" r="2.5"/><path d="m10.6 15.6-1 3.4 2.4-1 2.4 1-1-3.4"/>',
    "scales": '<path d="M12 3v18"/><path d="M7 21h10"/><path d="M4 7h16"/><path d="M7 7 4 14a3 3 0 0 0 6 0z"/><path d="m17 7-3 7a3 3 0 0 0 6 0z"/>',
    "globe": '<circle cx="12" cy="12" r="9"/><path d="M3 12h18"/><path d="M12 3a14 14 0 0 1 0 18 14 14 0 0 1 0-18"/>',
    "building": '<path d="M4 21V5a1 1 0 0 1 1-1h9a1 1 0 0 1 1 1v16"/><path d="M15 9h4a1 1 0 0 1 1 1v11"/><path d="M3 21h18"/><path d="M8 8h3M8 12h3M8 16h3"/>',
    "phone": '<path d="M5 4h4l2 5-2.5 1.5a11 11 0 0 0 5 5L15 13l5 2v4a2 2 0 0 1-2 2A16 16 0 0 1 3 6a2 2 0 0 1 2-2"/>',
    "arrow": '<path d="M5 12h14"/><path d="m13 6 6 6-6 6"/>',
    "chev": '<path d="m6 9 6 6 6-6"/>',
    "menu": '<path d="M4 7h16M4 12h16M4 17h16"/>',
    "close": '<path d="M6 6l12 12M18 6 6 18"/>',
    "lang": '<circle cx="12" cy="12" r="9"/><path d="M3 12h18"/><path d="M12 3a14 14 0 0 1 0 18 14 14 0 0 1 0-18"/>',
    "clock": '<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/>',
    "mail": '<rect x="3" y="5" width="18" height="14" rx="2"/><path d="m3 7 9 6 9-6"/>',
    "chat": '<path d="M21 12a8 8 0 0 1-11.8 7L4 20.5 5.5 15.6A8 8 0 1 1 21 12z"/>',
    "languages": '<path d="M4 5h8M8 3v2M6 5c0 4 2.5 7 6 8"/><path d="M11 5c-.5 3-2.5 6-7 8"/><path d="m13 21 4-9 4 9M14.5 18h5"/>',
    "map": '<path d="M9 4 3 6v14l6-2 6 2 6-2V4l-6 2z"/><path d="M9 4v14M15 6v14"/>',
    "device": '<rect x="6" y="2.5" width="12" height="19" rx="2.5"/><path d="M11 18.5h2"/>',
    "clipboard": '<rect x="5" y="4" width="14" height="17" rx="2"/><path d="M9 4V3h6v1"/><path d="M9 11h6M9 15h4"/>',
}
# WhatsApp-style glyph (filled)
WA_SVG = ('<svg viewBox="0 0 24 24" aria-hidden="true" focusable="false" fill="currentColor">'
          '<path d="M12 2a10 10 0 0 0-8.6 15.1L2 22l5-1.3A10 10 0 1 0 12 2zm0 18.2a8.2 8.2 0 0 1-4.2-1.2l-.3-.2-3 .8.8-2.9-.2-.3A8.2 8.2 0 1 1 12 20.2z"/>'
          '<path d="M16.6 14.1c-.3-.1-1.5-.7-1.7-.8-.2-.1-.4-.1-.6.1l-.8 1c-.1.2-.3.2-.5.1a6.7 6.7 0 0 1-3.3-2.9c-.2-.4.2-.4.7-1.3.1-.2 0-.3 0-.4l-.8-1.8c-.2-.5-.4-.4-.6-.4h-.5a1 1 0 0 0-.7.3 3 3 0 0 0-.9 2.2 5.2 5.2 0 0 0 1.1 2.7 11.8 11.8 0 0 0 4.5 4c1.7.7 2.3.8 3.2.6a2.7 2.7 0 0 0 1.7-1.2 2.2 2.2 0 0 0 .2-1.2c-.1-.1-.3-.2-.5-.3z"/></svg>')


def icon(name, cls=""):
    c = f' class="{cls}"' if cls else ""
    return (f'<svg{c} viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" '
            f'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false">{ICONS[name]}</svg>')


# ---------------------------------------------------------------- URL helpers
def path_of(key, lang):
    slug = SLUGS[key][lang]
    return f"/{lang}/" + (f"{slug}/" if slug else "")


def abs_url(key, lang):
    return SITE_URL + path_of(key, lang)


def rel(from_key, to_path):
    """Relative link from the page `from_key` to an absolute site path, so the site
    also works when previewed from a sub-folder (e.g. user.github.io/repo/)."""
    depth = 1 if not SLUGS[from_key]["en"] else 2   # /xx/ = 1, /xx/slug/ = 2
    prefix = "../" * depth
    return prefix + to_path.lstrip("/")


def tel_link(which, lang, cls=""):
    t = UI[lang]
    if which == "us":
        return f'<a href="tel:{PHONE_US_TEL}" class="{cls}">{icon("phone")}<span>{t["us_label"]} {PHONE_US_DISPLAY}</span></a>'
    return f'<a href="tel:{PHONE_MX_TEL}" class="{cls}">{icon("phone")}<span>{t["mx_label"]} <span class="cc">+52 </span>{PHONE_MX_DISPLAY}</span></a>'


def wa_url(lang):
    return f"https://wa.me/{WHATSAPP_NUMBER}?text={quote(UI[lang]['wa_text'])}"


# ---------------------------------------------------------------- head
def head(key, lang, extra_ld=None):
    t = UI[lang]
    title, desc = SEO[key][lang]
    other = t["other"]
    a = rel(key, "/assets/")
    ld = [org_schema(lang)] if key in ("home", "contact", "about") else []
    if key != "home":
        ld.append(breadcrumb_schema(key, lang))
    if extra_ld:
        ld.append(extra_ld)
    ld_html = "".join(
        f'\n<script type="application/ld+json">{json.dumps(x, ensure_ascii=False, separators=(",", ":"))}</script>'
        for x in ld)
    return f"""<!doctype html>
<html lang="{'es-MX' if lang == 'es' else 'en-US'}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{abs_url(key, lang)}">
<link rel="alternate" hreflang="{lang}" href="{abs_url(key, lang)}">
<link rel="alternate" hreflang="{other}" href="{abs_url(key, other)}">
<link rel="alternate" hreflang="x-default" href="{abs_url(key, 'en')}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="{FIRM}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{abs_url(key, lang)}">
<meta property="og:image" content="{SITE_URL}{OG_IMAGE}">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:locale" content="{t['locale']}">
<meta property="og:locale:alternate" content="{UI[other]['locale']}">
<meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#1D1A17">
<link rel="icon" href="{a}favicon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="{a}apple-touch-icon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Source+Serif+4:ital,opsz,wght@0,8..60,600;1,8..60,600&display=swap">
<link rel="stylesheet" href="{a}css/styles.css">
<script src="{a}js/main.js" defer></script>{ld_html}
</head>
<body>
<a class="skip-link" href="#main">{t['skip']}</a>
"""


# ---------------------------------------------------------------- schema.org
def org_schema(lang):
    t = UI[lang]
    return {
        "@context": "https://schema.org",
        "@type": "LegalService",
        "@id": SITE_URL + "/#firm",
        "name": FIRM,
        "url": abs_url("home", lang),
        "logo": SITE_URL + "/assets/logo.jpg",
        "image": SITE_URL + OG_IMAGE,
        "description": SEO["home"][lang][1],
        "email": EMAIL,
        "telephone": PHONE_US_TEL,
        "contactPoint": [
            {"@type": "ContactPoint", "telephone": PHONE_US_TEL, "contactType": "customer service",
             "areaServed": "US", "availableLanguage": ["English", "Spanish"]},
            {"@type": "ContactPoint", "telephone": PHONE_MX_TEL, "contactType": "customer service",
             "areaServed": "MX", "availableLanguage": ["Spanish", "English"]},
        ],
        "areaServed": [
            {"@type": "State", "name": "Jalisco", "containedInPlace": {"@type": "Country", "name": "Mexico"}},
            {"@type": "State", "name": "Michoacán", "containedInPlace": {"@type": "Country", "name": "Mexico"}},
            {"@type": "State", "name": "Colima", "containedInPlace": {"@type": "Country", "name": "Mexico"}},
            {"@type": "State", "name": "Washington", "containedInPlace": {"@type": "Country", "name": "United States"}},
            {"@type": "State", "name": "Arizona", "containedInPlace": {"@type": "Country", "name": "United States"}},
        ],
        "availableLanguage": ["en", "es"],
        "knowsLanguage": ["en", "es"],
        "openingHoursSpecification": [{
            "@type": "OpeningHoursSpecification",
            "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"],
            "opens": "08:30", "closes": "17:00"}],
        "knowsAbout": [PRACTICE[k][lang]["name"] for k in PRACTICE_KEYS],
    }


def breadcrumb_schema(key, lang):
    items = [{"@type": "ListItem", "position": 1, "name": UI[lang]["home"], "item": abs_url("home", lang)}]
    name = PRACTICE[key][lang]["name"] if key in PRACTICE else UI[lang].get(key, SEO[key][lang][0])
    items.append({"@type": "ListItem", "position": 2, "name": name, "item": abs_url(key, lang)})
    return {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": items}


def faq_schema(faqs):
    return {"@context": "https://schema.org", "@type": "FAQPage",
            "mainEntity": [{"@type": "Question", "name": q,
                            "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in faqs]}


# ---------------------------------------------------------------- header / footer
def header(key, lang):
    t = UI[lang]
    other = t["other"]
    r = lambda p: rel(key, p)  # noqa: E731
    cur = lambda k: ' aria-current="page"' if k == key else ""  # noqa: E731
    sub = "\n".join(
        f'          <li><a href="{r(path_of(k, lang))}"{cur(k)}>{PRACTICE[k][lang]["name"]}</a></li>'
        for k in PRACTICE_KEYS)
    return f"""<div class="utility">
  <div class="wrap">
    <span class="hours">{icon("clock")}&nbsp;{t['hours_short']}{'&nbsp;' + TZ if TZ else ''}</span>
    {tel_link("us", lang)}
    {tel_link("mx", lang)}
  </div>
</div>
<header class="site-header">
  <div class="wrap header-inner">
    <a class="brand" href="{r(path_of('home', lang))}" aria-label="{FIRM}, {t['home'].lower()}">
      <img src="{r('/assets/logo-dark.png')}" alt="{FIRM}" width="95" height="44">
    </a>
    <nav id="primary-nav" class="primary-nav" aria-label="{t['menu']}">
      <ul class="nav-list">
        <li class="has-submenu">
          <button class="submenu-btn" type="button" aria-expanded="false" aria-controls="submenu-services">{t['services']} {icon("chev")}</button>
          <ul class="submenu" id="submenu-services">
{sub}
          </ul>
        </li>
        <li><a href="{r(path_of('about', lang))}"{cur('about')}>{t['about']}</a></li>
        <li><a href="{r(path_of('history', lang))}"{cur('history')}>{t['history']}</a></li>
        <li><a href="{r(path_of('team', lang))}"{cur('team')}>{t['team']}</a></li>
        <li><a href="{r(path_of('contact', lang))}"{cur('contact')}>{t['contact']}</a></li>
        <li class="nav-cta"><a class="btn btn-primary" href="{r(path_of('contact', lang))}">{t['cta']}</a></li>
      </ul>
    </nav>
    <a class="lang-toggle" href="{r(path_of(key, other))}" hreflang="{other}" lang="{other}" data-set-lang="{other}" aria-label="{t['switch_aria']}">{icon("lang")}<span>{t['other_short']}</span></a>
    <a class="btn btn-primary header-cta" href="{r(path_of('contact', lang))}">{t['cta']}</a>
    <button class="menu-btn" type="button" aria-expanded="false" aria-controls="primary-nav">
      <span class="visually-hidden">{t['menu']}</span>{icon("menu", "i-open")}{icon("close", "i-close")}
    </button>
  </div>
</header>
"""


def footer(key, lang):
    t = UI[lang]
    r = lambda p: rel(key, p)  # noqa: E731
    services = "\n".join(
        f'          <li><a href="{r(path_of(k, lang))}">{PRACTICE[k][lang]["name"]}</a></li>' for k in PRACTICE_KEYS)
    return f"""<footer class="site-footer">
  <div class="wrap">
    <div class="footer-grid">
      <div>
        <a class="footer-logo" href="{r(path_of('home', lang))}"><img src="{r('/assets/logo-white.png')}" alt="{FIRM}" width="104" height="48" loading="lazy"></a>
        <p>{t['footer_blurb']}</p>
        <p><a href="{r(path_of('home', t['other']))}" hreflang="{t['other']}" lang="{t['other']}" data-set-lang="{t['other']}">{t['other_label']}</a></p>
        <!--
          SOCIAL LINKS: uncomment and add real URLs when the client provides them.
          <ul class="social" aria-label="Social media">
            <li><a href="https://www.facebook.com/REPLACE" rel="noopener">Facebook</a></li>
            <li><a href="https://www.instagram.com/REPLACE" rel="noopener">Instagram</a></li>
            <li><a href="https://www.linkedin.com/company/REPLACE" rel="noopener">LinkedIn</a></li>
          </ul>
        -->
      </div>
      <nav aria-label="{t['footer_services']}">
        <h2>{t['footer_services']}</h2>
        <ul>
{services}
        </ul>
      </nav>
      <nav aria-label="{t['footer_firm']}">
        <h2>{t['footer_firm']}</h2>
        <ul>
          <li><a href="{r(path_of('about', lang))}">{t['about']}</a></li>
          <li><a href="{r(path_of('history', lang))}">{t['history']}</a></li>
          <li><a href="{r(path_of('team', lang))}">{t['team']}</a></li>
          <li><a href="{r(path_of('contact', lang))}">{t['contact']}</a></li>
          <!-- <li><a href="PRIVACY-NOTICE-URL">Privacy notice / Aviso de privacidad</a></li>  See PLACEHOLDERS.md -->
        </ul>
      </nav>
      <div>
        <h2>{t['footer_contact']}</h2>
        <ul>
          <li><a href="tel:{PHONE_US_TEL}">{t['us_label']} {PHONE_US_DISPLAY}</a></li>
          <li><a href="tel:{PHONE_MX_TEL}">{t['mx_label']} +52 {PHONE_MX_DISPLAY}</a></li>
          <li><a href="mailto:{EMAIL}">{EMAIL}</a></li>
          <li style="padding-top:6px">{t['hours_days']}<br>{t['hours_time']}{' ' + TZ if TZ else ''}</li>
        </ul>
      </div>
    </div>
    <div class="disclaimer">
      <p>{t['disclaimer']}</p>
      <p class="copyright">© <span id="year">{date.today().year}</span> {FIRM}. {t['rights']}</p>
    </div>
  </div>
</footer>
<a class="wa-float" href="{wa_url(lang)}" target="_blank" rel="noopener" aria-label="{t['wa_aria']}">{WA_SVG}<span class="wa-label">{t['wa_label']}</span></a>
</body>
</html>
"""


def cta_band(key, lang):
    t = UI[lang]
    return f"""<section class="section" aria-labelledby="cta-title">
  <div class="wrap">
    <div class="cta-band reveal">
      <h2 id="cta-title">{t['cta_title']}</h2>
      <p>{t['cta_text']}</p>
      <div class="btn-row">
        <a class="btn btn-light" href="{rel(key, path_of('contact', lang))}">{t['cta']}</a>
        <a class="btn btn-ghost-light" href="tel:{PHONE_US_TEL}">{icon("phone")}{t['us_label']} {PHONE_US_DISPLAY}</a>
        <a class="btn btn-ghost-light" href="tel:{PHONE_MX_TEL}">{icon("phone")}{t['mx_label']} {PHONE_MX_DISPLAY}</a>
      </div>
    </div>
  </div>
</section>
"""


def breadcrumb(key, lang, name):
    t = UI[lang]
    return f"""<nav class="breadcrumb" aria-label="Breadcrumb">
      <ol><li><a href="{rel(key, path_of('home', lang))}">{t['home']}</a></li><li aria-current="page">{name}</li></ol>
    </nav>"""


def service_cards(key, lang, keys=PRACTICE_KEYS, heading_level=3):
    t = UI[lang]
    out = []
    for k in keys:
        p = PRACTICE[k]
        c = p[lang]
        tag = {"mx": t["mx_label"], "us": t["us_label"], "both": f"{t['mx_label']} · {t['us_label']}"}[p["country"]]
        icls = "icon us" if p["country"] == "us" else "icon"
        out.append(f"""      <article class="card reveal">
        <div class="{icls}">{icon(p['icon'])}</div>
        <span class="tag">{tag}</span>
        <h{heading_level}>{c['name']}</h{heading_level}>
        <p>{c['card']}</p>
        <a class="card-link" href="{rel(key, path_of(k, lang))}">{t['learn']}<span class="visually-hidden">: {c['name']}</span>{icon('arrow')}</a>
      </article>""")
    return "\n".join(out)


def write(path, html):
    full = os.path.join(ROOT, path.lstrip("/"))
    if full.endswith("/"):
        full += "index.html"
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w", encoding="utf-8") as f:
        f.write(html)


# ================================================================ PAGES
HOME = {
    "en": {
        "eyebrow": "Mexico · United States",
        "h1": "Legal help in Mexico and the U.S., <em>in your language</em>",
        "lead": "Do you live in the U.S. but have a property, a family matter or paperwork in Mexico? We take care of it for you, often without you needing to travel. We also help with U.S. immigration and Washington business formation.",
        "call": "Call now",
        "img_alt": "Colorful papel picado banners strung between the towers of a historic stone church in Mexico",
        "mx": "Mexico:", "us": "U.S.:",
        "svc_eyebrow": "Practice areas", "svc_h": "How we can help",
        "svc_p": "Matters in two countries, handled by one bilingual team.",
        "how_eyebrow": "Simple process", "how_h": "Getting started is easy",
        "how": [
            ("Tell us what's happening", "Call, send a WhatsApp message or fill out the form. Your first consultation is free."),
            ("Get a clear plan", "We explain your options, the steps and the costs in plain language before you decide."),
            ("We handle it", "We take care of the paperwork and procedures and keep you updated until it's done."),
        ],
        "trust_eyebrow": "Why Arce Law", "trust_h": "A team you can trust on both sides of the border",
        "trust": [
            ("languages", "Fully bilingual", "Every conversation, document explanation and update in English or Spanish, whichever you prefer."),
            ("map", "Two countries, one team", "Mexico and U.S. matters are often connected. We see the whole picture."),
            ("device", "Help from a distance", "Phone, WhatsApp, video calls and email, so you can handle matters in Mexico from the U.S."),
            ("clipboard", "Clear next steps", "You'll always know what's happening, what comes next and what we need from you."),
        ],
    },
    "es": {
        "eyebrow": "México · Estados Unidos",
        "h1": "Asesoría legal en México y Estados Unidos, <em>en su idioma</em>",
        "lead": "¿Vive en Estados Unidos y tiene una propiedad, un asunto familiar o un trámite pendiente en México? Nosotros nos encargamos, muchas veces sin que usted tenga que viajar. También le ayudamos con inmigración en EE. UU. y con la apertura de empresas en Washington.",
        "call": "Llamar ahora",
        "img_alt": "Papel picado de colores colgado entre las torres de una iglesia histórica de cantera en México",
        "mx": "México:", "us": "EE. UU.:",
        "svc_eyebrow": "Áreas de práctica", "svc_h": "¿En qué le podemos ayudar?",
        "svc_p": "Asuntos en dos países, atendidos por un mismo equipo bilingüe.",
        "how_eyebrow": "Proceso sencillo", "how_h": "Empezar es muy fácil",
        "how": [
            ("Cuéntenos su caso", "Llámenos, escríbanos por WhatsApp o llene el formulario. Su primera consulta es gratuita."),
            ("Reciba un plan claro", "Le explicamos sus opciones, los pasos y los costos con palabras sencillas antes de que decida."),
            ("Nosotros nos encargamos", "Hacemos los trámites y gestiones y le mantenemos informado hasta terminar."),
        ],
        "trust_eyebrow": "Por qué Arce Law", "trust_h": "Un equipo de confianza de los dos lados de la frontera",
        "trust": [
            ("languages", "Totalmente bilingües", "Cada llamada, explicación y actualización en español o en inglés, como usted prefiera."),
            ("map", "Dos países, un solo equipo", "Los asuntos en México y en EE. UU. muchas veces están relacionados. Vemos el panorama completo."),
            ("device", "Atención a distancia", "Teléfono, WhatsApp, videollamada y correo, para resolver sus asuntos en México desde Estados Unidos."),
            ("clipboard", "Pasos claros", "Siempre sabrá qué está pasando, qué sigue y qué necesitamos de usted."),
        ],
    },
}


def page_home(lang):
    t, h = UI[lang], HOME[lang]
    key = "home"
    how = "\n".join(f"        <li class=\"reveal\"><h3>{a}</h3><p>{b}</p></li>" for a, b in h["how"])
    trust = "\n".join(f"""        <div class="trust-item reveal">{icon(i)}<h3>{a}</h3><p>{b}</p></div>""" for i, a, b in h["trust"])
    body = f"""<main id="main">
<section class="hero">
  <div class="wrap hero-grid">
    <div>
      <span class="eyebrow">{h['eyebrow']}</span>
      <h1>{h['h1']}</h1>
      <p class="lead">{h['lead']}</p>
      <div class="btn-row">
        <a class="btn btn-primary" href="{rel(key, path_of('contact', lang))}">{t['cta']}</a>
        <a class="btn btn-outline" href="tel:{PHONE_US_TEL if lang == 'en' else PHONE_MX_TEL}">{icon('phone')}{h['call']}</a>
      </div>
      <div class="juris">
        <span><strong>{h['mx']}</strong>&nbsp;Jalisco, Michoacán, Colima</span>
        <span class="us"><strong>{h['us']}</strong>&nbsp;Washington, Arizona</span>
      </div>
    </div>
    <div class="hero-media">
      <img src="{rel(key, '/assets/img/home-hero-papel-picado-1200x900.jpg')}" alt="{h['img_alt']}" width="1200" height="900" fetchpriority="high">
    </div>
  </div>
</section>

<section class="section section-sand" aria-labelledby="services-title">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">{h['svc_eyebrow']}</span>
      <h2 id="services-title">{h['svc_h']}</h2>
      <p>{h['svc_p']}</p>
    </div>
    <div class="card-grid cols-3">
{service_cards(key, lang)}
    </div>
  </div>
</section>

<section class="section" aria-labelledby="how-title">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">{h['how_eyebrow']}</span>
      <h2 id="how-title">{h['how_h']}</h2>
    </div>
    <ol class="steps steps-row">
{how}
    </ol>
  </div>
</section>

<section class="section section-dark" aria-labelledby="trust-title">
  <div class="wrap">
    <div class="section-head">
      <span class="eyebrow">{h['trust_eyebrow']}</span>
      <h2 id="trust-title">{h['trust_h']}</h2>
    </div>
    <div class="trust-grid">
{trust}
    </div>
  </div>
</section>


{cta_band(key, lang)}
</main>
"""
    write(path_of(key, lang), head(key, lang) + header(key, lang) + body + footer(key, lang))


def page_practice(key, lang):
    t = UI[lang]
    p = PRACTICE[key]
    c = p[lang]
    items = "\n".join(f"          <li><strong>{a}</strong><span>{b}</span></li>" for a, b in c["items"])
    steps = "\n".join(f"        <li class=\"reveal\"><h3>{a}</h3><p>{b}</p></li>" for a, b in c["steps"])
    faqs = "\n".join(f"""      <details>
        <summary>{q}</summary>
        <div class="answer"><p>{a}</p></div>
      </details>""" for q, a in c["faqs"])
    intro = "\n".join(f"        <p>{x}</p>" for x in c["intro"])
    related = "\n".join(f'      <li><a href="{rel(key, path_of(k, lang))}">{PRACTICE[k][lang]["name"]}</a></li>'
                        for k in PRACTICE_KEYS if k != key)
    extra_note = ""
    if key == "llc":
        extra_note = f"""
        <div class="callout"><p>{'Government filing fees are set by the state and federal agencies and change from time to time. We will confirm current fees before filing.' if lang == 'en' else 'Las cuotas de registro las fijan las dependencias estatales y federales y cambian de vez en cuando. Le confirmamos las cuotas vigentes antes de presentar.'}</p></div>"""
    icls = "page-hero-icon"
    body = f"""<main id="main">
<section class="page-hero">
  <div class="wrap">
    {breadcrumb(key, lang, c['name'])}
    <div class="{icls}">{icon(p['icon'])}</div>
    <span class="eyebrow">{c['name']}</span>
    <h1>{c['h1']}</h1>
    <p class="lead">{c['lead']}</p>
    <p class="served"><strong>{t['served']}:</strong> {c['served']}</p>
    <div class="btn-row">
      <a class="btn btn-primary" href="{rel(key, path_of('contact', lang))}">{t['cta']}</a>
      <a class="btn btn-outline" href="{wa_url(lang)}" target="_blank" rel="noopener">{icon('chat')}WhatsApp</a>
    </div>
  </div>
</section>

<section class="section" aria-labelledby="overview-title">
  <div class="wrap split">
    <div class="prose reveal">
      <h2 id="overview-title">{t['what_we_do']}</h2>
{intro}{extra_note}
    </div>
    <ul class="check-list reveal">
{items}
    </ul>
  </div>
</section>

<section class="section section-sand" aria-labelledby="process-title">
  <div class="wrap narrow">
    <div class="section-head">
      <span class="eyebrow">{t['process']}</span>
      <h2 id="process-title">{'Step by step' if lang == 'en' else 'Paso a paso'}</h2>
    </div>
    <ol class="steps">
{steps}
    </ol>
  </div>
</section>

<section class="section" aria-labelledby="faq-title">
  <div class="wrap narrow">
    <h2 id="faq-title">{t['faq']}</h2>
    <div class="faq">
{faqs}
    </div>
  </div>
</section>

{cta_band(key, lang)}

<section class="section" style="padding-top:0" aria-labelledby="related-title">
  <div class="wrap">
    <h2 id="related-title" style="font-size:1.3rem">{t['related']}</h2>
    <ul class="related">
{related}
    </ul>
  </div>
</section>
</main>
"""
    write(path_of(key, lang), head(key, lang, faq_schema(c["faqs"])) + header(key, lang) + body + footer(key, lang))


ABOUT = {
    "en": {
        "eyebrow": "About us", "h1": "Legal help that bridges Mexico and the United States",
        "lead": "Arce Law helps individuals, families and businesses with legal matters in Mexico and the U.S., in English or Spanish, wherever they live.",
        "story_h": "Our story",
        "story": HISTORY["en"]["paras"][:2],
        "values_h": "How we work",
        "values": [
            ("Clarity", "We explain the law and the process in plain language so you can make informed decisions."),
            ("Responsiveness", "We keep you updated and answer your questions by phone, WhatsApp, video call or email."),
            ("Honesty", "We tell you what's realistic, including when a case isn't worth pursuing."),
        ],
        "where_h": "Locations, hours & contact",
        "hours_h": "Hours", "contact_h": "Contact",
        "mx_h": "Mexico", "us_h": "United States",
        "mx_list": ["Jalisco", "Michoacán", "Colima"],
        "us_list": ["Washington State", "Arizona"],
        "team_link": "Meet the team",
    },
    "es": {
        "eyebrow": "Nosotros", "h1": "Asesoría legal que une a México y Estados Unidos",
        "lead": "Arce Law ayuda a personas, familias y empresas con asuntos legales en México y Estados Unidos, en español o en inglés, vivan donde vivan.",
        "story_h": "Nuestra historia",
        "story": HISTORY["es"]["paras"][:2],
        "values_h": "Cómo trabajamos",
        "values": [
            ("Claridad", "Le explicamos la ley y el proceso con palabras sencillas para que tome decisiones informadas."),
            ("Atención oportuna", "Le mantenemos informado y respondemos sus dudas por teléfono, WhatsApp, videollamada o correo."),
            ("Honestidad", "Le decimos lo que es realista, incluso cuando un asunto no conviene."),
        ],
        "where_h": "Ubicación, horario y contacto",
        "hours_h": "Horario", "contact_h": "Contacto",
        "mx_h": "México", "us_h": "Estados Unidos",
        "mx_list": ["Jalisco", "Michoacán", "Colima"],
        "us_list": ["Estado de Washington", "Arizona"],
        "team_link": "Conozca al equipo",
    },
}


def page_about(lang):
    key = "about"
    a = ABOUT[lang]
    story = "\n".join(f"      <p>{x}</p>" for x in a["story"])
    vals = "\n".join(f'      <div class="value reveal"><h3>{x}</h3><p>{y}</p></div>' for x, y in a["values"])
    li = lambda xs: "".join(f"<li>{x}</li>" for x in xs)  # noqa: E731
    body = f"""<main id="main">
<section class="page-hero">
  <div class="wrap">
    {breadcrumb(key, lang, UI[lang]['about'])}
    <span class="eyebrow">{a['eyebrow']}</span>
    <h1>{a['h1']}</h1>
    <p class="lead">{a['lead']}</p>
  </div>
</section>

<section class="section" aria-labelledby="story-title">
  <div class="wrap narrow">
    <div class="prose reveal">
      <h2 id="story-title">{a['story_h']}</h2>
{story}
      <p><a href="{rel(key, path_of('history', lang))}">{HISTORY[lang]['read_more']} →</a><br><a href="{rel(key, path_of('team', lang))}">{a['team_link']} →</a></p>
    </div>
  </div>
</section>

<section class="section section-sand" aria-labelledby="values-title">
  <div class="wrap">
    <div class="section-head"><h2 id="values-title">{a['values_h']}</h2></div>
    <div class="values">
{vals}
    </div>
  </div>
</section>

<section class="section" aria-labelledby="where-title">
  <div class="wrap">
    <div class="section-head"><h2 id="where-title">{a['where_h']}</h2></div>
    <div class="juris-table juris-4">
      <div class="juris-box reveal"><h3>{a['mx_h']}</h3><ul>{li(a['mx_list'])}</ul></div>
      <div class="juris-box us reveal"><h3>{a['us_h']}</h3><ul>{li(a['us_list'])}</ul></div>
      <div class="juris-box plain reveal"><h3>{a['hours_h']}</h3>
        <p>{UI[lang]['hours_days']}<br>{UI[lang]['hours_time']}</p>
        {'<p class="tz">' + TZ + '</p>' if TZ else ''}</div>
      <div class="juris-box plain reveal"><h3>{a['contact_h']}</h3>
        <p><a href="tel:{PHONE_US_TEL}">{UI[lang]['us_label']}: {PHONE_US_DISPLAY}</a><br>
        <a href="tel:{PHONE_MX_TEL}">{UI[lang]['mx_label']}: +52 {PHONE_MX_DISPLAY}</a><br>
        <a href="mailto:{EMAIL}">{EMAIL}</a></p></div>
    </div>
  </div>
</section>

{cta_band(key, lang)}
</main>
"""
    write(path_of(key, lang), head(key, lang) + header(key, lang) + body + footer(key, lang))


TEAM = {
    "en": {"eyebrow": "Our team", "h1": "Meet the people behind Arce Law",
           "lead": "A bilingual team serving clients in Mexico and the United States.",
           "role": "Role", "creds": "Education & credentials", "lic": "Bar / licensing", "langs": "Languages",
           "alt": "Photo coming soon", "note": "Team bios", "full": "Read full bio"},
    "es": {"eyebrow": "Nuestro equipo", "h1": "Conozca al equipo de Arce Law",
           "lead": "Un equipo bilingüe al servicio de clientes en México y Estados Unidos.",
           "role": "Cargo", "creds": "Formación y credenciales", "lic": "Cédula / licencia", "langs": "Idiomas",
           "alt": "Fotografía próximamente", "note": "Biografías", "full": "Leer biografía completa"},
}


def page_team(lang):
    key = "team"
    tm = TEAM[lang]
    cards = []
    for m in TEAM_MEMBERS:
        d = m[lang]
        if m["photo"]:
            img = f'<img src="{rel(key, "/assets/img/" + m["photo"])}" alt="{m["name"]}" width="800" height="1000" loading="lazy">'
        else:
            img = (f'<img src="{rel(key, "/assets/img/" + m["placeholder"])}" alt="{tm["alt"]}: {m["name"]}" '
                   f'width="800" height="1000" loading="lazy">')
        full = ""
        if d.get("bio"):
            paras = "".join(f"<p>{x}</p>" for x in d["bio"])
            full = f'''
          <details class="bio">
            <summary>{tm['full']}<span class="visually-hidden">: {m['name']}</span></summary>
            <div class="bio-text">{paras}</div>
          </details>'''
        summary = f'<p class="summary">{d["summary"]}</p>' if d.get("summary") else ""
        rows = "".join(f"\n            <div><dt>{lbl}</dt><dd>{d[f]}</dd></div>"
                       for lbl, f in ((tm["creds"], "education"), (tm["lic"], "licensing"), (tm["langs"], "languages")) if d.get(f))
        cards.append(f"""      <article class="member reveal">
        {img}
        <div class="member-body">
          <h3>{m['name']}</h3>
          <p class="role">{d['role']}</p>
          {summary}
          <dl>{rows}
          </dl>{full}
        </div>
      </article>""")
    body = f"""<main id="main">
<section class="page-hero">
  <div class="wrap">
    {breadcrumb(key, lang, UI[lang]['team'])}
    <span class="eyebrow">{tm['eyebrow']}</span>
    <h1>{tm['h1']}</h1>
    <p class="lead">{tm['lead']}</p>
  </div>
</section>
<section class="section" aria-label="{tm['note']}">
  <div class="wrap">
    <!-- Team members are defined in TEAM_MEMBERS in tools/content.py -->
    <div class="team-grid">
{chr(10).join(cards)}
    </div>
  </div>
</section>
{cta_band(key, lang)}
</main>
"""
    write(path_of(key, lang), head(key, lang) + header(key, lang) + body + footer(key, lang))


CONTACT = {
    "en": {
        "eyebrow": "Contact", "h1": "Request your free consultation",
        "lead": "Tell us a little about your situation and we'll get back to you. Prefer to talk now? Call or send us a WhatsApp message.",
        "form_h": "Intake form",
        "name": "Full name", "phone": "Phone", "phone_hint": "Include country code if outside the U.S.",
        "email": "Email", "pref": "Preferred language", "en": "English", "es": "Spanish",
        "service": "Service needed", "choose": "Choose one…", "notsure": "Not sure / Other",
        "where": "Where is the matter?", "w_us": "United States", "w_mx": "Mexico", "w_both": "Both", "w_ns": "Not sure",
        "msg": "Briefly describe your situation", "msg_hint": "Please don't include confidential details yet.",
        "consent": "I understand that sending this form does not create an attorney-client relationship and that I should not include confidential information.",
        "send": "Send request", "req": "required",
        "call_h": "Call us", "wa_h": "WhatsApp", "wa_btn": "Message us on WhatsApp",
        "hours_h": "Hours", "email_h": "Email",
        "subject": "New consultation request (EN) – arce-law.com",
    },
    "es": {
        "eyebrow": "Contacto", "h1": "Solicite su consulta gratuita",
        "lead": "Cuéntenos un poco sobre su situación y nos comunicaremos con usted. ¿Prefiere hablar ahora? Llámenos o escríbanos por WhatsApp.",
        "form_h": "Formulario de contacto",
        "name": "Nombre completo", "phone": "Teléfono", "phone_hint": "Incluya la lada internacional si no está en EE. UU.",
        "email": "Correo electrónico", "pref": "Idioma de preferencia", "en": "Inglés", "es": "Español",
        "service": "Servicio que necesita", "choose": "Seleccione una opción…", "notsure": "No estoy seguro / Otro",
        "where": "¿Dónde es el asunto?", "w_us": "Estados Unidos", "w_mx": "México", "w_both": "En ambos", "w_ns": "No estoy seguro",
        "msg": "Describa brevemente su situación", "msg_hint": "Por favor no incluya todavía datos confidenciales.",
        "consent": "Entiendo que enviar este formulario no crea una relación abogado-cliente y que no debo incluir información confidencial.",
        "send": "Enviar solicitud", "req": "obligatorio",
        "call_h": "Llámenos", "wa_h": "WhatsApp", "wa_btn": "Escríbanos por WhatsApp",
        "hours_h": "Horario de atención", "email_h": "Correo",
        "subject": "Nueva solicitud de consulta (ES) – arce-law.com",
    },
}


def page_contact(lang):
    key = "contact"
    t, c = UI[lang], CONTACT[lang]
    req = f'<span class="req" aria-hidden="true">*</span><span class="visually-hidden"> ({c["req"]})</span>'
    opts = "\n".join(f'              <option value="{PRACTICE[k]["en"]["name"]}">{PRACTICE[k][lang]["name"]}</option>'
                     for k in PRACTICE_KEYS)

    def choice(name, val, label, checked=False, required=False):
        i = f"{name}-{val.lower().replace(' ', '-').replace('.', '')}"
        return (f'<div class="choice"><input type="radio" id="{i}" name="{name}" value="{val}"'
                f'{" checked" if checked else ""}{" required" if required else ""}><label for="{i}">{label}</label></div>')

    body = f"""<main id="main">
<section class="page-hero">
  <div class="wrap">
    {breadcrumb(key, lang, t['contact'])}
    <span class="eyebrow">{c['eyebrow']}</span>
    <h1>{c['h1']}</h1>
    <p class="lead">{c['lead']}</p>
  </div>
</section>
<section class="section">
  <div class="wrap contact-grid">
    <div class="form-card">
      <h2 style="font-size:1.5rem">{c['form_h']}</h2>
      <!-- Formspree: replace YOUR_FORM_ID in tools/content.py (FORMSPREE_ID) or directly in this action URL. -->
      <form id="intake-form" action="https://formspree.io/f/{FORMSPREE_ID}" method="POST" novalidate>
        <input type="hidden" name="_subject" value="{c['subject']}">
        <input type="hidden" name="page_language" value="{lang}">
        <div class="hp" aria-hidden="true"><label for="gotcha">Leave blank</label><input type="text" id="gotcha" name="_gotcha" tabindex="-1" autocomplete="off"></div>

        <div class="field">
          <label for="f-name">{c['name']} {req}</label>
          <input type="text" id="f-name" name="name" autocomplete="name" required>
        </div>
        <div class="field-row">
          <div class="field">
            <label for="f-phone">{c['phone']} {req}<span class="hint">{c['phone_hint']}</span></label>
            <input type="tel" id="f-phone" name="phone" autocomplete="tel" inputmode="tel" required>
          </div>
          <div class="field">
            <label for="f-email">{c['email']} {req}<span class="hint spacer" aria-hidden="true">&nbsp;</span></label>
            <input type="email" id="f-email" name="email" autocomplete="email" required>
          </div>
        </div>
        <fieldset>
          <legend>{c['pref']} {req}</legend>
          <div class="choices">
            {choice('preferred_language', 'Spanish', c['es'], checked=(lang == 'es'), required=True)}
            {choice('preferred_language', 'English', c['en'], checked=(lang == 'en'))}
          </div>
        </fieldset>
        <div class="field">
          <label for="f-service">{c['service']} {req}</label>
          <select id="f-service" name="service" required>
              <option value="">{c['choose']}</option>
{opts}
              <option value="Not sure / Other">{c['notsure']}</option>
          </select>
        </div>
        <fieldset>
          <legend>{c['where']} {req}</legend>
          <div class="choices">
            {choice('matter_location', 'U.S.', c['w_us'], required=True)}
            {choice('matter_location', 'Mexico', c['w_mx'])}
            {choice('matter_location', 'Both', c['w_both'])}
            {choice('matter_location', 'Not sure', c['w_ns'])}
          </div>
        </fieldset>
        <div class="field">
          <label for="f-msg">{c['msg']} {req}<span class="hint">{c['msg_hint']}</span></label>
          <textarea id="f-msg" name="message" required></textarea>
        </div>
        <div class="consent">
          <input type="checkbox" id="f-consent" name="acknowledgment" value="yes" required>
          <label for="f-consent">{c['consent']}</label>
        </div>
        <button class="btn btn-primary" type="submit" style="width:100%">{c['send']}</button>
        <div id="form-status" class="form-status" role="status" aria-live="polite" tabindex="-1"></div>
      </form>
    </div>

    <aside class="contact-side">
      <div class="info-card">
        <h2>{c['call_h']}</h2>
        <a class="phone-link" href="tel:{PHONE_US_TEL}"><span class="pi">{icon('phone')}</span><span><small>{t['us_label']}</small><b>+1 {PHONE_US_DISPLAY}</b></span></a>
        <a class="phone-link" href="tel:{PHONE_MX_TEL}"><span class="pi">{icon('phone')}</span><span><small>{t['mx_label']}</small><b>+52 {PHONE_MX_DISPLAY}</b></span></a>
      </div>
      <div class="info-card">
        <h2>{c['wa_h']}</h2>
        <a class="btn btn-primary" style="width:100%;background:var(--wa)" href="{wa_url(lang)}" target="_blank" rel="noopener">{WA_SVG}{c['wa_btn']}</a>
      </div>
      <div class="info-card">
        <h2>{c['hours_h']}</h2>
        <dl class="hours-list">
          <dt>{t['hours_days']}</dt><dd>{t['hours_time']}</dd>
          <dt>{t['closed']}</dt><dd>{t['closed_v']}</dd>
        </dl>
        {'<p style="margin:10px 0 0;font-size:.92rem">' + TZ + '</p>' if TZ else ''}
      </div>
      <div class="info-card">
        <h2>{c['email_h']}</h2>
        <p style="margin:0"><a href="mailto:{EMAIL}">{EMAIL}</a></p>
      </div>
    </aside>
  </div>
</section>
</main>
"""
    write(path_of(key, lang), head(key, lang) + header(key, lang) + body + footer(key, lang))


# ---------------------------------------------------------------- root files
def page_root():
    html = f"""<!doctype html>
<html lang="es-MX">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{FIRM} | Legal Help in Mexico &amp; the U.S. / Asesoría Legal en México y EE. UU.</title>
<meta name="description" content="{SEO['home']['en'][1]}">
<link rel="canonical" href="{SITE_URL}/">
<link rel="alternate" hreflang="en" href="{abs_url('home', 'en')}">
<link rel="alternate" hreflang="es" href="{abs_url('home', 'es')}">
<link rel="alternate" hreflang="x-default" href="{SITE_URL}/">
<meta property="og:title" content="{FIRM}">
<meta property="og:description" content="{SEO['home']['en'][1]}">
<meta property="og:url" content="{SITE_URL}/">
<meta property="og:image" content="{SITE_URL}{OG_IMAGE}">
<link rel="icon" href="assets/favicon.svg" type="image/svg+xml">
<link rel="stylesheet" href="assets/css/styles.css">
<script>
  /* Send visitors to their language: saved choice first, then browser language. */
  (function () {{
    var l = null;
    try {{ l = localStorage.getItem("arce-lang"); }} catch (e) {{}}
    if (l !== "en" && l !== "es") {{
      var langs = navigator.languages || [navigator.language || "en"];
      l = String(langs[0] || "en").toLowerCase().indexOf("es") === 0 ? "es" : "en";
    }}
    location.replace(l + "/");
  }})();
</script>
</head>
<body>
<main class="chooser">
  <div>
    <img src="assets/logo-dark.png" alt="{FIRM}" width="139" height="64">
    <h1 style="font-size:1.6rem">Choose your language · Elija su idioma</h1>
    <div class="btn-row">
      <a class="btn btn-primary" href="es/" hreflang="es" lang="es">Español</a>
      <a class="btn btn-outline" href="en/" hreflang="en" lang="en">English</a>
    </div>
  </div>
</main>
</body>
</html>
"""
    write("/index.html", html)


def page_404():
    # 404 is served at any URL, so use absolute paths here.
    html = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Page not found / Página no encontrada | {FIRM}</title>
<meta name="robots" content="noindex">
<link rel="icon" href="/assets/favicon.svg" type="image/svg+xml">
<link rel="stylesheet" href="/assets/css/styles.css">
</head>
<body>
<main class="chooser">
  <div>
    <img src="/assets/logo-dark.png" alt="{FIRM}" width="139" height="64">
    <h1 style="font-size:1.8rem">Page not found</h1>
    <p lang="es-MX" style="font-family:var(--font-serif);font-size:1.4rem;margin-top:-8px">Página no encontrada</p>
    <p style="color:var(--muted)">The page you're looking for doesn't exist. <span lang="es-MX">La página que busca no existe.</span></p>
    <div class="btn-row">
      <a class="btn btn-primary" href="/en/">Go to home</a>
      <a class="btn btn-outline" href="/es/" lang="es-MX">Ir al inicio</a>
    </div>
  </div>
</main>
</body>
</html>
"""
    write("/404.html", html)


def sitemap():
    rows = []
    for key in SLUGS:
        for lang in ("en", "es"):
            alts = "".join(
                f'\n    <xhtml:link rel="alternate" hreflang="{l}" href="{abs_url(key, l)}"/>' for l in ("en", "es"))
            alts += f'\n    <xhtml:link rel="alternate" hreflang="x-default" href="{abs_url(key, "en")}"/>'
            pri = "1.0" if key == "home" else ("0.8" if key in PRACTICE else "0.6")
            rows.append(f"""  <url>
    <loc>{abs_url(key, lang)}</loc>
    <lastmod>{TODAY}</lastmod>
    <priority>{pri}</priority>{alts}
  </url>""")
    xml = ('<?xml version="1.0" encoding="UTF-8"?>\n'
           '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">\n'
           + "\n".join(rows) + "\n</urlset>\n")
    write("/sitemap.xml", xml)
    write("/robots.txt", f"User-agent: *\nAllow: /\n\nSitemap: {SITE_URL}/sitemap.xml\n")


def page_history(lang):
    key = "history"
    h = HISTORY[lang]
    paras = "\n".join(f"      <p>{x}</p>" for x in h["paras"])
    body = f"""<main id="main">
<section class="page-hero">
  <div class="wrap">
    {breadcrumb(key, lang, UI[lang]['history'])}
    <span class="eyebrow">{h['eyebrow']}</span>
    <h1>{h['h1']}</h1>
  </div>
</section>
<section class="section">
  <div class="wrap narrow prose history-text reveal">
{paras}
      <p><a href="{rel(key, path_of('team', lang))}">{h['team_link']} →</a></p>
  </div>
</section>
{cta_band(key, lang)}
</main>
"""
    write(path_of(key, lang), head(key, lang) + header(key, lang) + body + footer(key, lang))


def main():
    for lang in ("en", "es"):
        page_home(lang)
        for k in PRACTICE_KEYS:
            page_practice(k, lang)
        page_about(lang)
        page_history(lang)
        page_team(lang)
        page_contact(lang)
    page_root()
    page_404()
    sitemap()
    print("Built", 2 * len(SLUGS), "pages + index.html, 404.html, sitemap.xml, robots.txt")


if __name__ == "__main__":
    main()
