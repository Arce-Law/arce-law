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
| Site URL | `https://www.arce-law.com` | Confirm www vs. apex domain (must match `CNAME`) |

## Content and credentials (do not publish unverified)
- **Home, credentials strip:** bar admissions and licenses (Mexican cédula profesional, U.S. state bar), memberships, years in practice
- **About:** firm history, founder story, office locations
- **About, "Where we help":** exactly which matters are handled in which jurisdiction, and by whom
- **Team (4 card slots):** photo, name, role, education, bar/licensing number or "non-attorney staff", languages, short bio. Add or remove `<article class="member">` blocks to match the real team
- **U.S. Immigration page:** the name and state bar admission of the licensed attorney (or DOJ-accredited representative) who handles immigration. **Important:** in the U.S. only licensed attorneys and accredited representatives may give immigration legal advice. Washington's Immigration Service Fraud Prevention Act (RCW 19.154) strictly limits what non-attorneys can offer. If no U.S.-licensed attorney is on the team, this page must be rewritten or removed.
- **Washington LLC page:** who handles business formation and their Washington licensing
- **Contact:** free-consultation terms (length, format, limits), plus office address(es) or remove that block
- **Testimonials (home page, hidden):** only real, permission-granted reviews. Remove `hidden` from the section to show it. Check bar advertising rules first
- **Wording check:** the copy uses "lawyer/abogado" (for SEO terms like "abogado en Jalisco") and "attorney-client relationship." Confirm this is accurate for the firm in each country.

## Images (`assets/img/`, replace with the same filename or update the references)
| File | Use | Size |
|---|---|---|
| `../logo.jpg` | Header, footer and schema logo. **Currently a temporary text logo; drop the real one in** | ~height 88px+ for retina |
| `home-hero-client-consultation-1200x900-PLACEHOLDER.jpg` | Home hero | 1200×900 (4:3) |
| `about-office-or-founder-1200x800-PLACEHOLDER.jpg` | About page | 1200×800 (3:2) |
| `team-member-{1-4}-portrait-800x1000-PLACEHOLDER.jpg` | Team headshots | 800×1000 (4:5) |
| `og-share-image-1200x630-PLACEHOLDER.jpg` | Link previews (Facebook, WhatsApp, LinkedIn) | 1200×630 |

Compress photos before uploading (e.g. squoosh.app, quality ~70, under ~150 KB each). If you rename a file, also update its alt text in `tools/build_site.py`.

## Structured data / SEO
- Add the office `address` to the `LegalService` schema in `org_schema()` (`tools/build_site.py`) once confirmed. Also create or claim **Google Business Profile** listings for both offices; for local search ("abogado en Jalisco") that matters more than anything on the site.
- Social links: a commented-out block is in the footer (`footer()` in `build_site.py`). Uncomment it when real URLs exist.

## Recommended additions
- **Privacy notice / Aviso de Privacidad.** The form collects personal data, and Mexico's data protection law requires an aviso de privacidad. A commented-out footer link is ready for it.
- An `apple-touch-icon.png` (180×180) made from the real logo.
