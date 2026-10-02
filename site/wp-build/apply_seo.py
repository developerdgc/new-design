"""Apply seo.json to Rank Math via its REST API (needs DIGIRANX_MCP_AUTH)."""
import json,os,urllib.request
AUTH="Basic "+os.environ["DIGIRANX_MCP_AUTH"]
for pid,v in json.load(open(os.path.join(os.path.dirname(__file__),'seo.json'))).items():
    body={"objectID":int(pid),"objectType":"post","meta":{"rank_math_title":v['title'],"rank_math_description":v['description'],"rank_math_focus_keyword":v['focus']}}
    r=urllib.request.Request("https://digiranxpro.com/wp-json/rankmath/v1/updateMeta",data=json.dumps(body).encode(),headers={"Authorization":AUTH,"Content-Type":"application/json"},method="POST")
    with urllib.request.urlopen(r) as x: print(pid,x.status)
