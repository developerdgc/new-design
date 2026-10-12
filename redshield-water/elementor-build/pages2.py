"""Page layouts mirroring redshield-water/index.html section by section."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from rs2 import *

# ================================================================= header / footer
def logo(label, size=30, fs=19.5):
    return row(label, [pic(label + " Mark", "logo.svg", "RedShield Water", f"width: {size}px; height: {size}px; min-width: {size}px;"),
                       t(label + " Text", "<em>Red</em><strong>Shield</strong><b> Water</b>",
                         f"font-size: {fs}px; font-weight: 800; letter-spacing: -0.02em; white-space: nowrap; color: #ffffff; & em {{ color: {RED}; font-style: normal; }} & strong {{ color: #ffffff; }} & b {{ color: {BLUE}; }} @media(--mobile) {{ font-size: 17px; }}")],
               9, "flex-wrap: nowrap; width: auto; flex: 0 0 auto;", href="home")
NAV = [("Home", "home"), ("About", "about"), ("Services", "services"), ("Pricing", "pricing"), ("Areas", "areas"), ("FAQs", "faqs"), ("Contact", "contact")]
def navlink(label, text, href, mobile=False):
    return box(label, [t(label + " Text", text, f"font-size: {15 if mobile else 14.4}px; font-weight: 500; color: #c3ccd9; white-space: nowrap; &:hover {{ color: #ffffff; }}")],
               f"padding: {'6px 9px' if mobile else '0 11px'}; width: auto; flex: 0 0 auto; align-items: center;" + ("" if mobile else " height: 62px;"), href=href)
DD = open(os.path.join(BASE, "ddclass")).read().strip()
def dropdown(label, text, href, items):
    menu = col(label + " Menu", [row(f"{label} Item {i}", [ico(f"{label} Item {i} Icon", ic_, "red", 18, "margin-top: 2px;"),
                                                             col(f"{label} Item {i} Text", [t(f"{label} Item {i} Title", a, "font-size: 14.7px; font-weight: 500; color: #d6dde8;"), t(f"{label} Item {i} Sub", s_, f"font-size: 12.5px; color: {MUTEDD};")], 1)],
                                     10, "flex-wrap: nowrap; align-items: flex-start; width: 100%; padding: 10px 12px; border-radius: 8px; &:hover { background-color: #111b2c; }", href=h_)
                                 for i, (ic_, a, s_, h_) in enumerate(items, 1)], 0)
    menu.cls = ["rs-dd-menu"]
    trig = row(label + " Trigger", [t(label + " Text", text, "font-size: 14.4px; font-weight: 500; color: #c3ccd9; white-space: nowrap;"), ico(label + " Chevron", "down", "muted", 13)], 5,
               "flex-wrap: nowrap; height: 62px; padding: 0 11px;", href=href)
    return box(label, [trig, menu], f"position: relative; padding: 0; width: auto; flex: 0 0 auto; &:hover .{DD} {{ display: flex; }} &:hover {{ color: #ffffff; }}")
def header():
    svc = dropdown("Menu Services", "Services", "services", [("wrench", "All Services", "Emergency &amp; general plumbing", "services"), ("drain", "Blocked Drain Service", "Unblocking, repairs, installs", "bds"),
                                                             ("drop", "Leeds Drain Unblocking", "From £80 · 45-min response", "ldu")])
    areas = dropdown("Menu Areas", "Areas", "areas", [("pin", "All Areas We Cover", "Yorkshire-wide coverage", "areas"), ("pin", "Leeds Emergency Plumber", "23+ Leeds neighbourhoods", "leeds"),
                                                      ("pin", "Harrogate Emergency Plumber", "25-mile radius", "harrogate"), ("pin", "Yorkshire Emergency Plumber", "Dales to the coast", "yorkshire")])
    items = [navlink("Menu Home", "Home", "home"), navlink("Menu About", "About", "about"), svc, navlink("Menu Pricing", "Pricing", "pricing"), areas,
             navlink("Menu FAQs", "FAQs", "faqs"), navlink("Menu Contact", "Contact", "contact")]
    nav = row("Main Menu", items +
              [row("Menu Safety Videos", [ico("Menu Safety Videos Icon", "playc", "white", 15), t("Menu Safety Videos Text", "Safety Videos", "font-size: 14.4px; font-weight: 500; color: #d6dde8; white-space: nowrap;")], 6,
                   "flex-wrap: nowrap; width: auto; flex: 0 0 auto; margin-left: 6px; padding: 6px 12px; border-radius: 999px; border: 1px solid rgba(255,255,255,0.16); &:hover { background-color: rgba(220,38,38,0.2); }", href="tutorials")],
              4, "flex-wrap: nowrap; width: auto; flex: 1 1 auto; justify-content: center; @media(--tablet) { display: none; }", tag="nav")
    call_b = btn("Header Call", PHONE, TEL, "red", "sm", "phone", "flex: 0 0 auto; @media(--mobile) { display: none; }")
    bar = row("Header Bar", [logo("Logo"), nav, row("Header Actions", [call_b, mobile_call(), mobile_menu()], 8, "flex-wrap: nowrap; flex: 0 0 auto; position: static;")], 14,
              f"flex-wrap: nowrap; justify-content: space-between; max-width: {W}px; margin: 0 auto; padding: 0 20px; min-height: 62px; width: 100%; position: static; @media(--mobile) {{ padding: 0 14px; }}")
    # sticky header is the containing block for the dropdown panel of the mobile menu
    return box("Site Header", [bar], f"flex-direction: column; padding: 0; background-color: rgba(6,11,19,0.97); backdrop-filter: blur(10px); border-bottom: 1px solid {LINED}; position: sticky; top: 0; z-index: 50;", tag="header")

def mobile_call():
    return box("Mobile Call", [ico("Mobile Call Icon", "phone", "white", 18)], f"display: none; width: 40px; height: 40px; padding: 0; align-items: center; justify-content: center; border-radius: 10px; background-color: {RED}; flex: 0 0 auto; @media(--mobile) {{ display: flex; }}", href=TEL)
def mobile_menu():
    """Hamburger built on the accordion widget: it renders as native <details>, so it opens and closes without any JavaScript."""
    def mlink(label, text, href, sub=False):
        return box(label, [t(label + " Text", text, f"font-size: {14.5 if sub else 16.5}px; font-weight: {500 if sub else 600}; color: {'#aab5c5' if sub else '#ffffff'};")],
                   f"padding: {'9px 14px 9px 30px' if sub else '13px 14px'}; width: 100%; border-radius: 8px; &:hover {{ background-color: #111b2c; }}", href=href)
    group = lambda title, links: col(f"MM {title}", [t(f"MM {title} Title", title, "font-size: 12px; font-weight: 700; letter-spacing: 0.08em; text-transform: uppercase; color: #ff6b6b; padding: 12px 14px 4px;")] +
                                     [mlink(f"MM {title} {a}", a, h_, True) for a, h_ in links], 0, "width: 100%;")
    panel = col("MM Panel", [mlink("MM Home", "Home", "home"), mlink("MM About", "About Us", "about"),
                             group("Services", [("All Services", "services"), ("Blocked Drain Service", "bds"), ("Leeds Drain Unblocking", "ldu")]),
                             mlink("MM Pricing", "Pricing Plan", "pricing"),
                             group("Areas", [("All Areas We Cover", "areas"), ("Leeds Emergency Plumber", "leeds"), ("Harrogate Emergency Plumber", "harrogate"), ("Yorkshire Emergency Plumber", "yorkshire")]),
                             mlink("MM FAQs", "FAQs", "faqs"), mlink("MM Videos", "Free Safety Tutorials", "tutorials"), mlink("MM Contact", "Contact Us", "contact"),
                             btn("MM Call", f"Call {PHONE}", TEL, "red", "md", "phone", "width: 100%; margin-top: 10px;")], 2,
                f"width: 100%; max-height: calc(100vh - 80px); overflow-y: auto; padding: 10px 14px 18px; background-color: #060b13; border-top: 1px solid {LINED}; box-shadow: 0 20px 40px rgba(0,0,0,0.55);")
    item = N("e-accordion-item", "MM Item", {}, "position: static; padding: 0; border: 0; background-color: transparent; &[open] > summary { background-color: #dc2626; border-color: #dc2626; }", None, [
        N("e-accordion-item-header", "MM Toggle", {}, "list-style: none; cursor: pointer; width: 40px; height: 40px; padding: 0; display: flex; align-items: center; justify-content: center; border-radius: 10px; "
          "border: 1px solid rgba(255,255,255,0.22); background-color: rgba(255,255,255,0.06); &::-webkit-details-marker { display: none; } &::after { display: none; content: none; }", None, [
            N("e-accordion-item-title", "MM Toggle Title", {}, "padding: 0; margin: 0; width: 100%; height: 100%; display: flex; align-items: center; justify-content: center; flex: 1 1 auto;", None, [ico("MM Toggle Icon", "menu", "white", 20, "margin: auto;")])]),
        N("e-accordion-item-content", "MM Content", {}, "position: absolute; top: 100%; left: 0; right: 0; padding: 0; z-index: 60;", None, [panel])])
    return N("e-accordion", "Mobile Menu", {"default_state": "all_collapsed", "max_expanded": "one", "show_icon": False, "faq_schema": False},
             "display: none; position: static; padding: 0; gap: 0; width: auto; flex: 0 0 auto; @media(--tablet) { display: flex; }", None, [item])

def footer():
    FL = "font-size: 14.7px; color: #a3afc0; &:hover { color: #ffffff; }"
    def flink(label, text, href): return box(label, [t(label + " Text", text, FL)], "padding: 0; width: fit-content;", href=href)
    def fcol(label, title, links): return col(label, [h(label + " Title", title, "h4", "font-size: 15.2px; font-weight: 700; color: #ffffff; margin-bottom: 5px;")] + [flink(f"{label} {a}", a, b) for a, b in links], 9)
    c1 = col("Footer Brand", [logo("Footer Logo"), t("Footer About", "24/7 emergency plumbing services across Yorkshire. Fast response, guaranteed work, no hidden costs.", "font-size: 14.7px; line-height: 1.6; color: #a3afc0;"),
                              row("Footer Rating", [tp_stars("Footer Stars", 17), t("Footer Trustpilot", "Trustpilot", f"font-size: 14.7px; font-weight: 700; color: {TP};")], 8)], 14)
    c2 = fcol("Footer Services", "Services", [("Burst Pipes", "services"), ("Leak Detection", "services"), ("Blocked Drains", "bds"), ("Boiler Repairs", "services"), ("Leeds Drain Unblocking", "ldu")])
    c3 = fcol("Footer Company", "Company", [("About Us", "about"), ("Pricing Plan", "pricing"), ("Service Areas", "areas"), ("FAQs", "faqs"), ("Free Safety Tutorials", "tutorials"), ("Contact Us", "contact")])
    def citem(i, icon, text, href=None):
        return row(f"Footer Contact {i}", [ico(f"Footer Contact {i} Icon", icon, "red", 15), t(f"Footer Contact {i} Text", text, FL)], 8, "flex-wrap: nowrap; width: fit-content;", href=href)
    c4 = col("Footer Contact", [h("Footer Contact Title", "Contact", "h4", "font-size: 15.2px; font-weight: 700; color: #ffffff; margin-bottom: 5px;"),
                                citem(1, "phone", PHONE, TEL), citem(2, "mail", EMAIL, f"mailto:{EMAIL}"), citem(3, "pin", "Yorkshire, UK"), citem(4, "clock", "Open 24 hours, 7 days"),
                                citem(5, "yt", "YouTube tutorials", "https://www.youtube.com/@RedShieldWater")], 9)
    g = cgrid("Footer Columns", [c1, c2, c3, c4], "1.4fr 1fr 1fr 1.2fr", 36, "", "repeat(2, minmax(0, 1fr))")
    g.style += " @media(--mobile) { grid-template-columns: minmax(0, 1fr); }"
    bl = lambda a, b: box(f"Footer Bottom {a}", [t(f"Footer Bottom {a} Text", a, "font-size: 13.1px; color: #a3afc0; &:hover { color: #ffffff; }")], "padding: 0; width: auto;", href=b)
    bottom = row("Footer Bottom", [t("Copyright", "© 2026 RedShield Water. All rights reserved.", "font-size: 13.1px; color: #a3afc0;"),
                                   row("Footer Bottom Links", [bl("Leeds", "leeds"), t("Dot 1", "·", "font-size: 13.1px; color: #a3afc0;"), bl("Harrogate", "harrogate"), t("Dot 2", "·", "font-size: 13.1px; color: #a3afc0;"),
                                                               bl("Yorkshire", "yorkshire"), t("Footer Bottom Suffix", "Emergency Plumber", "font-size: 13.1px; color: #a3afc0;")], 5, "width: auto;")],
                 12, f"width: 100%; justify-content: space-between; border-top: 1px solid {LINED}; margin-top: 44px; padding-top: 22px;")
    powered = row("Footer Powered", [t("Powered By", "Powered by", "font-size: 13.1px; color: #7d8a9c;"),
                                     box("Powered Link", [t("Powered Name", "EmmEn Tech", "font-size: 13.1px; font-weight: 700; color: #c3ccd9; &:hover { color: #ffffff; }")], "padding: 0; width: auto;", href="https://emmenntech.com/")],
                  5, "width: 100%; justify-content: center; margin-top: 18px;")
    return box("Site Footer", [wrap("Footer Wrap", [g, bottom, powered], 0, "padding-top: 64px; padding-bottom: 26px;")], "flex-direction: column; padding: 0; background-color: #04080e;", tag="footer")

# ================================================================= HOME
def home_hero():
    chips_ = row("Hero Towns", [t(f"Town {x}", x, "font-size: 14.1px; color: #d5dde8; padding: 6px 13px; border-radius: 999px; background-color: rgba(255,255,255,0.07); border: 1px solid rgba(255,255,255,0.13); backdrop-filter: blur(4px);")
                                for x in ["Leeds", "Harrogate", "York", "Huddersfield", "Halifax", "Doncaster", "Wakefield"]], 8, "justify-content: center;")
    avail = row("Hero Available", [N("e-image", "Hero Available Dot", {"image": {"src": {"url": f"{IMG}icons/dot-green.svg", "alt": ""}, "size": "full"}}, "display: block; width: 9px; height: 9px;"),
                                   t("Hero Available Text", "Engineers available now <span>· 24/7 emergency response</span>", "font-size: 14.1px; font-weight: 600; color: #e2e8f0; white-space: nowrap; & span { color: #94a3b8; font-weight: 500; } @media(--mobile) { & span { display: none; } }")],
                 10, f"flex-wrap: nowrap; width: fit-content; margin: 0 auto; padding: 7px 16px 7px 12px; {GLASS_PILL}")
    title = h("Hero Title", "Emergency Plumber<br><em>45 Minutes Away</em>", "h1",
              f"font-size: 68.8px; font-weight: 800; letter-spacing: -0.035em; line-height: 1.08; color: #ffffff; text-align: center; max-width: 16ch; margin: 0 auto; text-shadow: 0 2px 24px rgba(0,0,0,0.35); {BRUSH} @media(--tablet) {{ font-size: 56px; }} @media(--mobile) {{ font-size: 36.8px; }}")
    btns = row("Hero Buttons", [callbtn("Hero Call", "Call now · immediate response"), btn("Hero Services", "View Our Services", "services", "ghost", "lg")], 14, "justify-content: center;")
    top = wrap("Hero Wrap", [avail, title, chips_, btns, hstats(4)], 22, "align-items: center; padding-top: 72px; padding-bottom: 44px;")
    top.kids[-1].style += " margin-left: auto; margin-right: auto;"
    return box("Hero", [top, reviews_strip(), ticker()],
               f"flex-direction: column; padding: 0; background: radial-gradient(70% 60% at 50% 38%, rgba(6,11,19,0.35), rgba(6,11,19,0.85) 100%), linear-gradient(180deg, rgba(6,11,19,0.15) 0%, rgba(6,11,19,0.4) 60%, #060b13 98%), url({IMG}hero-bg.jpg) center / cover no-repeat; background-color: {INK};", tag="section")

def home():
    leeds = split("Leeds Layout",
                  col("Leeds Areas", [head("Leeds Areas", "Local engineers", "Areas We Cover in Leeds", "We provide emergency plumbing services across Leeds and surrounding areas.", left=True, mb=0, title_style="font-size: 30.4px;"),
                                      pinlist("Leeds Pins", ["Leeds City Centre", "Horsforth", "Rothwell", "Roundhay", "Pudsey", "Otley", "Headingley", "Morley", "Yeadon", "Chapel Allerton", "Garforth", "And surrounding areas"]),
                                      btn("View All Areas", "View All Areas", "areas", "line", "sm", None, "margin-top: 26px;")], 0),
                  col("Jobs Board", [head("Jobs", "Live board", "Recent Emergency Jobs in Leeds", None, left=True, mb=6, title_style="font-size: 30.4px;"), col("Jobs List", jobs(3), 12),
                                     btn("View More Jobs", "View More Jobs", "leeds", "line", "sm", None, "margin-top: 8px;")], 14), "start")
    return [home_hero(),
            sec("How It Works", "mist", [how_strip()], 56),
            sec("Services", "white", [head("Services", None, "Our <em>Emergency</em> Services", "Professional plumbing services available 24/7 across Yorkshire. We handle emergencies with speed and expertise.")] + svc_grid()),
            diag_section("mist"),
            sec("Leeds Areas And Jobs", "white", [leeds]),
            sec("Pricing Plans", "dark2", [head("Plans", None, "Choose Your <em>Response Speed</em>", "Transparent call-out options. No surprises.", dark=True)] + plans()),
            sec("Service Area", "mist", [areamap()]),
            sec("Tutorial Banner Section", "white", [slim()], 56),
            cta("Need a ", "Plumber", " Urgently?", "We're ready to respond 24/7. Call now for immediate assistance anywhere in Yorkshire.")]

# ================================================================= ABOUT
def about():
    how4 = grid("How Cards", [icon_card("How 1", "phone", "1. You call", "A real plumber answers, 24/7. We talk you through turning off the water to limit damage."),
                              icon_card("How 2", "bolt", "2. We dispatch", "Choose immediate, same-day or standard booking. Immediate response targets arrival within 45 minutes."),
                              icon_card("How 3", "pound", "3. Fixed quote", "The engineer diagnoses the problem and gives you the price before any work starts."),
                              icon_card("How 4", "shield", "4. Guaranteed repair", "We fix it properly, test it and leave it tidy. The repair is guaranteed for 12 months.")], 4, 22)
    why = split("Why Layout", col("Why", [head("Why", "Why choose us", "Why Choose RedShield Water?", None, left=True, mb=10),
                                          tlist("Why List", ["24/7 emergency call out, always answered", "Fully qualified &amp; insured engineers", "15+ years of industry experience", "Modern drain-clearing and camera equipment", "Competitive, transparent pricing", "12-month repair guarantee"])], 0),
                col("Quotes", [quote("Quote 1", "“Tonda, the engineer, was extremely professional and clearly knew exactly what he was doing. He arrived on time, explained the issue clearly, and got straight to work.”"),
                               quote("Quote 2", "“I called Redshield at about 1am on a Saturday night and was told they would be there in 15 minutes. I could not believe it!”"),
                               t("Quotes Note", 'Customers often mention our engineer Tonda by name. Read more reviews on the <a href="/">home page</a>.', f"font-size: 14.4px; color: {MUTED}; & a {{ color: {RED}; }}")], 16), "start")
    return [phero("svc-general.jpg", [("Home", "home"), "About Us"], "shield", "Yorkshire's emergency plumbing team", "The plumbers who <em>pick up at 1am</em>",
                  "RedShield Water is a local Yorkshire plumbing and drainage team. We answer the phone day and night, aim to be at your door within 45 minutes, and guarantee our repairs for 12 months.",
                  [callbtn("Hero Call", "Call now · 24/7", "md"), btn("Hero Services", "Our Services", "services", "ghost")]),
            sec("Stats Section", "dark", [stats_band()]),
            sec("Our Story", "white", [split("Story Layout", prose("Story", "Our story", "Built for the moment water goes where it shouldn't", [
                "Plumbing emergencies don't wait for office hours. A burst pipe behind the kitchen wall, a toilet overflowing at midnight or water coming through the ceiling needs someone who answers the phone and turns up fast.",
                "That's why RedShield Water exists. When you call, you speak to a real plumber who will help you <strong>isolate the water and stop further damage</strong> before we arrive. Then an engineer is dispatched straight to you, carrying the parts and equipment to fix most problems on the first visit.",
                "We cover Leeds, Harrogate, York, Huddersfield, Halifax, Doncaster, Wakefield and the rest of Yorkshire. We're fully insured, we quote before we start, and we back our repairs with a <strong>12-month guarantee</strong>."]),
                photo("Story Photo", "svc-burst.jpg", "RedShield engineer repairing a burst pipe", "pin", "Local Yorkshire engineers, no national call-centre"))]),
            sec("How We Work", "mist", [head("How We Work", "How we work", "From your call to a fixed problem"), how4]),
            sec("Why Choose Us", "white", [why]),
            cta("Speak to a ", "Real Plumber", " Now", "Day or night, a RedShield engineer is ready to help anywhere in Yorkshire.")]

# ================================================================= SERVICES
def services_page():
    return [phero("svc-leak.jpg", [("Home", "home"), "Our Services"], "wrench", "Plumbing &amp; drainage, 24/7", "Our <em>Services</em>",
                  "Emergency plumbing, leak detection, blocked drains, boilers and everyday repairs. One local team for every plumbing problem in your home or business.",
                  [callbtn("Hero Call", "Call now · 24/7", "md"), btn("Hero Pricing", "See Pricing", "pricing", "ghost")]),
            sec("Emergency Services", "white", [head("Emergency", "24/7 emergency", "Emergency Plumbing Services", "Fixed on arrival wherever possible. We stop the water first, then repair the cause.")] + svc_grid()),
            sec("Drainage", "white", [head("Drainage", "Drainage", "Drainage Services You Can Rely On", "From blocked drains to full system installations, we've got the skills and equipment to get the job done right."), drain_cards(),
                                      row("Drainage Buttons", [btn("Drainage BDS", "Blocked Drain Service", "bds", "red"), btn("Drainage LDU", "Leeds Drain Unblocking", "ldu", "line")], 14, "justify-content: center; margin-top: 34px;")]),
            cta("Not Sure What You ", "Need", "?", "Call and describe the problem. We'll tell you what to do right now and get the right engineer out.")]

# ================================================================= PRICING
def pricing_page():
    inc = split("Included Layout", col("Included", [head("Included", "What's included", "Every job, every price", None, left=True, mb=8),
                                                    tlist("Included List", ["Quote agreed before any work starts", "Call-out fee deducted from the final bill", "12-month guarantee on our workmanship", "Fully insured local engineers", "Clean-up and testing before we leave"])], 0),
                faq("pricing", "Pricing FAQ"), "start")
    return [phero("hero-bg.jpg", [("Home", "home"), "Pricing Plan"], "pound", "No hidden costs", "Simple, <em>Transparent</em> Pricing",
                  "Pick how fast you need us. You always get a quote before work starts, and the call-out fee is deducted from your final bill when you go ahead with the repair.", None, solo=True),
            sec("Pricing Plans", "dark2", [head("Plans", None, "Choose Your <em>Response Speed</em>", "Transparent call-out options. No surprises.", dark=True)] + plans(), 72, 0, "padding-top: 40px;"),
            sec("Drain Pricing", "white", [head("Drain Pricing", "Drain unblocking", "Drain Pricing", "Three response tiers. Quoted before we start. Call-out fee always deducted from the final bill."), tiers()]),
            sec("What's Included", "mist", [inc]),
            cta("Get a Price ", "Right Now", "", "Call us, describe the problem and we'll tell you the call-out and likely cost before we set off.")]

# ================================================================= AREAS
def areas_page():
    def chipcol(label, eb, title, key, link_txt, href):
        return col(label, [eyebrow(label + " Eyebrow", eb), h2(label + " Title", title, "font-size: 28.8px;"), chips(label + " Chips", key), textlink(label + " Link", link_txt + " →", href, RED, 16, False)], 16)
    return [phero("hero-kitchen.jpg", [("Home", "home"), "Service Areas"], "pin", "Yorkshire-wide coverage", "Areas We <em>Cover</em>",
                  "Fast emergency response across Yorkshire, from Leeds city centre to Harrogate, York, Huddersfield, Halifax, Doncaster and Wakefield.",
                  [callbtn("Hero Call", "Call now · 24/7", "md")], callcard("Leeds, Harrogate &amp; all of Yorkshire")),
            sec("Service Area", "white", [areamap()]),
            sec("Local Area Pages", "mist", [head("Local Areas", None, "Local Area Pages", "Tap a location to see local services, recent jobs and coverage."), area_cards(),
                                             t("Not Listed", 'Not listed? <a href="tel:+447848298987">Call us anyway</a> – we may still be able to help!', f"font-size: 16px; color: {MUTED}; text-align: center; margin-top: 28px; & a {{ color: {RED}; font-weight: 700; }}")]),
            sec("Neighbourhoods", "white", [split("Neighbourhood Layout", chipcol("Leeds Neighbourhoods", "Leeds", "Leeds neighbourhoods", "leeds", "Leeds Emergency Plumber", "leeds"),
                                                   chipcol("Harrogate Neighbourhoods", "Harrogate", "Harrogate &amp; 25-mile radius", "harrogate", "Harrogate Emergency Plumber", "harrogate"), "start")]),
            cta("Are You ", "In Our Area", "?", "If you're anywhere in Yorkshire, call us. We aim to respond within 45 minutes.")]

# ================================================================= FAQS
def faqs_page():
    return [phero("svc-drains.jpg", [("Home", "home"), "FAQs"], "alert", "Answers in plain English", "Frequently Asked <em>Questions</em>",
                  "Emergencies, response times, prices and drains. If your question isn't here, call us. It's quicker.", None, solo=True),
            sec("All FAQs", "white", [col("FAQ Column", [faq_tabs()], 0, "max-width: 860px; margin: 0 auto; width: 100%;")]),
            cta("Still Have a ", "Question", "?", f"Call 24/7 and speak to a plumber, or email {EMAIL}.")]

def faq_tabs():
    cats = [("all", "All"), ("emergency", "Emergencies"), ("pricing", "Pricing"), ("drains", "Drains"), ("areas", "Areas")]
    pill = (f"width: auto; min-width: 0; padding: 8px 14px; border-radius: 999px; border: 1px solid {LINE}; background-color: #ffffff; color: {TEXT}; cursor: pointer; "
            f"&[aria-selected=\"true\"] {{ background-color: {TEXT}; border-color: {TEXT}; color: #ffffff; }}")
    menu = N("e-tabs-menu", "FAQ Filter", {}, "display: flex; flex-wrap: wrap; gap: 8px; justify-content: flex-start;", None,
             [N("e-tab", f"FAQ Filter {name}", {}, pill, None, [t(f"FAQ Filter {name} Text", name, "font-size: 14.1px; font-weight: 600; color: inherit;")]) for _, name in cats])
    area = N("e-tabs-content-area", "FAQ Lists", {}, "", None, [N("e-tab-content", f"FAQ List {name}", {}, "padding: 0;", None, [faq(key, f"FAQ {name}")]) for key, name in cats])
    return N("e-tabs", "FAQ Tabs", {"default-active-tab": 0}, "gap: 26px;", None, [menu, area])

# ================================================================= TUTORIALS
def tutorials_page():
    right = grid("Tutorial Cards", [dcard("Tutorial Card 1", "shield", "Handle issues before they get devastating", "Minimise water damage while help is on the way."),
                                    dcard("Tutorial Card 2", "pound", "Save on hiring a plumber", "Simple household jobs you can safely do yourself.")], 2, 22, tablet=2)
    guides = grid("Guides", [guide("Stop Tap Guide", "How to turn off your stop tap", ["<strong>Find it.</strong> Usually under the kitchen sink, near the front door, or where the water pipe enters the house.",
                                                                                     "<strong>Turn it clockwise</strong> (righty-tighty) until it stops. Don't force a stiff valve with tools.",
                                                                                     "<strong>Open the cold taps</strong> to drain water left in the pipes.", "<strong>Still running?</strong> Check for an outside stop tap near the boundary, then call us."]),
                             guide("Electrics Guide", "Water near electrics or a ceiling bulging?", ["<strong>Switch off electrics</strong> at the consumer unit if water is near sockets or light fittings, as long as it's safe to reach.",
                                                                                                     "<strong>Keep out from under</strong> a sagging ceiling. Move valuables out of the room.", "<strong>Catch the water</strong> with buckets and towels. Turn off the stop tap.",
                                                                                                     f"<strong>Call {PHONE}.</strong> We'll talk you through the next step while the engineer travels."])], 2, 28)
    return [phero("svc-burst.jpg", [("Home", "home"), "Free Safety Tutorials"], "playc", "Free Video Tutorials", "Plumbing Safety &amp; <em>DIY Tutorials</em>",
                  "Learn essential skills to minimise water damage and protect your home while waiting for professional help.",
                  [btn("Hero YouTube", "Watch All Videos on YouTube", "https://www.youtube.com/@RedShieldWater", "red", "md", "yt")], right),
            sec("Tutorial Videos", "white", [head("Videos", "Water control &amp; damage prevention", "DIY Plumbing Safety Tutorials"), videos(4)]),
            sec("Quick Guides", "mist", [guides]),
            cta("Can't Stop the ", "Water", "?", "Call now. A plumber will talk you through it while an engineer is on the way.")]

# ================================================================= CONTACT
def contact_page():
    body_ = split("Contact Layout", col("Contact Info", [head("Contact", "Reach us directly", "Get in touch", None, left=True, mb=0, title_style="font-size: 32px;"), contact_tiles()], 18),
                  msgform("Contact Form"), "start")
    area = split("Contact Area Layout", map_box(), prose("Contact Area", "Our service area", "Covering all of Yorkshire, from the Dales to the coast",
                                                          ["Leeds, Harrogate, York, Huddersfield, Halifax, Doncaster, Wakefield and surrounding towns and villages."],
                                                          btn("Contact Area Button", "View All Areas", "areas", "ghost"), dark=True))
    return [phero("hero-kitchen.jpg", [("Home", "home"), "Contact Us"], None, "● Available Right Now", "Contact <em>RedShield Water</em>",
                  "For emergencies, calling is always the fastest option. We aim to respond within 45 minutes across Yorkshire.", None, solo=True,
                  extra=None),
            sec("Contact Section", "white", [body_]),
            sec("Contact Area", "dark", [area], 56)]

# ================================================================= LEEDS
def leeds_page():
    hero = phero("hero-kitchen.jpg", [("Home", "home"), ("Areas", "areas"), "Leeds"], "clock", "24/7 Emergency Response", "Emergency Plumber <em>Leeds</em>",
                 "<strong>45-Minute Response for Burst Pipes, Leaks, Blocked Toilets &amp; Urgent Plumbing Repairs.</strong> Speak to a real plumber now. We'll help you isolate the issue and stop further damage before we arrive.",
                 [callbtn("Hero Call", "Call now · 24/7"), btn("Hero Contact", "Request a Call Back", "contact", "ghost", "lg")])
    hero.kids.append(reviews_strip())
    cov = split("Coverage Layout", col("Coverage", [eyebrow("Coverage Eyebrow", "Coverage"), h2("Coverage Title", "Areas We Cover in Leeds", "", True), lead("Coverage Lead", "Local engineers covering Leeds and surrounding neighbourhoods.", "", True),
                                                    chips("Coverage Chips", "leeds", True), t("Coverage More", "…and many more areas across Leeds.", f"font-size: 14.4px; color: {MUTEDD};")], 16),
                col("Leeds Jobs", [eyebrow("Leeds Jobs Eyebrow", "Live board"), h2("Leeds Jobs Title", "Recent Emergency Plumbing Jobs in Leeds", "font-size: 28.8px;", True), col("Leeds Jobs List", jobs(3, True), 12)], 12), "start")
    fq = cgrid("Leeds FAQ Layout", [col("Leeds FAQ", [eyebrow("Leeds FAQ Eyebrow", "Emergency plumbing FAQs"), h2("Leeds FAQ Title", "Emergency plumbing in Leeds, your questions answered"),
                                                      col("Leeds FAQ List", [faq("leeds", "Leeds Questions")], 0, "margin-top: 8px;")], 14), callback("Request Emergency Call Back", "Leeds Callback")],
               "minmax(0, 1.5fr) minmax(0, 1fr)", 36, "align-items: start;")
    return [hero,
            sec("Leeds Videos", "white", [head("Leeds Videos", "While you wait", "Emergency DIY Tips While You Wait", "Minimise damage before our team arrives."), videos(4)]),
            sec("Leeds Repairs", "mist", [split("Leeds Prose Layout", prose("Leeds Prose", "Leeds plumbing", "24/7 Plumbing Repairs in Leeds", [
                "RedShield Water provides emergency plumbing repairs across Leeds for burst pipes, leaking ceilings, blocked toilets, water leaks, overflowing toilets, blocked drains, no hot water, and urgent plumbing issues. We aim to arrive within <strong>45 minutes</strong> where available and provide insured repairs with a <strong>12-month workmanship guarantee</strong>.",
                "Our engineers cover Leeds City Centre, Headingley, Roundhay, Chapel Allerton, Horsforth, Pudsey, Morley, Rothwell, Garforth, Otley, Yeadon and nearby areas."],
                btn("Leeds Prose Call", "Call Now", TEL, "red", "md", "phone")), photo("Leeds Photo", "hero-kitchen.jpg", "Kitchen plumbing repair in Leeds", "clock", "Typical Leeds arrival: 45 minutes"))]),
            sec("Leeds Services", "white", [head("Leeds Services", None, "Emergency Plumbing Services in Leeds", "Fast, insured emergency response for every common plumbing problem in Leeds."), problems("Leeds")]),
            sec("Leeds Coverage", "dark2", [cov]),
            sec("Leeds FAQs", "mist", [fq]),
            cta("Need a Plumber in ", "Leeds", " Right Now?", "Burst pipe, blocked toilet, water leak or leaking ceiling? Don't wait. Call RedShield Water now for fast plumbing help across Leeds.")]

# ================================================================= HARROGATE
def harrogate_page():
    hero = phero("hero-kitchen.jpg", [("Home", "home"), ("Areas", "areas"), "Harrogate"], "clock", "24/7 Emergency Response", "Emergency Plumber <em>Harrogate</em>",
                 "Serving all Harrogate areas including Starbeck, Bilton, Knaresborough, Pannal, Killinghall, Hampsthwaite, Boroughbridge &amp; more.",
                 [callbtn("Hero Call", "Call now · 24/7"), btn("Hero Contact", "Send a Message", "contact", "ghost", "lg")], callcard("Harrogate &amp; all surrounding areas"))
    hero.kids.append(reviews_strip())
    return [hero,
            sec("Harrogate Videos", "white", [split("Harrogate Videos Layout", col("Harrogate Videos Text", [eyebrow("HV Eyebrow", "While you wait"), h2("HV Title", "Emergency DIY Tips While You Wait"), lead("HV Lead", "Learn how to minimise damage before our team arrives.")], 16),
                                                     videos(2, 1, 2))]),
            sec("Harrogate Coverage", "dark2", [split("Harrogate Coverage Layout", map_box("harrogate"),
                                                      col("Harrogate Coverage Text", [eyebrow("HC Eyebrow", "Coverage"), h2("HC Title", "We Cover Harrogate", "", True), lead("HC Lead", "Serving Harrogate and all surrounding areas within a 25-mile radius.", "", True), chips("HC Chips", "harrogate", True)], 16))]),
            diag_section("mist"),
            sec("Harrogate FAQs", "white", [col("Harrogate FAQ Column", [head("Harrogate FAQ", None, "Frequently Asked Questions", "Emergency plumbing in Harrogate, your questions answered."), faq("harrogate", "Harrogate Questions")], 0, "max-width: 860px; margin: 0 auto; width: 100%;")]),
            cta("Need an Emergency Plumber in ", "Harrogate", "?", "Don't wait for a small leak to become expensive damage. Burst pipe, blocked toilet, leaking tap or water through the ceiling? Call now.")]

# ================================================================= YORKSHIRE
def yorkshire_page():
    return [phero("hero-kitchen.jpg", [("Home", "home"), ("Areas", "areas"), "Yorkshire"], "clock", "24/7 Emergency Response", "Need an <em>Emergency Plumber</em> in Yorkshire?",
                  "We serve the whole of West Yorkshire and all surrounding areas, including Leeds, Harrogate, York, Huddersfield, Halifax, Doncaster, Wakefield &amp; more.",
                  [callbtn("Hero Call", "Call now · 24/7"), btn("Hero Contact", "Send a Message", "contact", "ghost", "lg")], callcard("Yorkshire wide coverage")),
            sec("Yorkshire Videos", "white", [head("Yorkshire Videos", None, "Emergency DIY Tips While You Wait", "Learn how to minimise damage before our team arrives."), videos(4)]),
            sec("Yorkshire About", "mist", [split("Yorkshire Prose Layout", prose("Yorkshire Prose", "Yorkshire plumbers", "24/7 plumbing across Yorkshire", [
                "When a plumbing emergency strikes in Yorkshire, you need a fast, reliable expert who can respond immediately. At RedShield Water, we provide <strong>24/7 plumbing services across Yorkshire</strong>, including Leeds, Wakefield, Huddersfield, Halifax, and surrounding areas.",
                "Whether you're dealing with burst pipes, blocked drains, leaking boilers, overflowing toilets, or sudden loss of water, our experienced team is ready to attend quickly and resolve the issue before it causes costly damage.",
                "We prioritise rapid response times, transparent pricing, and long-lasting repairs. If you're searching for a “plumber near me” in Yorkshire, trust our local team to deliver professional, efficient, and affordable solutions when you need them most."]), map_box())]),
            sec("Yorkshire Contact", "mist", [split("Yorkshire Contact Layout", col("Yorkshire Contact Info", [head("Yorkshire Contact", "Reach us directly", "For emergencies, calling is always fastest", None, left=True, mb=0, title_style="font-size: 32px;"),
                                                                                                         contact_tiles("Yorkshire wide coverage")], 18), msgform("Yorkshire Form", False, False), "start")]),
            cta("Plumbing Emergency in ", "Yorkshire", "?", "We aim to respond within 45 minutes across Yorkshire. Call now.")]

# ================================================================= LEEDS DRAIN UNBLOCKING
def ldu_page():
    cards = grid("Blockage Cards", [icon_card("Blockage 1", "toilet", "Blocked Toilets", "Fast clearance of blocked or overflowing toilets, sanitised, no mess left behind."),
                                    icon_card("Blockage 2", "tap", "Blocked Sinks &amp; Showers", "Kitchen sinks, bathroom basins and shower trays cleared with the right tool for the job."),
                                    icon_card("Blockage 3", "bolt", "Powerful Water Jetting", "A strong jet of water clears grease, roots and dirt that a plunger can't shift."),
                                    icon_card("Blockage 4", "drain", "Outside Drains &amp; Manholes", "Blocked outside drains, drain covers and manholes cleared across Leeds.")], 4, 22)
    why = split("LDU Why Layout", col("LDU Why", [head("LDU Why", "Why Leeds calls us first", "Why Leeds Calls RedShield First", None, left=True, mb=8),
                                                  tlist("LDU Why List", ["Powerful drain-clearing equipment on every van", "Camera checks inside the pipe if a drain keeps blocking", "Fixed-fee quotes before any work starts",
                                                                         "Local Leeds engineers, no national call-centre delays", "Fully insured, guaranteed workmanship", "24/7 line for sewage, flooding &amp; overflows"])], 0),
                ba_box("LDU Compare", "drain", 16))
    return [phero("drain-maint.jpg", [("Home", "home"), ("Services", "services"), "Leeds Drain Unblocking"], "clock", "24/7 Emergency Drain Unblocking", "Drain Unblocking <em>Leeds</em>",
                  "Blocked toilet, sink, shower or outside drain? Our Leeds drainage team responds in 45 minutes with high-pressure jetting and fixed-fee pricing.",
                  [callbtn("Hero Call", "Call now · 24/7"), btn("Hero Pricing", "See Pricing", "pricing", "ghost", "lg")], callcard("Leeds &amp; surrounding areas")),
            sec("Blockages", "white", [head("Blockages", None, "Every Blockage. <em>Cleared Today.</em>", "From a single slow sink to a full sewage backup, Leeds homes and businesses trust us to clear it on the first visit."), cards]),
            sec("LDU Pricing", "mist", [head("LDU Pricing", None, "Transparent Leeds Drain Pricing", "Three response tiers. Quoted before we start. Call-out fee always deducted from the final bill."), tiers()]),
            sec("LDU Why Section", "white", [why]),
            sec("LDU FAQs", "mist", [col("LDU FAQ Column", [head("LDU FAQ", None, "Drain Unblocking Leeds – FAQs"), faq("ldu", "LDU Questions")], 0, "max-width: 860px; margin: 0 auto; width: 100%;")]),
            cta("Blocked Drain in ", "Leeds", "? Call Now.", "45-minute emergency response, 24 hours a day, across Leeds.")]

# ================================================================= BLOCKED DRAIN SERVICE
def bds_page():
    def mrow(i, icon, title, text):
        return row(f"Maint {i}", [icbox(f"Maint {i} Icon", icon, "red", REDS, 44, 10, 19), col(f"Maint {i} Text", [t(f"Maint {i} Title", title, f"font-size: 16.8px; font-weight: 700; color: {TEXT};"), body(f"Maint {i} Body", text, 13.6)], 2, "flex: 1;")],
                   14, f"flex-wrap: nowrap; align-items: flex-start; padding: 18px; border-radius: 12px; border: 1px solid {LINE}; background-color: #ffffff; {SH}")
    maint = col("Maintenance Card", [eyebrow("Maintenance Eyebrow", "Maintenance"), h3("Maintenance Title", "Prevent Problems Before They Start", 24),
                                     body("Maintenance Lead", "Regular maintenance can save you time, money and stress by preventing costly drainage issues."),
                                     mrow(1, "shield", "Avoid Blockages", "Keep your system clear and flowing with regular checks."), mrow(2, "clock", "Extend Lifespan", "Proper care extends the life of your drains and pipes."),
                                     mrow(3, "pound", "Save Money", "Prevent expensive repairs down the line with proactive care."), btn("Maintenance Book", "Book Maintenance", "contact", "line")], 14,
                f"background-color: #ffffff; border: 1px solid {LINE}; border-radius: 14px; padding: 30px; {SH}")
    why = split("BDS Why Layout", col("BDS Why", [head("BDS Why", "Why choose us", "Why Choose RedShield Water?", None, left=True, mb=8),
                                                  tlist("BDS Why List", ["24/7 Emergency Call Out", "Fully Qualified &amp; Insured", "15+ Years of Industry Experience", "State-of-the-Art Equipment", "Competitive Pricing", "Customer Satisfaction Guaranteed"]),
                                                  btn("BDS About", "More About Us", "about", "red", "md", None, "margin-top: 18px;")], 0), maint, "start")
    extra = t("Hero Tagline", "Fast. Reliable. Professional.", "font-size: 20.8px; font-weight: 700; color: #ffffff;")
    return [phero("svc-drains.jpg", [("Home", "home"), ("Services", "services"), "Blocked Drain Service"], None, None, "Expert Drainage <em>Solutions</em>",
                  "We provide a full range of drainage services including unblocking, repairs, installations and maintenance for homes and businesses across Yorkshire.",
                  [btn("Hero Services", "Our Services", "services", "red"), btn("Hero Quote", "Get A Quote", "contact", "ghost")], callcard("Homes &amp; businesses across Yorkshire"), extra=extra),
            sec("Drain Services", "white", [head("Drain Services", "Our services", "Drainage Services You Can Rely On", "From blocked drains to full system installations, we've got the skills and equipment to get the job done right. Drag the photos to compare before and after."), drain_cards()]),
            sec("BDS Why Section", "mist", [why]),
            sec("BDS Pricing", "white", [head("BDS Pricing", None, "Drain Pricing", "Quoted before we start. Call-out fee deducted from the final bill."), tiers()]),
            cta("Need Help With Your ", "Drains", "?", "Get in touch today for fast, friendly and professional service.")]

PAGES = {"home": home, "about": about, "services": services_page, "pricing": pricing_page, "areas": areas_page, "faqs": faqs_page, "tutorials": tutorials_page,
         "contact": contact_page, "leeds": leeds_page, "harrogate": harrogate_page, "yorkshire": yorkshire_page, "ldu": ldu_page, "bds": bds_page}
PARTS = {"header": (40, header), "footer": (41, footer)}

if __name__ == "__main__":
    key = sys.argv[1]; dry = "--dry" in sys.argv; pub = "--publish" in sys.argv
    if key in PARTS: push(PARTS[key][0], [PARTS[key][1]()], dry, pub)
    else: push(P[key], PAGES[key](), dry, pub)
