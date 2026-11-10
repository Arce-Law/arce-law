# Arce Law website

A static, bilingual (English/Spanish) site for GitHub Pages. Plain HTML, CSS and a little vanilla JS. Nothing to install and nothing for the server to build.

- `/en/…` and `/es/…`: every page in both languages, with a header toggle that keeps you on the same page
- `/index.html`: sends visitors to their language (saved choice, then browser language)
- `assets/css/styles.css`: all styles. Colors are tokens at the top of the file
- `assets/js/main.js`: mobile menu, form submission, small reveal animation
- `tools/`: **optional** generator. All copy lives in `tools/content.py`; run `python3 tools/build_site.py` to regenerate every page, `sitemap.xml` and `robots.txt` (Python 3, standard library only)

**Editing:** either edit `tools/content.py` and re-run the build (recommended, so both languages and all 20 pages stay in sync), or edit the HTML directly. If you edit HTML by hand, don't re-run the build afterwards or your edits will be overwritten.

**Preview locally:** `python3 -m http.server 8000`, then open http://localhost:8000/

See **PLACEHOLDERS.md** for everything that still needs client confirmation.

## Deploy to GitHub Pages with a custom domain
1. Push this folder to a GitHub repository (the site files must be at the repo root).
2. In the repo, go to **Settings → Pages → Build and deployment**, set **Source: Deploy from a branch**, choose **`main` / `(root)`**, and save.
3. **Custom domain (at launch):** while previewing, the site runs at its github.io address with no `CNAME` file. To go live, enter `www.arce-law.com` under Settings → Pages → Custom domain and save. GitHub adds the `CNAME` file for you (pull it before editing locally).
4. **DNS** (at the domain registrar):
   - `CNAME` record: `www` → `<your-github-username>.github.io`
   - `A` records for the apex `arce-law.com`: `185.199.108.153`, `185.199.109.153`, `185.199.110.153`, `185.199.111.153` (optional `AAAA`: `2606:50c0:8000::153`, `…8001::153`, `…8002::153`, `…8003::153`)
   - **Keep the existing MX records** so email keeps working.
5. Wait for DNS to propagate (minutes to a few hours), then check **Enforce HTTPS** in Settings → Pages.
6. Recommended: verify the domain under your GitHub account settings (Pages → verified domains) to prevent takeover.
7. Submit `https://www.arce-law.com/sitemap.xml` in Google Search Console, and set up 301 redirects from the old site's URLs if any of them have search traffic.

Links are relative, so the site also works at `https://<user>.github.io/<repo>/` before the domain is connected. Only the 404 page needs the custom domain to load its styles.
