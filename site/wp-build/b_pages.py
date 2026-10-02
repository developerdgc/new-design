"""Inner pages: python3 b_pages.py <page> <post_id>  ->  p_<page>.json"""
import json,sys
from gen import *
from blocks import *
from sections import *
page,POST=sys.argv[1],int(sys.argv[2])
b=B(); e=b.el
FAQ_ALL=[(f[1],f[2]) for f in D['FAQS']]

def about_intro(more_link=("Explore Our Services","services")):
    ticks=e("e-grid","About Ticks",[e("e-flexbox",f"Tick {t}",[svgi(b,f"Tick {t} Icon","check",19,"#FF2EA6"),e("e-paragraph",f"Tick {t} Text",cfg={"paragraph":t},style="font-size: 15px; font-weight: 600; color: #0E0A1F;")],style="gap: 10px; align-items: center; padding: 0px;")
        for t in ["SEO and local search experts","Websites built to convert","Clear monthly reporting","No long lock-in contracts"]],style="grid-template-columns: repeat(2, 1fr); grid-template-rows: auto; gap: 10px; padding: 0px; width: 100%; @media(--mobile){ grid-template-columns: 1fr; }")
    return section(b,"About",[e("e-grid","About Grid",[
        e("e-div-block","About Media",[e("e-image","About Image",cfg=img("digiranx-pro-team-at-work"),style="width: 100%; height: 100%; object-fit: cover; aspect-ratio: 4 / 3; border-radius: 10px;"),
            e("e-flexbox","About Badge",[e("e-div-block","About Badge Line",style="width: 22px; height: 3px; min-width: 22px; padding: 0px; background: #FF2EA6; border-radius: 2px;"),e("e-paragraph","About Badge Text",cfg={"paragraph":"Proudly based in Wolverhampton"},style="color: #FFFFFF; font-weight: 600; font-size: 18px; @media(--mobile){ font-size: 15px; }")],
                style="position: absolute; left: 0px; bottom: 0px; gap: 12px; align-items: center; padding: 14px 22px; border-radius: 0px 10px 0px 10px; background: rgba(17,10,46,0.92); width: auto;")],
            style="position: relative; padding: 0px; border-radius: 10px; overflow: hidden;"),
        e("e-flexbox","About Copy",[eyebrow(b,"About Eyebrow","Who We Are"),
            e("e-heading","About Title",cfg={"tag":"h2","title":"A Wolverhampton Digital Marketing Agency Built Around Your Growth"}),
            e("e-paragraph","About Text 1",cfg={"paragraph":"At DIGIRANX PRO LTD, we're a passionate team dedicated to helping businesses grow and shine online. Based in Wolverhampton, we combine creativity, experience, and smart strategies to strengthen your online presence, connect with your audience, and help your brand grow in today's digital world."},style="font-size: 15.5px;"),
            e("e-paragraph","About Text 2",cfg={"paragraph":"We work with local trades, shops, clinics and service businesses across Wolverhampton, Birmingham, Walsall, Dudley and Telford, as well as companies across the UK. Every plan starts with a free audit, a clear proposal and fixed prices, so you always know what you are paying for and what you will get."},style="font-size: 15.5px;"),
            ticks,
            e("e-paragraph","About Quote",cfg={"paragraph":"Where creative thinking meets digital growth."},style="border-left: 3px solid #FF2EA6; padding-left: 16px; font-size: 18px; font-weight: 500; color: #0E0A1F;"),
            button(b,"About Button",more_link[0],link_page(more_link[1]))],
            style="flex-direction: column; align-items: flex-start; gap: 18px; padding: 0px;")],
        style="grid-template-columns: repeat(2, 1fr); grid-template-rows: auto; gap: 56px; align-items: center; padding: 0px; @media(--tablet){ grid-template-columns: 1fr; gap: 36px; }")])

def mvv():
    cards=[e("e-flexbox",f"Value {t}",[circle_icon(b,f"Value {t} Icon",ic,52),e("e-heading",f"Value {t} Title",cfg={"tag":"h3","title":t},style="font-size: 21px; font-weight: 600;"),e("e-paragraph",f"Value {t} Text",cfg={"paragraph":d},style="font-size: 15.5px;")],
        style="flex-direction: column; gap: 12px; padding: 30px 26px; background: #FFFFFF;",classes=["dg-card"]) for t,ic,d in [
        ("Our Mission","target","To give every business, big or small, the online presence it deserves, with honest advice and work that brings in real customers."),
        ("Our Vision","eye","To be the West Midlands' most trusted digital partner, known for creative ideas and measurable growth."),
        ("Our Values","heart","Transparency in every report, creativity in every project, and treating your budget like it's our own.")]]
    return section(b,"Values",[head(b,"Values Head","What Drives Us","Our Mission, Vision And Values"),e("e-grid","Values Grid",cards,style=GRID3)],classes=["dg-bg-light"])

def audit_band(img_name="digital-strategy-meeting"):
    def fact(cid,big,small): return e("e-flexbox",cid,[e("e-paragraph",cid+" Big",cfg={"paragraph":big},style="font-size: 42px; font-weight: 700; line-height: 1; color: #FFFFFF; @media(--mobile){ font-size: 32px; }"),e("e-paragraph",cid+" Small",cfg={"paragraph":small},style="font-size: 16px; color: rgba(255,255,255,0.82);")],style="flex-direction: column; gap: 6px; padding: 0px; width: auto;")
    fhead,frm=form(b,"Audit Form","audit",title="Request Your Free Audit",note="We reply within one working day, Monday to Friday.",subject="Free audit request - digiranxpro.com")
    return section(b,"Audit",[e("e-grid","Audit Grid",[
        e("e-flexbox","Audit Copy",[eyebrow(b,"Audit Eyebrow","Free Growth Audit",dark=True),
            e("e-heading","Audit Title",cfg={"tag":"h2","title":"Let's Find Out What's Holding Your Business Back Online"},classes=["dg-text-white"]),
            e("e-paragraph","Audit Text",cfg={"paragraph":"Tell us about your business and we'll send a free audit of your website, Google profile and competitors within one working day."},classes=["dg-text-soft-white"]),
            e("e-flexbox","Audit Facts",[fact("Fact Services","15+","Digital Services"),fact("Fact Hours","8am–10pm","Monday to Friday"),fact("Fact Reply","24 hrs","Reply Time")],
                style="gap: 36px; flex-wrap: wrap; padding: 28px 0px 0px 0px; margin-top: 12px; border-top: 1px dashed rgba(255,255,255,0.35);")],
            style="flex-direction: column; align-items: flex-start; gap: 14px; padding: 0px;"),
        e("e-flexbox","Audit Form Card",fhead+[frm],style="flex-direction: column; gap: 10px; padding: 32px; border-radius: 10px; background: #FFFFFF; box-shadow: 0 30px 60px -20px rgba(0,0,0,0.45); @media(--mobile){ padding: 22px; }")],
        style="grid-template-columns: 1fr 0.95fr; grid-template-rows: auto; gap: 56px; align-items: center; padding: 0px; @media(--tablet){ grid-template-columns: 1fr; gap: 32px; }")],
        style=f"background: linear-gradient(90deg, rgba(17,10,46,0.95) 0%, rgba(40,20,120,0.85) 50%, rgba(98,46,240,0.55) 100%), {bgurl(img_name)} center / cover no-repeat;")

roots=[]
if page=="about":
    roots=[page_hero(b,"About Us","A Wolverhampton team helping businesses grow and shine online.",[("About Us",None)],"digiranx-pro-team-at-work"),
        about_intro(),mvv(),
        steps_section(b,"Process","How We Work","A Simple Process From First Call To Growth",[("Discover","A free call and audit to understand your business, customers and competitors."),("Plan","A clear proposal with goals, timelines and fixed prices. No surprises."),("Create","We design, build and launch, keeping you updated at every stage."),("Grow","We track results every month and keep improving what works.")]),
        why_section(b,light=True),reviews_section(b),final_cta(b)]
elif page=="services":
    roots=[page_hero(b,"Our Services","Fifteen digital services, one team. Pick what you need today and add more as you grow.",[("Our Services",None)],"digital-strategy-meeting"),
        section(b,"All Services",[head(b,"All Services Head","What We Offer","Digital Marketing Services In Wolverhampton","From your first website to page-one rankings, every digital service your business needs, handled by one team. Filter by what you need below."),services_tabs(b)]),
        audit_band(),
        steps_section(b,"Process","How We Work","Every Service Follows The Same Clear Process",[("Discover","Free audit and call to understand your goals."),("Plan","Fixed-price proposal with clear deliverables."),("Deliver","We build, launch and keep you updated."),("Report","Monthly results and next steps in plain English.")]),
        final_cta(b)]
elif page=="contact":
    def ci(cid,ic,title,lines,link=None):
        return e("e-flexbox",cid,[circle_icon(b,cid+" Icon",ic,48),e("e-heading",cid+" Title",cfg={"tag":"h3","title":title},style="font-size: 19px; font-weight: 600;"),
            e("e-paragraph",cid+" Text",cfg=dict({"paragraph":lines},**({"link":link_url(link)} if link else {})),style="font-size: 15px;"+(" font-weight: 700;" if link else ""))],
            style="flex-direction: column; gap: 10px; padding: 26px 22px;",classes=["dg-card","dg-card-tint"])
    fhead,frm=form(b,"Contact Form","contact",title="Send Us A Message",note="Fill in the form and our team will be in touch within one working day.",subject="New contact enquiry - digiranxpro.com")
    roots=[page_hero(b,"Contact Us","Tell us about your business and we'll reply within one working day.",[("Contact Us",None)],"free-website-audit-consultation"),
        section(b,"Contact",[
            e("e-grid","Contact Info Grid",[ci("Contact Call","phone","Call Us","+44 7445 652671","tel:+447445652671"),ci("Contact Email","mail","Email Us","info@digiranxpro.com","mailto:info@digiranxpro.com"),
                ci("Contact Visit","pin","Visit Us","Office 1922, 85 Dunstall Hill, Wolverhampton, WV6 0SR, UK"),ci("Contact Hours","clock","Opening Hours","Mon – Fri: 8am – 10pm<br>Sat – Sun: Closed")],
                style="grid-template-columns: repeat(4, 1fr); grid-template-rows: auto; gap: 18px; padding: 0px; margin-bottom: 48px; @media(--tablet){ grid-template-columns: repeat(2, 1fr); } @media(--mobile){ grid-template-columns: 1fr; }"),
            e("e-grid","Contact Main Grid",[
                e("e-flexbox","Map Card",[e("e-flexbox","Map Card Copy",[eyebrow(b,"Map Eyebrow","Our Office",dark=True),e("e-heading","Map Title",cfg={"tag":"h3","title":"85 Dunstall Hill, Wolverhampton"},style="color: #FFFFFF; font-size: 22px;"),
                    button(b,"Map Button","Open In Google Maps",link_url("https://www.google.com/maps/search/?api=1&query=85+Dunstall+Hill+Wolverhampton+WV6+0SR",True),"white",True,style="padding: 9px 18px; font-size: 14px;")],style="flex-direction: column; align-items: flex-start; gap: 8px; padding: 0px;")],
                    style=f"min-height: 340px; align-items: flex-end; padding: 26px; border-radius: 10px; background: linear-gradient(180deg, rgba(17,10,46,0.1), rgba(17,10,46,0.92)), {bgurl('google-business-profile-optimisation')} center / cover no-repeat;"),
                e("e-flexbox","Contact Form Card",fhead+[frm],style="flex-direction: column; gap: 10px; padding: 32px; @media(--mobile){ padding: 22px; }",classes=["dg-card"])],
                style="grid-template-columns: 0.9fr 1.1fr; grid-template-rows: auto; gap: 40px; align-items: stretch; padding: 0px; @media(--tablet){ grid-template-columns: 1fr; }")]),
        faq_box(b,"Contact FAQ",FAQ_ALL[:10],"Frequently Asked Questions","Straight answers to the questions business owners ask us most.",light=True)]
elif page=="faqs":
    roots=[page_hero(b,"FAQs","Straight answers about our services, pricing and how we work.",[("FAQs",None)],"why-choose-digiranx-pro"),
        faq_box(b,"All FAQ",FAQ_ALL,"Everything You Need To Know","Our services, pricing, process and support, all in one place."),final_cta(b)]
elif page in ("privacy-policy","terms-conditions","cookie-policy"):
    P=json.load(open('policies.json'))[page]
    kids=[e("e-paragraph","Policy Updated",cfg={"paragraph":"<strong>Last updated:</strong> 2 October 2026 · DIGIRANX PRO LTD, Office 1922, 85 Dunstall Hill, Wolverhampton, WV6 0SR"},style="font-size: 15px; padding: 18px 22px; border-radius: 10px; background: #F7F3FF; border: 1px solid #DCCFFF;")]
    for i,(h,body) in enumerate(P['sections']):
        kids.append(e("e-heading",f"Policy H {i+1}",cfg={"tag":"h2","title":h},style="font-size: 24px; margin-top: 14px;"))
        txt="<ul>"+"".join(f"<li>{x}</li>" for x in body)+"</ul>" if isinstance(body,list) else body
        kids.append(e("e-paragraph",f"Policy P {i+1}",cfg={"paragraph":txt},style="font-size: 16px; line-height: 1.75;",classes=["dg-policy-text"]))
    roots=[page_hero(b,P['title'],P['lead'],[(P['title'],None)],"digital-strategy-meeting"),
        section(b,"Policy",[e("e-flexbox","Policy Body",kids,style="flex-direction: column; gap: 14px; padding: 0px; max-width: 860px; width: 100%; margin: 0px auto;")])]
json.dump(b.payload(POST,"".join(roots)),open(f'p_{page}.json','w')); print(page,POST,len(json.dumps(b.payload(POST,"".join(roots)))))
