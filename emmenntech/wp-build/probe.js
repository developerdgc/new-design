// node shot.js <url> <out.png> [width] [full:1|0]
const { chromium } = require('playwright');
const { execFile } = require('child_process');
let active=0;const q=[];const slot=()=>new Promise(r=>{if(active<3){active++;r();}else q.push(r)});const free=()=>{const n=q.shift();if(n)n();else active--;};
const UA='Mozilla/5.0';
const run1=u=>new Promise((res,rej)=>execFile('curl',['-sSL','-A',UA,'-D','-','--max-time','40',u],{encoding:'buffer',maxBuffer:64*1024*1024},(e,o)=>e?rej(e):res(o)));
const run=async u=>{await slot();await new Promise(r=>setTimeout(r,60));try{for(let t=0;t<5;t++){const o=await run1(u);const h=o.slice(0,600).toString();if(!/HTTP\/[\d.]+ (429|503)/.test(h))return o;await new Promise(r=>setTimeout(r,4000*(t+1)));}return await run1(u);}finally{free();}};
(async()=>{
 const [url,out,w='1440',full='1']=process.argv.slice(2);
 const b=await chromium.launch();
 const ctx=await b.newContext({viewport:{width:+w,height:900}});
 await ctx.route('**/*',async route=>{
   const u=route.request().url(); if(!u.startsWith('http')) return route.continue();
   if(/google-analytics|googletagmanager|gravatar/.test(u)) return route.abort();
   try{const s=await run(u);let idx=0,he;while(true){const e=s.indexOf('\r\n\r\n',idx);he=e;if(s.slice(e+4,e+9).toString().startsWith('HTTP/')){idx=e+4;continue;}break;}
     const head=s.slice(idx,he).toString(),body=s.slice(he+4);const ct=(head.match(/content-type:\s*([^\r\n]+)/i)||[])[1]||'application/octet-stream';
     await route.fulfill({status:parseInt(head.split(' ')[1])||200,headers:{'content-type':ct,'access-control-allow-origin':'*'},body});
   }catch(e){await route.abort();}
 });
 const p=await ctx.newPage();const errs=[];p.on('pageerror',e=>errs.push(e.message));
 await p.goto(url,{waitUntil:'domcontentloaded',timeout:120000});await p.waitForLoadState('load',{timeout:90000}).catch(()=>{});
 await p.evaluate(async()=>{for(let y=0;y<document.body.scrollHeight;y+=600){scrollTo(0,y);await new Promise(r=>setTimeout(r,120))}scrollTo(0,0)});
 await p.waitForTimeout(1500);
 const info=await p.evaluate(()=>({h:document.body.scrollHeight,ov:document.documentElement.scrollWidth-innerWidth,fonts:[...new Set([...document.querySelectorAll('h1,h2,p')].slice(0,8).map(e=>getComputedStyle(e).fontFamily))]}));
 console.log(JSON.stringify(info),'ERR',errs.slice(0,3));
 const probe=await p.evaluate(()=>{const r=s=>{const e=document.querySelector(s);if(!e)return null;const b=e.getBoundingClientRect();return [Math.round(b.width),Math.round(b.height)]};const wide=[...document.querySelectorAll("body *")].filter(e=>{const b=e.getBoundingClientRect();return b.right>innerWidth+2&&b.width>0}).filter(e=>!e.closest(".em-ticker")).map(e=>(e.textContent||"").trim().slice(0,40)+" | "+getComputedStyle(e).position+" R"+Math.round(e.getBoundingClientRect().right)).slice(0,12);return {slot:r(".em-globe-slot"),core:r(".em-globe-fallback"),iframes:document.querySelectorAll("iframe").length,wide}});console.log(JSON.stringify(probe,null,1));await b.close();
})();
