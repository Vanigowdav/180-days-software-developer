# Day 37 — CSS Specificity, Cascade, Inheritance, Lists/Links, Backgrounds/Borders

## 1. CSS Specificity, Cascade Algorithm, and Inheritance

### Specificity
Determines which CSS rule wins when multiple rules target the same element.

| Selector type | Specificity value |
|---|---|
| Inline styles | 1000 |
| ID selector (`#id`) | 100 |
| Class, attribute, pseudo-class (`.class`, `[attr]`, `:hover`) | 10 |
| Type selector, pseudo-element (`div`, `::before`) | 1 |
| Universal selector (`*`) | 0 (no specificity) |

- Higher specificity wins, regardless of order in the file.
- Inline CSS > ID > Class > Type > Universal.

### `!important`
- Overrides normal specificity rules — highest priority.
- **Best practice:** avoid using it; it makes debugging/overriding styles harder later. Use only as a last resort (e.g. utility classes, overriding third-party CSS).

### Cascade Algorithm (high level)
When multiple rules apply, CSS decides the winner in this order:
1. **Origin/Importance** — `!important` rules > author styles > browser default styles
2. **Specificity** — higher specificity wins
3. **Source order** — if specificity is equal, the last rule declared wins

### Inheritance (high level)
- Some CSS properties automatically pass from parent to child elements (e.g. `color`, `font-family`, `line-height`).
- Others do **not** inherit by default (e.g. `margin`, `padding`, `border`, `width`).
- Can force inheritance with `inherit` keyword, or reset with `initial` / `unset`.

---

## 2. Styling Lists and Links

### Spacing list items
- Use `margin` (space outside each `<li>`) or `line-height` (space within/around line box) to control spacing between list items.

### `list-style` properties
| Property | Purpose |
|---|---|
| `list-style-type` | Bullet/number style (`disc`, `circle`, `square`, `decimal`, `none`, etc.) |
| `list-style-position` | `inside` or `outside` — whether marker sits inside or outside content box |
| `list-style-image`