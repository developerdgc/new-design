const { chromium } = require('playwright');
const { execFileSync } = require('child_process');
async function viaCurl(route) { const req = route.request(); const u = req.url(); if (!/^https?:/.test(u) || req.method() !== 'GET') return route.continue();
  try { const hdr = '/tmp/_h' + process.pid; const body = execFileSync('curl', ['-sSL', '--max-time', '40', '-D', hdr, u], { maxBuffer: 64 * 1024 * 1024 });
    const h = require('fs').readFileSync(hdr, 'utf8').split(/\r?\n\r?\n/).filter(Boolean).pop();
    return route.fulfill({ status: +((h.match(/HTTP\/[\d.]+\s+(\d+)/) || [])[1] || 200), body, headers: { 'content-type': (h.match(/content-type:\s*([^\r\n]+)/i) || [])[1] || 'application/octet-stream' } }); } catch (e) { return route.abort(); } }
const U = 'https://newportfolio.digitalgrowthcatalyze.com';
(async()=>{const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium'});
// desktop
{ const p=await b.newPage({viewport:{width:1440,height:900},ignoreHTTPSErrors:true}); const errs=[]; p.on('pageerror',e=>errs.push(e.message)); await p.route('**/*', viaCurl);
  await p.goto(U+'/?r='+Math.random(),{waitUntil:'load',timeout:120000}); await p.waitForTimeout(1500);
  console.log('D', JSON.stringify(await p.evaluate(()=>{const q=s=>document.querySelector(s); const st=document.querySelectorAll('.dgc-stat')[1]; const bs=getComputedStyle(st,'::before'); const n=q('.dgc-nav').getBoundingClientRect(); const c=q('.dgc-nav .dgc-btn-hot').getBoundingClientRect(); const br=q('.dgc-brand').getBoundingClientRect(); const f=getComputedStyle(q('.dgc-ftr-p')), fh=getComputedStyle(q('.dgc-ftr-h'));
   return {divider:[bs.top,bs.height,st.getBoundingClientRect().height], nav:[n.x,n.width,n.height], cta:[c.width,c.height], brand:[br.width,br.height], ftrP:f.fontFamily+' '+f.fontSize+' '+f.fontWeight, ftrH:fh.fontFamily+' '+fh.fontSize+' '+fh.fontWeight, shotSrc:q('img.dgc-shot').currentSrc.split('/').pop()}})));
  const el=await p.$('.dgc-brand'); await el.scrollIntoViewIfNeeded(); await p.waitForTimeout(1200); await el.screenshot({path:'r2-brand-d.png'});
  await p.click('.dgc-case',{force:true}); await p.waitForTimeout(2500);
  console.log('D case', JSON.stringify(await p.evaluate(()=>{const m=document.querySelector('.dgc-cmodal[open]'); const x=m.querySelector('.dgc-x').getBoundingClientRect(), sv=m.querySelector('.dgc-x svg').getBoundingClientRect(); const im=m.querySelector('img'); return {svgOff:[sv.x-x.x, sv.y-x.y, x.width], img:[im.naturalWidth, im.currentSrc.split('/').pop()]}})));
  await p.screenshot({path:'r2-case-d.png'}); await p.keyboard.press('Escape');
  const ftr=await p.$('.dgc-ftr'); await ftr.scrollIntoViewIfNeeded(); await p.waitForTimeout(500); await ftr.screenshot({path:'r2-ftr-d.png'});
  console.log('D errors', errs); await p.close(); }
// phone (touch)
{ const ctx=await b.newContext({viewport:{width:390,height:844},isMobile:true,hasTouch:true,deviceScaleFactor:2,ignoreHTTPSErrors:true}); const p=await ctx.newPage(); const errs=[]; p.on('pageerror',e=>errs.push(e.message)); await p.route('**/*', viaCurl);
  for (const path of ['/','/case-studies/','/video-reviews/']) {
    await p.goto(U+path+'?r='+Math.random(),{waitUntil:'load',timeout:120000}); await p.waitForTimeout(1500);
    console.log('M', path, JSON.stringify(await p.evaluate(()=>{const bs=[...document.querySelectorAll('.dgc-hero .dgc-btn-orange, .dgc-hero .dgc-btn-ghost, .dgc-phero-btns .dgc-btn')].map(e=>{const r=e.getBoundingClientRect();return [Math.round(r.x),Math.round(r.y),Math.round(r.width)]}); return {btns:bs, scrollW:document.documentElement.scrollWidth, nav:(r=>[r.x,r.width])(document.querySelector('.dgc-nav').getBoundingClientRect())}})));
  }
  await p.goto(U+'/?r='+Math.random(),{waitUntil:'load',timeout:120000}); await p.waitForTimeout(1500);
  console.log('M stats', await p.evaluate(()=>[...document.querySelectorAll('.dgc-stat')].map(e=>getComputedStyle(e).display).join(',')));
  const sl=await p.$('.dgc-lslider'); await sl.scrollIntoViewIfNeeded(); await p.waitForTimeout(1500);
  console.log('M slider', await p.evaluate(()=>{const s=document.querySelector('.dgc-lslider'); return [getComputedStyle(s).display, s.querySelectorAll('.dgc-lslide').length, [...document.querySelectorAll('.dgc-grid > .dgc-c-logo')].filter(e=>getComputedStyle(e).display!=='none').length, Math.round(s.getBoundingClientRect().width)]}));
  await sl.screenshot({path:'r2-slider-m.png'});
  await p.tap('.dgc-lslider__arrow[data-dir="1"]'); await p.waitForTimeout(800); await sl.screenshot({path:'r2-slider-m2.png'});
  await p.tap('.dgc-lslide:nth-child(2)'); await p.waitForTimeout(1200);
  console.log('M kit', JSON.stringify(await p.evaluate(()=>{const m=document.querySelector('.dgc-kitmodal[open]'); if(!m) return 'closed'; const r=m.getBoundingClientRect(), x=m.querySelector('.dgc-x').getBoundingClientRect(); return {modal:[r.x,r.y,r.width,r.height].map(Math.round), x:[x.x,x.y,x.right].map(Math.round), vw:innerWidth}})));
  await p.screenshot({path:'r2-kit-m.png'}); await p.tap('.dgc-kitmodal[open] .dgc-x'); await p.waitForTimeout(600);
  const c=await p.$('.dgc-case'); await c.scrollIntoViewIfNeeded(); await c.tap(); await p.waitForTimeout(2000);
  console.log('M case', JSON.stringify(await p.evaluate(()=>{const m=document.querySelector('.dgc-cmodal[open]'); const r=m.getBoundingClientRect(), x=m.querySelector('.dgc-x').getBoundingClientRect(); return {modal:[r.x,r.y,r.width,r.height].map(Math.round), x:[x.x,x.y,x.right].map(Math.round)}})));
  await p.screenshot({path:'r2-case-m.png'}); await p.tap('.dgc-cmodal[open] .dgc-x'); await p.waitForTimeout(600);
  const v=await p.$('.dgc-vthumb'); await v.scrollIntoViewIfNeeded(); 
  console.log('M vthumb transform after scroll', await p.evaluate(()=>getComputedStyle(document.querySelector('.dgc-vthumb')).transform));
  const st=await p.$('.dgc-stats'); await st.scrollIntoViewIfNeeded(); await p.waitForTimeout(600); await st.screenshot({path:'r2-stats-m.png'});
  await p.evaluate(()=>scrollTo(0,0)); await p.waitForTimeout(500); await p.screenshot({path:'r2-hero-m.png'});
  console.log('M errors', errs); await ctx.close(); }
await b.close()})();
