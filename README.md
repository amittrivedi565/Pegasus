# Pegasus Website

Marketing website for **Pegasus**, an enterprise technology company. Built with plain HTML, CSS and JavaScript — no frameworks or build step.

## Structure

```
.
├── index.html          # Home page
├── css/
│   └── styles.css      # Global styles & design tokens
├── js/
│   └── main.js         # Site scripts (mobile nav, etc.)
├── assets/
│   ├── images/         # Logos, photos
│   └── icons/          # SVG icons
└── docs/               # Design references (not deployed)
```

## Run locally

Open `index.html` in a browser, or serve the folder:

```sh
python3 -m http.server 8000
```

Then visit http://localhost:8000.

## Industry pages

`construction.html` and `hospitality.html` are generated from one shared template, so they stay consistent.
To change their content, edit the page's section in `tools/industry-pages/gen_industry.py`, then run from the site root:

```sh
python3 tools/industry-pages/gen_industry.py all
```

The navbar and footer are copied from `index.html` each time, so re-run it after changing those too.

## SmartHomes page

`smarthomes.html` is the dark, luxury page for Pegasus SmartHomes (styles in `css/smarthomes.css`).
Edit its content in `tools/smarthomes/gen_smarthomes.py`, then run from the site root:

```sh
python3 tools/smarthomes/gen_smarthomes.py
```

