---
name: hyperframes-overview-pptx-export
description: Export HyperFrames overview.html files into final 16:9 PowerPoint .pptx decks by capturing each data-slide scene as a full-slide PNG and inserting optional speaker-note text as PPT speaker notes. Use when a user asks to convert, export, or deliver a HyperFrames overview HTML deck as PPT/PPTX, especially when PDF export or browser loading is unreliable and the visual result must match overview.html.
---

# HyperFrames Overview PPTX Export

Use this skill to turn a finished `topics/<topic>/overview.html` into a presentation-ready `.pptx`.

Default to image-based slides for visual fidelity. Do not rebuild HTML content as editable PowerPoint shapes unless the user explicitly asks for editable slide elements.

## Workflow

1. Confirm the source `overview.html` path and topic folder.
2. Check that slides are represented by `#detail-frame .scene[data-slide]`.
3. Export by numeric `data-slide` order, not DOM order. Overview files may have scenes in a different DOM order after restore or manual edits.
4. Hide overview UI chrome during capture: sidebar, header, nav buttons, aim overlays, edit controls.
5. Capture each scene at `1920x1080` and insert it full-bleed into a 16:9 PPTX slide.
6. Copy `.speaker-note` text from each scene into PPT speaker notes when present.
7. Validate slide count, screenshot dimensions, PPT internal slide count, and a few representative slides.

## Script

Use `scripts/export_overview_to_pptx.mjs` from this skill. Copy it into the workspace or run it in place.

Typical command from a HyperFrames workspace root:

```powershell
node <skill-dir>\scripts\export_overview_to_pptx.mjs `
  --topic why-ai-49th-oxxodok-airbnb `
  --expected-slides 34
```

Useful options:

```text
--topic <name>              Uses topics/<name>/overview.html
--overview <path>           Direct path to overview.html
--out <path>                Output .pptx path
--screens-dir <path>        Screenshot output directory
--expected-slides <number>  Fail if data-slide count differs
--width <px>                Capture width, default 1920
--height <px>               Capture height, default 1080
--no-notes                  Skip PPT speaker notes
```

If `playwright` or `pptxgenjs` is missing, install them in the workspace:

```powershell
npm install playwright pptxgenjs
npx playwright install chromium
```

## Validation

After export, verify:

- screenshot count equals expected slide count
- each screenshot is `1920x1080`
- PPT internal `ppt/slides/slide*.xml` count equals expected slide count
- representative slides render correctly, especially recently edited capture-heavy slides
- notes count is acceptable when the deck uses `.speaker-note`

For PowerShell PPT integrity checks, see `references/validation.md`.

## Failure Handling

- If the script reports the wrong slide count, inspect `data-slide` values first.
- If slides appear black or empty, ensure the export CSS targets the actual frame selector and that the active class is not overridden.
- If the PPT order is wrong, sort by numeric `data-slide`, never by DOM position.
- If local or remote images are missing, open `overview.html` in Chromium and wait for fonts and images before capture.
