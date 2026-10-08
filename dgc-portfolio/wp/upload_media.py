"""Convert referenced images to WebP and upload everything to the WordPress Media Library (resumable)."""
import json, os, io, urllib.request, concurrent.futures as cf
from PIL import Image
Image.MAX_IMAGE_PIXELS = None
import mcp
ROOT = '/home/user/new-design/dgc-portfolio/'
B = 'https://newportfolio.digitalgrowthcatalyze.com/wp-json/wp/v2/media'
MAP = 'media-map.json'
done = json.load(open(MAP)) if os.path.exists(MAP) else {}
refs = json.load(open('refs.json'))
def slug(r): return r.replace('img/', '').replace('/', '-').rsplit('.', 1)[0]
def prep(r):
    p = ROOT + r
    if r.endswith('.mp4'): return open(p, 'rb').read(), slug(r) + '.mp4', 'video/mp4'
    im = Image.open(p); b = io.BytesIO()
    alpha = im.mode in ('RGBA', 'LA', 'P')
    im = im.convert('RGBA' if alpha else 'RGB')
    im.save(b, 'WEBP', quality=88 if alpha else 82, method=6)
    return b.getvalue(), slug(r) + '.webp', 'image/webp'
def up(r):
    data, name, ct = prep(r)
    req = urllib.request.Request(B, data, {'Authorization': mcp.AUTH, 'Content-Type': ct, 'Content-Disposition': f'attachment; filename="{name}"'})
    with urllib.request.urlopen(req, timeout=300) as x: d = json.loads(x.read())
    return r, {'id': d['id'], 'url': d['source_url'], 'w': d.get('media_details', {}).get('width'), 'h': d.get('media_details', {}).get('height'), 'bytes': len(data)}
todo = [r for r in refs if r not in done]
with cf.ThreadPoolExecutor(4) as ex:
    for fut in cf.as_completed([ex.submit(up, r) for r in todo]):
        try:
            r, info = fut.result(); done[r] = info; json.dump(done, open(MAP, 'w'), indent=1)
        except Exception as e: print('FAIL', e)
print('uploaded', len(done), '/', len(refs), 'total MB', round(sum(v['bytes'] for v in done.values()) / 1e6, 1))
