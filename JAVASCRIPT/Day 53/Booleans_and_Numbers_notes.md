# Day 53 — Booleans and Numbers

## 1. Numbers & Arithmetic Operators

```js
let a = 10;
let b = 3;

console.log(a + b); // 13  addition
console.log(a - b); // 7   subtraction
console.log(a * b); // 30  multiplication
console.log(a / b); // 3.333... division
console.log(a % b); // 1   modulus (remainder)
console.log(a ** b); // 1000  exponentiation (a to the power of b)
```

### Order of Operations (PEMDAS)

```js
console.log(2 + 3 * 4);   // 14 (multiplication first)
console.log((2 + 3) * 4); // 20 (parentheses first)
```

### Type Coercion (common bug source)

JavaScript automatically converts types in certain operations — this is **type coercion**, and it can cause unexpected results.

```js
console.log("5" + 3);   // "53"  -> + with a string triggers concatenation
console.log("5" - 3);   // 2     -> - forces numeric conversion
console.log("5" * "2"); // 10    -> * forces numeric conversion
console.log(5 + true);  // 6     -> true coerces to 1
console.log(5 + false); // 5     -> false coerces to 0
console.log("5" == 5);  // true  -> == allows type coercion
console.log("5" === 5); // false -> === checks type AND value
```

> 🐛 **Debugging tip:** Type coercion bugs often come from mixing strings and numbers with `+`. Use `Number()`, `String()`, or `parseInt()`/`parseFloat()` to convert explicitly instead of relying on coercion.

```js
let input = "42"; // from a form or prompt()
let num = Number(input);
console.log(num + 8); // 50 (not "428")
```

---

## 2. Operator Behavior — Increment & Decrement

```js
let count = 5;

count++; // post-increment: count = count + 1
console.log(count); // 6

count--; // post-decrement: count = count - 1
console.log(count); // 5
```

### Prefix vs Postfix — the tricky part

```js
let x = 5;
console.log(x++); // 5 (returns OLD value, THEN increments)
console.log(x);   // 6

let y = 5;
console.log(++y); // 6 (increments FIRST, then returns new value)
console.log(y);   // 6
```

| Operator | Behavior |
|----------|----------|
| `x++` | Returns current value, *then* increments |
| `++x` | Increments *first*, then returns new value |
| `x--` | Returns current value, *then* decrements |
| `--x` | Decrements *first*, then returns new value |

> 🐛 **Common bug:** Using `x++` inside an expression when you meant `++x` (or vice versa) gives an off-by-one result.

---

## 3. Booleans, Equality & Inequality Operators

A **Boolean** is `true` or `false` — often the result of a comparison.

```js
console.log(5 == "5");   // true  (loose equality — coerces types)
console.log(5 === "5");  // false (strict equality — checks type too)
console.log(5 != "5");   // false (loose inequality)
console.log(5 !== "5");  // true  (strict inequality)
```

> ✅ **Best practice:** Prefer `===` and `!==` over `==` and `!=` to avoid unexpected type coercion bugs.

---

## 4. Comparison Operators

```js
console.log(10 > 5);   // true
console.log(10 < 5);   // false
console.log(10 >= 10); // true
console.log(10 <= 9);  // false
```

| Operator | Meaning |
|----------|---------|
| `>` | Greater than |
| `<` | Less than |
| `>=` | Greater than or equal to |
| `<=` | Less than or equal to |
| `==` / `===` | Equal / strictly equal |
| `!=` / `!==` | Not equal / strictly not equal |

- Comparisons always evaluate to a **Boolean** (`true`/`false`).

---

## 5. Unary Operators

A **unary operator** works on a single value/operand.

```js
let num = 5;

console.log(-num);   // -5   (negation)
console.log(+num);   // 5    (unary plus - forces numeric conversion)
console.log(+"42");  // 42   (converts string to number)
console.log(!true);  // false (logical NOT)
console.log(!false); // true

typeof num; // "number" -> typeof is also a unary operator
```

- `++` and `--` (from earlier) are also unary operators.
- Unary `+` is a quick way to convert a string to a number: `+"10"` → `10`.

---

## 6. Bitwise Operators

Bitwise operators work directly on the **binary (bit) representation** of numbers.

```js
console.log(5 & 1);  // 1   AND  (0101 & 0001 = 0001)
console.log(5 | 1);  // 5   OR   (0101 | 0001 = 0101)
console.log(5 ^ 1);  // 4   XOR  (0101 ^ 0001 = 0100)
console.log(~5);     // -6  NOT  (inverts all bits)
console.log(5 << 1); // 10  left shift  (multiplies by 2)
console.log(5 >> 1); // 2   right shift (divides by 2, rounds down)
```

| Operator | Name | Description |
|----------|------|-------------|
| `&` | AND | 1 only if both bits are 1 |
| `\|` | OR | 1 if either bit is 1 |
| `^` | XOR | 1 if bits are different |
| `~` | NOT | Inverts all bits |
| `<<` | Left shift | Shifts bits left |
| `>>` | Right shift | Shifts bits right |

- Rarely used in everyday app code, but common in low-level tasks: flags, permissions, performance-critical math.

---

## 7. Conditional Statements — if / else if / else

```js
let age = 20;

if (age < 13) {
  console.log("Child");
} else if (age < 20) {
  console.log("Teenager");
} else {
  console.log("Adult");
}
// "Adult"
```

- `if` runs a block only when its condition is `true`.
- `else if` checks additional conditions in order.
- `else` runs when none of the above conditions were true.
- Only the **first matching** block runs — the rest are skipped.

```js
// Ternary operator - shorthand for simple if/else
let status = age >= 18 ? "Adult" : "Minor";
console.log(status); // "Adult"
```

---

## 8. Binary Logical Operators

```js
console.log(true && false); // false  -> AND: both must be true
console.log(true || false); // true   -> OR: at least one must be true
console.log(!true);         // false  -> NOT: flips the boolean

// Practical use in conditions
let age = 25;
let hasLicense = true;

if (age >= 18 && hasLicense) {
  console.log("Can drive");
}

let isWeekend = true;
let isHoliday = false;

if (isWeekend || isHoliday) {
  console.log("No work today");
}
```

| Operator | Name | Returns `true` when... |
|----------|------|--------------------------|
| `&&` | AND | Both sides are true |
| `\|\|` | OR | At least one side is true |
| `!` | NOT | Inverts the value |

- **Short-circuit evaluation:** `&&` stops at the first falsy value; `||` stops at the first truthy value.

```js
console.log(false && sayHi()); // sayHi() never runs
console.log(true || sayHi());  // sayHi() never runs
```

---

## 9. The `Math` Object

`Math` is a built-in object with properties and methods for mathematical operations.

```js
console.log(Math.round(4.5));   // 5   rounds to nearest integer
console.log(Math.floor(4.9));   // 4   rounds down
console.log(Math.ceil(4.1));    // 5   rounds up
console.log(Math.abs(-10));     // 10  absolute value
console.log(Math.max(3, 7, 2)); // 7   largest value
console.log(Math.min(3, 7, 2)); // 2   smallest value
console.log(Math.pow(2, 3));    // 8   2 to the power of 3
console.log(Math.sqrt(16));     // 4   square root
console.log(Math.random());     // random number between 0 and 1 (exclusive of 1)

// Random integer between 1 and 10
let randomNum = Math.floor(Math.random() * 10) + 1;
console.log(randomNum);

console.log(Math.PI); // 3.141592653589793
```

| Method/Property | Purpose |
|------------------|---------|
| `Math.round()` | Round to nearest whole number |
| `Math.floor()` | Round down |
| `Math.ceil()` | Round up |
| `Math.abs()` | Absolute value |
| `Math.max()` / `Math.min()` | Largest / smallest of given values |
| `Math.pow(base, exp)` | Exponentiation |
| `Math.sqrt()` | Square root |
| `Math.random()` | Random decimal between 0 (inclusive) and 1 (exclusive) |
| `Math.PI` | The value of π |

---

## 🧠 Quick Recap

- Arithmetic: `+ - * / % **` — watch out for **type coercion** with `+` and strings.
- `x++`/`++x` differ in *when* the value is returned vs updated.
- Use `===`/`!==` over `==`/`!=` to avoid coercion bugs.
- Comparison operators (`> < >= <=`) always return a Boolean.
- Unary operators act on one value: `-`, `+`, `!`, `typeof`.
- Bitwise operators (`& | ^ ~ << >>`) work on binary bit patterns.
- `if / else if / else` runs the first matching block; ternary `? :` is a shorthand.
- Logical operators `&&`, `||`, `!` combine/invert conditions, with short-circuit evaluation.
- `Math` object provides handy methods: `round`, `floor`, `ceil`, `abs`, `max`, `min`, `pow`, `sqrt`, `random`.