"""Offline stand-in for mcp.py: records class definitions, never touches a site."""
CLASSES = {}; ORDER = []; PRIO = []; VARS = []
SERVER = 'stub'; URL = ''; AUTH = 'Basic stub'
class Any(dict):
    def __getitem__(self, k): return dict.get(self, k, Any())
    def get(self, k, d=None): return dict.get(self, k, Any() if d is None else d)
def _rec(label, css):
    if label not in CLASSES: ORDER.append(label)
    CLASSES[label] = css
def upsert_classes(C):
    for k, v in C.items(): _rec(k, v)
    return 'ok'
def call(name, args=None):
    args = args or {}
    if name == 'elementor-manage-classes':
        for op in args.get('operations', []):
            if op.get('action') in ('create', 'update') and op.get('css') is not None: _rec(op['label'], op['css'])
        return {'results': [{'status': 'ok'} for _ in args.get('operations', [])]}
    if name == 'elementor-manage-global-variable': VARS.extend(args.get('operations', []))
    if name == 'elementor-get-page-structure': return {'elements': []}
    return Any(success=True)
def class_labels(): return list(CLASSES)
def drop_dups(): return []
def prioritize(labels): PRIO.append(list(labels))
def put_section(*a, **k): return Any(success=True)
def class_ids(): return {}
def tools(): return []
def init(): return {}
