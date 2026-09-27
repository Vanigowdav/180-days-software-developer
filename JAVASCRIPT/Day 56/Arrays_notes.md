# Day 55 — Arrays

## 1. Working with Arrays — The Basics

An **array** is an ordered list of values, stored in a single variable. Elements can be of any data type — even mixed types.

```js
let fruits = ["apple", "banana", "cherry"];
let mixed = [1, "two", true, null];
let empty = [];
```

### Accessing Elements (zero-indexed)

```js
let fruits = ["apple", "banana", "cherry"];

console.log(fruits[0]); // "apple"
console.log(fruits[2]); // "cherry"
console.log(fruits[5]); // undefined (out of range)

console.log(fruits.length); // 3

// Last element
console.log(fruits[fruits.length - 1]); // "cherry"
```

### Modifying Elements

```js
let fruits = ["apple", "banana", "cherry"];
fruits[1] = "blueberry";
console.log(fruits); // ["apple", "blueberry", "cherry"]
```

### Adding / Removing from the Ends

```js
let fruits = ["apple", "banana"];

fruits.push("cherry");     // add to end
console.log(fruits); // ["apple", "banana", "cherry"]

fruits.pop();               // remove from end
console.log(fruits); // ["apple", "banana"]

fruits.unshift("mango");   // add to beginning
console.log(fruits); // ["mango", "apple", "banana"]

fruits.shift();             // remove from beginning
console.log(fruits); // ["apple", "banana"]
```

| Method | Action | Modifies End |
|--------|--------|--------------|
| `push()` | Add to end | Yes |
| `pop()` | Remove from end | Yes |
| `unshift()` | Add to beginning | Yes |
| `shift()` | Remove from beginning | Yes |

### Looping Through an Array

```js
let fruits = ["apple", "banana", "cherry"];

for (let i = 0; i < fruits.length; i++) {
  console.log(fruits[i]);
}

// Or with forEach
fruits.forEach(fruit => console.log(fruit));
```

---

## 2. Finding the Index of an Element — `indexOf()`

```js
let colors = ["red", "green", "blue", "green"];

console.log(colors.indexOf("green")); // 1 (first match)
console.log(colors.indexOf("purple")); // -1 (not found)

console.log(colors.lastIndexOf("green")); // 3 (last match)
```

- Returns the **index** of the first matching element, or `-1` if it isn't found.
- Useful for finding *where* something is before removing or updating it.

---

## 3. Adding & Removing Elements from the Middle — `splice()`

`splice(startIndex, deleteCount, ...itemsToAdd)` modifies the original array in place.

### Removing elements

```js
let numbers = [1, 2, 3, 4, 5];

// Remove 2 elements starting at index 1
let removed = numbers.splice(1, 2);

console.log(numbers); // [1, 4, 5]
console.log(removed); // [2, 3] -> splice returns the removed items
```

### Adding elements (without removing)

```js
let numbers = [1, 2, 5];

numbers.splice(2, 0, 3, 4); // at index 2, remove 0, insert 3 and 4
console.log(numbers); // [1, 2, 3, 4, 5]
```

### Replacing elements

```js
let numbers = [1, 2, 99, 4];

numbers.splice(2, 1, 3); // remove 1 item at index 2, insert 3
console.log(numbers); // [1, 2, 3, 4]
```

| Parameter | Meaning |
|-----------|---------|
| `startIndex` | Where to start changing the array |
| `deleteCount` | How many elements to remove |
| `...itemsToAdd` | Elements to insert at that position (optional) |

> ⚠️ `splice()` **mutates** the original array. Use `slice()` (below) if you want a non-destructive copy instead.

---

## 4. Checking if an Array Contains a Value — `includes()`

```js
let fruits = ["apple", "banana", "cherry"];

console.log(fruits.includes("banana")); // true
console.log(fruits.includes("mango"));  // false
```

- Returns a **boolean** — cleaner than checking `indexOf() !== -1`.

```js
// Old way
console.log(fruits.indexOf("banana") !== -1); // true

// Modern way
console.log(fruits.includes("banana")); // true
```

---

## 5. Shallow Copies of an Array

A **shallow copy** duplicates the array itself (a new array in memory), but if it contains objects/arrays, those nested references still point to the *same* underlying objects.

### Why copying matters

```js
let original = [1, 2, 3];
let notACopy = original; // ❌ just another reference to the SAME array

notACopy.push(4);
console.log(original); // [1, 2, 3, 4] -> original was also changed!
```

### Ways to create a shallow copy

```js
let original = [1, 2, 3];

// 1. slice() with no arguments
let copy1 = original.slice();

// 2. Spread operator
let copy2 = [...original];

// 3. Array.from()
let copy3 = Array.from(original);

// 4. concat() with nothing added
let copy4 = [].concat(original);

copy1.push(4);
console.log(original); // [1, 2, 3] -> unaffected
console.log(copy1);    // [1, 2, 3, 4]
```

### The "shallow" part — nested objects still shared

```js
let original = [{ name: "Alice" }];
let copy = [...original]; // shallow copy

copy[0].name = "Bob";
console.log(original[0].name); // "Bob" -> nested object was shared!
```

- Shallow copy = top-level array is new, but nested objects/arrays inside are still **references** to the same data.
- For a true independent copy of nested data, you'd need a **deep copy** (e.g., `structuredClone()` or `JSON.parse(JSON.stringify(...))`).

| Method | Shallow Copy? |
|--------|----------------|
| `slice()` | ✅ |
| `[...spread]` | ✅ |
| `Array.from()` | ✅ |
| `concat()` | ✅ |
| Direct assignment (`=`) | ❌ (same reference, not a copy) |

---

## Quick Recap

- Arrays are ordered, zero-indexed lists — access with `arr[i]`, check size with `.length`.
- `push`/`pop` work on the end; `unshift`/`shift` work on the beginning.
- `indexOf()` finds an element's position (`-1` if missing).
- `splice()` adds/removes/replaces elements **in place**, anywhere in the array.
- `includes()` gives a quick true/false existence check.
- Direct assignment (`=`) copies the **reference**, not the array — use `slice()`, spread `[...]`, `Array.from()`, or `concat()` for a shallow copy.
- Shallow copies duplicate the array itself but still share nested object/array references.