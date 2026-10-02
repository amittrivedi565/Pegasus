// Pegasus — site scripts

document.addEventListener("DOMContentLoaded", () => {
  initNavbar();
  initStories();
  initTabs();
  initSubnav();
  initLuxury();

  // Footer year
  const year = document.getElementById("year");
  if (year) year.textContent = new Date().getFullYear();
});

function initNavbar() {
  const navbar = document.querySelector(".navbar");
  const nav = document.querySelector(".navbar__nav");
  const toggle = document.querySelector(".navbar__toggle");
  const items = document.querySelectorAll(".nav-item");
  const desktop = window.matchMedia("(min-width: 1025px) and (hover: hover)");
  const CLOSE_DELAY = 150;
  let closeTimer;

  const setOpen = (item, open) => {
    item.classList.toggle("is-open", open);
    item.querySelector(".nav-link").setAttribute("aria-expanded", String(open));
  };

  const closeAll = (except) => {
    items.forEach((item) => {
      if (item !== except) setOpen(item, false);
    });
  };

  items.forEach((item) => {
    const link = item.querySelector(".nav-link");

    // Click / tap toggles the menu (desktop and mobile accordion)
    // (on hover devices the menu is already open from mouseenter, so keep it open)
    link.addEventListener("click", () => {
      const open = desktop.matches || !item.classList.contains("is-open");
      closeAll(item);
      setOpen(item, open);
    });

    // Hover opens the mega menu on desktop
    item.addEventListener("mouseenter", () => {
      if (!desktop.matches) return;
      clearTimeout(closeTimer);
      closeAll(item);
      setOpen(item, true);
    });

    item.addEventListener("mouseleave", () => {
      if (!desktop.matches) return;
      closeTimer = setTimeout(() => setOpen(item, false), CLOSE_DELAY);
    });
  });

  // Mobile hamburger
  if (toggle && nav) {
    toggle.addEventListener("click", () => {
      const open = nav.classList.toggle("is-open");
      toggle.setAttribute("aria-expanded", String(open));
      if (!open) closeAll();
    });
  }

  // Following a link inside the menu closes everything (menus now jump to on-page sections)
  nav.querySelectorAll(".mega a").forEach((a) => {
    a.addEventListener("click", () => {
      closeAll();
      nav.classList.remove("is-open");
      toggle.setAttribute("aria-expanded", "false");
    });
  });

  // Escape closes any open menu and returns focus to its trigger
  document.addEventListener("keydown", (e) => {
    if (e.key !== "Escape") return;
    const openItem = document.querySelector(".nav-item.is-open");
    if (openItem) {
      setOpen(openItem, false);
      openItem.querySelector(".nav-link").focus();
    }
  });

  // Clicking outside the navbar closes menus
  document.addEventListener("click", (e) => {
    if (!navbar.contains(e.target)) closeAll();
  });

  // Reset mobile state when resizing to desktop
  desktop.addEventListener("change", () => {
    closeAll();
    nav.classList.remove("is-open");
    toggle.setAttribute("aria-expanded", "false");
  });
}

// Customer stories: one story open at a time, media panel follows the selection
function initStories() {
  const stories = document.querySelectorAll(".story");
  const media = document.querySelectorAll(".story-media");

  stories.forEach((story, index) => {
    story.querySelector(".story__title").addEventListener("click", () => {
      stories.forEach((s, i) => {
        const active = i === index;
        s.classList.toggle("is-active", active);
        s.querySelector(".story__title").setAttribute("aria-expanded", String(active));
        media[i]?.classList.toggle("is-active", active);
      });
    });
  });
}

// Accessible tabs: click or arrow keys switch panels
function initTabs() {
  document.querySelectorAll('[role="tablist"]').forEach((list) => {
    const tabs = [...list.querySelectorAll('[role="tab"]')];

    const select = (tab) => {
      tabs.forEach((t) => {
        const active = t === tab;
        t.setAttribute("aria-selected", String(active));
        t.tabIndex = active ? 0 : -1;
        document.getElementById(t.getAttribute("aria-controls")).hidden = !active;
      });
    };

    tabs.forEach((tab, i) => {
      tab.addEventListener("click", () => select(tab));
      tab.addEventListener("keydown", (e) => {
        const step = { ArrowRight: 1, ArrowLeft: -1 }[e.key];
        if (!step) return;
        const next = tabs[(i + step + tabs.length) % tabs.length];
        select(next);
        next.focus();
      });
    });
  });
}

// Page sub-navigation: highlight the section currently in view
function initSubnav() {
  const links = [...document.querySelectorAll(".subnav__links a")];
  if (!links.length) return;

  const setActive = (id) => {
    links.forEach((a) => a.classList.toggle("is-active", a.getAttribute("href") === "#" + id));
  };

  // A section counts as "current" when it crosses a band 30-40% down the viewport
  const observer = new IntersectionObserver((entries) => {
    entries.forEach((entry) => {
      if (entry.isIntersecting) setActive(entry.target.id);
    });
  }, { rootMargin: "-30% 0px -60% 0px" });

  links
    .map((a) => document.querySelector(a.getAttribute("href")))
    .filter(Boolean)
    .forEach((section) => observer.observe(section));
}

// SmartHomes luxury page: gentle scroll reveals + interactive scene panel
function initLuxury() {
  if (!document.querySelector(".lx")) return;
  const reduceMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  // Reveal on scroll (content stays visible without JS or with reduced motion)
  if (!reduceMotion && "IntersectionObserver" in window) {
    document.documentElement.classList.add("lx-anim");
    const observer = new IntersectionObserver((entries) => {
      entries.forEach((entry) => {
        if (!entry.isIntersecting) return;
        entry.target.classList.add("is-visible");
        observer.unobserve(entry.target);
      });
    }, { rootMargin: "0px 0px -10% 0px", threshold: 0.12 });
    document.querySelectorAll(".lx-reveal").forEach((el) => observer.observe(el));
  }

  // Scene controller: each button carries its values in data-* attributes
  const panel = document.querySelector("[data-scene-panel]");
  if (!panel) return;
  const buttons = panel.querySelectorAll(".lx-scene");
  const fields = panel.querySelectorAll("[data-field]");

  buttons.forEach((button) => {
    button.addEventListener("click", () => {
      buttons.forEach((b) => {
        const active = b === button;
        b.classList.toggle("is-active", active);
        b.setAttribute("aria-pressed", String(active));
      });
      panel.style.setProperty("--glow", button.dataset.glow);

      fields.forEach((dd) => {
        const value = button.dataset[dd.dataset.field];
        if (reduceMotion) {
          dd.textContent = value;
          return;
        }
        dd.classList.add("is-changing");
        setTimeout(() => {
          dd.textContent = value;
          dd.classList.remove("is-changing");
        }, 250);
      });
    });
  });
}

