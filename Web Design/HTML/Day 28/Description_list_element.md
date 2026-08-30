## 3. The Description List Element (`<dl>`)

The `<dl>` element (description list) is used to display a list of 
**terms and their descriptions** — like a glossary or a set of 
key-value pairs.

### The Three Tags Used Together

| Tag | Meaning |
|---|---|
| `<dl>` | Description List — the container for the whole list |
| `<dt>` | Description Term — the word/term being defined |
| `<dd>` | Description Definition — the explanation for that term |

### Basic Example

```html
<dl>
  <dt>HTML</dt>
  <dd>The standard markup language for creating web pages.</dd>

  <dt>CSS</dt>
  <dd>A stylesheet language used to style HTML elements.</dd>
</dl>
```

### How It Renders
```
HTML
    The standard markup language for creating web pages.
CSS
    A stylesheet language used to style HTML elements.
```
The browser automatically indents the `<dd>` content under its `<dt>` term.

### A Term Can Have Multiple Descriptions

```html
<dl>
  <dt>Browser</dt>
  <dd>Software used to access and view websites.</dd>
  <dd>Examples include Chrome, Firefox, and Safari.</dd>
</dl>
```

### Common Usage
- Glossaries and dictionaries
- FAQ pages (term = question, description = answer)
- Metadata display (e.g., product specifications: term = "Weight", description = "1.2kg")
- Naming conventions or definitions in documentation

### `<dl>` vs `<ul>`/`<ol>` — When to Use Which
- Use `<ul>`/`<ol>` for a **simple list of items** with no term-definition relationship
- Use `<dl>` when each item has a **name/term paired with an explanation**

---