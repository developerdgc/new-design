const { chromium } = require('playwright');
const { execFileSync } = require('child_process');
async function viaCurl(route) { const req = route.request(); const u = req.url(); if (!/^https?:/.test(u) || req.method() !== 'GET') return route.continue();
  try { const hdr = '/tmp/_h' + process.pid; const body = execFileSync('curl', ['-sSL', '--max-time', '40', '-D', hdr, u], { maxBuffer: 64 * 1024 * 1024 });
    const h = require('fs').readFileSync(hdr, 'utf8').split(/\r?\n\r?\n/).filter(Boolean).pop();
    return route.fulfill({ status: +((h.match(/HTTP\/[\d.]+\s+(\d+)/) || [])[1] || 200), body, headers: { 'content-type': (h.match(/content-type:\s*([^\r\n]+)/i) || [])[1] || 'application/octet-stream' } }); } catch (e) { return route.abort(); } }
(async()=>{const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium'});
const ctx=await b.newContext({viewport:{width:390,height:844},isMobile:true,hasTouch:true,deviceScaleFactor:2,ignoreHTTPSErrors:true}); const p=await ctx.newPage(); await p.route('**/*', viaCurl);
await p.goto('https://newportfolio.digitalgrowthcatalyze.com/?r='+Math.random(),{waitUntil:'load',timeout:120000}); await p.waitForTimeout(1500);
const sl=await p.$('.dgc-lslider'); await sl.scrollIntoViewIfNeeded(); await p.waitForTimeout(2000); await sl.screenshot({path:'fin-slider-m.png'});
await p.tap('.dgc-tab.dgc-f-logo'); await p.waitForTimeout(800); const sl2=await p.$('.dgc-lslider'); await sl2.scrollIntoViewIfNeeded(); await p.waitForTimeout(800);
console.log('logo tab slider', await p.evaluate(()=>getComputedStyle(document.querySelector('.dgc-lslider')).display));
await ctx.close(); await b.close()})();
