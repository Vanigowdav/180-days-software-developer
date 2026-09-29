#  Day 56 — Introduction to JavaScript Objects and Their Properties

## 1. What Is an Object, and How Do You Access Properties?

An **object** is a collection of related data stored as **key-value pairs** (called "properties"). Objects group information together in a structured way.

```js
const person = {
  name: "Alice",
  age: 30,
  isStudent: false
};
```

- `name`, `age`, `isStudent` = **keys** (also called properties).
- `"Alice"`, `30`, `false` = **values**.

### Dot Notation

```js
console.log(person.name); // "Alice"
console.log(person.age);  // 30
```

- Simple and readable — use when the key name is known and valid (no spaces/special chars).

### Bracket Notation

```js
console.log(person["name"]); // "Alice"

// Useful when the key is dynamic (stored in a variable)
let key = "age";
console.log(person[key]); // 30

// Also required for keys with spaces or special characters
const car = { "model year": 2024 };
console.log(car["model year"]); // 2024
// console.log(car.model year); // ❌ SyntaxError
```

| Dot Notation | Bracket Notation |
|--------------|-------------------|
| `obj.key` | `obj["key"]` |
| Key must be a valid identifier | Key can be any string/expression |
| Can't use variables for the key | Can use a variable for the key |

---

## 2. Removing Properties from an Object

Use the `delete` operator to remove a property.

```js
const person = {
  name: "Alice",
  age: 30
};

delete person.age;
console.log(person); // { name: "Alice" }

delete person["name"];
console.log(person); // {}
```

- `delete` permanently removes the key-value pair from the object.
- Returns `true` if successful.

```js
console.log(delete person.name); // true
```

---

## 3. Checking If an Object Has a Property

### `in` operator

```js
const person = { name: "Alice", age: 30 };

console.log("name" in person);    // true
console.log("email" in person);   // false
```

### `hasOwnProperty()`

```js
console.log(person.hasOwnProperty("age"));   // true
console.log(person.hasOwnProperty("email")); // false
```

### Checking for `undefined` (less reliable)

```js
console.log(person.email !== undefined); // false
// ⚠️ Fails if a property legitimately holds the value undefined
```

| Method | Notes |
|--------|-------|
| `"key" in obj` | Checks own **and** inherited properties |
| `obj.hasOwnProperty("key")` | Checks only the object's own properties (safer, more common) |

---

## 4. Accessing Nested Objects and Arrays in Objects

Objects can contain other objects and arrays as values — you chain dot/bracket notation to reach deeper values.

```js
const user = {
  name: "Maya",
  address: {
    city: "Bengaluru",
    zip: "560001"
  },
  hobbies: ["reading", "chess", "hiking"]
};

console.log(user.address.city);     // "Bengaluru"
console.log(user["address"]["zip"]); // "560001"

console.log(user.hobbies[0]);       // "reading"
console.log(user.hobbies[2]);       // "hiking"
```

### Deeper nesting

```js
const company = {
  name: "TechCorp",
  employees: [
    { name: "Sam", role: "Developer" },
    { name: "Jo", role: "Designer" }
  ]
};

console.log(company.employees[0].name); // "Sam"
console.log(company.employees[1].role); // "Designer"
```

### Optional chaining (safer access for possibly-missing properties)

```js
console.log(user.address?.country); // undefined (no error, even though "country" doesn't exist)
console.log(user.job?.title);       // undefined (no error, even though "job" doesn't exist at all)
```

- Without `?.`, accessing a property on `undefined` (like `user.job.title` when `job` doesn't exist) throws a `TypeError`.

---

## 5. Primitive vs Non-Primitive Data Types

### Primitive Data Types

Stored **by value**. Copying a primitive creates a completely independent copy.

```js
let a = 5;
let b = a; // b gets a COPY of the value
b = 10;

console.log(a); // 5 (unchanged)
console.log(b); // 10
```

Primitive types: `Number`, `String`, `Boolean`, `undefined`, `null`, `Symbol`, `BigInt`.

### Non-Primitive (Reference) Data Types

Stored **by reference**. Copying a variable copies the *reference* to the same object in memory — both variables point to the same data.

```js
let obj1 = { value: 5 };
let obj2 = obj1; // obj2 points to the SAME object
obj2.value = 10;

console.log(obj1.value); // 10 -> obj1 changed too!
console.log(obj2.value); // 10
```

Non-primitive types: `Object`, `Array`, `Function`.

| Primitive | Non-Primitive (Reference) |
|-----------|-----------------------------|
| Number, String, Boolean, undefined, null, Symbol, BigInt | Object, Array, Function |
| Stored by value | Stored by reference |
| Copying creates an independent value | Copying shares the same underlying data |
| Compared by value (`5 === 5` → true) | Compared by reference (`{} === {}` → false) |

```js
console.log({} === {}); // false -> different objects in memory
const obj = {};
console.log(obj === obj); // true -> same reference
```

---

## 6. Functions vs. Object Methods

A **function** is standalone code you define and call independently.
A **method** is simply a function that's stored as a property of an object.

```js
// Regular function
function greet(name) {
  return `Hello, ${name}`;
}
console.log(greet("Alex")); // "Hello, Alex"

// Object with a method
const person = {
  name: "Alex",
  greet: function () {
    return `Hello, my name is ${this.name}`;
  },
  // Shorthand method syntax (ES6)
  sayBye() {
    return `Bye from ${this.name}`;
  }
};

console.log(person.greet());  // "Hello, my name is Alex"
console.log(person.sayBye()); // "Bye from Alex"
```

- Methods are called using **dot notation** on the object (`person.greet()`).
- Methods commonly use `this` to refer to the object they belong to (arrow functions don't rebind `this`, so regular functions or shorthand syntax are typically used for methods that need `this`).

---

## 7. The `Object()` Constructor

`Object()` is a built-in constructor function that can create a new, empty object — but **object literal syntax `{}` is preferred** in almost all cases.

```js
// Using the Object() constructor
const obj1 = new Object();
obj1.name = "Alice";
console.log(obj1); // { name: "Alice" }

// Preferred: object literal
const obj2 = {
  name: "Alice"
};
console.log(obj2); // { name: "Alice" }
```

### `Object()` can also convert values

```js
console.log(typeof Object("hello")); // "object" -> wraps a string as an Object
console.log(typeof Object(42));      // "object" -> wraps a number as an Object
```

### When to actually use `Object()`

- Rarely needed for everyday object creation — the literal `{}` syntax is shorter, clearer, and more idiomatic.
- `Object()` (and related static methods like `Object.keys()`, `Object.values()`, `Object.entries()`, `Object.assign()`) are more useful for **working with** existing objects than creating new ones.

```js
const person = { name: "Alice", age: 30 };

console.log(Object.keys(person));   // ["name", "age"]
console.log(Object.values(person)); // ["Alice", 30]
console.log(Object.entries(person)); // [["name","Alice"], ["age",30]]
```

---

## Quick Recap

- Objects store data as key-value pairs; access with **dot notation** (`obj.key`) or **bracket notation** (`obj["key"]`, needed for dynamic/special keys).
- `delete obj.key` removes a property.
- Check for a property with `"key" in obj` or `obj.hasOwnProperty("key")`.
- Access nested data by chaining `.` / `[]`; use `?.` (optional chaining) to safely access possibly-missing properties.
- **Primitives** (Number, String, Boolean, undefined, null, Symbol, BigInt) copy **by value**.
- **Non-primitives** (Object, Array, Function) copy **by reference**.
- A **method** = a function stored as a property on an object, called via `obj.method()`.
- Prefer object literals `{}` over `new Object()` for creating objects; `Object.keys/values/entries` are handy for working with existing ones.