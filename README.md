# Pegasus Website

Marketing website for **Pegasus**, an enterprise technology company. Built with plain HTML, CSS and JavaScript — no frameworks or build step.

## Structure

```
.
├── public/                 # The deployed site — everything in here is published
│   ├── index.html          # Home page
│   ├── construction.html   # Generated (tools/industry-pages)
│   ├── hospitality.html    # Generated (tools/industry-pages)
│   ├── smarthomes.html     # Generated (tools/smarthomes)
│   ├── _headers            # Cloudflare response headers
│   ├── css/                # Global styles & design tokens, smarthomes.css
│   ├── js/                 # Site scripts (mobile nav, etc.)
│   └── assets/             # Logos, photos, favicons
├── tools/                  # Page generators + SEO (not deployed)
├── docs/                   # Design references (not deployed)
├── src/worker.js           # Routes smarthomes.mypegasus.in to the SmartHomes page
└── wrangler.jsonc          # Cloudflare config: serves public/ + the worker
```

## Run locally

Serve the `public` folder:

```sh
python3 -m http.server 8000 -d public
```

Then visit http://localhost:8000.

## Industry pages

`construction.html` and `hospitality.html` are generated from one shared template, so they stay consistent.
To change their content, edit the page's section in `tools/industry-pages/gen_industry.py`, then run:

```sh
python3 tools/industry-pages/gen_industry.py all
```

The navbar and footer are copied from `public/index.html` each time, so re-run it after changing those too.

## SmartHomes page

`smarthomes.html` is the dark, luxury page for Pegasus SmartHomes (styles in `public/css/smarthomes.css`).
Edit its content in `tools/smarthomes/gen_smarthomes.py`, then run:

```sh
python3 tools/smarthomes/gen_smarthomes.py
```

## SmartHomes subdomain

The SmartHomes page lives at **https://smarthomes.mypegasus.in/**. `src/worker.js` serves it at the subdomain root and
301-redirects `mypegasus.in/smarthomes` there. Links from the SmartHomes page to other pages point at `https://mypegasus.in/`
(handled in `gen_smarthomes.py`). The subdomain is attached as a custom domain on the Worker in the Cloudflare dashboard.

## SEO

`tools/seo/seo.py` holds each page's title, description, canonical URL, share image and structured data (JSON-LD).
The page generators apply it automatically; after editing `public/index.html` or anything in `seo.py`, run:

```sh
python3 tools/seo/seo.py                      # index.html, 404.html, sitemap.xml, robots.txt, share images
python3 tools/industry-pages/gen_industry.py all
python3 tools/smarthomes/gen_smarthomes.py
```

`src/worker.js` gives every page one address (https, no `www`, no `.html`) with 301 redirects, and missing URLs get `public/404.html`.
After the first deploy, add both `mypegasus.in` and `smarthomes.mypegasus.in` in Google Search Console and submit `https://mypegasus.in/sitemap.xml`.

## Deploy (Cloudflare)

Only the `public/` folder is published; `docs/` and `tools/` never are. There is no build step.

- **Cloudflare Workers, Git-connected (current setup):** connect the repo; Cloudflare reads `wrangler.jsonc` and runs `npx wrangler deploy`. Leave the build command empty.
- **From your machine:** `npx wrangler login` once, then `npx wrangler deploy`.

`public/_headers` sets basic security headers and a 7-day cache on `assets/`.
