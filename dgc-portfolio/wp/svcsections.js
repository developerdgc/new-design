const { chromium } = require('playwright');
const { execFileSync } = require('child_process');
async function viaCurl(route) { const req = route.request(); const u = req.url(); if (!/^https?:/.test(u) || req.method() !== 'GET') return route.continue();
  try { const hdr = '/tmp/_h' + process.pid; const body = execFileSync('curl', ['-sSL', '--max-time', '40', '-D', hdr, u], { maxBuffer: 64 * 1024 * 1024 });
    const h = require('fs').readFileSync(hdr, 'utf8').split(/\r?\n\r?\n/).filter(Boolean).pop();
    return route.fulfill({ status: +((h.match(/HTTP\/[\d.]+\s+(\d+)/) || [])[1] || 200), body, headers: { 'content-type': (h.match(/content-type:\s*([^\r\n]+)/i) || [])[1] || 'application/octet-stream' } }); } catch (e) { return route.abort(); } }
(async()=>{const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium'});
for (const s of ['google-business-profile','google-ads-lsa','seo-services','ai-geo-optimization']) { const p=await b.newPage({viewport:{width:1366,height:800},ignoreHTTPSErrors:true}); await p.route('**/*', viaCurl);
 await p.goto('https://digitalgrowthcatalyze.com/'+s+'/?nc='+Math.random(),{waitUntil:'load',timeout:120000}); await p.waitForTimeout(1000);
 console.log('=====', s, JSON.stringify(await p.evaluate(()=>{const root=document.querySelector('[data-elementor-type="wp-page"]'); return [...root.children].map((c,i)=>{const hs=[...c.querySelectorAll('h1,h2,h3')].map(h=>h.textContent.trim().replace(/\s+/g,' ').slice(0,50)).slice(0,3); return [i, c.dataset.id, Math.round(c.getBoundingClientRect().height), getComputedStyle(c).backgroundColor, hs]})})));
 await p.close(); }
await b.close()})();
