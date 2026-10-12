import json, sys, urllib.request, os
URL="https://redshieldwater.emmenntech.com/wp-json/elementor/mcp/"
AUTH=os.environ["RS_MCP_AUTH"]  # "Basic <base64 user:app-password>", never commit it
SF=os.path.join(os.path.dirname(os.path.abspath(__file__)),"rsw","session")
def post(body, sid=None):
    h={"Authorization":AUTH,"Content-Type":"application/json","Accept":"application/json, text/event-stream"}
    if sid: h["Mcp-Session-Id"]=sid
    r=urllib.request.Request(URL,data=json.dumps(body).encode(),headers=h,method="POST")
    try:
        with urllib.request.urlopen(r,timeout=120) as resp:
            raw=resp.read().decode(); sid2=resp.headers.get("Mcp-Session-Id")
    except urllib.error.HTTPError as e:
        raw=e.read().decode(); sid2=None
    if raw.startswith("event:") or "\ndata:" in raw or raw.startswith("data:"):
        raw="\n".join(l[5:].strip() for l in raw.splitlines() if l.startswith("data:"))
    return (json.loads(raw) if raw.strip() else None), sid2
def session():
    if os.path.exists(SF): return open(SF).read().strip()
    res,sid=post({"jsonrpc":"2.0","id":0,"method":"initialize","params":{"protocolVersion":"2025-06-18","capabilities":{},"clientInfo":{"name":"claude-test","version":"1"}}})
    post({"jsonrpc":"2.0","method":"notifications/initialized"},sid)
    open(SF,"w").write(sid); return sid
if __name__=="__main__":
    method=sys.argv[1]; params=json.loads(sys.argv[2]) if len(sys.argv)>2 else {}
    sid=session(); res,_=post({"jsonrpc":"2.0","id":1,"method":method,"params":params},sid)
    if res and "error" in res and "session" in json.dumps(res["error"]).lower():
        os.remove(SF); sid=session(); res,_=post({"jsonrpc":"2.0","id":1,"method":method,"params":params},sid)
    print(json.dumps(res,indent=1))
