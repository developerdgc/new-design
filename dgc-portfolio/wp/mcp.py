"""Tiny JSON-RPC client for the Elementor MCP endpoint (used until the session loads the server natively)."""
import json, os, re, sys, urllib.request
# DGC_SITE=main -> digitalgrowthcatalyze.com, DGC_SITE=portfolio -> portfolio.digitalgrowthcatalyze.com (live portfolio), default -> staging.
SERVER = {'main': 'digital-growth-catalyze-main-elementor', 'portfolio': 'digital-growth-catalyze-elementor'}.get(os.environ.get('DGC_SITE', ''), 'portfolio-site-elementor')
_cfg = json.load(open(os.path.expanduser('~/.claude.json')))['mcpServers'][SERVER]
URL = _cfg['url']; AUTH = _cfg['headers']['Authorization']
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
    # Drafts on the live main site must stay drafts: publishing is blocked unless DGC_ALLOW_PUBLISH=1.
    if name == 'elementor-publish-document' and SERVER == 'digital-growth-catalyze-main-elementor' and os.environ.get('DGC_ALLOW_PUBLISH') != '1':
        return {'skipped': 'publish blocked on main site', 'post_id': (args or {}).get('post_id')}
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
    for i in range(0, len(ops), 8):
        r = call('elementor-manage-classes', {'operations': ops[i:i + 8]})
        out += [(x.get('label'), x.get('error')) for x in r['results'] if x['status'] != 'ok']
    return out or 'ok'
def drop_dups():
    d = [l for l in class_labels() if l and l.startswith('DUP_')]
    if d: call('elementor-manage-classes', {'operations': [{'action': 'delete', 'label': l} for l in d]})
    return d

def put_section(post_id, title, index, **kw):
    """(Re)build one root section, identified by its root configuration-id/title, at a fixed position on the page."""
    roots = call('elementor-get-page-structure', {'post_id': post_id}).get('elements', [])
    old = [e['id'] for e in roots if e.get('title') == title]
    if old: call('elementor-manage-elements', {'post_id': post_id, 'operations': [{'action': 'delete', 'element_id': i} for i in old]})
    r = call('elementor-build-composition', dict(post_id=post_id, parent_id='document', mode='append', **kw))
    call('elementor-publish-document', {'post_id': post_id})
    roots = call('elementor-get-page-structure', {'post_id': post_id}).get('elements', [])
    ids = [e['id'] for e in roots if e.get('title') == title]
    if ids and [e['id'] for e in roots].index(ids[-1]) != index:
        call('elementor-manage-elements', {'post_id': post_id, 'operations': [{'action': 'move', 'element_id': ids[-1], 'new_parent_id': 'document', 'index': index}]})
        call('elementor-publish-document', {'post_id': post_id})
    return r

def class_ids():
    g = call('elementor-read-resource', {'uri': 'elementor://global-classes'})
    c = json.loads(g['content']) if isinstance(g.get('content'), str) else g
    items = c if isinstance(c, list) else c.get('classes', c.get('items', []))
    return {x.get('label'): x.get('id') for x in items}
def prioritize(labels):
    """Move modifier classes to the top of the priority list so they beat base classes."""
    ids = class_ids()
    moves = [{'id': ids[l], 'position': 'start'} for l in reversed(labels) if l in ids]
    for i in range(0, len(moves), 20): call('elementor-reorder-classes', {'moves': moves[i:i + 20]})
