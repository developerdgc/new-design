"""Global classes: CSS-mask icons + header/footer building blocks."""
import mcp, json, urllib.parse, re
def icon_css(svg_body, size=16, stroke=False, sw=2.6):
    svg = re.sub(r'<svg[^>]*>', '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" ' + ('fill="none" stroke="black" stroke-width="' + str(sw) + '" stroke-linecap="round" stroke-linejoin="round">' if stroke else 'fill="black">'), svg_body, count=1)
    u = 'url("data:image/svg+xml,' + urllib.parse.quote(svg) + '")'
    return f'display: inline-block; width: {size}px; height: {size}px; min-width: 0; padding: 0; flex: none; background-color: currentColor; -webkit-mask: {u} center / contain no-repeat; mask: {u} center / contain no-repeat;'
ICONS = {n: open(f'icons/{n}.svg').read() for n in ['phone', 'mail', 'facebook', 'instagram', 'linkedin', 'arrow-right', 'burger', 'pin', 'chevron-up']}
C = {
 'dgc-hdr': 'position: fixed; top: 0; left: 0; right: 0; z-index: 100; flex-direction: column; padding: 0 16px; gap: 0; transition: transform 0.35s;',
 'dgc-hdr-top': 'display: grid; grid-template-columns: 1fr auto 1fr; align-items: center; max-width: 1260px; width: 100%; margin: 0 auto; height: 50px; padding: 0 10px; color: #ffffff; font-family: Manrope; font-size: 0.92rem; font-weight: 600; transition: opacity 0.3s; @media(--mobile) { grid-template-columns: 1fr; justify-items: center; height: 44px; }',
 'dgc-toplink': 'display: inline-flex; align-items: center; gap: 9px; width: auto; padding: 0; color: #ffffff; text-decoration: none; transition: color 0.25s; &:hover { color: var(--cyan); }',
 'dgc-hide-mobile': '@media(--mobile) { display: none; }',
 'dgc-nav': 'align-items: center; justify-content: space-between; gap: 28px; max-width: 1280px; width: 100%; margin: 6px auto 0; min-height: 84px; padding: 0 22px 0 30px; border: 1.5px solid rgba(255,255,255,0.75); border-radius: 10px; background: rgba(20,45,58,0.55); backdrop-filter: blur(14px) saturate(140%); box-shadow: 0 20px 40px -24px rgba(0,0,0,0.7); transition: background 0.3s, border-color 0.3s; @media(--tablet) { min-height: 72px; padding: 0 14px 0 18px; gap: 14px; }',
 'dgc-navlinks': 'align-items: center; gap: 10px; width: auto; padding: 0; margin: 0 auto; @media(--tablet) { display: none; }',
 'dgc-navlink': 'background: transparent; color: #ffffff; font-family: Manrope; font-size: 0.9rem; font-weight: 800; letter-spacing: 0.01em; text-transform: uppercase; padding: 9px 10px; border-radius: 0; transition: color 0.25s; &:hover { color: var(--cyan); }',
 'dgc-btn-hot': 'display: inline-flex; align-items: center; gap: 10px; width: auto; padding: 15px 26px; border-radius: 10px; background: var(--orange); color: var(--abyss); font-family: Manrope; font-size: 1rem; font-weight: 800; text-decoration: none; box-shadow: 0 12px 24px -12px rgba(246,164,64,0.9); transition: background 0.25s, color 0.25s, transform 0.25s; &:hover { background: #ffffff; color: var(--navy); }',
 'dgc-burger': 'display: none; align-items: center; justify-content: center; width: 46px; height: 46px; min-width: 0; padding: 0; border: 1px solid rgba(255,255,255,0.3); border-radius: 10px; background: transparent; color: #ffffff; cursor: pointer; @media(--tablet) { display: flex; }',
 'dgc-hide-tablet': '@media(--tablet) { display: none; }',
}
def main():
    ops = [{'action': 'create', 'label': 'ico-' + n, 'css': icon_css(sv, 16, stroke=n in ('arrow-right', 'chevron-up'))} for n, sv in ICONS.items()]
    for k, v in C.items(): ops.append({'action': 'create', 'label': k, 'css': v})
    r = mcp.call('elementor-manage-classes', {'operations': ops})
    print([(x.get('label'), x['status'], x.get('error', '')) for x in r['results'] if x['status'] != 'ok'] or 'all ok', len(r['results']))

if __name__ == '__main__':
    main()
