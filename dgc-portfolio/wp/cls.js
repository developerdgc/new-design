const { chromium } = require('playwright');
const { execFileSync } = require('child_process');
async function viaCurl(route) { const req = route.request(); const u = req.url(); if (!/^https?:/.test(u) || req.method() !== 'GET') return route.continue();
  try { const hdr = '/tmp/_h' + process.pid; const body = execFileSync('curl', ['-sSL', '--max-time', '40', '-D', hdr, u], { maxBuffer: 64 * 1024 * 1024 });
    const h = require('fs').readFileSync(hdr, 'utf8').split(/\r?\n\r?\n/).filter(Boolean).pop();
    return route.fulfill({ status: +((h.match(/HTTP\/[\d.]+\s+(\d+)/) || [])[1] || 200), body, headers: { 'content-type': (h.match(/content-type:\s*([^\r\n]+)/i) || [])[1] || 'application/octet-stream' } }); } catch (e) { return route.abort(); } }
(async()=>{const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium'});
for (const path of ['/video-reviews/','/case-studies/','/']) { const p=await b.newPage({viewport:{width:412,height:823},ignoreHTTPSErrors:true});await p.route('**/*', viaCurl);
await p.addInitScript(()=>{window.__ls=[];new PerformanceObserver(l=>{for(const e of l.getEntries()){if(e.hadRecentInput)continue;window.__ls.push({v:+e.value.toFixed(4),t:Math.round(e.startTime),src:e.sources.map(s=>{const n=s.node;return n&&n.nodeType===1?(n.tagName+'.'+[...n.classList].filter(c=>c.startsWith('dgc')||c.startsWith('e-')).slice(0,3).join('.')+' '+JSON.stringify([s.previousRect.y,s.currentRect.y,s.previousRect.height,s.currentRect.height])):(n?n.nodeName:'?')})})}}).observe({type:'layout-shift',buffered:true});});
await p.goto('https://newportfolio.digitalgrowthcatalyze.com'+path+'?r='+Math.random(),{waitUntil:'load',timeout:120000}); await p.waitForTimeout(4000);
console.log(path, JSON.stringify(await p.evaluate(()=>window.__ls),null,0)); await p.close();}
await b.close()})();
