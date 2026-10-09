"""Upload 800px-wide website screenshots and record the unscaled file URL as hd_url in media-map.json."""
import json, os, urllib.request, concurrent.futures as cf
import mcp
H = '/tmp/claude-0/-home-user-new-design/c0b0073b-578a-5cca-805d-2082208a4256/scratchpad/hires/'
B = 'https://newportfolio.digitalgrowthcatalyze.com/wp-json/wp/v2/media'
MM = json.load(open('media-map.json'))
def up(k):
    data = open(H + f'hd-{k}.webp', 'rb').read()
    req = urllib.request.Request(B, data, {'Authorization': mcp.AUTH, 'Content-Type': 'image/webp', 'Content-Disposition': f'attachment; filename="work-hd-{k}.webp"'})
    d = json.loads(urllib.request.urlopen(req, timeout=300).read()); md = d.get('media_details', {})
    url = d['source_url']
    if md.get('original_image'): url = url.rsplit('/', 1)[0] + '/' + md['original_image']
    return k, d['id'], url
todo = [f[3:-5] for f in os.listdir(H) if f.startswith('hd-') and 'hd_url' not in MM.get(f'img/work/{f[3:-5]}.jpg', {})]
with cf.ThreadPoolExecutor(4) as ex:
    for k, i, url in ex.map(up, todo):
        MM[f'img/work/{k}.jpg'].update(hd_id=i, hd_url=url); print(k, i, url.rsplit('/', 1)[1])
json.dump(MM, open('media-map.json', 'w'), indent=1)
