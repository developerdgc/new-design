const { chromium } = require('playwright');
const { execFileSync } = require('child_process');
async function viaCurl(route) { const req = route.request(); const u = req.url(); if (!/^https?:/.test(u) || req.method() !== 'GET') return route.continue();
  try { const hdr = '/tmp/_h' + process.pid; const body = execFileSync('curl', ['-sSL', '--max-time', '40', '-D', hdr, u], { maxBuffer: 64 * 1024 * 1024 });
    const h = require('fs').readFileSync(hdr, 'utf8').split(/\r?\n\r?\n/).filter(Boolean).pop();
    return route.fulfill({ status: +((h.match(/HTTP\/[\d.]+\s+(\d+)/) || [])[1] || 200), body, headers: { 'content-type': (h.match(/content-type:\s*([^\r\n]+)/i) || [])[1] || 'application/octet-stream' } }); } catch (e) { return route.abort(); } }
const U='https://newportfolio.digitalgrowthcatalyze.com';
(async()=>{const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium'});
{ const p=await b.newPage({viewport:{width:1366,height:620},ignoreHTTPSErrors:true}); const errs=[]; p.on('pageerror',e=>errs.push(e.message)); await p.route('**/*', viaCurl);
  await p.goto(U+'/?r='+Math.random(),{waitUntil:'load',timeout:120000}); await p.waitForTimeout(1500);
  console.log('widths', await p.evaluate(()=>{const g=document.querySelector('.dgc-grid').getBoundingClientRect(), br=document.querySelector('.dgc-brand').getBoundingClientRect(), gh=document.querySelector('.dgc-ghead').getBoundingClientRect(); return [Math.round(gh.x),Math.round(gh.width),Math.round(br.x),Math.round(br.width),Math.round(br.height)]}));
  const br=await p.$('.dgc-brand'); await br.scrollIntoViewIfNeeded(); await p.waitForTimeout(1500); await p.screenshot({path:'v3-brand.png'});
  const cases=await p.$$('a.dgc-case'); 
  await cases[0].scrollIntoViewIfNeeded(); await cases[0].click({force:true}); await p.waitForTimeout(6000);
  const s1=await p.evaluate(()=>document.querySelector('.dgc-cmodal img').getAttribute('src').split('/').pop()); await p.keyboard.press('Escape'); await p.waitForTimeout(500);
  await cases[1].click({force:true}); await p.waitForTimeout(150);
  const mid=await p.evaluate(()=>{const i=document.querySelector('.dgc-cmodal img');return [i.getAttribute('src').split('/').pop(), getComputedStyle(i).display, !document.querySelector('.dgc-cmodal__load').hidden]});
  await p.screenshot({path:'v3-case-mid.png'}); await p.waitForTimeout(6000);
  const end=await p.evaluate(()=>{const i=document.querySelector('.dgc-cmodal img');return [i.getAttribute('src').split('/').pop(), getComputedStyle(i).display, !document.querySelector('.dgc-cmodal__load').hidden, document.querySelector('.dgc-cmodal__bar b').textContent]});
  console.log('first', s1, '| second while loading', mid, '| second loaded', end, errs); await p.close(); }
{ const ctx=await b.newContext({viewport:{width:390,height:844},isMobile:true,hasTouch:true,ignoreHTTPSErrors:true}); const p=await ctx.newPage(); await p.route('**/*', viaCurl);
  await p.goto(U+'/?r='+Math.random(),{waitUntil:'load',timeout:120000}); await p.waitForTimeout(1200);
  console.log('mobile nav', await p.evaluate(()=>{const r=document.querySelector('.dgc-nav').getBoundingClientRect();return [r.x, r.width]})); await p.screenshot({path:'v3-hdr-m.png',clip:{x:0,y:0,width:390,height:200}}); await ctx.close(); }
await b.close()})();
