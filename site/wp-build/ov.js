const { chromium } = require('playwright');
const { execFile } = require('child_process');
const run=(u)=>new Promise((res,rej)=>execFile('curl',['-sSL','--max-time','40','-D','-',u],{maxBuffer:1e8,encoding:'buffer'},(e,o)=>e?rej(e):res(o)));
const cache={};
(async()=>{const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium'});
for(const w of [360,390,768,1024,1366]){const p=await b.newPage({viewport:{width:w,height:800}});
await p.route(/^https:\/\//,async r=>{const u=r.request().url();
  if(!/digiranxpro|fonts\.g|gstatic/.test(u)||/\.(jpg|png|jpeg|webp)/.test(u)) return r.abort();
  try{if(!cache[u]){const o=await run(u.includes('uploads/elementor/css')?u+(u.includes('?')?'&':'?')+'cb='+Date.now():u);let rest=o,head='';while(rest.slice(0,5).toString()==='HTTP/'){const s=rest.indexOf(Buffer.from('\r\n\r\n'));head=rest.slice(0,s).toString();rest=rest.slice(s+4);}cache[u]={body:rest,ct:(head.match(/content-type:\s*([^\r\n]+)/i)||[])[1]||'text/html'};}
  await r.fulfill({status:200,body:cache[u].body,contentType:cache[u].ct});}catch(e){await r.abort();}});
for(const pg of ['','about-us/','our-services/','contact-us/','faqs/','blog/','how-to-rank-higher-on-google-maps-in-2026/','privacy-policy/','not-a-real-page/','gbp-optimization/','web-development/','custom-web-design/','responsive-development/','ui-ux-designing/','graphic-designing/','reviews/','seo-digital-marketing/','landing-pages/','software-development/','social-media-marketing/','branding/','google-ads/','citations-backlinks/','e-commerce-solutions/']){
  await p.goto('https://digiranxpro.com/'+pg,{waitUntil:'domcontentloaded',timeout:90000});await p.waitForTimeout(1200);
  const r=await p.evaluate(()=>{const W=document.documentElement.clientWidth;const o=[];document.querySelectorAll('body *').forEach(e=>{if(e.closest('.dg-mega-panel,.elementor-location-popup,[data-elementor-type=popup]'))return;const rc=e.getBoundingClientRect();if(rc.width&&rc.right>W+1&&getComputedStyle(e).position!=='fixed')o.push((e.getAttribute('data-id')||e.tagName)+':'+Math.round(rc.right));});return [document.documentElement.scrollWidth-W,o.slice(0,4)];});
  if(r[0]>0||r[1].length) console.log(w,pg||'home',JSON.stringify(r));}
await p.close();}
console.log('done');await b.close();})();
