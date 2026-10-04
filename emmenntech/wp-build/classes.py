"""Create/update V4 global classes. Usage: python3 classes.py > classes.json; python3 mcp.py elementor-manage-classes @classes.json"""
import json

FONT = "font-family: var(--em-font);"
CLASSES = {
    "em-section": "flex-direction: column; align-items: center; width: 100%; padding: 104px 24px; gap: 0px; @media(--tablet){ padding: 80px 24px; } @media(--mobile){ padding: 64px 16px; }",
    "em-wrap": "flex-direction: column; width: 100%; max-width: 1320px; padding: 0px; gap: 0px;",
    "em-band-dark": "background: #071233;",
    "em-band-light": "background: #EEF5FF;",
    "em-eb": "font-family: var(--em-mono); font-size: 12.5px; font-weight: 600; line-height: 1; letter-spacing: 0.12em; text-transform: uppercase; color: #1F6BE0;",
    "em-eb-dark": "color: #7AF0F5;",
    "em-h1": "font-size: 72px; line-height: 1.02; @media(--tablet){ font-size: 54px; } @media(--mobile){ font-size: 40px; }",
    "em-h2": "font-size: 48px; line-height: 1.08; @media(--tablet){ font-size: 38px; } @media(--mobile){ font-size: 30px; }",
    "em-h3": "font-size: 22px; line-height: 1.25;",
    "em-lead": "font-size: 18px; line-height: 1.65; color: #5B6683; @media(--mobile){ font-size: 16px; }",
    "em-on-dark": "color: #FFFFFF;",
    "em-soft-dark": "color: rgba(255,255,255,0.78);",
    "em-btn": FONT + " font-size: 15.5px; font-weight: 800; line-height: 1; padding: 15px 26px; border-radius: 50px; border-width: 1.5px; border-style: solid; border-color: transparent; width: auto; text-align: center;",
    "em-btn-g": "background: linear-gradient(90deg, #22C6E0 0%, #1F6BE0 100%); color: #FFFFFF; box-shadow: 0 12px 28px -12px rgba(31,107,224,0.8);",
    "em-btn-w": "background: #FFFFFF; color: #0C1530;",
    "em-btn-o": "background: transparent; color: #FFFFFF; border-color: rgba(255,255,255,0.45);",
    "em-btn-ol": "background: #FFFFFF; color: #0C1530; border-color: #D3E3FB;",
    "em-card": "background: #FFFFFF; border: 1px solid #D3E3FB; border-radius: 22px;",
    "em-ico": "flex: 0 0 48px; width: 48px; height: 48px; padding: 0px; border-radius: 12px; align-items: center; justify-content: center; background: linear-gradient(135deg, #22C6E0 0%, #1F6BE0 100%); color: #FFFFFF;",
    "em-ico-o": "background: linear-gradient(135deg, #FFA53D 0%, #FF5F3A 100%);",
    "em-ico-r": "border-radius: 50%;",
    "em-lift": "transition: transform 0.3s;",
    "em-zoom": "overflow: hidden;",
    "em-tile-photo": "position: relative; overflow: hidden;",
    "em-nav": "gap: 2px;",
    "em-nav-link": FONT + " font-size: 15.5px; font-weight: 700; color: rgba(255,255,255,0.88); padding: 9px 14px; border-radius: 50px;",
    "em-status": "gap: 8px; align-items: center;",
    "em-status-dot": "width: 8px; height: 8px; border-radius: 50%; background: #3BE39A; padding: 0px;",
    "em-hero": "position: relative; overflow: hidden;",
    "em-globe-slot": "position: relative;",
    "em-globe-fallback": "position: relative;",
    "em-ring": "border-radius: 50%;",
    "em-ring-rev": "border-radius: 50%;",
    "em-bob": "position: absolute;",
    "em-bob-2": "position: absolute;",
    "em-bob-3": "position: absolute;",
    "em-ticker": "width: 100%; padding: 18px 0px; background: #040B22;",
    "em-ticker-track": "gap: 22px; align-items: center; padding: 0px;",
    "em-tab": "border-radius: 16px;",
    "em-tab-num": "font-family: var(--em-mono);",
    "em-tab-go": "border-radius: 50%;",
    "em-vtab": "border-radius: 18px;",
    "em-panel": "position: relative; overflow: hidden;",
    "em-panel-bg": "position: absolute;",
    "em-chat": "gap: 14px;",
    "em-q-bubble": "border-radius: 20px 20px 20px 6px;",
    "em-acc": "gap: 12px;",
    "em-form": "gap: 14px 16px;",
    "em-input": FONT + " width: 100%; padding: 13px 14px; border-radius: 12px; border: 1px solid #D3E3FB; background: #F5F9FF; font-size: 15.5px; color: #0C1530;",
    "em-label": FONT + " font-size: 14px; font-weight: 700; color: #0C1530;",
    "em-hq-dot": "border-radius: 50%;",
    "em-footer": "background: #040B22;",
    "em-social": "transition: background 0.2s;",
    "em-wordmark": FONT + " font-weight: 900; letter-spacing: -0.04em; line-height: 0.82; text-align: center;",
    "em-nl-home": "transition: background 0.2s, color 0.2s;",
    "em-nl-about": "transition: background 0.2s, color 0.2s;",
    "em-nl-services": "transition: background 0.2s, color 0.2s;",
    "em-nl-blog": "transition: background 0.2s, color 0.2s;",
    "em-nl-contact": "transition: background 0.2s, color 0.2s;",
    "em-mobile-menu": "gap: 6px;",
    "em-cta": "position: relative; overflow: hidden;",
    "em-banner": "position: relative; overflow: hidden;",
    "em-btab": "cursor: pointer;",
    "em-nl-faq": "transition: background 0.2s, color 0.2s;",
    "em-faq-plus": "border-radius: 50%;",
    "em-jp": "position: relative;",
    "em-jp-node": "border-radius: 50%;",
    "em-jp-img": "border-radius: 16px;",
}

if __name__ == "__main__":
    import sys
    action = sys.argv[1] if len(sys.argv) > 1 else "create"
    ops = [{"action": action, "label": k, "css": v} for k, v in CLASSES.items()]
    if action == "update":
        for o in ops: o["mode"] = "replace"
    batches = [ops[i:i + 50] for i in range(0, len(ops), 50)]
    for i, bt in enumerate(batches):
        json.dump({"operations": bt}, open(f"/tmp/classes_{i}.json", "w"))
    print(len(batches))
