"""Global classes for the Work section (title, tabs, grid, website / brand / case cards)."""
import sys
sys.path.insert(0, '/tmp/claude-0/-home-user-new-design/c0b0073b-578a-5cca-805d-2082208a4256/scratchpad')
import mcp
from classes_base import icon_css
from common import ICONS
LINE = '#dde8ea'
C = {
 # section + title
 'dgc-work-sec': 'position: relative; overflow: hidden; flex-direction: column; gap: 0; padding: 120px 0 150px; background: #ffffff; font-family: Manrope; color: #181818; @media(--mobile) { padding: 76px 0; }',
 'dgc-work-gridbg': 'position: absolute; inset: 0; padding: 0; pointer-events: none; opacity: 0.45; background-image: linear-gradient(#dde8ea 1px, transparent 1px), linear-gradient(90deg, #dde8ea 1px, transparent 1px); background-size: 80px 80px; -webkit-mask-image: linear-gradient(180deg, #000, transparent 30%, transparent 70%, #000); mask-image: linear-gradient(180deg, #000, transparent 30%, transparent 70%, #000);',
 'dgc-work-wrap': 'position: relative; z-index: 1;',
 'dgc-wtitle': 'display: grid; grid-template-columns: 1fr auto; grid-template-rows: auto; align-items: end; gap: 40px; padding: 0; @media(--mobile) { grid-template-columns: 1fr; gap: 24px; }',
 'dgc-kicker': 'display: inline-flex; align-items: center; gap: 10px; font-family: Manrope; font-size: 0.74rem; font-weight: 800; letter-spacing: 0.22em; text-transform: uppercase; color: var(--orange-ink);',
 'dgc-wtitle-big': 'display: flex; align-items: flex-start; gap: 0.08em; margin-top: 18px; font-family: Unbounded; font-size: clamp(4.2rem, 15vw, 12.5rem); font-weight: 800; line-height: 0.8; letter-spacing: -0.06em; color: var(--ink);',
 'dgc-wtitle-side': 'max-width: 34ch; padding: 0 0 8px;',
 'dgc-body-p': 'display: block; font-family: Manrope; font-size: 1rem; line-height: 1.7; color: #181818;',
 'dgc-hint': 'display: inline-flex; align-items: center; gap: 10px; width: auto; margin-top: 16px; padding: 0; font-size: 0.82rem; font-weight: 700; color: var(--ink);',
 'dgc-hint-mouse': 'position: relative; flex: none; width: 22px; height: 34px; min-width: 0; padding: 0; border-radius: 10px; border: 2px solid var(--ink);',
 'dgc-hint-t': 'display: none;',
 # tabs + sub filters
 'dgc-filters': 'flex-wrap: wrap; justify-content: center; gap: 12px; margin-top: 48px; padding: 34px 0 0; border-top: 1px solid #dde8ea; @media(--mobile) { gap: 10px; }',
 'dgc-tab': 'display: inline-flex; align-items: center; width: auto; padding: 17px 32px; border: 0; border-radius: 10px; background: var(--orange); color: var(--abyss); font-family: Manrope; font-size: 1rem; font-weight: 800; line-height: 1; cursor: pointer; box-shadow: 0 10px 22px -14px rgba(246,164,64,0.9); transition: background 0.25s, color 0.25s, transform 0.25s, box-shadow 0.25s; &:hover { background: var(--navy); color: #ffffff; transform: translateY(-2px); } @media(--mobile) { padding: 14px 20px; font-size: 0.92rem; }',
 'dgc-subfilters': 'flex-wrap: wrap; justify-content: center; gap: 8px; margin-top: 22px; padding: 0;',
 'dgc-subfilters-grid': 'grid-column: 1 / -1; justify-content: flex-start; margin-top: -24px;',
 'dgc-stab': 'display: inline-flex; align-items: center; width: auto; padding: 11px 18px; border: 1.5px solid var(--navy); border-radius: 10px; background: #ffffff; color: var(--navy); font-family: Manrope; font-size: 0.88rem; font-weight: 700; line-height: 1; cursor: pointer; transition: background 0.25s, color 0.25s; &:hover { background: var(--navy); color: #ffffff; }',
 'dgc-f-all': 'min-width: 0;', 'dgc-f-web': 'min-width: 0;', 'dgc-f-logo': 'min-width: 0;', 'dgc-f-case': 'min-width: 0;',
 'dgc-sub-case': 'display: none;',
 'dgc-sf-all': 'min-width: 0;', 'dgc-sf-gbp': 'min-width: 0;', 'dgc-sf-aio': 'min-width: 0;', 'dgc-sf-ppc': 'min-width: 0;', 'dgc-sf-lsa': 'min-width: 0;', 'dgc-sf-seo': 'min-width: 0;',
 'dgc-lcard-dark': 'min-width: 0;', 'dgc-lcard-light': 'min-width: 0;', 'dgc-sub-all': 'min-width: 0;',
 # grid + group headings
 'dgc-grid': 'display: grid; grid-template-columns: repeat(3, 1fr); grid-template-rows: auto; gap: 56px 34px; margin-top: 64px; padding: 0; @media(--tablet) { grid-template-columns: repeat(2, 1fr); } @media(--mobile) { grid-template-columns: 1fr; }',
 'dgc-ghead': 'grid-column: 1 / -1; display: flex; align-items: center; gap: 22px; padding: 0; @media(--mobile) { gap: 12px; }',
 'dgc-ghead-h': 'display: block; font-family: Unbounded; font-size: clamp(1.4rem, 2.6vw, 2.1rem); font-weight: 700; line-height: 1.08; letter-spacing: -0.02em; white-space: nowrap; color: var(--ink); @media(--mobile) { white-space: normal; }',
 'dgc-ghead-line': 'flex: 1; height: 2px; min-width: 20px; padding: 0; border-radius: 2px; background: linear-gradient(90deg, #f6a440, transparent); @media(--mobile) { display: none; }',
 'dgc-ghead-btn': 'display: inline-flex; align-items: center; gap: 8px; width: auto; flex: none; padding: 13px 22px; border-radius: 10px; background: var(--orange); color: var(--abyss); font-family: Manrope; font-size: 0.92rem; font-weight: 800; text-decoration: none; box-shadow: 0 12px 24px -12px rgba(246,164,64,0.9); transition: background 0.25s, color 0.25s, transform 0.25s; &:hover { background: var(--navy); color: #ffffff; transform: translateY(-2px); } @media(--mobile) { margin-left: auto; padding: 10px 14px; font-size: 0.8rem; white-space: nowrap; }',
 'dgc-g-web': 'min-width: 0;', 'dgc-g-logo': 'min-width: 0;', 'dgc-g-case': 'min-width: 0;',
 # card base + categories
 'dgc-work': 'min-width: 0; padding: 0; transition: opacity 0.4s, filter 0.4s, translate 0.5s;',
 'dgc-c-web': 'min-width: 0;', 'dgc-c-logo': 'min-width: 0;', 'dgc-c-brand': 'grid-column: 1 / -1;', 'dgc-c-case': 'min-width: 0;',
 'dgc-ch-gbp': 'min-width: 0;', 'dgc-ch-aio': 'min-width: 0;', 'dgc-ch-ppc': 'min-width: 0;', 'dgc-ch-lsa': 'min-width: 0;', 'dgc-ch-seo': 'min-width: 0;',
 # website card
 'dgc-device': 'position: relative; display: flex; flex-direction: column; gap: 0; padding: 0 10px; border-radius: 10px; text-decoration: none; background: linear-gradient(160deg, #0d3c4f, #021720 70%); box-shadow: 0 30px 50px -30px rgba(6,40,54,0.6); transition: transform 0.5s, box-shadow 0.5s;',
 'dgc-device-top': 'display: flex; align-items: center; gap: 0; height: 38px; padding: 0;',
 'dgc-device-url': 'display: block; flex: 1; min-width: 0; margin-left: 10px; padding: 3px 10px; border-radius: 6px; background: rgba(255,255,255,0.06); color: rgba(255,255,255,0.55); font-family: Manrope; font-size: 0.72rem; line-height: 1.5; white-space: nowrap; overflow: hidden; text-overflow: ellipsis;',
 'dgc-screen2': 'position: relative; height: 430px; padding: 0; overflow: hidden; border-radius: 8px; background: #ffffff; @media(--mobile) { height: 400px; }',
 'dgc-shot': 'display: block; width: 100%; height: 100%; object-fit: cover; object-position: top;',
 'dgc-chin': 'display: flex; align-items: center; justify-content: center; height: 30px; font-family: Unbounded; font-size: 0.56rem; letter-spacing: 0.3em; color: rgba(255,255,255,0.28);',
 'dgc-wmeta': 'display: grid; grid-template-columns: 1fr auto; grid-template-rows: auto; align-items: center; gap: 16px; padding: 20px 4px 0; @media(--tablet) { grid-template-columns: 1fr auto; } @media(--mobile) { grid-template-columns: 1fr auto; }',
 'dgc-wmeta-txt': 'min-width: 0; padding: 0;',
 'dgc-wmeta-h': 'display: block; font-family: Manrope; font-size: 1.04rem; font-weight: 800; line-height: 1.3; letter-spacing: -0.01em; color: var(--ink); white-space: nowrap; overflow: hidden; text-overflow: ellipsis;',
 'dgc-wmeta-p': 'display: flex; align-items: center; gap: 8px; margin-top: 2px; font-family: Manrope; font-size: 0.84rem; color: #181818;',
 'dgc-go': 'display: flex; align-items: center; justify-content: center; flex: none; width: 46px; height: 46px; padding: 0; border-radius: 50%; border: 1.5px solid #dde8ea; color: var(--ink); text-decoration: none; transition: background 0.3s, border-color 0.3s, color 0.3s, transform 0.3s; &:hover { background: var(--orange); border: 1.5px solid #f6a440; color: var(--abyss); transform: rotate(45deg); }',
 'dgc-go-off': 'opacity: 0.35;',
 # brand panel / logo card
 'dgc-brand': 'position: relative; display: grid; grid-template-columns: 0.92fr 1.3fr; grid-template-rows: auto; gap: 12px; align-items: stretch; width: 100%; max-width: 1040px; margin: 0 auto; padding: 14px; overflow: hidden; border-radius: 10px; @media(--tablet) { grid-template-columns: 0.92fr 1.3fr; padding: 14px; gap: 12px; } @media(--mobile) { grid-template-columns: 1fr; padding: 10px; gap: 10px; }',
 'dgc-brand-top': 'position: absolute; left: 0; right: 0; top: 0; width: auto; height: 4px; padding: 0;',
 'dgc-brand-main': 'display: flex; padding: 0; min-width: 0;',
 'dgc-brand-mocks': 'display: grid; grid-template-columns: 1fr 1fr; grid-template-rows: auto; gap: 8px; align-content: start; padding: 0;',
 'dgc-bm': 'display: block; padding: 0; overflow: hidden; aspect-ratio: 16 / 9; border-radius: 10px; border: 1px solid #dde8ea; background: #0c0e10;',
 'dgc-bm-img': 'display: block; width: 100%; height: 100%; object-fit: cover; transition: scale 0.7s;',
 'dgc-lcard': 'position: relative; display: block; width: 100%; aspect-ratio: 4 / 3.3; padding: 0; overflow: hidden; border-radius: 10px; isolation: isolate; box-shadow: 0 30px 50px -30px rgba(6,40,54,0.7);',
 'dgc-lcard-panel': 'flex: 1; aspect-ratio: auto; min-height: 220px; @media(--tablet) { aspect-ratio: auto; min-height: 220px; } @media(--mobile) { aspect-ratio: 4 / 3.4; min-height: 0; }',
 'dgc-lsheet': 'position: absolute; left: 12%; right: 12%; top: 13%; bottom: 25%; width: auto; height: auto; display: flex; align-items: center; justify-content: center; padding: 5% 8%; border-radius: 10px; transition: transform 0.6s, box-shadow 0.6s;',
 'dgc-lsheet-panel': 'left: 10%; right: 10%; top: 9%; bottom: 24%;',
 'dgc-lsheet-img': 'display: block; width: 100%; height: 100%; object-fit: contain;',
 'dgc-lfoot': 'position: absolute; left: 12%; right: 12%; bottom: 7.5%; width: auto; display: flex; align-items: center; justify-content: space-between; gap: 10px; padding: 0; font-family: Manrope; font-size: 0.66rem; font-weight: 800; letter-spacing: 0.16em; text-transform: uppercase; color: var(--fog);',
 'dgc-lid': 'display: grid; gap: 4px; padding: 0; min-width: 0;',
 'dgc-lid-name': 'display: block; font-family: Manrope; font-size: 1.02rem; font-weight: 800; letter-spacing: -0.01em; text-transform: none; color: #ffffff;',
 'dgc-lid-sub': 'display: block; font-size: 0.7rem; font-weight: 700; letter-spacing: 0.14em; text-transform: uppercase;',
 'dgc-lsw': 'display: flex; align-items: center; justify-content: flex-end; flex-wrap: nowrap; gap: 5px; width: auto; padding: 0;',
 'dgc-sw': 'width: 14px; height: 14px; min-width: 0; padding: 0; border-radius: 4px; border: 1px solid rgba(255,255,255,0.3);',
 'dgc-lhex': 'display: block; margin-left: 4px; font-size: 0.66rem; letter-spacing: 0.08em; color: #ffffff;',
 'dgc-lbtn': 'position: relative; display: block; width: 100%; padding: 0; border: 0; border-radius: 10px; background: transparent; text-align: left; cursor: pointer;',
 'dgc-lhint': 'position: absolute; right: 14px; top: 14px; z-index: 2; display: block; padding: 10px 15px; border-radius: 10px; background: var(--orange); color: var(--abyss); font-family: Manrope; font-size: 0.8rem; font-weight: 800; opacity: 0; transition: opacity 0.3s, background 0.25s, color 0.25s; &:hover { background: #ffffff; color: var(--navy); }',
 'dgc-kit': 'display: none;',
 # case study card
 'dgc-case': 'position: relative; display: flex; flex-direction: column; gap: 0; width: 100%; aspect-ratio: 5 / 4; padding: 24px; overflow: hidden; isolation: isolate; border: 1px solid rgba(28,222,225,0.18); border-radius: 10px; color: #ffffff; text-decoration: none; cursor: pointer; background: radial-gradient(70% 60% at 80% 100%, rgba(246,164,64,0.38), transparent 70%), radial-gradient(60% 50% at 0% 0%, rgba(28,222,225,0.18), transparent 70%), linear-gradient(150deg, #0b3a4d 0%, #062836 55%, #021720 100%); transition: transform 0.45s, border-color 0.35s, box-shadow 0.45s; &:hover { transform: translateY(-8px); border: 1px solid rgba(246,164,64,0.7); box-shadow: 0 40px 60px -30px rgba(6,40,54,0.85), 0 0 0 1px rgba(246,164,64,0.4); }',
 'dgc-case-mark': 'position: absolute; z-index: -1; right: -12%; top: -14%; width: 66%; height: auto; opacity: 0.06; transform: rotate(-14deg); transition: transform 0.8s, opacity 0.5s;',
 'dgc-case-top': 'display: flex; align-items: center; gap: 12px; padding: 0;',
 'dgc-case-ic': 'display: flex; align-items: center; justify-content: center; flex: none; width: 52px; height: 52px; padding: 0; border-radius: 10px; background: var(--orange); color: var(--abyss); box-shadow: 0 12px 24px -10px rgba(246,164,64,0.8); transition: transform 0.45s;',
 'dgc-case-label': 'display: block; font-family: Manrope; font-size: 0.7rem; font-weight: 800; letter-spacing: 0.2em; text-transform: uppercase; color: var(--cyan);',
 'dgc-case-title': 'display: block; margin-top: auto; font-family: Unbounded; font-size: clamp(1.05rem, 2.1vw, 2rem); font-weight: 700; line-height: 1.05; letter-spacing: -0.02em; text-transform: uppercase; color: #ffffff; overflow-wrap: anywhere;',
 'dgc-case-foot': 'display: flex; align-items: center; justify-content: space-between; gap: 10px; margin-top: 18px; padding: 14px 0 0; border-top: 1px solid rgba(255,255,255,0.12);',
 'dgc-case-logo': 'display: block; width: auto; height: 22px; opacity: 0.85;',
 'dgc-case-go': 'display: inline-flex; align-items: center; gap: 8px; width: auto; padding: 0; font-family: Manrope; font-size: 0.8rem; font-weight: 800; color: var(--orange); white-space: nowrap;',
 'dgc-case-go-i': 'display: flex; align-items: center; justify-content: center; width: 28px; height: 28px; border-radius: 50%; border: 1.5px solid #f6a440; font-style: normal; transition: background 0.3s, color 0.3s, transform 0.3s;',
 # bottom buttons
 'dgc-more': 'justify-content: center; gap: 12px; margin-top: 40px; padding: 0;',
 'dgc-btn-hot-light': 'border: 1.5px solid transparent; background: var(--orange); color: var(--abyss); box-shadow: 0 10px 30px -10px rgba(246,164,64,0.7); &:hover { transform: translateY(-2px); background: var(--navy); color: #ffffff; }',
 'dgc-more-btn': 'min-width: 0;', 'dgc-allcase': 'display: none;',
}
for name, body in ICONS.items():
    C[f'ico-c-{name}'] = icon_css(f'<svg viewBox="0 0 24 24">{body}</svg>', 26, True, 1.8)
if __name__ == '__main__':
    print('dups', mcp.drop_dups()); print('classes', mcp.upsert_classes(C), len(C))
