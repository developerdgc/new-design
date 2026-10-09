"""digitalgrowthcatalyze.com service pages: one row of case-study cards between 'Why DGC' and 'Benefits'.
Builds into the (published) page's autosave, moves the new section into place, and only publishes with --publish."""
import os, sys, json
os.environ['DGC_SITE'] = 'main'
sys.path.insert(0, '/tmp/claude-0/-home-user-new-design/c0b0073b-578a-5cca-805d-2082208a4256/scratchpad')
import mcp
from build_work import Frag, case_card, link, SITE
from common import cases_by_channel
INDEX = 6  # after 'WHY DGC' (5), before 'Benefits of Choosing Us' (6 -> 7)
TITLE = 'Service Case Studies'
by = {}
for rank, cs in cases_by_channel(): by.setdefault(cs[2], []).append(cs)
PAGES = {  # page id: (cases, heading, text)
 3260: (by['Google Business Profile'][:4], 'Real Google Business Profile Results', 'How we moved local businesses into the map pack and turned profile views into calls.'),
 2634: (by['Google Ads'][:2] + by['Local Services Ads'][:2], 'Real Google Ads & LSA Results', 'Campaigns that turned ad budget into booked jobs for local service businesses.'),
 3249: (by['Web SEO'][:4], 'Real SEO Results', 'How we grew rankings, traffic and leads for local businesses.'),
 3235: (by['AI Overview'][:4], 'Real AI Overview Results', 'How we got local businesses named in Google\'s AI answers.'),
}
C = {
 'dgc-svc-cases': 'flex-direction: column; gap: 0; padding: 80px 0 90px; background: #ffffff; font-family: Manrope; @media(--mobile) { padding: 56px 0 64px; }',
 'dgc-svc-head': 'flex-direction: column; align-items: center; gap: 0; margin-bottom: 40px; padding: 0 16px; text-align: center; @media(--mobile) { margin-bottom: 28px; }',
 'dgc-svc-kicker': 'display: inline-block; padding: 12px 21px; border-radius: 5px; background: #f6a440; color: #000000; font-family: Marcellus SC; font-size: 14px; font-weight: 700; line-height: 1.2; letter-spacing: 1.4px; text-transform: uppercase;',
 'dgc-svc-h2': 'display: block; margin-top: 18px; font-family: Raleway; font-size: 34px; font-weight: 700; line-height: 1.2; color: #06232f; @media(--mobile) { font-size: 26px; }',
 'dgc-svc-p': 'display: block; max-width: 640px; margin-top: 10px; font-family: Poppins; font-size: 16px; line-height: 1.6; color: #333333; @media(--mobile) { font-size: 14px; }',
 'dgc-svc-cgrid': 'display: flex; flex-wrap: nowrap; justify-content: center; gap: 24px; padding: 0 0 6px; @media(--tablet) { justify-content: flex-start; gap: 16px; overflow-x: auto; scroll-snap-type: x mandatory; padding: 0 0 14px; } @media(--mobile) { gap: 14px; }',
 'dgc-svc-citem': 'flex: 0 0 calc(25% - 18px); min-width: 0; padding: 0; scroll-snap-align: start; @media(--tablet) { flex: 0 0 46%; } @media(--mobile) { flex: 0 0 86%; }',
 'dgc-svc-more': 'justify-content: center; margin-top: 36px; padding: 0;',
}
def build(pid):
    cases, h2, p = PAGES[pid]
    f = Frag()
    for i, cs in enumerate(cases, 1): case_card(f, i, cs)
    for k in list(f.cls):  # plain items, not homepage work cards
        if f.cls[k][:2] == ['dgc-work', 'dgc-c-case']: f.cls[k] = ['dgc-svc-citem'] + f.cls[k][2:]
    f.x = (f'<e-flexbox configuration-id="{TITLE}"><e-div-block configuration-id="SC Wrap"><e-flexbox configuration-id="SC Head">'
           '<e-paragraph configuration-id="SC Kicker"></e-paragraph><e-heading configuration-id="SC Title"></e-heading><e-paragraph configuration-id="SC Text"></e-paragraph></e-flexbox>'
           f'<e-flexbox configuration-id="SC Grid">{f.x}</e-flexbox>'
           '<e-flexbox configuration-id="SC More"><e-flexbox configuration-id="SC Button"><e-paragraph configuration-id="SC Button Text"></e-paragraph><e-div-block configuration-id="SC Button Icon"></e-div-block></e-flexbox></e-flexbox>'
           '</e-div-block></e-flexbox>')
    f.cfg.update({TITLE: {'tag': 'section'}, 'SC Kicker': {'paragraph': 'Case Studies', 'tag': 'span'}, 'SC Title': {'tag': 'h2', 'title': h2}, 'SC Text': {'paragraph': p},
                  'SC Button': {'tag': 'a', 'link': link(SITE + '/case-studies/')}, 'SC Button Text': {'paragraph': 'View All Case Studies', 'tag': 'span'}})
    f.cls.update({TITLE: ['dgc-svc-cases'], 'SC Wrap': ['dgc-wrap'], 'SC Head': ['dgc-svc-head'], 'SC Kicker': ['dgc-svc-kicker'], 'SC Title': ['dgc-svc-h2'],
                  'SC Text': ['dgc-svc-p'], 'SC Grid': ['dgc-svc-cgrid'], 'SC More': ['dgc-svc-more'], 'SC Button': ['dgc-mhero-btn'], 'SC Button Icon': ['ico-arrow-right']})
    roots = mcp.call('elementor-get-page-structure', {'post_id': pid})['elements']
    old = [e['id'] for e in roots if e.get('title') == TITLE]
    if old: mcp.call('elementor-manage-elements', {'post_id': pid, 'operations': [{'action': 'delete', 'element_id': i} for i in old]})
    r = mcp.call('elementor-build-composition', {'post_id': pid, 'parent_id': 'document', 'mode': 'append', 'xml_structure': f.x, 'element_config': f.cfg, 'classes': f.cls, 'style': f.sty})
    rid = (r.get('root_element_ids') or [None])[0]
    mv = mcp.call('elementor-manage-elements', {'post_id': pid, 'operations': [{'action': 'move', 'element_id': rid, 'new_parent_id': 'document', 'index': INDEX}]})
    print(pid, 'built', r.get('success'), r.get('warnings'), rid, 'move', mv.get('status'), [x.get('status') for x in mv.get('results', [])])
if __name__ == '__main__':
    print('classes', mcp.upsert_classes(C))
    for pid in PAGES: build(pid)
    if '--publish' in sys.argv:
        os.environ['DGC_ALLOW_PUBLISH'] = '1'
        for pid in PAGES: print(pid, json.dumps(mcp.call('elementor-publish-document', {'post_id': pid}))[:120])
