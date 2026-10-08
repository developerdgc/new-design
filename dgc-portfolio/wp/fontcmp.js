const { chromium } = require('playwright');
const { execFileSync } = require('child_process');
async function viaCurl(route) { const req = route.request(); const u = req.url(); if (!/^https?:/.test(u) || req.method() !== 'GET') return route.continue();
  try { const hdr = '/tmp/_h' + process.pid; const body = execFileSync('curl', ['-sSL', '--max-time', '40', '-D', hdr, u], { maxBuffer: 64 * 1024 * 1024 });
    const h = require('fs').readFileSync(hdr, 'utf8').split(/\r?\n\r?\n/).filter(Boolean).pop();
    return route.fulfill({ status: +((h.match(/HTTP\/[\d.]+\s+(\d+)/) || [])[1] || 200), body, headers: { 'content-type': (h.match(/content-type:\s*([^\r\n]+)/i) || [])[1] || 'application/octet-stream' } }); } catch (e) { return route.abort(); } }
(async()=>{const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium'});
for (const block of [false,true]) for (const path of ['/video-reviews/','/case-studies/','/']) { const p=await b.newPage({viewport:{width:412,height:823},ignoreHTTPSErrors:true});
await p.route('**/*', r=> block && /fonts\.(gstatic|googleapis)/.test(r.request().url()) ? r.abort() : viaCurl(r));
await p.goto('https://newportfolio.digitalgrowthcatalyze.com'+path+'?r='+Math.random(),{waitUntil:'load',timeout:120000}); await p.waitForTimeout(1500);
console.log(block?'NOFONT':'FONT', path, JSON.stringify(await p.evaluate(()=>{const h=document.querySelector('h1'); const s=h.closest('section'); return {h1:Math.round(h.getBoundingClientRect().height), h1y:Math.round(h.getBoundingClientRect().y), sec:Math.round(s.getBoundingClientRect().height), ff:getComputedStyle(h).fontFamily, kick: Math.round(s.querySelector('span,p').getBoundingClientRect().y)}})));
await p.close();}
await b.close()})();
