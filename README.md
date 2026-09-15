# timqiu1998.github.io

Personal site for Tianyin (Tim) Qiu. Static HTML/CSS/JS, no build step required
to serve; design follows a black landing page with a particle-network canvas and
short interior pages.

```
index.html              landing page (hand-written)
about/ impact/ ...      interior pages, GENERATED from tools/content_*.html
tools/build.py          wraps each content file in the shared header/footer
tools/content_*.html    the editable body of each interior page
css/main.css            design tokens + all styles
js/network.js           landing canvas + mailto assembly
js/site.js              interior: progress bar, back-to-top, nav state, mailto
img/                    headshot, og.jpg (share preview), favicon.svg
assets/Tim_Qiu_CV.pdf   CV
```

## Editing

- Interior page text: edit `tools/content_<page>.html`, then run
  `python tools/build.py` and commit the regenerated `<page>/index.html`.
- Nav, header, footer, page titles: edit `PAGES`/`nav()`/`page()` in `tools/build.py`
  and rebuild. The landing page's pills are in `index.html` directly.
- Landing page: `index.html`.
- CV: replace `assets/Tim_Qiu_CV.pdf`, keeping the filename. Strip phone and
  home address from the contact line first; only the email is public.
- Email is written as `(at)`/`(dot)` in the HTML and turned into a `mailto:`
  by JavaScript, so it is clickable for people and useless to scrapers.

## Deploy

Push to `main`; GitHub Pages serves the root. Live at <https://timqiu1998.github.io>.
