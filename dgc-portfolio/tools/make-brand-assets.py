import os, zipfile, io, json
from PIL import Image, ImageChops
Image.MAX_IMAGE_PIXELS = None
OUT = '/home/user/new-design/dgc-portfolio/img/brands/'
# slug: (zip, logo file, crop-logo-box-fraction or None, [mockup files])
B = {
 'genia-mcpherson': ('mockuppng', 'Gold PNG.png', None, ['3.png', '1.png', '5.png', '4.png']),
 'kam-rc': ('kamrc', '6.png', None, ['1.png', '8.png', '9.png', '7.png']),
 'irina-stoyan': ('irina', 'Irina stoyan png.png', None, ['7.png', '5.png', '8.png', '4.png']),
 'specialized-cabinets': ('logozip', 'Png.png', None, ['New.png', 'card.png', 'Shopping-Bag-Mockup-Vol6.png', 'red label.png']),
 'visa-help': ('vh247', 'final l.png', (.035, .035, .965, .63), ['PSD_65.png', '3.png', '4.png', '6.png']),
}
colors = {}
for slug, (zn, logo, box, mocks) in B.items():
    z = zipfile.ZipFile(f'dl/{zn}.zip'); d = OUT + slug; os.makedirs(d, exist_ok=True)
    im = Image.open(io.BytesIO(z.read(logo))).convert('RGBA')
    if box:
        w, h = im.size; im = im.crop((int(box[0]*w), int(box[1]*h), int(box[2]*w), int(box[3]*h)))
        # make near-white background transparent-ish: trim to content on white
        bg = Image.new('RGB', im.size, (255, 255, 255)); diff = ImageChops.difference(im.convert('RGB'), bg).convert('L').point(lambda v: 255 if v > 18 else 0)
        bb = diff.getbbox(); im = im.crop(bb)
        # knock out white
        px = im.load()
        for y in range(im.height):
            for x in range(im.width):
                r, g, b, a = px[x, y]
                m = min(r, g, b)
                if m > 235: px[x, y] = (r, g, b, 0)
    else:
        im = im.crop(im.getbbox())
    pad = int(max(im.size) * .03); c = Image.new('RGBA', (im.width + 2*pad, im.height + 2*pad)); c.paste(im, (pad, pad)); im = c
    im.thumbnail((900, 900), Image.LANCZOS); im.save(f'{d}/logo.png', optimize=True)
    # brand colour = most common saturated colour in the logo
    sm = im.copy(); sm.thumbnail((200, 200)); cnt = {}
    for r, g, b, a in sm.getdata():
        if a < 200: continue
        mx, mn = max(r, g, b), min(r, g, b)
        if mx - mn < 60 or mx < 90: continue
        k = (r // 24 * 24, g // 24 * 24, b // 24 * 24); cnt[k] = cnt.get(k, 0) + 1
    k = max(cnt, key=cnt.get); colors[slug] = '#%02x%02x%02x' % k
    for i, m in enumerate(mocks, 1):
        mi = Image.open(io.BytesIO(z.read(m))).convert('RGBA')
        bb = mi.getchannel('A').point(lambda v: 255 if v > 10 else 0).getbbox(); mi = mi.crop(bb)
        bgc = Image.new('RGB', mi.size, (12, 14, 16)); bgc.paste(mi, mask=mi.getchannel('A'))
        bgc.thumbnail((1400, 1400), Image.LANCZOS); bgc.save(f'{d}/m{i}.jpg', quality=80, optimize=True, progressive=True)
    print(slug, colors[slug], im.size, sum(os.path.getsize(f'{d}/{f}') for f in os.listdir(d)) // 1024, 'KB')
json.dump(colors, open('brand_colors.json', 'w'))
