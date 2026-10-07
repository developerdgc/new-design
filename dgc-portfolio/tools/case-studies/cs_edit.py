import re, sys, html, glob, os, shutil
S = '/tmp/claude-0/-home-user-new-design/c0b0073b-578a-5cca-805d-2082208a4256/scratchpad'
sys.path.insert(0, S)
from cs_data import P
SRC = S + '/artifact-files/33456778-7583-4ed3-9394-50fb437b74e2/project/'
OUT = S + '/canvas/project/'
e = html.escape
NAVY, ORANGE, CYAN, TEAL = '#07222F', '#F6A440', '#1CDEE1', '#0E6D74'
REDACT = '<span style="display: inline-block; width: 150px; height: 0.95em; background: #000000; border-radius: 3px; vertical-align: -0.14em; margin-right: 6px"></span>'
ICON = '<svg width="24" height="24" style="display: block; flex-shrink: 0" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="#07222F" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M3 3v18h18"/><path d="M7 15l4-4 3 3 5-6"/></svg>'

def head(title, sub):
    return (f'<div style="display: flex; align-items: center; gap: 12px; margin-bottom: 18px"><div style="width: 48px; height: 48px; border-radius: 14px; background: linear-gradient(135deg, #FFC56E 0%, #F6A440 45%, #E5861C 100%); box-shadow: 0 10px 22px rgba(246,164,64,0.4); display: flex; align-items: center; justify-content: center; flex-shrink: 0">{ICON}</div>'
            f'<div><div style="font: 600 15.1px Unbounded, sans-serif; color: #FFFFFF">{e(title)}</div><div style="font: 500 12.5px Poppins, sans-serif; color: #8FB1B8">{e(sub)}</div></div></div>')

def bar_row(label, disp, frac, badge='', color=ORANGE):
    b = f'<span style="margin-left: 8px; font: 700 11px Poppins, sans-serif; color: #07222F; background: {CYAN}; padding: 2px 7px; border-radius: 999px">{e(badge)}</span>' if badge else ''
    w = max(4, round(frac * 100, 1))
    return (f'<div style="display: flex; flex-direction: column; gap: 7px"><div style="display: flex; align-items: center; justify-content: space-between; gap: 10px"><span style="font: 600 13px Poppins, sans-serif; color: #CFE3E7">{e(label)}{b}</span><span style="font: 600 17px Unbounded, sans-serif; color: #FFFFFF">{e(disp)}</span></div>'
            f'<div style="height: 12px; border-radius: 999px; background: rgba(255,255,255,0.08); overflow: hidden"><div style="width: {w}%; height: 100%; border-radius: 999px; background: linear-gradient(90deg, {color}, #FFC56E)"></div></div></div>')

def foot(text):
    return f'<div style="margin-top: auto; padding-top: 16px; border-top: 1px solid rgba(255,255,255,0.12); font: 500 12.5px/1.5 Poppins, sans-serif; color: #8FB1B8">{text}</div>'

def chart_body(spec):
    kind = spec[0]
    if kind == 'bars':
        rows, cap = spec[1], spec[2]
        mx = max(r[2] for r in rows)
        body = ''.join(bar_row(l, d, v / mx, bdg) for l, d, v, bdg in rows)
        return head('Results at a glance', 'From the client’s Google Business Profile') + f'<div style="display: flex; flex-direction: column; gap: 18px">{body}</div>' + foot('★ ' + e(cap))
    if kind == 'ba':
        out = ''
        for l, bd, bv, ad, av, low in spec[1]:
            mx = max(bv, av)
            note = ' <span style="color: #8FB1B8; font-weight: 500">(lower is better)</span>' if low else ''
            out += (f'<div style="display: flex; flex-direction: column; gap: 7px"><div style="font: 600 13px Poppins, sans-serif; color: #CFE3E7">{e(l)}{note}</div>'
                    f'<div style="display: grid; grid-template-columns: 54px minmax(0,1fr) 54px; align-items: center; gap: 10px"><span style="font: 600 11px Poppins, sans-serif; color: #8FB1B8">Before</span><div style="height: 10px; border-radius: 999px; background: rgba(255,255,255,0.08)"><div style="width: {max(4, bv / mx * 100):.1f}%; height: 100%; border-radius: 999px; background: #5C7780"></div></div><span style="font: 600 13px Poppins, sans-serif; color: #CFE3E7; text-align: right">{e(bd)}</span></div>'
                    f'<div style="display: grid; grid-template-columns: 54px minmax(0,1fr) 54px; align-items: center; gap: 10px"><span style="font: 700 11px Poppins, sans-serif; color: {ORANGE}">After</span><div style="height: 10px; border-radius: 999px; background: rgba(255,255,255,0.08)"><div style="width: {max(4, av / mx * 100):.1f}%; height: 100%; border-radius: 999px; background: linear-gradient(90deg, {ORANGE}, #FFC56E)"></div></div><span style="font: 700 14px Unbounded, sans-serif; color: #FFFFFF; text-align: right">{e(ad)}</span></div></div>')
        return head('Before vs. after', 'Google Search Console · 6 months vs. previous 6') + f'<div style="display: flex; flex-direction: column; gap: 22px">{out}</div>' + foot('Bars compare each metric with its own previous period.')
    if kind == 'rank':
        stats = ''.join(f'<div style="flex: 1; background: rgba(255,255,255,0.06); border-radius: 12px; padding: 14px"><div style="font: 600 22px Unbounded, sans-serif; color: #FFFFFF">{e(v)}</div><div style="font: 500 12px Poppins, sans-serif; color: #8FB1B8; margin-top: 4px">{e(l)}</div></div>' for l, v in spec[1])
        steps = ''
        for i, (lab, h, col) in enumerate([('Jan', 18, '#5C7780'), ('', 34, '#3E8F96'), ('', 56, '#1A9AA3'), ('', 78, '#E5861C'), ('Sep', 100, ORANGE)]):
            steps += f'<div style="flex: 1; display: flex; flex-direction: column; align-items: center; gap: 6px; justify-content: flex-end; height: 130px"><div style="width: 100%; height: {h}%; border-radius: 8px 8px 3px 3px; background: {col}"></div><span style="font: 600 11px Poppins, sans-serif; color: #8FB1B8; height: 14px">{lab}</span></div>'
        return (head('Ranking climb', 'Tracked supercar keywords · Jan → Sep 2026') +
                '<div style="display: flex; justify-content: space-between; font: 600 12px Poppins, sans-serif; margin-bottom: 8px"><span style="color: #8FB1B8">Not ranking</span><span style="color: #F6A440">#1 on Google</span></div>'
                f'<div style="display: flex; gap: 10px; align-items: flex-end">{steps}</div>'
                f'<div style="display: flex; gap: 10px; margin-top: 18px">{stats}</div>' + foot('Illustrative climb from not ranking to #1; numbers from Google Search Console.'))
    if kind == 'ring':
        hit, tot, mk = spec[1], spec[2], spec[3]
        pct = hit / tot * 100
        chips = ''.join(f'<span style="font: 600 12.5px Poppins, sans-serif; color: #FFFFFF; background: rgba(28,222,225,0.12); border: 1px solid rgba(28,222,225,0.35); padding: 6px 12px; border-radius: 999px">{e(m)}</span>' for m in mk)
        dots = ''.join(f'<div style="display: flex; align-items: center; gap: 10px; font: 500 13px Poppins, sans-serif; color: #CFE3E7"><span style="width: 20px; height: 20px; border-radius: 50%; background: {ORANGE}; display: flex; align-items: center; justify-content: center; font: 700 12px Poppins, sans-serif; color: #07222F">✓</span>Question {i + 1}: client named</div>' for i in range(tot))
        return (head('AI answer coverage', 'Google AI Mode · tracked customer questions') +
                f'<div style="display: flex; align-items: center; gap: 22px"><div style="width: 132px; height: 132px; flex-shrink: 0; border-radius: 50%; background: conic-gradient({ORANGE} 0 {pct}%, rgba(255,255,255,0.1) 0); display: flex; align-items: center; justify-content: center"><div style="width: 100px; height: 100px; border-radius: 50%; background: {NAVY}; display: flex; flex-direction: column; align-items: center; justify-content: center"><span style="font: 600 26px Unbounded, sans-serif; color: #FFFFFF">{hit}/{tot}</span><span style="font: 500 11px Poppins, sans-serif; color: #8FB1B8">named</span></div></div>'
                f'<div style="display: flex; flex-direction: column; gap: 9px">{dots}</div></div>'
                f'<div style="margin-top: 20px; font: 600 12px Poppins, sans-serif; letter-spacing: 1.4px; text-transform: uppercase; color: #8FB1B8">Markets covered</div><div style="display: flex; flex-wrap: wrap; gap: 8px; margin-top: 10px">{chips}</div>')
    if kind == 'cost':
        rows, stats = spec[1], spec[2]
        mx = max(v for _, v in rows)
        cols = ''.join(f'<div style="flex: 1; display: flex; flex-direction: column; align-items: center; gap: 8px; justify-content: flex-end; height: 190px"><span style="font: 600 16px Unbounded, sans-serif; color: #FFFFFF">${v:,.2f}</span><div style="width: 64%; height: {max(4, v / mx * 100) * 0.72:.1f}%; border-radius: 10px 10px 3px 3px; background: linear-gradient(180deg, #FFC56E, {ORANGE})"></div><span style="font: 600 12px Poppins, sans-serif; color: #CFE3E7; text-align: center">{e(l)}</span></div>' for l, v in rows)
        st = ''.join(f'<div style="flex: 1; min-width: 0; background: rgba(255,255,255,0.06); border-radius: 12px; padding: 14px 16px"><div style="font: 600 22px Unbounded, sans-serif; color: #FFFFFF">{e(v)}</div><div style="font: 500 12px Poppins, sans-serif; color: #8FB1B8; margin-top: 4px">{e(l)}</div></div>' for v, l in stats)
        return (head('What each result cost', 'From the Google Ads account') +
                f'<div style="display: grid; grid-template-columns: minmax(0, 1.1fr) minmax(0, 1fr); gap: 28px; align-items: end"><div style="display: flex; gap: 14px; align-items: flex-end; border-bottom: 1px solid rgba(255,255,255,0.15); padding-bottom: 4px">{cols}</div>'
                f'<div style="display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 10px">{st}</div></div>')
    if kind == 'mix':
        ph, msg, stats = spec[1], spec[2], spec[3]
        tot = ph + msg; pct = ph / tot * 100
        st = ''.join(f'<div style="flex: 1; min-width: 0; background: rgba(255,255,255,0.06); border-radius: 12px; padding: 14px 16px"><div style="font: 600 22px Unbounded, sans-serif; color: #FFFFFF">{e(v)}</div><div style="font: 500 12px Poppins, sans-serif; color: #8FB1B8; margin-top: 4px">{e(l)}</div></div>' for v, l in stats)
        leg = (f'<div style="display: flex; align-items: center; gap: 10px; font: 600 14px Poppins, sans-serif; color: #FFFFFF"><span style="width: 14px; height: 14px; border-radius: 4px; background: {ORANGE}"></span>Phone leads <span style="margin-left: auto; font: 600 18px Unbounded, sans-serif">{ph:,}</span></div>'
               f'<div style="display: flex; align-items: center; gap: 10px; font: 600 14px Poppins, sans-serif; color: #FFFFFF"><span style="width: 14px; height: 14px; border-radius: 4px; background: {CYAN}"></span>Message leads <span style="margin-left: auto; font: 600 18px Unbounded, sans-serif">{msg:,}</span></div>')
        return (head('Lead mix', 'Google Local Services Ads · charged leads') +
                f'<div style="display: grid; grid-template-columns: 150px minmax(0, 1fr) minmax(0, 1fr); gap: 28px; align-items: center"><div style="width: 150px; height: 150px; border-radius: 50%; background: conic-gradient({ORANGE} 0 {pct}%, {CYAN} 0); display: flex; align-items: center; justify-content: center"><div style="width: 108px; height: 108px; border-radius: 50%; background: {NAVY}; display: flex; flex-direction: column; align-items: center; justify-content: center"><span style="font: 600 24px Unbounded, sans-serif; color: #FFFFFF">{tot:,}</span><span style="font: 500 11px Poppins, sans-serif; color: #8FB1B8">leads</span></div></div>'
                f'<div style="display: flex; flex-direction: column; gap: 14px">{leg}</div><div style="display: flex; flex-direction: column; gap: 10px">{st}</div></div>')

def find_block(s, start):
    """Return end index of the <div> element starting at start (balanced)."""
    depth = 0
    for m in re.finditer(r'<div\b|</div>', s[start:]):
        depth += 1 if m.group(0) == '<div' else -1
        if depth == 0:
            return start + m.end()
    raise ValueError('unbalanced')

def facts(block):
    rows = re.findall(r'text-transform: uppercase; color: #5C7780">([^<]+)</span><span style="font: 600 16px Poppins, sans-serif">([^<]+)</span>', block)
    return [(html.unescape(a), html.unescape(b)) for a, b in rows]

def fact_chips(fs):
    return ''.join(f'<div style="display: flex; flex-direction: column; gap: 2px; background: #FFFFFF; border: 1px solid #DCE8EA; border-radius: 12px; padding: 12px 16px"><span style="font: 600 11.5px Poppins, sans-serif; letter-spacing: 1.3px; text-transform: uppercase; color: #5C7780">{e(a)}</span><span style="font: 600 15px Poppins, sans-serif; color: #07222F">{e(b)}</span></div>' for a, b in fs)

report = []
for f in sorted(glob.glob(SRC + '*.dc.html')):
    name = os.path.basename(f); s = open(f).read()
    para, spec = P[name]
    i = s.lower().find('business overview')
    # 2) overview paragraph: hidden business name + extended text
    m = re.search(r'(<p style="[^"]*">)(.*?)(</p>)', s[i:], re.S)
    a, b = i + m.start(2), i + m.end(2)
    s = s[:a] + REDACT + e(para).replace('&#x27;', '’') + s[b:]
    # 1) privacy block -> chart
    A = '<div style="width: 430px; flex-shrink: 0; background: #07222F; color: #FFFFFF; border-radius: 22px; padding: 26px 28px; box-shadow: 0 24px 50px rgba(7,34,47,0.25); display: flex; flex-direction: column; border-top: 4px solid #F6A440">'
    B = '<div style="border: 1px solid #DCE8EA; border-radius: 10px; overflow: hidden; border-top: 4px solid #07222F">'
    C = '<div style="width: 100%; position: relative; background: #FFFFFF; color: #07222F; border-radius: 14px; box-shadow: 0 24px 50px rgba(7,34,47,0.10)">'
    if A in s:
        st = s.index(A); en = find_block(s, st)
        s = s[:st] + A + chart_body(spec) + '</div>' + s[en:]; kind = 'A'
    elif B in s or C in s:
        key = B if B in s else C
        st = s.index(key); en = find_block(s, st)
        fs = [x for x in facts(s[st:en])]
        card = (f'<div style="display: flex; flex-direction: column; gap: 16px"><div style="background: #07222F; color: #FFFFFF; border-radius: 22px; padding: 26px 30px; box-shadow: 0 24px 50px rgba(7,34,47,0.25); border-top: 4px solid #F6A440">{chart_body(spec)}</div>'
                f'<div style="display: grid; grid-template-columns: repeat({min(4, max(1, len(fs)))}, minmax(0, 1fr)); gap: 10px">{fact_chips(fs)}</div></div>')
        s = s[:st] + card + s[en:]; kind = 'B' if key == B else 'C'
    else:
        kind = '??'
    left = len(re.findall(r'background: #000000', s))
    report.append((name, kind, left))
    open(OUT + name, 'w').write(s)
for r in report: print(*r)
