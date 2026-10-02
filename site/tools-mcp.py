#!/usr/bin/env python3
"""Minimal Elementor MCP client: mcp.py <tool> [json-args | @file.json]"""
import json, sys, os, base64, urllib.request, ssl
U="https://digiranxpro.com/wp-json/elementor/mcp/"
AUTH="Basic "+os.environ["DIGIRANX_MCP_AUTH"]
SF=os.path.join(os.path.dirname(__file__),".sid")
ctx=ssl.create_default_context(cafile=os.environ.get("SSL_CERT_FILE","/root/.ccr/ca-bundle.crt"))
def post(body,sid=None):
    h={"Authorization":AUTH,"Content-Type":"application/json","Accept":"application/json, text/event-stream","MCP-Protocol-Version":"2025-06-18"}
    if sid: h["mcp-session-id"]=sid
    req=urllib.request.Request(U,data=json.dumps(body).encode(),headers=h,method="POST")
    with urllib.request.urlopen(req,context=ctx,timeout=180) as r:
        return r.headers.get("mcp-session-id"), r.read().decode()
def session():
    if os.path.exists(SF): return open(SF).read().strip()
    sid,_=post({"jsonrpc":"2.0","id":1,"method":"initialize","params":{"protocolVersion":"2025-06-18","capabilities":{},"clientInfo":{"name":"cli","version":"1"}}})
    post({"jsonrpc":"2.0","method":"notifications/initialized"},sid)
    open(SF,"w").write(sid); return sid
def call(method,params,retry=True):
    sid=session()
    try: _,t=post({"jsonrpc":"2.0","id":2,"method":method,"params":params},sid)
    except urllib.error.HTTPError as e:
        body=e.read().decode()
        if retry and e.code in (400,404): os.remove(SF); return call(method,params,False)
        return json.dumps({"http_error":e.code,"body":body[:3000]})
    return t
if __name__=="__main__":
    tool=sys.argv[1]
    if tool=="tools/list": print(call("tools/list",{})); sys.exit()
    if tool=="resource": print(call("resources/read",{"uri":sys.argv[2]})); sys.exit()
    a=sys.argv[2] if len(sys.argv)>2 else "{}"
    args=json.load(open(a[1:])) if a.startswith("@") else json.loads(a)
    out=call("tools/call",{"name":tool,"arguments":args})
    try:
        j=json.loads(out)
        if "result" in j:
            for c in j["result"].get("content",[]): print(c.get("text",""))
            if j["result"].get("isError"): print("[isError]")
        else: print(out)
    except Exception: print(out)
