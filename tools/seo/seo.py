"""SEO for every page: titles, descriptions, canonical URLs, Open Graph/Twitter tags and JSON-LD.

The page generators call apply() on each page they write. Running this file directly
(python3 tools/seo/seo.py) also updates public/index.html and writes the 404 page,
sitemap.xml, robots.txt and the social share images.
"""
import datetime
import json
import os
import re
import subprocess

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.normpath(os.path.join(HERE, "..", ".."))
PUBLIC = os.path.join(ROOT, "public")

SITE = "https://mypegasus.in"
SH = "https://smarthomes.mypegasus.in"

ORG_ID = f"{SITE}/#organization"
WEBSITE_ID = f"{SITE}/#website"

ORG = {
    "@type": "Organization",
    "@id": ORG_ID,
    "name": "Pegasus",
    "url": f"{SITE}/",
    "logo": {"@type": "ImageObject", "url": f"{SITE}/assets/images/logo.png", "width": 432, "height": 111},
    "email": "connect@mypegasus.in",
    "telephone": "+91-731-474-5928",
    "address": {
        "@type": "PostalAddress",
        "streetAddress": "Awfis Winway, 7, Vijay Nagar, Scheme No 54",
        "addressLocality": "Indore",
        "addressRegion": "Madhya Pradesh",
        "postalCode": "452010",
        "addressCountry": "IN",
    },
    "contactPoint": {
        "@type": "ContactPoint",
        "contactType": "sales",
        "telephone": "+91-731-474-5928",
        "email": "connect@mypegasus.in",
    },
}

WEBSITE = {"@type": "WebSite", "@id": WEBSITE_ID, "url": f"{SITE}/", "name": "Pegasus", "publisher": {"@id": ORG_ID}}

# One entry per page. "service" describes the offering (schema.org Service: no price/rating needed).
PAGES = {
    "index.html": dict(
        url=f"{SITE}/",
        title="Pegasus | Construction & Hospitality ERP and Smart Automation",
        description="Pegasus builds industry ERP for construction (Pegasus Atlas) and hospitality (Pegasus Opera), "
                    "plus Pegasus SmartHomes automation. Based in Indore, India.",
        image=f"{SITE}/assets/images/og/pegasus.png",
        image_alt="Pegasus",
        crumbs=None,
        service=None,
    ),
    "construction.html": dict(
        url=f"{SITE}/construction",
        title="Pegasus Atlas | Construction ERP Software for Projects & Sites",
        description="Pegasus Atlas is construction ERP for job costing, procurement, subcontractors, equipment, "
                    "payroll and project finance. Book a demo with our Indore team.",
        image=f"{SITE}/assets/images/construction/hero.jpg",
        image_alt="Construction worker in a hard hat on a timber building frame",
        crumbs=[("Home", f"{SITE}/"), ("Construction", f"{SITE}/construction")],
        service=("Pegasus Atlas", "Construction ERP software"),
    ),
    "hospitality.html": dict(
        url=f"{SITE}/hospitality",
        title="Pegasus Opera | Hotel & Hospitality ERP Software",
        description="Pegasus Opera is hospitality ERP for hotels, resorts and restaurants: multi-property finance, "
                    "purchasing, inventory, workforce scheduling and guest data.",
        image=f"{SITE}/assets/images/hospitality/hero.jpg",
        image_alt="Waiter serving a table of guests in a busy restaurant",
        crumbs=[("Home", f"{SITE}/"), ("Hospitality", f"{SITE}/hospitality")],
        service=("Pegasus Opera", "Hospitality ERP software"),
    ),
    "smarthomes.html": dict(
        url=f"{SH}/",
        title="Pegasus SmartHomes | Smart Home, Hotel & Building Automation",
        description="Automate lights, climate, curtains, sensors, IoT devices and buildings with Pegasus "
                    "SmartHomes and Pegasus TV. Smart home and hotel automation from Indore.",
        image=f"{SITE}/assets/images/og/smarthomes.png",
        image_alt="Pegasus SmartHomes",
        crumbs=[("Pegasus", f"{SITE}/"), ("SmartHomes", f"{SH}/")],
        service=("Pegasus SmartHomes", "Smart home, hotel and building automation"),
    ),
    "404.html": dict(
        url=f"{SITE}/404",
        title="Page not found | Pegasus",
        description="The page you were looking for doesn't exist.",
        image=f"{SITE}/assets/images/og/pegasus.png",
        image_alt="Pegasus",
        crumbs=None,
        service=None,
        noindex=True,
    ),
}


def esc(text):
    return text.replace("&", "&amp;").replace('"', "&quot;").replace("<", "&lt;").replace(">", "&gt;")


def jsonld(page):
    graph = [ORG, WEBSITE]
    webpage = {
        "@type": "WebPage",
        "@id": f"{page['url']}#webpage",
        "url": page["url"],
        "name": page["title"],
        "description": page["description"],
        "isPartOf": {"@id": WEBSITE_ID},
        "about": {"@id": ORG_ID},
        "primaryImageOfPage": {"@type": "ImageObject", "url": page["image"]},
        "inLanguage": "en-IN",
    }
    if page["crumbs"]:
        webpage["breadcrumb"] = {"@id": f"{page['url']}#breadcrumb"}
        graph.append({
            "@type": "BreadcrumbList",
            "@id": f"{page['url']}#breadcrumb",
            "itemListElement": [{"@type": "ListItem", "position": i + 1, "name": n, "item": u}
                                for i, (n, u) in enumerate(page["crumbs"])],
        })
    if page["service"]:
        name, kind = page["service"]
        graph.append({
            "@type": "Service",
            "name": name,
            "serviceType": kind,
            "description": page["description"],
            "url": page["url"],
            "provider": {"@id": ORG_ID},
            "image": page["image"],
        })
    graph.insert(2, webpage)
    return json.dumps({"@context": "https://schema.org", "@graph": graph}, ensure_ascii=False, indent=2)


def head_block(page):
    robots = "noindex, follow" if page.get("noindex") else "index, follow, max-image-preview:large"
    canonical = "" if page.get("noindex") else f'  <link rel="canonical" href="{page["url"]}">\n'
    t, d, img = esc(page["title"]), esc(page["description"]), page["image"]
    return (
        "  <!-- seo:start (generated by tools/seo/seo.py) -->\n"
        f'  <meta name="robots" content="{robots}">\n'
        f"{canonical}"
        '  <meta property="og:site_name" content="Pegasus">\n'
        '  <meta property="og:locale" content="en_IN">\n'
        '  <meta property="og:type" content="website">\n'
        f'  <meta property="og:url" content="{page["url"]}">\n'
        f'  <meta property="og:title" content="{t}">\n'
        f'  <meta property="og:description" content="{d}">\n'
        f'  <meta property="og:image" content="{img}">\n'
        f'  <meta property="og:image:alt" content="{esc(page["image_alt"])}">\n'
        '  <meta name="twitter:card" content="summary_large_image">\n'
        f'  <meta name="twitter:title" content="{t}">\n'
        f'  <meta name="twitter:description" content="{d}">\n'
        f'  <meta name="twitter:image" content="{img}">\n'
        f'  <script type="application/ld+json">\n{jsonld(page)}\n  </script>\n'
        "  <!-- seo:end -->\n"
    )


def apply(html, filename):
    """Give a page its title, description, canonical, social tags and JSON-LD."""
    page = PAGES[filename]
    html = re.sub(r"<title>.*?</title>", f"<title>{esc(page['title'])}</title>", html, count=1, flags=re.S)
    html = re.sub(r'<meta name="description" content="[^"]*">',
                  f'<meta name="description" content="{esc(page["description"])}">', html, count=1)
    html = re.sub(r"  <!-- seo:start.*?<!-- seo:end -->\n", "", html, flags=re.S)
    html = re.sub(r'  <link rel="canonical"[^>]*>\n', "", html)
    html = html.replace("</title>\n", "</title>\n" + head_block(page), 1)
    assert html.count("<!-- seo:start") == 1 and f"<title>{esc(page['title'])}</title>" in html, filename
    return html


# ---------------------------------------------------------------- site files
def lastmod(path):
    try:
        out = subprocess.run(["git", "log", "-1", "--format=%cs", "--", path], cwd=ROOT,
                             capture_output=True, text=True).stdout.strip()
    except OSError:
        out = ""
    return out or datetime.date.today().isoformat()


def write_sitemap():
    urls = []
    for name, page in PAGES.items():
        if page.get("noindex"):
            continue
        urls.append(f"  <url>\n    <loc>{page['url']}</loc>\n    <lastmod>{lastmod('public/' + name)}</lastmod>\n  </url>")
    xml = ('<?xml version="1.0" encoding="UTF-8"?>\n'
           '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + "\n".join(urls) + "\n</urlset>\n")
    open(os.path.join(PUBLIC, "sitemap.xml"), "w").write(xml)


def write_robots():
    # served on both hosts; the sitemap also lists the SmartHomes subdomain
    open(os.path.join(PUBLIC, "robots.txt"), "w").write(
        "User-agent: *\nAllow: /\n\nSitemap: https://mypegasus.in/sitemap.xml\n")


def write_404():
    idx = open(os.path.join(PUBLIC, "index.html")).read()
    head_nav = idx[:idx.index("  <main>")]
    tail = idx[idx.index("  <!-- ===== Footer"):]
    main = """  <main>
    <section class="section">
      <div class="container">
        <header class="section-head">
          <h1 class="section-title">Page not found</h1>
          <p class="section-subtitle">The page you were looking for doesn't exist or has moved. Try one of these instead.</p>
        </header>
        <div class="ind-actions ind-actions--section">
          <a href="/" class="btn btn--primary">Go to the home page</a>
          <a href="/construction" class="btn btn--outline">Pegasus Atlas</a>
          <a href="/hospitality" class="btn btn--outline">Pegasus Opera</a>
          <a href="https://smarthomes.mypegasus.in/" class="btn btn--outline">Pegasus SmartHomes</a>
        </div>
      </div>
    </section>
  </main>

"""
    # served at any missing URL, so every link and asset path must be root-relative
    page = head_nav + main + tail
    page = re.sub(r'(href|src)="(?!https?:|mailto:|tel:|#|/)([^"]+)"', r'\1="/\2"', page)
    page = page.replace('href="/./"', 'href="/"')
    open(os.path.join(PUBLIC, "404.html"), "w").write(apply(page, "404.html"))


def write_og_images():
    """1200x630 share cards: dark stage, brand glows, logo."""
    from PIL import Image, ImageDraw, ImageFilter, ImageFont
    out = os.path.join(PUBLIC, "assets", "images", "og")
    os.makedirs(out, exist_ok=True)
    font_path = "/System/Library/Fonts/HelveticaNeue.ttc"

    def card(logo_file, logo_w, tagline, glows, name):
        W, H = 1200, 630
        bg = Image.new("RGB", (W, H), (8, 8, 12))
        glow = Image.new("RGB", (W, H), (8, 8, 12))
        d = ImageDraw.Draw(glow)
        for (cx, cy, r, col) in glows:
            d.ellipse((cx - r, cy - r, cx + r, cy + r), fill=col)
        glow = glow.filter(ImageFilter.GaussianBlur(110))
        bg = Image.blend(bg, glow, 0.85)
        logo = Image.open(os.path.join(PUBLIC, "assets", "images", logo_file)).convert("RGBA")
        logo = logo.resize((logo_w, round(logo.height * logo_w / logo.width)), Image.LANCZOS)
        canvas = bg.convert("RGBA")
        canvas.alpha_composite(logo, ((W - logo.width) // 2, (H - logo.height) // 2 - 30))
        if tagline and os.path.exists(font_path):
            font = ImageFont.truetype(font_path, 34)
            td = ImageDraw.Draw(canvas)
            tw = td.textlength(tagline, font=font)
            td.text(((W - tw) / 2, (H + logo.height) // 2 + 10), tagline, font=font, fill=(200, 203, 220))
        canvas.convert("RGB").save(os.path.join(out, name), optimize=True)

    card("logo-white.png", 520, "Industry ERP for construction and hospitality",
         [(260, 80, 260, (47, 99, 245)), (980, 560, 280, (106, 62, 242)), (1080, 90, 200, (226, 79, 201))], "pegasus.png")
    card("pegasus-smarthomes-logo.png", 760, "Automation for every sensor, IoT device and building",
         [(900, 120, 300, (92, 96, 254)), (640, 560, 260, (159, 84, 244)), (1160, 380, 220, (242, 65, 179))], "smarthomes.png")


if __name__ == "__main__":
    path = os.path.join(PUBLIC, "index.html")
    html = open(path).read()  # read fully before opening for write
    open(path, "w").write(apply(html, "index.html"))
    write_404()
    write_og_images()
    write_sitemap()
    write_robots()
    print("SEO applied: index.html, 404.html, sitemap.xml, robots.txt, og images")
