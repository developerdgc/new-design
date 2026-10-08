import mcp, json, html
M = {k: v['id'] for k, v in json.load(open('media-map.json')).items()}
SITE = 'https://newportfolio.digitalgrowthcatalyze.com'
link = lambda u: {'destination': u, 'isTargetBlank': False, 'tag': 'a'}
C = {
 'dgc-reviews': 'flex-direction: column; gap: 0; padding: 100px 0; background: var(--navy); color: var(--fog); font-family: Manrope; @media(--mobile) { padding: 76px 0; }',
 'dgc-reviews-head': 'display: flex; justify-content: space-between; align-items: flex-end; flex-wrap: wrap; gap: 28px;',
 'dgc-reviews-side': 'display: flex; align-items: center; flex-wrap: wrap; gap: 14px; width: auto; padding: 0;',
 'dgc-score': 'display: inline-flex; align-items: center; gap: 16px; width: auto; padding: 14px 20px; border-radius: 10px; border: 1px solid rgba(255,255,255,0.09); background: rgba(255,255,255,0.03);',
 'dgc-score-num': 'display: block; font-family: Unbounded; font-size: 2.2rem; font-weight: 700; line-height: 1; color: var(--orange);',
 'dgc-stars': 'display: block; color: var(--orange); letter-spacing: 2px; font-size: 0.9rem; line-height: 1.4;',
 'dgc-score-small': 'display: block; font-size: 0.84rem; color: var(--fog);',
 'dgc-quotes': 'display: grid; grid-template-columns: repeat(3, 1fr); grid-template-rows: auto; gap: 20px; margin-top: 48px; padding: 0; @media(--tablet) { grid-template-columns: 1fr; max-width: 640px; }',
 'dgc-quote': 'position: relative; display: flex; flex-direction: column; gap: 0; padding: 28px; border-radius: 10px; background: var(--navy-3); border: 1px solid rgba(255,255,255,0.09); transition: transform 0.3s, border-color 0.3s; &:hover { transform: translateY(-4px); border: 1px solid rgba(28,222,225,0.4); }',
 'dgc-quote-text': 'display: block; margin-top: 12px; font-family: Manrope; font-size: 0.95rem; line-height: 1.7; color: #d3e2e6;',
 'dgc-quote-by': 'display: flex; align-items: center; gap: 12px; margin-top: auto; padding: 20px 0 0;',
 'dgc-avatar': 'display: flex; align-items: center; justify-content: center; flex: none; width: 40px; height: 40px; border-radius: 50%; background: var(--cyan); color: var(--abyss); font-family: Manrope; font-weight: 800;',
 'dgc-avatar-orange': 'background: var(--orange);',
 'dgc-quote-name': 'display: block; font-family: Manrope; font-size: 1rem; font-weight: 700; line-height: 1.3; color: #ffffff; overflow-wrap: anywhere;',
 'dgc-quote-src': 'display: block; font-size: 0.78rem; color: var(--fog);',
 'dgc-cta': 'flex-direction: column; gap: 0; padding: 72px 0; background: #ffffff; font-family: Manrope; @media(--mobile) { padding: 76px 0; }',
 'dgc-cta-box': 'position: relative; overflow: hidden; isolation: isolate; display: grid; grid-template-columns: 1fr auto; grid-template-rows: auto; align-items: center; gap: 40px; padding: 40px 48px; border-radius: 10px; background: var(--orange); color: var(--navy); box-shadow: 0 30px 60px -40px rgba(246,164,64,0.9); @media(--tablet) { grid-template-columns: 1fr; gap: 28px; padding: 32px 24px; }',
 'dgc-cta-mark': 'position: absolute; z-index: -1; right: 2%; top: -70px; width: 230px; height: auto; pointer-events: none; opacity: 0.09; filter: brightness(0); transform: rotate(-14deg);',
 'dgc-kicker-navy': 'color: var(--navy);',
 'dgc-cta-h': 'display: block; margin-top: 10px; font-family: Unbounded; font-size: clamp(1.7rem, 3.4vw, 2.7rem); font-weight: 700; line-height: 1.08; letter-spacing: -0.03em; color: var(--abyss);',
 'dgc-cta-p': 'display: block; margin-top: 8px; font-family: Manrope; font-size: 1rem; font-weight: 600; line-height: 1.7; color: var(--navy);',
 'dgc-cta-btns': 'flex-wrap: wrap; gap: 12px; width: auto; padding: 0;',
 'dgc-btn-ink': 'border: 1.5px solid transparent; background: var(--navy); color: #ffffff; &:hover { background: #ffffff; color: var(--navy); }',
 'dgc-btn-line': 'border: 1.5px solid var(--navy); background: transparent; color: var(--navy); &:hover { background: var(--navy); color: #ffffff; }',
}
print('classes', mcp.upsert_classes(C))
mcp.prioritize(['dgc-avatar-orange', 'dgc-kicker-navy', 'dgc-btn-ink', 'dgc-btn-line', 'dgc-kicker-dark', 'dgc-h2-dark', 'dgc-sub-dark', 'dgc-go-off', 'dgc-lcard-panel', 'dgc-lsheet-panel', 'dgc-subfilters-grid', 'dgc-btn-orange', 'dgc-btn-ghost', 'dgc-btn-glass', 'dgc-btn-hot-light'])
REVIEWS = [('Jamaul Erskine', 'Digital Growth Catalyze LLC has been amazing for my towing business. Thanks to their efforts, I’m getting more calls and leads than ever before. Highly recommend them for any business looking to boost their online presence.'),
           ('Benjamin Keshishyan', 'This company has been a great help in growing my business. They helped me increase my calls and brought in more customers. Their service is professional, effective, and results-driven. Highly recommended for anyone looking to grow their customer base.'),
           ('McDowell’s Landscaping', 'David at Digital Growth Catalyze designed our new logo and built an awesome Google Business Profile. He was highly professional, patient, and great to work with. Thanks to DGC, our business profile is now being optimized too!')]
cfg, cls = {}, {}
q = ''
for i, (name, text) in enumerate(REVIEWS, 1):
    p = f'Review {i}'
    q += (f'<e-flexbox configuration-id="{p}"><e-paragraph configuration-id="{p} Stars"></e-paragraph><e-paragraph configuration-id="{p} Text"></e-paragraph>'
          f'<e-flexbox configuration-id="{p} By"><e-paragraph configuration-id="{p} Avatar"></e-paragraph><e-div-block configuration-id="{p} Who"><e-paragraph configuration-id="{p} Name"></e-paragraph><e-paragraph configuration-id="{p} Source"></e-paragraph></e-div-block></e-flexbox></e-flexbox>')
    cls.update({p: ['dgc-quote'], f'{p} Stars': ['dgc-stars'], f'{p} Text': ['dgc-quote-text'], f'{p} By': ['dgc-quote-by'], f'{p} Avatar': ['dgc-avatar'] + (['dgc-avatar-orange'] if i % 2 else []),
                f'{p} Name': ['dgc-quote-name'], f'{p} Source': ['dgc-quote-src']})
    cfg.update({p: {'tag': 'article'}, f'{p} Stars': {'paragraph': '★★★★★', 'tag': 'span'}, f'{p} Text': {'paragraph': html.escape(text)},
                f'{p} Avatar': {'paragraph': name[0], 'tag': 'span'}, f'{p} Name': {'paragraph': html.escape(name), 'tag': 'span'}, f'{p} Source': {'paragraph': 'Google review', 'tag': 'span'}})
XR = f'''<e-flexbox configuration-id="Testimonials"><e-div-block configuration-id="Testimonials Wrap">
 <e-flexbox configuration-id="Testimonials Head">
  <e-div-block configuration-id="Testimonials Title Block"><e-paragraph configuration-id="Testimonials Kicker"></e-paragraph><e-heading configuration-id="Testimonials Title"></e-heading></e-div-block>
  <e-flexbox configuration-id="Testimonials Side">
   <e-flexbox configuration-id="Video Reviews Button"><e-paragraph configuration-id="Video Reviews Button Text"></e-paragraph><e-div-block configuration-id="Video Reviews Button Icon"></e-div-block></e-flexbox>
   <e-flexbox configuration-id="Score"><e-paragraph configuration-id="Score Number"></e-paragraph><e-div-block configuration-id="Score Detail"><e-paragraph configuration-id="Score Stars"></e-paragraph><e-paragraph configuration-id="Score Count"></e-paragraph></e-div-block></e-flexbox>
  </e-flexbox>
 </e-flexbox>
 <e-grid configuration-id="Reviews Grid">{q}</e-grid>
</e-div-block></e-flexbox>'''
cfg.update({'Testimonials': {'tag': 'section'}, 'Testimonials Kicker': {'paragraph': 'Testimonials', 'tag': 'span'}, 'Testimonials Title': {'tag': 'h2', 'title': 'Real owners. <span>Real results.</span>'},
            'Video Reviews Button': {'tag': 'a', 'link': link(SITE + '/video-reviews/')}, 'Video Reviews Button Text': {'paragraph': 'View Video Reviews', 'tag': 'span'},
            'Score Number': {'paragraph': '5.0', 'tag': 'span'}, 'Score Stars': {'paragraph': '★★★★★', 'tag': 'span'}, 'Score Count': {'paragraph': '13 Google reviews', 'tag': 'span'}})
cls.update({'Testimonials': ['dgc-reviews'], 'Testimonials Wrap': ['dgc-wrap'], 'Testimonials Head': ['dgc-reviews-head'], 'Testimonials Kicker': ['dgc-kicker', 'dgc-kicker-cyan'],
            'Testimonials Title': ['dgc-h2', 'dgc-h2-dark', 'dgc-h2-cyan'], 'Testimonials Side': ['dgc-reviews-side'],
            'Video Reviews Button': ['dgc-btn', 'dgc-btn-orange'], 'Video Reviews Button Icon': ['ico-arrow-ur'],
            'Score': ['dgc-score'], 'Score Number': ['dgc-score-num'], 'Score Stars': ['dgc-stars'], 'Score Count': ['dgc-score-small'], 'Reviews Grid': ['dgc-quotes']})
sty = {'Testimonials Title Block': 'padding: 0; width: auto;', 'Score Detail': 'padding: 0;'}
mcp.upsert_classes({'dgc-kicker-cyan': 'color: var(--cyan);', 'dgc-h2-cyan': 'min-width: 0;'})
mcp.prioritize(['dgc-kicker-cyan'])
r = mcp.put_section(126, 'Testimonials', 6, xml_structure=XR, element_config=cfg, classes=cls, style=sty)
print('testimonials', r.get('success'), r.get('warnings'))
XC = '''<e-flexbox configuration-id="CTA"><e-div-block configuration-id="CTA Wrap"><e-grid configuration-id="CTA Box">
 <e-image configuration-id="CTA Watermark"></e-image>
 <e-div-block configuration-id="CTA Copy"><e-paragraph configuration-id="CTA Kicker"></e-paragraph><e-heading configuration-id="CTA Title"></e-heading><e-paragraph configuration-id="CTA Text"></e-paragraph></e-div-block>
 <e-flexbox configuration-id="CTA Buttons">
  <e-flexbox configuration-id="CTA Quote"><e-paragraph configuration-id="CTA Quote Text"></e-paragraph><e-div-block configuration-id="CTA Quote Icon"></e-div-block></e-flexbox>
  <e-flexbox configuration-id="CTA Call"><e-paragraph configuration-id="CTA Call Text"></e-paragraph></e-flexbox>
 </e-flexbox>
</e-grid></e-div-block></e-flexbox>'''
cfgc = {'CTA': {'tag': 'section'}, 'CTA Watermark': {'image': {'src': {'id': M['img/brand/dgc-mark-white.png']}, 'size': 'full'}},
        'CTA Kicker': {'paragraph': 'Let’s grow together', 'tag': 'span'}, 'CTA Title': {'tag': 'h2', 'title': 'Ready for more calls?'},
        'CTA Text': {'paragraph': 'Website, SEO, Google Ads or all three. Tell us where you want to grow.'},
        'CTA Quote': {'tag': 'a', 'link': link('https://digitalgrowthcatalyze.com/contact-us/')}, 'CTA Quote Text': {'paragraph': 'Get a Free Quote', 'tag': 'span'},
        'CTA Call': {'tag': 'a', 'link': link('tel:+18482062002')}, 'CTA Call Text': {'paragraph': 'Call +1 848-206-2002', 'tag': 'span'}}
clsc = {'CTA': ['dgc-cta'], 'CTA Wrap': ['dgc-wrap'], 'CTA Box': ['dgc-cta-box'], 'CTA Watermark': ['dgc-cta-mark'], 'CTA Kicker': ['dgc-kicker', 'dgc-kicker-navy'],
        'CTA Title': ['dgc-cta-h'], 'CTA Text': ['dgc-cta-p'], 'CTA Buttons': ['dgc-cta-btns'], 'CTA Quote': ['dgc-btn', 'dgc-btn-ink'], 'CTA Quote Icon': ['ico-arrow-ur'], 'CTA Call': ['dgc-btn', 'dgc-btn-line']}
r = mcp.put_section(126, 'CTA', 7, xml_structure=XC, element_config=cfgc, classes=clsc, style={'CTA Copy': 'padding: 0;'})
print('cta', r.get('success'), r.get('warnings'))
print([e.get('title') for e in mcp.call('elementor-get-page-structure', {'post_id': 126})['elements']])
