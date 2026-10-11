import json, sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import mcpc
def call(name, args):
    sid = mcpc.session()
    res, _ = mcpc.post({"jsonrpc":"2.0","id":1,"method":"tools/call","params":{"name":name,"arguments":args}}, sid)
    if res and "error" in res and "session" in json.dumps(res["error"]).lower():
        os.remove(mcpc.SF); sid = mcpc.session()
        res, _ = mcpc.post({"jsonrpc":"2.0","id":1,"method":"tools/call","params":{"name":name,"arguments":args}}, sid)
    if not res or "result" not in res: return {"_error": res}
    r = res["result"]; t = r["content"][0]["text"] if r.get("content") else ""
    try: out = json.loads(t)
    except Exception: out = {"_text": t}
    if r.get("isError"): out = {"_isError": True, **(out if isinstance(out, dict) else {"_v": out})}
    return out
if __name__ == "__main__":
    req = json.load(open(sys.argv[1]))
    print(json.dumps(call(req["name"], req["arguments"]), indent=1))
