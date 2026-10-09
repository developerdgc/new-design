"""Upload what the Case Studies + Video Reviews pages need to digitalgrowthcatalyze.com (resumable, WebP for images)."""
import os, io, json, sys, urllib.request, concurrent.futures as cf
os.environ.setdefault('DGC_SITE', 'main')
sys.path.insert(0, '..')
from PIL import Image
import mcp
from dgc_site import MEDIA, SITE
from common import CASES
ROOT = '/home/user/new-design/dgc-portfolio/'
B = SITE + '/wp-json/wp/v2/media'
done = json.load(open(MEDIA)) if os.path.exists(MEDIA) else {}
refs = [f'img/casestudies/{c[3]}.jpg' for c in CASES] + ['img/brand/dgc-mark-white.png', 'img/brand/dgc-logo-white.png'] \
     + [f'video/review-{i}.{e}' for i in range(1, 7) for e in ('jpg', 'mp4')]
def prep(r):
    p = ROOT + r; slug = 'dgc-' + r.replace('img/', '').replace('/', '-').rsplit('.', 1)[0]
    if r.endswith('.mp4'): return open(p, 'rb').read(), slug + '.mp4', 'video/mp4'
    im = Image.open(p); alpha = im.mode in ('RGBA', 'LA', 'P'); im = im.convert('RGBA' if alpha else 'RGB'); b = io.BytesIO()
    im.save(b, 'WEBP', quality=88 if alpha else 82, method=6); return b.getvalue(), slug + '.webp', 'image/webp'
def up(r):
    data, name, ct = prep(r)
    req = urllib.request.Request(B, data, {'Authorization': mcp.AUTH, 'Content-Type': ct, 'Content-Disposition': f'attachment; filename="{name}"', 'User-Agent': 'Mozilla/5.0'})
    with urllib.request.urlopen(req, timeout=300) as x: d = json.loads(x.read())
    md = d.get('media_details', {}) or {}
    return r, {'id': d['id'], 'url': d['source_url'], 'w': md.get('width'), 'h': md.get('height'), 'bytes': len(data)}
todo = [r for r in refs if r not in done]
with cf.ThreadPoolExecutor(3) as ex:
    for fut in cf.as_completed([ex.submit(up, r) for r in todo]):
        try: r, info = fut.result(); done[r] = info; json.dump(done, open(MEDIA, 'w'), indent=1); print('ok', r, info['id'])
        except Exception as e: print('FAIL', getattr(e, 'code', ''), str(e)[:150])
print('uploaded', len([r for r in refs if r in done]), '/', len(refs))
