const { chromium } = require('playwright');
const { execFileSync } = require('child_process');
async function viaCurl(route) { const req = route.request(); const u = req.url(); if (!/^https?:/.test(u) || req.method() !== 'GET') return route.continue();
  try { const hdr = '/tmp/_h' + process.pid; const body = execFileSync('curl', ['-sSL', '--max-time', '40', '-D', hdr, u], { maxBuffer: 64 * 1024 * 1024 });
    const h = require('fs').readFileSync(hdr, 'utf8').split(/\r?\n\r?\n/).filter(Boolean).pop();
    return route.fulfill({ status: +((h.match(/HTTP\/[\d.]+\s+(\d+)/) || [])[1] || 200), body, headers: { 'content-type': (h.match(/content-type:\s*([^\r\n]+)/i) || [])[1] || 'application/octet-stream' } }); } catch (e) { return route.abort(); } }
(async () => {
  const b = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium' });
  const p = await b.newPage({ viewport: { width: 1440, height: 900 }, ignoreHTTPSErrors: true }); const errs = []; p.on('pageerror', e => errs.push(e.message));
  await p.route('**/*', viaCurl);
  await p.goto('https://newportfolio.digitalgrowthcatalyze.com/?nc=' + Math.random(), { waitUntil: 'load', timeout: 120000 });
  await p.evaluate(async () => { for (let y = 0; y < document.body.scrollHeight; y += 600) { scrollTo(0, y); await new Promise(r => setTimeout(r, 200)); } scrollTo(0, 0); });
  await p.waitForTimeout(2500);
  await p.addStyleTag({ content: '.dgc-hdr{position:absolute!important;transform:none!important} .dgc-totop{display:none!important}' });
  await p.screenshot({ path: 'home-full.png', fullPage: true });
  console.log(errs, await p.evaluate(() => document.body.scrollHeight)); await b.close();
})();
