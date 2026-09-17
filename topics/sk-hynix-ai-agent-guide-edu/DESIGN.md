# DESIGN — AI Agent Guide 사내 교육 (Notion 최소 적용)

이 파일은 `new_md/DESIGN-Notion.md`를 이 topic에 고정 복사한 디자인 기준이다. 아래 "교육 자료 최소 적용 규칙"이 원문보다 우선한다. 원문은 마케팅 사이트 기준이므로 교육용 PDF에 필요한 부분만 가져온다.

## 교육 자료 최소 적용 규칙 (우선)

#> **final-touch 색 변경 (2026-09-17, 사용자 요청 12번)**: SK hynix 사내 교육의 빨강·주황·흰색 느낌에 맞추려고, `new_md/DESIGN-Notion.md` 안에 있는 색 중 Sticker Orange `#dd5b00`을 유일한 구조 액센트로, Deep Orange `#793400`을 반전 화면 배경과 경고 점 색으로 옮겼다. Notion 원문은 이 두 색을 장식용으로만 쓰지만, 이 topic에서는 파랑 1색 규칙을 '주황 1색 규칙'으로 치환해 같은 절제 원칙(구조 액센트 1개)을 지킨다. 원문에 빨강은 없어 쓰지 않았다.

## 토큰

| 토큰 | 값 | 용도 |
|---|---|---|
| `--canvas` | `#f6f5f4` | 슬라이드 배경 (Warm Paper) |
| `--surface` | `#ffffff` | 카드·패널 |
| `--hairline` | `#e6e6e6` | 1px 테두리·구분선 |
| `--ink` | `rgba(0,0,0,0.95)` | 제목·본문 |
| `--ink-2` | `#31302e` | 보조 본문 |
| `--ink-3` | `#615d59` | 캡션·출처·풋터 |
| `--accent` | `#dd5b00` | 유일한 구조 액센트. 강조 밑줄, 단계 번호, 현재 위치 표시 |
| `--accent-soft` | `rgba(221,91,0,0.08)` | 액센트 배경 틴트 |
| `--night` | `#793400` | 반전 화면 배경. S01 표지, G02 마무리, 구간 표지 D01–D07에만 |
| `--box-line` | `#8a857f` | 상자류 1px 테두리 (ROADMAP2, 2026-09-18). 캔버스 3.36:1 · 흰색 3.66:1 · 전환 틴트 3.29:1로 비텍스트 대비 3:1(WCAG 1.4.11)을 채운다. 표의 칸 선·코드 제목 밑선은 `--line-strong`까지만 |
| `--box-muted` | `#eeece9` | 낮춤 상자(`.dg-box.muted` 등)의 면. 캔버스와 같은 색이라 보이지 않던 것을 한 단계 내렸다 |
| `--on-night-line-strong` / `--on-night-fill` | 흰색 50% / 흰색 24% | 반전 배경 위 테두리(3.50:1)와 낮춤 면·지나온 정거장 채움 |
| `--ok` / `--warn` | `#1aae39` / `#dd5b00` | 비교 화면의 상태 점 전용. 글자·면 채우기 금지 |
| (전환 장면 배경) | `#fbf1ea` | 전환 장면(T01–T03)에만 쓰는 따뜻한 틴트 배경(주황 8%를 캔버스에 섞은 값). Notion의 '추천 요금제 틴트'처럼 면 채우기가 아닌 배경 틴트로 전환을 알린다. 제목 왼쪽 주황 막대와 함께 씀 |
| `--line-strong` | `#c8c4bf` | 점선 플레이스홀더·개념도 영역 테두리 (중립 파생값) |
| `--on-accent` / `--on-night` | `#ffffff` | 주황 면·짙은 주황 면 위 글자 |

### 타이포그래피

- 폰트 스택: `"Paperlogy", "Pretendard", "Malgun Gothic", "Inter", sans-serif`. Notion의 Inter 대신 한글 가독성을 위해 Paperlogy를 우선한다.
- 제목 700–800, 자간 음수(-1px 내외). 본문 400–500. 굵은 본문 금지.
- 1920×1080 기준 크기: 표지 제목 96–112px, 장면 제목 72–80px, 핵심 항목 40–48px, 보조 문장 32–36px, 출처·캡션 24–28px.

### 형태

- 모서리 12px 하나만 사용. 태그만 999px pill 허용.
- 그림자 없음. 면 구분은 1px 테두리와 흰 카드로만 한다. 상자류 테두리는 `--box-line`(배경 대비 3:1 이상)을 쓰고, 굵기는 중립 1px · 강조 2px 주황을 지킨다.
- 상자 안의 내용은 상하좌우 가운데 정렬이 기본이다(`.dg-box`, `.time-block`, 칩·태그). 목록형 카드(`.compare-col` 등)와 문장 상자(완료 조건·막히면)는 왼쪽 정렬을 유지하되 세로는 가운데로 둔다.
- 사진·썸네일은 네 모서리 모두 12px로 둥글린다(컨테이너가 아니라 그림 자체에).
- 여백은 8px 배수. 장면 안쪽 여백 상하 96px, 좌우 120px.

### 금지

- 스티커 팔레트(보라·분홍·주황·청록·초록·하늘)를 장식·면 채우기에 쓰지 않는다.
- 주황 외의 두 번째 구조 액센트를 만들지 않는다.
- 짙은 주황 반전 밴드를 S01·G02와 구간 표지 D01–D07 외 장면에 쓰지 않는다. 구간 표지는 주제(비유 축)가 바뀌는 지점을 표지처럼 알리는 장면이며 사용자 요청(2026-09-18)으로 예외가 됐다.
- 애니메이션·전환 효과를 쓰지 않는다. PDF에서 정지 상태 한 장으로 읽혀야 한다.
- 원문의 `#a39e98`(Ash)는 배경 대비가 약 2.4:1로 부족하므로 텍스트에 쓰지 않는다. 캡션은 `--ink-3`을 쓴다.

---

# 원문: new_md/DESIGN-Notion.md

## Overview

Notion looks like a well-organized desk in good daylight. The dominant surface is not pure white but a warm, paper-soft off-white — `{colors.canvas-soft}` (#f6f5f4) — that takes the clinical edge off the screen and makes long pages feel like a document rather than an app. Type is set in `NotionInter` (a tuned Inter) in near-black `{colors.ink}` at large, tightly-tracked weights, so headlines read as confident statements with very little letter-spacing slack at display sizes (`{typography.display-1}` pulls −2.125px of tracking at 64px). The whole system whispers in greys and blacks, then says exactly one thing in colour: a single, dependable blue, `{colors.primary}` (#0075de), reserved almost entirely for the primary call-to-action and inline links.

Against that quiet chrome, Notion lets a **playful multi-colour sticker palette** carry all of the brand's personality — purple, pink, orange, teal, green and sky-blue appear as small illustrated blocks, app-icon stickers, and category dots scattered through the marketing pages. These colours never structure the layout or paint a CTA; they decorate. The discipline is deliberate: the interface stays monochrome-plus-blue so the content (and the cheerful illustrations) can breathe. The one exception to the bright daylight is the homepage hero, which inverts into a deep indigo "night" band (`{colors.secondary}`) with white type and glowing sticker constellations — a single dark island in an otherwise light document.

Surfaces are defined by hairlines and the faintest layered shadows rather than heavy elevation. Cards round at a friendly 12px (`{rounded.lg}`), the marketing CTAs are fully-pill-shaped (`{rounded.full}`), and utility buttons round at a tighter 8px (`{rounded.md}`). Nothing is loud; the brand's character comes from restraint plus one well-placed splash of joy.

**Key Characteristics:**
- Warm paper-soft canvas `{colors.canvas-soft}` over pure white, never clinical
- Near-black `{colors.ink}` `NotionInter` type with tight negative tracking at display sizes (`{typography.display-1}`)
- Exactly one structural accent — Notion blue `{colors.primary}` — reserved for CTAs and links
- A decorative-only multi-colour sticker palette (`{colors.accent-purple}`, `{colors.accent-pink}`, `{colors.accent-orange}`, `{colors.accent-teal}`, `{colors.accent-green}`, `{colors.accent-sky}`) that adds personality without ever painting structure
- Pill-shaped marketing CTAs (`{rounded.full}`) contrasted with 8px utility buttons (`{rounded.md}`)
- Elevation by hairline + barely-there layered shadow, not heavy drop-shadows
- A single dark indigo hero "night" band (`{colors.secondary}`) inverting the otherwise daylight page rhythm

## Colors

> Source pages analysed: the Notion home page plus Pricing, Enterprise, Product (AI), Product (Agents), and Startups. Every secondary page resolved to the same core palette — Notion runs one tightly-scoped system across the marketing site.

### Brand & Accent
- **Notion Blue** (`{colors.primary}` — #0075de): the single structural accent. Primary CTA fill ("Get Notion free"), inline link colour, active-tab and focus signal. This is the only colour that ever paints an action.
- **Pressed Blue** (`{colors.primary-active}` — #005bab): the darker press state of the primary CTA.
- **Deep Indigo** (`{colors.secondary}` — #213183): the dark hero "night" band background and its sticker-constellation field; a deep brand-blue used for full-bleed inverted sections.

The remaining colours form Notion's **decorative sticker palette** — they appear only as illustrated blocks, app stickers and category dots, never as CTAs or structural fills:
- **Sticker Sky** (`{colors.accent-sky}` — #62aef0)
- **Sticker Purple** (`{colors.accent-purple}` — #d6b6f6) / **Deep Purple** (`{colors.accent-purple-deep}` — #391c57)
- **Sticker Pink** (`{colors.accent-pink}` — #ff64c8)
- **Sticker Orange** (`{colors.accent-orange}` — #dd5b00) / **Deep Orange** (`{colors.accent-orange-deep}` — #793400)
- **Sticker Teal** (`{colors.accent-teal}` — #2a9d99)
- **Sticker Green** (`{colors.accent-green}` — #1aae39)
- **Sticker Brown** (`{colors.accent-brown}` — #523410)

### Surface
- **White** (`{colors.canvas}` / `{colors.surface}` — #ffffff): card and panel surfaces, nav bar, form fields.
- **Warm Paper** (`{colors.canvas-soft}` — #f6f5f4): the signature page canvas and the footer band — a warm off-white that gives the whole site its document-like calm.
- **Hairline** (`{colors.hairline}` — #e6e6e6): 1px card borders and dividers, a black-at-10%-on-white blend kept solid for token reuse.

### Text
- **Ink** (`{colors.ink}` — #000000): primary headings and body text (rendered at ~95% alpha for a soft true-black).
- **Warm Charcoal** (`{colors.ink-secondary}` — #31302e): secondary body copy and footer text.
- **Stone** (`{colors.ink-muted}` — #615d59): supporting / muted copy.
- **Ash** (`{colors.ink-faint}` — #a39e98): captions, metadata, placeholder text.

### Semantic
Notion's marketing surfaces do not expose a dedicated error/success palette in the system chrome — status is carried by the sticker palette (e.g. `{colors.accent-green}` for affirmative ticks) rather than a separate semantic ramp.

## Typography

### Font Family
The entire system is set in **`NotionInter`** — Notion's tuned cut of Inter — with a fallback stack of `Inter, -apple-system, system-ui, "Segoe UI", Helvetica, Arial`. A single family carries everything from 64px display headlines to 12px eyebrows; there is no serif, no monospace display face. OpenType `lnum` (lining numerals) and `locl` features are enabled on body and heading roles.

### Hierarchy

| Token | Size | Weight | Line Height | Letter Spacing | Use |
|---|---|---|---|---|---|
| `{typography.display-1}` | 64px | 700 | 1.0 | −2.125px | Hero headline ("Meet the night shift") |
| `{typography.display-2}` | 54px | 700 | 1.04 | −1.875px | Large section headlines |
| `{typography.heading-1}` | 40px | 700 | 1.1 | −1px | Section headlines ("Plans and features") |
| `{typography.heading-2}` | 26px | 700 | 1.23 | −0.625px | Sub-section headings |
| `{typography.heading-3}` | 22px | 700 | 1.27 | −0.25px | Card titles |
| `{typography.title}` | 20px | 600 | 1.4 | −0.125px | Feature titles, callouts |
| `{typography.body-md}` | 16px | 400 | 1.5 | 0 | Default body copy |
| `{typography.body-sm}` | 15px | 400 | 1.33 | 0 | Dense body, table rows, nav |
| `{typography.button}` | 16px | 500 | 1.5 | 0 | Button labels |
| `{typography.caption}` | 14px | 400 | 1.43 | 0 | Captions, footnotes |
| `{typography.eyebrow}` | 12px | 600 | 1.33 | +0.125px | Pill badges, small labels |

### Principles
Notion's type voice is **tight, heavy, and quiet-confident**. Headlines lean on weight 700 and aggressive negative tracking (more negative the larger the size) so display copy feels set, not stretched. Body copy stays at a comfortable 1.5 line-height for document readability. The contrast between a heavy 700 headline and a calm 400 body is the primary expressive lever — there is no decorative typography, only a clear hierarchy.

### Note on Font Substitutes
`NotionInter` is a proprietary tuning of the open-source **Inter** family — substitute Inter directly. To approximate Notion's display tightness, apply the negative letter-spacing values in the table above explicitly (Inter at default tracking will read looser than `NotionInter`).

## Layout

### Spacing System
- **Base unit**: 8px.
- **Tokens (front matter)**: `{spacing.xxs}` 4px · `{spacing.xs}` 8px · `{spacing.sm}` 12px · `{spacing.md}` 16px · `{spacing.lg}` 24px · `{spacing.xl}` 28px · `{spacing.xxl}` 32px.
- Card interior padding lands around `{spacing.lg}` (24px); utility buttons use a tight 4px/14px; form fields pad at `{spacing.xxs}`-scale 6px. Section gaps stack the larger steps.

### Grid & Container
Content is centred in a wide max-width column (~1080–1300px on desktop per the extracted breakpoints) with generous outer gutters. Feature sections alternate between full-width text blocks and 2-up / 3-up card grids; the pricing page widens to a 4-column plan table. The dark hero spans full-bleed edge to edge while body sections respect the centred container.

### Whitespace Philosophy
Whitespace is the primary grouping device. Sections are separated by large vertical gaps rather than rules, and cards sit on the warm canvas with quiet hairlines instead of heavy frames. The effect is document-like: airy, scannable, and never crowded.

### Responsive Strategy

#### Breakpoints
| Name | Width | Key Changes |
|---|---|---|
| Wide | 1440px+ | Full multi-column grids, widest container |
| Desktop | 1080–1300px | Standard centred container, 3-up card grids |
| Tablet | 768–840px | Grids collapse to 2-up, nav begins condensing |
| Mobile | ≤600px | Single-column stacks, hamburger nav, full-width CTAs |

#### Touch Targets
Pill CTAs (`button-primary`, `button-secondary`) and utility buttons (`button-utility`) carry comfortable tap padding; aim for a 44×44px minimum hit area on mobile by preserving vertical padding even as labels shrink.

#### Collapsing Strategy
The top nav condenses to a hamburger below the tablet breakpoint; multi-column card grids collapse to a single stacked column; the pricing plan table reflows from 4 side-by-side columns into stacked plan cards. Section padding tightens but the warm-canvas rhythm is preserved.

#### Image Behavior
Product screenshots and illustration tiles sit inside rounded `{rounded.lg}` frames and scale fluidly within their grid cell. Sticker illustrations are small fixed-scale decorative assets that re-flow but do not crop.

## Elevation & Depth

| Level | Treatment | Use |
|---|---|---|
| 0 — Flat | Hairline border `{colors.hairline}`, no shadow | Default cards on the warm canvas |
| 1 — Soft | Layered micro-shadow: `rgba(0,0,0,0.01) 0 0.175px 1.041px`, `0.02 0 0.8px 2.925px`, `0.027 0 2.025px 7.847px`, `0.04 0 4px 18px` | Raised feature cards, floating buttons |
| 2 — Elevated | Deeper 5-stop stack ending in `rgba(0,0,0,0.05) 0 23px 52px` | Modals, popovers, the elevated white pill on the dark hero |

Notion's elevation philosophy is **barely-there**: shadows are built from many near-transparent layers so surfaces feel gently lifted off the paper rather than dramatically dropped. Most cards rely on a hairline alone.

### Decorative Depth
The brand's real depth cue is **illustration**, not shadow. The dark indigo hero (`{colors.secondary}`) uses glowing sticker stickers and a starfield to create a sense of a lit night scene, and feature sections layer small colourful app-icon stickers over plain surfaces to add playful dimensionality. Colour-blocked illustration tiles (purple, pink, orange, teal headers on otherwise-white cards) provide visual rhythm.

## Shapes

### Border Radius Scale

| Token | Value | Use |
|---|---|---|
| `{rounded.xs}` | 4px | Form fields, small tags, inline chips |
| `{rounded.sm}` | 5px | Menu items, list rows, status pills |
| `{rounded.md}` | 8px | Utility / nav buttons, smaller cards |
| `{rounded.lg}` | 12px | Feature cards, illustration frames, content tiles |
| `{rounded.xl}` | 16px | Large containers, image wells |
| `{rounded.full}` | 9999px | Marketing pill CTAs, badges, circular icon buttons |

### Photography Geometry
Product screenshots are framed in rounded `{rounded.lg}` / `{rounded.xl}` wells, typically full-bleed within their container with a hairline edge. Illustration tiles use colour-blocked header bands above white card bodies. Avatars and app-icon stickers are small, sometimes fully circular (`{rounded.full}`). There is no heavy art-direction crop — images scale within their rounded frame.

## Components

> **No hover states documented.** Every spec below documents Default and Active/Pressed states only. Variants live as separate `components:` front-matter entries and are described in their own sub-blocks.

### Navigation

**`nav-bar`** — Top navigation
- White surface `{colors.canvas}`, `{colors.ink}` link text at `{typography.body-sm}`, padding `{spacing.md}`. Sits as a slim sticky bar; left wordmark, centre product/solutions menu links, right "Log in" text link plus a `button-utility` "Get Notion free" CTA. Condenses to a hamburger below the tablet breakpoint.

### Buttons

**`button-primary`** — Primary CTA ("Get Notion free")
- Background `{colors.primary}`, text `{colors.on-primary}`, type `{typography.button}`, fully pill-shaped `{rounded.full}`. The single blue action on any page.
- Pressed state lives in `button-primary-pressed` (background `{colors.primary-active}`); marketing buttons also apply a brief `scale(0.9)` press transform.

**`button-primary-pressed`**
- Background `{colors.primary-active}`, text `{colors.on-primary}` — the depressed state of the primary CTA.

**`button-secondary`** — Secondary CTA ("Request a demo")
- White surface `{colors.surface}`, text `{colors.ink}`, type `{typography.button}`, pill `{rounded.full}`, carried by the soft Level-1 shadow. Pairs beside `button-primary` in the hero.

**`button-utility`** — Nav / plan-select button
- White surface `{colors.surface}`, text `{colors.ink}`, type `{typography.button}`, tighter `{rounded.md}` (8px), padding `4px 14px`, 1px `{colors.hairline}` border. Used for the nav CTA and pricing plan-select buttons where the marketing pill would be too large.

**`button-icon-circular`** — Carousel / media control
- Circular `{rounded.full}` control with a translucent `rgba(0,0,0,0.05)` fill and `{colors.on-primary}` glyph, used for slide and play/pause controls; applies a `scale(0.9)` press transform.

### Cards & Containers

**`feature-card`** — Content / feature card
- White surface `{colors.surface}`, `{colors.ink}` text, `{typography.body-md}`, rounded `{rounded.lg}` (12px), padding `{spacing.lg}` (24px). The workhorse marketing card; often topped by a colour-blocked illustration band from the sticker palette. Default elevation is flat (hairline only).

**`feature-card-elevated`** — Raised feature card
- Same chrome as `feature-card` with the soft Level-1 layered shadow for cards that float above the canvas (testimonials, floating product panels).

**`pricing-plan-card`** — Pricing plan column
- White surface `{colors.surface}`, `{colors.ink}` text, `{typography.body-sm}`, rounded `{rounded.md}` (8px), padding `{spacing.lg}`. A bordered column listing a plan's price and feature checklist, with a `button-utility` select action.

**`pricing-plan-card-featured`** — Highlighted plan column
- Warm `{colors.canvas-soft}` fill to lift the recommended tier off the white siblings, same `{rounded.md}` shape and padding. Distinguished by surface tint rather than a coloured border.

### Inputs & Forms

**`text-input`** — Text / number field
- White surface `{colors.surface}`, `{colors.ink}` text, `{typography.body-sm}`, 1px `rgb(221,221,221)` border, rounded `{rounded.xs}` (4px), padding `6px`. Square-ish corners deliberately tighter than the pill CTAs. Focus adds the soft Level-1 shadow.

### Signature Components

**`hero-band`** — Dark "night" hero
- Full-bleed deep indigo `{colors.secondary}` band carrying `{typography.display-1}` white headline, sticker-constellation field, and a `button-primary` + `button-secondary` CTA pair. The single inverted dark island in an otherwise daylight page.

**`badge-pill`** — Eyebrow / category pill
- White surface `{colors.surface}`, `{colors.primary}` text, `{typography.eyebrow}` (12px / 600), fully pill `{rounded.full}`, padding `4px 8px`. Small labels such as the pricing "Essential for staying organized" eyebrow and category tags.

**`footer`** — Site footer
- Warm `{colors.canvas-soft}` band, `{colors.ink-secondary}` link text at `{typography.caption}`, padding `{spacing.xxl}`. Multi-column link directory closing every page.

### Examples (illustrative)

> Kit-mirror demonstration surfaces. Each `ex-*` entry references brand-native primitives so downstream consumers (`/preview-design`, `/generate-kit`) re-skin the same 10 surfaces consistently.

**`ex-pricing-tier`** — Default Pricing tier card. Re-uses feature-card chrome with brand canvas-soft surface.
- Properties: `backgroundColor`, `textColor`, `borderColor`, `rounded`, `padding`

**`ex-pricing-tier-featured`** — Featured/highlighted tier — polarity-flipped surface (dark fill + light text in light mode, light fill + dark text in dark mode).
- Properties: `backgroundColor`, `textColor`, `rounded`, `padding`

**`ex-product-selector`** — What's Included summary card — re-purposed for SaaS / B2B verticals (NOT a literal product gallery).
- Properties: `backgroundColor`, `rounded`, `padding`

**`ex-cart-drawer`** — Subscription summary — re-purposed for SaaS / B2B (line items per add-on, not literal cart).
- Properties: `backgroundColor`, `rounded`, `padding`, `item-divider`

**`ex-app-shell-row`** — Sidebar nav row inside the App Shell example. Active state uses brand primary as the indicator.
- Properties: `backgroundColor`, `activeIndicator`, `rounded`, `padding`

**`ex-data-table-cell`** — Default data-table th + td chrome. Header uses mono-caps eyebrow typography; body uses body-sm.
- Properties: `headerBackground`, `headerTypography`, `bodyTypography`, `cellPadding`, `rowBorder`

**`ex-auth-form-card`** — Sign-in / sign-up card. Re-uses feature-card chrome with text-input primitives inside.
- Properties: `backgroundColor`, `rounded`, `padding`

**`ex-modal-card`** — Modal dialog surface — same chrome as feature-card with elevated shadow.
- Properties: `backgroundColor`, `rounded`, `padding`

**`ex-empty-state-card`** — Empty-state illustration frame.
- Properties: `backgroundColor`, `rounded`, `padding`, `captionTypography`

**`ex-toast`** — Toast notification surface — feature-card shape + medium shadow.
- Properties: `backgroundColor`, `rounded`, `padding`, `typography`


## Do's and Don'ts

### Do
- Reserve `{colors.primary}` for the primary action, inline links, and the active/focus signal — nothing decorative.
- Keep the page on the warm `{colors.canvas-soft}` canvas; use pure white `{colors.surface}` for cards and fields to create gentle figure/ground.
- Let the sticker palette (`{colors.accent-pink}`, `{colors.accent-teal}`, `{colors.accent-orange}`, …) live only in illustrations, icon tiles and category dots.
- Set headlines in heavy `{typography.display-1}`/`{typography.heading-1}` with their negative tracking applied explicitly.
- Use pill `{rounded.full}` for marketing CTAs and tighter `{rounded.md}` for nav/utility buttons — the contrast is intentional.
- Define surfaces with `{colors.hairline}` and the barely-there Level-1 shadow rather than heavy drop-shadows.
- Reserve the deep indigo `{colors.secondary}` "night" treatment for a single hero moment, not repeated bands.

### Don't
- Don't paint a CTA or structural fill in any sticker-palette colour — those are decoration only.
- Don't introduce a second structural accent alongside `{colors.primary}`.
- Don't put pill `{rounded.full}` radii on form fields — inputs stay tight at `{rounded.xs}` (4px).
- Don't drop heavy shadows; Notion's elevation is many near-transparent layers, never a hard cast.
- Don't set body copy in a heavy weight — keep 400 for readability and let weight 700 belong to headlines.
- Don't place type on pure clinical white for full pages; the warm `{colors.canvas-soft}` is core to the brand calm.
