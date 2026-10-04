# Kylie Washington Studio: Shopify project context

**For a new Claude session:** read this whole file first. It is the handoff from the previous session (Sep 30 – Oct 4, 2026). The user writes in Roman Urdu; reply in Roman Urdu. Client-facing messages are in English.

---

## 1. Project in one paragraph
The user (a developer with collaborator access through their organisation's Partner dashboard) is building a Shopify store for **Kylie Washington**, an Australian contemporary artist (Pearl Beach, NSW Central Coast). She sells **original paintings** and **limited edition fine art prints**. The site should feel **70% artist/gallery, 30% shop**: lots of white space, large artwork images, no pop-ups, no "SALE" styling. The client bought the paid **Prestige** theme and wants to keep it.

- Currency: **AUD**. Shipping: free within Australia, no international shipping (PDF policy).
- Old site (Canva): https://kyliewashington.com/ (single page, images in `_assets/media/`)
- Shopify Files CDN prefix: `https://cdn.shopify.com/s/files/1/0711/2769/5411/files/`
- Contact email in brief: kyliewashington@mail.com · Instagram/YouTube: @kyliewashington_art

## 2. Source documents (`source-docs/`)
| File | What it is |
|---|---|
| `brief-KYLIE_WASHINGTON.docx` | Original long creative brief (gallery positioning, homepage wireframe, print variants with canvas/frames, SEO, phasing). Partly superseded |
| `brief-Share_w_Ali.pdf` | Newer brief: menu, About text, Fine Art Prints intro, Wholesale text (**copied word-for-word from terrimaddenstudio.com, must be rewritten**), Terms of Service, Shipping policy, gift card and FAQ requests. Licensing link in it is wrong (points to a Springer article) |

### Latest client instructions (Oct 1, 2026). These override the briefs
1. Main categories: **Originals, Fine Art Prints, Licencing, Studio**
2. Print pricing like https://emhatton.com.au/products/year-of-the-horse-girls-ii-2 : one "Size" option, price updates on selection. Same prices for every print.
3. Page structure like **terrimaddenstudio.com**, with everything else under **Studio**
4. Only prints have size options. Painting sizes come from the client's Excel sheet.
5. Prints: rectangular works sell as **A4 / A3 / A2**. Square works: **40×40 $80 · 50×50 $120 · 75×75 $250**.
6. Excel sheet has name + availability. Sold paintings go to the **Archive** under Originals. **No edition numbers yet**.

## 3. What is DONE in Shopify
- **Metafield definitions** (Products, all Single line text): `custom.custom_year`, `custom.custom_medium`, `custom.custom_dimensions`, `custom.custom_framing`. Note the doubled `custom_` in the key.
- **Originals: 57 products imported with images** (`csv/kylie-washington_originals_WITH-IMAGES.csv`). 37 available, 20 sold (price $0, qty 0, tags `Sold`, `Archive`). Banksia 120×55 has price $0 + tag `Price Pending`. Colour Studies = 1 product with 4 variants. Year/medium are placeholders (2026, Acrylic on canvas).
- **Fine Art Prints: 45 products imported with images** (`csv/kylie-washington_fine-art-prints_FINAL.csv`). 19 square (Small 40×40 / Medium 50×50 / Large 75×75) and 26 rectangle (A4 / A3 / A2). All sizes $80 / $120 / $250 (A-size prices are an **assumption**, awaiting client). Inventory not tracked. "Orchid" print has no image (pending). Grevillea Spinning was removed (not in client list).
- All products are **Draft**.
- **Collections** (automated, by tag): Originals (`Originals` AND inventory > 0), Archive (`Originals` AND inventory < 1), Fine Art Prints (`Fine Art Prints`), Banksia (`Subject: Banksia`), Australian Flora (`Subject: Australian Flora`), Featured (manual, 4 homepage paintings).
- ⚠️ **Never delete products.** Deleting a product also deleted its images from Content → Files. To change products, re-import with "Overwrite products with matching handles".

## 4. Open questions sent to the client (final email, Oct 4)
1. A4/A3/A2 prices = $80/$120/$250?
2. "Orchid" print: on the list? (draft, no image)
3. Medium/year placeholders: which paintings differ?
4. Ceramics: images, titles, prices if selling (mentioned in PDF, no products exist)
5. Radical Radiance / Current Collection: still wanted? Which works?
6. Series collections (We Are The Stars, Birds Flocking, Berry Me, Tripdick, Waratah)?

Smaller items still unconfirmed: Morning vs "First Light" (old site says 30×30 $250), Waratahs ($150) shown as sold on the old site, "Madnolia" vs "Magnolia" title, are paintings signed / certificate of authenticity, Returns policy text, correct Licencing text, "Licencing" vs "Licensing" spelling (client's spelling used).

## 5. Reference sites analysed
| Site | Use it for |
|---|---|
| **terrimaddenstudio.com** (Shopify "Studio" theme) | **Main structure model**. Menu: Originals ▸ Available Originals, Archive · Fine Art Prints · Licensing · Studio ▸ About, Wholesale, Contact, Studio Journal, guides, Fine Art Print FAQs. Homepage: announcement bar → hero with 2 buttons → "The Studio" rich text → 3 columns (Originals / Prints / Licensing) → featured originals → testimonial → featured prints → gift certificate banner → "Created with care" image+text → newsletter. Original product tabs: About the Artwork / Details (Medium, Size, Finish, Presentation, Year) / Collecting this Artwork / Shipping. Licensing page: who it's for → how it works → what's included → pricing → enquire. Contact: general + media. Gift card $50/$100/$200/$500, 3 years valid |
| **www.alowgallery.com.au** (Squarespace) | Visual tone: few items, big headings ("ART LIVES ON WALLS"), caption under each work: *Title, Year · Medium · Size · Price* |
| **www.claudiokirac.com.au** (Shopify Studio theme) | Credibility strip (collections / seen in / accolades), "Art in real spaces" blog, commission process page, print variants as one "Size & Material" option |
| **stephbrookestudio.com** | Functional only: size-then-style selectors, shipping info icons, "Explore by colour" circles, "Our promise" icons |
| **emhatton.com.au** | Print size selector + price change (client's explicit example) |

## 6. Agreed site structure (follow this)
```
HEADER
Originals ▾        Available Originals (/collections/originals) · Archive (/collections/archive)
Fine Art Prints    /collections/fine-art-prints
Licencing          /pages/licencing
Studio ▾           About · Wholesale · Contact · Studio Journal (/blogs/journal) · Fine Art Print FAQs

FOOTER
Gift Certificate · FAQs · Shipping · Returns · Terms · Privacy · Instagram · YouTube · Newsletter ("Join the collectors list")
```
Dropped from earlier plans: Projects menu, Commissions page, Banksia/Australian Flora in the menu (the collections stay), Radical Radiance/Current, Explore by Colour, "See it in your space".

### Homepage (Terri Madden style)
0 Announcement bar ("Free shipping Australia-wide") · 1 Hero, 1 image + 2 buttons (View Originals / Shop Prints) · 2 "The Studio" intro (About text) · 3 Three columns: Originals / Fine Art Prints / Licencing · 4 Featured originals (4–6, caption Title, Year · Medium · Size · Price) · 5 Testimonial/credibility (if client provides) · 6 Featured prints (6) · 7 Gift certificate banner · 8 "Created with care" · 9 Newsletter

### Templates
- `product.original`: big gallery, "Acquire this work" button, Enquire link, tabs: About the Work / Artwork Details (metafields via dynamic source) / Collecting this Work / Delivery. No quantity selector.
- `product.print`: Size buttons, price updates, size note, tabs: Print Details / Sizes / Delivery.
- `collection`: 2–3 per row, natural image ratio (never crop paintings), filters via Search & Discovery (tags: Size, Subject, Colour, Shape).
- `collection.archive`: hide price, show "Sold".
- Custom code needed in Prestige: caption with year/medium/size on product cards; "Sold" instead of price on sold originals.

### Design system
Background `#F7F5F1`, text `#1F1D1B`, muted `#6E6962`, lines `#E3DED6`, charcoal buttons. Strong contemporary sans headings (uppercase, letter-spaced), clean sans body. Turn OFF: newsletter popup, quick view/add, hover second image, vendor, reviews, sale badges. Theme text: "Add to cart" → "Acquire this work" (originals), "Sold out" → "Sold".

### Pages content status
About ✅ (PDF) · FAQ ✅ draft in `reports/fine-art-prints-FAQ_draft.md` · Contact ✅ · Wholesale 🔨 rewrite (PDF text is copied) · Licencing 🔨 Terri structure, client text needed · Studio Journal ⏳ client stories · Gift card 🔨 create · Policies: Terms ✅, Shipping ✅ (PDF), Returns ❌, Privacy (Shopify template)

## 7. NEXT PHASE: theme build (not started)
Plan: Claude edits the theme via **Shopify CLI + Theme Access** on a duplicated theme; data (pages, menus) via the Shopify connector.
User setup checklist:
1. Duplicate Prestige → name **"Prestige – Kylie Build"** (never edit live theme)
2. Install **Theme Access** app → password `shptka_…`
3. Environment secrets: `SHOPIFY_FLAG_STORE` (xxx.myshopify.com), `SHOPIFY_CLI_THEME_TOKEN`, optional `STORE_PASSWORD`
4. Network allowlist: `*.myshopify.com`, `*.shopify.com`, `cdn.shopify.com`
5. Shopify connector connected at https://claude.ai/customize/connectors, then start a new session

First steps in the new session: test the connector (`get-shop-info`), `npm i -g @shopify/cli`, `shopify theme list`, `shopify theme pull --theme "Prestige – Kylie Build"`, list the available Prestige sections, then Phase A (theme settings) → B (templates + custom code) → C (pages, menus) → D (homepage) → E (remaining pages) → F (mobile QA). Estimate ~10–15 h of build plus client content waits. Never publish the theme; the user publishes.

### Status, Oct 4 2026 (session 2)
- Connector OK: store `7m41tm-1v.myshopify.com` ("My Store", Basic, AUD, AEDT). Env secrets `SHOPIFY_FLAG_STORE`, `SHOPIFY_CLI_THEME_TOKEN`, `STORE_PASSWORD` are set. Shopify CLI 4.8.4 works.
- Themes: Horizon `#145878089779` (live) · Prestige 11.4.1 `#145878188083` (unpublished, complete, ~220 files) · **Prestige – New Build `#146128306227`** (unpublished; the duplicate was named this instead of "Kylie Build").
- ⚠️ **"Prestige – New Build" `#146128306227` is incomplete on Shopify itself**: only 98 files (no `snippets/`, no `templates/`). Confirmed via Admin API `theme.files`. Do NOT use it; the user can delete it.
- ✅ **Build theme = "Prestige – Kylie Build" `#146130927667`** (unpublished). Created by pulling the complete Prestige and `shopify theme push --unpublished`. Verified complete via Admin API. Local copy: `kylie-washington/theme/` (in git). Work flow: edit locally → `shopify theme push --theme 146130927667 --path kylie-washington/theme` (never `--publish`, never `--allow-live`). Pull first if the user changed settings in the editor.
- Editor: https://7m41tm-1v.myshopify.com/admin/themes/146130927667/editor · Preview: https://7m41tm-1v.myshopify.com?preview_theme_id=146130927667
- Prestige sections usable on the homepage: announcement-bar, slideshow, image-with-text-overlay, rich-text, multi-column, featured-collections, testimonials, image-with-text, newsletter (+ others in `reports/prestige-sections.md`).

### Phase A (theme settings): DONE Oct 4, pushed to #146130927667
- `config/settings_data.json` `current` is now an object (was the "Prestige" preset). Colour schemes: 1 = paper `#f7f5f1`/ink `#1f1d1b` (default) · 2 = white (modals/drawers) · 3 = ink dark · 4 = transparent/white text (image overlays) · 5 = line-beige `#e3ded6`.
- Fonts (changed in Phase B at user's request for something more distinctive): headings **Tenor Sans** uppercase, letter spacing 12; body **Karla**, 16px desktop / 15px mobile. Confirmed loading on the preview. Buttons heading font, uppercase, square corners. Section spacing `lg`.
- Product cards: natural ratio, no hover image, no vendor, no rating, no quick buy, no discount badge, colour swatches hidden, body font. Sale accent set to ink (no red). Image zoom on hover off.
- Newsletter popup disabled (`overlay-group.json`). Free shipping bar off. Empty cart link → Originals.
- Locale `en.default.json`: "Sold out" → "Sold" (button + badge).
- Social: instagram.com/kyliewashington_art, youtube.com/@kyliewashington_art (URL format assumed; confirm).
- Not settable in theme settings, do in Phase B CSS: muted text `#6E6962`, line colour `#E3DED6`. Favicon/logo: need files from client.
- Playwright screenshots of the preview fail with ERR_CERT_AUTHORITY_INVALID through the sandbox proxy; verify visually via the preview link instead.

### Phase B (templates + custom code): DONE Oct 4, pushed to #146130927667
- `templates/product.original.json`: title, price, variant picker (Colour Studies), buy button "Acquire this work" (no quantity, no dynamic checkout), outline "Enquire about this work" button → /pages/contact, accordions About the Work (description) / Artwork Details (`snippets/artwork-details.liquid`, metafields) / Collecting this Work / Delivery (text from client shipping policy). Sticky add to cart off. Related products below.
- `templates/product.print.json`: size buttons (block style, price updates), print note, buy button, accordions Print Details / Sizes (built from the product's own Size option values) / Delivery (14-day print-to-order).
- `templates/collection.json` + `collection.archive.json`: title banner without image, 3 per row desktop / 1 per row mobile, wider spacing, filter drawer, no grid switcher/result count. Archive has no sort.
- Assigned via Admin API: 57 Originals → `original`, 45 prints → `print`, Archive collection → `archive`. (Live Horizon theme has no such templates, so it falls back to its default; harmless.)
- Custom code: `snippets/artwork-caption.liquid` (Year · Medium · Size under cards for products tagged `Originals`); `product-card.liquid` shows "Sold" instead of price for tag `Sold`; `buy-buttons.liquid` uses `product.general.acquire_button` for tag `Originals`; `assets/kylie.css` (muted #6E6962, details list) loaded in `layout/theme.liquid`; `acquire_button` key added to every locale.
- Verified Oct 4: temporarily set A Poem With AI + Wattle Me to Active and published to Online Store, checked both product templates on the preview (all tabs, metafield details, Acquire/Enquire buttons, size buttons, card caption), then set both back to **Draft**. They are still *published* to the Online Store channel (unpublish is blocked by the connector) but Draft keeps them hidden.
- Preview check from the sandbox works with curl (cookie jar + POST /password with `$STORE_PASSWORD`, then `?preview_theme_id=`); Playwright does not (TLS).

### Phase C (pages + menus): DONE Oct 4
- Pages created (all published; store is password protected): `about` (client text, PDF), `wholesale` (template `page.wholesale`, **rewritten by Claude**, needs client OK), `licencing` (template `page.licencing`, **structure + draft text by Claude**, client must supply real text and images), `fine-art-print-faqs` (template `page.faq`, 15 questions from `reports/fine-art-prints-FAQ_draft.md`; unconfirmed items left out: signed/numbered, edition size, paper name, packaging, change-of-mind returns, gift card). `contact` already existed.
- Blog `journal` (Studio Journal) created, empty. Old `news` blog left as is.
- New menus `kw-main` and `kw-footer` (the existing `main-menu`/`footer` are used by the live Horizon theme, so they were NOT touched). Kylie Build header uses `kw-main`, footer links use `kw-footer`.
- Footer menu links to /policies/shipping-policy, refund-policy, terms-of-service: these 404 until policies are added (Phase E). Only Privacy exists.
- Header group: demo countdown removed, announcement bar "Free shipping Australia-wide" (scheme 5), logo left + inline nav, country selector off. Footer group: demo icon row removed; blocks Kylie Washington Studio text / Information menu / "Join the collectors list" newsletter; Powered by Shopify off.
- Forms: Contact (Phone, Enquiry type dropdown), Wholesale (Business name*, Website/Instagram, Business type, Location), Licencing (Company, Artworks, Intended use, Territory and duration). All submissions go to the store email.
- ⚠️ Store name is still "My Store" (shows in header + footer). User must change it in Settings → Store details to "Kylie Washington Studio", or upload a logo.
- Gift Certificate not in footer yet: no gift card product exists (connector blocks gift card writes); create in admin.

## 8. Files in this folder
- `csv/`: Shopify import CSVs (originals with/without images, prints FINAL with images)
- `reports/`: image match reports, FAQ draft
- `scripts/`: Python generators used (`build_paintings.py`, `build_prints.py`, `add_images.py`) and the image→product maps (`map.py`, `pmap.py`, `newfiles.json`). Paths inside the scripts point to the old session scratchpad, so adjust them before re-running.
- `source-docs/`: client briefs
- Product images themselves are already in Shopify Content → Files and are not stored here. Dropbox source folders: Paintings `https://www.dropbox.com/scl/fo/gneb4m57m822xeuh3mynx/...` and Prints `https://www.dropbox.com/scl/fo/8x295966lx5j8bcdlmv7p/...` (ask the user for full links if needed).
