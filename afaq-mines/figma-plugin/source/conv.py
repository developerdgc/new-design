import json,sys,os
S=sys.argv[1]; out=sys.argv[2]
TITLES=[('home','01 Home'),('about','02 About Us'),('why-afaq','03 Why Afaq Mines'),('team','04 Our Team'),('global','05 Global Attraction'),('why-pakistan','06 Why Pakistan'),('regions','07 Regions'),('metallic','08 Metallic Minerals'),('industrial','09 Industrial Minerals'),('gemstones','10 Gem Stones'),('products','11 Our Products'),('processing','12 Processing'),('inquiry','13 Inquiry'),('contact','14 Contact Us')]
icons=[]; iconIdx={}
R=lambda v: round(v,1) if isinstance(v,float) else v
def hx(c): return '#%02x%02x%02x'%(round(c['r']*255),round(c['g']*255),round(c['b']*255))
def al(c): return round(c.get('a',1),3)
def fills(fs):
    o=[]
    for f in fs or []:
        if f.get('weak'): continue
        if f['t']=='solid': o.append(['s',hx(f['c']),al(f['c'])])
        elif f['t']=='img': o.append(['i',f['src']])
        elif f['t']=='lg': o.append(['g',f['angle'],[[hx(s['c']),al(s['c']),round(s['p'],3)] for s in f['stops']]])
    return o
def box(n,k):
    d={'k':k,'n':n.get('name'),'x':R(n['x']),'y':R(n['y']),'w':R(n['w']),'h':R(n['h'])}
    f=fills(n.get('fills'))
    if f: d['f']=f
    r=n.get('r') or [0,0,0,0]
    if any(r): d['r']=R(r[0]) if len(set(r))==1 else [R(v) for v in r]
    st=n.get('stroke')
    if st: d['st']=[hx(st['c']),al(st['c']),R(st['w'])]
    if n.get('sides'): d['sd']=[R(v) for v in n['sides']]
    sh=n.get('sh')
    if sh: d['sh']=[hx(sh['c']),al(sh['c']),sh['x'],sh['y'],sh['b'],1 if sh['inset'] else 0,sh['s']]
    if n.get('op',1)<1: d['o']=round(n['op'],3)
    return d
def conv(n):
    k=n['k']
    if k=='frame':
        d=box(n,'f'); d['c']=[x for x in (conv(c) for c in n.get('kids') or []) if x]; return d
    if k=='box': return box(n,'b')
    if k=='text':
        g=[]
        ts=None
        for s in n['segs']:
            f=s['f']; c=f['c'] or {'r':0,'g':0,'b':0,'a':1}
            g.append([s['t'],R(f['s']),f['w'],1 if f['i'] else 0,hx(c),al(c)])
            if f.get('stroke') and f['stroke']['c']: ts=[hx(f['stroke']['c']),f['stroke']['w']]
        d={'k':'t','x':R(n['x']),'y':R(n['y']),'w':R(n['w']),'h':R(n['h']),'g':g,'lh':R(n['lh']),'al':n['al']}
        if n.get('ls'): d['ls']=R(n['ls'])
        if ts: d['ts']=ts
        if n.get('op',1)<1: d['o']=round(n['op'],3)
        return d
    if k=='svg':
        v=n['svg']
        if v not in iconIdx: iconIdx[v]=len(icons); icons.append(v)
        d={'k':'s','v':iconIdx[v],'x':R(n['x']),'y':R(n['y']),'w':R(n['w']),'h':R(n['h'])}
        if n.get('op',1)<1: d['o']=round(n['op'],3)
        return d
    if k=='radio': return {'k':'r','x':R(n['x']),'y':R(n['y']),'w':R(n['w']),'h':R(n['h']),'on':n['on'],'c':hx(n['c'])}
pages=[]
for key,title in TITLES:
    J=json.load(open(f'{S}/{key}.json'))
    pages.append({'title':title,'w':J['w'],'h':J['h'],'tree':[x for x in (conv(c) for c in J['tree']) if x]})
data='const PAGES = '+json.dumps(pages,separators=(',',':'))+';\nconst ICONS = '+json.dumps(icons,separators=(',',':'))+';\n'
open(out,'w').write(data+open(os.path.join(os.path.dirname(__file__) or '.','runtime.js')).read())
srcs=set()
def walk(n):
    for f in n.get('f',[]) or []:
        if f[0]=='i': srcs.add(f[1])
    if n.get('k')=='f':
        for c in n.get('c',[]): walk(c)
for p in pages:
    for n in p['tree']: walk(n)
print('bytes',len(data),'icons',len(icons),'images',len(srcs))
json.dump(sorted(srcs),open(out+'.srcs.json','w'))
