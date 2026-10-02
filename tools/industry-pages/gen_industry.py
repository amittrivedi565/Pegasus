"""Generate industry pages (construction.html, hospitality.html) from one template.
Usage: python3 gen_industry.py [construction|hospitality|all]   (run from the site root)"""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from industry_helpers import CHEV, TABIDX, NL14, NL18, la, ICON, visual

ICON["heart"] = '<path d="M12 20s-7-4.5-7-10a4 4 0 0 1 7-2.6A4 4 0 0 1 19 10c0 5.5-7 10-7 10z"/>'
ICON["bed"] = '<path d="M3 18V7M3 14h18v4M21 14v-2a3 3 0 0 0-3-3h-7v5"/><circle cx="7" cy="11" r="1.8"/>'

def mail(subject):
    return "mailto:connect@mypegasus.in?subject=" + subject.replace(" ", "%20")

# ---------------------------------------------------------------- content
CONSTRUCTION = dict(
  file="construction.html", IND_NAME="Construction", IMG_DIR="construction", PRODUCT="Atlas",
  meta="Pegasus Atlas: construction ERP for project controls, procurement, people and finance.",
  HERO_TEXT="Plan better, build more safely and deliver every project on time and on budget, with one ERP built for the way construction really works.",
  HERO_CREDIT="Josh Olalde", HERO_ALT="Construction worker in a hard hat on a timber building frame", HERO_STYLE="",
  INTRO_TITLE="Industry software tailored for construction companies",
  INTRO_SUB="Pegasus Atlas brings estimating, project controls, procurement, people and finance together, so you can win more bids, build greener and run every project with confidence.",
  INTRO_CREDIT="Raymond Yeung", INTRO_ALT="Tower cranes rising over a city construction site",
  bullets=["Connect project teams to deliver quality projects",
           "Plan, procure and track materials with technology-driven tools",
           "Hire and develop the right talent for every site",
           "Keep equipment, subcontractors and costs under control",
           "Integrate responsible practices to reduce environmental impact"],
  PRODUCTS_TITLE="Construction solutions from Pegasus",
  PRODUCTS_SUB="Our construction software and AI products help you achieve cost-effective transformation and sustainable growth.",
  tabs=[
   ("erp", "Cloud ERP", [
     ("chart", "Real-time project insights", "Improve decision-making and efficiency with live job costing, inventory and supply chain data across every project.", ("Explore Pegasus Atlas", "#"), "demo"),
     ("sync", "Alignment across finance and field operations", "Connect site activity to back-office processes, so progress, costs and invoices always match what's happening on the ground.", ("Explore field operations", "#"), "quote"),
     ("invoice", "Project accounting and billing", "Manage budgets, progress billing, retentions and change orders in one place, with a full audit trail.", ("Learn more", "#"), "demo"),
     ("wrench", "Field service and maintenance", "Resolve issues faster and keep handed-over assets running with proactive, AI-enabled service management.", ("Explore Pegasus Argus", "index.html#section-three"), None)]),
   ("talent", "Talent management", [
     ("users", "Workforce planning", "Match the right crews and skills to every project phase, and forecast labour needs weeks ahead.", ("Learn more", "#"), "demo"),
     ("badge", "Skills and certifications", "Track tickets, licences and safety training for every worker, with alerts before anything expires.", ("Explore Pegasus Athena", "index.html#section-three"), None),
     ("clock", "Timesheets and payroll", "Capture site hours on any device and pay crews and subcontractors accurately and on time.", ("Learn more", "#"), "demo"),
     ("userplus", "Recruiting and onboarding", "Hire faster and get new starters site-ready with digital onboarding and inductions.", ("Learn more", "#"), None)]),
   ("supply", "Construction supply chain", [
     ("cart", "Procurement and sourcing", "Run tenders, compare bids and award packages, with AI that flags risk and best value.", ("Learn more", "#"), "demo"),
     ("boxes", "Materials and inventory", "Know what's on site, in transit and on order, and cut waste from over-ordering.", ("Learn more", "#"), None),
     ("handshake", "Subcontractor management", "Onboard, qualify and pay subcontractors, with compliance checks built in.", ("Learn more", "#"), "demo"),
     ("truck", "Equipment and fleet", "Track utilisation, location and maintenance for plant and vehicles across every site.", ("Learn more", "#"), None)]),
   ("opportunity", "Opportunity management", [
     ("calc", "Bids and estimating", "Build accurate estimates faster with cost libraries, historical data and AI suggestions.", ("Learn more", "#"), "demo"),
     ("funnel", "Pipeline and CRM", "See every opportunity from lead to contract, and focus on the bids you can win.", ("Learn more", "#"), None),
     ("doc", "Contracts and change orders", "Keep contract values, variations and approvals in sync with project costs.", ("Learn more", "#"), None),
     ("portal", "Client portals", "Share progress, documents and invoices with clients in one secure place.", ("Learn more", "#"), "demo")]),
   ("data", "Data insights", [
     ("dash", "Project dashboards", "Monitor cost, schedule and safety KPIs across your whole portfolio in real time.", ("Learn more", "#"), "demo"),
     ("spark", "AI cost forecasting", "Predict overruns before they happen with Pegasus Delphi AI models.", ("Explore Pegasus Delphi", "index.html#section-two"), None),
     ("db", "Unified construction data", "Bring ERP, site and BIM data together in Pegasus Gaia Data Cloud.", ("Explore Pegasus Gaia", "index.html#section-two"), None),
     ("shield", "Risk and compliance analytics", "Spot safety, quality and contract risks early, and act on them.", ("Learn more", "#"), None)]),
   ("innovation", "Digital innovation", [
     ("bot", "AI agents on site", "Ask Pegasus Muse for progress updates, approvals or reports in plain language.", ("Meet Pegasus Muse", "index.html#section-five"), None),
     ("plug", "Connected systems", "Integrate scheduling, BIM and accounting tools with Pegasus Iris Integration.", ("Explore Pegasus Iris", "index.html#section-two"), None),
     ("code", "Custom apps and workflows", "Build site apps and approval flows without code in Pegasus Daedalus Studio.", ("Explore Pegasus Daedalus", "index.html#section-two"), None),
     ("scale", "Responsible AI", "Govern every agent with approvals and audit trails in Pegasus Themis.", ("Explore Pegasus Themis", "index.html#section-two"), None)]),
  ],
  UC_TITLE="Explore how we can help your construction business run better",
  UC_SUB="Our construction solutions help you run resilient, sustainable supply chains, optimise operations and meet client expectations.",
  usecases=[
   ("Project delivery excellence", "Deliver on time, on budget and to quality with lean, connected project controls.", [("Explore Pegasus Atlas", "#products"), ("Sync your ERP with every job site", "#")]),
   ("Digitalised supply chain management", "Create an on-time supply chain with optimised planning and automated processes.", [("Explore procurement solutions", "#products"), "demo"]),
   ("Talent development and retention", "Train your existing people while hiring the right talent with a technology-based skillset.", [("Explore Pegasus Athena", "index.html#section-three"), "demo"]),
   ("Connected sites and equipment", "Capture and centralise data from plant, sensors and site teams to manage every asset effectively.", [("Learn more", "#")]),
   ("Environmental sustainability", "Track emissions and embed responsible practices across your construction and maintenance activities.", [("Learn more", "#"), "demo"]),
   ("Health, safety and compliance", "Record incidents, inspections and permits digitally, and prove compliance at any time.", ["demo"]),
  ],
  WHY_TITLE="Why construction teams choose Pegasus",
  whys=[("db", "One source of truth", "Estimating, projects, procurement and finance share one data model, so everyone works from the same numbers."),
        ("helmet", "Built for the field", "Mobile-first tools let site teams log progress, hours and materials from any device, right where the work happens."),
        ("pin", "Local expertise", "Our Indore-based team implements and supports Pegasus Atlas through Pegasus Odyssey and Argus services.")],
  SPECIALIST_BTN="Talk to a construction specialist",
  DEMO_TEXT="Book a 30-minute walkthrough with our construction specialists and see how Atlas fits your projects.",
  resources=[
   ("doc", "Guide", "Digital transformation for construction firms", "Learn practical strategies to modernise estimating, project controls and finance, and drive efficiency across your organisation.", ("Read the guide", "#")),
   ("bot", "Article", "Harnessing AI for construction management", "See how AI agents help construction teams save time, reduce costs and improve safety.", ("Read the article", "#")),
   ("play", "Demo", "AI on the job site with Pegasus Muse", "Explore how AI supports better planning, safety, efficiency and cost control for informed decision-making.", ("Watch the demo", "index.html#section-five")),
   ("dash", "White paper", "Maximising project visibility", "Learn how connecting field operations with back-office systems gives you a live view of every project.", ("Read the white paper", "#"))],
  NEXT_ROADMAP_TEXT="Explore what's coming next in our construction product portfolio.",
  SUBNAV_EXTRA="", SMARTHOMES="",
)

HOSPITALITY = dict(
  file="hospitality.html", IND_NAME="Hospitality", IMG_DIR="hospitality", PRODUCT="Opera",
  meta="Pegasus Opera: hospitality ERP for multi-property finance, purchasing, workforce and guest operations.",
  HERO_TEXT="Deliver memorable guest experiences and run every hotel, resort and restaurant more profitably, with one ERP built for hospitality.",
  HERO_CREDIT="Vitaly Gariev", HERO_ALT="Waiter serving a table of guests in a busy restaurant",
  HERO_STYLE=' style="object-position: 35% 50%"',
  INTRO_TITLE="Industry software tailored for hospitality businesses",
  INTRO_SUB="Pegasus Opera brings property finance, purchasing, inventory, people and guest operations together, so you can grow revenue, control costs and keep guests coming back.",
  INTRO_CREDIT="Wes Hicks", INTRO_ALT="Bright, calm hotel room with a made bed and sheer curtains",
  bullets=["Run multi-property finance and reporting from one platform",
           "Control food, beverage and supply costs with smarter purchasing",
           "Schedule the right people for every shift and season",
           "Keep rooms, kitchens and facilities in top condition",
           "Personalise every stay with connected guest data"],
  PRODUCTS_TITLE="Hospitality solutions from Pegasus",
  PRODUCTS_SUB="Our hospitality software and AI products help you raise margins, delight guests and grow sustainably.",
  tabs=[
   ("erp", "Cloud ERP", [
     ("chart", "Real-time property insights", "Track occupancy, revenue per room, costs and margins across every property in real time.", ("Explore Pegasus Opera", "#"), "demo"),
     ("sync", "Front of house meets back office", "Connect your property management and point-of-sale systems to finance, so revenue and costs reconcile automatically.", ("Explore Pegasus Iris", "index.html#section-two"), "quote"),
     ("invoice", "Multi-property accounting", "Consolidate entities, currencies and owner reports in one place, with a full audit trail.", ("Learn more", "#"), "demo"),
     ("wrench", "Maintenance and facilities", "Plan preventive maintenance and fix room issues faster with proactive, AI-enabled service management.", ("Explore Pegasus Argus", "index.html#section-three"), None)]),
   ("workforce", "Workforce management", [
     ("users", "Shift scheduling", "Match staffing to forecast occupancy and events across every department, from front desk to kitchen.", ("Learn more", "#"), "demo"),
     ("badge", "Training and certifications", "Track food safety, hygiene and service training for every team member, with alerts before anything expires.", ("Explore Pegasus Athena", "index.html#section-three"), None),
     ("clock", "Timesheets and payroll", "Capture hours, tips and service charges accurately, and pay every team on time.", ("Learn more", "#"), "demo"),
     ("userplus", "Seasonal hiring and onboarding", "Hire faster for peak seasons and get new starters guest-ready with digital onboarding.", ("Learn more", "#"), None)]),
   ("procurement", "Procurement and inventory", [
     ("cart", "Purchasing and sourcing", "Buy from approved suppliers at negotiated prices, with approvals and budgets built in.", ("Learn more", "#"), "demo"),
     ("boxes", "Food and beverage inventory", "Track stock across kitchens and bars, and cut waste with par levels and recipe costing.", ("Learn more", "#"), None),
     ("handshake", "Supplier management", "Onboard, rate and pay suppliers, with quality and compliance checks built in.", ("Learn more", "#"), "demo"),
     ("truck", "Central kitchens and distribution", "Plan production and deliveries from central kitchens to every outlet.", ("Learn more", "#"), None)]),
   ("guest", "Guest experience", [
     ("portal", "Guest profiles", "Bring stays, spend and preferences together into one view of every guest.", ("Learn more", "#"), "demo"),
     ("funnel", "Sales, groups and events", "Manage group bookings, events and corporate accounts from first enquiry to final invoice.", ("Learn more", "#"), None),
     ("doc", "Contracts and rate agreements", "Keep corporate rates, allotments and contracts in sync with billing.", ("Learn more", "#"), None),
     ("heart", "Loyalty and personalisation", "Reward returning guests and tailor offers using what you already know about them.", ("Learn more", "#"), "demo")]),
   ("data", "Data insights", [
     ("dash", "Portfolio dashboards", "Monitor occupancy, average daily rate, labour and food costs across your portfolio in real time.", ("Learn more", "#"), "demo"),
     ("spark", "AI demand forecasting", "Forecast occupancy and demand with Pegasus Delphi AI models to plan staffing and purchasing.", ("Explore Pegasus Delphi", "index.html#section-two"), None),
     ("db", "Unified guest and operations data", "Bring property, point-of-sale and ERP data together in Pegasus Gaia Data Cloud.", ("Explore Pegasus Gaia", "index.html#section-two"), None),
     ("shield", "Risk and compliance analytics", "Spot food safety, audit and contract risks early, and act on them.", ("Learn more", "#"), None)]),
   ("innovation", "Digital innovation", [
     ("bot", "AI agents for every team", "Ask Pegasus Muse for occupancy updates, approvals or reports in plain language.", ("Meet Pegasus Muse", "index.html#section-five"), None),
     ("plug", "Connected systems", "Integrate property management, point of sale, channel managers and accounting with Pegasus Iris Integration.", ("Explore Pegasus Iris", "index.html#section-two"), None),
     ("code", "Custom apps and workflows", "Build housekeeping, maintenance and approval apps without code in Pegasus Daedalus Studio.", ("Explore Pegasus Daedalus", "index.html#section-two"), None),
     ("scale", "Responsible AI", "Govern every agent with approvals and audit trails in Pegasus Themis.", ("Explore Pegasus Themis", "index.html#section-two"), None)]),
  ],
  UC_TITLE="Explore how we can help your hospitality business run better",
  UC_SUB="Our hospitality solutions help you control costs, empower your teams and deliver experiences guests remember.",
  usecases=[
   ("Profitable multi-property operations", "Standardise processes and see performance across every hotel, resort and restaurant.", [("Explore Pegasus Opera", "#products"), "demo"]),
   ("Smarter purchasing and inventory", "Cut food and supply costs with automated ordering, par levels and recipe costing.", [("Explore procurement solutions", "#products"), "demo"]),
   ("Engaged, well-trained teams", "Schedule, train and retain great people across every shift and season.", [("Explore Pegasus Athena", "index.html#section-three"), "demo"]),
   ("Well-maintained properties", "Plan preventive maintenance and fix issues before guests ever notice them.", [("Learn more", "#")]),
   ("Sustainable hospitality", "Track energy, water and waste, and embed responsible practices across your properties.", [("Learn more", "#"), "demo"]),
   ("Food safety and compliance", "Record checks, audits and certifications digitally, and prove compliance at any time.", ["demo"]),
  ],
  WHY_TITLE="Why hospitality teams choose Pegasus",
  whys=[("db", "One source of truth", "Finance, purchasing, people and guest operations share one data model across every property."),
        ("bed", "Built for every shift", "Mobile-first tools let front desk, kitchen and housekeeping teams work from any device, wherever they are."),
        ("pin", "Local expertise", "Our Indore-based team implements and supports Pegasus Opera through Pegasus Odyssey and Argus services.")],
  SPECIALIST_BTN="Talk to a hospitality specialist",
  DEMO_TEXT="Book a 30-minute walkthrough with our hospitality specialists and see how Opera fits your properties.",
  resources=[
   ("doc", "Guide", "Digital transformation for hotels and restaurants", "Learn practical strategies to modernise finance, purchasing and operations across your properties.", ("Read the guide", "#")),
   ("bot", "Article", "Harnessing AI in hospitality", "See how AI agents help hospitality teams save time, reduce costs and personalise every stay.", ("Read the article", "#")),
   ("play", "Demo", "AI at the front desk with Pegasus Muse", "Explore how AI supports better forecasting, staffing and guest service.", ("Watch the demo", "index.html#section-five")),
   ("dash", "White paper", "Maximising portfolio visibility", "Learn how connecting property systems with back-office finance gives you a live view of every property.", ("Read the white paper", "#"))],
  NEXT_ROADMAP_TEXT="Explore what's coming next in our hospitality product portfolio.",
)


CHEV_S = '<svg viewBox="0 0 16 16" aria-hidden="true"><path d="M6 3l5 5-5 5" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></svg>'
SH_MAIL = mail("Pegasus SmartHomes enquiry")

def sh_icon(paths):
    return f'<svg viewBox="0 0 24 24" aria-hidden="true">{paths}</svg>'

SH_FEATURES = [
  ("Full room automation", "Lighting, climate, curtains, TV and door locks respond to each guest, with personal scenes from check-in to checkout."),
  ("Every sensor that matters", "Occupancy, air quality, temperature, water leak, smoke and energy sensors keep every space safe and comfortable."),
  ("Smarter operations", "Housekeeping and maintenance get live room status and automatic alerts, so issues are fixed before guests notice."),
  ("Enterprise scale", "Manage one boutique hotel or a whole portfolio of enterprise buildings, connected to Pegasus Opera and your building systems."),
]
CHECK = '<path d="M5 12.5l4.5 4.5L19 7.5"/>'

SMARTHOMES_SECTION = f"""    <!-- ===== Pegasus SmartHomes (hospitality automation / IoT) ===== -->
    <section id="smarthomes" class="section sh">
      <div class="container">
        <div class="sh__panel">
          <div class="sh__content">
            <img class="sh__logo" src="assets/images/smarthomes-logo.png" alt="Pegasus SmartHomes" width="729" height="118">
            <h2 class="sh__title">Every sensor, one intelligent building</h2>
            <p class="sh__lead">Pegasus SmartHomes is hospitality automation that elevates every guest experience, from full room automation to large-scale enterprise buildings.</p>
            <ul class="sh__features">
{chr(10).join(f'              <li>{sh_icon(CHECK)}<div><strong>{t}</strong><span>{d}</span></div></li>' for t, d in SH_FEATURES)}
            </ul>
            <div class="ind-actions">
              <a href="smarthomes.html" class="btn btn--light">Discover Pegasus SmartHomes</a>
              <a href="{SH_MAIL}" class="btn btn--outline-light">Talk to us about SmartHomes</a>
            </div>
          </div>

          <!-- Illustrative smart-room control panel -->
          <div class="sh-room" aria-hidden="true">
            <div class="sh-room__head">
              <div><strong>Suite 1204</strong><span>Guest checked in</span></div>
              <span class="sh-room__status"><i></i>Occupied</span>
            </div>
            <div class="sh-room__tiles">
              <div class="sh-tile is-on">{sh_icon('<circle cx="12" cy="12" r="4"/><path d="M12 2v2M12 20v2M4 12H2M22 12h-2M5 5l1.5 1.5M17.5 17.5L19 19M5 19l1.5-1.5M17.5 6.5L19 5"/>')}<span>Lights</span><strong>Warm &middot; 60%</strong></div>
              <div class="sh-tile is-on">{sh_icon('<path d="M10 4a2 2 0 0 1 4 0v9.5a4 4 0 1 1-4 0z"/><path d="M12 10v6"/>')}<span>Climate</span><strong>22&deg;C</strong></div>
              <div class="sh-tile">{sh_icon('<path d="M3 4h18M5 4v14M19 4v14M5 18c2-4 2-10 0-14M19 18c-2-4-2-10 0-14"/>')}<span>Curtains</span><strong>Open</strong></div>
              <div class="sh-tile is-on">{sh_icon('<rect x="5" y="11" width="14" height="10" rx="2"/><path d="M8 11V7a4 4 0 0 1 8 0v4"/>')}<span>Door</span><strong>Locked</strong></div>
            </div>
            <p class="sh-room__label">Scenes</p>
            <div class="sh-room__scenes"><span class="is-active">Welcome</span><span>Relax</span><span>Sleep</span><span>Away</span></div>
            <p class="sh-room__label">Sensors</p>
            <div class="sh-room__sensors">
              <span><i></i>Occupancy</span><span><i></i>Air quality</span><span><i></i>Water leak</span><span><i></i>Energy</span>
            </div>
          </div>
        </div>
      </div>
    </section>

"""

HOSPITALITY["SUBNAV_EXTRA"] = '        <li><a href="#smarthomes">SmartHomes</a></li>\n'
HOSPITALITY["SMARTHOMES"] = SMARTHOMES_SECTION

PAGES = {"construction": CONSTRUCTION, "hospitality": HOSPITALITY}

# ---------------------------------------------------------------- build
def build(cfg):
    product = cfg["PRODUCT"]
    DEMO = mail(f"Pegasus {product} demo request")
    CONTACT = mail(f"Pegasus {product} enquiry")
    link_for = {"demo": ("Request a demo", DEMO), "quote": ("Request a quote", CONTACT)}
    L = lambda item: la(*link_for[item]) if isinstance(item, str) else la(*item)

    tabs_btn, panels = [], []
    for i, (key, label, cards) in enumerate(cfg["tabs"]):
        sel = i == 0
        aria = "true" if sel else "false"
        tabi = "" if sel else TABIDX
        hid = "" if sel else " hidden"
        tabs_btn.append(f'          <button class="ind-tab" role="tab" id="tab-{key}" aria-controls="panel-{key}" aria-selected="{aria}"{tabi}>{label}</button>')
        cards_html = []
        for icon, title, text, l1, l2 in cards:
            links = la(*l1) + ((NL18 + L(l2)) if l2 else "")
            cards_html.append(f'''            <article class="ind-card">
              {visual(icon)}
              <h3 class="ind-card__title">{title}</h3>
              <p class="ind-card__text">{text}</p>
              <div class="ind-links">
                  {links}
              </div>
            </article>''')
        panels.append(f'''        <div class="ind-panel" role="tabpanel" id="panel-{key}" aria-labelledby="tab-{key}"{hid}>
{chr(10).join(cards_html)}
        </div>''')

    uc_html = "\n".join(f'''          <div class="ind-usecase">
            <h3>{t}</h3>
            <p>{d}</p>
            <div class="ind-links">
              {NL14.join(L(l) for l in links)}
            </div>
          </div>''' for t, d, links in cfg["usecases"])

    why_html = "\n".join(f'''          <div class="ind-why">
            <span class="ind-why__icon"><svg viewBox="0 0 24 24" aria-hidden="true">{ICON[i]}</svg></span>
            <h3>{t}</h3>
            <p>{d}</p>
          </div>''' for i, t, d in cfg["whys"])

    res_html = "\n".join(f'''          <article class="ind-card">
            {visual(i, chip)}
            <h3 class="ind-card__title">{t}</h3>
            <p class="ind-card__text">{d}</p>
            <div class="ind-links">
              {la(*l)}
            </div>
          </article>''' for i, chip, t, d, l in cfg["resources"])

    bullets = "\n".join(f"              <li>{b}</li>" for b in cfg["bullets"])

    tpl = open(os.path.join(HERE, "industry_main.tpl")).read()
    fields = {k: v for k, v in cfg.items() if k.isupper()}
    main = tpl.format(DEMO=DEMO, CONTACT=CONTACT, TABS="\n".join(tabs_btn), PANELS="\n\n".join(panels),
                      USECASES=uc_html, WHYS=why_html, RESOURCES=res_html, BULLETS=bullets,
                      LA_ROADMAP=la(f"View the Pegasus {product} road map"), LA_OVERVIEW=la("Download the product overview"),
                      LA_PRODUCT_ROADMAP=la("View the product road map"), LA_JOURNEY=la("Plan your journey", "index.html#section-three"),
                      **fields)

    idx = open("index.html").read()
    head_nav = idx[:idx.index("  <main>")]
    tail = idx[idx.index("  <!-- ===== Footer"):]
    head_nav = head_nav.replace("<title>Pegasus</title>", f"<title>{cfg['IND_NAME']} | Pegasus</title>")
    head_nav = head_nav.replace('content="Pegasus — enterprise technology that connects everything."', f'content="{cfg["meta"]}"')
    page = head_nav + main + "\n" + tail
    page = page.replace('href="#section-', 'href="index.html#section-')
    page = page.replace('<a href="#" class="footer__top"', '<a href="#top" class="footer__top"')
    page = page.replace("<body>", '<body id="top">', 1)
    open(cfg["file"], "w").write(page)
    print("written", cfg["file"], len(page))

which = sys.argv[1] if len(sys.argv) > 1 else "all"
for name, cfg in PAGES.items():
    if which in ("all", name):
        build(cfg)
