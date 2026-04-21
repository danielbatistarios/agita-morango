# Design System — Agita Morango
Referência para todas as páginas do site. Extraído da home (`index.html`) em 2026-04-19.

---

## 1. Tokens CSS (`:root`)

```css
:root {
  --verde:        #4aa702;
  --verde-escuro: #3d8c02;
  --vermelho:     #9d0505;
  --dourado:      #D4AF37;
  --areia:        #e6dfd1;
  --carvao:       #2e2e2e;
  --carvao-deep:  #1a1a1a;
  --branco:       #ffffff;
  --titulo:       'League Spartan', sans-serif;
  --corpo:        'Bree Serif', serif;
  --editorial:    'Lora', serif;
  --r:            16px;
  --sombra:       0 4px 24px rgba(0,0,0,.10);
  --ease-out:     cubic-bezier(0.16, 1, 0.3, 1);
  --ease-spring:  cubic-bezier(0.34, 1.56, 0.64, 1);
}
```

---

## 2. Tipografia

| Papel | Fonte | Peso | Uso |
|---|---|---|---|
| Títulos (H1-H3, nav, botões) | League Spartan | 700/800/900 | Headlines, labels, CTAs |
| Corpo / subtítulos | Bree Serif | 400 | Parágrafos descritivos |
| Editorial / citações | Lora | 400/600/italic | Depoimentos, blockquotes, subheads |

**Google Fonts link (copiar no `<head>` de toda página):**
```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Bree+Serif&family=Lora:ital,wght@0,400;0,600;1,400&family=League+Spartan:wght@700;800;900&display=swap" rel="stylesheet">
```

**Tamanhos fluidos (clamp):**
- H1 hero: `clamp(2rem, 4.5vw, 3rem)`
- H2 seção: `clamp(1.6rem, 3.5vw, 2.2rem)`
- H2 metodologia: `clamp(1.6rem, 3vw, 2.1rem)`
- Stats (trust bar): `clamp(2.2rem, 4vw, 3rem)`

---

## 3. Fundos por seção

| Seção | Fundo |
|---|---|
| Nav | `#fff` + `border-bottom: 3px solid var(--verde)` |
| Hero | `linear-gradient(135deg, #3d8c02 0%, #4aa702 60%, #5ebe05 100%)` |
| Trust Bar | `var(--carvao)` |
| Serviços | `var(--areia)` |
| Metodologia | `#fff` |
| Clientes B2B / Marquee | `var(--carvao)` |
| Galeria | `var(--carvao-deep)` |
| Depoimentos | `var(--areia)` |
| FAQ | `#fff` |
| CTA Section | `var(--vermelho)` |
| Footer | `var(--carvao)` |

Padrão de alternância: branco / areia / carvão / branco / vermelho.

---

## 4. Botões

```css
.btn {
  display: inline-flex; align-items: center; gap: 8px;
  padding: 14px 32px; border-radius: 100px;
  font-family: var(--titulo); font-weight: 800; font-size: 0.95rem;
  letter-spacing: 0.4px;
  transition: transform .35s var(--ease-out), box-shadow .35s var(--ease-out);
}
/* Variantes */
.btn-verde    { background: var(--verde);    color: #fff; }
.btn-vermelho { background: var(--vermelho); color: #fff; }
.btn-outline  { background: transparent; color: #fff; border: 2px solid rgba(255,255,255,.7); }
```

Efeito shimmer no hover (via `::before` com gradiente branco deslizando).

---

## 5. Nav

- Sticky, height 64px, max-width container 1160px
- Logo: League Spartan 900, `1.3rem`, cor `var(--verde)`, parte "Morango" em `var(--vermelho)`
- Links: League Spartan 700, `0.85rem`, uppercase, `letter-spacing: 0.3px`
- CTA nav: `.btn-vermelho`
- Mobile: hamburger (3 barras) + drawer lateral direito (280px), overlay escuro
- `scroll-padding-top: 72px` para compensar nav sticky (no `mobile-patch.css`)

---

## 6. Cards de serviço

```css
.card {
  background: #fff;
  border-top: 4px solid var(--verde);   /* regra de ouro — border-top verde em todo card */
  border-radius: 16px;
  padding: 28px 24px;
  box-shadow: var(--sombra);
  transform-style: preserve-3d;
}
/* Hover 3D */
.card:hover { transform: translateY(-6px) rotateX(4deg); }
```

Grid: `repeat(4, 1fr)` desktop → `repeat(2, 1fr)` ≤1024px → `1fr` ≤540px.

**Ícone do card:** caixa 52×52px, `border-radius: 12px`, `background: linear-gradient(135deg, var(--verde), var(--verde-escuro))`, SVG branco 26×26px.

---

## 7. Section Header (padrão universal)

```html
<div class="section-header">
  <span class="section-eyebrow">Label em maiúsculas</span>
  <h2>Título da Seção</h2>
  <p>Subtítulo opcional em Lora</p>
</div>
```

```css
.section-eyebrow {
  font-family: var(--titulo); font-weight: 700; font-size: 0.7rem;
  letter-spacing: 2px; text-transform: uppercase; color: var(--verde);
}
.section-header h2 {
  font-family: var(--titulo); font-weight: 900;
  font-size: clamp(1.6rem, 3.5vw, 2.2rem); color: var(--carvao);
}
```

---

## 8. Marquee de logos (Clientes B2B)

- Fundo: `var(--carvao)`
- Animação: `translateX(-50%)` em 32s, dois grupos duplicados para loop infinito
- Mask edges: `linear-gradient(to right, transparent 0%, #000 10%, #000 90%, transparent 100%)`
- Logos: `filter: brightness(0) invert(1)` (converte tudo para branco), `opacity: .55`
- Classes especiais:
  - `.logo-grande` — height 72px (logos muito pequenos por natureza)
  - `.logo-unimed` — height 95px, max-width 280px (SVG com viewBox quadrado)
  - `.logo-sao-silvestre` — height 43px
- Logos **incompatíveis** com `brightness(0) invert(1)`: SVGs com fundo sólido colorido (ex: Morumbi Shopping tinha fundo verde oval — removido). Sempre verificar se o SVG tem `fill` no background antes de usar.

**Logos atuais (pasta `logos/`):**
`itau.svg`, `dolce-gabbana.svg`, `vivo.svg`, `votorantim.svg`, `unimed.svg`, `trackfield.svg`, `sao-silvestre.svg`, `banco-digimais.svg`, `tricolor-run.svg`, `coco-bambu.png`

---

## 9. Depoimentos

- Card: fundo `#fff`, `border-radius: 16px`, `box-shadow: var(--sombra)`
- Avatar: círculo 56×56px, `background: linear-gradient(135deg, var(--verde), var(--verde-escuro))`
- Texto citação: Lora italic, `1rem`, `line-height: 1.75`
- Nome: League Spartan 700
- Estrelas: SVG preenchido com `var(--dourado)`
- Hover: `translateY(-4px)`

---

## 10. CTA Section

- Fundo: `var(--vermelho)` com mesh SVG animado
- H2: League Spartan 900, branco
- Botão principal: `.btn` com fundo branco, texto `var(--vermelho)`
- Texto secundário: Bree Serif, `rgba(255,255,255,.75)`

---

## 11. Footer

- Fundo: `var(--carvao)`
- Logo repetido (League Spartan 900, verde)
- Links em 3 colunas + coluna de redes sociais
- Social icons: círculos 40×40px com border `rgba(255,255,255,.15)`, hover background `var(--verde)`
- Linha de copyright: `font-size: 0.82rem`, `color: rgba(255,255,255,.4)`

---

## 12. Efeitos e animações

| Efeito | Onde | Como |
|---|---|---|
| Blob animado | Hero | SVG `scale` + `rotate` em loop, `will-change: transform` |
| 3D card hover | Cards serviço, blog | `rotateX(4deg) translateY(-6px)`, `transform-style: preserve-3d` |
| Counter animado | Trust Bar | `IntersectionObserver` + `requestAnimationFrame`, vanilla JS |
| Reveal on scroll | Seções internas | `.reveal` com `opacity: 0 → 1`, `translateY(20px → 0)` |
| Parallax blob | Hero scroll | `requestAnimationFrame` no `scroll` event |
| Marquee infinito | Clientes B2B | CSS `animation: marquee-scroll 32s linear infinite` |
| Lightbox galeria | Galeria | JS vanilla, overlay `rgba(0,0,0,.92)` |

**`prefers-reduced-motion`:** blobs, mesh e reveal são desativados/estáticos. Marquee fica 60s.
**Hover em touch:** todos os hovers de card/btn estão dentro de `@media (hover: hover)`.

---

## 13. Responsividade

Arquivo: `mobile-patch.css` (linkar em toda página como último stylesheet antes de `</head>`).
Score base mobile: 62/100 → estimativa pós-patch: 84/100.

Breakpoints principais:
- `1024px` — cards 4col → 2col
- `900px` — cards grid tablet
- `820px` — hero 2col → 1col, nav mobile
- `640px` — padding seções reduzido, font-sizes mínimos, letter-spacing
- `540px` — cards 1col
- `480px` — trust bar 2×2, stat-num menor

---

## 14. Container e espaçamento

```css
.container { max-width: 1160px; margin: 0 auto; padding: 0 24px; }
```

Padding padrão de seção: `80px 24px` (desktop) → `52px` (mobile via patch).

---

## 15. Regras obrigatórias

- Zero travessão (—) em textos. Substituir por vírgula ou ponto.
- Textos em PT-BR em todos os elementos, inclusive `alt` de imagens.
- WhatsApp CTA: `https://wa.me/5511984049485`
- JSON-LD `@id` global: `https://agitamorango.com.br/#entity`
- Canonical e OG tags em toda página.
- `mobile-patch.css` linkado em toda página.
