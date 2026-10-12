"""Turn the artifact's inline SVG sprite into standalone coloured icon files for Elementor e-image widgets."""
import re, os, sys
SRC = "/home/user/new-design/redshield-water/index.html"
OUT = "/home/user/new-design/redshield-water/img/icons"
html = open(SRC).read()
SYMS = {m.group(1): (m.group(2), m.group(3)) for m in re.finditer(r'<symbol id="i-([a-z]+)" viewBox="([^"]+)">(.*?)</symbol>', html, re.S)}
FILLED = {"star", "play"}
def icon(name, color):
    vb, body = SYMS[name]
    attrs = f'fill="{color}" stroke="none"' if name in FILLED else f'fill="none" stroke="{color}" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"'
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{vb}" width="24" height="24" {attrs}>{body}</svg>'
COLORS = {"red": "#dc2626", "white": "#ffffff", "navy": "#0b2340", "green": "#22c55e", "lgreen": "#4ade80", "pink": "#ff6b6b", "salmon": "#ff8080",
          "gold": "#facc15", "text": "#0e1726", "muted": "#94a3b8", "reddark": "#b91c1c"}
if __name__ == "__main__":
    n = 0
    for name in SYMS:
        for cname, hexv in COLORS.items():
            open(f"{OUT}/{name}-{cname}.svg", "w").write(icon(name, hexv)); n += 1
    # Trustpilot star squares, brush underline, green dot
    star = SYMS["star"][1]
    def tp(count, size):
        cells = "".join(f'<rect x="{i*(size+3)}" y="0" width="{size}" height="{size}" fill="#00b67a"/><svg x="{i*(size+3)+size*0.15}" y="{size*0.15}" width="{size*0.7}" height="{size*0.7}" viewBox="0 0 24 24"><g fill="#fff">{star}</g></svg>' for i in range(count))
        return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {count*(size+3)-3} {size}" width="{count*(size+3)-3}" height="{size}">{cells}</svg>'
    open(f"{OUT}/tp-stars.svg", "w").write(tp(5, 22))
    open(f"{OUT}/brush-red.svg", "w").write('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 300 20" preserveAspectRatio="none"><path d="M4 14 C 70 4, 150 4, 296 10" fill="none" stroke="#dc2626" stroke-width="5" stroke-linecap="round" opacity=".85"/></svg>')
    open(f"{OUT}/dot-green.svg", "w").write('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 10 10" width="10" height="10"><circle cx="5" cy="5" r="4.5" fill="#22c55e"/></svg>')
    open(f"{OUT}/dot-white.svg", "w").write('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 10 10" width="10" height="10"><circle cx="5" cy="5" r="4.5" fill="#ffffff"/></svg>')
    print(len(SYMS), "symbols ->", n, "icon files")
