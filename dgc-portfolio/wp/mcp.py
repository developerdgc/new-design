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

def class_labels():
    g = call('elementor-read-resource', {'uri': 'elementor://global-classes'})
    c = json.loads(g['content']) if isinstance(g.get('content'), str) else g
    items = c if isinstance(c, list) else c.get('classes', c.get('items', []))
    return [x.get('label') for x in items]
def upsert_classes(C):
    """Create new global classes and replace the CSS of ones that already exist (never makes DUP_ copies)."""
    have = set(class_labels()); ops = []
    for k, v in C.items():
        ops.append({'action': 'update', 'label': k, 'css': v, 'mode': 'replace'} if k in have else {'action': 'create', 'label': k, 'css': v})
    out = []
    for i in range(0, len(ops), 50):
        r = call('elementor-manage-classes', {'operations': ops[i:i + 50]})
        out += [(x.get('label'), x.get('error')) for x in r['results'] if x['status'] != 'ok']
    return out or 'ok'
def drop_dups():
    d = [l for l in class_labels() if l and l.startswith('DUP_')]
    if d: call('elementor-manage-classes', {'operations': [{'action': 'delete', 'label': l} for l in d]})
    return d
