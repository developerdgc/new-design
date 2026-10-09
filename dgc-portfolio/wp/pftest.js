const { chromium } = require('playwright');
const { execFileSync } = require('child_process');
async function viaCurl(route) { const req = route.request(); const u = req.url(); if (!/^https?:/.test(u) || req.method() !== 'GET') return route.continue();
  try { const hdr = '/tmp/_h' + process.pid; const body = execFileSync('curl', ['-sSL', '--max-time', '40', '-D', hdr, u], { maxBuffer: 64 * 1024 * 1024 });
    const h = require('fs').readFileSync(hdr, 'utf8').split(/\r?\n\r?\n/).filter(Boolean).pop();
    return route.fulfill({ status: +((h.match(/HTTP\/[\d.]+\s+(\d+)/) || [])[1] || 200), body, headers: { 'content-type': (h.match(/content-type:\s*([^\r\n]+)/i) || [])[1] || 'application/octet-stream' } }); } catch (e) { return route.abort(); } }
const U='https://portfolio.digitalgrowthcatalyze.com';
(async()=>{const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium'});
for (const W of [1440, 390]) {
 const ctx=await b.newContext({viewport:{width:W,height:900},isMobile:W<500,hasTouch:W<500,ignoreHTTPSErrors:true}); const p=await ctx.newPage(); const errs=[]; p.on('pageerror',e=>errs.push(e.message)); await p.route('**/*', viaCurl);
 await p.goto(U+'/?nc='+Math.random(),{waitUntil:'load',timeout:120000}); await p.waitForTimeout(2500);
 const home=await p.evaluate(()=>{const roots=[...document.querySelectorAll('[data-elementor-type="wp-page"] > .e-con')].map(e=>[...e.classList].find(c=>c.startsWith('dgc-'))); const v=document.querySelector('.dgc-vlist'); return {roots, strip:v&&v.querySelectorAll(':scope > .dgc-vthumb').length, caps:document.querySelectorAll('.dgc-clients .dgc-vcap').length, charts:getComputedStyle(document.querySelector('.dgc-case'),'::before').backgroundImage.slice(0,30), scrollW:document.documentElement.scrollWidth}});
 const s=await p.$('.dgc-clients'); await s.scrollIntoViewIfNeeded(); await p.waitForTimeout(800); await s.screenshot({path:`pf-strip-${W}.png`});
 await p.evaluate(()=>{const a=[...document.querySelectorAll('.dgc-vlist .dgc-vbtn')].find(x=>/review-5/.test(x.getAttribute('href'))); a.click();}); await p.waitForTimeout(2000);
 const m=await p.evaluate(()=>{const d=document.querySelector('.dgc-vmodal[open]'); return d?d.querySelector('video').currentSrc.split('/').pop():'closed'}); await p.keyboard.press('Escape');
 await p.goto(U+'/video-reviews/?nc='+Math.random(),{waitUntil:'load',timeout:120000}); await p.waitForTimeout(2000);
 const vr=await p.evaluate(()=>({vids:document.querySelectorAll('.dgc-vgrid > .dgc-vthumb').length, rows:[...new Set([...document.querySelectorAll('.dgc-vgrid > .dgc-vthumb')].map(e=>Math.round(e.getBoundingClientRect().top)))].length, text:document.querySelectorAll('.dgc-pbody .dgc-vcap, .dgc-vnote').length, scrollW:document.documentElement.scrollWidth}));
 const g=await p.$('.dgc-vgrid'); await g.scrollIntoViewIfNeeded(); await p.waitForTimeout(1500); await g.screenshot({path:`pf-vgrid-${W}.png`});
 console.log(W, JSON.stringify(home), 'stripModal', m, JSON.stringify(vr), errs);
 await ctx.close(); }
await b.close()})();
