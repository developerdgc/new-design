const { chromium } = require('playwright');
const { execFileSync } = require('child_process');
async function viaCurl(route) { const req = route.request(); const u = req.url(); if (!/^https?:/.test(u) || req.method() !== 'GET') return route.continue();
  try { const hdr = '/tmp/_h' + process.pid; const body = execFileSync('curl', ['-sSL', '--max-time', '40', '-D', hdr, u], { maxBuffer: 64 * 1024 * 1024 });
    const h = require('fs').readFileSync(hdr, 'utf8').split(/\r?\n\r?\n/).filter(Boolean).pop();
    return route.fulfill({ status: +((h.match(/HTTP\/[\d.]+\s+(\d+)/) || [])[1] || 200), body, headers: { 'content-type': (h.match(/content-type:\s*([^\r\n]+)/i) || [])[1] || 'application/octet-stream' } }); } catch (e) { return route.abort(); } }
(async()=>{const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium'});
for (const W of [1440,390]) { const ctx=await b.newContext({viewport:{width:W,height:900},isMobile:W<500,hasTouch:W<500,ignoreHTTPSErrors:true}); const p=await ctx.newPage(); const errs=[]; p.on('pageerror',e=>errs.push(e.message)); await p.route('**/*', viaCurl);
 await p.goto('https://portfolio.digitalgrowthcatalyze.com/?nc='+Math.random(),{waitUntil:'load',timeout:120000}); await p.waitForTimeout(2500);
 const r=await p.evaluate(()=>{const s=document.querySelector('.dgc-work-sec'); const g=s.querySelector('.dgc-grid'); const vis=[...g.children].filter(c=>getComputedStyle(c).display!=='none'); const sr=s.getBoundingClientRect();
   return {secW:Math.round(sr.width), secPad:getComputedStyle(s).paddingTop, id:s.id, visible:vis.length, tabs:s.querySelectorAll('.dgc-tab').length, scrollW:document.documentElement.scrollWidth, shot:!!s.querySelector('img.dgc-shot')}});
 const tab=await p.$('.dgc-tab.dgc-f-web'); await tab.scrollIntoViewIfNeeded(); await tab.click({force:true}); await p.waitForTimeout(500);
 const web=await p.evaluate(()=>[...document.querySelectorAll('.dgc-grid > .dgc-work')].filter(c=>getComputedStyle(c).display!=='none').length);
 await p.click('.dgc-tab.dgc-f-case',{force:true}); await p.waitForTimeout(500); const c=await p.$('.dgc-grid a.dgc-case:visible'); await c.click({force:true}); await p.waitForTimeout(2500);
 const modal=await p.evaluate(()=>{const m=document.querySelector('.dgc-cmodal[open]'); return m?m.querySelector('img').naturalWidth:'closed'}); await p.keyboard.press('Escape');
 await p.click('.dgc-tab.dgc-f-all',{force:true}); await p.waitForTimeout(600); const s=await p.$('.dgc-work-sec'); await s.screenshot({path:`emb-${W}.png`});
 console.log(W, JSON.stringify(r), 'webTab', web, 'caseModal', modal, errs); await ctx.close(); }
await b.close()})();
