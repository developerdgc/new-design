"""Inner pages: python3 b_pages.py <about|services|blog|contact|post0..post5>"""
import json, sys
from blocks import *
import comps

b = B(); e = b.el
HM = comps.use(b)
S = C["SVC"]
which = sys.argv[1]
def post_link(i): return {"destination": {"id": PAGES["posts"][i]}, "tag": "a"}

# ---------- ABOUT ----------
def about():
    ban = banner(b, "Banner", "About Us", "We Build Tech Solutions <strong>That Work</strong>",
                 "No buzzwords. No fluff. Just SEO, ads, local search and websites that bring in customers, explained in plain language.",
                 "about-team-office", "strategy-meeting", "Since 2021", "EmmEnn Group LLC",
                 flex(b, "Banner Btns", [btn(b, "Banner B1", "Schedule Strategy Call", link_page("contact"), "g")], "gap: 12px;"))
    intro = col(b, "Story", [eyebrow(b, "Story Eb", "Our Story"),
        H(b, "Story H", "Straightforward Marketing For <strong>Growing Businesses</strong>", "h2", None, ["em-h2"]),
        P(b, "Story P1", "EmmEnn Tech provides SEO, local SEO, paid advertising, website development, social media marketing, and AI search optimization for businesses looking to improve their online visibility and generate more leads."),
        P(b, "Story P2", "We start by understanding your business, goals, customers, and current online presence, then focus on the work that actually improves visibility, website performance and lead generation.")],
        "gap: 18px; padding: 32px; grid-row: span 2; @media(--tablet){ grid-column: 1 / -1; grid-row: auto; } @media(--mobile){ padding: 24px; }", ["em-card"])
    photo = col(b, "Story Photo", [img_el(b, "Story Photo Img", "about-team-office", "", "EmmEnn Tech team"),
        flex(b, "Story Lbl", [ico_tile(b, "Story Lbl I", "location-dot", False, False, 38, 18),
                              col(b, "Story Lbl Tx", [P(b, "Story Lbl T", "1500 N Grant St", "font-weight: 700; color: #FFFFFF; line-height: 1.2;"),
                                                      P(b, "Story Lbl S", "Denver, CO 80203", "font-family: var(--em-mono); font-size: 11px; color: #7AF0F5;")], "gap: 2px;")],
             "position: absolute; left: 14px; right: 14px; bottom: 14px; gap: 12px; align-items: center; padding: 14px 16px; border-radius: 14px; background: rgba(7,18,51,0.82); z-index: 2;")],
        "grid-row: span 2; min-height: 420px; border-radius: 22px; @media(--mobile){ grid-row: auto; min-height: 320px; }", ["em-tile-photo"])
    def stat(cid, n, l, st):
        return col(b, cid, [P(b, cid + " N", n, "font-family: var(--em-num); font-size: 62px; font-weight: 700; line-height: 1; color: #FFFFFF;"),
                            P(b, cid + " L", l, "font-weight: 700; color: rgba(255,255,255,0.75);")], "gap: 6px; justify-content: flex-end; min-height: 170px; padding: 28px; border-radius: 22px; " + st)
    bento = section(b, "Story Sec", [e("e-grid", "Story Grid", [intro, photo,
        stat("Story S1", "5+", "Years of experience", "background: #071233;"),
        stat("Story S2", "10+", "Core services", f"background: linear-gradient(160deg, rgba(34,198,224,0.82), rgba(31,107,224,0.92)), {bg('client-report-review')} center / cover no-repeat;")],
        style="grid-template-columns: 1.25fr 0.85fr 0.9fr; grid-template-rows: auto auto; gap: 16px; padding: 0px; @media(--tablet){ grid-template-columns: 1fr 1fr; grid-template-rows: auto auto auto; } @media(--mobile){ grid-template-columns: 1fr; grid-template-rows: auto; }")], ["em-band-light"])
    def mv(cid, name, eb, t, p, dark):
        return flex(b, cid, [
            flex(b, cid + " Circ", [img_el(b, cid + " Img", name, "width: 100%; height: 100%; object-fit: cover;")],
                 "flex: 0 0 130px; width: 130px; height: 130px; border-radius: 50%; overflow: hidden; box-shadow: 0 0 0 6px rgba(63,208,222,0.35);"),
            col(b, cid + " T", [eyebrow(b, cid + " Eb", eb, dark), H(b, cid + " H", t, "h3", "font-size: 26px;" + (" color: #FFFFFF;" if dark else "")),
                                P(b, cid + " P", p, "color: rgba(255,255,255,0.75);" if dark else "color: #5B6683;")], "gap: 10px; flex: 1 1 auto;")],
            "gap: 22px; align-items: center; padding: 32px; border-radius: 26px; " + ("background: #071233;" if dark else "background: #FFFFFF; border: 1px solid #D3E3FB;") + " @media(--mobile){ flex-direction: column; align-items: flex-start; }")
    mvs = section(b, "MV", [e("e-grid", "MV Grid", [
        mv("MV 1", "client-success", "Mission", "Help Businesses Win Online", "Build a stronger online presence and generate more customers through digital marketing and technology.", False),
        mv("MV 2", "planning-whiteboard", "Vision", "Marketing You Can Understand", "Clear about what you're paying for, what work is being done, and what results it brings.", True)],
        style="grid-template-columns: 1fr 1fr; grid-template-rows: auto; gap: 22px; padding: 0px; @media(--tablet){ grid-template-columns: 1fr; }")])
    TL = [("2021", "EmmEnn Group LLC Founded", "Started in Denver, Colorado with SEO and website work for local businesses."),
          ("GROWTH", "100+ Projects Delivered", "Websites, landing pages and SEO campaigns across service businesses."),
          ("RETAINERS", "170+ Monthly Clients", "Ongoing SEO, Google Ads and local search on transparent monthly plans."),
          ("TODAY", "AI Search Optimization", "Helping clients show up in Google AI features and AI answer engines.")]
    stops = []
    for i, (yr, t, p) in enumerate(TL):
        n = f"TL {i+1}"
        stops.append(flex(b, n, [
            flex(b, n + " Dot", [], "flex: 0 0 18px; width: 18px; height: 18px; border-radius: 5px; margin-top: 26px; background: " + ("linear-gradient(90deg, #FFA53D, #FF5F3A)" if i == 3 else "linear-gradient(90deg, #22C6E0, #1F6BE0)") + "; box-shadow: 0 0 0 6px #EEF5FF;"),
            col(b, n + " Card", [P(b, n + " Y", yr, "font-family: var(--em-mono); font-size: 14px; font-weight: 700; color: #FF8A1F;"), H(b, n + " H", t, "h3", "font-size: 22px;"),
                                 P(b, n + " P", p, "color: #5B6683;")], "gap: 8px; padding: 22px 24px; flex: 1 1 auto;", ["em-card", "em-lift"])],
            "gap: 22px; align-items: flex-start;"))
    tl = section(b, "Journey", [head(b, "TL Head", "Our Journey", "The Route <strong>So Far</strong>", center=True),
                                col(b, "TL List", stops, "gap: 22px; max-width: 820px; width: 100%; align-self: center; border-left: 2px solid #B8CCEE; padding-left: 0px; margin-left: 8px;")], ["em-band-light"])
    vids = section(b, "Videos", [head(b, "Vid Head", "Video Reviews", "What Our <strong>Clients Say</strong>", dark=True), HM.videos("About Player")],
                   ["em-band-dark"], "background: radial-gradient(50% 70% at 0% 0%, rgba(31,107,224,0.35), transparent 70%), #040B22;")
    return [ban, HM.make_ticker("Ab Ticker"), bento, mvs, tl, vids, faq_chat(b, "FAQ"), cta(b, "CTA")]

# ---------- SERVICES ----------
def services():
    ban = banner(b, "Banner", "Our Services", "Comprehensive Digital <strong>Growth Solutions</strong>",
                 "We combine SEO, web development, paid advertising, and AI search optimization to help businesses improve their online visibility, generate qualified leads, and reach more customers.",
                 "services-banner", "seo-services", "6 core services", "One team, every channel",
                 flex(b, "Banner Btns", [btn(b, "Banner B1", "Get a Free Audit", link_page("contact"), "g")], "gap: 12px;"))
    exp = section(b, "Explorer Sec", [head(b, "Exp Head", "Service Explorer", "Pick A Service, <strong>See The Plan</strong>", dark=True), HM.explorer("Svc Explorer")],
                  ["em-band-dark"], "background: radial-gradient(45% 60% at 100% 0%, rgba(31,107,224,0.4), transparent 70%), #071233;")
    rows = []
    for i, s in enumerate(S):
        n = f"Row {i+1}"
        pic = col(b, n + " Pic", [img_el(b, n + " Img", dkey(s["img"]), "", s["name"]),
                                  flex(b, n + " IcoW", [ico_tile(b, n + " Ico", SVC_ICON[s["id"]], i % 2 == 1)], "position: absolute; left: 18px; top: 18px; z-index: 2; width: auto;")],
                  "flex: 0 0 42%; min-height: 460px; border-radius: 26px; @media(--tablet){ flex: 0 0 auto; width: 100%; min-height: 300px; }", ["em-tile-photo"])
        feats = [col(b, f"{n} F{j}", [P(b, f"{n} F{j} T", f[0], "font-weight: 800; color: #0C1530;"), P(b, f"{n} F{j} P", f[1], "font-size: 14.5px; color: #5B6683;")],
                     "gap: 4px; padding: 16px; border-radius: 16px; background: #F5F9FF; border: 1px solid #D3E3FB;") for j, f in enumerate(s["feats"])]
        probs = [P(b, f"{n} Pr{j}", p, "padding: 8px 14px; border-radius: 50px; background: #FFF1E6; color: #B4511A; font-weight: 700; font-size: 14px;") for j, p in enumerate(s["probs"])]
        txt = col(b, n + " Txt", [
            P(b, n + " Idx", f"SERVICE 0{i+1}", "font-family: var(--em-mono); font-size: 13px; color: #FF8A1F; letter-spacing: 0.2em;"),
            eyebrow(b, n + " Eb", s["name"]), H(b, n + " H", s["head"], "h2", None, ["em-h2"]), P(b, n + " P", s["intro"], None, ["em-lead"]),
            e("e-grid", n + " Feats", feats, style="grid-template-columns: 1fr 1fr; grid-template-rows: auto auto; gap: 12px; padding: 0px; @media(--mobile){ grid-template-columns: 1fr; grid-template-rows: auto; }"),
            P(b, n + " PrT", "Problems we solve", "font-weight: 800; color: #0C1530;"),
            flex(b, n + " Probs", probs, "gap: 8px; flex-wrap: wrap;"),
            btn(b, n + " Btn", f"Get a Free {s['name']} Audit", link_page("contact"), "g")],
            "gap: 16px; flex: 1 1 auto; align-items: flex-start;")
        kids = [txt, pic] if i % 2 else [pic, txt]
        rows.append(flex(b, n, kids, "gap: 56px; align-items: center; @media(--tablet){ flex-direction: column; align-items: flex-start; gap: 28px; }"))
    detail = section(b, "Details", [col(b, "Details List", rows, "gap: 96px; @media(--mobile){ gap: 64px; }")])
    # process route
    stops = []
    for i, (t, p) in enumerate(C["STEPS"]):
        n = f"Stop {i+1}"
        stops.append(col(b, n, [
            flex(b, n + " Pin", [P(b, n + " PinT", str(i + 1), "font-family: var(--em-num); font-weight: 700; font-size: 20px; color: #FFFFFF;")],
                 "flex: 0 0 56px; width: 56px; height: 56px; border-radius: 50% 50% 50% 6px; align-items: center; justify-content: center; background: " + ("linear-gradient(90deg, #FFA53D, #FF5F3A)" if i % 2 else "linear-gradient(90deg, #22C6E0, #1F6BE0)") + ";"),
            col(b, n + " Card", [P(b, n + " K", f"STOP 0{i+1}", "font-family: var(--em-mono); font-size: 11.5px; color: #1F6BE0; letter-spacing: 0.08em;"),
                                 H(b, n + " H", t, "h3", "font-size: 22px;"), P(b, n + " P", p, "font-size: 15px; color: #5B6683;")], "gap: 8px; padding: 20px 22px;", ["em-card", "em-lift"])],
            "gap: 12px; " + ("margin-top: 90px; @media(--tablet){ margin-top: 0px; }" if i % 2 else "")))
    route = section(b, "Process", [head(b, "Proc Head", "How We Work", "A Clear Route, <strong>Four Stops</strong>", "No guesswork. You always know where your campaign is and what happens next.", center=True),
                                   e("e-grid", "Proc Grid", stops, style="grid-template-columns: repeat(4, 1fr); grid-template-rows: auto; gap: 24px; padding: 0px; @media(--tablet){ grid-template-columns: 1fr 1fr; } @media(--mobile){ grid-template-columns: 1fr; }")],
                    ["em-band-light"])
    # platforms orbit (static rings + chips)
    plat = C["PLAT"]
    chips = []
    pos = [(50, 0), (100, 50), (50, 100), (0, 50), (85, 15), (85, 85), (15, 85), (15, 15)]
    for i, p in enumerate(plat):
        x, y = pos[i]
        chips.append(flex(b, f"Orb {i}", [P(b, f"Orb {i} T", p[0], "font-family: var(--em-num); font-weight: 700; font-size: 14px; color: #0C1530;")],
                          f"position: absolute; left: calc({x}% - 29px); top: calc({y}% - 29px); width: 58px; height: 58px; border-radius: 16px; background: #FFFFFF; border: 1px solid #D3E3FB; align-items: center; justify-content: center; box-shadow: 0 14px 26px -16px rgba(7,18,51,0.6); z-index: 2;"))
    orbit = col(b, "Orbit", [
        flex(b, "Orbit R1", [], "position: absolute; left: 0%; top: 0%; width: 100%; height: 100%; border: 1.5px dashed #B8CCEE; border-radius: 50%;", ["em-ring-rev"]),
        flex(b, "Orbit R2", [], "position: absolute; left: 18%; top: 18%; width: 64%; height: 64%; border: 1.5px dashed #B8CCEE; border-radius: 50%;", ["em-ring"]),
        flex(b, "Orbit Core", [flex(b, "Orbit LogoW", [img_el(b, "Orbit Logo", "icon", "width: 100%;", "EmmEnn Tech")], "width: 64px; height: 64px; padding: 0px;")],
             "position: absolute; left: 36%; top: 36%; width: 28%; height: 28%; padding: 0px; border-radius: 50%; background: #FFFFFF; border: 1px solid #D3E3FB; align-items: center; justify-content: center; box-shadow: 0 0 0 14px rgba(31,107,224,0.08), 0 20px 40px -20px rgba(7,18,51,0.5);")] + chips,
        "position: relative; flex: 0 0 440px; width: 440px; height: 440px; @media(--mobile){ flex: 0 0 280px; width: 280px; height: 280px; align-self: center; }")
    plist = [flex(b, f"Pl {i}", [ico_tile(b, f"Pl {i} I", "plug", i % 3 == 1, False, 40, 16),
                                 col(b, f"Pl {i} T", [P(b, f"Pl {i} N", p[1], "font-weight: 800; color: #0C1530;"), P(b, f"Pl {i} S", p[2], "font-size: 13px; color: #5B6683;")], "gap: 2px;")],
                  "gap: 12px; align-items: center; padding: 12px 14px; border-radius: 14px; background: #FFFFFF; border: 1px solid #D3E3FB;") for i, p in enumerate(plat)]
    plats = section(b, "Platforms", [flex(b, "Plat Grid", [orbit, col(b, "Plat R", [
        eyebrow(b, "Plat Eb", "Platforms"), H(b, "Plat H", "Everything Orbits <strong>Your Growth</strong>", "h2", None, ["em-h2"]),
        P(b, "Plat P", "We plug into the tools you already use and connect them, so every click, call and form is tracked back to its source.", None, ["em-lead"]),
        e("e-grid", "Plat List", plist, style="grid-template-columns: 1fr 1fr; grid-template-rows: auto; gap: 12px; padding: 0px; @media(--mobile){ grid-template-columns: 1fr; }")], "gap: 18px; flex: 1 1 auto;")],
        "gap: 60px; align-items: center; @media(--tablet){ flex-direction: column; gap: 40px; }")])
    return [ban, exp, HM.make_ticker("Svc Ticker"), detail, route, plats, faq_chat(b, "FAQ", light=True), cta(b, "CTA")]

# ---------- BLOG ----------
def post_card(i, p, prefix):
    n = f"{prefix} {i}"
    return col(b, n, [
        col(b, n + " Th", [img_el(b, n + " Img", dkey(p["img"]), "width: 100%; aspect-ratio: 16 / 10; object-fit: cover;", p["t"]),
                           P(b, n + " Cat", p["c"], "position: absolute; left: 14px; top: 14px; padding: 7px 14px; border-radius: 50px; background: #FFFFFF; font-family: var(--em-mono); font-size: 12px; color: #0C1530;")],
            "position: relative; overflow: hidden;", ["em-zoom"]),
        col(b, n + " In", [P(b, n + " M", f"{p['d']} · {p['m']} min read", "font-family: var(--em-mono); font-size: 12px; color: #5B6683;"),
                           H(b, n + " H", p["t"], "h3", "font-size: 20px; line-height: 1.3;"), P(b, n + " X", p["x"], "font-size: 15px; color: #5B6683;"),
                           P(b, n + " R", "Read article →", "font-weight: 800; color: #1F6BE0;")], "gap: 10px; padding: 20px 22px 24px 22px;")],
        "gap: 0px; border-radius: 24px; overflow: hidden; background: #FFFFFF; border: 1px solid #D3E3FB;", ["em-lift"], cfg={"link": post_link(i)})
def blog():
    ban = banner(b, "Banner", "Our Blog", "Field Notes For <strong>Growing Businesses</strong>",
                 "Practical guides on SEO, local search, Google Ads, websites and AI search. Written in plain language for business owners, not marketers.",
                 "contact-banner", "planning-whiteboard", "New posts monthly", "SEO · Ads · Local · AI")
    p0 = C["POSTS"][0]
    feat = flex(b, "Feat", [
        col(b, "Feat Img", [img_el(b, "Feat Img I", dkey(p0["img"]), "width: 100%; aspect-ratio: 16 / 10.5; object-fit: cover; border-radius: 20px;", p0["t"])], "flex: 1 1 55%;", ["em-zoom"]),
        col(b, "Feat Txt", [eyebrow(b, "Feat Eb", "Editor's Pick"), H(b, "Feat H", p0["t"], "h2", None, ["em-h2"]), P(b, "Feat X", p0["x"], None, ["em-lead"]),
                            P(b, "Feat M", f"{p0['d']} · {p0['m']} min read · EmmEnn Tech Team", "font-family: var(--em-mono); font-size: 12.5px; color: #5B6683;"),
                            btn(b, "Feat Btn", "Read Article", post_link(0), "g")], "gap: 16px; flex: 1 1 45%; padding: 10px 20px 10px 0px; @media(--tablet){ padding: 0px 8px 12px 8px; }")],
        "gap: 48px; align-items: center; padding: 16px; border-radius: 28px; background: #FFFFFF; border: 1px solid #D3E3FB; @media(--tablet){ flex-direction: column; gap: 20px; }")
    cats = ["All"] + list(dict.fromkeys(p["c"] for p in C["POSTS"]))
    tabs, panels = [], []
    for k, c in enumerate(cats):
        tabs.append(e("e-tab", f"BT {k}", [P(b, f"BT {k} T", c, "font-weight: 800; font-size: 15px; color: #0C1530;")],
                      style="width: auto; padding: 10px 20px; border-radius: 50px; border: 1px solid #D3E3FB; background: #FFFFFF;", classes=["em-btab"]))
        items = [post_card(i, p, f"BC{k}") for i, p in enumerate(C["POSTS"]) if c == "All" or p["c"] == c]
        panels.append(e("e-tab-content", f"BP {k}", [e("e-grid", f"BG {k}", items, style="grid-template-columns: repeat(3, 1fr); grid-template-rows: auto; gap: 22px; padding: 0px; @media(--tablet){ grid-template-columns: 1fr 1fr; } @media(--mobile){ grid-template-columns: 1fr; }")], style="padding: 0px;"))
    filt = e("e-tabs", "Blog Tabs", [e("e-tabs-menu", "Blog Menu", tabs, style="gap: 8px; flex-wrap: wrap; justify-content: center;"),
                                     e("e-tabs-content-area", "Blog Area", panels, style="padding: 0px;")], cfg={"default-active-tab": 0}, style="gap: 34px;")
    # newsletter band with a real form
    nl_form = e("e-form", "NL Form", [
        e("e-div-block", "NL Field", [e("e-form-input", "NL Input", cfg={"placeholder": "Your email address", "type": "email", "required": True, "_cssid": "nl-email"}, classes=["em-input"],
                                        style="background: rgba(255,255,255,0.08); border-color: rgba(255,255,255,0.18); color: #FFFFFF;")], style="flex: 1 1 260px; padding: 0px;"),
        e("e-form-submit-button", "NL Submit", cfg={"text": "Subscribe"}, classes=["em-btn", "em-btn-g"]),
        e("e-form-success-message", "NL Ok", [P(b, "NL OkT", "You're subscribed. Watch your inbox for next month's tip.", "font-size: 14px; color: #9CF3C9;")], style="flex: 1 1 100%; padding: 0px;"),
        e("e-form-error-message", "NL Err", [P(b, "NL ErrT", "Something went wrong. Please try again.", "font-size: 14px; color: #FFB08A;")], style="flex: 1 1 100%; padding: 0px;")],
        cfg={"form-name": "Newsletter", "actions-after-submit": ["email"], "email": {"to": [EMAIL], "subject": "New newsletter subscriber", "reply-to": "", "from-name": "EmmEnn Tech Website"}},
        style="gap: 10px; align-items: center; flex: 1 1 40%;", classes=["em-form"])
    nl = flex(b, "NL", [col(b, "NL Txt", [eyebrow(b, "NL Eb", "Newsletter", True), H(b, "NL H", "Get One Useful Tip <strong>Every Month</strong>", "h2", "color: #FFFFFF;", ["em-h2"]),
                                         P(b, "NL P", "SEO, Google Ads and local search ideas you can use the same day. No spam, unsubscribe anytime.", "color: rgba(255,255,255,0.75);")], "gap: 14px; flex: 1 1 55%;"),
                        nl_form], "gap: 32px; align-items: center; padding: 48px; border-radius: 28px; background: #071233; @media(--tablet){ flex-direction: column; align-items: stretch; padding: 32px; }", ["em-band-dark"])
    return [ban, HM.make_ticker("Blog Ticker"), section(b, "Feat Sec", [feat], ["em-band-light"]),
            section(b, "Posts", [head(b, "Posts Head", "Latest Articles", "Read, Learn, <strong>Grow</strong>", center=True), filt]),
            section(b, "NL Sec", [nl], ["em-band-light"]), cta(b, "CTA")]

# ---------- CONTACT ----------
def contact():
    ban = banner(b, "Banner", "Contact Us", "Let's Plot Your <strong>Next Move</strong>",
                 "Have a question, need technical support, or want to discuss a build? Send a message or contact us directly.",
                 "contact-banner", "client-success", "Reply in 1 business day", "Mon–Fri · 9–6 EST")
    def ci(cid, ic, lab, val, link=None, hot=False):
        return flex(b, cid, [ico_tile(b, cid + " I", ic, hot, False, 52),
                             col(b, cid + " T", [P(b, cid + " L", lab, "font-family: var(--em-mono); font-size: 11.5px; letter-spacing: 0.1em; text-transform: uppercase; color: #5B6683;"),
                                                 P(b, cid + " V", val, "font-weight: 800; font-size: 17px; color: #0C1530;", link=link)], "gap: 6px;")],
                    "gap: 16px; align-items: center; padding: 18px 20px; border-radius: 20px; background: #FFFFFF; border: 1px solid #D3E3FB;", ["em-lift"])
    lst = col(b, "CList", [ci("CI 1", "phone", "Call us", PHONE, link_url(TEL)), ci("CI 2", "envelope", "Email us", EMAIL, link_url(MAILTO), True),
                           ci("CI 3", "location-dot", "Visit us", "1500 N Grant St, Ste 76430, Denver, CO 80203"), ci("CI 4", "clock", "Office hours", "Mon–Fri, 9:00 AM – 6:00 PM EST", None, True)],
              "gap: 12px; flex: 1 1 40%;")
    mp = col(b, "Map", [
        img_el(b, "Map Dots", "world-map-dots-svg", "position: absolute; left: 4%; top: 6%; width: 92%; opacity: 0.55;", "World map"),
        flex(b, "Pin", [
            col(b, "HQ", [P(b, "HQ T", "EmmEnn Tech HQ", "font-weight: 800; color: #0C1530; font-size: 13.5px;"), P(b, "HQ S", "39.74° N, 104.99° W", "font-family: var(--em-mono); font-size: 10.5px; color: #1F6BE0;")],
                "position: absolute; left: -52px; bottom: 28px; width: 120px; padding: 8px 12px; border-radius: 12px; background: #FFFFFF; gap: 2px; box-shadow: 0 14px 30px -12px rgba(0,0,0,0.6);"),
            flex(b, "HQ Dot", [], "width: 16px; height: 16px; padding: 0px; border-radius: 50%; background: #FF8A1F;", ["em-hq-dot"])],
            "position: absolute; left: 22%; top: 34%; width: 16px; height: 16px; padding: 0px; z-index: 3;"),
        flex(b, "Map Cap", [P(b, "Map C1", "DENVER · COLORADO · USA", "font-family: var(--em-mono); font-size: 12px; color: rgba(255,255,255,0.65);"),
                            P(b, "Map C2", "SERVING US & UK CLIENTS", "font-family: var(--em-mono); font-size: 12px; color: rgba(255,255,255,0.65);")],
             "position: absolute; left: 20px; bottom: 18px; width: calc(100% - 40px); justify-content: space-between; gap: 12px; flex-wrap: wrap;")],
        "position: relative; flex: 1 1 60%; min-height: 380px; border-radius: 26px; overflow: hidden; background: #071233; @media(--tablet){ min-height: 300px; }")
    top = section(b, "Reach", [flex(b, "Reach Grid", [lst, mp], "gap: 22px; align-items: stretch; @media(--tablet){ flex-direction: column; }")])
    form_l = col(b, "Form L", [eyebrow(b, "Form Eb", "Book Free Consultation"), H(b, "Form H", "Three Steps To Your <strong>Growth Map</strong>", "h2", None, ["em-h2"]),
                               P(b, "Form P", "We'll look at your website, your Google profile and your competitors, and give you a clear plan in a free 30-minute call.", None, ["em-lead"]),
                               col(b, "Form Photo", [img_el(b, "Form Photo I", "client-success", "width: 100%; aspect-ratio: 16 / 9; object-fit: cover;", "EmmEnn Tech strategist with a client")],
                                   "border-radius: 20px; overflow: hidden;")], "gap: 16px; flex: 1 1 45%;")
    frm = HM.audit_form("Contact Card", "Book Free Consultation", "Tell us a little about your business.", "Book Free Consultation")
    form = section(b, "Form Sec", [flex(b, "Form Grid", [form_l, col(b, "Form R", [frm], "flex: 1 1 55%;")], "gap: 56px; align-items: center; @media(--tablet){ flex-direction: column; align-items: stretch; }")],
                   style="background: linear-gradient(120deg, #E3F3FF 0%, #F2F7FF 50%, #FFF0E4 100%);")
    return [ban, HM.make_ticker("Ct Ticker"), top, form, faq_chat(b, "FAQ")]

# ---------- POSTS ----------
def post(i):
    p = C["POSTS"][i]
    hero = flex(b, "Post Hero", [col(b, "Post Hero Wrap", [
        flex(b, "Post Crumb", [P(b, "PC1", "Home", "font-family: var(--em-mono); font-size: 13px; color: rgba(255,255,255,0.6);", link=link_page("home")),
                               P(b, "PC2", "/", "font-family: var(--em-mono); font-size: 13px; color: rgba(255,255,255,0.4);"),
                               P(b, "PC3", "Our Blog", "font-family: var(--em-mono); font-size: 13px; color: rgba(255,255,255,0.6);", link=link_page("blog")),
                               P(b, "PC4", "/", "font-family: var(--em-mono); font-size: 13px; color: rgba(255,255,255,0.4);"),
                               P(b, "PC5", p["c"], "font-family: var(--em-mono); font-size: 13px; color: #FF8A1F;")], "gap: 10px; flex-wrap: wrap;"),
        H(b, "Post Title", p["t"], "h1", "color: #FFFFFF; font-size: 56px; max-width: 900px; @media(--tablet){ font-size: 42px; } @media(--mobile){ font-size: 32px; }"),
        P(b, "Post Meta", f"{p['d']} · {p['m']} min read · EmmEnn Tech Team", "font-family: var(--em-mono); font-size: 13px; color: #7AF0F5;")], "gap: 18px;", ["em-wrap"])],
        "flex-direction: column; align-items: center; padding: 170px 24px 72px 24px; background: radial-gradient(40% 70% at 85% 40%, rgba(63,208,222,0.22), transparent 70%), #071233; @media(--mobile){ padding: 120px 16px 48px 16px; }", ["em-banner"])
    body = [img_el(b, "Post Cover", dkey(p["img"]), "width: 100%; aspect-ratio: 16 / 8; object-fit: cover; border-radius: 24px;", p["t"]),
            P(b, "Post Lead", p["x"], "font-size: 21px; font-weight: 700; color: #0C1530; line-height: 1.55;")]
    for j, para in enumerate(p["b"]):
        body.append(P(b, f"Post P{j}", para, "font-size: 18px; line-height: 1.75;"))
    body.append(flex(b, "Post CTA", [col(b, "Post CTA T", [H(b, "Post CTA H", "Want This Done For Your Business?", "h3", "color: #FFFFFF; font-size: 26px;"),
                                                          P(b, "Post CTA P", "Get a free audit of your website and Google presence.", "color: rgba(255,255,255,0.78);")], "gap: 6px; flex: 1 1 auto;"),
                                     btn(b, "Post CTA B", "Get a Free Audit", link_page("contact"), "g")],
                     "gap: 20px; align-items: center; padding: 28px; border-radius: 22px; background: #071233; margin-top: 12px; @media(--mobile){ flex-direction: column; align-items: flex-start; }"))
    art = section(b, "Article", [col(b, "Article Col", body, "gap: 22px; max-width: 820px; width: 100%; align-self: center;")])
    more = [post_card(k, C["POSTS"][k], "More") for k in range(6) if k != i][:3]
    rel = section(b, "More", [head(b, "More Head", "Keep Reading", "More From <strong>Our Blog</strong>", center=True),
                              e("e-grid", "More Grid", more, style="grid-template-columns: repeat(3, 1fr); grid-template-rows: auto; gap: 22px; padding: 0px; @media(--tablet){ grid-template-columns: 1fr; }")], ["em-band-light"])
    return [hero, HM.make_ticker("Post Ticker"), art, rel]


# ---------- FAQS ----------
FAQ10 = C["FAQ"] + [
    ["What services does EmmEnn Tech offer?", "SEO, local SEO and Google Business Profile, Google Ads, website development, social media marketing and AI search optimization. You can use one service or combine them into one plan."],
    ["How much do your services cost?", "Pricing depends on your goals, market and the services you need. After a free audit we send a clear monthly quote with no hidden fees. Ad spend and third-party tools are billed separately."],
    ["Is the growth audit really free?", "Yes. We review your website, Google profile and competitors, then walk you through what we found on a 30-minute call. There is no obligation to sign up."],
    ["Who will I be working with?", "You work directly with the EmmEnn Tech team that does the work. You get one point of contact, plain-English updates and a reply within one business day."]]

def faq_page():
    ban = banner(b, "Banner", "FAQs", "Questions, <strong>Answered Plainly</strong>",
                 "Everything business owners usually ask us before getting started: timelines, contracts, reports, pricing and how we work.",
                 "hero-team-strategy", "support-team", "10 common questions", "Still stuck? Just ask")
    items = []
    for i, (q, a) in enumerate(FAQ10):
        n = f"FQ {i+1}"
        title = flex(b, n + " Row", [
            P(b, n + " Num", f"{i+1:02d}", "font-family: var(--em-mono); font-size: 13px; font-weight: 700; color: #FF8A1F; flex: 0 0 34px;"),
            P(b, n + " Q", q, "font-weight: 800; font-size: 18px; color: #0C1530; flex: 1 1 0%; min-width: 0px; @media(--mobile){ font-size: 16px; }"),
            flex(b, n + " Plus", [icon(b, n + " PlusI", "plus", 14, "#FFFFFF")],
                 "flex: 0 0 36px; width: 36px; height: 36px; border-radius: 50%; align-items: center; justify-content: center; background: linear-gradient(135deg, #22C6E0, #1F6BE0);", ["em-faq-plus"])],
            "gap: 14px; align-items: center; width: 100%;")
        items.append(e("e-accordion-item", n, [
            e("e-accordion-item-header", n + " Header", [e("e-accordion-item-title", n + " Title", [title])], style="padding: 20px 22px; cursor: pointer;"),
            e("e-accordion-item-content", n + " Content", [P(b, n + " A", a, "font-size: 16.5px; line-height: 1.7; color: #5B6683;")], style="padding: 0px 22px 22px 70px; @media(--mobile){ padding: 0px 18px 20px 18px; }")],
            style="padding: 0px; border-radius: 20px; border: 1px solid #D3E3FB; background: #F5F9FF;"))
    acc = e("e-accordion", "FAQ Acc", items, cfg={"default_state": "first_expanded", "max_expanded": "one", "show_icon": False, "faq_schema": True},
            style="gap: 12px; padding: 0px; flex: 1 1 0%; min-width: 0px;", classes=["em-acc"])
    side = col(b, "FAQ Side", [
        col(b, "FAQ Side Card", [eyebrow(b, "FAQ Side Eb", "Still Have Questions?", True),
                                 H(b, "FAQ Side H", "Talk To A <strong>Real Person</strong>", "h3", "color: #FFFFFF; font-size: 30px;"),
                                 P(b, "FAQ Side P", "Call, email or book a free audit. We reply within one business day.", "color: rgba(255,255,255,0.75);"),
                                 flex(b, "FAQ Side Ph", [ico_tile(b, "FAQ Side PhI", "phone", True, True, 40), P(b, "FAQ Side PhT", PHONE, "font-weight: 800; color: #FFFFFF;", link=link_url(TEL))], "gap: 12px; align-items: center;"),
                                 flex(b, "FAQ Side Em", [ico_tile(b, "FAQ Side EmI", "envelope", False, True, 40), P(b, "FAQ Side EmT", EMAIL, "font-weight: 800; color: #FFFFFF;", link=link_url(MAILTO))], "gap: 12px; align-items: center;"),
                                 btn(b, "FAQ Side B", "Get a Free Audit", link_page("contact"), "g", "margin-top: 6px; width: 100%;")],
            "gap: 14px; padding: 28px; border-radius: 24px; background: radial-gradient(60% 60% at 100% 0%, rgba(31,107,224,0.45), transparent 70%), #071233;"),
        col(b, "FAQ Side Photo", [img_el(b, "FAQ Side Img", "client-report-review", "width: 100%; aspect-ratio: 4 / 3; object-fit: cover;", "EmmEnn Tech report review")],
            "border-radius: 24px; overflow: hidden;")],
        "gap: 16px; flex: 0 0 360px; position: sticky; top: 120px; @media(--tablet){ position: relative; top: 0px; flex: 0 0 auto; width: 100%; }")
    body = section(b, "FAQ Body", [head(b, "FAQ Head", "FAQs", "Everything You <strong>Wanted To Ask</strong>", "Tap a question to open the answer.", center=True),
                                   flex(b, "FAQ Grid", [acc, side], "gap: 36px; align-items: flex-start; @media(--tablet){ flex-direction: column; align-items: stretch; }")])
    return [ban, HM.make_ticker("FAQ Ticker"), body, cta(b, "CTA")]

# ---------- LEGAL ----------
def legal_doc(prefix, sections, intro, updated):
    kids = [P(b, prefix + " Upd", updated, "font-family: var(--em-mono); font-size: 12.5px; color: #1F6BE0; letter-spacing: 0.06em;"),
            P(b, prefix + " Intro", intro, "font-size: 19px; line-height: 1.7; color: #0C1530; font-weight: 600;")]
    for i, (h, paras) in enumerate(sections):
        kids.append(H(b, f"{prefix} H{i}", h, "h2", "font-size: 26px; margin-top: 14px; @media(--mobile){ font-size: 22px; }"))
        for j, t in enumerate(paras):
            kids.append(P(b, f"{prefix} P{i}-{j}", t, "font-size: 17px; line-height: 1.75; color: #3B4663;"))
    return kids

PRIVACY = [
    ("1. Who We Are", ["EmmEnn Tech is a digital marketing agency operated by EmmEnn Group LLC, 1500 N Grant St, Ste 76430, Denver, CO 80203, United States. In this policy, \"we\", \"us\" and \"our\" refer to EmmEnn Tech."]),
    ("2. Information We Collect", ["Information you give us: when you fill in a form on this website (such as the free audit, consultation, newsletter or client agreement form) we collect the details you enter, for example your name, email address, phone number, website address, the service you are interested in, your message and, for agreements, your electronic signature.",
                                    "Information collected automatically: like most websites, our hosting provider records basic technical data such as your IP address, browser type, device type, pages visited and the date and time of your visit. This is used for security and to keep the site working."]),
    ("3. How We Use Your Information", ["We use your information to reply to your enquiry, prepare audits and proposals, deliver and manage the services you request, send invoices and service updates, send our monthly newsletter if you subscribed, and improve our website and services.",
                                        "We do not sell your personal information."]),
    ("4. Cookies and Third-Party Services", ["Our website uses essential cookies needed for it to work. Video reviews are embedded from YouTube in privacy-enhanced mode, and fonts may be loaded from Google. These providers may receive technical data such as your IP address when their content loads. Their own privacy policies apply to that data.",
                                             "If we add analytics or advertising tools in the future, we will update this policy and, where required, ask for your consent."]),
    ("5. Sharing Your Information", ["We only share personal information with trusted service providers who help us run our business, such as website hosting, email and payment providers, and only as needed to provide our services. We may also disclose information if required by law or to protect our rights."]),
    ("6. Client Account Access", ["When we work on your website, Google Business Profile, ad accounts or other platforms, we use the access you grant only to perform the agreed services, and we keep credentials confidential."]),
    ("7. How Long We Keep Information", ["We keep enquiry and client information for as long as needed to provide our services and to meet legal, tax and accounting requirements. Newsletter subscribers can unsubscribe at any time."]),
    ("8. Your Rights", ["Depending on where you live, you may have the right to access, correct or delete your personal information, object to or limit how we use it, and withdraw consent. To make a request, email us at " + EMAIL + ". We will respond within a reasonable time."]),
    ("9. Security", ["We use reasonable technical and organisational measures to protect your information. No method of transmission over the internet is completely secure, so we cannot guarantee absolute security."]),
    ("10. Children's Privacy", ["Our services are intended for businesses and are not directed at children under 16. We do not knowingly collect personal information from children."]),
    ("11. Changes to This Policy", ["We may update this policy from time to time. The latest version will always be on this page with the date it was last updated."]),
    ("12. Contact Us", ["If you have questions about this policy or your information, contact EmmEnn Tech at " + EMAIL + " or call " + PHONE + "."])]

def privacy_page():
    ban = banner(b, "Banner", "Privacy Policy", "Privacy <strong>Policy</strong>",
                 "How EmmEnn Tech collects, uses and protects the information you share with us.",
                 "contact-banner", "about-team-office", "Your data, protected", "EmmEnn Group LLC")
    doc = legal_doc("PV", PRIVACY, "This Privacy Policy explains what information we collect when you visit emmenntech.com or use our services, how we use it, and the choices you have.", "LAST UPDATED · OCTOBER 4, 2026")
    body = section(b, "Doc", [col(b, "Doc Col", doc, "gap: 16px; max-width: 860px; width: 100%; align-self: center; padding: 44px; border-radius: 28px; background: #FFFFFF; border: 1px solid #D3E3FB; @media(--mobile){ padding: 24px; }")], ["em-band-light"])
    return [ban, HM.make_ticker("PV Ticker"), body, cta(b, "CTA")]

TERMS = [
    ("1. Services", "EmmEnnTech agrees to provide digital marketing, web development, AI-powered search, paid media, consulting, or other services described and agreed upon between EmmEnnTech and the Client."),
    ("2. Client Responsibilities", "The Client agrees to provide accurate information, required materials, access, approvals, and other resources reasonably necessary for EmmEnnTech to perform the agreed services."),
    ("3. Payment", "The Client agrees to pay all fees according to the pricing, payment schedule, proposal, invoice, or other written agreement provided by EmmEnnTech."),
    ("4. Advertising and Third-Party Costs", "Advertising budgets, software subscriptions, third-party platform fees, domains, hosting, and other external costs are separate from service fees unless expressly stated otherwise in writing."),
    ("5. Results and Performance", "EmmEnnTech will provide services using commercially reasonable efforts. However, specific business results, sales, leads, rankings, advertising performance, or revenue cannot be guaranteed because performance may depend on market conditions, competition, platforms, budgets, offers, and other factors."),
    ("6. Communication", "The Client agrees to maintain reasonable communication and provide timely feedback, approvals, and required information when requested."),
    ("7. Intellectual Property", "Ownership and usage rights for deliverables will be determined according to the applicable proposal, invoice, or written agreement between the Client and EmmEnnTech."),
    ("8. Confidentiality", "Both parties agree to treat confidential business information, credentials, strategies, customer information, and other non-public information received during the engagement appropriately and confidentially."),
    ("9. Termination", "Either party may terminate services according to the terms stated in the applicable proposal, agreement, or written communication. Any outstanding approved fees or committed expenses may remain payable."),
    ("10. Electronic Acceptance", "By signing electronically and submitting this agreement, the Client confirms that they have reviewed the information above, understand the terms presented, and agree to proceed with EmmEnnTech under the applicable service arrangement.")]

def agreement_page():
    hero = flex(b, "AG Hero", [col(b, "AG Hero Wrap", [
        P(b, "AG Badge", "CLIENT SERVICE AGREEMENT", "font-family: var(--em-mono); font-size: 12.5px; letter-spacing: 0.14em; color: #7AF0F5; padding: 8px 16px; border-radius: 50px; border: 1px dashed rgba(122,240,245,0.45); width: auto; align-self: center;"),
        H(b, "AG Title", "EmmEnnTech Client <strong>Service Agreement</strong>", "h1", "color: #FFFFFF; font-size: 58px; text-align: center; @media(--tablet){ font-size: 44px; } @media(--mobile){ font-size: 32px; }"),
        P(b, "AG Lead", "Please review the agreement carefully, complete your information, provide your electronic signature, and submit the agreement.", "color: rgba(255,255,255,0.8); font-size: 18px; text-align: center; max-width: 640px; align-self: center;")],
        "gap: 18px; align-items: center;", ["em-wrap"])],
        "flex-direction: column; align-items: center; padding: 170px 24px 72px 24px; background: radial-gradient(40% 70% at 85% 40%, rgba(63,208,222,0.22), transparent 70%), radial-gradient(35% 50% at 0% 100%, rgba(255,138,31,0.16), transparent 70%), #071233; @media(--mobile){ padding: 120px 16px 48px 16px; }", ["em-banner"])
    def step(cid, num, title):
        return flex(b, cid, [flex(b, cid + " N", [P(b, cid + " NT", num, "font-family: var(--em-num); font-weight: 700; color: #FFFFFF;")],
                                  "flex: 0 0 38px; width: 38px; height: 38px; border-radius: 50% 50% 50% 6px; align-items: center; justify-content: center; background: linear-gradient(90deg, #22C6E0, #1F6BE0);"),
                             H(b, cid + " H", title, "h2", "font-size: 24px;")], "gap: 14px; align-items: center; width: 100%; padding-bottom: 14px; border-bottom: 1px solid #D3E3FB;")
    def fld(cid, fid, label, kind, ph, full=False):
        return e("e-div-block", cid, [e("e-form-label", cid + " L", cfg={"text": label, "input-id": fid}, classes=["em-label"]),
                                      e("e-form-input", cid + " F", cfg={"placeholder": ph, "type": kind, "required": True, "_cssid": fid}, classes=["em-input"])],
                 style="display: flex; flex-direction: column; gap: 8px; padding: 0px; " + ("flex: 1 1 100%;" if full else "flex: 1 1 calc(33% - 12px); min-width: 220px;"))
    terms = [col(b, f"AG T{i}", [H(b, f"AG T{i} H", h, "h3", "font-size: 18px;"), P(b, f"AG T{i} P", t, "font-size: 15.5px; line-height: 1.7; color: #3B4663;")], "gap: 6px;")
             for i, (h, t) in enumerate(TERMS)]
    terms_box = col(b, "AG Terms", terms, "flex: 1 1 100%; gap: 18px; max-height: 460px; overflow-y: auto; padding: 24px; border-radius: 18px; background: #F5F9FF; border: 1px solid #D3E3FB;")
    consent = e("e-div-block", "AG Consent", [
        e("e-div-block", "AG Box", [e("e-form-checkbox", "AG Check", cfg={"name": "agreement_accepted", "value": "Accepted", "required": True})],
          style="display: grid; place-items: center; flex: 0 0 24px; width: 24px; height: 24px; padding: 0px; border-radius: 6px; border: 1.5px solid #1F6BE0; background: #FFFFFF; margin-top: 2px;"),
        P(b, "AG Consent T", "I confirm that I have read and understood this Client Service Agreement and agree to the terms presented above. I understand that my electronic signature represents my acceptance of this agreement.", "font-size: 15px; color: #0C1530; flex: 1 1 0%; min-width: 0px;")],
        style="display: flex; gap: 12px; align-items: flex-start; flex: 1 1 100%; padding: 16px; border-radius: 14px; background: #FFF6EE; border: 1px solid #FFD9B8;")
    kids = [step("AG S1", "1", "Client Information"),
            fld("AG Name", "ag-name", "Full Name *", "text", "Enter your full name"),
            fld("AG Email", "ag-email", "Email Address *", "email", "Enter your email address"),
            fld("AG Phone", "ag-phone", "Phone Number *", "tel", "Enter your phone number"),
            step("AG S2", "2", "Service Agreement"), terms_box,
            step("AG S3", "3", "Electronic Signature"),
            fld("AG Sign", "ag-signature", "Type your full legal name as your signature *", "text", "Your full legal name", True),
            consent,
            e("e-form-submit-button", "AG Submit", cfg={"text": "Sign & Submit Agreement"}, classes=["em-btn", "em-btn-g"]),
            P(b, "AG Note", "Your signed agreement will be securely submitted to EmmEnnTech.", "font-size: 13.5px; color: #5B6683; flex: 1 1 100%;"),
            e("e-form-success-message", "AG Ok", [P(b, "AG OkT", "Thank you. Your signed agreement has been submitted to EmmEnnTech. We will be in touch shortly.", "font-size: 15px; color: #0C1530;")],
              style="flex: 1 1 100%; border-radius: 12px; background: #E3F3FF; padding: 14px;"),
            e("e-form-error-message", "AG Err", [P(b, "AG ErrT", f"Sorry, the agreement could not be submitted. Please check the required fields, or email {EMAIL}.", "font-size: 15px; color: #8A2A0F;")],
              style="flex: 1 1 100%; border-radius: 12px; background: #FFF1E6; padding: 14px;")]
    frm = e("e-form", "AG Form", kids, cfg={"form-name": "Client Service Agreement", "actions-after-submit": ["email"],
                                             "email": {"to": [EMAIL], "subject": "Signed Client Service Agreement", "reply-to": "", "from-name": "EmmEnnTech Agreements"}},
            style="gap: 18px 16px; align-items: flex-start;", classes=["em-form"])
    card = col(b, "AG Card", [frm], "max-width: 920px; width: 100%; align-self: center; padding: 40px; border-radius: 28px; background: #FFFFFF; border: 1px solid #D3E3FB; box-shadow: 0 30px 70px -36px rgba(7,18,51,0.45); @media(--mobile){ padding: 22px; }")
    return [hero, HM.make_ticker("AG Ticker"), section(b, "AG Body", [card], ["em-band-light"])]

if which.startswith("post"):
    i = int(which[4:]); kids = post(i); pid = PAGES["posts"][i]
else:
    kids = {"about": about, "services": services, "blog": blog, "contact": contact, "faq": faq_page, "privacy": privacy_page, "agreement": agreement_page}[which](); pid = PAGES[which]
root = col(b, "Page", kids, "gap: 0px; width: 100%;")
json.dump(b.payload(pid, root), open(f'/tmp/p_{which}.json', 'w'))
