---
name: ppt-hyperframes-deck
description: Use when creating, revising, or QA-checking HyperFrames 16:9 decks or card-news topics in this v2 workspace.
---

# PPT HyperFrames Deck

Use this skill for repeatable presentation and card-news production in this repository. It complements `AGENTS.md` and preserves the `2_slide_master` HyperFrames method.

## Requirements Analysis

Capture these items before implementation:

- purpose, audience, duration or reading context
- source materials and evidence boundaries
- company/brand name
- design source: `new_md/DESIGN-회사이름.md`
- output target: `deck` or `card-news`
- topic folder name under `topics/<topic-name>/`
- final target: PDF or PPTX presentation file
- review target: overview review and manual Edit/Aim refinement before export

If the user asks for "PPT", default to a 16:9 HyperFrames deck source that will be reviewed in `overview.html` and then exported to PDF or PPTX. MP4 render is optional and only for explicit video requests.

## Architecture

Use a Generate-Review pipeline:

```text
intake -> content plan -> visual plan -> HyperFrames build -> overview QA -> user Edit/Aim review -> PDF/PPTX export
```

Use named subagents when the work is large enough to benefit from role separation:

- `topic_intake_router`: request and DESIGN markdown normalization
- `ppt_content_planner`: storyline and slide/card contract
- `ppt_visual_designer`: visual system and layout mapping
- `hyperframes_ppt_builder`: topic implementation
- `ppt_overview_qa`: overview and lint validation

## Implementation Plan

1. Read `AGENTS.md` and the relevant HyperFrames skill.
2. Find the matching `new_md/DESIGN-*.md` file.
3. Create or update `_workspace/topic_intake.md` for substantial work.
4. Write or update `_workspace/ppt_content_plan.md`.
5. Write or update `_workspace/ppt_visual_plan.md` when design choices are non-trivial.
6. Implement only allowed `data-skill` values for the selected output type.
7. Generate or update `topics/<topic-name>/overview.html` before any PDF/PPTX export.
8. Include `Edit` and `Aim` controls required by the overview edit workflow.
9. Apply user-provided overview patches to both `index.html` and `overview.html`.
10. Run topic validation and HyperFrames lint after HTML changes.

## Allowed Output Types

Deck:

- 1920x1080
- `title`, `title-bullets`, `title-image`, `title-tags`, `split`, `stat`, `steps`, `compare`, `evolution-flow`, `quote`, `kindergarten-notice`

Card-news:

- 1080x1080 by default
- `photo-cover`, `video-cover`, `stat`, `image-feature`

## QA Gates

Before reporting completion:

- topic folder contains `index.html`, `overview.html`, `meta.json`, and `hyperframes.json`
- topic folder contains `DESIGN.md`
- topic folder contains `exports/`
- `overview.html` includes `class="edit-btn"`
- `overview.html` includes Aim UI or `data-aim`
- all `data-skill` values are allowed for the selected output type
- lint was run or the reason it could not run is stated
- PDF/PPTX export was not run until the user finished overview review
- MP4 render was not run unless explicitly requested

See `references/ppt-checklist.md` for the detailed checklist.
