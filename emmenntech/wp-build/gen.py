"""Builder for elementor-build-composition payloads (EmmEnn Tech)."""
import json, re, os
HERE = os.path.dirname(os.path.abspath(__file__))
A = json.load(open(os.path.join(HERE, 'assets.json')))
PAGES = json.load(open(os.path.join(HERE, 'pages.json')))

# Media that has not been uploaded yet → closest uploaded stand-in.
# Upload the real file (same name) and rebuild to swap it in automatically.
SUBST = {
    'seo-services': 'client-report-review',
    'strategy-meeting': 'hero-team-strategy',
    'planning-whiteboard': 'hero-team-strategy',
    'support-team': 'contact-banner',
    'services-banner': 'ai-search-optimization',
    'social-media-marketing': 'happy-customers',
    'small-business-owner': 'happy-customers',
    'mobile-friendly-website': 'website-development',
}

def media(name):
    key = 'emmenntech-' + name
    if key not in A:
        key = 'emmenntech-' + SUBST[name]
    return A[key]

def img(name, size="full", alt=""):
    m = media(name)
    return {"image": {"src": {"id": m['id'], "alt": alt}, "size": size}}

def bg(name):
    return f"url({media(name)['url']})"

FA5 = {"magnifying-glass-chart": "search", "display": "desktop", "location-dot": "map-marker-alt", "xmark": "times",
       "wand-magic-sparkles": "magic", "share-nodes": "share-alt", "magnifying-glass": "search"}

def fa(icon, lib="fa-solid"):
    """Font Awesome 5 icon for e-svg (Elementor ships FA5), e.g. fa('phone')."""
    icon = FA5.get(icon, icon)
    pre = {"fa-solid": "fas", "fa-brands": "fab", "fa-regular": "far"}[lib]
    return {"svg": {"value": f"{pre} fa-{icon}", "library": lib}}

def link_page(key):
    return {"destination": {"id": PAGES[key]}, "tag": "a"}

def link_url(u, blank=False):
    return {"destination": u, "isTargetBlank": blank, "tag": "a"}

class B:
    def __init__(s):
        s.cfg = {}; s.sty = {}; s.cls = {}; s.ids = set()

    def el(s, tag, cid, kids=(), cfg=None, style=None, classes=None):
        cid = re.sub(r'[^A-Za-z0-9 _-]', '', cid.replace('&', 'and')).strip()
        assert cid not in s.ids, cid
        s.ids.add(cid)
        if cfg: s.cfg[cid] = cfg
        if style: s.sty[cid] = style
        if classes: s.cls[cid] = classes
        return f'<{tag} configuration-id="{cid}">{"".join(kids)}</{tag}>'

    def payload(s, post_id, xml, parent="document", mode="replace_children"):
        return {"post_id": post_id, "xml_structure": xml, "element_config": s.cfg,
                "style": s.sty, "classes": s.cls, "parent_id": parent, "mode": mode}

# design asset key (from ../src.html) -> media name in the Media Library
DESIGN = {
    's-seo': 'seo-services', 's-gbp': 'local-seo-google-maps', 's-landing': 'google-ads-management',
    's-webdev': 'website-development', 's-social': 'social-media-marketing', 'hero-bg': 'ai-search-optimization',
    's-reviews': 'happy-customers', 's-ecom': 'small-business-owner', 's-responsive': 'mobile-friendly-website',
    'about-office': 'about-team-office', 'about-meeting': 'strategy-meeting', 'cta-work': 'client-success',
    'why-team': 'client-report-review', 'blog-1': 'contact-banner', 'blog-2': 'planning-whiteboard',
    'blog-3': 'support-team', 'hero-wide': 'hero-team-strategy', 's-software': 'services-banner',
}
def dkey(ref):
    """'{{img:s-seo}}' or 's-seo' -> media name"""
    k = ref.replace('{{img:', '').replace('}}', '')
    return DESIGN.get(k, k)

C = json.load(open(os.path.join(HERE, 'content.json')))
