#  Day 57 — Working with JSON

## 1. What Is JSON?

**JSON** (JavaScript Object Notation) is a lightweight, text-based format for storing and exchanging data. It's commonly used to send data between a server and a web app (APIs).

```json
{
  "name": "Alice",
  "age": 30,
  "isStudent": false,
  "hobbies": ["reading", "chess"],
  "address": {
    "city": "Bengaluru",
    "zip": "560001"
  }
}
```

### JSON syntax rules

- Keys **must** be strings wrapped in double quotes (`"key"`, not `'key'` or `key`).
- Values can be: string, number, boolean, `null`, array, or another JSON object.
- **No** functions, `undefined`, comments, or trailing commas allowed.
- JSON looks a lot like a JS object literal, but it's just **text** — not actual JS objects until parsed.

```json
// ❌ Invalid JSON examples
{
  name: "Alice",        // key must be quoted
  age: undefined,       // undefined not allowed
  greet: function(){},  // functions not allowed
}
```

### Accessing values (once it's a JS object)

Since JSON structure mirrors JS objects, once you have JSON data as a JavaScript object, you access it the same way — dot or bracket notation.

```js
const data = {
  name: "Alice",
  age: 30,
  address: {
    city: "Bengaluru"
  },
  hobbies: ["reading", "chess"]
};

// Dot notation
console.log(data.name);          // "Alice"
console.log(data.address.city);  // "Bengaluru"

// Bracket notation
console.log(data["age"]);        // 30
console.log(data["address"]["city"]); // "Bengaluru"

// Arrays inside JSON-style objects
console.log(data.hobbies[0]);    // "reading"
```

---

## 2. `JSON.parse()` and `JSON.stringify()`

Raw JSON coming from an API, file, or `localStorage` is just a **string** — it needs to be converted into an actual JS object before you can work with it (and vice versa).

### `JSON.parse()` — string → JS object

Converts a JSON-formatted **string** into a usable JavaScript object.

```js
const jsonString = '{"name": "Alice", "age": 30}';

const obj = JSON.parse(jsonString);

console.log(obj);       // { name: "Alice", age: 30 }
console.log(obj.name);  // "Alice"
console.log(typeof obj); // "object"
```

> 💡 Common use case: parsing an API response.
```js
fetch("https://api.example.com/user")
  .then(response => response.json()) // fetch() actually parses JSON for you automatically
  .then(data => console.log(data.name));
```

### `JSON.stringify()` — JS object → string

Converts a JavaScript object into a JSON-formatted **string**, useful for sending data to a server or saving it in storage.

```js
const person = {
  name: "Alice",
  age: 30,
  hobbies: ["reading", "chess"]
};

const jsonString = JSON.stringify(person);

console.log(jsonString);
// '{"name":"Alice","age":30,"hobbies":["reading","chess"]}'
console.log(typeof jsonString); // "string"
```

> 💡 Common use case: saving data to `localStorage` (which only stores strings).
```js
localStorage.setItem("user", JSON.stringify(person));

const saved = JSON.parse(localStorage.getItem("user"));
console.log(saved.name); // "Alice"
```

### Pretty-printing with `JSON.stringify()`

```js
const person = { name: "Alice", age: 30 };

console.log(JSON.stringify(person, null, 2));
// {
//   "name": "Alice",
//   "age": 30
// }
```

- The 3rd argument (`2`) adds indentation spaces for readability.

### Quick comparison

| Method | Converts | Direction |
|--------|----------|-----------|
| `JSON.parse()` | JSON string → JS object | Incoming data (e.g., from an API) |
| `JSON.stringify()` | JS object → JSON string | Outgoing data (e.g., to an API or storage) |

```js
const obj = { a: 1 };
const str = JSON.stringify(obj); // '{"a":1}'
const backToObj = JSON.parse(str); // { a: 1 }

console.log(obj === backToObj); // false -> different objects, same shape
```

---

## Quick Recap

- **JSON** = text-based data format; keys must be double-quoted strings, no functions/`undefined`/comments allowed.
- Once JSON data becomes a JS object, access values the normal way: dot or bracket notation.
- `JSON.parse()` → turns a JSON **string** into a JS **object** (use for incoming data).
- `JSON.stringify()` → turns a JS **object** into a JSON **string** (use for outgoing data / storage).
- `JSON.stringify(obj, null, 2)` pretty-prints with indentation.