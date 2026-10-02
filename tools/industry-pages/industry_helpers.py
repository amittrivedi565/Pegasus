import os
CHEV = '<svg viewBox="0 0 16 16" aria-hidden="true"><path d="M6 3l5 5-5 5" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></svg>'
TABIDX = ' tabindex="-1"'
NL14 = "\n              "
NL18 = "\n                  "

def la(text, href="#"):
    ext = ' target="_blank" rel="noopener"' if href.startswith("http") else ""
    return f'<a href="{href}" class="link-arrow"{ext}>{text} {CHEV}</a>'

ICON = {
 "chart":   '<path d="M4 20h16M7 16v-5M12 16V7M17 16v-8"/>',
 "sync":    '<path d="M4 12a8 8 0 0 1 14-5.3M20 12a8 8 0 0 1-14 5.3"/><path d="M18 3v4h-4M6 21v-4h4"/>',
 "invoice": '<path d="M6 3h12v18l-3-2-3 2-3-2-3 2z"/><path d="M9 8h6M9 12h6"/>',
 "wrench":  '<path d="M14.5 5.5a4 4 0 0 0-5 5L4 16l4 4 5.5-5.5a4 4 0 0 0 5-5l-2.5 2.5-2.5-.5-.5-2.5z"/>',
 "users":   '<circle cx="9" cy="8" r="3"/><path d="M3 20c0-3.3 2.7-6 6-6s6 2.7 6 6"/><circle cx="17" cy="9" r="2.5"/><path d="M16.5 14c2.5.2 4.5 2.3 4.5 5"/>',
 "badge":   '<circle cx="12" cy="9" r="5"/><path d="M9 13.5L8 21l4-2 4 2-1-7.5"/>',
 "clock":   '<circle cx="12" cy="12" r="8"/><path d="M12 8v4l3 2"/>',
 "userplus":'<circle cx="10" cy="8" r="3.5"/><path d="M3.5 20c0-3.6 2.9-6.5 6.5-6.5M18 13v6M15 16h6"/>',
 "cart":    '<path d="M3 4h2l2.5 11h10.5l2-8H6.5"/><circle cx="9" cy="19" r="1.5"/><circle cx="17" cy="19" r="1.5"/>',
 "boxes":   '<rect x="3" y="12" width="8" height="8" rx="1"/><rect x="13" y="12" width="8" height="8" rx="1"/><rect x="8" y="3" width="8" height="8" rx="1"/>',
 "handshake":'<path d="M3 12l4-4 4 2 3-2 7 4M3 12l6 6 2-2M21 12l-5 5-3-3M9 18l2 2 2-2"/>',
 "truck":   '<path d="M2 6h11v10H2zM13 10h4l4 3v3h-8z"/><circle cx="6" cy="18" r="1.5"/><circle cx="17" cy="18" r="1.5"/>',
 "calc":    '<rect x="5" y="3" width="14" height="18" rx="2"/><path d="M8 7h8M8 12h.01M12 12h.01M16 12h.01M8 16h.01M12 16h.01M16 16h.01"/>',
 "funnel":  '<path d="M3 4h18l-7 8v6l-4 2v-8z"/>',
 "doc":     '<path d="M6 3h9l4 4v14H6z"/><path d="M9 11h7M9 15h7"/>',
 "portal":  '<rect x="3" y="4" width="18" height="14" rx="2"/><path d="M3 8h18M8 21h8"/>',
 "dash":    '<rect x="3" y="3" width="8" height="8" rx="1"/><rect x="13" y="3" width="8" height="5" rx="1"/><rect x="13" y="10" width="8" height="11" rx="1"/><rect x="3" y="13" width="8" height="8" rx="1"/>',
 "spark":   '<path d="M3 17l5-5 4 3 8-9"/><path d="M15 6h5v5"/>',
 "db":      '<ellipse cx="12" cy="6" rx="7" ry="3"/><path d="M5 6v12c0 1.7 3.1 3 7 3s7-1.3 7-3V6M5 12c0 1.7 3.1 3 7 3s7-1.3 7-3"/>',
 "shield":  '<path d="M12 3l8 3v6c0 5-3.5 8-8 9-4.5-1-8-4-8-9V6z"/><path d="M9 12l2 2 4-4"/>',
 "bot":     '<rect x="5" y="8" width="14" height="11" rx="3"/><path d="M12 4v4M9 13h.01M15 13h.01"/>',
 "plug":    '<path d="M9 3v5M15 3v5M6 8h12v4a6 6 0 0 1-12 0zM12 18v3"/>',
 "code":    '<path d="M8 7l-5 5 5 5M16 7l5 5-5 5"/>',
 "scale":   '<path d="M12 3v18M6 21h12M4 8h16M7 8l-3 7a3 3 0 0 0 6 0zM17 8l-3 7a3 3 0 0 0 6 0z"/>',
 "helmet":  '<path d="M4 17h16M5 17a7 7 0 0 1 14 0M10 10V6h4v4"/>',
 "play":    '<circle cx="12" cy="12" r="9"/><path d="M10 8.5v7l5.5-3.5z"/>',
 "pin":     '<path d="M12 21s-7-6.2-7-11.5a7 7 0 0 1 14 0C19 14.8 12 21 12 21z"/><circle cx="12" cy="9.5" r="2.5"/>',
}
def visual(icon, label=None):
    chip = f'<span class="ind-visual__chip">{label}</span>' if label else ""
    return f'<div class="ind-visual" aria-hidden="true">{chip}<svg viewBox="0 0 24 24">{ICON[icon]}</svg></div>'

