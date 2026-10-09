const { chromium } = require('playwright');
const { execFileSync } = require('child_process');
async function viaCurl(route) { const req = route.request(); const u = req.url(); if (!/^https?:/.test(u) || req.method() !== 'GET') return route.continue();
  try { const hdr = '/tmp/_h' + process.pid; const body = execFileSync('curl', ['-sSL', '--max-time', '40', '-D', hdr, u], { maxBuffer: 64 * 1024 * 1024 });
    const h = require('fs').readFileSync(hdr, 'utf8').split(/\r?\n\r?\n/).filter(Boolean).pop();
    return route.fulfill({ status: +((h.match(/HTTP\/[\d.]+\s+(\d+)/) || [])[1] || 200), body, headers: { 'content-type': (h.match(/content-type:\s*([^\r\n]+)/i) || [])[1] || 'application/octet-stream' } }); } catch (e) { return route.abort(); } }
(async()=>{const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium'});
{ const p=await b.newPage({viewport:{width:1366,height:700},ignoreHTTPSErrors:true}); await p.route('**/*', viaCurl);
  await p.goto('https://digitalgrowthcatalyze.com/about-us/?nc='+Math.random(),{waitUntil:'load',timeout:120000}); await p.waitForTimeout(1500);
  const links=await p.$$eval('[data-elementor-type="header"] a', as=>as.map(a=>a.textContent.trim()).filter(Boolean));
  console.log('desktop header links', JSON.stringify(links));
  const c=p.locator('[data-elementor-type="header"] a:text-is("Company"):visible').first(); await c.hover(); await p.waitForTimeout(900);
  await p.screenshot({path:'menu-d.png', clip:{x:0,y:0,width:1366,height:330}}); await p.close(); }
{ const ctx=await b.newContext({viewport:{width:390,height:844},isMobile:true,hasTouch:true,ignoreHTTPSErrors:true}); const p=await ctx.newPage(); await p.route('**/*', viaCurl);
  await p.goto('https://digitalgrowthcatalyze.com/about-us/?nc='+Math.random(),{waitUntil:'load',timeout:120000}); await p.waitForTimeout(1500);
  const t=p.locator('[data-elementor-type="header"] .elementor-menu-toggle:visible, [data-elementor-type="header"] [class*="toggle"]:visible, [data-elementor-type="header"] [class*="hamburger"]:visible').first();
  console.log('toggles', await t.count()); if (await t.count()) { await t.tap(); await p.waitForTimeout(1200); }
  console.log('mobile Company links visible', await p.locator('a:text-is("Company"):visible').count());
  await p.screenshot({path:'menu-m.png'}); await ctx.close(); }
await b.close()})();
