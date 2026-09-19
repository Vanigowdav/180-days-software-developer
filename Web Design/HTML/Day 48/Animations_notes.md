# CSS Animations and Accessibility — Complete Notes

## 1. What Are CSS Animations, and How Do They Work?

CSS animations let elements change style values over time, without JavaScript.

They are built using two parts:
- `@keyframes` — defines the stages of the animation
- `animation` property — applies the keyframes to an element

```css
@keyframes slidein {
  from {
    transform: translateX(0%);
  }
  to {
    transform: translateX(100%);
  }
}

.box {
  animation: slidein 3s ease-in-out infinite;
}
```

Key animation properties:
- `animation-name` — name of the `@keyframes` rule
- `animation-duration` — how long one cycle takes
- `animation-timing-function` — speed curve (e.g. `ease`, `linear`)
- `animation-delay` — wait time before starting
- `animation-iteration-count` — how many times it repeats (`infinite` for forever)
- `animation-direction` — normal, reverse, alternate

You can also define multiple stages using percentages:

```css
@keyframes colorChange {
  0% {
    background-color: red;
  }
  50% {
    background-color: yellow;
  }
  100% {
    background-color: green;
  }
}
```

## 2. What Are Accessibility Concerns Around Using Animations, and How Can prefers-reduced-motion Help?

Some users experience discomfort, dizziness, or motion sickness from animated or moving content — this is a real accessibility issue, not just a preference.

Operating systems provide a "reduce motion" setting for this reason.

CSS can detect this setting using the `prefers-reduced-motion` media query.

```css
@media (prefers-reduced-motion: reduce) {
  .box {
    animation: none;
  }
}
```

Best practices:
- Always provide a reduced-motion alternative for large or fast movements
- Avoid flashing content (can trigger seizures in photosensitive users)
- Keep essential information accessible even if animation is disabled
- Don't rely on animation alone to convey meaning

Example combining both normal and reduced-motion styles:

```css
.box {
  animation: slidein 3s ease-in-out infinite;
}

@media (prefers-reduced-motion: reduce) {
  .box {
    animation: none;
    transform: none;
  }
}
```

## Summary

CSS animations bring interfaces to life using `@keyframes` and the `animation` property, but accessibility must be considered — `prefers-reduced-motion` allows designers to respect user comfort by disabling or simplifying animations for those who need it.