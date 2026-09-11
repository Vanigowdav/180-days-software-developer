# Day 40 – CSS Units, Pseudo-classes & Pseudo-elements

## 📅 Day 40 Progress

Today I learned about:

* Absolute Units in CSS
* Relative Units in CSS
* Pseudo-classes
* Common Pseudo-classes
* Pseudo-elements
* Common Pseudo-elements
* Difference between Pseudo-classes and Pseudo-elements

---

# 1. CSS Units

CSS units are used to define the size of elements such as:

* Width
* Height
* Padding
* Margin
* Font size
* Border width
* Positioning

Example:

```css
.box {
  width: 200px;
  height: 100px;
  font-size: 20px;
}
```

Here:

* `200px` → width
* `100px` → height
* `20px` → font size

CSS units are mainly divided into:

1. Absolute units
2. Relative units

---

# 2. Absolute Units

Absolute units represent fixed sizes.

The most commonly used absolute unit is:

```text
px
```

### Common Absolute Units

| Unit | Meaning     |
| ---- | ----------- |
| `px` | Pixels      |
| `cm` | Centimeters |
| `mm` | Millimeters |
| `in` | Inches      |
| `pt` | Points      |
| `pc` | Picas       |

In web development, `px` is the most commonly used absolute unit.

---

## 2.1 Pixels – `px`

A pixel is a fixed unit commonly used for screen-based designs.

### Example

```html
<!DOCTYPE html>
<html>
<head>
  <style>
    .box {
      width: 200px;
      height: 100px;
      background-color: lightblue;
    }
  </style>
</head>

<body>

  <div class="box">
    Fixed Size Box
  </div>

</body>
</html>
```

The box will have:

```text
Width  = 200px
Height = 100px
```

### Important Point

`px` does not change based directly on the size of the parent element.

---

# 3. Relative Units

Relative units are calculated relative to something else.

They are useful for responsive web design.

Common relative units include:

```text
%
em
rem
vw
vh
vmin
vmax
```

---

# 4. Percentage – `%`

The `%` unit is usually relative to the size of the parent element.

### Example

```html
<!DOCTYPE html>
<html>
<head>
  <style>
    .parent {
      width: 500px;
      height: 200px;
      background-color: lightgray;
    }

    .child {
      width: 50%;
      height: 50%;
      background-color: lightblue;
    }
  </style>
</head>

<body>

  <div class="parent">
    <div class="child"></div>
  </div>

</body>
</html>
```

The child will be approximately:

```text
Width  = 50% of parent width
Height = 50% of parent height
```

---

# 5. `em` Unit

`em` is relative to the font size of the element or its inherited context.

Example:

```css
.parent {
  font-size: 20px;
}

.child {
  font-size: 2em;
}
```

Here:

```text
2em = 2 × 20px
    = 40px
```

### Example

```html
<!DOCTYPE html>
<html>
<head>
  <style>
    .parent {
      font-size: 20px;
    }

    .child {
      font-size: 2em;
    }
  </style>
</head>

<body>

  <div class="parent">
    Parent Text

    <div class="child">
      Child Text
    </div>
  </div>

</body>
</html>
```

### Important

`em` can become complicated when elements are nested because the size can depend on inherited font sizes.

---

# 6. `rem` Unit

`rem` means:

```text
Root em
```

It is relative to the font size of the root element, usually the `<html>` element.

Example:

```css
html {
  font-size: 16px;
}

h1 {
  font-size: 2rem;
}
```

Calculation:

```text
2rem = 2 × 16px
     = 32px
```

### Example

```html
<!DOCTYPE html>
<html>
<head>
  <style>
    html {
      font-size: 16px;
    }

    h1 {
      font-size: 2rem;
    }

    p {
      font-size: 1rem;
    }
  </style>
</head>

<body>

  <h1>Hello CSS</h1>
  <p>This is a paragraph.</p>

</body>
</html>
```

### Why `rem` is useful

`rem` makes it easier to maintain consistent font sizes throughout a website.

---

# 7. `vw` – Viewport Width

`vw` stands for:

```text
Viewport Width
```

`1vw` represents approximately 1% of the viewport width.

Example:

```css
.box {
  width: 50vw;
}
```

This means the element's width is approximately 50% of the viewport width.

### Example

```html
<!DOCTYPE html>
<html>
<head>
  <style>
    .box {
      width: 50vw;
      height: 100px;
      background-color: lightgreen;
    }
  </style>
</head>

<body>

  <div class="box"></div>

</body>
</html>
```

---

# 8. `vh` – Viewport Height

`vh` stands for:

```text
Viewport Height
```

`1vh` represents approximately 1% of the viewport height.

Example:

```css
.hero {
  height: 100vh;
}
```

This makes the element approximately as tall as the entire viewport.

### Example

```html
<!DOCTYPE html>
<html>
<head>
  <style>
    .hero {
      height: 100vh;
      background-color: lightblue;
    }
  </style>
</head>

<body>

  <section class="hero">
    Full Screen Section
  </section>

</body>
</html>
```

---

# 9. `vmin`

`vmin` represents the smaller value between:

```text
viewport width
viewport height
```

Example:

```css
.box {
  width: 50vmin;
}
```

The browser uses the smaller viewport dimension to calculate the size.

---

# 10. `vmax`

`vmax` represents the larger value between:

```text
viewport width
viewport height
```

Example:

```css
.box {
  width: 50vmax;
}
```

The browser uses the larger viewport dimension.

---

# 11. Absolute vs Relative Units

| Absolute Units | Relative Units |
| -------------- | -------------- |
| `px`           | `%`            |
| `cm`           | `em`           |
| `mm`           | `rem`          |
| `in`           | `vw`           |
| `pt`           | `vh`           |
| `pc`           | `vmin`         |
|                | `vmax`         |

### General Rule

Use absolute units when you need a more fixed size.

Use relative units when you want designs to adapt to different screen sizes or contexts.

---

# 12. Pseudo-classes

A pseudo-class is a CSS keyword used to select an element based on a particular state or condition.

Pseudo-classes start with:

```text
:
```

Example:

```css
button:hover {
  background-color: blue;
}
```

Here:

```text
:hover
```

is a pseudo-class.

It applies the style when the user moves the mouse over the button.

---

# 13. `:hover`

The `:hover` pseudo-class applies styles when the pointer is over an element.

### Example

```html
<!DOCTYPE html>
<html>
<head>
  <style>
    button {
      background-color: lightblue;
      padding: 10px 20px;
      border: none;
    }

    button:hover {
      background-color: blue;
      color: white;
    }
  </style>
</head>

<body>

  <button>Hover Me</button>

</body>
</html>
```

When the mouse moves over the button, the style changes.

---

# 14. `:active`

The `:active` pseudo-class applies while an element is being activated.

For example, while a button is being clicked.

### Example

```css
button:active {
  background-color: red;
}
```

Complete example:

```html
<!DOCTYPE html>
<html>
<head>
  <style>
    button {
      padding: 10px 20px;
    }

    button:active {
      background-color: red;
      color: white;
    }
  </style>
</head>

<body>

  <button>Click Me</button>

</body>
</html>
```

---

# 15. `:focus`

The `:focus` pseudo-class applies when an element receives focus.

It is commonly used with:

* Input fields
* Buttons
* Links
* Textareas

### Example

```html
<!DOCTYPE html>
<html>
<head>
  <style>
    input:focus {
      border: 2px solid blue;
      outline: none;
    }
  </style>
</head>

<body>

  <input type="text" placeholder="Enter your name">

</body>
</html>
```

When the input is selected, the border changes.

---

# 16. `:visited`

The `:visited` pseudo-class styles links that the user has already visited.

### Example

```html
<!DOCTYPE html>
<html>
<head>
  <style>
    a:visited {
      color: purple;
    }
  </style>
</head>

<body>

  <a href="https://example.com">
    Visit Example
  </a>

</body>
</html>
```

---

# 17. `:link`

The `:link` pseudo-class targets links that have not yet been visited.

### Example

```css
a:link {
  color: blue;
}
```

---

# 18. `:first-child`

The `:first-child` pseudo-class selects an element if it is the first child of its parent.

### Example

```html
<!DOCTYPE html>
<html>
<head>
  <style>
    li:first-child {
      color: red;
    }
  </style>
</head>

<body>

  <ul>
    <li>Apple</li>
    <li>Banana</li>
    <li>Mango</li>
  </ul>

</body>
</html>
```

Only `Apple` will become red.

---

# 19. `:last-child`

The `:last-child` pseudo-class selects the last child.

### Example

```css
li:last-child {
  color: green;
}
```

```html
<ul>
  <li>Apple</li>
  <li>Banana</li>
  <li>Mango</li>
</ul>
```

Only `Mango` will become green.

---

# 20. `:nth-child()`

The `:nth-child()` pseudo-class allows you to select a specific child based on its position.

### Example

```css
li:nth-child(2) {
  color: blue;
}
```

HTML:

```html
<ul>
  <li>Apple</li>
  <li>Banana</li>
  <li>Mango</li>
</ul>
```

The second item, `Banana`, becomes blue.

---

# 21. `:not()`

The `:not()` pseudo-class selects elements that do not match a specific selector.

### Example

```css
p:not(.special) {
  color: gray;
}
```

HTML:

```html
<p>Normal paragraph</p>

<p class="special">
  Special paragraph
</p>
```

The first paragraph will be gray, while the `.special` paragraph will not receive the style.

---

# 22. `:checked`

The `:checked` pseudo-class selects checked checkboxes or radio buttons.

### Example

```html
<!DOCTYPE html>
<html>
<head>
  <style>
    input:checked {
      accent-color: green;
    }
  </style>
</head>

<body>

  <label>
    <input type="checkbox">
    I agree
  </label>

</body>
</html>
```

---

# 23. `:disabled`

The `:disabled` pseudo-class selects disabled form controls.

### Example

```html
<!DOCTYPE html>
<html>
<head>
  <style>
    button:disabled {
      background-color: gray;
      color: white;
    }
  </style>
</head>

<body>

  <button disabled>
    Disabled Button
  </button>

</body>
</html>
```

---

# 24. Pseudo-elements

Pseudo-elements allow us to style a specific part of an element.

Pseudo-elements use:

```text
::
```

Example:

```css
p::first-letter {
  color: red;
}
```

Here:

```text
::first-letter
```

is a pseudo-element.

---

# 25. `::before`

`::before` inserts generated content before the content of an element.

### Example

```html
<!DOCTYPE html>
<html>
<head>
  <style>
    h2::before {
      content: "⭐ ";
    }
  </style>
</head>

<body>

  <h2>CSS Notes</h2>

</body>
</html>
```

Output:

```text
⭐ CSS Notes
```

---

# 26. `::after`

`::after` inserts generated content after the content of an element.

### Example

```html
<!DOCTYPE html>
<html>
<head>
  <style>
    h2::after {
      content: " ✔";
      color: green;
    }
  </style>
</head>

<body>

  <h2>Completed</h2>

</body>
</html>
```

---

# 27. `::first-letter`

`::first-letter` styles the first letter of text.

### Example

```html
<!DOCTYPE html>
<html>
<head>
  <style>
    p::first-letter {
      font-size: 40px;
      font-weight: bold;
      color: red;
    }
  </style>
</head>

<body>

  <p>
    CSS is used to style web pages.
  </p>

</body>
</html>
```

---

# 28. `::first-line`

`::first-line` styles the first line of text.

### Example

```css
p::first-line {
  font-weight: bold;
  color: blue;
}
```

The exact amount of text considered the first line depends on the available width of the element.

---

# 29. `::selection`

`::selection` styles the portion of text selected by the user.

### Example

```html
<!DOCTYPE html>
<html>
<head>
  <style>
    p::selection {
      background-color: yellow;
      color: black;
    }
  </style>
</head>

<body>

  <p>
    Select this text with your mouse.
  </p>

</body>
</html>
```

---

# 30. `::marker`

`::marker` styles the marker of list items.

### Example

```html
<!DOCTYPE html>
<html>
<head>
  <style>
    li::marker {
      color: red;
    }
  </style>
</head>

<body>

  <ul>
    <li>HTML</li>
    <li>CSS</li>
    <li>JavaScript</li>
  </ul>

</body>
</html>
```

---

# 31. Pseudo-class vs Pseudo-element

## Pseudo-class

Pseudo-classes select an element based on its state or condition.

Syntax:

```css
selector:pseudo-class
```

Examples:

```css
button:hover
input:focus
a:visited
li:first-child
```

---

## Pseudo-element

Pseudo-elements style a specific part of an element or create generated content.

Syntax:

```css
selector::pseudo-element
```

Examples:

```css
p::first-letter
p::first-line
h2::before
h2::after
```

---

# 32. Easy Way to Remember

## Pseudo-class

Think:

> "What state is the element in?"

Examples:

```text
:hover
:focus
:active
:checked
:disabled
```

## Pseudo-element

Think:

> "Which part of the element do I want to style?"

Examples:

```text
::first-letter
::first-line
::before
::after
::selection
```

---

# 33. Combined Example

This example combines:

* Relative units
* `:hover`
* `:focus`
* `:first-child`
* `::before`
* `::after`
* `::marker`

```html
<!DOCTYPE html>
<html>
<head>
  <title>Day 40 CSS Practice</title>

  <style>

    body {
      font-family: Arial, sans-serif;
      margin: 0;
      padding: 20px;
    }

    .container {
      width: 80%;
      max-width: 600px;
      margin: auto;
      padding: 2rem;
      background-color: lightgray;
    }

    h1::before {
      content: "📘 ";
    }

    h1::after {
      content: " ✓";
      color: green;
    }

    p:first-child {
      font-weight: bold;
    }

    button {
      padding: 1em 2em;
      border: none;
      cursor: pointer;
    }

    button:hover {
      background-color: blue;
      color: white;
    }

    button:active {
      background-color: red;
    }

    input {
      padding: 10px;
      width: 80%;
    }

    input:focus {
      border: 2px solid blue;
      outline: none;
    }

    li::marker {
      color: green;
    }

  </style>
</head>

<body>

  <div class="container">

    <h1>CSS Day 40</h1>

    <p>Today I learned CSS units and pseudo-classes.</p>

    <input
      type="text"
      placeholder="Enter your name"
    >

    <br><br>

    <button>
      Hover Me
    </button>

    <h2>Topics Learned</h2>

    <ul>
      <li>Absolute Units</li>
      <li>Relative Units</li>
      <li>Pseudo-classes</li>
      <li>Pseudo-elements</li>
    </ul>

  </div>

</body>
</html>
```

---

# 34. Important Syntax to Remember

## Absolute Unit

```css
.box {
  width: 200px;
}
```

## Percentage

```css
.box {
  width: 50%;
}
```

## em

```css
.text {
  font-size: 2em;
}
```

## rem

```css
.text {
  font-size: 2rem;
}
```

## Viewport Units

```css
.box {
  width: 50vw;
  height: 50vh;
}
```

## Pseudo-class

```css
button:hover {
  background-color: blue;
}
```

## Pseudo-element

```css
p::first-letter {
  color: red;
}
```

---

# 35. Key Takeaways

## CSS Units

* `px` → fixed/absolute unit
* `%` → relative to a containing context
* `em` → relative to font size/context
* `rem` → relative to root font size
* `vw` → viewport width
* `vh` → viewport height
* `vmin` → smaller viewport dimension
* `vmax` → larger viewport dimension

## Pseudo-classes

Used to style elements based on their state or condition.

Examples:

```text
:hover
:active
:focus
:visited
:link
:first-child
:last-child
:nth-child()
:not()
:checked
:disabled
```

## Pseudo-elements

Used to style a specific part of an element or generate content.

Examples:

```text
::before
::after
::first-letter
::first-line
::selection
::marker
```

---

# 📝 Day 40 Summary

Today I learned how CSS units control the size of elements and how relative units help create responsive designs.

I also learned about pseudo-classes, which allow me to style elements based on their state, such as hover, focus, active, checked, or disabled.

Finally, I learned about pseudo-elements, which allow me to style specific parts of elements or insert generated content using `::before` and `::after`.

