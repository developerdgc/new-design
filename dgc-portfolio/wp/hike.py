"""'Hike' artwork for the case-study tiles: rising glass bars + glowing zig-zag growth arrow."""
def hike_svg():
    bars = ''.join(f"<rect x='{x}' y='{220 - h}' width='38' height='{h}' rx='5' fill='url(#bar)'/><rect x='{x}' y='{220 - h}' width='38' height='3' rx='1.5' fill='#ffffff' fill-opacity='.55'/>"
                   for x, h in ((158, 46), (210, 74), (262, 104), (314, 140)))
    line = 'M96 178 L160 138 L206 156 L268 98 L306 114 L384 46'
    head = "<polygon points='399,31 395,58 374,41' fill='#ffffff'/>"
    return ("<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 400 220' preserveAspectRatio='xMaxYMax meet'>"
            "<defs><linearGradient id='bar' x1='0' y1='0' x2='0' y2='1'><stop offset='0' stop-color='#bff6f7' stop-opacity='.55'/><stop offset='1' stop-color='#1cdee1' stop-opacity='.04'/></linearGradient>"
            "<filter id='glow' x='-20%' y='-20%' width='140%' height='140%'><feGaussianBlur stdDeviation='6'/></filter></defs>"
            + bars +
            f"<path d='{line}' fill='none' stroke='#1cdee1' stroke-width='16' stroke-linecap='round' stroke-linejoin='round' stroke-opacity='.55' filter='url(#glow)'/>"
            f"<path d='{line}' fill='none' stroke='#ffffff' stroke-width='7' stroke-linecap='round' stroke-linejoin='round'/>" + head + "</svg>")
if __name__ == '__main__':
    open('hike.svg', 'w').write(hike_svg())
