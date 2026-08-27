# Day 25: HTML Fundamentals - Div Elements, Class & Id Attributes

## 1. What is a `div` Element?

The `div` element (short for "division") is a **generic container** 
in HTML. It has no special meaning by itself — it's used to group 
other HTML elements together.

```html
<div>
  <h2>Title</h2>
  <p>Some content here.</p>
</div>
```

### Why use `div`?
- **Grouping**: combine related elements (heading + paragraph + image) into one block
- **Structure**: organize a page into sections (header, content, footer)
- Note: `class`/`id` on a `div` become useful once you learn CSS — for now, just know it's a container.

---

## 2. What is the `class` Attribute?

The `class` attribute gives an HTML element a **name/label**. This 
name is what CSS (learned later) will use to style it. You can also 
give the same class name to multiple elements to group them.

```html
<div class="card">
  <p>This div has a class called "card"</p>
</div>
```

### Key Points
- An element can have **multiple classes**, separated by space:
```html
<div class="card featured">...</div>
```
- **Multiple elements** can share the same class name:
```html
<div class="card">Card 1</div>
<div class="card">Card 2</div>
```
- Right now, `class` doesn't visually change anything — it just labels the element. Styling comes later with CSS.

---

## 3. What is the `id` Attribute?

The `id` attribute gives a **single, unique name** to one specific 
element. Unlike `class`, an `id` should be used only **once per page**.

```html
<div id="header-section">
  <h1>My Website</h1>
</div>
```

### Key Points
- **Unique**: only one element on the page should use a given `id`
- Also used for **jumping to a section** on the same page (anchor links):
```html
<a href="#contact">Go to Contact</a>

<div id="contact">
  <p>Contact Us</p>
</div>
```
Clicking the link scrolls the page down to the `div` with `id="contact"`.

---

## 4. `class` vs `id` — Key Differences

| Feature | `class` | `id` |
|---|---|---|
| Uniqueness | Can repeat on multiple elements | Must be unique (one per page) |
| Purpose | Label a group of elements | Label one specific element |
| Multiple values allowed? | ✅ Yes (`class="card featured"`) | ❌ No (only one `id`) |
| Used for | Styling groups (CSS, later) | Targeting one element / page navigation |

---

## 5. Practice Example — `div`, `class`, and `id` Together

```html
<div id="main-container">
  <div class="product-card" id="biryani-card">
    <h3>Chicken Biryani</h3>
    <p>₹250</p>
    <button class="btn">Order Now</button>
  </div>

  <div class="product-card" id="pizza-card">
    <h3>Pizza</h3>
    <p>₹300</p>
    <button class="btn">Order Now</button>
  </div>
</div>
```

**Explanation:**
- `id="main-container"` — uniquely identifies the outer wrapper `div`
- `class="product-card"` — shared label on both cards (used later to style both the same way)
- `id="biryani-card"`, `id="pizza-card"` — unique labels for each individual card

---

## Key Takeaways
- `div` = generic container to group content
- `class` = reusable label, can be shared across multiple elements
- `id` = unique label, used once per page
- These attributes don't change how the page *looks* yet — that comes when you learn **CSS**