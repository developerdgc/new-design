const { chromium } = require('playwright');
const { execFileSync } = require('child_process');
async function viaCurl(route) { const req = route.request(); const u = req.url(); if (!/^https?:/.test(u) || req.method() !== 'GET') return route.continue();
  try { const hdr = '/tmp/_h' + process.pid; const body = execFileSync('curl', ['-sSL', '--max-time', '40', '-D', hdr, u], { maxBuffer: 64 * 1024 * 1024 });
    const h = require('fs').readFileSync(hdr, 'utf8').split(/\r?\n\r?\n/).filter(Boolean).pop();
    return route.fulfill({ status: +((h.match(/HTTP\/[\d.]+\s+(\d+)/) || [])[1] || 200), body, headers: { 'content-type': (h.match(/content-type:\s*([^\r\n]+)/i) || [])[1] || 'application/octet-stream' } }); } catch (e) { return route.abort(); } }
const fs = require('fs');
const low = JSON.parse(fs.readFileSync('../hires/low.json')).filter(x => x[2] && !/clarkexteriors/.test(x[2]));
(async () => {
  const b = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium' });
  for (const [k, , url] of low) {
    const p = await b.newPage({ viewport: { width: 1366, height: 900 }, ignoreHTTPSErrors: true });
    await p.route('**/*', viaCurl);
    try {
      await p.goto(url, { waitUntil: 'load', timeout: 90000 });
      await p.evaluate(async () => { for (let y = 0; y < document.body.scrollHeight; y += 300) { scrollTo(0, y); await new Promise(r => setTimeout(r, 120)); } scrollTo(0, 0); });
      await p.waitForTimeout(2500);
      await p.screenshot({ path: `../hires/cap-${k}.jpg`, fullPage: true, type: 'jpeg', quality: 92 });
      console.log('ok', k);
    } catch (e) { console.log('fail', k, e.message.slice(0, 80)); }
    await p.close();
  }
  await b.close();
})();
