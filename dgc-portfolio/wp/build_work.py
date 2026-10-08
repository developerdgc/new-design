"""Work section: title, tabs, filters, grid with website / brand / case cards (built in small batches)."""
import sys, json, re, html
sys.path.insert(0, '/tmp/claude-0/-home-user-new-design/c0b0073b-578a-5cca-805d-2082208a4256/scratchpad')
import mcp
from common import BRANDS, N_PANELS, CASES, cases_by_channel, CH_ORDER, CH_LABEL
SITE = 'https://newportfolio.digitalgrowthcatalyze.com'
MM = json.load(open('media-map.json')); MID = {k: v['id'] for k, v in MM.items()}
link = lambda u, blank=False: {'destination': u, 'isTargetBlank': blank, 'tag': 'a'}
img = lambda key: {'src': {'id': MID[key]}, 'size': 'full'}
CH = {'Google Business Profile': 'gbp', 'AI Overview': 'aio', 'Google Ads': 'ppc', 'Local Services Ads': 'lsa', 'Web SEO': 'seo'}
FIX = {'Guter Cleaning': 'Gutter Cleaning', 'Concreate': 'Concrete', 'Remolding': 'Remodeling', 'Junk removal': 'Junk Removal', 'Dry Wall Service': 'Drywall Service'}
def dom(u): return re.sub(r'^https?://(www\.)?', '', u).split('/')[0] if u else ''
def rgba(hx, a):
    hx = hx.lstrip('#'); r, g, b = (int(hx[i:i + 2], 16) for i in (0, 2, 4)); return f'rgba({r},{g},{b},{a})'
def mix(hx, other, p):  # p = share of hx
    a = [int(hx.lstrip('#')[i:i + 2], 16) for i in (0, 2, 4)]; b = [int(other.lstrip('#')[i:i + 2], 16) for i in (0, 2, 4)]
    return '#' + ''.join(f'{round(x * p + y * (1 - p)):02x}' for x, y in zip(a, b))

class Frag:
    def __init__(self): self.x, self.cfg, self.cls, self.sty = '', {}, {}, {}
    def el(self, tag, cid, cls=None, cfg=None, sty=None, inner=''):
        self.x += f'<{tag} configuration-id="{cid}">{inner}</{tag}>' if inner != None else ''
        if cls: self.cls[cid] = cls
        if cfg: self.cfg[cid] = cfg
        if sty: self.sty[cid] = sty
        return f'<{tag} configuration-id="{cid}">{inner}</{tag}>'

def web_card(f, i, it):
    p = f'Web {i}'; cat = FIX.get(it['label'], it['label']); d = dom(it['url']); title = d or f'{cat} Website'
    w, h = MM[it['file']]['w'], MM[it['file']]['h']; dur = min(10, max(3.5, h / w * 1.25))
    url_html = f'https://<b>{html.escape(d)}</b>' if d else 'Private client'
    go = (f'<e-flexbox configuration-id="{p} Go"><e-div-block configuration-id="{p} Go Icon"></e-div-block></e-flexbox>')
    x = (f'<e-div-block configuration-id="{p}">'
         f'<e-flexbox configuration-id="{p} Device"><e-flexbox configuration-id="{p} Bar"><e-paragraph configuration-id="{p} URL"></e-paragraph></e-flexbox>'
         f'<e-div-block configuration-id="{p} Screen"><e-image configuration-id="{p} Shot"></e-image></e-div-block><e-paragraph configuration-id="{p} Chin"></e-paragraph></e-flexbox>'
         f'<e-grid configuration-id="{p} Meta"><e-div-block configuration-id="{p} Meta Text"><e-heading configuration-id="{p} Title"></e-heading><e-paragraph configuration-id="{p} Tag"></e-paragraph></e-div-block>{go}</e-grid></e-div-block>')
    f.x += x
    f.cls.update({p: ['dgc-work', 'dgc-c-web'], f'{p} Device': ['dgc-device'], f'{p} Bar': ['dgc-device-top'], f'{p} URL': ['dgc-device-url'], f'{p} Screen': ['dgc-screen2'],
                  f'{p} Shot': ['dgc-shot'], f'{p} Chin': ['dgc-chin'], f'{p} Meta': ['dgc-wmeta'], f'{p} Meta Text': ['dgc-wmeta-txt'], f'{p} Title': ['dgc-wmeta-h'],
                  f'{p} Tag': ['dgc-wmeta-p'], f'{p} Go': ['dgc-go'] + ([] if it['url'] else ['dgc-go-off']), f'{p} Go Icon': ['ico-arrow-ur']})
    f.cfg.update({f'{p} Device': ({'tag': 'a', 'link': link(it['url'], True)} if it['url'] else {'tag': 'div'}),
                  f'{p} URL': {'paragraph': url_html, 'tag': 'span'}, f'{p} Shot': {'image': img(it['file'])}, f'{p} Chin': {'paragraph': 'DGC', 'tag': 'span'},
                  f'{p} Title': {'tag': 'h3', 'title': html.escape(title)}, f'{p} Tag': {'paragraph': f'<em>Web</em>{html.escape(cat)}', 'tag': 'p'},
                  f'{p} Go': ({'tag': 'a', 'link': link(it['url'], True)} if it['url'] else {'tag': 'div'})})
    f.sty[f'{p} Shot'] = f'transition: object-position {dur:.1f}s;'

def lcard(f, p, slug, name, color, theme, palette, panel):
    dark = theme == 'dark'
    bg = (f'radial-gradient(85% 70% at 100% 0%, {rgba(color, .42)}, transparent 62%), radial-gradient(70% 60% at 0% 100%, {rgba(color, .16)}, transparent 70%), linear-gradient(160deg, #1a1a1b, #050505)' if dark
          else f'radial-gradient(85% 70% at 100% 0%, {rgba(color, .30)}, transparent 62%), linear-gradient(160deg, #f4f8fb, #dfe7ee)')
    sheet_bg = 'linear-gradient(150deg, #17191b, #070809)' if dark else '#ffffff'
    left = (f'<e-div-block configuration-id="{p} ID"><e-paragraph configuration-id="{p} Name"></e-paragraph><e-paragraph configuration-id="{p} Sub"></e-paragraph></e-div-block>'
            if panel else f'<e-paragraph configuration-id="{p} Primary"></e-paragraph>')
    sw = ''.join(f'<e-div-block configuration-id="{p} Swatch {k}"></e-div-block>' for k in range(len(palette)))
    x = (f'<e-div-block configuration-id="{p} Card"><e-flexbox configuration-id="{p} Sheet"><e-image configuration-id="{p} Logo"></e-image></e-flexbox>'
         f'<e-flexbox configuration-id="{p} Foot">{left}<e-flexbox configuration-id="{p} Swatches">{sw}<e-paragraph configuration-id="{p} Hex"></e-paragraph></e-flexbox></e-flexbox></e-div-block>')
    f.cls.update({f'{p} Card': ['dgc-lcard'] + (['dgc-lcard-panel'] if panel else []) + ['dgc-lcard-' + theme], f'{p} Sheet': ['dgc-lsheet'] + (['dgc-lsheet-panel'] if panel else []),
                  f'{p} Logo': ['dgc-lsheet-img'], f'{p} Foot': ['dgc-lfoot'], f'{p} Swatches': ['dgc-lsw'], f'{p} Hex': ['dgc-lhex']})
    f.sty[f'{p} Card'] = f'background: {bg};'
    f.sty[f'{p} Sheet'] = f'background: {sheet_bg}; box-shadow: 0 30px 50px -24px rgba(0,0,0,0.85), 0 0 0 2px {color}, 0 0 28px -6px {rgba(color, .55)};'
    f.cfg.update({f'{p} Logo': {'image': img(f'img/brands/{slug}/logo.png')}, f'{p} Hex': {'paragraph': color.upper(), 'tag': 'span'}})
    for k, c in enumerate(palette):
        f.cls[f'{p} Swatch {k}'] = ['dgc-sw']; f.sty[f'{p} Swatch {k}'] = f'background: {c};' + ('' if dark else ' border: 1px solid rgba(0,0,0,0.15);')
    if not dark:
        f.sty[f'{p} Foot'] = 'color: #5b6670;'; f.sty[f'{p} Hex'] = 'color: #10202a;'
    if panel:
        f.cls.update({f'{p} ID': ['dgc-lid'], f'{p} Name': ['dgc-lid-name'], f'{p} Sub': ['dgc-lid-sub']})
        f.cfg.update({f'{p} Name': {'paragraph': html.escape(name), 'tag': 'span'}, f'{p} Sub': {'paragraph': 'Logo · Brand identity', 'tag': 'span'}})
        f.sty[f'{p} Sub'] = f'color: {mix(color, "#ffffff", .75)};' if dark else f'color: {color};'
        if not dark: f.sty[f'{p} Name'] = 'color: #10202a;'
    else:
        f.cfg[f'{p} Primary'] = {'paragraph': 'Primary logo', 'tag': 'span'}
    return x

def brand_panel(f, p, b):
    slug, name, color, theme, palette, mocks = b
    mx = ''.join(f'<e-div-block configuration-id="{p} Mock {k}"><e-image configuration-id="{p} Mock {k} Img"></e-image></e-div-block>' for k in range(len(mocks)))
    x = (f'<e-grid configuration-id="{p} Panel"><e-div-block configuration-id="{p} Topline"></e-div-block><e-div-block configuration-id="{p} Main">' + lcard(f, p, slug, name, color, theme, palette, True)
         + f'</e-div-block><e-grid configuration-id="{p} Mocks">{mx}</e-grid></e-grid>')
    f.cls.update({f'{p} Panel': ['dgc-brand'], f'{p} Topline': ['dgc-brand-top'], f'{p} Main': ['dgc-brand-main'], f'{p} Mocks': ['dgc-brand-mocks']})
    f.sty[f'{p} Panel'] = (f'background: linear-gradient(180deg, #ffffff, {mix(color, "#f7fafb", .06)}); border: 1.5px solid {mix(color, "#dde8ea", .45)}; '
                           f'box-shadow: 0 30px 60px -34px rgba(6,40,54,0.6), 0 0 0 6px {rgba(color, .08)};')
    f.sty[f'{p} Topline'] = f'background: linear-gradient(90deg, {color}, {rgba(color, .3)} 60%, transparent);'
    for k, (m, label) in enumerate(mocks):
        f.cls[f'{p} Mock {k}'] = ['dgc-bm']; f.cls[f'{p} Mock {k} Img'] = ['dgc-bm-img']
        f.cfg[f'{p} Mock {k} Img'] = {'image': img(f'img/brands/{slug}/{m}.jpg')}
    return x

def brand_item(f, i, b):
    p = f'Brand {i}'
    if i <= N_PANELS:
        f.x += f'<e-div-block configuration-id="{p}">' + brand_panel(f, p, b) + '</e-div-block>'
        f.cls[p] = ['dgc-work', 'dgc-c-logo', 'dgc-c-brand']
    else:
        slug, name, color, theme, palette, mocks = b
        f.x += (f'<e-div-block configuration-id="{p}"><e-flexbox configuration-id="{p} Button">' + lcard(f, p, slug, name, color, theme, palette, False)
                + f'<e-paragraph configuration-id="{p} Hint"></e-paragraph></e-flexbox>'
                + f'<e-div-block configuration-id="{p} Meta"><e-heading configuration-id="{p} Title"></e-heading><e-paragraph configuration-id="{p} Tag"></e-paragraph></e-div-block>'
                + f'<e-div-block configuration-id="{p} Kit">' + brand_panel(f, p + ' Kit', b) + '</e-div-block></e-div-block>')
        f.cls.update({p: ['dgc-work', 'dgc-c-logo'], f'{p} Button': ['dgc-lbtn'], f'{p} Hint': ['dgc-lhint'], f'{p} Meta': ['dgc-wmeta-txt'],
                      f'{p} Title': ['dgc-wmeta-h'], f'{p} Tag': ['dgc-wmeta-p'], f'{p} Kit': ['dgc-kit']})
        f.cfg.update({f'{p} Button': {'tag': 'button'}, f'{p} Hint': {'paragraph': 'View brand kit →', 'tag': 'span'},
                      f'{p} Title': {'tag': 'h3', 'title': html.escape(name)}, f'{p} Tag': {'paragraph': '<em>Logo</em>Brand identity', 'tag': 'p'}})
        f.sty[f'{p} Meta'] = 'padding: 20px 4px 0;'

def case_card(f, i, cs):
    title, icon, channel, image = cs; p = f'Case {i}'
    f.x += (f'<e-div-block configuration-id="{p}"><e-flexbox configuration-id="{p} Card"><e-image configuration-id="{p} Mark"></e-image>'
            f'<e-flexbox configuration-id="{p} Top"><e-flexbox configuration-id="{p} Icon Box"><e-div-block configuration-id="{p} Icon"></e-div-block></e-flexbox><e-paragraph configuration-id="{p} Label"></e-paragraph></e-flexbox>'
            f'<e-paragraph configuration-id="{p} Title"></e-paragraph>'
            f'<e-flexbox configuration-id="{p} Foot"><e-image configuration-id="{p} Logo"></e-image><e-flexbox configuration-id="{p} Go"><e-paragraph configuration-id="{p} Go Text"></e-paragraph><e-paragraph configuration-id="{p} Go Arrow"></e-paragraph></e-flexbox></e-flexbox>'
            f'</e-flexbox></e-div-block>')
    f.cls.update({p: ['dgc-work', 'dgc-c-case', 'dgc-ch-' + CH[channel]], f'{p} Card': ['dgc-case'], f'{p} Mark': ['dgc-case-mark'], f'{p} Top': ['dgc-case-top'],
                  f'{p} Icon Box': ['dgc-case-ic'], f'{p} Icon': ['ico-c-' + icon], f'{p} Label': ['dgc-case-label'], f'{p} Title': ['dgc-case-title'],
                  f'{p} Foot': ['dgc-case-foot'], f'{p} Logo': ['dgc-case-logo'], f'{p} Go': ['dgc-case-go'], f'{p} Go Arrow': ['dgc-case-go-i']})
    f.cfg.update({f'{p} Card': {'tag': 'a', 'link': link(MM[f'img/casestudies/{image}.jpg']['url'])}, f'{p} Mark': {'image': img('img/brand/dgc-mark-white.png')},
                  f'{p} Label': {'paragraph': html.escape(channel), 'tag': 'span'}, f'{p} Title': {'paragraph': html.escape(title), 'tag': 'span'},
                  f'{p} Logo': {'image': img('img/brand/dgc-logo-white.png')}, f'{p} Go Text': {'paragraph': 'Read the case study', 'tag': 'span'},
                  f'{p} Go Arrow': {'paragraph': '→', 'tag': 'span'}})

def skeleton():
    f = Frag()
    tabs = ''.join(f'<e-flexbox configuration-id="Tab {k}"><e-paragraph configuration-id="Tab {k} Text"></e-paragraph></e-flexbox>' for k in ('All', 'Websites', 'Logos', 'Case Studies'))
    for k, key in (('All', 'all'), ('Websites', 'web'), ('Logos', 'logo'), ('Case Studies', 'case')):
        f.cls[f'Tab {k}'] = ['dgc-tab', 'dgc-f-' + key]; f.cfg[f'Tab {k}'] = {'tag': 'button'}; f.cfg[f'Tab {k} Text'] = {'paragraph': k, 'tag': 'span'}
    def subs(prefix, extra):
        out = ''
        for key, label in [('all', 'All')] + [(CH[c], CH_LABEL[c]) for c in CH_ORDER]:
            cid = f'{prefix} {label}'; out += f'<e-flexbox configuration-id="{cid}"><e-paragraph configuration-id="{cid} Text"></e-paragraph></e-flexbox>'
            f.cls[cid] = ['dgc-stab', 'dgc-sf-' + key]; f.cfg[cid] = {'tag': 'button'}; f.cfg[cid + ' Text'] = {'paragraph': label, 'tag': 'span'}
        return out
    heads = ''
    for key, a, b, href, btn in (('web', 'Website', 'Projects', '#work-web', 'All websites →'), ('logo', 'Client', 'Logos', '#work-logo', 'Logo work →'), ('case', 'Case', 'Studies', SITE + '/case-studies/', 'All case studies →')):
        cid = f'Group {b}'
        heads += f'<e-flexbox configuration-id="{cid}"><e-heading configuration-id="{cid} Title"></e-heading><e-div-block configuration-id="{cid} Line"></e-div-block><e-flexbox configuration-id="{cid} Button"><e-paragraph configuration-id="{cid} Button Text"></e-paragraph></e-flexbox></e-flexbox>'
        f.cls.update({cid: ['dgc-ghead', 'dgc-g-' + key], f'{cid} Title': ['dgc-ghead-h'], f'{cid} Line': ['dgc-ghead-line'], f'{cid} Button': ['dgc-ghead-btn']})
        f.cfg.update({f'{cid} Title': {'tag': 'h3', 'title': f'{a} <span>{b}</span>'}, f'{cid} Button': {'tag': 'a', 'link': link(href)}, f'{cid} Button Text': {'paragraph': btn, 'tag': 'span'}})
    sub_case, sub_all = subs('Filter', None), subs('Filter All', None)
    X = f'''<e-flexbox configuration-id="Work">
 <e-div-block configuration-id="Work Grid Background"></e-div-block>
 <e-div-block configuration-id="Work Wrap">
  <e-grid configuration-id="Work Title Row">
   <e-div-block configuration-id="Work Title Left"><e-paragraph configuration-id="Work Kicker"></e-paragraph><e-heading configuration-id="Work Title"></e-heading></e-div-block>
   <e-div-block configuration-id="Work Title Side"><e-paragraph configuration-id="Work Intro"></e-paragraph>
    <e-flexbox configuration-id="Work Hint"><e-div-block configuration-id="Work Hint Mouse"></e-div-block><e-paragraph configuration-id="Work Hint Mouse Text"></e-paragraph><e-paragraph configuration-id="Work Hint Touch Text"></e-paragraph></e-flexbox>
   </e-div-block>
  </e-grid>
  <e-flexbox configuration-id="Work Tabs">{tabs}</e-flexbox>
  <e-flexbox configuration-id="Case Filters">{sub_case}</e-flexbox>
  <e-grid configuration-id="Work Grid">{heads}<e-flexbox configuration-id="Case Filters All">{sub_all}</e-flexbox></e-grid>
  <e-flexbox configuration-id="Work More"><e-flexbox configuration-id="More Websites"><e-paragraph configuration-id="More Websites Text"></e-paragraph><e-div-block configuration-id="More Websites Icon"></e-div-block></e-flexbox><e-flexbox configuration-id="All Case Studies"><e-paragraph configuration-id="All Case Studies Text"></e-paragraph><e-div-block configuration-id="All Case Studies Icon"></e-div-block></e-flexbox></e-flexbox>
 </e-div-block>
</e-flexbox>'''
    f.cls.update({'Work': ['dgc-work-sec'], 'Work Grid Background': ['dgc-work-gridbg'], 'Work Wrap': ['dgc-wrap', 'dgc-work-wrap'], 'Work Title Row': ['dgc-wtitle'],
                  'Work Kicker': ['dgc-kicker'], 'Work Title': ['dgc-wtitle-big'], 'Work Title Side': ['dgc-wtitle-side'], 'Work Intro': ['dgc-body-p'],
                  'Work Hint': ['dgc-hint'], 'Work Hint Mouse': ['dgc-hint-mouse'], 'Work Hint Touch Text': ['dgc-hint-t'], 'Work Tabs': ['dgc-filters'],
                  'Case Filters': ['dgc-subfilters', 'dgc-sub-case'], 'Work Grid': ['dgc-grid'], 'Case Filters All': ['dgc-subfilters', 'dgc-subfilters-grid', 'dgc-sub-all'],
                  'Work More': ['dgc-more'], 'More Websites': ['dgc-btn', 'dgc-btn-hot-light', 'dgc-more-btn'], 'More Websites Icon': ['ico-arrow-ur'],
                  'All Case Studies': ['dgc-btn', 'dgc-btn-hot-light', 'dgc-allcase'], 'All Case Studies Icon': ['ico-arrow-ur']})
    f.cfg.update({'Work': {'tag': 'section'}, 'Work Kicker': {'paragraph': 'Selected work', 'tag': 'span'}, 'Work Title': {'tag': 'h2', 'title': 'W<span>o</span>rk'},
                  'Work Intro': {'paragraph': 'Websites, logos and case studies for real local businesses. Every website screen shows the full homepage, top to bottom.'},
                  'Work Hint Mouse Text': {'paragraph': 'Hover a screen to scroll the whole page', 'tag': 'span'}, 'Work Hint Touch Text': {'paragraph': 'Scroll down and each site plays on its own', 'tag': 'span'},
                  'More Websites': {'tag': 'button'}, 'More Websites Text': {'paragraph': 'Show more websites', 'tag': 'span'},
                  'All Case Studies': {'tag': 'a', 'link': link(SITE + '/case-studies/')}, 'All Case Studies Text': {'paragraph': 'View All Case Studies', 'tag': 'span'}})
    f.x = X
    return f

def find(tree, title):
    for e in tree:
        if e.get('title') == title: return e
        r = find(e.get('elements', []), title)
        if r: return r

def append(post, parent, f):
    for attempt in range(3):
        try:
            r = mcp.call('elementor-build-composition', {'post_id': post, 'xml_structure': f.x, 'element_config': f.cfg, 'classes': f.cls, 'style': f.sty, 'parent_id': parent, 'mode': 'append'})
            mcp.call('elementor-publish-document', {'post_id': post}); return r
        except Exception as e:
            print('retry', attempt, str(e)[:200])
    raise RuntimeError('append failed')

if __name__ == '__main__':
    PAGE = 126
    f = skeleton()
    r = mcp.put_section(PAGE, 'Work', 3, xml_structure=f.x, element_config=f.cfg, classes=f.cls, style=f.sty)
    print('skeleton', r.get('success'), r.get('warnings'))
    tree = mcp.call('elementor-get-page-structure', {'post_id': PAGE})['elements']
    grid = find(tree, 'Work Grid')['id']; print('grid', grid)
    items = sorted(json.load(open('/tmp/claude-0/items.json')), key=lambda it: not it['url'])
    B = 5
    for s in range(0, len(items), B):
        f = Frag()
        for i, it in enumerate(items[s:s + B], s + 1): web_card(f, i, it)
        r = append(PAGE, grid, f); print('web', s + 1, '-', min(s + B, len(items)), r.get('success'), r.get('warnings'))
    for s in range(0, len(BRANDS), 2):
        f = Frag()
        for i, b in enumerate(BRANDS[s:s + 2], s + 1): brand_item(f, i, b)
        r = append(PAGE, grid, f); print('brands', s + 1, r.get('success'), r.get('warnings'))
    cases = [cs for rank, cs in cases_by_channel() if rank < 3]
    for s in range(0, len(cases), 5):
        f = Frag()
        for i, cs in enumerate(cases[s:s + 5], s + 1): case_card(f, i, cs)
        r = append(PAGE, grid, f); print('cases', s + 1, r.get('success'), r.get('warnings'))
    print([e.get('title') for e in mcp.call('elementor-get-page-structure', {'post_id': PAGE})['elements']])
