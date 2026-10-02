import json
from gen import *
b=B(); e=b.el
ROW="font-size: 18px; font-weight: 700; color: #0E0A1F; padding: 14px 4px; border-bottom: 1px solid #E6E3F0;"
def mlink(cid,text,key): return e("e-paragraph",cid,cfg={"paragraph":text,"link":link_page(key)},style=ROW)
svc_rows=[e("e-flexbox",f"Mobile Svc {SERVICE_NAMES[k][0]}",[e("e-flexbox",f"Mobile Svc Icon {SERVICE_NAMES[k][0]}",[e("e-svg",f"Mobile Svc Svg {SERVICE_NAMES[k][0]}",cfg=svg(SERVICE_NAMES[k][1]),style="width: 16px; height: 16px;")],style="flex: 0 0 32px; width: 32px; height: 32px; padding: 0px; border-radius: 8px; background: #F1ECFF; color: #7B3BFF; align-items: center; justify-content: center;"),
    e("e-paragraph",f"Mobile Svc Name {SERVICE_NAMES[k][0]}",cfg={"paragraph":SERVICE_NAMES[k][0]},style="font-size: 15px; font-weight: 600; color: #0E0A1F;")],cfg={"link":link_page(k)},style="gap: 12px; align-items: center; padding: 7px 4px;") for k in ["gbp-optimization","seo-digital-marketing","google-ads","citations-backlinks","reviews","custom-web-design","ui-ux-design","graphic-design","branding","social-media-marketing","web-development","responsive-development","landing-pages","ecommerce-solutions","software-development"]]
svc_rows.insert(0,e("e-paragraph","Mobile All Services",cfg={"paragraph":"View All Services →","link":link_page("services")},style="font-size: 15px; font-weight: 700; color: #4B2BD6; padding: 6px 4px 10px 4px;"))
acc=e("e-accordion","Mobile Services Accordion",[acc_item(b,"Mobile Services",[e("e-paragraph","Mobile Services Label",cfg={"paragraph":"Our Services"},style="font-size: 18px; font-weight: 700; color: #0E0A1F;")],svc_rows,
    header_style="padding: 14px 4px; border-bottom: 1px solid #E6E3F0;",content_style="padding: 6px 0px; display: flex; flex-direction: column; gap: 2px;",icon="chev",icon_style="width: 18px; height: 18px; color: #0E0A1F;")],
    cfg={"default_state":"all_collapsed","max_expanded":"one","show_icon":True},style="padding: 0px;")
top=e("e-flexbox","Mobile Menu Top",[e("e-image","Mobile Logo Icon",cfg=img("digiranx-pro-logo-icon"),style="width: 34px;"),e("e-image","Mobile Logo Word",cfg=img("digiranx-pro-logo-wordmark"),style="width: 120px;")],cfg={"link":link_page("home")},
    style="gap: 8px; align-items: center; padding: 12px; border-radius: 10px; background: #110A2E; margin-bottom: 8px;")
call=e("e-button","Mobile Call Button",cfg={"text":"Call +44 7445 652671","link":link_url("tel:+447445652671")},style="margin-top: 20px; width: 100%; text-align: center;",classes=["dg-btn","dg-btn-grad"])
mail=e("e-paragraph","Mobile Email",cfg={"paragraph":"info@digiranxpro.com","link":link_url("mailto:info@digiranxpro.com")},style="margin-top: 10px; text-align: center; font-size: 15px; font-weight: 600;")
root=e("e-flexbox","Mobile Menu",[top,mlink("Mobile Home","Home","home"),mlink("Mobile About","About Us","about"),acc,mlink("Mobile Blog","Our Blog","blog"),mlink("Mobile FAQs","FAQs","faqs"),mlink("Mobile Contact","Contact Us","contact"),call,mail],
    style="flex-direction: column; padding: 20px; background: #FFFFFF; gap: 0px;",classes=["dg-mobile-menu"])
json.dump(b.payload(133,root),open('p_popup.json','w')); print('ok')
