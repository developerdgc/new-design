const { chromium } = require('playwright');
const { execFileSync } = require('child_process');
async function viaCurl(route) { const req = route.request(); const u = req.url(); if (!/^https?:/.test(u) || req.method() !== 'GET') return route.continue();
  try { const hdr = '/tmp/_h' + process.pid; const body = execFileSync('curl', ['-sSL', '--max-time', '40', '-D', hdr, u], { maxBuffer: 64 * 1024 * 1024 });
    const h = require('fs').readFileSync(hdr, 'utf8').split(/\r?\n\r?\n/).filter(Boolean).pop();
    return route.fulfill({ status: +((h.match(/HTTP\/[\d.]+\s+(\d+)/) || [])[1] || 200), body, headers: { 'content-type': (h.match(/content-type:\s*([^\r\n]+)/i) || [])[1] || 'application/octet-stream' } }); } catch (e) { return route.abort(); } }
(async()=>{const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium'});
for (const W of [1024, 768, 390]) { const p=await b.newPage({viewport:{width:W,height:1000},ignoreHTTPSErrors:true});await p.route('**/*', viaCurl);
await p.goto('https://newportfolio.digitalgrowthcatalyze.com/portfolio/?r='+Math.random(),{waitUntil:'load',timeout:120000});
for (const s of ['.dgc-stats','.dgc-reviews']) { const el=await p.$(s); if(!el){console.log('none',s);continue;} await el.scrollIntoViewIfNeeded(); await p.waitForTimeout(2500); await el.screenshot({path:`t${W}-${s.split(',')[0].replace(/\W/g,'')}.png`}); }
console.log(W, await p.evaluate(()=>{const r={};for(const s of ['.dgc-brand','.dgc-about','.dgc-process']){const e=document.querySelector(s); if(e) r[s]=[...e.querySelectorAll('img')].map(i=>[i.loading,i.complete,i.naturalWidth])} return r;}));
await p.close();}
await b.close()})();
