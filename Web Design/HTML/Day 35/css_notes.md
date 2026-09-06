# Day 35: CSS Fundamentals

## 1. What is CSS?

CSS (Cascading Style Sheets) is used to style and visually control 
HTML elements — things like color, spacing, layout, fonts, and size. 
While HTML defines the **structure** of a page, CSS defines its 
**appearance**.

```html
<p>This is a paragraph.</p>
```
```css
p {
  color: blue;
}
```

---

## 2. Basic Anatomy of a CSS Rule

A CSS rule is made up of a **selector** and a **declaration block**.

```css
selector {
  property: value;
}
```

### Example Breakdown

```css
p {
  color: red;
  font-size: 16px;
}
```

| Part | Meaning |
|---|---|
| `p` | **Selector** — targets which HTML element(s) to style |
| `{ }` | **Declaration block** — holds all the styling rules |
| `color` | **Property** — the aspect being styled |
| `red` | **Value** — the setting applied to that property |
| `;` | Separates each declaration (required after every property-value pair) |

### Multiple Selectors
You can apply the **same styles to multiple elements** at once by 
separating selectors with a comma.

```css
h1, h2, p {
  color: navy;
  font-family: Arial;
}
```

**Without multiple selectors (repetitive):**
```css
h1 { color: navy; }
h2 { color: navy; }
p { color: navy; }
```

**With multiple selectors (cleaner):**
```css
h1, h2, p {
  color: navy;
}
```

### Multiple Declarations
A single selector can have **multiple property-value pairs** inside 
its declaration block.

```css
h1 {
  color: navy;
  font-size: 32px;
  text-align: center;
}
```

### Selecting by `id` and `class`

Besides selecting HTML elements directly (like `p`, `h1`), you can 
also target elements using their `id` or `class` attributes — this 
gives you more precise control.

#### `id` Selector — uses `#`
Targets a single, unique element (remember: `id` should only be 
used once per page).

```html
<h1 id="main-title">Welcome</h1>
```
```css
#main-title {
  color: darkred;
  font-size: 40px;
}
```

#### `class` Selector — uses `.`
Targets all elements sharing that class name (classes can repeat 
across multiple elements).

```html
<p class="highlight">Important note 1</p>
<p class="highlight">Important note 2</p>
```
```css
.highlight {
  background-color: yellow;
  font-weight: bold;
}
```

### Element vs Class vs ID Selector — Comparison

| Selector Type | Symbol | Targets | Example |
|---|---|---|---|
| Element | (none) | All elements of that tag | `p { }` |
| Class | `.` | All elements with that class | `.highlight { }` |
| ID | `#` | One unique element | `#main-title { }` |

### Combining Selector Types

```css
/* All paragraphs */
p {
  line-height: 1.5;
}

/* Only paragraphs with class "highlight" */
p.highlight {
  color: green;
}

/* The specific element with this id */
#main-title {
  text-decoration: underline;
}
```

### When to Use Which
- **Element selector** — for broad, general styling (e.g., all paragraphs)
- **Class selector** — for styling a reusable group of elements (most common in real projects)
- **ID selector** — for styling one specific, unique element (use sparingly)

---

## 3. The Meta Viewport Element

The viewport meta tag controls how a webpage is displayed on 
different devices, especially mobile phones. Without it, mobile 
browsers may render the page as a full desktop-width page and 
shrink it down, making text hard to read.

```html
<meta name="viewport" content="width=device-width, initial-scale=1.0">
```

### Breakdown

| Part | Meaning |
|---|---|
| `width=device-width` | Sets the page width to match the device's screen width |
| `initial-scale=1.0` | Sets the initial zoom level to 100% (no zoom in/out) |

This tag goes inside the `<head>` of your HTML document, and is 
essential for **responsive design**.

```html
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>My Page</title>
</head>
```

---

## 4. Three Ways to Add CSS

### A. Inline CSS
Applied directly on a single HTML element using the `style` attribute.

```html
<p style="color: green; font-size: 18px;">This is inline CSS.</p>
```

**When to use:** quick, one-off styling on a single element. 
**Downside:** hard to maintain, mixes content with styling, not reusable.

---

### B. Internal CSS
Written inside a `<style>` tag within the `<head>` of the HTML document. 
Applies to the whole page.

```html
<head>
  <style>
    p {
      color: purple;
      font-size: 18px;
    }
  </style>
</head>
<body>
  <p>This is internal CSS.</p>
</body>
```

**When to use:** styling for a single page. 
**Downside:** doesn't apply across multiple pages; can make HTML files large.

---

### C. External CSS
Written in a **separate `.css` file**, linked to the HTML document 
using the `<link>` tag.

**style.css**
```css
p {
  color: orange;
  font-size: 18px;
}
```

**index.html**
```html
<head>
  <link rel="stylesheet" href="style.css">
</head>
<body>
  <p>This is external CSS.</p>
</body>
```

**When to use:** best practice for real projects — keeps HTML and CSS 
separate, reusable across multiple pages, easier to maintain. 
**Downside:** requires an extra file and a working link path.

---

## 5. Comparison Table

| Method | Location | Scope | Best For |
|---|---|---|---|
| Inline | Inside the HTML tag (`style=""`) | Single element | Quick, one-time fixes |
| Internal | Inside `<style>` in `<head>` | Whole page | Single-page projects |
| External | Separate `.css` file, linked | Multiple pages | Real-world projects, best practice |

---

## Key Takeaways
- CSS = styling layer for HTML structure
- A CSS rule = selector + declaration block (property: value pairs)
- Selectors can target elements, classes (`.`), or IDs (`#`)
- Multiple selectors (comma-separated) apply the same styles to several elements at once
- The viewport meta tag makes a page responsive on mobile devices
- Three ways to add CSS: inline (element-level), internal (page-level), external (site-level, most scalable)
- External CSS is the industry-standard approach for real projects