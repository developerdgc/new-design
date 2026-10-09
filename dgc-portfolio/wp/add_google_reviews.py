"""Swap the static testimonial cards for the live 'Widgets for Google Reviews' (Trustindex) widget.
WordPress runs shortcodes on the_content after Elementor renders, so a plain span holding the shortcode
becomes the live widget on the front end (no V3 shortcode widget needed)."""
import json, mcp
PAGE = 126; SC = '[trustindex no-registration=google]'
print(mcp.upsert_classes({'dgc-greviews': 'display: block; width: 100%; margin-top: 44px; padding: 0; @media(--mobile) { margin-top: 32px; }'}))
def find(es, title):
    for e in es:
        if e.get('title') == title: return e
        x = find(e.get('elements', []), title)
        if x: return x
tree = mcp.call('elementor-get-page-structure', {'post_id': PAGE})['elements']
wrap, grid, count = find(tree, 'Testimonials Wrap'), find(tree, 'Reviews Grid'), find(tree, 'Score Count')
if not find(tree, 'Google Reviews Widget'):
    r = mcp.call('elementor-build-composition', {'post_id': PAGE, 'parent_id': wrap['id'], 'mode': 'append',
        'xml_structure': '<e-div-block configuration-id="Google Reviews Widget"><e-paragraph configuration-id="Google Reviews Shortcode"></e-paragraph></e-div-block>',
        'element_config': {'Google Reviews Shortcode': {'paragraph': SC, 'tag': 'span'}},
        'classes': {'Google Reviews Widget': ['dgc-greviews']}})
    print('widget', r.get('success'), r.get('warnings'))
ops = [{'action': 'update', 'element_id': count['id'], 'settings': {'paragraph': '15 Google reviews'}}] if count else []
if grid: ops.append({'action': 'delete', 'element_id': grid['id']})
if ops: print(json.dumps(mcp.call('elementor-manage-elements', {'post_id': PAGE, 'operations': ops}))[:300])
print(json.dumps(mcp.call('elementor-publish-document', {'post_id': PAGE}))[:100])
