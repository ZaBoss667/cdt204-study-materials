# PDF photo and text parser

`pdf_parser.py` is a small command-line tool for the course PDFs in this
workspace and for future PDFs added to it. It:

- extracts selectable PDF text while preserving page boundaries;
- scans a directory recursively for every `.pdf` file;
- renders selected pages as PNG files, which makes diagrams, photographs, and
  image-only pages available for inspection;
- optionally runs OCR on rendered pages with Tesseract; and
- emits readable Markdown by default or JSON for scripts.

The tool does not edit or replace source PDFs.

## Requirements

The current Linux setup already provides:

- `pdfinfo`
- `pdftotext`
- `pdftoppm`

OCR is optional. To enable it, install Tesseract and its language data using
your Linux distribution's package manager, then rerun with `--ocr`.

## Examples

Parse one PDF and print its text:

```bash
python3 tools/pdf_parser.py "Lesson 2 - ISA/Lecture 2 - ISA and Pipelining.pdf"
```

Parse selected pages and render them:

```bash
python3 tools/pdf_parser.py "Lecture 3 - Datapath and Pipelining Episode 1.pdf" \
  --pages 3,12-15 \
  --render-dir /tmp/cdt204-pages
```

Scan all current and future PDFs below the workspace:

```bash
python3 tools/pdf_parser.py . --pages 1-3 --json > /tmp/cdt204-pdfs.json
```

Render and OCR photographed or image-only pages when Tesseract is installed:

```bash
python3 tools/pdf_parser.py "Past Exams - Older" \
  --pages 1-4 \
  --render-dir /tmp/cdt204-ocr \
  --ocr --json > /tmp/cdt204-ocr.json
```

For a directory input, each PDF gets its own subdirectory under
`--render-dir`. Without `--render-dir`, `--ocr` uses a temporary directory and
returns its paths in the JSON output.

## Limitations

Text extraction depends on the PDF's text layer. OCR is only available when
the external Tesseract program is installed, and OCR output should be checked
for errors in equations, MIPS code, tables, and small labels. Rendering is
always available as a fallback for visual inspection.
