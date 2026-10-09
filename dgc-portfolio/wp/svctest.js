const { chromium } = require('playwright');
const { execFileSync } = require('child_process');
async function viaCurl(route) { const req = route.request(); const u = req.url(); if (!/^https?:/.test(u) || req.method() !== 'GET') return route.continue();
  try { const hdr = '/tmp/_h' + process.pid; const body = execFileSync('curl', ['-sSL', '--max-time', '40', '-D', hdr, u], { maxBuffer: 64 * 1024 * 1024 });
    const h = require('fs').readFileSync(hdr, 'utf8').split(/\r?\n\r?\n/).filter(Boolean).pop();
    return route.fulfill({ status: +((h.match(/HTTP\/[\d.]+\s+(\d+)/) || [])[1] || 200), body, headers: { 'content-type': (h.match(/content-type:\s*([^\r\n]+)/i) || [])[1] || 'application/octet-stream' } }); } catch (e) { return route.abort(); } }
const P = JSON.parse(require('fs').readFileSync('/tmp/claude-0/-home-user-new-design/c0b0073b-578a-5cca-805d-2082208a4256/scratchpad/preview-svc.json'));
(async()=>{const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium'});
for (const W of [1366, 390]) for (const [id,u] of Object.entries(P)) {
  const ctx=await b.newContext({viewport:{width:W,height:800},isMobile:W<500,hasTouch:W<500,ignoreHTTPSErrors:true}); const p=await ctx.newPage(); const errs=[]; p.on('pageerror',e=>errs.push(e.message)); await p.route('**/*', viaCurl);
  await p.goto(u,{waitUntil:'load',timeout:120000}); await p.waitForTimeout(1500);
  const info=await p.evaluate(()=>{const secs=document.querySelectorAll('.dgc-svc-cases'); const H=Math.round(secs[0].getBoundingClientRect().height); const btn=!!secs[0].querySelector('.dgc-mhero-btn');const root=[...document.querySelector('[data-elementor-type="wp-page"]').children]; const i=root.findIndex(c=>c.classList.contains('dgc-svc-cases')); const name=c=>{const h=c&&[...c.querySelectorAll('h2,h3')].find(x=>x.textContent.trim()); return h?h.textContent.trim().slice(0,22):''}; const g=document.querySelector('.dgc-svc-cgrid'); return {count:secs.length, H, btn, idx:i, before:name(root[i-1]), after:name(root[i+1]), cards:document.querySelectorAll('.dgc-svc-citem').length, shown:[...document.querySelectorAll('.dgc-svc-citem')].filter(e=>getComputedStyle(e).display!=='none').length, cardW:Math.round(document.querySelector('.dgc-svc-citem').getBoundingClientRect().width), rowsTop:[...new Set([...document.querySelectorAll('.dgc-svc-citem')].filter(e=>getComputedStyle(e).display!=='none').map(e=>Math.round(e.getBoundingClientRect().top)))].length, scrollW:document.documentElement.scrollWidth, noindex:[...document.querySelectorAll('meta[name=robots]')].some(m=>/noindex/.test(m.content)), gridScroll: g.scrollWidth>g.clientWidth+2}});
  const s=await p.$('.dgc-svc-cases'); await s.scrollIntoViewIfNeeded(); await p.waitForTimeout(1500); await s.screenshot({path:`svc-${id}-${W}.png`});
  const c=await p.$('.dgc-svc-cases a.dgc-case'); await c.click({force:true}); await p.waitForTimeout(2500);
  const modal=await p.evaluate(()=>{const m=document.querySelector('.dgc-cmodal[open]'); return m? m.querySelector('img').naturalWidth : 'closed'});
  console.log(W, id, JSON.stringify(info), 'modal', modal, errs.filter(e=>!/wp is not defined|Failed to fetch/.test(e)));
  await ctx.close(); }
await b.close()})();
