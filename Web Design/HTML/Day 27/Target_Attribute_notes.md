## 1. The `target` Attribute

The `target` attribute on an `<a>` tag controls **where** the linked 
page opens.

```html
<a href="https://example.com" target="_blank">Visit Example</a>
```

### The 4 Possible Values

| Value | Behavior |
|---|---|
| `_self` | Opens in the **same tab/window** (this is the default, even if you don't add `target` at all) |
| `_blank` | Opens in a **new tab/window** |
| `_parent` | Opens in the **parent frame** (used when a page is inside an `<iframe>`) |
| `_top` | Opens in the **full body of the window**, breaking out of all frames |

### Examples

```html
<!-- Opens in same tab (default behavior) -->
<a href="page2.html" target="_self">Same Tab</a>

<!-- Opens in a new tab -->
<a href="https://google.com" target="_blank">New Tab</a>

<!-- Opens in the parent frame (rarely used today, mostly legacy/iframe layouts) -->
<a href="page2.html" target="_parent">Parent Frame</a>

<!-- Breaks out of all frames, opens in full window -->
<a href="page2.html" target="_top">Top Window</a>
```

### Common Usage
- `_blank` — most commonly used, for external links (so the user doesn't lose your page)
- `_self` — default, rarely written explicitly
- `_parent` / `_top` — used in older websites that use `<frameset>` or `<iframe>` heavily; rare in modern web design

**Security tip:** When using `target="_blank"`, it's good practice to also add `rel="noopener noreferrer"` to prevent the new tab from having access to the original page.

```html
<a href="https://example.com" target="_blank" rel="noopener noreferrer">Safe Link</a>
```