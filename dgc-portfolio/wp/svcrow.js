const { chromium } = require('playwright');
const { execFileSync } = require('child_process');
async function viaCurl(route) { const req = route.request(); const u = req.url(); if (!/^https?:/.test(u) || req.method() !== 'GET') return route.continue();
  try { const hdr = '/tmp/_h' + process.pid; const body = execFileSync('curl', ['-sSL', '--max-time', '40', '-D', hdr, u], { maxBuffer: 64 * 1024 * 1024 });
    const h = require('fs').readFileSync(hdr, 'utf8').split(/\r?\n\r?\n/).filter(Boolean).pop();
    return route.fulfill({ status: +((h.match(/HTTP\/[\d.]+\s+(\d+)/) || [])[1] || 200), body, headers: { 'content-type': (h.match(/content-type:\s*([^\r\n]+)/i) || [])[1] || 'application/octet-stream' } }); } catch (e) { return route.abort(); } }
(async()=>{const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium'});
for (const W of [1366, 1280]) { const p=await b.newPage({viewport:{width:W,height:800},ignoreHTTPSErrors:true}); await p.route('**/*', viaCurl);
await p.goto('https://digitalgrowthcatalyze.com/google-business-profile/?nc='+Math.random(),{waitUntil:'load',timeout:120000}); await p.waitForTimeout(1500);
const s=await p.$('.dgc-svc-cgrid'); await s.scrollIntoViewIfNeeded(); await p.waitForTimeout(1500);
console.log(W, JSON.stringify(await p.evaluate(()=>[...document.querySelectorAll('.dgc-svc-citem')].filter(e=>getComputedStyle(e).display!=='none').map(c=>{const cr=c.getBoundingClientRect(), g=c.querySelector('.dgc-case-go').getBoundingClientRect(); return [Math.round(cr.width), Math.round(cr.right-g.right)]}))));
await s.screenshot({path:`svc-row-${W}.png`}); await p.close(); }
await b.close()})();
