# DigiRanx Pro: Elementor Build Plan

Source of truth for the design: `site/index.html` (published preview: https://claude.ai/artifact/H5QiHQs84cL951cnx64Txu).
Service page copy: `site/content/<slug>.json` (intro, why, benefits, steps, 6 FAQs, CTA, meta title and description).
Shared data (services, packages, reviews, general FAQs, blog posts, policies): inside the `<script>` of `site/index.html`.

## Stack
- Fresh WordPress, Hello Elementor theme, Elementor + Elementor Pro.
- Build from scratch with Flexbox Containers. Do not import the Xcelliance kit.
- Minimal plugins: Rank Math (SEO), plus a cache plugin later. No extra add-on packs.

## Global settings (Site Settings)
| Token | Value |
|---|---|
| Primary (violet) | `#7B3BFF` |
| Secondary (cyan) | `#1EC8F5` |
| Accent (magenta) | `#FF2EA6` |
| Text | `#16141F` |
| Heading | `#0E0A1F` |
| Navy (dark sections, footer) | `#110A2E` |
| Navy deep | `#0A0620` |
| Light section | `#F1EDFC` |
| Card tint | `#F7F3FF` |
| Card border | `#DCCFFF` |
| Button gradient | `#16B4F0` to `#7B3BFF` (90deg) |

- Font: Urbanist (400 to 800) for everything. Headings: Transform = Capitalize.
- Type: Hero H1 62px, page H1 56px, H2 38px, H3 20 to 24px, body 16px / 1.65.
- Content width 1320px, side padding 24px. Section padding 56 to 84px.
- Radius: cards and containers 10px, buttons 8px.
- Hover rule: light sections hover to navy bg + white text; dark sections hover to white or cyan bg + navy text.
- Breakpoints to check: 320, 375, 414, 768, 1024, 1280, 1366, 1920.

## Phases
1. **Setup:** Site Settings (colours, fonts, buttons, layout width), permalinks, create all pages, upload logo and images (`site/img`, `site/logo-*.png`).
2. **Theme Builder:** Header (pill bar, Menu widget with mega menu 5/5/5, call button), Footer ("Get connected" strip + 4 columns + policy links), Back to Top.
3. **Homepage:** Hero (texture bg + 3D globe), 3-card strip, About, dark Services band (6 + View All), light audit form, Reviews (world-dots bg), Why Choose Us, FAQ (split layout, 6), final CTA.
4. **Inner pages:** About, Services listing (15 + filter), Contact, FAQs (2-column box, 12), Blog archive + Single Post template, Privacy Policy, Terms & Conditions, Cookie Policy.
5. **15 service pages:** one master layout (Hero, Intro + What's Included, Why Choose Us, Benefits, Packages, Steps timeline, 10 FAQs, call CTA; sidebar with All Services + Request a Quote form), then duplicate and fill from `site/content/<slug>.json`.
6. **SEO:** Rank Math titles and descriptions from the JSON files, LocalBusiness schema, sitemap.
7. **QA:** responsive pass, form emails to info@digiranxpro.com, speed check.

## Before going live
- Replace placeholder claims: hero "4.9 rating", the AI-written reviews, and package prices if they change.
- Add real social media links.
- Have the policy pages reviewed.

## Progress log
### Phase 1 (setup) - done via MCP on 2 Oct 2026
- 18 V4 global variables (`dg-*` colours, `dg-font` Urbanist, radius, container, section padding).
- Site-wide default styles for h1-h6, p, a (Urbanist, capitalised headings, dark text).
- 22 global classes: `dg-section`, `dg-wrap`, `dg-bg-light`, `dg-bg-dark`, `dg-sec-head(-center)`, `dg-eyebrow(-dark)`, `dg-lead`, `dg-btn` + `dg-btn-grad|white|outline|ghost-w` (+ `-on-dark` hover modifiers), `dg-card(-tint)`, `dg-icon-box`, `dg-icon-circle`, `dg-text-white`, `dg-text-soft-white`.
- Draft pages (post IDs): Home 39, About Us 40, Our Services 41, Blog 42, FAQs 43, Contact Us 44, Terms & Conditions 45, Cookie Policy 46, Privacy Policy 3.
  Services: GBP 47, Web Development 48, Custom Web Design 49, Responsive Development 50, UI/UX 51, Graphic 52, Reviews 53, SEO 54, Landing Pages 55, Software 56, Social Media 57, Branding 58, Google Ads 59, Citations & Backlinks 60, E-commerce 61.
- Media upload pack: `site/wp-upload/` (SEO-named images, logos, SVG icons). MCP cannot upload media; upload manually.
- `site/tools-mcp.py`: CLI client for the MCP server (reads `DIGIRANX_MCP_AUTH`).
