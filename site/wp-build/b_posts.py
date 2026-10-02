import json,subprocess,base64,urllib.request,ssl
from gen import *
D=json.load(open('data.json'))
import os; AUTH="Basic "+os.environ["DIGIRANX_MCP_AUTH"]
ctx=ssl.create_default_context(cafile="/root/.ccr/ca-bundle.crt")
def rest(method,path,body=None):
    req=urllib.request.Request("https://digiranxpro.com/wp-json/wp/v2/"+path,data=json.dumps(body).encode() if body else None,headers={"Authorization":AUTH,"Content-Type":"application/json"},method=method)
    with urllib.request.urlopen(req,context=ctx) as r: return json.loads(r.read())
def mcp(tool,args):
    open('_a.json','w').write(json.dumps(args))
    return subprocess.run(["python3","mcp.py",tool,"@_a.json"],capture_output=True,text=True).stdout
IMGK={"s-gbp":"google-business-profile-optimisation","s-webdev":"web-development-wolverhampton","s-ads":"google-ads-management","s-reviews":"google-review-management","s-social":"social-media-marketing-wolverhampton","s-branding":"branding-agency-wolverhampton"}
cats={c['name']:c['id'] for c in rest("GET","categories?per_page=100")}
ids={}
existing={189:"How to Rank Higher on Google Maps in 2026"}
for i,p in enumerate(D['POSTS']):
    if p['cat'] not in cats: cats[p['cat']]=rest("POST","categories",{"name":p['cat']})['id']
    if i==0: pid=189
    else: pid=json.loads(mcp("elementor-create-page",{"title":p['title'],"post_type":"post"}))['id']
    slug=p['title'].lower().replace("'","").replace("?","").replace(":","")
    slug="-".join(slug.split())
    y,m=2026,{"Sep":9,"Aug":8}[p['date'].split()[1]]; d=int(p['date'].split()[0])
    rest("POST",f"posts/{pid}",{"categories":[cats[p['cat']]],"slug":slug,"excerpt":p['ex'],"featured_media":A[IMGK[p['img']]],"date":f"{y}-{m:02d}-{d:02d}T09:00:00"})
    # body
    b=B(); e=b.el; kids=[]
    for j,(kind,val) in enumerate(p['body']):
        if kind=="p": kids.append(e("e-paragraph",f"Body P {j}",cfg={"paragraph":val},style="font-size: 17.5px; line-height: 1.8;"))
        elif kind=="h": kids.append(e("e-heading",f"Body H {j}",cfg={"tag":"h2","title":val},style="font-size: 28px; margin-top: 10px;"))
        else: kids.append(e("e-paragraph",f"Body L {j}",cfg={"paragraph":"<ul>"+"".join(f"<li>{x}</li>" for x in val)+"</ul>"},style="font-size: 17px; line-height: 1.8;",classes=["dg-policy-text"]))
    root=e("e-flexbox","Article Body",kids,style="flex-direction: column; gap: 20px; padding: 0px;")
    r=json.loads(mcp("elementor-build-composition",b.payload(pid,root)))
    ids[p['slug']]=pid; print(pid,p['cat'],r.get('success'),slug)
json.dump(ids,open('posts.json','w'))
