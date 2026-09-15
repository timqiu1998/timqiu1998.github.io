// Theme toggle: explicit choice wins, otherwise follow the OS.
(function () {
  var root = document.documentElement;

  function stored() {
    try { return localStorage.getItem('theme'); } catch (e) { return null; }
  }
  function save(v) {
    try { v ? localStorage.setItem('theme', v) : localStorage.removeItem('theme'); } catch (e) {}
  }
  function systemDark() {
    return window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches;
  }
  function current() {
    var t = root.getAttribute('data-theme');
    return t || (systemDark() ? 'dark' : 'light');
  }

  var toggle = document.querySelector('.theme-toggle');
  if (toggle) {
    toggle.addEventListener('click', function () {
      var next = current() === 'dark' ? 'light' : 'dark';
      root.setAttribute('data-theme', next);
      save(next);
      toggle.setAttribute('aria-label', next === 'dark' ? 'Switch to light theme' : 'Switch to dark theme');
    });
  }

  // Follow the OS only while the user has not made an explicit choice.
  if (window.matchMedia) {
    var mq = window.matchMedia('(prefers-color-scheme: dark)');
    var onChange = function () { if (!stored()) root.removeAttribute('data-theme'); };
    mq.addEventListener ? mq.addEventListener('change', onChange) : mq.addListener(onChange);
  }

  // Highlight the section currently in view.
  var links = Array.prototype.slice.call(document.querySelectorAll('.nav-links a[href^="#"]'));
  var targets = links
    .map(function (a) { return document.querySelector(a.getAttribute('href')); })
    .filter(Boolean);

  if (targets.length && 'IntersectionObserver' in window) {
    var obs = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        if (!e.isIntersecting) return;
        links.forEach(function (a) {
          var on = a.getAttribute('href') === '#' + e.target.id;
          a.style.color = on ? 'var(--text)' : '';
          a.style.background = on ? 'var(--bg-sunk)' : '';
        });
      });
    }, { rootMargin: '-72px 0px -70% 0px' });
    targets.forEach(function (t) { obs.observe(t); });
  }

  // Fall back to initials if no headshot has been dropped in yet.
  var avatar = document.querySelector('.avatar');
  if (avatar) {
    avatar.addEventListener('error', function () {
      var ph = document.createElement('div');
      ph.className = 'avatar';
      ph.style.cssText =
        'display:grid;place-items:center;font-size:2.6rem;font-weight:600;' +
        'color:var(--text-dim);letter-spacing:-.03em';
      ph.textContent = 'TQ';
      avatar.replaceWith(ph);
    });
  }
})();
