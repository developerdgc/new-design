"""digitalgrowthcatalyze.com menus: replace 'Customer Success' with a 'Company' parent whose dropdown holds
Case Studies + Video Reviews (Main Menu id 6 and Mobile Menu id 14). Saves a backup of the original items first."""
import os, json, urllib.request
os.environ['DGC_SITE'] = 'main'
import mcp
B = 'https://digitalgrowthcatalyze.com/wp-json/wp/v2/'
def req(path, data=None, method='GET'):
    r = urllib.request.Request(B + path, json.dumps(data).encode() if data is not None else None, {'Authorization': mcp.AUTH, 'Content-Type': 'application/json', 'User-Agent': 'Mozilla/5.0'}, method=method)
    return json.load(urllib.request.urlopen(r, timeout=120))
items = req('menu-items?per_page=100&context=edit')
if not os.path.exists('menu-backup-main.json'): json.dump(items, open('menu-backup-main.json', 'w'), indent=1)
P = json.load(open('pages-main.json'))
for menu in (6, 14):
    mine = sorted([i for i in items if i['menus'] == menu], key=lambda i: i['menu_order'])
    old = next((i for i in mine if i['object'] == 'page' and i['object_id'] == 2184), None)
    if any((i['title']['raw'] if isinstance(i['title'], dict) else i['title']) == 'Company' and i['parent'] == 0 for i in mine):
        print(menu, 'already done'); continue
    assert old, menu
    pos = old['menu_order']
    # make room for the two children right after the Company item
    for i in mine:
        if i['menu_order'] > pos: req(f"menu-items/{i['id']}", {'menu_order': i['menu_order'] + 2}, 'POST')
    company = req(f"menu-items/{old['id']}", {'title': 'Company', 'type': 'custom', 'url': '#', 'object': 'custom', 'object_id': 0, 'menu_order': pos}, 'POST')
    for n, (key, title) in enumerate((('case-studies', 'Case Studies'), ('video-reviews', 'Video Reviews')), 1):
        c = req('menu-items', {'title': title, 'type': 'post_type', 'object': 'page', 'object_id': P[key]['id'], 'parent': company['id'], 'menus': menu, 'menu_order': pos + n, 'status': 'publish'}, 'POST')
        print(menu, 'child', c['id'], title)
    print(menu, 'company', company['id'], company['url'])
for i in sorted([i for i in req('menu-items?per_page=100&context=edit') if i['menus'] == 6], key=lambda i: i['menu_order']):
    print('  ', i['menu_order'], ('  ' if i['parent'] else '') + (i['title']['raw'] if isinstance(i['title'], dict) else i['title']), i['url'])
