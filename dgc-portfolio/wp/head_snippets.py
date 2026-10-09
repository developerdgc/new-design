import json, urllib.request, html
import mcp
B = 'https://newportfolio.digitalgrowthcatalyze.com/wp-json/wp/v2/elementor_snippet'
def post(url, body):
    r = urllib.request.Request(url, json.dumps(body).encode(), {'Authorization': mcp.AUTH, 'Content-Type': 'application/json'}, method='POST')
    return json.load(urllib.request.urlopen(r))
FONTS = '''<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="preload" as="font" type="font/woff2" crossorigin href="https://fonts.gstatic.com/s/unbounded/v12/Yq6W-LOTXCb04q32xlpwu8Zf.woff2">
<link rel="preload" as="font" type="font/woff2" crossorigin href="https://fonts.gstatic.com/s/manrope/v20/xn7gYHE41ni1AdIRggexSg.woff2">'''
# Size-matched fallbacks so text keeps its width while the Google fonts load (less layout shift).
ADJ = {'Manrope': 102, 'Unbounded': 128, 'Poppins': 111}
SELS = json.load(open('font_sels.json'))
def fallback_css():
    out = []
    for fam, adj in ADJ.items():
        out.append(f'@font-face{{font-family:"{fam} Fallback";src:local("Arial"),local("Liberation Sans"),local("Helvetica");font-weight:100 500;size-adjust:{adj}%}}')
        out.append(f'@font-face{{font-family:"{fam} Fallback";src:local("Arial Bold"),local("Arial-BoldMT"),local("Liberation Sans Bold"),local("Helvetica Bold");font-weight:600 900;size-adjust:{adj}%}}')
        if not SELS.get(fam): continue
        out.append(',\n'.join('body ' + x for x in SELS[fam]) + f'{{font-family:{fam},"{fam} Fallback",sans-serif}}')
    return '<style id="dgc-font-fallbacks">\n' + '\n'.join(out) + '\n</style>'
FONTS += '\n' + fallback_css()
def meta(title, desc, url):
    t, d = html.escape(title), html.escape(desc)
    return (f'<meta name="description" content="{d}">\n<meta property="og:type" content="website">\n<meta property="og:title" content="{t}">\n'
            f'<meta property="og:description" content="{d}">\n<meta property="og:url" content="{url}">\n<meta name="twitter:card" content="summary_large_image">')
S = 'https://newportfolio.digitalgrowthcatalyze.com'
SNIPS = [
 ('DGC head: font preload', FONTS, ['include/general']),
 ('DGC head: Portfolio meta', meta('Portfolio – Digital Growth Catalyze', 'Websites, logos, case studies and video reviews from Digital Growth Catalyze, the web, SEO and Google Ads agency for local service businesses across the USA.', S + '/'), ['include/singular/front_page']),
 ('DGC head: Case Studies meta', meta('Case Studies – Digital Growth Catalyze', 'Case studies from Digital Growth Catalyze clients across towing, cleaning, limo, car rental, contracting and more.', S + '/case-studies/'), ['include/singular/page/128']),
 ('DGC head: Video Reviews meta', meta('Video Reviews – Digital Growth Catalyze', 'Video reviews from Digital Growth Catalyze clients: real business owners talking about their websites, SEO and Google Ads results.', S + '/video-reviews/'), ['include/singular/page/130']),
]
if __name__ == '__main__':
    ids = json.load(open('snippets.json')) if __import__('os').path.exists('snippets.json') else {}
    for title, code, cond in SNIPS:
        body = {'title': title, 'status': 'publish', 'meta': {'_elementor_code': code, '_elementor_location': 'elementor_head', '_elementor_priority': 1}}
        d = post(B + (f'/{ids[title]}' if title in ids else ''), body); ids[title] = d['id']
        r = mcp.call('elementor-manage-site-parts', {'operations': [{'action': 'update', 'post_id': d['id'], 'conditions': cond}]})
        print(title, d['id'], json.dumps(r)[:200])
    json.dump(ids, open('snippets.json', 'w'), indent=1)
