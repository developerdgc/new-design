import mcp, json
from classes_base import icon_css
M = {k: v['id'] for k, v in json.load(open('media-map.json')).items()}
ARROW_UR = '<svg viewBox="0 0 24 24"><path d="M7 17 17 7M9 7h8v8"/></svg>'
STAR = '<svg viewBox="0 0 24 24"><path d="M12 17.3 18.2 21l-1.6-7L22 9.2l-7.2-.6L12 2 9.2 8.6 2 9.2 7.4 14l-1.6 7z"/></svg>'
C = {
 'ico-arrow-ur': icon_css(ARROW_UR, 16, stroke=True),
 'ico-star': icon_css(STAR, 19),
 'dgc-wrap': 'max-width: 1288px; width: 100%; margin: 0 auto; padding: 0 24px; @media(--mobile) { padding: 0 16px; }',
 'dgc-btn': 'display: inline-flex; align-items: center; gap: 10px; width: auto; padding: 15px 26px; border-radius: 10px; font-family: Manrope; font-size: 0.95rem; font-weight: 700; line-height: 1; white-space: nowrap; text-decoration: none; cursor: pointer; transition: transform 0.25s, background 0.25s, color 0.25s, border-color 0.25s, box-shadow 0.25s;',
 'dgc-btn-orange': 'border: 1.5px solid transparent; background: var(--orange); color: var(--abyss); box-shadow: 0 10px 30px -10px rgba(246,164,64,0.7); &:hover { transform: translateY(-2px); background: #ffffff; color: var(--navy); }',
 'dgc-btn-ghost': 'background: transparent; border: 1.5px solid rgba(255,255,255,0.22); color: #ffffff; &:hover { background: var(--cyan); border: 1.5px solid var(--cyan); color: var(--abyss); }',
 'dgc-btn-glass': 'background: rgba(255,255,255,0.06); border: 1.5px solid rgba(255,255,255,0.3); color: #ffffff; backdrop-filter: blur(6px); &:hover { background: #22c8cc; border: 1.5px solid #22c8cc; color: var(--abyss); }',
 'dgc-hero': 'position: relative; overflow: hidden; flex-direction: column; padding: 210px 0 56px; background: radial-gradient(55% 75% at 0% 0%, rgba(251,142,40,0.55), transparent 62%), radial-gradient(50% 70% at 100% 100%, rgba(34,200,204,0.55), transparent 62%), radial-gradient(40% 50% at 75% 20%, rgba(34,200,204,0.18), transparent 70%), linear-gradient(-60deg, #0b4250 0%, #062836 55%, #041d28 100%); color: var(--fog); font-family: Manrope; @media(--tablet) { padding: 190px 0 48px; } @media(--mobile) { padding: 170px 0 40px; }',
 'dgc-dots-hero': 'position: absolute; inset: 0; padding: 0; pointer-events: none; background-image: radial-gradient(rgba(255,255,255,0.12) 1px, transparent 1px); background-size: 26px 26px; -webkit-mask-image: radial-gradient(ellipse 70% 60% at 30% 40%, #000 30%, transparent 75%); mask-image: radial-gradient(ellipse 70% 60% at 30% 40%, #000 30%, transparent 75%);',
 'dgc-hero-line': 'position: absolute; left: 0; right: 0; bottom: 0; height: 3px; padding: 0; background: linear-gradient(90deg, #fb8e28, #22c8cc);',
 'dgc-hero-grid': 'position: relative; z-index: 1; grid-template-columns: 1.05fr 0.95fr; grid-template-rows: auto; gap: 40px; align-items: center; @media(--tablet) { grid-template-columns: 1fr; gap: 56px; }',
 'dgc-rate': 'display: inline-flex; align-items: center; gap: 12px; width: auto; padding: 6px 16px 6px 6px; border-radius: 10px; border: 1px solid rgba(255,255,255,0.09); background: rgba(255,255,255,0.06); font-size: 0.84rem; color: #dbe8eb;',
 'dgc-face': 'display: grid; place-items: center; width: 30px; height: 30px; margin-left: -8px; border-radius: 50%; border: 2px solid var(--navy); font-family: Manrope; font-size: 0.74rem; font-weight: 800; color: var(--abyss);',
 'dgc-hero-h1': 'display: block; margin-top: 22px; font-family: Unbounded; font-size: clamp(2.3rem, 4.6vw, 4.1rem); font-weight: 700; line-height: 1.04; letter-spacing: -0.035em; text-transform: capitalize; color: #ffffff;',
 'dgc-hero-lead': 'display: block; margin-top: 22px; max-width: 46ch; font-family: Manrope; font-size: 1.06rem; line-height: 1.7; color: #dcebef;',
 'dgc-show': 'position: relative; height: 470px; padding: 0; @media(--tablet) { height: 460px; max-width: 640px; margin: 0 auto; } @media(--mobile) { height: 380px; }',
 'dgc-screen': 'position: absolute; padding: 0; border-radius: 10px; overflow: hidden; background: #ffffff; box-shadow: 0 40px 80px -30px rgba(0,0,0,0.7), 0 0 0 1px rgba(255,255,255,0.08);',
 'dgc-screen-bar': 'display: flex; align-items: center; gap: 5px; height: 24px; padding: 0 10px; background: #f1f5f6;',
 'dgc-dot': 'width: 7px; height: 7px; min-width: 0; padding: 0; border-radius: 50%; background: #cbd8dc;',
 'dgc-pan': 'display: block; width: 100%; height: calc(100% - 24px); object-fit: cover; object-position: top;',
 'dgc-badge': 'position: absolute; z-index: 6; left: -18px; top: -14px; display: flex; align-items: center; justify-content: center; width: 132px; height: 132px; padding: 0; border-radius: 50%; background: var(--orange); color: var(--abyss); text-decoration: none; box-shadow: 0 20px 40px -18px rgba(246,164,64,0.9); @media(--mobile) { width: 104px; height: 104px; left: -4px; top: auto; bottom: 70px; }',
 'dgc-spin': 'position: absolute; inset: 0; width: 100%; height: 100%;',
 'dgc-float': 'position: absolute; z-index: 5; display: flex; align-items: center; gap: 12px; width: auto; padding: 11px 15px; border-radius: 10px; background: rgba(4,32,44,0.82); backdrop-filter: blur(10px); border: 1px solid rgba(255,255,255,0.09); box-shadow: 0 20px 40px -20px rgba(0,0,0,0.6); color: #ffffff;',
 'dgc-bob': 'will-change: transform;',
 'dgc-float-ic': 'display: flex; align-items: center; justify-content: center; width: 36px; height: 36px; padding: 0; border-radius: 10px; background: var(--orange); color: var(--abyss);',
}
print('dups removed', len(mcp.drop_dups())); print('classes', mcp.upsert_classes(C))

link = lambda u, blank=False: {'destination': u, 'isTargetBlank': blank, 'tag': 'a'}
img = lambda key: {'src': {'id': M[key]}, 'size': 'full'}
def screen(n):
    return f'<e-div-block configuration-id="Screen {n}"><e-flexbox configuration-id="Screen {n} Bar"><e-div-block configuration-id="Screen {n} Dot 1"></e-div-block><e-div-block configuration-id="Screen {n} Dot 2"></e-div-block><e-div-block configuration-id="Screen {n} Dot 3"></e-div-block></e-flexbox><e-image configuration-id="Screen {n} Image"></e-image></e-div-block>'
X = f'''<e-flexbox configuration-id="Hero">
 <e-div-block configuration-id="Hero Dots"></e-div-block>
 <e-div-block configuration-id="Hero Line"></e-div-block>
 <e-grid configuration-id="Hero Grid">
  <e-div-block configuration-id="Hero Copy">
   <e-flexbox configuration-id="Rating Pill">
    <e-flexbox configuration-id="Faces"><e-paragraph configuration-id="Face B"></e-paragraph><e-paragraph configuration-id="Face D"></e-paragraph><e-paragraph configuration-id="Face J"></e-paragraph><e-paragraph configuration-id="Face N"></e-paragraph></e-flexbox>
    <e-paragraph configuration-id="Stars"></e-paragraph>
    <e-paragraph configuration-id="Rating Text"></e-paragraph>
   </e-flexbox>
   <e-heading configuration-id="Hero Title"></e-heading>
   <e-paragraph configuration-id="Hero Lead"></e-paragraph>
   <e-flexbox configuration-id="Hero Buttons">
    <e-flexbox configuration-id="See The Work"><e-paragraph configuration-id="See The Work Text"></e-paragraph><e-div-block configuration-id="See The Work Icon"></e-div-block></e-flexbox>
    <e-flexbox configuration-id="Free Quote"><e-paragraph configuration-id="Free Quote Text"></e-paragraph></e-flexbox>
   </e-flexbox>
  </e-div-block>
  <e-div-block configuration-id="Hero Showcase">
   <e-div-block configuration-id="Show">
    <e-flexbox configuration-id="Badge"><e-image configuration-id="Badge Ring"></e-image><e-paragraph configuration-id="Badge Arrow"></e-paragraph></e-flexbox>
    {screen('B')}{screen('C')}{screen('A')}
    <e-flexbox configuration-id="Years Card"><e-flexbox configuration-id="Years Icon"><e-div-block configuration-id="Years Star"></e-div-block></e-flexbox><e-div-block configuration-id="Years Copy"><e-paragraph configuration-id="Years Number"></e-paragraph><e-paragraph configuration-id="Years Label"></e-paragraph></e-div-block></e-flexbox>
   </e-div-block>
   <e-flexbox configuration-id="Show CTA"><e-flexbox configuration-id="All Web Projects"><e-paragraph configuration-id="All Web Projects Text"></e-paragraph><e-div-block configuration-id="All Web Projects Icon"></e-div-block></e-flexbox></e-flexbox>
  </e-div-block>
 </e-grid>
</e-flexbox>'''
cfg = {
 'Hero': {'tag': 'section'},
 'Face B': {'paragraph': 'B', 'tag': 'span'}, 'Face D': {'paragraph': 'D', 'tag': 'span'}, 'Face J': {'paragraph': 'J', 'tag': 'span'}, 'Face N': {'paragraph': 'N', 'tag': 'span'},
 'Stars': {'paragraph': '★★★★★', 'tag': 'span'}, 'Rating Text': {'paragraph': '<b>5.0 Star Ratings</b>', 'tag': 'span'},
 'Hero Title': {'tag': 'h1', 'title': 'Marketing That Makes The <span>Phone</span> <span>Ring.</span>'},
 'Hero Lead': {'paragraph': 'Websites, Local SEO, Google Ads and branding for towing, cleaning, contracting and limo companies across the USA. One team that turns searches into booked jobs.'},
 'See The Work': {'tag': 'a', 'link': link('#work')}, 'See The Work Text': {'paragraph': 'See the work', 'tag': 'span'},
 'Free Quote': {'tag': 'a', 'link': link('https://digitalgrowthcatalyze.com/contact-us/')}, 'Free Quote Text': {'paragraph': 'Get a Free Quote', 'tag': 'span'},
 'Badge': {'tag': 'a', 'link': link('#work')}, 'Badge Ring': {'image': img('generated/hero-badge-ring')}, 'Badge Arrow': {'paragraph': '↓', 'tag': 'span'},
 'Screen A Image': {'image': img('img/work/exotic-cars.jpg')}, 'Screen B Image': {'image': img('img/work/orange-county-towing.jpg')}, 'Screen C Image': {'image': img('img/work/black-n-black.jpg')},
 'Years Number': {'paragraph': '17+', 'tag': 'span'}, 'Years Label': {'paragraph': 'years in digital', 'tag': 'span'},
 'All Web Projects': {'tag': 'a', 'link': link('#work-websites')}, 'All Web Projects Text': {'paragraph': 'See All Web Projects', 'tag': 'span'},
}
cls = {
 'Hero': ['dgc-hero'], 'Hero Dots': ['dgc-dots-hero'], 'Hero Line': ['dgc-hero-line'], 'Hero Grid': ['dgc-wrap', 'dgc-hero-grid'],
 'Rating Pill': ['dgc-rate'], 'Face B': ['dgc-face'], 'Face D': ['dgc-face'], 'Face J': ['dgc-face'], 'Face N': ['dgc-face'],
 'Hero Title': ['dgc-hero-h1'], 'Hero Lead': ['dgc-hero-lead'],
 'See The Work': ['dgc-btn', 'dgc-btn-orange'], 'See The Work Icon': ['ico-arrow-ur'], 'Free Quote': ['dgc-btn', 'dgc-btn-ghost'],
 'Show': ['dgc-show'], 'Badge': ['dgc-badge'], 'Badge Ring': ['dgc-spin'],
 'Years Card': ['dgc-float', 'dgc-bob'], 'Years Icon': ['dgc-float-ic'], 'Years Star': ['ico-star'],
 'All Web Projects': ['dgc-btn', 'dgc-btn-glass'], 'All Web Projects Icon': ['ico-arrow-ur'],
}
for n in 'ABC':
    cls[f'Screen {n}'] = ['dgc-screen']; cls[f'Screen {n} Bar'] = ['dgc-screen-bar']; cls[f'Screen {n} Image'] = ['dgc-pan']
    for d in '123': cls[f'Screen {n} Dot {d}'] = ['dgc-dot']
sty = {
 'Hero Grid': 'display: grid;', 'Hero Copy': 'padding: 0;', 'Hero Showcase': 'padding: 0;',
 'Faces': 'width: auto; padding: 0 0 0 8px; gap: 0;',
 'Face B': 'background: #1cdee1;', 'Face D': 'background: #f6a440;', 'Face J': 'background: #9ff6f7;', 'Face N': 'background: #ffd29a;',
 'Stars': 'color: var(--orange); letter-spacing: 2px; font-size: 0.9rem;', 'Rating Text': 'color: #ffffff;',
 'Hero Buttons': 'flex-wrap: wrap; gap: 12px; margin-top: 30px; padding: 0;',
 'Badge Arrow': 'position: relative; font-family: Unbounded; font-size: 1.5rem; font-weight: 700; line-height: 1;',
 'Screen A': 'width: 56%; height: 400px; left: 22%; top: 24px; z-index: 3; @media(--mobile) { width: 70%; left: 15%; height: 340px; }',
 'Screen B': 'width: 42%; height: 320px; left: 0; top: 100px; z-index: 2; transform: rotate(-5deg); opacity: 0.92; @media(--mobile) { width: 52%; height: 260px; }',
 'Screen C': 'width: 42%; height: 320px; right: 0; top: 76px; z-index: 1; transform: rotate(5deg); opacity: 0.92; @media(--mobile) { width: 52%; height: 260px; }',
 'Screen A Dot 1': 'background: #ff6b5f;', 'Screen A Dot 2': 'background: #f6a440;', 'Screen A Dot 3': 'background: #3ccf6e;',
 'Screen B Dot 1': 'background: #ff6b5f;', 'Screen B Dot 2': 'background: #f6a440;', 'Screen B Dot 3': 'background: #3ccf6e;',
 'Screen C Dot 1': 'background: #ff6b5f;', 'Screen C Dot 2': 'background: #f6a440;', 'Screen C Dot 3': 'background: #3ccf6e;',
 'Years Card': 'right: -4px; top: 0; @media(--mobile) { right: 0; }',
 'Years Copy': 'padding: 0; min-width: 0;',
 'Years Number': 'display: block; font-family: Unbounded; font-size: 1.25rem; font-weight: 700; line-height: 1;',
 'Years Label': 'display: block; font-size: 0.72rem; line-height: 1.3; color: var(--fog);',
 'Show CTA': 'justify-content: center; margin-top: 26px; padding: 0; position: relative; z-index: 6;',
}
r = mcp.call('elementor-build-composition', {'post_id': 126, 'xml_structure': X, 'element_config': cfg, 'classes': cls, 'style': sty, 'parent_id': 'document', 'mode': 'replace_children'})
print(json.dumps({k: r.get(k) for k in ('success', 'warnings', 'root_element_ids')})[:1500])
print(json.dumps(mcp.call('elementor-publish-document', {'post_id': 126}))[:150])
