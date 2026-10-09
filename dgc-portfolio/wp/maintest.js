const { chromium } = require('playwright');
const { execFileSync } = require('child_process');
async function viaCurl(route) { const req = route.request(); const u = req.url(); if (!/^https?:/.test(u) || req.method() !== 'GET') return route.continue();
  try { const hdr = '/tmp/_h' + process.pid; const body = execFileSync('curl', ['-sSL', '--max-time', '40', '-D', hdr, u], { maxBuffer: 64 * 1024 * 1024 });
    const h = require('fs').readFileSync(hdr, 'utf8').split(/\r?\n\r?\n/).filter(Boolean).pop();
    return route.fulfill({ status: +((h.match(/HTTP\/[\d.]+\s+(\d+)/) || [])[1] || 200), body, headers: { 'content-type': (h.match(/content-type:\s*([^\r\n]+)/i) || [])[1] || 'application/octet-stream' } }); } catch (e) { return route.abort(); } }
const P = JSON.parse(require('fs').readFileSync('/tmp/claude-0/-home-user-new-design/c0b0073b-578a-5cca-805d-2082208a4256/scratchpad/preview-main.json'));
(async()=>{const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium'});
for (const W of [1440, 390]) for (const [n,u] of Object.entries(P)) {
  const ctx=await b.newContext({viewport:{width:W,height:900},isMobile:W<500,hasTouch:W<500,ignoreHTTPSErrors:true}); const p=await ctx.newPage(); const errs=[]; p.on('pageerror',e=>errs.push(e.message)); await p.route('**/*', viaCurl);
  await p.goto(u,{waitUntil:'load',timeout:120000});
  await p.evaluate(async()=>{for(let y=0;y<document.body.scrollHeight;y+=400){scrollTo(0,y);await new Promise(r=>setTimeout(r,120))} scrollTo(0,0)}); await p.waitForTimeout(2000);
  const info=await p.evaluate(()=>({title:document.title, robots:[...document.querySelectorAll('meta[name=robots]')].map(m=>m.content), header:!!document.querySelector('[data-elementor-type="header"]'), footer:!!document.querySelector('[data-elementor-type="footer"]'), snippet:!!document.getElementById('dgc-interactions-js'), cards:document.querySelectorAll('.dgc-cgrid > .dgc-cs-item').length, vids:document.querySelectorAll('.dgc-vgrid > .dgc-vthumb').length, scrollW:document.documentElement.scrollWidth}));
  let extra='';
  if (n==='cases') { await p.click('.dgc-pbody .dgc-sf-lsa'); await p.waitForTimeout(300); extra+=' lsa='+await p.$$eval('.dgc-cgrid > .dgc-cs-item', els=>els.filter(e=>getComputedStyle(e).display!=='none').length); await p.click('.dgc-pbody .dgc-sf-all'); await p.waitForTimeout(300);
    const c=await p.$('a.dgc-case'); await c.scrollIntoViewIfNeeded(); await c.click({force:true}); await p.waitForTimeout(3000); extra+=' modal='+await p.evaluate(()=>{const m=document.querySelector('.dgc-cmodal[open]'); return m? m.querySelector('img').naturalWidth : 'closed'}); await p.screenshot({path:`main-${n}-${W}-modal.png`}); await p.keyboard.press('Escape'); }
  if (n==='videos') { const v=await p.$('.dgc-vgrid .dgc-vbtn'); await v.scrollIntoViewIfNeeded(); await v.click({force:true}); await p.waitForTimeout(2000); extra+=' video='+await p.evaluate(()=>{const m=document.querySelector('.dgc-vmodal[open]'); return m? m.querySelector('video').currentSrc.split('/').pop() : 'closed'}); await p.keyboard.press('Escape'); }
  await p.evaluate(()=>scrollTo(0,0)); await p.waitForTimeout(400);
  await p.screenshot({path:`main-${n}-${W}.png`, fullPage:true});
  console.log(W, n, JSON.stringify(info), extra, errs);
  await ctx.close(); }
await b.close()})();
