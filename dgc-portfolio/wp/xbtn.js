const { chromium } = require('playwright');
const { execFileSync } = require('child_process');
async function viaCurl(route) { const req = route.request(); const u = req.url(); if (!/^https?:/.test(u) || req.method() !== 'GET') return route.continue();
  try { const hdr = '/tmp/_h' + process.pid; const body = execFileSync('curl', ['-sSL', '--max-time', '40', '-D', hdr, u], { maxBuffer: 64 * 1024 * 1024 });
    const h = require('fs').readFileSync(hdr, 'utf8').split(/\r?\n\r?\n/).filter(Boolean).pop();
    return route.fulfill({ status: +((h.match(/HTTP\/[\d.]+\s+(\d+)/) || [])[1] || 200), body, headers: { 'content-type': (h.match(/content-type:\s*([^\r\n]+)/i) || [])[1] || 'application/octet-stream' } }); } catch (e) { return route.abort(); } }
(async()=>{const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium'});
for (const W of [1440, 390]) { const p=await b.newPage({viewport:{width:W,height:900},ignoreHTTPSErrors:true});await p.route('**/*', viaCurl);
await p.goto('https://newportfolio.digitalgrowthcatalyze.com/?r='+Math.random(),{waitUntil:'load',timeout:120000}); await p.waitForTimeout(1500);
for (const [name, sel, dlg] of [['case','.dgc-case','.dgc-cmodal'],['kit','.dgc-c-brand .dgc-lbtn, .dgc-lbtn','.dgc-kitmodal']]) {
  const el = await p.$(sel); if (!el) { console.log('no', sel); continue; } await el.scrollIntoViewIfNeeded(); await el.click({force:true}); await p.waitForTimeout(1500);
  const info = await p.evaluate(d=>{const m=document.querySelector(d+'[open]'); if(!m) return 'not open'; const x=m.querySelector('.dgc-x'); const r=x.getBoundingClientRect(), mr=m.getBoundingClientRect(), s=getComputedStyle(x), sv=x.querySelector('svg').getBoundingClientRect(); const ms=getComputedStyle(m);
    return {x:[r.x,r.y,r.width,r.height].map(Math.round), svg:[sv.x-r.x,sv.y-r.y,sv.width,sv.height].map(Math.round), modal:[mr.x,mr.y,mr.width,mr.height].map(Math.round), pad:s.padding, disp:s.display, trans:s.transition.slice(0,120), mOverflow:ms.overflow, vw:innerWidth, vh:innerHeight};}, dlg);
  console.log(W, name, JSON.stringify(info));
  await p.screenshot({path:`x-${name}-${W}.png`});
  const xb = await p.$(dlg+'[open] .dgc-x'); if (xb) { await xb.hover(); await p.waitForTimeout(120); await p.screenshot({path:`x-${name}-${W}-hover.png`, clip: await xb.boundingBox().then(bb=>({x:Math.max(0,bb.x-60),y:Math.max(0,bb.y-40),width:160,height:130}))}); await xb.click(); await p.waitForTimeout(600); }
}
await p.close(); }
await b.close()})();
