"""Portfolio homepage Work section split over small private holder pages so each opens in the Elementor editor.
582 keeps the section skeleton + case cards; new holders carry website cards (20 per page) and logo cards.
The homepage embeds them in order; the interactions script moves the extra cards into the main grid."""
import os, json, urllib.request
os.environ.setdefault('DGC_SITE', 'portfolio')
import mcp
from build_work import Frag, web_card, brand_item, append, BRANDS
from dgc_site import SITE
MAIN = 582; B = SITE + '/wp-json/wp/v2/'
def req(p, data=None, method='GET'):
    r = urllib.request.Request(B + p, json.dumps(data).encode() if data is not None else None, {'Authorization': mcp.AUTH, 'Content-Type': 'application/json', 'User-Agent': 'Mozilla/5.0'}, method=method)
    return json.load(urllib.request.urlopen(r, timeout=120))
items = sorted(json.load(open('/tmp/claude-0/items.json')), key=lambda it: not it['url'])
parts = [('Homepage Work: Websites 1-20', 'web', list(enumerate(items[0:20], 1))),
         ('Homepage Work: Websites 21-40', 'web', list(enumerate(items[20:40], 21))),
         ('Homepage Work: Websites 41-55', 'web', list(enumerate(items[40:], 41))),
         ('Homepage Work: Logos', 'brand', list(enumerate(BRANDS, 1)))]
STATE = 'work-holders-portfolio.json'
st = json.load(open(STATE)) if os.path.exists(STATE) else {}
print(mcp.upsert_classes({'dgc-work-extra': 'display: flex; flex-direction: column; gap: 24px;'}))
for title, kind, rows in parts:
    if title in st: print('exists', title, st[title]); continue
    pid = mcp.call('elementor-create-page', {'title': title, 'post_type': 'page'})['id']
    r = mcp.call('elementor-build-composition', {'post_id': pid, 'parent_id': 'document', 'mode': 'append', 'xml_structure': '<e-div-block configuration-id="Work Extra"></e-div-block>', 'classes': {'Work Extra': ['dgc-work-extra']}})
    holder = r['root_element_ids'][0]
    step = 5 if kind == 'web' else 2
    for s in range(0, len(rows), step):
        f = Frag()
        for i, it in rows[s:s + step]: (web_card if kind == 'web' else brand_item)(f, i, it)
        append(pid, holder, f)
    req(f'pages/{pid}', {'status': 'private'}, 'POST')
    st[title] = pid; json.dump(st, open(STATE, 'w'), indent=1); print('built', title, pid)
# remove the moved cards from the main holder
tree = mcp.call('elementor-get-page-structure', {'post_id': MAIN})['elements']
def find(es, t):
    for e in es:
        if e.get('title') == t: return e
        x = find(e.get('elements', []), t)
        if x: return x
grid = find(tree, 'Work Grid')
gone = [c['id'] for c in grid['elements'] if c['title'].split(' ')[0] in ('Web', 'Brand')]
for s in range(0, len(gone), 40): mcp.call('elementor-manage-elements', {'post_id': MAIN, 'operations': [{'action': 'delete', 'element_id': i} for i in gone[s:s + 40]]})
mcp.call('elementor-publish-document', {'post_id': MAIN}); req(f'pages/{MAIN}', {'status': 'private'}, 'POST')
print('removed from main', len(gone))
# homepage: embed main + extras in order
codes = ''.join(f'[elementor-template id="{i}"]' for i in [MAIN] + [st[t] for t, _, _ in parts])
code_el = find(mcp.call('elementor-get-page-structure', {'post_id': 126})['elements'], 'Work Embed Code')
print(mcp.call('elementor-manage-elements', {'post_id': 126, 'operations': [{'action': 'update', 'element_id': code_el['id'], 'settings': {'paragraph': codes}}]}).get('status'))
mcp.call('elementor-publish-document', {'post_id': 126}); print(codes)
def count(e): return 1 + sum(count(c) for c in e.get('elements', []))
for pid in [126, MAIN] + [st[t] for t, _, _ in parts]: print(pid, sum(count(e) for e in mcp.call('elementor-get-page-structure', {'post_id': pid})['elements']))
