const { chromium } = require('playwright');
(async () => { const b = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium' }); const p = await b.newPage({ viewport: { width: 528, height: 528 } });
  await p.route(/fonts\.googleapis\.com/, r => r.fulfill({ path: __dirname + '/../gf/gf.css', contentType: 'text/css' }));
  await p.route(/fonts\.gstatic\.com/, r => r.fulfill({ path: __dirname + '/../gf/' + r.request().url().split('/').pop(), contentType: 'font/woff2' }));
  await p.goto('file://' + __dirname + '/ring.html'); await p.evaluate(() => document.fonts.ready); await p.waitForTimeout(300);
  await p.locator('svg').screenshot({ path: __dirname + '/badge-ring.png', omitBackground: true }); await b.close(); })();
