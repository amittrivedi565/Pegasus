  <!-- ===== Page sub-navigation ===== -->
  <nav class="subnav" aria-label="{IND_NAME} page sections">
    <div class="container subnav__inner">
      <div class="subnav__title">
        <a href="index.html#section-one" class="subnav__crumb">Industries</a>
        <span>{IND_NAME}</span>
      </div>
      <ul class="subnav__links">
        <li><a href="#overview" class="is-active">Overview</a></li>
        <li><a href="#products">Products</a></li>
{SUBNAV_EXTRA}        <li><a href="#use-cases">Use cases</a></li>
        <li><a href="#why-pegasus">Why Pegasus</a></li>
        <li><a href="#get-started">Get started</a></li>
      </ul>
    </div>
  </nav>

  <main>
    <!-- ===== Hero ===== -->
    <section id="overview" class="ind-hero">
      <div class="container ind-hero__inner">
        <div class="ind-hero__content">
          <h1 class="ind-hero__title">{IND_NAME}</h1>
          <p class="ind-hero__text">{HERO_TEXT}</p>
          <div class="ind-actions">
            <a href="{DEMO}" class="btn btn--light">Request a demo</a>
            <a href="#products" class="btn btn--outline-light">Explore Pegasus {PRODUCT}</a>
          </div>
        </div>
        <div class="ind-hero__media">
          <!-- Photo: {HERO_CREDIT} / Unsplash (unsplash.com/license) -->
          <img src="assets/images/{IMG_DIR}/hero.jpg" alt="{HERO_ALT}" width="1600" height="900"{HERO_STYLE}>
        </div>
      </div>
    </section>

    <!-- ===== Intro ===== -->
    <section class="section">
      <div class="container">
        <header class="section-head">
          <h2 class="section-title">{INTRO_TITLE}</h2>
          <p class="section-subtitle">{INTRO_SUB}</p>
        </header>
        <div class="ind-intro">
          <!-- Photo: {INTRO_CREDIT} / Unsplash (unsplash.com/license) -->
          <img class="ind-intro__media" src="assets/images/{IMG_DIR}/intro.jpg" alt="{INTRO_ALT}" width="1600" height="900" loading="lazy">
          <div class="ind-intro__text">
            <h3>Pegasus {PRODUCT} can help you:</h3>
            <ul class="ind-bullets">
{BULLETS}
            </ul>
          </div>
        </div>
      </div>
    </section>

{SMARTHOMES}    <!-- ===== Products (tabs) ===== -->
    <section id="products" class="section">
      <div class="container">
        <header class="section-head">
          <h2 class="section-title">{PRODUCTS_TITLE}</h2>
          <p class="section-subtitle">{PRODUCTS_SUB}</p>
        </header>

        <div class="ind-tabs" role="tablist" aria-label="Solution areas">
{TABS}
        </div>

{PANELS}

        <div class="ind-actions ind-actions--section">
          <a href="{CONTACT}" class="btn btn--primary">Contact us to get started</a>
          <a href="index.html#section-one" class="btn btn--outline">Explore more industries</a>
        </div>
      </div>
    </section>

    <!-- ===== Use cases ===== -->
    <section id="use-cases" class="section">
      <div class="container">
        <header class="section-head">
          <h2 class="section-title">{UC_TITLE}</h2>
          <p class="section-subtitle">{UC_SUB}</p>
        </header>
        <div class="ind-usecases">
{USECASES}
        </div>
      </div>
    </section>

    <!-- ===== Why Pegasus (in place of customer stories) ===== -->
    <section id="why-pegasus" class="section">
      <div class="container">
        <header class="section-head">
          <h2 class="section-title">{WHY_TITLE}</h2>
        </header>
        <div class="ind-whys">
{WHYS}
        </div>
        <div class="ind-actions ind-actions--section">
          <a href="{CONTACT}" class="btn btn--outline">{SPECIALIST_BTN}</a>
        </div>

        <aside class="ind-banner">
          <div>
            <p class="ind-banner__eyebrow">Live demo</p>
            <h2 class="ind-banner__title">See Pegasus {PRODUCT} in action</h2>
            <p>{DEMO_TEXT}</p>
          </div>
          <a href="{DEMO}" class="btn btn--primary">Book a demo</a>
        </aside>
      </div>
    </section>

    <!-- ===== Take the next step ===== -->
    <section id="get-started" class="section">
      <div class="container">
        <header class="section-head">
          <h2 class="section-title">Take the next step</h2>
          <p class="section-subtitle">Talk to our team about your business and see how Pegasus {PRODUCT} fits.</p>
        </header>
        <div class="ind-actions ind-actions--section">
          <a href="{CONTACT}" class="btn btn--primary">Contact us to get started</a>
          <a href="index.html#section-one" class="btn btn--outline">Explore more industries</a>
        </div>
      </div>
    </section>
  </main>
