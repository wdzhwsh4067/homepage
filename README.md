# Shaohuang Wang — Personal Academic Website

A minimalist, static personal academic website for **Shaohuang Wang**, a Computer
Science Master's student at Xinjiang University and developer at NLPIR Lab.

The site is pure **HTML / CSS / JS** with no build step, no framework, and no
server. It works by simply opening `index.html` in a browser and is ready to host
on GitHub Pages.

## Structure

```
index.html        Single-page site (semantic HTML5)
css/style.css     All styling, design tokens, and responsive rules
js/main.js        Tiny progressive enhancement (footer year, mobile menu)
static/           Images: profile photo, publication figures, skills diagram
LICENSE
```

## Sections

About / Hero · Education · Publications (two featured papers with figures + full
list) · Research Experience · Skills · Contact, with a sticky top navigation that
anchor-links to each section.

## View locally

Open the file directly:

```
open index.html        # macOS
xdg-open index.html    # Linux
```

Or serve it (any static server works):

```
python3 -m http.server 8000
# then visit http://localhost:8000
```

## Deploy to GitHub Pages

1. Push this repository to GitHub.
2. In the repository, go to **Settings → Pages**.
3. Under **Build and deployment**, set **Source** to *Deploy from a branch*.
4. Choose the branch (e.g. `main`) and the `/ (root)` folder, then **Save**.
5. The site will be published at `https://<username>.github.io/<repo>/`.

No build or CI is required — GitHub Pages serves the static files as-is.

## Design

Neutral, light palette with a restrained warm terracotta accent, `Inter` for body
text and `Lora` for headings (loaded from Google Fonts), generous whitespace, and
a clean typographic hierarchy. Fully responsive: the layout collapses to a single
column on small screens and the navigation becomes a toggle menu.
