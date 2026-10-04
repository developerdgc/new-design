"""Shared section builders for EmmEnn Tech pages."""
from gen import *

PHONE = "+1 (720) 583-7100"; TEL = "tel:+17205837100"
EMAIL = "info@emmenntech.com"; MAILTO = "mailto:info@emmenntech.com"
ADDRESS = "1500 N Grant St, Ste 76430, Denver, CO 80203, United States"
HOURS = "Mon – Fri: 9:00 AM – 6:00 PM EST"
# icon per service (Font Awesome)
SVC_ICON = {"seo": "magnifying-glass-chart", "local-seo": "location-dot", "google-ads": "bullhorn",
            "web": "code", "social": "share-nodes", "ai-search": "wand-magic-sparkles"}

def P(b, cid, text, style=None, classes=None, link=None, tag=None):
    cfg = {"paragraph": text}
    if link: cfg["link"] = link
    if tag: cfg["tag"] = tag
    return b.el("e-paragraph", cid, cfg=cfg, style=style, classes=classes)

def H(b, cid, text, tag="h2", style=None, classes=None):
    return b.el("e-heading", cid, cfg={"tag": tag, "title": text}, style=style, classes=classes)

def flex(b, cid, kids, style="", classes=None, cfg=None):
    return b.el("e-flexbox", cid, kids, cfg=cfg, style="padding: 0px; " + style, classes=classes)

def col(b, cid, kids, style="", classes=None, cfg=None):
    return flex(b, cid, kids, "flex-direction: column; " + style, classes, cfg)

def icon(b, cid, name, size=20, color=None, lib="fa-solid", style=""):
    st = f"width: {size}px; height: {size}px; flex: 0 0 {size}px; " + (f"color: {color}; " if color else "") + style
    return b.el("e-svg", cid, cfg=fa(name, lib), style=st)

def ico_tile(b, cid, name, hot=False, round_=False, size=48, isz=None):
    cls = ["em-ico"] + (["em-ico-o"] if hot else []) + (["em-ico-r"] if round_ else [])
    st = f"flex: 0 0 {size}px; width: {size}px; height: {size}px;"
    return flex(b, cid, [icon(b, cid + " Svg", name, isz or int(size * 0.46), "#FFFFFF")], st, cls)

def eyebrow(b, cid, text, dark=False):
    return P(b, cid, text, classes=["em-eb"] + (["em-eb-dark"] if dark else []))

def head(b, cid, eb, title, lead=None, center=False, dark=False, tag="h2", style="", title_style=None):
    kids = [eyebrow(b, cid + " Eyebrow", eb, dark),
            H(b, cid + " Title", title, tag, title_style, ["em-h2"] + (["em-on-dark"] if dark else []))]
    if lead:
        kids.append(P(b, cid + " Lead", lead, "max-width: 640px;" if center else "max-width: 620px;",
                      ["em-lead"] + (["em-soft-dark"] if dark else [])))
    al = "align-items: center; text-align: center;" if center else "align-items: flex-start;"
    return col(b, cid, kids, f"gap: 16px; {al} margin-bottom: 52px; @media(--mobile){{ margin-bottom: 36px; }} " + style)

def btn(b, cid, text, link, kind="g", style=None):
    return b.el("e-button", cid, cfg={"text": text, "link": link}, style=style, classes=["em-btn", "em-btn-" + kind])

def section(b, cid, kids, classes=None, style="", wrap_style=""):
    # no inline padding here: the em-section class owns section spacing
    return b.el("e-flexbox", cid, [col(b, cid + " Wrap", kids, wrap_style, ["em-wrap"])],
                style="flex-direction: column; align-items: center; " + style, classes=["em-section"] + (classes or []))

def img_el(b, cid, name, style="", alt="", classes=None):
    return b.el("e-image", cid, cfg=img(name, alt=alt), style=style, classes=classes)

def bullet(b, cid, text, color="#1F6BE0", dark=False):
    return flex(b, cid, [
        flex(b, cid + " Tick", [icon(b, cid + " Svg", "check", 11, "#FFFFFF")],
             f"flex: 0 0 20px; width: 20px; height: 20px; border-radius: 6px; background: {color}; align-items: center; justify-content: center;"),
        P(b, cid + " Text", text, "font-weight: 700; font-size: 16px; color: " + ("#FFFFFF" if dark else "#0C1530") + ";")],
        "gap: 10px; align-items: center;")

def interact(direction="bottom", delay=0, effect="slide"):
    import itertools
    interact.n = getattr(interact, 'n', 0) + 1
    return [{"interaction_id": f"em-anim-{interact.n}", "trigger": "scrollIn",
             "animation": {"effect": effect, "type": "in", "direction": direction,
                           "timing_config": {"duration": {"unit": "ms", "size": 700}, "delay": {"unit": "ms", "size": delay}},
                           "config": {"easing": "easeOut", "replay": False}}}]

# ---------- shared sections ----------
def faq_chat(b, cid, light=False):
    """FAQ as chat bubbles using native accordion."""
    e = b.el
    items = []
    for i, (q, a) in enumerate(C["FAQ"]):
        n = f"{cid} {i+1}"
        q_bub = flex(b, n + " QB", [P(b, n + " Q", q, "font-weight: 800; font-size: 16px; color: #0C1530;")],
                     "padding: 14px 18px; background: #FFFFFF; border: 1px solid #D3E3FB; width: auto;", ["em-q-bubble"])
        title = flex(b, n + " QRow", [
            flex(b, n + " QAv", [P(b, n + " QAvT", "?", "font-weight: 900; color: #1F6BE0;")],
                 "flex: 0 0 36px; width: 36px; height: 36px; border-radius: 50%; background: #E3ECFB; align-items: center; justify-content: center;"),
            q_bub], "gap: 12px; align-items: flex-end;")
        ans = flex(b, n + " ARow", [
            flex(b, n + " ABub", [P(b, n + " A", a, "font-weight: 600; font-size: 15.5px; color: #FFFFFF;")],
                 "padding: 14px 18px; border-radius: 20px 20px 6px 20px; background: linear-gradient(90deg, #22C6E0 0%, #1F6BE0 100%); max-width: 640px;"),
            flex(b, n + " AAv", [b.el("e-image", n + " AAvImg", cfg=img("icon"), style="width: 22px; height: 22px;")],
                 "flex: 0 0 36px; width: 36px; height: 36px; border-radius: 50%; background: #071233; align-items: center; justify-content: center;")],
            "gap: 12px; align-items: flex-end; justify-content: flex-end; margin-top: 10px;")
        items.append(e("e-accordion-item", n, [
            e("e-accordion-item-header", n + " Header", [e("e-accordion-item-title", n + " Title", [title])], style="padding: 0px;"),
            e("e-accordion-item-content", n + " Content", [ans], style="padding: 0px;")], style="padding: 0px; border: 0px; background: transparent;"))
    acc = e("e-accordion", cid + " Acc", items, cfg={"default_state": "first_expanded", "max_expanded": "one", "show_icon": False, "faq_schema": True},
            style="gap: 14px; padding: 0px; flex: 1 1 auto; min-width: 0px;", classes=["em-chat"])
    photo = col(b, cid + " Photo", [
        img_el(b, cid + " PhotoImg", "support-team", "width: 100%; height: 100%; object-fit: cover;", "EmmEnn Tech support specialist"),
        col(b, cid + " PhotoCap", [
            flex(b, cid + " Online", [flex(b, cid + " OnlineDot", [], "", ["em-status-dot"]),
                                      P(b, cid + " OnlineT", "Team online · Mon–Fri", "font-family: var(--em-mono); font-size: 12px; color: #9CF3C9;")], "", ["em-status"]),
            P(b, cid + " PhotoT", "Real people answer, not bots.", "font-size: 20px; font-weight: 800; color: #FFFFFF;")],
            "position: absolute; left: 18px; right: 18px; bottom: 18px; gap: 8px; z-index: 2;")],
        "flex: 0 0 34%; position: relative; border-radius: 24px; overflow: hidden; aspect-ratio: 4/5; align-self: flex-start; background: linear-gradient(180deg, transparent 50%, rgba(4,11,34,0.92)); @media(--tablet){ display: none; }",
        ["em-tile-photo"])
    grid = flex(b, cid + " Grid", [photo, acc], "gap: 28px; align-items: flex-start; width: 100%; max-width: 1180px; align-self: center;")
    contacts = flex(b, cid + " Ask", [
        flex(b, cid + " AskPhone", [icon(b, cid + " AskPhoneI", "phone", 16, "#FF8A1F"), P(b, cid + " AskPhoneT", PHONE, "font-weight: 800; color: #0C1530;", link=link_url(TEL))],
             "gap: 10px; align-items: center; padding: 12px 18px; border-radius: 50px; background: #FFFFFF; border: 1px solid #D3E3FB; width: auto;"),
        flex(b, cid + " AskMail", [icon(b, cid + " AskMailI", "envelope", 16, "#FF8A1F"), P(b, cid + " AskMailT", EMAIL, "font-weight: 800; color: #0C1530;", link=link_url(MAILTO))],
             "gap: 10px; align-items: center; padding: 12px 18px; border-radius: 50px; background: #FFFFFF; border: 1px solid #D3E3FB; width: auto;")],
        "gap: 12px; justify-content: center; flex-wrap: wrap; margin-top: 28px;")
    return section(b, cid, [head(b, cid + " Head", "FAQs", "Ask Us <strong>Anything</strong>", "Tap a question to see our answer.", center=True), grid, contacts],
                   ["em-band-light"] if light else None)

def cta(b, cid):
    big = col(b, cid + " Big", [b.el("e-image", cid + " BigImg", cfg=img("icon", alt=""), style="width: 100%;", classes=["em-ring"])],
              "flex: 0 0 280px; width: 280px; align-items: center; justify-content: center; filter: drop-shadow(0 0 40px rgba(63,208,222,0.55)); @media(--tablet){ flex: 0 0 180px; width: 180px; }")
    copy = col(b, cid + " Copy", [
        eyebrow(b, cid + " Eb", "Free Strategy Call", True),
        H(b, cid + " Title", "Ready To Plot Your Route To <strong>More Customers?</strong>", "h2", "color: #FFFFFF; font-size: 52px; @media(--tablet){ font-size: 38px; } @media(--mobile){ font-size: 30px; }"),
        P(b, cid + " Text", "Book a free 30-minute call. We'll look at your website, your Google profile and your competitors, and give you a clear plan.", "color: rgba(255,255,255,0.82); max-width: 560px;"),
        flex(b, cid + " Btns", [btn(b, cid + " B1", "Get My Free Audit", link_page("contact"), "g"), btn(b, cid + " B2", "View Services", link_page("services"), "o")], "gap: 12px; flex-wrap: wrap;"),
        flex(b, cid + " Chips", [
            flex(b, cid + " C1", [icon(b, cid + " C1I", "phone", 14, "#FF8A1F"), P(b, cid + " C1T", PHONE, "color: #FFFFFF; font-weight: 700; font-size: 14px;", link=link_url(TEL))],
                 "gap: 8px; align-items: center; padding: 8px 14px; border-radius: 50px; background: rgba(255,255,255,0.08); border: 1px solid rgba(255,255,255,0.12); width: auto;"),
            flex(b, cid + " C2", [icon(b, cid + " C2I", "envelope", 14, "#FF8A1F"), P(b, cid + " C2T", EMAIL, "color: #FFFFFF; font-weight: 700; font-size: 14px;", link=link_url(MAILTO))],
                 "gap: 8px; align-items: center; padding: 8px 14px; border-radius: 50px; background: rgba(255,255,255,0.08); border: 1px solid rgba(255,255,255,0.12); width: auto;")],
            "gap: 10px; flex-wrap: wrap;")],
        "gap: 18px; flex: 1 1 auto;")
    card = flex(b, cid + " Card", [copy, big],
                f"gap: 24px; align-items: center; width: 100%; padding: 64px; border-radius: 32px; background: radial-gradient(60% 90% at 100% 50%, rgba(63,208,222,0.35), transparent 65%), radial-gradient(45% 80% at 0% 100%, rgba(255,138,31,0.25), transparent 65%), linear-gradient(120deg, rgba(10,46,122,0.93), rgba(7,18,51,0.9) 70%), {bg('strategy-meeting')} center / cover no-repeat; @media(--tablet){{ flex-direction: column-reverse; align-items: flex-start; padding: 40px; }} @media(--mobile){{ padding: 28px; }}",
                ["em-cta"])
    return section(b, cid, [card], style="padding-top: 0px;")

def banner(b, cid, crumb, title, lead, bg_name, arch_name, tag_title, tag_sub, buttons=None):
    t = col(b, cid + " Text", [
        flex(b, cid + " Crumb", [P(b, cid + " CrumbHome", "Home", "font-family: var(--em-mono); font-size: 13px; color: rgba(255,255,255,0.6);", link=link_page("home")),
                                 P(b, cid + " CrumbSep", "/", "font-family: var(--em-mono); font-size: 13px; color: rgba(255,255,255,0.4);"),
                                 P(b, cid + " CrumbCur", crumb, "font-family: var(--em-mono); font-size: 13px; color: #FF8A1F;")], "gap: 10px;"),
        H(b, cid + " Title", title, "h1", "color: #FFFFFF; font-size: 68px; @media(--tablet){ font-size: 50px; } @media(--mobile){ font-size: 38px; }"),
        P(b, cid + " Lead", lead, "color: rgba(255,255,255,0.8); max-width: 560px; font-size: 18px;")] + ([buttons] if buttons else []),
        "gap: 18px; flex: 1 1 55%;")
    arch = col(b, cid + " Arch", [
        img_el(b, cid + " ArchImg", arch_name, "width: 100%; aspect-ratio: 1 / 1.05; object-fit: cover; border-radius: 220px 220px 26px 26px; border: 1px solid rgba(122,240,245,0.3);"),
        col(b, cid + " Tag", [P(b, cid + " TagT", tag_title, "font-weight: 800; color: #0C1530;"),
                              P(b, cid + " TagS", tag_sub, "font-family: var(--em-mono); font-size: 11px; color: #1F6BE0;")],
            "position: absolute; right: -10px; top: 30px; padding: 12px 16px; border-radius: 16px; background: #FFFFFF; box-shadow: 0 20px 40px -18px rgba(0,0,0,0.6); gap: 2px; width: auto;"),
        flex(b, cid + " Px", [flex(b, cid + " Px1", [], "width: 24px; height: 24px; background: #7AF0F5;"),
                              flex(b, cid + " Px2", [], "width: 38px; height: 38px; background: #FF8A1F; margin-top: -14px;"),
                              flex(b, cid + " Px3", [], "width: 30px; height: 30px; background: #1F6BE0; margin-top: 24px; margin-left: -38px;")],
             "position: absolute; left: -22px; bottom: 30px; gap: 0px; align-items: flex-start;")],
        "flex: 0 0 40%; max-width: 440px; position: relative; @media(--tablet){ flex: 0 0 auto; width: 100%; max-width: 360px; }")
    inner = flex(b, cid + " Grid", [t, arch], "gap: 40px; align-items: center; justify-content: space-between; width: 100%; @media(--tablet){ flex-direction: column; align-items: flex-start; }")
    return flex(b, cid, [col(b, cid + " Wrap", [inner], "", ["em-wrap"])],
                f"flex-direction: column; align-items: center; width: 100%; padding: 170px 24px 80px 24px; background: radial-gradient(40% 70% at 85% 40%, rgba(63,208,222,0.22), transparent 70%), linear-gradient(90deg, rgba(5,13,42,0.96) 0%, rgba(5,13,42,0.88) 50%, rgba(7,18,51,0.8) 100%), {bg(bg_name)} center / cover no-repeat, #071233; @media(--tablet){{ padding: 140px 24px 64px 24px; }} @media(--mobile){{ padding: 120px 16px 56px 16px; }}",
                ["em-banner"])

def svc_link(sid):
    return {"destination": {"id": PAGES["services"]}, "tag": "a"}
