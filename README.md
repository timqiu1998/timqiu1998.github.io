# timqiu1998.github.io

Personal academic site for Tianyin (Tim) Qiu. Plain HTML/CSS/JS — no build step,
no dependencies, no framework.

```
index.html          all content lives here
css/style.css       design tokens + layout (light/dark)
js/main.js          theme toggle, scroll-spy nav, avatar fallback
img/headshot.jpg    profile photo
assets/             CV PDF
```

## Deploy

The repository must be named exactly `timqiu1998.github.io` for GitHub Pages to
serve it at the root domain.

```bash
git init
git add -A
git commit -m "Personal site"
git branch -M main
git remote add origin https://github.com/timqiu1998/timqiu1998.github.io.git
git push -u origin main
```

Then in the repository: **Settings → Pages → Build and deployment → Source:
Deploy from a branch**, branch `main`, folder `/ (root)`. The site goes live at
<https://timqiu1998.github.io> within a minute or two.

## Updating

- **Text** — edit `index.html`; sections are marked with comment banners.
- **CV** — replace `assets/Tim_Qiu_CV.pdf`, keeping the filename.
- **Photo** — replace `img/headshot.jpg` (square crop; 800×800 works well).
- **Colors** — the `:root` and `:root[data-theme="dark"]` blocks at the top of
  `css/style.css` hold every color as a variable. The dark palette is defined
  twice on purpose: once for the explicit toggle and once under
  `prefers-color-scheme` for visitors who never touch it.
