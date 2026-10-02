import json,subprocess,time,sys
from gen import PAGES,SERVICE_NAMES
def mcp(tool,args):
    for t in range(4):
        out=subprocess.run(["python3","mcp.py",tool,args if args.startswith('@') else args],capture_output=True,text=True).stdout
        if '"http_error"' not in out and out.strip(): return out
        time.sleep(3)
    return out
slugs=sys.argv[1:] or list(SERVICE_NAMES)
for s in slugs:
    pid=PAGES[s]
    if s!="seo-digital-marketing":
        subprocess.run(["python3","b_service.py",s],capture_output=True)
        r=mcp("elementor-build-composition","@p_svc_"+s+".json")
        ok=json.loads(r).get('success') if r.strip().startswith('{') else r[:200]
    else: ok='skip-build'
    st=mcp("elementor-update-page-settings",json.dumps({"post_id":pid,"settings":{"template":"elementor_header_footer","hide_title":"yes"}}))
    pub=mcp("elementor-publish-document",json.dumps({"post_id":pid}))
    print(s,pid,ok,'settings' ,'"success":true' in st,'publish',json.loads(pub).get('status') if pub.strip().startswith('{') else pub[:100],flush=True)
