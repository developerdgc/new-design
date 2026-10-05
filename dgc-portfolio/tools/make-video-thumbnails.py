from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageEnhance
F='/tmp/claude-0/fonts/'
UNB=F+'Yq6F-LOTXCb04q32xlpat-6uR42XTqtG65j2040.ttf'; UNB7=F+'Yq6F-LOTXCb04q32xlpat-6uR42XTqtG6__2040.ttf'
MAN8=F+'xn7_YHE41ni1AdIRqAuZuw1Bx9mbZk59E-_F.ttf'; MAN6=F+'xn7_YHE41ni1AdIRqAuZuw1Bx9mbZk4jE-_F.ttf'
OUT='/home/user/new-design/dgc-portfolio/video/'
NAVY=(6,40,54); ABYSS=(2,23,32); ORANGE=(246,164,64); CYAN=(28,222,225)
W,H=720,1280
logo=Image.open('/home/user/new-design/dgc-portfolio/img/brand/dgc-logo-white.png').convert('RGBA')
DATA=[(1,'CLARK','EXTERIORS','Roofing contractor','0:23'),
      (2,'HUSKINS','SERVICES','Cleaning & remodeling','0:15'),
      (3,'REAL CLIENT.','REAL RESULTS.','Client video review','0:34'),
      (4,'REAL CLIENT.','REAL RESULTS.','Client video review','1:40')]
def grad(h, top, bottom, a0, a1):
    g=Image.new('L',(1,h))
    for y in range(h): g.putpixel((0,y), int(a0+(a1-a0)*(y/(h-1))**1.4))
    return g.resize((W,h))
def star(d, cx, cy, r, fill):
    import math
    pts=[]
    for k in range(10):
        ang=math.pi/2+k*math.pi/5; rr=r if k%2==0 else r*0.45
        pts.append((cx+rr*math.cos(ang), cy-rr*math.sin(ang)))
    d.polygon(pts, fill=fill)
for i,l1,l2,sub,dur in DATA:
    im=Image.open(f'/tmp/claude-0/frames/best{i}.png').convert('RGB')
    im=im.resize((W,int(im.height*W/im.width)),Image.LANCZOS).crop((0,0,W,H))
    im=ImageEnhance.Contrast(im).enhance(1.06); im=ImageEnhance.Color(im).enhance(1.08)
    im=im.convert('RGBA')
    # top + bottom shading in brand navy
    top=Image.new('RGBA',(W,300),ABYSS+(0,)); top.putalpha(grad(300,0,0,170,0).transpose(Image.FLIP_TOP_BOTTOM).transpose(Image.FLIP_TOP_BOTTOM))
    tmask=Image.new('L',(1,300))
    for y in range(300): tmask.putpixel((0,y), int(170*(1-y/299)**1.5))
    top.putalpha(tmask.resize((W,300))); im.alpha_composite(top,(0,0))
    bh=760; bot=Image.new('RGBA',(W,bh),ABYSS+(0,))
    bmask=Image.new('L',(1,bh))
    for y in range(bh): bmask.putpixel((0,y), int(238*min(1,(y/(bh-1))*1.35)**0.95))
    bot.putalpha(bmask.resize((W,bh))); im.alpha_composite(bot,(0,H-bh))
    # orange glow bottom-right
    glow=Image.new('RGBA',(W,H),(0,0,0,0)); gd=ImageDraw.Draw(glow); gd.ellipse((W-360,H-420,W+260,H+180),fill=ORANGE+(70,)); glow=glow.filter(ImageFilter.GaussianBlur(90)); im.alpha_composite(glow)
    d=ImageDraw.Draw(im)
    # logo top-left
    lg=logo.copy(); lg.thumbnail((170,60)); im.alpha_composite(lg,(44,48))
    # pill top-right
    f=ImageFont.truetype(MAN8,22); txt='VIDEO REVIEW'; tw=d.textlength(txt,font=f)
    x1=W-44; x0=x1-tw-56; d.rounded_rectangle((x0,50,x1,96),radius=23,fill=ORANGE)
    d.ellipse((x0+18,66,x0+32,80),fill=ABYSS); d.text((x0+42,58),txt,font=f,fill=ABYSS)
    # stars
    y=H-400
    for k in range(5): star(d, 62+k*42, y, 17, ORANGE)
    # name
    fs=78 if len(l1)<10 else 58
    fn=ImageFont.truetype(UNB,fs)
    while max(d.textlength(l1,font=fn), d.textlength(l2,font=fn))>W-110: fs-=2; fn=ImageFont.truetype(UNB,fs)
    d.rectangle((44,y+42,52,y+42+fs*2+14),fill=ORANGE)
    d.text((72,y+36),l1,font=fn,fill=(255,255,255))
    d.text((72,y+36+fs+8),l2,font=fn,fill=(255,255,255) if i>2 else ORANGE)
    # sub + duration
    fsub=ImageFont.truetype(MAN6,30); yy=y+36+2*fs+50
    d.text((44,yy),sub,font=fsub,fill=CYAN)
    fd=ImageFont.truetype(MAN8,24); dw=d.textlength(dur,font=fd)
    chip=Image.new('RGBA',(W,H),(0,0,0,0)); cd=ImageDraw.Draw(chip)
    cd.rounded_rectangle((W-44-dw-62,yy-4,W-44,yy+42),radius=21,fill=(255,255,255,46),outline=(255,255,255,110),width=2)
    im.alpha_composite(chip); d=ImageDraw.Draw(im)
    d.polygon([(W-44-dw-42,yy+9),(W-44-dw-42,yy+29),(W-44-dw-26,yy+19)],fill=(255,255,255))
    d.text((W-44-dw-16,yy+4),dur,font=fd,fill=(255,255,255))
    # bottom brand line
    d.rectangle((0,H-10,W*0.6,H),fill=ORANGE); d.rectangle((W*0.6,H-10,W,H),fill=CYAN)
    im.convert('RGB').save(OUT+f'review-{i}.jpg',quality=82,optimize=True,progressive=True)
print('done')
