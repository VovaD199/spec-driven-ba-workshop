# Build tools / Інструменти збірки

## `check_links.py`
Checks relative Markdown links and forbids the old template-folder paths. Run before every commit / Перевіряє відносні посилання; запускайте перед кожним комітом:

```bash
python3 tools/check_links.py
```

## `build_materials.py`
Turns the Markdown instructions (uk and en) into HTML and PDF with **coloured blocks**: COPY (blue), IN CURSOR CHAT (purple), IN FIGMA MAKE (pink), CHECK (green), IF IT FAILED (orange), SAFETY (red), REQUIRED / submission (gold), HINT (teal). Colours are in `materials.css`. Markers are recognised in both languages.
Перетворює Markdown-інструкції на HTML і PDF із кольоровими блоками; мітки впізнаються обома мовами.

### Requirements / Потрібно
- Python 3 and `pip install markdown`
- Chrome, Edge or Chromium for PDF (found automatically on Windows and macOS; on Linux set `SDD_PDF_BROWSER=/path/to/chrome` if needed). If PDF hangs, use headless Chromium (`chrome-headless-shell`).

### Examples / Приклади
```bash
# one file, student version (mentor sections hidden, <details> collapsed)
python3 tools/build_materials.py materials/uk/day-1/day-1-instruction.md --pdf

# all student materials, both languages
python3 tools/build_materials.py --all --pdf

# mentor version (mentor sections shown, <details> opened; includes mentor/ guides)
python3 tools/build_materials.py --all --pdf --teacher

# plain Markdown for participants without mentor sections
python3 tools/build_materials.py materials/en/day-2/day-2-instruction.md --strip-md
```
Output goes to `build/` (not committed). File names: `<name>.<lang>[-teacher].pdf`.

## What the script does / Що робить скрипт
- Wraps a marked paragraph and the code block or list after it in a coloured box.
- Hides the "For the mentor" / "Review criteria" sections and the DRAFT note for students; `--teacher` keeps them.
- Colours the rows of the "How to use this instruction" legend table.

## Limitations / Обмеження
- Mermaid diagrams are not drawn: they appear as code in the PDF.
- Relative links to other Markdown files are not clickable in the PDF.
- Not tested on Windows and macOS: the PDF step was run only on Linux (headless Chromium).
- Slides are not generated (none exist yet).
- Moodle upload itself was not tested: see `moodle/`.
