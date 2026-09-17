# Day 46 — CSS Attribute Selectors Notes (Part 2)



---

# What are Attribute Selectors?

Attribute selectors allow CSS to style HTML elements **based on their attributes** instead of only using tag names, classes, or IDs.

## Basic Syntax

```css
element[attribute] {
  /* CSS styles */
}
```

Example:

```css
a[href] {
  color: blue;
}
```

This selects every `<a>` element that has an `href` attribute.

---

# 1. Target Elements with `href`

The `href` attribute makes a link clickable.

## index.html

```html
<a href="https://google.com">Google</a>

<a href="https://youtube.com">YouTube</a>

<a>Normal Text</a>
```

## styles.css

```css
a[href] {
  color: blue;
  text-decoration: underline;
}
```

## Output

```text
Google      → Blue & Underlined

YouTube     → Blue & Underlined

Normal Text → Default
```

### Explanation

Only links that contain `href` are selected.

---

# 2. Target Elements with `title`

The `title` attribute provides additional information.

## index.html

```html
<a href="https://google.com" title="Search Engine">
  Google
</a>

<a href="https://youtube.com">
  YouTube
</a>
```

## styles.css

```css
a[title] {
  font-weight: bold;
  color: purple;
}
```

## Output

```text
Google  → Bold Purple

YouTube → Normal
```

### Explanation

Only elements with a `title` attribute are styled.

---

# 3. Multiple Attributes

You can combine attribute selectors.

## index.html

```html
<a href="https://google.com" title="Google">
  Google
</a>

<a href="https://youtube.com">
  YouTube
</a>

<a title="Example">
  Example
</a>
```

## styles.css

```css
a[href][title] {
  color: green;
}
```

## Output

```text
Google  → Green

YouTube → Default

Example → Default
```

### Explanation

The element must contain **both** attributes.

---

# 4. Exact Attribute Value

Target a specific value.

## index.html

```html
<a href="https://google.com">Google</a>

<a href="https://youtube.com">YouTube</a>
```

## styles.css

```css
a[href="https://google.com"] {
  color: red;
}
```

## Output

```text
Google  → Red

YouTube → Default
```

### Explanation

The value must match exactly.

---

# 5. `[attr~=value]`

`~=` matches a word inside a space-separated list.

## index.html

```html
<a class="btn primary large">
  Visit Site
</a>

<a class="btn large">
  Read More
</a>
```

## styles.css

```css
a[class~="primary"] {
  background: green;
  color: white;
}
```

## Output

```text
Visit Site → Green Button

Read More → Default
```

### Explanation

The word `primary` must exist in the class list.

---

# 6. `[attr^=value]` (Starts With)

`^=` checks whether the value **starts with** something.

## index.html

```html
<a href="https://google.com">Google</a>

<a href="http://example.com">Example</a>
```

## styles.css

```css
a[href^="https://"] {
  color: green;
}
```

## Output

```text
Google  → Green

Example → Default
```

### Explanation

Only values beginning with `https://` are selected.

---

# 7. `[attr$=value]` (Ends With)

`$=` checks whether the value **ends with** something.

## index.html

```html
<a href="resume.pdf">Resume</a>

<a href="photo.jpg">Photo</a>
```

## styles.css

```css
a[href$=".pdf"] {
  color: red;
  font-weight: bold;
}
```

## Output

```text
Resume → Red Bold

Photo  → Default
```

### Explanation

Useful for styling downloadable PDF links.

---

# 8. `lang` Attribute

The `lang` attribute specifies the language of content.

## index.html

```html
<p lang="en">Hello World</p>

<p lang="kn">ನಮಸ್ಕಾರ</p>

<p lang="fr">Bonjour</p>
```

## styles.css

```css
p[lang="en"] {
  font-style: italic;
  color: blue;
}
```

## Output

```text
Hello World → Blue Italic

ನಮಸ್ಕಾರ    → Default

Bonjour     → Default
```

### Explanation

Only English paragraphs are selected.

---

# 9. `data-lang` Attribute

`data-lang` stores custom information.

## index.html

```html
<p data-lang="en">Hello</p>

<p data-lang="fr">Bonjour</p>
```

## styles.css

```css
p[data-lang="fr"] {
  color: blue;
  font-weight: bold;
}
```

## Output

```text
Hello    → Default

Bonjour  → Blue Bold
```

### Explanation

Useful for multilingual websites.

---

# 10. Ordered List `type` Attribute

The `type` attribute changes numbering style.

## Numerical List

### index.html

```html
<ol type="1">
  <li>HTML</li>
  <li>CSS</li>
</ol>
```

Output

```text
1. HTML
2. CSS
```

---

## Alphabet List

### index.html

```html
<ol type="A">
  <li>HTML</li>
  <li>CSS</li>
</ol>
```

Output

```text
A. HTML
B. CSS
```

---

## Roman Numerals

### index.html

```html
<ol type="I">
  <li>HTML</li>
  <li>CSS</li>
</ol>
```

Output

```text
I. HTML
II. CSS
```

---

# 11. Style Ordered Lists by `type`

## index.html

```html
<ol type="A">
  <li>Apple</li>
  <li>Banana</li>
</ol>

<ol type="i">
  <li>HTML</li>
  <li>CSS</li>
</ol>
```

## styles.css

```css
ol[type="A"] {
  color: purple;
  font-weight: bold;
}

ol[type="i"] {
  color: green;
}
```

## Output

```text
A. Apple
B. Banana

i. HTML
ii. CSS
```

---

# Attribute Selector Cheat Sheet

| Selector | Meaning |
|----------|---------|
| `[attr]` | Attribute exists |
| `[attr="value"]` | Exact value |
| `[attr~="word"]` | Contains word |
| `[attr^="text"]` | Starts with |
| `[attr$="text"]` | Ends with |

---

# Complete Example

## index.html

```html
<h2>Attribute Selector Demo</h2>

<a href="https://google.com" title="Google">
  Google
</a>

<p lang="en">Welcome</p>

<p data-lang="fr">Bonjour</p>

<ol type="A">
  <li>HTML</li>
  <li>CSS</li>
</ol>
```

## styles.css

```css
a[href] {
  color: blue;
}

a[title] {
  font-weight: bold;
}

p[lang="en"] {
  color: green;
}

p[data-lang="fr"] {
  color: purple;
}

ol[type="A"] {
  color: orange;
}
```

---

# Summary

| Attribute | Purpose |
|-----------|---------|
| `href` | Target clickable links |
| `title` | Target elements with extra information |
| `lang` | Style content by language |
| `data-lang` | Style using custom language data |
| `type` | Style ordered lists by numbering type |

---

# Easy Memory Trick

```text
[attr]
↓
Attribute exists

[attr="value"]
↓
Exact value

~=  Contains word

^=  Starts with

$=  Ends with
```