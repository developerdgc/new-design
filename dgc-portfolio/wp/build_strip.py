import mcp, json
from classes_base import icon_css
from dgc_site import SITE, MEDIA, PAGES
MM = json.load(open(MEDIA)); M = {k: v['id'] for k, v in MM.items()}
PAGE = json.load(open(PAGES))['portfolio']['id']
PLAY = '<svg viewBox="0 0 24 24"><path d="M8 5v14l11-7z"/></svg>'
VIDEOS = ['review-1', 'review-2', 'review-3', 'review-4', 'review-5', 'review-6']  # thumbnails only, no captions
INDUSTRIES = ['Towing', 'Cleaning', 'Limousine', 'Construction', 'Roofing', 'Painting', 'Home Inspection', 'Carpet Cleaning', 'Garage Doors', 'Janitorial', 'Real Estate', 'Junk Removal', 'Auto Detailing', 'Gutters']
C = {
 'ico-play': icon_css(PLAY, 20),
 'dgc-clients': 'position: relative; flex-direction: column; gap: 0; padding: 36px 0 44px; overflow: hidden; background: var(--navy-2); border-top: 1px solid rgba(255,255,255,0.09); font-family: Manrope;',
 'dgc-clients-head': 'display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 16px; margin-bottom: 26px;',
 'dgc-live': 'display: inline-flex; align-items: center; gap: 12px; width: auto; padding: 0; color: #ffffff; font-size: 0.78rem; font-weight: 800; letter-spacing: 0.2em; text-transform: uppercase;',
 'dgc-live-dot': 'width: 9px; height: 9px; min-width: 0; padding: 0; border-radius: 50%; background: #3ccf6e; box-shadow: 0 0 0 5px rgba(60,207,110,0.18);',
 'dgc-textlink': 'display: inline-flex; align-items: center; gap: 8px; width: auto; padding: 0; color: var(--orange); font-size: 0.88rem; font-weight: 800; text-decoration: none; transition: color 0.25s; &:hover { color: #ffffff; }',
 'dgc-track': 'display: flex; flex-wrap: nowrap; align-items: center; gap: 0; width: max-content; padding: 64px 0 56px; margin: -40px 0 -24px;',
 'dgc-vlist': 'display: flex; flex-wrap: nowrap; gap: 18px; width: auto; padding: 0 18px 0 0;',
 'dgc-vthumb': 'position: relative; flex: none; width: 196px; padding: 0; transition: transform 0.45s, opacity 0.35s, filter 0.35s;',
 'dgc-vbtn': 'position: relative; display: block; width: 100%; aspect-ratio: 9 / 16; padding: 0; overflow: hidden; border: 2px solid rgba(246,164,64,0.75); border-radius: 10px; background: var(--navy-3); cursor: pointer; box-shadow: 0 0 0 4px rgba(255,255,255,0.06), 0 18px 34px -16px rgba(0,0,0,0.8); transition: border-color 0.35s, box-shadow 0.45s;',
 'dgc-vimg': 'position: absolute; inset: 0; width: 100%; height: 100%; object-fit: cover;',
 'dgc-play': 'position: absolute; z-index: 2; left: 50%; top: 64%; display: flex; align-items: center; justify-content: center; width: 52px; height: 52px; margin: -26px 0 0 -26px; padding: 0; border-radius: 50%; background: rgba(246,164,64,0.95); color: var(--abyss); box-shadow: 0 0 0 8px rgba(246,164,64,0.25); transition: transform 0.3s, background 0.3s, box-shadow 0.3s;',
 'dgc-vcap': 'display: block; margin-top: 12px; padding: 0; text-align: left; color: #ffffff; transition: opacity 0.3s;',
 'dgc-vname': 'display: block; font-size: 0.92rem; font-weight: 700; line-height: 1.25;',
 'dgc-vsub': 'display: block; margin-top: 4px; font-size: 0.74rem; font-weight: 700; color: var(--orange);',
 'dgc-ribbon': 'position: relative; z-index: 1; width: 104%; margin: 22px -2% 0; padding: 14px 0; overflow: hidden; background: var(--orange); transform: rotate(-2.2deg); box-shadow: 0 20px 40px -20px rgba(0,0,0,0.6);',
 'dgc-rtrack': 'display: flex; flex-wrap: nowrap; gap: 0; width: max-content; padding: 0;',
 'dgc-rlist': 'display: flex; flex-wrap: nowrap; gap: 0; width: auto; padding: 0;',
 'dgc-rword': 'display: flex; align-items: center; gap: 26px; padding-right: 26px; font-family: Unbounded; font-size: 1.05rem; font-weight: 700; text-transform: uppercase; white-space: nowrap; color: var(--abyss);',
}
print('classes', mcp.upsert_classes(C))
link = lambda u, blank=False: {'destination': u, 'isTargetBlank': blank, 'tag': 'a'}
cards = ''
cfg, cls, sty = {}, {}, {}
for i, k in enumerate(VIDEOS, 1):
    p = f'Video {i}'
    cards += (f'<e-div-block configuration-id="{p}"><e-flexbox configuration-id="{p} Button"><e-image configuration-id="{p} Poster"></e-image>'
              f'<e-flexbox configuration-id="{p} Play"><e-div-block configuration-id="{p} Play Icon"></e-div-block></e-flexbox></e-flexbox></e-div-block>')
    cfg[f'{p} Button'] = {'tag': 'a', 'link': link(MM[f'video/{k}.mp4']['url'])}
    cfg[f'{p} Poster'] = {'image': {'src': {'id': M[f'video/{k}.jpg']}, 'size': 'full'}}
    cls[p] = ['dgc-vthumb']; cls[f'{p} Button'] = ['dgc-vbtn']; cls[f'{p} Poster'] = ['dgc-vimg']; cls[f'{p} Play'] = ['dgc-play']
    cls[f'{p} Play Icon'] = ['ico-play']
    sty[f'{p} Play Icon'] = 'margin-left: 3px;'
words = ''
for i, w in enumerate(INDUSTRIES, 1):
    words += f'<e-paragraph configuration-id="Industry {i}"></e-paragraph>'
    cfg[f'Industry {i}'] = {'paragraph': w, 'tag': 'span'}; cls[f'Industry {i}'] = ['dgc-rword']
X = f'''<e-flexbox configuration-id="Video Strip">
 <e-flexbox configuration-id="Strip Head">
  <e-flexbox configuration-id="Strip Label"><e-div-block configuration-id="Live Dot"></e-div-block><e-paragraph configuration-id="Strip Label Text"></e-paragraph></e-flexbox>
  <e-flexbox configuration-id="Strip Link"><e-paragraph configuration-id="Strip Link Text"></e-paragraph><e-div-block configuration-id="Strip Link Icon"></e-div-block></e-flexbox>
 </e-flexbox>
 <e-flexbox configuration-id="Video Track"><e-flexbox configuration-id="Video List">{cards}</e-flexbox></e-flexbox>
 <e-div-block configuration-id="Industry Ribbon"><e-flexbox configuration-id="Ribbon Track"><e-flexbox configuration-id="Ribbon List">{words}</e-flexbox></e-flexbox></e-div-block>
</e-flexbox>'''
cfg.update({'Video Strip': {'tag': 'section'}, 'Strip Label Text': {'paragraph': 'Video reviews', 'tag': 'span'},
            'Strip Link': {'tag': 'a', 'link': link(SITE + '/video-reviews/')}, 'Strip Link Text': {'paragraph': 'Watch all video reviews', 'tag': 'span'}})
cls.update({'Video Strip': ['dgc-clients'], 'Strip Head': ['dgc-wrap', 'dgc-clients-head'], 'Strip Label': ['dgc-live'], 'Live Dot': ['dgc-live-dot'],
            'Strip Link': ['dgc-textlink'], 'Strip Link Icon': ['ico-arrow-ur'], 'Video Track': ['dgc-track'], 'Video List': ['dgc-vlist'],
            'Industry Ribbon': ['dgc-ribbon'], 'Ribbon Track': ['dgc-rtrack'], 'Ribbon List': ['dgc-rlist']})
sty['Strip Link Icon'] = 'width: 15px; height: 15px;'
r = mcp.put_section(PAGE, 'Video Strip', 1, xml_structure=X, element_config=cfg, classes=cls, style=sty)
print(json.dumps({k: r.get(k) for k in ('success', 'warnings', 'root_element_ids')})[:600])
print(json.dumps(mcp.call('elementor-publish-document', {'post_id': PAGE}))[:120])
