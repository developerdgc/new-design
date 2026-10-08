const { chromium } = require('playwright');
const { execFileSync } = require('child_process');
async function viaCurl(route) { const req = route.request(); const u = req.url(); if (!/^https?:/.test(u) || req.method() !== 'GET') return route.continue();
  try { const hdr = '/tmp/_h' + process.pid; const body = execFileSync('curl', ['-sSL', '--max-time', '40', '-D', hdr, u], { maxBuffer: 64 * 1024 * 1024 });
    const h = require('fs').readFileSync(hdr, 'utf8').split(/\r?\n\r?\n/).filter(Boolean).pop();
    return route.fulfill({ status: +((h.match(/HTTP\/[\d.]+\s+(\d+)/) || [])[1] || 200), body, headers: { 'content-type': (h.match(/content-type:\s*([^\r\n]+)/i) || [])[1] || 'application/octet-stream' } }); } catch (e) { return route.abort(); } }
(async () => {
  const b = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium' });
  for (const W of [1440, 390]) {
    const p = await b.newPage({ viewport: { width: W, height: 900 }, ignoreHTTPSErrors: true }); const errs = []; p.on('pageerror', e => errs.push(e.message));
    await p.route('**/*', viaCurl);
    await p.goto('https://newportfolio.digitalgrowthcatalyze.com/case-studies/?nc=' + Math.random(), { waitUntil: 'load', timeout: 120000 });
    await p.evaluate(async () => { for (let y = 0; y < document.body.scrollHeight; y += 500) { scrollTo(0, y); await new Promise(r => setTimeout(r, 200)); } scrollTo(0, 0); });
    await p.waitForTimeout(2000);
    await p.screenshot({ path: `cs-${W}-top.png` });
    const vis = () => p.$$eval('.dgc-cgrid > .dgc-cs-item', els => els.filter(e => getComputedStyle(e).display !== 'none').length);
    console.log(W, 'all', await vis(), 'current nav', await p.$$eval('.dgc-navlink.is-current', e => e.map(x => x.textContent.trim())));
    await p.click('.dgc-pbody .dgc-sf-lsa'); await p.waitForTimeout(300); console.log('lsa', await vis());
    await p.click('.dgc-pbody .dgc-sf-all'); await p.waitForTimeout(300);
    const lib = await p.$('.dgc-pbody'); await lib.scrollIntoViewIfNeeded(); await p.waitForTimeout(1500); await lib.screenshot({ path: `cs-${W}-lib.png` });
    await p.click('.dgc-cgrid .dgc-case', { force: true }); await p.waitForTimeout(2000); console.log('modal', await p.evaluate(() => !!document.querySelector('.dgc-cmodal[open]')));
    console.log('errors', errs, 'scrollW', await p.evaluate(() => document.documentElement.scrollWidth));
    await p.close();
  }
  await b.close();
})();
