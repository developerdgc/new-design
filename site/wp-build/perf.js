const { chromium } = require('playwright');
const { execFile } = require('child_process');
const run=(u)=>new Promise((res,rej)=>execFile('curl',['-sSL','--max-time','40','-D','-',u],{maxBuffer:1e8,encoding:'buffer'},(e,o)=>e?rej(e):res(o)));
(async()=>{const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium'});
for(const pg of ['','seo-digital-marketing/']){const p=await b.newPage({viewport:{width:1366,height:800}});
let n=0,bytes=0;const kinds={};
await p.route(/^https:\/\//,async r=>{const u=r.request().url();
  if(!/digiranxpro|fonts\.g|gstatic/.test(u)) return r.abort();
  try{const o=await run(u);let rest=o,head='';while(rest.slice(0,5).toString()==='HTTP/'){const s=rest.indexOf(Buffer.from('\r\n\r\n'));head=rest.slice(0,s).toString();rest=rest.slice(s+4);}
  n++;bytes+=rest.length;const ext=(u.split('?')[0].match(/\.([a-z0-9]+)$/)||[0,'html'])[1];kinds[ext]=(kinds[ext]||0)+rest.length;
  await r.fulfill({status:200,body:rest,contentType:(head.match(/content-type:\s*([^\r\n]+)/i)||[])[1]||'text/html'});}catch(e){await r.abort();}});
await p.goto('https://digiranxpro.com/'+pg,{waitUntil:'load',timeout:120000});
for(let y=0;y<16000;y+=700){await p.evaluate(y=>scrollTo(0,y),y);await p.waitForTimeout(100);}await p.waitForTimeout(1500);
console.log(pg||'home','requests',n,'uncompressed KB',Math.round(bytes/1024),JSON.stringify(Object.fromEntries(Object.entries(kinds).map(([k,v])=>[k,Math.round(v/1024)]))));await p.close();}
await b.close();})();
