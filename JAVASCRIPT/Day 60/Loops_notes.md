#  Day 60 — Loops

## 1. How Do Loops and Iteration Work?

A **loop** repeats a block of code multiple times, until a condition is no longer met. This repetition is called **iteration**.

### The classic `for` loop

```js
for (let i = 0; i < 5; i++) {
  console.log(i);
}
// 0
// 1
// 2
// 3
// 4
```

The `for` loop has three parts, separated by semicolons:

```js
for (initialization; condition; increment) {
  // code to repeat
}
```

| Part | Purpose | Example |
|------|---------|---------|
| Initialization | Runs once, before the loop starts | `let i = 0` |
| Condition | Checked before each iteration; loop stops when false | `i < 5` |
| Increment/Update | Runs after each iteration | `i++` |

### Looping over an array with `for`

```js
const fruits = ["apple", "banana", "cherry"];

for (let i = 0; i < fruits.length; i++) {
  console.log(fruits[i]);
}
// "apple"
// "banana"
// "cherry"
```

### Counting down

```js
for (let i = 5; i > 0; i--) {
  console.log(i);
}
// 5, 4, 3, 2, 1
```

> ⚠️ **Infinite loops:** forgetting to update the counter (or using a condition that's never false) causes the loop to run forever and freeze your program.
```js
// ❌ Infinite loop - i is never incremented
for (let i = 0; i < 5;) {
  console.log(i);
}
```

---

## 2. The `for...of` Loop

`for...of` iterates over the **values** of an iterable (arrays, strings, Maps, Sets, etc.) — simpler and cleaner than a classic `for` loop when you just need each value.

```js
const fruits = ["apple", "banana", "cherry"];

for (const fruit of fruits) {
  console.log(fruit);
}
// "apple"
// "banana"
// "cherry"
```

### Looping over a string

```js
for (const char of "Hi!") {
  console.log(char);
}
// "H"
// "i"
// "!"
```

### When to use `for...of`

- You need each **value**, not the index.
- Works on **arrays, strings, Maps, Sets** — anything "iterable."
- ❌ Does **not** work directly on plain objects (`{}`) — they aren't iterable.

```js
const numbers = [10, 20, 30];

for (const num of numbers) {
  console.log(num * 2);
}
// 20, 40, 60
```

---

## 3. The `for...in` Loop

`for...in` iterates over the **enumerable keys (property names)** of an object (or the indices of an array).

```js
const person = {
  name: "Alice",
  age: 30,
  city: "Bengaluru"
};

for (const key in person) {
  console.log(key, person[key]);
}
// "name" "Alice"
// "age" 30
// "city" "Bengaluru"
```

### `for...in` with arrays (generally avoid)

```js
const fruits = ["apple", "banana", "cherry"];

for (const index in fruits) {
  console.log(index, fruits[index]);
}
// "0" "apple"
// "1" "banana"
// "2" "cherry"
```

> ⚠️ `for...in` gives you the **index as a string**, and it's designed for objects, not arrays. For arrays, prefer `for...of`, `.forEach()`, or a classic `for` loop instead.

### `for...of` vs `for...in`

| Loop | Iterates Over | Best For |
|------|-----------------|----------|
| `for...of` | **Values** | Arrays, strings, Maps, Sets |
| `for...in` | **Keys** (property names / indices) | Plain objects |

```js
const person = { name: "Alice", age: 30 };

// for...in -> keys
for (const key in person) {
  console.log(key); // "name", "age"
}

// To get values from an object, combine with bracket notation
for (const key in person) {
  console.log(person[key]); // "Alice", 30
}
```

---

## 4. `while` Loop vs. `do...while` Loop

### `while` loop

Checks the condition **before** each iteration — if false from the start, the loop body never runs.

```js
let i = 0;

while (i < 5) {
  console.log(i);
  i++;
}
// 0, 1, 2, 3, 4
```

```js
let count = 10;

while (count < 5) {
  console.log("This never runs");
}
// (nothing is printed)
```

### `do...while` loop

Checks the condition **after** each iteration — so the loop body always runs **at least once**, even if the condition is false from the start.

```js
let i = 0;

do {
  console.log(i);
  i++;
} while (i < 5);
// 0, 1, 2, 3, 4
```

```js
let count = 10;

do {
  console.log("This runs once, regardless!");
} while (count < 5);
// "This runs once, regardless!"
```

| `while` | `do...while` |
|---------|----------------|
| Checks condition **before** running the body | Checks condition **after** running the body |
| May run **zero** times | Always runs **at least once** |

### Common use case for `while`

```js
// Useful when the number of iterations isn't known ahead of time
let userInput;

while (userInput !== "quit") {
  userInput = prompt("Type 'quit' to exit:");
}
```

---

## 5. `break` and `continue`

### `break` — exits the loop entirely

```js
for (let i = 0; i < 10; i++) {
  if (i === 5) {
    break; // stop the loop completely
  }
  console.log(i);
}
// 0, 1, 2, 3, 4
```

### `continue` — skips to the next iteration

```js
for (let i = 0; i < 5; i++) {
  if (i === 2) {
    continue; // skip this iteration, move to the next one
  }
  console.log(i);
}
// 0, 1, 3, 4 (2 is skipped, loop continues)
```

### Practical example — finding the first match

```js
const numbers = [3, 7, 11, 14, 19];

for (const num of numbers) {
  if (num % 2 === 0) {
    console.log(`First even number: ${num}`);
    break; // no need to keep checking once found
  }
}
// "First even number: 14"
```

### Practical example — skipping invalid values

```js
const scores = [85, -1, 92, -1, 78];

for (const score of scores) {
  if (score < 0) {
    continue; // skip invalid scores
  }
  console.log(`Valid score: ${score}`);
}
// "Valid score: 85"
// "Valid score: 92"
// "Valid score: 78"
```

| Statement | Effect |
|-----------|--------|
| `break` | Exits the loop immediately — no further iterations run |
| `continue` | Skips the rest of the current iteration and moves to the next one |

---

## Quick Recap

- **`for`** loop → classic 3-part loop (`init; condition; increment`), great for indexed control.
- **`for...of`** → iterates over **values** (arrays, strings, Maps, Sets).
- **`for...in`** → iterates over **keys** (best for plain objects; avoid for arrays).
- **`while`** → checks condition **before** running — may run zero times.
- **`do...while`** → checks condition **after** running — always runs at least once.
- **`break`** → exits the loop entirely.
- **`continue`** → skips the current iteration, moves to the next.