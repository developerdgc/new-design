"""Crop/resize every image instance in the tree, tag nodes with an image key, and pack the tree into a PNG."""
import json, sys, hashlib, os
from urllib.parse import urlparse, unquote
from PIL import Image
sys.path.insert(0, os.path.dirname(__file__)); from datapng import encode
ROOT = '/home/user/new-design/dgc-portfolio'
name = sys.argv[1]; D = os.path.dirname(__file__)
t = json.load(open(f'{D}/tree-{name}.json'))
os.makedirs(f'{D}/img', exist_ok=True)
keys = {}
def pos(v, free):
    if v is None: return 0.5
    v = v.strip()
    if v.endswith('%'): return float(v[:-1]) / 100
    if v in ('left', 'top'): return 0
    if v in ('right', 'bottom'): return 1
    if v == 'center': return .5
    try: return min(1, max(0, float(v.replace('px', '')) / free)) if free else .5
    except: return .5
def prep(src, w, h, fit, opos):
    path = os.path.join(D, 'shots', src[5:] + '.png') if src.startswith('shot:') else ROOT + unquote(urlparse(src).path)
    im = Image.open(path); iw, ih = im.size
    px, py = (opos or '50% 50%').split()[:2] if opos and len(opos.split()) > 1 else ('50%', '50%')
    if fit == 'FILL' and w > 0 and h > 0:
        ar = w / h
        if iw / ih > ar: cw, ch = round(ih * ar), ih
        else: cw, ch = iw, round(iw / ar)
        x = round((iw - cw) * pos(px, iw - cw)); y = round((ih - ch) * pos(py, ih - ch))
        im = im.crop((x, y, x + cw, y + ch))
    tw = min(im.width, round(w * 2))
    if tw < im.width: im = im.resize((tw, max(1, round(im.height * tw / im.width))), Image.LANCZOS)
    alpha = im.mode in ('RGBA', 'LA', 'P')
    k = hashlib.md5(f'{src}|{im.size}|{x if fit=="FILL" else 0}|{y if fit=="FILL" else 0}'.encode()).hexdigest()[:10] if fit == 'FILL' else hashlib.md5(f'{src}|{im.size}'.encode()).hexdigest()[:10]
    if k not in keys:
        f = f'{D}/img/{k}.' + ('png' if alpha else 'jpg')
        (im.convert('RGBA').save(f, optimize=True) if alpha else im.convert('RGB').save(f, quality=86, optimize=True))
        keys[k] = f
    return k
def walk(n):
    if n['t'] == 'I': n['k'] = prep(n['src'], n['w'], n['h'], n['fit'], n.get('pos')); n.pop('src'); n.pop('pos', None)
    for f in n.get('fl', []):
        if f['k'] == 'U': f['key'] = prep(f['src'], n['w'], n['h'], 'FILL', None); f.pop('src')
    for c in n.get('ch', []): walk(c)
for s in t['sections']: walk(s)
json.dump(keys, open(f'{D}/imgkeys-{name}.json', 'w'))
data = json.dumps(t, separators=(',', ':'), ensure_ascii=True).encode()
print('images', len(keys), 'json', len(data), 'png', encode(data, f'{D}/data-{name}.png'))
