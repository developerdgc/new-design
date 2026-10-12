const { chromium } = require('playwright');
const { execFileSync } = require('child_process');
async function viaCurl(route) { const req = route.request(); const u = req.url(); if (!/^https?:/.test(u) || req.method() !== 'GET') return route.continue();
  try { const hdr = '/tmp/_h' + process.pid; const body = execFileSync('curl', ['-sSL', '--max-time', '40', '-D', hdr, u], { maxBuffer: 64 * 1024 * 1024 });
    const h = require('fs').readFileSync(hdr, 'utf8').split(/\r?\n\r?\n/).filter(Boolean).pop();
    return route.fulfill({ status: +((h.match(/HTTP\/[\d.]+\s+(\d+)/) || [])[1] || 200), body, headers: { 'content-type': (h.match(/content-type:\s*([^\r\n]+)/i) || [])[1] || 'application/octet-stream' } }); } catch (e) { return route.abort(); } }
(async()=>{const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium'});
const p=await b.newPage({viewport:{width:1440,height:900},ignoreHTTPSErrors:true}); await p.route('**/*', viaCurl);
await p.goto('https://portfolio.digitalgrowthcatalyze.com/?nc='+Math.random(),{waitUntil:'load',timeout:120000}); await p.waitForTimeout(2500);
const order=()=>p.evaluate(()=>[...document.querySelectorAll('.dgc-grid > .dgc-c-web')].filter(c=>getComputedStyle(c).display!=='none').sort((a,b)=>(+a.style.order)-(+b.style.order)).slice(0,4).map(c=>(c.querySelector('a.dgc-device')||{}).href||c.textContent.trim().slice(0,30)));
console.log('All', JSON.stringify(await order()));
await p.click('.dgc-tab.dgc-f-web',{force:true}); await p.waitForTimeout(500); console.log('Websites', JSON.stringify(await order()), 'count', await p.evaluate(()=>document.querySelectorAll('.dgc-grid > .dgc-c-web').length));
const c=await p.$('.dgc-grid > .dgc-c-web a[href*="junkcarbuyer1"]'); const card=await c.evaluateHandle(a=>a.closest('.dgc-work')); await card.scrollIntoViewIfNeeded(); await p.waitForTimeout(1500); await card.screenshot({path:'../hires/junk-card.png'});
await b.close()})();
