"""Bump paragraph font sizes site-wide and apply homepage/header tweaks via manage-elements."""
import json,subprocess,re,sys,time
def mcp(tool,args):
    open('_r.json','w').write(json.dumps(args))
    for _ in range(4):
        out=subprocess.run(["python3","mcp.py",tool,"@_r.json"],capture_output=True,text=True).stdout
        if out.strip().startswith('{') and '"http_error"' not in out: return json.loads(out)
        time.sleep(3)
    raise SystemExit(f"{tool} failed: {out[:300]}")
MAP={13.5:14,14:15,14.5:15.5,15:16,15.5:16.5,16:17,16.5:17.5,17:18,17.5:18,18:19}
def bump(css):
    def f(m):
        v=float(m.group(1)); n=MAP.get(v)
        return f"font-size: {n:g}px" if n else m.group(0)
    return re.sub(r"font-size:\s*([\d.]+)px",f,css)
SKIP_TITLES=("Reviews Quote Mark","Not Found Code","Popular Label")
def walk(n,out):
    for x in n:
        out.append(x); walk(x.get('elements',[]),out)
def nodes(pid):
    top=mcp("elementor-get-page-structure",{"post_id":pid})['elements']; allx=[]
    for t in top:
        sub=mcp("elementor-get-page-structure",{"post_id":pid,"element_id":t['id'],"include_content":True})['elements']
        walk(sub,allx)
    return allx
def apply(pid,ops):
    for i in range(0,len(ops),50):
        r=mcp("elementor-manage-elements",{"post_id":pid,"operations":ops[i:i+50]})
        bad=[x for x in r.get('results',[]) if x.get('status')!='ok']
        if bad: print("  errors",bad[:2])
    p=mcp("elementor-publish-document",{"post_id":pid})
    return p.get('status')

def para_ops(allx):
    ops=[]
    for x in allx:
        if x.get('widgetType')!='e-paragraph' or x.get('title','').startswith(SKIP_TITLES): continue
        css=(x.get('styles') or {}).get('css','')
        if not css: continue
        new=bump(css)
        if new!=css: ops.append({"action":"update","element_id":x['id'],"style":new,"style_apply_mode":"replace"})
    return ops

def by_title(allx,title): return [x['id'] for x in allx if x.get('title')==title]

import itertools
_c=itertools.count(1)
def anim(direction,delay=0,effect="slide"):
    return [{"interaction_id":f"dg-anim-{next(_c)}","trigger":"scrollIn","animation":{"effect":effect,"type":"in","direction":direction,
        "timing_config":{"duration":{"unit":"ms","size":700},"delay":{"unit":"ms","size":delay}},"config":{"easing":"easeOut","replay":False}}}]

if __name__=="__main__":
    ids=[int(x) for x in sys.argv[1:]]
    for pid in ids:
        allx=nodes(pid); ops=[] if pid==141 else para_ops(allx)
        if pid==39:
            T=lambda t:by_title(allx,t)
            ops+=[{"action":"update","element_id":i,"style":"padding: 140px 24px 160px 24px; @media(--tablet){ padding: 120px 24px 150px 24px; } @media(--mobile){ padding: 110px 16px 140px 16px; }"} for i in T("Hero")]
            ops+=[{"action":"update","element_id":i,"settings":{"image":{"src":{"id":276,"alt":"Digital marketing network globe"},"size":"full"}},"style":"max-width: 580px; @media(--tablet){ max-width: 420px; }"} for i in T("Hero Globe")]
            ops+=[{"action":"update","element_id":i,"style":"padding: 56px 24px 56px 24px; @media(--mobile){ padding: 44px 16px 44px 16px; }"} for i in T("Audit")]
            ops+=[{"action":"update","element_id":i,"style":"gap: 40px; grid-template-columns: 1fr 1fr;"} for i in T("Audit Grid")]
            ops+=[{"action":"update","element_id":i,"style":"padding: 26px; gap: 6px;"} for i in T("Audit Form Card")]
            ops+=[{"action":"update","element_id":i,"style":"font-size: 32px; @media(--mobile){ font-size: 26px; }"} for i in T("Audit Title")]
            ops+=[{"action":"update","element_id":i,"style":"padding: 20px 0px 0px 0px; margin-top: 6px; gap: 28px;"} for i in T("Audit Facts")]
            for t in ["Fact Services Big","Fact Hours Big","Fact Reply Big"]:
                ops+=[{"action":"update","element_id":i,"style":"font-size: 34px; @media(--mobile){ font-size: 28px; }"} for i in T(t)]
            ops+=[{"action":"update","element_id":i,"style":"min-height: 84px;"} for i in T("Audit Form About Your Business Field")]
            ops+=[{"action":"update","element_id":i,"style":"font-size: 22px;"} for i in T("Audit Form Heading")]
            # entrance animations (selected sections only)
            for t,a in [("About Media",anim("left")),("About Copy",anim("right",150)),("Audit Copy",anim("left")),("Audit Form Card",anim("right",150)),
                        ("Why Copy",anim("left")),("Why Media",anim("right",150)),("Final CTA Banner",anim("bottom",0,"fade"))]:
                ops+=[{"action":"update","element_id":i,"interactions":a} for i in T(t)]
            for k,t in enumerate(["SEO and Digital Marketing Card","GBP Optimization Card","Web Development Card","Social Media Marketing Card","Google Ads Card","Branding Card"]):
                ops+=[{"action":"update","element_id":i,"interactions":anim("bottom",(k%3)*120)} for i in T(t)]
        if pid==141:
            ops+=[{"action":"update","element_id":i,"style":"padding: 14px 12px 14px 24px; @media(--mobile){ padding: 10px 8px 10px 12px; }"} for i in by_title(allx,"Header Bar")]
        st=apply(pid,ops) if ops else 'no-ops'
        print(pid,len(ops),st,flush=True)
