# CSS Grid — Complete Notes

## 1. What Is CSS Grid, and How Does It Differ from Flexbox?

CSS Grid is a two-dimensional layout system.

It allows you to arrange elements in rows AND columns at the same time.

Flexbox is one-dimensional (only row OR column at a time).

```css
.container {
  display: grid;
}
```

Use Grid for:
- Full page layouts
- Card grids
- Complex UI structures

## 2. How Can You Create Flexible Grids with the fr Unit?

The `fr` unit represents a fraction of the available space in the grid container.

```css
.container {
  display: grid;
  grid-template-columns: 1fr 1fr 1fr;
}
```

This creates 3 equal-width columns.

You can also mix fr with fixed units:

```css
.container {
  grid-template-columns: 200px 1fr 2fr;
}
```

## 3. How Can You Create Gaps Between Tracks in a Grid?

Use `gap` (or `row-gap` / `column-gap`) to add spacing between grid tracks.

```css
.container {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 20px;
}
```

- `row-gap` — space between rows
- `column-gap` — space between columns
- `gap` — shorthand for both

## 4. How Can You Repeat Track Listings in a Grid Layout?

The `repeat()` function avoids writing the same value multiple times.

```css
.container {
  grid-template-columns: repeat(3, 1fr);
}
```

This is the same as writing `1fr 1fr 1fr`.

You can also repeat patterns:

```css
.container {
  grid-template-columns: repeat(2, 100px 200px);
}
```

## 5. What Is the Difference Between an Implicit and Explicit Grid?

- Explicit grid: tracks you define using `grid-template-columns` / `grid-template-rows`.
- Implicit grid: extra tracks automatically created when content overflows the explicit grid.

```css
.container {
  display: grid;
  grid-template-columns: 1fr 1fr;
  grid-auto-rows: 100px;
}
```

`grid-auto-rows` / `grid-auto-columns` control the size of implicitly created tracks.

## 6. What Is the minmax() Function and How Does It Work?

`minmax()` sets a minimum and maximum size for a track.

```css
.container {
  grid-template-columns: minmax(100px, 1fr) 1fr;
}
```

This ensures a track never shrinks below 100px, but can grow up to 1fr.

Commonly combined with `repeat()` and `auto-fit`/`auto-fill`:

```css
.container {
  grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
}
```

## 7. How Do the grid-column and grid-row Properties Work?

These properties control how many tracks an item spans.

```css
.item {
  grid-column: 1 / 3;
  grid-row: 1 / 2;
}
```

- `grid-column: 1 / 3` — item spans from column line 1 to line 3 (covers 2 columns).
- Shorthand `span` keyword can also be used:

```css
.item {
  grid-column: span 2;
}
```

## 8. How Can You Position Items on the Grid Using the grid-template-areas Property?

`grid-template-areas` lets you name sections of the grid and place items visually.

```css
.container {
  display: grid;
  grid-template-columns: 1fr 3fr;
  grid-template-areas:
    "sidebar header"
    "sidebar content";
}

.sidebar {
  grid-area: sidebar;
}

.header {
  grid-area: header;
}

.content {
  grid-area: content;
}
```

Each string in `grid-template-areas` represents a row, and each word represents a column's area name.

## Summary

CSS Grid is a powerful two-dimensional layout system that works alongside Flexbox to build complex, responsive designs with precise control over rows, columns, gaps, and item placement.