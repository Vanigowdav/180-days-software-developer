# 📘 CSS & Design Notes — Typography to Accessibility

---

## 1. Typography Best Practices

**Definition:** Art of arranging text for readability, hierarchy, and accessibility.

### Readable fonts

```css
p { font-family: 'Open Sans', Arial, sans-serif; }
```

**Output:** Clean, simple text — easy to scan and read quickly, unlike decorative/cursive fonts.

### Visual hierarchy via size

```css
h1 { font-size: 40px; }
h2 { font-size: 28px; color: #555; }
p  { font-size: 18px; color: #777; }
```

**Output:** Eyes land on h1 first (biggest), then h2, then p — reading order is guided automatically by size.

### Limit font count

Use only **2–3 fonts max** per design → keeps things consistent, faster to load, stronger branding.



## 2. Font Families

**Definition:** A group of fonts sharing the same base design (e.g., Arial → Arial Bold, Arial Italic — like siblings).

### Fallback fonts (priority list)

```css
p {
  font-family: Arial, Lato, sans-serif;
}
```

**Output:** Browser tries Arial first → if missing, tries Lato → if that's missing too, uses ANY generic sans-serif font on the device. Text never disappears!

> **Fun fact:** Fallback happens character-by-character — if one font is missing just ONE symbol, only that symbol borrows from the next font in line.

### Generic font families

serif | sans-serif | monospace | cursive | fantasy


**Output:** Always put one of these LAST in your font-family list — it's the final safety net so text is always readable.

**Quiz:** How to list fallback fonts in CSS? → Separate with commas: `font-family: Arial, Lato, sans-serif;`

---

## 3. Web-Safe Fonts

**Definition:** Fonts pre-installed on almost every device/browser — reliable, consistent rendering.

### Examples
Sans-serif: Arial, Verdana, Trebuchet MS
Serif: Times New Roman, Georgia


**Output:** These render correctly for nearly EVERY visitor, no download needed → faster page load + consistent look.

**Real life:** Web-safe fonts = a plain white T-shirt everyone already owns. Custom fonts = a special outfit you have to order and wait for delivery.

**Quiz:** Which is NOT a web-safe font — Arial, Verdana, Georgia, Dancing Script? → **Dancing Script** (decorative, not pre-installed everywhere)

---

## 4. @font-face Rule

**Definition:** Lets you use ANY font on your site by telling the browser where to download the font file from — even if the user doesn't have it installed.

### Basic usage

```css
@font-face {
  font-family: "MyCustomFont";
  src: url("myfont.woff2") format("woff2");
}

body {
  font-family: "MyCustomFont", sans-serif;
}
```

**Output:** 3 steps only: (1) name the font, (2) point to the file, (3) use that name anywhere like a normal font. Browser downloads & applies it automatically.

**Formats:** `woff2` (best compression), `woff`, `opentype`, `truetype`, `svg`, `embedded-opentype`.

**Real life:** Like ordering a special outfit online — `@font-face` is the "delivery address" telling the browser exactly where to fetch the font from.

**Quiz:** Which descriptor is REQUIRED in `@font-face`? → `src` (tells browser where the font file is)

---

## 5. External Fonts (Google Fonts & Font Squirrel)

**Definition:** Font files hosted on someone else's server (not your own project) — offers way more variety than web-safe fonts.

### Using Google Fonts (link method)

```html
<link href="https://fonts.googleapis.com/css2?family=Roboto" rel="stylesheet">
```

```css
body { font-family: "Roboto", sans-serif; }
```

**Output:** Browser fetches Roboto from Google's servers when the page loads, then applies it site-wide.

### Using @import (CSS method)

```css
@import url('https://fonts.googleapis.com/css2?family=Roboto');
```

### Font Squirrel

Download a "Webfont Kit" → get font files + a ready-made `@font-face` rule + license info.

**Careful:** Too many external fonts = slower website load time. Balance style with performance!

**Quiz:** Drawback of using multiple external fonts? → Increased website load time.

---

## 6. text-shadow Property

**Syntax:** `text-shadow: x-offset y-offset blur-radius color;`

### Basic shadow

```css
p { text-shadow: 3px 2px #ff0000; }
```

**Output:** Red shadow appears 3px to the right, 2px down from the text. Positive = right/down. Negative = left/up.

### Adding blur (optional 3rd value)

```css
p { text-shadow: 3px 2px 3px #ff0000; }
```

**Output:** Shadow becomes soft and smooth instead of a sharp red copy — looks like a real shadow. Default blur = 0 (sharp).

### Multiple layered shadows

```css
p {
  text-shadow: 
    1px 1px 0px red,
    2px 2px 0px orange,
    3px 3px 0px yellow;
}
```

**Output:** Three colored shadow layers stack behind the text (first = front layer), creating a fun 3D/retro effect.

**Quiz:** Black shadow, right offset, 5px blur — correct code? → `text-shadow: 5px 0px 5px black;`

---

## 7. Color Contrast Checking Tools

**Purpose:** Verify text/background color combos are readable for everyone, including visually impaired users (WCAG standards).

### WebAIM's Color Contrast Checker
Enter foreground hex: 
#333333
Enter background hex: 
#FFFFFF
→ Tool shows contrast ratio + AA/AAA pass/fail


**Output:** Instant online check — paste your two hex codes, get a pass/fail result against WCAG guidelines.

### TPGi Colour Contrast Analyzer

Desktop app. Can scan a WHOLE webpage (not just 2 colors), has an eyedropper tool, and can simulate color blindness.

**Real life:** Like trying on someone else's glasses prescription to see how your design "feels" to a color-blind user.

**Quiz:** What do WCAG AA/AAA levels refer to? → Minimum contrast ratios required for accessibility.

---

## 8. Hiding Content Accessibly

**Key concept:** The "accessibility tree" is what screen readers use to understand a page. Some hiding methods REMOVE content from it entirely.

| Method | Visible? | Takes space? | Screen reader access? |
|---|---|---|---|
| `display: none` | No | No | ❌ No |
| `visibility: hidden` | No | Yes | ❌ No |
| `.sr-only` (visually hidden) | No | No | ✅ Yes |
| `hidden` attribute | No | No | ❌ No |

### Screen-reader-only trick

```css
.sr-only {
  position: absolute;
  width: 1px;
  height: 1px;
  overflow: hidden;
  clip: rect(0, 0, 0, 0);
}
```

**Output:** Sighted users see nothing extra, but screen reader users hear the hidden text — e.g. a button shows "✕" visually but announces "Close menu" out loud.

**Real life:** `display:none` = removing a room from the building blueprint entirely. `visibility:hidden` = room still exists (takes space) but is locked & invisible. `.sr-only` = a room only accessible by a special "secret" entrance (screen readers) — everyone else can't see it.

**Quiz:** When should you hide content? → Only when it genuinely enhances the user experience.

---

## Quick Recap Table

| # | Topic | One-Line Reminder |
|---|---|---|
| 1 | Typography | Readable fonts, size hierarchy, limit to 2-3 fonts |
| 2 | Font Families | Group of related fonts; use comma-separated fallbacks |
| 3 | Web-Safe Fonts | Pre-installed everywhere (Arial, Verdana, Georgia...) |
| 4 | @font-face | Define & load any custom font via `src: url(...)` |
| 5 | External Fonts | Google Fonts / Font Squirrel — hosted on external servers |
| 6 | text-shadow | `x y blur color` — layered shadows via commas |
| 7 | Contrast Tools | WebAIM (online) & TPGi (desktop) check WCAG contrast ratios |
| 8 | Hiding Content | Use `.sr-only` to hide visually but keep screen-reader accessible |

---
