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
6. **SEO (skipped for now at the client's request):** Rank Math titles and descriptions from the JSON files, LocalBusiness schema, sitemap.
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

### Phase 2 (header, footer, mobile menu) - done
- Header site part **141** (published, all pages): pill bar, logo, nav, 5/5/5 mega menu with icons, call button, burger (tablet/mobile) that opens popup **133**.
- Footer site part **132** (published, all pages): "Get Connected" strip, 4 columns, policy links, copyright, Back to Top button.
- Mobile menu popup **133** (published): links, services accordion (15), call button.
- Site-wide CSS lives in the Elementor kit (post 7) custom CSS: `site/wp-build/site.css` (mega menu hover, icon fill fix, footer link colours).
- Builder scripts: `site/wp-build/*.py` (generate `elementor-build-composition` payloads).
- Notes: V4 breakpoints are only `tablet` (<=1024) and `mobile` (<=767). `build-composition` into an already-published document does not reach the live site; build into a fresh draft and publish, or use `manage-elements` + publish.

### Phase 3 (homepage) - done
- Home page **39** published (Elementor Full Width template): hero, 3-card strip, About, dark Services (6 + View All), light audit form (e-form, emails info@digiranxpro.com), Reviews (6), Why Choose Us, FAQ (6, FAQ schema on), final CTA.
- Hero visual uses the logo mark until `digiranx-hero-globe.png` is uploaded; then swap the "Hero Globe" image.
- Shared section builders: `site/wp-build/blocks.py`; page builder: `site/wp-build/b_home.py`.

### Phase 4 (inner pages + blog) - done
- Published: About Us 40, Our Services 41 (filter tabs, 15 services), Contact Us 44 (info cards, map card, form, 10 FAQs), FAQs 43 (12 FAQs in one 2-column box), Privacy 3, Terms 45, Cookie 46.
- Hero globe image (attachment 167) placed on Home.
- Blog: page 42 set as Posts page via REST; 6 posts (189, 192, 195, 198, 201, 204) with categories, slugs, excerpts, featured images and Elementor bodies.
- Theme Builder: Blog Archive **208** (include/archive, loop grid) and Blog Single Post **209** (include/singular/post).
- Site title "DigiRanx Pro", tagline "Where creative thinking meets digital growth". Sample "Hello world!" post moved to Trash.
- WordPress REST API also accepts the application password (used for settings, categories, post meta).
- Overflow check passed at 360/390/768/1024/1280px on all live pages.

### Phase 5 (15 service pages) - done
- Built from `site/content/<slug>.json` with `site/wp-build/b_service.py` (run all: `run_services.py`). Layout: hero, intro + cover, What's Included, Why Choose Us, Benefits, sidebar (All Services + Request a Quote form), Packages (3 plans), 5-step timeline, 10 FAQs (FAQ schema), call CTA.
- All 15 published with the Elementor Full Width template. URLs: /gbp-optimization/, /web-development/, /custom-web-design/, /responsive-development/, /ui-ux-designing/, /graphic-designing/, /reviews/, /seo-digital-marketing/, /landing-pages/, /software-development/, /social-media-marketing/, /branding/, /google-ads/, /citations-backlinks/, /e-commerce-solutions/.
- Image attachment 92 slug changed to `custom-web-design-image` so the page could take `/custom-web-design/`.
- Overflow check passed at 375/768/1280px on all 15 pages.

### Phase 7 (QA) - done
- All 26 pages/posts return 200, one H1 each, page titles "<Page> – DigiRanx Pro"; 30 internal links all 200.
- Alt text set on 34 Media Library images via REST (renders site-wide).
- Favicon: `digiranx-pro-favicon.png` (attachment 251) set as Site Icon.
- Custom 404 site part **252** (returns HTTP 404).
- Header nav kept on one line at 1025-1200px (kit CSS).
- Form test: contact form submitted once ("TEST - QA check"); Elementor reported "Email sent successfully" and showed the success message.
- Bug fixed: select options with "&" rendered as "&amp;amp;"; all 18 forms now use "and".
- Overflow check passed at 360/390/768/1024/1366px on all pages including 404.
- Speed: home TTFB ~0.5s (LiteSpeed cache hit), uncached inner pages 1.3-2.3s on first hit. Home ~78 requests / ~3.3 MB uncompressed (JS ~830 KB from Elementor + plugins, Roboto fonts from the default kit ~200 KB).

## Recommended next steps (manual, in WP Admin)
- LiteSpeed Cache: enable page cache for all pages, image optimisation (WebP), CSS/JS minify.
- Elementor > Settings: load Google Fonts locally; remove unused Roboto/Roboto Slab from the default kit typography.
- Deactivate unused Hostinger plugins (e.g. Hostinger Reach) if not needed.
- Install an SMTP plugin (e.g. WP Mail SMTP) so form emails reach the inbox reliably.
- Phase 6 (Rank Math meta titles/descriptions, LocalBusiness schema) when ready - copy is in `site/content/*.json`.

### Revision 1 (after client review)
- Hover fix: Elementor stores gradients as `background-image`, so class hovers that only changed `background-color` were invisible. Kit CSS now resets `background` on hover for all buttons, header call button, back-to-top and tabs (`site/wp-build/site.css`, "v2 hover system").
- Hero: shorter padding; new brighter globe `digiranx-hero-globe-v2.webp` (attachment 276), max-width 580px.
- Entrance animations (scrollIn, slide/fade) on Home: About image/copy, 6 service cards (staggered), audit copy/form, Why copy/media, final CTA (`animonly.py`).
- Header bar padding 14px (taller).
- Home audit section tightened (padding 56px, smaller heading/facts, shorter textarea).
- Paragraph sizes +1px site-wide (default p 17px; local sizes bumped via `restyle.py`).
- Forms: Urbanist font, 15.5px inputs, 14px labels, no inner padding.
- Privacy Policy page (3) had `_elementor_edit_mode` empty, so the Elementor layout never rendered; set to `builder` via REST.

### Phase 6 (SEO) - done
- Rank Math REST appeared after the setup wizard. `site/wp-build/apply_seo.py` wrote title, meta description and focus keyword for all 30 pages/posts (`seo.json`); verified live.
- Sitemaps: page-sitemap.xml and post-sitemap.xml return 200; sitemap_index.xml was a stale LiteSpeed-cached 404 (fresh request returns 200) - purge LiteSpeed cache.
- Remaining in Rank Math UI: Titles & Meta > Local SEO (address, phone, email, hours Mon-Fri 08:00-22:00); Titles & Meta > Pages > Schema Type = None (pages currently get Article schema); WP user display name shows as "Taha Dev" in Person schema.

### Hero Lottie
- Client added an Elementor Pro Lottie widget with `digiranx-globe-lottie.json` (attachment 314, loop, autoplay). Kit CSS adds a soft glow and limits it to 420px on tablet / 320px on mobile.

### Service URL hierarchy
- Page 41 slug changed to `services`; the 15 service pages now have parent 41, so URLs are `/services/<slug>/`. Old `/<slug>/` URLs 301 automatically. `/our-services/` returns 404 and needs a manual Rank Math redirect to `/services/` (the Hostinger WAF blocks the Rank Math redirection REST call).
