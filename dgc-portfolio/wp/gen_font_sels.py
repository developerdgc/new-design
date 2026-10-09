"""Collect every global-class selector that sets a web font (feeds the size-matched fallbacks in head_snippets.py)."""
import re, json, urllib.request
sels = {}
for pid in (126, 128, 130):
    h = urllib.request.urlopen(urllib.request.Request(f'https://newportfolio.digitalgrowthcatalyze.com/?page_id={pid}&nc=fs', headers={'User-Agent': 'Mozilla/5.0'})).read().decode()
    for u in set(re.findall(r"href='([^']*elementor/css/[^']*\.css[^']*)'", h)):
        css = urllib.request.urlopen(urllib.request.Request(u, headers={'User-Agent': 'Mozilla/5.0'})).read().decode()
        for m in re.finditer(r'([^{}]+)\{[^}]*font-family:(Manrope|Unbounded|Poppins)[;}]', css):
            for s in m.group(1).split(','):
                s = s.strip()
                if s.startswith('.elementor .dgc-') and ':' not in s: sels.setdefault(m.group(2), set()).add(s)
json.dump({k: sorted(sels.get(k, [])) for k in ('Manrope', 'Unbounded', 'Poppins')}, open('font_sels.json', 'w'), indent=0)
print({k: len(v) for k, v in sels.items()})
