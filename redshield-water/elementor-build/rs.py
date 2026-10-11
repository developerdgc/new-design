"""Builds RedShield Water pages in Elementor (V4 atomic widgets) through the MCP build-composition tool."""
import json, os, sys, html
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
          "#blocked-drain-service": "bds", "#services": "services"}
RED = "#dc2626"

# ---------------------------------------------------------------- node model
class N:
    def __init__(s, t, label, cfg=None, style="", cls=None, kids=None):
        s.t, s.label, s.cfg, s.style, s.cls, s.kids = t, label, cfg or {}, style, cls or [], kids or []

def link(href):
    if isinstance(href, str) and href in P: href = P[href]
    if isinstance(href, int): return {"destination": {"id": href}, "tag": "a"}
    return {"destination": href, "tag": "a", **({"isTargetBlank": True} if href.startswith("http") else {})}

def flex(label, kids, style="", cls=None, tag=None, href=None):
    cfg = {}
    if tag: cfg["tag"] = tag
    if href is not None: cfg["link"] = link(href); cfg["tag"] = "a"
    return N("e-flexbox", label, cfg, style, cls, kids)
def col(label, kids, gap=16, style="", cls=None, **kw):
    return flex(label, kids, f"flex-direction: column; gap: {gap}px; padding: 0; " + style, cls, **kw)
def row(label, kids, gap=12, style="", cls=None, **kw):
    return flex(label, kids, f"flex-direction: row; flex-wrap: wrap; gap: {gap}px; padding: 0; align-items: center; " + style, cls, **kw)
def grid(label, kids, cols=3, gap=22, style="", cls=None):
    return N("e-grid", label, {}, f"grid-template-columns: repeat({cols}, minmax(0, 1fr)); grid-template-rows: auto; gap: {gap}px; padding: 0; "
             f"@media(--tablet) {{ grid-template-columns: repeat({min(cols, 2)}, minmax(0, 1fr)); }} @media(--mobile) {{ grid-template-columns: repeat(1, minmax(0, 1fr)); }} " + style, cls, kids)
def _fix(text, cls, style):
    cls = list(cls or [])
    if "rs-h2-light" in cls: cls.remove("rs-h2-light"); style = style + " color: #ffffff;"
    if "rs-on-dark" in cls: cls.remove("rs-on-dark"); style = style + " color: #aab5c5;"
    if "<em>" in text and "rs-em-red" not in cls: cls.append("rs-em-red")
    if "<b>" in text and "rs-b-gold" not in cls and "rs-b-green" not in cls: cls.append("rs-b-gold")
    return cls, style
def h(label, text, tag="h2", cls=None, style=""):
    cls, style = _fix(text, cls, style)
    return N("e-heading", label, {"tag": tag, "title": text}, style, cls)
def p(label, text, cls=None, style=""):
    cls, style = _fix(text, cls, style)
    return N("e-paragraph", label, {"paragraph": text}, style, cls)
def btn(label, text, href, cls=("rs-btn-red",), style=""):
    return N("e-button", label, {"text": text, "link": link(href)}, style, list(cls))
def img(label, file, alt, style="", href=None):
    url = file if file.startswith("http") else IMG + file
    cfg = {"image": {"src": {"url": url, "alt": alt}, "size": "full"}}
    if href is not None: cfg["link"] = link(href)
    return N("e-image", label, cfg, "display: block; width: 100%; height: auto; " + style)
def red(t): return f"<em>{t}</em>"
def accordion(label, items, dark=False):
    its = []
    for i, (q, a) in enumerate(items):
        its.append(N("e-accordion-item", f"{label} Item {i+1}", style="background-color: #ffffff; border: 1px solid var(--rs-line); border-radius: 12px; overflow: hidden; box-shadow: 0 1px 2px rgba(14,23,38,0.06), 0 10px 26px -14px rgba(14,23,38,0.28);", kids=[
            N("e-accordion-item-header", f"{label} Q{i+1} Header", style="padding: 18px 20px; cursor: pointer;", kids=[
                N("e-accordion-item-title", f"{label} Q{i+1} Title", kids=[p(f"{label} Q{i+1}", q, style="font-family: var(--rs-font); font-size: 16px; font-weight: 700; color: var(--rs-text);")])]),
            N("e-accordion-item-content", f"{label} A{i+1} Body", style="padding: 0 20px 18px;", kids=[p(f"{label} A{i+1}", a, ["rs-body"])])]))
    return N("e-accordion", label, {"default_state": "all_collapsed", "max_expanded": "one", "show_icon": True, "faq_schema": True}, "gap: 10px;", None, its)

# ---------------------------------------------------------------- serialisation
def serialise(roots):
    used, xml_parts, cfg, sty, cls = {}, [], {}, {}, {}
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
    xml = "".join(walk(r) for r in roots)
    return xml, cfg, sty, cls

def push(post_id, sections, replace_first=True, dry=False):
    """Send each section as its own build-composition call (keeps payloads small)."""
    out = []
    for i, sec in enumerate(sections):
        xml, cfg, sty, cls = serialise([sec])
        args = {"post_id": post_id, "xml_structure": xml, "element_config": cfg, "style": sty, "classes": cls,
                "mode": "replace_children" if (i == 0 and replace_first) else "append", "parent_id": "document"}
        if dry: args["dry_run"] = True
        r = call("elementor-build-composition", args)
        bad = r.get("_isError") or r.get("_error")
        warn = r.get("warnings") or []
        print(f"  [{post_id}] section {i+1}/{len(sections)} {sec.label}: {'ERROR ' + json.dumps(r)[:600] if bad else 'ok'}" + (f" warnings={json.dumps(warn)[:400]}" if warn else ""))
        out.append(r)
        if bad: break
    if not dry: refresh_css(post_id, sections[0].style)
    return out

def refresh_css(post_id, root_style):
    """A manage-elements save makes Elementor regenerate the page's cached CSS (build-composition alone does not)."""
    import re
    st = call("elementor-get-page-structure", {"post_id": post_id})
    ids = re.findall(r'"id": "([0-9a-f]+)"', json.dumps(st))
    if not ids: print("  css refresh: no root found"); return
    r = call("elementor-manage-elements", {"post_id": post_id, "operations": [{"action": "update", "element_id": ids[0], "style": root_style}]})
    print(f"  [{post_id}] css refresh: {r.get('status', json.dumps(r)[:200])}")

# ---------------------------------------------------------------- shared sections
def wrap(label, kids, gap=28, style=""):
    return col(label, kids, gap, "max-width: 1200px; margin: 0 auto; padding: 0 20px; " + style)
def section(label, kind, kids, gap=28, style="", wrap_style=""):
    return flex(label, [wrap(label + " Inner", kids, gap, wrap_style)], "flex-direction: column; " + style, [f"rs-sec-{kind}"], tag="section")
def head(label, eyebrow, title, lead=None, dark=False, center=True):
    k = []
    if eyebrow: k.append(p(label + " Eyebrow", eyebrow, ["rs-eyebrow"], "text-align: center;" if center else ""))
    k.append(h(label + " Title", title, "h2", ["rs-h2"] + (["rs-h2-light"] if dark else []), "text-align: center;" if center else ""))
    if lead: k.append(p(label + " Lead", lead, ["rs-lead"] + (["rs-on-dark"] if dark else []), "text-align: center; max-width: 680px; margin: 0 auto;" if center else "max-width: 640px;"))
    return col(label + " Heading", k, 12, "align-items: center; margin-bottom: 8px;" if center else "margin-bottom: 8px;")

GLASS = "background-color: rgba(9,15,27,0.62); border: 1px solid rgba(255,255,255,0.14); border-radius: 14px; backdrop-filter: blur(8px);"
def stat(label, big, small):
    return col(label, [p(label + " Value", big, style="font-family: var(--rs-font); font-size: 24px; font-weight: 800; color: #ffffff; text-align: center; line-height: 1.2;"),
                       p(label + " Label", small, style="font-family: var(--rs-font); font-size: 13px; color: #9fb0c5; text-align: center;")], 2,
               "padding: 14px 10px; " + GLASS)
def stats(n=3):
    s = [stat("Stat Arrival", f"45 {red('min')}", "Typical arrival"), stat("Stat Guarantee", f"12 {red('mo')}", "Repair guarantee"),
         stat("Stat Rating", '5.0 <b>★★★★★</b>' if n == 4 else '5.0 <b>★</b>', "Trustpilot rating"), stat("Stat Hours", f"24{red('/')}7", "Always answered")][:n]
    return grid("Hero Stats", s, n, 12, f"max-width: {220*n}px; @media(--mobile) {{ grid-template-columns: repeat({2 if n == 4 else 3}, minmax(0, 1fr)); }}")

def callcard(area="Leeds, Harrogate &amp; all of Yorkshire", solid=False):
    return col("Call Card", [
        p("Call Card Label", "24/7 EMERGENCY CALL OUT", style="font-family: var(--rs-font); font-size: 13px; font-weight: 700; letter-spacing: 0.06em; color: #ff6b6b;"),
        p("Call Card Note", "We're here when you need us.", ["rs-body", "rs-on-dark"], "font-size: 14px;"),
        p("Call Card Number", PHONE, style="font-family: var(--rs-font); font-size: 38px; font-weight: 800; color: #ffffff; letter-spacing: -0.01em;"),
        p("Call Card Points", f"✓ 45-minute target arrival<br>✓ {area}<br>✓ 12-month repair guarantee", ["rs-body", "rs-on-dark"], "font-size: 15px; line-height: 1.9;"),
        btn("Call Card Button", "Call Now", TEL, style="text-align: center;")], 10, "padding: 28px; " + ("background-color: #0b2340; border-radius: 16px;" if solid else GLASS) + " box-shadow: 0 30px 60px -24px rgba(0,0,0,0.6);")

def hero(crumbs, badge, title, sub, photo, buttons, solo=False, area=None):
    left = [p("Hero Breadcrumb", crumbs, style="font-family: var(--rs-font); font-size: 13px; color: #8c9bb0;" + (" text-align: center;" if solo else "")),
            p("Hero Badge", badge, style="font-family: var(--rs-font); font-size: 14px; font-weight: 600; color: #e2e8f0; padding: 7px 16px; border-radius: 999px; " + GLASS + " width: fit-content;" + (" margin: 0 auto;" if solo else "")),
            h("Hero Title", title, "h1", style="font-family: var(--rs-font); font-size: 54px; font-weight: 800; letter-spacing: -0.035em; line-height: 1.1; color: #ffffff; text-shadow: 0 2px 24px rgba(0,0,0,0.35); @media(--mobile) { font-size: 36px; }" + (" text-align: center;" if solo else "")),
            p("Hero Intro", sub, style="font-family: var(--rs-font); font-size: 18px; line-height: 1.6; color: #c3cedc; max-width: 600px;" + (" text-align: center; margin: 0 auto;" if solo else "")),
            row("Hero Buttons", buttons, 12, "justify-content: center;" if solo else ""),
            stats(3)]
    if solo:
        left[-1].style += " margin: 0 auto;"
    lc = col("Hero Content", left, 20, "align-items: center;" if solo else "")
    inner = [lc] if solo else [lc, callcard(area or "Leeds, Harrogate &amp; all of Yorkshire")]
    grid_style = "grid-template-columns: minmax(0, 1fr);" if solo else "grid-template-columns: minmax(0, 1.35fr) minmax(0, 1fr); align-items: center; @media(--tablet) { grid-template-columns: minmax(0, 1fr); }"
    body = N("e-grid", "Hero Layout", {}, grid_style + " grid-template-rows: auto; gap: 40px; padding: 0 20px; max-width: 1200px; margin: 0 auto; @media(--mobile) { grid-template-columns: minmax(0, 1fr); }", None, inner)
    shade = "rgba(6,11,19,0.6), rgba(6,11,19,0.85)" if solo else "90deg, rgba(6,11,19,0.9) 0%, rgba(6,11,19,0.55) 62%, rgba(6,11,19,0.35) 100%"
    bg = f"background: linear-gradient({shade}), url({IMG}{photo}) center / cover no-repeat;" if solo else f"background: linear-gradient({shade}), url({IMG}{photo}) center / cover no-repeat;"
    return flex("Hero", [body], f"flex-direction: column; padding: 64px 0 64px; {bg} @media(--mobile) {{ padding: 44px 0; }}", tag="section")

def call_btn(label="Hero Call Button"): return btn(label, f"📞 Call {PHONE}", TEL)
def ghost(label, text, href): return btn(label, text, href, ("rs-btn-ghost",))

def reviews(kind="dark"):
    cards = [col(f"Review {i+1}", [p(f"Review {i+1} Stars", "★★★★★", style="font-size: 18px; letter-spacing: 2px; color: var(--rs-trustpilot);"),
                                  h(f"Review {i+1} Title", t, "h3", ["rs-h3"], "font-size: 16px;"),
                                  p(f"Review {i+1} Text", b, ["rs-body"], "font-size: 14px;"),
                                  p(f"Review {i+1} By", "Verified Trustpilot reviewer", style="font-family: var(--rs-font); font-size: 12px; color: var(--rs-muted);")], 8,
                 "flex: 0 0 300px; background-color: #ffffff; border-radius: 12px; padding: 18px;") for i, (t, b) in enumerate(D["REVIEWS"])]
    top = p("Trustpilot Summary", '<strong>Excellent &nbsp;★★★★★</strong>&nbsp; Rated by customers on <strong>Trustpilot</strong>', ["rs-strong-green"],
            style="font-family: var(--rs-font); font-size: 16px; color: #c7d0dc; text-align: center;")
    strip = row("Review Strip", cards, 16, "flex-wrap: nowrap; overflow-x: auto; padding: 4px 4px 18px; align-items: stretch; scroll-snap-type: x mandatory;")
    return section("Reviews", kind, [top, strip], 20, "padding-top: 36px;" if kind == "dark" else "")

def how3():
    steps = [("1", "Call us, any time", "A real plumber answers 24/7 and tells you how to stop the water."),
             ("2", "We come to you", "For emergencies we aim to be at your door within 45 minutes."),
             ("3", "Price first, then the fix", "You get the price before we start. Repairs are guaranteed for 12 months.")]
    cards = [row(f"Step {n}", [p(f"Step {n} Number", n, style="font-family: var(--rs-font); width: 42px; height: 42px; line-height: 42px; text-align: center; border-radius: 50%; background-color: var(--rs-text); color: #ffffff; font-weight: 800; flex-shrink: 0;"),
                               col(f"Step {n} Text", [h(f"Step {n} Title", t, "h3", ["rs-h3"], "font-size: 17px;"), p(f"Step {n} Body", b, ["rs-body"], "font-size: 15px;")], 4, "flex: 1;")],
                 14, "align-items: flex-start; flex-wrap: nowrap;", ["rs-card"]) for n, t, b in steps]
    return section("How It Works", "mist", [grid("How Steps", cards, 3, 18)], 0, "padding: 48px 0;")

def svc_card(i, imgf, title, desc, hot, href):
    target = P[HASH2P[href]] if href in HASH2P else TEL
    panel = col(f"Service {i} Panel", ([p(f"Service {i} Tag", "24/7", ["rs-tag"], "width: fit-content;")] if hot else []) + [
        h(f"Service {i} Title", title, "h3", style="font-family: var(--rs-font); font-size: 20px; font-weight: 700; color: #ffffff;"),
        p(f"Service {i} Text", desc, style="font-family: var(--rs-font); font-size: 15px; line-height: 1.55; color: #d3dbe6;"),
        p(f"Service {i} Link", ("Learn more →" if href else "Call about this →"), style="font-family: var(--rs-font); font-size: 14px; font-weight: 700; color: #ff8080;")], 8,
        "padding: 18px; background-color: rgba(8,14,26,0.88); border: 1px solid rgba(255,255,255,0.08); border-radius: 12px; border-bottom: 3px solid #dc2626;")
    return col(f"Service {i}", [panel], 0, f"justify-content: flex-end; min-height: 330px; padding: 12px; border-radius: 16px; overflow: hidden; "
               f"background: linear-gradient(180deg, rgba(6,11,19,0) 35%, rgba(6,11,19,0.55) 100%), url({IMG}svc-{imgf}.jpg) center / cover no-repeat; "
               "box-shadow: 0 1px 2px rgba(14,23,38,0.06), 0 10px 26px -14px rgba(14,23,38,0.28); transition: transform 0.25s; &:hover { transform: translateY(-4px); }", href=target)

def services(kind="white", eyebrow=None, title=f"Our {red('Emergency')} Services",
             lead="Professional plumbing services available 24/7 across Yorkshire. We handle emergencies with speed and expertise."):
    cards = [svc_card(i + 1, *s[:3], s[4] if len(s) > 4 else False, s[5] if len(s) > 5 else None) for i, s in enumerate(D["SERVICES"])]
    also = p("Also Fix", "<strong>We also fix:</strong> &nbsp;Dripping taps · Toilets &amp; cisterns · Radiators · Hot water cylinders · Outside taps · Washing machine leaks",
             ["rs-body"], "text-align: center; font-size: 15px;")
    return section("Services", kind, [head("Services", eyebrow, title, lead), grid("Service Cards", cards, 3, 22), also], 28)

def issues_and_call(title="What Plumbing Issue Do You Have?", kind="mist"):
    items = [(k, "<ol>" + "".join(f"<li>{s}</li>" for s in v[1]) + "</ol>") for k, v in D["ISSUES"].items()]
    left = col("Issue Help", [p("Issue Eyebrow", "Quick help", ["rs-eyebrow"]), h("Issue Title", title, "h2", ["rs-h2"], "font-size: 34px;"),
                              p("Issue Lead", "Tap your problem to see what to do right now, before we arrive.", ["rs-lead"]),
                              accordion("Issue Steps", items),
                              p("Issue Note", "<strong>Not sure what to do?</strong> Turn off your stop tap if you can, then call us. A plumber will talk you through it.",
                                ["rs-body"], "background-color: #fff7ed; border: 1px solid #fed7aa; border-radius: 12px; padding: 16px 18px; color: #6b4a22;")], 14)
    right = col("Help Card", [h("Help Card Title", "GET EMERGENCY HELP NOW", "h3", style="font-family: var(--rs-font); font-size: 22px; font-weight: 800; color: #ffffff;"),
                              p("Help Card Text", "Fast response across Leeds &amp; all of Yorkshire. Call and a real plumber answers, day or night.", style="font-family: var(--rs-font); font-size: 15px; line-height: 1.6; color: #a9bbd2;"),
                              p("Help Card Number", PHONE, style="font-family: var(--rs-font); font-size: 34px; font-weight: 800; color: #ffffff;"),
                              btn("Help Card Call", "📞 Call Me Now", TEL, style="text-align: center;"),
                              btn("Help Card Message", "Send a message", "contact", ("rs-btn-ghost",), "text-align: center;"),
                              p("Help Card Private", "🔒 Your details are kept private and secure", style="font-family: var(--rs-font); font-size: 13px; color: #a9bbd2; text-align: center;")], 14,
                "padding: 28px; background-color: #0b2340; border-radius: 16px; box-shadow: 0 30px 60px -20px rgba(11,35,64,0.6);")
    g = N("e-grid", "Issue Layout", {}, "grid-template-columns: minmax(0, 1.5fr) minmax(0, 1fr); grid-template-rows: auto; gap: 36px; padding: 0; align-items: start; @media(--tablet) { grid-template-columns: minmax(0, 1fr); }", None, [left, right])
    return section("Plumbing Issues", kind, [g])

def jobs_cards(n):
    return [row(f"Job {i+1}", [col(f"Job {i+1} Text", [h(f"Job {i+1} Title", t, "h4", ["rs-h3"], "font-size: 16px;"), p(f"Job {i+1} Body", d, ["rs-body"], "font-size: 14px;")], 4, "flex: 1;"),
                                p(f"Job {i+1} When", w, style="font-family: var(--rs-font); font-size: 12px; font-weight: 700; color: #b91c1c; border: 1px solid rgba(220,38,38,0.4); border-radius: 5px; padding: 3px 8px;")],
                12, "flex-wrap: nowrap; align-items: flex-start;", ["rs-card"]) for i, (w, t, d, _) in enumerate(D["JOBS"][:n])]

def chips(label, key):
    return row(label, [p(f"{label} {i+1}", c, ["rs-chip"]) for i, c in enumerate(D["CHIPS"][key].split("|"))], 8)

def leeds_areas_jobs(kind="white", n=3):
    left = col("Leeds Areas", [p("Leeds Areas Eyebrow", "Local engineers", ["rs-eyebrow"]), h("Leeds Areas Title", "Areas We Cover in Leeds", "h2", ["rs-h2"], "font-size: 32px;"),
                               p("Leeds Areas Lead", "Emergency plumbing across Leeds and the surrounding neighbourhoods.", ["rs-lead"]), chips("Leeds Chips", "leeds"),
                               btn("Leeds Areas Button", "View Leeds page", "leeds", ("rs-btn-line",), "width: fit-content;")], 14)
    right = col("Recent Jobs", [p("Recent Jobs Eyebrow", "Recent work", ["rs-eyebrow"]), h("Recent Jobs Title", "Recent Emergency Jobs in Leeds", "h2", ["rs-h2"], "font-size: 32px;")] + jobs_cards(n), 12)
    return section("Leeds Areas And Jobs", kind, [grid("Leeds Layout", [left, right], 2, 48)])

def plans():
    def plan(n, flag, flagbg, title, price, pick, ticks, btext, bhref, hot=False):
        return col(f"Plan {n}", [p(f"Plan {n} Flag", flag, style=f"font-family: var(--rs-font); font-size: 11px; font-weight: 800; letter-spacing: 0.1em; color: {'#1a1400' if flagbg == '#eab308' else '#ffffff'}; background-color: {flagbg}; border-radius: 5px; padding: 5px 10px; width: fit-content;"),
                                 h(f"Plan {n} Title", title, "h3", style="font-family: var(--rs-font); font-size: 21px; font-weight: 700; color: #ffffff;"),
                                 row(f"Plan {n} Price Row", [p(f"Plan {n} Price", price, style=f"font-family: var(--rs-font); font-size: 48px; font-weight: 800; line-height: 1; color: {RED if hot else '#ffffff'};"), p(f"Plan {n} Price Unit", "call-out", style="font-family: var(--rs-font); font-size: 15px; color: #aab5c5;")], 8, "align-items: baseline;"),
                                 p(f"Plan {n} Pick", pick, style="font-family: var(--rs-font); font-size: 15px; font-weight: 600; color: #ffffff; background-color: rgba(255,255,255,0.05); border-radius: 8px; padding: 10px 12px;"),
                                 p(f"Plan {n} Points", "<br>".join("✓ " + t for t in ticks), ["rs-body", "rs-on-dark"], "font-size: 15px; line-height: 1.9;"),
                                 btn(f"Plan {n} Button", btext, bhref, ("rs-btn-red",) if hot else ("rs-btn-ghost",), "text-align: center; margin-top: auto;")], 14,
                   f"padding: 30px 26px; background-color: var(--rs-panel); border-radius: 16px; border: {'2px solid #dc2626' if hot else '1px solid var(--rs-line-dark)'};")
    cards = [plan(1, "FASTEST", "#dc2626", "Immediate Response", "£50", "Choose this if water is leaking or flooding right now.", ["Engineer sent straight away", "Usually with you within 45 minutes", "You go to the front of the queue"], "Get Help Now", TEL, True),
             plan(2, "BEST PRICE", "#16a34a", "Same Day Service", "£25", "Choose this if there's a problem but it isn't getting worse.", ["We visit later today", "Fixed the same day", "Emergencies are seen first"], "Book Today", TEL),
             plan(3, "FLEXIBLE BOOKING", "#eab308", "Standard Booking", "£0", "Choose this if the job can wait a day or more.", ["No call-out fee", "Pick a day that suits you", "Good for planned work"], "Schedule Visit", "contact")]
    note = p("Plans Note", "The call-out fee is taken off your final bill if you go ahead. You always get the repair price before we start. Fully insured, 12-month guarantee.",
             ["rs-body", "rs-on-dark"], "text-align: center; max-width: 640px; margin: 0 auto;")
    return section("Pricing Plans", "dark", [head("Plans", None, f"Choose Your {red('Response Speed')}", "Transparent call-out options. No surprises.", True), grid("Plan Cards", cards, 3, 22), note])

def tiers(kind="white", title="Drain Pricing", lead="Three response tiers. Quoted before we start. Call-out fee always deducted from the final bill."):
    t = [("Standard", "From £80", "Same-day visit", "Call-out fee taken off the final bill.", False),
         ("Priority", "From £120", "Within 2 hours", "For blockages that are getting worse or overflowing.", False),
         ("Emergency", "From £180", "45-min response", "Sewage, flooding, or several fixtures blocked at once.", True)]
    cards = [col(f"Tier {i+1}", [p(f"Tier {i+1} Name", n.upper(), style="font-family: var(--rs-font); font-size: 12px; font-weight: 800; letter-spacing: 0.12em; color: var(--rs-muted);"),
                                 p(f"Tier {i+1} Price", pr, style="font-family: var(--rs-font); font-size: 34px; font-weight: 800; color: var(--rs-text);"),
                                 p(f"Tier {i+1} Speed", sp, style="font-family: var(--rs-font); font-size: 15px; font-weight: 700; color: #b91c1c;"),
                                 p(f"Tier {i+1} Note", nt, ["rs-body"], "font-size: 15px;")], 6, ("border: 2px solid #dc2626;" if hot else ""), ["rs-card"])
             for i, (n, pr, sp, nt, hot) in enumerate(t)]
    return section("Drain Prices", kind, [head("Tiers", "Drain unblocking", title, lead), grid("Tier Cards", cards, 3, 18)])

def area_map(kind="mist", centre="leeds"):
    if centre == "harrogate":
        title, loc, text, mapf = f"We Cover {red('Harrogate')}", "Harrogate + 25 miles", "Serving Harrogate and all surrounding areas within a 25-mile radius, including York and Ripon.", "map-harrogate.svg"
        pills = [("Harrogate", None, 1), ("Starbeck",), ("Bilton",), ("Knaresborough",), ("Pannal",), ("Killinghall",), ("Hampsthwaite",), ("Boroughbridge",), ("Ripon",), ("York", "yorkshire"), ("Wetherby",), ("Otley",)]
    else:
        title, loc, text, mapf = f"Areas We {red('Cover')}", "All of Yorkshire", "Based in Leeds, our engineers cover West Yorkshire and beyond. Homes inside the first ring usually see us within 45 minutes.", "map-leeds.svg"
        pills = [("Leeds", "leeds", 1), ("Harrogate", "harrogate"), ("York", "yorkshire"), ("Wakefield", "yorkshire"), ("Huddersfield", "yorkshire"), ("Halifax", "yorkshire"), ("Doncaster", "yorkshire"),
                 ("Bradford",), ("Dewsbury",), ("Pontefract",), ("Otley",), ("Wetherby",), ("Selby",), ("Knaresborough",)]
    pill_nodes = []
    for i, pl in enumerate(pills):
        name, href, home = (list(pl) + [None, None])[:3]
        st = "font-family: var(--rs-font); font-size: 14px; font-weight: 600; border-radius: 999px; padding: 9px 14px; " + \
             ("background-color: #dc2626; color: #ffffff; border: 1px solid #dc2626;" if home else "background-color: #ffffff; color: var(--rs-text); border: 1px solid var(--rs-line); box-shadow: 0 1px 2px rgba(14,23,38,0.06), 0 10px 26px -14px rgba(14,23,38,0.28);")
        pill_nodes.append(btn(f"Town {name}", f"📍 {name}", href, (), st) if href else p(f"Town {name}", f"📍 {name}", style=st))
    left = col("Area Copy", [p("Area Eyebrow", "Service area", ["rs-eyebrow"]), h("Area Title", title, "h2", ["rs-h2"]),
                             p("Area Location", f'📍 Location: <em>{loc}</em>', style="font-family: var(--rs-font); font-size: 15px; font-weight: 600; color: #ffffff; background-color: var(--rs-navy); border-radius: 10px; padding: 9px 15px; width: fit-content;"),
                             p("Area Text", text, ["rs-lead"]), row("Town Pills", pill_nodes, 9),
                             row("Area Footer", [p("Area Footer Text", "Not listed? Call us anyway, we may still be able to help.", ["rs-body"], "max-width: 280px;"), btn("Area Call", f"📞 Call {PHONE}", TEL)], 18,
                                 "padding-top: 20px; border-top: 1px solid var(--rs-line);")], 18)
    right = col("Map", [img("Coverage Map", mapf, f"Map of RedShield Water's service area around {centre.title()}", "border-radius: 16px;"),
                        p("Map Caption", f'●&nbsp; 45-minute response from {centre.title()}', style="font-family: var(--rs-font); font-size: 15px; font-weight: 700; color: #ffffff; background-color: #dc2626; border-radius: 12px; padding: 12px 16px;")],
                12, "padding: 12px; background-color: #0c1524; border-radius: 20px; box-shadow: 0 28px 56px -24px rgba(6,11,19,0.6);")
    g = N("e-grid", "Area Layout", {}, "grid-template-columns: minmax(0, 1fr) minmax(0, 520px); grid-template-rows: auto; gap: 52px; padding: 0; align-items: center; @media(--tablet) { grid-template-columns: minmax(0, 1fr); }", None, [left, right])
    return section("Service Area", kind, [g])

def videos_section(kind="white", n=4, start=0, title="Emergency DIY Tips While You Wait", lead="Short videos that help you limit the damage before we arrive.", eyebrow="While you wait"):
    cards = [col(f"Video {i+1}", [img(f"Video {i+1} Thumbnail", v[2].replace("img/", ""), v[0], "border-radius: 12px; aspect-ratio: 16 / 9; object-fit: cover;", v[3]),
                                  p(f"Video {i+1} Number", f"VIDEO {i+1}", ["rs-eyebrow"], "font-size: 12px;"),
                                  h(f"Video {i+1} Title", v[0], "h3", ["rs-h3"], "font-size: 17px;"), p(f"Video {i+1} Text", v[1], ["rs-body"], "font-size: 14px;"),
                                  btn(f"Video {i+1} Watch", "▶ Watch on YouTube", v[3], ("rs-btn-line",), "width: fit-content; font-size: 14px; padding: 9px 16px;")], 8, "padding: 14px;", ["rs-card"])
             for i, v in list(enumerate(D["VIDEOS"]))[start:start + n]]
    return section("Videos", kind, [head("Videos", eyebrow, title, lead), grid("Video Cards", cards, min(n, 4), 20)])

def slim_tutorials():
    r = row("Tutorial Banner", [col("Tutorial Banner Text", [h("Tutorial Banner Title", "Waiting for the plumber?", "h3", ["rs-h3"]),
                                                             p("Tutorial Banner Lead", "Watch our free short videos on turning off your water and limiting the damage.", ["rs-body"])], 4, "flex: 1;"),
                                btn("Tutorial Banner Button", "Watch free videos", "tutorials", ("rs-btn-line",))], 18, "justify-content: space-between;", ["rs-card"])
    return section("Tutorial Banner Section", "white", [r], 0, "padding: 48px 0;")

def cta(a, b, c, sub):
    return section("Call To Action", "dark", [
        p("CTA Badge", "<b>●</b> Available Right Now", ["rs-b-green"], style="font-family: var(--rs-font); font-size: 14px; font-weight: 600; color: #e2e8f0; padding: 7px 16px; border-radius: 999px; border: 1px solid rgba(255,255,255,0.16); background-color: rgba(255,255,255,0.06); width: fit-content; margin: 0 auto;"),
        h("CTA Title", f"{a}{red(b)}{c}", "h2", ["rs-h2", "rs-h2-light"], "text-align: center;"),
        p("CTA Text", sub, ["rs-lead", "rs-on-dark"], "text-align: center; max-width: 620px; margin: 0 auto;"),
        btn("CTA Button", f"📞 Call {PHONE}", TEL, style="margin: 0 auto; font-size: 18px; padding: 18px 32px;"),
        p("CTA Facts", "🕒 45 Min Response &nbsp;&nbsp; 🛡 Work Guaranteed &nbsp;&nbsp; 📞 Always Answered", style="font-family: var(--rs-font); font-size: 15px; color: #a6b2c3; text-align: center;")],
        18, "background: radial-gradient(50% 70% at 50% 50%, rgba(220,38,38,0.1), rgba(6,11,19,0) 70%), #060b13;")

def faq_section(cat, title, kind="white", eyebrow="FAQs", lead=None):
    items = [(q, a) for c, q, a in D["FAQ"] if cat == "all" or cat in c.split()]
    return section(f"FAQ {cat}", kind, [head("FAQ " + cat, eyebrow, title, lead), col("FAQ Wrap", [accordion(f"FAQ {cat}", items)], 0, "max-width: 860px; margin: 0 auto; width: 100%;")])

def problems_grid(town=""):
    cards = [col(f"Problem {i+1}", [h(f"Problem {i+1} Title", t + (f" {town}" if town and "Stop Tap" not in t else ""), "h3", ["rs-h3"], "font-size: 17px;"),
                                    p(f"Problem {i+1} Text", d, ["rs-body"], "font-size: 15px;"),
                                    btn(f"Problem {i+1} Call", "Call now →", TEL, (), "font-family: var(--rs-font); font-size: 14px; font-weight: 700; color: #b91c1c; background-color: transparent; padding: 0; text-align: left;")], 8, "", ["rs-card"])
             for i, (_, t, d) in enumerate(D["PROBLEMS"])]
    return grid("Problem Cards", cards, 4, 18)

def contact_tiles(area="Leeds, Harrogate &amp; all of Yorkshire"):
    tiles = [("Call us 24/7", "07848 298 987", TEL), ("Email us", EMAIL, f"mailto:{EMAIL}"), ("Service area", area, None), ("Opening hours", "24 hours, 7 days a week", None)]
    out = []
    for i, (lab, val, href) in enumerate(tiles):
        kids = [p(f"Contact {i+1} Label", lab, style="font-family: var(--rs-font); font-size: 13px; font-weight: 600; color: var(--rs-muted);"),
                (btn(f"Contact {i+1} Value", val, href, (), "font-family: var(--rs-font); font-size: 19px; font-weight: 700; color: var(--rs-text); background-color: transparent; padding: 0; text-align: left;") if href
                 else p(f"Contact {i+1} Value", val, style="font-family: var(--rs-font); font-size: 19px; font-weight: 700; color: var(--rs-text);"))]
        out.append(col(f"Contact {i+1}", kids, 4, "padding: 18px 20px;", ["rs-card"]))
    return col("Contact Tiles", out, 12)

def why_list(label, items):
    return p(label, "<br>".join(f'<em>✓</em>&nbsp; {t}' for t in items), ["rs-body"],
             "font-size: 17px; line-height: 2.1; color: var(--rs-text); font-weight: 500;")

def two_col(label, left, right, ratio="1fr 1fr", align="center"):
    a, b = ratio.split()
    return N("e-grid", label, {}, f"grid-template-columns: minmax(0, {a}) minmax(0, {b}); grid-template-rows: auto; gap: 48px; padding: 0; align-items: {align}; @media(--tablet) {{ grid-template-columns: minmax(0, 1fr); }}", None, [left, right])
