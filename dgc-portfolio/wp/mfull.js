const { chromium } = require('playwright');
const { execFileSync } = require('child_process');
async function viaCurl(route) { const req = route.request(); const u = req.url(); if (!/^https?:/.test(u) || req.method() !== 'GET') return route.continue();
  try { const hdr = '/tmp/_h' + process.pid; const body = execFileSync('curl', ['-sSL', '--max-time', '40', '-D', hdr, u], { maxBuffer: 64 * 1024 * 1024 });
    const h = require('fs').readFileSync(hdr, 'utf8').split(/\r?\n\r?\n/).filter(Boolean).pop();
    return route.fulfill({ status: +((h.match(/HTTP\/[\d.]+\s+(\d+)/) || [])[1] || 200), body, headers: { 'content-type': (h.match(/content-type:\s*([^\r\n]+)/i) || [])[1] || 'application/octet-stream' } }); } catch (e) { return route.abort(); } }
const U = 'https://newportfolio.digitalgrowthcatalyze.com';
(async()=>{const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium'});
const ctx=await b.newContext({viewport:{width:390,height:844},isMobile:true,hasTouch:true,deviceScaleFactor:1,ignoreHTTPSErrors:true}); const p=await ctx.newPage(); await p.route('**/*', viaCurl);
for (const [n,path] of [['home','/'],['cases','/case-studies/'],['videos','/video-reviews/']]) {
  await p.goto(U+path+'?r='+Math.random(),{waitUntil:'load',timeout:120000});
  await p.evaluate(async()=>{for(let y=0;y<document.body.scrollHeight;y+=300){scrollTo(0,y);await new Promise(r=>setTimeout(r,100))} scrollTo(0,0)}); await p.waitForTimeout(2000);
  // vertical gaps between consecutive visible blocks inside each root section: report big empty bands
  console.log(n, JSON.stringify(await p.evaluate(()=>{const roots=[...document.querySelectorAll('[data-elementor-type="wp-page"] > .e-con, [data-elementor-type="footer"] .dgc-ftr')];
    return roots.map(r=>{const s=getComputedStyle(r);const cls=[...r.classList].find(c=>c.startsWith('dgc-'));return [cls,Math.round(r.getBoundingClientRect().height),s.paddingTop,s.paddingBottom]})})));
  await p.screenshot({path:`m-full-${n}.png`,fullPage:true});
}
await ctx.close(); await b.close()})();
