---
name: hyperframes-capture-overlap
description: Split long AI chat screenshots into question and answer crop images, then place them as readable overlapping capture cards in HyperFrames overview or slide decks. Use when working on HyperFrames slides with GPT, Gemini, Claude, or other AI screenshots that must fit inside a slide placeholder without clipped text, with controlled overlap, crop sizing, and Airbnb-style light capture-stage styling.
---

# HyperFrames Capture Overlap

## Overview

Use this skill when a single tall AI screenshot must become two readable images inside a HyperFrames slide: a smaller question crop and a larger answer crop. Preserve readability first, then tune overlap and size.

## Workflow

1. Inspect the source image dimensions and visual structure.
2. Split the source into question and answer crop files.
3. Replace or confirm the slide markup uses `.capture-crop-layout`, `.capture-crop.question`, and `.capture-crop.answer`.
4. Add slide-specific CSS at the end of `overview.html` so it wins the cascade.
5. Verify with a browser screenshot and bounding boxes.

## Crop Images

Use `scripts/split_capture.py` for repeatable cropping.

```powershell
python <skill-dir>\scripts\split_capture.py `
  --source topics\<topic>\pictures\ex2.jpg `
  --question-out topics\<topic>\pictures\ex2-question.jpg `
  --answer-out topics\<topic>\pictures\ex2-answer.jpg `
  --question-box 275,42,745,692 `
  --answer-box 38,710,728,1430 `
  --question-size 470x650 `
  --answer-size 690x720
```

Crop boxes are `left,top,right,bottom` in source-image pixels. If the user says "same ratio as before," read the old `*-question` and `*-answer` image dimensions first, then resize the new crops to those same output sizes.

Use `Image.Resampling.LANCZOS` and save JPG with quality around `95` unless the existing file format is PNG.

## Markup Pattern

Use this structure inside the target `.capture-placeholder`. Keep AI type visible in `.capture-ai-label`.

```html
<div class="capture-empty">
  <div class="capture-crop-layout ex2">
    <div class="capture-ai-label">Gemini - ex2</div>
    <figure class="capture-crop question">
      <span>Question</span>
      <img src="pictures/ex2-question.jpg" alt="Gemini example 2 question capture" />
    </figure>
    <figure class="capture-crop answer">
      <span>Answer</span>
      <img src="pictures/ex2-answer.jpg" alt="Gemini example 2 answer capture" />
    </figure>
  </div>
</div>
```

Remove decorative dark browser top bars when the images need more space.

## CSS Pattern

Append slide-specific CSS near the end of the `<style>` block. Do not rely on earlier generic capture rules because overview files often have duplicate cascades.

```css
[data-slide="21"] .visual { height:920px; align-self:start; }
[data-slide="21"] .example-capture-layout.wide-copy {
  height:100%;
  align-items:stretch;
  grid-template-columns:minmax(210px, 19%) minmax(0, 81%);
  gap:12px;
}
[data-slide="21"] .capture-placeholder {
  height:100%;
  width:calc(100% + 46px);
  padding:8px;
  background:linear-gradient(145deg, #fff7f8 0%, #ffffff 46%, #f7f7f7 100%) !important;
  border:1px solid rgba(255,56,92,.14);
  box-shadow:0 30px 70px rgba(34,34,34,.12), 0 10px 30px rgba(255,56,92,.08);
}
[data-slide="21"] .capture-empty,
[data-slide="21"] .capture-crop-layout.ex2 {
  height:100%;
  background:
    linear-gradient(rgba(34,34,34,.035) 1px, transparent 1px),
    linear-gradient(90deg, rgba(34,34,34,.035) 1px, transparent 1px),
    radial-gradient(circle at 86% 12%, rgba(255,56,92,.12), transparent 34%),
    linear-gradient(145deg, #fffafb, #f7f7f7 72%, #ffffff) !important;
  background-size:34px 34px, 34px 34px, auto, auto;
}
[data-slide="21"] .capture-crop { position:absolute; }
[data-slide="21"] .capture-crop img {
  position:absolute !important;
  inset:0 !important;
  width:100% !important;
  height:100% !important;
  max-width:none !important;
  max-height:none !important;
  object-fit:contain !important;
}
[data-slide="21"] .capture-crop.question { right:1%; top:1.5%; width:41%; height:67%; }
[data-slide="21"] .capture-crop.answer { left:1%; bottom:1.5%; width:60%; height:75%; }
```

Tune only the final two `.question` and `.answer` rules for each slide. The preferred result is:

- placeholder right and bottom gaps under about `30px`
- question and answer images fully contained in their frames
- overlap width small enough not to hide important text
- answer card horizontal whitespace near zero when the answer crop is tall
- stage background light, not black, unless the slide intentionally uses a dark theme

## Verification

Use Playwright or browser automation to measure:

```js
const active = '#detail-frame > .scene.active';
const box = (sel) => {
  const r = document.querySelector(sel).getBoundingClientRect();
  return { x: Math.round(r.x), y: Math.round(r.y), w: Math.round(r.width), h: Math.round(r.height), right: Math.round(r.right), bottom: Math.round(r.bottom) };
};
```

Check:

- `question img` and `answer img` are inside their figure bounds.
- `placeholder` almost reaches the slide right and bottom edges.
- overlap area is intentional and does not hide key text.
- `npx hyperframes lint topics/<topic>` has zero errors.

When exporting PDF after this work, regenerate any PDF-only export HTML so it sees the latest `overview.html`.
