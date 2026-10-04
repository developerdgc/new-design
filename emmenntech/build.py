import re,base64
s=open('src.html').read()
s=s.replace('{{DATA}}',open('data.js').read())
MK='<svg class="mk" viewBox="20 20 470 460" aria-hidden="true"><defs><linearGradient id="ID" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#7AF0F5"/><stop offset="1" stop-color="#3FB8E8"/></linearGradient></defs><g fill="url(#ID)"><path d="M28 249A221 221 0 1 1 249 470L249 387A138 138 0 1 0 111 249Z"/><rect x="165" y="300" width="85" height="87"/><rect x="42" y="330" width="55" height="55"/><rect x="97" y="385" width="68" height="67"/></g></svg>'
s=s.replace('{{RING}}','<svg class="ring" viewBox="20 20 470 460" aria-hidden="true"><path fill="#7AF0F5" d="M28 249A221 221 0 1 1 249 470L249 387A138 138 0 1 0 111 249Z"/></svg>')
s=s.replace('{{PX}}','<svg class="px" viewBox="0 0 90 76" aria-hidden="true"><rect x="34" y="0" width="38" height="38" fill="#FF8A1F"/><rect x="0" y="14" width="24" height="24" fill="#7AF0F5"/><rect x="24" y="38" width="30" height="30" fill="#1F6BE0"/></svg>')
s=s.replace('{{MARK}}',MK.replace('ID','mkg1')).replace('{{MARK2}}',MK.replace('ID','mkg2'))
s=re.sub(r'\{\{i:(\w+)\}\}',r'<span class="i" data-i="\1"></span>',s)
uri=lambda p,m:f'data:{m};base64,'+base64.b64encode(open(p,'rb').read()).decode()
s=s.replace('{{mark}}',uri('assets/mark.png','image/png'))
for i in range(1,8): s=s.replace('{{p%d}}'%i,uri('assets/p%d.jpg'%i,'image/jpeg'))
for n in set(re.findall(r'\{\{img:([\w-]+)\}\}',s)): s=s.replace('{{img:%s}}'%n,uri('assets/%s.jpg'%n,'image/jpeg'))
for v in ['0HTQh_vvbmc','LByRG9RuCSY','fV2UIO6vWaM','uLUuJYvsjco']: s=s.replace('{{v_%s}}'%v,uri('assets/v_%s.jpg'%v,'image/jpeg'))
s=s.replace('{{svg:world}}',uri('assets/world.svg','image/svg+xml'))
left=re.findall(r'\{\{[^}]+\}\}',s); assert not left,left
open('emmenntech-site.html','w').write(s); print(len(s))
