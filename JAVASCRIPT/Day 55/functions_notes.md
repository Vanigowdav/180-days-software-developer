# Day 55 — Working with Functions

## 1. What Is the Purpose of Functions?

A **function** is a reusable block of code designed to perform a specific task. Instead of repeating the same code, you define it once and **call** it whenever needed.

### Function Declaration

```js
function greet(name) {
  return `Hello, ${name}!`;
}

console.log(greet("Maya")); // "Hello, Maya!"
console.log(greet("Sam"));  // "Hello, Sam!"
```

- `name` is a **parameter** — a placeholder for the value passed in.
- `"Maya"` / `"Sam"` are **arguments** — the actual values passed when calling the function.
- `return` sends a value back out of the function; without it, a function returns `undefined`.

### Function Expression

```js
const add = function (a, b) {
  return a + b;
};

console.log(add(3, 4)); // 7
```

- Here the function is stored in a variable (`add`) rather than declared with a name directly.

### Why use functions?

- **Reusability** — write logic once, use it many times.
- **Organization** — breaks a program into smaller, manageable pieces.
- **Readability** — descriptive function names make code self-documenting.

```js
function calculateArea(width, height) {
  return width * height;
}

console.log(calculateArea(5, 10)); // 50
console.log(calculateArea(3, 7));  // 21
```

### Default Parameters

```js
function greetUser(name = "Guest") {
  return `Welcome, ${name}!`;
}

console.log(greetUser());        // "Welcome, Guest!"
console.log(greetUser("Alex"));  // "Welcome, Alex!"
```

---

## 2. Arrow Functions

**Arrow functions** are a more concise syntax for writing function expressions, introduced in ES6.

```js
// Regular function expression
const add = function (a, b) {
  return a + b;
};

// Arrow function equivalent
const addArrow = (a, b) => {
  return a + b;
};

console.log(addArrow(3, 4)); // 7
```

### Implicit Return (shorthand)

If the function body is a single expression, you can omit `{}` and `return`:

```js
const add = (a, b) => a + b;
console.log(add(2, 3)); // 5

const square = x => x * x; // single parameter -> parentheses optional
console.log(square(5)); // 25

const sayHi = () => "Hi!"; // no parameters -> empty parentheses required
console.log(sayHi()); // "Hi!"
```

### Arrow Functions and `this`

Arrow functions don't have their own `this` — they inherit `this` from the surrounding (enclosing) scope. This makes them especially useful inside callbacks like `.map()`, `.forEach()`, etc.

```js
const numbers = [1, 2, 3];
const doubled = numbers.map(num => num * 2);
console.log(doubled); // [2, 4, 6]
```

| Regular Function | Arrow Function |
|-------------------|-----------------|
| Has its own `this` | Inherits `this` from surrounding scope |
| Can be used as a constructor | Cannot be used as a constructor |
| Verbose syntax | Concise syntax |
| Has `arguments` object | Does not have its own `arguments` object |

---

## 3. Scope — Global, Local, and Block Scope

**Scope** determines where a variable is accessible in your code.

### Global Scope

Variables declared outside any function or block are in the **global scope** — accessible anywhere in the program.

```js
let globalVar = "I'm global";

function showGlobal() {
  console.log(globalVar); // accessible here
}

showGlobal(); // "I'm global"
console.log(globalVar); // accessible here too
```

### Local (Function) Scope

Variables declared inside a function are **local** to that function — they can't be accessed from outside it.

```js
function myFunction() {
  let localVar = "I'm local";
  console.log(localVar); // works
}

myFunction();
console.log(localVar); // ❌ ReferenceError: localVar is not defined
```

### Block Scope

Variables declared with `let` or `const` inside a block (`{}` — e.g., `if`, `for`, `while`) are scoped **only to that block**.

```js
if (true) {
  let blockVar = "I'm block-scoped";
  console.log(blockVar); // works inside the block
}

console.log(blockVar); // ❌ ReferenceError: blockVar is not defined
```

### `var` vs `let`/`const` scope difference

```js
if (true) {
  var oldStyle = "function-scoped, not block-scoped";
}
console.log(oldStyle); // ✅ works — var ignores block scope

if (true) {
  let newStyle = "block-scoped";
}
console.log(newStyle); // ❌ ReferenceError
```

- `var` is scoped to the nearest **function** (ignores blocks) — one more reason `let`/`const` are preferred.

### Scope Chain (nested functions)

Inner functions/blocks can access variables from their outer (enclosing) scope, but not vice versa.

```js
let outerVar = "outer";

function outerFunction() {
  let innerVar = "inner";

  function innerFunction() {
    console.log(outerVar); // ✅ accessible (from global scope)
    console.log(innerVar); // ✅ accessible (from outer function scope)
  }

  innerFunction();
}

outerFunction();
// console.log(innerVar); // ❌ not accessible outside outerFunction
```

| Scope Type | Declared Where | Accessible From |
|------------|-----------------|------------------|
| Global | Outside any function/block | Anywhere in the program |
| Local (function) | Inside a function | Only within that function |
| Block | Inside `{}` (if/for/while, etc.) with `let`/`const` | Only within that block |

---

## Quick Recap

- **Functions** package reusable logic; use **parameters** to receive input and `return` to send output back.
- **Arrow functions** (`=>`) are a shorter syntax, support implicit return, and inherit `this` from their surrounding scope.
- **Scope** controls variable visibility:
  - **Global** → accessible everywhere.
  - **Local/function** → accessible only inside that function.
  - **Block** → accessible only inside `{}` when using `let`/`const`.
- Prefer `let`/`const` over `var` for predictable block-level scoping.