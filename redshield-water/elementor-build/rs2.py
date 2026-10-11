"""RedShield Water Elementor builder, v2: mirrors the artifact (redshield-water/index.html) component by component.
Container width 1330px. Every value below is taken from the artifact's CSS (1rem = 16px)."""
import json, os, sys, html, re
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from call import call

BASE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "rsw")
SHA = open(os.path.join(BASE, "sha")).read().strip()
IMG = f"https://cdn.jsdelivr.net/gh/developerdgc/new-design@{SHA}/redshield-water/img/"
D = json.load(open(os.path.join(BASE, "data.json")))
PHONE, TEL, EMAIL = "07848 298987", "tel:+447848298987", "Admin@redshield.uk"
P = {"home": 27, "about": 28, "services": 29, "pricing": 30, "areas": 31, "faqs": 32, "tutorials": 33, "contact": 34,
     "leeds": 35, "harrogate": 36, "yorkshire": 37, "ldu": 38, "bds": 39}
HASH2P = {"#leeds-emergency-plumber": "leeds", "#harrogate-emergency-plumber": "harrogate", "#yorkshire-emergency-plumber": "yorkshire",
          "#blocked-drain-service": "bds", "#services": "services", "#leeds-drain-unblocking": "ldu", "#areas": "areas", "#contact": "contact",
          "#pricing": "pricing", "#about": "about", "#tutorials": "tutorials", "#faqs": "faqs", "#home": "home"}
W = 1330
# colours (artifact :root)
INK, PANEL, PANEL2, LINED = "#060b13", "#0b1220", "#111b2c", "#1c2636"
NAVY, RED, REDD, REDS, BLUE, TP = "#0b2340", "#dc2626", "#b91c1c", "#fde8e8", "#2b8fe3", "#00b67a"
MIST, LINE, TEXT, MUTED, MUTEDD, ONDARK = "#f4f6f9", "#d4dbe5", "#0e1726", "#475163", "#aab5c5", "#eef2f7"
SH = "box-shadow: 0 1px 2px rgba(14,23,38,0.06), 0 10px 26px -14px rgba(14,23,38,0.28);"
F = "font-family: Inter;"

# ------------------------------------------------------------------ node model
class N:
    def __init__(s, t, label, cfg=None, style="", cls=None, kids=None):
        s.t, s.label, s.cfg, s.style, s.cls, s.kids = t, label, cfg or {}, style, cls or [], kids or []

def link(href):
    if isinstance(href, str) and href in HASH2P: href = HASH2P[href]
    if isinstance(href, str) and href in P: href = P[href]
    if isinstance(href, int): return {"destination": {"id": href}, "tag": "a"}
    return {"destination": href, "tag": "a", **({"isTargetBlank": True} if href.startswith("http") else {})}

def box(label, kids, style="", tag=None, href=None, t="e-flexbox"):
    cfg = {}
    if tag: cfg["tag"] = tag
    if href is not None: cfg["link"] = link(href)
    return N(t, label, cfg, style, None, kids)
def col(label, kids, gap=0, style="", **kw): return box(label, kids, f"flex-direction: column; gap: {gap}px; padding: 0; " + style, **kw)
def row(label, kids, gap=0, style="", **kw): return box(label, kids, f"flex-direction: row; flex-wrap: wrap; align-items: center; gap: {gap}px; padding: 0; width: auto; " + style, **kw)
def grid(label, kids, cols, gap=22, style="", tablet=None, mobile=1):
    tablet = tablet or min(cols, 2)
    return N("e-grid", label, {}, f"grid-template-columns: repeat({cols}, minmax(0, 1fr)); grid-template-rows: auto; gap: {gap}px; padding: 0; "
             f"@media(--tablet) {{ grid-template-columns: repeat({tablet}, minmax(0, 1fr)); }} @media(--mobile) {{ grid-template-columns: repeat({mobile}, minmax(0, 1fr)); }} " + style, None, kids)
def cgrid(label, kids, cols_css, gap, style="", tablet="minmax(0, 1fr)"):
    return N("e-grid", label, {}, f"grid-template-columns: {cols_css}; grid-template-rows: auto; gap: {gap}px; padding: 0; @media(--tablet) {{ grid-template-columns: {tablet}; }} " + style, None, kids)

def _emcls(text, style):
    # <em> = red word, <b> inside dark text = white bold; implemented as nested rules on the element itself
    if "<em>" in text: style += f" & em {{ color: {RED}; font-style: normal; }}"
    return style
def t(label, text, style=""):  # paragraph
    return N("e-paragraph", label, {"paragraph": text}, F + " " + _emcls(text, style))
def h(label, text, tag="h2", style=""):
    return N("e-heading", label, {"tag": tag, "title": text}, F + " " + _emcls(text, style))
def ico(label, name, color="red", size=18, style=""):
    return N("e-image", label, {"image": {"src": {"url": f"{IMG}icons/{name}-{color}.svg", "alt": ""}, "size": "full"}},
             f"display: block; width: {size}px; height: {size}px; min-width: {size}px; flex-shrink: 0; " + style)
def pic(label, file, alt, style="", href=None):
    url = file if file.startswith("http") else IMG + file
    cfg = {"image": {"src": {"url": url, "alt": alt}, "size": "full"}}
    if href is not None: cfg["link"] = link(href)
    return N("e-image", label, cfg, "display: block; width: 100%; height: auto; " + style)

# ------------------------------------------------------------------ type scale (artifact)
def eyebrow(label, text, style=""): return t(label, text, f"font-size: 12.5px; font-weight: 700; letter-spacing: 0.14em; text-transform: uppercase; color: {RED}; " + style)
def h2(label, text, style="", dark=False):
    return h(label, text, "h2", f"font-size: 37.6px; font-weight: 800; letter-spacing: -0.02em; line-height: 1.15; color: {'#ffffff' if dark else TEXT}; @media(--mobile) {{ font-size: 26.4px; }} " + style)
def lead(label, text, style="", dark=False): return t(label, text, f"font-size: 17px; line-height: 1.6; color: {MUTEDD if dark else MUTED}; " + style)
def body(label, text, size=15.2, style="", color=MUTED): return t(label, text, f"font-size: {size}px; line-height: 1.6; color: {color}; " + style)
def h3(label, text, size=18.4, style="", color=TEXT, tag="h3"): return h(label, text, tag, f"font-size: {size}px; font-weight: 700; line-height: 1.3; color: {color}; " + style)

# ------------------------------------------------------------------ buttons (flexbox links so they can carry an icon)
BTN = {"red": (f"background-color: {RED}; color: #ffffff; border: 2px solid {RED}; &:hover {{ background-color: {REDD}; border-color: {REDD}; }}", "white"),
       "ghost": ("background-color: rgba(255,255,255,0.04); color: #ffffff; border: 2px solid rgba(255,255,255,0.35); &:hover { border-color: #ffffff; }", "white"),
       "line": (f"background-color: transparent; color: {TEXT}; border: 2px solid {TEXT}; &:hover {{ background-color: {TEXT}; color: #ffffff; }}", "text")}
SIZE = {"sm": (14.4, "8.6px 15.8px"), "md": (16, "14.4px 24px"), "lg": (17.3, "17.3px 31px")}
def btn(label, text, href, kind="red", size="md", icon=None, style=""):
    fs, pad = SIZE[size]; st, icol = BTN[kind]
    kids = ([ico(label + " Icon", icon, icol, round(fs))] if icon else []) + [t(label + " Text", text, f"font-size: {fs}px; font-weight: 700; color: inherit; white-space: nowrap;")]
    return row(label, kids, 9, f"justify-content: center; flex-wrap: nowrap; padding: {pad}; border-radius: 8px; width: fit-content; transition: background-color 0.15s, transform 0.15s; {st} &:hover {{ transform: translateY(-1px); }} " + style, href=href)
def callbtn(label, small, size="lg", style=""):
    fs = SIZE[size][0]
    return col(label, [t(label + " Small", small, "font-size: 11.5px; font-weight: 600; letter-spacing: 0.08em; text-transform: uppercase; color: #ffffff; opacity: 0.85; line-height: 1.15;"),
                       row(label + " Number", [ico(label + " Icon", "phone", "white", 19), t(label + " Digits", PHONE, "font-size: 19.2px; font-weight: 700; color: #ffffff; line-height: 1.15;")], 8, "flex-wrap: nowrap;")],
               0, f"align-items: flex-start; padding: 11px {31 if size == 'lg' else 24}px; border-radius: 8px; width: fit-content; background-color: {RED}; border: 2px solid {RED}; &:hover {{ background-color: {REDD}; }} @media(--mobile) {{ align-items: center; }} " + style, href=TEL)
def textlink(label, text, href, color=RED, size=14.7, arrow=True):
    return row(label, [t(label + " Text", text, f"font-size: {size}px; font-weight: 700; color: {color};")] + ([ico(label + " Arrow", "arrow", "red" if color == RED else "salmon", 16)] if arrow else []),
               6, "flex-wrap: nowrap; width: fit-content;", **({"href": href} if href else {}))

# ------------------------------------------------------------------ sections
BG = {"white": "background-color: #ffffff;", "mist": f"background-color: {MIST};", "dark": f"background-color: {INK};",
      "dark2": f"background: linear-gradient(180deg, {INK}, {PANEL});"}
def wrap(label, kids, gap=0, style=""):
    return col(label, kids, gap, f"width: 100%; max-width: {W}px; margin: 0 auto; padding: 0 20px; " + style)
def sec(label, bg, kids, pad=72, gap=0, style="", wstyle=""):
    return box(label, [wrap(label + " Wrap", kids, gap, wstyle)], f"flex-direction: column; padding: {pad}px 0; {BG[bg]} @media(--mobile) {{ padding: {min(pad, 52)}px 0; }} " + style, tag="section")
def head(label, eyebrow_txt, title, lead_txt=None, dark=False, left=False, mb=36, title_style=""):
    k = []
    al = "text-align: left;" if left else "text-align: center;"
    if eyebrow_txt: k.append(eyebrow(label + " Eyebrow", eyebrow_txt, al))
    k.append(h2(label + " Title", title, al + " " + title_style, dark))
    if lead_txt: k.append(lead(label + " Lead", lead_txt, al, dark))
    return col(label + " Head", k, 14, ("align-items: flex-start;" if left else "align-items: center; max-width: 680px; margin: 0 auto;") + f" margin-bottom: {mb}px; width: 100%;")
def split(label, a, b, align="center", ratio=("1fr", "1fr"), gap=48):
    return cgrid(label, [a, b], f"minmax(0, {ratio[0]}) minmax(0, {ratio[1]})", gap, f"align-items: {align};")

# ------------------------------------------------------------------ shared pieces
GLASS_PILL = "background-color: rgba(6,11,19,0.55); border: 1px solid rgba(255,255,255,0.14); border-radius: 999px; backdrop-filter: blur(6px);"
def badge(label, icon, text, icon_color="green", center=False):
    k = ([ico(label + " Icon", icon, icon_color, 15)] if icon else []) + [t(label + " Text", text, "font-size: 13.6px; font-weight: 600; color: #e2e8f0; white-space: nowrap;")]
    return row(label, k, 8, f"flex-wrap: nowrap; padding: 7px 16px 7px 12px; width: fit-content; {GLASS_PILL}" + (" margin: 0 auto;" if center else ""))
def hstat(label, big, small, stars=False, inner=False):
    v = [t(label + " Value", big, f"font-size: {21.6 if inner else 24.8}px; font-weight: 800; letter-spacing: -0.02em; color: #ffffff; line-height: 1.2; @media(--mobile) {{ font-size: 17.6px; }}")]
    if stars: v.append(t(label + " Stars", "★★★★★", f"font-size: 14px; letter-spacing: 1px; color: #fbbf24; @media(--mobile) {{ display: none; }}"))
    return col(label, [row(label + " Top", v, 6, "justify-content: center; flex-wrap: nowrap;"),
                       t(label + " Label", small, "font-size: 12.8px; color: #9fb0c5; text-align: center;")], 2,
               "align-items: center; padding: 14px 12px; background-color: rgba(9,15,27,0.6); border: 1px solid rgba(255,255,255,0.12); border-radius: 14px; backdrop-filter: blur(8px);")
def hstats(n):
    s = [hstat("Stat Arrival", "45<em> min</em>", "Typical arrival", inner=n == 3), hstat("Stat Guarantee", "12<em> mo</em>", "Repair guarantee", inner=n == 3),
         hstat("Stat Rating", "5.0", "Trustpilot rating", True, n == 3), hstat("Stat Hours", "24<em>/</em>7", "Always answered")][:n]
    return grid("Hero Stats", s, n, 12, f"width: 100%; max-width: {860 if n == 4 else 520}px; margin-top: {6 if n == 4 else 2}px;", tablet=n, mobile=2 if n == 4 else 3)
BRUSH = f"& em {{ color: {RED}; font-style: normal; display: inline-block; padding-bottom: 0.08em; background-image: url({IMG}icons/brush-red.svg); background-repeat: no-repeat; background-position: 50% 100%; background-size: 96% 0.3em; }}"

def tp_stars(label, h_px=17):
    w = round(h_px * 5 + 12)
    return N("e-image", label, {"image": {"src": {"url": f"{IMG}icons/tp-stars.svg", "alt": "5 stars on Trustpilot"}, "size": "full"}}, f"display: block; height: {h_px}px; width: {w}px; flex-shrink: 0;")

def review_card(i, title, text):
    return col(f"Review {i}", [row(f"Review {i} Top", [tp_stars(f"Review {i} Stars", 17), t(f"Review {i} Brand", "Trustpilot", f"font-size: 12px; font-weight: 700; color: {TP};")], 0, "justify-content: space-between; flex-wrap: nowrap; width: 100%;"),
                               h3(f"Review {i} Title", title, 15.7, "", TEXT, "h4"),
                               t(f"Review {i} Text", text, "font-size: 14.1px; line-height: 1.6; color: #3d4757; display: -webkit-box; -webkit-line-clamp: 4; -webkit-box-orient: vertical; overflow: hidden;"),
                               t(f"Review {i} By", "— Verified Trustpilot reviewer", f"font-size: 12.5px; color: {MUTED};")], 8,
               "flex: 0 0 310px; width: 310px; background-color: #ffffff; border-radius: 12px; padding: 18px 18px 16px; box-shadow: 0 10px 30px -12px rgba(0,0,0,0.5);")
def reviews_strip():
    headrow = row("Trustpilot Head", [t("TP Excellent", "Excellent", f"font-size: 18.4px; font-weight: 700; color: {TP};"), tp_stars("TP Stars", 22),
                                      t("TP Rated", "Rated by customers on", "font-size: 15.2px; color: #c7d0dc;"),
                                      row("TP Brand", [ico("TP Brand Star", "star", "lgreen", 18), t("TP Brand Text", "Trustpilot", f"font-size: 15.2px; font-weight: 700; color: {TP};")], 4, "flex-wrap: nowrap;")],
                  14, "justify-content: center; padding-top: 6px; width: 100%;")
    cards = [review_card(i + 1, a, b) for i, (a, b) in enumerate(D["REVIEWS"])]
    strip = row("Review Strip", cards, 18, "width: 100%; flex-wrap: nowrap; overflow-x: auto; padding: 22px 20px 34px; align-items: stretch; scrollbar-width: none; "
                "-webkit-mask-image: linear-gradient(90deg, transparent, #000 6%, #000 94%, transparent); mask-image: linear-gradient(90deg, transparent, #000 6%, #000 94%, transparent);")
    return col("Reviews", [headrow, strip], 0, "width: 100%;")
def ticker():
    return box("Services Ticker", [wrap("Ticker Wrap", [t("Ticker Text", "<strong>Our Services:</strong> Emergency Plumbing • Burst Pipes • Leaks &amp; Drips • Blocked Drains • Heating Issues • Installations &amp; Repairs",
                                                       "font-size: 14.7px; color: #9fb0c5; text-align: center; & strong { color: #ffffff; display: block; margin-bottom: 22px; }")])],
               f"flex-direction: column; padding: 90px 0 62px; border-top: 1px solid {LINED};")

def callcard(area="Leeds, Harrogate &amp; all of Yorkshire"):
    li = lambda i, n, txt: row(f"Call Card Point {i}", [ico(f"Call Card Point {i} Icon", n, "red", 16), t(f"Call Card Point {i} Text", txt, "font-size: 14.4px; color: #c3cedc;")], 8, "flex-wrap: nowrap;")
    return col("Call Card", [
        row("Call Card Label", [box("Call Card Icon", [ico("Call Card Phone", "phone", "pink", 19)], "width: 46px; height: 46px; min-width: 46px; padding: 0; border-radius: 50%; background-color: rgba(220,38,38,0.15); align-items: center; justify-content: center;"),
                                col("Call Card Label Text", [t("Call Card Title", "24/7 EMERGENCY CALL OUT", "font-size: 13.6px; font-weight: 700; letter-spacing: 0.06em; color: #ff6b6b;"),
                                                             t("Call Card Note", "We're here when you need us.", f"font-size: 13.1px; color: {MUTEDD};")], 0, "width: auto;")], 12, "flex-wrap: nowrap;"),
        box("Call Card Number Link", [t("Call Card Number", PHONE, "font-size: 38.4px; font-weight: 800; color: #ffffff; letter-spacing: -0.01em; @media(--mobile) { font-size: 28.8px; }")], "padding: 0;", href=TEL),
        box("Call Card Rule", [], f"height: 1px; min-height: 1px; padding: 0; background-color: {LINED}; margin: 4px 0;"),
        col("Call Card Points", [li(1, "clock", "45-minute target arrival"), li(2, "pin", area), li(3, "shield", "12-month repair guarantee")], 8),
        btn("Call Card Button", "Call Now", TEL, "red", "md", "phone", "width: 100%;")], 12,
        f"padding: 26px; background-color: rgba(11,18,32,0.88); border: 1px solid {LINED}; border-radius: 16px; backdrop-filter: blur(8px);")

def phero(photo, crumbs, badge_icon, badge_txt, title, sub, buttons, right=None, solo=False, extra=None, badge_icon_color="green"):
    crumb_nodes = []
    for i, c in enumerate(crumbs):
        if i: crumb_nodes.append(t(f"Crumb Sep {i}", "/", "font-size: 13.1px; color: #8c9bb0;"))
        if isinstance(c, tuple): crumb_nodes.append(box(f"Crumb {c[0]}", [t(f"Crumb {c[0]} Text", c[0], "font-size: 13.1px; color: #8c9bb0; &:hover { color: #ffffff; }")], "padding: 0; width: auto;", href=c[1]))
        else: crumb_nodes.append(t(f"Crumb {c}", c, "font-size: 13.1px; color: #8c9bb0;"))
    al = "text-align: center;" if solo else ""
    kids = [row("Hero Crumbs", crumb_nodes, 8, "justify-content: center;" if solo else "")]
    if badge_txt: kids.append(badge("Hero Badge", badge_icon, badge_txt, badge_icon_color, solo))
    kids.append(h("Hero Title", title, "h1", f"font-size: 54.4px; font-weight: 800; letter-spacing: -0.035em; line-height: 1.1; color: #ffffff; text-shadow: 0 2px 24px rgba(0,0,0,0.35); {al} {BRUSH} @media(--tablet) {{ font-size: 44px; }} @media(--mobile) {{ font-size: 33.6px; }}"))
    if extra: kids.append(extra)
    kids.append(t("Hero Intro", sub, f"font-size: 18.4px; line-height: 1.6; color: #c3cedc; max-width: 640px; {al} & strong {{ color: #ffffff; }}" + (" margin: 0 auto;" if solo else "")))
    if buttons: kids.append(row("Hero Buttons", buttons, 14, "justify-content: center;" if solo else ""))
    kids.append(hstats(3))
    if solo: kids[-1].style += " margin-left: auto; margin-right: auto;"
    left = col("Hero Content", kids, 18, "align-items: center;" if solo else "align-items: flex-start;")
    inner = [left] if solo else [left, right if right is not None else callcard()]
    grid_cols = "minmax(0, 1fr)" if solo else "minmax(0, 1.35fr) minmax(0, 1fr)"
    layout = cgrid("Hero Layout", inner, grid_cols, 40, f"align-items: center; width: 100%; max-width: {W}px; margin: 0 auto; padding: 48px 20px 56px;")
    shade = ("radial-gradient(70% 70% at 50% 45%, rgba(6,11,19,0.4), rgba(6,11,19,0.85) 100%), linear-gradient(0deg, #060b13, rgba(6,11,19,0) 40%)" if solo else
             "linear-gradient(90deg, rgba(6,11,19,0.88) 0%, rgba(6,11,19,0.5) 62%, rgba(6,11,19,0.35)), linear-gradient(0deg, #060b13, rgba(6,11,19,0) 38%)")
    return box("Hero", [layout], f"flex-direction: column; padding: 0; background: {shade}, url({IMG}{photo}) center / cover no-repeat; background-color: {INK};", tag="section")

def stats_band():
    s = [col(f"Stat {i}", [t(f"Stat {i} Value", v, "font-size: 35.2px; font-weight: 800; color: #ffffff; letter-spacing: -0.03em; line-height: 1.1;"),
                           t(f"Stat {i} Label", l, f"font-size: 14.1px; color: {MUTEDD};")], 4, f"padding: 26px 22px; background-color: {PANEL};")
         for i, (v, l) in enumerate([("24<em>/</em>7", "Emergency line, every day of the year"), ("45<em> min</em>", "Target arrival time across Yorkshire"),
                                     ("12<em> mo</em>", "Guarantee on our repair workmanship"), ("15<em>+</em>", "Years of industry experience")], 1)]
    return grid("Stats", s, 4, 1, f"background-color: {LINED}; border: 1px solid {LINED}; border-radius: 14px; overflow: hidden;", tablet=2, mobile=2)

def icbox(label, name, color="red", bg=REDS, size=46, radius=11, isz=21):
    return box(label, [ico(label + " Glyph", name, color, isz)], f"width: {size}px; height: {size}px; min-width: {size}px; padding: 0; border-radius: {radius}px; background-color: {bg}; align-items: center; justify-content: center;")
def card(label, kids, gap=10, style=""):
    return col(label, kids, gap, f"background-color: #ffffff; border: 1px solid {LINE}; border-radius: 14px; padding: 26px; {SH} " + style)
def icon_card(label, icon, title, text, link_txt=None, href=None):
    k = [icbox(label + " Icon", icon), h3(label + " Title", title), body(label + " Text", text)]
    if link_txt: k.append(textlink(label + " Link", link_txt, href, RED, 14.7))
    return card(label, k, 10)

def photo(label, file, alt, cap_icon, cap):
    return box(label, [pic(label + " Image", file, alt, "width: 100%; height: 100%; aspect-ratio: 4 / 3; object-fit: cover;"),
                       row(label + " Caption", [ico(label + " Caption Icon", cap_icon, "red", 16), t(label + " Caption Text", cap, "font-size: 14.1px; color: #ffffff;")], 10,
                           "flex-wrap: nowrap; position: absolute; left: 14px; right: 14px; bottom: 14px; width: auto; padding: 12px 14px; border-radius: 10px; background-color: rgba(6,11,19,0.85);")],
               "position: relative; padding: 0; border-radius: 16px; overflow: hidden;")

def tlist(label, items, gap=12):
    return col(label, [row(f"{label} {i}", [ico(f"{label} {i} Icon", "check", "red", 17, "margin-top: 3px;"), t(f"{label} {i} Text", it, f"font-size: 15.7px; line-height: 1.5; color: {TEXT};")], 10, "flex-wrap: nowrap; align-items: flex-start;")
                       for i, it in enumerate(items, 1)], gap)

def quote(label, text):
    return col(label, [tp_stars(label + " Stars", 17), body(label + " Text", text, 15.7, "", "#334155"),
                       row(label + " Footer", [t(label + " By", "Verified Trustpilot reviewer ·", f"font-size: 13.1px; color: {MUTED};"), t(label + " Brand", "Trustpilot", f"font-size: 13.1px; font-weight: 700; color: {TP};")], 6)],
               12, f"background-color: #ffffff; border: 1px solid {LINE}; border-radius: 14px; padding: 24px; {SH}")

def how_strip():
    steps = [("1", "Call us, any time", "A real plumber answers 24/7 and tells you how to stop the water."),
             ("2", "We come to you", "For emergencies we aim to be at your door within 45 minutes."),
             ("3", "Price first, then the fix", "You get the price before we start. Repairs are guaranteed for 12 months.")]
    cells = [row(f"Step {n}", [t(f"Step {n} Number", n, f"font-size: 16px; font-weight: 700; color: #ffffff; background-color: {TEXT}; width: 40px; height: 40px; min-width: 40px; line-height: 40px; text-align: center; border-radius: 50%;"),
                               col(f"Step {n} Text", [h3(f"Step {n} Title", a, 16.3), body(f"Step {n} Body", b, 14.7)], 4, "flex: 1;")],
                 14, "width: 100%; flex-wrap: nowrap; align-items: flex-start; padding: 22px 24px;" + ("" if n == "1" else f" border-left: 1px solid {LINE}; @media(--tablet) {{ border-left: 0; border-top: 1px solid {LINE}; }}"))
             for n, a, b in steps]
    return grid("How Strip", cells, 3, 0, f"background-color: #ffffff; border: 1px solid {LINE}; border-radius: 14px; overflow: hidden; {SH}", tablet=1)

def svc_card(i, imgf, title, desc, icon, hot, href):
    target = href if href else TEL
    panel = col(f"Service {i} Body", [
        box(f"Service {i} Icon", [ico(f"Service {i} Glyph", icon, "white", 19)], f"position: absolute; top: -22px; right: 16px; width: 46px; height: 46px; padding: 0; border-radius: 50%; background-color: {RED}; border: 3px solid #080e1a; align-items: center; justify-content: center;"),
        h3(f"Service {i} Title", title, 19.2, "padding-right: 44px;", "#ffffff"),
        t(f"Service {i} Text", desc, "font-size: 14.9px; line-height: 1.55; color: #d3dbe6;"),
        row(f"Service {i} More", [t(f"Service {i} More Text", "Learn more" if href else "Call about this", "font-size: 14.4px; font-weight: 700; color: #ff8080;"), ico(f"Service {i} Arrow", "arrow", "salmon", 16)], 6, "flex-wrap: nowrap; margin-top: 4px;")],
        6, "position: relative; padding: 18px 18px 16px; background-color: rgba(8,14,26,0.86); border: 1px solid rgba(255,255,255,0.08); border-radius: 12px; backdrop-filter: blur(8px); border-bottom: 3px solid transparent;")
    kids = ([row(f"Service {i} Tag", [ico(f"Service {i} Tag Icon", "clock", "white", 13), t(f"Service {i} Tag Text", "24/7", "font-size: 11.5px; font-weight: 800; letter-spacing: 0.06em; color: #ffffff;")], 5,
                 f"flex-wrap: nowrap; position: absolute; top: 14px; left: 14px; width: auto; padding: 5px 9px; border-radius: 6px; background-color: {RED};")] if hot else []) + [panel]
    return col(f"Service {i}", kids, 0, f"position: relative; justify-content: flex-end; min-height: 330px; padding: 12px; border-radius: 16px; overflow: hidden; color: #ffffff; "
               f"background: linear-gradient(180deg, rgba(6,11,19,0) 35%, rgba(6,11,19,0.55) 100%), url({IMG}svc-{imgf}.jpg) center / cover no-repeat; background-color: {INK}; {SH} "
               "transition: transform 0.25s; &:hover { transform: translateY(-4px); }", href=target)
def svc_grid():
    cards = [svc_card(i + 1, s[0], s[1], s[2], s[3], len(s) > 4 and s[4], s[5] if len(s) > 5 else None) for i, s in enumerate(D["SERVICES"])]
    also = row("Also Fix", [t("Also Label", "We also fix:", f"font-size: 14.7px; font-weight: 700; color: {TEXT}; margin-right: 4px;")] +
               [t(f"Also {x}", x, f"font-size: 14.7px; font-weight: 600; color: {TEXT}; padding: 6px 12px; border-radius: 999px; background-color: {MIST}; border: 1px solid {LINE};")
                for x in ["Dripping taps", "Toilets &amp; cisterns", "Radiators", "Hot water cylinders", "Outside taps", "Washing machine leaks"]], 10, "justify-content: center; margin-top: 30px;")
    return [grid("Service Cards", cards, 3, 22), also]

# --- diagnose (tabs) + callback form
def diagnose():
    issues = list(D["ISSUES"].items())
    tabs = [N("e-tab", "Issue Tab Not Sure", {}, "display: none;", None, [t("Issue Tab Not Sure Text", "Not sure")])]
    contents = [N("e-tab-content", "Issue Advice Not Sure", {}, "padding: 0;", None, [col("Advice Not Sure Box", [
        row("Advice Not Sure Head", [ico("Advice Not Sure Icon", "alert", "text", 17), h3("Advice Not Sure Title", "Not sure what to do?", 16, "", TEXT, "h4")], 8, "flex-wrap: nowrap;"),
        t("Advice Not Sure Note", "Turn off your stop tap if possible and call us now. We'll put you in immediate contact with a plumber who will talk you through the best options.", "font-size: 13.8px; line-height: 1.6; color: #7c5c3c;")],
        10, "padding: 18px 20px; border-radius: 12px; background-color: #fff7ed; border: 1px solid #fed7aa;")])]
    for k, (icon, steps) in issues:
        tabs.append(N("e-tab", f"Issue Tab {k}", {}, f"width: auto; min-width: 0; padding: 50px 8px 12px; border: 1.5px solid {LINE}; border-radius: 12px; background-color: #ffffff; color: {TEXT}; text-align: center; {SH} "
                      f"background-image: url({IMG}icons/{icon}-text.svg); background-repeat: no-repeat; background-position: 50% 16px; background-size: 26px 26px; cursor: pointer; transition: border-color 0.15s, transform 0.15s; "
                      f"&:hover {{ border-color: {RED}; transform: translateY(-2px); }} &[aria-selected=\"true\"] {{ border-color: {RED}; background-color: {REDS}; color: {REDD}; }}", None,
                      [t(f"Issue Tab {k} Text", k, "font-size: 13.1px; font-weight: 600; color: inherit; text-align: center; line-height: 1.3;")]))
        contents.append(N("e-tab-content", f"Issue Advice {k}", {}, "padding: 0;", None, [col(f"Advice {k} Box", [
            row(f"Advice {k} Head", [ico(f"Advice {k} Icon", "alert", "text", 17), h3(f"Advice {k} Title", f"{k}: do this now", 16, "", TEXT, "h4")], 8, "flex-wrap: nowrap;"),
            t(f"Advice {k} Steps", "<ol>" + "".join(f"<li>{s}</li>" for s in steps) + "</ol>", "font-size: 14.9px; line-height: 1.7; color: #4a3b2b; & ol { margin: 0; padding-left: 1.2em; }"),
            btn(f"Advice {k} Call", f"Call {PHONE}", TEL, "red", "sm", "phone")],
            10, "padding: 18px 20px; border-radius: 12px; background-color: #fff7ed; border: 1px solid #fed7aa;")]))
    tabs_el = N("e-tabs", "Issue Tabs", {"default-active-tab": 0}, "gap: 16px; margin-top: 22px;", None, [
        N("e-tabs-menu", "Issue Tab Menu", {}, "display: grid; grid-template-columns: repeat(auto-fill, minmax(112px, 1fr)); gap: 10px; justify-content: stretch;", None, tabs),
        N("e-tabs-content-area", "Issue Advice Area", {}, "", None, contents)])
    return col("Diagnose", [eyebrow("Diagnose Eyebrow", "Quick diagnosis"),
                            h2("Diagnose Title", "What Plumbing Issue Do You Have?", "font-size: 35.2px; margin-top: 8px; @media(--mobile) { font-size: 25.6px; }"),
                            lead("Diagnose Lead", "Tap your problem for what to do right now, then call your local plumbing team for fast, same-day repair.", "margin-top: 10px;"),
                            tabs_el], 0)

INPUT = f"width: 100%; padding: 12px 14px; border-radius: 8px; border: 1.5px solid {LINE}; background-color: #ffffff; color: {TEXT}; font-family: Inter; font-size: 15.2px; &:focus {{ border-color: {RED}; }}"
def form_field(form, i, label_txt, kind, ph, req=True, area=False, dark=False, options=None):
    lab = N("e-form-label", f"{form} Label {i}", {"text": label_txt}, f"font-family: Inter; font-size: 13.1px; font-weight: 600; color: {'#ffffff' if dark else TEXT}; opacity: 0.85;")
    st = INPUT + (" border-color: transparent;" if dark else "")
    if options: inp = N("e-form-select", f"{form} Field {i}", {"options": options, "required": req}, st)
    elif area: inp = N("e-form-textarea", f"{form} Field {i}", {"placeholder": ph, "rows": 5, "required": req}, st + " min-height: 120px;")
    else: inp = N("e-form-input", f"{form} Field {i}", {"placeholder": ph, "type": kind, "required": req}, st)
    return col(f"{form} Group {i}", [lab, inp], 6)
def form_tail(form, ok_dark=False):
    return [N("e-form-success-message", f"{form} Success", kids=[t(f"{form} Success Text", f"Thanks, your message has been sent. For an emergency, call {PHONE}.", f"font-size: 14.4px; color: {'#ffffff' if ok_dark else '#065f46'};")]),
            N("e-form-error-message", f"{form} Error", kids=[t(f"{form} Error Text", f"Sorry, something went wrong. Please call {PHONE}.", "font-size: 14.4px; color: #b91c1c;")])]
FORMCFG = lambda name: {"form-name": name, "actions-after-submit": ["email"], "email": {"to": [EMAIL], "subject": f"New RedShield Water enquiry: {name}"}}
SUBMIT = f"font-family: Inter; font-weight: 700; color: #ffffff; background-color: {RED}; border-radius: 8px; width: 100%; &:hover {{ background-color: {REDD}; }}"
def callback(title="Get Emergency Help Now", label="Callback Form"):
    opts = [{"key": "Select an issue", "value": ""}] + [{"key": k, "value": k} for k in D["ISSUES"]] + [{"key": "Other", "value": "Other"}]
    kids = [h(f"{label} Title", title.upper(), "h3", "font-size: 22.4px; font-weight: 800; letter-spacing: -0.01em; color: #ffffff;"),
            t(f"{label} Sub", f"Fast response across Leeds &amp; surrounding areas. For the fastest response call {PHONE}.", "font-size: 14.4px; line-height: 1.5; color: #a9bbd2; margin-top: -6px;"),
            form_field(label, 1, "Your name *", "text", "Your Name", dark=True), form_field(label, 2, "Phone number *", "tel", "Phone Number", dark=True),
            form_field(label, 3, "Postcode *", "text", "Postcode", dark=True), form_field(label, 4, "What's the problem? *", "", "", dark=True, options=opts),
            N("e-form-submit-button", f"{label} Submit", {"text": "Call Me Back Now"}, SUBMIT + " font-size: 17.3px; padding: 17px 31px;"),
            row(f"{label} Fine", [ico(f"{label} Lock", "lock", "white", 13), t(f"{label} Fine Text", "Your details are kept private and secure", "font-size: 12.8px; color: #ffffff;")], 6, "justify-content: center; opacity: 0.75;")] + form_tail(label, True)
    return N("e-form", label, FORMCFG("callback"), f"display: flex; flex-direction: column; gap: 12px; padding: 28px; border-radius: 16px; background-color: {NAVY}; box-shadow: 0 30px 60px -20px rgba(11,35,64,0.6);", None, kids)
def msgform(label="Message Form", postcode=True, placeholders=True):
    ph = (lambda s: s) if placeholders else (lambda s: "")
    r1 = cgrid(f"{label} Row 1", [form_field(label, 1, "Your Name *", "text", ph("Jane Smith")), form_field(label, 2, "Email Address *", "email", ph("jane@email.com"))], "repeat(2, minmax(0, 1fr))", 12, "", "minmax(0, 1fr)")
    r2 = (cgrid(f"{label} Row 2", [form_field(label, 3, "Phone Number", "tel", ph("07..."), False), form_field(label, 4, "Postcode", "text", ph("LS1 4AP"), False)], "repeat(2, minmax(0, 1fr))", 12, "", "minmax(0, 1fr)")
          if postcode else form_field(label, 3, "Phone Number", "tel", "", False))
    kids = [h(f"{label} Title", "Send Us a Message", "h3", f"font-size: 21.6px; font-weight: 700; color: {TEXT};"),
            t(f"{label} Intro", "Describe your issue and we'll get back to you as soon as possible.", f"font-size: 15.2px; color: {MUTED}; margin-top: -6px;"),
            r1, r2, form_field(label, 5, "How Can We Help? *", "text", ph("e.g. Water dripping through the kitchen ceiling under the bathroom"), True, True),
            N("e-form-submit-button", f"{label} Submit", {"text": "Send Message"}, SUBMIT + " font-size: 16px; padding: 14px 24px;")] + form_tail(label)
    return N("e-form", label, FORMCFG("message"), f"display: flex; flex-direction: column; gap: 14px; padding: 28px; border-radius: 16px; background-color: #ffffff; border: 1px solid {LINE}; border-top: 4px solid {RED}; {SH}", None, kids)
def diag_section(bg="mist", title="Get Emergency Help Now"):
    return sec("Plumbing Issues", bg, [cgrid("Diag Layout", [diagnose(), callback(title)], "minmax(0, 1.5fr) minmax(0, 1fr)", 36, "align-items: start;")])

# --- areas / jobs
def pinlist(label, items):
    return grid(label, [row(f"{label} {x}", [ico(f"{label} {x} Icon", "pin", "red", 16), t(f"{label} {x} Text", x, f"font-size: 14.9px; color: {TEXT};")], 8, "flex-wrap: nowrap;") for x in items], 3, 10, "margin-top: 20px; column-gap: 18px;", tablet=3, mobile=2)
def jobs(n, dark=False):
    out = []
    for i, (w, title, d, icon) in enumerate(D["JOBS"][:n], 1):
        out.append(cgrid(f"Job {i}", [icbox(f"Job {i} Icon", icon, "pink" if dark else "navy", PANEL2 if dark else MIST, 40, 10, 19),
                                      col(f"Job {i} Text", [h3(f"Job {i} Title", title, 15.7, "", "#ffffff" if dark else TEXT, "h4"), body(f"Job {i} Body", d, 14.1, "", MUTEDD if dark else MUTED)], 2),
                                      t(f"Job {i} When", w, f"font-size: 11.5px; font-weight: 700; color: {RED}; border: 1px solid rgba(220,38,38,0.4); border-radius: 5px; padding: 3px 8px; white-space: nowrap;")],
                         "auto minmax(0, 1fr) auto", 14, f"align-items: start; padding: 16px; border-radius: 12px; border: 1px solid {LINED if dark else LINE}; background-color: {PANEL if dark else '#ffffff'};" + ("" if dark else " " + SH),
                         "auto minmax(0, 1fr) auto"))
    return out
def chips(label, key, dark=False):
    st = (f"background-color: {PANEL}; border: 1px solid {LINED}; color: #c9d3e0;" if dark else f"background-color: #ffffff; border: 1px solid {LINE}; color: {TEXT};")
    return row(label, [t(f"{label} {i}", c, f"font-size: 13.8px; font-weight: 500; padding: 7px 13px; border-radius: 999px; {st}") for i, c in enumerate(D["CHIPS"][key].split("|"), 1)], 8)
def area_cards():
    return grid("Area Cards", [col(f"Area {a}", [icbox(f"Area {a} Icon", "pin", "red", REDS, 40, 10, 19), h3(f"Area {a} Title", a, 17.6), body(f"Area {a} Text", d, 14.1),
                                                  textlink(f"Area {a} Go", "View area", None, RED, 13.6)], 8,
                                   f"background-color: #ffffff; border: 1px solid {LINE}; border-radius: 14px; padding: 22px; {SH} transition: border-color 0.15s, transform 0.15s; &:hover {{ border-color: {RED}; transform: translateY(-2px); }}", href=hh)
                               for a, d, hh in D["AREAS"]], 4, 22)

# --- pricing
def plans():
    def plan(n, flag, flagbg, flagfg, border, icon, icol, title, price, pick, ticks, btext, bkind, bhref, hot=False):
        tick_nodes = col(f"Plan {n} Ticks", [row(f"Plan {n} Tick {i}", [ico(f"Plan {n} Tick {i} Icon", "check", "pink" if hot else "lgreen", 16, "margin-top: 3px;"), t(f"Plan {n} Tick {i} Text", x, f"font-size: 14.7px; color: {ONDARK};")], 9, "flex-wrap: nowrap; align-items: flex-start;")
                                             for i, x in enumerate(ticks, 1)], 9)
        return col(f"Plan {n}", [
            t(f"Plan {n} Flag", flag, f"position: absolute; top: -13px; left: 50%; transform: translateX(-50%); font-size: 11.2px; font-weight: 800; letter-spacing: 0.1em; padding: 5px 12px; border-radius: 5px; white-space: nowrap; background-color: {flagbg}; color: {flagfg};"),
            icbox(f"Plan {n} Icon", icon, icol, "rgba(255,255,255,0.06)", 46, 11, 21),
            h3(f"Plan {n} Title", title, 20, "", "#ffffff"),
            row(f"Plan {n} Price", [t(f"Plan {n} Amount", price, f"font-size: 48px; font-weight: 800; letter-spacing: -0.03em; line-height: 1; color: {RED if hot else '#ffffff'};"), t(f"Plan {n} Unit", "call-out", f"font-size: 14.4px; color: {MUTEDD};")], 8, "align-items: baseline; flex-wrap: nowrap;"),
            t(f"Plan {n} Pick", pick, "font-size: 14.7px; font-weight: 600; color: #ffffff; background-color: rgba(255,255,255,0.05); border-radius: 8px; padding: 10px 12px;"),
            tick_nodes, btn(f"Plan {n} Button", btext, bhref, bkind, "md", None, "width: 100%; margin-top: auto;")], 14,
            f"position: relative; padding: 34px 26px 26px; background-color: {PANEL}; border: 2px solid {border}; border-radius: 16px; overflow: visible;")
    cards = [plan(1, "FASTEST", RED, "#ffffff", RED, "bolt", "pink", "Immediate Response", "£50", "Choose this if water is leaking or flooding right now.", ["Engineer sent straight away", "Usually with you within 45 minutes", "You go to the front of the queue"], "Get Help Now", "red", TEL, True),
             plan(2, "BEST PRICE", "#16a34a", "#ffffff", "#2a4a3a", "sun", "lgreen", "Same Day Service", "£25", "Choose this if there's a problem but it isn't getting worse.", ["We visit later today", "Fixed the same day", "Emergencies are seen first"], "Book Today", "ghost", TEL),
             plan(3, "FLEXIBLE BOOKING", "#eab308", "#1a1400", "#4a4426", "cal", "gold", "Standard Booking", "£0", "Choose this if the job can wait a day or more.", ["No call-out fee", "Pick a day that suits you", "Good for planned work"], "Schedule Visit", "ghost", "contact")]
    note = t("Plans Note", "The call-out fee is taken off your final bill if you go ahead. You always get the price for the repair before we start. Fully insured, 12-month guarantee.", "font-size: 14.4px; color: #b7c2d1; text-align: center; max-width: 640px; margin: 30px auto 0;")
    return [grid("Plan Cards", cards, 3, 24, "align-items: stretch; padding-top: 14px;", tablet=1), note]
def tiers():
    data = [("STANDARD", "From £80", "Same-day visit", "Call-out fee deducted from final bill.", False), ("PRIORITY", "From £120", "Within 2 hours", "For escalating blockages and overflows.", False),
            ("EMERGENCY", "From £180", "45-min response", "Sewage, flooding, multi-fixture failure.", True)]
    return grid("Tiers", [col(f"Tier {i}", [t(f"Tier {i} Name", a, f"font-size: 11.8px; font-weight: 800; letter-spacing: 0.12em; color: {MUTED};"), t(f"Tier {i} Price", b, f"font-size: 32px; font-weight: 800; letter-spacing: -0.02em; color: {TEXT};"),
                                            t(f"Tier {i} Speed", c, f"font-size: 15.2px; font-weight: 700; color: {RED};"), body(f"Tier {i} Note", d, 14.4)], 6,
                              f"background-color: #ffffff; border: 1px solid {RED if hot else LINE}; border-radius: 14px; padding: 24px; " + ("box-shadow: 0 18px 40px -20px rgba(220,38,38,0.5);" if hot else SH))
                          for i, (a, b, c, d, hot) in enumerate(data, 1)], 3, 18, tablet=1)

# --- map
def map_box(centre="leeds"):
    name = "Harrogate" if centre == "harrogate" else "Leeds"
    return box("Coverage Map", [pic("Coverage Map Image", f"map-{centre}.svg", f"Map of RedShield Water's service area: rings at 10, 20 and 30 miles around {name}", "width: 100%; height: auto; aspect-ratio: 1 / 1;"),
                                row("Map Card", [row("Map Card Label", [ico("Map Card Dot", "dot", "white", 9) if False else N("e-image", "Map Card Dot", {"image": {"src": {"url": f"{IMG}icons/dot-white.svg", "alt": ""}, "size": "full"}}, "display: block; width: 9px; height: 9px;"),
                                                                        t("Map Card Text", f"45-minute response from {name}", "font-size: 14.7px; font-weight: 700; color: #ffffff;")], 9, "flex-wrap: nowrap; width: auto;"),
                                                 box("Map Card Link", [t("Map Card Link Text", "Open in Google Maps →", "font-size: 14.1px; font-weight: 700; color: #ffffff; text-decoration: underline; text-underline-offset: 3px;")], "padding: 0; width: auto;",
                                                     href=f"https://www.google.com/maps/search/?api=1&query={name}+Yorkshire")],
                                    8, f"justify-content: space-between; position: absolute; left: 14px; right: 14px; bottom: 14px; width: auto; padding: 12px 16px; border-radius: 12px; background-color: {RED}; box-shadow: 0 14px 30px rgba(0,0,0,0.35);")],
               f"position: relative; padding: 0; border-radius: 18px; overflow: hidden; background-color: #0c1524; border: 1px solid {LINED}; box-shadow: 0 28px 56px -24px rgba(6,11,19,0.6);")
PILLS = [("Leeds", "leeds", 1), ("Harrogate", "harrogate"), ("York", "yorkshire"), ("Wakefield", "yorkshire"), ("Huddersfield", "yorkshire"), ("Halifax", "yorkshire"), ("Doncaster", "yorkshire"),
         ("Bradford",), ("Dewsbury",), ("Pontefract",), ("Otley",), ("Wetherby",), ("Selby",), ("Knaresborough",)]
def areamap():
    pills = []
    for pl in PILLS:
        n, hh, home = (list(pl) + [None, None])[:3]
        st = (f"background-color: {RED}; border: 1.5px solid {RED};" if home else f"background-color: #ffffff; border: 1.5px solid {LINE}; {SH} &:hover {{ border-color: {RED}; transform: translateY(-2px); }}")
        pills.append(row(f"Pill {n}", [ico(f"Pill {n} Icon", "pin", "white" if home else "red", 15), t(f"Pill {n} Text", n, f"font-size: 14.7px; font-weight: 600; color: {'#ffffff' if home else TEXT};")], 7,
                         f"flex-wrap: nowrap; width: auto; min-height: 40px; padding: 0 14px; border-radius: 999px; transition: border-color 0.15s, transform 0.15s; {st}", href=hh))
    copy = col("Area Copy", [col("Area Head", [eyebrow("Area Eyebrow", "Service area"), h2("Area Title", "Areas We <em>Cover</em>")], 12),
                             row("Area Location", [ico("Area Location Icon", "pin", "white", 16), t("Area Location Text", 'Location: <em>All of Yorkshire</em>', "font-size: 14.7px; font-weight: 600; color: #ffffff; & em { color: #ff7a7a; }")], 9,
                                 f"flex-wrap: nowrap; width: fit-content; padding: 9px 15px; border-radius: 10px; background-color: {INK};"),
                             lead("Area Text", "Based in Leeds, our engineers cover West Yorkshire and beyond. Homes inside the first ring usually see us within 45 minutes."),
                             row("Area Pills", pills, 9),
                             row("Area Foot", [t("Area Foot Text", "Not listed? Call us anyway, we may still be able to help.", f"font-size: 16px; font-weight: 500; color: {MUTED}; max-width: 300px;"), btn("Area Call", f"Call {PHONE}", TEL, "red", "md", "phone")], 22,
                                 f"padding-top: 20px; border-top: 1px solid {LINE}; width: 100%;")], 20, "align-items: flex-start;")
    return cgrid("Area Layout", [copy, map_box()], "minmax(0, 1fr) minmax(0, 540px)", 52, "align-items: center;")

# --- misc blocks
def slim():
    return row("Tutorial Banner", [col("Tutorial Banner Text", [t("Tutorial Banner Title", "Waiting for the plumber?", f"font-size: 16.8px; font-weight: 700; color: {TEXT};"),
                                                                body("Tutorial Banner Lead", "Watch our free short videos on turning off your water and limiting the damage.", 16)], 2, "flex: 1;"),
                                   btn("Tutorial Banner Button", "Watch free videos", "tutorials", "line", "sm")], 24,
               f"width: 100%; justify-content: space-between; padding: 20px 24px; border-radius: 14px; background-color: #ffffff; border: 1px solid {LINE}; {SH}")
def cta(a, b, c, sub):
    trust = row("CTA Trust", [row(f"CTA Trust {i}", [ico(f"CTA Trust {i} Icon", n, "red", 15), t(f"CTA Trust {i} Text", x, "font-size: 14.4px; color: #a6b2c3;")], 8, "flex-wrap: nowrap;")
                              for i, (n, x) in enumerate([("clock", "45 Min Response"), ("shield", "Work Guaranteed"), ("phone", "Always Answered")], 1)], 28, "justify-content: center;")
    k = [row("CTA Badge", [N("e-image", "CTA Badge Dot", {"image": {"src": {"url": f"{IMG}icons/dot-green.svg", "alt": ""}, "size": "full"}}, "display: block; width: 8px; height: 8px;"),
                           t("CTA Badge Text", "Available Right Now", "font-size: 13.6px; font-weight: 600; color: #f1f5f9;")], 8,
             "flex-wrap: nowrap; width: fit-content; margin: 0 auto; padding: 6px 14px; border-radius: 999px; border: 1px solid rgba(255,255,255,0.18); background-color: rgba(255,255,255,0.06);"),
         h("CTA Title", f"{a}<em>{b}</em>{c}", "h2", "font-size: 41.6px; font-weight: 800; letter-spacing: -0.02em; line-height: 1.15; color: #ffffff; text-align: center; @media(--mobile) { font-size: 27.2px; }"),
         t("CTA Text", sub, "font-size: 17.9px; line-height: 1.6; color: #a9b6c8; text-align: center; max-width: 620px; margin: 0 auto;"),
         btn("CTA Button", f"Call {PHONE}", TEL, "red", "lg", "phone", "margin: 0 auto;"), trust]
    return box("Call To Action", [wrap("CTA Wrap", k, 16, "align-items: center; padding-top: 64px; padding-bottom: 64px;")],
               f"flex-direction: column; padding: 0; background: radial-gradient(50% 70% at 50% 50%, rgba(220,38,38,0.1), rgba(6,11,19,0) 70%), {INK};", tag="section")
def videos(n=4, start=0, cols=4):
    cards = [box(f"Video {k+1}", [col(f"Video {k+1} Inner", [
        box(f"Video {k+1} Thumb", [pic(f"Video {k+1} Image", v[2].replace("img/", ""), v[0], "width: 100%; height: 100%; aspect-ratio: 16 / 9; object-fit: cover;"),
                                   box(f"Video {k+1} Play", [ico(f"Video {k+1} Play Icon", "play", "white", 22, "margin-left: 3px;")],
                                       f"position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); width: 54px; height: 54px; padding: 0; border-radius: 50%; background-color: {RED}; align-items: center; justify-content: center;")],
            f"position: relative; padding: 0; border-radius: 12px; overflow: hidden; background-color: {NAVY};"),
        t(f"Video {k+1} Number", f"TUTORIAL {k+1}", f"font-size: 12px; font-weight: 800; letter-spacing: 0.1em; color: {RED};"),
        h3(f"Video {k+1} Title", v[0], 16.8), body(f"Video {k+1} Text", v[1], 14.1)], 12)], "padding: 0;", href=v[3])
             for k, v in list(enumerate(D["VIDEOS"]))[start:start + n]]
    return grid("Video Cards", cards, cols, 22)
ACC_HEAD = (f"position: relative; padding: 18px 54px 18px 20px; cursor: pointer; list-style: none; &::-webkit-details-marker {{ display: none; }} "
            f"&::after {{ content: '+'; position: absolute; right: 18px; top: 50%; transform: translateY(-50%); width: 26px; height: 26px; line-height: 26px; text-align: center; border-radius: 50%; background-color: {REDS}; color: {RED}; font-family: Inter; font-weight: 700; font-size: 16px; }}")
def faq_items(items, label):
    its = []
    for i, (q, a) in enumerate(items, 1):
        its.append(N("e-accordion-item", f"{label} {i}", {}, f"background-color: #ffffff; border: 1px solid {LINE}; border-radius: 12px; overflow: hidden; {SH} &[open] {{ border-color: rgba(220,38,38,0.45); }} &[open] > summary::after {{ content: '–'; }}", None, [
            N("e-accordion-item-header", f"{label} {i} Header", {}, ACC_HEAD, None, [
                N("e-accordion-item-title", f"{label} {i} Title", {}, "", None, [t(f"{label} {i} Q", q, f"font-size: 16px; font-weight: 600; color: {TEXT};")])]),
            N("e-accordion-item-content", f"{label} {i} Body", {}, "padding: 0 20px 18px;", None, [t(f"{label} {i} A", a, f"font-size: 15.2px; line-height: 1.6; color: {MUTED}; max-width: 75ch;")])]))
    return N("e-accordion", label, {"default_state": "all_collapsed", "max_expanded": "one", "show_icon": True, "faq_schema": True}, "gap: 10px; padding: 0;", None, its)
def faq(cat, label=None):
    items = [(q, a) for c, q, a in D["FAQ"] if cat == "all" or cat in c.split()]
    return faq_items(items, label or f"FAQ {cat.title()}")
def problems(town=""):
    return grid("Problem Cards", [icon_card(f"Problem {i}", ic_, tt + (f" {town}" if town and "Stop Tap" not in tt else ""), d, "Call now", TEL) for i, (ic_, tt, d) in enumerate(D["PROBLEMS"], 1)], 4, 22)
def contact_tiles(area="Yorkshire wide coverage"):
    def tile(i, icon, small, big, extra=None, href=None):
        k = [t(f"Contact {i} Label", small, f"font-size: 13.1px; color: {MUTED};"), t(f"Contact {i} Value", big, f"font-size: 16.8px; font-weight: 700; color: {TEXT}; word-break: break-word;")]
        if extra: k.append(t(f"Contact {i} Extra", extra, f"font-size: 13.6px; color: {MUTED};"))
        return row(f"Contact {i}", [icbox(f"Contact {i} Icon", icon, "red", REDS, 44, 10, 19), col(f"Contact {i} Text", k, 2, "flex: 1;")], 14,
                   f"flex-wrap: nowrap; align-items: flex-start; padding: 18px; border-radius: 12px; border: 1px solid {LINE}; background-color: #ffffff; {SH}", href=href)
    return col("Contact Tiles", [tile(1, "phone", "Call Us 24/7", "07848 298 987", href=TEL), tile(2, "mail", "Email Us", EMAIL, href=f"mailto:{EMAIL}"),
                                 tile(3, "pin", "Service Area", area), tile(4, "clock", "Opening Hours", "24 hours, 7 days a week", "Emergency services always available")], 14)
def drain_cards():
    out = []
    data = [("Drain Unblocking", "Fast and effective solutions for blocked drains. We clear blockages in minutes, not hours.", "drain"),
            ("Drain Repairs", "We repair all types of drainage issues. From cracked pipes to root intrusion, we fix it properly.", "pipe"),
            ("Drain Installations", "High quality installations built to last. New pipework, connections and complete system upgrades.", None, "drain-install"),
            ("Drain Maintenance", "Keep your drains running smoothly all year round. Regular maintenance prevents costly emergencies.", None, "drain-maint")]
    for i, (tt, d, ba, *im) in enumerate(data, 1):
        media = ba_box(f"Drain {i} Compare", ba) if ba else box(f"Drain {i} Photo Box", [pic(f"Drain {i} Photo", im[0] + ".jpg", tt, "width: 100%; height: 100%; aspect-ratio: 4 / 3; object-fit: cover;")], "padding: 0; overflow: hidden;")
        out.append(col(f"Drain {i}", [media, col(f"Drain {i} Body", [h3(f"Drain {i} Title", tt, 17.3), body(f"Drain {i} Text", d, 14.4),
                                                                      box(f"Drain {i} Link", [t(f"Drain {i} Link Text", "Learn More →", f"font-size: 14.4px; font-weight: 700; color: {RED};")], "padding: 0; width: fit-content;", href="contact")], 8, "padding: 20px;")],
                       0, f"background-color: #ffffff; border: 1px solid {LINE}; border-radius: 14px; overflow: hidden; {SH}"))
    return grid("Drain Cards", out, 4, 22)
def ba_box(label, key, radius=0):
    lab = lambda txt, side, bg: t(f"{label} {txt}", txt, f"position: absolute; bottom: 10px; {side}: 10px; font-size: 11.5px; font-weight: 700; padding: 3px 8px; border-radius: 4px; color: #ffffff; background-color: {bg};")
    return box(label, [pic(f"{label} Before", f"{key}-before.jpg", "Before", "position: absolute; top: 0; left: 0; width: 100%; height: 100%; object-fit: cover;"),
                       pic(f"{label} After", f"{key}-after.jpg", "After", "position: absolute; top: 0; left: 0; width: 100%; height: 100%; object-fit: cover; clip-path: inset(0 0 0 50%);"),
                       box(f"{label} Bar", [], "position: absolute; top: 0; bottom: 0; left: 50%; width: 3px; min-width: 3px; padding: 0; background-color: #ffffff; transform: translateX(-50%);"),
                       box(f"{label} Knob", [], "position: absolute; top: 50%; left: 50%; width: 30px; height: 30px; padding: 0; border-radius: 50%; background-color: #ffffff; transform: translate(-50%, -50%); box-shadow: 0 2px 10px rgba(0,0,0,0.4);"),
                       lab("Before", "left", "rgba(0,0,0,0.7)"), lab("After", "right", RED)],
               f"position: relative; padding: 0; aspect-ratio: 4 / 3; overflow: hidden; background-color: #222222; border-radius: {radius}px;")
def guide(label, title, steps):
    return col(label, [eyebrow(label + " Eyebrow", "Quick guide"), h3(label + " Title", title, 22.4),
                       col(label + " Steps", [cgrid(f"{label} Step {i}", [t(f"{label} Step {i} No", str(i), f"font-size: 13.6px; font-weight: 800; color: #ffffff; background-color: {RED}; width: 30px; height: 30px; line-height: 30px; text-align: center; border-radius: 50%;"),
                                                                       t(f"{label} Step {i} Text", s, f"font-size: 15px; line-height: 1.6; color: {MUTED}; & strong {{ color: {TEXT}; }}")], "34px minmax(0, 1fr)", 12, "", "34px minmax(0, 1fr)")
                                             for i, s in enumerate(steps, 1)], 12, "margin-top: 8px;")], 10,
               f"background-color: #ffffff; border: 1px solid {LINE}; border-radius: 14px; padding: 30px; {SH}")
def dcard(label, icon, title, text):
    return col(label, [icbox(label + " Icon", icon, "pink", "rgba(220,38,38,0.14)"), h3(label + " Title", title, 18.4, "", ONDARK), body(label + " Text", text, 15.2, "", MUTEDD)], 10,
               f"background-color: {PANEL}; border: 1px solid {LINED}; border-radius: 14px; padding: 26px;")
def prose(label, eyebrow_txt, title, paras, extra=None, dark=False):
    k = [eyebrow(label + " Eyebrow", eyebrow_txt), h2(label + " Title", title, "", dark)] + \
        [t(f"{label} P{i}", p_, f"font-size: 16.3px; line-height: 1.65; color: {MUTEDD if dark else MUTED}; & strong {{ color: {'#ffffff' if dark else TEXT}; }}") for i, p_ in enumerate(paras, 1)]
    if extra: k.append(extra)
    return col(label, k, 16, "max-width: 68ch;")

# ------------------------------------------------------------------ serialise / push
def serialise(roots):
    used, cfg, sty, cls = {}, {}, {}, {}
    def uid(lbl):
        lbl = "".join(ch for ch in lbl if ch.isalnum() or ch in " -")[:60].strip() or "Element"
        n = used.get(lbl, 0); used[lbl] = n + 1
        return lbl if n == 0 else f"{lbl} {n+1}"
    def walk(n):
        cid = uid(n.label)
        if n.cfg: cfg[cid] = n.cfg
        if n.style: sty[cid] = n.style
        if n.cls: cls[cid] = n.cls
        return f'<{n.t} configuration-id="{html.escape(cid, quote=True)}">' + "".join(walk(k) for k in n.kids) + f"</{n.t}>"
    return "".join(walk(r) for r in roots), cfg, sty, cls

def push(post_id, sections, dry=False, publish=False):
    for i, s in enumerate(sections):
        xml, cfg, sty, cls = serialise([s])
        args = {"post_id": post_id, "xml_structure": xml, "element_config": cfg, "style": sty, "classes": cls,
                "mode": "replace_children" if i == 0 else "append", "parent_id": "document"}
        if dry: args["dry_run"] = True
        r = call("elementor-build-composition", args)
        bad = r.get("_isError") or r.get("_error")
        warn = [w for w in (r.get("warnings") or []) if "wrapped" not in w]
        print(f"  [{post_id}] {i+1}/{len(sections)} {s.label}: {'ERROR ' + json.dumps(r)[:700] if bad else 'ok'}" + (f" warnings={json.dumps(warn)[:500]}" if warn else ""))
        if bad: return False
    if not dry:
        # a published document keeps edits in an autosave; manage-elements only works once that is promoted
        if publish: call("elementor-publish-document", {"post_id": post_id})
        refresh_css(post_id, sections[0].style)
        if publish: print(f"  [{post_id}] publish: {call('elementor-publish-document', {'post_id': post_id}).get('status')}")
    return True

def refresh_css(post_id, root_style):
    st = call("elementor-get-page-structure", {"post_id": post_id})
    ids = re.findall(r'"id": "([0-9a-f]+)"', json.dumps(st))
    import time
    for k in range(6):
        time.sleep(2 + 3 * k)
        r = call("elementor-manage-elements", {"post_id": post_id, "operations": [{"action": "update", "element_id": ids[0], "style": "min-width: 0;"}]})
        if r.get("status") == "ok": break
    print(f"  [{post_id}] css refresh: {r.get('status')}")
