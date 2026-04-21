# Seções Obrigatórias — Agita Morango (Páginas de Serviço)

> Referência definitiva para todas as páginas de serviço. Antes de qualquer edição: abra este arquivo. Após qualquer edição: marque o status da página no final.

---

## Ordem obrigatória das seções (14 + footer)

| # | Seção | ID âncora | CSS class | Obrigatória? |
|---|---|---|---|---|
| 1 | HERO | `#hero-h1` | `.hero` | Sim |
| 2 | BREADCRUMB | — | `.breadcrumb` | Sim |
| 3 | O QUE É | `#oque-title` ou `#oque-h2` | — | Sim |
| 4 | CARDS (6 H3) | `#cards-title` ou `#inclui-h2` | `.cards-section` | Sim |
| 5 | FORM multi-step | `#form-title` | `.form-section` | Sim |
| 6 | GALERIA (6 items) | `#galeria-title` | `.galeria-section` | Sim |
| 7 | EQUIP (4 cards) | `#equip-title` | `.equipamento-section` | Sim |
| 8 | DIFERENCIAIS (4 cards) | `#dif-title` | — | Sim |
| 9 | DEPOIMENTOS (3 cards) | `#depo-title` | `.depo-section` | Sim |
| 10 | E-E-A-T | `#eeat-title` | `.eeat-section` | Sim |
| 11 | RELACIONADOS (3 cards) | `#rel-title` | — | Sim |
| 12 | FAQ (5 perguntas H3) | `#faq-title` | — | Sim |
| 13 | ONDE ESTAMOS | `#onde-title` | `.onde-estamos` | Sim |
| 14 | FOOTER | — | `.footer` | Sim |
| — | LIGHTBOX (fora do main) | `#lbBackdrop` | — | Sim (para galeria funcionar) |

---

## Regras críticas por seção

### 1. HERO
- H1 com keyword principal + variante geo
- `.hero-badge` acima do H1
- `.hero-sub`: QUE entrega + COMO diferencia + RESULTADO emocional (3 frases)
- `.hero-btns`: btn-primary WhatsApp + btn-outline para âncora interna
- `.hero-card`: stats (4 itens) OU checklist do que inclui
- **NUNCA usar `<h3>` dentro de `.hero-card`** — usar `<p class="hero-card-label"><strong>...</strong></p>`

### 2. BREADCRUMB
- `<nav class="breadcrumb">` com `<ol>`
- 3 níveis: Home → Serviços → Nome da Página
- Link "Serviços" aponta para `/empresa-de-recreacao-em-sao-paulo/`

### 3. O QUE É
- `<p class="section-label">` acima do H2
- H2 descreve o serviço profissional, não o genérico
- 3 parágrafos mínimo no `.oque-text`
- `.oque-img` com placeholder descritivo em PT-BR
- Opcional: `.dj-callout` para diferenciação de serviço relacionado

### 4. CARDS (6 H3)
- 6 cards obrigatórios
- Cada card: `.card-icon` + `<h3 class="card-title">` + `<p class="card-text">`
- H3 = entregável (o que o cliente RECEBE), não processo
- Grid com scroll carousel em mobile (`.scroll-carousel`)

### 5. FORM multi-step
- Fundo escuro com `.form-mesh` e `.form-noise`
- H2 fixo: "Sua festa está a uma mensagem de distância."
- 3 a 4 passos + tela de confirmação (step 5)
- Passo final: nome + WhatsApp + botão enviar
- `.form-promises`: 3 bullets (sem compromisso, resposta 2h, proposta personalizada)
- Botão enviar abre WhatsApp: `https://wa.me/5511984049485`

### 6. GALERIA
- **CSS galeria-item desktop:** `flex: 0 0 calc(33.333% - 11px); height: 220px`
- **CSS galeria-item mobile (max-width:640px):** `flex: 0 0 76vw; height: 180px`
- 6 items com `data-lb-type`, `data-lb-src`, `data-lb-caption`, `onclick="lbOpen(this)"`
- Cada item: `.galeria-item-inner` (SVG + span) + `.galeria-overlay`
- H2 com `class="section-title section-title-white"` (fundo escuro)

### 7. EQUIP (4 cards)
- Fundo escuro (`.equipamento-section`)
- H2 com `section-title-white`
- 4 cards: `.equip-icon` + `<h3 class="equip-title">` + `.equip-text`
- Conteúdo: equipamento físico que o profissional leva (som, luz, microfone, etc.)

### 8. DIFERENCIAIS (4 cards)
- Fundo branco/claro
- 4 cards: `.dif-icon` + `<h3 class="dif-title">` + `.dif-text`
- Os 4 diferenciais fixos da Agita Morango:
  1. Formação profissional (recreador formado)
  2. Reposição garantida (substituto sem custo)
  3. Nota fiscal e seguro
  4. Adaptação por faixa etária / especificidade do serviço

### 9. DEPOIMENTOS (3 cards)
- `.depo-section` com fundo claro
- 3 cards: `.depo-stars` (★★★★★) + `.depo-text` (aspas) + `.depo-author` + `.depo-location`
- Localizações reais de SP (bairro + cidade)
- **Sem travessão (—)**

### 10. E-E-A-T
- `.eeat-section` com fundo escuro
- H2 fixo: **"15 anos animando festas infantis em São Paulo"**
- `.eeat-text`: 3 parágrafos fixos:
  1. "A Agita Morango é uma empresa especializada... fundada em 2009..."
  2. "[Serviço] faz parte do portfólio... profissionais com dupla formação... link para `/equipe-de-recreadores-infantis-em-sao-paulo/`"
  3. "Todos os contratos incluem nota fiscal, seguro... atende eventos particulares e corporativos"
- `.eeat-stats` 4 stats fixos: **15+** anos / **12k** famílias / **4.9** estrelas (620 reviews) / **NF** nota fiscal

### 11. RELACIONADOS (3 cards)
- 3 cards: `<h3 class="rel-card-title">` + `.rel-card-text` + `.rel-card-link` (com "→")
- Serviços que complementam (não concorrem) com a página atual
- Links internos reais

### 12. FAQ (5 perguntas H3)
- `<div class="faq-list" role="list">`
- 5 `<div class="faq-item" role="listitem">`
- **Cada pergunta: `<button class="faq-question">` contendo `<h3>texto</h3>` + `<span class="faq-icon">▾</span>`**
- `<div class="faq-answer" hidden>` após o button
- 5 temas obrigatórios: equipamento/material | vs concorrente | contratação avulsa | limitações técnicas | cobertura geo
- Mencionar "Agita Morango" pelo nome nas respostas
- JS: `function toggleFaq(btn)` — ver código padrão abaixo

### 13. ONDE ESTAMOS
- `.onde-estamos` com `.onde-mesh` (fundo escuro com textura)
- H2: "Baseados em SP, levamos [serviço] para toda a Grande SP"
- `.onde-mapa`: iframe Google Maps (Rua Imaculada, 291, SP)
- `.onde-info`: 4 rows (Endereço, WhatsApp, Atendimento, Área de Atuação)
- `.onde-cidades`: tags das cidades atendidas (SP, Guarulhos, Osasco, Alphaville, Barueri, ABC)
- `.btn-onde` WhatsApp com ícone SVG

### 14. FOOTER
- 5 colunas: brand-col + Para Festas + Para Empresas + Serviços + Sobre Nós
- Links idênticos em todas as páginas
- Copyright: `&copy; 2026` (nunca 2025)
- `.footer-wordmark` com "Agita Morango"

### LIGHTBOX (fora do `<main>`, antes do footer ou após)
- `<div id="lbBackdrop" style="display:none;position:fixed;...">` — nunca usar `display:flex` inicial
- Botão fechar + `id="lbPrev"` + `id="lbNext"` + `id="lbImg"` + `id="lbIframe"` + `id="lbCaption"` + `id="lbCounter"`
- JS obrigatório: `lbBuild()`, `lbShow(idx)`, `lbOpen(el)`, `lbNav(dir)`, `lbClose()` + keyboard handler

---

## JS padrão — FAQ toggleFaq

```js
function toggleFaq(btn) {
  var expanded = btn.getAttribute('aria-expanded') === 'true';
  btn.setAttribute('aria-expanded', String(!expanded));
  var answer = btn.nextElementSibling;
  if (answer) { answer.hidden = expanded; }
}
```

## JS padrão — Lightbox

```js
var lbItems = [], lbIndex = 0;
function lbBuild() { lbItems = Array.from(document.querySelectorAll('.galeria-item[data-lb-type]')); }
function lbShow(idx) {
  if (!lbItems.length) lbBuild();
  lbIndex = (idx + lbItems.length) % lbItems.length;
  var el = lbItems[lbIndex];
  var type = el.dataset.lbType;
  var bd = document.getElementById('lbBackdrop');
  document.getElementById('lbCaption').textContent = el.dataset.lbCaption || '';
  document.getElementById('lbCounter').textContent = (lbIndex + 1) + ' / ' + lbItems.length;
  var img = document.getElementById('lbImg');
  var ifr = document.getElementById('lbIframe');
  if (type === 'video') {
    img.style.display = 'none'; ifr.style.display = 'block';
    ifr.src = el.dataset.lbSrc;
  } else {
    ifr.style.display = 'none'; ifr.src = '';
    img.style.display = 'block'; img.src = el.dataset.lbSrc;
    img.alt = el.dataset.lbCaption || '';
  }
  document.getElementById('lbPrev').style.display = lbItems.length > 1 ? 'flex' : 'none';
  document.getElementById('lbNext').style.display = lbItems.length > 1 ? 'flex' : 'none';
  bd.style.display = 'flex'; document.body.style.overflow = 'hidden';
}
function lbOpen(el) { if (!lbItems.length) lbBuild(); lbShow(lbItems.indexOf(el)); }
function lbNav(dir) { lbShow(lbIndex + dir); }
function lbClose() {
  var bd = document.getElementById('lbBackdrop');
  bd.style.display = 'none'; document.body.style.overflow = '';
  var ifr = document.getElementById('lbIframe'); ifr.src = ''; ifr.style.display = 'none';
  document.getElementById('lbImg').style.display = 'block';
}
document.addEventListener('keydown', function(e) {
  var bd = document.getElementById('lbBackdrop');
  if (bd.style.display === 'none') return;
  if (e.key === 'Escape') lbClose();
  if (e.key === 'ArrowLeft') lbNav(-1);
  if (e.key === 'ArrowRight') lbNav(1);
});
```

---

## CSS crítico que não pode faltar

```css
/* Galeria */
.galeria-item { flex: 0 0 calc(33.333% - 11px); height: 220px; border-radius: 14px; overflow: hidden; background: #333; position: relative; cursor: pointer; }
.galeria-item img { width: 100%; height: 100%; object-fit: cover; }
@media (max-width: 640px) {
  .galeria-item { flex: 0 0 76vw; height: 180px; }
}

/* Hero card label (nunca h3 dentro de hero-card) */
.hero-card-label { font-family: 'League Spartan', sans-serif; font-size: 1.1rem; color: #fff; margin-bottom: 20px; display: block; }
```

---

## Seções opcionais/exclusivas por página

Algumas páginas têm seções exclusivas que NÃO substituem as obrigatórias — são inseridas após a seção CARDS (posição 4) ou após DEPOIMENTOS (posição 9):

| Página | Seção exclusiva | Posição |
|---|---|---|
| `baladinha-kids-infantil-em-sp/` | SETLIST (`.setlist-section`) | após CARDS |
| `dj-infantil-para-festas-em-sao-paulo/` | FICHA TÉCNICA (`.ficha-tecnica`) | dentro de O QUE É |
| Páginas geo | CONTEXTO LOCAL (bairros/tiles) | antes de ONDE ESTAMOS |

---

## Status das páginas (atualizar após cada edição)

| Página | Hero | BC | Oque | Cards | Form | Galeria | Equip | Dif | Depo | EEAT | Rel | FAQ | Onde | LB | Copyright |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `dj-infantil-para-festas-em-sao-paulo/` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅(5) | ✅ | ✅ | ✅2026 |
| `festa-do-pijama-em-sao-paulo/` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅(5) | ✅ | ✅ | ✅2026 |
| `baladinha-kids-infantil-em-sp/` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅(5) | ✅ | ✅ | ✅2026 |
| `oficinas-criativas-infantis-em-sp/` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅(5) | ✅ | ✅ | ✅2026 |
| `espaco-baby-para-festa-sp/` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅(5) | ✅ | ✅ | ✅2026 |
| `animacao-infantil-para-festas-em-sp/` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅(5) | ✅ | ✅ | ✅2026 |
| `equipe-de-recreadores-infantis-em-sao-paulo/` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅(5) | ✅ | ✅ | ✅2026 |
| `aniversario-infantil-em-sao-paulo/` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅(5) | ✅ | ✅ | ✅2026 |
| `colonia-de-ferias-infantil-sp/` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅(5) | ✅ | ✅ | ✅2026 |
| `dia-das-criancas-em-sao-paulo/` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅(5) | ✅ | ✅ | ✅2026 |
| `festa-das-cores-em-sao-paulo/` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅(5) | ✅ | ✅ | ✅2026 |
| `carnaval-infantil-em-sao-paulo/` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅(5) | ✅ | ✅ | ✅2026 |
| `halloween-para-festas-e-eventos-em-sao-paulo/` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅(5) | ✅ | ✅ | ✅2026 |
| `natal-infantil-para-festas-e-eventos-em-sao-paulo/` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅(5) | ✅ | ✅ | ✅2026 |
| `pascoa-para-festas-e-eventos-em-sao-paulo/` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅(5) | ✅ | ✅ | ✅2026 |
| `festa-de-ano-novo-infantil-em-sao-paulo/` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅(5) | ✅ | ✅ | ✅2026 |
| `festa-junina-infantil-em-sao-paulo/` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅(5) | ✅ | ✅ | ✅2026 |
| `show-musical-infantil-em-sao-paulo/` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅(5) | ✅ | ✅ | ✅2026 |
| `personagens-para-festas-infantis-em-sao-paulo/` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅(5) | ✅ | ✅ | ✅2026 |
| `camarim-infantil-para-festas-em-sao-paulo/` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅(5) | ✅ | ✅ | ✅2026 |
| `festas-tematicas-em-sao-paulo/` | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅(5) | ✅ | ✅ | ✅2026 |

> Legenda: ✅ OK | ❌ Faltando | ⚠️ Problema

---

## Workflow de edição (seguir sempre)

1. Abrir esta tabela de status
2. Identificar ❌ na linha da página
3. Para cada ❌: copiar o bloco HTML da página de referência (`dj-infantil-para-festas-em-sao-paulo/`)
4. Adaptar copy para o serviço da página (trocar nome do serviço, H2, H3s, textos)
5. Manter CSS class names idênticos — nunca inventar classes novas
6. Atualizar a tabela de status
7. Rodar `node upload-all.mjs --dry-run` e confirmar 0 erros antes de subir
