#!/usr/bin/env python3
"""
propagate-nav-footer.py
Extrai megamenu + footer do arquivo piloto (dj-infantil) e propaga para todas as páginas.
Usage: python3 propagate-nav-footer.py [--dry-run]
"""
import os
import re
import sys

DRY_RUN    = '--dry-run' in sys.argv
UPDATE_NAV = '--update-nav' in sys.argv  # Force-atualiza nav+footer HTML em páginas já com megamenu
BASE_DIR = '/Users/jrios/agita-morango-seo'
PILOT    = os.path.join(BASE_DIR, 'dj-infantil-para-festas-em-sao-paulo', 'index.html')

# ── Padrões de detecção do bloco NAV CSS antigo (diversas variantes) ──
# Vamos substituir tudo entre início do bloco nav e o início do .hero ou outro seletor
NAV_CSS_PATTERNS = [
    # Variante 1: nav com background carvao-deep (páginas antigas estilo DJ)
    (r'\.nav \{ background: var\(--carvao-deep\).*?\.nav-mobile\.open \{ display: flex; \}',
     re.DOTALL),
    # Variante 2: nav com background #fff (páginas home-style)
    (r'    /\* ── NAV ── \*/\s*\.nav \{.*?\.nav-drawer-panel \.btn \{ margin-top: 16px; justify-content: center; \}',
     re.DOTALL),
    # Variante 3: nav simples inline
    (r'    \.nav \{ background:.*?\.nav-mobile\.open \{ display: flex; \}',
     re.DOTALL),
]

# Padrões de detecção do bloco FOOTER CSS antigo
FOOTER_CSS_PATTERNS = [
    (r'    \.footer \{ background: var\(--carvao-deep\).*?\.footer-bottom \{[^}]*\}',
     re.DOTALL),
    (r'    /\* ── FOOTER ── \*/\s*\.footer \{.*?\.footer-bottom a:hover \{ color: var\(--verde\); \}',
     re.DOTALL),
]

# ── HTML patterns ──
# NAV HTML antigo — variante a: <nav class="nav"
NAV_HTML_PATTERNS = [
    (r'<nav class="nav"[^>]*>.*?</nav>\s*', re.DOTALL),
    (r'<!-- ══ NAV ══ -->.*?<!-- Drawer mobile -->.*?</div>\s*(?=<main|<section)', re.DOTALL),
    (r'<!-- ══ NAV ══ -->.*?</div>\s*\n\s*\n\s*<main', re.DOTALL),
]

FOOTER_HTML_PATTERNS = [
    (r'<footer class="footer"[^>]*>.*?</footer>', re.DOTALL),
]

def read_pilot():
    with open(PILOT, 'r', encoding='utf-8') as f:
        return f.read()

def extract_block(html, start_marker, end_marker):
    start = html.find(start_marker)
    end   = html.find(end_marker, start)
    if start == -1 or end == -1:
        return None
    return html[start:end + len(end_marker)]

def extract_nav_css(pilot_html):
    marker_start = '    /* ── MEGAMENU NAV ── */'
    # Termina antes de .hero
    idx_start = pilot_html.find(marker_start)
    # Encontrar onde começa o próximo bloco após o megamenu CSS
    idx_end = pilot_html.find('\n    .hero {', idx_start)
    if idx_start == -1 or idx_end == -1:
        raise ValueError('Não encontrou bloco NAV CSS no piloto')
    return pilot_html[idx_start:idx_end].rstrip()

def extract_footer_css(pilot_html):
    marker_start = '    /* ── FOOTER ── */'
    idx_start = pilot_html.find(marker_start)
    # Termina antes de @media ou próximo comentário
    idx_end = pilot_html.find('\n    @media', idx_start)
    if idx_start == -1 or idx_end == -1:
        raise ValueError('Não encontrou bloco FOOTER CSS no piloto')
    return pilot_html[idx_start:idx_end].rstrip()

def extract_nav_html(pilot_html):
    # De <header class="nav" até </div>\n</div> do mobile overlay
    marker_start = '<header class="nav"'
    marker_end   = '</div>'  # fecha o nav-mobile-overlay
    idx_start = pilot_html.find(marker_start)
    # O mobile overlay termina com </div>\n\n<main
    # Precisamos pegar tudo até antes de <main
    idx_main = pilot_html.find('\n<main', idx_start)
    if idx_main == -1:
        import re as _re
        m = _re.search(r'\n\s*<main', pilot_html[idx_start:])
        if m:
            idx_main = idx_start + m.start()
    if idx_start == -1 or idx_main == -1:
        raise ValueError('Não encontrou NAV HTML no piloto')
    return pilot_html[idx_start:idx_main].rstrip()

def extract_footer_html(pilot_html):
    marker_start = '<footer class="footer" role="contentinfo">'
    marker_end   = '</footer>'
    idx_start = pilot_html.find(marker_start)
    idx_end   = pilot_html.find(marker_end, idx_start)
    if idx_start == -1 or idx_end == -1:
        raise ValueError('Não encontrou FOOTER HTML no piloto')
    return pilot_html[idx_start:idx_end + len(marker_end)]

def extract_megamenu_js(pilot_html):
    marker_start = '  /* ── MEGAMENU JS ── */'
    marker_end   = '  })();'
    idx_start = pilot_html.find(marker_start)
    idx_end   = pilot_html.find(marker_end, idx_start)
    if idx_start == -1 or idx_end == -1:
        raise ValueError('Não encontrou MEGAMENU JS no piloto')
    return pilot_html[idx_start:idx_end + len(marker_end)]

def has_megamenu(html):
    return (
        '/* ── MEGAMENU NAV ── */' in html
        or 'MEGAMENU NAV' in html
        or 'nav-mega-inner' in html
        or 'mega-nav' in html
    )

def is_redirect(html):
    return 'http-equiv' in html.lower() and 'refresh' in html.lower()

def replace_nav_css(html, new_nav_css):
    patterns = [
        # Estilo carvao-deep com mobile-close (colonia, espaco-baby, recreacao-a-domicilio style)
        r'    \.nav \{ background: var\(--carvao-deep\).*?\.mobile-close \{[^}]+\}',
        # Estilo carvao-deep com nav-mobile.open (DJ page original)
        r'    \.nav \{ background: var\(--carvao-deep\).*?\.nav-mobile\.open \{ display: flex; \}',
        # Estilo /* ──── NAV ──── */ com nav-drawer-close (empresa-de-recreacao style)
        r'    /\* ──+\s*NAV\s*──+\s*\*/\s*\.nav \{.*?\.nav-drawer-close \{[^}]+\}',
        # Estilo /* ──── NAV ──── */ com nav-drawer-panel .btn (home-style)
        r'    /\* ──+\s*NAV\s*──+\s*\*/\s*\.nav \{.*?\.nav-drawer-panel \.btn \{[^}]+\}',
        # Estilo /* ── NAV ── */ multi-linha (empresa-de-recreacao variante menor)
        r'    /\* ── NAV ── \*/\s*\.nav \{.*?\.nav-hamburger span \{[^}]+\}',
        # /* NAV */ comment style com nav-drawer-panel .btn (blog, sobre style)
        r'    /\* NAV \*/\s*\.nav \{.*?\.nav-drawer-panel \.btn \{[^}]+\}',
        # Sem comment, .nav direta com nav-drawer-panel .btn (contato, faq, orcamento style)
        r'    \.nav \{ position: sticky.*?\.nav-drawer-panel \.btn \{[^}]+\}',
        # /* NAV */ comment style com .hamburger class e .mobile-menu (recreacao-a-domicilio style)
        r'    /\* NAV \*/\s*\.nav \{.*?\.mobile-close \{[^}]+\}',
        # /* NAV */ comment style sem mobile-close (variante mais curta com .hamburger span)
        r'    /\* NAV \*/\s*\.nav \{.*?\.hamburger span \{[^}]+\}',
        # Variante genérica .nav expandida com nav-mobile
        r'    \.nav \{[^}]+\}.*?\.nav-mobile\.open \{ display: flex; \}',
        # Variante site-header expandida (zona leste style - sem nav-toggle, apenas nav-links hidden)
        r'    \.site-header \{[^}]+\}.*?@media \(max-width: 768px\) \{ \.nav-links \{ display: none; \} \}',
        # Variante site-header com nav-toggle span
        r'    \.site-header \{.*?\.nav-toggle span \{[^}]+\}',
        # cases-e-clientes: header { background... } + nav[aria-label] + .nav-cta:hover
        r'    header \{\s*\n\s*background: var\(--carvao-deep\).*?\.nav-cta:hover \{[^}]+\} \}',
        r'    header \{\s*background: var\(--carvao-deep\).*?\.nav-cta:hover \{[^}]+\} \}',
        # Variante header sem classe expandida (aniversario, nav-toggle style)
        r'    header \{ position: sticky.*?\.nav-toggle span \{[^}]+\}',
        # Variante site-nav expandida (carnaval, dia-das-criancas, festa-cores, festa-pijama)
        r'    nav\.site-nav \{.*?\.nav-toggle span \{[^}]+\}',
        # CSS minificado: .nav{background... (linha única com tudo)
        r'\.nav\{background:[^<]+?\.nav-mobile\.open\{display:flex\}',
        # CSS minificado variante sem nav-mobile (apenas .nav{...}.nav-inner{...}.nav-toggle{...})
        r'\.nav\{background:[^<]+?\.nav-toggle span\{[^}]+\}',
        # CSS minificado .nav{position:sticky... (background não é primeira prop — eventos, terceirizacao)
        r'    \.nav\{position:sticky[^<]+?\.nav-hamburger span\{[^}]+\}',
        # .nav { com multiline block terminando em .nav-burger span (atelie style)
        r'    \.nav \{\n[^<]+?\.nav-burger span \{[^}]+\}',
        # .nav { numa linha + drawer terminando em .nav-overlay (mesas-e-cadeiras style)
        r'    \.nav \{ position: sticky[^<]+?\.nav-overlay \{[^}]+\}',
        # .nav { numa linha terminando em .nav-hamburger span (ativacoes style)
        r'    \.nav \{ position: sticky[^<]+?\.nav-hamburger span \{[^}]+\}',
        # header { com background carvao-deep terminando em .nav-cta:hover (alphaville style)
        r'    header \{\n\s*background: var\(--carvao-deep\)[^<]+?\.nav-cta:hover \{[^}]+\}',
        # header { position:sticky terminando em .nav-toggle span multiline (show-musical style)
        r'    header \{\n\s*position: sticky[^<]+?\.nav-toggle span \{[^}]+\}',
        # header { com mob-overlay/mob-close (aniversario-infantil style)
        r'    header \{[^<]+?\.mob-close \{[^}]+\}',
        # .nav { com mob-overlay/mob-close (baladinha-kids-sem-dj style)
        r'    \.nav \{ background: var\(--branco\)[^<]+?\.mob-close \{[^}]+\}',
    ]
    for pat in patterns:
        m = re.search(pat, html, re.DOTALL)
        if m:
            return html[:m.start()] + new_nav_css + html[m.end():]
    return None

def replace_footer_css(html, new_footer_css):
    patterns = [
        r'    \.footer \{ background: var\(--carvao-deep\).*?\.footer-bottom \{ max-width:[^}]+\}',
        r'    /\* ──+\s*FOOTER\s*──+\s*\*/.*?(?=\n    @media|\n  </style>)',
        # .footer-grid variante (recreacao-a-domicilio, festas-tematicas, carnaval, dia-das-criancas)
        r'    \.footer-grid \{ display: grid.*?\.footer-bottom \{[^}]+\}',
        # .footer com .footer-top variante (contato, faq, orcamento style)
        r'    \.footer \{ background.*?\.footer-copy \{[^}]+\}',
        r'    \.footer \{.*?\.footer-bottom \{[^}]+\}',
        # site-footer variante (zona leste style)
        r'    \.site-footer \{.*?\.footer-bottom \{[^}]+\}',
        # footer sem classe explícita
        r'    footer \{[^}]+\}.*?\.footer-bottom \{[^}]+\}',
        # CSS minificado .footer{background:...} numa linha
        r'\.footer\{background:[^<]+?\.footer-bottom\{[^}]+\}',
        # author page simplificado com .footer-bottom-simple
        r'    \.footer-bottom-simple \{[^<]+?\.footer-bottom-simple a \{[^}]+\}',
    ]
    for pat in patterns:
        m = re.search(pat, html, re.DOTALL)
        if m:
            return html[:m.start()] + new_footer_css + html[m.end():]
    return None

def replace_nav_html(html, new_nav_html):
    patterns = [
        # Nav simples estilo: <nav class="nav"...>...</nav>\n<div class="nav-mobile"...>
        r'<nav class="nav".*?</nav>\s*\n<div class="nav-mobile".*?</div>',
        # Nav drawer estilo home
        r'<!-- ══ NAV ══ -->.*?<!-- Drawer mobile -->.*?</div>(?=\s*\n\s*\n\s*(?:<main|<section))',
        # Apenas nav simples sem drawer
        r'<nav class="nav"[^>]*>.*?</nav>',
        # Header estilo alternativo <header class="nav">
        r'<header class="nav"[^>]*>.*?</header>',
        # site-header variante (zona leste, abc, barueri, guarulhos)
        r'<header class="site-header"[^>]*>.*?</header>',
        # Bare <header> com nav-inner ou header-inner (aniversario, cases-e-clientes etc)
        r'<header>\s*<div class="(?:nav|header)-inner">.*?</header>',
        # site-nav variante (carnaval, dia-das-criancas, festa-cores, festa-pijama)
        r'<nav class="site-nav"[^>]*>.*?</nav>',
        # bolha-style: <nav class="nav" aria-label="..."> sem .nav-mobile separado
        r'<nav class="nav"[^>]*>.*?</nav>\s*\n(?=<(?:nav|section|main|div))',
    ]
    for pat in patterns:
        m = re.search(pat, html, re.DOTALL)
        if m:
            remainder = html[m.end():]
            if 'nav-mobile-overlay' in remainder[:500]:
                mo = re.search(r'<div class="nav-mobile-overlay".*?</div>\s*\n', html, re.DOTALL)
                if mo and mo.start() >= m.start():
                    return html[:m.start()] + new_nav_html + html[mo.end():]
            return html[:m.start()] + new_nav_html + html[m.end():]
    return None

def replace_footer_html(html, new_footer_html):
    patterns = [
        r'<!-- ══ FOOTER ══ -->.*?</footer>',
        r'<footer class="footer".*?</footer>',
        # site-footer variante (zona leste, abc, barueri, guarulhos)
        r'<footer class="site-footer"[^>]*>.*?</footer>',
        # bare <footer role="contentinfo"> variante (carnaval, dia-das-criancas)
        r'<footer role="contentinfo">.*?</footer>',
        # bare <footer> variante (aniversario)
        r'<footer>.*?</footer>',
    ]
    for pat in patterns:
        m = re.search(pat, html, re.DOTALL)
        if m:
            return html[:m.start()] + new_footer_html + html[m.end():]
    return None

def replace_nav_js(html, new_js):
    patterns = [
        r'/\* Nav mobile \*/\s*\(function\(\) \{.*?\}\)\(\);',
        r'// ── NAV HAMBURGUER ──.*?(?=\s*//|</script>)',
        r'var btnHamburger.*?document\.addEventListener\(\'keydown\'.*?\}\);',
        # btnHamburger getElementById variante (empresa-de-recreacao style)
        r"const btnHamburger = document\.getElementById\('btnHamburger'\).*?document\.addEventListener\('keydown'.*?\}\);",
        r"const btnHamburger = document\.getElementById\('btnHamburger'\).*?drawerOverlay\.addEventListener\('click'[^;]+\);",
        # hamburger getElementById variante simples (recreacao-a-domicilio style)
        r"const hamburger = document\.getElementById\('hamburger'\).*?mobileClose\.addEventListener\('click'[^;]+\);",
        # nav-toggle variante inline com onclick (carnaval, dia-das-criancas, festa-cores)
        # JS está no onclick="" do botão, sem bloco JS separado — não há bloco a substituir
        # nav-toggle variante zona leste (aniversario: document.querySelector)
        r"document\.querySelector\('\.nav-toggle'\)\?\.addEventListener\('click',\s*\(\)\s*=>\s*\{.*?\}\s*\}\s*\}\s*\}\s*\}\s*\}\s*\}\s*\}\s*\}\);",
        r"document\.querySelector\('\.nav-toggle'\)\?\.addEventListener\('click'.*?\}\s*\}\s*\}\);",
        # nav-toggle via querySelector genérico
        r"document\.querySelector\('\.nav-toggle'\)\?\.addEventListener\('click'.*?\}\);",
    ]
    for pat in patterns:
        m = re.search(pat, html, re.DOTALL)
        if m:
            return html[:m.start()] + new_js + html[m.end():]
    return None

def process_file(path, nav_css, footer_css, nav_html, footer_html, nav_js):
    with open(path, 'r', encoding='utf-8') as f:
        original = f.read()

    if is_redirect(original):
        print(f'  SKIP (redirect): {path}')
        return False

    if has_megamenu(original) and not UPDATE_NAV:
        print(f'  SKIP (já tem megamenu): {path}')
        return False

    html = original

    if UPDATE_NAV and has_megamenu(original):
        # Modo atualização: substitui bloco header+overlay completo + footer HTML
        # Captura tudo de <header class="nav" até antes de <main (inclui overlay antigo e novo)
        m = re.search(r'<header class="nav".*?(?=\n\s*<main)', html, re.DOTALL)
        if m:
            html = html[:m.start()] + nav_html + html[m.end():]
            print(f'  HTML nav OK (update completo)')
        else:
            # Fallback: tenta padrão genérico
            result = replace_nav_html(html, nav_html)
            if result:
                html = result
                print(f'  HTML nav OK (update fallback)')
            else:
                print(f'  AVISO: HTML nav não encontrado em {path}')

        result = replace_footer_html(html, footer_html)
        if result:
            html = result
            print(f'  HTML footer OK (update)')
        else:
            print(f'  AVISO: HTML footer não encontrado em {path}')
    else:
        # Modo normal: substitui CSS + HTML + JS

        # 1. CSS nav
        result = replace_nav_css(html, nav_css)
        if result:
            html = result
            print(f'  CSS nav OK')
        else:
            print(f'  AVISO: CSS nav não encontrado em {path}')

        # 2. CSS footer
        result = replace_footer_css(html, footer_css)
        if result:
            html = result
            print(f'  CSS footer OK')
        else:
            print(f'  AVISO: CSS footer não encontrado em {path}')

        # 3. CSS mobile footer (corrigir grid-template-columns)
        html = re.sub(
            r'(\.footer-inner \{ grid-template-columns: 1fr; \})',
            '.footer-inner { grid-template-columns: 1fr 1fr; gap: 32px; }\n      .footer-brand-col { grid-column: 1 / -1; }',
            html
        )

        # 4. HTML nav
        result = replace_nav_html(html, nav_html)
        if result:
            html = result
            print(f'  HTML nav OK')
        else:
            print(f'  AVISO: HTML nav não encontrado em {path}')

        # 5. HTML footer
        result = replace_footer_html(html, footer_html)
        if result:
            html = result
            print(f'  HTML footer OK')
        else:
            print(f'  AVISO: HTML footer não encontrado em {path}')

        # 6. JS nav — tenta substituir bloco existente; se não encontrar, injeta antes de </body>
        result = replace_nav_js(html, nav_js)
        if result:
            html = result
            print(f'  JS nav OK (substituído)')
        else:
            # Fallback: injetar megamenu JS em script próprio antes de </body>
            inject = f'\n<script>\n{nav_js}\n</script>\n'
            if '</body>' in html:
                html = html.replace('</body>', inject + '</body>', 1)
                print(f'  JS nav OK (injetado antes de </body>)')
            else:
                print(f'  AVISO: JS nav não injetado — sem </body> em {path}')

    if html == original:
        print(f'  SEM ALTERACOES: {path}')
        return False

    if not DRY_RUN:
        with open(path, 'w', encoding='utf-8') as f:
            f.write(html)

    return True

def main():
    pilot_html = read_pilot()

    nav_css    = extract_nav_css(pilot_html)
    footer_css = extract_footer_css(pilot_html)
    nav_html   = extract_nav_html(pilot_html)
    footer_html= extract_footer_html(pilot_html)
    nav_js     = extract_megamenu_js(pilot_html)

    print(f'[{"DRY RUN" if DRY_RUN else "LIVE"}] Propagando megamenu para todas as páginas...\n')

    # Coletar todos os index.html exceto o piloto e a home
    pages = []
    for root, dirs, files in os.walk(BASE_DIR):
        for fname in files:
            if fname == 'index.html':
                fpath = os.path.join(root, fname)
                if fpath == PILOT:
                    continue
                pages.append(fpath)

    ok = skip = warn = 0
    for path in sorted(pages):
        rel = os.path.relpath(path, BASE_DIR)
        print(f'\n[{rel}]')
        changed = process_file(path, nav_css, footer_css, nav_html, footer_html, nav_js)
        if changed:
            ok += 1
        else:
            skip += 1

    print(f'\n{"="*60}')
    print(f'Total: {ok} alterados, {skip} ignorados')
    if DRY_RUN:
        print('[DRY RUN] Nenhum arquivo foi salvo.')

if __name__ == '__main__':
    main()
