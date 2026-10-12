const { chromium } = require('playwright');
const { execFileSync } = require('child_process');
async function viaCurl(route) { const req = route.request(); const u = req.url(); if (!/^https?:/.test(u) || req.method() !== 'GET') return route.continue();
  try { const hdr = '/tmp/_h' + process.pid; const body = execFileSync('curl', ['-sSL', '--max-time', '40', '-D', hdr, u], { maxBuffer: 64 * 1024 * 1024 });
    const h = require('fs').readFileSync(hdr, 'utf8').split(/\r?\n\r?\n/).filter(Boolean).pop();
    return route.fulfill({ status: +((h.match(/HTTP\/[\d.]+\s+(\d+)/) || [])[1] || 200), body, headers: { 'content-type': (h.match(/content-type:\s*([^\r\n]+)/i) || [])[1] || 'application/octet-stream' } }); } catch (e) { return route.abort(); } }
(async()=>{const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium'});
const p=await b.newPage({viewport:{width:1440,height:900},ignoreHTTPSErrors:true}); await p.route('**/*', viaCurl);
await p.goto('https://portfolio.digitalgrowthcatalyze.com/?nc='+Math.random(),{waitUntil:'load',timeout:120000}); await p.waitForTimeout(2500);
console.log('order', await p.evaluate(()=>[...document.querySelectorAll('.dgc-grid > .dgc-work')].map(c=>(c.className.match(/dgc-c-(web|logo|case)/)||[])[1]).join('').replace(/(web)+/,'W..').replace(/(logo)+/,'L..').replace(/(case)+/,'C..')), 'total', await p.evaluate(()=>document.querySelectorAll('.dgc-grid > .dgc-work').length), 'leftover extras', await p.evaluate(()=>document.querySelectorAll('.dgc-work-extra > *').length));
await p.click('.dgc-tab.dgc-f-web',{force:true}); for(let i=0;i<6;i++){ const m=await p.$('.dgc-more-btn'); if(!m||!(await m.isVisible())) break; await m.click({force:true}); await p.waitForTimeout(300);}
console.log('web shown after more', await p.evaluate(()=>[...document.querySelectorAll('.dgc-grid > .dgc-c-web')].filter(c=>getComputedStyle(c).display!=='none').length));
await p.click('.dgc-tab.dgc-f-logo',{force:true}); await p.waitForTimeout(400); const l=await p.$('.dgc-lbtn'); await l.click({force:true}); await p.waitForTimeout(1200);
console.log('kit modal', await p.evaluate(()=>!!document.querySelector('.dgc-kitmodal[open] .dgc-brand')));
await b.close()})();
