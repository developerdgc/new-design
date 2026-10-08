import mcp, json, html
from classes_base import icon_css
M = {k: v['id'] for k, v in json.load(open('media-map.json')).items()}
CHECK = '<svg viewBox="0 0 24 24"><path d="M9 16.2 4.8 12l-1.4 1.4L9 19 21 7l-1.4-1.4z"/></svg>'
C = {
 'ico-check': icon_css(CHECK, 14),
 'dgc-about': 'flex-direction: column; gap: 0; padding: 120px 0; background: var(--mist); font-family: Manrope; @media(--mobile) { padding: 76px 0; }',
 'dgc-about-grid': 'display: grid; grid-template-columns: 1fr 1fr; grid-template-rows: auto; gap: 80px; align-items: center; @media(--tablet) { grid-template-columns: 1fr; gap: 56px; }',
 'dgc-collage': 'position: relative; padding: 0 60px 70px 0; isolation: isolate; @media(--tablet) { max-width: 560px; } @media(--mobile) { padding: 0 24px 50px 0; }',
 'dgc-collage-stripes': 'position: absolute; z-index: -1; right: 24px; top: -24px; width: 46%; height: 52%; padding: 0; border-radius: 10px; opacity: 0.55; background: repeating-linear-gradient(-45deg, #f6a440 0 2px, transparent 2px 12px);',
 'dgc-collage-main': 'padding: 0; overflow: hidden; border-radius: 10px; aspect-ratio: 4 / 4.6; box-shadow: 0 40px 60px -40px rgba(6,40,54,0.6);',
 'dgc-collage-small': 'position: absolute; right: 0; bottom: 0; width: 52%; padding: 0; overflow: hidden; border-radius: 10px; border: 8px solid var(--mist); aspect-ratio: 4 / 3; box-shadow: 0 30px 50px -30px rgba(6,40,54,0.6);',
 'dgc-since': 'position: absolute; left: -22px; top: 36px; width: auto; padding: 18px 22px; border-radius: 10px; background: var(--orange); color: var(--abyss); box-shadow: 0 24px 40px -20px rgba(6,40,54,0.8); @media(--mobile) { left: -6px; top: 18px; padding: 14px 16px; }',
 'dgc-since-year': 'display: block; font-family: Unbounded; font-size: 2.4rem; font-weight: 700; line-height: 1; color: var(--abyss); @media(--mobile) { font-size: 1.8rem; }',
 'dgc-since-txt': 'display: block; font-size: 0.82rem; font-weight: 700; color: var(--navy);',
 'dgc-ticks': 'flex-wrap: wrap; gap: 10px; margin-top: 26px; padding: 0;',
 'dgc-tick': 'display: flex; align-items: center; gap: 8px; width: auto; padding: 8px 14px 8px 8px; border-radius: 10px; background: #ffffff; border: 1px solid #dde8ea; font-size: 0.88rem; font-weight: 700; color: #181818;',
 'dgc-tick-ic': 'display: flex; align-items: center; justify-content: center; flex: none; width: 22px; height: 22px; padding: 0; border-radius: 50%; background: var(--orange); color: var(--abyss);',
 'dgc-svc-list': 'display: grid; grid-template-columns: 1fr 1fr; grid-template-rows: auto; gap: 0 18px; margin-top: 34px; padding: 0; border-top: 1px solid #dde8ea; @media(--mobile) { grid-template-columns: 1fr; }',
 'dgc-svc': 'display: flex; justify-content: space-between; align-items: center; gap: 10px; padding: 16px 4px; border-bottom: 1px solid #dde8ea; font-size: 1rem; font-weight: 700; color: #181818; text-decoration: none; transition: color 0.25s, padding 0.25s; &:hover { color: var(--orange-ink); padding: 16px 4px 16px 10px; }',
}
print('classes', mcp.upsert_classes(C))
link = lambda u: {'destination': u, 'isTargetBlank': False, 'tag': 'a'}
TICKS = ['17+ years of expertise', 'Visibility where customers search', 'Hands-on support']
SVC = [('ai-geo-optimization', 'AI & GEO Optimization'), ('google-business-profile', 'Google Business Profile'), ('seo-services', 'Search Engine Optimization'),
       ('google-ads-lsa', 'Google Ads & LSA'), ('website-development', 'Website Development'), ('social-media-marketing', 'Social Media Marketing')]
cfg, cls = {}, {}
ticks = ''
for i, t in enumerate(TICKS, 1):
    ticks += f'<e-flexbox configuration-id="Tick {i}"><e-flexbox configuration-id="Tick {i} Badge"><e-div-block configuration-id="Tick {i} Icon"></e-div-block></e-flexbox><e-paragraph configuration-id="Tick {i} Text"></e-paragraph></e-flexbox>'
    cls.update({f'Tick {i}': ['dgc-tick'], f'Tick {i} Badge': ['dgc-tick-ic'], f'Tick {i} Icon': ['ico-check']}); cfg[f'Tick {i} Text'] = {'paragraph': t, 'tag': 'span'}
svcs = ''
for i, (slug, t) in enumerate(SVC, 1):
    svcs += f'<e-flexbox configuration-id="Service {i}"><e-paragraph configuration-id="Service {i} Text"></e-paragraph><e-div-block configuration-id="Service {i} Icon"></e-div-block></e-flexbox>'
    cls.update({f'Service {i}': ['dgc-svc'], f'Service {i} Icon': ['ico-arrow-ur', 'dgc-svc-ic']})
    cfg.update({f'Service {i}': {'tag': 'a', 'link': link(f'https://digitalgrowthcatalyze.com/{slug}/')}, f'Service {i} Text': {'paragraph': html.escape(t), 'tag': 'span'}})
X = f'''<e-flexbox configuration-id="About"><e-grid configuration-id="About Grid">
 <e-div-block configuration-id="Collage">
  <e-div-block configuration-id="Collage Stripes"></e-div-block>
  <e-div-block configuration-id="Collage Main"><e-image configuration-id="Collage Main Photo"></e-image></e-div-block>
  <e-div-block configuration-id="Collage Small"><e-image configuration-id="Collage Small Photo"></e-image></e-div-block>
  <e-div-block configuration-id="Since Badge"><e-paragraph configuration-id="Since Year"></e-paragraph><e-paragraph configuration-id="Since Text"></e-paragraph></e-div-block>
 </e-div-block>
 <e-div-block configuration-id="About Copy">
  <e-paragraph configuration-id="About Kicker"></e-paragraph><e-heading configuration-id="About Title"></e-heading>
  <e-paragraph configuration-id="About Text 1"></e-paragraph><e-paragraph configuration-id="About Text 2"></e-paragraph>
  <e-flexbox configuration-id="Ticks">{ticks}</e-flexbox>
  <e-grid configuration-id="Service List">{svcs}</e-grid>
  <e-flexbox configuration-id="About Button"><e-paragraph configuration-id="About Button Text"></e-paragraph><e-div-block configuration-id="About Button Icon"></e-div-block></e-flexbox>
 </e-div-block>
</e-grid></e-flexbox>'''
cfg.update({
 'About': {'tag': 'section'},
 'Collage Main Photo': {'image': {'src': {'id': M['img/stock/team-laptops.jpg']}, 'size': 'full'}},
 'Collage Small Photo': {'image': {'src': {'id': M['img/stock/client-high-five.jpg']}, 'size': 'full'}},
 'Since Year': {'paragraph': '2009', 'tag': 'span'}, 'Since Text': {'paragraph': 'Growing local businesses since', 'tag': 'span'},
 'About Kicker': {'paragraph': 'About us', 'tag': 'span'}, 'About Title': {'tag': 'h2', 'title': 'Digital Growth <span>Catalyze</span> LLC'},
 'About Text 1': {'paragraph': 'We build the systems that put you in front of the right customers at the right moment. Google Ads that generate real calls. Local SEO that ranks you where buyers search. Websites that turn visitors into booked jobs.'},
 'About Text 2': {'paragraph': 'Since 2009 we’ve worked with local service businesses: towing, HVAC, cleaning, contracting and auto, on Google, Google Maps and the AI tools your customers now trust.'},
 'About Button': {'tag': 'a', 'link': link('https://digitalgrowthcatalyze.com/about-us/')}, 'About Button Text': {'paragraph': 'More about us', 'tag': 'span'},
})
cls.update({'About': ['dgc-about'], 'About Grid': ['dgc-wrap', 'dgc-about-grid'], 'Collage': ['dgc-collage'], 'Collage Stripes': ['dgc-collage-stripes'],
            'Collage Main': ['dgc-collage-main'], 'Collage Main Photo': ['dgc-cover'], 'Collage Small': ['dgc-collage-small'], 'Collage Small Photo': ['dgc-cover'],
            'Since Badge': ['dgc-since'], 'Since Year': ['dgc-since-year'], 'Since Text': ['dgc-since-txt'],
            'About Kicker': ['dgc-kicker'], 'About Title': ['dgc-h2'], 'About Text 1': ['dgc-sub'], 'About Text 2': ['dgc-sub'],
            'Ticks': ['dgc-ticks'], 'Service List': ['dgc-svc-list'],
            'About Button': ['dgc-btn', 'dgc-btn-hot-light'], 'About Button Icon': ['ico-arrow-ur']})
sty = {'About Copy': 'padding: 0;', 'About Text 1': 'margin-top: 18px;', 'About Text 2': 'margin-top: 12px;', 'About Button': 'margin-top: 34px;'}
mcp.upsert_classes({'dgc-svc-ic': 'transition: transform 0.25s;'})
r = mcp.put_section(126, 'About', 5, xml_structure=X, element_config=cfg, classes=cls, style=sty)
print(json.dumps({k: r.get(k) for k in ('success', 'warnings')}))
print([e.get('title') for e in mcp.call('elementor-get-page-structure', {'post_id': 126})['elements']])
