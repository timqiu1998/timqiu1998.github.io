// Interior pages: back-to-top button, reading-progress fallback, current-page nav state.
(function () {
  var top = document.querySelector('.back-to-top');
  var bar = document.querySelector('.reading-progress');
  var scrollTimeline = CSS.supports && CSS.supports('animation-timeline: scroll()');

  function onScroll() {
    var y = window.scrollY || document.documentElement.scrollTop;
    if (top) top.classList.toggle('visible', y > 400);
    if (bar && !scrollTimeline) {
      var max = document.documentElement.scrollHeight - window.innerHeight;
      bar.style.transform = 'scaleX(' + (max > 0 ? Math.min(1, y / max) : 0) + ')';
    }
  }
  window.addEventListener('scroll', onScroll, { passive: true });
  onScroll();

  if (top) {
    top.addEventListener('click', function (e) {
      e.preventDefault();
      window.scrollTo({ top: 0, behavior: 'smooth' });
    });
  }

  // Mark the nav link for the page we are on.
  var here = location.pathname.replace(/\/index\.html$/, '/');
  document.querySelectorAll('.nav-link').forEach(function (a) {
    var href = a.getAttribute('href');
    if (href && href !== '/' && here.indexOf(href.replace(/\/$/, '')) === 0) {
      a.setAttribute('aria-current', 'page');
    }
  });

  var y = document.getElementById('year');
  if (y) y.textContent = new Date().getFullYear();

  // The address never appears assembled in the HTML; scrapers get the (at)/(dot) text.
  document.querySelectorAll('a[data-u][data-d]').forEach(function (a) {
    a.setAttribute('href', 'mailto:' + a.getAttribute('data-u') + '@' + a.getAttribute('data-d'));
  });
})();
