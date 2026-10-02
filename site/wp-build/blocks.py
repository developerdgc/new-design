"""Reusable section builders shared by all pages."""
from gen import *
UP="https://digiranxpro.com/wp-content/uploads/2026/10/"
def bgurl(name,ext="jpg"): return f"url({UP}{name}.{ext})"
WHITE="#FFFFFF"

def section(b,cid,kids,style="",classes=None,wrap_style=""):
    e=b.el
    return e("e-flexbox",cid,[e("e-flexbox",cid+" Wrap",kids,style="flex-direction: column; "+wrap_style,classes=["dg-wrap"])],
             style="flex-direction: column; align-items: center; "+style,classes=["dg-section"]+(classes or []))

def eyebrow(b,cid,text,dark=False):
    return b.el("e-paragraph",cid,cfg={"paragraph":text},classes=["dg-eyebrow"]+(["dg-eyebrow-dark"] if dark else []))

def head(b,cid,eyebrow_text,title,lead=None,center=True,dark=False,tag="h2",style=""):
    e=b.el
    kids=[eyebrow(b,cid+" Eyebrow",eyebrow_text,dark),
          e("e-heading",cid+" Title",cfg={"tag":tag,"title":title},classes=(["dg-text-white"] if dark else None))]
    if lead: kids.append(e("e-paragraph",cid+" Lead",cfg={"paragraph":lead},classes=["dg-lead"]+(["dg-text-soft-white"] if dark else [])))
    return e("e-flexbox",cid,kids,style=style,classes=["dg-sec-head-center" if center else "dg-sec-head"])

def button(b,cid,text,link,kind="grad",on_dark=False,style=None):
    cls=["dg-btn","dg-btn-"+kind]
    if on_dark and kind=="grad": cls=["dg-btn-grad-on-dark"]+cls
    if on_dark and kind=="white": cls=["dg-btn-white-on-dark"]+cls
    return b.el("e-button",cid,cfg={"text":text,"link":link},classes=cls,style=style)

def svgi(b,cid,ic,size=20,color=None,style=""):
    return b.el("e-svg",cid,cfg=svg(ic),style=f"width: {size}px; height: {size}px; flex: 0 0 {size}px; "+(f"color: {color}; " if color else "")+style)

def circle_icon(b,cid,ic,size=44,bg="#FF2EA6"):
    return b.el("e-flexbox",cid,[svgi(b,cid+" Svg",ic,int(size*0.42),"#FFFFFF")],
        style=f"flex: 0 0 {size}px; width: {size}px; height: {size}px; padding: 0px; border-radius: 50%; background: {bg}; align-items: center; justify-content: center;")

def icon_box(b,cid,ic,size=44):
    return b.el("e-flexbox",cid,[svgi(b,cid+" Svg",ic,int(size*0.45),"#7B3BFF")],
        style=f"flex: 0 0 {size}px; width: {size}px; height: {size}px; padding: 0px; border-radius: 10px; background: #F1ECFF; align-items: center; justify-content: center;")

def stars(b,cid,color="#FF2EA6"):
    return b.el("e-flexbox",cid,[svgi(b,f"{cid} {i}","star",16,color) for i in range(5)],style="gap: 3px; padding: 0px; width: auto; flex: 0 0 auto;")

def page_hero(b,title,lead,crumbs,img_name):
    """Inner page banner. crumbs: list of (label, page_key or None)."""
    e=b.el
    cr=[e("e-paragraph","Crumb Home",cfg={"paragraph":"Home","link":link_page("home")},style="font-size: 14.5px; font-weight: 600; color: #1EC8F5;")]
    for i,(lab,key) in enumerate(crumbs):
        cr.append(e("e-paragraph",f"Crumb Sep {i}",cfg={"paragraph":"›"},style="font-size: 14.5px; color: rgba(255,255,255,0.6);"))
        cfg={"paragraph":lab}
        if key: cfg["link"]=link_page(key)
        cr.append(e("e-paragraph",f"Crumb {i}",cfg=cfg,style="font-size: 14.5px; font-weight: 600; color: "+("#1EC8F5" if key else "#FFFFFF")+";"))
    kids=[e("e-heading","Page Title",cfg={"tag":"h1","title":title},style="color: #FFFFFF; text-align: center; font-size: 56px; @media(--tablet){ font-size: 44px; } @media(--mobile){ font-size: 34px; }")]
    if lead: kids.append(e("e-paragraph","Page Lead",cfg={"paragraph":lead},style="color: rgba(255,255,255,0.86); font-size: 17px; text-align: center; max-width: 680px;"))
    kids.append(e("e-flexbox","Breadcrumbs",cr,style="gap: 8px; align-items: center; flex-wrap: wrap; justify-content: center; width: auto; padding: 8px 18px; border-radius: 8px; background: rgba(255,255,255,0.1);",classes=["dg-crumbs"]))
    return e("e-flexbox","Page Hero",[e("e-flexbox","Page Hero Wrap",kids,style="flex-direction: column; align-items: center; gap: 14px; max-width: 1320px; width: 100%; padding: 0px;")],
        style=f"flex-direction: column; align-items: center; justify-content: center; min-height: 460px; padding: 200px 24px 110px 24px; background: linear-gradient(90deg, rgba(11,6,36,0.94) 0%, rgba(26,14,82,0.88) 55%, rgba(98,46,240,0.6) 100%), {bgurl(img_name)} center / cover no-repeat; @media(--tablet){{ min-height: 380px; padding: 160px 24px 80px 24px; }} @media(--mobile){{ padding: 140px 16px 64px 16px; }}")

def help_card(b,cid,title="Still Have A Question?",text="Talk to our team Monday to Friday, 8am to 10pm."):
    e=b.el
    def row(rid,ic,val,link):
        return e("e-flexbox",rid,[svgi(b,rid+" Svg",ic,18,"#FF2EA6"),e("e-paragraph",rid+" Text",cfg={"paragraph":val,"link":link_url(link)},style="font-size: 15px; font-weight: 700; color: #FFFFFF;")],
            style="gap: 10px; align-items: center; padding: 11px 14px; border-radius: 10px; background: rgba(255,255,255,0.08);",classes=["dg-help-row"])
    return e("e-flexbox",cid,[e("e-heading",cid+" Title",cfg={"tag":"h3","title":title},style="color: #FFFFFF; font-size: 22px;"),
        e("e-paragraph",cid+" Text",cfg={"paragraph":text},style="color: rgba(255,255,255,0.78); font-size: 15px;"),
        row(cid+" Phone","phone","+44 7445 652671","tel:+447445652671"),row(cid+" Email","mail","info@digiranxpro.com","mailto:info@digiranxpro.com")],
        style="flex-direction: column; gap: 12px; padding: 26px; border-radius: 10px; background: #110A2E;",classes=["dg-help-card"])

def faq_accordion(b,cid,items,tint=True,schema=True):
    """items: list of (q,a)."""
    e=b.el
    its=[acc_item(b,f"{cid} {i+1}",[e("e-paragraph",f"{cid} {i+1} Q",cfg={"paragraph":q},style="font-size: 17px; font-weight: 700; color: #0E0A1F; text-transform: capitalize; @media(--mobile){ font-size: 16px; }")],
            [e("e-paragraph",f"{cid} {i+1} A",cfg={"paragraph":a},style="font-size: 15.5px; line-height: 1.7;")],
            item_style="padding: 0px; border-radius: 10px; border: 1px solid #DCCFFF; background: "+("#F7F3FF" if tint else "#FFFFFF")+"; overflow: hidden;",
            header_style="padding: 18px 20px; gap: 16px; @media(--mobile){ padding: 16px; }",content_style="padding: 0px 20px 20px 20px;",
            icon="plus",icon_style="width: 18px; height: 18px; color: #7B3BFF;") for i,(q,a) in enumerate(items)]
    return e("e-accordion",cid,its,cfg={"default_state":"first_expanded","max_expanded":"one","show_icon":True,"faq_schema":schema},style="gap: 12px; padding: 0px;",classes=["dg-faq"])

def form(b,cid,fields_id,title=None,note=None,subject="New enquiry from digiranxpro.com",compact=False):
    """Contact/audit form wrapped in e-form."""
    e=b.el
    from gen import SERVICE_NAMES
    LBL="font-size: 13.5px; font-weight: 700; color: #0E0A1F; margin-bottom: 6px;"
    INP="width: 100%; height: auto; padding: 12px 16px; border-radius: 10px; border: 1px solid #E6E3F0; background: #F6F5FB; font-size: 15px; color: #0E0A1F; &:focus { border-color: #7B3BFF; background: #FFFFFF; }"
    half="" if compact else "flex: 1 1 calc(50% - 8px); min-width: 220px;"
    def fld(key,label,kind,ph,full=False,required=False):
        fid=f"{fields_id}-{key}"
        inner=[e("e-form-label",f"{cid} {label} Label",cfg={"text":label,"input-id":fid},style=LBL)]
        if kind=="textarea":
            inner.append(e("e-form-textarea",f"{cid} {label} Field",cfg={"placeholder":ph,"rows":4,"required":required},style=INP+" min-height: 110px;"))
        elif kind=="select":
            opts=[{"key":"Select a service","value":"Select a service"}]+[{"key":v[0].replace("&","and"),"value":v[0].replace("&","and")} for v in SERVICE_NAMES.values()]+[{"key":"Not sure yet","value":"Not sure yet"}]
            inner.append(e("e-form-select",f"{cid} {label} Field",cfg={"name":key,"options":opts},style=INP))
        else:
            inner.append(e("e-form-input",f"{cid} {label} Field",cfg={"placeholder":ph,"type":kind,"required":required,"_cssid":fid},style=INP))
        return e("e-div-block",f"{cid} {label} Group",inner,style="padding: 0px; "+("flex: 1 1 100%;" if full or compact else half))
    kids=[fld("name","Full Name","text","John Smith",required=True),fld("email","Email Address","email","john@company.co.uk",required=True),
          fld("phone","Phone Number","tel","07xxx xxxxxx"),fld("service","Service Needed","select",""),
          fld("message","About Your Business","textarea","Your website, what you sell and what you'd like to improve",full=True),
          e("e-form-submit-button",f"{cid} Submit",cfg={"text":"Send Request"},classes=["dg-btn","dg-btn-grad"],style="margin-top: 4px;"+(" width: 100%;" if compact else "")),
          e("e-form-success-message",f"{cid} Success",[e("e-paragraph",f"{cid} Success Text",cfg={"paragraph":"Thanks! Your request has been sent. We reply within one working day, Monday to Friday."},style="font-size: 14.5px; color: #0E0A1F;")],style="flex: 1 1 100%; border-radius: 10px; background: #F1ECFF; padding: 14px;"),
          e("e-form-error-message",f"{cid} Error",[e("e-paragraph",f"{cid} Error Text",cfg={"paragraph":"Sorry, something went wrong. Please call +44 7445 652671 or email info@digiranxpro.com."},style="font-size: 14.5px; color: #8A0F4F;")],style="flex: 1 1 100%; border-radius: 10px; background: #FFE6F4; padding: 14px;")]
    frm=e("e-form",cid,kids,cfg={"form-name":title or "Website Enquiry","actions-after-submit":["email"],
        "email":{"to":["info@digiranxpro.com"],"subject":subject,"reply-to":"","from-name":"DigiRanx Pro Website"}},
        style="gap: 14px 16px; align-items: flex-start;")
    head=[]
    if title: head.append(e("e-heading",cid+" Heading",cfg={"tag":"h3","title":title},style="font-size: 24px;"))
    if note: head.append(e("e-paragraph",cid+" Note",cfg={"paragraph":note},style="font-size: 14.5px; margin-bottom: 6px;"))
    return head,frm

def final_cta(b):
    e=b.el
    copy=e("e-flexbox","Final CTA Copy",[
        e("e-heading","Final CTA Title",cfg={"tag":"h2","title":"Ready To Grow Your Business Online?"},style="color: #FFFFFF; font-size: 36px; @media(--mobile){ font-size: 26px; }"),
        e("e-paragraph","Final CTA Text",cfg={"paragraph":"Book a free 30-minute strategy call. We'll look at your website, your Google profile and your competitors, and give you a clear plan."},style="color: rgba(255,255,255,0.9); font-size: 15.5px;"),
        e("e-flexbox","Final CTA Buttons",[button(b,"Final CTA Call","Book A Free Call",link_page("contact"),"white",True),button(b,"Final CTA Services","View Services",link_page("services"),"ghost-w")],style="gap: 10px; flex-wrap: wrap; padding: 0px; margin-top: 6px;")],
        style="flex-direction: column; align-items: flex-start; gap: 14px; padding: 48px; width: 50%; margin-left: auto; @media(--tablet){ width: 100%; padding: 32px; } @media(--mobile){ padding: 26px; }")
    banner=e("e-flexbox","Final CTA Banner",[copy],style=f"width: 100%; min-height: 330px; align-items: center; padding: 0px; border-radius: 10px; overflow: hidden; background: linear-gradient(90deg, rgba(30,170,245,0.35) 0%, rgba(98,46,240,0.85) 55%, rgba(75,30,210,0.98) 100%), {bgurl('digital-strategy-meeting')} left center / cover no-repeat; @media(--tablet){{ background: linear-gradient(180deg, rgba(30,170,245,0.55), rgba(98,46,240,0.95)), {bgurl('digital-strategy-meeting')} center / cover no-repeat; }}")
    return section(b,"Final CTA",[banner],style="padding-top: 0px;")
