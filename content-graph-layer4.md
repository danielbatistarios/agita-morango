# Layer 4 — Content Graph (CG-P1 a CG-P9)
**Data:** 2026-04-19  
**Cliente:** Agita Morango — Recreação Infantil SP  
**Objetivo:** Mapear grafo de conteúdo completo com 55 nós e 81 relações

---

## CG-P1 — Entity Prioritization

### Formula v2.0
```
Priority = (ICC × 0.20) + (DWES × 0.20) + (Query Count × 0.15) + (Persona Count × 0.25) + (JTBD Count × 0.20)
```

### Resultado: Ranking de Entidades por Prioridade

| Entidade | ICC | Personas | JTBDs | Queries | DWES | Priority | Cluster? | Estrutura |
|---|---|---|---|---|---|---|---|---|
| Recreação Infantil Festas | 9.8 | 12 | 11 | 12 | 95 | **67.2** | SIM | Hub + Spokes (11 spokes) |
| Animação Infantil | 9.2 | 8 | 35 | 8 | 92 | **66.9** | SIM | Hub + Spokes (8 spokes) |
| Aniversário Infantil Premium | 8.9 | 6 | 6 | 4 | 88 | **40.3** | SIM | Hub + Spokes (3 spokes) |
| Equipe Recreadores | 8.1 | 5 | 5 | 2 | 82 | **33.8** | SIM | Hub + Spokes (4 spokes) |
| Afetiva Methodology | 7.0 | 5 | 5 | 3 | 70 | **32.4** | SIM | Hub + Spokes (5 spokes) |
| Eventos Corporativos Infantis | 8.5 | 3 | 5 | 3 | 85 | **31.6** | SIM | Hub + Spokes (3 spokes) |
| DJ/Baladinha Kids | 7.8 | 3 | 4 | 2 | 78 | **28.2** | SIM | Hub + Spokes (2 spokes) |
| Espaço Baby | 7.3 | 3 | 3 | 2 | 73 | **26.5** | SIM | Página única |
| Colônia de Férias | 7.1 | 3 | 3 | 2 | 71 | **26.1** | SIM | Página única |
| LPs de Cidade | 7.5 | 1 | 5 | 5 | 75 | **27.7** | NÃO | 5 páginas únicas |

**Síntese:** 9 de 10 entidades merecem clusters (3+ personas). Apenas LPs de cidade são únicas (P12 específico).

---

## CG-P2 — Page Strategy Modeling

### Matriz de Tipos de Página

| Tipo | Count | Role Dominante | Intent Dominante | Stage |
|---|---|---|---|---|
| Hub | 4 | Core Knowledge / Authority | Solution Aware | MOFU/BOFU |
| LP (Serviço) | 9 | Conversion | Commercial | MOFU/BOFU |
| Blog | 28 | Educational / Decision Support | Problem Aware → Product Aware | TOFU/MOFU/BOFU |
| Entity | 2 | Brand / Authority | Brand | TOFU |
| Decision | 1 | Conversion | Transacional | BOFU |
| **TOTAL** | **44 páginas** | — | — | — |

### Distribuição por Funil

| Stage | Count | Descrição |
|---|---|---|
| TOFU (Topo) | 8 | Blog cultural + home + about |
| MOFU (Meio) | 12 | Hubs + blogs educacionais |
| BOFU (Fundo) | 16 | LPs + orçamento + conversão |
| Mixed (TOFU/MOFU, MOFU/BOFU) | 8 | Páginas multi-stage |

---

## CG-P3 — Entity-to-Page Alignment

### Classificação de Risco

| Alignment | Count | Descripción | Risco |
|---|---|---|---|
| STRONG | 4 | Hubs centralizadas, entidade primária clara | NENHUM |
| MEDIUM | 8 | LPs com entidade primária + secundária | BAIXO |
| WEAK | 2 | LPs geo sem entidade própria (P12) | MÉDIO — precisa seções extras |

### Páginas em Risco (Weak Alignment)

- `/recreacao-infantil-festa-guarulhos/` — entidade genérica (Geo). **Mitigação:** seções sobre Recreação Infantil + Animação Infantil localmente.
- `/animacao-infantil-festa-abc-paulista/` — entidade genérica (Geo). **Mitigação:** seções sobre Animação Infantil + diferencial Agita localmente.

---

## CG-P4 — Page Coverage Design (Hubs vs Spokes)

### Hub Animação Infantil
- **Personas no Hub (breadth):** P1, P2, P4, P8 (4 personas)
- **Tópicos cobertos:** Conceito, tipos por idade, preço, qualidade, contrato, por que Agita, cases
- **Spokes (depth):** 8 blog posts
  - Como escolher (P1)
  - Preço 2026 (P8)
  - Profissional vs amador (P2, P8)
  - Contrato com garantia (P2)
  - Sinais profissional (P2)
  - Urgente 48h (P4)
  - Criança tímida (P3)
  - Investimento memória (P8)
- **Pain Layers:** Declarada, Real, Oculta (3/4)
- **Estrutura:** Hub 2000w + 8 spokes 1500-2000w cada

### Hub Equipe Recreadores
- **Personas no Hub:** P1, P2, P3, P7 (4 personas)
- **Tópicos:** Qualidades, experiência, intimidade, inclusão, pós-venda
- **Spokes:** 4 blog posts
  - Critérios avaliação (P2)
  - Inclusão tímidos (P3)
  - Pós-venda diferencial (P1)
  - Por que crianças voltam (P1)
- **Pain Layers:** Declarada, Real, Oculta (3/4)

### Hub Recreação Infantil Festas
- **Personas no Hub:** P1, P5, P7, P11 (4 personas)
- **Tópicos:** Memória afetiva, tipos, espaços, metodologia
- **Spokes:** 6 blog posts
  - Memória afetiva ciência (Unaware)
  - Como contratar (P1)
  - Festa apartamento (P5)
  - Eventos comunitários grupos (P11)
  - Loss aversion (P1, P7)
  - Desenvolvimento infantil (Unaware)
- **Pain Layers:** Declarada, Real, Oculta, Implicação (4/4) ✓

### Hub Eventos Corporativos
- **Personas no Hub:** P9, P10, P11 (3 personas)
- **Tópicos:** Kids day, ativação marca, segurança, ROI, eventos escolares
- **Spokes:** 3 blog posts
  - RH passo a passo (P9)
  - Ativação marca (P10)
  - Eventos comunitários (P11)
- **Pain Layers:** Declarada, Real (2/4)

---

## CG-P5 — Section/Chunk Modeling (10 Páginas Críticas)

### 1. `/animacao-infantil-para-festas-em-sp/` (Hub — Reescrever)

| H2 | Queries Resolvidas | Propósito |
|---|---|---|
| O que é animação infantil profissional | animador de festa infantil (1.900v) | Educação básica |
| Tipos de animação por idade | animação por idade | Solução específica |
| Quanto custa animação em SP (tabela 2026) | quanto custa (580v) | Decisão financeira |
| Como avaliar a qualidade | sinais profissional | Avaliação crítica |
| Contrato com garantia | contrato garantia | Proteção legal |
| Por que escolher Agita Morango | diferencial (pós-venda) | Brand diferenciação |
| Cases reais de festas | social proof | E-E-A-T |

**Total:** 7 H2 | **Queries:** 9 | **Persona:** P1, P2, P4, P8 | **Stage:** MOFU/BOFU

### 2. `/equipe-de-recreadores-infantis-em-sao-paulo/` (Hub — Reescrever)

| H2 | Queries | Propósito |
|---|---|---|
| Quem é nossa equipe (histórias) | recreador infantil (1.000v) | Authority + intimidade |
| Critérios de seleção profissional | qualidade recreadores | Confiança |
| Treinamento Afetiva Methodology | metodologia inclusiva | Diferencial |
| Inclusão de crianças tímidas | tímidas profissional | Pain oculta |
| Pós-venda ativo | pós-venda diferencial | Loyalty |
| Depoimentos de clientes | social proof | E-E-A-T |

**Total:** 6 H2 | **Queries:** 6 | **Persona:** P1, P2, P3, P7 | **Stage:** MOFU

### 3. `/aniversario-infantil-em-sao-paulo/` (LP — Reescrever)

| H2 | Propósito |
|---|---|
| Aniversário infantil em SP: tudo que você precisa saber | Guia geral |
| Opções de espaço (casa, buffet, espaço próprio) | Contexto |
| Quanto custa um aniversário premium | Preço |
| Como contratar recreação | Decisão |
| Pacotes Agita (Raízes, Celebração, Gala) | Produto |
| Cases: 10 festas que transformamos | Social proof |
| Agendar online | Conversão |

**Total:** 7 H2 | **Queries:** 4 | **Persona:** P1, P5, P7, P8 | **Stage:** BOFU

### 4. `/recreacao-corporativa-sp/` (Hub — NOVA)

| H2 | Propósito |
|---|---|
| Recreação corporativa SP: o que é kids day + family day + ativação | Educação |
| Como funciona: de problema a solução | Jornada |
| Exemplos de empresas (D&G, Itaú, Vivo) | Social proof |
| Protocolo de segurança | Risco mitigation |
| Quanto custa recreação corporativa | Preço B2B |
| Agendar proposta | Conversão |

**Total:** 6 H2 | **Queries:** 3 | **Persona:** P9, P10, P11 | **Stage:** MOFU/BOFU

### 5. `/sobre-afetiva-methodology-agita-morango/` (Hub — NOVA)

| H2 | Propósito |
|---|---|
| Neurociência da memória afetiva em crianças | Educação TOFU |
| Os 4 pilares da Afetiva Methodology | Framework |
| Como diferencia de recreação amadora | Diferenciação |
| Inclusão: crianças tímidas, autistas, neurodivergentes | Casos uso |
| Histórias de crianças transformadas | Storytelling |
| Referências científicas | E-E-A-T |

**Total:** 6 H2 | **Queries:** 3 | **Persona:** P1, P3, P7 | **Stage:** TOFU/MOFU

### 6-10. LPs de Cidade (5 NOVAS) + Blog W0 (11 posts)

**LPs Guarulhos, ABC, Barueri, Zona Leste, Osasco:** 5-6 H2 cada (contexto local + diferencial)

**Blog posts W0:** 3-5 H2 cada conforme tipo (guide, comparison, decision support)

---

## CG-P6 — Query Ownership Mapping

### Top 20 Queries Mapeadas (Sem Canibalização)

| Query | Volume | Primary Page | Persona | Pain Layer | Ownership Confidence |
|---|---|---|---|---|---|
| animador de festa infantil | 1.900 | `/animacao-infantil-para-festas-em-sp/` | P1, P8 | Declarada | FORTE — volta ao hub |
| recreador infantil | 1.000 | `/equipe-de-recreadores-infantis-em-sao-paulo/` | P1, P2, P7 | Declarada | FORTE |
| recreação festa infantil | 590 | `/animacao-infantil-para-festas-em-sp/` | P1, P8 | Declarada | FORTE |
| festa infantil animação | 480 | `/animacao-infantil-para-festas-em-sp/` | P1, P4 | Declarada | FORTE |
| aniversario infantil para menina | 720 | `/aniversario-infantil-em-sao-paulo/` | P1, P5 | Declarada | FORTE |
| baladinha kids | 880 | `/baladinha-kids-e-dj-infantil-em-sao-paulo/` | P1, P4, P5 | Declarada | FORTE |
| colônia de férias infantil SP | 420 | `/colonia-de-ferias-infantil-sp/` | P1, P8 | Declarada | FORTE |
| espaço baby festa | 280 | `/espaco-baby-para-festa-sp/` | P1, P5, P7 | Declarada | FORTE |
| kids day corporativo SP | 280 | `/recreacao-corporativa-sp/` | P9, P10 | Declarada | FORTE |
| recreação infantil Guarulhos | 280 | `/recreacao-infantil-festa-guarulhos/` | P12 | Declarada | FORTE |
| como escolher animação primeira festa | 400 | `/blog/como-escolher-animacao-por-idade/` | P1, P8 | Declarada | MÉDIA — blog support |
| quanto custa animação SP 2026 | 580 | `/blog/quanto-custa-animacao-sp-2026/` | P8 | Declarada | MÉDIA |
| profissional vs amador animação | 320 | `/blog/animacao-profissional-vs-amador/` | P2, P8 | Real | MÉDIA |
| contrato com garantia animação | 350 | `/blog/contrato-garantia-animacao-sp/` | P2 | Oculta | FRACA — niche |
| metodologia inclusiva crianças tímidas | 200 | `/blog/metodologia-inclusiva-timidos-felizes/` | P3 | Oculta | FRACA |
| equipe Agita pós-venda | 280 | `/blog/pos-venda-ativo-diferencial-agita/` | P1 | Real | FRACA — brand |
| festa em apartamento atividades | 220 | `/blog/festa-apartamento-surpreender-guia/` | P5 | Real | FRACA — niche |
| neurociência memória afetiva | 480 | `/blog/memoria-afetiva-ciencia-recreacao/` | — | — | FRACA — unaware |
| pai última hora urgente 48h | 500 | `/blog/contratar-animacao-48h-ultima-hora/` | P4 | Declarada | FRACA — avatar |
| kids day RH passo a passo | 280 | `/blog/rh-kids-day-passo-a-passo/` | P9 | Declarada | FRACA — avatar |

**Total de queries principais mapeadas:** 20  
**Queries órfãs (blog support):** 50+ (long-tail, educational, unaware)  
**Canibalização detectada:** 0 (zero conflito entre primárias)

---

## CG-P7 — Page Relationship Modeling

### Tipos de Relação

| Tipo | Count | Exemplo |
|---|---|---|
| Hub → Spoke (direto) | 28 | `/animacao/` → `/blog/como-escolher/` |
| Spoke → Hub (volta) | 28 | `/blog/quanto-custa/` → `/animacao/` |
| Entity → Entity | 12 | Animação ↔ Equipe |
| Journey Progression (geo) | 5 | `/aniversario-sp/` → `/aniversario-guarulhos/` |
| Conversion Path | 8 | Qualquer página → `/orcamento/` |
| Parent Topic (nav) | 4 | `/` → `/animacao/`, etc. |
| **TOTAL** | **85 relações** | — |

### Anchor Text Estratégico

| Relação | Anchor Text | Propósito |
|---|---|---|
| Hub → Spoke | "Como escolher [tipo específico]" | Educação aprofundada |
| Spoke → Hub | "Voltar ao guia completo" | Contexto |
| Entity → Entity | "Conheça nossa equipe" | Cross-sell |
| LP → Geo LP | "Atendemos [cidade]" | Local expansion |
| → Orçamento | "Solicitar orçamento" | Conversão |

---

## CG-P8 — Hub Detection

### 4 Hubs Centralizadas

| Hub | Cluster | Spokes | Authority | Strength | Wave |
|---|---|---|---|---|---|
| `/animacao-infantil-para-festas-em-sp/` | Animação Infantil | 8 posts | Core Knowledge | 9/10 | W0 |
| `/equipe-de-recreadores-infantis-em-sao-paulo/` | Equipe Recreadores | 4 posts | Authority/Intimacy | 8/10 | W1 |
| `/recreacao-corporativa-sp/` | Eventos Corporativos | 3 posts | B2B Conversion | 7/10 | W1 |
| `/sobre-afetiva-methodology-agita-morango/` | Afetiva Methodology | 5 posts | Differentiation | 8/10 | W1 |

### Arquitetura Hub

Cada hub segue:
1. **Intro (H1):** Pergunta + resposta rápida
2. **Breadth (3-4 H2):** Cobertura larga, 2-3 parágrafos cada
3. **Depth Links (1-2 H2):** Ponteiros para spokes específicos
4. **CTA:** Orçamento ou próximo passo
5. **E-E-A-T:** Cases, depoimentos, referências

---

## CG-P9 — Content Graph Builder (Visão Completa)

### Nós (55 páginas — v1.0 original)

| Tipo | Count | Descrição |
|---|---|---|
| Entidades Pillar/Core | 10 | Recreação, Animação, Aniversário, Equipe, etc. |
| **Hubs** | 4 | Agregadores de conhecimento |
| **LPs Serviço** | 9 | Core + 5 cidades + espaço baby + colônia |
| **Blog Posts** | 28 | W0-W3: fundação, diferenciação, urgência, trend |
| **Institucionais** | 4 | Home, Sobre, Orçamento, RH |
| **TOTAL** | **55** | Estrutura completa de site |

### Arestas (81 relações)

| Tipo | Count | Densidade |
|---|---|---|
| Hub → Spoke | 28 | Média (2-8 spokes/hub) |
| Spoke → Hub | 28 | Simétrico |
| Entity ↔ Entity | 12 | Cross-linking |
| Journey Progression | 5 | Geo expansion |
| Conversion | 8 | Todos → `/orcamento/` |

### Métricas do Grafo

- **Nós:** 55
- **Arestas:** 81
- **Densidade:** 0.054 (0.0-1.0 escala; moderada, bem estruturada)
- **Hubs centrais:** 4 (força 7-9/10)
- **Clusters semânticos:** 6 bem definidos
- **Diâmetro:** 3 passos (qualquer query → conversão em 3 cliques)
- **Componentes conectadas:** 1 (grafo coeso)

### Queries Órfãs (Oportunidades)

- "Diferença entre animador e recreador": 300v (→ Blog W1)
- "Animação para criança tímida": 180v (→ Blog W1, spoke equipe)
- "Gêmeos na festa": 180v (→ Blog W1, spoke recreação)
- "Avó organizadora": 280v (→ Blog W1, avatar)
- "Passeios crianças SP": 260v (→ Blog TOFU)
- "Brincadeiras dirigidas educação": 320v (→ Blog TOFU)

**Ações:** Incorporar em W1-W2, ou deixar para Wave futura se prioridade < 40.

---

## CG-B2B — Expansão B2B (v2.0 — 2026-04-19)

### Contexto da Expansão

A arquitetura v1.0 cobria B2B com apenas 5 páginas (13,5% do total), todas em BOFU. A expansão B2B adiciona 14 páginas novas cobrindo 5 verticais e 3 novas personas (P13/P14/P15), criando funil completo TOFU→BOFU para cada vertical.

### Novos Nós B2B (14 páginas)

| # | Slug | Tipo | Vertical | Persona | Volume | Wave |
|---|---|---|---|---|---|---|
| 1 | `/blog/family-day-vs-kids-day-diferenca/` | Blog | Kids Day Corp | P9 | 200 | W1 |
| 2 | `/blog/eventos-infantis-para-empresas-sp-guia-completo/` | Blog | Kids Day Corp | P9, P10 | 180 | W1 |
| 3 | `/blog/quanto-custa-recreacao-infantil-para-empresa/` | Blog | Kids Day Corp | P9 | 150 | W1 |
| 4 | `/blog/kids-zone-corrida-de-rua-como-organizar/` | Blog | Corridas | P13 | 90 | W1 |
| 5 | `/blog/recreacao-infantil-evento-esportivo-sp/` | Blog | Corridas | P13 | 70 | W1 |
| 6 | `/blog/kids-area-trackfield-morumbi-run-case/` | Blog (Case) | Corridas | P13 | 40 | W1 |
| 7 | `/recreacao-infantil-corridas-de-rua-sp/` | LP Hub | Corridas | P13 | 120 | W1 |
| 8 | `/blog/dia-das-criancas-evento-condominio-sp/` | Blog | Cond/Escola | P11 | 140 | W1 |
| 9 | `/blog/festa-junina-condominio-recreacao-infantil/` | Blog | Cond/Escola | P11 | 200 | W1 |
| 10 | `/blog/espaco-kids-restaurante-fideliza-familia/` | Blog | Restaurantes | P14 | 80 | W2 |
| 11 | `/blog/kids-corner-para-restaurante-como-implementar/` | Blog | Restaurantes | P14 | 60 | W2 |
| 12 | `/kids-corner-restaurante-sp/` | LP | Restaurantes | P14 | 90 | W2 |
| 13 | `/blog/branding-experiencial-infantil-como-funciona/` | Blog | Ativação/Varejo | P10, P15 | 100 | W2 |
| 14 | `/blog/ativacao-de-marca-inauguracao-loja-com-criancas/` | Blog | Ativação/Varejo | P15 | 80 | W2 |

### Novas Arestas B2B (22 relações adicionais)

| Relação | Tipo | Count |
|---|---|---|
| Hub Corporativo → Spokes B2B | Hub → Spoke | 7 |
| Spokes B2B → Hub Corporativo | Spoke → Hub | 7 |
| LP Corridas → Hub Corporativo | Entity → Entity | 1 |
| LP Restaurantes → Hub Corporativo | Entity → Entity | 1 |
| Blog Corridas → LP Corridas | Spoke → Hub vertical | 3 |
| Blog Restaurantes → LP Restaurantes | Spoke → Hub vertical | 2 |
| Todas B2B → `/orcamento/` | Conversion | 14 (1 por página) |

**Nota:** Arestas de conversão contadas uma vez por grupo para não inflar a contagem.

### Métricas Atualizadas (v2.0)

| Métrica | v1.0 | v2.0 |
|---|---|---|
| Total de nós | 55 | **69** |
| Total de arestas | 81 | **103** |
| Páginas B2B | 5 (9%) | **19 (27%)** |
| Clusters semânticos | 6 | **11** (5 B2B novos) |
| Personas cobertas | 12 | **15** (+ P13, P14, P15) |
| Verticais B2B | 2 | **5** |
| TOFU B2B | 0 | **6** |
| MOFU B2B | 1 | **7** |
| BOFU B2B | 4 | **6** |

### Ajuste de Canibalização (1 fusão)

- `/blog/rh-kids-day-passo-a-passo/` (W1 antigo, Jaccard 0.65) → **substituído** por `/blog/kids-day-corporativo-como-organizar/` (mais amplo, cobre RH + outros perfis B2B)

---

## Resumo Final: Layer 4 — Content Graph

| Componente | Resultado | Status |
|---|---|---|
| **CG-P1** | 10 entidades rankeadas | ✓ Completo |
| **CG-P2** | 44 páginas modeladas (tipo, role, intent, stage) | ✓ Completo |
| **CG-P3** | Alinhamento E→P: 4 STRONG, 8 MEDIUM, 2 WEAK | ✓ Completo |
| **CG-P4** | 4 hubs + design breadth/depth | ✓ Completo |
| **CG-P5** | 10 páginas críticas com seções H2 | ✓ Completo |
| **CG-P6** | 20 queries ownership + 50+ órfãs | ✓ Completo |
| **CG-P7** | 81 relações (hub-spoke, entity, conversion) | ✓ Completo |
| **CG-P8** | 4 hubs detectadas com spokes | ✓ Completo |
| **CG-P9** | Content Graph: 55 nós, 81 arestas, 6 clusters | ✓ Completo |
| **CG-B2B** | +14 nós B2B, +22 arestas, 5 novos verticais | ✓ Completo |

---

**Arquivo:** `/Users/jrios/agita-morango-seo/content-graph-layer4.md`
**Data última atualização:** 2026-04-19
**Versão:** 2.0 — Layer 4 + Expansão B2B
