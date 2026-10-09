"""digitalgrowthcatalyze.com: give Case Studies + Video Reviews the same page hero as the rest of the live site
(gradient band, glowing rounded box, uppercase title, one-line subtitle, 'Get a Free Quote' button)."""
import os, json
os.environ['DGC_SITE'] = 'main'
import mcp
from build_work import link
from dgc_site import SITE, PAGES
P = json.load(open(PAGES))
BG = SITE + '/wp-content/uploads/2026/02/Footer-Gradient-1.png'
C = {
 'dgc-mhero': f'position: relative; flex-direction: column; align-items: center; justify-content: center; gap: 0; min-height: 90vh; padding: 220px 20px 70px; background-image: url("{BG}"); background-size: cover; background-position: center center; background-repeat: no-repeat; @media(--mobile) {{ min-height: 45vh; padding: 150px 20px 30px; }}',
 'dgc-mhero-box': 'display: flex; flex-direction: column; align-items: center; gap: 0; width: 70%; max-width: 1100px; padding: 50px 30px; border-radius: 20px; box-shadow: inset 2px 1px 14px 2px #f6a440; text-align: center; @media(--tablet) { width: 85%; } @media(--mobile) { width: 100%; padding: 30px; }',
 'dgc-mhero-h1': 'display: block; margin: 0; font-family: Raleway; font-size: 45px; font-weight: 700; line-height: 1.2; text-transform: uppercase; color: #ffffff; @media(--mobile) { font-size: 30px; }',
 'dgc-mhero-sub': 'display: block; margin-top: 10px; font-family: Poppins; font-size: 16px; font-weight: 500; line-height: 1.5; color: #ffffff; @media(--mobile) { font-size: 14px; }',
 'dgc-mhero-btn': 'display: inline-flex; align-items: center; gap: 12px; width: auto; margin-top: 20px; padding: 16px 25px; border-radius: 10px; background: #f6a440; color: #000000; font-family: Poppins; font-size: 16px; font-weight: 600; line-height: 1.1; text-decoration: none; @media(--mobile) { font-size: 14px; }',
}
print('classes', mcp.upsert_classes(C))
HEROES = {
 'case-studies': ('Case Studies', 'Your Growth Partner in the Digital Era | Real Results for Local Businesses'),
 'video-reviews': ('Video Reviews', 'Your Growth Partner in the Digital Era | Hear It From Our Clients'),
}
X = '''<e-flexbox configuration-id="Page Hero"><e-flexbox configuration-id="Hero Box"><e-heading configuration-id="Hero Title"></e-heading><e-paragraph configuration-id="Hero Sub"></e-paragraph>
 <e-flexbox configuration-id="Hero Quote"><e-paragraph configuration-id="Hero Quote Text"></e-paragraph><e-div-block configuration-id="Hero Quote Icon"></e-div-block></e-flexbox></e-flexbox></e-flexbox>'''
for key, (title, sub) in HEROES.items():
    cfg = {'Page Hero': {'tag': 'section'}, 'Hero Title': {'tag': 'h1', 'title': title}, 'Hero Sub': {'paragraph': sub},
           'Hero Quote': {'tag': 'a', 'link': link(SITE + '/contact-us/')}, 'Hero Quote Text': {'paragraph': 'Get a Free Quote', 'tag': 'span'}}
    cls = {'Page Hero': ['dgc-mhero'], 'Hero Box': ['dgc-mhero-box'], 'Hero Title': ['dgc-mhero-h1'], 'Hero Sub': ['dgc-mhero-sub'],
           'Hero Quote': ['dgc-mhero-btn'], 'Hero Quote Icon': ['ico-arrow-right']}
    r = mcp.put_section(P[key]['id'], 'Page Hero', 0, xml_structure=X, element_config=cfg, classes=cls)
    print(key, r.get('success'), r.get('warnings'), [e.get('title') for e in mcp.call('elementor-get-page-structure', {'post_id': P[key]['id']})['elements']])
