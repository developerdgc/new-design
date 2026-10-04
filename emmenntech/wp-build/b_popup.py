import json
from blocks import *
b = B(); e = b.el
NAV = [("home", "Home"), ("about", "About Us"), ("services", "Our Services"), ("blog", "Our Blog"), ("faq", "FAQs"), ("contact", "Contact Us")]
links = [P(b, f"M {l}", l, "font-size: 26px; font-weight: 800; color: #FFFFFF; padding: 10px 0px; border-bottom: 1px solid rgba(255,255,255,0.1);", link=link_page(k)) for k, l in NAV]
box = col(b, "Mobile Menu", [
    img_el(b, "M Logo", "logo-for-dark-bg", "width: 170px; margin-bottom: 18px;", "EmmEnn Tech")] + links + [
    btn(b, "M CTA", "Get a Free Audit", link_page("contact"), "g", "margin-top: 18px; width: 100%;"),
    P(b, "M Phone", PHONE, "font-weight: 700; color: #7AF0F5; margin-top: 10px;", link=link_url(TEL))],
    "gap: 4px; padding: 90px 28px 40px 28px; background: #071233; width: 100%; min-height: 100vh;", ["em-mobile-menu"])
json.dump(b.payload(PAGES["popup"], box), open('/tmp/p_popup.json', 'w'))
