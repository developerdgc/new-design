import json
from blocks import *
b = B(); e = b.el
soc = [("facebook-f", "Facebook"), ("instagram", "Instagram"), ("linkedin-in", "LinkedIn"), ("youtube", "YouTube")]
def social(prefix, dark=True):
    return flex(b, prefix + " Social", [flex(b, f"{prefix} {n}", [icon(b, f"{prefix} {n} Svg", ic, 16, None, "fa-brands")],
        "flex: 0 0 40px; width: 40px; height: 40px; border-radius: 50%; align-items: center; justify-content: center; color: #FFFFFF; border: 1px solid rgba(255,255,255,0.55);",
        ["em-social"], cfg={"link": link_page("contact")}) for ic, n in soc], "gap: 10px; width: auto;")
# connect strip
strip = flex(b, "Connect", [col(b, "Connect Wrap", [flex(b, "Connect Row", [
    col(b, "Connect L", [P(b, "Connect Eb", "Stay On Route", "color: #03121A;", ["em-eb"]),
                         H(b, "Connect Title", "Get Connected With Us", "h3", "color: #FFFFFF; font-size: 32px; @media(--mobile){ font-size: 24px; }")], "gap: 8px; width: auto; flex: 1 1 auto;"),
    flex(b, "Connect R", [social("Strip"), btn(b, "Connect CTA", "Get a Free Audit", link_page("contact"), "w")], "gap: 16px; align-items: center; flex-wrap: wrap; width: auto;")],
    "justify-content: space-between; align-items: center; gap: 20px; flex-wrap: wrap; width: 100%;")], "", ["em-wrap"])],
    "flex-direction: column; align-items: center; padding: 26px 24px; background: linear-gradient(90deg, #22C6E0 0%, #1F6BE0 100%); @media(--mobile){ padding: 24px 16px; }")
def fcol(cid, title, kids, style=""):
    return col(b, cid, [P(b, cid + " T", title, "color: #FFFFFF; margin-bottom: 14px;", ["em-eb"])] + kids, "gap: 12px; " + style)
NAV = [("home", "Home"), ("about", "About Us"), ("services", "Our Services"), ("blog", "Our Blog"), ("contact", "Contact Us")]
explore = fcol("F Explore", "Explore", [P(b, f"F N {l}", l, "font-size: 15.5px; color: rgba(255,255,255,0.72);", link=link_page(k)) for k, l in NAV])
services = fcol("F Services", "Services", [P(b, f"F S {s['name']}", s['name'], "font-size: 15.5px; color: rgba(255,255,255,0.72);", link=link_page("services")) for s in C["SVC"]])
def reach(cid, ic, text, link=None, strong=False):
    return flex(b, cid, [icon(b, cid + " I", ic, 16, "#FF8A1F", style="margin-top: 4px;"),
                         P(b, cid + " T", text, "font-size: 15px; " + ("color: #FFFFFF; font-weight: 700;" if strong else "color: rgba(255,255,255,0.72);"), link=link)], "gap: 10px; align-items: flex-start;")
contact = fcol("F Reach", "Direct Reach", [reach("F R Phone", "phone", PHONE, link_url(TEL), True), reach("F R Mail", "envelope", EMAIL, link_url(MAILTO), True),
                                           reach("F R Addr", "location-dot", ADDRESS), reach("F R Hours", "clock", HOURS)])
about = col(b, "F About", [img_el(b, "F Logo", "logo-for-dark-bg", "width: 210px;", "EmmEnn Tech"),
                           P(b, "F About T", "Your partner for SEO, Google Ads, local search and websites that bring in real customers.", "font-size: 15.5px; color: rgba(255,255,255,0.72); max-width: 340px;"),
                           social("Foot")], "gap: 18px;")
grid = e("e-grid", "F Grid", [about, explore, services, contact],
         style="grid-template-columns: 1.4fr 0.8fr 1fr 1.2fr; grid-template-rows: auto; gap: 40px; padding: 0px; @media(--tablet){ grid-template-columns: 1fr 1fr; grid-template-rows: auto auto; } @media(--mobile){ grid-template-columns: 1fr; grid-template-rows: auto; }")
word = P(b, "F Wordmark", "EmmEnn Tech", "font-size: 190px; margin-top: 50px; @media(--tablet){ font-size: 110px; } @media(--mobile){ font-size: 54px; }", ["em-wordmark"])
bottom = flex(b, "F Bottom", [P(b, "F Copy", "© 2021–2026 EmmEnn Group LLC. All rights reserved.", "font-size: 14px; color: rgba(255,255,255,0.6);"),
                              P(b, "F Legal", "Privacy Policy · Online Agreement", "font-size: 14px; color: rgba(255,255,255,0.6);", link=link_page("contact"))],
              "justify-content: space-between; gap: 16px; flex-wrap: wrap; padding: 20px 0px; border-top: 1px solid rgba(255,255,255,0.12); width: 100%;")
foot = flex(b, "Footer", [col(b, "Footer Wrap", [grid, word, bottom], "", ["em-wrap"])],
            "flex-direction: column; align-items: center; padding: 80px 24px 0px 24px; overflow: hidden; @media(--mobile){ padding: 56px 16px 0px 16px; }", ["em-footer"])
root = col(b, "Site Footer", [strip, foot], "gap: 0px; width: 100%;")
json.dump(b.payload(PAGES["footer"], root), open('/tmp/p_footer.json', 'w'))
