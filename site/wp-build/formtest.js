const { chromium } = require('playwright');
const { execFile } = require('child_process');
const fs=require('fs');
const run=(args)=>new Promise((res,rej)=>execFile('curl',args,{maxBuffer:1e8,encoding:'buffer'},(e,o)=>e?rej(e):res(o)));
(async()=>{const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium'});
const p=await b.newPage({viewport:{width:1366,height:900}});const posts=[];
await p.route(/^https:\/\//,async r=>{const req=r.request();const u=req.url();
  if(!/digiranxpro|fonts\.g|gstatic/.test(u)||/\.(jpg|jpeg|png|webp)/.test(u)) return r.abort();
  const args=['-sS','--max-time','60','-D','-','-X',req.method()];
  if(req.method()!=='GET'){const h=req.headers();for(const k of ['content-type','x-wp-nonce','accept','x-requested-with']) if(h[k]) args.push('-H',`${k}: ${h[k]}`);
    const body=req.postDataBuffer();if(body){fs.writeFileSync('/tmp/_body',body);args.push('--data-binary','@/tmp/_body');}posts.push(u);}
  else args.push('-L');
  args.push(u);
  try{const o=await run(args);let rest=o,head='',status=200;while(rest.slice(0,5).toString()==='HTTP/'){const s=rest.indexOf(Buffer.from('\r\n\r\n'));head=rest.slice(0,s).toString();rest=rest.slice(s+4);status=+(head.match(/HTTP\/\S+ (\d+)/)||[0,200])[1];}
  if(req.method()!=='GET') console.log('POST',u.slice(0,90),status,rest.toString().slice(0,300));
  await r.fulfill({status,body:rest,contentType:(head.match(/content-type:\s*([^\r\n]+)/i)||[])[1]||'text/html'});}catch(e){console.log('ERR',e.message.slice(0,100));await r.abort();}});
await p.goto('https://digiranxpro.com/contact-us/',{waitUntil:'load',timeout:120000});await p.waitForTimeout(2000);
const f=p.locator('form:has(select)').first();await f.scrollIntoViewIfNeeded();
await f.locator('input[type=text]').first().fill('TEST - QA check');
await f.locator('input[type=email]').first().fill('info@digiranxpro.com');
await f.locator('input[type=tel]').first().fill('07000000000');
await f.locator('select').first().selectOption({label:'SEO & Digital Marketing'},{force:true}).catch(e=>console.log('select skip'));
await f.locator('textarea').first().fill('This is an automated test submission from the website QA check. Please ignore.');
await f.locator('button, input[type=submit]').last().click();
await p.waitForTimeout(6000);
const vis=await p.evaluate(()=>{const s=document.querySelector('[data-e-type] .e-form-success-message-base, .e-form-success-message-base');const er=document.querySelector('.e-form-error-message-base');return {success:s?getComputedStyle(s).display:'none-found',error:er?getComputedStyle(er).display:'none-found',state:document.querySelector('form')?.getAttribute('data-form-state')||document.querySelector('form')?.className.slice(0,120)};});
console.log(JSON.stringify(vis));await f.screenshot({path:'formtest.png'});await b.close();})();
