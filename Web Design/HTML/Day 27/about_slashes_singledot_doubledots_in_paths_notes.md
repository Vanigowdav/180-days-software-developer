## 3. Slashes, Single Dot, and Double Dot in Paths

When writing relative paths, these symbols matter:

| Symbol | Meaning |
|---|---|
| `/` | Separates folders (like a folder path) |
| `./` | Refers to the **current folder** (optional, often left out) |
| `../` | Refers to the **parent folder** (one level up) |
| `../../` | Goes **two levels up** |

### Examples

Imagine this folder structure:
```
project/
  ├── index.html
  ├── about.html
  └── images/
        └── photo.jpg
```

**From `index.html` linking to `photo.jpg` (same level → into a subfolder):**
```html
<img src="images/photo.jpg">
<!-- or explicitly: -->
<img src="./images/photo.jpg">
```

**From `images/gallery.html` linking back to `index.html` (go up one level):**
```html
<a href="../index.html">Home</a>
```

**From a deeper folder, going up two levels:**
```
project/
  ├── index.html
  └── blog/
        └── posts/
              └── post1.html
```
```html
<!-- from post1.html, going up 2 folders to reach index.html -->
<a href="../../index.html">Home</a>
```

### Common Usage
- `/` — used constantly to separate folder names
- `./` — rarely written explicitly, but understood as "current folder"
- `../` — very common when linking between pages in different folders
- `../../` or more — used in deeply nested folder structures
