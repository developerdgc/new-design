# Homepage → editable Figma layers

These scripts rebuilt `portfolio-artifact.html` as native Figma layers (frames, text, vectors, image fills) in
https://www.figma.com/design/w3P3nS0ZtoAjzwenRXHXsa

1. `extract.js` — Playwright walks the rendered page (fonts served locally from a Google Fonts copy in `../gf`) and writes a layout tree: boxes, fills/gradients, borders, radii, shadows, text runs, inline SVG icons, images. Tiled/masked textures and SVG text are captured as small PNGs.
   `W=1440 OUT=tree-desktop.json node extract.js`
2. `prep.py desktop` — crops each image to its on-page box, then packs the tree into a PNG (`datapng.py`), because the Figma plugin runtime has no `fetch`.
3. Upload the data PNG and images with the Figma MCP `upload_assets` tool onto placeholder rectangles (`up.py uuid:file …`).
4. `builder.js` runs through `use_figma`. It decodes the PNG, then builds sections into the page frame.

The page is laid out with absolute positions, not auto-layout. Hover, scroll and popup interactions are not carried over.
