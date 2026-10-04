// Serves the static site in public/ and gives every page one canonical address:
//   https://mypegasus.in/, /construction, /hospitality  and  https://smarthomes.mypegasus.in/
// Only runs for the page paths listed in run_worker_first (wrangler.jsonc); assets are served directly.
const MAIN_HOST = "mypegasus.in";
const SMARTHOMES_HOST = "smarthomes.mypegasus.in";

// page path -> canonical path on the main site
const MAIN_PAGES = {
  "/": "/",
  "/index.html": "/",
  "/construction": "/construction",
  "/construction.html": "/construction",
  "/hospitality": "/hospitality",
  "/hospitality.html": "/hospitality",
};
const SMARTHOMES_PATHS = new Set(["/smarthomes", "/smarthomes.html"]);

const redirect = (location) => Response.redirect(location, 301);

export default {
  async fetch(request, env) {
    const url = new URL(request.url);
    const { hostname, pathname, search } = url;

    // www, *.workers.dev and plain http all collapse onto https://mypegasus.in
    if (hostname === `www.${MAIN_HOST}` || hostname.endsWith(".workers.dev")) {
      return redirect(`https://${MAIN_HOST}${MAIN_PAGES[pathname] ?? pathname}${search}`);
    }
    if (url.protocol === "http:" && (hostname === MAIN_HOST || hostname === SMARTHOMES_HOST)) {
      url.protocol = "https:";
      return redirect(url.toString());
    }

    if (hostname === SMARTHOMES_HOST) {
      // smarthomes.mypegasus.in/ shows the SmartHomes page (address bar stays on the subdomain)
      if (pathname === "/") {
        url.pathname = "/smarthomes";
        return env.ASSETS.fetch(new Request(url, request));
      }
      if (SMARTHOMES_PATHS.has(pathname)) return redirect(`https://${SMARTHOMES_HOST}/${search}`);
      // other pages live on the main site
      if (pathname in MAIN_PAGES) return redirect(`https://${MAIN_HOST}${MAIN_PAGES[pathname]}${search}`);
    } else if (hostname === MAIN_HOST) {
      if (SMARTHOMES_PATHS.has(pathname)) return redirect(`https://${SMARTHOMES_HOST}/${search}`);
      // /index.html and *.html -> extensionless canonical (301 instead of the assets' 307)
      if (MAIN_PAGES[pathname] && MAIN_PAGES[pathname] !== pathname) {
        return redirect(`https://${MAIN_HOST}${MAIN_PAGES[pathname]}${search}`);
      }
    }

    return env.ASSETS.fetch(request);
  },
};
