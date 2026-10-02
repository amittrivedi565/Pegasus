// Serves the static site in public/ and maps the SmartHomes subdomain to the SmartHomes page.
const SMARTHOMES_HOST = "smarthomes.mypegasus.in";

export default {
  async fetch(request, env) {
    const url = new URL(request.url);

    if (url.hostname === SMARTHOMES_HOST) {
      // smarthomes.mypegasus.in/ shows the SmartHomes page (address bar stays on the subdomain)
      if (url.pathname === "/") {
        url.pathname = "/smarthomes";
        return env.ASSETS.fetch(new Request(url, request));
      }
    } else if (url.pathname === "/smarthomes" || url.pathname === "/smarthomes.html") {
      // one canonical address: mypegasus.in/smarthomes -> smarthomes.mypegasus.in
      return Response.redirect(`https://${SMARTHOMES_HOST}/${url.search}`, 301);
    }

    return env.ASSETS.fetch(request);
  },
};
