import json,sys
from gen import *
from blocks import *
b=B(); e=b.el
pop=["seo-digital-marketing","gbp-optimization","web-development","google-ads"]
chips=[e("e-paragraph",f"Popular {SERVICE_NAMES[k][0]}",cfg={"paragraph":SERVICE_NAMES[k][0],"link":link_page(k)},style="font-size: 14.5px; font-weight: 600; color: #FFFFFF; padding: 8px 14px; border-radius: 8px; border: 1px solid rgba(255,255,255,0.3);",classes=["dg-chip"]) for k in pop]
root=e("e-flexbox","Not Found",[e("e-flexbox","Not Found Wrap",[
    e("e-paragraph","Not Found Code",cfg={"paragraph":"404"},style="font-size: 140px; font-weight: 800; line-height: 1; @media(--mobile){ font-size: 96px; }",classes=["dg-grad-text"]),
    e("e-heading","Not Found Title",cfg={"tag":"h1","title":"Page Not Found"},style="color: #FFFFFF; font-size: 44px; text-align: center; @media(--mobile){ font-size: 32px; }"),
    e("e-paragraph","Not Found Text",cfg={"paragraph":"The page you are looking for has moved or no longer exists. Try one of these links instead."},style="color: rgba(255,255,255,0.85); font-size: 17px; text-align: center; max-width: 560px;"),
    e("e-flexbox","Not Found Buttons",[button(b,"Not Found Home","Back To Home",link_page("home"),"grad",True),button(b,"Not Found Contact","Contact Us",link_page("contact"),"ghost-w")],style="gap: 12px; flex-wrap: wrap; justify-content: center; padding: 0px; margin-top: 8px;"),
    e("e-paragraph","Popular Label",cfg={"paragraph":"Popular services"},style="color: #FF2EA6; font-size: 13px; font-weight: 700; letter-spacing: 0.1em; text-transform: uppercase; margin-top: 26px;"),
    e("e-flexbox","Popular Links",chips,style="gap: 10px; flex-wrap: wrap; justify-content: center; padding: 0px;")],
    style="flex-direction: column; align-items: center; gap: 14px; max-width: 900px; width: 100%; padding: 0px;")],
    style=f"flex-direction: column; align-items: center; justify-content: center; min-height: 100vh; padding: 180px 24px 100px 24px; background: radial-gradient(50% 60% at 50% 40%, rgba(123,59,255,0.45), transparent 70%), linear-gradient(180deg, rgba(11,6,36,0.94), rgba(42,20,120,0.92)), {bgurl('digiranx-hero-tech-texture')} center / cover no-repeat; @media(--mobile){{ padding: 140px 16px 80px 16px; }}")
json.dump(b.payload(int(sys.argv[1]),root),open('p_404.json','w'))
