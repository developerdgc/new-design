import mcp, json, html
M = {k: v['id'] for k, v in json.load(open('media-map.json')).items()}
C = {
 'dgc-process': 'position: relative; overflow-x: clip; flex-direction: column; gap: 0; padding: 110px 0; font-family: Manrope; color: var(--fog); background: radial-gradient(38% 55% at 0% 0%, rgba(28,222,225,0.55), transparent 70%), radial-gradient(34% 50% at 100% 100%, rgba(28,222,225,0.45), transparent 70%), #062836; @media(--mobile) { padding: 76px 0; }',
 'dgc-process-grid': 'display: grid; grid-template-columns: 0.9fr 1.1fr; grid-template-rows: auto; gap: 64px; align-items: start; @media(--tablet) { grid-template-columns: 1fr; gap: 56px; }',
 'dgc-process-aside': 'position: sticky; top: 110px; padding: 0; @media(--tablet) { position: static; }',
 'dgc-kicker-dark': 'color: var(--orange);',
 'dgc-h2': 'display: block; margin-top: 16px; font-family: Unbounded; font-size: clamp(1.9rem, 4.2vw, 3.3rem); font-weight: 700; line-height: 1.08; letter-spacing: -0.025em; color: var(--ink);',
 'dgc-h2-dark': 'color: #ffffff;',
 'dgc-sub': 'display: block; max-width: 54ch; margin-top: 16px; font-family: Manrope; font-size: 1.04rem; line-height: 1.7; color: #181818;',
 'dgc-sub-dark': 'color: var(--fog);',
 'dgc-process-img': 'position: relative; margin-top: 34px; padding: 0; overflow: hidden; border-radius: 10px; aspect-ratio: 4 / 3;',
 'dgc-cover': 'display: block; width: 100%; height: 100%; object-fit: cover;',
 'dgc-process-cap': 'position: absolute; z-index: 1; left: 22px; right: 22px; bottom: 18px; display: flex; align-items: center; gap: 10px; font-family: Manrope; font-size: 1rem; font-weight: 700; line-height: 1.5; color: #ffffff;',
 'dgc-steps': 'flex-direction: column; gap: 0; padding: 0; border-top: 1px solid rgba(255,255,255,0.09);',
 'dgc-step': 'display: grid; grid-template-columns: 74px 1fr; grid-template-rows: auto; gap: 20px; padding: 30px 0; border-bottom: 1px solid rgba(255,255,255,0.09); transition: background 0.3s; @media(--mobile) { grid-template-columns: 56px 1fr; }',
 'dgc-step-n': 'display: block; font-family: Unbounded; font-size: 2.4rem; font-weight: 800; line-height: 1; color: transparent; -webkit-text-stroke: 1px rgba(246,164,64,0.75); transition: color 0.35s; @media(--mobile) { font-size: 1.9rem; }',
 'dgc-step-body': 'padding: 0; min-width: 0;',
 'dgc-step-h': 'display: block; font-family: Unbounded; font-size: 1.3rem; font-weight: 700; line-height: 1.08; color: #ffffff;',
 'dgc-step-p': 'display: block; margin-top: 8px; font-family: Manrope; font-size: 1rem; line-height: 1.7; color: var(--fog);',
 'dgc-chips': 'flex-wrap: wrap; gap: 8px; margin-top: 16px; padding: 0;',
 'dgc-chip': 'display: inline-block; padding: 6px 12px; border-radius: 10px; background: rgba(246,164,64,0.1); border: 1px solid rgba(246,164,64,0.3); font-family: Manrope; font-size: 0.78rem; font-weight: 700; line-height: 1.4; color: #ffd9a8;',
}
print('classes', mcp.upsert_classes(C))
STEPS = [('Discover', 'We study your market, your competitors and the jobs you want more of.', ['Competitor check', 'Keyword research']),
         ('Design', 'A brand, website and ads that look and sound like your business.', ['Logo & branding', 'Website design']),
         ('Build', 'Fast website, Google Business Profile and ad campaigns set up to win calls.', ['Website build', 'GBP & Ads setup']),
         ('Launch & grow', 'We go live, then keep improving your rankings, reviews and ads.', ['Local SEO', 'Google Ads & LSA'])]
cfg, cls = {}, {}
steps = ''
for i, (h, p, chips) in enumerate(STEPS, 1):
    s = f'Step {i}'
    ch = ''.join(f'<e-paragraph configuration-id="{s} Chip {k}"></e-paragraph>' for k in range(len(chips)))
    steps += (f'<e-grid configuration-id="{s}"><e-paragraph configuration-id="{s} Number"></e-paragraph><e-div-block configuration-id="{s} Body">'
              f'<e-heading configuration-id="{s} Title"></e-heading><e-paragraph configuration-id="{s} Text"></e-paragraph><e-flexbox configuration-id="{s} Chips">{ch}</e-flexbox></e-div-block></e-grid>')
    cls.update({s: ['dgc-step'], f'{s} Number': ['dgc-step-n'], f'{s} Body': ['dgc-step-body'], f'{s} Title': ['dgc-step-h'], f'{s} Text': ['dgc-step-p'], f'{s} Chips': ['dgc-chips']})
    cfg.update({f'{s} Number': {'paragraph': f'0{i}', 'tag': 'span'}, f'{s} Title': {'tag': 'h3', 'title': html.escape(h)}, f'{s} Text': {'paragraph': p}})
    for k, c in enumerate(chips):
        cls[f'{s} Chip {k}'] = ['dgc-chip']; cfg[f'{s} Chip {k}'] = {'paragraph': c, 'tag': 'span'}
X = f'''<e-flexbox configuration-id="How We Work"><e-grid configuration-id="Process Grid">
 <e-div-block configuration-id="Process Aside">
  <e-paragraph configuration-id="Process Kicker"></e-paragraph><e-heading configuration-id="Process Title"></e-heading><e-paragraph configuration-id="Process Sub"></e-paragraph>
  <e-div-block configuration-id="Process Image"><e-image configuration-id="Process Photo"></e-image><e-div-block configuration-id="Process Shade"></e-div-block><e-paragraph configuration-id="Process Caption"></e-paragraph></e-div-block>
 </e-div-block>
 <e-flexbox configuration-id="Steps">{steps}</e-flexbox>
</e-grid></e-flexbox>'''
cfg.update({'How We Work': {'tag': 'section'}, 'Process Kicker': {'paragraph': 'How we work', 'tag': 'span'},
            'Process Title': {'tag': 'h2', 'title': 'Four steps. <span>One goal:</span> more calls.'},
            'Process Sub': {'paragraph': 'One dedicated team plans, builds and grows your whole online presence.'},
            'Process Photo': {'image': {'src': {'id': M['img/stock/planning-wall.jpg']}, 'size': 'full'}},
            'Process Caption': {'paragraph': 'Every project is planned around how your customers search and call'}})
cls.update({'How We Work': ['dgc-process'], 'Process Grid': ['dgc-wrap', 'dgc-process-grid'], 'Process Aside': ['dgc-process-aside'],
            'Process Kicker': ['dgc-kicker', 'dgc-kicker-dark'], 'Process Title': ['dgc-h2', 'dgc-h2-dark', 'dgc-h2-orange'], 'Process Sub': ['dgc-sub', 'dgc-sub-dark'],
            'Process Image': ['dgc-process-img'], 'Process Photo': ['dgc-cover'], 'Process Caption': ['dgc-process-cap'], 'Steps': ['dgc-steps']})
sty = {'Process Shade': 'position: absolute; inset: 0; padding: 0; background: linear-gradient(to top, rgba(2,23,32,0.85), transparent 55%);'}
mcp.upsert_classes({'dgc-h2-orange': 'min-width: 0;'})
r = mcp.put_section(126, 'How We Work', 4, xml_structure=X, element_config=cfg, classes=cls, style=sty)
print(json.dumps({k: r.get(k) for k in ('success', 'warnings')}))
print([e.get('title') for e in mcp.call('elementor-get-page-structure', {'post_id': 126})['elements']])
