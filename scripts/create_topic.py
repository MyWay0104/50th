from __future__ import annotations

import argparse
import json
import logging
import shutil
import sys
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
NEW_MD_DIR = ROOT / "new_md"
TOPICS_DIR = ROOT / "topics"
DEFAULT_DURATION_SECONDS = 15

logging.basicConfig(level=logging.INFO, format="%(message)s")
logger = logging.getLogger(__name__)


@dataclass(frozen=True)
class TopicConfig:
    name: str
    title: str
    company: str
    output_type: str
    design_path: Path
    target_dir: Path


def _slug(value: str) -> str:
    normalized = value.strip().lower().replace(" ", "-").replace("_", "-")
    return "".join(char for char in normalized if char.isalnum() or char == "-").strip("-")


def _find_design(company: str, explicit_path: str | None) -> Path:
    if explicit_path:
        path = Path(explicit_path)
        if not path.is_absolute():
            path = ROOT / path
        if not path.exists():
            raise FileNotFoundError(f"Design markdown not found: {path}")
        return path

    candidates = sorted(NEW_MD_DIR.glob("DESIGN-*.md"))
    if not candidates:
        raise FileNotFoundError("No DESIGN markdown found under new_md/DESIGN-*.md")

    company_key = company.lower().replace(" ", "")
    for candidate in candidates:
        if company_key and company_key in candidate.stem.lower().replace(" ", ""):
            return candidate
    return candidates[0]


def _copy_root_config(target_dir: Path) -> None:
    for filename in ("hyperframes.json", "meta.json"):
        source = ROOT / filename
        if source.exists():
            shutil.copy2(source, target_dir / filename)


def _write_json(path: Path, payload: dict[str, object]) -> None:
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def _write_brief(config: TopicConfig) -> None:
    content = f"""# {config.title}

## 문제 분석

- 출력 타입: `{config.output_type}`
- 회사/브랜드: `{config.company}`
- 디자인 원본: `{config.design_path}`
- topic 경로: `{config.target_dir}`

## 설계

이 topic은 `2_slide_master` 방식의 HyperFrames 구성과 v2 harness workflow를 따른다.

## 구현

- `index.html`: HyperFrames composition
- `overview.html`: 사용자 검토 및 Edit/Aim 수정 화면
- `DESIGN.md`: topic에 고정된 디자인 기준 문서
- `exports/`: 최종 PDF/PPTX 발표자료 파일 위치

## 코드

```powershell
python scripts\\validate_topic.py topics\\{config.name}
npx hyperframes lint topics\\{config.name}
```

## 테스트 방법

1. `overview.html`을 브라우저 또는 preview 서버에서 확인한다.
2. `Edit`를 누르고 수정한다.
3. `Aim`을 선택한다.
4. `Done`을 눌러 patch를 클립보드로 복사한다.
5. Codex가 patch를 반영한 뒤 다시 overview를 확인한다.
6. 최종 확인 후 PDF 또는 PPTX export를 요청한다.

## 향후 개선사항

- 실제 발표 내용과 자료를 반영해 slide/card copy를 확정한다.
- 필요한 이미지와 도표 asset을 `assets/`에 추가한다.
"""
    (config.target_dir / "BRIEF.md").write_text(content, encoding="utf-8")


def _deck_index(title: str, company: str) -> str:
    return f"""<!doctype html>
<html lang="ko">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>{title}</title>
    <link rel="preconnect" href="https://cdn.jsdelivr.net" />
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/fonts-archive/Paperlogy/subsets/Paperlogy-dynamic-subset.css" />
    <style>
      @font-face {{
        font-family: "Paperlogy";
        font-weight: 400;
        font-style: normal;
        font-display: swap;
        src: url("https://cdn.jsdelivr.net/gh/fonts-archive/Paperlogy/Paperlogy-4Regular.woff2") format("woff2");
      }}
      @font-face {{
        font-family: "Paperlogy";
        font-weight: 800;
        font-style: normal;
        font-display: swap;
        src: url("https://cdn.jsdelivr.net/gh/fonts-archive/Paperlogy/Paperlogy-8ExtraBold.woff2") format("woff2");
      }}
      @font-face {{
        font-family: "Paperlogy";
        font-weight: 900;
        font-style: normal;
        font-display: swap;
        src: url("https://cdn.jsdelivr.net/gh/fonts-archive/Paperlogy/Paperlogy-9Black.woff2") format("woff2");
      }}
      * {{ box-sizing: border-box; }}
      html, body {{
        width: 100%;
        height: 100%;
        margin: 0;
        overflow: hidden;
        background: #111827;
        font-family: "Paperlogy", "Inter", "Helvetica Neue", Arial, sans-serif;
      }}
      #root {{
        position: relative;
        width: 1920px;
        height: 1080px;
        overflow: hidden;
        background: #f8fafc;
        color: #111827;
      }}
      .scene {{
        position: absolute;
        inset: 0;
        display: flex;
        flex-direction: column;
        justify-content: center;
        padding: 88px 112px;
        overflow: hidden;
      }}
      .hero {{
        background: linear-gradient(135deg, #0f172a 0%, #172554 52%, #f8fafc 52%, #f8fafc 100%);
        color: #ffffff;
      }}
      .light {{ background: #f8fafc; color: #111827; }}
      .accent {{ color: #2563eb; }}
      .eyebrow {{
        margin: 0 0 26px;
        color: inherit;
        font-size: 24px;
        font-weight: 800;
        opacity: 0.78;
      }}
      h1, h2 {{
        max-width: 1120px;
        margin: 0;
        font-size: 84px;
        line-height: 1.08;
        letter-spacing: 0;
      }}
      p {{
        max-width: 960px;
        margin: 28px 0 0;
        color: inherit;
        font-size: 30px;
        line-height: 1.45;
        opacity: 0.78;
      }}
      .grid {{
        display: grid;
        grid-template-columns: repeat(3, minmax(0, 1fr));
        gap: 22px;
        margin-top: 48px;
      }}
      .card {{
        min-height: 238px;
        padding: 34px;
        border: 1px solid #d9e2ef;
        border-radius: 8px;
        background: #ffffff;
      }}
      .card h3 {{
        margin: 0 0 14px;
        font-size: 34px;
        line-height: 1.22;
      }}
      .card p {{
        margin: 0;
        font-size: 23px;
        color: #475569;
      }}
      .brand, .slide-num {{
        position: absolute;
        bottom: 52px;
        font-size: 18px;
        font-weight: 800;
        opacity: 0.72;
      }}
      .brand {{ left: 112px; }}
      .slide-num {{ right: 112px; }}
    </style>
  </head>
  <body>
    <div id="root" data-output-type="deck" data-composition-id="main" data-start="0" data-duration="{DEFAULT_DURATION_SECONDS}" data-width="1920" data-height="1080">
      <section id="s1" class="scene clip hero" data-skill="title" data-start="0" data-duration="5" data-track-index="0">
        <div class="eyebrow">{company} | 16:9 HyperFrames Deck</div>
        <h1>{title}</h1>
        <p>DESIGN.md를 기반으로 발표 목적, 청중, 메시지를 반영해 완성할 첫 슬라이드입니다.</p>
        <div class="brand">{company}</div>
        <div class="slide-num">01 / 03</div>
      </section>
      <section id="s2" class="scene clip light" data-skill="title-bullets" data-start="5" data-duration="5" data-track-index="0">
        <div class="eyebrow accent">핵심 메시지</div>
        <h2>주제의 맥락, 변화, 실행 포인트를 한 흐름으로 정리합니다.</h2>
        <div class="grid">
          <article class="card"><h3>맥락</h3><p>청중이 왜 지금 이 내용을 들어야 하는지 설명합니다.</p></article>
          <article class="card"><h3>변화</h3><p>기술, 시장, 조직 관점의 핵심 변화를 요약합니다.</p></article>
          <article class="card"><h3>실행</h3><p>발표 이후 바로 논의할 결정을 제시합니다.</p></article>
        </div>
        <div class="brand">{company}</div>
        <div class="slide-num">02 / 03</div>
      </section>
      <section id="s3" class="scene clip hero" data-skill="quote" data-start="10" data-duration="5" data-track-index="0">
        <div class="eyebrow">정리</div>
        <h2>좋은 발표는 정보보다 판단 기준을 남깁니다.</h2>
        <p>사용자 피드백을 반영해 이 문장을 topic의 결론으로 교체하세요.</p>
        <div class="brand">{company}</div>
        <div class="slide-num">03 / 03</div>
      </section>
    </div>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/gsap.min.js"></script>
    <script>
      window.__timelines = window.__timelines || {{}};
      const tl = gsap.timeline({{ paused: true, defaults: {{ ease: "power2.out" }} }});
      document.querySelectorAll(".scene").forEach((scene) => {{
        const start = Number(scene.dataset.start || 0);
        tl.fromTo(`#${{scene.id}} .eyebrow, #${{scene.id}} h1, #${{scene.id}} h2, #${{scene.id}} p, #${{scene.id}} .card`, {{ autoAlpha: 0, y: 28 }}, {{ autoAlpha: 1, y: 0, duration: 0.8, stagger: 0.06 }}, start + 0.25);
      }});
      window.__timelines.main = tl;
    </script>
  </body>
</html>
"""


def _card_index(title: str, company: str) -> str:
    return f"""<!doctype html>
<html lang="ko">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>{title}</title>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/fonts-archive/Paperlogy/subsets/Paperlogy-dynamic-subset.css" />
    <style>
      @font-face {{
        font-family: "Paperlogy";
        font-weight: 400;
        font-style: normal;
        font-display: swap;
        src: url("https://cdn.jsdelivr.net/gh/fonts-archive/Paperlogy/Paperlogy-4Regular.woff2") format("woff2");
      }}
      @font-face {{
        font-family: "Paperlogy";
        font-weight: 800;
        font-style: normal;
        font-display: swap;
        src: url("https://cdn.jsdelivr.net/gh/fonts-archive/Paperlogy/Paperlogy-8ExtraBold.woff2") format("woff2");
      }}
      @font-face {{
        font-family: "Paperlogy";
        font-weight: 900;
        font-style: normal;
        font-display: swap;
        src: url("https://cdn.jsdelivr.net/gh/fonts-archive/Paperlogy/Paperlogy-9Black.woff2") format("woff2");
      }}
      * {{ box-sizing: border-box; }}
      html, body {{
        width: 100%;
        height: 100%;
        margin: 0;
        overflow: hidden;
        background: #0f172a;
        font-family: "Paperlogy", "Inter", "Helvetica Neue", Arial, sans-serif;
      }}
      #root {{
        position: relative;
        width: 1080px;
        height: 1080px;
        overflow: hidden;
        background: #f8fafc;
        color: #111827;
      }}
      .card-scene {{
        position: absolute;
        inset: 0;
        display: flex;
        flex-direction: column;
        justify-content: space-between;
        padding: 72px;
        overflow: hidden;
      }}
      .cover {{
        background: linear-gradient(160deg, #0f172a, #1d4ed8 62%, #f8fafc 62%);
        color: #ffffff;
      }}
      .stat-scene {{ background: #f8fafc; color: #111827; }}
      .label {{
        width: fit-content;
        border: 1px solid currentColor;
        border-radius: 999px;
        padding: 10px 18px;
        font-size: 24px;
        font-weight: 900;
      }}
      h1, h2 {{
        margin: 0;
        font-size: 74px;
        line-height: 1.08;
        letter-spacing: 0;
      }}
      p {{
        margin: 22px 0 0;
        color: inherit;
        font-size: 30px;
        line-height: 1.42;
        opacity: 0.78;
      }}
      .stat {{
        color: #2563eb;
        font-size: 146px;
        line-height: 1;
        font-weight: 900;
      }}
      .brand {{
        font-size: 22px;
        font-weight: 900;
        opacity: 0.74;
      }}
    </style>
  </head>
  <body>
    <div id="root" data-output-type="card-news" data-composition-id="main" data-start="0" data-duration="{DEFAULT_DURATION_SECONDS}" data-width="1080" data-height="1080">
      <section id="c1" class="card-scene clip cover" data-skill="photo-cover" data-start="0" data-duration="5" data-track-index="0">
        <div class="label">{company}</div>
        <div><h1>{title}</h1><p>DESIGN.md를 기준으로 카드뉴스의 첫 장 메시지를 완성하세요.</p></div>
        <div class="brand">01 / 03</div>
      </section>
      <section id="c2" class="card-scene clip stat-scene" data-skill="stat" data-start="5" data-duration="5" data-track-index="0">
        <div class="label">핵심 수치</div>
        <div><div class="stat">3</div><h2>핵심 포인트를 세 가지로 압축합니다.</h2><p>근거가 있는 숫자와 짧은 해석을 함께 제시합니다.</p></div>
        <div class="brand">{company} | 02 / 03</div>
      </section>
      <section id="c3" class="card-scene clip cover" data-skill="image-feature" data-start="10" data-duration="5" data-track-index="0">
        <div class="label">정리</div>
        <div><h2>독자가 저장하고 싶은 결론을 남깁니다.</h2><p>행동 제안 또는 다음 질문으로 마무리합니다.</p></div>
        <div class="brand">{company} | 03 / 03</div>
      </section>
    </div>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/gsap.min.js"></script>
    <script>
      window.__timelines = window.__timelines || {{}};
      const tl = gsap.timeline({{ paused: true, defaults: {{ ease: "power2.out" }} }});
      document.querySelectorAll(".card-scene").forEach((scene) => {{
        const start = Number(scene.dataset.start || 0);
        tl.fromTo(`#${{scene.id}} .label, #${{scene.id}} h1, #${{scene.id}} h2, #${{scene.id}} p, #${{scene.id}} .stat`, {{ autoAlpha: 0, y: 24 }}, {{ autoAlpha: 1, y: 0, duration: 0.75, stagger: 0.06 }}, start + 0.25);
      }});
      window.__timelines.main = tl;
    </script>
  </body>
</html>
"""


def _overview(title: str, company: str, output_type: str) -> str:
    items = [
        ("01", "title" if output_type == "deck" else "photo-cover", title, "도입 메시지를 수정하세요."),
        ("02", "title-bullets" if output_type == "deck" else "stat", "핵심 메시지", "근거와 구조를 수정하세요."),
        ("03", "quote" if output_type == "deck" else "image-feature", "정리", "결론과 행동 제안을 수정하세요."),
    ]
    cards = "\n".join(
        f"""        <article class="slide-card" data-slide="{number}" data-skill="{skill}" data-aim="message">
          <div class="slide-label"><span>{number} / {skill}</span><select class="aim-select" aria-label="Aim"><option>message</option><option>layout</option><option>tone</option><option>visual</option></select></div>
          <div class="stage">
            <h2 data-editable="true">{heading}</h2>
            <p data-editable="true">{body}</p>
          </div>
        </article>"""
        for number, skill, heading, body in items
    )
    return f"""<!doctype html>
<html lang="ko">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>{title} Overview</title>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/fonts-archive/Paperlogy/subsets/Paperlogy-dynamic-subset.css" />
    <style>
      @font-face {{
        font-family: "Paperlogy";
        font-weight: 400;
        font-style: normal;
        font-display: swap;
        src: url("https://cdn.jsdelivr.net/gh/fonts-archive/Paperlogy/Paperlogy-4Regular.woff2") format("woff2");
      }}
      @font-face {{
        font-family: "Paperlogy";
        font-weight: 800;
        font-style: normal;
        font-display: swap;
        src: url("https://cdn.jsdelivr.net/gh/fonts-archive/Paperlogy/Paperlogy-8ExtraBold.woff2") format("woff2");
      }}
      @font-face {{
        font-family: "Paperlogy";
        font-weight: 900;
        font-style: normal;
        font-display: swap;
        src: url("https://cdn.jsdelivr.net/gh/fonts-archive/Paperlogy/Paperlogy-9Black.woff2") format("woff2");
      }}
      * {{ box-sizing: border-box; }}
      body {{
        margin: 0;
        background: #eef2f7;
        color: #111827;
        font-family: "Paperlogy", "Inter", "Helvetica Neue", Arial, sans-serif;
      }}
      .topbar {{
        position: sticky;
        top: 0;
        z-index: 10;
        display: flex;
        align-items: center;
        justify-content: space-between;
        min-height: 64px;
        padding: 0 28px;
        border-bottom: 1px solid #d9e2ef;
        background: rgba(255, 255, 255, 0.94);
        backdrop-filter: blur(12px);
      }}
      .brand {{ font-size: 16px; font-weight: 900; }}
      .actions {{ display: flex; align-items: center; gap: 10px; }}
      .edit-btn {{
        border: 1px solid #b7c3d6;
        border-radius: 8px;
        padding: 8px 12px;
        background: #ffffff;
        color: #111827;
        font: inherit;
        font-weight: 900;
        cursor: pointer;
      }}
      main {{
        display: grid;
        grid-template-columns: 280px minmax(0, 1fr);
        min-height: calc(100vh - 64px);
      }}
      .strip {{
        position: sticky;
        top: 64px;
        height: calc(100vh - 64px);
        overflow: auto;
        padding: 18px;
        border-right: 1px solid #d9e2ef;
        background: #f8fafc;
      }}
      .thumb {{
        display: block;
        margin-bottom: 14px;
        padding: 12px;
        border: 1px solid #d9e2ef;
        border-radius: 8px;
        background: #ffffff;
        color: inherit;
        text-decoration: none;
      }}
      .thumb-title {{ margin: 0 0 6px; font-size: 14px; font-weight: 900; }}
      .thumb-meta {{ color: #64748b; font-size: 12px; font-weight: 800; }}
      .detail {{ display: grid; gap: 28px; padding: 34px; }}
      .slide-card {{
        border: 1px solid #d9e2ef;
        border-radius: 8px;
        background: #ffffff;
        box-shadow: rgba(15, 23, 42, 0.08) 0 16px 34px -20px;
      }}
      .slide-label {{
        display: flex;
        align-items: center;
        justify-content: space-between;
        padding: 14px 18px;
        border-bottom: 1px solid #d9e2ef;
        color: #475569;
        font-size: 13px;
        font-weight: 900;
      }}
      .aim-select {{
        border: 1px solid #b7c3d6;
        border-radius: 8px;
        padding: 7px 10px;
        background: #ffffff;
        font: inherit;
      }}
      .stage {{
        aspect-ratio: {"16 / 9" if output_type == "deck" else "1 / 1"};
        overflow: hidden;
        padding: 48px;
      }}
      .stage h2 {{ margin: 0; font-size: 44px; line-height: 1.15; }}
      .stage p {{ margin: 18px 0 0; color: #475569; font-size: 22px; line-height: 1.45; }}
      .editing [data-editable="true"] {{ outline: 2px dashed #2563eb; outline-offset: 4px; }}
      .toast {{
        position: fixed;
        right: 24px;
        bottom: 24px;
        display: none;
        max-width: 440px;
        padding: 14px 16px;
        border-radius: 8px;
        background: #111827;
        color: #ffffff;
        font-size: 14px;
        line-height: 1.4;
      }}
      .toast.show {{ display: block; }}
    </style>
  </head>
  <body>
    <header class="topbar">
      <div class="brand">{company} | {title} | {output_type}</div>
      <div class="actions">
        <span>Aim</span>
        <button class="edit-btn" id="nav-edit" type="button">Edit</button>
      </div>
    </header>
    <main>
      <nav class="strip" aria-label="slide thumbnails">
        <a class="thumb" href="#slide-01"><p class="thumb-title">01. 도입</p><div class="thumb-meta">Aim: message</div></a>
        <a class="thumb" href="#slide-02"><p class="thumb-title">02. 핵심</p><div class="thumb-meta">Aim: layout</div></a>
        <a class="thumb" href="#slide-03"><p class="thumb-title">03. 정리</p><div class="thumb-meta">Aim: tone</div></a>
      </nav>
      <section class="detail">
{cards}
      </section>
    </main>
    <div class="toast" id="toast" role="status"></div>
    <script>
      const editButton = document.querySelector("#nav-edit");
      const toast = document.querySelector("#toast");
      const editables = [...document.querySelectorAll('[data-editable="true"]')];
      let editing = false;

      function showToast(message) {{
        toast.textContent = message;
        toast.classList.add("show");
        window.setTimeout(() => toast.classList.remove("show"), 2800);
      }}

      async function copyPatch() {{
        const lines = ["# Overview edits - {title}", ""];
        document.querySelectorAll("[data-slide]").forEach((slide) => {{
          const aim = slide.querySelector(".aim-select")?.value || slide.dataset.aim || "message";
          lines.push(`## Slide ${{slide.dataset.slide}} (${{slide.dataset.skill}})`);
          lines.push(`- aim: ${{aim}}`);
          slide.querySelectorAll('[data-editable="true"]').forEach((node, index) => {{
            lines.push(`- editable ${{index + 1}}: ${{node.innerHTML}}`);
          }});
          lines.push("");
        }});
        await navigator.clipboard.writeText(lines.join("\\n"));
      }}

      editButton.addEventListener("click", async () => {{
        editing = !editing;
        document.body.classList.toggle("editing", editing);
        editButton.textContent = editing ? "Done" : "Edit";
        editables.forEach((node) => {{
          node.contentEditable = editing ? "true" : "false";
        }});
        if (!editing) {{
          await copyPatch();
          showToast("수정 patch가 클립보드에 복사되었습니다. 다음 요청에 붙여 넣으면 반영할 수 있습니다.");
        }}
      }});
    </script>
  </body>
</html>
"""


def create_topic(config: TopicConfig) -> None:
    if config.target_dir.exists():
        raise FileExistsError(f"Topic already exists: {config.target_dir}")

    (config.target_dir / "assets").mkdir(parents=True)
    (config.target_dir / "exports").mkdir()
    (config.target_dir / "renders").mkdir()
    (config.target_dir / "snapshots").mkdir()

    _copy_root_config(config.target_dir)
    shutil.copy2(config.design_path, config.target_dir / "DESIGN.md")

    index_html = _card_index(config.title, config.company) if config.output_type == "card-news" else _deck_index(config.title, config.company)
    (config.target_dir / "index.html").write_text(index_html, encoding="utf-8")
    (config.target_dir / "overview.html").write_text(_overview(config.title, config.company, config.output_type), encoding="utf-8")
    _write_brief(config)
    _write_json(
        config.target_dir / "topic.json",
        {
            "name": config.name,
            "title": config.title,
            "company": config.company,
            "outputType": config.output_type,
            "designSource": str(config.design_path),
            "createdAt": datetime.now(timezone.utc).isoformat(),
        },
    )


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Create a new HyperFrames topic.")
    parser.add_argument("--name", required=True, help="Topic slug under topics/")
    parser.add_argument("--title", required=True, help="Human-readable topic title")
    parser.add_argument("--company", required=True, help="Company or brand name")
    parser.add_argument("--type", choices=("deck", "card-news"), default="deck", help="Output type")
    parser.add_argument("--design", help="Optional explicit DESIGN markdown path")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    name = _slug(args.name)
    if not name:
        logger.error("Invalid topic name: %s", args.name)
        return 1

    try:
        design_path = _find_design(args.company, args.design)
        config = TopicConfig(
            name=name,
            title=args.title,
            company=args.company,
            output_type=args.type,
            design_path=design_path,
            target_dir=TOPICS_DIR / name,
        )
        create_topic(config)
    except (FileNotFoundError, FileExistsError, OSError) as exc:
        logger.error("Topic creation failed: %s", exc)
        return 1

    logger.info("Topic created: %s", config.target_dir)
    logger.info("Design copied from: %s", config.design_path)
    return 0


if __name__ == "__main__":
    sys.exit(main())
