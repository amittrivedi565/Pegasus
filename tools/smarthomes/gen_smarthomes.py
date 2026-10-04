"""Generate smarthomes.html (dark luxury page for Pegasus SmartHomes).
Navbar and footer are copied from index.html and switched to their dark variants.
Usage: python3 tools/smarthomes/gen_smarthomes.py   (reads/writes pages in public/)"""

import os
import re

SITE = "https://mypegasus.in/"                 # main site
SUBDOMAIN = "https://smarthomes.mypegasus.in/"  # this page is served at the subdomain root
PUBLIC = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "public")  # the deployed site

MAIL = "mailto:connect@mypegasus.in?subject=Pegasus%20SmartHomes%20consultation"
SURVEY = "mailto:connect@mypegasus.in?subject=Pegasus%20SmartHomes%20site%20survey"
TEL = "tel:+917314745928"

def icon(paths, cls=""):
    c = f' class="{cls}"' if cls else ""
    return f'<svg{c} viewBox="0 0 24 24" aria-hidden="true">{paths}</svg>'

ARROW = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M4 12h16M14 6l6 6-6 6"/></svg>'

PILLARS = [
  ("I", "Invisible", "Sensors and controls disappear into the architecture. People feel the comfort, never the technology."),
  ("II", "Intuitive", "One touch, one word or nothing at all: every room, floor and building responds to the people in it."),
  ("III", "Intelligent", "Every device, sensor and system learns, saves energy and alerts your team before small issues become problems."),
]

MOMENTS = [
  ("arrival", "01", "18:40", "Arrival", "Recognised before the door",
   "As the guest checks in, their suite comes alive. The digital key activates, the corridor lights guide the way and the room is already at their preferred temperature.",
   ["Digital key activates on check-in", "Corridor lighting guides the way", "Suite pre-cooled to the guest's preference"],
   "Elegant hotel entrance glowing at night"),
  ("welcome", "02", "18:45", "Welcome", "A suite that remembers",
   "Curtains draw back to reveal the view, lighting settles into a warm welcome scene, and the music and preferences from the guest's last stay are ready and waiting.",
   ["Curtains open to the view", "Personal welcome lighting scene", "Preferences carried over from past stays"],
   "Hotel suite with a warm lamp and a city view through tall windows"),
  ("evening", "03", "22:30", "Evening", "Evening, in a single word",
   "Say “relax” and the lights dim, the curtains close and the air cools slightly. Do not disturb reaches housekeeping instantly, with no sign on the door.",
   ["Voice scenes with Siri and Google Assistant", "Lights, curtains and climate in harmony", "Do not disturb shared with staff instantly"],
   "Bedroom bathed in warm evening light"),
  ("morning", "04", "06:50", "Morning", "Sunrise, on schedule",
   "Curtains open gently with the alarm, the lights rise to daylight and the bathroom is warm and ready, so every guest wakes naturally and on time.",
   ["Curtains open with the alarm", "Circadian lighting rises to daylight", "Bathroom warmed before the guest steps in"],
   "Morning sunlight glowing through sheer curtains"),
]

DOMAINS = [
  ("Lighting", "Scenes, schedules and daylight-aware dimming in every space.", '<path d="M9 18h6M10 21h4M12 3a6 6 0 0 0-4 10.5c.7.7 1 1.5 1 2.5h6c0-1 .3-1.8 1-2.5A6 6 0 0 0 12 3z"/>'),
  ("Climate &amp; HVAC", "Air conditioning, heating and ventilation that follow occupancy.", '<path d="M10 4a2 2 0 0 1 4 0v9.5a4 4 0 1 1-4 0z"/><path d="M12 10v6"/>'),
  ("Curtains &amp; blinds", "Motorised shading on schedules, scenes or a single tap.", '<path d="M3 4h18M5 4v16M19 4v16M5 20c2.5-4 2.5-12 0-16M19 20c-2.5-4-2.5-12 0-16M9 4v16M15 4v16"/>'),
  ("Sensors", "Presence, air, water, smoke and more, feeding one system.", '<circle cx="12" cy="12" r="2"/><path d="M8.5 8.5a5 5 0 0 0 0 7M15.5 8.5a5 5 0 0 1 0 7M5.6 5.6a9 9 0 0 0 0 12.8M18.4 5.6a9 9 0 0 1 0 12.8"/>'),
  ("IoT devices", "Any connected device on one network, monitored and controlled.", '<rect x="7" y="7" width="10" height="10" rx="2"/><path d="M10 3v4M14 3v4M10 17v4M14 17v4M3 10h4M3 14h4M17 10h4M17 14h4"/>'),
  ("Access &amp; security", "Keyless entry, cameras and alarms, room by room.", '<rect x="5" y="11" width="14" height="10" rx="2"/><path d="M8 11V7a4 4 0 0 1 8 0v4M12 15v2"/>'),
  ("Energy &amp; metering", "Live consumption per room, floor and building.", '<path d="M13 3L5 13h6l-1 8 8-10h-6z"/>'),
  ("Building systems", "Pumps, plant rooms, lifts and building management, connected.", '<path d="M4 21V5l8-3 8 3v16M4 21h16M9 21v-4h6v4M8 8h2M14 8h2M8 12h2M14 12h2"/>'),
]

SENSORS = [
  ("Presence", "Knows when a room is occupied, and when it isn't.", '<circle cx="12" cy="7" r="3"/><path d="M6 21v-2a6 6 0 0 1 12 0v2M3 9a9 9 0 0 1 2-4M21 9a9 9 0 0 0-2-4"/>'),
  ("Climate", "Temperature and humidity tuned to every guest.", '<path d="M10 4a2 2 0 0 1 4 0v9.5a4 4 0 1 1-4 0z"/><path d="M12 10v6"/>'),
  ("Air quality", "CO₂ and air freshness, balanced automatically.", '<path d="M3 8h11a3 3 0 1 0-3-3M3 12h15a3 3 0 1 1-3 3M3 16h8"/>'),
  ("Light", "Daylight-aware scenes that follow the hour.", '<circle cx="12" cy="12" r="4"/><path d="M12 2v2M12 20v2M4 12H2M22 12h-2M5 5l1.5 1.5M17.5 17.5L19 19M5 19l1.5-1.5M17.5 6.5L19 5"/>'),
  ("Water", "Leak detection that stops damage before it spreads.", '<path d="M12 3s6 6.5 6 11a6 6 0 0 1-12 0c0-4.5 6-11 6-11z"/>'),
  ("Fire safety", "Smoke and heat alerts sent straight to your team.", '<path d="M12 3c1 4 5 5.5 5 10a5 5 0 0 1-10 0c0-2.5 1.5-4 2.5-5 .5 2 1.5 3 2.5 3 0-3-1-5 0-8z"/>'),
  ("Energy", "Room-by-room metering that cuts waste quietly.", '<path d="M13 3L5 13h6l-1 8 8-10h-6z"/>'),
  ("Access", "Keyless entry and security, room by room.", '<rect x="5" y="11" width="14" height="10" rx="2"/><path d="M8 11V7a4 4 0 0 1 8 0v4M12 15v2"/>'),
]

SCALE = [
  ("Room", "Full room automation",
   "Lighting, climate, curtains, media, sensors and access orchestrated in one space: a suite, an apartment, a home or an office."),
  ("Building", "Every floor, one view",
   "Rooms, lobbies, corridors, kitchens, parking and plant rooms on one live dashboard, connected to Pegasus Opera and your building systems."),
  ("Enterprise", "An entire skyline",
   "Hotels, residences and commercial towers across cities, with central monitoring, energy optimisation and round-the-clock support from our team."),
]

CONNECT = ["Pegasus Opera", "IoT devices", "Property management", "Point of sale", "Building management", "Energy systems", "Pegasus TV", "Voice assistants"]

# Scene controller values: scene -> (lights, climate, curtains, music, glow 0-1)
SCENES = {
  "welcome": ("Warm · 70%", "22°C", "Open", "Jazz · low", 0.9),
  "relax":   ("Amber · 35%", "23°C", "Half", "Ambient", 0.55),
  "sleep":   ("Off", "20°C", "Closed", "Off", 0.12),
  "away":    ("Off", "Eco · 26°C", "Closed", "Off", 0.0),
}


# ---------------------------------------------------------------- automation showcase
STEPS = [
  ("Sense", "Sensors read presence, climate, air, water, smoke and energy in every space.",
   '<circle cx="12" cy="12" r="2"/><path d="M8.5 8.5a5 5 0 0 0 0 7M15.5 8.5a5 5 0 0 1 0 7M5.6 5.6a9 9 0 0 0 0 12.8M18.4 5.6a9 9 0 0 1 0 12.8"/>'),
  ("Connect", "Lighting, HVAC, curtains, access, IoT devices and building systems join one platform.",
   '<rect x="7" y="7" width="10" height="10" rx="2"/><path d="M10 3v4M14 3v4M10 17v4M14 17v4M3 10h4M3 14h4M17 10h4M17 14h4"/>'),
  ("Automate", "Rules and scenes act instantly, from a single room to a whole building.",
   '<circle cx="12" cy="12" r="3"/><path d="M12 2v3M12 19v3M2 12h3M19 12h3M4.9 4.9L7 7M17 17l2.1 2.1M4.9 19.1L7 17M17 7l2.1-2.1"/>'),
  ("Manage from anywhere", "Every room, device and schedule in one app and one live dashboard.",
   '<rect x="7" y="2.5" width="10" height="19" rx="2.5"/><path d="M11 18.5h2"/>'),
]

PRODUCTS = [
  dict(key="node", img="flow-node", ping=(76, 40), device=("Blaze 2 Node", "Lounge"), flow=["Evening scene triggered", "Pendants on &middot; 70%", "Downlights dimmed to 40%"], toggles=[("Pendants", True), ("Downlights", True)], credit="Neon Wang", eyebrow="Smart lighting automation", name="Blaze 2 Node",
       title="Small device.<br><em>Big convenience.</em>",
       text="A retrofit module that makes your existing switches smart. Control lights from the mobile app, by voice or through automations, without changing a single switch plate.",
       feats=[("Controls two switches", "Independent on/off for two circuits"),
              ("Retrofit, no rewiring", "Fits behind your existing switchboard"),
              ("Works with the mobile app", "Plus voice and scheduled automations"),
              ("Reliable and stable", "Built for round-the-clock hospitality use")],
       alt="Hotel lounge with warm pendant and ceiling lighting"),
  dict(key="sensor", img="flow-sensor", ping=(53.4, 20.3), device=("MMC Sensor", "Corridor, level 12"), flow=["Motion detected", "Corridor lights &middot; 100%", "Auto-off after 2 min"], toggles=None, credit="Vitalii Khodzinskyi", eyebrow="Automatic lighting control", name="MMC Microwave Sensor",
       title="Lights when you need them.<br><em>Off when you don't.</em>",
       text="The microwave sensor detects movement and turns lights on and off automatically. It is ideal for washrooms, corridors and common areas.",
       feats=[("Motion detection", "Senses presence, even through light partitions"),
              ("Automatic on/off", "No switches to reach for"),
              ("Energy saving", "Lights never stay on in empty rooms"),
              ("Reliable performance", "Discreet ceiling mount for any space")],
       alt="Hotel corridor with a ceiling-mounted motion sensor"),
  dict(key="curtain", img="flow-curtain", ping=(47, 25), device=("Curtain Motor", "Suite 1204"), flow=["06:50 &middot; Alarm", "Curtains opening", "Daylight scene on"], toggles=None, credit="Anton Sobotyak", eyebrow="Effortless curtain automation", name="Smart Curtain Motor",
       title="Natural light.<br><em>On your terms.</em>",
       text="A smart curtain motor with built-in Wi-Fi and remote control. Open or close your curtains with a tap, a voice command or an automation.",
       feats=[("App and remote control", "Every curtain, from anywhere"),
              ("Scheduled timings", "Open at sunrise, close at sunset"),
              ("Better natural light", "Daylight exactly when you want it"),
              ("Modern, elegant living", "Whisper-quiet, clean-lined track")],
       alt="Morning sunlight through sheer curtains onto a bed"),
]

APP_TILES = [("Living room", "Lights", True), ("Curtains", "Open", True), ("Climate", "AC &middot; 23°C", True),
             ("Lobby", "Lights", True), ("Washroom", "Auto sensor", True), ("Water tank", "Pump auto", False)]
APP_FEATS = [
  ("Control devices from anywhere", '<circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3c2.5 2.5 3.5 5.5 3.5 9S14.5 18.5 12 21c-2.5-2.5-3.5-5.5-3.5-9S9.5 5.5 12 3z"/>'),
  ("Create schedules and scenes", '<circle cx="12" cy="13" r="8"/><path d="M12 9v4l2.5 2M9 2h6"/>'),
  ("Voice control with Siri and Google", '<rect x="9" y="3" width="6" height="11" rx="3"/><path d="M5 11a7 7 0 0 0 14 0M12 18v3"/>'),
  ("A simple, elegant interface", '<rect x="4" y="4" width="16" height="16" rx="4"/><path d="M9 12l2 2 4-4"/>'),
]

def device_card(p):
    name, room = p["device"]
    extra = ""
    if p["toggles"]:
        extra = "".join(f'<span class="lx-device__row">{t}<b class="lx-toggle{" is-on" if on else ""}"></b></span>' for t, on in p["toggles"])
    elif p["key"] == "curtain":
        extra = '<span class="lx-device__row">Open<b class="lx-device__pct">65%</b></span><span class="lx-device__bar"><i></i></span>'
    else:
        extra = '<span class="lx-device__row">Presence<b class="lx-device__live">Live</b></span>'
    return (f'<div class="lx-device" aria-hidden="true"><span class="lx-device__name"><i></i>{name}</span>'
            f'<span class="lx-device__room">{room}</span>{extra}</div>')

def showcase_top():
    steps = "\n".join(f"""          <li class="lx-step lx-reveal">
            <span class="lx-step__ring">{icon(p)}</span>
            <span class="lx-step__num">0{i + 1}</span>
            <h3>{t}</h3>
            <p>{d}</p>
          </li>""" for i, (t, d, p) in enumerate(STEPS))

    products = []
    for i, p in enumerate(PRODUCTS):
        flip = " lx-product--flip" if i % 2 else ""
        feats = "".join(f"<li><strong>{a}</strong><span>{b}</span></li>" for a, b in p["feats"])
        flow = "".join(f'<li style="--i: {n}"><span>0{n + 1}</span>{s}</li>' for n, s in enumerate(p["flow"]))
        products.append(f"""        <article class="lx-product lx-product--{p['key']}{flip}">
          <div class="lx-product__stage lx-reveal" style="--px: {p['ping'][0]}%; --py: {p['ping'][1]}%">
            <!-- Photo: {p['credit']} / Unsplash (unsplash.com/license) -->
            <img src="assets/images/smarthomes/{p['img']}.jpg" alt="{p['alt']}" width="1400" height="1120" loading="lazy">
            <span class="lx-ping" aria-hidden="true"><i></i><i></i><i></i></span>
            {device_card(p)}
            <ol class="lx-flow" aria-label="{p['name']} automation flow">{flow}</ol>
          </div>
          <div class="lx-product__text lx-reveal">
            <p class="lx-eyebrow">{p['eyebrow']}</p>
            <p class="lx-product__name">{p['name']}</p>
            <h3 class="lx-product__title">{p['title']}</h3>
            <p class="lx-product__body">{p['text']}</p>
            <ul class="lx-product__feats">{feats}</ul>
          </div>
        </article>""")

    return f"""    <!-- ===== How it works ===== -->
    <section class="lx-section lx-how">
      <div class="container">
        <header class="lx-head lx-reveal">
          <p class="lx-eyebrow">How it works</p>
          <h2 class="lx-title">Every system,<br><em>working as one.</em></h2>
        </header>
        <div class="lx-how__track">
          <svg class="lx-wave" viewBox="0 0 1200 200" preserveAspectRatio="none" aria-hidden="true">
            <defs>
              <linearGradient id="lx-wave-grad" x1="0" x2="1">
                <stop offset="0" stop-color="#2f63f5" stop-opacity="0"/>
                <stop offset=".2" stop-color="#6a3ef2"/>
                <stop offset=".6" stop-color="#b44fe0"/>
                <stop offset="1" stop-color="#e24fc9" stop-opacity="0"/>
              </linearGradient>
            </defs>
            <path class="lx-wave__glow" d="M0 120 C 200 20, 350 20, 500 100 S 800 190, 950 100 S 1150 40, 1200 70"/>
            <path class="lx-wave__line" d="M0 120 C 200 20, 350 20, 500 100 S 800 190, 950 100 S 1150 40, 1200 70"/>
          </svg>
          <ol class="lx-steps">
{steps}
          </ol>
        </div>
      </div>
    </section>

    <!-- ===== The collection (products) ===== -->
    <section class="lx-section lx-section--alt lx-collection">
      <div class="container">
        <header class="lx-head lx-head--split lx-reveal">
          <div>
            <p class="lx-eyebrow">The collection</p>
            <h2 class="lx-title">Designed devices,<br><em>quietly brilliant.</em></h2>
          </div>
          <p class="lx-head__text">A few of our own devices, each built to disappear into beautiful interiors. Behind them, one platform runs every sensor, IoT device and building system you have.</p>
        </header>
        <!-- Each stage shows the device's automation flow over a real interior -->
{chr(10).join(products)}
      </div>
    </section>

"""

def app_section():
    tiles = "".join(f'<div class="lx-app__tile{" is-on" if on else ""}"><i></i><strong>{a}</strong><span>{b}</span></div>'
                    for a, b, on in APP_TILES)
    feats = "\n".join(f"            <li>{icon(p)}<span>{t}</span></li>" for t, p in APP_FEATS)
    return f"""    <!-- ===== One app ===== -->
    <section class="lx-section lx-appsec">
      <div class="container lx-app">
        <div class="lx-app__phone lx-reveal" aria-hidden="true">
          <div class="lx-app__screen">
            <div class="lx-app__bar"><span>21:45</span><span class="lx-app__notch"></span><span>5G</span></div>
            <img class="lx-app__logo" src="assets/images/pegasus-smarthomes-logo.png" alt="" width="1200" height="218">
            <div class="lx-app__tabs"><span class="is-active">Home</span><span>Rooms</span><span>Scenes</span></div>
            <div class="lx-app__grid">{tiles}</div>
          </div>
        </div>
        <div class="lx-app__text lx-reveal">
          <p class="lx-eyebrow">Your property in your hands</p>
          <h2 class="lx-title">One app.<br><em>Complete control.</em></h2>
          <p class="lx-control__body">Control lights, climate, curtains, sensors and every connected device across your rooms and buildings from one easy-to-use mobile app, available on Android and iOS.</p>
          <ul class="lx-app__feats">
{feats}
          </ul>
          <p class="lx-app__stores"><span>Android</span><span>iOS</span><span>Siri</span><span>Google Assistant</span></p>
        </div>
      </div>
    </section>

"""

# ---------------------------------------------------------------- Pegasus TV
TV_APPS = ["Live TV", "Apps", "Music", "Photos"]
TV_TILES = [("Lights", "Warm &middot; 70%", True), ("Climate", "23&deg;C", True), ("Curtains", "Closed", False), ("Front door", "Locked", True)]
TV_FEATS = [
  ("Pegasus smart OS, built on Android", '<rect x="3" y="4" width="18" height="12" rx="2"/><path d="M8 20h8M12 16v4"/>'),
  ("Every IoT device on the big screen", '<circle cx="12" cy="12" r="2"/><path d="M8.5 8.5a5 5 0 0 0 0 7M15.5 8.5a5 5 0 0 1 0 7M5.6 5.6a9 9 0 0 0 0 12.8M18.4 5.6a9 9 0 0 1 0 12.8"/>'),
  ("Scenes and controls from the remote", '<rect x="8" y="2.5" width="8" height="19" rx="4"/><circle cx="12" cy="8" r="1.6"/><path d="M10.5 13h3M10.5 16h3"/>'),
  ("Live alerts from every sensor", '<path d="M6 16V11a6 6 0 0 1 12 0v5l1.5 2h-15z"/><path d="M10 20.5a2 2 0 0 0 4 0"/>'),
]

def tv_section():
    apps = "".join(f"<span>{a}</span>" for a in TV_APPS)
    tiles = "".join(f'<div class="lx-tv__tile{" is-on" if on else ""}"><i></i><strong>{t}</strong><span>{v}</span></div>'
                    for t, v, on in TV_TILES)
    feats = "\n".join(f"            <li>{icon(p)}<span>{t}</span></li>" for t, p in TV_FEATS)
    return f"""    <!-- ===== Pegasus TV ===== -->
    <section class="lx-section lx-section--alt">
      <div class="container lx-tvsec">
        <div class="lx-tvsec__text lx-reveal">
          <p class="lx-eyebrow">Pegasus TV</p>
          <h2 class="lx-title">The screen that<br><em>runs the room.</em></h2>
          <p class="lx-control__body">Pegasus-branded smart TVs run Pegasus, our smart OS built on Android and integrated with every SmartHomes device. Watch your favourite apps, then dim the lights, set the temperature or close the curtains without leaving the sofa.</p>
          <ul class="lx-app__feats">
{feats}
          </ul>
        </div>

        <!-- Illustrative Pegasus OS home screen -->
        <div class="lx-tv lx-reveal" aria-hidden="true">
          <div class="lx-tv__screen">
            <div class="lx-tv__bar">
              <img src="assets/images/pegasus-tv-logo.png" alt="" width="428" height="107">
              <span class="lx-tv__status"><span class="lx-tv__toast"><i></i>Motion detected &middot; Lobby</span>21:45</span>
            </div>
            <p class="lx-tv__hello">Good evening<span>Living room &middot; 23&deg;C</span></p>
            <div class="lx-tv__apps">{apps}</div>
            <div class="lx-tv__home">
              <p>Smart home</p>
              <div class="lx-tv__tiles">{tiles}</div>
            </div>
          </div>
          <span class="lx-tv__stand"></span>
        </div>
      </div>
    </section>

"""

def build():
    pillars = "\n".join(f'''          <div class="lx-pillar lx-reveal">
            <span class="lx-pillar__num">{n}</span>
            <h3>{t}</h3>
            <p>{d}</p>
          </div>''' for n, t, d in PILLARS)

    moments = []
    for i, (img, num, time, label, title, text, specs, alt) in enumerate(MOMENTS):
        flip = " lx-moment--flip" if i % 2 else ""
        lazy = ' loading="lazy"'
        spec_html = "".join(f"<li>{s}</li>" for s in specs)
        moments.append(f'''        <article class="lx-moment{flip}">
          <figure class="lx-moment__media lx-reveal">
            <img src="assets/images/smarthomes/{img}.jpg" alt="{alt}" width="1200" height="1500"{lazy}>
          </figure>
          <div class="lx-moment__text lx-reveal">
            <span class="lx-moment__num">{num}</span>
            <p class="lx-eyebrow">{time} <span aria-hidden="true">&mdash;</span> {label}</p>
            <h3 class="lx-moment__title">{title}</h3>
            <p class="lx-moment__body">{text}</p>
            <ul class="lx-specs">{spec_html}</ul>
          </div>
        </article>''')

    domains = "\n".join(f'''          <div class="lx-sensor lx-reveal">
            {icon(p)}
            <h3>{t}</h3>
            <p>{d}</p>
          </div>''' for t, d, p in DOMAINS)

    sensors = "\n".join(f'''          <div class="lx-sensor lx-reveal">
            {icon(p)}
            <h3>{t}</h3>
            <p>{d}</p>
          </div>''' for t, d, p in SENSORS)

    scale = "\n".join(f'''          <div class="lx-tier lx-reveal">
            <p class="lx-eyebrow">{k}</p>
            <h3>{t}</h3>
            <p>{d}</p>
          </div>''' for k, t, d in SCALE)

    connect = '<span class="lx-dot" aria-hidden="true"></span>'.join(f"<span>{c}</span>" for c in CONNECT)

    scene_buttons = "".join(
        f'<button type="button" class="lx-scene{" is-active" if k == "welcome" else ""}" data-scene="{k}" '
        f'data-lights="{v[0]}" data-climate="{v[1]}" data-curtains="{v[2]}" data-music="{v[3]}" data-glow="{v[4]}" '
        f'aria-pressed="{"true" if k == "welcome" else "false"}">{k.capitalize()}</button>'
        for k, v in SCENES.items())
    w = SCENES["welcome"]

    return f'''  <main class="lx">
    <!-- ===== Hero ===== -->
    <section class="lx-hero">
      <div class="lx-hero__aura" aria-hidden="true">
        <span class="lx-hero__glow lx-hero__glow--indigo"></span>
        <span class="lx-hero__glow lx-hero__glow--violet"></span>
        <span class="lx-hero__glow lx-hero__glow--pink"></span>
        <span class="lx-hero__rings"><i></i><i></i><i></i></span>
      </div>
      <div class="container lx-hero__inner">
        <img class="lx-hero__logo" src="assets/images/pegasus-smarthomes-logo.png" alt="Pegasus SmartHomes" width="1200" height="218">
        <h1 class="lx-hero__title">The art of the<br><em>intelligent building.</em></h1>
        <p class="lx-hero__text">Automation for every sensor, IoT device and building system, across homes, hotels and entire properties, from a single room to an entire skyline.</p>
        <div class="lx-actions">
          <a href="{MAIL}" class="lx-btn lx-btn--solid">Arrange a private consultation</a>
          <a href="#the-experience" class="lx-btn">Discover the experience</a>
        </div>
      </div>
      <a href="#the-experience" class="lx-scroll" aria-label="Scroll to the experience"><span>Scroll</span><i></i></a>
    </section>

    <!-- ===== Manifesto ===== -->
    <section id="the-experience" class="lx-section lx-manifesto">
      <div class="container">
        <p class="lx-eyebrow lx-reveal">The experience</p>
        <p class="lx-statement lx-reveal">Light that knows the hour. Air that knows the guest. A building that <em>thinks ahead</em>, quietly, invisibly, beautifully.</p>
        <div class="lx-pillars">
{pillars}
        </div>
      </div>
    </section>

    <!-- ===== What we automate ===== -->
    <section class="lx-section lx-section--alt">
      <div class="container">
        <header class="lx-head lx-head--split lx-reveal">
          <div>
            <p class="lx-eyebrow">What we automate</p>
            <h2 class="lx-title">Not just lights.<br><em>Everything.</em></h2>
          </div>
          <p class="lx-head__text">Homes, hotels, offices and entire buildings: if it can be sensed, switched or measured, Pegasus SmartHomes can automate it.</p>
        </header>
        <div class="lx-sensors">
{domains}
        </div>
      </div>
    </section>

{showcase_top()}    <!-- ===== A day in the suite ===== -->
    <section class="lx-section">
      <div class="container">
        <header class="lx-head lx-reveal">
          <p class="lx-eyebrow">In hospitality: a day in the suite</p>
          <h2 class="lx-title">Choreographed from arrival<br>to <em>sunrise.</em></h2>
        </header>
        <!-- Photos (Unsplash): arrival @albert-stoynov, welcome @sung-jin-cho, evening @archee-lal, morning @fujiphilm -->
{chr(10).join(moments)}
      </div>
    </section>

    <!-- ===== Sensors ===== -->
    <section class="lx-section lx-section--alt">
      <div class="container">
        <header class="lx-head lx-head--split lx-reveal">
          <div>
            <p class="lx-eyebrow">The sensors</p>
            <h2 class="lx-title">Every sensor,<br><em>beautifully hidden.</em></h2>
          </div>
          <p class="lx-head__text">Discreet, wireless and built for homes, hotels and commercial buildings, each sensor quietly feeds one intelligent system that looks after your guests and your building.</p>
        </header>
        <div class="lx-sensors">
{sensors}
        </div>
      </div>
    </section>

{app_section()}{tv_section()}    <!-- ===== Scale ===== -->
    <section class="lx-scale">
      <!-- Photo: Petar Avramoski / Unsplash (unsplash.com/license) -->
      <img class="lx-scale__bg" src="assets/images/sectors/construction.jpg" alt="" width="1600" height="900" loading="lazy">
      <div class="container lx-scale__inner">
        <header class="lx-head lx-reveal">
          <p class="lx-eyebrow">Scale</p>
          <h2 class="lx-title">From one suite<br>to an <em>entire skyline.</em></h2>
        </header>
        <div class="lx-tiers">
{scale}
        </div>
      </div>
    </section>

    <!-- ===== Scene controller (interactive) ===== -->
    <section class="lx-section">
      <div class="container lx-control">
        <div class="lx-control__text lx-reveal">
          <p class="lx-eyebrow">Guest control</p>
          <h2 class="lx-title">Your suite,<br><em>in your hand.</em></h2>
          <p class="lx-control__body">Guests set the mood from the in-room panel, their phone or simply their voice. Your team sees every room, live, from one elegant dashboard.</p>
          <ul class="lx-specs lx-specs--inline"><li>In-room panel</li><li>Guest app</li><li>Voice control</li><li>Staff dashboard</li></ul>
          <p class="lx-hint">Try a scene on the panel.</p>
        </div>

        <div class="lx-panel lx-reveal" data-scene-panel style="--glow: {w[4]}">
          <div class="lx-panel__glow" aria-hidden="true"></div>
          <div class="lx-panel__head">
            <div>
              <p class="lx-eyebrow">Suite 1204</p>
              <p class="lx-panel__guest">Good evening</p>
            </div>
            <span class="lx-panel__status"><i></i>Occupied</span>
          </div>
          <div class="lx-panel__scenes" role="group" aria-label="Scenes">{scene_buttons}</div>
          <dl class="lx-panel__grid" aria-live="polite">
            <div><dt>Lights</dt><dd data-field="lights">{w[0]}</dd></div>
            <div><dt>Climate</dt><dd data-field="climate">{w[1]}</dd></div>
            <div><dt>Curtains</dt><dd data-field="curtains">{w[2]}</dd></div>
            <div><dt>Music</dt><dd data-field="music">{w[3]}</dd></div>
          </dl>
          <div class="lx-panel__sensors" aria-hidden="true">
            <span><i></i>Presence</span><span><i></i>Air</span><span><i></i>Water</span><span><i></i>Energy</span>
          </div>
        </div>
      </div>
    </section>

    <!-- ===== Connected ===== -->
    <section class="lx-connect">
      <div class="container">
        <p class="lx-eyebrow">Connected to everything you run</p>
        <p class="lx-connect__list">{connect}</p>
      </div>
    </section>

    <!-- ===== Close ===== -->
    <section class="lx-close">
      <!-- Photo: mr_wdh / Unsplash (unsplash.com/license) -->
      <img class="lx-close__bg" src="assets/images/smarthomes/close.jpg" alt="" width="1800" height="1012" loading="lazy">
      <div class="container lx-close__inner lx-reveal">
        <p class="lx-eyebrow">Private consultation</p>
        <h2 class="lx-close__title">Let us design your<br><em>intelligent property.</em></h2>
        <p class="lx-close__text">From a single room to a portfolio of hotels and buildings, our SmartHomes team in Indore will survey, design and deliver it with you.</p>
        <div class="lx-actions lx-actions--center">
          <a href="{MAIL}" class="lx-btn lx-btn--solid">Arrange a consultation</a>
          <a href="{SURVEY}" class="lx-btn">Book a site survey</a>
        </div>
        <p class="lx-close__contact">
          <a href="{TEL}">+91 0731 474 5928</a><span aria-hidden="true">&middot;</span><a href="mailto:connect@mypegasus.in">connect@mypegasus.in</a><span aria-hidden="true">&middot;</span><span>Vijay Nagar, Indore</span>
        </p>
      </div>
    </section>
  </main>
'''

def main():
    os.chdir(PUBLIC)
    idx = open("index.html").read()
    head_nav = idx[:idx.index("  <main>")]
    tail = idx[idx.index("  <!-- ===== Footer"):]

    head_nav = head_nav.replace("<title>Pegasus</title>", "<title>Pegasus SmartHomes</title>")
    head_nav = head_nav.replace('content="Pegasus — enterprise technology that connects everything."',
                                'content="Pegasus SmartHomes: automation for sensors, IoT devices, buildings and hospitality, from a single room to enterprise properties."')
    head_nav = head_nav.replace('<meta name="theme-color" content="#000000">', '<meta name="theme-color" content="#0b0b0c">')
    fonts = ('  <link rel="preconnect" href="https://fonts.googleapis.com">\n'
             '  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>\n'
             '  <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Outfit:wght@200;300;400;500&display=swap">\n')
    head_nav = head_nav.replace('  <link rel="stylesheet" href="css/styles.css">\n',
                                fonts + '  <link rel="stylesheet" href="css/styles.css">\n  <link rel="stylesheet" href="css/smarthomes.css">\n')
    head_nav = re.sub(r"<body[^>]*>", '<body id="top" class="theme-dark">', head_nav, count=1)
    # dark navbar: white logo
    head_nav = re.sub(r'<a href="index.html" class="navbar__logo" aria-label="Pegasus home">\s*<img[^>]*>',
                      f'<a href="{SUBDOMAIN}" class="navbar__logo navbar__logo--smarthomes" aria-label="Pegasus SmartHomes home">\n'
                      '        <img src="assets/images/pegasus-smarthomes-logo.png" alt="Pegasus SmartHomes" width="1200" height="218">',
                      head_nav)
    tail = re.sub(r'(class="footer__logo"[^>]*>\s*<img src="assets/images/)logo\.png', r'\1logo-white.png', tail)
    tail = tail.replace('<a href="#" class="footer__top"', '<a href="#top" class="footer__top"')

    page = head_nav + build() + "\n" + tail
    page = page.replace('href="#section-', 'href="index.html#section-')
    # served from the subdomain, so links to other pages must point at the main site
    page = re.sub(r'href="index\.html', f'href="{SITE}', page)
    page = re.sub(r'href="(construction|hospitality)\.html', rf'href="{SITE}\1', page)
    page = page.replace("<title>Pegasus SmartHomes</title>", f'<title>Pegasus SmartHomes</title>\n  <link rel="canonical" href="{SUBDOMAIN}">', 1)
    assert 'navbar__logo--smarthomes' in page and 'logo-white.png' in page, "logo swap failed"
    assert '<body id="top" class="theme-dark">' in page, "dark theme class missing"
    open("smarthomes.html", "w").write(page)
    print("written smarthomes.html", len(page))

main()
