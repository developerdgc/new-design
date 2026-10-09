const { chromium } = require('playwright');
const { execFileSync } = require('child_process');
async function viaCurl(route) { const req = route.request(); const u = req.url(); if (!/^https?:/.test(u) || req.method() !== 'GET') return route.continue();
  try { const hdr = '/tmp/_h' + process.pid; const body = execFileSync('curl', ['-sSL', '--max-time', '40', '-D', hdr, u], { maxBuffer: 64 * 1024 * 1024 });
    const h = require('fs').readFileSync(hdr, 'utf8').split(/\r?\n\r?\n/).filter(Boolean).pop();
    return route.fulfill({ status: +((h.match(/HTTP\/[\d.]+\s+(\d+)/) || [])[1] || 200), body, headers: { 'content-type': (h.match(/content-type:\s*([^\r\n]+)/i) || [])[1] || 'application/octet-stream' } }); } catch (e) { return route.abort(); } }
(async()=>{const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium'});
for (const W of [1440, 390]) { const p=await b.newPage({viewport:{width:W,height:900},ignoreHTTPSErrors:true}); const errs=[]; p.on('pageerror',e=>errs.push(e.message)); await p.route('**/*', viaCurl);
 await p.goto('https://newportfolio.digitalgrowthcatalyze.com/?r='+Math.random(),{waitUntil:'load',timeout:120000});
 const s=await p.$('.dgc-reviews'); await s.scrollIntoViewIfNeeded(); await p.waitForTimeout(5000);
 console.log(W, JSON.stringify(await p.evaluate(()=>{const w=document.querySelector('.dgc-greviews'); const r=w.getBoundingClientRect(); return {h:Math.round(r.height), w:Math.round(r.width), ti:!!w.querySelector('.ti-widget'), count:document.querySelector('.dgc-score-small').textContent, scrollW:document.documentElement.scrollWidth}})), errs);
 await s.screenshot({path:`grev-${W}.png`}); await p.close(); }
await b.close()})();
