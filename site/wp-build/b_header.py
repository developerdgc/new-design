import json
from gen import *
b=B(); e=b.el
MENU=[("Search & Ads",[("gbp-optimization","GBP Optimization","pin","Rank higher in Google Maps"),("seo-digital-marketing","SEO & Digital Marketing","trend","Page-one Google rankings"),("google-ads","Google Ads","target","Pay-per-click that converts"),("citations-backlinks","Citations & Backlinks","link","Local listings and quality links"),("reviews","Reviews","star","More genuine 5-star reviews")]),
("Design & Social",[("custom-web-design","Custom Web Design","pen","Original designs for your brand"),("ui-ux-design","UI/UX Designing","layout","Journeys people enjoy using"),("graphic-design","Graphic Designing","palette","Social, print and ad creatives"),("branding","Branding","gem","Logos and brand identities"),("social-media-marketing","Social Media Marketing","share","Content, community and ads")]),
("Build & Develop",[("web-development","Web Development","code","Fast, secure websites"),("responsive-development","Responsive Development","devices","Perfect on every screen"),("landing-pages","Landing Pages","window","Pages built to convert ads"),("ecommerce-solutions","E-commerce Solutions","cart","Shopify and WooCommerce stores"),("software-development","Software Development","cpu","Web apps and automation")])]
NAVLINK="font-family: var(--dg-font); font-size: 15.5px; font-weight: 600; color: #FFFFFF; background: transparent; padding: 10px 12px; border-radius: 8px; &:hover { color: #1EC8F5; }"
def navlink(cid,text,key): return e("e-button",cid,cfg={"text":text,"link":link_page(key)},style=NAVLINK)
cols=[]
for gi,(gname,items) in enumerate(MENU):
    rows=[e("e-paragraph",f"Mega Group {gi+1} Title",cfg={"paragraph":gname},style="font-size: 12.5px; font-weight: 700; letter-spacing: 0.12em; text-transform: uppercase; color: #4B2BD6; padding: 4px 12px 10px 12px; border-bottom: 1px solid #E6E3F0; margin-bottom: 6px;")]
    for slug,name,ic,sub in items:
        rows.append(e("e-flexbox",f"Mega Link {name}",[
            e("e-flexbox",f"Mega Icon {name}",[e("e-svg",f"Mega Svg {name}",cfg=svg(ic),style="width: 19px; height: 19px;")],style="flex: 0 0 38px; width: 38px; height: 38px; min-width: 38px; padding: 0px; border-radius: 10px; background: #F1ECFF; color: #7B3BFF; align-items: center; justify-content: center;"),
            e("e-div-block",f"Mega Text {name}",[e("e-paragraph",f"Mega Name {name}",cfg={"paragraph":name},style="font-size: 15.5px; font-weight: 700; color: #0E0A1F; line-height: 1.25;"),e("e-paragraph",f"Mega Sub {name}",cfg={"paragraph":sub},style="font-size: 12.5px; color: #16141F; line-height: 1.35;")],style="padding: 0px; min-width: 0px; flex: 1 1 auto;")],
            cfg={"link":link_page(slug)},style="gap: 12px; align-items: center; width: 100%; padding: 8px 10px; border-radius: 10px; transition: background 0.2s; &:hover { background: #110A2E; }",classes=["dg-mega-link"]))
    cols.append(e("e-flexbox",f"Mega Column {gi+1}",rows,style="flex-direction: column; gap: 2px; padding: 0px;"))
mega=e("e-div-block","Mega Panel",[
    e("e-grid","Mega Grid",cols,style="grid-template-columns: repeat(3, 1fr); grid-template-rows: auto; gap: 14px; padding: 0px;"),
    e("e-flexbox","Mega Footer",[e("e-paragraph","Mega Footer Note",cfg={"paragraph":"15 services, one Wolverhampton team. Mon – Fri, 8am – 10pm."},style="font-size: 14.5px; color: #16141F;"),
        e("e-paragraph","Mega View All",cfg={"paragraph":"View All Services →","link":link_page("services")},style="font-size: 15px; font-weight: 700; color: #4B2BD6; &:hover { color: #FF2EA6; }")],
        style="justify-content: space-between; align-items: center; gap: 12px; flex-wrap: wrap; margin-top: 10px; padding: 14px 12px 0px 12px; border-top: 1px solid #E6E3F0;")],
    style="position: absolute; left: 0px; right: 0px; top: 100%; padding: 22px; margin-top: 12px; background: #FFFFFF; border-radius: 10px; box-shadow: 0 30px 70px -20px rgba(10,6,32,0.45); z-index: 100;",classes=["dg-mega-panel"])
services=e("e-div-block","Services Menu Item",[
    e("e-flexbox","Services Trigger",[e("e-paragraph","Services Label",cfg={"paragraph":"Our Services","link":link_page("services")},style="font-size: 16px; font-weight: 600; color: #FFFFFF; &:hover { color: #1EC8F5; }"),
        e("e-svg","Services Chevron",cfg=svg("chev"),style="width: 16px; height: 16px; color: #FFFFFF;")],style="gap: 6px; align-items: center; padding: 10px 12px; cursor: pointer; width: auto; flex: 0 0 auto;"),
    mega],style="padding: 0px; min-width: 0px; position: static; width: auto; flex: 0 0 auto;",classes=["dg-mega-item"])
nav=e("e-flexbox","Main Navigation",[navlink("Nav Home","Home","home"),navlink("Nav About","About Us","about"),services,navlink("Nav Blog","Our Blog","blog"),navlink("Nav FAQs","FAQs","faqs"),navlink("Nav Contact","Contact Us","contact")],
    style="gap: 2px; align-items: center; padding: 0px; flex: 0 1 auto; width: auto; @media(--tablet){ display: none; }")
brand=e("e-flexbox","Brand",[e("e-image","Logo Icon",cfg=img("digiranx-pro-logo-icon"),style="width: 40px; @media(--mobile){ width: 32px; }"),
    e("e-image","Logo Wordmark",cfg=img("digiranx-pro-logo-wordmark"),style="width: 148px; @media(--mobile){ width: 108px; }")],cfg={"link":link_page("home")},style="gap: 10px; align-items: center; padding: 0px; flex: 0 0 auto; width: auto;")
call=e("e-flexbox","Call Button",[
    e("e-flexbox","Call Icon",[e("e-svg","Call Svg",cfg=svg("phone"),style="width: 17px; height: 17px; color: #FFFFFF;")],style="flex: 0 0 36px; width: 36px; height: 36px; padding: 0px; border-radius: 6px; background: rgba(255,255,255,0.2); align-items: center; justify-content: center;"),
    e("e-div-block","Call Text",[e("e-paragraph","Call Label",cfg={"paragraph":"Call us today"},style="font-size: 11.5px; font-weight: 600; color: rgba(255,255,255,0.85); line-height: 1.1;"),
        e("e-paragraph","Call Number",cfg={"paragraph":"+44 7445 652671"},style="font-size: 16px; font-weight: 700; color: #FFFFFF; line-height: 1.2;")],style="padding: 0px; @media(--mobile){ display: none; }")],
    cfg={"link":link_url("tel:+447445652671")},style="gap: 10px; align-items: center; width: auto; flex: 0 0 auto; padding: 6px 16px 6px 6px; border-radius: 8px; background: linear-gradient(90deg, #16B4F0 0%, #7B3BFF 100%); box-shadow: 0 8px 22px -10px rgba(123,59,255,0.7); transition: background 0.2s; &:hover { background: #FFFFFF; } @media(--mobile){ padding: 5px; }",classes=["dg-call-btn"])
burger=e("e-flexbox","Menu Toggle",[e("e-svg","Menu Toggle Svg",cfg=svg("menu"),style="width: 22px; height: 22px; color: #FFFFFF;")],
    cfg={"link":{"destination":{"name":"popup","settings":{"popup":"133"}},"tag":"a"}},style="display: none; flex: 0 0 46px; width: 46px; height: 46px; padding: 0px; border-radius: 8px; border: 1px solid rgba(255,255,255,0.25); align-items: center; justify-content: center; @media(--tablet){ display: flex; }")
actions=e("e-flexbox","Header Actions",[call,burger],style="gap: 10px; align-items: center; padding: 0px; flex: 0 0 auto; width: auto;")
bar=e("e-flexbox","Header Bar",[brand,nav,actions],style="width: 100%; max-width: 1320px; position: relative; justify-content: space-between; align-items: center; gap: 14px; padding: 10px 10px 10px 22px; background: rgba(10,6,32,0.82); border: 1px solid rgba(200,190,255,0.22); border-radius: 10px; backdrop-filter: blur(12px); @media(--mobile){ padding: 8px 8px 8px 12px; }")
shell=e("e-flexbox","Header Shell",[bar],style="position: absolute; top: 16px; left: 0px; right: 0px; z-index: 99; justify-content: center; padding: 0px 24px; @media(--mobile){ padding: 0px 12px; top: 12px; }")
json.dump(b.payload(141,shell),open('p_header.json','w'))
print(141)
