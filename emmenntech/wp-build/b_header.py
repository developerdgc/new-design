import json
from blocks import *
b = B(); e = b.el
NAV = [("home", "Home"), ("about", "About Us"), ("services", "Our Services"), ("blog", "Our Blog"), ("faq", "FAQs"), ("contact", "Contact Us")]
def navlink(key, label):
    return P(b, f"Nav {label}", label, None, ["em-nav-link", f"em-nl-{key}"], link=link_page(key))
brand = flex(b, "Brand", [img_el(b, "Logo", "logo-for-dark-bg", "width: 200px; @media(--mobile){ width: 158px; }", "EmmEnn Tech")],
             "width: auto; flex: 0 0 auto; align-items: center;", cfg={"link": link_page("home")})
nav = flex(b, "Main Nav", [navlink(k, l) for k, l in NAV], "align-items: center; width: auto; flex: 0 1 auto; @media(--tablet){ display: none; }", ["em-nav"])
status = flex(b, "Status", [flex(b, "Status Dot", [], "", ["em-status-dot"]),
                            P(b, "Status Text", "Accepting new clients", "font-family: var(--em-mono); font-size: 12px; color: #9CF3C9; white-space: nowrap;")],
              "width: auto;", ["em-status"])
cta = btn(b, "Header CTA", "Free Audit", link_page("contact"), "g", "padding: 13px 22px; @media(--mobile){ display: none; }")
burger = flex(b, "Burger", [icon(b, "Burger Svg", "bars", 20, "#FFFFFF")],
              "display: none; flex: 0 0 46px; width: 46px; height: 46px; border-radius: 50%; border: 1px solid rgba(255,255,255,0.22); align-items: center; justify-content: center; @media(--tablet){ display: flex; }",
              cfg={"link": {"destination": {"name": "popup", "settings": {"popup": str(PAGES["popup"])}}, "tag": "a"}})
actions = flex(b, "Actions", [status, cta, burger], "gap: 16px; align-items: center; width: auto; flex: 0 0 auto;")
bar = flex(b, "Bar", [brand, nav, actions],
           "width: 100%; max-width: 1320px; justify-content: space-between; align-items: center; gap: 18px; height: 70px; padding: 0px 10px 0px 22px; border-radius: 50px; background: rgba(7,18,51,0.82); border: 1px solid rgba(255,255,255,0.14); backdrop-filter: blur(16px); box-shadow: 0 20px 50px -24px rgba(0,0,0,0.6); @media(--mobile){ height: 62px; padding: 0px 8px 0px 16px; }")
shell = flex(b, "Header Shell", [bar], "position: fixed; top: 14px; left: 0px; right: 0px; z-index: 999; justify-content: center; padding: 0px 24px; @media(--mobile){ padding: 0px 16px; }")
json.dump(b.payload(PAGES["header"], shell), open('/tmp/p_header.json', 'w'))
