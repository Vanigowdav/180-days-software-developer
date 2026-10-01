#  Day 58 — Optional Chaining and Object Destructuring

## 1. The Optional Chaining Operator (`?.`)

**Optional chaining** safely accesses deeply nested properties without throwing an error if something along the chain is `null` or `undefined`.

### The problem it solves

```js
const user = {
  name: "Alice",
  address: {
    city: "Bengaluru"
  }
};

console.log(user.job.title);
// ❌ TypeError: Cannot read properties of undefined (reading 'title')
// because `user.job` doesn't exist at all
```

### Using `?.`

```js
console.log(user.job?.title); // undefined (no error!)
console.log(user.address?.city); // "Bengaluru" (works normally if it exists)
```

- If the property **before** `?.` is `null`/`undefined`, the expression short-circuits and returns `undefined` immediately — instead of throwing an error.

### Optional chaining with methods

```js
const user = {
  name: "Alice",
  greet() {
    return "Hi!";
  }
};

console.log(user.greet?.());  // "Hi!" (method exists, so it's called)
console.log(user.sayBye?.()); // undefined (method doesn't exist, skipped safely)
```

### Optional chaining with arrays

```js
const data = {
  hobbies: ["reading", "chess"]
};

console.log(data.hobbies?.[0]);   // "reading"
console.log(data.pets?.[0]);      // undefined (no error, even though "pets" doesn't exist)
```

### Chaining multiple levels deep

```js
const company = {
  name: "TechCorp",
  ceo: {
    name: "Jordan"
  }
};

console.log(company.ceo?.address?.city); // undefined (no error at any level)
console.log(company.cfo?.name);          // undefined ("cfo" doesn't exist at all)
```

### Combining with the Nullish Coalescing Operator (`??`)

```js
const city = user.address?.city ?? "Unknown city";
console.log(city); // "Bengaluru" or "Unknown city" if address doesn't exist
```

| Without `?.` | With `?.` |
|--------------|-----------|
| Throws `TypeError` if a property in the chain is missing | Returns `undefined` safely |
| Requires manual checks (`if (user && user.job)`) | One-line safe access |

---

## 2. Object Destructuring

**Destructuring** lets you unpack properties from an object into individual variables in a single, concise line.

### Basic destructuring

```js
const person = {
  name: "Alice",
  age: 30,
  city: "Bengaluru"
};

// Without destructuring
const name1 = person.name;
const age1 = person.age;

// With destructuring
const { name, age, city } = person;

console.log(name); // "Alice"
console.log(age);  // 30
console.log(city); // "Bengaluru"
```

- Variable names **must match** the object's property keys (unless you rename them — see below).

### Renaming variables while destructuring

```js
const person = { name: "Alice", age: 30 };

const { name: fullName, age: years } = person;

console.log(fullName); // "Alice"
console.log(years);    // 30
// console.log(name);  // ❌ ReferenceError - "name" was renamed to fullName
```

### Default values

```js
const person = { name: "Alice" };

const { name, age = 18 } = person;

console.log(name); // "Alice"
console.log(age);  // 18 (default used since person.age doesn't exist)
```

### Destructuring nested objects

```js
const user = {
  name: "Alice",
  address: {
    city: "Bengaluru",
    zip: "560001"
  }
};

const { address: { city, zip } } = user;

console.log(city); // "Bengaluru"
console.log(zip);  // "560001"
```

### Destructuring in function parameters

```js
function greet({ name, age }) {
  return `${name} is ${age} years old`;
}

const person = { name: "Alice", age: 30 };
console.log(greet(person)); // "Alice is 30 years old"
```

### Combining destructuring with optional chaining

```js
function getCity(user) {
  const { city } = user.address ?? {};
  return city ?? "Unknown";
}

console.log(getCity({ address: { city: "Bengaluru" } })); // "Bengaluru"
console.log(getCity({})); // "Unknown"
```

### Rest pattern with destructuring

```js
const person = { name: "Alice", age: 30, city: "Bengaluru", job: "Dev" };

const { name, ...rest } = person;

console.log(name); // "Alice"
console.log(rest); // { age: 30, city: "Bengaluru", job: "Dev" }
```

---

## Quick Recap

- **Optional chaining (`?.`)** safely accesses nested properties/methods/array items, returning `undefined` instead of throwing when something is missing.
- Pair `?.` with `??` to supply a fallback value when the result is `null`/`undefined`.
- **Object destructuring** `const { key } = obj` unpacks properties into variables in one line.
- Supports **renaming** (`{ key: newName }`), **default values** (`{ key = default }`), **nested destructuring**, and destructuring directly in **function parameters**.
- The **rest pattern** (`...rest`) gathers remaining properties into a new object.