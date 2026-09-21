# 📅 Day 50 — Introduction to JavaScript

## 1. What Is JavaScript?

JavaScript is a **programming language** that adds interactivity and dynamic behavior to websites.

| Language | Role |
|----------|------|
| HTML | Structure (content, elements) |
| CSS | Styling (colors, layout, fonts) |
| JavaScript | Behavior (interactivity, logic, dynamic updates) |

- HTML = markup language
- CSS = stylesheet language
- JavaScript = programming language

**Example — how they work together:**

```html
<!-- index.html -->
<!DOCTYPE html>
<html>
<head>
  <link rel="stylesheet" href="style.css">
</head>
<body>
  <h1 id="title">Hello World</h1>
  <button id="myBtn">Click Me</button>

  <script src="script.js"></script>
</body>
</html>
```

```css
/* style.css */
#title {
  color: green;
}
```

```js
// script.js
document.getElementById("myBtn").addEventListener("click", function () {
  alert("Button was clicked!");
});
```

- HTML → structure (heading + button)
- CSS → style (green heading)
- JS → behavior (alert on click)

---

## 2. Data Types in JavaScript

A **data type** = the kind of value stored (number, text, etc.)
A **variable** = a named container that holds a value of a specific data type.

### Primitive Data Types

```js
// Number (integers & floats)
let age = 25;
let price = 3.14;

// String (text)
let name1 = "Alice";   // double quotes
let name2 = 'Bob';     // single quotes

// Boolean (true / false)
let isLoggedIn = true;

// Undefined - declared but no value assigned
let score;
console.log(score); // undefined

// Null - intentionally empty value
let user = null;
```

### Complex / Reference Data Types

```js
// Object - collection of key-value pairs
const person = {
  name: "Alice",
  age: 30
};

// Symbol - unique, immutable identifier
const mySymbol = Symbol("mySymbol");

// BigInt - for numbers larger than Number can hold
const bigNumber = 1234567890123456789012345678901234567890n;
```

> 📝 `console.log()` prints output to the browser console (used for debugging).
> `//` starts a single-line comment — ignored when the code runs.

---

## 3. Variables

Variables are containers that store data you can access/modify later in your program.

### Declaring with `let`

```js
let age;          // declared, no value → undefined
age = 25;          // assignment
console.log(age);  // 25
```

### Reassigning a `let` variable

```js
let age = 25;
age = 30;           // reassignment (no 'let' needed again)
console.log(age);   // 30
```

- **Initialization** = assigning a value to a variable for the first time.
- **Reassignment** = giving a new value to an already-declared variable.

### Naming Rules

```js
// ✅ Valid
let age;
let _score;
let $total;
let player1Score;

// ❌ Invalid
let 1stPlace;     // cannot start with a number
let total-score!; // no special characters like - or !
```

- Must start with a **letter**, `_`, or `$` (never a number).
- Cannot use reserved keywords: `let`, `const`, `function`, `return`, etc.
- Avoid special characters (`!`, `@`, etc.).

### Naming Convention: camelCase

```js
let thisIsCamelCase;
let anotherExampleVariable;
let freeCodeCampStudents;
```

- First word lowercase, each following word capitalized.

### Case Sensitivity

```js
let age = 25;
let Age = 99;

console.log(age); // 25
console.log(Age); // 99 -> different variable!
```

---

## 4. `let` vs `const`

| Feature | `let` | `const` |
|---------|-------|---------|
| Reassignment | ✅ Allowed | ❌ Not allowed |
| Redeclaration | ❌ Not allowed | ❌ Not allowed |
| Must initialize at declaration | ❌ No | ✅ Yes |

### `let` — reassignable

```js
let score = 10;
score = 20;          // ✅ works
console.log(score);  // 20
```

### `const` — constant, cannot be reassigned

```js
const maxScore = 100;
maxScore = 200; // ❌ TypeError: Assignment to constant variable.
```

### `const` must be initialized immediately

```js
const age; // ❌ SyntaxError: Missing initializer in const declaration
```

### Neither can be redeclared

```js
let age = 25;
let age = 90; // ❌ SyntaxError: Identifier 'age' has already been declared
```

### `let` can be declared without a value (assign later)

```js
let city;
city = "Bengaluru"; // ✅ works
```

### When to use which

- Use **`let`** → value will change over time (e.g., score, counters, loop variables).
- Use **`const`** → value should stay fixed (e.g., config values, constants).

### `var` (legacy — avoid)

```js
var oldStyle = "not recommended";
```

- Similar to `let`, but has wider (function-level) scope → more prone to bugs.
- Modern JS prefers `let` and `const`.

---

## 🧠 Quick Recap

- **JS** = behavior layer on top of HTML (structure) + CSS (style).
- **Data types**: Number, String, Boolean, Undefined, Null, Object, Symbol, BigInt.
- **Variables** = named containers; use camelCase; can't start with a number.
- **`let`** → reassignable, not redeclarable.
- **`const`** → must initialize immediately, never reassignable.
- Prefer `let`/`const` over `var`.