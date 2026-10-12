const { chromium } = require('playwright');
const { execFileSync } = require('child_process');
async function viaCurl(route) { const req = route.request(); const u = req.url(); if (!/^https?:/.test(u) || req.method() !== 'GET') return route.continue();
  try { const hdr = '/tmp/_h' + process.pid; const body = execFileSync('curl', ['-sSL', '--max-time', '40', '-D', hdr, u], { maxBuffer: 64 * 1024 * 1024 });
    const h = require('fs').readFileSync(hdr, 'utf8').split(/\r?\n\r?\n/).filter(Boolean).pop();
    return route.fulfill({ status: +((h.match(/HTTP\/[\d.]+\s+(\d+)/) || [])[1] || 200), body, headers: { 'content-type': (h.match(/content-type:\s*([^\r\n]+)/i) || [])[1] || 'application/octet-stream' } }); } catch (e) { return route.abort(); } }
(async()=>{const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium'});
const p=await b.newPage({viewport:{width:1440,height:900},ignoreHTTPSErrors:true}); await p.route('**/*', viaCurl);
await p.goto('https://portfolio.digitalgrowthcatalyze.com/?nc='+Math.random(),{waitUntil:'load',timeout:120000}); await p.waitForTimeout(2500);
const cnt=()=>p.evaluate(()=>{const o={}; [...document.querySelectorAll('.dgc-grid > *')].filter(c=>getComputedStyle(c).display!=='none').forEach(c=>{const k=(c.className.match(/dgc-c-(\w+)|dgc-ghead|dgc-lslider/)||['other'])[0]; o[k]=(o[k]||0)+1}); return JSON.stringify(o)});
console.log('load', await cnt(), await p.evaluate(()=>[...document.querySelectorAll('.dgc-tab')].map(t=>t.textContent.trim()+(t.classList.contains('is-active')?'*':'')).join(' ')));
await b.close()})();
