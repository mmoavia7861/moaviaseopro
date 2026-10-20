# Moavia SEO Pro — Fast Multi-Page Digital Agency Website

A complete, responsive static marketing website for Moavia SEO Pro. Uses semantic HTML5, modern CSS and plain JavaScript—**no build framework, package manager, external font service, analytics tracker, or JavaScript dependency**.

## Pages

| URL / file | Purpose |
| --- | --- |
| `index.html` | Homepage, services, lead form, illustrative ROI calculator, pricing summary, scripted support |
| `services/seo.html` | SEO audit, on-page, off-page, technical, local and e-commerce SEO plus 3 pricing tiers |
| `services/web-development.html` | WordPress, custom builds, landing pages, e-commerce, maintenance plus 3 tiers |
| `services/meta-ads.html` | Facebook/Instagram, lead gen, catalogs, tracking plus 3 tiers |
| `services/google-ads.html` | Search, Display, Shopping, YouTube, conversion tracking plus 3 tiers |
| `about.html` | Story, mission, skills and values |
| `contact.html` | Lead contact form, WhatsApp, email, phone, socials, map placeholder |
| `privacy.html` | How basic client-side and optional hosting-provider processing works |

## Folder structure

```text
moavia-seo-pro-site/
├── index.html
├── about.html
├── contact.html
├── privacy.html
├── robots.txt
├── sitemap.xml
├── .nojekyll
├── netlify.toml
├── assets/
│   ├── css/styles.css
│   ├── js/main.js
│   └── images/
│       ├── moavia-logo.webp
│       ├── moavia-logo-256.png
│       └── favicon.png
├── services/
│   ├── seo.html
│   ├── web-development.html
│   ├── meta-ads.html
│   └── google-ads.html
└── scripts/build_pages.py
```

## Local preview

1. Unzip and open a terminal in the folder.
2. Run `python -m http.server 8000` (Windows may use `py -m http.server 8000`).
3. Open `http://localhost:8000/` in your browser.

Opening `index.html` directly also displays the site, but an HTTP server is preferred for testing form behavior.

## Edit content, pricing and SEO

- **Content, site-wide header/footer, page templates, 3-tier pricing, meta tags, canonical tags, schema and sitemap** are generated in `scripts/build_pages.py`. Modify this source and run:

  ```bash
  python scripts/build_pages.py
  ```

- Output files are normal, independently deployable HTML. If you edit generated HTML files directly, a later regeneration will overwrite those edits.
- **Design and responsive rules:** `assets/css/styles.css`.
- **Support widget, calculator, theme, mobile menu, forms:** `assets/js/main.js`.
- Logo images were optimized from the supplied brand logo. Replace their actual files to update branding.
- All prices are **indicative examples, quoted in USD**. Confirm before publishing. Advertising spend, hosting, domain registrations, software and third-party costs are additional.
- No real testimonials or case-study performance were provided; sections use clearly labeled placeholders/examples rather than fictitious reviews or fabricated results.
- The map is intentionally a placeholder because no verified physical business location was provided. Do not invent a map location or misleading location schema.

## SEO configuration — read before publishing

The starter's `SITE_URL` in `scripts/build_pages.py` is:

```python
SITE_URL = 'https://mmoavia7861.github.io/moaviaseopro/'
```

This project URL is a **deployment default only**; it does not mean the site is currently published there. All HTML canonicals, OG URLs, structured data identifiers, robots sitemap location, and sitemap URLs are generated from this variable.

When you own a custom domain, replace it with your final public canonical origin, such as:

```python
SITE_URL = 'https://www.your-owned-domain.com/'
```

Then run `python scripts/build_pages.py` **before deployment**. Use either www or apex consistently and arrange a 301 redirect from the other hostname through your host. Do not publish with a canonical URL pointing to a different site. Rebuild whenever the domain or paths change. Test the structured data with Schema.org Validator and Google's Rich Results Test (eligibility for specific rich results is not guaranteed). Google's FAQ rich-result display is restricted; markup does not ensure a search feature.

### `robots.txt` at a GitHub Pages project URL

At a project URL like `username.github.io/Repo/`, `robots.txt` sits at `/Repo/robots.txt`, **not** at the shared domain root. Search engines usually look for `https://username.github.io/robots.txt`. The XML sitemap URL inside it remains discoverable if submitted directly. With a custom apex/www domain mapped to this repository, `robots.txt` is served at the root as expected.

## GitHub Pages deployment

1. Create a new GitHub repository, named `moaviaseopro`.
2. Upload **the contents** of this folder into the repository root (not a second nested `moavia-seo-pro-site/` folder).
3. In **Settings → Pages**, select **Deploy from a branch**, `main`, root `/`, and Save.
4. On the default project URL, check the built path `https://USERNAME.github.io/REPOSITORY/`; ensure `SITE_URL` matches your real username and repository exactly. Rebuild if it does not.
5. Test all inner pages, links, forms, metadata and smartphone layout.

### Connect your owned .com to GitHub Pages

1. Purchase the `.com` through your chosen registrar. Add it under GitHub repository **Settings → Pages → Custom domain**.
2. If using `www`, create a DNS **CNAME** record (`www` → `YOUR-USERNAME.github.io`) at your registrar; use the **actual GitHub username** and host documentation.
3. If using the apex domain, configure GitHub's documented DNS `A`/`AAAA` records at your registrar (check GitHub's current addresses; do not copy potentially outdated IPs from a static README).
4. Optionally add a repository-root file `CNAME` containing **only** your owned domain name (e.g. `www.your-owned-domain.com`), if your Pages configuration does not already manage it.
5. Wait for DNS propagation and enable **Enforce HTTPS** in GitHub Pages once eligible.
6. Change `SITE_URL` to the **final HTTPS custom URL**, rerun the generator, commit changed files and verify canonicals + sitemap.

**Do not add an actual `CNAME` file with an example domain before you own and configure it.**

## Vercel deployment

Import the GitHub repository as a new Vercel project. It is a static site; choose **Other / no framework**, no build command, and publish the repository root. Add your owned domain in Vercel Domains and follow the DNS entries Vercel supplies. Update `SITE_URL`, rebuild and redeploy. Its default `.vercel.app` hostname should redirect to the canonical custom domain once configured.

## Netlify deployment and optional first-party form handling

Connect the repository to Netlify or drag-and-drop the folder. No build command is needed; publish directory is `.`. The included `netlify.toml` sets reasonable baseline security headers.

**Default contact form mode:** `assets/js/main.js` uses `FORM_PROVIDER = 'whatsapp'`. The validated form prepares a WhatsApp chat with the inquiry, then **the visitor must press Send in WhatsApp**. There is **no invisible backend submission**; it works for static GitHub Pages/Vercel/Netlify hosting.

**Native Netlify Forms mode:**

1. Deploy this repository to Netlify with Forms enabled. HTML forms are labeled `data-netlify="true"` with hidden `form-name` fields and honeypots.
2. Change `FORM_PROVIDER` in `assets/js/main.js` from `'whatsapp'` to `'netlify'`.
3. Redeploy and complete an end-to-end test. Review the site's Netlify **Forms** dashboard for stored submissions. Optional notifications (email etc.) require setup in Netlify.
4. Update on-page wording and privacy policy as appropriate to your final processing arrangement. WhatsApp language is the shipped default and shouldn't remain misleading after switching provider.

## Support assistant

The floating chat is **a small, fully functional scripted FAQ assistant** written in JavaScript. It answers known questions about services and pricing and links directly to WhatsApp. **It does not call an LLM or external AI API, is not generative AI and has no server-side human handoff**. To add genuine LLM responses, a secure backend and API integration would be required; no API key should be exposed in browser code.

## Privacy and operational notes

- Theme setting uses `localStorage`, if allowed by the browser.
- Default chat does not store messages or send them to a server.
- No cookies, analytics, marketing pixels or advertising tags are shipped.
- Contact forms use required consent checkboxes and client validation; WhatsApp is the external transmission service.
- Responsive CSS includes reduced-motion preferences and visible keyboard focus styles.
- Pricing, capabilities and case-study samples must be verified against actual business practices before launch.
- Do not invent a street address, customer ratings, Google reviews or measurable results. LocalBusiness structured data is present but the organization has no verified street address; local rich-result eligibility is not established.
- Performance is optimized for a small static site, but **a 95+ PageSpeed/Lighthouse score cannot be promised without real deployed-device tests**; inspect actual Core Web Vitals and hosting headers after going live.
