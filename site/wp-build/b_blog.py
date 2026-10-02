import json,sys
from gen import *
from blocks import *
ARCH,SINGLE=int(sys.argv[1]),int(sys.argv[2])
DT=lambda n,s=None:{"name":n,"settings":s or {}}
# ---------- ARCHIVE ----------
b=B(); e=b.el
card=e("e-collection-loop-item","Post Card Item",[e("e-flexbox","Post Card",[
    e("e-image","Post Card Image",cfg={"image":{"src":DT("post-featured-image"),"size":"medium_large"}},style="width: 100%; aspect-ratio: 16 / 10; object-fit: cover;"),
    e("e-flexbox","Post Card Body",[
        e("e-paragraph","Post Card Date",cfg={"paragraph":DT("post-date")},style="font-size: 13px; font-weight: 600; color: #D0157F; background: #FFE6F4; padding: 4px 10px; border-radius: 8px; width: fit-content;"),
        e("e-heading","Post Card Title",cfg={"tag":"h3","title":DT("post-title")},style="font-size: 20px; font-weight: 700; text-transform: none;"),
        e("e-paragraph","Post Card Excerpt",cfg={"paragraph":DT("post-excerpt",{"max_length":22})},style="font-size: 15px;"),
        e("e-paragraph","Post Card More",cfg={"paragraph":"Read More →"},style="font-size: 15px; font-weight: 700; color: #4B2BD6;")],
        style="flex-direction: column; gap: 10px; padding: 20px 22px 24px 22px; flex: 1 1 auto;")],
    cfg={"link":{"destination":DT("post-url"),"tag":"a"}},
    style="flex-direction: column; padding: 0px; height: 100%; border-radius: 10px; overflow: hidden; background: #F7F3FF; border: 1px solid #DCCFFF; box-shadow: 0 14px 34px -18px rgba(60,30,160,0.30); transition: border-color 0.25s, transform 0.25s; &:hover { border-color: #9B6BFF; transform: translateY(-4px); }",classes=["dg-post-card"])],style="padding: 0px;")
loop=e("e-collection-loop","Blog Loop",[e("e-collection-loop-layout","Blog Loop Grid",[card],style="grid-template-columns: repeat(3, 1fr); gap: 22px; @media(--tablet){ grid-template-columns: repeat(2, 1fr); } @media(--mobile){ grid-template-columns: 1fr; }")],
    cfg={"query":{"template_type":"post","source":"current_query","posts_per_page":9}},style="width: 100%;")
arch=[page_hero(b,"Our Blog","Practical guides on SEO, Google Maps, websites and ads for UK business owners.",[("Our Blog",None)],"blog-social-media-strategy"),
    section(b,"Blog List",[loop]),final_cta(b)]
json.dump(b.payload(ARCH,"".join(arch)),open('p_archive.json','w'))
# ---------- SINGLE ----------
b=B(); e=b.el
hero=e("e-flexbox","Post Hero",[e("e-flexbox","Post Hero Wrap",[
    e("e-flexbox","Post Crumbs",[e("e-paragraph","Post Crumb Home",cfg={"paragraph":"Home","link":link_page("home")},style="font-size: 14.5px; font-weight: 600; color: #1EC8F5;"),e("e-paragraph","Post Crumb Sep",cfg={"paragraph":"›"},style="font-size: 14.5px; color: rgba(255,255,255,0.6);"),
        e("e-paragraph","Post Crumb Blog",cfg={"paragraph":"Our Blog","link":link_page("blog")},style="font-size: 14.5px; font-weight: 600; color: #1EC8F5;")],style="gap: 8px; align-items: center; justify-content: center; width: auto; padding: 8px 18px; border-radius: 8px; background: rgba(255,255,255,0.1);",classes=["dg-crumbs"]),
    e("e-heading","Post Title",cfg={"tag":"h1","title":DT("post-title")},style="color: #FFFFFF; text-align: center; font-size: 48px; max-width: 900px; text-transform: none; @media(--tablet){ font-size: 38px; } @media(--mobile){ font-size: 30px; }"),
    e("e-paragraph","Post Meta",cfg={"paragraph":DT("post-date",{"before":"Published "})},style="color: rgba(255,255,255,0.85); font-size: 15px;")],
    style="flex-direction: column; align-items: center; gap: 16px; max-width: 1320px; width: 100%; padding: 0px;")],
    style=f"flex-direction: column; align-items: center; justify-content: center; min-height: 460px; padding: 200px 24px 110px 24px; background: linear-gradient(90deg, rgba(11,6,36,0.94) 0%, rgba(26,14,82,0.88) 55%, rgba(98,46,240,0.6) 100%), {bgurl('blog-team-planning')} center / cover no-repeat; @media(--tablet){{ min-height: 380px; padding: 160px 24px 80px 24px; }} @media(--mobile){{ padding: 140px 16px 64px 16px; }}")
body=e("e-flexbox","Post Section",[e("e-div-block","Post Article",[
    e("e-image","Post Featured Image",cfg={"image":{"src":DT("post-featured-image"),"size":"full"}},style="width: 100%; aspect-ratio: 16 / 9; object-fit: cover; border-radius: 10px; margin-bottom: 28px;"),
    e("e-div-block","Post Body",[e("theme-post-content","Post Content")],style="padding: 0px;",classes=["dg-post-body"]),
    e("e-flexbox","Post CTA",[e("e-heading","Post CTA Title",cfg={"tag":"h3","title":"Want Us To Do This For You?"},style="color: #FFFFFF; font-size: 22px;"),
        e("e-paragraph","Post CTA Text",cfg={"paragraph":"Our team can handle it end to end. Get a free audit and a clear plan."},style="color: rgba(255,255,255,0.8);"),
        button(b,"Post CTA Button","Get A Free Audit",link_page("contact"),"grad",True)],
        style="flex-direction: column; align-items: flex-start; gap: 12px; padding: 28px; margin-top: 36px; border-radius: 10px; background: #110A2E;")],
    style="max-width: 780px; width: 100%; padding: 0px;")],style="justify-content: center; padding: 72px 24px; @media(--mobile){ padding: 48px 16px; }")
json.dump(b.payload(SINGLE,hero+body+final_cta(b)),open('p_single.json','w'))
print('ok')
