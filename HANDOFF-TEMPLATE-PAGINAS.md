# Handoff Note — Template de Página de Serviço (Referência: DJ Infantil)

**Arquivo piloto:** `dj-infantil-para-festas-em-sao-paulo/index.html`
**URL R2:** `https://pub-bd2efcc812524f54a8c492f90052f3bd.r2.dev/agita-morango/dj-infantil-para-festas-em-sao-paulo/index.html`

---

## Estrutura de Seções (ordem obrigatória)

| # | ID / Anchor | H-tag | Texto de referência (DJ Infantil) | Adaptação para outras páginas |
|---|---|---|---|---|
| 1 | `hero` | H1 | "DJ Infantil para **Festas em SP**" | Substitua "DJ Infantil" pelo serviço e "Festas em SP" pelo contexto |
| 2 | breadcrumb | — | Home › Servicos › DJ Infantil | Atualizar cada nível |
| 3 | `#oque-title` | H2 | "O que faz o DJ infantil profissional" | "O que é [serviço] profissional" |
| 4 | `#cards-title` + H3s | H2 + H3 | "Tudo que o DJ infantil entrega na sua festa" + 6 cards com H3 | Trocar por 6 entregas do serviço |
| 5 | `#form-title` | H2 | "Sua festa esta a uma mensagem de distancia." | Igual em todas as páginas |
| 6 | `#galeria-title` | H2 | "DJ Infantil Agita Morango em Acao" | "[Serviço] Agita Morango em Ação" |
| 7 | `#equip-title` + H3s | H2 + H3 | "Equipamento profissional incluso" + 4 itens H3 | Adaptar para recursos/materiais do serviço |
| 8 | `#dif-title` + H3s | H2 + H3 | "Diferenciais do DJ Infantil Agita Morango" + 4 H3s | Mesmos 4 diferenciais (reposição, NF, formação, faixa etária) |
| 9 | `#depo-title` | H2 | "O que os pais falam do DJ Infantil" | "O que os pais falam de [serviço]" |
| 10 | `#eeat-title` | H2 | "15 anos animando festas infantis em Sao Paulo" | Igual em todas as páginas (E-E-A-T da empresa) |
| 11 | `#rel-title` | H2 | "Servicos que combinam com o DJ Infantil" | Trocar pelos serviços relacionados corretos |
| 12 | `#faq-title` + H3s | H2 + H3s | "Perguntas sobre o DJ Infantil" + 5 H3s de FAQ | 5 perguntas reais do serviço (não genéricas) |
| 13 | `#onde-title` | H2 | "Baseados em SP, levamos o DJ para toda a Grande SP" | Igual em todas as páginas |
| 14 | footer H4s | H4 | Para Festas / Para Empresas / Servicos / Sobre Nos | Igual em todas as páginas |

---

## Hero — Anatomia

```html
<div class="hero-badge">🎧 [Emoji] [Credencial curta do serviço]</div>
<h1>NOME DO SERVIÇO para <span>CONTEXTO (ex: Festas em SP)</span></h1>
<p class="hero-sub">
  Descrição em 2-3 linhas com: o QUE entrega, COMO diferencia, RESULTADO emocional.
  Sem jargão. Termina com verbo de transformação.
</p>
<div class="hero-btns">
  <a href="https://wa.me/5511984049485..." class="btn-hero btn-hero-primary">Solicitar [SERVIÇO]</a>
  <a href="#o-que-inclui" class="btn-hero btn-hero-outline">O que está incluso</a>
</div>
```

**Hero-card (direita):** 4 stats visuais — use emojis + label. DJ usa: 🔊 som / 💡 luzes / 🎤 mic / 4.9 avaliação.
Para outros serviços: adaptar para o que é visualmente "entregável" daquele serviço.

---

## Seção E-E-A-T — COPY FIXO (copiar igual em todas as páginas)

```html
<div class="section-label">Quem é a Agita Morango</div>
<h2 id="eeat-title" class="section-title">15 anos animando festas infantis em Sao Paulo</h2>
```

**3 parágrafos fixos:**
1. Empresa fundada em 2009, foco 3–12 anos, +15 anos de consistência.
2. Serviço específico operado por profissionais com dupla formação (técnica + recreação). Link para /equipe-de-recreadores-infantis-em-sao-paulo/
3. Nota fiscal + seguro civil + garantia de reposição. Atende festas e corporativo.

**4 stats fixos:** `15+` anos / `12k` famílias / `4.9` avaliação (620 reviews) / `NF` nota fiscal + seguro

---

## FAQ — Regras de construção

- **Quantidade:** 5 perguntas por página
- **Tag:** cada pergunta = `<h3>` dentro de `.faq-item`
- **Padrão:** 1 pergunta sobre equipamento/material, 1 sobre diferença vs concorrente, 1 sobre contratação avulsa, 1 sobre limitações (volume/tempo/área), 1 sobre abrangência geográfica
- **Schema JSON-LD:** `"@type": "FAQPage"` com todas as 5 perguntas no `<head>`
- Respostas: 2–4 frases. Mencionar Agita Morango pelo nome. Terminar com ação suave ("entre em contato").

---

## Galeria — Regra

- **Estrutura:** grid `3 colunas` desktop, `2 colunas` tablet, `1 coluna` mobile
- **Item destacado:** `grid-column: 1 / 3` (item 1 ocupa 2 colunas)
- **Placeholder atual:** SVGs cinzas com ícone de foto + label descritivo
- **Quando tiver fotos reais:** substituir SVG por `<img src="..." loading="lazy" alt="[descrição SEO]">`
- **Itens de vídeo:** classe `.is-video` com `play-btn`

---

## Cards "O que inclui" — 6 cards com H3

Padrão de cada card:
```html
<div class="card">
  <div class="card-icon">[EMOJI]</div>
  <h3 class="card-title">[NOME DO ENTREGÁVEL]</h3>
  <p class="card-desc">[1 frase de benefício]</p>
</div>
```

**Regra:** o card-title (H3) deve ser o **entregável** (o que o cliente recebe), não o processo.
Exemplo correto: "Mix de hits infantis ao vivo" — não: "Seleção musical"

---

## Relacionados — Regra de linkagem

- 4 a 6 cards de serviços complementares
- Cada card linka para outra página do site
- **Regra:** nunca linkar para o serviço da própria página; escolher serviços que naturalmente vêm juntos na mesma contratação
- Exemplo DJ: Animação → Baladinha Kids → Personagens → Espaço Baby

---

## Breadcrumb — padrão

```html
Home › Servicos › [NOME DA PÁGINA]
/        /empresa-de-recreacao-em-sao-paulo/    [slug-da-pagina]/
```

Para páginas corporativas: `Home › Corporativo › [NOME]`
Para blog: `Home › Blog › [TÍTULO DO ARTIGO]`

---

## Schema JSON-LD — checklist

No `<head>` de cada página de serviço:
- [ ] `BreadcrumbList` com 3 níveis
- [ ] `FAQPage` com 5 Q&A
- [ ] `LocalBusiness` ou `Service` (se ainda não tiver)

---

## Diferenciais — copy fixo (sempre os mesmos 4 H3s)

```
H3: DJ e recreador formado → [Profissional e recreador formado] → adaptado para cada serviço
H3: Reposição garantida   → cópia igual
H3: Nota fiscal e seguro  → cópia igual
H3: Adaptado por faixa etária → cópia igual
```

Apenas o primeiro H3 muda — adaptar para o tipo de profissional do serviço.

---

## Seção "Onde estamos" — copy fixo

H2 fixo: "Baseados em SP, levamos o [SERVIÇO] para toda a Grande SP"
Grid de bairros/regiões: sempre os mesmos 8-12 tiles de localização.

---

## Tokens de design — referência rápida

| Token | Valor |
|---|---|
| `--verde` | `#4aa702` |
| `--vermelho` | `#9d0505` |
| `--carvao-deep` | `#1a1a1a` |
| Fonte título | League Spartan 900 |
| Fonte corpo | Bree Serif |
| Fonte destaque itálico | Lora italic |

---

## Checklist antes de publicar

- [ ] H1 contém keyword principal (serviço + SP ou variante geo)
- [ ] H2s não repetem entre si
- [ ] H3s de FAQ são perguntas reais (testadas no Google Suggest)
- [ ] E-E-A-T está igual ao piloto (mesmos 3 parágrafos, mesmos stats)
- [ ] Breadcrumb atualizado
- [ ] `<title>` e `<meta description>` presentes
- [ ] Schema FAQPage no head
- [ ] Galeria com alt text descritivo em cada item
- [ ] Link para /equipe-de-recreadores-infantis-em-sao-paulo/ na seção E-E-A-T
- [ ] CTAs do footer e megamenu apontam para URLs corretas
- [ ] `node upload-all.mjs --dry-run` antes de subir
