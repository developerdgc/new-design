const { chromium } = require('playwright');
const { execFile } = require('child_process');
const fs=require('fs');
const run=(u)=>new Promise((res,rej)=>execFile('curl',['-sSL','--max-time','40','-D','-',u],{maxBuffer:1e8,encoding:'buffer'},(e,o)=>e?rej(e):res(o)));
const cache={};
const PAGES=['','about-us/','services/','contact-us/','faqs/','blog/','privacy-policy/','terms-conditions/','cookie-policy/','services/gbp-optimization/','services/web-development/','services/custom-web-design/','services/responsive-development/','services/ui-ux-designing/','services/graphic-designing/','services/reviews/','services/seo-digital-marketing/','services/landing-pages/','services/software-development/','services/social-media-marketing/','services/branding/','services/google-ads/','services/citations-backlinks/','services/e-commerce-solutions/','how-to-rank-higher-on-google-maps-in-2026/','does-your-small-business-really-need-branding/'];
(async()=>{const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium'});
const p=await b.newPage({viewport:{width:1366,height:800}});
const errs=[];p.on('pageerror',e=>errs.push(e.message));p.on('console',m=>{if(m.type()==='error')errs.push('console:'+m.text().slice(0,120))});
await p.route(/^https:\/\//,async r=>{const u=r.request().url();
  if(!/digiranxpro|fonts\.g|gstatic/.test(u)||/\.(jpg|png|jpeg|webp)/.test(u)) return r.abort();
  try{if(!cache[u]){const o=await run(u);let rest=o,head='',status=200;while(rest.slice(0,5).toString()==='HTTP/'){const s=rest.indexOf(Buffer.from('\r\n\r\n'));head=rest.slice(0,s).toString();rest=rest.slice(s+4);}status=+(head.match(/HTTP\/\S+ (\d+)/)||[0,200])[1];cache[u]={body:rest,status,ct:(head.match(/content-type:\s*([^\r\n]+)/i)||[])[1]||'text/html'};}
  await r.fulfill({status:cache[u].status,body:cache[u].body,contentType:cache[u].ct});}catch(e){await r.abort();}});
const links=new Set();const report=[];
for(const pg of PAGES){errs.length=0;
  const resp=await p.goto('https://digiranxpro.com/'+pg,{waitUntil:'domcontentloaded',timeout:90000});await p.waitForTimeout(800);
  const r=await p.evaluate(()=>({title:document.title,h1:[...document.querySelectorAll('h1')].map(h=>h.innerText.trim().slice(0,60)),noalt:[...document.querySelectorAll('img')].filter(i=>!i.getAttribute('alt')).map(i=>(i.getAttribute('src')||'').split('/').pop()).slice(0,20),
    links:[...document.querySelectorAll('a[href]')].map(a=>a.href).filter(h=>h.startsWith('https://digiranxpro.com')),pageid:[...document.querySelectorAll('a[href*="page_id"]')].length}));
  r.links.forEach(l=>links.add(l.split('#')[0]));
  report.push({pg:pg||'home',status:resp.status(),title:r.title,h1:r.h1,noalt:r.noalt.length,noaltSample:[...new Set(r.noalt)].slice(0,6),pageid:r.pageid,errs:[...new Set(errs)].slice(0,3)});}
fs.writeFileSync('qa_report.json',JSON.stringify({report,links:[...links]},null,1));
for(const x of report) console.log(JSON.stringify(x));
console.log('links',links.size);await b.close();})();
