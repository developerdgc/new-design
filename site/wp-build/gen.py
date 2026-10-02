"""Tiny builder for elementor-build-composition payloads."""
import json, itertools, re
A={a['title']:a['id'] for a in json.load(open('assets.json'))}
PAGES={"home":39,"about":40,"services":41,"blog":42,"faqs":43,"contact":44,"terms":45,"cookie":46,"privacy":3,
 "gbp-optimization":47,"web-development":48,"custom-web-design":49,"responsive-development":50,"ui-ux-design":51,"graphic-design":52,"reviews":53,"seo-digital-marketing":54,"landing-pages":55,"software-development":56,"social-media-marketing":57,"branding":58,"google-ads":59,"citations-backlinks":60,"ecommerce-solutions":61}
def icon(n): return A['icon-'+n]
class B:
    def __init__(s): s.cfg={}; s.sty={}; s.cls={}; s.ids=set()
    def el(s,tag,cid,kids=(),cfg=None,style=None,classes=None):
        cid=re.sub(r'[^A-Za-z0-9 _-]','',cid.replace('&','and')).strip()
        assert cid not in s.ids, cid; s.ids.add(cid)
        if cfg: s.cfg[cid]=cfg
        if style: s.sty[cid]=style
        if classes: s.cls[cid]=classes
        inner="".join(kids)
        return f'<{tag} configuration-id="{cid}">{inner}</{tag}>'
    def payload(s,post_id,xml,parent="document",mode="replace_children"):
        return {"post_id":post_id,"xml_structure":xml,"element_config":s.cfg,"style":s.sty,"classes":s.cls,"parent_id":parent,"mode":mode}
def link_page(key,label=None): return {"destination":{"id":PAGES[key]},"tag":"a"}
def link_url(u,blank=False): return {"destination":u,"isTargetBlank":blank,"tag":"a"}
def img(name,size="full"): return {"image":{"src":{"id":A[name]},"size":size}}
def svg(n): return {"svg":{"id":icon(n)}}
SERVICE_NAMES={"gbp-optimization":("GBP Optimization","pin"),"web-development":("Web Development","code"),"custom-web-design":("Custom Web Design","pen"),"responsive-development":("Responsive Development","devices"),"ui-ux-design":("UI/UX Designing","layout"),"graphic-design":("Graphic Designing","palette"),"reviews":("Reviews","star"),"seo-digital-marketing":("SEO & Digital Marketing","trend"),"landing-pages":("Landing Pages","window"),"software-development":("Software Development","cpu"),"social-media-marketing":("Social Media Marketing","share"),"branding":("Branding","gem"),"google-ads":("Google Ads","target"),"citations-backlinks":("Citations & Backlinks","link"),"ecommerce-solutions":("E-commerce Solutions","cart")}
def acc_item(b,cid,title_kids,content_kids,item_style=None,header_style=None,content_style=None,icon="plus",icon_style="width: 16px; height: 16px;"):
    e=b.el
    return e("e-accordion-item",cid,[
        e("e-accordion-item-header",cid+" Header",[e("e-accordion-item-title",cid+" Title",title_kids),
            e("e-accordion-item-icon",cid+" Icon",[e("e-svg",cid+" Icon Svg",cfg=svg(icon),style=icon_style)],style="width: auto; height: auto;")],style=header_style),
        e("e-accordion-item-content",cid+" Content",content_kids,style=content_style)],style=item_style)
