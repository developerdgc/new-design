import sys, json
sys.path.insert(0, '/tmp/claude-0/-home-user-new-design/c0b0073b-578a-5cca-805d-2082208a4256/scratchpad')
import mcp
from build_work import Frag, case_card, append, CH, MID, link, SITE
from common import cases_by_channel, CH_ORDER, CH_LABEL
from dgc_site import PAGES
PAGE = json.load(open(PAGES))['case-studies']['id']
C = {
 'dgc-phero': 'position: relative; overflow: hidden; isolation: isolate; flex-direction: column; gap: 0; padding: 222px 0 76px; color: var(--fog); font-family: Manrope; background: radial-gradient(38% 55% at 0% 0%, rgba(28,222,225,0.55), transparent 70%), radial-gradient(34% 50% at 100% 100%, rgba(28,222,225,0.45), transparent 70%), #062836; @media(--mobile) { padding: 180px 0 56px; }',
 'dgc-phero-mark': 'position: absolute; z-index: -1; right: 6%; top: 50%; width: 320px; height: auto; margin-top: -160px; opacity: 0.07; pointer-events: none; transform: rotate(-14deg);',
 'dgc-phero-h1': 'display: block; max-width: 16ch; margin-top: 18px; font-family: Unbounded; font-size: clamp(2.3rem, 5vw, 4.4rem); font-weight: 700; line-height: 1.02; letter-spacing: -0.035em; color: #ffffff;',
 'dgc-phero-p': 'display: block; max-width: 54ch; margin-top: 18px; font-family: Manrope; font-size: 1.06rem; line-height: 1.7; color: var(--fog);',
 'dgc-phero-btns': 'flex-wrap: wrap; gap: 12px; margin-top: 28px; padding: 0;',
 'dgc-pbody': 'flex-direction: column; gap: 0; padding: 80px 0 100px; background: #ffffff; font-family: Manrope; @media(--mobile) { padding: 56px 0 72px; }',
 'dgc-cs-filters': 'margin: 0 0 44px; padding: 0; border-top: 0;',
 'dgc-cs-item': 'min-width: 0;',
 'dgc-cgrid': 'display: grid; grid-template-columns: repeat(3, 1fr); grid-template-rows: auto; gap: 26px; @media(--tablet) { grid-template-columns: repeat(2, 1fr); } @media(--mobile) { grid-template-columns: 1fr; }',
}
print('classes', mcp.upsert_classes(C))
mcp.prioritize(['dgc-cs-filters'])
# 1) page hero
XH = '''<e-flexbox configuration-id="Page Hero"><e-image configuration-id="Page Hero Mark"></e-image><e-div-block configuration-id="Page Hero Wrap">
 <e-paragraph configuration-id="Page Hero Kicker"></e-paragraph><e-heading configuration-id="Page Hero Title"></e-heading><e-paragraph configuration-id="Page Hero Text"></e-paragraph>
 <e-flexbox configuration-id="Page Hero Buttons"><e-flexbox configuration-id="Browse Button"><e-paragraph configuration-id="Browse Button Text"></e-paragraph><e-div-block configuration-id="Browse Button Icon"></e-div-block></e-flexbox><e-flexbox configuration-id="Videos Button"><e-paragraph configuration-id="Videos Button Text"></e-paragraph></e-flexbox></e-flexbox>
</e-div-block></e-flexbox>'''
cfg = {'Page Hero': {'tag': 'section'}, 'Page Hero Mark': {'image': {'src': {'id': MID['img/brand/dgc-mark-white.png']}, 'size': 'full'}},
       'Page Hero Kicker': {'paragraph': 'Case studies', 'tag': 'span'}, 'Page Hero Title': {'tag': 'h1', 'title': 'How we grow local <span>businesses.</span>'},
       'Page Hero Text': {'paragraph': 'A closer look at the strategy behind the results: what we built, what we changed on Google, and what it did for calls and leads across diverse industries.'},
       'Browse Button': {'tag': 'a', 'link': link('#cases')}, 'Browse Button Text': {'paragraph': 'Browse case studies', 'tag': 'span'},
       'Videos Button': {'tag': 'a', 'link': link(SITE + '/video-reviews/')}, 'Videos Button Text': {'paragraph': 'Watch video reviews', 'tag': 'span'}}
cls = {'Page Hero': ['dgc-phero'], 'Page Hero Mark': ['dgc-phero-mark'], 'Page Hero Wrap': ['dgc-wrap'], 'Page Hero Kicker': ['dgc-kicker', 'dgc-kicker-dark'],
       'Page Hero Title': ['dgc-phero-h1', 'dgc-h2-orange'], 'Page Hero Text': ['dgc-phero-p'], 'Page Hero Buttons': ['dgc-phero-btns'],
       'Browse Button': ['dgc-btn', 'dgc-btn-orange'], 'Browse Button Icon': ['ico-arrow-ur'], 'Videos Button': ['dgc-btn', 'dgc-btn-ghost']}
r = mcp.put_section(PAGE, 'Page Hero', 0, xml_structure=XH, element_config=cfg, classes=cls); print('hero', r.get('success'), r.get('warnings'))
# 2) filters + grid shell
f = Frag(); tabs = ''
for key, label in [('all', 'All')] + [(CH[c], CH_LABEL[c]) for c in CH_ORDER]:
    cid = f'Filter {label}'; tabs += f'<e-flexbox configuration-id="{cid}"><e-paragraph configuration-id="{cid} Text"></e-paragraph></e-flexbox>'
    f.cls[cid] = ['dgc-tab', 'dgc-sf-' + key]; f.cfg[cid] = {'tag': 'button'}; f.cfg[cid + ' Text'] = {'paragraph': label, 'tag': 'span'}
f.x = f'<e-flexbox configuration-id="Case Library"><e-div-block configuration-id="Case Library Wrap"><e-flexbox configuration-id="Case Library Filters">{tabs}</e-flexbox><e-grid configuration-id="Case Library Grid"></e-grid></e-div-block></e-flexbox>'
f.cfg['Case Library'] = {'tag': 'section'}
f.cls.update({'Case Library': ['dgc-pbody'], 'Case Library Wrap': ['dgc-wrap'], 'Case Library Filters': ['dgc-filters', 'dgc-cs-filters'], 'Case Library Grid': ['dgc-cgrid']})
r = mcp.put_section(PAGE, 'Case Library', 1, xml_structure=f.x, element_config=f.cfg, classes=f.cls, style=f.sty); print('library', r.get('success'), r.get('warnings'))
tree = mcp.call('elementor-get-page-structure', {'post_id': PAGE})['elements']
def find(es, t):
    for e in es:
        if e.get('title') == t: return e
        x = find(e.get('elements', []), t)
        if x: return x
grid = find(tree, 'Case Library Grid')['id']
cases = [cs for rank, cs in cases_by_channel()]
for s in range(0, len(cases), 5):
    f = Frag()
    for i, cs in enumerate(cases[s:s + 5], s + 1): case_card(f, i, cs)
    for k in list(f.cls):  # library cards are plain items, not homepage work cards
        if f.cls[k][:2] == ['dgc-work', 'dgc-c-case']: f.cls[k] = ['dgc-cs-item'] + f.cls[k][2:]
    r = append(PAGE, grid, f); print('cases', s + 1, r.get('success'), r.get('warnings'))
# 3) CTA (same as homepage)
import build_reviews_cta_lib as ctalib
r = mcp.put_section(PAGE, 'CTA', 2, **ctalib.cta()); print('cta', r.get('success'), r.get('warnings'))
print([e.get('title') for e in mcp.call('elementor-get-page-structure', {'post_id': PAGE})['elements']])
