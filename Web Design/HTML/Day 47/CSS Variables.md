# CSS Variables

## Part B — Working with CSS Variables

**freeCodeCamp Responsive Web Design v9**

**Progress: 35 of 120 steps complete**

---

# 1. What Are CSS Custom Properties?

CSS Custom Properties are commonly called **CSS Variables**.

They allow us to store a value once and reuse it in multiple places in our CSS.

A custom property name must start with two hyphens:

```css
--variable-name
```

### Example

```css
:root {
  --primary-color: blue;
  --main-padding: 20px;
}
```

Here:

- `--primary-color` is a CSS custom property.
- `blue` is its value.
- `--main-padding` is another CSS custom property.
- `20px` is its value.

---

# 2. Why Do We Use CSS Variables?

CSS variables are useful when the same value is used multiple times.

For example, without variables:

```css
h1 {
  color: blue;
}

button {
  background-color: blue;
}

a {
  color: blue;
}
```

If we want to change `blue` to another color, we need to modify it in multiple places.

With CSS variables:

```css
:root {
  --primary-color: blue;
}

h1 {
  color: var(--primary-color);
}

button {
  background-color: var(--primary-color);
}

a {
  color: var(--primary-color);
}
```

Now we can change the color in one place:

```css
:root {
  --primary-color: green;
}
```

All elements using the variable will use the new value.

---

# 3. How Do We Create a CSS Variable?

CSS variables are created using two hyphens `--`.

### Syntax

```css
--variable-name: value;
```

### Example

```css
:root {
  --primary-color: #2563eb;
  --secondary-color: #16a34a;
  --spacing: 20px;
}
```

Here we created three variables:

```text
--primary-color
--secondary-color
--spacing
```

---

# 4. What Is `:root`?

`:root` represents the root element of the document.

For an HTML document, `:root` normally represents the `<html>` element.

CSS variables are commonly declared inside `:root` when we want them to be available throughout the page.

### Example

```css
:root {
  --primary-color: #2563eb;
  --text-color: #333;
  --card-padding: 20px;
}
```

These variables can then be used in different selectors.

---

# 5. How Do We Use a CSS Variable?

We use the `var()` function to access a CSS variable.

### Syntax

```css
var(--variable-name)
```

### Example

```css
:root {
  --primary-color: blue;
}

h1 {
  color: var(--primary-color);
}
```

The browser reads:

```css
color: var(--primary-color);
```

as the value stored in:

```css
--primary-color: blue;
```

So the result is effectively:

```css
color: blue;
```

---

# 6. CSS Variables Can Store Different Values

CSS variables can store many types of CSS values.

### Colors

```css
:root {
  --primary-color: #2563eb;
}
```

### Font Sizes

```css
:root {
  --heading-size: 2rem;
}
```

### Spacing

```css
:root {
  --main-padding: 20px;
}
```

### Border Radius

```css
:root {
  --border-radius: 10px;
}
```

### Width

```css
:root {
  --container-width: 1200px;
}
```

---

# 7. Example Using Multiple Variables

```css
:root {
  --primary-color: #2563eb;
  --secondary-color: #16a34a;
  --text-color: #333;
  --spacing: 20px;
  --radius: 10px;
}

.card {
  color: var(--text-color);
  padding: var(--spacing);
  border-radius: var(--radius);
}

.button {
  background-color: var(--primary-color);
}

.success {
  background-color: var(--secondary-color);
}
```

---

# 8. Global CSS Variables

A variable declared inside `:root` can generally be used throughout the document.

### Example

```css
:root {
  --primary-color: blue;
}

h1 {
  color: var(--primary-color);
}

p {
  color: var(--primary-color);
}

button {
  background-color: var(--primary-color);
}
```

The same variable is being reused in multiple selectors.

---

# 9. Local CSS Variables

CSS variables can also be declared inside a specific selector.

### Example

```css
.card {
  --card-color: purple;

  color: var(--card-color);
}
```

The variable is scoped to that element and its descendants according to normal CSS inheritance and cascading rules.

### Example

```css
.card {
  --card-color: purple;
}

.card h2 {
  color: var(--card-color);
}
```

The `h2` can use the variable because it is inside `.card`.

---

# 10. Global vs Local Variables

## Global Variable

```css
:root {
  --primary-color: blue;
}
```

Can generally be used throughout the document.

## Local Variable

```css
.card {
  --card-color: purple;
}
```

Primarily available within that element's scope and descendants.

### Simple Understanding

```text
:root
  |
  |-- Global Variables
  |
  |-- Header
  |-- Main
  |-- Card
  |-- Footer
```

A local variable is more limited:

```text
Card
 |
 |-- Card Heading
 |-- Card Paragraph
 |-- Card Button
```

---

# 11. Changing a CSS Variable

One major advantage of CSS variables is that we can change the value in one place.

### Before

```css
:root {
  --primary-color: blue;
}
```

### After

```css
:root {
  --primary-color: green;
}
```

Any element using:

```css
var(--primary-color)
```

will now use the new value.

---

# 12. CSS Variable Fallback Values

The `var()` function can have a fallback value.

### Syntax

```css
var(--variable, fallback-value)
```

If the custom property is unavailable or invalid in that context, the fallback can be used.

### Example

```css
h1 {
  color: var(--primary-color, blue);
}
```

This means:

> Use `--primary-color` if available. Otherwise, use `blue`.

---

# 13. Example of a Fallback

```css
.button {
  background-color: var(--button-color, blue);
}
```

If this variable exists:

```css
:root {
  --button-color: green;
}
```

The button uses:

```css
background-color: green;
```

If the variable is unavailable, the fallback is used:

```css
background-color: blue;
```

---

# 14. Multiple Fallback Values

Fallbacks can also be nested.

### Example

```css
color: var(--primary-color, var(--secondary-color, blue));
```

The browser checks:

1. `--primary-color`
2. If unavailable, `--secondary-color`
3. If that is also unavailable, `blue`

### Flow

```text
--primary-color
       ↓
   Available?
    /     \
  Yes      No
   ↓        ↓
  Use   --secondary-color
              ↓
          Available?
           /     \
         Yes      No
          ↓        ↓
         Use      blue
```

---

# 15. What Is the `@property` Rule?

The `@property` rule allows us to register a CSS custom property with additional information about how the property should behave.

It can define:

- The type of value allowed
- Whether the property inherits
- Its initial value

### Basic Syntax

```css
@property --variable-name {
  syntax: "<type>";
  inherits: true;
  initial-value: value;
}
```

---

# 16. The `syntax` Descriptor

The `syntax` descriptor defines what type of value the custom property accepts.

### Example

```css
@property --box-color {
  syntax: "<color>";
  inherits: false;
  initial-value: blue;
}
```

Here:

```css
syntax: "<color>";
```

means the property expects a color value.

### Other Common Syntax Types

```css
<color>
<length>
<number>
<percentage>
<angle>
<time>
```

---

# 17. The `inherits` Descriptor

The `inherits` descriptor controls whether the custom property inherits its value from its parent.

### Example

```css
@property --box-color {
  syntax: "<color>";
  inherits: false;
  initial-value: blue;
}
```

Here:

```css
inherits: false;
```

means the property does not inherit its value from its parent.

### With Inheritance

```css
@property --text-size {
  syntax: "<length>";
  inherits: true;
  initial-value: 16px;
}
```

The property can inherit from its parent.

---

# 18. The `initial-value` Descriptor

`initial-value` defines the initial value of a registered custom property.

### Example

```css
@property --box-color {
  syntax: "<color>";
  inherits: false;
  initial-value: blue;
}
```

If no valid value is provided, the property's initial value is:

```css
blue
```

### Important Difference

`initial-value` in `@property` is not the same thing as the fallback in `var()`.

### `var()` fallback

```css
color: var(--primary-color, blue);
```

The `blue` value is used if the variable cannot provide a usable value in that declaration.

### `@property` initial value

```css
@property --primary-color {
  syntax: "<color>";
  inherits: false;
  initial-value: blue;
}
```

The `initial-value` defines the registered property's initial value.

---

# 19. Complete `@property` Example

```css
@property --box-color {
  syntax: "<color>";
  inherits: false;
  initial-value: blue;
}

.box {
  --box-color: red;

  background-color: var(--box-color);
}
```

The `.box` uses:

```css
red
```

because the custom property has been assigned:

```css
--box-color: red;
```

---

# 20. Why Use `@property`?

`@property` provides more control over custom properties.

It allows the browser to know:

- What type of value the property should contain
- Whether the property should inherit
- What its initial value should be

This can also make certain custom properties more suitable for animations and transitions.

---

# 21. CSS Variables With Media Queries

CSS variables can be changed inside media queries.

This is useful for responsive designs.

### Example

```css
:root {
  --container-width: 90%;
  --font-size: 16px;
}

@media (min-width: 768px) {
  :root {
    --container-width: 80%;
    --font-size: 18px;
  }
}
```

On smaller screens:

```text
--container-width: 90%
--font-size: 16px
```

On screens 768px and wider:

```text
--container-width: 80%
--font-size: 18px
```

---

# 22. Responsive CSS Variables Example

```css
:root {
  --container-width: 95%;
  --heading-size: 1.8rem;
  --card-padding: 15px;
}

@media (min-width: 768px) {

  :root {
    --container-width: 90%;
    --heading-size: 2.2rem;
    --card-padding: 20px;
  }

}

@media (min-width: 1024px) {

  :root {
    --container-width: 80%;
    --heading-size: 2.5rem;
    --card-padding: 25px;
  }

}

.container {
  width: var(--container-width);
  margin: 0 auto;
}

h1 {
  font-size: var(--heading-size);
}

.card {
  padding: var(--card-padding);
}
```

This allows us to change several values for different screen sizes without rewriting the same CSS properties repeatedly.

---

# 23. Complete CSS Variables Example

## Project Structure

```text
css-variables/
│
├── index.html
│
└── styles.css
```

---

## index.html

```html
<!DOCTYPE html>
<html lang="en">

<head>

  <meta charset="UTF-8">

  <meta
    name="viewport"
    content="width=device-width, initial-scale=1.0"
  >

  <title>CSS Variables</title>

  <link rel="stylesheet" href="styles.css">

</head>

<body>

  <main class="container">

    <h1>CSS Variables</h1>

    <p class="description">
      CSS variables allow us to store and reuse values.
    </p>

    <section class="cards">

      <article class="card">

        <h2>HTML</h2>

        <p>
          HTML provides the structure of a webpage.
        </p>

        <button>Learn More</button>

      </article>


      <article class="card">

        <h2>CSS</h2>

        <p>
          CSS controls the appearance and layout.
        </p>

        <button>Learn More</button>

      </article>


      <article class="card">

        <h2>Responsive Design</h2>

        <p>
          Responsive design adapts websites to different screens.
        </p>

        <button>Learn More</button>

      </article>

    </section>

  </main>

</body>

</html>
```

---

## styles.css

```css
:root {
  --primary-color: #2563eb;
  --secondary-color: #16a34a;
  --text-color: #333;
  --background-color: #f5f5f5;

  --container-width: 90%;
  --card-padding: 20px;
  --border-radius: 10px;
  --card-gap: 20px;
}


/* ------------------------------
   Basic Reset
--------------------------------- */

* {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}


/* ------------------------------
   Body
--------------------------------- */

body {
  font-family: Arial, sans-serif;
  background-color: var(--background-color);
  color: var(--text-color);
}


/* ------------------------------
   Container
--------------------------------- */

.container {
  width: var(--container-width);
  max-width: 1200px;
  margin: 0 auto;
  padding: 30px 0;
}


/* ------------------------------
   Heading
--------------------------------- */

h1 {
  color: var(--primary-color);
  margin-bottom: 10px;
}


/* ------------------------------
   Description
--------------------------------- */

.description {
  margin-bottom: 30px;
}


/* ------------------------------
   Cards
--------------------------------- */

.cards {
  display: grid;
  grid-template-columns: 1fr;
  gap: var(--card-gap);
}


/* ------------------------------
   Card
--------------------------------- */

.card {
  background-color: white;
  padding: var(--card-padding);
  border-radius: var(--border-radius);
}


/* ------------------------------
   Button
--------------------------------- */

button {
  margin-top: 15px;
  padding: 10px 15px;
  background-color: var(--primary-color);
  color: white;
  border: none;
  border-radius: var(--border-radius);
}


/* ------------------------------
   Tablet
--------------------------------- */

@media (min-width: 768px) {

  :root {
    --container-width: 90%;
    --card-padding: 25px;
  }

  .cards {
    grid-template-columns: repeat(2, 1fr);
  }

}


/* ------------------------------
   Desktop
--------------------------------- */

@media (min-width: 1024px) {

  :root {
    --container-width: 80%;
    --card-padding: 30px;
  }

  .cards {
    grid-template-columns: repeat(3, 1fr);
  }

}
```

---

# 24. How the CSS Variables Work in This Example

We first create the variables:

```css
:root {
  --primary-color: #2563eb;
  --card-padding: 20px;
  --border-radius: 10px;
}
```

Then we use them:

```css
h1 {
  color: var(--primary-color);
}

.card {
  padding: var(--card-padding);
  border-radius: var(--border-radius);
}
```

Instead of writing the values repeatedly, we reuse the variables.

---

# 25. Changing the Theme Using CSS Variables

Suppose we want to change the primary color.

Instead of changing many selectors:

```css
h1 {
  color: blue;
}

button {
  background-color: blue;
}
```

We can change only the variable:

```css
:root {
  --primary-color: purple;
}
```

The elements using:

```css
var(--primary-color)
```

will automatically use the new color.

This makes theme changes easier.

---

# 26. CSS Variables and Responsive Design

CSS variables are especially useful with responsive design.

### Mobile

```css
:root {
  --card-gap: 15px;
  --card-padding: 15px;
}
```

### Tablet

```css
@media (min-width: 768px) {

  :root {
    --card-gap: 20px;
    --card-padding: 20px;
  }

}
```

### Desktop

```css
@media (min-width: 1024px) {

  :root {
    --card-gap: 30px;
    --card-padding: 30px;
  }

}
```

The same CSS properties can use the variables:

```css
.cards {
  gap: var(--card-gap);
}

.card {
  padding: var(--card-padding);
}
```

---

# 27. Simple CSS Variable Flow

```text
Create Variable
      ↓
--primary-color: blue;
      ↓
Use Variable
      ↓
var(--primary-color)
      ↓
CSS Property
      ↓
color: var(--primary-color);
```

---

# 28. Simple `@property` Flow

```text
@property
    ↓
Define Custom Property
    ↓
syntax
    ↓
inherits
    ↓
initial-value
    ↓
Use the Custom Property
```

Example:

```css
@property --box-color {
  syntax: "<color>";
  inherits: false;
  initial-value: blue;
}
```

---

# 29. CSS Variables vs Normal CSS Values

## Without CSS Variables

```css
.card {
  border-radius: 10px;
  padding: 20px;
}

.button {
  border-radius: 10px;
  padding: 20px;
}
```

If we want to change `10px` or `20px`, we need to update multiple places.

## With CSS Variables

```css
:root {
  --radius: 10px;
  --spacing: 20px;
}

.card {
  border-radius: var(--radius);
  padding: var(--spacing);
}

.button {
  border-radius: var(--radius);
  padding: var(--spacing);
}
```

Now we can change the values in one place:

```css
:root {
  --radius: 15px;
  --spacing: 25px;
}
```

---

# 30. Quick Revision

## CSS Custom Property

A reusable CSS value whose name starts with `--`.

```css
:root {
  --primary-color: blue;
}
```

## `var()`

Used to access a CSS custom property.

```css
color: var(--primary-color);
```

## `:root`

Commonly used to define global CSS variables.

```css
:root {
  --primary-color: blue;
}
```

## Fallback

Provides another value if the custom property cannot be used.

```css
color: var(--primary-color, blue);
```

## `@property`

Registers a custom property and allows us to define its type, inheritance behavior, and initial value.

```css
@property --box-color {
  syntax: "<color>";
  inherits: false;
  initial-value: blue;
}
```

## `syntax`

Defines the type of value accepted.

```css
syntax: "<color>";
```

## `inherits`

Controls whether the registered custom property inherits.

```css
inherits: false;
```

## `initial-value`

Defines the initial value of a registered custom property.

```css
initial-value: blue;
```

## CSS Variables + Media Queries

Variables can be changed at different breakpoints.

```css
:root {
  --padding: 15px;
}

@media (min-width: 768px) {
  :root {
    --padding: 25px;
  }
}
```

---

