document.addEventListener('DOMContentLoaded',function(){
  var burger=document.querySelector('.burger');
  var links=document.querySelector('.links');
  if(burger&&links){burger.addEventListener('click',function(){links.classList.toggle('open')});}
  document.querySelectorAll('.links a').forEach(function(a){
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
      var v=function(id){var el=document.getElementById(id);return el?el.value.trim():'';};
      var body='Name: '+v('name')+'\nEmail: '+v('email')+'\nTheme: '+v('theme')+'\n\n'+v('message');
      window.location.href='mailto:darkshadowjourneys@protonmail.com?subject='+encodeURIComponent('Journey enquiry - '+v('theme'))+'&body='+encodeURIComponent(body);
      var note=form.querySelector('.form-note');
      if(note){note.innerHTML='Your email app should now open with your enquiry ready to send. If nothing happened, email <a href="mailto:darkshadowjourneys@protonmail.com">darkshadowjourneys@protonmail.com</a> directly.';}
    });
  }
  document.querySelectorAll('a.btn-primary, a.nav-cta').forEach(function(a){
    a.addEventListener('click',function(){if(window.dsjTrack){window.dsjTrack('cta_click',{link_text:a.textContent.trim()});}});
  });
});
