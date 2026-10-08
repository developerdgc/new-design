const { chromium } = require('playwright');
const { execFileSync } = require('child_process');
const cache = new Map();
async function viaCurl(route) {
  const req = route.request(); const u = req.url();
  if (!/^https?:/.test(u) || req.method() !== 'GET') return route.continue();
  try {
    let hit = cache.get(u);
    if (!hit) { const hdr = '/tmp/_h' + process.pid; const body = execFileSync('curl', ['-sSL', '--max-time', '40', '-D', hdr, u], { maxBuffer: 64 * 1024 * 1024 });
      const h = require('fs').readFileSync(hdr, 'utf8').split(/\r?\n\r?\n/).filter(Boolean).pop();
      hit = { body, ct: (h.match(/content-type:\s*([^\r\n]+)/i) || [])[1] || 'application/octet-stream', st: +((h.match(/HTTP\/[\d.]+\s+(\d+)/) || [])[1] || 200) }; cache.set(u, hit); }
    return route.fulfill({ status: hit.st, body: hit.body, headers: { 'content-type': hit.ct } });
  } catch (e) { return route.abort(); }
}
(async () => {
  const b = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium' });
  const W = +(process.env.W || 1440);
  const p = await b.newPage({ viewport: { width: W, height: 900 }, ignoreHTTPSErrors: true }); const errs = []; p.on('pageerror', e => errs.push(e.message));
  await p.route('**/*', viaCurl);
  await p.goto('https://newportfolio.digitalgrowthcatalyze.com/?nc=' + Date.now() + Math.random(), { waitUntil: 'load', timeout: 120000 });
  await p.evaluate(async () => { document.querySelectorAll('img').forEach(i => i.loading = 'eager'); });
  const sec = await p.$('.dgc-work-sec');
  const vis = () => p.$$eval('.dgc-grid > .dgc-work', els => els.filter(e => getComputedStyle(e).display !== 'none').sort((a, b) => (+a.style.order) - (+b.style.order)).map(e => (e.className.match(/dgc-c-(\w+)/) || [])[1] + ((e.className.match(/dgc-ch-(\w+)/) || [])[1] ? ':' + e.className.match(/dgc-ch-(\w+)/)[1] : '')));
  console.log('ALL', (await vis()).join(' '));
  await p.evaluate(async () => { const s = document.querySelector('.dgc-work-sec'); const top = s.getBoundingClientRect().top + scrollY; for (let y = top; y < top + s.offsetHeight; y += 500) { scrollTo(0, y); await new Promise(r => setTimeout(r, 250)); } }); await p.waitForTimeout(2500);
  await sec.screenshot({ path: `work-${W}-all.png` });
  await p.click('.dgc-f-web'); await p.waitForTimeout(400); console.log('WEB', (await vis()).length, 'more visible', await p.$eval('.dgc-more-btn', e => getComputedStyle(e).display));
  await p.click('.dgc-more-btn'); await p.waitForTimeout(300); console.log('WEB+more', (await vis()).length);
  await p.click('.dgc-f-logo'); await p.waitForTimeout(400); console.log('LOGO', (await vis()).join(' '));
  await p.click('.dgc-lbtn'); await p.waitForTimeout(800); console.log('kit open', await p.evaluate(() => !!document.querySelector('.dgc-kitmodal[open]')));
  await p.screenshot({ path: `work-${W}-kit.png` }); await p.keyboard.press('Escape');
  await p.click('.dgc-f-case'); await p.waitForTimeout(400); console.log('CASE', (await vis()).join(' '), 'allcase', await p.$eval('.dgc-allcase', e => getComputedStyle(e).display));
  await p.click('.dgc-sub-case .dgc-sf-ppc'); await p.waitForTimeout(300); console.log('CASE ppc', (await vis()).join(' '));
  await p.click('.dgc-f-all'); await p.waitForTimeout(300);
  await p.click('.dgc-grid .dgc-case', { force: true }); await p.waitForTimeout(2500); console.log('case modal', await p.evaluate(() => !!document.querySelector('.dgc-cmodal[open]')));
  await p.screenshot({ path: `work-${W}-case.png` });
  console.log('errors', errs, 'scrollW', await p.evaluate(() => document.documentElement.scrollWidth));
  await b.close();
})();
