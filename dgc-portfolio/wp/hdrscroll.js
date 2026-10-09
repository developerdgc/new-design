const { chromium } = require('playwright');
const { execFileSync } = require('child_process');
async function viaCurl(route) { const req = route.request(); const u = req.url(); if (!/^https?:/.test(u) || req.method() !== 'GET') return route.continue();
  try { const hdr = '/tmp/_h' + process.pid; const body = execFileSync('curl', ['-sSL', '--max-time', '40', '-D', hdr, u], { maxBuffer: 64 * 1024 * 1024 });
    const h = require('fs').readFileSync(hdr, 'utf8').split(/\r?\n\r?\n/).filter(Boolean).pop();
    return route.fulfill({ status: +((h.match(/HTTP\/[\d.]+\s+(\d+)/) || [])[1] || 200), body, headers: { 'content-type': (h.match(/content-type:\s*([^\r\n]+)/i) || [])[1] || 'application/octet-stream' } }); } catch (e) { return route.abort(); } }
(async()=>{const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium'});
const ctx=await b.newContext({viewport:{width:390,height:844},isMobile:true,hasTouch:true,ignoreHTTPSErrors:true}); const p=await ctx.newPage(); await p.route('**/*', viaCurl);
await p.goto('https://newportfolio.digitalgrowthcatalyze.com/case-studies/?r='+Math.random(),{waitUntil:'load',timeout:120000}); await p.waitForTimeout(1000);
await p.evaluate(()=>scrollTo(0,1500)); await p.waitForTimeout(1000);
console.log('logged-out', await p.evaluate(()=>{const n=document.querySelector('.dgc-nav').getBoundingClientRect();const h=document.querySelector('.dgc-hdr');return [Math.round(n.y), h.className.includes('is-scrolled'), getComputedStyle(h).top, getComputedStyle(h).transform]}));
// simulate a logged-in visit: admin bar class + 46px bar that scrolls away on small screens
await p.evaluate(()=>document.body.classList.add('admin-bar')); await p.waitForTimeout(500);
console.log('admin-bar', await p.evaluate(()=>{const n=document.querySelector('.dgc-nav').getBoundingClientRect();return Math.round(n.y)}));
await ctx.close(); await b.close()})();
