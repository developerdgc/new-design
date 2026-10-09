"""Rebuild only the Video Library section of the Video Reviews page: 6 videos, no captions or note under them.
Run with DGC_SITE=main for digitalgrowthcatalyze.com, without it for the portfolio staging site."""
import json
import mcp
from build_work import link
from dgc_site import MEDIA, PAGES
MM = json.load(open(MEDIA))
PAGE = json.load(open(PAGES))['video-reviews']['id']
VIDEOS = ['review-1', 'review-2', 'review-3', 'review-4', 'review-5', 'review-6']
# rows of 4 (3 on tablet, 2 on phones); an unfinished last row is centred
print('classes', mcp.upsert_classes({
 'dgc-vgrid': 'display: flex; flex-wrap: wrap; justify-content: center; align-items: flex-start; gap: 24px; @media(--tablet) { gap: 20px; } @media(--mobile) { gap: 14px; }',
 'dgc-vg-item': 'flex: none; width: calc(25% - 18px); @media(--tablet) { width: calc(33.333% - 14px); } @media(--mobile) { width: calc(50% - 7px); }',
}))
cards, cfg, cls, sty = '', {}, {}, {}
for i, k in enumerate(VIDEOS, 1):
    p = f'Video {i}'
    cards += (f'<e-div-block configuration-id="{p}"><e-flexbox configuration-id="{p} Button"><e-image configuration-id="{p} Poster"></e-image>'
              f'<e-flexbox configuration-id="{p} Play"><e-div-block configuration-id="{p} Play Icon"></e-div-block></e-flexbox></e-flexbox></e-div-block>')
    cfg[f'{p} Button'] = {'tag': 'a', 'link': link(MM[f'video/{k}.mp4']['url'])}
    cfg[f'{p} Poster'] = {'image': {'src': {'id': MM[f'video/{k}.jpg']['id']}, 'size': 'full'}}
    cls[p] = ['dgc-vthumb', 'dgc-vg-item']; cls[f'{p} Button'] = ['dgc-vbtn', 'dgc-vbtn-light']; cls[f'{p} Poster'] = ['dgc-vimg']
    cls[f'{p} Play'] = ['dgc-play']; cls[f'{p} Play Icon'] = ['ico-play']; sty[f'{p} Play Icon'] = 'margin-left: 3px;'
X = f'<e-flexbox configuration-id="Video Library"><e-div-block configuration-id="Video Library Wrap"><e-grid configuration-id="Video Grid">{cards}</e-grid></e-div-block></e-flexbox>'
cfg['Video Library'] = {'tag': 'section'}
cls.update({'Video Library': ['dgc-pbody'], 'Video Library Wrap': ['dgc-wrap'], 'Video Grid': ['dgc-vgrid']})
r = mcp.put_section(PAGE, 'Video Library', 1, xml_structure=X, element_config=cfg, classes=cls, style=sty)
print('videos', r.get('success'), r.get('warnings'), [e.get('title') for e in mcp.call('elementor-get-page-structure', {'post_id': PAGE})['elements']])
