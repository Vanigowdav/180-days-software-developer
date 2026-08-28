## 3. Common Attributes — With Examples

### `controls`
Shows the play, pause, and volume buttons so the user can control playback.

```html
<audio controls>
  <source src="song.mp3" type="audio/mpeg">
</audio>
```
Without `controls`, the audio player won't show any buttons at all — the user can't play or pause it manually.

---

### `autoplay`
Starts playing the media automatically as soon as the page loads, without the user clicking play.

```html
<video autoplay width="400">
  <source src="intro.mp4" type="video/mp4">
</video>
```
⚠️ Most browsers block autoplay with sound unless the video is also `muted`.

---

### `loop`
Makes the media repeat automatically once it finishes playing.

```html
<audio controls loop>
  <source src="background-music.mp3" type="audio/mpeg">
</audio>
```
Useful for background music or looping short video clips.

---

### `muted`
Starts the media with the sound turned off.

```html
<video controls muted width="400">
  <source src="demo.mp4" type="video/mp4">
</video>
```
Often used together with `autoplay`, since browsers usually only allow autoplay if the video is muted.

---

### `width` / `height`
Sets the display size of the video on the page (only works with `<video>`, not `<audio>`).

```html
<video controls width="500" height="300">
  <source src="movie.mp4" type="video/mp4">
</video>
```
If you don't set this, the video plays at its original file size, which might be too big or too small for your layout.

---

### Combining Multiple Attributes

You can use more than one attribute together:

```html
<video controls autoplay muted loop width="400">
  <source src="promo.mp4" type="video/mp4">
</video>
```
This video will: play automatically, start muted, show controls, and loop when it ends.