import csv, os
exec(open('dbx/map.py').read())
BASE="https://cdn.shopify.com/s/files/1/0711/2769/5411/files/"
imgs={h:[f"{h}.jpg" if i==0 else f"{h}-{i+1}.jpg" for i in range(len(v[0]))] for h,v in M.items()}
imgs["pink-waratah"]=["pink-waratah.jpg"]
ready=set(os.listdir('dbx/out/ready'))|{"pink-waratah.jpg"}
for fl in imgs.values():
    for f in fl: assert f in ready, f
def process(src,dst,kind):
    rows=list(csv.DictReader(open(src,encoding='utf-8'))); H=list(rows[0].keys())
    out=[];title={}
    for r in rows:
        if r['Title']: title[r['Handle']]=r['Title']
    for i,r in enumerate(rows):
        out.append(r)
        last=(i+1==len(rows)) or rows[i+1]['Handle']!=r['Handle']
        if last:
            h=r['Handle']; fl=imgs.get(h,[])
            first=[x for x in out if x['Handle']==h][0]
            for n,f in enumerate(fl,1):
                alt=f"{title[h]}, {kind} by Kylie Washington" + ("" if n==1 else f" (view {n})")
                if n==1:
                    first.update({"Image Src":BASE+f,"Image Position":"1","Image Alt Text":alt})
                else:
                    out.append({**{k:"" for k in H},"Handle":h,"Image Src":BASE+f,"Image Position":str(n),"Image Alt Text":alt})
    with open(dst,'w',newline='',encoding='utf-8') as fo:
        w=csv.DictWriter(fo,fieldnames=H); w.writeheader(); w.writerows(out)
    withimg=sum(1 for h in title if h in imgs); nimg=sum(len(imgs[h]) for h in title if h in imgs)
    print(dst,len(title),'products,',withimg,'with images,',nimg,'images')
process('shopify/kylie-washington_originals_shopify-import.csv','shopify/kylie-washington_originals_WITH-IMAGES.csv','original painting')
process('shopify/kylie-washington_fine-art-prints_shopify-import.csv','shopify/kylie-washington_fine-art-prints_WITH-IMAGES.csv','fine art print')
