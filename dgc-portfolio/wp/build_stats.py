import mcp, json
from classes_base import icon_css
I = {
 'monitor': '<svg viewBox="0 0 24 24"><rect x="3" y="4" width="18" height="14" rx="2"/><path d="M3 8h18M8 21h8M12 18v3"/></svg>',
 'layers': '<svg viewBox="0 0 24 24"><path d="M12 3 3 8l9 5 9-5z"/><path d="m3 13 9 5 9-5"/></svg>',
 'doc': '<svg viewBox="0 0 24 24"><path d="M7 3h7l5 5v13H7z"/><path d="M14 3v5h5M10 13h6M10 17h6"/></svg>',
 'calendar': '<svg viewBox="0 0 24 24"><rect x="3" y="5" width="18" height="16" rx="2"/><path d="M3 10h18M8 3v4M16 3v4"/></svg>',
 'star-o': '<svg viewBox="0 0 24 24"><path d="M12 3l2.7 5.6 6.1.9-4.4 4.3 1 6.1L12 17l-5.4 2.9 1-6.1L3.2 9.5l6.1-.9z"/></svg>',
}
C = {f'ico-{k}': icon_css(v, 24, True, 1.9) for k, v in I.items()}
C.update({
 'dgc-stats-band': 'position: relative; z-index: 2; flex-direction: column; padding: 0 0 20px; background: linear-gradient(180deg, #04202c 0 70px, #ffffff 70px);',
 'dgc-stats': 'display: grid; grid-template-columns: repeat(5, 1fr); grid-template-rows: auto; gap: 0; padding: 0; overflow: hidden; border: 2px solid var(--navy); border-radius: 10px; background: linear-gradient(180deg, #ffffff, #f1f7f8); box-shadow: 0 30px 60px -30px rgba(6,40,54,0.45); @media(--tablet) { grid-template-columns: repeat(3, 1fr); } @media(--mobile) { grid-template-columns: repeat(2, 1fr); }',
 'dgc-stat': 'position: relative; display: flex; flex-direction: column; align-items: center; gap: 0; padding: 34px 18px 30px; text-align: center; font-family: Manrope; transition: background 0.3s; &:hover { background: #fff8ef; } @media(--mobile) { padding: 26px 12px; }',
 'dgc-stat-ic': 'display: flex; align-items: center; justify-content: center; width: 50px; height: 50px; margin: 0 auto 16px; padding: 0; border-radius: 50%; background: var(--navy); color: #ffffff; box-shadow: 0 10px 20px -10px rgba(6,40,54,0.8);',
 'dgc-stat-num': 'display: block; font-family: Unbounded; font-size: clamp(2rem, 3.4vw, 3rem); font-weight: 700; line-height: 1; letter-spacing: -0.03em; color: var(--ink); font-variant-numeric: tabular-nums;',
 'dgc-stat-label': 'display: block; margin-top: 10px; font-size: 0.9rem; font-weight: 700; color: var(--ink-3);',
})
print('classes', mcp.upsert_classes(C))
STATS = [('monitor', '55', '+', 'Websites launched'), ('layers', '30', '+', 'Industries served'), ('doc', '20', '+', 'Case studies'), ('calendar', '17', '+', 'Years of expertise'), ('star-o', '5.0', '★', 'Google rating')]
x, cfg, cls = '', {}, {}
for i, (ic, n, sup, label) in enumerate(STATS, 1):
    p = f'Stat {i}'
    x += f'<e-flexbox configuration-id="{p}"><e-flexbox configuration-id="{p} Icon Disc"><e-div-block configuration-id="{p} Icon"></e-div-block></e-flexbox><e-paragraph configuration-id="{p} Number"></e-paragraph><e-paragraph configuration-id="{p} Label"></e-paragraph></e-flexbox>'
    cfg[f'{p} Number'] = {'paragraph': f'{n}<sup>{sup}</sup>', 'tag': 'span'}
    cfg[f'{p} Label'] = {'paragraph': label, 'tag': 'span'}
    cls[p] = ['dgc-stat']; cls[f'{p} Icon Disc'] = ['dgc-stat-ic']; cls[f'{p} Icon'] = [f'ico-{ic}']; cls[f'{p} Number'] = ['dgc-stat-num']; cls[f'{p} Label'] = ['dgc-stat-label']
X = f'<e-flexbox configuration-id="Stats"><e-div-block configuration-id="Stats Wrap"><e-grid configuration-id="Stats Card">{x}</e-grid></e-div-block></e-flexbox>'
cfg['Stats'] = {'tag': 'section'}
cls.update({'Stats': ['dgc-stats-band'], 'Stats Wrap': ['dgc-wrap'], 'Stats Card': ['dgc-stats']})
r = mcp.put_section(126, 'Stats', 2, xml_structure=X, element_config=cfg, classes=cls)
print(json.dumps({k: r.get(k) for k in ('success', 'warnings', 'root_element_ids')})[:500])
print([e.get('title') for e in mcp.call('elementor-get-page-structure', {'post_id': 126})['elements']])
