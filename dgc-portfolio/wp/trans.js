const { chromium } = require('playwright');
const { execFileSync } = require('child_process');
async function viaCurl(route) { const req = route.request(); const u = req.url(); if (!/^https?:/.test(u) || req.method() !== 'GET') return route.continue();
  try { const hdr = '/tmp/_h' + process.pid; const body = execFileSync('curl', ['-sSL', '--max-time', '40', '-D', hdr, u], { maxBuffer: 64 * 1024 * 1024 });
    const h = require('fs').readFileSync(hdr, 'utf8').split(/\r?\n\r?\n/).filter(Boolean).pop();
    return route.fulfill({ status: +((h.match(/HTTP\/[\d.]+\s+(\d+)/) || [])[1] || 200), body, headers: { 'content-type': (h.match(/content-type:\s*([^\r\n]+)/i) || [])[1] || 'application/octet-stream' } }); } catch (e) { return route.abort(); } }
(async () => {
  const b = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium' });
  for (const [n, u] of [['ART', 'file:///home/user/new-design/dgc-portfolio/portfolio-artifact.html'], ['WP', 'https://newportfolio.digitalgrowthcatalyze.com/?r=' + Math.random()]]) {
    const p = await b.newPage({ viewport: { width: 1440, height: 900 }, ignoreHTTPSErrors: true }); await p.route('**/*', viaCurl);
    await p.goto(u, { waitUntil: 'load', timeout: 120000 }); await p.waitForTimeout(2000);
    const r = await p.evaluate(() => { const out = {}; for (const e of document.querySelectorAll('body *')) { const s = getComputedStyle(e); if (s.transitionDuration === '0s') continue;
      const k = (e.className.toString().split(' ').filter(c => c && !/^e-|elementor/.test(c))[0] || e.tagName) ; const v = s.transitionProperty.slice(0, 50) + ' | ' + s.transitionDuration.slice(0, 40) + ' | ' + s.transitionTimingFunction.slice(0, 50);
      out[k] = out[k] || v; } return out; });
    console.log('=====', n); for (const [k, v] of Object.entries(r)) console.log(k.padEnd(22), v);
    await p.close();
  }
  await b.close();
})();
