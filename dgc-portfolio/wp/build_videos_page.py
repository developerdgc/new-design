import sys, json
sys.path.insert(0, '/tmp/claude-0/-home-user-new-design/c0b0073b-578a-5cca-805d-2082208a4256/scratchpad')
import mcp
from build_work import MID, link, SITE
MM = json.load(open('media-map.json'))
PAGE = json.load(open('pages.json'))['video-reviews']['id']
VIDEOS = [('review-1', 'Clark Exteriors', 'Roofing contractor'), ('review-2', 'Huskins Services LLC', 'Cleaning & remodeling'), ('review-3', 'Dawn', 'Client video review'), ('review-4', 'Chase, Clean Cut', 'Client video review')]
C = {
 'dgc-vgrid': 'display: grid; grid-template-columns: repeat(4, 1fr); grid-template-rows: auto; gap: 24px; @media(--tablet) { grid-template-columns: repeat(3, 1fr); } @media(--mobile) { grid-template-columns: repeat(2, 1fr); gap: 14px; }',
 'dgc-vg-item': 'width: auto;',
 'dgc-vbtn-light': 'border: 2px solid #f6a440; box-shadow: 0 18px 34px -18px rgba(6,40,54,0.6);',
 'dgc-vname-dark': 'color: #071c25;',
 'dgc-vsub-dark': 'color: #b9650c;',
 'dgc-vnote': 'display: block; margin-top: 36px; text-align: center; font-family: Manrope; font-size: 0.92rem; color: #181818;',
}
print('classes', mcp.upsert_classes(C))
mcp.prioritize(['dgc-vg-item', 'dgc-vbtn-light', 'dgc-vname-dark', 'dgc-vsub-dark'])
# 1) page hero (same classes as the Case Studies hero)
XH = '''<e-flexbox configuration-id="Page Hero"><e-image configuration-id="Page Hero Mark"></e-image><e-div-block configuration-id="Page Hero Wrap">
 <e-paragraph configuration-id="Page Hero Kicker"></e-paragraph><e-heading configuration-id="Page Hero Title"></e-heading><e-paragraph configuration-id="Page Hero Text"></e-paragraph>
 <e-flexbox configuration-id="Page Hero Buttons"><e-flexbox configuration-id="Watch Button"><e-paragraph configuration-id="Watch Button Text"></e-paragraph><e-div-block configuration-id="Watch Button Icon"></e-div-block></e-flexbox><e-flexbox configuration-id="Cases Button"><e-paragraph configuration-id="Cases Button Text"></e-paragraph></e-flexbox></e-flexbox>
</e-div-block></e-flexbox>'''
cfg = {'Page Hero': {'tag': 'section'}, 'Page Hero Mark': {'image': {'src': {'id': MID['img/brand/dgc-mark-white.png']}, 'size': 'full'}},
       'Page Hero Kicker': {'paragraph': 'Video reviews', 'tag': 'span'}, 'Page Hero Title': {'tag': 'h1', 'title': 'Hear it from our <span>clients.</span>'},
       'Page Hero Text': {'paragraph': 'Real business owners, on camera, talking about working with Digital Growth Catalyze. Click any video to watch it with sound.'},
       'Watch Button': {'tag': 'a', 'link': link('#videos')}, 'Watch Button Text': {'paragraph': 'Watch the reviews', 'tag': 'span'},
       'Cases Button': {'tag': 'a', 'link': link(SITE + '/case-studies/')}, 'Cases Button Text': {'paragraph': 'Read case studies', 'tag': 'span'}}
cls = {'Page Hero': ['dgc-phero'], 'Page Hero Mark': ['dgc-phero-mark'], 'Page Hero Wrap': ['dgc-wrap'], 'Page Hero Kicker': ['dgc-kicker', 'dgc-kicker-dark'],
       'Page Hero Title': ['dgc-phero-h1', 'dgc-h2-orange'], 'Page Hero Text': ['dgc-phero-p'], 'Page Hero Buttons': ['dgc-phero-btns'],
       'Watch Button': ['dgc-btn', 'dgc-btn-orange'], 'Watch Button Icon': ['ico-arrow-ur'], 'Cases Button': ['dgc-btn', 'dgc-btn-ghost']}
r = mcp.put_section(PAGE, 'Page Hero', 0, xml_structure=XH, element_config=cfg, classes=cls); print('hero', r.get('success'), r.get('warnings'))
# 2) video grid
cards, cfg, cls, sty = '', {}, {}, {}
for i, (k, name, sub) in enumerate(VIDEOS, 1):
    p = f'Video {i}'
    cards += (f'<e-div-block configuration-id="{p}"><e-flexbox configuration-id="{p} Button"><e-image configuration-id="{p} Poster"></e-image>'
              f'<e-flexbox configuration-id="{p} Play"><e-div-block configuration-id="{p} Play Icon"></e-div-block></e-flexbox></e-flexbox>'
              f'<e-div-block configuration-id="{p} Caption"><e-paragraph configuration-id="{p} Name"></e-paragraph><e-paragraph configuration-id="{p} Sub"></e-paragraph></e-div-block></e-div-block>')
    cfg[f'{p} Button'] = {'tag': 'a', 'link': link(MM[f'video/{k}.mp4']['url'])}
    cfg[f'{p} Poster'] = {'image': {'src': {'id': MM[f'video/{k}.jpg']['id']}, 'size': 'full'}}
    cfg[f'{p} Name'] = {'paragraph': name, 'tag': 'span'}; cfg[f'{p} Sub'] = {'paragraph': sub, 'tag': 'span'}
    cls[p] = ['dgc-vthumb', 'dgc-vg-item']; cls[f'{p} Button'] = ['dgc-vbtn', 'dgc-vbtn-light']; cls[f'{p} Poster'] = ['dgc-vimg']; cls[f'{p} Play'] = ['dgc-play']
    cls[f'{p} Play Icon'] = ['ico-play']; cls[f'{p} Caption'] = ['dgc-vcap']; cls[f'{p} Name'] = ['dgc-vname', 'dgc-vname-dark']; cls[f'{p} Sub'] = ['dgc-vsub', 'dgc-vsub-dark']
    sty[f'{p} Play Icon'] = 'margin-left: 3px;'
X = f'''<e-flexbox configuration-id="Video Library"><e-div-block configuration-id="Video Library Wrap"><e-grid configuration-id="Video Grid">{cards}</e-grid><e-paragraph configuration-id="Video Note"></e-paragraph></e-div-block></e-flexbox>'''
cfg.update({'Video Library': {'tag': 'section'}, 'Video Note': {'paragraph': 'More video reviews are on the way.'}})
cls.update({'Video Library': ['dgc-pbody'], 'Video Library Wrap': ['dgc-wrap'], 'Video Grid': ['dgc-vgrid'], 'Video Note': ['dgc-vnote']})
r = mcp.put_section(PAGE, 'Video Library', 1, xml_structure=X, element_config=cfg, classes=cls, style=sty); print('videos', r.get('success'), r.get('warnings'))
# 3) CTA (same as homepage)
import build_reviews_cta_lib as ctalib
r = mcp.put_section(PAGE, 'CTA', 2, **ctalib.cta()); print('cta', r.get('success'), r.get('warnings'))
print([e.get('title') for e in mcp.call('elementor-get-page-structure', {'post_id': PAGE})['elements']])
