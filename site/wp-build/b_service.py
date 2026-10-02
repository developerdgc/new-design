"""python3 b_service.py <slug>  ->  p_svc_<slug>.json"""
import json,sys
from gen import *
from blocks import *
from sections import *
slug=sys.argv[1]; POST=PAGES[slug]
s=SVC[slug]; C=json.load(open(f'../content/{slug}.json'))
NAME,ICON=SERVICE_NAMES[slug]
GROUPS=D['GROUPS']
b=B(); e=b.el

def h2(cid,t): return e("e-heading",cid,cfg={"tag":"h2","title":t},style="font-size: 32px; @media(--mobile){ font-size: 26px; }")
def para(cid,t): return e("e-paragraph",cid,cfg={"paragraph":t},style="font-size: 16px; line-height: 1.75;")

# ---------- main column ----------
intro=e("e-flexbox","Intro",[e("e-image","Cover",cfg={"image":{"src":{"id":A[IMG[slug]],"alt":f"{NAME} services in Wolverhampton by DigiRanx Pro"},"size":"full"}},style="width: 100%; aspect-ratio: 16 / 8; object-fit: cover; border-radius: 10px; margin-bottom: 8px;"),
    eyebrow(b,"Intro Eyebrow",GROUPS[s['group']]['name']),h2("Intro Title",C['intro']['h2'])]+[para(f"Intro P {i+1}",p) for i,p in enumerate(C['intro']['paras'])],
    style="flex-direction: column; gap: 16px; padding: 0px;")
included=e("e-flexbox","Included",[h2("Included Title","What's Included"),
    e("e-grid","Included Grid",[e("e-flexbox",f"Included {i+1}",[svgi(b,f"Included {i+1} Icon","check",20,"#FF2EA6",style="margin-top: 2px;"),
        e("e-div-block",f"Included {i+1} Copy",[e("e-paragraph",f"Included {i+1} Title",cfg={"paragraph":t},style="font-weight: 700; color: #0E0A1F; font-size: 16.5px;"),e("e-paragraph",f"Included {i+1} Text",cfg={"paragraph":d},style="font-size: 14.5px;")],style="padding: 0px; flex: 1 1 auto;")],
        style="gap: 14px; align-items: flex-start; padding: 18px; border-radius: 10px; background: #F7F3FF; border: 1px solid #DCCFFF;") for i,(t,d) in enumerate(s['feats'])],
        style="grid-template-columns: repeat(2, 1fr); grid-template-rows: auto; gap: 14px; padding: 0px; @media(--mobile){ grid-template-columns: 1fr; }")],
    style="flex-direction: column; gap: 16px; padding: 0px;")
WHY_IC=["users","chart","clock","shield"]
why=e("e-flexbox","Why Block",[eyebrow(b,"Why Eyebrow","Why Choose Us"),h2("Why Title",C['why']['h2']),para("Why Lead",C['why']['lead']),
    e("e-grid","Why Points",[e("e-flexbox",f"Why Point {i+1}",[circle_icon(b,f"Why Point {i+1} Icon",WHY_IC[i%4]),
        e("e-div-block",f"Why Point {i+1} Copy",[e("e-heading",f"Why Point {i+1} Title",cfg={"tag":"h3","title":p['t']},style="font-size: 17px; margin-bottom: 4px;"),e("e-paragraph",f"Why Point {i+1} Text",cfg={"paragraph":p['d']},style="font-size: 14.5px; line-height: 1.6;")],style="padding: 0px; flex: 1 1 auto;")],
        style="gap: 14px; align-items: flex-start; padding: 18px; border-radius: 10px; background: #F7F3FF; border: 1px solid #DCCFFF;") for i,p in enumerate(C['why']['points'])],
        style="grid-template-columns: repeat(2, 1fr); grid-template-rows: auto; gap: 14px; padding: 0px; @media(--mobile){ grid-template-columns: 1fr; }")],
    style="flex-direction: column; gap: 16px; padding: 0px;")
BEN_IC=["trend","target","users","zap","shield","chart"]
ben=e("e-flexbox","Benefits Block",[eyebrow(b,"Benefits Eyebrow","Benefits"),h2("Benefits Title",C['benefits']['h2']),para("Benefits Lead",C['benefits']['lead']),
    e("e-grid","Benefits Grid",[e("e-flexbox",f"Benefit {i+1}",[icon_box(b,f"Benefit {i+1} Icon",BEN_IC[i%6],42),e("e-heading",f"Benefit {i+1} Title",cfg={"tag":"h3","title":x['t']},style="font-size: 17px;"),e("e-paragraph",f"Benefit {i+1} Text",cfg={"paragraph":x['d']},style="font-size: 14.5px; line-height: 1.6;")],
        style="flex-direction: column; gap: 8px; padding: 22px; border-radius: 10px; background: #FFFFFF; border: 1.5px solid #C9B5FF; box-shadow: 0 14px 34px -22px rgba(60,30,160,0.35);",classes=["dg-benefit"]) for i,x in enumerate(C['benefits']['items'])],
        style="grid-template-columns: repeat(2, 1fr); grid-template-rows: auto; gap: 16px; padding: 0px; @media(--mobile){ grid-template-columns: 1fr; }")],
    style="flex-direction: column; gap: 16px; padding: 0px;")
main=e("e-flexbox","Main Column",[intro,included,why,ben],style="flex-direction: column; gap: 44px; padding: 0px; min-width: 0px;")

# ---------- sidebar ----------
links=[e("e-flexbox",f"Side {SERVICE_NAMES[k][0]}",[e("e-flexbox",f"Side {SERVICE_NAMES[k][0]} Icon",[svgi(b,f"Side {SERVICE_NAMES[k][0]} Svg",SERVICE_NAMES[k][1],16,"#FFFFFF" if k==slug else "#7B3BFF")],
        style="flex: 0 0 32px; width: 32px; height: 32px; padding: 0px; border-radius: 8px; align-items: center; justify-content: center; background: "+("rgba(255,255,255,0.2)" if k==slug else "#F1ECFF")+";"),
    e("e-paragraph",f"Side {SERVICE_NAMES[k][0]} Name",cfg={"paragraph":SERVICE_NAMES[k][0]},style="font-size: 15px; font-weight: 600; color: "+("#FFFFFF" if k==slug else "#0E0A1F")+";")],
    cfg={"link":link_page(k)},
    style="gap: 12px; align-items: center; padding: 9px 10px; border-radius: 10px; "+("background: linear-gradient(90deg, #16B4F0 0%, #7B3BFF 100%);" if k==slug else "background: #FFFFFF; border: 1px solid #ECE5FF;"),
    classes=(["dg-side-cur"] if k==slug else ["dg-side-link"])) for k in SVC]
side_list=e("e-flexbox","All Services Box",[e("e-heading","All Services Title",cfg={"tag":"h4","title":"All Services"},style="font-size: 19px; padding: 4px 8px 10px 8px;")]+links,
    style="flex-direction: column; gap: 4px; padding: 18px; border-radius: 10px; background: #F7F3FF; border: 1px solid #DCCFFF;")
qhead,qform=form(b,"Quote Form","quote",subject=f"Quote request: {NAME} - digiranxpro.com",compact=True)
quote=e("e-flexbox","Quote Box",[e("e-heading","Quote Title",cfg={"tag":"h4","title":"Request A Quote"},style="font-size: 20px;"),
    e("e-paragraph","Quote Text",cfg={"paragraph":f"Get a free {NAME} quote within one working day."},style="font-size: 14px; margin-bottom: 8px;"),qform],
    style="flex-direction: column; gap: 4px; padding: 22px; border-radius: 10px; background: #FFFFFF; border: 1px solid #DCCFFF; box-shadow: 0 14px 34px -18px rgba(60,30,160,0.30);",classes=["dg-quote-box"])
side=e("e-flexbox","Sidebar",[side_list,quote],style="flex-direction: column; gap: 20px; padding: 0px; position: sticky; top: 30px; @media(--tablet){ position: static; }")
top=section(b,"Service Content",[e("e-grid","Service Layout",[main,side],style="grid-template-columns: minmax(0, 1fr) 340px; grid-template-rows: auto; gap: 48px; align-items: start; padding: 0px; @media(--tablet){ grid-template-columns: 1fr; }")])

# ---------- packages ----------
def plan(i,p):
    pop=p.get('pop')
    price=[e("e-paragraph",f"Plan {i+1} Price",cfg={"paragraph":"Custom" if p['price']=="Custom" else f"<sup style=\"font-size:24px;color:#7B3BFF\">£</sup>{p['price']}"},style="font-size: 52px; font-weight: 700; line-height: 1; color: #0E0A1F; text-align: center;"),
           e("e-paragraph",f"Plan {i+1} Unit",cfg={"paragraph":"Get a quote" if p['price']=="Custom" else ("One-off" if p['unit']=="one-off" else "Monthly")},style="font-size: 14px; font-weight: 600; text-align: center;")]
    feats=e("e-flexbox",f"Plan {i+1} Features",[e("e-flexbox",f"Plan {i+1} Feature {j+1}",[svgi(b,f"Plan {i+1} Feature {j+1} Icon","check",17,"#7B3BFF",style="margin-top: 3px;"),e("e-paragraph",f"Plan {i+1} Feature {j+1} Text",cfg={"paragraph":f},style="font-size: 14.5px;")],
        style="gap: 10px; align-items: flex-start; padding: 9px 0px; border-bottom: 1px solid #E6E3F0;") for j,f in enumerate(p['feats'])],
        style="flex-direction: column; padding: 6px 16px; border: 1px dashed #DCCFFF; border-radius: 10px; flex: 1 1 auto;")
    pay=e("e-flexbox",f"Plan {i+1} Pay",[e("e-paragraph",f"Plan {i+1} Pay {x}",cfg={"paragraph":x},style="font-size: 10.5px; font-weight: 800; letter-spacing: 0.03em; color: #0E0A1F; padding: 3px 7px; border-radius: 5px; border: 1px solid #E6E3F0;") for x in ["VISA","MASTERCARD","AMEX","PAYPAL"]],style="gap: 8px; justify-content: center; flex-wrap: wrap; padding: 0px;")
    grad="linear-gradient(90deg, #1EC8F5 0%, #7B3BFF 60%, #FF2EA6 100%)" if pop else "linear-gradient(90deg, #16B4F0 0%, #7B3BFF 100%)"
    return e("e-flexbox",f"Plan {i+1}",[
        e("e-flexbox",f"Plan {i+1} Head",[e("e-heading",f"Plan {i+1} Name",cfg={"tag":"h3","title":p['name']+" Plan"},style="color: #FFFFFF; font-size: 24px; font-weight: 600; text-align: center;"),e("e-paragraph",f"Plan {i+1} Desc",cfg={"paragraph":p['desc']},style="color: rgba(255,255,255,0.88); font-size: 13.5px; text-align: center;")]+
            ([e("e-paragraph",f"Plan {i+1} Badge",cfg={"paragraph":"Most Popular"},style="font-size: 11px; font-weight: 800; letter-spacing: 0.08em; text-transform: uppercase; color: #FFFFFF; background: rgba(255,255,255,0.22); padding: 3px 10px; border-radius: 8px; margin-top: 6px;")] if pop else []),
            style=f"flex-direction: column; align-items: center; gap: 4px; padding: 22px 20px; background: {grad};"),
        e("e-flexbox",f"Plan {i+1} Body",price+[feats,button(b,f"Plan {i+1} Button","Get Started",link_page("contact"),"grad",style="width: 100%; text-align: center;"),pay],style="flex-direction: column; gap: 16px; padding: 24px 20px 22px 20px; flex: 1 1 auto;")],
        style="flex-direction: column; padding: 0px; border-radius: 10px; overflow: hidden; background: #FFFFFF; border: "+("2px solid #7B3BFF" if pop else "1px solid #DCCFFF")+"; box-shadow: 0 14px 34px -18px rgba(60,30,160,0.30);")
packages=section(b,"Packages",[head(b,"Packages Head","Choose Price Package",f"{NAME} Packages","Simple, fixed prices in GBP. All prices exclude VAT."),
    e("e-grid","Packages Grid",[plan(i,p) for i,p in enumerate(s['plans'])],style="grid-template-columns: repeat(3, 1fr); grid-template-rows: auto; gap: 20px; align-items: stretch; padding: 0px; @media(--tablet){ grid-template-columns: 1fr; max-width: 460px; margin: 0px auto; }"),
    e("e-flexbox","Packages Need",[e("e-paragraph","Packages Need Text",cfg={"paragraph":"Need a custom package?"},style="font-size: 18px; font-weight: 600; color: #0E0A1F;"),button(b,"Packages Need Button","Contact Our Team",link_page("contact"),"outline",style="padding: 8px 18px; font-size: 14px;")],
        style="justify-content: center; align-items: center; gap: 16px; flex-wrap: wrap; padding: 0px; margin-top: 34px;")],classes=["dg-bg-light"])

steps=timeline_section(b,"Steps","How It Works",C['steps']['h2'],C['steps']['lead'],[(x['t'],x['d']) for x in C['steps']['items']])
GEN=[2,7,6,9]
faq_items=[(f['q'],f['a']) for f in C['faqs']]+[(D['FAQS'][i][1],D['FAQS'][i][2]) for i in GEN]
faqs=faq_box(b,"Service FAQ",faq_items,f"{NAME} Questions Answered",f"Straight answers to what business owners ask us about {NAME}.",light=True)
cta=section(b,"Call CTA",[e("e-flexbox","Call CTA Banner",[
    e("e-flexbox","Call CTA Copy",[e("e-heading","Call CTA Title",cfg={"tag":"h2","title":C['cta']['h2']},style="color: #FFFFFF; font-size: 34px; @media(--mobile){ font-size: 26px; }"),e("e-paragraph","Call CTA Text",cfg={"paragraph":C['cta']['p']},style="color: rgba(255,255,255,0.86);")],style="flex-direction: column; gap: 8px; padding: 0px; flex: 1 1 420px;"),
    e("e-flexbox","Call CTA Actions",[
        e("e-flexbox","Call CTA Phone",[circle_icon(b,"Call CTA Phone Icon","phone",44,"linear-gradient(90deg, #16B4F0 0%, #7B3BFF 100%)"),e("e-paragraph","Call CTA Phone Text",cfg={"paragraph":"+44 7445 652671"},style="font-size: 18px; font-weight: 700; color: #0E0A1F;")],
            cfg={"link":link_url("tel:+447445652671")},style="gap: 12px; align-items: center; padding: 8px 22px 8px 8px; border-radius: 10px; background: #FFFFFF; width: auto; transition: background 0.2s; &:hover { background: #1EC8F5; }"),
        button(b,"Call CTA Book","Book A Free Call",link_page("contact"),"white",True)],style="gap: 10px; flex-wrap: wrap; align-items: center; padding: 0px; width: auto;")],
    style="justify-content: space-between; align-items: center; gap: 24px; flex-wrap: wrap; padding: 44px; border-radius: 10px; background: linear-gradient(100deg, #120A33 0%, #3A1A9E 60%, #7B3BFF 100%); @media(--mobile){ padding: 26px; }")])

hero=page_hero(b,NAME,s['short'],[("Our Services","services"),(NAME,None)],IMG[slug])
json.dump(b.payload(POST,"".join([hero,top,packages,steps,faqs,cta])),open(f'p_svc_{slug}.json','w'))
print(slug,POST)
