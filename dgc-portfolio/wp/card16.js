const { chromium } = require('playwright');
const { execFileSync } = require('child_process');
async function viaCurl(route) { const req = route.request(); const u = req.url(); if (!/^https?:/.test(u) || req.method() !== 'GET') return route.continue();
  try { const hdr = '/tmp/_h' + process.pid; const body = execFileSync('curl', ['-sSL', '--max-time', '40', '-D', hdr, u], { maxBuffer: 64 * 1024 * 1024 });
    const h = require('fs').readFileSync(hdr, 'utf8').split(/\r?\n\r?\n/).filter(Boolean).pop();
    return route.fulfill({ status: +((h.match(/HTTP\/[\d.]+\s+(\d+)/) || [])[1] || 200), body, headers: { 'content-type': (h.match(/content-type:\s*([^\r\n]+)/i) || [])[1] || 'application/octet-stream' } }); } catch (e) { return route.abort(); } }
const P = JSON.parse(require('fs').readFileSync('/tmp/claude-0/-home-user-new-design/c0b0073b-578a-5cca-805d-2082208a4256/scratchpad/preview-main.json'));
(async()=>{const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium'});
const p=await b.newPage({viewport:{width:1440,height:900},ignoreHTTPSErrors:true}); await p.route('**/*', viaCurl);
await p.goto(P.cases,{waitUntil:'load',timeout:120000}); await p.waitForTimeout(1500);
const cards=await p.$$('.dgc-cgrid > .dgc-cs-item'); await cards[15].scrollIntoViewIfNeeded(); await p.waitForTimeout(2500);
console.log(JSON.stringify(await p.evaluate(()=>[...document.querySelectorAll('.dgc-cgrid > .dgc-cs-item')].filter((c,i)=>i==2||i==15).map(c=>{const f=c.querySelector('.dgc-case-foot'); const b=e=>{if(!e)return null;const r=e.getBoundingClientRect();return [Math.round(r.x),Math.round(r.width),Math.round(r.height)]}; return {card:b(c), foot:b(f), kids:[...f.children].map(k=>[k.className.toString().split(' ').filter(x=>x.startsWith('dgc')).join('.'), b(k), k.tagName, k.currentSrc?k.currentSrc.split('/').pop():''])}}))));
await cards[15].screenshot({path:'main-card16.png'}); await b.close()})();
