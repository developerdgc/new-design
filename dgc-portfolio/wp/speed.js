const { chromium } = require('playwright');
const { execFileSync } = require('child_process');
async function viaCurl(route) { const req = route.request(); const u = req.url(); if (!/^https?:/.test(u) || req.method() !== 'GET') return route.continue();
  try { const hdr = '/tmp/_h' + process.pid; const body = execFileSync('curl', ['-sSL', '--max-time', '40', '-D', hdr, u], { maxBuffer: 64 * 1024 * 1024 });
    const h = require('fs').readFileSync(hdr, 'utf8').split(/\r?\n\r?\n/).filter(Boolean).pop();
    return route.fulfill({ status: +((h.match(/HTTP\/[\d.]+\s+(\d+)/) || [])[1] || 200), body, headers: { 'content-type': (h.match(/content-type:\s*([^\r\n]+)/i) || [])[1] || 'application/octet-stream' } }); } catch (e) { return route.abort(); } }
const W = +(process.env.W || 1440);
(async () => {
  const b = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium' });
  for (const [n, u] of [['ART', 'file:///home/user/new-design/dgc-portfolio/portfolio-artifact.html'], ['WP', 'https://newportfolio.digitalgrowthcatalyze.com/?r=' + Math.random()]]) {
    const p = await b.newPage({ viewport: { width: W, height: 900 }, ignoreHTTPSErrors: true }); await p.route('**/*', viaCurl);
    await p.goto(u, { waitUntil: 'load', timeout: 120000 }); await p.waitForTimeout(3000);
    const snap = () => p.evaluate(() => document.getAnimations().filter(a => a.animationName).map(a => { const e = a.effect.target; const m = new DOMMatrix(getComputedStyle(e).transform); const s = getComputedStyle(e);
      return [a.animationName, e.className.toString().split(' ').filter(c => !/^e-|elementor/.test(c)).join('.').slice(0, 30), +m.m41.toFixed(1), +m.m42.toFixed(1), s.objectPosition, Math.round(e.getBoundingClientRect().width), Math.round(e.getBoundingClientRect().height), a.effect.getComputedTiming().iterations, getComputedStyle(e).animationTimingFunction]; }));
    const a = await snap(); await p.waitForTimeout(1000); const c = await snap();
    console.log('=====', n); a.forEach((x, i) => console.log(x[0], x[1], 'dx/s', (c[i][2] - x[2]).toFixed(1), 'dy/s', (c[i][3] - x[3]).toFixed(1), 'objpos', x[4], '->', c[i][4], 'size', x[5] + 'x' + x[6], x[8]));
    await p.close();
  }
  await b.close();
})();
