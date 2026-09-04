# Python Dunder (Magic) Methods

## What are Dunder Methods?

**Dunder** = **D**ouble **UNDER**score. These are special methods that start and end with two underscores, e.g. `__init__`, `__str__`, `__eq__`.

Python calls these methods **automatically** in response to certain operations or built-in functions — you don't call them directly yourself (usually).

You've already used two:
- `__init__` → called automatically when you create a new object
- `__str__` → called automatically when you do `print(object)`

## Why They Matter

They let your custom classes work naturally with Python's built-in operators and functions — `==`, `+`, `<`, `len()`, etc. Without them, Python doesn't know how to compare, add, or measure your custom objects meaningfully.

## Common Dunder Methods (Grouped by Purpose)

### 1. Representation
| Method | Triggered by | Purpose |
|---|---|---|
| `__str__` | `print(obj)` | Readable output, for end users |
| `__repr__` | typing object in shell/debugger | Unambiguous output, for developers |

### 2. Comparison
| Method | Triggered by |
|---|---|
| `__eq__` | `obj1 == obj2` |
| `__lt__` | `obj1 < obj2` |
| `__gt__` | `obj1 > obj2` |

>  Without `__eq__`, Python compares objects by **memory location**, not field values. Two objects with identical data will show `False` with `==` unless `__eq__` is defined.

### 3. Arithmetic
| Method | Triggered by |
|---|---|
| `__add__` | `obj1 + obj2` |
| `__sub__` | `obj1 - obj2` |

Useful when an object logically supports addition (money, vectors, etc.)

### 4. Container-like Behavior
| Method | Triggered by |
|---|---|
| `__len__` | `len(obj)` |
| `__getitem__` | `obj[index]` |
| `__contains__` | `item in obj` |

