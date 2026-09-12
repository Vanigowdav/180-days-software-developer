# Day 42 – CSS + UI Design Notes

## Topics Learned

- Color Theory
- CSS Color Formats
- Gradients
- Text Input Styling
- `appearance: none`
- Special Input Elements

---

# 1. Color Theory

Color theory is a set of principles used to choose and combine colors so a design looks attractive, readable, and communicates the right feeling.

### Color Wheel

- **Primary Colors:** Red, Blue, Yellow
- **Secondary Colors:** Green, Orange, Purple
- **Complementary Colors:** Opposite colors on the color wheel → strong contrast
- **Analogous Colors:** Colors next to each other → calm look
- **Triadic Colors:** Three evenly spaced colors → balanced and vibrant

### Warm Colors

- Red
- Orange
- Yellow

Usually feel energetic and exciting.

### Cool Colors

- Blue
- Green
- Purple

Usually feel calm and professional.

### 60-30-10 Rule

A common UI color guideline:

- **60%** → Dominant color
- **30%** → Secondary color
- **10%** → Accent color

### Example

```css
body {
  background-color: #e0f2fe;
}

button {
  background-color: #2563eb;
}

.alert {
  background-color: #f97316;
}