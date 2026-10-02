import json,sys
from gen import *
from blocks import *
D=json.load(open('data.json'))
SVC={s['slug']:s for s in D['SERVICES']}
IMG={"gbp-optimization":"google-business-profile-optimisation","web-development":"web-development-wolverhampton","custom-web-design":"custom-web-design","responsive-development":"responsive-web-development","ui-ux-design":"ui-ux-design-services","graphic-design":"graphic-design-wolverhampton","reviews":"google-review-management","seo-digital-marketing":"seo-services-wolverhampton","landing-pages":"landing-page-design","software-development":"custom-software-development","social-media-marketing":"social-media-marketing-wolverhampton","branding":"branding-agency-wolverhampton","google-ads":"google-ads-management","citations-backlinks":"local-citations-backlinks","ecommerce-solutions":"ecommerce-website-development"}
AVATAR={"p-1":"client-james-whitfield","p-2":"client-sophie-harrington","p-3":"client-daniel-okafor","p-4":"client-emily-carter","p-5":"client-raj-mehta","p-6":"client-hannah-lewis"}
POST=int(sys.argv[1]); GLOBE=sys.argv[2] if len(sys.argv)>2 else "digiranx-pro-logo-icon"
b=B(); e=b.el

def svc_card(b,slug,prefix=""):
    s=SVC[slug]; n=SERVICE_NAMES[slug][0]; p=prefix+n
    return e("e-flexbox",f"{p} Card",[
        e("e-flexbox",f"{p} Card Top",[e("e-heading",f"{p} Card Title",cfg={"tag":"h3","title":n},style="font-size: 19px; font-weight: 600; color: #0E0A1F;"),svgi(b,f"{p} Card Icon",SERVICE_NAMES[slug][1],24,"#FF2EA6")],
            style="justify-content: space-between; align-items: center; gap: 10px; padding: 8px 8px 0px 8px;"),
        e("e-flexbox",f"{p} Card Body",[e("e-paragraph",f"{p} Card Text",cfg={"paragraph":s['short']},style="color: rgba(255,255,255,0.94); font-size: 14.5px;"),
            button(b,f"{p} Card Button","Learn More",link_page(slug),"white",style="padding: 9px 18px; font-size: 14px;")],
            style=f"flex-direction: column; justify-content: flex-end; align-items: flex-start; gap: 18px; min-height: 210px; padding: 22px 18px; border-radius: 10px; background: linear-gradient(180deg, rgba(30,170,245,0.80) 0%, rgba(98,46,240,0.92) 100%), {bgurl(IMG[slug])} center / cover no-repeat; flex: 1 1 auto;")],
        style="flex-direction: column; gap: 14px; padding: 14px; border-radius: 10px; background: #FFFFFF; border: 1px solid #DCCFFF; box-shadow: 0 20px 50px -24px rgba(0,0,0,0.55); transition: border-color 0.25s, box-shadow 0.25s; &:hover { border-color: #1EC8F5; box-shadow: 0 24px 50px -20px rgba(30,200,245,0.45); }")

# ---------- HERO ----------
hero=e("e-flexbox","Hero",[e("e-flexbox","Hero Wrap",[
    e("e-flexbox","Hero Copy",[
        e("e-heading","Hero Title",cfg={"tag":"h1","title":"Where Creative Thinking Meets Digital Growth"},style="color: #FFFFFF; font-size: 62px; line-height: 1.12; @media(--tablet){ font-size: 48px; } @media(--mobile){ font-size: 38px; }"),
        e("e-paragraph","Hero Lead",cfg={"paragraph":"DIGIRANX PRO builds websites, ranks businesses on Google and runs ads that bring in real customers. One Wolverhampton team for everything your business needs online."},style="color: rgba(255,255,255,0.86); font-size: 18px; max-width: 500px; @media(--mobile){ font-size: 16px; }"),
        e("e-flexbox","Hero Buttons",[button(b,"Hero Audit Button","Get A Free Audit",link_page("contact"),"grad",True),button(b,"Hero Services Button","Our Services",link_page("services"),"ghost-w")],style="gap: 12px; flex-wrap: wrap; padding: 0px; margin-top: 12px;")],
        style="flex-direction: column; gap: 20px; padding: 0px; flex: 1 1 50%; @media(--tablet){ flex: 1 1 100%; }"),
    e("e-flexbox","Hero Visual",[e("e-image","Hero Globe",cfg=img(GLOBE),style="width: 100%; max-width: 520px; @media(--tablet){ max-width: 400px; }",classes=["dg-float"])],
        style="justify-content: flex-end; padding: 0px; flex: 1 1 50%; @media(--tablet){ justify-content: center; flex: 1 1 100%; }")],
    style="max-width: 1320px; width: 100%; align-items: center; gap: 24px; padding: 0px; @media(--tablet){ flex-direction: column; }")],
    style=f"flex-direction: column; align-items: center; padding: 160px 24px 190px 24px; background: radial-gradient(50% 60% at 75% 45%, rgba(123,59,255,0.45), transparent 70%), linear-gradient(180deg, rgba(11,6,36,0.92) 0%, rgba(26,14,82,0.86) 60%, rgba(42,20,120,0.90) 100%), {bgurl('digiranx-hero-tech-texture')} center / cover no-repeat; @media(--tablet){{ padding: 130px 24px 170px 24px; }} @media(--mobile){{ padding: 120px 16px 160px 16px; }}")

# ---------- TRIO ----------
def trio_card(cid,ic,title,text,slug,image=None):
    bg=f"background: linear-gradient(180deg, rgba(30,170,245,0.55), rgba(98,46,240,0.92)), {bgurl(image)} center / cover no-repeat;" if image else "background: #110A2E;"
    return e("e-flexbox",cid,[svgi(b,cid+" Icon",ic,34,"#FF2EA6",style="margin-bottom: 22px;"),e("e-heading",cid+" Title",cfg={"tag":"h3","title":title},style="color: #FFFFFF; font-size: 21px;"),
        e("e-paragraph",cid+" Text",cfg={"paragraph":text},style="color: rgba(255,255,255,0.78); font-size: 14.5px;")],cfg={"link":link_page(slug)},
        style="flex-direction: column; gap: 12px; padding: 30px 24px; border-radius: 10px; transition: transform 0.25s; &:hover { transform: translateY(-4px); } "+bg)
trio=e("e-flexbox","Feature Strip",[e("e-grid","Feature Strip Box",[
    trio_card("Feature Google","trend","Get Found On Google","SEO and Google Business Profile work that puts you in front of local buyers.","seo-digital-marketing"),
    trio_card("Feature Websites","code","Websites That Convert","Fast, mobile-friendly websites designed to turn visitors into enquiries.","web-development"),
    trio_card("Feature Ads","target","Ads And Social That Sell","Google Ads and social campaigns that bring ready-to-buy customers.","google-ads","seo-services-wolverhampton")],
    style="max-width: 1320px; width: 100%; grid-template-columns: repeat(3, 1fr); grid-template-rows: auto; gap: 14px; padding: 14px; border-radius: 10px; background: #FFFFFF; border: 1px solid #DCCFFF; box-shadow: 0 14px 34px -18px rgba(60,30,160,0.30); @media(--tablet){ grid-template-columns: 1fr; }")],
    style="justify-content: center; padding: 0px 24px; margin-top: -110px; position: relative; z-index: 2; @media(--mobile){ padding: 0px 16px; }")

# ---------- ABOUT ----------
ticks=e("e-grid","About Ticks",[e("e-flexbox",f"Tick {t}",[svgi(b,f"Tick {t} Icon","check",19,"#FF2EA6"),e("e-paragraph",f"Tick {t} Text",cfg={"paragraph":t},style="font-size: 15px; font-weight: 600; color: #0E0A1F;")],style="gap: 10px; align-items: center; padding: 0px;")
    for t in ["SEO and local search experts","Websites built to convert","Clear monthly reporting","No long lock-in contracts"]],style="grid-template-columns: repeat(2, 1fr); grid-template-rows: auto; gap: 10px; padding: 0px; width: 100%; @media(--mobile){ grid-template-columns: 1fr; }")
about=section(b,"About",[e("e-grid","About Grid",[
    e("e-div-block","About Media",[e("e-image","About Image",cfg=img("digiranx-pro-team-at-work"),style="width: 100%; height: 100%; object-fit: cover; aspect-ratio: 4 / 3; border-radius: 10px;"),
        e("e-flexbox","About Badge",[e("e-div-block","About Badge Line",style="width: 22px; height: 3px; min-width: 22px; padding: 0px; background: #FF2EA6; border-radius: 2px;"),e("e-paragraph","About Badge Text",cfg={"paragraph":"Proudly based in Wolverhampton"},style="color: #FFFFFF; font-weight: 600; font-size: 18px; @media(--mobile){ font-size: 15px; }")],
            style="position: absolute; left: 0px; bottom: 0px; gap: 12px; align-items: center; padding: 14px 22px; border-radius: 0px 10px 0px 10px; background: rgba(17,10,46,0.92); width: auto;")],
        style="position: relative; padding: 0px; border-radius: 10px; overflow: hidden;"),
    e("e-flexbox","About Copy",[eyebrow(b,"About Eyebrow","Who We Are"),
        e("e-heading","About Title",cfg={"tag":"h2","title":"Helping Businesses Grow And Shine Online"}),
        e("e-paragraph","About Text 1",cfg={"paragraph":"At DIGIRANX PRO LTD, we're a passionate team dedicated to helping businesses grow and shine online. Based in Wolverhampton, we combine creativity, experience, and smart strategies to strengthen your online presence, connect with your audience, and help your brand grow in today's digital world."},style="font-size: 15.5px;"),
        e("e-paragraph","About Text 2",cfg={"paragraph":"As a full-service digital marketing agency in Wolverhampton, we help local and UK businesses get found on Google, win more enquiries and look professional everywhere online. From SEO and Google Business Profile optimisation to web design, Google Ads and social media, one team plans and delivers it all."},style="font-size: 15.5px;"),
        ticks,
        e("e-paragraph","About Quote",cfg={"paragraph":"Where creative thinking meets digital growth."},style="border-left: 3px solid #FF2EA6; padding-left: 16px; font-size: 18px; font-weight: 500; color: #0E0A1F;"),
        button(b,"About Button","More About Us",link_page("about"))],
        style="flex-direction: column; align-items: flex-start; gap: 18px; padding: 0px;")],
    style="grid-template-columns: repeat(2, 1fr); grid-template-rows: auto; gap: 56px; align-items: center; padding: 0px; @media(--tablet){ grid-template-columns: 1fr; gap: 36px; }")])

# ---------- SERVICES (dark) ----------
HOME_SVC=["seo-digital-marketing","gbp-optimization","web-development","social-media-marketing","google-ads","branding"]
services=section(b,"Services",[
    e("e-flexbox","Services Head Row",[head(b,"Services Head","What We Offer","Digital Marketing Services That Grow Your Business",
        "SEO, Google Business Profile, websites, Google Ads, social media and branding. Every service your business needs to win customers online, delivered by one Wolverhampton team.",center=False,dark=True,style="max-width: 640px;"),
        button(b,"Services View All","View All Services",link_page("services"),"white",True)],
        style="justify-content: space-between; align-items: flex-end; gap: 24px; flex-wrap: wrap; padding: 0px; margin-bottom: 40px;"),
    e("e-grid","Services Grid",[svc_card(b,s) for s in HOME_SVC],style="grid-template-columns: repeat(3, 1fr); grid-template-rows: auto; gap: 20px; padding: 0px; @media(--tablet){ grid-template-columns: repeat(2, 1fr); } @media(--mobile){ grid-template-columns: 1fr; }")],
    style=f"background: radial-gradient(40% 60% at 90% 10%, rgba(255,46,166,0.22), transparent 70%), radial-gradient(45% 60% at 5% 90%, rgba(30,200,245,0.20), transparent 70%), linear-gradient(180deg, #120A33, #1B0F4D);",classes=["dg-world-bg"])

# ---------- CTA FORM (light) ----------
def fact(cid,big,small): return e("e-flexbox",cid,[e("e-paragraph",cid+" Big",cfg={"paragraph":big},style="font-size: 42px; font-weight: 700; line-height: 1; @media(--mobile){ font-size: 32px; }",classes=["dg-grad-text"]),e("e-paragraph",cid+" Small",cfg={"paragraph":small},style="font-size: 16px;")],style="flex-direction: column; gap: 6px; padding: 0px; width: auto;")
fhead,frm=form(b,"Audit Form","audit",title="Request Your Free Audit",note="We reply within one working day, Monday to Friday.",subject="Free audit request - digiranxpro.com")
cta=section(b,"Audit",[e("e-grid","Audit Grid",[
    e("e-flexbox","Audit Copy",[eyebrow(b,"Audit Eyebrow","Free Growth Audit"),
        e("e-heading","Audit Title",cfg={"tag":"h2","title":"Let's Find Out What's Holding Your Business Back Online"}),
        e("e-paragraph","Audit Text",cfg={"paragraph":"Tell us about your business and we'll send a free audit of your website, Google profile and competitors within one working day."}),
        e("e-flexbox","Audit Facts",[fact("Fact Services","15+","Digital Services"),fact("Fact Hours","8am–10pm","Monday to Friday"),fact("Fact Reply","24 hrs","Reply Time")],
            style="gap: 36px; flex-wrap: wrap; padding: 28px 0px 0px 0px; margin-top: 12px; border-top: 1px dashed #DCCFFF;")],
        style="flex-direction: column; align-items: flex-start; gap: 14px; padding: 0px;"),
    e("e-flexbox","Audit Form Card",fhead+[frm],style="flex-direction: column; gap: 10px; padding: 32px; border-radius: 10px; background: #FFFFFF; border: 1px solid #DCCFFF; box-shadow: 0 24px 50px -24px rgba(60,30,160,0.35); @media(--mobile){ padding: 22px; }")],
    style="grid-template-columns: 1fr 0.95fr; grid-template-rows: auto; gap: 56px; align-items: center; padding: 0px; @media(--tablet){ grid-template-columns: 1fr; gap: 32px; }")],
    style="background: radial-gradient(40% 70% at 0% 0%, rgba(30,200,245,0.14), transparent 70%), radial-gradient(40% 70% at 100% 100%, rgba(255,46,166,0.12), transparent 70%), #F1EDFC;")

# ---------- REVIEWS ----------
def review(i,r):
    text,name,biz,av=r
    return e("e-flexbox",f"Review {i+1}",[stars(b,f"Review {i+1} Stars"),e("e-paragraph",f"Review {i+1} Text",cfg={"paragraph":text},style="text-align: center; font-size: 16px; line-height: 1.7; flex: 1 1 auto;"),
        e("e-flexbox",f"Review {i+1} Author",[e("e-image",f"Review {i+1} Avatar",cfg=img(AVATAR[av]),style="width: 52px; height: 52px; border-radius: 50%; object-fit: cover;"),
            e("e-div-block",f"Review {i+1} Who",[e("e-paragraph",f"Review {i+1} Name",cfg={"paragraph":name},style="font-weight: 700; color: #0E0A1F; font-size: 16px;"),e("e-paragraph",f"Review {i+1} Business",cfg={"paragraph":biz},style="font-size: 13.5px;")],style="padding: 0px;")],
            style="gap: 12px; align-items: center; padding: 0px; width: auto;")],
        style="flex-direction: column; align-items: center; gap: 18px; padding: 30px 26px;",classes=["dg-card","dg-card-tint"])
reviews=section(b,"Reviews",[head(b,"Reviews Head","Testimonials","Reviews From Our Happy Clients",style="margin-bottom: 12px;"),
    e("e-paragraph","Reviews Quote Mark",cfg={"paragraph":"”"},style="text-align: center; font-size: 64px; font-weight: 800; line-height: 0.6; height: 34px; color: #FF2EA6; margin-bottom: 28px;"),
    e("e-grid","Reviews Grid",[review(i,r) for i,r in enumerate(D['REVIEWS'])],style="grid-template-columns: repeat(3, 1fr); grid-template-rows: auto; gap: 24px; padding: 0px; @media(--tablet){ grid-template-columns: repeat(2, 1fr); } @media(--mobile){ grid-template-columns: 1fr; }")],
    style="background: #FFFFFF; position: relative;",classes=["dg-reviews-bg"])

# ---------- WHY ----------
def why_item(cid,ic,t,d): return e("e-flexbox",cid,[circle_icon(b,cid+" Icon",ic),e("e-div-block",cid+" Copy",[e("e-heading",cid+" Title",cfg={"tag":"h3","title":t},style="font-size: 20px; font-weight: 600; margin-bottom: 4px;"),e("e-paragraph",cid+" Text",cfg={"paragraph":d},style="font-size: 14.5px;")],style="padding: 0px; flex: 1 1 auto;")],style="gap: 16px; align-items: flex-start; padding: 0px;")
def bar(cid,label,val): return e("e-flexbox",cid,[e("e-flexbox",cid+" Labels",[e("e-paragraph",cid+" Label",cfg={"paragraph":label},style="font-size: 13px; font-weight: 700; color: #0E0A1F;"),e("e-paragraph",cid+" Value",cfg={"paragraph":val},style="font-size: 13px; font-weight: 700; color: #0E0A1F;")],style="justify-content: space-between; padding: 0px;"),
    e("e-div-block",cid+" Track",[e("e-div-block",cid+" Fill",style="width: 100%; height: 5px; padding: 0px; border-radius: 5px; background: linear-gradient(90deg, #1EC8F5 0%, #7B3BFF 55%, #FF2EA6 100%);")],style="height: 5px; padding: 0px; border-radius: 5px; background: #ECE8F7;")],style="flex-direction: column; gap: 5px; padding: 0px;")
why=section(b,"Why",[e("e-grid","Why Grid",[
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
    style="grid-template-columns: repeat(2, 1fr); grid-template-rows: auto; gap: 64px; align-items: center; padding: 0px; @media(--tablet){ grid-template-columns: 1fr; gap: 40px; }")],classes=["dg-bg-light"])

# ---------- FAQ (split) ----------
faqs=[(f[1],f[2]) for f in D['FAQS'][:6]]
faq=section(b,"FAQ",[e("e-grid","FAQ Grid",[
    e("e-flexbox","FAQ Aside",[head(b,"FAQ Head","FAQs","Frequently Asked Questions","The things business owners ask us most. Can't see yours? Call or email and we'll help.",center=False),help_card(b,"FAQ Help")],
        style="flex-direction: column; gap: 22px; padding: 0px;"),
    faq_accordion(b,"Home FAQ",faqs,tint=True)],
    style="grid-template-columns: 0.8fr 1.2fr; grid-template-rows: auto; gap: 64px; align-items: start; padding: 0px; @media(--tablet){ grid-template-columns: 1fr; gap: 32px; }")])

root=[hero,trio,about,services,cta,reviews,why,faq,final_cta(b)]
json.dump(b.payload(POST,"".join(root)),open('p_home.json','w')); print(len(json.dumps(b.payload(POST,"".join(root)))))
