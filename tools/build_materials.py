#!/usr/bin/env python3
"""Builds course materials (Markdown, uk + en) into HTML and PDF with coloured blocks.
Збирає навчальні матеріали (Markdown, uk + en) у HTML і PDF з кольоровими блоками.

Usage / Використання:
    python tools/build_materials.py materials/uk/day-1/day-1-instruction.md [more files...]
        [--teacher]   show mentor/teacher sections and open <details> (hidden by default)
        [--pdf]       also make a PDF via Chrome/Edge/Chromium (headless)
        [--out build] output folder
        [--all]       build all materials/<lang>/*/*.md (student version; mentor/ too with --teacher)
    python tools/build_materials.py --all --pdf [--teacher]

Needs: pip install markdown
Language (uk/en) is taken from the path (/en/ → English markers, else Ukrainian).
"""
import argparse
import html
import os
import re
import shutil
import subprocess
import sys

import markdown

HERE = os.path.dirname(os.path.abspath(__file__))
CSS_PATH = os.path.join(HERE, 'materials.css')

# Paragraph start (after **) -> colour class; both languages
MARKERS = [
    ("**КОПІЮЙТЕ", 'c-copy'), ("**COPY", 'c-copy'),
    ("**У ЧАТ CURSOR", 'c-chat'), ("**IN CURSOR CHAT", 'c-chat'),
    ("**У FIGMA MAKE", 'c-figma'), ("**IN FIGMA MAKE", 'c-figma'),
    ("**ПЕРЕВІРТЕ", 'c-check'), ("**CHECK", 'c-check'),
    ("**ЯКЩО НЕ ВИЙШЛО", 'c-fail'), ("**IF IT FAILED", 'c-fail'),
    ("**БЕЗПЕКА", 'c-safety'), ("**SAFETY", 'c-safety'),
    ("**Здача", 'c-deliver'), ("**Submission", 'c-deliver'),
    ("**Обов'язкове", 'c-deliver'), ("**Обов’язкове", 'c-deliver'), ("**Required", 'c-deliver'),
    ("*Орієнтир", 'c-hint'), ("*Hint", 'c-hint'),
]

TEACHER_HEADING = re.compile(r'^(#{1,6})\s+(.*(Для викладача|Для ментора|Критерії перевірки \(ментору\)|Для менторів|Для куратора|For the mentor|Review criteria \(for the mentor\)|For mentors|For the curator).*)$')

ROW_CLASSES = {
    'КОПІЮЙТЕ': 'row-c-copy',
    'У ЧАТ CURSOR': 'row-c-chat',
    'У FIGMA MAKE': 'row-c-figma',
    'ПЕРЕВІРТЕ': 'row-c-check',
    'ЯКЩО НЕ ВИЙШЛО': 'row-c-fail',
    'БЕЗПЕКА': 'row-c-safety',
    "ОБОВ'ЯЗКОВЕ": 'row-c-deliver',
    'ОБОВ’ЯЗКОВЕ': 'row-c-deliver',
    'ОРІЄНТИР': 'row-c-hint',
    'COPY': 'row-c-copy',
    'IN CURSOR CHAT': 'row-c-chat',
    'IN FIGMA MAKE': 'row-c-figma',
    'CHECK': 'row-c-check',
    'IF IT FAILED': 'row-c-fail',
    'SAFETY': 'row-c-safety',
    'REQUIRED': 'row-c-deliver',
    'HINT': 'row-c-hint',
}


def color_legend_table(body):
    """Фарбує рядки таблиці «Як користуватися інструкцією» за позначкою в першій клітинці."""
    m = re.search(r'(<h2[^>]*>(?:Як користуватися інструкцією|How to use this instruction)</h2>\s*)<table>(.*?)</table>', body, re.S)
    if not m:
        return body
    table = m.group(2)

    def row(rm):
        cell = re.search(r'<td[^>]*>(.*?)</td>', rm.group(1), re.S)
        key = re.sub(r'<[^>]+>', '', cell.group(1)).strip() if cell else ''
        cls = ROW_CLASSES.get(key)
        return ('<tr class="%s">' % cls if cls else '<tr>') + rm.group(1) + '</tr>'

    table = re.sub(r'<tr>(.*?)</tr>', row, table, flags=re.S)
    return body[:m.start()] + m.group(1) + '<table class="legend-table">' + table + '</table>' + body[m.end():]


def split_blocks(text):
    """Ділить Markdown на блоки: заголовок / огороджений код / решта (абзац, список, таблиця, цитата)."""
    lines = text.split('\n')
    blocks, cur, in_fence = [], [], False
    for line in lines:
        if line.strip().startswith('```'):
            if not in_fence:
                if cur:
                    blocks.append(('para', '\n'.join(cur)))
                    cur = []
                in_fence = True
                cur.append(line)
            else:
                cur.append(line)
                blocks.append(('fence', '\n'.join(cur)))
                cur = []
                in_fence = False
            continue
        if in_fence:
            cur.append(line)
            continue
        if line.strip() == '':
            if cur:
                blocks.append(('para', '\n'.join(cur)))
                cur = []
            continue
        if re.match(r'^#{1,6}\s', line) and not cur:
            blocks.append(('heading', line))
            continue
        cur.append(line)
    if cur:
        blocks.append(('fence' if in_fence else 'para', '\n'.join(cur)))
    return blocks


def is_list(block):
    return re.match(r'^(\s*[-*]\s|\s*\d+\.\s)', block[1].split('\n')[0]) is not None


LIST_LINE = re.compile(r'^\s*([-*+]|\d+\.)\s+')


def fix_lists(body):
    """Python-Markdown вимагає порожнього рядка перед списком: додаємо його."""
    out = []
    prev = ''
    for line in body.split('\n'):
        if LIST_LINE.match(line) and prev.strip() and not LIST_LINE.match(prev) and not prev.startswith('>') and not prev.startswith('|') and not prev.startswith(' '):
            out.append('')
        out.append(line)
        prev = line
    return '\n'.join(out)


def transform(text, teacher, callouts=True):
    blocks = [(k, fix_lists(b) if k == 'para' else b) for k, b in split_blocks(text)]
    out = []
    i = 0
    skip_level = None
    first_quote_done = False
    while i < len(blocks):
        kind, body = blocks[i]
        # розділи для викладача
        if kind == 'heading':
            m = TEACHER_HEADING.match(body)
            level = len(body) - len(body.lstrip('#'))
            if skip_level is not None and level <= skip_level:
                skip_level = None
            if m and not teacher:
                skip_level = level
                i += 1
                continue
        if skip_level is not None:
            i += 1
            continue
        if kind == 'para' and body.lstrip().startswith('>'):
            first_line = body.lstrip()[1:].strip()
            if not teacher and (first_line.startswith('ЧЕРНЕТКА') or first_line.startswith('DRAFT') or first_line.startswith('**Для викладача') or first_line.startswith('Для викладача') or first_line.startswith('**For the mentor') or first_line.startswith('For the mentor')):
                i += 1
                continue
        # кольорові маркери
        if kind == 'para':
            cls = None
            stripped = body.lstrip()
            for prefix, c in MARKERS:
                if stripped.startswith(prefix):
                    cls = c
                    break
            if cls and callouts:
                group = [body]
                if i + 1 < len(blocks):
                    nkind, nbody = blocks[i + 1]
                    if nkind == 'fence' or (nkind == 'para' and is_list(blocks[i + 1])):
                        group.append(nbody)
                        i += 1
                out.append('<div class="callout %s" markdown="1">\n\n%s\n\n</div>' % (cls, '\n\n'.join(group)))
                i += 1
                continue
        out.append(body)
        i += 1
    return '\n\n'.join(out) + '\n'


def render(md_path, teacher):
    text = open(md_path, encoding='utf8').read()
    text = transform(text, teacher)
    body = markdown.markdown(text, extensions=['extra', 'md_in_html', 'sane_lists', 'toc'])
    if teacher:
        body = body.replace('<details>', '<details open>')
    title = os.path.splitext(os.path.basename(md_path))[0]
    m = re.search(r'<h1[^>]*>(.*?)</h1>', body, re.S)
    if m:
        title = re.sub(r'<[^>]+>', '', m.group(1))
    css = open(CSS_PATH, encoding='utf8').read()
    body = color_legend_table(body)
    lang = 'en' if '/en/' in md_path.replace('\\', '/') else 'uk'
    return '<!doctype html>\n<html lang="%s"><head><meta charset="utf-8">' \
           '<meta name="viewport" content="width=device-width, initial-scale=1">' \
           '<title>%s</title><style>%s</style></head><body>%s</body></html>' % (lang, html.escape(title), css, body)


def find_browser():
    env = os.environ.get('SDD_PDF_BROWSER')
    if env and os.path.exists(env):
        return env
    candidates = [
        r'C:\Program Files\Google\Chrome\Application\chrome.exe',
        r'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe',
        r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe',
        r'C:\Program Files\Microsoft\Edge\Application\msedge.exe',
        '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',
        '/Applications/Microsoft Edge.app/Contents/MacOS/Microsoft Edge',
    ]
    import glob
    candidates += sorted(glob.glob('/opt/pw-browsers/chromium_headless_shell-*/chrome-headless-shell-linux*/chrome-headless-shell'))
    candidates += sorted(glob.glob('/opt/pw-browsers/chromium-*/chrome-linux*/chrome'))
    for c in candidates:
        if os.path.exists(c):
            return c
    for name in ('google-chrome', 'chromium', 'chromium-browser', 'microsoft-edge'):
        found = shutil.which(name)
        if found:
            return found
    return None


def to_pdf(html_path, pdf_path):
    browser = find_browser()
    if not browser:
        print('Chrome/Edge/Chromium not found for PDF (set SDD_PDF_BROWSER)', file=sys.stderr)
        return False
    uri = 'file://' + ('/' if not os.path.abspath(html_path).startswith('/') else '') + os.path.abspath(html_path).replace('\\', '/')
    import tempfile
    profile = tempfile.mkdtemp(prefix='materials-pdf-')
    cmd = [browser, '--headless=new', '--disable-gpu', '--no-sandbox', '--no-pdf-header-footer',
           '--user-data-dir=' + profile,
           '--print-to-pdf=' + os.path.abspath(pdf_path), uri]
    try:
        subprocess.run(cmd, check=False, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, timeout=120)
    except subprocess.TimeoutExpired:
        print('Browser timed out', file=sys.stderr)
        return False
    return os.path.exists(pdf_path)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('files', nargs='*')
    ap.add_argument('--all', action='store_true', help='build all day instructions (uk, en)')
    ap.add_argument('--teacher', action='store_true')
    ap.add_argument('--pdf', action='store_true')
    ap.add_argument('--strip-md', action='store_true',
                    help='зберегти чистий Markdown для учасників (без розділів викладача й позначки ЧЕРНЕТКА), без HTML/PDF')
    ap.add_argument('--out', default='build')
    args = ap.parse_args()
    if args.all:
        import glob
        root = os.path.dirname(HERE)
        args.files += sorted(glob.glob(os.path.join(root, 'materials', '*', '*', '*.md')))
        if args.teacher:
            args.files += sorted(glob.glob(os.path.join(root, 'mentor', '*', '*.md')))
    if not args.files:
        ap.error('give files or --all')
    os.makedirs(args.out, exist_ok=True)
    if args.strip_md:
        for f in args.files:
            text = open(f, encoding='utf8').read()
            out_md = os.path.join(args.out, os.path.basename(f))
            open(out_md, 'w', encoding='utf8', newline='\n').write(transform(text, False, callouts=False))
            print('MD:', out_md)
        return
    for f in args.files:
        lang = 'en' if '/en/' in f.replace('\\', '/') else 'uk'
        name = os.path.splitext(os.path.basename(f))[0] + '.' + lang + ('-teacher' if args.teacher else '')
        html_path = os.path.join(args.out, name + '.html')
        open(html_path, 'w', encoding='utf8').write(render(f, args.teacher))
        print('HTML:', html_path)
        if args.pdf:
            pdf_path = os.path.join(args.out, name + '.pdf')
            print('PDF:', pdf_path, 'OK' if to_pdf(html_path, pdf_path) else 'failed')


if __name__ == '__main__':
    main()
