import json,sys
from gen import *
b=B(); e=b.el
POST=int(sys.argv[1])
LINK="font-size: 15px; color: rgba(255,255,255,0.85); line-height: 1.5;"
H4="font-size: 17px; font-weight: 600; color: #FFFFFF; margin-bottom: 14px; text-transform: capitalize;"
def flink(cid,text,key=None,url=None):
    return e("e-paragraph",cid,cfg={"paragraph":text,"link":link_page(key) if key else link_url(url)},style=LINK)
soc=[e("e-flexbox",f"Social {n}",[e("e-svg",f"Social {n} Svg",cfg=svg(ic),style="width: 16px; height: 16px; color: #FFFFFF;")],style="flex: 0 0 40px; width: 40px; height: 40px; padding: 0px; border-radius: 50%; border: 1px solid rgba(255,255,255,0.45); align-items: center; justify-content: center; transition: background 0.2s; &:hover { background: #FFFFFF; }",classes=["dg-social"]) for n,ic in [("Facebook","fb"),("Instagram","ig"),("LinkedIn","in"),("YouTube","yt")]]
connect=e("e-flexbox","Connect Strip",[e("e-heading","Connect Title",cfg={"tag":"h3","title":"Get Connected With Us"},style="color: #FFFFFF; font-size: 26px; font-weight: 600; @media(--mobile){ font-size: 20px; }"),
    e("e-flexbox","Social Icons",soc,style="gap: 12px; padding: 0px; width: auto; flex: 0 0 auto;")],
    style="width: 100%; justify-content: center; align-items: center; gap: 24px; flex-wrap: wrap; padding: 16px 24px; background: linear-gradient(90deg, #16B4F0 0%, #7B3BFF 100%);")
col1=e("e-flexbox","Footer About",[e("e-image","Footer Logo",cfg=img("digiranx-pro-logo-full"),style="width: 190px; margin-bottom: 4px;"),
    e("e-paragraph","Footer Tagline",cfg={"paragraph":"Your trusted partner in building a stronger online presence with creative strategies and results-driven digital solutions."},style="font-size: 15px; color: rgba(255,255,255,0.85); line-height: 1.7;"),
    e("e-flexbox","Footer Inline Contact",[
        e("e-flexbox","Footer Inline Phone",[e("e-svg","Footer Inline Phone Svg",cfg=svg("phone"),style="width: 17px; height: 17px; color: #FF2EA6;"),e("e-paragraph","Footer Inline Phone Text",cfg={"paragraph":"+44 7445 652671","link":link_url("tel:+447445652671")},style=LINK)],style="gap: 8px; align-items: center; padding: 0px; width: auto; flex: 0 0 auto;"),
        e("e-flexbox","Footer Inline Email",[e("e-svg","Footer Inline Email Svg",cfg=svg("mail"),style="width: 17px; height: 17px; color: #FF2EA6;"),e("e-paragraph","Footer Inline Email Text",cfg={"paragraph":"info@digiranxpro.com","link":link_url("mailto:info@digiranxpro.com")},style=LINK)],style="gap: 8px; align-items: center; padding: 0px; width: auto; flex: 0 0 auto;")],
        style="gap: 8px 18px; flex-wrap: wrap; padding: 0px; margin-top: 8px;")],
    style="flex-direction: column; gap: 14px; padding: 0px;")
col2=e("e-flexbox","Footer Quick Links",[e("e-heading","Footer Quick Links Title",cfg={"tag":"h4","title":"Quick Links"},style=H4)]+[flink(f"Footer Link {t}",t,k) for t,k in [("Home","home"),("About Us","about"),("Our Services","services"),("Our Blog","blog"),("FAQs","faqs"),("Contact Us","contact"),("Privacy Policy","privacy")]],style="flex-direction: column; gap: 9px; padding: 0px;")
svcs=["seo-digital-marketing","gbp-optimization","web-development","social-media-marketing","google-ads","branding"]
col3=e("e-flexbox","Footer Services",[e("e-heading","Footer Services Title",cfg={"tag":"h4","title":"Services"},style=H4)]+[flink(f"Footer Service {SERVICE_NAMES[k][0]}",SERVICE_NAMES[k][0],k) for k in svcs]+[flink("Footer View All Services","View All Services","services")],style="flex-direction: column; gap: 9px; padding: 0px;")
def crow(cid,ic,text):
    return e("e-flexbox",cid,[e("e-svg",cid+" Svg",cfg=svg(ic),style="flex: 0 0 18px; width: 18px; height: 18px; color: #FF2EA6; margin-top: 3px;"),e("e-paragraph",cid+" Text",cfg={"paragraph":text},style=LINK)],style="gap: 12px; align-items: flex-start; padding: 0px;")
col4=e("e-flexbox","Footer Contact",[e("e-heading","Footer Contact Title",cfg={"tag":"h4","title":"Contact Info"},style=H4),
    crow("Footer Address","pin","Office 1922, 85 Dunstall Hill, Wolverhampton, WV6 0SR, UK"),
    crow("Footer Hours","clock","Monday – Friday: 8am – 10pm<br>Saturday – Sunday: Closed"),
    crow("Footer Phone","phone","+44 7445 652671"),crow("Footer Email","mail","info@digiranxpro.com")],style="flex-direction: column; gap: 14px; padding: 0px;")
grid=e("e-grid","Footer Grid",[col1,col2,col3,col4],style="grid-template-columns: 1.5fr 0.8fr 0.9fr 1.2fr; grid-template-rows: auto; gap: 40px; padding: 0px; @media(--tablet){ grid-template-columns: 1fr 1fr; } @media(--mobile){ grid-template-columns: 1fr; gap: 32px; }")
bottom=e("e-flexbox","Footer Bottom",[
    e("e-flexbox","Footer Policies",[flink("Footer Privacy","Privacy Policy","privacy"),e("e-paragraph","Footer Sep 1",cfg={"paragraph":"|"},style="color: rgba(255,255,255,0.3); font-size: 13.5px;"),flink("Footer Terms","Terms & Conditions","terms"),e("e-paragraph","Footer Sep 2",cfg={"paragraph":"|"},style="color: rgba(255,255,255,0.3); font-size: 13.5px;"),flink("Footer Cookie","Cookie Policy","cookie")],style="gap: 10px; padding: 0px; flex-wrap: wrap; width: auto;"),
    e("e-paragraph","Footer Copyright",cfg={"paragraph":"Copyright © 2026 DIGIRANX PRO LTD. All rights reserved."},style="font-size: 13.5px; color: rgba(255,255,255,0.85);")],
    style="justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 12px; margin-top: 48px; padding: 22px 0px 0px 0px; border-top: 1px solid rgba(255,255,255,0.15);")
main=e("e-flexbox","Footer Main",[e("e-div-block","Footer Wrap",[grid,bottom],style="width: 100%; max-width: 1320px; padding: 0px;")],style="width: 100%; justify-content: center; padding: 60px 24px 28px 24px; background: #110A2E; @media(--mobile){ padding: 48px 16px 24px 16px; }")
totop=e("e-flexbox","Back To Top",[e("e-svg","Back To Top Svg",cfg=svg("arrow"),style="width: 22px; height: 22px; color: #FFFFFF; transform: rotate(-90deg);")],cfg={"link":link_url("#")},
    style="position: fixed; right: 20px; bottom: 20px; z-index: 98; width: 50px; height: 50px; padding: 0px; border-radius: 50%; align-items: center; justify-content: center; background: linear-gradient(90deg, #16B4F0 0%, #7B3BFF 100%); box-shadow: 0 12px 26px -10px rgba(123,59,255,0.8); transition: background 0.2s; &:hover { background: #110A2E; }",classes=["dg-to-top"])
root=e("e-div-block","Site Footer",[connect,main,totop],style="width: 100%; padding: 0px;",classes=["dg-footer"])
json.dump(b.payload(POST,root),open('p_footer.json','w')); print('ok')
