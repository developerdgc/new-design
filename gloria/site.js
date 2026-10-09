(function(){
  var root=document.documentElement;
  var reduce=window.matchMedia&&matchMedia('(prefers-reduced-motion: reduce)').matches;

  // quote forms (preview only, not connected yet)
  document.querySelectorAll('form[data-quote], #qf').forEach(function(f){
    f.addEventListener('submit',function(e){
      e.preventDefault();
      var ok=f.querySelector('.ok');if(ok)ok.classList.add('show');
    });
  });

  if(reduce||!('IntersectionObserver' in window))return;

  // scroll reveal with a small stagger inside each group
  var sel=['.sc','.col','.about .copy>*','.sechead>*','.center>*','.tile','.ctab .txt>*','.ctab .pic','.sbar',
           '.wtx>*','.wimg','.wc','.t','.gal figure','.fbox','footer .fc>div','.revbar','.ci','.cform','.cside','.mapcard'];
  var els=document.querySelectorAll(sel.join(','));
  els.forEach(function(el){
    var sib=el.parentElement?Array.prototype.indexOf.call(el.parentElement.children,el):0;
    el.style.setProperty('--d',(Math.min(sib,6)*90)+'ms');
    el.classList.add('rv');
  });
  root.classList.add('anim');

  function countUp(b){
    var to=+b.dataset.count,from=+(b.dataset.from||0),suf=b.dataset.suffix||'',t0=null,dur=1600;
    function step(t){if(!t0)t0=t;var k=Math.min(1,(t-t0)/dur),e=1-Math.pow(1-k,3);
      b.textContent=Math.round(from+(to-from)*e)+suf;if(k<1)requestAnimationFrame(step)}
    requestAnimationFrame(step);
  }
  var io=new IntersectionObserver(function(ents){
    ents.forEach(function(en){
      if(!en.isIntersecting)return;
      en.target.classList.add('in');
      en.target.querySelectorAll('[data-count]').forEach(countUp);
      io.unobserve(en.target);
    });
  },{threshold:.12,rootMargin:'0px 0px -40px 0px'});
  els.forEach(function(el){io.observe(el)});
  // anything already scrolled past (anchor jumps, restored scroll) shows at once
  addEventListener('load',function(){els.forEach(function(el){if(el.getBoundingClientRect().bottom<0)el.classList.add('in')})});
})();
