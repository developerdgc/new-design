# RedShield Water: Elementor build scripts

Builds the 13 RedShield Water pages plus header and footer on redshieldwater.emmenntech.com
through the Elementor MCP server (`/wp-json/elementor/mcp/`). Content and design match `../index.html`.

    export RS_MCP_AUTH="Basic <base64 of username:application-password>"
    python3 pages2.py home --publish   # current builder (mirrors ../index.html, 1330px container)
    python3 pages.py home          # first builder, kept for reference; or: about services pricing areas faqs tutorials contact
                                   #     leeds harrogate yorkshire ldu bds header footer
    python3 pages.py home --dry    # validate only, saves nothing

Page IDs: home 27, about 28, services 29, pricing 30, areas 31, faqs 32, tutorials 33, contact 34,
leeds 35, harrogate 36, yorkshire 37, ldu 38, bds 39; header 40, footer 41.
Images load from jsDelivr at the commit in `rsw/sha`.
After each build, `refresh_css` re-saves the first section through manage-elements, because
Elementor only regenerates a page's cached CSS on that save path.
Header (40) and footer (41) are published, so after rebuilding them run
`publish-document` on them again to push the staged autosave live.

`pages2.py` / `rs2.py` rebuild each page component by component from the artifact's CSS values.
Icons are standalone SVGs generated from the artifact sprite by `icons.py` (img/icons/), loaded through jsDelivr.
Published documents: build -> publish -> CSS refresh (manage-elements) -> publish again; `push(..., publish=True)` does this.

## Interactive extras
- **Auto-scrolling reviews**: `reviews_strip()` duplicates the cards and attaches an Elementor interaction (custom keyframes, x 0 → -50%, linear loop).
- **Before/after drag**: `ba_box()` is CSS only — the "before" layer is a `resize: horizontal` box over the "after" photo (drag the white corner handle; desktop browsers).
- **Copy buttons**: the pills carry the `rs-copy` / `rs-copy-value` classes. The click script (`copy-buttons.html`) must be added once in WP Admin → Elementor → Custom Code, because the MCP server cannot add JavaScript.
