const { chromium } = require('playwright');
const { execFileSync } = require('child_process');
async function viaCurl(route) { const req = route.request(); const u = req.url(); if (!/^https?:/.test(u) || req.method() !== 'GET') return route.continue();
  try { const hdr = '/tmp/_h' + process.pid; const body = execFileSync('curl', ['-sSL', '--max-time', '40', '-D', hdr, u], { maxBuffer: 64 * 1024 * 1024 });
    const h = require('fs').readFileSync(hdr, 'utf8').split(/\r?\n\r?\n/).filter(Boolean).pop();
    return route.fulfill({ status: +((h.match(/HTTP\/[\d.]+\s+(\d+)/) || [])[1] || 200), body, headers: { 'content-type': (h.match(/content-type:\s*([^\r\n]+)/i) || [])[1] || 'application/octet-stream' } }); } catch (e) { return route.abort(); } }
(async()=>{const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium'});
for (const [n,u] of [['main','https://digitalgrowthcatalyze.com/case-studies/'],['pf','https://portfolio.digitalgrowthcatalyze.com/case-studies/']]) {
  const p=await b.newPage({viewport:{width:1366,height:800},ignoreHTTPSErrors:true}); await p.route('**/*', viaCurl);
  await p.goto(u+'?nc='+Math.random(),{waitUntil:'load',timeout:120000}); await p.waitForTimeout(1500);
  const g=await p.$('.dgc-cgrid'); await g.scrollIntoViewIfNeeded(); await p.waitForTimeout(1500); await g.screenshot({path:`var-${n}.png`}); await p.close(); }
await b.close()})();
