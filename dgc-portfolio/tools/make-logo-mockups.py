"""Builds dark, business-themed photo mockups for client logos.

Usage: python3 tools/make-logo-mockups.py   (run from dgc-portfolio/)
Each logo in LOGOS gets two mockups: img/mockups/<slug>-1.jpg and -2.jpg.
Base photos (Unsplash) live in tools/mockup-bases/.
"""
from PIL import Image, ImageChops, ImageDraw, ImageEnhance, ImageFilter

BASES = 'tools/mockup-bases/'
OUT = 'img/mockups/'
# slug, brand colour, the two mockups to use
LOGOS = [
    ('rainbow-restoration', '#b3121f', ('truck', 'darkcard')),
    ('clean-environments', '#2f8fc4', ('truck', 'laptop')),
    ('many-colors', '#f2c230', ('darkcard', 'truck')),
    ('clark-exteriors', '#d03030', ('truck', 'laptop')),
]
CROPS = {  # 900:743 crop box in each base photo
    'truck': (225, 0, 1355, 933), 'darkcard': (180, 0, 1310, 933), 'laptop': (250, 160, 1150, 903),
}


def hexrgb(h):
    h = h.lstrip('#'); return tuple(int(h[i:i + 2], 16) for i in (0, 2, 4))


def persp_coeffs(pa, pb):
    """Perspective coefficients mapping target quad pa onto source points pb."""
    A, B = [], []
    for (x, y), (u, v) in zip(pa, pb):
        A.append([x, y, 1, 0, 0, 0, -u * x, -u * y]); B.append(u)
        A.append([0, 0, 0, x, y, 1, -v * x, -v * y]); B.append(v)
    M = [row[:] + [b] for row, b in zip(A, B)]
    for c in range(8):
        p = max(range(c, 8), key=lambda r: abs(M[r][c])); M[c], M[p] = M[p], M[c]
        for r in range(8):
            if r != c:
                f = M[r][c] / M[c][c]
                M[r] = [a - f * b for a, b in zip(M[r], M[c])]
    return [M[i][8] / M[i][i] for i in range(8)]


def light_version(logo):
    """Logo for dark surfaces: dark ink becomes white, colours stay."""
    px = logo.load(); out = logo.copy(); po = out.load()
    for y in range(logo.height):
        for x in range(logo.width):
            r, g, b, a = px[x, y]
            if a == 0:
                continue
            lum = (0.299 * r + 0.587 * g + 0.114 * b) / 255
            if lum < 0.42 and max(r, g, b) < 150:
                po[x, y] = (245, 245, 242, a)
    return out


def fit(logo, w, h, pad=0.1):
    canvas = Image.new('RGBA', (w, h), (0, 0, 0, 0))
    lg = logo.copy(); lg.thumbnail((int(w * (1 - 2 * pad)), int(h * (1 - 2 * pad))), Image.LANCZOS)
    canvas.alpha_composite(lg, ((w - lg.width) // 2, (h - lg.height) // 2))
    return canvas


def warp(art, quad, size):
    w, h = art.size
    return art.transform(size, Image.PERSPECTIVE, persp_coeffs(quad, [(0, 0), (w, 0), (w, h), (0, h)]), Image.BICUBIC)


def paint(base, layer, opacity=1.0, shade=True):
    """Print the layer onto the surface, keeping the surface's light and texture."""
    a = layer.split()[3].point(lambda v: int(v * opacity))
    top = layer.convert('RGB')
    if shade:
        lum = base.convert('L').filter(ImageFilter.GaussianBlur(6))
        lum = ImageEnhance.Brightness(lum).enhance(4.0)  # dark surface -> near 1.0 multiplier
        top = ImageChops.multiply(top, Image.merge('RGB', [lum] * 3))
    return Image.composite(top, base, a)


def mock_truck(base, logo, color):
    # flat side panel of the box truck
    quad = [(240, 222), (760, 212), (760, 462), (240, 466)]
    art = fit(light_version(logo), 1040, 500, pad=0.06)
    out = paint(base, warp(art, quad, base.size), 0.94, shade=False)
    # brand stripe along the lower panel
    d = Image.new('RGBA', base.size, (0, 0, 0, 0)); ImageDraw.Draw(d).polygon([(205, 486), (768, 482), (768, 498), (205, 502)], fill=hexrgb(color) + (235,))
    return paint(out, d, 1.0, shade=False)


def mock_darkcard(base, logo, color):
    quad = [(528, 250), (800, 252), (796, 445), (526, 443)]
    art = fit(light_version(logo), 900, 640, pad=0.08)
    out = paint(base, warp(art, quad, base.size), 0.95, shade=False)
    d = Image.new('RGBA', base.size, (0, 0, 0, 0)); ImageDraw.Draw(d).polygon([(560, 470), (760, 471), (760, 476), (560, 475)], fill=hexrgb(color) + (230,))
    return paint(out, d, 1.0, shade=False)


def mock_laptop(base, logo, color):
    screen = [(497, 405), (779, 404), (778, 588), (497, 590)]
    w, h = 1128, 740
    page = Image.new('RGBA', (w, h), (8, 30, 40, 255)); dr = ImageDraw.Draw(page)
    c = hexrgb(color)
    for y in range(h):  # soft brand glow
        t = y / h; dr.line((0, y, w, y), fill=(int(8 + (c[0] - 8) * .18 * (1 - t)), int(30 + (c[1] - 30) * .18 * (1 - t)), int(40 + (c[2] - 40) * .18 * (1 - t)), 255))
    dr.rectangle((0, 0, w, 40), fill=(4, 20, 28, 255))
    for i, col in enumerate([(255, 107, 95), (246, 164, 64), (60, 207, 110)]):
        dr.ellipse((18 + i * 26, 13, 32 + i * 26, 27), fill=col + (255,))
    page.alpha_composite(fit(light_version(logo), w, h - 160, pad=0.16), (0, 40))
    dr.rounded_rectangle((w // 2 - 120, h - 130, w // 2 + 120, h - 78), radius=26, fill=c + (255,))
    scr = warp(page, screen, base.size)
    return Image.composite(scr.convert('RGB'), base, scr.split()[3])


FN = {'truck': mock_truck, 'darkcard': mock_darkcard, 'laptop': mock_laptop}

for slug, color, kinds in LOGOS:
    logo = Image.open(f'img/logos/{slug}.png').convert('RGBA')
    logo = logo.crop(logo.getbbox())
    big = logo.resize((logo.width * 3, logo.height * 3), Image.LANCZOS)
    for n, kind in enumerate(kinds, 1):
        base = Image.open(BASES + kind + '.jpg').convert('RGB')
        img = FN[kind](base, big, color).crop(CROPS[kind]).resize((900, 743), Image.LANCZOS)
        img.save(f'{OUT}{slug}-{n}.jpg', quality=82, optimize=True, progressive=True)
        print(slug, n, kind)
