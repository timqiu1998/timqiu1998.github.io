// Drifting particle network behind the landing page.
(function () {
  var canvas = document.getElementById('network');
  if (!canvas) return;
  var ctx = canvas.getContext('2d');
  var reduce = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  var nodes = [];
  var nodeCount = window.innerWidth <= 768 ? 15 : 150;
  var connectionDistance = 200;
  var nodeSize = 2;
  var nodeColor = 'rgba(255, 255, 255, 0.55)';
  var lineColor = 'rgba(255, 255, 255, 0.07)';

  function size() {
    canvas.width = window.innerWidth;
    canvas.height = window.innerHeight;
  }

  function seed() {
    nodes.length = 0;
    for (var i = 0; i < nodeCount; i++) {
      nodes.push({
        x: Math.random() * canvas.width,
        y: Math.random() * canvas.height,
        vx: (Math.random() - 0.5) * 0.5,
        vy: (Math.random() - 0.5) * 0.5
      });
    }
  }

  function draw() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);

    for (var i = 0; i < nodes.length; i++) {
      var n = nodes[i];
      if (!reduce) {
        n.x += n.vx; n.y += n.vy;
        if (n.x < 0) n.x = canvas.width;  if (n.x > canvas.width)  n.x = 0;
        if (n.y < 0) n.y = canvas.height; if (n.y > canvas.height) n.y = 0;
      }
      ctx.beginPath();
      ctx.arc(n.x, n.y, nodeSize, 0, Math.PI * 2);
      ctx.fillStyle = nodeColor;
      ctx.fill();
    }

    for (i = 0; i < nodes.length; i++) {
      for (var j = i + 1; j < nodes.length; j++) {
        var dx = nodes[i].x - nodes[j].x, dy = nodes[i].y - nodes[j].y;
        var d = Math.sqrt(dx * dx + dy * dy);
        if (d < connectionDistance) {
          ctx.beginPath();
          ctx.moveTo(nodes[i].x, nodes[i].y);
          ctx.lineTo(nodes[j].x, nodes[j].y);
          ctx.strokeStyle = lineColor;
          ctx.lineWidth = 1 - d / connectionDistance;
          ctx.stroke();
        }
      }
    }
  }

  function loop() { draw(); requestAnimationFrame(loop); }

  size(); seed();
  window.addEventListener('resize', function () {
    nodeCount = window.innerWidth <= 768 ? 15 : 150;
    size(); seed(); if (reduce) draw();
  });

  if (reduce) draw(); else loop();

  // The address never appears assembled in the HTML; scrapers get the (at)/(dot) text.
  document.querySelectorAll('a[data-u][data-d]').forEach(function (a) {
    a.setAttribute('href', 'mailto:' + a.getAttribute('data-u') + '@' + a.getAttribute('data-d'));
  });
})();
