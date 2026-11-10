# Placeholders to fill in or confirm with the client

Every unconfirmed item shows on the site as a yellow **[CONFIRM WITH CLIENT: …]** tag, so nothing ships by accident.
To find them all: `grep -rn "CONFIRM WITH CLIENT" tools/ en/ es/`

Edit values in `tools/content.py` (settings at the top) or `tools/build_site.py` (page templates), then run `python3 tools/build_site.py`.

## Global settings (`tools/content.py`, top of file)
| Item | Current value | Action |
|---|---|---|
| WhatsApp number | `15555550123` (fake) | Real number, digits only, with country code (e.g. `5213334084797` or `12062009513`) |
| Formspree form ID | `YOUR_FORM_ID` | Create a form at formspree.io, set the notification email, paste the ID. The form shows a "not connected" message until you do |
| Email | `info@arce-law.com` | Confirm once the domain mailbox exists (it currently goes nowhere) |
| Time zone for hours | shown as a placeholder (header, footer, contact) | Replace the `TZ = ph("time zone")` line, e.g. `TZ = "(Pacific Time)"` / `"(hora del Centro de México)"` |
| Site URL | `https://www.arce-law.com` | Confirm www vs. apex domain (must match the custom domain set in Settings → Pages at launch) |

## Content and credentials (do not publish unverified)
- **Home, credentials strip:** bar admissions and licenses (Mexican cédula profesional, U.S. state bar), memberships, years in practice
- **About:** firm history, founder story, office locations
- **About, "Where we help":** exactly which matters are handled in which jurisdiction, and by whom
- **Team** (`TEAM_MEMBERS` in `tools/content.py`). Names, roles and the two founders' bios come from the old site.
  - **Gilberto Arce:** WSBA license **type and number**. His old bio calls him a "Foreign Law Consultant" and also says he was "admitted to the Washington Bar". In Washington, a Foreign Law Consultant (APR 14) is a limited license to advise on the law of the foreign country (Mexico), **not** U.S. law. Check the WSBA lawyer directory. If he holds that limited license, the U.S. Immigration and Washington LLC pages need rethinking. Photo cropped from the old site; a proper headshot would be better.
  - **Alejandra Gomez Arce:** cédula profesional number and a **headshot**. The old site's only photo of her is a family beach photo that includes a child, so I didn't use it.
  - **Ivan Bono, Fernanda Zavala:** the old site has only name and title. Need bio, education, cédula/licensing and photo.
  - Copyedits to confirm: "Jus Sempen Loquitur" corrected to "Jus Semper Loquitur"; "defense council" corrected to "counsel"; the ABA described as a membership (the old text said "admitted").
- **U.S. Immigration page:** the name and state bar admission of the licensed attorney (or DOJ-accredited representative) who handles immigration. **Important:** in the U.S. only licensed attorneys and accredited representatives may give immigration legal advice. Washington's Immigration Service Fraud Prevention Act (RCW 19.154) strictly limits what non-attorneys can offer. If no U.S.-licensed attorney is on the team, this page must be rewritten or removed.
- **Washington LLC page:** who handles business formation and their Washington licensing
- **Contact:** free-consultation terms (length, format, limits), plus office address(es) or remove that block
- **Testimonials (home page, hidden):** only real, permission-granted reviews. Remove `hidden` from the section to show it. Check bar advertising rules first
- **Wording check:** the copy uses "lawyer/abogado" (for SEO terms like "abogado en Jalisco") and "attorney-client relationship." Confirm this is accurate for the firm in each country.

## Images (`assets/img/`, replace with the same filename or update the references)
| File | Use | Size |
|---|---|---|
| `about-office-or-founder-1200x800-PLACEHOLDER.jpg` | About page | 1200×800 (3:2) |
| `team-{alejandra-gomez-arce,ivan-bono,fernanda-zavala}-800x1000-PLACEHOLDER.jpg` | Team headshots (then set `photo` in `TEAM_MEMBERS`) | 800×1000 (4:5) |

The home hero (`home-hero-papel-picado-1200x900.jpg`) is the client's own photo.

Compress photos before uploading (e.g. squoosh.app, quality ~70, under ~150 KB each). If you rename a file, also update its alt text in `tools/build_site.py`.

## Structured data / SEO
- Add the office `address` to the `LegalService` schema in `org_schema()` (`tools/build_site.py`) once confirmed. Also create or claim **Google Business Profile** listings for both offices; for local search ("abogado en Jalisco") that matters more than anything on the site.
- Social links: a commented-out block is in the footer (`footer()` in `build_site.py`). Uncomment it when real URLs exist.

## Recommended additions
- **Privacy notice / Aviso de Privacidad.** The form collects personal data, and Mexico's data protection law requires an aviso de privacidad. A commented-out footer link is ready for it.
- Logo files: `assets/logo-dark.png` (header), `assets/logo-white.png` (footer), `assets/logo.jpg` (search/schema), `assets/img/og-share-image-1200x630.jpg` and `assets/apple-touch-icon.png` were all made from the client's logo. A vector (SVG/AI/PDF) version from the client would make them sharper.
