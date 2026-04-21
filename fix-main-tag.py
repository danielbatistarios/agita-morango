#!/usr/bin/env python3
"""
Insere <main id="conteudo-principal"> antes da primeira <section
e </main> antes do <footer, em todas as páginas que ainda não têm <main>.
"""
import os, re

BASE = '/Users/jrios/agita-morango-seo'

# Páginas que já têm <main> — pular
already_has_main = set()

fixed = []
skipped = []
errors = []

for root, dirs, files in os.walk(BASE):
    # skip node_modules, .git, etc
    dirs[:] = [d for d in dirs if not d.startswith('.') and d != 'node_modules' and d != 'logos' and d != 'img']
    for fname in files:
        if fname != 'index.html':
            continue
        path = os.path.join(root, fname)
        rel = os.path.relpath(path, BASE)

        with open(path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Skip if already has <main
        if '<main' in content:
            skipped.append(rel)
            continue

        # Find first <section
        section_match = re.search(r'<section\b', content)
        if not section_match:
            errors.append(f'{rel} — sem <section>')
            continue

        # Find <footer
        footer_match = re.search(r'<footer\b', content)
        if not footer_match:
            errors.append(f'{rel} — sem <footer>')
            continue

        # Insert <main> before first <section
        insert_pos = section_match.start()
        new_content = (
            content[:insert_pos]
            + '<main id="conteudo-principal">\n'
            + content[insert_pos:]
        )

        # Find </main> insertion point — before <footer (in the NEW content)
        footer_match2 = re.search(r'<footer\b', new_content)
        insert_pos2 = footer_match2.start()
        new_content = (
            new_content[:insert_pos2]
            + '</main>\n\n'
            + new_content[insert_pos2:]
        )

        with open(path, 'w', encoding='utf-8') as f:
            f.write(new_content)

        fixed.append(rel)

print(f'\n✅ Corrigidas: {len(fixed)}')
for f in fixed:
    print(f'   {f}')

print(f'\n⏭  Puladas (já tinham <main>): {len(skipped)}')
for s in skipped:
    print(f'   {s}')

if errors:
    print(f'\n❌ Erros: {len(errors)}')
    for e in errors:
        print(f'   {e}')
