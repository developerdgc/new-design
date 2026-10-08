# DGC Portfolio homepage: Figma export

## Import into Figma
1. Open a Figma design file.
2. Drag `DGC-Homepage-Desktop-Figma.svg` (1440 px wide) and `DGC-Homepage-Mobile-Figma.svg` (390 px wide) onto the canvas.
3. Each SVG arrives as a frame with one named layer per section: Header, Hero + Video Reviews, Stats, Work, How We Work, About, Testimonials, CTA and Footer.

The images are sharp at 2x (desktop) and 3x (mobile). Tall sections are split into tiles of 4000 px or less, so Figma does not downscale them.

The section PNGs (`desktop-0N-*.png` and `mobile-0N-*.png`) are the same sections as individual images. `desktop-full-homepage.jpg` is a quick 1x preview of the whole page.

These layers are pixel images. Text and shapes are **not editable**. For fully editable layers, use one of these:
- import the live page with the **html.to.design** Figma plugin, or
- connect the Figma connector in Claude so the page can be rebuilt as native Figma layers.

## Design tokens (create these as Figma styles)

| Token | Hex | Use |
|---|---|---|
| Navy | `#062836` | Dark sections, hero |
| Navy 2 | `#04202c` | Deeper panels |
| Navy 3 | `#0a3546` | Cards on dark |
| Abyss | `#021720` | Darkest shade |
| Teal | `#116466` | Active tab, footer gradient |
| Cyan | `#1cdee1` | Accent text, glows |
| Orange | `#f6a440` | Primary buttons, accents |
| Orange ink | `#b9650c` | Orange text on white |
| Ink | `#071c25` | Headings on white |
| Body text (white sections) | `#181818` | Paragraphs |
| Ink 3 | `#6a7d85` | Muted labels |
| Fog | `#b9cdd3` | Paragraphs on dark |
| Mist | `#eef5f6` | Light section background |
| Line | `#dde8ea` | Borders |
| Paper | `#ffffff` | White |

**Fonts:** headings use **Unbounded** (600, 700 and 800). Body text uses **Manrope** (400 to 800). Both are on Google Fonts.

**Radius:** 10 px maximum. **Buttons:** on hover, both the background and the text colour change.
