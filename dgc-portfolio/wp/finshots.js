const { chromium } = require('playwright');
const { execFileSync } = require('child_process');
async function viaCurl(route) { const req = route.request(); const u = req.url(); if (!/^https?:/.test(u) || req.method() !== 'GET') return route.continue();
  try { const hdr = '/tmp/_h' + process.pid; const body = execFileSync('curl', ['-sSL', '--max-time', '40', '-D', hdr, u], { maxBuffer: 64 * 1024 * 1024 });
    const h = require('fs').readFileSync(hdr, 'utf8').split(/\r?\n\r?\n/).filter(Boolean).pop();
    return route.fulfill({ status: +((h.match(/HTTP\/[\d.]+\s+(\d+)/) || [])[1] || 200), body, headers: { 'content-type': (h.match(/content-type:\s*([^\r\n]+)/i) || [])[1] || 'application/octet-stream' } }); } catch (e) { return route.abort(); } }
(async()=>{const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium'});
for (const W of [1024]) { const p=await b.newPage({viewport:{width:W,height:900},ignoreHTTPSErrors:true}); await p.route('**/*', viaCurl);
await p.goto('https://newportfolio.digitalgrowthcatalyze.com/?r='+Math.random(),{waitUntil:'load',timeout:120000});
const e=await p.$$('.dgc-brand'); await e[1].scrollIntoViewIfNeeded(); await p.waitForTimeout(3000); await e[0].scrollIntoViewIfNeeded(); await p.waitForTimeout(3000);
const bb=await e[0].boundingBox(); await p.screenshot({path:`fin-brand-${W}.png`, clip:{x:0,y:bb.y-10,width:W,height:Math.min(880,bb.height*2+60)}});
const l=await p.$('.dgc-lbtn'); await l.scrollIntoViewIfNeeded(); await l.click({force:true}); await p.waitForTimeout(2500); await p.screenshot({path:`fin-kit-${W}.png`});
await p.close(); }
await b.close()})();
