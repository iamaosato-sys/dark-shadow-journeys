/* Dark Shadow Journeys consent + Google Analytics 4 (Consent Mode v2).
   Analytics only loads if window.GA_ID is set AND the visitor accepts. */
(function () {
  var KEY = 'dsj.consent';
  window.dataLayer = window.dataLayer || [];
  function gtag() { dataLayer.push(arguments); }
  window.gtag = gtag;

  // Default: everything denied until the visitor chooses.
  gtag('consent', 'default', {
    ad_storage: 'denied',
    ad_user_data: 'denied',
    ad_personalization: 'denied',
    analytics_storage: 'denied',
    wait_for_update: 500
  });

  if (window.GSC_TOKEN) {
    var m = document.createElement('meta');
    m.name = 'google-site-verification';
    m.content = window.GSC_TOKEN;
    document.head.appendChild(m);
  }

  var loaded = false;
  function loadGA() {
    if (loaded || !window.GA_ID) return;
    loaded = true;
    var s = document.createElement('script');
    s.async = true;
    s.src = 'https://www.googletagmanager.com/gtag/js?id=' + encodeURIComponent(window.GA_ID);
    document.head.appendChild(s);
    gtag('js', new Date());
    gtag('config', window.GA_ID, { anonymize_ip: true });
  }

  function read() { try { return localStorage.getItem(KEY); } catch (e) { return null; } }
  function save(v) { try { localStorage.setItem(KEY, v); } catch (e) {} }

  function apply(choice) {
    if (choice === 'granted') {
      gtag('consent', 'update', { analytics_storage: 'granted' });
      loadGA();
    } else {
      gtag('consent', 'update', { analytics_storage: 'denied' });
    }
  }

  function banner() {
    if (document.getElementById('consentBanner')) return;
    var b = document.createElement('div');
    b.id = 'consentBanner';
    b.className = 'consent';
    b.setAttribute('role', 'region');
    b.setAttribute('aria-label', 'Cookie choices');
    b.innerHTML =
      '<p><strong>Cookies?</strong> ' +
      'With your OK we use Google Analytics cookies to count visits and improve the site. Nothing loads until you choose. ' +
      '<a href="privacy.html">Details</a></p>' +
      '<div class="consent-btns">' +
      '<button type="button" data-c="denied">Reject</button>' +
      '<button type="button" data-c="granted">Accept</button></div>';
    b.addEventListener('click', function (e) {
      var c = e.target.getAttribute && e.target.getAttribute('data-c');
      if (!c) return;
      save(c);
      apply(c);
      b.remove();
    });
    document.body.appendChild(b);
  }

  var current = read();
  if (current) apply(current);

  document.addEventListener('DOMContentLoaded', function () {
    if (!current) banner();
    var cs = document.getElementById('cookieSettings');
    if (cs) cs.addEventListener('click', banner);
  });

  window.dsjTrack = function (name, params) {
    if (loaded && read() === 'granted') gtag('event', name, params || {});
  };
})();
