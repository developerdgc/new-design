"""Tiny JSON-RPC client for the Elementor MCP endpoint (used until the session loads the server natively)."""
import json, os, re, sys, urllib.request
URL = 'https://newportfolio.digitalgrowthcatalyze.com/wp-json/elementor/mcp/'
AUTH = json.load(open(os.path.expanduser('~/.claude.json')))['mcpServers']['portfolio-site-elementor']['headers']['Authorization']
_sid = None; _id = 0
def _post(payload):
    global _sid
    h = {'Authorization': AUTH, 'Content-Type': 'application/json', 'Accept': 'application/json, text/event-stream'}
    if _sid: h['Mcp-Session-Id'] = _sid
    req = urllib.request.Request(URL, json.dumps(payload).encode(), h)
    with urllib.request.urlopen(req, timeout=120) as r:
        _sid = r.headers.get('Mcp-Session-Id') or _sid
        body = r.read().decode()
    m = re.search(r'\{.*\}', body, re.S)
    return json.loads(m.group(0)) if m else {}
def init():
    global _id; _id += 1
    return _post({'jsonrpc': '2.0', 'id': _id, 'method': 'initialize', 'params': {'protocolVersion': '2025-03-26', 'capabilities': {}, 'clientInfo': {'name': 'claude', 'version': '1'}}})
def call(name, args=None):
    global _id
    if not _sid: init()
    _id += 1
    d = _post({'jsonrpc': '2.0', 'id': _id, 'method': 'tools/call', 'params': {'name': name, 'arguments': args or {}}})
    if 'error' in d: raise RuntimeError(d['error'])
    res = d['result']; out = []
    for c in res.get('content', []):
        t = c.get('text', '')
        try: out.append(json.loads(t))
        except Exception: out.append(t)
    if res.get('isError'): raise RuntimeError(out)
    return out[0] if len(out) == 1 else out
def tools():
    global _id
    if not _sid: init()
    _id += 1
    return _post({'jsonrpc': '2.0', 'id': _id, 'method': 'tools/list'})['result']['tools']
if __name__ == '__main__':
    print(json.dumps(call(sys.argv[1], json.loads(sys.argv[2]) if len(sys.argv) > 2 else {}), indent=1)[:int(os.environ.get('N', 4000))])
