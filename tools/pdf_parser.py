#!/usr/bin/env python3
"""Extract text from PDFs and make image pages available for inspection.

The tool works with one PDF or a directory of PDFs. It preserves page
boundaries, renders selected pages to PNG, and can optionally run Tesseract
OCR over those rendered pages when that optional program is installed.
Source PDFs are never modified.
"""

from __future__ import annotations

import argparse
import json
import shutil
import subprocess
import tempfile
from pathlib import Path


def run(command: list[str]) -> str:
    try:
        result = subprocess.run(command, check=True, text=True, capture_output=True)
    except FileNotFoundError as exc:
        raise SystemExit(f"Required command is unavailable: {exc.filename}") from exc
    except subprocess.CalledProcessError as exc:
        message = exc.stderr.strip() or "command failed"
        raise SystemExit(f"{' '.join(command)}: {message}") from exc
    return result.stdout


def page_count(pdf: Path) -> int:
    info = run(["pdfinfo", str(pdf)])
    for line in info.splitlines():
        if line.startswith("Pages:"):
            return int(line.split(":", 1)[1].strip())
    raise SystemExit("pdfinfo did not report a page count")


def parse_pages(value: str, maximum: int) -> list[int]:
    pages: set[int] = set()
    for part in value.split(","):
        part = part.strip()
        if "-" in part:
            start_text, end_text = part.split("-", 1)
            start, end = int(start_text), int(end_text)
            pages.update(range(min(start, end), max(start, end) + 1))
        else:
            pages.add(int(part))
    invalid = sorted(p for p in pages if p < 1 or p > maximum)
    if invalid:
        raise SystemExit(f"page(s) outside 1..{maximum}: {', '.join(map(str, invalid))}")
    return sorted(pages)


def extract(pdf: Path, pages: list[int]) -> list[dict[str, object]]:
    all_text = run(["pdftotext", "-layout", str(pdf), "-"]).split("\f")
    return [{"page": page, "text": all_text[page - 1].rstrip()} for page in pages]


def render(pdf: Path, pages: list[int], output_dir: Path) -> list[str]:
    output_dir.mkdir(parents=True, exist_ok=True)
    paths = []
    for page in pages:
        prefix = output_dir / f"page-{page:04d}"
        run(["pdftoppm", "-f", str(page), "-l", str(page), "-png", "-singlefile", str(pdf), str(prefix)])
        paths.append(str(prefix.with_suffix(".png")))
    return paths


def ocr_images(image_paths: list[str]) -> dict[str, str]:
    if not shutil.which("tesseract"):
        raise SystemExit(
            "OCR requested but tesseract is not installed. Install tesseract-ocr "
            "and rerun with --ocr."
        )
    result = {}
    for image in image_paths:
        result[image] = run(["tesseract", image, "stdout", "--psm", "6"]).rstrip()
    return result


def pdfs_from_path(path: Path) -> list[Path]:
    if path.is_file():
        if path.suffix.lower() != ".pdf":
            raise SystemExit(f"Expected a PDF file: {path}")
        return [path]
    if path.is_dir():
        return sorted(p for p in path.rglob("*.pdf") if p.is_file())
    raise SystemExit(f"Path not found: {path}")


def process(pdf: Path, args: argparse.Namespace, shared_output: bool) -> dict[str, object]:
    total = page_count(pdf)
    pages = parse_pages(args.pages, total) if args.pages else list(range(1, total + 1))
    result: dict[str, object] = {
        "file": str(pdf),
        "pages": total,
        "extracted": extract(pdf, pages),
    }
    if args.render_dir or args.ocr:
        if args.render_dir:
            output_dir = (
                args.render_dir / pdf.parent.name / pdf.stem
                if shared_output
                else args.render_dir
            )
        else:
            output_dir = Path(tempfile.mkdtemp(prefix="pdf-parser-"))
        rendered = render(pdf, pages, output_dir)
        result["rendered"] = rendered
        if args.ocr:
            result["ocr"] = ocr_images(rendered)
    return result


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("path", type=Path, help="a PDF file or directory to scan recursively")
    parser.add_argument("--pages", help="pages such as 1,3-5; defaults to all pages")
    parser.add_argument("--render-dir", type=Path, help="also render selected pages as PNG")
    parser.add_argument("--ocr", action="store_true", help="OCR rendered pages using optional tesseract")
    parser.add_argument("--json", action="store_true", help="emit machine-readable JSON")
    args = parser.parse_args()

    pdfs = pdfs_from_path(args.path)
    if not pdfs:
        raise SystemExit(f"No PDF files found under {args.path}")
    results = [process(pdf, args, args.path.is_dir()) for pdf in pdfs]
    result: object = results if args.path.is_dir() or len(results) > 1 else results[0]

    if args.json:
        print(json.dumps(result, ensure_ascii=False, indent=2))
        return
    for item in results:
        print(f"# {Path(item['file']).name}\n\nPages: {item['pages']}\n")
        for page in item["extracted"]:
            print(f"## Page {page['page']}\n\n{page['text']}\n")
        if "rendered" in item:
            print("## Rendered pages\n")
            print("\n".join(f"- `{path}`" for path in item["rendered"]))


if __name__ == "__main__":
    main()
