"""Bigger reusable sections (services cards, reviews, why, steps, faq box, cta form)."""
import json
from gen import *
from blocks import *
D=json.load(open('data.json'))
SVC={s['slug']:s for s in D['SERVICES']}
IMG={"gbp-optimization":"google-business-profile-optimisation","web-development":"web-development-wolverhampton","custom-web-design":"custom-web-design","responsive-development":"responsive-web-development","ui-ux-design":"ui-ux-design-services","graphic-design":"graphic-design-wolverhampton","reviews":"google-review-management","seo-digital-marketing":"seo-services-wolverhampton","landing-pages":"landing-page-design","software-development":"custom-software-development","social-media-marketing":"social-media-marketing-wolverhampton","branding":"branding-agency-wolverhampton","google-ads":"google-ads-management","citations-backlinks":"local-citations-backlinks","ecommerce-solutions":"ecommerce-website-development"}
AVATAR={"p-1":"client-james-whitfield","p-2":"client-sophie-harrington","p-3":"client-daniel-okafor","p-4":"client-emily-carter","p-5":"client-raj-mehta","p-6":"client-hannah-lewis"}
GROUP_ORDER=[("grow","Search & Ads"),("design","Design & Social"),("build","Build & Develop")]

def svc_card(b,slug,prefix="",dark=True):
    e=b.el; s=SVC[slug]; n=SERVICE_NAMES[slug][0]; p=prefix+n
    shadow="0 20px 50px -24px rgba(0,0,0,0.55)" if dark else "0 14px 34px -18px rgba(60,30,160,0.30)"
    hover="&:hover { border-color: #1EC8F5; box-shadow: 0 24px 50px -20px rgba(30,200,245,0.45); }" if dark else "&:hover { border-color: #9B6BFF; box-shadow: 0 22px 44px -20px rgba(90,40,220,0.45); }"
    return e("e-flexbox",f"{p} Card",[
        e("e-flexbox",f"{p} Card Top",[e("e-heading",f"{p} Card Title",cfg={"tag":"h3","title":n},style="font-size: 19px; font-weight: 600; color: #0E0A1F;"),svgi(b,f"{p} Card Icon",SERVICE_NAMES[slug][1],24,"#FF2EA6")],
            style="justify-content: space-between; align-items: center; gap: 10px; padding: 8px 8px 0px 8px;"),
        e("e-flexbox",f"{p} Card Body",[e("e-paragraph",f"{p} Card Text",cfg={"paragraph":s['short']},style="color: rgba(255,255,255,0.94); font-size: 14.5px;"),
            button(b,f"{p} Card Button","Learn More",link_page(slug),"white",style="padding: 9px 18px; font-size: 14px;")],
            style=f"flex-direction: column; justify-content: flex-end; align-items: flex-start; gap: 18px; min-height: 210px; padding: 22px 18px; border-radius: 10px; background: linear-gradient(180deg, rgba(30,170,245,0.80) 0%, rgba(98,46,240,0.92) 100%), {bgurl(IMG[slug])} center / cover no-repeat; flex: 1 1 auto;")],
        style=f"flex-direction: column; gap: 14px; padding: 14px; border-radius: 10px; background: #FFFFFF; border: 1px solid #DCCFFF; box-shadow: {shadow}; transition: border-color 0.25s, box-shadow 0.25s; {hover}")

GRID3="grid-template-columns: repeat(3, 1fr); grid-template-rows: auto; gap: 20px; padding: 0px; @media(--tablet){ grid-template-columns: repeat(2, 1fr); } @media(--mobile){ grid-template-columns: 1fr; }"

def services_tabs(b):
    """All 15 services with filter tabs (All + 3 groups)."""
    e=b.el
    tabs=[("All Services",list(SVC.keys()))]+[(name,[k for k,s in SVC.items() if s['group']==g]) for g,name in GROUP_ORDER]
    menu=e("e-tabs-menu","Service Filter Menu",[e("e-tab",f"Filter Tab {i+1}",[e("e-paragraph",f"Filter Tab {i+1} Label",cfg={"paragraph":t},style="font-size: 15px; font-weight: 600;")],
        style="width: auto; padding: 9px 18px; border-radius: 8px; border: 1px solid #DCCFFF; background: #FFFFFF; color: #0E0A1F; transition: background 0.2s, color 0.2s; &:hover { background: #110A2E; color: #FFFFFF; border-color: #110A2E; }",classes=["dg-tab"]) for i,(t,_) in enumerate(tabs)],
        style="gap: 8px; flex-wrap: wrap; justify-content: center;")
    area=e("e-tabs-content-area","Service Filter Panels",[e("e-tab-content",f"Filter Panel {i+1}",[e("e-grid",f"Filter Grid {i+1}",[svc_card(b,k,prefix=f"T{i+1} ",dark=False) for k in keys],style=GRID3)],style="padding: 0px;") for i,(t,keys) in enumerate(tabs)],style="padding: 0px;")
    return e("e-tabs","Service Filter",[menu,area],cfg={"default-active-tab":0},style="gap: 34px;")

def reviews_section(b,light=False):
    e=b.el
    def review(i,r):
        text,name,biz,av=r
        return e("e-flexbox",f"Review {i+1}",[stars(b,f"Review {i+1} Stars"),e("e-paragraph",f"Review {i+1} Text",cfg={"paragraph":text},style="text-align: center; font-size: 16px; line-height: 1.7; flex: 1 1 auto;"),
            e("e-flexbox",f"Review {i+1} Author",[e("e-image",f"Review {i+1} Avatar",cfg=img(AVATAR[av]),style="width: 52px; height: 52px; border-radius: 50%; object-fit: cover;"),
                e("e-div-block",f"Review {i+1} Who",[e("e-paragraph",f"Review {i+1} Name",cfg={"paragraph":name},style="font-weight: 700; color: #0E0A1F; font-size: 16px;"),e("e-paragraph",f"Review {i+1} Business",cfg={"paragraph":biz},style="font-size: 13.5px;")],style="padding: 0px;")],
                style="gap: 12px; align-items: center; padding: 0px; width: auto;")],
            style="flex-direction: column; align-items: center; gap: 18px; padding: 30px 26px;"+(" background: #FFFFFF;" if light else ""),classes=["dg-card"]+([] if light else ["dg-card-tint"]))
    return section(b,"Reviews",[head(b,"Reviews Head","Testimonials","Reviews From Our Happy Clients",style="margin-bottom: 12px;"),
        e("e-paragraph","Reviews Quote Mark",cfg={"paragraph":"”"},style="text-align: center; font-size: 64px; font-weight: 800; line-height: 0.6; height: 34px; color: #FF2EA6; margin-bottom: 28px;"),
        e("e-grid","Reviews Grid",[review(i,r) for i,r in enumerate(D['REVIEWS'])],style="grid-template-columns: repeat(3, 1fr); grid-template-rows: auto; gap: 24px; padding: 0px; @media(--tablet){ grid-template-columns: repeat(2, 1fr); } @media(--mobile){ grid-template-columns: 1fr; }")],
        style="background: "+("#F1EDFC" if light else "#FFFFFF")+"; position: relative;",classes=["dg-reviews-bg"])

def why_section(b,light=True):
    e=b.el
    def why_item(cid,ic,t,d): return e("e-flexbox",cid,[circle_icon(b,cid+" Icon",ic),e("e-div-block",cid+" Copy",[e("e-heading",cid+" Title",cfg={"tag":"h3","title":t},style="font-size: 20px; font-weight: 600; margin-bottom: 4px;"),e("e-paragraph",cid+" Text",cfg={"paragraph":d},style="font-size: 14.5px;")],style="padding: 0px; flex: 1 1 auto;")],style="gap: 16px; align-items: flex-start; padding: 0px;")
    def bar(cid,label,val): return e("e-flexbox",cid,[e("e-flexbox",cid+" Labels",[e("e-paragraph",cid+" Label",cfg={"paragraph":label},style="font-size: 13px; font-weight: 700; color: #0E0A1F;"),e("e-paragraph",cid+" Value",cfg={"paragraph":val},style="font-size: 13px; font-weight: 700; color: #0E0A1F;")],style="justify-content: space-between; padding: 0px;"),
        e("e-div-block",cid+" Track",[e("e-div-block",cid+" Fill",style="width: 100%; height: 5px; padding: 0px; border-radius: 5px; background: linear-gradient(90deg, #1EC8F5 0%, #7B3BFF 55%, #FF2EA6 100%);")],style="height: 5px; padding: 0px; border-radius: 5px; background: #ECE8F7;")],style="flex-direction: column; gap: 5px; padding: 0px;")
    return section(b,"Why",[e("e-grid","Why Grid",[
        e("e-flexbox","Why Copy",[head(b,"Why Head","Why Choose Us","Where Creative Thinking Meets Digital Growth","We are a small, focused team. You speak to the people doing the work, decisions happen quickly, and your business never gets lost in a queue.",center=False),
            e("e-flexbox","Why List",[why_item("Why Team","users","One Team, Every Channel","Web, SEO, ads, social and branding planned together, not in silos."),
                why_item("Why Reporting","chart","Clear, Honest Reporting","Monthly reports in plain English that show calls, leads and sales."),
                why_item("Why Hours","clock","Long Support Hours","Available 8am to 10pm, Monday to Friday, when you need us.")],style="flex-direction: column; gap: 22px; padding: 0px; margin-top: 28px;")],
            style="flex-direction: column; padding: 0px;"),
        e("e-div-block","Why Media",[e("e-image","Why Image",cfg=img("why-choose-digiranx-pro"),style="width: 90%; aspect-ratio: 1 / 1.05; object-fit: cover; border-radius: 10px; @media(--mobile){ width: 100%; }"),
            e("e-flexbox","Why Card",[e("e-heading","Why Card Title",cfg={"tag":"h4","title":"Building Brands With Smart Digital Strategy"},style="font-size: 18px; font-weight: 600;"),
                e("e-paragraph","Why Card Text",cfg={"paragraph":"What every client gets from day one."},style="font-size: 13.5px;"),
                bar("Bar Reply","Reply within 1 working day","100%"),bar("Bar UK","UK-based account team","100%")],
                style="position: absolute; right: 0px; bottom: 0px; width: 270px; flex-direction: column; gap: 10px; padding: 22px; border-radius: 10px; background: #FFFFFF; border: 1px solid #DCCFFF; box-shadow: 0 14px 34px -18px rgba(60,30,160,0.30); @media(--mobile){ position: relative; width: 100%; margin-top: -30px; }")],
            style="position: relative; padding: 0px 0px 40px 0px; @media(--mobile){ padding: 0px; }")],
        style="grid-template-columns: repeat(2, 1fr); grid-template-rows: auto; gap: 64px; align-items: center; padding: 0px; @media(--tablet){ grid-template-columns: 1fr; gap: 40px; }")],classes=(["dg-bg-light"] if light else None))

def steps_section(b,cid,eyebrow_text,title,steps,light=False,lead=None):
    e=b.el
    cards=[e("e-flexbox",f"{cid} Step {i+1}",[e("e-paragraph",f"{cid} Step {i+1} Num",cfg={"paragraph":f"0{i+1}"},style="font-size: 40px; font-weight: 800; line-height: 1;",classes=["dg-grad-text"]),
        e("e-heading",f"{cid} Step {i+1} Title",cfg={"tag":"h3","title":t},style="font-size: 20px; font-weight: 600;"),e("e-paragraph",f"{cid} Step {i+1} Text",cfg={"paragraph":d},style="font-size: 15px;")],
        style="flex-direction: column; gap: 10px; padding: 28px 24px;"+(" background: #FFFFFF;" if light else ""),classes=["dg-card"]+([] if light else ["dg-card-tint"])) for i,(t,d) in enumerate(steps)]
    return section(b,cid,[head(b,cid+" Head",eyebrow_text,title,lead),
        e("e-grid",cid+" Grid",cards,style=f"grid-template-columns: repeat({len(steps)}, 1fr); grid-template-rows: auto; gap: 20px; padding: 0px; @media(--tablet){{ grid-template-columns: repeat(2, 1fr); }} @media(--mobile){{ grid-template-columns: 1fr; }}")],
        classes=(["dg-bg-light"] if light else None))

def timeline_section(b,cid,eyebrow_text,title,lead,steps,light=False):
    """Numbered vertical timeline rows (service pages)."""
    e=b.el
    rows=[e("e-flexbox",f"{cid} Row {i+1}",[
        e("e-flexbox",f"{cid} Row {i+1} Num",[e("e-paragraph",f"{cid} Row {i+1} Num Text",cfg={"paragraph":f"0{i+1}"},style="color: #FFFFFF; font-size: 22px; font-weight: 800;")],
            style="flex: 0 0 64px; width: 64px; height: 64px; padding: 0px; border-radius: 10px; align-items: center; justify-content: center; background: linear-gradient(90deg, #16B4F0 0%, #7B3BFF 100%); box-shadow: 0 10px 24px -10px rgba(123,59,255,0.7); @media(--mobile){ flex: 0 0 52px; width: 52px; height: 52px; }"),
        e("e-heading",f"{cid} Row {i+1} Title",cfg={"tag":"h3","title":t},style="flex: 0 0 260px; font-size: 19px; @media(--tablet){ flex: 1 1 auto; }"),
        e("e-paragraph",f"{cid} Row {i+1} Text",cfg={"paragraph":d},style="flex: 1 1 0px; font-size: 15.5px; line-height: 1.7; @media(--tablet){ flex: 1 1 100%; }")],
        style="gap: 24px; align-items: center; padding: 18px 26px 18px 18px; border-radius: 10px; border: 1px solid #DCCFFF; background: "+("#FFFFFF" if light else "#F7F3FF")+"; @media(--tablet){ flex-wrap: wrap; gap: 12px 16px; align-items: flex-start; }") for i,(t,d) in enumerate(steps)]
    return section(b,cid,[head(b,cid+" Head",eyebrow_text,title,lead),e("e-flexbox",cid+" Rows",rows,style="flex-direction: column; gap: 14px; padding: 0px; max-width: 1040px; width: 100%; margin: 0px auto;")],classes=(["dg-bg-light"] if light else None))

def faq_box(b,cid,items,title,lead,light=False):
    """Single container, two accordion columns, contact footer row."""
    e=b.el
    half=(len(items)+1)//2
    cols=[faq_accordion(b,f"{cid} Col {c+1}",items[c*half:(c+1)*half],tint=light) for c in range(2)]
    box=e("e-flexbox",cid+" Box",[
        e("e-grid",cid+" Cols",cols,style="grid-template-columns: repeat(2, 1fr); grid-template-rows: auto; gap: 12px 18px; align-items: start; padding: 0px; @media(--tablet){ grid-template-columns: 1fr; }"),
        e("e-flexbox",cid+" Foot",[e("e-paragraph",cid+" Foot Text",cfg={"paragraph":"<strong>Still have a question?</strong> Talk to our team Monday to Friday, 8am to 10pm."},style="font-size: 15px;"),
            e("e-flexbox",cid+" Foot Buttons",[button(b,cid+" Call","Call +44 7445 652671",link_url("tel:+447445652671"),"grad",style="padding: 9px 18px; font-size: 14px;"),button(b,cid+" Mail","info@digiranxpro.com",link_url("mailto:info@digiranxpro.com"),"outline",style="padding: 8px 16px; font-size: 14px;")],style="gap: 10px; flex-wrap: wrap; padding: 0px; width: auto;")],
            style="justify-content: space-between; align-items: center; gap: 14px; flex-wrap: wrap; margin-top: 20px; padding: 18px 0px 0px 0px; border-top: 1px dashed #DCCFFF;")],
        style="flex-direction: column; padding: 28px; border-radius: 10px; border: 1px solid #DCCFFF; box-shadow: 0 18px 44px -24px rgba(60,30,160,0.35); background: "+("#FFFFFF" if light else "#F7F3FF")+"; @media(--mobile){ padding: 16px; }")
    return section(b,cid,[head(b,cid+" Head","FAQs",title,lead),box],classes=(["dg-bg-light"] if light else None))
