const { chromium } = require('playwright');
const { execFileSync } = require('child_process');
const cache = new Map();
async function viaCurl(route) {
  const req = route.request(); const u = req.url();
  if (!/^https?:/.test(u) || req.method() !== 'GET') return route.continue();
  try {
    let hit = cache.get(u);
    if (!hit) {
      const hdr = '/tmp/_h' + process.pid;
      const body = execFileSync('curl', ['-sSL', '--max-time', '40', '-D', hdr, u], { maxBuffer: 64 * 1024 * 1024 });
      const h = require('fs').readFileSync(hdr, 'utf8').split(/\r?\n\r?\n/).filter(Boolean).pop();
      const ct = (h.match(/content-type:\s*([^\r\n]+)/i) || [])[1] || 'application/octet-stream';
      const st = +((h.match(/HTTP\/[\d.]+\s+(\d+)/) || [])[1] || 200);
      hit = { body, ct, st }; cache.set(u, hit);
    }
    return route.fulfill({ status: hit.st, body: hit.body, headers: { 'content-type': hit.ct, 'access-control-allow-origin': '*' } });
  } catch (e) { return route.abort(); }
}
(async () => {
  const [url, out, bg] = [process.argv[2], process.argv[3], process.argv[4] || ''];
  const b = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium' });
  for (const [n, w, h] of [['d', 1440, 900], ['m', 390, 844]]) {
    const p = await b.newPage({ viewport: { width: w, height: h }, ignoreHTTPSErrors: true }); const errs = []; p.on('pageerror', e => errs.push(e.message)); await p.route('**/*', viaCurl);
    await p.goto(url + (url.includes('?') ? '&' : '?') + 'nc=' + Date.now(), { waitUntil: 'load', timeout: 90000 });
    if (bg) await p.addStyleTag({ content: bg });
    await p.waitForTimeout(800);
    await p.screenshot({ path: `${out}-${n}.png`, fullPage: process.env.FULL === '1' });
    if (n === 'm' && process.env.MENU) { await p.click('.dgc-burger'); await p.waitForTimeout(300); await p.screenshot({ path: `${out}-m-menu.png` }); }
    if (process.env.SEL) { const el = await p.$(process.env.SEL); if (el) { await el.scrollIntoViewIfNeeded(); await p.waitForTimeout(+(process.env.WAIT || 500)); await el.screenshot({ path: `${out}-${n}-sel.png` }); if (process.env.SELHOVER) { const hh = await p.$(process.env.SELHOVER); await hh.hover({ force: true }); await p.waitForTimeout(500); await el.screenshot({ path: `${out}-${n}-selhover.png` }); } }
      if (process.env.HOVER) { const h = await p.$(process.env.HOVER); if (h) { await h.hover({ force: true }); await p.waitForTimeout(700); await p.screenshot({ path: `${out}-${n}-hover.png` }); await h.click({ force: true }); await p.waitForTimeout(900); await p.screenshot({ path: `${out}-${n}-click.png` }); console.log('modal open', await p.evaluate(() => !!document.querySelector('.dgc-vmodal[open]'))); } } }
    if (process.env.BOTTOM) { await p.evaluate(() => scrollTo(0, document.body.scrollHeight)); await p.waitForTimeout(700); await p.screenshot({ path: `${out}-${n}-bottom.png`, fullPage: false }); }
    if (process.env.SCROLL) { await p.evaluate(() => scrollTo(0, 400)); await p.waitForTimeout(600); await p.screenshot({ path: `${out}-${n}-scrolled.png` }); }
    console.log(n, 'errors', errs.slice(0, 3), 'scrollW', await p.evaluate(() => document.documentElement.scrollWidth));
    await p.close();
  }
  await b.close();
})();
