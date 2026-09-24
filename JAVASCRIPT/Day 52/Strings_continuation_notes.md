#  Day 52 — Working with Strings in JavaScript

## 1. Bracket Notation — Accessing Characters

Strings are indexed like arrays (starting at `0`). Use square brackets `[]` to access a character at a specific position.

```js
let word = "Hello";

console.log(word[0]); // "H"
console.log(word[1]); // "e"
console.log(word[4]); // "o"
console.log(word[10]); // undefined (out of range)

// Length of a string
console.log(word.length); // 5

// Get the last character
console.log(word[word.length - 1]); // "o"
```

---

## 2. Newlines & Escape Characters

**Escape characters** use a backslash `\` to insert special characters inside a string.

```js
console.log("Line one\nLine two");
// Line one
// Line two

console.log("She said \"hello\"");   // She said "hello"
console.log('It\'s a nice day');     // It's a nice day
console.log("Tab\tSpaced");          // Tab   Spaced
console.log("Backslash: \\");        // Backslash: \
```

| Escape | Meaning |
|--------|---------|
| `\n` | New line |
| `\t` | Tab |
| `\'` | Single quote |
| `\"` | Double quote |
| `\\` | Backslash |

> 💡 Template literals (backticks) let you write real newlines without `\n`:
```js
let multiLine = `Line one
Line two`;
console.log(multiLine);
```

---

## 3. Template Literals & String Interpolation

**Template literals** use backticks `` ` `` instead of quotes, allowing embedded expressions via `${}` — called **string interpolation**.

```js
let name = "Maya";
let age = 22;

let intro = `My name is ${name} and I'm ${age} years old.`;
console.log(intro);
// "My name is Maya and I'm 22 years old."

// Expressions work too
console.log(`Next year I'll be ${age + 1}.`);
// "Next year I'll be 23."

// Multi-line strings
let card = `
Name: ${name}
Age: ${age}
`;
console.log(card);
```

- Cleaner than `+` concatenation, supports multi-line strings and embedded expressions.

---

## 4. Finding the Position of a Substring

### `indexOf()`

```js
let sentence = "The quick brown fox";

console.log(sentence.indexOf("quick")); // 4
console.log(sentence.indexOf("cat"));   // -1 (not found)
```

### `lastIndexOf()`

```js
let text = "banana";
console.log(text.lastIndexOf("a")); // 5 (last occurrence)
```

- Returns the **index** where the substring starts, or `-1` if not found.

---

## 5. The `prompt()` Method

`prompt()` displays a popup dialog asking the user for input. It returns the input as a **string** (or `null` if canceled).

```js
let userName = prompt("What is your name?");
console.log(`Hello, ${userName}!`);

let ageInput = prompt("How old are you?");
let age = Number(ageInput); // convert string to number
console.log(age + 1);
```

- Only works in a **browser environment** (not in Node.js by default).
- Execution pauses until the user responds.

---

## 6. ASCII, `charCodeAt()`, and `fromCharCode()`

**ASCII** (American Standard Code for Information Interchange) maps characters to numeric codes (e.g., `"A"` = 65, `"a"` = 97).

### `charCodeAt()` — character → code

```js
let letter = "A";
console.log(letter.charCodeAt(0)); // 65

let word = "Hi";
console.log(word.charCodeAt(0)); // 72 ("H")
console.log(word.charCodeAt(1)); // 105 ("i")
```

### `String.fromCharCode()` — code → character

```js
console.log(String.fromCharCode(65)); // "A"
console.log(String.fromCharCode(97)); // "a"
console.log(String.fromCharCode(72, 105)); // "Hi"
```

- Useful for character-shifting logic (e.g., Caesar ciphers, capitalization tricks).

---

## 7. Testing if a String Contains a Substring

### `includes()`

```js
let sentence = "JavaScript is fun";

console.log(sentence.includes("fun"));    // true
console.log(sentence.includes("Python")); // false
```

- Returns a **boolean** — best choice for a simple yes/no check (cleaner than `indexOf() !== -1`).

```js
// Old way
console.log(sentence.indexOf("fun") !== -1); // true

// Modern way
console.log(sentence.includes("fun")); // true
```

---

## 8. Extracting a Substring

### `slice(start, end)`

```js
let text = "Hello World";

console.log(text.slice(0, 5));   // "Hello"
console.log(text.slice(6));      // "World" (to the end)
console.log(text.slice(-5));     // "World" (negative = from the end)
```

### `substring(start, end)`

```js
console.log(text.substring(0, 5)); // "Hello"
// Similar to slice, but doesn't support negative indices (treats them as 0)
```

- `end` index is **not included** in the result.

---

## 9. Changing String Casing

```js
let word = "Hello World";

console.log(word.toUpperCase()); // "HELLO WORLD"
console.log(word.toLowerCase()); // "hello world"
```

- Both return a **new** string; the original remains unchanged (strings are immutable).

---

## 10. Trimming Whitespace

```js
let messy = "   Hello World   ";

console.log(messy.trim());       // "Hello World"
console.log(messy.trimStart());  // "Hello World   "
console.log(messy.trimEnd());    // "   Hello World"
```

- `trim()` removes whitespace from **both** ends.
- `trimStart()` / `trimEnd()` remove from just one side.

---

## 11. String Modification Methods

```js
let str = "Hello World";

// replace() — replaces first match
console.log(str.replace("World", "JS")); // "Hello JS"

// replaceAll() — replaces all matches
console.log("a-a-a".replaceAll("a", "b")); // "b-b-b"

// split() — turns a string into an array
console.log("apple,banana,cherry".split(",")); // ["apple", "banana", "cherry"]

// concat() — joins strings together
console.log("Hello".concat(" ", "World")); // "Hello World"

// repeat() — repeats a string n times
console.log("ab".repeat(3)); // "ababab"

// padStart() / padEnd() — pad to a target length
console.log("5".padStart(2, "0")); // "05"
console.log("5".padEnd(2, "0"));   // "50"
```

- All of these return a **new** string — none mutate the original (remember: strings are immutable).

---

## Quick Recap

| Task | Method |
|------|--------|
| Access a character | `str[index]` |
| Escape special chars | `\n`, `\t`, `\'`, `\"`, `\\` |
| Embed variables in a string | Template literals `` `${}` `` |
| Find substring position | `indexOf()`, `lastIndexOf()` |
| Get user input | `prompt()` |
| Char ↔ ASCII code | `charCodeAt()` / `String.fromCharCode()` |
| Check if substring exists | `includes()` |
| Extract part of a string | `slice()`, `substring()` |
| Change case | `toUpperCase()`, `toLowerCase()` |
| Remove whitespace | `trim()`, `trimStart()`, `trimEnd()` |
| Modify/build strings | `replace()`, `replaceAll()`, `split()`, `concat()`, `repeat()`, `padStart()`, `padEnd()` |