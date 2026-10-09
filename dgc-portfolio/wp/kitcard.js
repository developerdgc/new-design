const { chromium } = require('playwright');
const { execFileSync } = require('child_process');
async function viaCurl(route) { const req = route.request(); const u = req.url(); if (!/^https?:/.test(u) || req.method() !== 'GET') return route.continue();
  try { const hdr = '/tmp/_h' + process.pid; const body = execFileSync('curl', ['-sSL', '--max-time', '40', '-D', hdr, u], { maxBuffer: 64 * 1024 * 1024 });
    const h = require('fs').readFileSync(hdr, 'utf8').split(/\r?\n\r?\n/).filter(Boolean).pop();
    return route.fulfill({ status: +((h.match(/HTTP\/[\d.]+\s+(\d+)/) || [])[1] || 200), body, headers: { 'content-type': (h.match(/content-type:\s*([^\r\n]+)/i) || [])[1] || 'application/octet-stream' } }); } catch (e) { return route.abort(); } }
(async()=>{const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium'});
for (const W of [360, 390]) { const ctx=await b.newContext({viewport:{width:W,height:800},isMobile:true,hasTouch:true,deviceScaleFactor:2,ignoreHTTPSErrors:true}); const p=await ctx.newPage(); await p.route('**/*', viaCurl);
 await p.goto('https://newportfolio.digitalgrowthcatalyze.com/?r='+Math.random(),{waitUntil:'load',timeout:120000}); await p.waitForTimeout(1200);
 const sl=await p.$('.dgc-lslider'); await sl.scrollIntoViewIfNeeded(); await p.waitForTimeout(800);
 for (const k of [1,2]) { await p.tap(`.dgc-lslide:nth-child(${k})`); await p.waitForTimeout(1800);
  const card=await p.$('.dgc-kitmodal[open] .dgc-lcard'); console.log(W,k, JSON.stringify(await p.evaluate(()=>{const m=document.querySelector('.dgc-kitmodal[open]'); const q=s=>{const e=m.querySelector(s); if(!e) return null; const r=e.getBoundingClientRect(); return [Math.round(r.x),Math.round(r.y),Math.round(r.width),Math.round(r.height)]}; return {card:q('.dgc-lcard'), sheet:q('.dgc-lsheet'), foot:q('.dgc-lfoot'), id:q('.dgc-lid'), sw:q('.dgc-lsw')}})));
  await card.screenshot({path:`kitcard-${W}-${k}.png`}); await p.tap('.dgc-kitmodal[open] .dgc-x'); await p.waitForTimeout(600); }
 await ctx.close(); }
await b.close()})();
