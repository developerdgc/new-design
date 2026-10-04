import json
from blocks import *
b = B(); e = b.el
S = C["SVC"]

# ---------------- 1. HERO ----------------
coord = flex(b, "Hero Coord", [icon(b, "Hero Coord I", "location-dot", 14, "#FF8A1F"),
                               P(b, "Hero Coord T", "HQ 39.74° N, 104.99° W · Denver, CO", "font-family: var(--em-mono); font-size: 12.5px; color: #7AF0F5; letter-spacing: 0.05em;")],
             "gap: 10px; align-items: center; width: auto; padding: 8px 14px; border-radius: 50px; border: 1px dashed rgba(122,240,245,0.45);")
hero_txt = col(b, "Hero Text", [
    coord,
    H(b, "Hero Title", "We Navigate Your Business To More <strong>Customers</strong>", "h1", "color: #FFFFFF;", ["em-h1"]),
    P(b, "Hero Lead", "SEO, Google Ads, local search and websites, mapped to one goal: more qualified leads. Clear strategy, practical execution, and reports you can actually read.",
      "color: rgba(255,255,255,0.8); font-size: 18px; max-width: 520px;"),
    flex(b, "Hero Btns", [btn(b, "Hero B1", "Get a Free Audit", link_page("contact"), "g"), btn(b, "Hero B2", "Explore Services", link_page("services"), "o")], "gap: 12px; flex-wrap: wrap;")],
    "gap: 24px; flex: 1 1 52%; align-items: flex-start; z-index: 2;")

def pin(cid, ic, title, sub, pos, cls, hot=False):
    return flex(b, cid, [ico_tile(b, cid + " Ico", ic, hot, True, 30, 14),
                         col(b, cid + " Txt", [P(b, cid + " T", title, "font-size: 13.5px; font-weight: 700; color: #FFFFFF; line-height: 1.2;"),
                                               P(b, cid + " S", sub, "font-family: var(--em-mono); font-size: 11px; color: #7CF3BE; line-height: 1.2;")], "gap: 2px; width: auto;")],
                f"gap: 10px; align-items: center; width: auto; padding: 8px 14px 8px 8px; border-radius: 50px; background: rgba(7,18,51,0.85); border: 1px solid rgba(122,240,245,0.35); backdrop-filter: blur(8px); z-index: 3; {pos}", [cls])

globe = col(b, "Globe Slot", [
    # fallback art (fades when the 3D script mounts a canvas)
    flex(b, "Globe Fallback", [
        flex(b, "Ring Outer", [], "position: absolute; left: 0%; top: 0%; width: 100%; height: 100%; border: 1.5px dashed rgba(122,240,245,0.28);", ["em-ring-rev"]),
        flex(b, "Ring Mid", [], "position: absolute; left: 12%; top: 12%; width: 76%; height: 76%; border: 1.5px solid rgba(255,138,31,0.35); border-top-color: transparent; border-left-color: transparent;", ["em-ring"]),
        flex(b, "Globe Core", [img_el(b, "Globe Dots", "world-map-dots-svg", "width: 150%; max-width: none; opacity: 0.55;")],
             "position: absolute; left: 20%; top: 20%; width: 60%; height: 60%; border-radius: 50%; overflow: hidden; align-items: center; justify-content: center; background: radial-gradient(circle at 35% 30%, #13306E, #06123A 70%); box-shadow: 0 0 80px 10px rgba(63,208,222,0.35), inset 0 0 40px rgba(122,240,245,0.25);"),
        flex(b, "Globe Logo", [img_el(b, "Globe Logo Img", "icon", "width: 100%;", "EmmEnn Tech")],
             "position: absolute; left: 42%; top: 42%; width: 16%; filter: drop-shadow(0 0 18px rgba(122,240,245,0.7));")],
        "position: absolute; left: 0px; top: 0px; width: 100%; height: 100%;", ["em-globe-fallback"]),
    pin("Pin A", "magnifying-glass-chart", "Page 1 Rankings", "▲ 14 positions", "left: -4%; top: 18%;", "em-bob"),
    pin("Pin B", "phone", "More Calls", "+38% this month", "right: -4%; top: 46%;", "em-bob-2", True),
    pin("Pin C", "location-dot", "Map Pack", "Top 3 in Maps", "left: 6%; bottom: 8%;", "em-bob-3")],
    "position: relative; flex: 0 0 540px; width: 540px; height: 540px; @media(--tablet){ flex: 0 0 440px; width: 440px; height: 440px; align-self: center; } @media(--mobile){ flex: 0 0 300px; width: 300px; height: 300px; }",
    ["em-globe-slot"])

def hud(cid, label, value):
    return col(b, cid, [P(b, cid + " L", label, "font-family: var(--em-mono); font-size: 11.5px; letter-spacing: 0.1em; text-transform: uppercase; color: rgba(255,255,255,0.55);"),
                        P(b, cid + " V", value, "font-family: var(--em-num); font-size: 24px; font-weight: 700; color: #FFFFFF; line-height: 1.1;")],
               "gap: 6px; padding: 22px 18px; border-left: 1px solid rgba(255,255,255,0.12); @media(--mobile){ padding: 16px 12px; }")
hud_row = e("e-grid", "HUD", [hud("HUD 1", "Projects delivered", "200+"), hud("HUD 2", "Retainer clients", "170+"),
                               hud("HUD 3", "Avg. reply time", "< 1 day"), hud("HUD 4", "Client rating", "5.0 ★")],
            style="grid-template-columns: repeat(4, 1fr); grid-template-rows: auto; gap: 0px; padding: 0px; margin-top: 56px; border-top: 1px solid rgba(255,255,255,0.12); @media(--tablet){ grid-template-columns: 1fr 1fr; grid-template-rows: auto auto; }")
hero = flex(b, "Hero", [col(b, "Hero Wrap", [
    flex(b, "Hero Grid", [hero_txt, globe], "gap: 24px; align-items: center; justify-content: space-between; width: 100%; @media(--tablet){ flex-direction: column; align-items: flex-start; gap: 48px; }"),
    hud_row], "", ["em-wrap"])],
    f"flex-direction: column; align-items: center; width: 100%; padding: 160px 24px 0px 24px; background: radial-gradient(45% 60% at 78% 45%, rgba(63,208,222,0.24), transparent 70%), radial-gradient(35% 50% at 100% 100%, rgba(255,138,31,0.22), transparent 70%), linear-gradient(90deg, rgba(5,13,42,0.95) 0%, rgba(5,13,42,0.86) 45%, rgba(7,18,51,0.78) 100%), {bg('hero-team-strategy')} center 30% / cover no-repeat, #071233; @media(--tablet){{ padding: 140px 24px 0px 24px; }} @media(--mobile){{ padding: 120px 16px 0px 16px; }}",
    ["em-hero"])

# ---------------- 2. GROWTH ROUTE ----------------
CK = [("magnifying-glass-chart", False, "seo-services", "Get Found", "SEO, local SEO and Google Business Profile put you in front of people already searching."),
      ("display", True, "mobile-friendly-website", "Get Chosen", "A fast website, strong reviews and clear offers make them pick you over competitors."),
      ("phone", False, "happy-customers", "Get Customers", "Google Ads, tracking and follow-up turn interest into calls, forms and sales.")]
cps = []
for i, (ic, hot, im, t, p) in enumerate(CK):
    n = f"CP {i+1}"
    cps.append(col(b, n, [
        flex(b, n + " Node", [ico_tile(b, n + " Ico", ic, hot, True, 52)],
             "flex: 0 0 76px; width: 76px; height: 76px; border-radius: 50%; background: #FFFFFF; border: 2px solid #D3E3FB; align-items: center; justify-content: center; box-shadow: 0 14px 30px -18px rgba(31,107,224,0.6);", ["em-jp-node"]),
        img_el(b, n + " Img", im, "width: 100%; max-width: 300px; aspect-ratio: 16 / 10; object-fit: cover; border-radius: 16px; border: 4px solid #FFFFFF; box-shadow: 0 18px 34px -20px rgba(7,18,51,0.6);", "", ["em-jp-img"]),
        P(b, n + " K", f"CHECKPOINT 0{i+1}", "font-family: var(--em-mono); font-size: 12px; color: #FF8A1F; letter-spacing: 0.12em;"),
        H(b, n + " T", t, "h3", "font-size: 24px;"),
        P(b, n + " P", p, "color: #5B6683; max-width: 320px;")] +
        ([icon(b, n + " Arrow", "arrow-right", 20, "#1F6BE0", style="position: absolute; right: -24px; top: 28px; @media(--tablet){ display: none; }")] if i < 2 else []),
        "position: relative; gap: 12px; align-items: center; text-align: center; z-index: 1;", ["em-jp"]))
route_line = flex(b, "Route Line", [], "position: absolute; left: 16.6%; top: 38px; width: 66.8%; height: 0px; border-top: 2px dashed #B8CCEE; z-index: 0; @media(--tablet){ display: none; }")
route = section(b, "Route", [
    head(b, "Route Head", "Your Growth Route", "From Searching To <strong>Signed Customer</strong>", "Every service we run moves a customer one checkpoint closer to calling you.", center=True),
    e("e-grid", "Route Grid", [route_line] + cps, style="position: relative; grid-template-columns: repeat(3, 1fr); grid-template-rows: auto; gap: 28px; padding: 0px; @media(--tablet){ grid-template-columns: 1fr; grid-template-rows: auto; gap: 44px; }")])

# ---------------- 3. BENTO ABOUT ----------------
intro = col(b, "Bento Intro", [
    eyebrow(b, "Bento Eb", "Who We Are"),
    H(b, "Bento Title", "Digital Marketing, <strong>Without The Fluff</strong>", "h2", None, ["em-h2"]),
    P(b, "Bento P", "EmmEnn Tech helps businesses improve their visibility, generate qualified leads, and turn more website visitors into customers through SEO, paid advertising, web development, and local search."),
    col(b, "Bento Ticks", [bullet(b, "Bento T1", "You know what you're paying for"), bullet(b, "Bento T2", "You see the work being done"), bullet(b, "Bento T3", "You get results in plain language")], "gap: 10px;"),
    btn(b, "Bento Btn", "More About Us", link_page("about"), "g")],
    "gap: 18px; padding: 32px; grid-row: span 2; align-items: flex-start; @media(--tablet){ grid-column: 1 / -1; grid-row: auto; } @media(--mobile){ padding: 24px; }", ["em-card"])
photo = col(b, "Bento Photo", [
    img_el(b, "Bento Photo Img", "about-team-office", "", "EmmEnn Tech team working together"),
    flex(b, "Bento Photo Lbl", [ico_tile(b, "Bento Lbl Ico", "location-dot", False, False, 38, 18),
                                col(b, "Bento Lbl Txt", [P(b, "Bento Lbl T", "Denver, Colorado", "font-weight: 700; color: #FFFFFF; line-height: 1.2;"),
                                                         P(b, "Bento Lbl S", "Serving the US & UK", "font-family: var(--em-mono); font-size: 11px; color: #7AF0F5;")], "gap: 2px;")],
         "position: absolute; left: 14px; right: 14px; bottom: 14px; gap: 12px; align-items: center; padding: 14px 16px; border-radius: 14px; background: rgba(7,18,51,0.82); backdrop-filter: blur(8px); z-index: 2;")],
    "grid-row: span 2; min-height: 420px; border-radius: 22px; @media(--mobile){ grid-row: auto; min-height: 320px; }", ["em-tile-photo"])
def stat(cid, num, label, style):
    return col(b, cid, [P(b, cid + " N", num, "font-family: var(--em-num); font-size: 62px; font-weight: 700; line-height: 1; color: #FFFFFF; @media(--mobile){ font-size: 46px; }"),
                        P(b, cid + " L", label, "font-weight: 700; color: rgba(255,255,255,0.75);")],
               "gap: 6px; justify-content: flex-end; min-height: 170px; padding: 28px; border-radius: 22px; " + style)
s1 = stat("Bento S1", "200+", "Projects completed", "background: radial-gradient(60% 80% at 100% 0%, rgba(63,208,222,0.25), transparent 70%), #071233;")
s2 = stat("Bento S2", "170+", "Retainer clients", f"background: linear-gradient(160deg, rgba(34,198,224,0.82), rgba(31,107,224,0.92)), {bg('client-success')} center / cover no-repeat;")
bento = section(b, "Bento", [e("e-grid", "Bento Grid", [intro, photo, s1, s2],
    style="grid-template-columns: 1.25fr 0.85fr 0.9fr; grid-template-rows: auto auto; gap: 16px; padding: 0px; @media(--tablet){ grid-template-columns: 1fr 1fr; grid-template-rows: auto auto auto; } @media(--mobile){ grid-template-columns: 1fr; grid-template-rows: auto; }")],
    ["em-band-light"])

# ---------------- 4. SERVICE EXPLORER ----------------
def explorer(prefix):
    tabs, panels = [], []
    for i, s in enumerate(S):
        n = f"{prefix} {i+1}"
        tabs.append(e("e-tab", n + " Tab", [P(b, n + " TabT", f"<b>{s['name']}</b><br><span>{s['feats'][0][0]} · {s['feats'][1][0]}</span>",
                                              "font-size: 17px; color: #FFFFFF; line-height: 1.35;")],
                      style="width: 100%; padding: 16px 18px; border: 1px solid rgba(255,255,255,0.12); background: rgba(255,255,255,0.03); &:hover { background: rgba(255,255,255,0.08); }",
                      classes=["em-tab"]))
        feats = [flex(b, f"{n} F{j}", [icon(b, f"{n} F{j} I", "check", 14, "#FF8A1F", style="margin-top: 5px;"),
                                       P(b, f"{n} F{j} T", f[0], "color: #FFFFFF; font-weight: 600; font-size: 15px;")], "gap: 10px; align-items: flex-start;") for j, f in enumerate(s["feats"])]
        panels.append(e("e-tab-content", n + " Panel", [col(b, n + " Card", [
            img_el(b, n + " Bg", dkey(s["img"]), "", "", ["em-panel-bg"]),
            flex(b, n + " Shade", [], "position: absolute; left: 0px; top: 0px; width: 100%; height: 100%; z-index: -1; background: linear-gradient(180deg, rgba(7,18,51,0.15) 0%, rgba(7,18,51,0.7) 42%, rgba(4,11,34,0.97) 78%);"),
            col(b, n + " In", [
                P(b, n + " K", f"SERVICE 0{i+1} / 06", "font-family: var(--em-mono); font-size: 12px; color: #7AF0F5; letter-spacing: 0.12em;"),
                H(b, n + " H", s["head"], "h3", "color: #FFFFFF; font-size: 32px; @media(--mobile){ font-size: 26px; }"),
                P(b, n + " P", s["intro"], "color: rgba(255,255,255,0.8); max-width: 560px;"),
                e("e-grid", n + " Feats", feats, style="grid-template-columns: 1fr 1fr; grid-template-rows: auto auto; gap: 10px 18px; padding: 0px; @media(--mobile){ grid-template-columns: 1fr; grid-template-rows: auto; }"),
                flex(b, n + " Btns", [btn(b, n + " B1", "Full Details", link_page("services"), "w"), btn(b, n + " B2", "Free Audit", link_page("contact"), "o")], "gap: 10px; flex-wrap: wrap;")],
                "gap: 14px; padding: 30px; z-index: 1;")],
            "min-height: 520px; justify-content: flex-end; border-radius: 24px; border: 1px solid rgba(255,255,255,0.12); background: linear-gradient(180deg, rgba(7,18,51,0.1) 0%, rgba(7,18,51,0.65) 40%, rgba(4,11,34,0.97) 75%); isolation: isolate;",
            ["em-panel"])], style="padding: 0px;"))
    menu = e("e-tabs-menu", prefix + " Menu", tabs, style="flex-direction: column; gap: 8px; flex: 0 0 38%; @media(--tablet){ flex: 0 0 auto; width: 100%; }")
    area = e("e-tabs-content-area", prefix + " Area", panels, style="flex: 1 1 auto; min-width: 0px; padding: 0px;")
    return e("e-tabs", prefix, [menu, area], cfg={"default-active-tab": 0},
             style="flex-direction: row; gap: 24px; align-items: stretch; @media(--tablet){ flex-direction: column; }")
svc = section(b, "Services", [
    flex(b, "Svc Head Row", [head(b, "Svc Head", "Service Explorer", "Pick A Service, <strong>See The Plan</strong>", dark=True, style="margin-bottom: 0px; width: auto; flex: 1 1 auto;"),
                             btn(b, "Svc All", "All Services", link_page("services"), "w")],
         "justify-content: space-between; align-items: flex-end; gap: 24px; margin-bottom: 52px; flex-wrap: wrap;"),
    explorer("Explorer")],
    ["em-band-dark"], "background: radial-gradient(45% 60% at 100% 0%, rgba(31,107,224,0.4), transparent 70%), radial-gradient(35% 50% at 0% 100%, rgba(255,138,31,0.14), transparent 70%), #071233;")

# ---------------- 5. TICKER ----------------
WORDS = ["SEO That Ranks", "Local SEO & Maps", "Google Ads", "Website Development", "Social Media", "AI Search Optimization", "Free Growth Audit"]
def make_ticker(prefix="Ticker"):
    items = []
    for k in range(2):
        for i, w in enumerate(WORDS):
            items.append(P(b, f"{prefix} {k} {i}", w.upper(), "font-size: 30px; font-weight: 800; color: #FFFFFF; line-height: 1; @media(--mobile){ font-size: 20px; }"))
            items.append(P(b, f"{prefix} {k} {i} Sep", "■", "font-size: 14px; color: #FF8A1F;"))
    return flex(b, prefix, [flex(b, prefix + " Track", items, "", ["em-ticker-track"])], "padding: 34px 0px; border-top: 1px solid rgba(255,255,255,0.12); border-bottom: 1px solid rgba(255,255,255,0.12); @media(--mobile){ padding: 24px 0px; }", ["em-ticker"])
ticker = make_ticker()

# ---------------- 6. AUDIT FORM ----------------
def gets(cid, ic, t, s, hot=False):
    return flex(b, cid, [ico_tile(b, cid + " I", ic, hot, False, 44),
                         col(b, cid + " Tx", [P(b, cid + " T", t, "font-weight: 800; color: #0C1530; line-height: 1.3;"), P(b, cid + " S", s, "font-size: 14px; color: #5B6683;")], "gap: 2px;")],
                "gap: 14px; align-items: center; padding: 12px 14px; border-radius: 16px; background: rgba(255,255,255,0.7); border: 1px solid #D3E3FB;")
def field(cid, fid, label, kind, ph, full=False, req=False):
    inner = [e("e-form-label", cid + " L", cfg={"text": label, "input-id": fid}, classes=["em-label"])]
    if kind == "textarea":
        inner.append(e("e-form-textarea", cid + " F", cfg={"placeholder": ph, "rows": 4, "required": req}, style="min-height: 110px;", classes=["em-input"]))
    elif kind == "select":
        opts = [{"key": "Select a service", "value": "Select a service"}] + [{"key": s["name"], "value": s["name"]} for s in S] + [{"key": "Not sure yet", "value": "Not sure yet"}]
        inner.append(e("e-form-select", cid + " F", cfg={"name": "service", "options": opts}, classes=["em-input"]))
    else:
        inner.append(e("e-form-input", cid + " F", cfg={"placeholder": ph, "type": kind, "required": req, "_cssid": fid}, classes=["em-input"]))
    return e("e-div-block", cid, inner, style="display: flex; flex-direction: column; gap: 8px; padding: 0px; " + ("flex: 1 1 100%;" if full else "flex: 1 1 calc(50% - 8px); min-width: 220px;"))
def audit_form(cid, title, sub, button):
    kids = [field(cid + " Name", cid.lower().replace(" ", "-") + "-name", "Full name", "text", "Your name", req=True),
            field(cid + " Email", cid.lower().replace(" ", "-") + "-email", "Email", "email", "you@company.com", req=True),
            field(cid + " Phone", cid.lower().replace(" ", "-") + "-phone", "Phone", "tel", "+1 ..."),
            field(cid + " Web", cid.lower().replace(" ", "-") + "-web", "Website", "url", "https://"),
            field(cid + " Svc", cid.lower().replace(" ", "-") + "-svc", "Service needed", "select", "", full=True),
            field(cid + " Msg", cid.lower().replace(" ", "-") + "-msg", "What do you want more of?", "textarea", "Calls, form leads, online sales, map rankings…", full=True),
            e("e-form-submit-button", cid + " Submit", cfg={"text": button}, classes=["em-btn", "em-btn-g"], style="margin-top: 4px;"),
            e("e-form-success-message", cid + " Ok", [P(b, cid + " OkT", "Thanks! Your request has been sent. We reply within one business day.", "font-size: 14.5px; color: #0C1530;")],
              style="flex: 1 1 100%; border-radius: 12px; background: #E3F3FF; padding: 14px;"),
            e("e-form-error-message", cid + " Err", [P(b, cid + " ErrT", f"Sorry, something went wrong. Please call {PHONE} or email {EMAIL}.", "font-size: 14.5px; color: #8A2A0F;")],
              style="flex: 1 1 100%; border-radius: 12px; background: #FFF1E6; padding: 14px;")]
    frm = e("e-form", cid + " Form", kids, cfg={"form-name": title, "actions-after-submit": ["email"],
                                                 "email": {"to": [EMAIL], "subject": f"New request from emmenntech.com: {title}", "reply-to": "", "from-name": "EmmEnn Tech Website"}},
            style="align-items: flex-start;", classes=["em-form"])
    return col(b, cid, [H(b, cid + " H", title, "h3", "font-size: 26px;"), P(b, cid + " Sub", sub, "font-size: 14.5px; color: #5B6683; margin-top: -6px;"), frm],
               "gap: 16px; padding: 32px; border-radius: 26px; background: #FFFFFF; border: 1px solid #D3E3FB; box-shadow: 0 30px 70px -36px rgba(7,18,51,0.45); @media(--mobile){ padding: 22px; }")
audit_l = col(b, "Audit L", [
    eyebrow(b, "Audit Eb", "Free Growth Audit"),
    H(b, "Audit H", "Get Your Free <strong>Growth Map</strong> In 48 Hours", "h2", None, ["em-h2"]),
    P(b, "Audit P", "Tell us about your business. We review your website, Google profile and competitors, then send a clear plan.", None, ["em-lead"]),
    col(b, "Audit Photo", [img_el(b, "Audit Photo Img", "local-seo-google-maps", "width: 100%; aspect-ratio: 16 / 7; object-fit: cover;", "Map planning"),
                           flex(b, "Audit Photo Tag", [icon(b, "Audit Tag I", "location-dot", 14, "#FF8A1F"), P(b, "Audit Tag T", "Your growth map", "font-weight: 800; color: #0C1530; font-size: 14px;")],
                                "position: absolute; left: 16px; top: 16px; gap: 8px; align-items: center; padding: 8px 14px; border-radius: 50px; background: #FFFFFF; width: auto; z-index: 2;")],
        "position: relative; border-radius: 20px; overflow: hidden;"),
    gets("Audit G1", "magnifying-glass-chart", "SEO & Google visibility check", "Where you rank today and the quickest wins."),
    gets("Audit G2", "location-dot", "Google Business Profile review", "What's stopping you from the map pack.", True),
    gets("Audit G3", "display", "Website conversion notes", "Fixes that turn visitors into calls.")],
    "gap: 16px; flex: 1 1 45%;")
audit = section(b, "Audit", [flex(b, "Audit Grid", [audit_l, col(b, "Audit R", [audit_form("Audit Card", "Request Your Free Audit", "We reply within one business day.", "Send Request")], "flex: 1 1 55%;")],
                                  "gap: 56px; align-items: center; @media(--tablet){ flex-direction: column; align-items: stretch; gap: 36px; }")],
                style="background: linear-gradient(120deg, #E3F3FF 0%, #F2F7FF 50%, #FFF0E4 100%);")

# ---------------- 7. VIDEO REVIEWS ----------------
def videos(prefix):
    V = C["VIDS"]; tabs, panels = [], []
    for i, v in enumerate(V):
        n = f"{prefix} {i+1}"
        t = v["t"].replace("“", "").replace("”", "")
        thumb = flex(b, n + " Th", [b.el("e-image", n + " ThImg", cfg={"image": {"src": {"url": f"https://i.ytimg.com/vi/{v['id']}/hqdefault.jpg", "alt": ""}, "size": "full"}},
                                         style="position: absolute; left: 0px; top: 0px; width: 100%; height: 100%; object-fit: cover;"),
                                    flex(b, n + " ThPlay", [icon(b, n + " ThPlayI", "play", 14, "#FFFFFF", style="margin-left: 3px;")],
                                         "position: absolute; left: calc(50% - 18px); top: calc(50% - 18px); width: 36px; height: 36px; border-radius: 50%; align-items: center; justify-content: center; background: linear-gradient(90deg, #FFA53D, #FF5F3A); z-index: 2;")],
                     "position: relative; flex: 0 0 132px; width: 132px; aspect-ratio: 16 / 10; border-radius: 12px; overflow: hidden; background: #0C1530; @media(--mobile){ flex: 0 0 104px; width: 104px; }")
        tabs.append(e("e-tab", n + " Tab", [flex(b, n + " TabRow", [thumb, P(b, n + " TabT", f"<span>0{i+1} · {v['s']}</span><br><b>{t}</b>", "font-size: 15.5px; color: #FFFFFF; line-height: 1.35; flex: 1 1 0%; min-width: 0px; white-space: normal;")], "gap: 14px; align-items: center; width: 100%;")],
                      style="width: 100%; padding: 10px; border: 1px solid rgba(255,255,255,0.12); background: rgba(255,255,255,0.04); &:hover { background: rgba(255,255,255,0.08); }",
                      classes=["em-vtab"]))
        panels.append(e("e-tab-content", n + " Panel", [b.el("e-youtube", n + " Video", cfg={"source": f"https://www.youtube.com/watch?v={v['id']}", "player_controls": True, "privacy_mode": True, "lazyload": True, "rel": False},
                                                             style="width: 100%; aspect-ratio: 16 / 9; border-radius: 24px; border: 1px solid rgba(122,240,245,0.25);")], style="padding: 0px;"))
    menu = e("e-tabs-menu", prefix + " Menu", tabs, style="flex-direction: column; gap: 12px; flex: 0 0 34%; @media(--tablet){ flex: 0 0 auto; width: 100%; }")
    area = e("e-tabs-content-area", prefix + " Area", panels, style="flex: 1 1 auto; min-width: 0px; padding: 0px;")
    return e("e-tabs", prefix, [area, menu], cfg={"default-active-tab": 0}, style="flex-direction: row; gap: 22px; align-items: flex-start; @media(--tablet){ flex-direction: column; }")
vid = section(b, "Videos", [
    flex(b, "Vid Head Row", [head(b, "Vid Head", "Video Reviews", "Hear It Straight From <strong>Our Clients</strong>", dark=True, style="margin-bottom: 0px; width: auto; flex: 1 1 auto;"),
                             P(b, "Vid Note", "Pick a review from the playlist and press play.", "color: rgba(255,255,255,0.7); max-width: 320px;")],
         "justify-content: space-between; align-items: flex-end; gap: 24px; margin-bottom: 52px; flex-wrap: wrap;"),
    videos("Player")],
    ["em-band-dark"], "background: radial-gradient(50% 70% at 0% 0%, rgba(31,107,224,0.35), transparent 70%), radial-gradient(40% 60% at 100% 100%, rgba(255,138,31,0.16), transparent 70%), #040B22;")

# ---------------- 8. REVIEWS WALL ----------------
score = col(b, "Score", [
    eyebrow(b, "Score Eb", "Client Rating", True),
    P(b, "Score N", "5.0", "font-family: var(--em-num); font-size: 64px; font-weight: 700; color: #FFFFFF; line-height: 1;"),
    P(b, "Score Stars", "★★★★★", "font-size: 22px; letter-spacing: 3px; color: #FFB547;"),
    P(b, "Score P", "Average across our written and video reviews.", "color: rgba(255,255,255,0.75);")],
    "gap: 12px; padding: 28px; border-radius: 22px; background: #071233; break-inside: avoid; margin-bottom: 18px;")
wphoto = col(b, "Wall Photo", [img_el(b, "Wall Photo Img", "small-business-owner", "width: 100%; aspect-ratio: 4 / 3.2; object-fit: cover;", "Business owner serving a customer"),
                               P(b, "Wall Photo T", "Real businesses, real results", "position: absolute; left: 14px; bottom: 14px; padding: 8px 14px; border-radius: 50px; background: #FFFFFF; font-weight: 800; font-size: 14px; color: #0C1530;")],
             "position: relative; border-radius: 22px; overflow: hidden; break-inside: avoid; margin-bottom: 18px;")
cards = [score, wphoto]
for i, (q, loc) in enumerate([t for t in C["TST"] if t[1] not in ("London, UK", "Denver, USA")]):
    n = f"Rev {i+1}"
    ini = "".join(w[0] for w in loc.split(",")[0].split())[:2]
    cards.append(col(b, n, [
        P(b, n + " Q", "“", "font-size: 54px; font-weight: 900; line-height: 0.6; height: 26px; color: #FF8A1F;"),
        P(b, n + " T", q, "font-size: 16px; color: #2B3550;"),
        flex(b, n + " Who", [flex(b, n + " Av", [P(b, n + " AvT", ini, "font-weight: 800; color: #FFFFFF; font-size: 14px;")],
                                  "flex: 0 0 42px; width: 42px; height: 42px; border-radius: 12px; align-items: center; justify-content: center; background: linear-gradient(135deg, #22C6E0, #1F6BE0);"),
                             col(b, n + " Nm", [P(b, n + " N", "Verified Client", "font-weight: 800; color: #0C1530;"),
                                                P(b, n + " L", loc, "font-family: var(--em-mono); font-size: 12px; color: #5B6683;")], "gap: 2px; flex: 1 1 auto;"),
                             P(b, n + " S", "★★★★★", "font-size: 13px; color: #FF8A1F; letter-spacing: 1px;")],
             "gap: 12px; align-items: center; padding-top: 14px; border-top: 1px dashed #D3E3FB;")],
        "gap: 14px; padding: 24px; break-inside: avoid; margin-bottom: 18px;", ["em-card", "em-lift"]))
wall = section(b, "Wall", [head(b, "Wall Head", "Testimonials", "What Clients Say <strong>In Writing</strong>", center=True),
                           e("e-div-block", "Wall Cols", cards, style="display: block; column-count: 3; column-gap: 18px; padding: 0px; @media(--tablet){ column-count: 2; } @media(--mobile){ column-count: 1; }")])

# ---------------- 9. COMPARE ----------------
rows = [e("e-grid", "Cmp Top", [P(b, "Cmp Top L", "", ""),
                                flex(b, "Cmp Top Us", [img_el(b, "Cmp Top Logo", "icon", "width: 22px;"), P(b, "Cmp Top UsT", "EMMENN TECH", "font-family: var(--em-mono); font-size: 12.5px; letter-spacing: 0.1em; color: #FFFFFF;")],
                                     "gap: 10px; align-items: center; padding: 20px 24px; background: linear-gradient(90deg, #22C6E0, #1F6BE0);"),
                                P(b, "Cmp Top Them", "TYPICAL AGENCY", "font-family: var(--em-mono); font-size: 12.5px; letter-spacing: 0.1em; color: rgba(255,255,255,0.6); padding: 20px 24px;")],
          style="grid-template-columns: 1.1fr 1.3fr 1.1fr; grid-template-rows: auto; gap: 0px; padding: 0px; background: #071233; align-items: center; @media(--mobile){ grid-template-columns: 1fr 1fr; } ")]
for i, (lbl, us, them) in enumerate(C["COMPARE"]):
    n = f"Cmp {i+1}"
    rows.append(e("e-grid", n, [
        P(b, n + " L", lbl, "font-weight: 800; color: #0C1530; padding: 18px 24px; @media(--mobile){ grid-column: 1 / -1; padding-bottom: 0px; }"),
        flex(b, n + " Us", [flex(b, n + " UsI", [icon(b, n + " UsIS", "check", 11, "#FFFFFF")], "flex: 0 0 22px; width: 22px; height: 22px; border-radius: 50%; background: linear-gradient(90deg, #22C6E0, #1F6BE0); align-items: center; justify-content: center;"),
                            P(b, n + " UsT", us, "font-weight: 700; color: #0C1530;")], "gap: 10px; align-items: center; padding: 18px 24px; height: 100%; background: linear-gradient(90deg, rgba(34,198,224,0.1), rgba(31,107,224,0.1));"),
        flex(b, n + " Th", [flex(b, n + " ThI", [icon(b, n + " ThIS", "xmark", 11, "#D2502B")], "flex: 0 0 22px; width: 22px; height: 22px; border-radius: 50%; background: #FBE3DA; align-items: center; justify-content: center;"),
                            P(b, n + " ThT", them, "color: #5B6683;")], "gap: 10px; align-items: center; padding: 18px 24px;")],
        style="grid-template-columns: 1.1fr 1.3fr 1.1fr; grid-template-rows: auto; gap: 0px; padding: 0px; align-items: center; border-top: 1px solid #D3E3FB; @media(--mobile){ grid-template-columns: 1fr 1fr; grid-template-rows: auto auto; }"))
table = col(b, "Cmp Table", rows, "border-radius: 24px; overflow: hidden; border: 1px solid #D3E3FB; background: #FFFFFF; box-shadow: 0 30px 60px -40px rgba(7,18,51,0.5); flex: 1 1 62%; min-width: 0px;")
cphoto = col(b, "Cmp Photo", [img_el(b, "Cmp Photo Img", "client-report-review", "", "EmmEnn Tech strategist reviewing a client report"),
                              col(b, "Cmp Photo Cap", [P(b, "Cmp Cap T", "Same team, start to finish", "font-size: 20px; font-weight: 800; color: #FFFFFF;"),
                                                       P(b, "Cmp Cap S", "You talk to the people doing the work.", "font-size: 14.5px; color: rgba(255,255,255,0.8);")],
                                  "position: absolute; left: 20px; right: 20px; bottom: 18px; gap: 4px; z-index: 2;")],
              "flex: 0 0 34%; min-height: 360px; border-radius: 24px; background: linear-gradient(180deg, transparent 45%, rgba(4,11,34,0.9)); @media(--tablet){ flex: 0 0 auto; min-height: 260px; }",
              ["em-tile-photo"])
compare = section(b, "Compare", [head(b, "Cmp Head", "Why EmmEnn Tech", "Us vs. The <strong>Typical Agency</strong>", center=True),
                                 flex(b, "Cmp Grid", [cphoto, table], "gap: 20px; align-items: stretch; @media(--tablet){ flex-direction: column; }")], ["em-band-light"])

if __name__ == '__main__' or True:
  root = col(b, "Home", [hero, route, bento, svc, ticker, audit, vid, wall, compare, faq_chat(b, "FAQ"), cta(b, "CTA")], "gap: 0px; width: 100%;")
  json.dump(b.payload(PAGES["home"], root), open('/tmp/p_home.json', 'w'))
