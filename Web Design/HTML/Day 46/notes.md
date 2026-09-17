# Day 46 — CSS Positioning Notes (Part 1)

---

# What is CSS Positioning?

CSS positioning controls **where an HTML element appears** on a webpage.

There are five main position values:

| Position | Purpose |
|----------|---------|
| `static` | Default position |
| `relative` | Move from original position |
| `absolute` | Position inside parent |
| `fixed` | Stick to browser screen |
| `sticky` | Becomes fixed while scrolling |

---

# 1. Static Position

Static is the **default position** of every HTML element.

## index.html

```html
<div class="container">
  <h2>My Website</h2>

  <p>This is the first paragraph.</p>

  <button>Read More</button>
</div>
```

## styles.css

```css
.container {
  border: 2px solid gray;
  padding: 20px;
}
```

## Output

```text
My Website

This is the first paragraph.

[ Read More ]
```

### Explanation

- No `position` property is used.
- Elements appear from top to bottom.
- This is called **Normal Document Flow**.

---

# 2. Relative Position

Relative moves an element **without removing its original space**.

## index.html

```html
<div class="box">Relative Box</div>
```

## styles.css

```css
.box {
  position: relative;
  top: 20px;
  left: 30px;

  width: 180px;
  padding: 20px;
  background: skyblue;
}
```

## Before

```text
[ Relative Box ]
```

## After

```text
      [ Relative Box ]
```

### Explanation

- `top:20px` → moves down
- `left:30px` → moves right
- Original space remains empty.

---

# 3. Absolute Position

Absolute removes the element from the normal flow.

Always give the parent `position: relative`.

## index.html

```html
<div class="parent">
  <div class="child">SALE</div>
</div>
```

## styles.css

```css
.parent {
  position: relative;

  width: 250px;
  height: 150px;

  background: #eee;
}

.child {
  position: absolute;

  top: 10px;
  right: 10px;

  background: crimson;
  color: white;
  padding: 8px;
}
```

## Output

```text
+----------------------+
|                SALE  |
|                      |
|                      |
+----------------------+
```

### Explanation

- Parent becomes reference.
- Child stays inside parent.
- Original space is not reserved.

---

# 4. Fixed Position

Fixed elements stay attached to the browser screen.

## index.html

```html
<header>My Navbar</header>

<main>
  <p>Lots of content...</p>
</main>
```

## styles.css

```css
header {
  position: fixed;

  top: 0;
  left: 0;

  width: 100%;

  background: navy;
  color: white;
  padding: 15px;
}

main {
  margin-top: 70px;
}
```

## Output

```text
+----------------------+
| My Navbar            |
+----------------------+

Content...

Content...
```

### Explanation

- Navbar always stays visible.
- Scroll does not move it.
- Relative to viewport.

---

# 5. Sticky Position

Sticky behaves like Relative first, then Fixed.

## index.html

```html
<h1>My Blog</h1>

<nav>Categories</nav>

<section>
  <p>Long content...</p>
</section>
```

## styles.css

```css
nav {
  position: sticky;
  top: 0;

  background: orange;
  padding: 12px;
}
```

## Before Scroll

```text
My Blog

Categories

Content...
```

## After Scroll

```text
Categories

Content...
Content...
```

### Explanation

- Initially normal.
- After reaching top, it sticks.
- `top` is required.

---

# 6. Floats

Floats make text wrap around images.

## index.html

```html
<div class="article">
  <img src="image.jpg" alt="Nature">

  <p>
    This paragraph wraps around the image because
    the image is floated to the left.
  </p>
</div>
```

## styles.css

```css
img {
  float: left;

  width: 120px;

  margin-right: 15px;
}

.article {
  border: 1px solid gray;
  padding: 15px;
}
```

## Output

```text
[IMAGE]  This text wraps around
         the image nicely...
```

### Explanation

- Image moves left.
- Text fills remaining space.
- Used in blogs and magazines.

---

# 7. Clearfix

Floated children can collapse the parent.

## Without Clearfix

```html
<div class="container">
  <img src="image.jpg">

  <p>Paragraph</p>
</div>
```

```css
img {
  float: left;
}
```

Parent border may collapse.

---

## With Clearfix

## styles.css

```css
.container::after {
  content: "";
  display: block;
  clear: both;
}
```

### Explanation

- `::after` creates invisible element.
- `clear: both` clears left & right floats.
- Parent expands correctly.

---

# 8. Z-Index

Z-index controls overlapping layers.

## index.html

```html
<div class="box1">1</div>

<div class="box2">2</div>

<div class="box3">3</div>
```

## styles.css

```css
.box1,
.box2,
.box3 {
  position: absolute;

  width: 120px;
  height: 120px;
}

.box1 {
  background: red;
  left: 30px;
  top: 30px;
  z-index: 1;
}

.box2 {
  background: green;
  left: 70px;
  top: 70px;
  z-index: 5;
}

.box3 {
  background: blue;
  left: 110px;
  top: 110px;
  z-index: 10;
}
```

## Output

```text
Blue (10)
Green (5)
Red (1)
```

### Explanation

- Higher value appears on top.
- Works only on positioned elements.
- Commonly used for modals and tooltips.

---

# Position Summary

| Position | Removed From Flow | Reference |
|----------|-------------------|-----------|
| Static | No | Normal flow |
| Relative | No | Original position |
| Absolute | Yes | Parent |
| Fixed | Yes | Viewport |
| Sticky | Initially No | Viewport after scroll |

---

# Key Notes

- `static` → Default layout
- `relative` → Move but keep space
- `absolute` → Float inside parent
- `fixed` → Always visible
- `sticky` → Stick while scrolling
- `float` → Wrap text around image
- `clearfix` → Fix collapsed parent
- `z-index` → Controls overlapping order