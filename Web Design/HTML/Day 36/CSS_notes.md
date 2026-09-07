# Day 35 – CSS Notes

## 1. Types of CSS

### Inline CSS
- Written inside the HTML element.
- Affects only one element.

```html
<p style="color:red;">Hello</p>
```

### Internal CSS
- Written inside the `<style>` tag.
- Used for a single webpage.

```html
<style>
  p {
    color: blue;
  }
</style>
```

### External CSS (Best Practice)
- Written in a separate `.css` file.
- Reusable across multiple pages.

```html
<link rel="stylesheet" href="style.css">
```

---

## 2. Width & Height

- `width` → controls horizontal size.
- `height` → controls vertical size.

```css
div {
  width: 300px;
  height: 150px;
}
```

Units: `px`, `%`, `vw`, `vh`

---

## 3. CSS Combinators

| Combinator | Meaning |
|------------|---------|
| `A B` | Descendant |
| `A > B` | Direct child |
| `A + B` | Adjacent sibling |
| `A ~ B` | General sibling |

```css
div p { color: blue; }
div > p { color: red; }
h1 + p { color: green; }
h1 ~ p { color: orange; }
```

---

## 4. Inline vs Block Elements

### Block
- Takes full width.
- Starts on a new line.

Examples:
- `div`
- `p`
- `h1`

### Inline
- Takes only required width.
- Stays in the same line.

Examples:
- `span`
- `a`
- `strong`

---

## 5. Inline-Block

- Stays inline.
- Can set width & height.

```css
button {
  display: inline-block;
  width: 120px;
}
```

---

## 6. Margin vs Padding

**Margin** = Outside space

**Padding** = Inside space

```css
.box {
  margin: 20px;
  padding: 15px;
}
```

Summary

Margin → Border → Padding → Content