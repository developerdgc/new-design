import csv, re

SOLD = " This work has been acquired and now forms part of the artist's archive."

# (title, dims "WxH" or "", price or None, sold, framing, medium, subjects, colours, description)
P = [
("Ghost Gum","60x60",None,True,"",None,["Australian Flora","Eucalyptus"],[],
 "The ghost gum is one of the most recognisable forms in the Australian landscape: pale, luminous and quietly enduring. In Ghost Gum, Kylie Washington returns to the tree as a symbol of resilience, a form that sheds its bark, weathers drought and fire, and continues to stand. The painting holds the tension between stillness and survival, drawing attention to the smooth, almost glowing trunk. Like much of Kylie's work, it asks us to look more closely at what grows around us, and at what it teaches us about renewal."),
("Banksia Serrata","58x68",None,True,"",None,["Banksia","Australian Flora"],[],
 "Banksia serrata, the old man banksia, grows along Australia's east coast and sits at the heart of Kylie Washington's visual language. Gnarled, serrated and built to survive fire, the banksia becomes more than a botanical subject here; it stands for adaptation and regeneration. This painting celebrates the plant's sculptural character: the textured cones, the saw-toothed leaves and the sense of a form shaped by time and weather. It is a portrait of endurance, made with warmth and close attention."),
("You Can Rain On Me","30x40x4",250,False,"","Acrylic on wooden board",[],[],
 "You Can Rain On Me is an invitation to welcome what arrives rather than resist it. Painted on wooden board, the work carries the idea that rain, like difficulty, is also what makes growth possible. In the Australian landscape, rain after a long dry spell is a moment of release and renewal, and this painting holds that feeling of relief and optimism. The intimate scale and the warmth of the timber surface give the work a tactile, personal quality, suited to a space where it can be seen up close."),
]
STARS = "{t} is one of a series of small works exploring a single idea through different colour moods. The title speaks to connection: the notion that we are made of the same material as the night sky, and that each of us carries a small light of our own. In this version, {c} Intimate in scale, it works beautifully on its own or grouped with others from the series, and makes a considered first original for a new collector."
for col, line in [("Yellow","yellow brings warmth and brightness, a sense of morning rather than night."),
                  ("Green","green brings a quieter, botanical calm, connecting the work to growth and the natural world."),
                  ("Purple","purple lends a dusky, dreamlike depth, somewhere between twilight and night."),
                  ("Red","red adds energy and heat, a pulse of intensity within the series.")]:
    t=f"We Are The Stars ({col})"
    P.append((t,"21x25",150,False,"","Acrylic on board",["Stars"],[col],STARS.format(t=t,c=line)))
P += [
("A Poem With AI","140x95",750,False,"",None,[],[],
 "A Poem With AI is a large-scale work that reflects on creativity at a moment of rapid technological change. The title suggests a dialogue between the human hand and a new kind of intelligence, between intuition and algorithm. Rather than choosing a side, the painting sits within the question of what it means to make something meaningful now. At 140 × 95 cm it is a statement piece, with the presence to anchor a living room, hallway or workspace, and to spark conversation."),
("We Are The Stars","115x81",None,True,"",None,["Stars"],[],
 "The large work that gives its name to the We Are The Stars series, this painting explores connection, belonging and the idea that we share the same origins as the night sky. At 115 × 81 cm it has an immersive presence, inviting the viewer to step into its field of colour and light. The smaller works in the series revisit the same idea in intimate form."),
("I Promise This Is The Last One","30x20",150,False,"",None,[],[],
 "The title of this small painting reads as a wry, honest nod to the artist's compulsion to keep making just one more. I Promise This Is The Last One captures that familiar studio moment when an idea won't let go. Compact at 30 × 20 cm, it has the spontaneity of a work made in the flow of practice, and brings a playful, personal note to a shelf, desk or gallery wall."),
("Banksia x Two","30x30",150,False,"",None,["Banksia","Australian Flora"],[],
 "Two banksia forms sit side by side in this intimate square work, a quiet study in companionship and pairing. The banksia is a recurring motif in Kylie Washington's practice, a plant that survives fire, reseeds and returns, and here it becomes a meditation on growth shared rather than alone. At 30 × 30 cm, the work is ideal for smaller walls, or to be grouped with other works from the Banksia series."),
("Banksia Monstera","30x30",150,False,"",None,["Banksia","Australian Flora"],[],
 "Banksia Monstera brings together two very different botanical worlds: the hardy Australian banksia and the lush, sculptural leaves of the monstera. The pairing sets resilience beside abundance and native bushland beside the indoor garden, creating a playful dialogue between the wild and the domestic. Part of Kylie Washington's ongoing exploration of the banksia, this 30 × 30 cm work carries a fresh, contemporary energy suited to living spaces."),
("Banksia 3","30x30",150,False,"",None,["Banksia","Australian Flora"],[],
 "Banksia 3 is part of an ongoing series of small works in which Kylie Washington returns to the banksia again and again. Each painting approaches the plant differently, through its cones, its textures and its rhythm of growth, building a body of work that treats a single native species as a lens on resilience and regeneration. At 30 × 30 cm, it is a considered and collectable piece, and pairs well with other works from the series."),
("Banksia Green","30x30",150,False,"",None,["Banksia","Australian Flora"],["Green"],
 "In Banksia Green, the familiar banksia form is explored through a palette of greens, drawing attention to new growth, foliage and the vitality of the Australian bush. Green is the colour of regeneration, of what returns after fire and drought, and it gives this small work a fresh, calm energy. At 30 × 30 cm, it sits comfortably in a smaller space, or as part of a grouping of Banksia works."),
]
BERRY = "{t} belongs to a series of three works sharing the same format, each explored through a different colour. The title is playful, but the subject is abundance: berries as a symbol of fruitfulness, nourishment and seasonal renewal. {c} At 50 × 90 cm, its elongated format makes it well suited to a hallway, above a console or bedhead, or hung alongside the other works in the series."
for col, line in [("Red","In red, the work is rich, warm and bold."),
                  ("Purple","In purple, it is deep and moody, with a sense of dusk and ripeness."),
                  ("Green","In green, it is fresh and botanical, closer to the leaf than the fruit.")]:
    t=f"Berry Me ({col})"
    P.append((t,"50x90",250,False,"",None,["Berries"],[col],BERRY.format(t=t,c=line)))
P += [
("Pink Banksia for Lou","",None,True,"",None,["Banksia","Australian Flora"],["Pink"],
 "Pink Banksia for Lou reimagines one of the artist's most recognisable subjects through soft pink. The shift in colour loosens the banksia from botanical realism and turns it into something more joyful and personal, a celebration of the plant's form rather than a record of it. The work reflects the central thread of Kylie Washington's practice: the banksia as a symbol of resilience, adaptation and renewal."),
("She's So Ambitious","50x60",500,False,"",None,[],[],
 "She's So Ambitious has a confident, forward-leaning spirit, as its title suggests. Whether read as a portrait of a plant pushing towards the light or of a person determined to grow, the work celebrates drive and the energy it takes to flourish. One of a group of works with playful, character-driven titles, it brings personality and warmth to a room. At 50 × 60 cm, it is a substantial original with genuine presence."),
("Yellow Banksia","",None,True,"",None,["Banksia","Australian Flora"],["Yellow"],
 "Yellow Banksia captures the banksia in golden flower, when the cones glow against the grey-green bush. Bright and optimistic, the painting celebrates the plant at its most generous: the moment of bloom that follows seasons of endurance. It is one of many works in which Kylie Washington returns to the banksia as a symbol of resilience and renewal."),
("Oysters","60x60",200,False,"",None,["Coastal","Still Life"],[],
 "Oysters turns to the coastline and one of its quiet treasures. Shaped by tide and salt water, the oyster is an emblem of coastal life on the Central Coast, where Kylie Washington's studio is based. The painting celebrates texture, pearlescent colour and the pleasure of shared tables by the water. At 60 × 60 cm, it is a generous square work that would sit beautifully in a kitchen, dining area or coastal home."),
("Landscape Drip","25x18",None,True,"",None,["Landscape"],[],
 "Landscape Drip is a small, loose study in which paint is allowed to move and run, letting the landscape emerge through process as much as intention. The drips suggest rain, erosion and the passing of time, the forces that shape the land. Intimate in scale, it reflects the experimental side of Kylie Washington's practice."),
("Flock Me","45x38",None,True,"Custom framed in white with mount","Painting on canvas paper",["Birds"],[],
 "Flock Me takes its cue from the gathering of a flock, reflecting on community, movement and the instinct to belong. Playful in title and generous in spirit, it is a work about togetherness. Painted on canvas paper and custom framed in white with a mount, it has a finished, gallery-ready quality."),
("Dinner at #94","",None,True,"",None,[],[],
 "Dinner at #94 is a painting about place, memory and the rituals that bring people together. The title points to a particular address and a particular evening, the kind of shared meal that becomes a lasting memory. Personal and warm, it reflects Kylie Washington's interest in the relationships between people and place."),
("Morning","35x35",200,False,"",None,[],[],
 "Morning captures the quiet promise of a new day: soft light, fresh air and a sense of beginning again. It is a small, contemplative work about renewal on a daily scale, a reminder that regeneration is found not only in the seasons but in ordinary moments. At 35 × 35 cm, it is well suited to a bedroom, reading corner or any space that benefits from calm."),
("Last Star","45x65",250,False,"Unframed","Acrylic on board",["Stars"],[],
 "Last Star holds the moment just before dawn, when a single star lingers as the night gives way. It is a painting about endings and beginnings, and the quiet persistence of light. Related in spirit to the We Are The Stars series, it continues the artist's interest in our connection to the night sky. Painted on board and supplied unframed, at 45 × 65 cm."),
("Banksia Aemula","50x65",700,False,"Custom framed in oak with mount",None,["Banksia","Australian Flora"],[],
 "Banksia Aemula is a substantial framed work dedicated to the banksia, the plant at the centre of Kylie Washington's visual language. The painting celebrates the banksia's sculptural cones and textured foliage, and its remarkable ability to regenerate after fire. It is both a botanical portrait and a symbol of resilience. Custom framed in oak with a mount and ready to hang, at 50 × 65 cm."),
("Everyone Loves Lemons","40x50",None,True,"",None,["Fruit","Still Life"],["Yellow"],
 "Everyone Loves Lemons is a bright, joyful celebration of one of life's simplest pleasures. The lemon, sunny, generous and familiar from backyard trees across Australia, becomes a small emblem of optimism and abundance. It is a companion to Everyone Loves Limes."),
("Everyone Loves Limes","30x30",None,True,"",None,["Fruit","Still Life"],["Green"],
 "Everyone Loves Limes is a zesty, cheerful companion to Everyone Loves Lemons. The lime, bright, fresh and full of zing, becomes a small celebration of colour and everyday pleasure, bringing a burst of green energy to any space."),
("Night Birds","30x40",180,False,"",None,["Birds"],[],
 "Night Birds turns to the hours after dark, when the bush is alive with quiet movement. The painting reflects on the creatures that inhabit the night, and on the stillness and mystery of the landscape once the day has ended. Its intimate 30 × 40 cm scale makes it a compelling piece for a smaller wall or a grouping."),
("Sophia, Billy and The Eggs","45x60",None,True,"",None,[],[],
 "Sophia, Billy and The Eggs is a warm, personal work with a storytelling title, the kind of painting that grows out of everyday life and the people and moments that fill it. It reflects the playful, human side of Kylie Washington's practice and her interest in the relationships between people and place."),
("Pink Waratah","33x33",150,False,"",None,["Waratah","Australian Flora"],["Pink"],
 "The waratah is one of Australia's most striking native flowers and the floral emblem of New South Wales. In Pink Waratah, Kylie Washington paints the bloom in soft pink rather than its familiar red, turning a bold native icon into something tender and unexpected. Part of a series of 33 × 33 cm botanical works, it is an accessible original that sits beautifully alone or in a group."),
("Pink Bits","33x33",None,True,"",None,["Botanical"],["Pink"],
 "Pink Bits is a playful botanical study from a series of 33 × 33 cm works, focusing on fragments of flower and colour rather than the whole. Soft, bright and cheerful, it reflects the joy that runs through Kylie Washington's work with flora."),
("Orchid","33x33",None,True,"",None,["Botanical"],[],
 "Orchid is part of a series of 33 × 33 cm botanical works in which Kylie Washington paints single blooms up close. The orchid, delicate yet surprisingly resilient, is celebrated for its elegant form and colour."),
("Orchid 2","33x33",None,True,"",None,["Botanical"],[],
 "A companion to Orchid, Orchid 2 returns to the same flower with a fresh eye, exploring its form, petals and colour in a second intimate study. The pair reflect the artist's habit of revisiting a subject to see it anew."),
("Purple","33x33",None,True,"",None,["Botanical"],["Purple"],
 "Purple is a botanical study defined by its colour, a saturated work from the 33 × 33 cm series of flower paintings. By naming the work after its palette, Kylie Washington puts colour itself at the centre of the experience."),
("Green Spray","33x33",None,True,"",None,["Botanical"],["Green"],
 "Green Spray captures a spray of foliage, fresh and full of movement. Part of the 33 × 33 cm botanical series, it celebrates the greenery that so often plays a supporting role to the flower, giving it the spotlight instead."),
("She's So Pretty","40x45",300,False,"",None,[],[],
 "She's So Pretty is a joyful, affectionate painting that celebrates beauty in its most unguarded form. One of a group of works with playful, character-driven titles, it treats its subject almost as a personality: charming, bright and full of life. At 40 × 45 cm, it is a lovely mid-sized original for a bedroom, dressing room or living space."),
("Blue Stamen","33x33",150,False,"",None,["Botanical"],["Blue"],
 "Blue Stamen zooms in on the heart of the flower, the stamen, where pollen is carried and new life begins. Painted in blue, the work takes a small botanical detail and turns it into something bold and graphic. Part of the 33 × 33 cm botanical series, it pairs well with the other flower studies."),
("Sunset Field","",None,True,"",None,["Landscape"],[],
 "Sunset Field captures the landscape at the end of the day, when the light turns golden and the field glows with warmth. It is a painting about slowing down and noticing the beauty of a passing moment."),
("Mandarin Bowl","40x30",150,False,"",None,["Fruit","Still Life"],[],
 "Mandarin Bowl is a bright, sunny still life celebrating a simple domestic pleasure. The vivid orange of the mandarins brings warmth and energy, while the bowl anchors the work in everyday life. At 40 × 30 cm, it is a cheerful piece for a kitchen, dining area or breakfast nook."),
("Colour Studies","",50,False,"",None,["Colour Study"],[],
 "These four colour studies are small, spontaneous works in which Kylie Washington explores colour relationships, the building blocks of every larger painting. Each study is a unique original and offers an intimate glimpse into the artist's process. Choose your favourite, or collect all four to hang together as a group. An accessible way to begin collecting original work."),
("Waratahs","33x33",150,False,"",None,["Waratah","Australian Flora"],[],
 "Waratahs gathers the bold blooms of one of Australia's most striking native flowers, the floral emblem of New South Wales. Confident and dramatic, the waratah is a flower that commands attention, and this work celebrates its sculptural form and presence. Part of the 33 × 33 cm botanical series."),
("Dusk Flowers","60x60",450,False,"",None,["Botanical"],[],
 "Dusk Flowers captures the moment when daylight fades and colour deepens, when flowers seem to glow in the last light. The painting explores the quiet beauty of transition, and the idea that endings can be just as radiant as beginnings. At 60 × 60 cm, it is a generous square work with the presence to hold a wall on its own."),
("Tulip","60x60",450,False,"",None,["Botanical"],[],
 "Tulip celebrates a single bloom with bold simplicity. The tulip, elegant and upright, becomes a study of form, colour and poise at a generous scale. At 60 × 60 cm, the work has a striking graphic quality that suits contemporary interiors."),
("Jack and the Bean Stalk","60x60",450,False,"",None,["Botanical"],[],
 "Jack and the Bean Stalk draws on the familiar fairy tale of a plant that grows beyond all expectation. It is a playful meditation on ambition, imagination and the wild energy of growth, translated into a botanical painting. At 60 × 60 cm, it is a joyful work that would sit equally well in a family home or a creative workspace."),
("StarStruck","60x60",450,False,"",None,["Stars"],[],
 "StarStruck is a painting about wonder: the feeling of being dazzled, captivated or suddenly lit up. Connected to the artist's recurring interest in stars and the night sky, it carries an energy of delight and possibility. At 60 × 60 cm, it is a confident, uplifting work for a living room or entry."),
("Oranges","15x15",50,False,"",None,["Fruit","Still Life"],[],
 "Oranges is a tiny, cheerful still life, a small burst of citrus colour at just 15 × 15 cm. Intimate and affordable, it is perfect for a shelf, a kitchen nook or as a gift, and offers an easy way to begin collecting original art."),
("Two Pears In A Pod","15x15",50,False,"",None,["Fruit","Still Life"],[],
 "Two Pears In A Pod is a playful twist on the familiar saying, a small still life about companionship and pairing. At 15 × 15 cm, it is a charming and affordable original, ideal for a shelf, a kitchen or as a gift."),
("Sisters","60x60",None,True,"",None,[],[],
 "Sisters is a painting about closeness, kinship and growing side by side. Whether read through two blooms or two people, it reflects on the bonds that shape us. At 60 × 60 cm, it is one of the more substantial works in the collection."),
("Banksia","120x55",0,False,"Framed",None,["Banksia","Australian Flora"],[],
 "Banksia is a large, elongated work dedicated to the plant at the heart of Kylie Washington's practice. At 120 × 55 cm, the format gives the banksia room to stretch, celebrating its sculptural cones, textured foliage and remarkable capacity to regenerate after fire. A statement piece suited to a hallway, above a sofa or bed, or a larger open-plan space."),
("The Road Out","",None,True,"",None,["Landscape"],[],
 "The Road Out is a landscape about journeys, departures and the promise of what lies ahead. The road becomes a metaphor for change, and for the courage it takes to move forward."),
("Wattle","50x40",None,True,"",None,["Wattle","Australian Flora"],["Yellow"],
 "Wattle celebrates the golden blossom that is Australia's national floral emblem. Soft, bright and abundant, wattle is among the first plants to return after fire, making it a natural symbol of resilience and renewal within Kylie Washington's practice."),
("Grevillea","60x60",450,False,"",None,["Grevillea","Australian Flora"],[],
 "Grevillea celebrates one of Australia's most distinctive native plants, with its spidery, curling flowers loved by nectar-feeding birds. Here the grevillea becomes a study in rhythm, colour and the intricate beauty of native flora. At 60 × 60 cm, it is a generous work with strong presence."),
("Red Protea","33x33",150,False,"",None,["Protea","Botanical"],["Red"],
 "Red Protea celebrates a bloom renowned for its sculptural, almost architectural form. A relative of the banksia and waratah in the Proteaceae family, the protea sits naturally within the artist's exploration of hardy, fire-adapted flora. Part of the 33 × 33 cm botanical series."),
("She's Got Such A Sunny Disposition","60x60",450,False,"",None,[],[],
 "She's Got Such A Sunny Disposition is a warm, optimistic painting that radiates good humour. One of the artist's works with playful, character-driven titles, it celebrates brightness of spirit and the ability to find light in any season. At 60 × 60 cm, it brings an uplifting presence to a living room, kitchen or entry."),
("Waratah In Lounge","107x90",1050,False,"Framed in black",None,["Waratah","Australian Flora"],[],
 "Waratah In Lounge brings one of Australia's most striking native flowers indoors. The waratah, floral emblem of New South Wales, is set within the context of the home, a reflection on how the natural world enters and shapes the spaces we live in. At 107 × 90 cm, it is a major statement work, with the scale and presence to become the focal point of a room."),
]

KEEP={'I Promise This Is The Last One':'i-promise-its-the-last-one','Pink Banksia for Lou':'pink-banksia'}
def handle(t):
    if t in KEEP: return KEEP[t]
    return re.sub(r'-+','-',re.sub(r'[^a-z0-9]+','-',t.lower().replace("'",""))).strip('-')
def size_tag(d):
    if not d: return None
    m=max(int(x) for x in d.split('x')[:2])
    return "Small" if m<40 else "Medium" if m<=70 else "Large" if m<=100 else "Statement"

META = ["Year (product.metafields.custom.custom_year)","Medium (product.metafields.custom.custom_medium)",
        "Dimensions (product.metafields.custom.custom_dimensions)","Framing (product.metafields.custom.custom_framing)"]
H = ["Handle","Title","Body (HTML)","Vendor","Product Category","Type","Tags","Published",
     "Option1 Name","Option1 Value","Variant SKU","Variant Grams","Variant Inventory Tracker",
     "Variant Inventory Qty","Variant Inventory Policy","Variant Fulfillment Service","Variant Price",
     "Variant Compare At Price","Variant Requires Shipping","Variant Taxable","Variant Barcode",
     "Image Src","Image Position","Image Alt Text","Gift Card","SEO Title","SEO Description",
     "Variant Weight Unit","Status"] + META

rows=[]; handles=set()
for i,(t,d,price,sold,frame,medium,subj,cols,desc) in enumerate(P,1):
    h=handle(t); assert h not in handles, h; handles.add(h)
    dims = d.replace('x',' × ')+' cm' if d else ''
    tags=["Originals","Paintings","Original Artwork","Sold" if sold else "Available"]
    if sold: tags.append("Archive")
    if price==0 and not sold: tags.append("Price Pending")
    if size_tag(d): tags.append("Size: "+size_tag(d))
    tags += ["Subject: "+s for s in subj] + ["Colour: "+c for c in cols]
    body="<p>"+desc+(SOLD if sold else "")+"</p>"
    seo_t=f"{t} | Original Painting by Kylie Washington"
    seo_d=f"{t}, an original painting by Australian contemporary artist Kylie Washington."+(f" {dims}." if dims else "")+(" Sold, archive work." if sold else "")
    base={"Handle":h,"Title":t,"Body (HTML)":body,"Vendor":"Kylie Washington","Type":"Original Artwork",
          "Tags":", ".join(tags),"Published":"FALSE","Gift Card":"FALSE","SEO Title":seo_t,"SEO Description":seo_d,
          "Status":"draft",META[0]:"2026",META[1]:medium or "Acrylic on canvas",META[2]:dims,META[3]:frame}
    def variant(opt_name,opt_val,sku,qty,pr):
        return {"Option1 Name":opt_name,"Option1 Value":opt_val,"Variant SKU":sku,"Variant Grams":"",
                "Variant Inventory Tracker":"shopify","Variant Inventory Qty":str(qty),"Variant Inventory Policy":"deny",
                "Variant Fulfillment Service":"manual","Variant Price":f"{pr:.2f}","Variant Requires Shipping":"TRUE",
                "Variant Taxable":"TRUE","Variant Weight Unit":"kg"}
    sku=f"KW-PT-{i:03d}"
    if t=="Colour Studies":
        rows.append({**base,**variant("Study","Colour Study 1",sku+"-1",1,50)})
        for k in (2,3,4): rows.append({"Handle":h,**variant("Study",f"Colour Study {k}",f"{sku}-{k}",1,50)})
    else:
        rows.append({**base,**variant("Title","Default Title",sku,0 if sold else 1,price or 0)})

out="/tmp/claude-0/-home-user-new-design/28e41a16-b9c5-503d-ae7d-6b51934b74cb/scratchpad/shopify/kylie-washington_originals_shopify-import.csv"
with open(out,"w",newline="",encoding="utf-8") as f:
    w=csv.DictWriter(f,fieldnames=H); w.writeheader(); [w.writerow(r) for r in rows]
print(len(P),"products",len(rows),"rows")
print("sold",sum(p[3] for p in P),"available",sum(not p[3] for p in P))
for p in P: 
    wc=len(p[8].split()); 
    if wc<35 or wc>150: print("words",p[0],wc)

test=[r for r in rows if r["Handle"] in ("ghost-gum","a-poem-with-ai","colour-studies")]
with open(out.replace(".csv","_TEST-3-products.csv"),"w",newline="",encoding="utf-8") as f:
    w=csv.DictWriter(f,fieldnames=H); w.writeheader(); [w.writerow(r) for r in test]
print("test rows",len(test))
