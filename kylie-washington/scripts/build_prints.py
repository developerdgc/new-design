import csv, re
# (title, subjects, colours, intro line)
P = [
("Wattle Me",["Wattle","Australian Flora"],["Yellow"],"A playful, golden celebration of wattle, Australia's national floral emblem and one of the first plants to return after fire."),
("Dusk Protea",["Protea","Botanical"],[],"The sculptural protea caught in the soft, fading light of dusk."),
("I'll Leave The Light On",[],[],"A warm, reassuring work about home, welcome and the light kept burning for someone you love."),
("Slipstreaming",[],[],"A work about movement and momentum, and the currents that carry us forward."),
("Cordelia Shadows",[],[],"An atmospheric work built on the interplay of light and shadow."),
("Queen of the Slipstream",[],[],"A confident work about riding the currents of change with grace and poise."),
("Ferning",["Botanical"],[],"Inspired by unfurling fern fronds and the patterns of new growth."),
("Etching 1",[],[],"A study in line and texture, the first of a pair of works titled Etching."),
("Etching 2",[],[],"A study in line and texture, the second of a pair of works titled Etching."),
("Blood on the Table",[],[],"A striking, provocative work that invites a second look."),
("Banksia Typography",["Banksia","Australian Flora"],[],"The banksia reimagined through typography, featuring the place names of Pearl Beach and Patonga, home to Kylie's studio."),
("Vessel",[],[],"A work about holding and carrying: the vessel as a form, and as a metaphor for what we hold within."),
("Underwater Roll",["Ocean"],[],"A fluid, immersive work inspired by movement beneath the surface of the water."),
("Turn Lights On Pink",[],["Pink"],"One of a pair of works about energy and attraction, about being lit up by someone or something. This version is in pink."),
("Turn Lights On Red",[],["Red"],"One of a pair of works about energy and attraction, about being lit up by someone or something. This version is in red."),
("Tripdick 1",[],[],"Part one of a cheeky three-part series (a play on 'triptych'), designed to hang alone or together as a set."),
("Tripdick 2",[],[],"Part two of a cheeky three-part series (a play on 'triptych'), designed to hang alone or together as a set."),
("Tripdick 3",[],[],"Part three of a cheeky three-part series (a play on 'triptych'), designed to hang alone or together as a set."),
("Dinner",[],[],"A work about the family dinner table and the ritual of gathering, where the days are long and the years are short."),
("The Chosen One",[],[],"A confident work with a title that carries personality and a wink of humour."),
("Starry Ghosts",["Stars"],[],"A dreamy, nocturnal work connecting the Australian landscape with the night sky."),
("Smoky Amber",[],["Amber"],"Warm amber tones and a smoky atmosphere that evoke the Australian bush."),
("Shadow Light Tips",["Botanical"],[],"Botanical tips caught between shadow and light."),
("Red Light District Gum",["Eucalyptus","Australian Flora"],["Red"],"A cheeky, bold take on the Australian gum, with a title full of wit."),
("Rays",[],[],"A work about light, warmth and radiance."),
("Tips",["Botanical"],[],"A close study of botanical tips, the growing points where new life begins."),
("Orchid Cut",["Orchid","Botanical"],[],"The orchid reimagined through cut and collage, fragmenting the bloom into bold new forms."),
("Night Spawning",["Ocean"],[],"Inspired by the mysterious rhythms of life after dark, when nature quietly renews itself."),
("Milk Blossom",["Botanical"],[],"A soft, delicate celebration of blossom."),
("Magnolia",["Botanical"],[],"A celebration of the magnolia's generous, sculptural bloom."),
("Light Touch Lily",["Botanical"],[],"The lily rendered with a light touch: delicate, graceful and luminous."),
("Home Is Where The Heart Is",[],[],"A warm work about belonging, and the places and people that make a home."),
("Gummy Bear",["Eucalyptus","Australian Flora"],[],"A playful take on the Australian gum, full of humour."),
("Glory Fingers",["Botanical"],[],"A lively botanical work with a playful title and a sense of reaching, upward growth."),
("From The Darkness Comes Light",[],[],"A work about hope and renewal: the light that follows darkness, just as the bush regenerates after fire."),
("Everyone Loves Limes",["Fruit"],["Green"],"A zesty, cheerful celebration of the lime, a companion to Everyone Loves Lemons."),
("Everyone Loves Lemons",["Fruit"],["Yellow"],"A bright, sunny celebration of the lemon, a favourite from backyard trees across Australia."),
("Centre Point",[],[],"A work about focus and balance that draws the eye to its centre."),
("Pining",[],[],"A work about longing, with a title that plays on the feeling of missing someone."),
("Noose Around Her Neck",[],[],"A powerful, emotionally charged work exploring pressure, constraint and resilience."),
("Moonlight Banksia",["Banksia","Australian Flora"],[],"The banksia under moonlight, a nocturnal view of the plant at the heart of Kylie's practice."),
("Orchid",["Orchid","Botanical"],[],"An elegant celebration of the orchid, delicate yet surprisingly resilient."),
("Blushing",[],["Pink"],"A soft, tender work in blushing tones."),
("Not How I Was Feeling",[],[],"An honest, emotional work about the gap between how things look and how we feel."),
("Spinning Me Around",[],[],"A work full of movement and energy, about the people and moments that turn our world around."),
]
STD = ("<p>Created from Kylie Washington's original artwork, each fine art print captures the colour, texture and expressive energy of the original work. "
       "Printed in Australia on museum-grade fine art paper using archival inks, these high-quality prints are designed to retain their depth and vibrancy for years to come.</p>"
       "<ul><li>Limited edition</li><li>Museum-grade fine art paper, archival inks</li><li>{sizes}</li><li>Frame not included</li>"
       "<li>Printed to order and usually dispatched within 14 days</li><li>Free shipping within Australia</li>"
       "<li>Custom sizes available on request. Please enquire.</li></ul>")
SQUARE={"Etching 1","Etching 2","Underwater Roll","Turn Lights On Pink","Turn Lights On Red","The Chosen One","Starry Ghosts","Smoky Amber","Night Spawning","Milk Blossom","Magnolia","Home Is Where The Heart Is","Glory Fingers","Centre Point","Pining","Noose Around Her Neck","Blushing","Not How I Was Feeling","Orchid"}
SQ=[("Small - 40 x 40 cm",80,"S"),("Medium - 50 x 50 cm",120,"M"),("Large - 75 x 75 cm",250,"L")]
RECT=[("A4 - 21 x 29.7 cm",80,"A4"),("A3 - 29.7 x 42 cm",120,"A3"),("A2 - 42 x 59.4 cm",250,"A2")]
META=["Year (product.metafields.custom.custom_year)","Medium (product.metafields.custom.custom_medium)",
      "Dimensions (product.metafields.custom.custom_dimensions)","Framing (product.metafields.custom.custom_framing)"]
H=["Handle","Title","Body (HTML)","Vendor","Product Category","Type","Tags","Published","Option1 Name","Option1 Value",
   "Variant SKU","Variant Grams","Variant Inventory Tracker","Variant Inventory Qty","Variant Inventory Policy",
   "Variant Fulfillment Service","Variant Price","Variant Compare At Price","Variant Requires Shipping","Variant Taxable",
   "Variant Barcode","Image Src","Image Position","Image Alt Text","Gift Card","SEO Title","SEO Description",
   "Variant Weight Unit","Status"]+META
def slug(t): return re.sub(r'-+','-',re.sub(r'[^a-z0-9]+','-',t.lower().replace("'",""))).strip('-')
rows=[];hs=set()
for i,(t,subj,cols,line) in enumerate(P,1):
    h=slug(t)+"-fine-art-print"; assert h not in hs; hs.add(h)
    sq=t in SQUARE; SIZES=SQ if sq else RECT
    tags=["Fine Art Prints","Prints","Limited Edition","Shape: "+("Square" if sq else "Rectangle")]+["Subject: "+s for s in subj]+["Colour: "+c for c in cols]
    for j,(sz,pr,code) in enumerate(SIZES):
        v={"Handle":h,"Option1 Name":"Size","Option1 Value":sz,"Variant SKU":f"KW-PR-{i:03d}-{code}",
           "Variant Inventory Tracker":"","Variant Inventory Policy":"continue","Variant Fulfillment Service":"manual",
           "Variant Price":f"{pr:.2f}","Variant Requires Shipping":"TRUE","Variant Taxable":"TRUE","Variant Weight Unit":"kg"}
        if j==0:
            v.update({"Title":t,"Body (HTML)":f"<p>{line}</p>"+STD.format(sizes=("Square print: 40 x 40 cm, 50 x 50 cm or 75 x 75 cm" if sq else "Printed to standard A4, A3 or A2 paper sizes")),"Vendor":"Kylie Washington","Type":"Fine Art Print",
                "Tags":", ".join(tags),"Published":"FALSE","Gift Card":"FALSE",
                "SEO Title":f"{t} | Limited Edition Fine Art Print by Kylie Washington",
                "SEO Description":f"{t}, a limited edition fine art print by Australian artist Kylie Washington. Archival inks on museum-grade paper. Free shipping in Australia.",
                "Status":"draft",META[0]:"2026",META[1]:"Archival inks on museum-grade fine art paper",META[2]:("40 x 40 cm / 50 x 50 cm / 75 x 75 cm" if sq else "A4 / A3 / A2"),META[3]:"Unframed"})
        rows.append(v)
out="kylie-washington_fine-art-prints_shopify-import.csv"
with open(out,"w",newline="",encoding="utf-8") as f:
    w=csv.DictWriter(f,fieldnames=H);w.writeheader();[w.writerow(r) for r in rows]
print(len(P),"products",len(rows),"rows")
