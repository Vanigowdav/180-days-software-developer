## 2. Absolute Path vs Relative Path

### Absolute Path
A **full URL** that includes the protocol (`https://`) and domain name. 
It points to a file no matter where your current page is located.

```html
<a href="https://example.com/images/photo.jpg">Photo</a>
```

### Relative Path
A path **relative to the current file's location**. It doesn't include 
the domain — it only works within your own project/website structure.

```html
<a href="images/photo.jpg">Photo</a>
```

### Comparison Table

| Feature | Absolute Path | Relative Path |
|---|---|---|
| Includes domain? | Yes |  No |
| Works if you move the project to another server? | ✅ Yes (always points to the same place) |  Yes (as long as folder structure stays the same) |
| Used for | Linking to external websites | Linking within your own website/project |
| Example | `https://mysite.com/about.html` | `about.html` or `../about.html` |

### When to Use Which
- **Absolute path** → linking to another website (external link)
- **Relative path** → linking to your own pages/files (internal link)
