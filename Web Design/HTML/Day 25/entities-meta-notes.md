# Day 25: HTML Entities & Meta Description

## 1. HTML Entities

Special codes used to display reserved characters (`<`, `>`, `&`) 
as plain text instead of the browser interpreting them as HTML.

```html
<p>This is an &lt;img/&gt; element</p>
```
→ displays as: `This is an <img/> element`

### Common Entities
| Character | Entity |
|---|---|
| `<` | `&lt;` |
| `>` | `&gt;` |
| `&` | `&amp;` |
| `"` | `&quot;` |
| `'` | `&apos;` |

**Rule:** `&` and `<` must always be escaped. `>`, `"`, `'` are optional in plain text but good practice.

---

## 2. Meta Description

An HTML tag in `<head>` that summarizes a page's content 
(150–160 characters). Shown as the snippet under the title in 
search results.

```html
<head>
  <meta name="description" content="Brief summary of the page here.">
</head>
```

### Key Points
-Adding a meta description doesn't directly boost your Google ranking.
-But it does affect whether people click on your link or not. 
-The more people click, the more it can indirectly help your ranking over time. 
-One thing to keep in mind though — if your description doesn't match what people are actually searching for, Google might ignore it and show different text instead.

'''html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <titl>MY Favourite Foods</titl></title>
  <meta name="description" content="A page about my favorite foods including fried rice, masal dosa  with fun facts about each dish.">
</head>
<body>
    <div>
    <h1>My Food Menu</h1>
    <h2>Fried Rice</h2>
    <p>Spicy &gt; Mild</p>
    <h2>Masal Dosa</h2>
    <p>Terms &amp; Conditions apply</p>
    <h2>Pizza</h2>
    <p>"Use &lt;name&gt; a placeholder in the recipe</p>
    </div>
</body>
</html>
'''

