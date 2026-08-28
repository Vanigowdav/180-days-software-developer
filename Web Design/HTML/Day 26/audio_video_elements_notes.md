# Day 26: HTML Audio and Video Elements

## 1. The `<audio>` Element

The `audio` element is used to embed sound content, like music or 
other audio files, directly into a webpage.

```html
<audio controls>
  <source src="song.mp3" type="audio/mpeg">
</audio>
```

---

## 2. The `<video>` Element

The `video` element is used to embed video content directly into 
a webpage.

```html
<video controls width="400">
  <source src="movie.mp4" type="video/mp4">
</video>
```

---

## 3. Common Attributes

| Attribute | Purpose |
|---|---|
| `controls` | Shows play/pause/volume buttons |
| `autoplay` | Starts playing automatically when the page loads |
| `loop` | Repeats the media after it ends |
| `muted` | Starts the media muted |
| `width` / `height` | Sets the display size (used with video, not audio) |

---

## 4. Why Use the `<source>` Element?

The `source` element lets you provide multiple file formats for 
the same media. If the browser doesn't support one format, it 
tries the next one listed.

```html
<video controls>
  <source src="movie.mp4" type="video/mp4">
  <source src="movie.webm" type="video/webm">
  Your browser doesn't support video.
</video>
```

---

## Key Takeaways
- `<audio>` = embed sound/music
- `<video>` = embed video content
- `controls` attribute gives the user playback buttons
- `<source>` allows fallback formats for better browser compatibility