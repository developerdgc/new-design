const { chromium } = require('playwright');
const { execFileSync } = require('child_process');
async function viaCurl(route) { const req = route.request(); const u = req.url(); if (!/^https?:/.test(u) || req.method() !== 'GET') return route.continue();
  try { const hdr = '/tmp/_h' + process.pid; const body = execFileSync('curl', ['-sSL', '--max-time', '40', '-D', hdr, u], { maxBuffer: 64 * 1024 * 1024 });
    const h = require('fs').readFileSync(hdr, 'utf8').split(/\r?\n\r?\n/).filter(Boolean).pop();
    return route.fulfill({ status: +((h.match(/HTTP\/[\d.]+\s+(\d+)/) || [])[1] || 200), body, headers: { 'content-type': (h.match(/content-type:\s*([^\r\n]+)/i) || [])[1] || 'application/octet-stream' } }); } catch (e) { return route.abort(); } }
(async()=>{const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium'});
for (const W of [1440,390]) { const p=await b.newPage({viewport:{width:W,height:900},ignoreHTTPSErrors:true}); await p.route('**/*', viaCurl);
 await p.goto('https://digitalgrowthcatalyze.com/about-us/?r='+Math.random(),{waitUntil:'load',timeout:120000}); await p.waitForTimeout(1500);
 console.log(W, JSON.stringify(await p.evaluate(()=>{
  const h1=[...document.querySelectorAll('h1,h2')].find(e=>/ABOUT US/i.test(e.textContent)); 
  const st=(e,keys)=>{const s=getComputedStyle(e);const r=e.getBoundingClientRect();return Object.assign({cls:e.className.toString().slice(0,60),tag:e.tagName,box:[Math.round(r.x),Math.round(r.y+scrollY),Math.round(r.width),Math.round(r.height)]},Object.fromEntries(keys.map(k=>[k,s[k]])))};
  const chain=[]; let e=h1; for(let i=0;i<7&&e;i++){chain.push(st(e,['backgroundImage','backgroundColor','borderTopWidth','borderTopColor','borderRadius','boxShadow','paddingTop','paddingBottom','paddingLeft','maxWidth','minHeight'])); e=e.parentElement;}
  const sub=h1.closest('.e-con, .elementor-element').parentElement.querySelector('p, .elementor-widget-text-editor');
  const btn=h1.closest('.e-con-inner, .e-con').querySelector('a.elementor-button, a');
  return {h1:st(h1,['fontFamily','fontSize','fontWeight','lineHeight','textTransform','color','letterSpacing']), sub: sub && st(sub,['fontFamily','fontSize','fontWeight','color','lineHeight']), btn: btn && st(btn,['fontFamily','fontSize','fontWeight','color','backgroundColor','borderRadius','paddingTop','paddingLeft','boxShadow']), chain};
 })));
 await p.close(); }
await b.close()})();
