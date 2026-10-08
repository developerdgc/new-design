import html
e = html.escape
S = '/tmp/claude-0/-home-user-new-design/c0b0073b-578a-5cca-805d-2082208a4256/scratchpad'
LINES = open(S + '/lines.svg').read()
MAIN_URL = 'https://claude.ai/artifact/V7aRsgUfucDzCMmVpQvS83'
VID_URL = 'https://claude.ai/artifact/UJVdEQgTu5RaGLeUZTtCWL'
def case_url():
    import os
    p = S + '/case_url.txt'
    return open(p).read().strip() if os.path.exists(p) else '#'
# 24x24 line icons, one per industry
ICONS = {
 'car': '<path d="M3 15v-2.5l2.2-4A2 2 0 0 1 7 7.5h7.5a3 3 0 0 1 2.3 1.1L19 11l1.6.5a1.5 1.5 0 0 1 1.1 1.4V15"/><path d="M2 15h20"/><circle cx="7" cy="16" r="2"/><circle cx="17" cy="16" r="2"/><path d="M6 11h11"/>',
 'leaf': '<path d="M12 21v-6"/><path d="M12 15C7 15 3 11 3 6c4 0 7 2 9 5 2-3 5-5 9-5 0 5-4 9-9 9z"/><path d="M12 15V3"/>',
 'limo': '<path d="M1.5 15v-2l2-3h17l2 3v2z"/><path d="M6 10l1.5-2h9L18 10"/><circle cx="6" cy="16" r="1.8"/><circle cx="18" cy="16" r="1.8"/><path d="M10 10v5M14 10v5"/>',
 'fan': '<circle cx="12" cy="12" r="9"/><circle cx="12" cy="12" r="1.5"/><path d="M12 10.5C12 7 13.5 5 16 5c0 3-1.5 5.5-4 5.5zM13.3 12.8c3 1.7 4 4 2.8 6.2-2.6-1.5-3.8-4-2.8-6.2zM10.7 12.8c-3 1.7-5.5 1.5-6.7-.7 2.6-1.5 5.3-1.3 6.7.7z"/>',
 'tow': '<path d="M2 16V9h8v7"/><path d="M10 11h4l3 3v2h-7"/><path d="M2 9l5-4h3"/><path d="M21 7l-4 6"/><path d="M21 7v3"/><circle cx="6" cy="17" r="2"/><circle cx="15" cy="17" r="2"/>',
 'carpet': '<rect x="3" y="4" width="13" height="16" rx="1"/><path d="M16 6h3a2 2 0 0 1 0 4h-3"/><path d="M6 8h7M6 12h7M6 16h7"/>',
 'sparkle': '<path d="M12 3l1.8 4.7L18.5 9.5l-4.7 1.8L12 16l-1.8-4.7L5.5 9.5l4.7-1.8z"/><path d="M19 15l.8 2.2L22 18l-2.2.8L19 21l-.8-2.2L16 18l2.2-.8z"/>',
 'wall': '<rect x="3" y="4" width="18" height="16" rx="1"/><path d="M3 9.3h18M3 14.7h18M9 4v5.3M15 4v5.3M6 9.3v5.4M12 9.3v5.4M18 9.3v5.4M9 14.7V20M15 14.7V20"/>',
 'tire': '<circle cx="12" cy="12" r="9"/><circle cx="12" cy="12" r="4"/><path d="M12 3v5M12 16v5M3 12h5M16 12h5M5.6 5.6l3.6 3.6M14.8 14.8l3.6 3.6M18.4 5.6l-3.6 3.6M9.2 14.8l-3.6 3.6"/>',
 'spray': '<path d="M8 8h6l1 3v9a1 1 0 0 1-1 1H8a1 1 0 0 1-1-1v-9z"/><path d="M9 8V5h4v3"/><path d="M13 5h3l1 2"/><path d="M19 4l2-1M19 7h2.5M19 10l2 1"/>',
 'building': '<path d="M3 21h18"/><path d="M4 9l8-5 8 5"/><path d="M6 10v8M10 10v8M14 10v8M18 10v8"/><path d="M4 18h16"/>',
 'plane': '<path d="M2 16l20-6-3-2-7 2-5-5H5l3 6-4 1-2-2H1z"/><path d="M3 20h18"/>',
 'smoke': '<path d="M4 20h16"/><path d="M8 20v-4h8v4"/><path d="M9 12c0-2 2-2 2-4s-2-2-2-4M13 12c0-2 2-2 2-4s-2-2-2-4"/>',
 'concrete': '<path d="M3 21h18"/><path d="M5 21v-6h14v6"/><path d="M8 15V9h8v6"/><path d="M10 9V5h4v4"/>',
 'bus': '<rect x="4" y="3" width="16" height="15" rx="2"/><path d="M4 11h16M4 7h16"/><circle cx="8" cy="15" r="1"/><circle cx="16" cy="15" r="1"/><path d="M7 18v2M17 18v2"/>',
}
# (title, icon, channel, image in img/casestudies) — order: homepage shows the first six
CASES = [
    ('Cannabis Dispensary', 'leaf', 'Google Business Profile', 'gbp-cannabis-dispensary'),
    ('Towing Company', 'tow', 'Google Ads', 'ads-towing-company'),
    ('Cleaning Company', 'spray', 'AI Overview', 'aio-cleaning-company'),
    ('Air Duct Cleaning', 'fan', 'Local Services Ads', 'lsa-air-duct-cleaning'),
    ('Exotic Car Rental', 'car', 'Web SEO', 'seo-exotic-car-rental'),
    ('Limousine Service', 'limo', 'Google Business Profile', 'gbp-limousine-service'),
    ('Exotic Car Rental', 'car', 'Google Business Profile', 'gbp-exotic-car-rental'),
    ('Hookah Lounge', 'smoke', 'Google Business Profile', 'gbp-hookah-lounge'),
    ('Concrete Contractor', 'concrete', 'Google Business Profile', 'gbp-concrete-contractor'),
    ('Airport Transportation', 'plane', 'AI Overview', 'aio-airport-transportation'),
    ('Architecture Firm', 'building', 'AI Overview', 'aio-architecture-firm'),
    ('Air Duct Cleaning', 'fan', 'Google Ads', 'ads-air-duct-cleaning'),
    ('Cleaning Company', 'spray', 'Google Ads', 'ads-cleaning-company'),
    ('Exotic Car Rental', 'car', 'Google Ads', 'ads-exotic-car-rental'),
    ('Mobile Tire Service', 'tire', 'Google Ads', 'ads-mobile-tire-service'),
    ('Towing Company', 'tow', 'Local Services Ads', 'lsa-towing-company'),
    ('Carpet Cleaning', 'carpet', 'Local Services Ads', 'lsa-carpet-cleaning'),
    ('Auto Detailing & Coatings', 'sparkle', 'Web SEO', 'seo-auto-detailing-coatings'),
    ('Drywall Contractor', 'wall', 'Web SEO', 'seo-drywall-contractor'),
    ('Commercial Cleaning', 'spray', 'Web SEO', 'seo-commercial-cleaning'),
]
# Add a file path (PDF or image) as the third value later to open it on click
def case_card(title, icon, channel, img):
    return (f'<button class="case" type="button" data-title="{e(title)}" data-channel="{e(channel)}" data-file="img/casestudies/{img}.jpg">'
            f'<img class="case__mark" src="img/brand/dgc-mark-white.png" alt="" aria-hidden="true">'
            f'<span class="case__top"><span class="case__ic"><svg viewBox="0 0 24 24" aria-hidden="true">{ICONS[icon]}</svg></span><span class="case__label">{e(channel)}</span></span>'
            f'<span class="case__title">{e(title)}</span>'
            f'<span class="case__foot"><img src="img/brand/dgc-logo-white.png" alt="DGC" width="78" height="22"><span class="case__go">Read the case study<i aria-hidden="true">→</i></span></span></button>')
VIDEOS = [
    ('review-1', 'Clark Exteriors', 'Roofing contractor'),
    ('review-2', 'Huskins Services LLC', 'Cleaning & remodeling'),
    ('review-3', 'Dawn', 'Client video review'),
    ('review-4', 'Chase, Clean Cut', 'Client video review'),
]
PLAY = '<svg viewBox="0 0 24 24"><path d="M8 5v14l11-7z"/></svg>'
def video_card(k, name, sub):
    return (f'<li class="vthumb" data-src="video/{k}.mp4" data-name="{e(name)}"><button type="button" aria-label="Play video review from {e(name)}">'
            f'<img src="video/{k}.jpg" alt="Video review from {e(name)}" loading="lazy">'
            f'<span class="play" aria-hidden="true">{PLAY}</span></button>'
            f'<span class="vcap"><b>{e(name)}</b><em>{e(sub)}</em></span></li>')

# Client brands: slug, name, brand colour, mockups [(image or None, label)].
# Logo: img/brands/<slug>/logo.png when present, else img/logos/<slug>.png.
# The first two show as full branding panels; the rest open the same panel in a popup.
# slug, name, brand colour, card theme, palette swatches, mockups (file in img/brands/<slug>/, label for alt text)
BRANDS = [
    ('genia-mcpherson', 'Genia McPherson', '#d4a446', 'dark', ['#d4a446', '#ffffff', '#0b0b0b'], [('m1', 'Street banner'), ('m2', 'Business cards'), ('m3', 'Shopping bag'), ('m4', 'Card set')]),
    ('irina-stoyan', 'Irina Stoyan', '#e0c25a', 'dark', ['#e0c25a', '#cfcfcf', '#0b0b0b'], [('m1', 'Embossed letterhead'), ('m2', 'Business cards'), ('m3', 'Shopping bag'), ('m4', 'Hang tag')]),
    ('specialized-cabinets', 'Specialized Cabinets Inc', '#d39f55', 'dark', ['#d39f55', '#ffffff', '#0b0b0b'], [('m1', 'Embossed letterhead'), ('m2', 'Business cards'), ('m3', 'Shopping bag'), ('m4', 'Hang tag')]),
    ('kam-rc', 'Kam RC Inc', '#f04e0f', 'dark', ['#f04e0f', '#ffffff', '#0b0b0b'], [('m1', 'Card set'), ('m2', 'Business cards'), ('m3', 'Shopping bag'), ('m4', 'Hang tag')]),
    ('visa-help', 'Visa Help 24/7', '#1597d5', 'light', ['#1597d5', '#6d6e71', '#ffffff'], [('m1', 'Business cards'), ('m2', 'Shopping bag'), ('m3', 'Hang tag'), ('m4', 'Card set')]),
]
N_PANELS = 2
import os as _os
_ROOT = '/home/user/new-design/dgc-portfolio/'
def brand_logo(slug):
    p = f'img/brands/{slug}/logo.png'
    return p if _os.path.exists(_ROOT + p) else f'img/logos/{slug}.png'
def lcard(slug, name, color, theme, palette, panel=False):
    left = (f'<span class="lcard__id"><b>{e(name)}</b><small>Logo · Brand identity</small></span>' if panel else '<span>Primary logo</span>')
    sw = ''.join(f'<i style="background:{c}"></i>' for c in palette)
    return (f'<div class="lcard lcard--{theme}" style="--c:{color}"><span class="lcard__sheet"><img src="{brand_logo(slug)}" alt="{e(name)} logo" loading="lazy"></span>'
            f'<span class="lcard__foot">{left}<span class="lcard__sw" aria-hidden="true">{sw}<b>{color.upper()}</b></span></span></div>')
def bmock(img, label, name):
    return f'<figure class="bm"><div class="bm__img"><img src="{img}" alt="{e(name)} {e(label.lower())} mockup" loading="lazy"></div></figure>'
def brand_meta(name):
    return f'<div class="wmeta"><div><h3>{e(name)}</h3><p><em>Logo</em>Brand identity</p></div></div>'
def brand_panel(slug, name, color, theme, palette, mocks):
    return (f'<div class="brand" style="--c:{color}"><div class="brand__main">{lcard(slug, name, color, theme, palette, panel=True)}</div>'
            f'<div class="brand__mocks">{"".join(bmock(f"img/brands/{slug}/{m[0]}.jpg", m[1], name) for m in mocks)}</div></div>')
def brand_card(slug, name, color, theme, palette, mocks=None):
    return (f'<button class="lbtn" type="button" data-brand="{slug}" aria-label="Open the {e(name)} brand kit">{lcard(slug, name, color, theme, palette)}'
            f'<span class="lbtn__hint">View brand kit <i aria-hidden="true">→</i></span></button>{brand_meta(name)}')
def brand_templates():
    return ''.join(f'<template id="bk-{b[0]}">{brand_panel(*b)}</template>' for b in BRANDS[N_PANELS:])

CH_ORDER = ['Google Business Profile', 'AI Overview', 'Google Ads', 'Local Services Ads', 'Web SEO']
CH_LABEL = {'Google Business Profile': 'Google Profile', 'AI Overview': 'AI Overview', 'Google Ads': 'PPC', 'Local Services Ads': 'LSA', 'Web SEO': 'Web SEO'}
def cases_by_channel():
    out = []
    for ch in CH_ORDER:
        out += [(i, cs) for i, cs in enumerate([x for x in CASES if x[2] == ch])]
    return out  # (rank within channel, case)
def case_filter_tabs(cls='tab'):
    return (f'<button class="{cls}" type="button" data-f="all" aria-pressed="true">All</button>' +
            ''.join(f'<button class="{cls}" type="button" data-f="{e(ch)}" aria-pressed="false">{CH_LABEL[ch]}</button>' for ch in CH_ORDER))
