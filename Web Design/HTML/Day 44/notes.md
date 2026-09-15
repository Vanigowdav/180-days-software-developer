````md
# CSS Learning Notes

---

# 1. CSS Transform

## What Is the `transform` Property?

The CSS `transform` property allows you to visually change an element without changing the normal layout of the page.

You can use it to:

- Move an element
- Rotate an element
- Make an element bigger or smaller
- Combine multiple transformations

### Basic Syntax

```css
.element {
  transform: transform-function;
}
```

---

## `translate()`

`translate()` moves an element from its original position.

### Example

```css
.box {
  transform: translate(50px, 20px);
}
```

### Meaning

- `50px` → moves right
- `20px` → moves down

### Daily-Life Example

Imagine a chair.

If you move the chair 50 cm to the right and 20 cm forward, the chair itself has moved visually.

---

## `translateX()`

Moves an element horizontally.

```css
.box {
  transform: translateX(50px);
}
```

The element moves 50px to the right.

---

## `translateY()`

Moves an element vertically.

```css
.box {
  transform: translateY(30px);
}
```

The element moves 30px downward.

---

## `rotate()`

Rotates an element.

```css
.box {
  transform: rotate(45deg);
}
```

The element rotates by 45 degrees.

### Daily-Life Example

Think about rotating a photo frame.

The frame stays in the same place but changes its angle.

---

## `scale()`

`scale()` changes the size of an element.

### Make Bigger

```css
.box {
  transform: scale(1.5);
}
```

The element becomes 1.5 times its original size.

### Make Smaller

```css
.box {
  transform: scale(0.5);
}
```

The element becomes half its original size.

### Different X and Y Scaling

```css
.box {
  transform: scale(1.5, 2);
}
```

- `1.5` → horizontal scaling
- `2` → vertical scaling

---

## Combining Transforms

You can use multiple transform functions together.

```css
.box {
  transform: translateX(50px) rotate(20deg) scale(1.2);
}
```

This will:

1. Move the element
2. Rotate it
3. Increase its size

---

## Important Point

Transforms usually change the visual appearance or position of an element without changing the normal document flow.

---

## Accessibility Considerations

Be careful when using transforms.

### 1. Visual Order vs DOM Order

A transformed element may visually appear somewhere different from its actual position in the HTML.

Screen readers usually follow the document/DOM order, not the visual transform.

### 2. Text Size

Avoid scaling text so much that it becomes difficult to read.

### 3. Animations

Too much movement or animation can cause discomfort for some users.

### 4. Interactive Elements

Buttons and links should remain easy to see and interact with.

---

# 2. CSS Box Model

Every HTML element can be understood as a box.

The CSS Box Model contains four main parts:

1. Content
2. Padding
3. Border
4. Margin

```text
+--------------------------------+
|             Margin             |
|   +------------------------+   |
|   |         Border         |   |
|   |  +------------------+  |   |
|   |  |     Padding      |  |   |
|   |  |  +------------+  |  |   |
|   |  |  |  Content   |  |  |   |
|   |  |  +------------+  |  |   |
|   |  +------------------+  |   |
|   +------------------------+   |
+--------------------------------+
```

---

## Content

Content is the actual information inside an element.

Examples:

- Text
- Image
- Video
- Other HTML elements

```css
.box {
  width: 300px;
  height: 200px;
}
```

The width and height normally refer to the content area when using the default `content-box`.

### Daily-Life Example

Think of a gift.

The actual gift inside the box is the content.

---

# Padding

Padding is the space between the content and the border.

```css
.box {
  padding: 20px;
}
```

This creates 20px of space around the content inside the element.

### Daily-Life Example

Imagine sitting on a sofa.

The space between you and the outside edge of the sofa is like padding.

---

## Padding Shorthand

### One Value

```css
padding: 20px;
```

Applies to all four sides.

```text
Top    = 20px
Right  = 20px
Bottom = 20px
Left   = 20px
```

### Two Values

```css
padding: 10px 20px;
```

```text
Top/Bottom = 10px
Left/Right = 20px
```

### Three Values

```css
padding: 10px 20px 30px;
```

```text
Top         = 10px
Left/Right  = 20px
Bottom      = 30px
```

### Four Values

```css
padding: 10px 20px 30px 40px;
```

The order is:

```text
Top → Right → Bottom → Left
```

Memory trick:

```text
TRBL
Top
Right
Bottom
Left
```

---

# Border

A border surrounds the padding and content.

```css
.box {
  border: 5px solid blue;
}
```

The three main border properties are:

```text
Border Width
Border Style
Border Color
```

Example:

```css
.box {
  border-width: 5px;
  border-style: solid;
  border-color: blue;
}
```

---

## Border Shorthand

```css
.box {
  border: 5px solid blue;
}
```

Meaning:

```text
5px   → width
solid → style
blue  → color
```

---

## Border Width

```css
.box {
  border-width: 5px;
}
```

You can also use multiple values:

```css
.box {
  border-width: 5px 10px 15px 20px;
}
```

Order:

```text
Top → Right → Bottom → Left
```

---

# Margin

Margin creates space outside the border.

```css
.box {
  margin: 20px;
}
```

### Daily-Life Example

Imagine two people sitting on chairs.

The space between the two chairs is like margin.

```text
Element 1        Element 2
[       ]        [       ]
     ← margin →
```

---

## Margin Shorthand

### One Value

```css
margin: 20px;
```

All four sides = 20px.

### Two Values

```css
margin: 10px 20px;
```

```text
Top/Bottom = 10px
Left/Right = 20px
```

### Three Values

```css
margin: 10px 20px 30px;
```

```text
Top        = 10px
Left/Right = 20px
Bottom     = 30px
```

### Four Values

```css
margin: 10px 20px 30px 40px;
```

```text
Top → Right → Bottom → Left
```

---

## Box Model Memory Trick

```text
Content
   ↓
Padding
   ↓
Border
   ↓
Margin
```

Remember:

```text
Padding = Space INSIDE
Margin  = Space OUTSIDE
```

---

# 3. CSS Margin Collapsing

Margin collapsing happens mainly with vertical margins.

When two vertical margins touch, they can combine into one margin instead of adding together.

---

## Example: Adjacent Siblings

```css
.box1 {
  margin-bottom: 20px;
}

.box2 {
  margin-top: 30px;
}
```

You might expect:

```text
20px + 30px = 50px
```

But because of margin collapsing, the resulting vertical gap is generally:

```text
30px
```

The larger margin wins.

---

## Daily-Life Example

Imagine two people standing between two chairs.

One person says:

> I need 20 cm space.

The other says:

> I need 30 cm space.

Instead of requiring 50 cm, only the larger required space may be used.

---

# Parent and First Child Margin Collapse

Margins can also collapse between a parent and its first child under certain conditions.

Example:

```css
.parent {
  margin-top: 20px;
}

.child {
  margin-top: 40px;
}
```

If nothing separates the margins, they can collapse.

The resulting margin can be:

```text
40px
```

instead of:

```text
20px + 40px = 60px
```

---

## What Can Prevent Margin Collapse?

Adding something between the margins can prevent the collapse.

For example:

```css
.parent {
  padding-top: 1px;
}
```

or:

```css
.parent {
  border-top: 1px solid black;
}
```

The padding or border separates the margins.

---

## Empty Elements

An empty element can also have its top and bottom margins collapse when there is no content, padding, or border separating them.

Example:

```css
.empty {
  margin-top: 20px;
  margin-bottom: 30px;
}
```

The margins can collapse to:

```text
30px
```

---

## Important Point

Margin collapsing mainly affects vertical margins.

Horizontal margins do not collapse in the same way.

---

# 4. CSS `box-sizing`

The `box-sizing` property controls how the width and height of an element are calculated.

There are two important values:

```css
content-box
border-box
```

---

# `content-box`

`content-box` is the default value.

```css
.box {
  box-sizing: content-box;
}
```

With `content-box`:

```text
width = Content only
height = Content only
```

Padding and border are added outside the specified width and height.

---

## Example

```css
.box {
  width: 300px;
  padding: 20px;
  border: 4px solid black;
}
```

Total width:

```text
Content = 300px
Left Padding = 20px
Right Padding = 20px
Left Border = 4px
Right Border = 4px

Total = 300 + 20 + 20 + 4 + 4

Total Width = 348px
```

---

# `border-box`

```css
.box {
  box-sizing: border-box;
}
```

With `border-box`, the specified width includes:

```text
Content
+
Padding
+
Border
```

But margin is still outside.

---

## Example

```css
.box {
  width: 300px;
  padding: 20px;
  border: 4px solid black;
  box-sizing: border-box;
}
```

The total rendered width remains:

```text
300px
```

The browser automatically adjusts the content area to fit the padding and border.

---

# Why Is `border-box` Useful?

It makes layouts easier to control.

For example:

```css
* {
  box-sizing: border-box;
}
```

This is a very common CSS rule.

It means all elements use `border-box`.

This is especially useful for responsive layouts.

---

# `content-box` vs `border-box`

| Property | content-box | border-box |
|---|---|---|
| Default | Yes | No |
| Width includes padding | No | Yes |
| Width includes border | No | Yes |
| Width includes margin | No | No |
| Easy for responsive layouts | Less convenient | More convenient |

---

# 5. CSS Reset

A CSS reset removes or changes browser default styles so that you can start with a more consistent styling baseline.

Different browsers may have different default styles.

For example:

```html
<h1>Hello</h1>
<p>Hello World</p>
```

Browsers automatically provide default:

- Margins
- Font sizes
- Spacing
- Other styles

A CSS reset gives the developer more control.

---

## Simple Custom CSS Reset

```css
* {
  margin: 0;
  padding: 0;
}
```

The `*` is called the universal selector.

It selects all HTML elements.

---

## Why Use a CSS Reset?

Without a reset:

```text
Browser defaults
      ↓
Your CSS
```

With a reset:

```text
Reset browser defaults
      ↓
Your CSS
```

This makes styling more predictable.

---

# Advantages of a Custom Reset

A custom reset gives you:

- More control
- Flexibility
- A clean starting point
- Ability to choose exactly what to reset

Example:

```css
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}
```

---

# Third-Party CSS Resets

Instead of creating your own reset, developers can use existing CSS reset libraries.

Examples:

```text
Normalize.css
sanitize.css
```

---

## Normalize.css

Normalize.css attempts to make browser styles more consistent while preserving useful browser defaults.

It can be useful when you want consistency without removing everything.

---

## sanitize.css

sanitize.css is another CSS library that provides a normalized baseline for styling.

---

# Accessibility and CSS Reset

Be careful when removing browser defaults.

Some default styles are useful for accessibility.

For example:

```css
*:focus {
  outline: none;
}
```

Removing focus indicators can make keyboard navigation difficult.

Always make sure interactive elements remain accessible.

---

# Performance

Adding external reset stylesheets can add extra resources that the browser needs to download.

For small projects, a simple custom reset may be enough.

---

# 6. CSS `filter`

The CSS `filter` property applies graphical effects to elements.

It can be used with:

- Images
- Text
- Containers
- Other HTML elements

---

## Basic Syntax

```css
.element {
  filter: function(amount);
}
```

---

# `blur()`

Creates a blur effect.

```css
img {
  filter: blur(2px);
}
```

The image becomes blurry.

---

# `brightness()`

Controls brightness.

```css
img {
  filter: brightness(150%);
}
```

The image becomes brighter.

---

## Completely Black

```css
img {
  filter: brightness(0%);
}
```

`brightness(0%)` makes the element completely black.

---

# `grayscale()`

Converts an element into grayscale.

```css
img {
  filter: grayscale(100%);
}
```

The image becomes black and white.

---

# `sepia()`

Creates a warm, old-photo-like effect.

```css
img {
  filter: sepia(80%);
}
```

---

# `hue-rotate()`

Changes the colors of an element.

```css
img {
  filter: hue-rotate(90deg);
}
```

---

# Combining Multiple Filters

Multiple filters can be applied together.

```css
img {
  filter: contrast(120%) brightness(110%) sepia(20%);
}
```

The filters are applied together.

---

# Other Filter Functions

Some other useful functions include:

```css
contrast()
invert()
saturate()
```

Example:

```css
img {
  filter: contrast(120%);
}
```

---

## Accessibility Considerations

Do not overuse filters.

For example, excessive:

- Blur
- Brightness
- Color changes
- Animations

may make content difficult to understand or use.

Always keep readability and accessibility in mind.

---

# 7. CSS Flexbox

Flexbox is a CSS layout system used to arrange elements in rows or columns.

Flexbox is especially useful for:

- Navigation bars
- Cards
- Buttons
- Menus
- Page layouts
- Centering elements

---

# Creating a Flex Container

Use:

```css
.container {
  display: flex;
}
```

The parent becomes a:

```text
Flex Container
```

Its direct children become:

```text
Flex Items
```

Example:

```html
<div class="container">
  <div>Box 1</div>
  <div>Box 2</div>
  <div>Box 3</div>
</div>
```

```css
.container {
  display: flex;
}
```

The boxes are placed in a row by default.

---

# Default Flex Direction

The default value is:

```css
flex-direction: row;
```

Example:

```css
.container {
  display: flex;
  flex-direction: row;
}
```

The items are arranged horizontally.

```text
[Box 1] [Box 2] [Box 3]
```

---

# Main Axis

The main axis is the primary direction in which flex items are arranged.

For:

```css
flex-direction: row;
```

the main axis is horizontal.

```text
Main Axis
────────────────────────→

[1] [2] [3]
```

---

# Cross Axis

The cross axis is perpendicular to the main axis.

For:

```css
flex-direction: row;
```

the cross axis is vertical.

```text
        Cross Axis
            ↓
            |
[1] [2] [3]
            |
            ↓
```

---

# Important Rule

The main axis is NOT always horizontal.

`flex-direction` determines the main axis.

---

# `flex-direction: row`

```css
.container {
  display: flex;
  flex-direction: row;
}
```

Items are arranged from left to right.

```text
[1] [2] [3]
```

---

# `flex-direction: row-reverse`

```css
.container {
  display: flex;
  flex-direction: row-reverse;
}
```

The order is reversed.

```text
[3] [2] [1]
```

---

# `flex-direction: column`

```css
.container {
  display: flex;
  flex-direction: column;
}
```

Items are arranged vertically.

```text
[1]

[2]

[3]
```

The main axis becomes vertical.

---

# `flex-direction: column-reverse`

```css
.container {
  display: flex;
  flex-direction: column-reverse;
}
```

The vertical order is reversed.

```text
[3]

[2]

[1]
```

---

# 8. Common Flexbox Properties

Important Flexbox properties include:

```text
flex-wrap
flex-flow
justify-content
align-items
align-self
```

---

# `flex-wrap`

The `flex-wrap` property controls whether flex items can move to another line.

---

## `nowrap`

This is the default value.

```css
.container {
  flex-wrap: nowrap;
}
```

The items remain on one line.

```text
[1] [2] [3] [4] [5]
```

If there is not enough space, items may shrink to fit.

---

## `wrap`

```css
.container {
  flex-wrap: wrap;
}
```

Items can move to a new line when there is not enough space.

Example:

```text
[1] [2] [3]
[4] [5]
```

This is useful for responsive card layouts.

---

## `wrap-reverse`

```css
.container {
  flex-wrap: wrap-reverse;
}
```

Items can wrap, but the wrapping direction is reversed.

---

# `flex-flow`

`flex-flow` is a shorthand property for:

```text
flex-direction
+
flex-wrap
```

Example:

```css
.container {
  flex-flow: row wrap;
}
```

This means:

```text
flex-direction: row;
flex-wrap: wrap;
```

Another example:

```css
.container {
  flex-flow: column wrap;
}
```

---

# `justify-content`

`justify-content` controls the alignment of flex items along the main axis.

Example:

```css
.container {
  display: flex;
  justify-content: center;
}
```

---

## `flex-start`

```css
.container {
  justify-content: flex-start;
}
```

Items move toward the beginning of the main axis.

```text
[1] [2] [3]----------------
```

---

## `flex-end`

```css
.container {
  justify-content: flex-end;
}
```

Items move toward the end.

```text
----------------[1] [2] [3]
```

---

## `center`

```css
.container {
  justify-content: center;
}
```

Items are centered along the main axis.

```text
------[1] [2] [3]------
```

---

## `space-between`

```css
.container {
  justify-content: space-between;
}
```

The first item is at the beginning.

The last item is at the end.

Remaining space is placed between the items.

```text
[1]--------[2]--------[3]
```

There is no extra space at the edges.

---

## `space-around`

```css
.container {
  justify-content: space-around;
}
```

Each item gets space around it.

The space at the edges is smaller than the space between items.

```text
--[1]----[2]----[3]--
```

---

## `space-evenly`

```css
.container {
  justify-content: space-evenly;
}
```

All spaces are equal.

```text
---[1]---[2]---[3]---
```

The gaps between items and the edges are equal.

---

# `align-items`

`align-items` controls alignment along the cross axis.

Example:

```css
.container {
  display: flex;
  align-items: center;
}
```

When the direction is:

```css
flex-direction: row;
```

the cross axis is vertical.

Therefore, `align-items` controls vertical alignment.

---

## `align-items: center`

```css
.container {
  display: flex;
  align-items: center;
}
```

Items are centered along the cross axis.

---

## `align-items: flex-start`

```css
.container {
  align-items: flex-start;
}
```

Items move toward the beginning of the cross axis.

---

## `align-items: flex-end`

```css
.container {
  align-items: flex-end;
}
```

Items move toward the end of the cross axis.

---

## `align-items: stretch`

```css
.container {
  align-items: stretch;
}
```

Flex items can stretch along the cross axis when their cross-axis size is `auto`.

Example:

```css
.container {
  display: flex;
  align-items: stretch;
}
```

If the items do not have an explicit cross-axis size, they can stretch to fill the available space.

---

# `align-self`

`align-self` is used to control the cross-axis alignment of one individual flex item.

Example:

```css
.container {
  display: flex;
  align-items: center;
}

.box2 {
  align-self: flex-end;
}
```

Here:

- Other items follow `align-items`
- `.box2` gets its own alignment

---

## Example

```html
<div class="container">
  <div>Box 1</div>
  <div class="special">Box 2</div>
  <div>Box 3</div>
</div>
```

```css
.container {
  display: flex;
  align-items: center;
}

.special {
  align-self: flex-end;
}
```

Only `Box 2` is moved toward the end of the cross axis.

---

# Flexbox Quick Memory

```text
display: flex
      ↓
Creates Flex Container

flex-direction
      ↓
Decides Main Axis

flex-wrap
      ↓
Controls Wrapping

flex-flow
      ↓
flex-direction + flex-wrap

justify-content
      ↓
Main Axis Alignment

align-items
      ↓
Cross Axis Alignment for All Items

align-self
      ↓
Cross Axis Alignment for One Item
```

---

# Flexbox Daily-Life Example

Imagine arranging books on a shelf.

```text
[Book 1] [Book 2] [Book 3]
```

`display: flex`:

```text
Put books in an organized layout.
```

`flex-direction`:

```text
Decides whether books are arranged horizontally or vertically.
```

`justify-content`:

```text
Decides how the books are distributed along the main direction.
```

`align-items`:

```text
Controls their position across the other direction.
```

`flex-wrap`:

```text
Allows books to move to another shelf/line when there is not enough space.
```

`align-self`:

```text
Moves one particular book differently from the others.
```

---

# Final CSS Flexbox Revision

```text
display: flex
        ↓
Flex Container

Direct Children
        ↓
Flex Items

flex-direction
        ↓
Main Axis Direction

row
        ↓
Horizontal Main Axis

column
        ↓
Vertical Main Axis

flex-wrap
        ↓
Controls Wrapping

flex-flow
        ↓
Direction + Wrapping

justify-content
        ↓
Main Axis Alignment

align-items
        ↓
Cross Axis Alignment

align-self
        ↓
One Flex Item's Cross Axis Alignment
```
````
