"""Custom Code on digitalgrowthcatalyze.com, scoped to the Case Studies + Video Reviews pages only:
interactions (popups, filters, video player) at body end; font preload/fallbacks + noindex in the head."""
import os, json, urllib.request
os.environ['DGC_SITE'] = 'main'
import mcp
from head_snippets import FONTS
PAGES = json.load(open('pages-main.json')); IDS = [PAGES['case-studies']['id'], PAGES['video-reviews']['id']]
COND = [f'include/singular/page/{i}' for i in IDS]
B = 'https://digitalgrowthcatalyze.com/wp-json/wp/v2/'
def req(path, data=None, method='GET'):
    r = urllib.request.Request(B + path, json.dumps(data).encode() if data is not None else None, {'Authorization': mcp.AUTH, 'Content-Type': 'application/json', 'User-Agent': 'Mozilla/5.0'}, method=method)
    return json.load(urllib.request.urlopen(r, timeout=120))
NOINDEX = '<meta name="robots" content="noindex, nofollow">'
# the main site does not load Elementor's Google Fonts, so these two pages load the portfolio fonts themselves
GFONTS = ('<style id="dgc-webfonts">'  # LiteSpeed strips Google Fonts <link>s on this site, so declare the faces directly
          '@font-face{font-family:"Unbounded";font-style:normal;font-weight:200 900;font-display:swap;src:url(https://fonts.gstatic.com/s/unbounded/v12/Yq6W-LOTXCb04q32xlpwu8Zf.woff2) format("woff2");unicode-range:U+0000-00FF,U+0131,U+0152-0153,U+02BB-02BC,U+02C6,U+02DA,U+02DC,U+0304,U+0308,U+0329,U+2000-206F,U+20AC,U+2122,U+2191,U+2193,U+2212,U+2215,U+FEFF,U+FFFD}'
          '@font-face{font-family:"Manrope";font-style:normal;font-weight:200 800;font-display:swap;src:url(https://fonts.gstatic.com/s/manrope/v20/xn7gYHE41ni1AdIRggexSg.woff2) format("woff2");unicode-range:U+0000-00FF,U+0131,U+0152-0153,U+02BB-02BC,U+02C6,U+02DA,U+02DC,U+0304,U+0308,U+0329,U+2000-206F,U+20AC,U+2122,U+2191,U+2193,U+2212,U+2215,U+FEFF,U+FFFD}'
          '</style>')
SNIPS = [('DGC interactions (case studies + video reviews)', open('/home/user/new-design/dgc-portfolio/wp/dgc-interactions.html').read(), 'elementor_body_end'),
         ('DGC head: fonts + noindex (case studies + video reviews)', NOINDEX + '\n' + GFONTS + '\n' + FONTS, 'elementor_head')]
ids = json.load(open('snippets-main.json')) if os.path.exists('snippets-main.json') else {}
for title, code, loc in SNIPS:
    body = {'title': title, 'status': 'publish', 'meta': {'_elementor_code': code, '_elementor_location': loc, '_elementor_priority': 1}}
    d = req('elementor_snippet' + (f'/{ids[title]}' if title in ids else ''), body, 'POST'); ids[title] = d['id']
    r = mcp.call('elementor-manage-site-parts', {'operations': [{'action': 'update', 'post_id': d['id'], 'conditions': COND}]})
    print(title, d['id'], json.dumps(r)[:160])
json.dump(ids, open('snippets-main.json', 'w'), indent=1)
# Yoast noindex too (keeps the pages out of the Yoast sitemap) - only works if Yoast exposes the meta over REST
for i in IDS:
    try:
        d = req(f'pages/{i}', {'meta': {'_yoast_wpseo_meta-robots-noindex': '1', '_yoast_wpseo_meta-robots-nofollow': '1'}}, 'POST')
        print('yoast meta', i, {k: v for k, v in d.get('meta', {}).items() if 'yoast' in k} or 'not exposed')
    except Exception as e: print('yoast meta', i, 'failed', getattr(e, 'code', ''), str(e)[:100])

# keep the site-wide "Single Post" theme template (banner + quote sidebar) off these two pages, and use the full-width page template
SINGLE = 3770
parts = mcp.call('elementor-list-site-parts', {})['result']
cond = next(p for p in parts if p['id'] == SINGLE)['conditions']
want = cond + [c for c in (f'exclude/singular/page/{i}' for i in IDS) if c not in cond]
if want != cond: print('single template', json.dumps(mcp.call('elementor-manage-site-parts', {'operations': [{'action': 'update', 'post_id': SINGLE, 'conditions': want}]}))[:220])
for i in IDS: print('template', i, req(f'pages/{i}', {'template': 'elementor_header_footer'}, 'POST')['template'])
