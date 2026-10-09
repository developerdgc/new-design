const { chromium } = require('playwright');
const { execFileSync } = require('child_process');
async function viaCurl(route) { const req = route.request(); const u = req.url(); if (!/^https?:/.test(u) || req.method() !== 'GET') return route.continue();
  try { const hdr = '/tmp/_h' + process.pid; const body = execFileSync('curl', ['-sSL', '--max-time', '40', '-D', hdr, u], { maxBuffer: 64 * 1024 * 1024 });
    const h = require('fs').readFileSync(hdr, 'utf8').split(/\r?\n\r?\n/).filter(Boolean).pop();
    return route.fulfill({ status: +((h.match(/HTTP\/[\d.]+\s+(\d+)/) || [])[1] || 200), body, headers: { 'content-type': (h.match(/content-type:\s*([^\r\n]+)/i) || [])[1] || 'application/octet-stream' } }); } catch (e) { return route.abort(); } }
const P = JSON.parse(require('fs').readFileSync('/tmp/claude-0/-home-user-new-design/c0b0073b-578a-5cca-805d-2082208a4256/scratchpad/preview-main.json'));
(async()=>{const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium'});
for (const W of [1366,390]) for (const [n,u] of [['about','https://digitalgrowthcatalyze.com/about-us/?r=1'],['faqs','https://digitalgrowthcatalyze.com/faqs/?r=1'],['cases',P.cases]]) {
 const p=await b.newPage({viewport:{width:W,height:768},ignoreHTTPSErrors:true}); await p.route('**/*', viaCurl);
 await p.goto(u,{waitUntil:'load',timeout:120000}); await p.waitForTimeout(1500);
 console.log(W, n, JSON.stringify(await p.evaluate(()=>{const h=document.querySelector('h1'); let s=h; while(s && s.parentElement && !s.parentElement.matches('[data-elementor-type="wp-page"]')) s=s.parentElement; const r=s.getBoundingClientRect(), hb=h.getBoundingClientRect(); const box=h.closest('.e-con'); const br=box.getBoundingClientRect(); const cs=getComputedStyle(s); return {sectionTop:Math.round(r.top), sectionBottom:Math.round(r.bottom), h1Top:Math.round(hb.top), boxH:Math.round(br.height), boxW:Math.round(br.width), pad:cs.paddingTop+'/'+cs.paddingBottom, minH:cs.minHeight}})));
 await p.close(); }
await b.close()})();
