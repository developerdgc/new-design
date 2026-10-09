"""Copy the portfolio design system (global variables + global classes, same priority order) to digitalgrowthcatalyze.com.
Class CSS comes from the offline capture of the build scripts (capture/captured.json); order from staging (staging_meta.json)."""
import os, json
os.environ['DGC_SITE'] = 'main'
import mcp
assert mcp.SERVER == 'digital-growth-catalyze-elementor'
CAP = json.load(open('../capture/captured.json')); META = json.load(open('../capture/staging_meta.json'))
# 1) variables
have = json.loads(mcp.call('elementor-read-resource', {'uri': 'elementor://global-variables'})['content'])['variables']
have_labels = {v['label'] for v in have.values()}
ops = [{'action': 'create', 'type': t, 'label': l, 'value': v} for l, t, v, _ in META['vars'] if l not in have_labels]
if ops: r = mcp.call('elementor-manage-global-variable', {'operations': ops}); print('vars', json.dumps(r)[:200])
# 2) classes
C = {l: CAP['classes'][l] for l in CAP['order']}
print('classes', mcp.upsert_classes(C)); print('dups removed', mcp.drop_dups())
# 3) priority = staging order (highest first)
ids = mcp.class_ids(); pr = [l for l in META['priority'] if l in ids]
moves = [{'id': ids[l], 'position': 'start'} for l in reversed(pr)]
for i in range(0, len(moves), 20): mcp.call('elementor-reorder-classes', {'moves': moves[i:i + 20]})
now = mcp.class_labels(); print('order matches staging:', [l for l in now if l in pr] == pr, len(now))
