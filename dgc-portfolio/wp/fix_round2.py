"""Round-2 review fixes: footer typography on the site's fonts, header size matched to the artifact."""
import re, mcp
FILES = ['classes_base.py', 'build_footer.py']
NEW = {
 'dgc-nav': lambda s: s.replace('max-width: 1280px', 'max-width: 1260px'),
 'dgc-ftr': lambda s: s.replace('font-family: Poppins;', 'font-family: Manrope;'),
 'dgc-ftr-h': lambda s: 'font-family: Unbounded; font-size: 1.15rem; font-weight: 700; line-height: 1.3; letter-spacing: -0.01em; color: var(--orange); text-decoration: underline; text-decoration-thickness: 2px; text-underline-offset: 7px; margin-bottom: 28px; @media(--mobile) { font-size: 1.05rem; margin-bottom: 18px; }',
 'dgc-ftr-link': lambda s: s.replace('font-size: 1.05rem;', 'font-family: Manrope; font-size: 0.98rem; font-weight: 600;'),
 'dgc-ftr-p': lambda s: 'font-family: Manrope; font-size: 0.98rem; line-height: 1.7; color: var(--fog); max-width: 40ch; margin-top: 22px;',
 'dgc-ftr-crow': lambda s: s.replace('font-size: 1.05rem;', 'font-family: Manrope; font-size: 0.98rem; font-weight: 600;'),
 'dgc-ftr-h5': lambda s: 'font-family: Unbounded; font-size: 1.05rem; font-weight: 700; color: #ffffff; margin: 30px 0 14px;',
 'dgc-ftr-base': lambda s: s.replace('font-family: Poppins; font-size: 1.05rem; color: #ffffff;', 'font-family: Manrope; font-size: 0.92rem; font-weight: 500; color: var(--fog);'),
}
out = {}
for fn in FILES:
    src = open(fn).read()
    for label, f in NEW.items():
        m = re.search(r"(\n '" + re.escape(label) + r"': ')([^']*)(')", src)
        if not m: continue
        new = f(m.group(2)); assert new != m.group(2) or label in out, label
        src = src[:m.start(2)] + new + src[m.end(2):]; out[label] = new
    open(fn, 'w').write(src)
print(sorted(out), len(out) == len(NEW))
print(mcp.upsert_classes(out))
