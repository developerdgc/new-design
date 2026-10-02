const { chromium } = require('playwright');
const { execFile } = require('child_process');
const run=(u)=>new Promise((res,rej)=>execFile('curl',['-sSL','--max-time','40','-D','-',u],{maxBuffer:1e8,encoding:'buffer'},(e,o)=>e?rej(e):res(o)));
(async()=>{const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium'});const p=await b.newPage({viewport:{width:1440,height:900}});
await p.route(/^https:\/\//,async r=>{const u=r.request().url();if(!/digiranxpro|fonts\.g|gstatic/.test(u)||/\.(jpg|jpeg|webp)/.test(u)) return r.abort();
  try{const o=await run(u.includes('uploads/elementor/css')?u+'&cb='+Date.now():u);let rest=o,head='';while(rest.slice(0,5).toString()==='HTTP/'){const s=rest.indexOf(Buffer.from('\r\n\r\n'));head=rest.slice(0,s).toString();rest=rest.slice(s+4);}
  await r.fulfill({status:200,body:rest,contentType:(head.match(/content-type:\s*([^\r\n]+)/i)||[])[1]||'text/html'});}catch(e){await r.abort();}});
const bg=(sel)=>p.evaluate(s=>{const e=document.querySelector(s);const c=getComputedStyle(e);return (c.backgroundImage.slice(0,30)+' | '+c.backgroundColor+' | '+c.color);},sel);
await p.goto('https://digiranxpro.com/',{waitUntil:'load'});await p.waitForTimeout(2500);
for(const [name,sel] of [['call','.dg-call-btn'],['heroAudit','.dg-btn-grad'],['ghost','.dg-btn-ghost-w'],['white','.dg-btn-white'],['toTop','.dg-to-top']]){
  const before=await bg(sel);await p.hover(sel);await p.waitForTimeout(400);console.log(name,'\n  before',before,'\n  hover ',await bg(sel));await p.mouse.move(0,0);await p.waitForTimeout(300);}
await p.hover('.dg-call-btn');await p.waitForTimeout(400);await p.screenshot({path:'hov_call.png',clip:{x:1100,y:0,width:340,height:110}});
await p.goto('https://digiranxpro.com/our-services/',{waitUntil:'load'});await p.waitForTimeout(2500);
const tab='.dg-tab[aria-selected="false"]';const t0=await bg(tab);await p.hover(tab);await p.waitForTimeout(400);console.log('tab\n  before',t0,'\n  hover ',await bg(tab));
await (await p.$('.dg-tab')).scrollIntoViewIfNeeded();await p.screenshot({path:'hov_tab.png',clip:{x:300,y:0,width:840,height:900}});
await p.goto('https://digiranxpro.com/contact-us/',{waitUntil:'load'});await p.waitForTimeout(2000);
const fm=p.locator('form:has(select)').first();await fm.scrollIntoViewIfNeeded();await fm.screenshot({path:'hov_form.png'});
console.log(await p.evaluate(()=>{const f=document.querySelector('form');const i=f.querySelector('input');return getComputedStyle(f).padding+' | input font '+getComputedStyle(i).fontFamily+' '+getComputedStyle(i).fontSize;}));
await b.close();})();
