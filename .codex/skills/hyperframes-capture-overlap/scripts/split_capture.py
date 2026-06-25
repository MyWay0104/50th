from __future__ import annotations

import argparse
from pathlib import Path

from PIL import Image


def parse_box(value: str) -> tuple[int, int, int, int]:
    parts = [int(part.strip()) for part in value.split(",")]
    if len(parts) != 4:
        raise argparse.ArgumentTypeError("box must be left,top,right,bottom")
    left, top, right, bottom = parts
    if right <= left or bottom <= top:
        raise argparse.ArgumentTypeError("box right/bottom must be greater than left/top")
    return left, top, right, bottom


def parse_size(value: str) -> tuple[int, int]:
    left, sep, right = value.lower().partition("x")
    if sep != "x":
        raise argparse.ArgumentTypeError("size must be WIDTHxHEIGHT")
    width = int(left)
    height = int(right)
    if width <= 0 or height <= 0:
        raise argparse.ArgumentTypeError("size values must be positive")
    return width, height


def save_crop(
    source: Image.Image,
    box: tuple[int, int, int, int],
    output: Path,
    size: tuple[int, int] | None,
    quality: int,
) -> None:
    crop = source.crop(box)
    if size is not None:
        crop = crop.resize(size, Image.Resampling.LANCZOS)
    output.parent.mkdir(parents=True, exist_ok=True)
    suffix = output.suffix.lower()
    if suffix in {".jpg", ".jpeg"}:
        crop.convert("RGB").save(output, quality=quality, optimize=True)
    else:
        crop.save(output)


def main() -> None:
    parser = argparse.ArgumentParser(description="Split a tall AI screenshot into question and answer crop files.")
    parser.add_argument("--source", required=True, type=Path)
    parser.add_argument("--question-out", required=True, type=Path)
    parser.add_argument("--answer-out", required=True, type=Path)
    parser.add_argument("--question-box", required=True, type=parse_box)
    parser.add_argument("--answer-box", required=True, type=parse_box)
    parser.add_argument("--question-size", type=parse_size)
    parser.add_argument("--answer-size", type=parse_size)
    parser.add_argument("--quality", type=int, default=95)
    args = parser.parse_args()

    source = Image.open(args.source).convert("RGB")
    save_crop(source, args.question_box, args.question_out, args.question_size, args.quality)
    save_crop(source, args.answer_box, args.answer_out, args.answer_size, args.quality)

    for output in [args.question_out, args.answer_out]:
        image = Image.open(output)
        print(f"{output}: {image.size[0]}x{image.size[1]}")


if __name__ == "__main__":
    main()
