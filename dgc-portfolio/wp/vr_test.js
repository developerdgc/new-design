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
    await p.goto('https://newportfolio.digitalgrowthcatalyze.com/video-reviews/?nc=' + Math.random(), { waitUntil: 'load', timeout: 120000 });
    await p.evaluate(async () => { for (let y = 0; y < document.body.scrollHeight; y += 500) { scrollTo(0, y); await new Promise(r => setTimeout(r, 200)); } scrollTo(0, 0); });
    await p.waitForTimeout(2000);
    await p.screenshot({ path: `vr-${W}-top.png` });
    console.log(W, 'cards', await p.$$eval('.dgc-vgrid > .dgc-vthumb', e => e.length), 'nav', await p.$$eval('.dgc-navlink.is-current', e => e.map(x => x.textContent.trim())), 'id', await p.evaluate(() => document.querySelector('.dgc-pbody').id));
    const lib = await p.$('.dgc-pbody'); await lib.scrollIntoViewIfNeeded(); await p.waitForTimeout(1500); await lib.screenshot({ path: `vr-${W}-lib.png` });
    if (W > 1000) { await p.hover('.dgc-vgrid > .dgc-vthumb:nth-child(2) .dgc-vbtn'); await p.waitForTimeout(700); await lib.screenshot({ path: `vr-${W}-hover.png` }); }
    await p.click('.dgc-vgrid .dgc-vbtn', { force: true }); await p.waitForTimeout(2500);
    console.log('modal', await p.evaluate(() => { const d = document.querySelector('.dgc-vmodal'); const v = d && d.querySelector('video'); return [!!(d && d.open), v && v.currentSrc.slice(-30), d && d.querySelector('.dgc-vmodal__bar').textContent]; }));
    await p.screenshot({ path: `vr-${W}-modal.png` });
    console.log('errors', errs, 'scrollW', await p.evaluate(() => document.documentElement.scrollWidth));
    await p.close();
  }
  await b.close();
})();
