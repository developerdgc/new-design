"""Make the branding panels more compact (review round 2, desktop item 7)."""
import re, mcp
NEW = {
 'dgc-brand': 'position: relative; display: grid; grid-template-columns: 0.92fr 1.3fr; grid-template-rows: auto; gap: 12px; align-items: stretch; width: 100%; max-width: 1040px; margin: 0 auto; padding: 14px; overflow: hidden; border-radius: 10px; @media(--tablet) { grid-template-columns: 0.92fr 1.3fr; padding: 14px; gap: 12px; } @media(--mobile) { grid-template-columns: 1fr; padding: 10px; gap: 10px; }',
 'dgc-brand-mocks': 'display: grid; grid-template-columns: 1fr 1fr; grid-template-rows: auto; gap: 8px; align-content: start; padding: 0;',
 'dgc-bm': 'display: block; padding: 0; overflow: hidden; aspect-ratio: 16 / 9; border-radius: 10px; border: 1px solid #dde8ea; background: #0c0e10;',
 'dgc-lcard-panel': 'flex: 1; aspect-ratio: auto; min-height: 220px; @media(--tablet) { aspect-ratio: auto; min-height: 220px; } @media(--mobile) { aspect-ratio: 4 / 3.4; min-height: 0; }',
}
src = open('work_classes.py').read()
for k, v in NEW.items():
    src, n = re.subn(r"(\n '" + re.escape(k) + r"': ')[^']*(')", lambda m: m.group(1) + v + m.group(2), src); assert n == 1, k
open('work_classes.py', 'w').write(src)
print(mcp.upsert_classes(NEW))
