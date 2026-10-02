const { chromium } = require('playwright');
const { execFile } = require('child_process');
const run=(u)=>new Promise((res,rej)=>execFile('curl',['-sSL','--max-time','40','-D','-',u],{maxBuffer:1e8,encoding:'buffer'},(e,o)=>e?rej(e):res(o)));
const cache={};
(async()=>{const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium'});
for(const w of [1025,1100,1180,1280,1340,1440]){const p=await b.newPage({viewport:{width:w,height:700}});
await p.route(/^https:\/\//,async r=>{const u=r.request().url();
  if(!/digiranxpro|fonts\.g|gstatic/.test(u)||/\.(jpg|jpeg|webp)/.test(u)) return r.abort();
  try{if(!cache[u]){const o=await run(u);let rest=o,head='';while(rest.slice(0,5).toString()==='HTTP/'){const s=rest.indexOf(Buffer.from('\r\n\r\n'));head=rest.slice(0,s).toString();rest=rest.slice(s+4);}cache[u]={body:rest,ct:(head.match(/content-type:\s*([^\r\n]+)/i)||[])[1]||'text/html'};}
  await r.fulfill({status:200,body:cache[u].body,contentType:cache[u].ct});}catch(e){await r.abort();}});
await p.goto('https://digiranxpro.com/',{waitUntil:'domcontentloaded'});await p.waitForTimeout(1500);await p.evaluate(()=>document.fonts.ready);
const r=await p.evaluate(()=>{const bar=document.querySelector('[data-elementor-type=header] .e-con .e-con');const links=[...bar.querySelectorAll('.e-button-base, .dg-mega-item > .e-con:first-child')];const tops=links.map(l=>Math.round(l.getBoundingClientRect().top));
 return {barH:Math.round(bar.getBoundingClientRect().height),tops:[...new Set(tops)],overflow:bar.scrollWidth-bar.clientWidth};});
console.log(w,JSON.stringify(r));await p.screenshot({path:`nav_${w}.png`,clip:{x:0,y:0,width:w,height:100}});await p.close();}
await b.close();})();
