## 2. Understanding Nuanced Semantic Elements

Beyond the common ones (`header`, `nav`, `main`, `footer`), there are 
more specific semantic elements for particular kinds of content.

| Element | Purpose |
|---|---|
| `<article>` | Self-contained content that makes sense on its own (e.g., a blog post, news article) |
| `<section>` | A thematic grouping of content, usually with its own heading |
| `<aside>` | Content related but separate from the main content (e.g., a sidebar, ads, related links) |
| `<figure>` | Groups media content (like an image) with its caption |
| `<figcaption>` | The caption for a `<figure>` |
| `<time>` | Represents a specific date/time |
| `<mark>` | Highlights text for reference |

### Examples

**`<article>` — self-contained content:**
```html
<article>
  <h2>How to Learn HTML</h2>
  <p>HTML is the foundation of web development...</p>
</article>
```

**`<section>` — grouped content with a theme:**
```html
<section>
  <h2>About Us</h2>
  <p>We are a small team building web tools.</p>
</section>
```

**`<aside>` — related but separate content:**
```html
<aside>
  <h3>Related Articles</h3>
  <ul>
    <li>Understanding CSS</li>
    <li>JavaScript Basics</li>
  </ul>
</aside>
```

**`<figure>` + `<figcaption>` — media with caption:**
```html
<figure>
  <img src="chart.png" alt="Sales chart">
  <figcaption>Fig 1: Sales growth over 6 months</figcaption>
</figure>
```

**`<time>` — machine-readable date:**
```html
<p>Published on <time datetime="2026-08-30">August 30, 2026</time></p>
```

### `article` vs `section` — Common Confusion
- Use `<article>` when the content could **stand alone** (e.g., a blog post, if removed from the page, would still make full sense)
- Use `<section>` when it's a **part of a larger whole**, grouped by theme, but not meant to stand alone independently

---