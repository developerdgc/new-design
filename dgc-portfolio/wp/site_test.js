const { chromium } = require('playwright');
const { execFileSync } = require('child_process');
async function viaCurl(route) { const req = route.request(); const u = req.url(); if (!/^https?:/.test(u) || req.method() !== 'GET') return route.continue();
  try { const hdr = '/tmp/_h' + process.pid; const body = execFileSync('curl', ['-sSL', '--max-time', '40', '-D', hdr, u], { maxBuffer: 64 * 1024 * 1024 });
    const h = require('fs').readFileSync(hdr, 'utf8').split(/\r?\n\r?\n/).filter(Boolean).pop();
    return route.fulfill({ status: +((h.match(/HTTP\/[\d.]+\s+(\d+)/) || [])[1] || 200), body, headers: { 'content-type': (h.match(/content-type:\s*([^\r\n]+)/i) || [])[1] || 'application/octet-stream' } }); } catch (e) { return route.abort(); } }
const fs = require('fs');
const PAGES = { home: '/portfolio/', cases: '/case-studies/', videos: '/video-reviews/' };
const WIDTHS = [1440, 1024, 768, 390];
const out = { pages: {}, links: new Set() };
(async () => {
  const b = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium' });
  for (const [name, path] of Object.entries(PAGES)) for (const W of WIDTHS) {
    const p = await b.newPage({ viewport: { width: W, height: 900 }, ignoreHTTPSErrors: true });
    const errs = [], cons = [], bad = [];
    p.on('pageerror', e => errs.push(e.message)); p.on('console', m => m.type() === 'error' && cons.push(m.text().slice(0, 160)));
    p.on('response', r => r.status() >= 400 && bad.push(r.status() + ' ' + r.url()));
    await p.route('**/*', viaCurl);
    await p.goto('https://newportfolio.digitalgrowthcatalyze.com' + path + '?nc=' + Math.random(), { waitUntil: 'load', timeout: 120000 });
    await p.evaluate(async () => { for (let y = 0; y < document.body.scrollHeight; y += 400) { scrollTo(0, y); await new Promise(r => setTimeout(r, 150)); } scrollTo(0, 0); });
    await p.waitForTimeout(2500);
    const r = await p.evaluate(() => {
      const vw = document.documentElement.clientWidth;
      const over = [...document.querySelectorAll('body *')].filter(e => { const b = e.getBoundingClientRect(); if (!b.width) return false;
        let a = e; while (a = a.parentElement) { const s = getComputedStyle(a); if (/hidden|clip/.test(s.overflowX)) return false; } return b.right > vw + 1 || b.left < -1; })
        .slice(0, 6).map(e => e.tagName + '.' + [...e.classList].join('.'));
      const imgs = [...document.images];
      return { scrollW: document.documentElement.scrollWidth, vw, over,
        brokenImg: imgs.filter(i => i.complete && !i.naturalWidth).map(i => i.src), noAlt: imgs.filter(i => !i.hasAttribute('alt')).map(i => i.src.split('/').pop()),
        h1: [...document.querySelectorAll('h1')].map(h => h.textContent.trim()), title: document.title,
        desc: (document.querySelector('meta[name=description]') || {}).content || null,
        links: [...document.querySelectorAll('a[href]')].map(a => a.href), emptyLinks: [...document.querySelectorAll('a')].filter(a => !a.getAttribute('href') || a.getAttribute('href') === '#').length,
        tiny: [...document.querySelectorAll('p,span,a,li')].filter(e => e.offsetParent && e.children.length === 0 && e.textContent.trim() && parseFloat(getComputedStyle(e).fontSize) < 11).length,
        h: document.body.scrollHeight };
    });
    r.links.forEach(l => out.links.add(l.split('#')[0].replace(/\?nc=.*/, ''))); delete r.links;
    out.pages[`${name}@${W}`] = { ...r, errs, cons: [...new Set(cons)], bad: [...new Set(bad)] };
    await p.screenshot({ path: `site-${name}-${W}.png`, fullPage: true });
    await p.close();
  }
  await b.close();
  out.links = [...out.links];
  fs.writeFileSync('site_test.json', JSON.stringify(out, null, 1));
  console.log('done');
})();
