## 1. Importance of Semantic HTML

Semantic HTML means using HTML elements that clearly describe their 
**meaning and purpose**, not just how they look. Instead of using 
generic `<div>` for everything, semantic tags tell the browser (and 
developers) exactly what kind of content is inside.

### Non-Semantic Example
```html
<div class="header">My Website</div>
<div class="nav">...</div>
<div class="main-content">...</div>
<div class="footer">...</div>
```
A `<div>` doesn't tell anyone what it actually contains — you only 
know because of the class name.

### Semantic Example
```html
<header>My Website</header>
<nav>...</nav>
<main>...</main>
<footer>...</footer>
```
Here, the tag name itself explains its purpose.

### Why Semantic HTML Matters
- **Accessibility**: screen readers use semantic tags to help visually 
  impaired users navigate a page (e.g., jump directly to `<nav>` or `<main>`)
- **SEO**: search engines better understand page structure and content importance
- **Readability**: developers can understand the code faster without 
  relying on class names
- **Maintainability**: cleaner, more organized code that's easier to update

---