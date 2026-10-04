"""python3 run.py header footer popup home ... : build payloads, push, (optionally) publish."""
import json, subprocess, sys, time
PAGES = json.load(open('pages.json'))
def mcp(tool, arg):
    for t in range(4):
        out = subprocess.run(["python3", "mcp.py", tool, arg], capture_output=True, text=True).stdout
        if out.strip() and '"http_error"' not in out: return out
        time.sleep(4)
    return out
publish = '--publish' in sys.argv
for name in [a for a in sys.argv[1:] if not a.startswith('--')]:
    r = subprocess.run(["python3", f"b_{name}.py"], capture_output=True, text=True)
    if r.returncode: print(name, 'BUILD ERROR', r.stderr[-800:]); continue
    out = mcp("elementor-build-composition", f"@/tmp/p_{name}.json")
    try: j = json.loads(out); ok = j.get('success'); err = j if not ok else ''
    except Exception: ok = False; err = out[:800]
    print(name, PAGES[name], 'ok' if ok else ('FAIL ' + str(err)[:900]), flush=True)
    if ok and publish:
        print('  publish', mcp("elementor-publish-document", json.dumps({"post_id": PAGES[name]}))[:90], flush=True)
