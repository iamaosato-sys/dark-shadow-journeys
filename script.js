document.addEventListener('DOMContentLoaded',function(){
  var burger=document.querySelector('.burger');
  var links=document.querySelector('nav.links');
  if(burger&&links){burger.addEventListener('click',function(){links.classList.toggle('open')});}
  document.querySelectorAll('nav.links a').forEach(function(a){
    if(a.getAttribute('href')===location.pathname.split('/').pop()||(location.pathname==='/'&&a.getAttribute('href')==='index.html')){a.classList.add('active')}
    a.addEventListener('click',function(){links&&links.classList.remove('open')});
  });
  document.querySelectorAll('.accordion-item').forEach(function(item){
    item.querySelector('.accordion-q').addEventListener('click',function(){
      var open=item.classList.contains('open');
      document.querySelectorAll('.accordion-item').forEach(function(i){i.classList.remove('open')});
      if(!open){item.classList.add('open')}
    });
  });
  var form=document.getElementById('enquiry-form');
  if(form){
    form.addEventListener('submit',function(e){
      e.preventDefault();
      var btn=form.querySelector('button[type=submit]');
      btn.textContent='Sending…';
      setTimeout(function(){
        form.innerHTML='<p style="color:#d4b876;font-family:Georgia,serif;font-size:1.2rem;">Thank you. Your enquiry has been received — we typically reply within one working day with a first thought on your journey.</p>';
      },700);
    });
  }
  if(typeof gtag==='function'){
    document.querySelectorAll('a.btn-primary, a.nav-cta').forEach(function(a){
      a.addEventListener('click',function(){gtag('event','cta_click',{link_text:a.textContent.trim()})});
    });
  }
});
