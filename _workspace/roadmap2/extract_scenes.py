"""현재 덱(index.html)에서 빌더용 재료를 뽑는다. 덱 원본은 읽기만 한다.

만드는 것:
- scenes/<장면ID>.html : 장면(<section>) 하나씩 — 유지 장면은 그대로 복사하고, 보강 장면은 이 파일을 고친다
- scene-styles.css      : <style id="scene-styles"> 안의 CSS 전부 — 빌더가 쓸 수 있는 클래스 목록
- scene_order.txt       : 현재 장면 순서(장면ID · data-skill · BLOCK)

사용법: python _workspace/roadmap2/extract_scenes.py topics/<topic>/index.html _workspace/roadmap2
"""
import logging
import re
import sys
from pathlib import Path

logging.basicConfig(level=logging.INFO, format="%(message)s")
log = logging.getLogger("extract_scenes")

SECTION_RE = re.compile(r'<section\b[^>]*class="scene\b[^"]*"[^>]*>.*?</section>', re.S)
SCENE_ID_RE = re.compile(r'data-scene-id="([^"]+)"')
SKILL_RE = re.compile(r'data-skill="([^"]+)"')
STYLE_RE = re.compile(r'<style id="scene-styles">(.*?)</style>', re.S)
BLOCK_RE = re.compile(r"<!-- BLOCK:(\w+) START -->(.*?)<!-- BLOCK:\1 END -->", re.S)


def main(index_path, out_dir):
  """index.html 을 읽어 장면별 파일, CSS, 순서표를 저장한다."""
  html = Path(index_path).read_text(encoding="utf-8")
  out = Path(out_dir)
  scenes_dir = out / "scenes"
  scenes_dir.mkdir(parents=True, exist_ok=True)

  style = STYLE_RE.search(html)
  if style is None:
    raise SystemExit('<style id="scene-styles"> 를 찾지 못했습니다')
  (out / "scene-styles.css").write_text(style.group(1).strip() + "\n", encoding="utf-8")

  order_lines = []
  for block in BLOCK_RE.finditer(html):
    block_name, block_html = block.group(1), block.group(2)
    for section in SECTION_RE.finditer(block_html):
      scene = section.group(0)
      scene_id = SCENE_ID_RE.search(scene).group(1)
      skill = SKILL_RE.search(scene).group(1)
      (scenes_dir / f"{scene_id}.html").write_text(scene + "\n", encoding="utf-8")
      order_lines.append(f"{len(order_lines) + 1}\t{scene_id}\t{skill}\t{block_name}")

  (out / "scene_order.txt").write_text("\n".join(order_lines) + "\n", encoding="utf-8")
  log.info("장면 %d개 → %s", len(order_lines), scenes_dir)
  log.info("CSS %d자 → %s", len(style.group(1)), out / "scene-styles.css")


if __name__ == "__main__":
  main(sys.argv[1], sys.argv[2])
