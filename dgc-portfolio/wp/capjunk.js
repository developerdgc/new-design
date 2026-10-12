const { chromium } = require('playwright');
const { execFileSync } = require('child_process');
async function viaCurl(route) { const req = route.request(); const u = req.url(); if (!/^https?:/.test(u) || req.method() !== 'GET') return route.continue();
  try { const hdr = '/tmp/_h' + process.pid; const body = execFileSync('curl', ['-sSL', '--max-time', '40', '-A', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/126 Safari/537.36', '-e', 'https://junkcarbuyer1.com/', '-D', hdr, u], { maxBuffer: 64 * 1024 * 1024 });
    const h = require('fs').readFileSync(hdr, 'utf8').split(/\r?\n\r?\n/).filter(Boolean).pop();
    return route.fulfill({ status: +((h.match(/HTTP\/[\d.]+\s+(\d+)/) || [])[1] || 200), body, headers: { 'content-type': (h.match(/content-type:\s*([^\r\n]+)/i) || [])[1] || 'application/octet-stream' } }); } catch (e) { return route.abort(); } }
(async()=>{const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium'});
const p=await b.newPage({viewport:{width:1366,height:900},ignoreHTTPSErrors:true}); await p.route('**/*', viaCurl);
await p.goto('https://junkcarbuyer1.com/',{waitUntil:'load',timeout:120000});
await p.evaluate(async()=>{for(let y=0;y<document.body.scrollHeight;y+=300){scrollTo(0,y);await new Promise(r=>setTimeout(r,150))} scrollTo(0,0)}); await p.waitForTimeout(3000);
console.log(await p.title(), await p.evaluate(()=>document.body.scrollHeight));
await p.screenshot({path:'../hires/cap-junkcarbuyer1.jpg', fullPage:true, type:'jpeg', quality:92}); await b.close()})();
