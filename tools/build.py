"""Assemble the interior pages: wrap each content_<page>.html in the shared chrome.

Run:  python build.py   (writes <page>/index.html into the site repo)
The landing page (index.html) is a separate hand-written file.
"""
import io, os, re

SITE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
HERE = os.path.dirname(os.path.abspath(__file__))
NAME = "Tianyin (Tim) Qiu, PhD"
BASE = "https://timqiu1998.github.io"

PAGES = [  # (slug, nav label, <title>, description)
    ("about",        "About",        "About",        "Who I am and what I build: agentic AI and physics-based design for drug discovery."),
    ("impact",       "Impact",       "Impact",       "What shipped, what it changed, and the numbers behind it."),
    ("experience",   "Experience",   "Experience",   "Industry and research experience."),
    ("publications", "Publications", "Publications", "Peer-reviewed publications and preprints."),
    ("recognition",  "Recognition",  "Recognition",  "Funding, awards, and professional service."),
]

ICONS = {
    "github":   '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 .5C5.65.5.5 5.65.5 12c0 5.08 3.29 9.39 7.86 10.91.58.1.79-.25.79-.56v-2.17c-3.2.7-3.87-1.37-3.87-1.37-.52-1.33-1.28-1.68-1.28-1.68-1.04-.71.08-.7.08-.7 1.15.08 1.76 1.19 1.76 1.19 1.03 1.76 2.7 1.25 3.36.96.1-.75.4-1.25.73-1.54-2.55-.29-5.24-1.28-5.24-5.69 0-1.26.45-2.29 1.19-3.09-.12-.29-.52-1.46.11-3.05 0 0 .97-.31 3.17 1.18a11 11 0 0 1 5.78 0c2.2-1.49 3.17-1.18 3.17-1.18.63 1.59.23 2.76.11 3.05.74.8 1.19 1.83 1.19 3.09 0 4.42-2.7 5.39-5.26 5.68.41.36.78 1.05.78 2.12v3.15c0 .31.21.67.8.56A11.5 11.5 0 0 0 23.5 12C23.5 5.65 18.35.5 12 .5z"/></svg>',
    "linkedin": '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M20.45 20.45h-3.55v-5.57c0-1.33-.03-3.04-1.85-3.04-1.85 0-2.14 1.45-2.14 2.94v5.67H9.36V9h3.41v1.56h.05c.47-.9 1.63-1.85 3.36-1.85 3.6 0 4.27 2.37 4.27 5.45v6.29zM5.34 7.43a2.06 2.06 0 1 1 0-4.12 2.06 2.06 0 0 1 0 4.12zM7.12 20.45H3.56V9h3.56v11.45zM22.22 0H1.77C.79 0 0 .77 0 1.73v20.54C0 23.23.79 24 1.77 24h20.45c.98 0 1.78-.77 1.78-1.73V1.73C24 .77 23.2 0 22.22 0z"/></svg>',
    "scholar":  '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 3 1 9l11 6 9-4.91V17h2V9L12 3zm0 14.1L5 13.3v3.2c0 1.9 3.1 3.5 7 3.5s7-1.6 7-3.5v-3.2l-7 3.8z"/></svg>',
    "orcid":    '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 0a12 12 0 1 0 0 24 12 12 0 0 0 0-24zM7.37 5.4a1.03 1.03 0 1 1 0 2.06 1.03 1.03 0 0 1 0-2.06zm-.8 3.2h1.6v9.2h-1.6V8.6zm3.5 0h4.3c4.1 0 5.9 2.93 5.9 4.6 0 2.36-1.87 4.6-5.87 4.6h-4.33V8.6zm1.6 1.45v6.3h2.5c3.6 0 4.43-2.7 4.43-3.15 0-1.73-1.1-3.15-4.5-3.15h-2.43z"/></svg>',
    "cv":       '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M6 2h8l6 6v14H6V2zm7 1.5V9h5.5L13 3.5zM8 12h8v1.5H8V12zm0 3h8v1.5H8V15zm0 3h5v1.5H8V18z"/></svg>',
}
LINKS = [
    ("GitHub",         "https://github.com/timqiu1998",                              "github"),
    ("LinkedIn",       "https://www.linkedin.com/in/tianyin-qiu-9b863b152",          "linkedin"),
    ("Google Scholar", "https://scholar.google.com/citations?user=ViLQhdYAAAAJ",     "scholar"),
    ("ORCID",          "https://orcid.org/0000-0002-3490-8469",                      "orcid"),
    ("CV (PDF)",       "/assets/Tim_Qiu_CV.pdf",                                     "cv"),
]

def nav(current):
    out = []
    for slug, label, _, _ in PAGES:
        cur = ' aria-current="page"' if slug == current else ''
        out.append('            <a href="/%s/" class="nav-link"%s>%s</a>' % (slug, cur, label))
    out.append('            <a href="/assets/Tim_Qiu_CV.pdf" class="nav-link">CV</a>')
    return "\n".join(out)

def footer_links():
    return "\n".join(
        '            <a href="%s" title="%s" aria-label="%s"%s>%s</a>'
        % (url, label, label, '' if url.startswith('/') else ' rel="noopener"', ICONS[icon])
        for label, url, icon in LINKS
    )

def page(slug, label, title, desc, body):
    return """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>%(title)s | %(name)s</title>
<meta name="description" content="%(desc)s">
<meta property="og:type" content="website">
<meta property="og:title" content="%(title)s | %(name)s">
<meta property="og:description" content="%(desc)s">
<meta property="og:url" content="%(base)s/%(slug)s/">
<meta property="og:image" content="%(base)s/img/headshot.jpg">
<link rel="canonical" href="%(base)s/%(slug)s/">
<link rel="icon" href="/img/favicon.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Spectral:wght@200;300;400;500;600&amp;display=swap" rel="stylesheet">
<link rel="stylesheet" href="/css/main.css">
</head>
<body>
    <div class="reading-progress" aria-hidden="true"></div>
    <header class="header">
        <h1 class="site-title"><a href="/">%(name)s</a></h1>
        <nav class="navigation" aria-label="Site">
%(nav)s
        </nav>
    </header>
    <div class="container">
        <article class="content %(slug)s">
            <h1>%(label)s</h1>
            <hr>
%(body)s
        </article>
    </div>
    <footer class="footer">
        <div class="footer-links">
%(flinks)s
        </div>
        <p class="copyright">&copy; <span id="year">2026</span> %(name)s</p>
    </footer>
    <a href="#" class="back-to-top" aria-label="Back to top">
        <svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 19V5M5 12l7-7 7 7"/></svg>
    </a>
    <script src="/js/site.js"></script>
</body>
</html>
""" % dict(title=title, name=NAME, desc=desc, base=BASE, slug=slug, label=label,
           nav=nav(slug), body=body.rstrip("\n"), flinks=footer_links())

def main():
    for slug, label, title, desc in PAGES:
        src = os.path.join(HERE, "content_%s.html" % slug)
        if not os.path.exists(src):
            print("skip  %-13s (no %s)" % (slug, os.path.basename(src))); continue
        body = io.open(src, encoding="utf8").read()
        out_dir = os.path.join(SITE, slug); os.makedirs(out_dir, exist_ok=True)
        out = os.path.join(out_dir, "index.html")
        io.open(out, "w", encoding="utf8", newline="\n").write(page(slug, label, title, desc, body))
        words = len(re.sub(r"<[^>]+>", " ", body).split())
        print("wrote %-13s %5d words" % (slug + "/", words))

if __name__ == "__main__":
    main()
