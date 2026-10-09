const { chromium } = require('playwright');
const { execFileSync } = require('child_process');
async function viaCurl(route) { const req = route.request(); const u = req.url(); if (!/^https?:/.test(u) || req.method() !== 'GET') return route.continue();
  try { const hdr = '/tmp/_h' + process.pid; const body = execFileSync('curl', ['-sSL', '--max-time', '40', '-D', hdr, u], { maxBuffer: 64 * 1024 * 1024 });
    const h = require('fs').readFileSync(hdr, 'utf8').split(/\r?\n\r?\n/).filter(Boolean).pop();
    return route.fulfill({ status: +((h.match(/HTTP\/[\d.]+\s+(\d+)/) || [])[1] || 200), body, headers: { 'content-type': (h.match(/content-type:\s*([^\r\n]+)/i) || [])[1] || 'application/octet-stream' } }); } catch (e) { return route.abort(); } }
const W = +(process.env.W || 1440);
const ART = 'file:///home/user/new-design/dgc-portfolio/' + (process.env.APAGE || 'portfolio-artifact.html');
const WP = 'https://newportfolio.digitalgrowthcatalyze.com' + (process.env.WPAGE || '/') + '?r=' + Math.random();
const probe = () => {
  const box = e => { if (!e) return null; const r = e.getBoundingClientRect(), s = getComputedStyle(e); return { x: Math.round(r.x), y: Math.round(r.y + scrollY), w: Math.round(r.width), h: Math.round(r.height), pt: s.paddingTop, pb: s.paddingBottom }; };
  const roots = document.querySelector('[data-elementor-type="wp-page"]') ? [...document.querySelectorAll('[data-elementor-type="wp-page"] > .e-con, [data-elementor-type="wp-page"] > section')] : [...document.querySelectorAll('main > section, main > div')];
  const hdr = document.querySelector('.site-head, [data-elementor-type="header"]');
  const nav = document.querySelector('.site-head .nav .wrap, .dgc-nav');
  const ftr = document.querySelector('footer, [data-elementor-type="footer"]');
  const anims = document.getAnimations().map(a => (a.animationName || a.transitionProperty || '?') + ':' + (a.effect && a.effect.getTiming().duration)).slice(0, 40);
  const ff = e => e && (s => `${s.fontFamily.split(',')[0]} ${s.fontSize} ${s.fontWeight}`)(getComputedStyle(e));
  return { sections: roots.map(e => [e.className.toString().split(' ').filter(c => !c.startsWith('e-') && c !== 'elementor-element').join('.').slice(0, 40), box(e)]),
    hdr: box(hdr), nav: box(nav), ftr: box(ftr), anims,
    ftrText: ftr && [...new Set([...ftr.querySelectorAll('p,a,h2,h3,h4,h5,li,span')].filter(e => e.children.length === 0 && e.textContent.trim()).map(e => e.tagName + ' ' + ff(e)))].slice(0, 12),
    bodyP: ff(document.querySelector('.about p, .dgc-about p')) };
};
(async () => {
  const b = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium' });
  for (const [n, u] of [['ART', ART], ['WP', WP]]) {
    const p = await b.newPage({ viewport: { width: W, height: 900 }, ignoreHTTPSErrors: true }); await p.route('**/*', viaCurl);
    await p.goto(u, { waitUntil: 'load', timeout: 120000 }); await p.waitForTimeout(2500);
    console.log(n, JSON.stringify(await p.evaluate(probe)));
    await p.close();
  }
  await b.close();
})();
