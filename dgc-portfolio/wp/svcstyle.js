const { chromium } = require('playwright');
const { execFileSync } = require('child_process');
async function viaCurl(route) { const req = route.request(); const u = req.url(); if (!/^https?:/.test(u) || req.method() !== 'GET') return route.continue();
  try { const hdr = '/tmp/_h' + process.pid; const body = execFileSync('curl', ['-sSL', '--max-time', '40', '-D', hdr, u], { maxBuffer: 64 * 1024 * 1024 });
    const h = require('fs').readFileSync(hdr, 'utf8').split(/\r?\n\r?\n/).filter(Boolean).pop();
    return route.fulfill({ status: +((h.match(/HTTP\/[\d.]+\s+(\d+)/) || [])[1] || 200), body, headers: { 'content-type': (h.match(/content-type:\s*([^\r\n]+)/i) || [])[1] || 'application/octet-stream' } }); } catch (e) { return route.abort(); } }
(async()=>{const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium'});
const p=await b.newPage({viewport:{width:1366,height:800},ignoreHTTPSErrors:true}); await p.route('**/*', viaCurl);
await p.goto('https://digitalgrowthcatalyze.com/google-business-profile/?nc='+Math.random(),{waitUntil:'load',timeout:120000});
await p.evaluate(async()=>{for(let y=0;y<document.body.scrollHeight;y+=400){scrollTo(0,y);await new Promise(r=>setTimeout(r,100))}}); await p.waitForTimeout(1500);
const root=await p.$$('[data-elementor-type="wp-page"] > *'); 
const a=await root[4].boundingBox(), c=await root[6].boundingBox();
await p.evaluate(y=>scrollTo(0,y), a.y + (await p.evaluate(()=>scrollY)) - 0);
console.log(JSON.stringify(await p.evaluate(()=>{const root=[...document.querySelector('[data-elementor-type="wp-page"]').children]; const pick=(sec)=>{const k=[...sec.querySelectorAll('h2,h3,h4,h5,h6,p,span')].find(e=>/WHY DGC|WHAT WE DO/.test(e.textContent.trim())&&e.children.length===0); const h=sec.querySelector('h2'); const st=e=>e&&(s=>({ff:s.fontFamily,fs:s.fontSize,fw:s.fontWeight,c:s.color,bg:s.backgroundColor,pad:s.padding,br:s.borderRadius,tt:s.textTransform,ls:s.letterSpacing}))(getComputedStyle(e)); const cs=getComputedStyle(sec); return {kicker:k&&k.textContent.trim(), kst:st(k), kparent:st(k&&k.parentElement), h2:h&&h.textContent.trim().slice(0,40), h2st:st(h), secPad:cs.padding, secBg:cs.backgroundColor+' '+cs.backgroundImage.slice(0,80)}}; return [pick(root[4]), pick(root[5])]})));
await root[5].screenshot({path:'svc-why.png'}); await root[6].screenshot({path:'svc-ben.png'}); await root[4].screenshot({path:'svc-what.png'});
await b.close()})();
