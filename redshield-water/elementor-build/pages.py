import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from rs import *

def home_hero():
    towns = row("Hero Towns", [p(f"Town Chip {t}", t, style="font-family: var(--rs-font); font-size: 14px; color: #d5dde8; padding: 6px 13px; border-radius: 999px; background-color: rgba(255,255,255,0.07); border: 1px solid rgba(255,255,255,0.14);")
                               for t in ["Leeds", "Harrogate", "York", "Huddersfield", "Halifax", "Doncaster", "Wakefield"]], 8, "justify-content: center;")
    kids = [p("Hero Badge", "<b>●</b>&nbsp; Engineers available now · 24/7 emergency response", ["rs-b-green"],
              style="font-family: var(--rs-font); font-size: 14px; font-weight: 600; color: #e2e8f0; padding: 7px 16px; border-radius: 999px; " + GLASS + " width: fit-content; margin: 0 auto;"),
            h("Hero Title", "Emergency Plumber<br><em>45 Minutes Away</em>", "h1",
              style="& em { text-decoration: underline; text-decoration-thickness: 5px; text-underline-offset: 12px; } font-family: var(--rs-font); font-size: 66px; font-weight: 800; letter-spacing: -0.035em; line-height: 1.12; color: #ffffff; text-align: center; text-shadow: 0 2px 24px rgba(0,0,0,0.35); @media(--tablet) { font-size: 52px; } @media(--mobile) { font-size: 38px; }"),
            towns,
            row("Hero Buttons", [btn("Hero Call Button", f"📞 Call Now – {PHONE}", TEL, style="font-size: 18px; padding: 18px 30px;"), ghost("Hero Services Button", "View Our Services", "services")], 12, "justify-content: center;"),
            stats(4)]
    kids[-1].style += " margin: 6px auto 0; width: 100%;"
    inner = col("Hero Content", kids, 22, "align-items: center; max-width: 1000px; margin: 0 auto; padding: 0 20px;")
    return flex("Hero", [inner], f"flex-direction: column; padding: 80px 0 64px; background: radial-gradient(70% 60% at 50% 38%, rgba(6,11,19,0.35), rgba(6,11,19,0.85) 100%), url({IMG}hero-bg.jpg) center / cover no-repeat; @media(--mobile) {{ padding: 52px 0 44px; }}", tag="section")

def home():
    return [home_hero(), reviews("dark"), how3(), services("white"), issues_and_call(), leeds_areas_jobs("white"), plans(), area_map("mist"), slim_tutorials(),
            cta("Need a ", "Plumber", " Urgently?", "We're ready to respond 24/7. Call now for immediate assistance anywhere in Yorkshire.")]

PAGES = {"home": home}


# ======================================================= header / footer
NAV = [("Home", "home"), ("About", "about"), ("Services", "services"), ("Pricing", "pricing"), ("Areas", "areas"), ("FAQs", "faqs"), ("Contact", "contact")]
NAVST = "font-family: var(--rs-font); font-size: 15px; font-weight: 500; color: #c3ccd9; background-color: transparent; padding: 8px 10px; border-radius: 0; white-space: nowrap; flex-shrink: 0; &:hover { color: #ffffff; }"
def header():
    logo = row("Logo", [img("Logo Mark", "logo.svg", "RedShield Water", "width: 32px; min-width: 32px; flex-shrink: 0; @media(--mobile) { width: 26px; min-width: 26px; }"),
                        p("Logo Text", "<em>Red</em>Shield <b>Water</b>", ["rs-em-red"], "font-family: var(--rs-font); font-size: 21px; font-weight: 800; letter-spacing: -0.02em; color: #ffffff; white-space: nowrap; & b { color: #2b8fe3; } @media(--mobile) { font-size: 17px; }")],
               9, "flex-wrap: nowrap; width: auto; flex: 0 0 auto;", href="home")
    nav = row("Main Menu", [btn(f"Menu {t}", t, k, (), NAVST) for t, k in NAV] +
              [btn("Menu Safety Videos", "▶ Safety Videos", "tutorials", (), NAVST + " border: 1px solid rgba(255,255,255,0.18); border-radius: 999px; padding: 6px 14px; margin-left: 6px;")], 2,
              "flex-wrap: nowrap; width: auto; flex: 1 1 auto; justify-content: center; @media(--tablet) { display: none; }", tag="nav")
    call_b = btn("Header Call", f"📞 {PHONE}", TEL, style="font-size: 15px; padding: 11px 18px; white-space: nowrap; flex-shrink: 0; @media(--mobile) { font-size: 13px; padding: 9px 12px; }")
    bar = row("Header Bar", [logo, nav, call_b], 16, "flex-wrap: nowrap; justify-content: space-between; max-width: 1260px; margin: 0 auto; padding: 0 20px; min-height: 62px;")
    mob = row("Mobile Menu", [btn(f"Mobile {t}", t, k, (), NAVST + " font-size: 14px; padding: 6px 9px;") for t, k in NAV + [("Videos", "tutorials")]], 2,
              "display: none; justify-content: center; flex-wrap: wrap; padding: 2px 12px 10px; @media(--tablet) { display: flex; }", tag="nav")
    return flex("Site Header", [bar, mob], "flex-direction: column; padding: 0; background-color: rgba(6,11,19,0.97); border-bottom: 1px solid #1c2636; position: sticky; top: 0; z-index: 50;", tag="header")

def footer():
    FT = "font-family: var(--rs-font); font-size: 15px; color: #a3afc0; background-color: transparent; padding: 3px 0; text-align: left; &:hover { color: #ffffff; }"
    H4 = "font-family: var(--rs-font); font-size: 16px; font-weight: 700; color: #ffffff; margin-bottom: 6px;"
    c1 = col("Footer Brand", [p("Footer Logo", "<em>Red</em>Shield <b>Water</b>", ["rs-em-red"], "font-family: var(--rs-font); font-size: 22px; font-weight: 800; color: #ffffff; & b { color: #2b8fe3; }"),
                              p("Footer About", "24/7 emergency plumbing services across Yorkshire. Fast response, guaranteed work, no hidden costs.", style="font-family: var(--rs-font); font-size: 15px; line-height: 1.6; color: #a3afc0;"),
                              p("Footer Rating", "<strong>★★★★★ Trustpilot</strong>", ["rs-strong-green"], "font-family: var(--rs-font); font-size: 15px;")], 12)
    c2 = col("Footer Services", [h("Footer Services Title", "Services", "h4", style=H4)] + [btn(f"Footer S {t}", t, k, (), FT) for t, k in
             [("Burst pipes", "services"), ("Leak detection", "services"), ("Blocked drains", "bds"), ("Boiler repairs", "services"), ("Leeds drain unblocking", "ldu")]], 4)
    c3 = col("Footer Company", [h("Footer Company Title", "Company", "h4", style=H4)] + [btn(f"Footer C {t}", t, k, (), FT) for t, k in
             [("About us", "about"), ("Pricing plan", "pricing"), ("Service areas", "areas"), ("FAQs", "faqs"), ("Free safety tutorials", "tutorials"), ("Contact us", "contact")]], 4)
    c4 = col("Footer Contact", [h("Footer Contact Title", "Contact", "h4", style=H4), btn("Footer Phone", f"📞 {PHONE}", TEL, (), FT + " font-size: 18px; font-weight: 700; color: #ffffff;"),
                                btn("Footer Email", f"✉ {EMAIL}", f"mailto:{EMAIL}", (), FT), p("Footer Area", "📍 Yorkshire, UK<br>🕒 Open 24 hours, 7 days", style="font-family: var(--rs-font); font-size: 15px; line-height: 1.9; color: #a3afc0;"),
                                btn("Footer YouTube", "▶ YouTube tutorials", "https://www.youtube.com/@RedShieldWater", (), FT)], 6)
    g = N("e-grid", "Footer Columns", {}, "grid-template-columns: 1.4fr 1fr 1fr 1.2fr; grid-template-rows: auto; gap: 36px; padding: 0; @media(--tablet) { grid-template-columns: repeat(2, minmax(0, 1fr)); } @media(--mobile) { grid-template-columns: minmax(0, 1fr); }", None, [c1, c2, c3, c4])
    bottom = row("Footer Bottom", [p("Copyright", "© 2026 RedShield Water. All rights reserved.", style="font-family: var(--rs-font); font-size: 13px; color: #8a96a8;"),
                                   row("Footer Local Links", [btn(f"Footer L {t}", f"{t} Emergency Plumber", k, (), FT + " font-size: 13px;") for t, k in [("Leeds", "leeds"), ("Harrogate", "harrogate"), ("Yorkshire", "yorkshire")]], 14)],
                 12, "justify-content: space-between; border-top: 1px solid #1c2636; padding-top: 20px;")
    return flex("Site Footer", [wrap("Footer Inner", [g, bottom], 36)], "flex-direction: column; padding: 64px 0 26px; background-color: #04080e;", tag="footer")

# ======================================================= inner pages
def about():
    nums = grid("About Numbers", [col(f"Number {i}", [p(f"Number {i} Value", v, style="font-family: var(--rs-font); font-size: 38px; font-weight: 800; color: #ffffff;"),
                                                      p(f"Number {i} Label", l, style="font-family: var(--rs-font); font-size: 15px; color: #aab5c5;")], 4, "", ["rs-card-dark"])
                                  for i, (v, l) in enumerate([(f"24{red('/')}7", "Emergency line, every day of the year"), (f"45{red(' min')}", "Target arrival across Yorkshire"),
                                                              (f"12{red(' mo')}", "Guarantee on our repairs"), (f"15{red('+')}", "Years of industry experience")])], 4, 16)
    story = two_col("Story", col("Story Text", [p("Story Eyebrow", "Our story", ["rs-eyebrow"]), h("Story Title", "Built for the moment water goes where it shouldn't", "h2", ["rs-h2"]),
        p("Story P1", "Plumbing emergencies don't wait for office hours. A burst pipe behind the kitchen wall, a toilet overflowing at midnight or water coming through the ceiling needs someone who answers the phone and turns up fast.", ["rs-lead"]),
        p("Story P2", "When you call RedShield, you speak to a real plumber who helps you <strong>turn off the water and limit the damage</strong> before we arrive. Then an engineer comes straight to you with the parts to fix most problems on the first visit.", ["rs-lead"]),
        p("Story P3", "We cover Leeds, Harrogate, York, Huddersfield, Halifax, Doncaster, Wakefield and the rest of Yorkshire. We're fully insured, we quote before we start, and our repairs come with a <strong>12-month guarantee</strong>.", ["rs-lead"])], 16),
        img("Story Photo", "svc-burst.jpg", "RedShield engineer repairing a burst pipe", "border-radius: 16px; aspect-ratio: 4 / 3; object-fit: cover;"))
    why = two_col("Why", col("Why Text", [p("Why Eyebrow", "Why choose us", ["rs-eyebrow"]), h("Why Title", "Why Choose RedShield Water?", "h2", ["rs-h2"]),
        why_list("Why List", ["24/7 emergency call out, always answered", "Fully qualified &amp; insured engineers", "15+ years of industry experience", "Modern drain-clearing and camera equipment", "Clear prices, agreed before we start", "12-month repair guarantee"])], 14),
        col("Quotes", [col(f"Quote {i}", [p(f"Quote {i} Stars", "<strong>★★★★★</strong>", ["rs-strong-green"]), p(f"Quote {i} Text", q, ["rs-body"], "font-size: 16px; color: var(--rs-text);"),
                                            p(f"Quote {i} By", "Verified Trustpilot reviewer", ["rs-body"], "font-size: 13px;")], 8, "", ["rs-card"]) for i, q in enumerate([
            "“Tonda, the engineer, was extremely professional and clearly knew exactly what he was doing. He arrived on time, explained the issue clearly, and got straight to work.”",
            "“I called Redshield at about 1am on a Saturday night and was told they would be there in 15 minutes. I could not believe it!”"])], 16), "1fr 1fr", "start")
    return [hero("Home / About Us", "🛡 Yorkshire's emergency plumbing team", f"The plumbers who {red('pick up at 1am')}",
                 "RedShield Water is a local Yorkshire plumbing and drainage team. We answer day and night, aim to be at your door within 45 minutes, and guarantee our repairs for 12 months.",
                 "svc-general.jpg", [call_btn(), ghost("Hero Services Button", "Our Services", "services")]),
            section("About Numbers Section", "dark", [nums], 0, "padding: 48px 0;"), section("Our Story", "white", [story]), how3(), section("Why Choose Us", "white", [why]),
            cta("Speak to a ", "Real Plumber", " Now", "Day or night, a RedShield engineer is ready to help anywhere in Yorkshire.")]

def drain_cards():
    items = [("Drain Unblocking", "Blocked drains cleared fast, usually in minutes, not hours.", "drain-after.jpg"),
             ("Drain Repairs", "Cracked pipes and roots in drains fixed properly.", "pipe-after.jpg"),
             ("Drain Installations", "New pipework, connections and full system upgrades built to last.", "drain-install.jpg"),
             ("Drain Maintenance", "Regular checks that stop blockages before they happen.", "drain-maint.jpg")]
    return grid("Drain Cards", [col(f"Drain {i}", [img(f"Drain {i} Photo", f, t, "aspect-ratio: 4 / 3; object-fit: cover;"),
                                                   col(f"Drain {i} Body", [h(f"Drain {i} Title", t, "h3", ["rs-h3"]), p(f"Drain {i} Text", d, ["rs-body"], "font-size: 15px;"),
                                                                           btn(f"Drain {i} Link", "Get a quote →", "contact", (), "font-family: var(--rs-font); font-size: 14px; font-weight: 700; color: #b91c1c; background-color: transparent; padding: 0; text-align: left;")], 8, "padding: 20px;")],
                                    0, "padding: 0; overflow: hidden;", ["rs-card"]) for i, (t, d, f) in enumerate(items, 1)], 4, 20)

def services_page():
    return [hero("Home / Our Services", "🔧 Plumbing &amp; drainage, 24/7", f"Our {red('Services')}",
                 "Emergencies, leaks, blocked drains, boilers and everyday repairs. One local team for every plumbing problem in your home or business.",
                 "svc-leak.jpg", [call_btn(), ghost("Hero Pricing Button", "See Pricing", "pricing")]),
            services("mist", "24/7 emergency", "Emergency Plumbing Services", "Fixed on arrival wherever possible. We stop the water first, then repair the cause."),
            section("Drainage", "white", [head("Drainage", "Drainage", "Drainage Services You Can Rely On", "From blocked drains to full system installations, we've got the skills and equipment to get the job done right."),
                                          drain_cards(), row("Drainage Links", [btn("Drainage BDS", "Blocked Drain Service", "bds"), btn("Drainage LDU", "Leeds Drain Unblocking", "ldu", ("rs-btn-line",))], 12, "justify-content: center;")]),
            cta("Not Sure What You ", "Need", "?", "Call and describe the problem. We'll tell you what to do right now and send the right engineer.")]

def pricing_page():
    inc = two_col("Included", col("Included Text", [p("Included Eyebrow", "What's included", ["rs-eyebrow"]), h("Included Title", "Every job, every price", "h2", ["rs-h2"]),
        why_list("Included List", ["Price agreed before any work starts", "Call-out fee taken off the final bill", "12-month guarantee on our workmanship", "Fully insured local engineers", "Clean-up and testing before we leave"])], 14),
        accordion("Pricing FAQ", [(q, a) for c, q, a in D["FAQ"] if "pricing" in c.split()]), "1fr 1fr", "start")
    return [hero("Home / Pricing Plan", "£ No hidden costs", f"Simple, {red('Transparent')} Pricing",
                 "Pick how fast you need us. You always get the repair price before work starts, and the call-out fee comes off your final bill when you go ahead.",
                 "hero-bg.jpg", [call_btn()], solo=True),
            plans(), tiers("mist"), section("What's Included", "white", [inc]),
            cta("Get a Price ", "Right Now", "", "Describe the problem on the phone and we'll tell you the call-out and likely cost before we set off.")]

def areas_page():
    cards = [col(f"Area {t}", [h(f"Area {t} Title", f"📍 {t}", "h3", ["rs-h3"]), p(f"Area {t} Text", d, ["rs-body"], "font-size: 15px;"),
                               p(f"Area {t} Link", "View area →", style="font-family: var(--rs-font); font-size: 14px; font-weight: 700; color: #b91c1c;")], 6, "", ["rs-card"],
                 href=P[HASH2P[hh]]) for t, d, hh in D["AREAS"]]
    chipcards = two_col("Area Chips", col("Leeds Chip Card", [p("Leeds Chip Eyebrow", "Leeds", ["rs-eyebrow"]), h("Leeds Chip Title", "Leeds neighbourhoods", "h3", ["rs-h3"], "font-size: 24px;"), chips("Leeds Neighbourhoods", "leeds"),
                                                          btn("Leeds Chip Link", "Leeds Emergency Plumber →", "leeds", ("rs-btn-line",), "width: fit-content;")], 14, "", ["rs-card"]),
                        col("Harrogate Chip Card", [p("Harrogate Chip Eyebrow", "Harrogate", ["rs-eyebrow"]), h("Harrogate Chip Title", "Harrogate &amp; 25-mile radius", "h3", ["rs-h3"], "font-size: 24px;"), chips("Harrogate Areas", "harrogate"),
                                                    btn("Harrogate Chip Link", "Harrogate Emergency Plumber →", "harrogate", ("rs-btn-line",), "width: fit-content;")], 14, "", ["rs-card"]), "1fr 1fr", "start")
    return [hero("Home / Service Areas", "📍 Yorkshire-wide coverage", f"Areas We {red('Cover')}",
                 "Fast emergency response across Yorkshire, from Leeds city centre to Harrogate, York, Huddersfield, Halifax, Doncaster and Wakefield.",
                 "hero-kitchen.jpg", [call_btn()]),
            area_map("white"), section("Local Area Pages", "mist", [head("Local Areas", "Local pages", "Local Area Pages", "Tap a location to see local services, recent jobs and coverage."), grid("Area Cards", cards, 4, 18)]),
            section("Neighbourhoods", "white", [chipcards]),
            cta("Are You ", "In Our Area", "?", "If you're anywhere in Yorkshire, call us. We aim to respond within 45 minutes.")]

def faqs_page():
    groups = [("emergency", "Emergencies"), ("pricing", "Prices"), ("drains", "Drains"), ("areas", "Areas")]
    seen, blocks = set(), []
    for key, name in groups:
        items = [(q, a) for c, q, a in D["FAQ"] if key in c.split() and q not in seen]
        seen.update(q for q, _ in items)
        if items: blocks += [h(f"FAQ Group {name}", name, "h3", ["rs-h3"], "font-size: 22px; margin-top: 18px;"), accordion(f"FAQ {name}", items)]
    return [hero("Home / FAQs", "❓ Answers in plain English", f"Frequently Asked {red('Questions')}",
                 "Emergencies, response times, prices and drains. If your question isn't here, call us. It's quicker.", "svc-drains.jpg", [call_btn()], solo=True),
            section("All FAQs", "mist", [col("FAQ Groups", blocks, 12, "max-width: 860px; margin: 0 auto; width: 100%;")]),
            cta("Still Have a ", "Question", "?", f"Call 24/7 and speak to a plumber, or email {EMAIL}.")]

def guide(label, title, steps):
    return col(label, [p(label + " Eyebrow", "Quick guide", ["rs-eyebrow"]), h(label + " Title", title, "h3", ["rs-h3"], "font-size: 24px;"),
                       p(label + " Steps", "<ol>" + "".join(f"<li>{s}</li>" for s in steps) + "</ol>", ["rs-body"], "font-size: 16px; line-height: 1.8;")], 10, "padding: 30px;", ["rs-card"])

def tutorials_page():
    g = two_col("Guides", guide("Stop Tap Guide", "How to turn off your stop tap", ["<strong>Find it.</strong> Usually under the kitchen sink, near the front door, or where the water pipe comes into the house.",
                                                                                    "<strong>Turn it clockwise</strong> until it stops. Don't force a stiff tap with tools.", "<strong>Open the cold taps</strong> to drain the water left in the pipes.",
                                                                                    "<strong>Still running?</strong> Look for an outside stop tap near your boundary, then call us."]),
                guide("Electrics Guide", "Water near electrics or a sagging ceiling?", ["<strong>Switch off the electrics</strong> at the fuse box if water is near sockets or lights, and it's safe to reach.",
                                                                                        "<strong>Stay out from under</strong> a sagging ceiling. Move valuables out of the room.", "<strong>Catch the water</strong> with buckets and towels, and turn off the stop tap.",
                                                                                        f"<strong>Call {PHONE}.</strong> We'll talk you through it while the engineer travels."]), "1fr 1fr", "start")
    return [hero("Home / Free Safety Tutorials", "▶ Free video tutorials", f"Plumbing Safety &amp; {red('DIY Tutorials')}",
                 "Learn essential skills to minimise water damage and protect your home while waiting for professional help.", "svc-burst.jpg",
                 [btn("Hero YouTube", "▶ Watch All Videos on YouTube", "https://www.youtube.com/@RedShieldWater"), ghost("Hero Call", f"📞 {PHONE}", TEL)]),
            videos_section("mist", 4, 0, "DIY Plumbing Safety Tutorials", "Water control and damage prevention. Watch these before you need them.", "Water control"),
            section("Quick Guides", "white", [g]),
            cta("Can't Stop the ", "Water", "?", "Call now. A plumber will talk you through it while an engineer is on the way.")]

def contact_form(label="Contact Form"):
    def field(i, lab, kind, ph, req=True, area=False):
        inp = N("e-form-textarea", f"{label} Field {i}", {"placeholder": ph, "rows": 5, "required": req}, "width: 100%; padding: 12px 14px; border: 1.5px solid #d4dbe5; border-radius: 10px; font-family: Inter; font-size: 16px;") if area else \
              N("e-form-input", f"{label} Field {i}", {"placeholder": ph, "type": kind, "required": req}, "width: 100%; padding: 12px 14px; border: 1.5px solid #d4dbe5; border-radius: 10px; font-family: Inter; font-size: 16px;")
        return col(f"{label} Group {i}", [N("e-form-label", f"{label} Label {i}", {"text": lab + (" *" if req else "")}, "font-family: Inter; font-size: 14px; font-weight: 600; color: #0e1726;"), inp], 6)
    kids = [h(f"{label} Title", "Send Us a Message", "h3", ["rs-h3"], "font-size: 24px;"),
            p(f"{label} Intro", "Describe your issue and we'll get back to you as soon as possible. For emergencies, please call.", ["rs-body"]),
            field(1, "Your name", "text", "Jane Smith"), field(2, "Email address", "email", "jane@email.com"), field(3, "Phone number", "tel", "07...", False),
            field(4, "How can we help?", "text", "e.g. Water dripping through the kitchen ceiling", True, True),
            N("e-form-submit-button", f"{label} Submit", {"text": "Send Message"}, "font-family: Inter; font-size: 16px; font-weight: 700; color: #ffffff; background-color: #dc2626; padding: 15px 24px; border-radius: 8px; width: 100%; &:hover { background-color: #b91c1c; }"),
            N("e-form-success-message", f"{label} Success", kids=[p(f"{label} Success Text", "Thanks, your message has been sent. We'll be in touch shortly. For an emergency, call " + PHONE + ".", style="font-family: Inter; color: #065f46;")]),
            N("e-form-error-message", f"{label} Error", kids=[p(f"{label} Error Text", "Sorry, something went wrong. Please call " + PHONE + ".", style="font-family: Inter; color: #b91c1c;")])]
    return N("e-form", label, {"form-name": "RedShield contact", "actions-after-submit": ["email"], "email": {"to": [EMAIL], "subject": "New RedShield Water website enquiry"}},
             "display: flex; flex-direction: column; gap: 14px; background-color: #ffffff; border: 1px solid #d4dbe5; border-top: 4px solid #dc2626; border-radius: 16px; padding: 28px; box-shadow: 0 1px 2px rgba(14,23,38,0.06), 0 10px 26px -14px rgba(14,23,38,0.28);", None, kids)

def contact_page():
    body = two_col("Contact Layout", col("Contact Info", [p("Contact Eyebrow", "Reach us directly", ["rs-eyebrow"]), h("Contact Title", "Get in touch", "h2", ["rs-h2"]),
                                                         p("Contact Lead", "For emergencies, calling is always the fastest option. We aim to respond within 45 minutes across Yorkshire.", ["rs-lead"]), contact_tiles()], 14),
                   contact_form(), "1fr 1fr", "start")
    return [hero("Home / Contact Us", "● Available right now", f"Contact {red('RedShield Water')}",
                 "For emergencies, calling is always the fastest option. We aim to respond within 45 minutes across Yorkshire.", "hero-kitchen.jpg", [call_btn()], solo=True),
            section("Contact Section", "mist", [body]), area_map("white")]

def leeds_page():
    prose = two_col("Leeds Prose", col("Leeds Prose Text", [p("Leeds Prose Eyebrow", "Leeds plumbing", ["rs-eyebrow"]), h("Leeds Prose Title", "24/7 Plumbing Repairs in Leeds", "h2", ["rs-h2"]),
        p("Leeds Prose P1", "RedShield Water provides emergency plumbing repairs across Leeds for burst pipes, leaking ceilings, blocked toilets, water leaks, overflowing toilets, blocked drains, no hot water, and urgent plumbing issues. We aim to arrive within <strong>45 minutes</strong> where available and provide insured repairs with a <strong>12-month workmanship guarantee</strong>.", ["rs-lead"]),
        p("Leeds Prose P2", "Our engineers cover Leeds City Centre, Headingley, Roundhay, Chapel Allerton, Horsforth, Pudsey, Morley, Rothwell, Garforth, Otley, Yeadon and nearby areas.", ["rs-lead"]),
        btn("Leeds Prose Call", f"📞 Call {PHONE}", TEL, style="width: fit-content;")], 14),
        img("Leeds Prose Photo", "hero-kitchen.jpg", "Kitchen plumbing repair in Leeds", "border-radius: 16px; aspect-ratio: 4 / 3; object-fit: cover;"))
    faq = two_col("Leeds FAQ Layout", col("Leeds FAQ", [p("Leeds FAQ Eyebrow", "Emergency plumbing FAQs", ["rs-eyebrow"]), h("Leeds FAQ Title", "Emergency plumbing in Leeds, your questions answered", "h2", ["rs-h2"], "font-size: 32px;"),
                                                       accordion("Leeds Questions", [(q, a) for c, q, a in D["FAQ"] if "leeds" in c.split()])], 14), callcard("Leeds &amp; surrounding areas", True), "1.5fr 1fr", "start")
    return [hero("Home / Areas / Leeds", "🕒 24/7 Emergency Response", f"Emergency Plumber {red('Leeds')}",
                 "<strong>45-minute response for burst pipes, leaks, blocked toilets &amp; urgent plumbing repairs.</strong> Speak to a real plumber now. We'll help you isolate the issue and stop further damage before we arrive.",
                 "hero-kitchen.jpg", [call_btn(), ghost("Hero Contact", "Request a Call Back", "contact")], area="Leeds &amp; surrounding areas"),
            reviews("dark"), videos_section("white"), section("Leeds Repairs", "mist", [prose]),
            section("Leeds Services", "white", [head("Leeds Services", None, "Emergency Plumbing Services in Leeds", "Fast, insured emergency response for every common plumbing problem in Leeds."), problems_grid("Leeds")]),
            leeds_areas_jobs("mist", 6), section("Leeds FAQs", "white", [faq]),
            cta("Need a Plumber in ", "Leeds", " Right Now?", "Burst pipe, blocked toilet, water leak or leaking ceiling? Don't wait. Call RedShield Water now for fast plumbing help across Leeds.")]

def harrogate_page():
    return [hero("Home / Areas / Harrogate", "🕒 24/7 Emergency Response", f"Emergency Plumber {red('Harrogate')}",
                 "Burst pipes, blocked toilets, leaks, overflowing toilets, blocked kitchen drains, hot water cylinders, sewage jetting and manhole clearing. Serving Starbeck, Bilton, Knaresborough, Pannal, Killinghall, Hampsthwaite, Boroughbridge &amp; more.",
                 "svc-burst.jpg", [call_btn(), ghost("Hero Contact", "Send a Message", "contact")], area="Harrogate &amp; all surrounding areas"),
            reviews("dark"), videos_section("white", 2, 1, "Emergency DIY Tips While You Wait", "Learn how to minimise damage before our team arrives."),
            area_map("mist", "harrogate"), issues_and_call("What Plumbing Issue Do You Have?", "white"),
            faq_section("harrogate", "Frequently Asked Questions", "mist", "FAQs", "Emergency plumbing in Harrogate, your questions answered."),
            cta("Need an Emergency Plumber in ", "Harrogate", "?", "Don't wait for a small leak to become expensive damage. Burst pipe, blocked toilet, leaking tap or water through the ceiling? Call now.")]

def yorkshire_page():
    prose = two_col("Yorkshire Prose", col("Yorkshire Prose Text", [p("Yorkshire Prose Eyebrow", "Yorkshire plumbers", ["rs-eyebrow"]), h("Yorkshire Prose Title", "24/7 plumbing across Yorkshire", "h2", ["rs-h2"]),
        p("Yorkshire Prose P1", "When a plumbing emergency strikes in Yorkshire, you need a fast, reliable expert who can respond immediately. At RedShield Water, we provide <strong>24/7 plumbing services across Yorkshire</strong>, including Leeds, Wakefield, Huddersfield, Halifax, and surrounding areas.", ["rs-lead"]),
        p("Yorkshire Prose P2", "Whether you're dealing with burst pipes, blocked drains, leaking boilers, overflowing toilets, or sudden loss of water, our experienced team is ready to attend quickly and resolve the issue before it causes costly damage.", ["rs-lead"]),
        p("Yorkshire Prose P3", "We prioritise rapid response times, transparent pricing, and long-lasting repairs. If you're searching for a “plumber near me” in Yorkshire, trust our local team.", ["rs-lead"])], 14),
        img("Yorkshire Photo", "svc-drains.jpg", "Blocked drain being cleared", "border-radius: 16px; aspect-ratio: 4 / 3; object-fit: cover;"))
    contact = two_col("Yorkshire Contact", col("Yorkshire Contact Info", [p("Yorkshire Contact Eyebrow", "Reach us directly", ["rs-eyebrow"]), h("Yorkshire Contact Title", "For emergencies, calling is fastest", "h2", ["rs-h2"], "font-size: 32px;"), contact_tiles("Yorkshire-wide coverage")], 14),
                      contact_form("Yorkshire Form"), "1fr 1fr", "start")
    return [hero("Home / Areas / Yorkshire", "🕒 24/7 Emergency Response", f"Need an {red('Emergency Plumber')} in Yorkshire?",
                 "We serve the whole of West Yorkshire and all surrounding areas, including Leeds, Harrogate, York, Huddersfield, Halifax, Doncaster, Wakefield &amp; more.",
                 "svc-drains.jpg", [call_btn(), ghost("Hero Contact", "Send a Message", "contact")], area="Yorkshire-wide coverage"),
            videos_section("white"), section("Yorkshire About", "mist", [prose]), area_map("white"), section("Yorkshire Contact Section", "mist", [contact]),
            cta("Plumbing Emergency in ", "Yorkshire", "?", "We aim to respond within 45 minutes across Yorkshire. Call now.")]

def ldu_page():
    cards = [col(f"Blockage {i}", [h(f"Blockage {i} Title", t, "h3", ["rs-h3"]), p(f"Blockage {i} Text", d, ["rs-body"], "font-size: 15px;")], 8, "", ["rs-card"]) for i, (t, d) in enumerate([
        ("Blocked Toilets", "Fast clearance of blocked or overflowing toilets, sanitised, no mess left behind."), ("Blocked Sinks &amp; Showers", "Kitchen sinks, bathroom basins and shower trays cleared with the right tool for the job."),
        ("Powerful Water Jetting", "A strong jet of water clears grease, roots and dirt that a plunger can't shift."), ("Outside Drains &amp; Manholes", "Blocked outside drains, drain covers and manholes cleared across Leeds.")], 1)]
    why = two_col("LDU Why", col("LDU Why Text", [p("LDU Why Eyebrow", "Why Leeds calls us first", ["rs-eyebrow"]), h("LDU Why Title", "Why Leeds Calls RedShield First", "h2", ["rs-h2"]),
        why_list("LDU Why List", ["Powerful drain-clearing equipment on every van", "Camera check inside the pipe if a drain keeps blocking", "Fixed-fee quotes before any work starts", "Local Leeds engineers, no call-centre delays", "Fully insured, guaranteed workmanship", "24/7 line for sewage, flooding &amp; overflows"])], 14),
        grid("LDU Before After", [col("LDU Before", [img("LDU Before Photo", "drain-before.jpg", "Blocked drain before clearing", "border-radius: 12px; aspect-ratio: 3 / 4; object-fit: cover;"), p("LDU Before Label", "Before", ["rs-tag"], "width: fit-content; background-color: #0e1726;")], 8),
                                  col("LDU After", [img("LDU After Photo", "drain-after.jpg", "Drain after clearing", "border-radius: 12px; aspect-ratio: 3 / 4; object-fit: cover;"), p("LDU After Label", "After", ["rs-tag"], "width: fit-content; background-color: #16a34a;")], 8)], 2, 14,
             "@media(--mobile) { grid-template-columns: repeat(2, minmax(0, 1fr)); }"))
    return [hero("Home / Services / Leeds Drain Unblocking", "🕒 24/7 Emergency Drain Unblocking", f"Drain Unblocking {red('Leeds')}",
                 "Blocked toilet, sink, shower or outside drain? Our Leeds drainage team responds in 45 minutes with powerful water-jetting equipment and fixed-fee pricing.",
                 "drain-maint.jpg", [call_btn(), ghost("Hero Pricing", "See Pricing", "pricing")], area="Leeds &amp; surrounding areas"),
            section("Blockages", "mist", [head("Blockages", None, f"Every Blockage. {red('Cleared Today.')}", "From a single slow sink to a full sewage backup, Leeds homes and businesses trust us to clear it on the first visit."), grid("Blockage Cards", cards, 4, 18)]),
            tiers("white", "Transparent Leeds Drain Pricing"), section("LDU Why Section", "mist", [why]),
            faq_section("ldu", "Drain Unblocking Leeds – FAQs", "white"),
            cta("Blocked Drain in ", "Leeds", "? Call Now.", "45-minute emergency response, 24 hours a day, across Leeds.")]

def bds_page():
    maint = col("Maintenance Card", [p("Maintenance Eyebrow", "Maintenance", ["rs-eyebrow"]), h("Maintenance Title", "Prevent Problems Before They Start", "h3", ["rs-h3"], "font-size: 26px;"),
                                     p("Maintenance Lead", "Regular maintenance can save you time, money and stress by preventing costly drainage issues.", ["rs-body"])] +
                [col(f"Maint {i}", [h(f"Maint {i} Title", t, "h4", ["rs-h3"], "font-size: 16px;"), p(f"Maint {i} Text", d, ["rs-body"], "font-size: 14px;")], 2, "padding: 14px 16px; background-color: var(--rs-mist); border-radius: 10px;")
                 for i, (t, d) in enumerate([("Avoid Blockages", "Keep your system clear and flowing with regular checks."), ("Extend Lifespan", "Proper care makes your drains and pipes last longer."), ("Save Money", "Prevent expensive repairs down the line.")], 1)] +
                [btn("Maintenance Book", "Book Maintenance", "contact", ("rs-btn-line",), "width: fit-content;")], 12, "padding: 30px;", ["rs-card"])
    why = two_col("BDS Why", col("BDS Why Text", [p("BDS Why Eyebrow", "Why choose us", ["rs-eyebrow"]), h("BDS Why Title", "Why Choose RedShield Water?", "h2", ["rs-h2"]),
        why_list("BDS Why List", ["24/7 Emergency Call Out", "Fully Qualified &amp; Insured", "15+ Years of Industry Experience", "State-of-the-Art Equipment", "Competitive Pricing", "Customer Satisfaction Guaranteed"]),
        btn("BDS About", "More About Us", "about", style="width: fit-content;")], 14), maint, "1fr 1fr", "start")
    return [hero("Home / Services / Blocked Drain Service", "🛠 Fast. Reliable. Professional.", f"Expert Drainage {red('Solutions')}",
                 "We provide a full range of drainage services including unblocking, repairs, installations and maintenance for homes and businesses across Yorkshire.",
                 "svc-drains.jpg", [call_btn(), ghost("Hero Quote", "Get A Quote", "contact")], area="Homes &amp; businesses across Yorkshire"),
            section("Drain Services", "mist", [head("Drain Services", "Our services", "Drainage Services You Can Rely On", "From blocked drains to full system installations, we've got the skills and equipment to get the job done right."), drain_cards()]),
            section("BDS Why Section", "white", [why]), tiers("mist"),
            cta("Need Help With Your ", "Drains", "?", "Get in touch today for fast, friendly and professional service.")]

PAGES.update({"about": about, "services": services_page, "pricing": pricing_page, "areas": areas_page, "faqs": faqs_page, "tutorials": tutorials_page,
              "contact": contact_page, "leeds": leeds_page, "harrogate": harrogate_page, "yorkshire": yorkshire_page, "ldu": ldu_page, "bds": bds_page})
PARTS = {"header": (40, header), "footer": (41, footer)}

if __name__ == "__main__":
    key = sys.argv[1]; dry = "--dry" in sys.argv
    if key in PARTS: push(PARTS[key][0], [PARTS[key][1]()], dry=dry)
    else: push(P[key], PAGES[key](), dry=dry)
