"""덱이 CDN에서 불러오는 글꼴·스크립트를 topic 안의 로컬 파일로 바꾼다.

인터넷이 막힌 곳(사내망)에서는 CDN 글꼴이 내려오지 않아 글꼴이 바뀌고, 그러면 줄바꿈과 넘침이 전부 달라진다.
저장소 공용 폴더(`assets/vendor/`)의 파일을 topic 으로 복사하고 index.html 의 URL 을 상대 경로로 바꾼다.

사용:
    python scripts/deck/localize_assets.py topics/<topic>
    python scripts/deck/localize_assets.py topics/<topic> --check   (바꿀 것이 남았는지만 확인)
"""
from __future__ import annotations

import argparse
import logging
import re
import shutil
import sys
from pathlib import Path

logging.basicConfig(level=logging.INFO, format="%(message)s")
logger = logging.getLogger(__name__)

VENDOR_ROOT = Path("assets/vendor")
# (CDN URL 조각, topic 안 상대 경로)
MAP = {
    "https://cdn.jsdelivr.net/gh/fonts-archive/Paperlogy/": "assets/vendor/fonts/",
    "https://cdn.jsdelivr.net/npm/@fontsource/jetbrains-mono@5.0.20/files/": "assets/vendor/fonts/",
    "https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/gsap.min.js": "assets/vendor/js/gsap.min.js",
}
PRECONNECT_RE = re.compile(r'\n[ \t]*<link rel="preconnect"[^>]*>')


def localize(text: str, topic_dir: Path, vendor_root: Path, copied: list[str]) -> str:
    """URL 을 상대 경로로 바꾸고 필요한 파일을 topic 으로 복사한다."""
    for url in sorted(set(re.findall(r'https?://[^"\')\s]+', text))):
        for prefix, target_dir in MAP.items():
            if not url.startswith(prefix):
                continue
            name = Path(url).name
            rel = target_dir if target_dir.endswith(name) else f"{target_dir}{name}"
            source = vendor_root / Path(rel).relative_to("assets/vendor")
            destination = topic_dir / rel
            if not destination.exists():
                if not source.exists():
                    logger.info("  ! 공용 폴더에 없음: %s (먼저 받아 두세요)", source)
                    break
                destination.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(source, destination)
                copied.append(rel)
            text = text.replace(url, rel)
            break
    return PRECONNECT_RE.sub("", text)


def main() -> int:
    """index.html 을 고치고 남은 외부 URL 수를 종료 코드로 돌려준다."""
    parser = argparse.ArgumentParser(description="CDN 자산 로컬화")
    parser.add_argument("topic", type=Path, help="topics/<topic> 폴더")
    parser.add_argument("--vendor", type=Path, default=VENDOR_ROOT, help="공용 자산 폴더")
    parser.add_argument("--check", action="store_true", help="고치지 않고 남은 외부 참조만 센다")
    args = parser.parse_args()

    index_path = args.topic / "index.html" if args.topic.is_dir() else args.topic
    text = index_path.read_text(encoding="utf-8")
    if args.check:
        left = [u for u in re.findall(r'(?:src|href)="(https?://[^"]+)"', text)]
        logger.info("외부 참조 %d건 %s", len(left), left[:5])
        return 1 if left else 0

    copied: list[str] = []
    new_text = localize(text, index_path.parent, args.vendor, copied)
    index_path.write_text(new_text, encoding="utf-8", newline="\n")
    left = re.findall(r'(?:src|href)="(https?://[^"]+)"', new_text)
    logger.info("복사 %d개: %s", len(copied), ", ".join(copied) or "없음")
    logger.info("남은 외부 참조 %d건 %s", len(left), left[:5])
    logger.info("overview.html 은 scripts/sync_overview.py 로 다시 만드세요.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
