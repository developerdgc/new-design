const { chromium } = require('playwright');
const { execFileSync } = require('child_process');
async function viaCurl(route) { const req = route.request(); const u = req.url(); if (!/^https?:/.test(u) || req.method() !== 'GET') return route.continue();
  try { const hdr = '/tmp/_h' + process.pid; const body = execFileSync('curl', ['-sSL', '--max-time', '40', '-D', hdr, u], { maxBuffer: 64 * 1024 * 1024 });
    const h = require('fs').readFileSync(hdr, 'utf8').split(/\r?\n\r?\n/).filter(Boolean).pop();
    return route.fulfill({ status: +((h.match(/HTTP\/[\d.]+\s+(\d+)/) || [])[1] || 200), body, headers: { 'content-type': (h.match(/content-type:\s*([^\r\n]+)/i) || [])[1] || 'application/octet-stream' } }); } catch (e) { return route.abort(); } }
const P = JSON.parse(require('fs').readFileSync('/tmp/claude-0/-home-user-new-design/c0b0073b-578a-5cca-805d-2082208a4256/scratchpad/preview-main.json'));
(async()=>{const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium'});
for (const W of [1366, 390]) { const ctx=await b.newContext({viewport:{width:W,height:768},isMobile:W<500,hasTouch:W<500,ignoreHTTPSErrors:true}); const p=await ctx.newPage(); const errs=[]; p.on('pageerror',e=>errs.push(e.message)); await p.route('**/*', viaCurl);
 await p.goto(P.videos,{waitUntil:'load',timeout:120000}); await p.waitForTimeout(2000);
 const info=await p.evaluate(()=>({vids:document.querySelectorAll('.dgc-vgrid > .dgc-vthumb').length, text:[...document.querySelectorAll('.dgc-pbody p, .dgc-pbody span')].map(e=>e.textContent.trim()).filter(Boolean), posters:[...document.querySelectorAll('.dgc-vgrid img')].map(i=>i.naturalWidth>1).join(','), heroH:Math.round(document.querySelector('.dgc-mhero').getBoundingClientRect().height)}));
 await p.screenshot({path:`v6-${W}.png`});
 const g=await p.$('.dgc-vgrid'); await g.scrollIntoViewIfNeeded(); await p.waitForTimeout(1500); await g.screenshot({path:`v6-grid-${W}.png`});
 const v=await p.$$('.dgc-vgrid .dgc-vbtn'); await v[4].click({force:true}); await p.waitForTimeout(2500);
 const m=await p.evaluate(()=>{const d=document.querySelector('.dgc-vmodal[open]'); return d? [d.querySelector('video').currentSrc.split('/').pop(), getComputedStyle(d.querySelector('.dgc-vmodal__bar')).display] : 'closed'});
 console.log(W, JSON.stringify(info), m, errs); await ctx.close(); }
await b.close()})();
