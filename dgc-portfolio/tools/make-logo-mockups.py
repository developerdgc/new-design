"""Builds photo mockups for client logos.

Usage: python3 tools/make-logo-mockups.py   (run from dgc-portfolio/)
Each logo in LOGOS gets two mockups, written to img/mockups/<slug>-1.jpg and -2.jpg.
Base photos (Unsplash) live in tools/mockup-bases/.
"""
from PIL import Image, ImageChops, ImageDraw, ImageFilter, ImageOps

BASES = 'tools/mockup-bases/'
OUT = 'img/mockups/'
# slug, card colour, the two mockups to use
LOGOS = [
    ('rainbow-restoration', '#b3121f', ('wallsign', 'cards')),
    ('clean-environments', '#2f8fc4', ('tee', 'mug')),
    ('many-colors', '#f2c230', ('mug', 'polesign')),
    ('clark-exteriors', '#1b1e22', ('polesign', 'cards')),
]
CROPS = {  # final 4:3.3 crop box in the base photo
    'cards': (85, 0, 1216, 933), 'mug': (160, 0, 1291, 933), 'tee': (140, 0, 1271, 933),
    'wallsign': (150, 0, 1281, 933), 'polesign': (21, 120, 1379, 1240),
}

def hexrgb(h):
    h = h.lstrip('#'); return tuple(int(h[i:i + 2], 16) for i in (0, 2, 4))

def persp_coeffs(pa, pb):
    # pa: target points, pb: source points (solves 8x8 system without numpy)
    A, B = [], []
    for (x, y), (u, v) in zip(pa, pb):
        A.append([x, y, 1, 0, 0, 0, -u * x, -u * y]); B.append(u)
        A.append([0, 0, 0, x, y, 1, -v * x, -v * y]); B.append(v)
    n = 8
    M = [row[:] + [b] for row, b in zip(A, B)]
    for c in range(n):
        p = max(range(c, n), key=lambda r: abs(M[r][c])); M[c], M[p] = M[p], M[c]
        for r in range(n):
            if r != c:
                f = M[r][c] / M[c][c]
                M[r] = [a - f * b for a, b in zip(M[r], M[c])]
    return [M[i][n] / M[i][i] for i in range(n)]

def fit_logo(logo, w, h, pad=0.12, bg=None):
    canvas = Image.new('RGBA', (w, h), bg or (255, 255, 255, 0))
    lg = logo.copy(); lg.thumbnail((int(w * (1 - 2 * pad)), int(h * (1 - 2 * pad))), Image.LANCZOS)
    canvas.alpha_composite(lg, ((w - lg.width) // 2, (h - lg.height) // 2))
    return canvas

def warp(art, quad, size):
    w, h = art.size
    c = persp_coeffs(quad, [(0, 0), (w, 0), (w, h), (0, h)])
    return art.transform(size, Image.PERSPECTIVE, c, Image.BICUBIC)

def multiply(base, layer):
    """Multiply an RGBA layer onto an RGB base, respecting alpha."""
    rgb = Image.new('RGB', base.size, (255, 255, 255)); rgb.paste(layer, mask=layer.split()[3])
    mult = ImageChops.multiply(base, rgb)
    return Image.composite(mult, base, layer.split()[3])

def poly_mask(size, pts, blur=1.2):
    m = Image.new('L', size, 0); ImageDraw.Draw(m).polygon(pts, fill=255)
    return m.filter(ImageFilter.GaussianBlur(blur))

def mock_cards(base, logo, color):
    left = [(200, 366), (578, 171), (742, 356), (352, 596)]
    tint = Image.new('RGB', base.size, hexrgb(color))
    base = Image.composite(ImageChops.multiply(base, tint), base, poly_mask(base.size, left))
    face = [(540, 513), (893, 305), (1105, 497), (705, 757)]
    art = fit_logo(logo, 1100, 770, pad=0.14)
    return multiply(base, warp(art, face, base.size))

def mock_mug(base, logo, color):
    art = fit_logo(logo, 330, 330, pad=0.02)
    # squeeze the sides a little so the logo follows the mug's curve
    strips, w = [], art.width
    out = Image.new('RGBA', art.size, (0, 0, 0, 0)); x = 0
    for i in range(w):
        t = (i / (w - 1)) * 2 - 1; nx = int((w / 2) + (w / 2) * (t * (1 - 0.12 * t * t)) * 0.98)
        col = art.crop((i, 0, i + 1, art.height)); out.paste(col, (min(w - 1, nx), 0), col)
    layer = Image.new('RGBA', base.size, (0, 0, 0, 0)); layer.alpha_composite(out, (725 - w // 2, 470 - art.height // 2))
    return multiply(base, layer)

def mock_tee(base, logo, color):
    art = fit_logo(logo, 250, 200, pad=0.0)
    layer = Image.new('RGBA', base.size, (0, 0, 0, 0)); layer.alpha_composite(art, (705 - 125, 250))
    # fabric texture: keep shading of the shirt by multiplying
    return multiply(base, layer)

def mock_wallsign(base, logo, color):
    face = [(543, 237), (902, 196), (902, 661), (543, 653)]
    base = Image.composite(Image.new('RGB', base.size, (250, 250, 247)), base, poly_mask(base.size, face, 0.8))
    art = fit_logo(logo, 900, 1100, pad=0.12)
    layer = warp(art, face, base.size)
    out = base.copy(); out.paste(layer, mask=layer.split()[3]); return out

def mock_polesign(base, logo, color):
    face = [(510, 238), (895, 315), (898, 1052), (505, 1000)]
    m = poly_mask(base.size, face, 6)
    light = Image.blend(base, Image.new('RGB', base.size, (246, 247, 248)), 0.72)
    base = Image.composite(light, base, m)
    art = fit_logo(logo, 800, 1500, pad=0.12)
    return multiply(base, warp(art, face, base.size))

FN = {'cards': mock_cards, 'mug': mock_mug, 'tee': mock_tee, 'wallsign': mock_wallsign, 'polesign': mock_polesign}

for slug, color, kinds in LOGOS:
    logo = Image.open(f'img/logos/{slug}.png').convert('RGBA')
    logo = logo.crop(logo.getbbox())
    big = logo.resize((logo.width * 3, logo.height * 3), Image.LANCZOS)
    for n, kind in enumerate(kinds, 1):
        base = Image.open(BASES + kind + '.jpg').convert('RGB')
        img = FN[kind](base, big, color).crop(CROPS[kind]).resize((900, 743), Image.LANCZOS)
        img.save(f'{OUT}{slug}-{n}.jpg', quality=80, optimize=True, progressive=True)
        print(slug, n, kind)
