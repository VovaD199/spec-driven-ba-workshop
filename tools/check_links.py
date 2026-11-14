#!/usr/bin/env python3
"""Check that relative Markdown links and `materials/...` / `templates/...` paths in *.md exist.
Usage: python3 tools/check_links.py   (exit code 1 if broken links found)"""
import re, sys, pathlib
root = pathlib.Path(__file__).resolve().parent.parent
link = re.compile(r'\[[^\]]*\]\(([^)#\s]+)(?:#[^)]*)?\)')
bad = []
for md in root.rglob('*.md'):
    if '.git' in md.parts:
        continue
    for m in link.finditer(md.read_text(encoding='utf-8')):
        t = m.group(1)
        if re.match(r'^[a-z]+:', t):
            continue
        p = (root / t.lstrip('/')) if t.startswith('/') else (md.parent / t)
        if not p.exists():
            bad.append(f'{md.relative_to(root)}: {t}')
    # legacy path guard
    if re.search(r'(?<![\w/])course/', md.read_text(encoding='utf-8')) and 'docs' not in md.parts:
        bad.append(f'{md.relative_to(root)}: legacy `course/` path')
print('\n'.join(bad) or 'OK: no broken links')
sys.exit(1 if bad else 0)
