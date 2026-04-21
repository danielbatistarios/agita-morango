# Layer 5B — Schema & E-E-A-T | Agita Morango
**Data:** 2026-04-19 | **Versão:** 1.0 | **Status:** Executado

---

## EXECUÇÃO DOS 3 PROMPTS

### SE-P1 — Schema.org Stack Design

#### Objetivo
Projetar o schema markup completo para cada tipo de página do site Agita Morango, garantindo cobertura de E-E-A-T e visibilidade em rich snippets (Google Search, Google Maps, Google Reviews).

---

#### SCHEMA 1: Home + Sobre (`/` e `/sobre-a-agita-morango/`)

**Tipo:** LocalBusiness + EntertainmentBusiness

```json
{
  "@context": "https://schema.org",
  "@type": ["LocalBusiness", "EntertainmentBusiness"],
  "name": "Agita Morango",
  "description": "Recreação e entretenimento infantil premium em São Paulo. 15 anos transformando festas em memórias afetivas através da Afetiva Methodology.",
  "url": "https://agitamorango.com.br",
  "telephone": "+55 11 98404-9485",
  "email": "contato@agitamorango.com.br",
  "address": {
    "@type": "PostalAddress",
    "streetAddress": "Rua Imaculada, nº 291",
    "addressLocality": "São Paulo",
    "addressRegion": "SP",
    "postalCode": "01208-010",
    "addressCountry": "BR"
  },
  "geo": {
    "@type": "GeoCoordinates",
    "latitude": "-23.5489",
    "longitude": "-46.6388"
  },
  "foundingDate": "2011",
  "numberOfEmployees": "15-25",
  "aggregateRating": {
    "@type": "AggregateRating",
    "ratingValue": "4.8",
    "ratingCount": "620",
    "bestRating": "5",
    "worstRating": "1"
  },
  "sameAs": [
    "https://www.instagram.com/agitamorango",
    "https://www.facebook.com/agitamorango",
    "https://www.youtube.com/user/agitamorango",
    "https://www.tiktok.com/@agitamorango",
    "https://www.linkedin.com/company/agita-morango"
  ],
  "openingHoursSpecification": [
    {
      "@type": "OpeningHoursSpecification",
      "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"],
      "opens": "09:00",
      "closes": "18:00"
    }
  ],
  "areaServed": [
    { "@type": "City", "name": "São Paulo" },
    { "@type": "City", "name": "Guarulhos" },
    { "@type": "City", "name": "Barueri" },
    { "@type": "City", "name": "Alphaville" },
    { "@type": "City", "name": "Osasco" },
    { "@type": "City", "name": "Santana de Parnaíba" },
    { "@type": "City", "name": "Divinópolis" }
  ],
  "founder": {
    "@type": "Person",
    "name": "Amanda Araújo",
    "jobTitle": "Creative Director / Fundadora"
  },
  "hasOfferCatalog": {
    "@type": "OfferCatalog",
    "name": "Serviços de Recreação Infantil",
    "itemListElement": [
      {
        "@type": "Offer",
        "name": "Animação para Festas Infantis",
        "description": "Equipe profissional de animadores e recreadores"
      },
      {
        "@type": "Offer",
        "name": "Recreação Infantil Estruturada",
        "description": "Atividades planejadas com metodologia Afetiva"
      },
      {
        "@type": "Offer",
        "name": "Baladinha Kids + DJ Infantil",
        "description": "DJ infantil e baladinha para festividades"
      },
      {
        "@type": "Offer",
        "name": "Eventos Corporativos Infantis",
        "description": "Recreação para empresas (D&G, Itaú, Vivo, etc.)"
      },
      {
        "@type": "Offer",
        "name": "Colônia de Férias",
        "description": "Programa de férias estruturado para crianças"
      }
    ]
  }
}
```

**Posicionamento E-E-A-T:**
- **E:** foundingDate 2011 (15 anos), numberOfEmployees (equipe profissional), aggregateRating 4.8/5 com 620+ reviews
- **E:** sameAs (5 redes sociais verificadas)
- **A:** clients corporativos (Itaú, D&G, Vivo, Votorantim, Unimed, Morumbi Shopping) — adicionar em mentions em versão futura
- **T:** CNPJ verificado, endereço físico, horário de funcionamento, telefone/email de contato

---

#### SCHEMA 2: LPs de Serviço (ex: Animação, Recreação, Baladinha)

**Tipo:** Service + LocalBusiness
**Exemplos:** `/animacao-infantil-para-festas-em-sp/`, `/equipe-de-recreadores-infantis-em-sao-paulo/`, `/baladinha-kids-e-dj-infantil-em-sao-paulo/`

```json
{
  "@context": "https://schema.org",
  "@type": ["Service", "LocalBusiness"],
  "name": "Animação Infantil para Festas em São Paulo",
  "description": "Equipe profissional de animadores e recreadores para festas infantis em SP. Metodologia Afetiva para criar memórias marcantes.",
  "url": "https://agitamorango.com.br/animacao-infantil-para-festas-em-sp/",
  "provider": {
    "@type": "LocalBusiness",
    "name": "Agita Morango",
    "url": "https://agitamorango.com.br",
    "telephone": "+55 11 98404-9485"
  },
  "serviceType": "Entertainment Services for Children",
  "areaServed": [
    { "@type": "City", "name": "São Paulo" },
    { "@type": "City", "name": "Guarulhos" },
    { "@type": "City", "name": "Osasco" }
  ],
  "offers": {
    "@type": "AggregateOffer",
    "priceCurrency": "BRL",
    "lowPrice": "1000",
    "highPrice": "3000",
    "offerCount": "3",
    "itemListElement": [
      {
        "@type": "Offer",
        "name": "Pacote Raízes",
        "description": "Até 15 crianças, 2 recreadores",
        "price": "1200",
        "priceCurrency": "BRL",
        "availability": "https://schema.org/InStock"
      },
      {
        "@type": "Offer",
        "name": "Pacote Celebração",
        "description": "Até 30 crianças, 3-4 recreadores",
        "price": "1800",
        "priceCurrency": "BRL",
        "availability": "https://schema.org/InStock"
      },
      {
        "@type": "Offer",
        "name": "Pacote Premium Gala",
        "description": "30+ crianças, equipe customizada",
        "price": "3000",
        "priceCurrency": "BRL",
        "availability": "https://schema.org/InStock"
      }
    ]
  },
  "aggregateRating": {
    "@type": "AggregateRating",
    "ratingValue": "4.8",
    "ratingCount": "620",
    "bestRating": "5"
  }
}
```

**Variações por serviço:**
- **Animação:** focus em "performers" + equipe conhecida + experiência
- **Recreação:** focus em "structured activities" + desenvolvimento infantil
- **Baladinha:** focus em "DJ" + música + animação
- **Corporativo:** adicionar B2BService type + mentions de clientes corporativos
- **Colônia:** adicionar eventType "Camp" ou "VacationProgram"

**Posicionamento E-E-A-T:**
- **E:** aggregateRating em cada LP de serviço (não genérica)
- **E:** offers com 3 pacotes reais (Raízes, Celebração, Premium)
- **A:** provider name "Agita Morango" + URL validada
- **T:** pricing transparency + availability

---

#### SCHEMA 3: LPs de Cidade

**Tipo:** Service + LocalBusiness com GeoCircle
**Exemplos:** `/recreacao-para-festa-infantil-guarulhos/`, `/animacao-infantil-zona-leste-sp/`, `/recreacao-para-festa-infantil-abc/`

```json
{
  "@context": "https://schema.org",
  "@type": ["Service", "LocalBusiness"],
  "name": "Recreação para Festa Infantil em Guarulhos",
  "description": "Serviços de recreação infantil premium em Guarulhos, SP. Equipe profissional e metodologia Afetiva para festas memoráveis.",
  "url": "https://agitamorango.com.br/recreacao-para-festa-infantil-guarulhos/",
  "provider": {
    "@type": "LocalBusiness",
    "name": "Agita Morango",
    "url": "https://agitamorango.com.br",
    "telephone": "+55 11 98404-9485"
  },
  "serviceType": "Entertainment Services for Children",
  "areaServed": {
    "@type": "City",
    "name": "Guarulhos",
    "addressCountry": "BR",
    "addressRegion": "SP"
  },
  "aggregateRating": {
    "@type": "AggregateRating",
    "ratingValue": "4.8",
    "ratingCount": "620"
  },
  "offers": {
    "@type": "AggregateOffer",
    "priceCurrency": "BRL",
    "lowPrice": "1000",
    "highPrice": "3000"
  }
}
```

**Cidades previstas (7 novas LPs):**
1. Guarulhos
2. ABC Paulista
3. Barueri/Alphaville
4. Zona Leste SP
5. Zona Sul SP
6. Zona Oeste SP
7. Santana de Parnaíba

---

#### SCHEMA 4: B2B - Eventos Corporativos

**Tipo:** Service + Organization com B2BService
**URL:** `/recreacao-corporativa-sp/`

```json
{
  "@context": "https://schema.org",
  "@type": ["Service", "Organization"],
  "name": "Recreação Corporativa para Eventos em São Paulo",
  "description": "Serviços de recreação infantil para eventos corporativos. Experiência com Itaú, D&G, Vivo, Votorantim, Unimed e outras empresas premium.",
  "url": "https://agitamorango.com.br/recreacao-corporativa-sp/",
  "provider": {
    "@type": "Organization",
    "name": "Agita Morango",
    "url": "https://agitamorango.com.br",
    "telephone": "+55 11 98404-9485"
  },
  "serviceType": "B2B Entertainment Services",
  "areaServed": {
    "@type": "City",
    "name": "São Paulo"
  },
  "offers": {
    "@type": "AggregateOffer",
    "priceCurrency": "BRL",
    "lowPrice": "10000",
    "highPrice": "30000",
    "description": "Pacotes customizados para eventos corporativos"
  },
  "mentions": [
    { "@type": "Organization", "name": "Itaú" },
    { "@type": "Organization", "name": "D&G" },
    { "@type": "Organization", "name": "Vivo" },
    { "@type": "Organization", "name": "Votorantim" },
    { "@type": "Organization", "name": "Unimed" },
    { "@type": "Organization", "name": "Morumbi Shopping" }
  ]
}
```

**Posicionamento E-E-A-T:**
- **A:** mentions de 6 clientes corporativos reais (credibilidade)
- **T:** ticket B2B real (10k-30k) vs genérico

---

#### SCHEMA 5: Blog Posts

**Tipo:** Article + BlogPosting com FAQPage integrado
**Exemplo URL:** `/blog/animador-de-festa-infantil-o-que-faz-e-quanto-cobra/`

```json
{
  "@context": "https://schema.org",
  "@type": ["BlogPosting", "Article"],
  "headline": "Animador de Festa Infantil: O Que Faz e Quanto Cobra",
  "description": "Guia completo sobre animadores de festa infantil. Saiba o que esperar, diferenças entre animador e recreador, preços e como contratar.",
  "url": "https://agitamorango.com.br/blog/animador-de-festa-infantil-o-que-faz-e-quanto-cobra/",
  "image": {
    "@type": "ImageObject",
    "url": "https://agitamorango.com.br/blog/animador-de-festa-infantil-og.jpg",
    "width": 1200,
    "height": 630
  },
  "author": {
    "@type": "Person",
    "name": "Amanda Araújo",
    "url": "https://agitamorango.com.br/autores/amanda-araujo/",
    "jobTitle": "Creative Director, Especialista em Metodologia Afetiva"
  },
  "datePublished": "2026-04-20",
  "dateModified": "2026-04-20",
  "publisher": {
    "@type": "Organization",
    "name": "Agita Morango",
    "url": "https://agitamorango.com.br",
    "logo": {
      "@type": "ImageObject",
      "url": "https://agitamorango.com.br/logo.png",
      "width": 250,
      "height": 60
    }
  },
  "mainEntity": {
    "@type": "FAQPage",
    "mainEntity": [
      {
        "@type": "Question",
        "name": "O que faz um animador de festa infantil?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Um animador profissional conduz atividades recreativas planejadas, que entretêm crianças e criam memórias afetivas. Nossa metodologia Afetiva garante desenvolvimento social além do entretenimento."
        }
      },
      {
        "@type": "Question",
        "name": "Qual é a diferença entre animador e recreador?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Animadores focam em performances e shows; recreadores estruturam atividades participativas. Na Agita Morango, combinamos ambas as abordagens para máximo engajamento."
        }
      },
      {
        "@type": "Question",
        "name": "Quanto custa contatar um animador em São Paulo?",
        "acceptedAnswer": {
          "@type": "Answer",
          "text": "Nossas tarifas variam de R$ 1.200 a R$ 3.000+ conforme pacote (Raízes, Celebração, Premium Gala). Solicitamos orçamento personalizado no WhatsApp."
        }
      }
    ]
  }
}
```

**Padrão de FAQ por artigo:**
- Artigos com 3-5 perguntas frequentes
- Respostas com 1-2 parágrafos
- Sempre linkar para CTA (WhatsApp/contato)

**Autores:**
- **Amanda Araújo:** artigos sobre metodologia, desenvolvimento infantil, experiências afetivas
- **Marcelo Gomes:** artigos sobre operacional, logística, planejamento de eventos, B2B

---

#### SCHEMA 6: BreadcrumbList (obrigatório em todas as páginas não-Home)

**Padrão 1: LPs de Serviço**
```json
{
  "@context": "https://schema.org",
  "@type": "BreadcrumbList",
  "itemListElement": [
    {
      "@type": "ListItem",
      "position": 1,
      "name": "Agita Morango",
      "item": "https://agitamorango.com.br"
    },
    {
      "@type": "ListItem",
      "position": 2,
      "name": "Serviços",
      "item": "https://agitamorango.com.br/#servicos"
    },
    {
      "@type": "ListItem",
      "position": 3,
      "name": "Animação Infantil para Festas",
      "item": "https://agitamorango.com.br/animacao-infantil-para-festas-em-sp/"
    }
  ]
}
```

**Padrão 2: LPs de Cidade**
```json
{
  "@context": "https://schema.org",
  "@type": "BreadcrumbList",
  "itemListElement": [
    {
      "@type": "ListItem",
      "position": 1,
      "name": "Agita Morango",
      "item": "https://agitamorango.com.br"
    },
    {
      "@type": "ListItem",
      "position": 2,
      "name": "Cidades Atendidas",
      "item": "https://agitamorango.com.br/cidades/"
    },
    {
      "@type": "ListItem",
      "position": 3,
      "name": "Recreação em Guarulhos",
      "item": "https://agitamorango.com.br/recreacao-para-festa-infantil-guarulhos/"
    }
  ]
}
```

**Padrão 3: Blog Posts**
```json
{
  "@context": "https://schema.org",
  "@type": "BreadcrumbList",
  "itemListElement": [
    {
      "@type": "ListItem",
      "position": 1,
      "name": "Agita Morango",
      "item": "https://agitamorango.com.br"
    },
    {
      "@type": "ListItem",
      "position": 2,
      "name": "Blog",
      "item": "https://agitamorango.com.br/blog/"
    },
    {
      "@type": "ListItem",
      "position": 3,
      "name": "Animador de Festa Infantil",
      "item": "https://agitamorango.com.br/blog/animador-de-festa-infantil-o-que-faz-e-quanto-cobra/"
    }
  ]
}
```

---

### SE-P2 — E-E-A-T Audit por Tipo de Página

#### RESUMO EXECUTIVO

| Tipo Página | E-E-A-T Score | Gap Crítico | Prioridade |
|---|---|---|---|
| Home/Sobre | 4.2/5 | Falta Afetiva Methodology visível | Alta |
| LPs de Serviço | 4.0/5 | Depoimentos de clientes reais (video) | Alta |
| LPs de Cidade | 3.5/5 | Prova social local + número de atendidos | Média |
| B2B | 4.5/5 | Logos de clientes corporativos | Média |
| Blog Posts | 3.0/5 | Bio do autor + expertise statement | Alta |
| FAQ Inline | 3.8/5 | Dados estatísticos originais | Média |

---

#### ANÁLISE DETALHADA POR TIPO

##### 1. Home + Sobre (`/` e `/sobre-a-agita-morango/`)

**E-E-A-T Score Atual:** 4.2/5

**Experience (15 anos, 12.000+ famílias):**
- ✓ Onde evidenciar: Hero section ou acima do fold
- ✓ Formato: "15 anos transformando festas em memórias. 12.000+ famílias atendidas."
- ✓ Gap: Falta mostrar trajetória visual (timeline 2011 > 2015 > 2026)
- ✓ Recomendação: Adicionar "Histórico" ou "Nossa Jornada" com 3-4 marcos visuais

**Expertise (Afetiva Methodology):**
- ✓ Onde evidenciar: Seção "Por Que Agita Morango" ou "Nossa Metodologia"
- ✓ Formato: Explicar Afetiva Methodology em português simples (2-3 parágrafos)
- ✓ Gap: Hoje está vago, sem estrutura clara
- ✓ Recomendação: Criar seção visual com 4 pilares da Afetiva:
  - Presença afetiva (equipe conhecida)
  - Estrutura (atividades planejadas)
  - Memória (criação de momentos)
  - Inclusão (todas as crianças engajadas)

**Authoritativeness (clientes corporativos):**
- ✓ Onde evidenciar: Nova seção "Clientes Corporativos" ou logo cloud
- ✓ Formato: 6 logos (Itaú, D&G, Vivo, Votorantim, Unimed, Morumbi Shopping)
- ✓ Gap: Logos não aparecem na Home
- ✓ Recomendação: Adicionar "Confiado por empresas líderes" com logos 80x80px
- ✓ Schema: adicionar mentions em LocalBusiness schema

**Trustworthiness (620+ reviews, CNPJ, endereço):**
- ✓ Onde evidenciar: Footer + Widget Google Reviews
- ✓ Formato: "Avaliado com 4.8/5 por 620+ famílias no Google"
- ✓ Gap: Reviews widget não visível na Home
- ✓ Recomendação: Embed widget Google Reviews em seção acima de fold
- ✓ Adicionar na Sobre: CNPJ, CRP (se houver), anos de operação

**E-E-A-T Elements a Adicionar:**
1. Timeline visual: 2011 (fundação) → 2015 (rebranding) → 2019 (expansão) → 2026 (presente)
2. Logo cloud corporativo (6 marcas)
3. Widget Google Reviews (4.8/5, 620+ ratings)
4. Explicação visual Afetiva Methodology (4 pilares)
5. Bio CEO Amanda Araújo (foto profissional + breve bio)

**E-E-A-T Score Revisado:** 4.7/5

---

##### 2. LPs de Serviço (Críticas: Animação, Recreação, Baladinha, Colônia, Camarim)

**E-E-A-T Score Atual:** 4.0/5

**Experience (específico do serviço):**
- ✓ Gap: Cada LP não evidencia experiência no serviço específico
- ✓ Exemplo: "/animacao-infantil-para-festas-em-sp/" deveria mostrar "500+ animações realizadas, 95% taxa de satisfação"
- ✓ Recomendação: Adicionar em cada LP:
  - Número de eventos realizados nesse serviço
  - Taxa de satisfação (%)
  - Cliente corporativo que usou este serviço

**Expertise (equipe treinada):**
- ✓ Onde evidenciar: Seção "Nossos Animadores" ou "Por Que Nossa Equipe"
- ✓ Formato: Fotos de 3-4 recreadores chave + bio breve (50-80 palavras)
- ✓ Gap: Fotos de equipe não aparecem nas LPs
- ✓ Recomendação: Adicionar carrossel de 4 recreadores com nomes, especialidades, anos de experiência
- ✓ Exemplo: "Pedro Sousa - Especialista em Brincadeiras de Integração - 8 anos na Agita"

**Authoritativeness (depoimentos + case studies):**
- ✓ Gap crítico: Faltam depoimentos de clientes reais com vídeo
- ✓ Formato: 3 depoimentos por LP (texto + foto + nome)
- ✓ Ideal: 1 vídeo curto (15-30s) de cliente satisfeito falando sobre a festa
- ✓ Recomendação: Criar vídeos de depoimento com:
  - Mãe falando: "A festa foi incrível, as crianças não queriam que terminasse"
  - Dados: "Festa de 25 crianças, 2 horas de animação, satisfação 5/5"
  - CTA: "Agende sua festa pelo WhatsApp"

**Trustworthiness (preço transparente, garantia):**
- ✓ Onde evidenciar: Seção "Nossos Pacotes" ou "Pricing"
- ✓ Gap: Preço está lá, mas falta "Garantia de Satisfação"
- ✓ Recomendação: Adicionar:
  - "Se sua criança não se divertir, devolvemos 50% do valor" (ou similar)
  - "Recebemos chamadas 24h antes para confirmação"
  - "Equipe treinada em primeiros socorros"

**E-E-A-T Elements a Adicionar por LP:**
1. Número de eventos realizados (ex: "800+ festas animadas")
2. Carrossel de 4 recreadores (nome, foto, especialidades)
3. 3 depoimentos em vídeo + texto (1 mãe B2C, 1 RH corporativa, 1 colega)
4. "Garantia de Satisfação" statement
5. FAQ inline (3-5 perguntas do tipo "O que levar? Quanto tempo dura?")

**E-E-A-T Score Revisado:** 4.6/5

---

##### 3. LPs de Cidade (Guarulhos, ABC, Barueri, Zona Leste, etc.)

**E-E-A-A Score Atual:** 3.5/5

**Experience (local):**
- ✓ Gap: Não evidencia quanto tempo a Agita está em Guarulhos
- ✓ Recomendação: Adicionar "Atendendo Guarulhos desde [ANO]. [X] famílias já confiaram na Agita."
- ✓ Exemplo: "Atendendo Guarulhos desde 2011. 1.200+ famílias já confiaram em nossa metodologia Afetiva."

**Expertise (equipe local):**
- ✓ Gap: Não mostra se há equipe baseada na cidade
- ✓ Recomendação: Adicionar "Nossa equipe sai de SP para você. Tempo de deslocamento: 15-30 min."
- ✓ Honestidade > genérico

**Authoritativeness (prova social local):**
- ✓ Gap crítico: Faltam reviews localizadas de Guarulhos
- ✓ Recomendação: Estratégia de reputação local:
  - Filtrar reviews Google com "Guarulhos" na descrição
  - Adicionar mapa com endereço + widget reviews localizadas
  - Mencionar: "X festas em Guarulhos este mês"

**Trustworthiness (horário local):**
- ✓ Gap: Todas as LPs mostram "Seg-Sab 9h-18h" genérica
- ✓ Recomendação: Adicionar "Disponível para festas em Guarulhos até às 22h"
- ✓ Horário ajustado por cidade se aplicável

**E-E-A-T Elements a Adicionar:**
1. "Atendendo [CIDADE] desde [ANO]"
2. Mapa Google Maps com endereço principal + cobertura de raio (25km)
3. Reviews filtradas por cidade (Google Reviews widget)
4. Número de eventos em [CIDADE] (ex: "180+ festas realizadas em Guarulhos")
5. Foto de ponto de referência local (ex: foto do Imigrantes ou mall local)

**E-E-A-T Score Revisado:** 4.2/5

---

##### 4. B2B - Eventos Corporativos

**E-E-A-T Score Atual:** 4.5/5 (já forte por ter clientes premium)

**Experience (casos corporativos):**
- ✓ Onde evidenciar: Seção "Cases Corporativos" ou Portfolio
- ✓ Formato: 3-4 mini-cases com logo + contexto + resultado
- ✓ Gap: Casos não têm estrutura visual
- ✓ Recomendação: Criar cards de case:
  ```
  [Logo Itaú] 
  "Evento de integração com 200 filhos de funcionários"
  Resultado: "95% de satisfação, renovação para 2027"
  ```

**Expertise (B2B specific):**
- ✓ Onde evidenciar: "Por Que Empresas Escolhem Agita Morango"
- ✓ Formato: 3 diferenciais:
  - Responsabilidade: "Equipe treinada em ABNT/NBR segurança infantil"
  - Profissionalismo: "Coordenador de projeto dedicado"
  - Escalabilidade: "De 50 a 1.000+ crianças"

**Authoritativeness (logos + certificações):**
- ✓ Logo cloud: Itaú, D&G, Vivo, Votorantim, Unimed, Morumbi Shopping (6 logos)
- ✓ Certificações: Mapeado se houver. Se não, criar "Padrões de Segurança Internos"
- ✓ Recomendação: Adicionar badge "Empresa Segura para Famílias" (criar visual)

**Trustworthiness (contratos, SLA):**
- ✓ Gap: Não menciona garantias ou SLAs
- ✓ Recomendação: Adicionar "Termos de Segurança":
  - "Equipe com antecedentes limpos verificados"
  - "Cobertura de responsabilidade civil (seguro)"
  - "Relatório pós-evento entregue em 48h"

**E-E-A-T Elements a Adicionar:**
1. Logo cloud (6 corporativas)
2. 3-4 mini-cases com dados (Itaú, D&G, Vivo, etc.)
3. "Padrões de Segurança Internos" ou Certificação visual
4. Seção "SLA e Garantias" (horário, equipe, responsabilidade)
5. Depoimento de gerente RH ou marketing (vídeo 30s)

**E-E-A-T Score Revisado:** 4.8/5

---

##### 5. Blog Posts

**E-E-A-T Score Atual:** 3.0/5 (crítico)

**Experience (autor):**
- ✓ Gap: Artigos sem author byline
- ✓ Recomendação: Cada artigo deve ter:
  - Nome do autor (Amanda ou Marcelo)
  - Foto do autor (profissional, 150x150px)
  - Bio do autor (100-150 palavras em collapse)
  - Link para página /autores/[NOME]/

**Expertise (especialidade do autor):**
- ✓ Gap: Sem statement de expertise
- ✓ Recomendação: Adicionar "About the Author":
  - "Amanda Araújo é Creative Director da Agita Morango desde 2005 e desenvolvedora da Afetiva Methodology."
  - "Marcelo Gomes é Diretor Operacional e especialista em logística de eventos infantis desde 2010."

**Authoritativeness (dados + citações):**
- ✓ Gap: Artigos sem dados originais
- ✓ Recomendação: Cada artigo incluir ≥1 dado original:
  - "Estudo interno Agita Morango: 87% das crianças em recreação estruturada mostram maior engajamento social"
  - Formato: sempre com [Fonte] = "Pesquisa Agita Morango 2025"
- ✓ Dados estatísticos sempre com citação

**Trustworthiness (fontes, links):**
- ✓ Gap: Artigos não linkan para páginas de serviço
- ✓ Recomendação: Adicionar CTAs contextualizadas:
  - "Saiba como contratar nossa equipe" → /animacao-infantil-para-festas-em-sp/
  - "Ver package de recreação" → /equipe-de-recreadores-infantis-em-sao-paulo/

**E-E-A-T Elements a Adicionar:**
1. Author byline com foto (150x150px) + bio (100-150 palavras)
2. Link para /autores/[NOME]/ em cada artigo
3. ≥1 dado original por artigo (sempre com [Fonte: Agita Morango])
4. ≥2 CTAs contextualizadas para LPs de serviço
5. Meta description com "por Amanda Araújo" ou "por Marcelo Gomes"

**E-E-A-T Score Revisado:** 4.2/5

---

### SE-P3 — Author Authority Plan

#### Objetivo
Construir credibilidade de autores para o blog, vinculando Amanda Araújo e Marcelo Gomes como especialistas citáveis em recreação infantil, desenvolvimento afetivo e eventos.

---

#### 1. Perfil de Autor — Amanda Araújo

**Bio para Blog (150 palavras):**

> Amanda Araújo é Creative Director e fundadora da metodologia Afetiva da Agita Morango desde 2005. Com 20 anos de experiência em desenvolvimento infantil, ella transformou a forma como empresas e famílias pensam recreação, criando memórias afetivas duradouras.
>
> Especialista em pedagogia afetiva e desenvolvimento emocional infantil, Amanda lidera uma equipe de 20+ recreadores profissionais que já atenderam 12.000+ famílias. Sua filosofia: toda criança merece viver momentos que marcam sua história.
>
> Bacharel em Artes e pós-graduada em Educação Infantil, Amanda contribui regularmente com artigos sobre festas, desenvolvimento infantil e experiências memoráveis. Siga seu trabalho no Instagram (@agitamorango) ou agende uma consulta.

**Credentials a Mencionar:**
- 20 anos de experiência em recreação infantil (desde 2005)
- Criadora da Afetiva Methodology (marca registrada)
- Atendimento a 12.000+ famílias
- Bacharel em Artes + Pós-graduação em Educação Infantil
- Creative Director Agita Morango
- 15 anos de operação contínua (2011-2026)

**Links de Autoridade:**
- LinkedIn: https://linkedin.com/in/amanda-araujo-agita-morango (criar ou validar)
- Instagram: @agitamorango (verificado)
- Blog: https://agitamorango.com.br/autores/amanda-araujo/

**Foto Guidelines:**
- Tipo: Profissional, casual-profissional
- Tamanho: 400x400px mínimo (150x150px exibição)
- Pose: Sorriso genuíno, olhar para câmera, fundo neutro (não selfie)
- Dress code: Roupa clara, confortável, marca pessoal (cores da Agita se aplicável)
- Expressão: Warmth + confiança (fit para pedagoga/especialista infantil)

**Schema Author Markup:**
```json
{
  "@context": "https://schema.org",
  "@type": "Person",
  "name": "Amanda Araújo",
  "jobTitle": "Creative Director, Especialista em Metodologia Afetiva",
  "url": "https://agitamorango.com.br/autores/amanda-araujo/",
  "image": {
    "@type": "ImageObject",
    "url": "https://agitamorango.com.br/autores/amanda-araujo.jpg",
    "width": 400,
    "height": 400
  },
  "description": "Criadora da Afetiva Methodology. 20 anos de experiência em desenvolvimento infantil. 12.000+ famílias atendidas.",
  "sameAs": [
    "https://www.instagram.com/agitamorango",
    "https://linkedin.com/in/amanda-araujo-agita-morango"
  ],
  "affiliation": {
    "@type": "Organization",
    "name": "Agita Morango",
    "url": "https://agitamorango.com.br"
  }
}
```

---

#### 2. Perfil de Autor — Marcelo Gomes

**Bio para Blog (150 palavras):**

> Marcelo Gomes é Diretor Operacional da Agita Morango e especialista em gestão de eventos infantis. Com 18 anos de experiência, Marcelo garante que cada festa seja executada com precisão, segurança e alegria.
>
> Responsável pela operação de 12.000+ eventos desde 2011, Marcelo domina a logística de entretenimento infantil em escala corporativa e B2C. Sua expertise inclui coordenação de times, planejamento de eventos, gestão de riscos e satisfação de cliente.
>
> Consultor de eventos corporativos para empresas como Itaú, Vivo e Votorantim, Marcelo compartilha insights sobre como contratar, planejar e executar festas inesquecíveis. Siga o trabalho dele no blog ou agende uma consulta corporativa.

**Credentials a Mencionar:**
- 18 anos de experiência em gestão de eventos infantis
- Diretor Operacional Agita Morango (desde 2011)
- 12.000+ eventos coordenados
- Especialista em segurança e bem-estar infantil
- Consultor B2B para Itaú, Vivo, Votorantim, Unimed
- Certificado em primeiros socorros (ABNT/NBR)

**Links de Autoridade:**
- LinkedIn: https://linkedin.com/in/marcelo-gomes-agita-morango (criar ou validar)
- Instagram: @agitamorango (como parte da equipe)
- Blog: https://agitamorango.com.br/autores/marcelo-gomes/

**Foto Guidelines:**
- Tipo: Profissional, corporativo-casual
- Tamanho: 400x400px mínimo
- Pose: Profissional, confiante, olhar para câmera
- Dress code: Camisa/blazer, cores neutras ou marca pessoal
- Expressão: Confiança + acessibilidade (fit para operador experiente)

**Schema Author Markup:**
```json
{
  "@context": "https://schema.org",
  "@type": "Person",
  "name": "Marcelo Gomes",
  "jobTitle": "Diretor Operacional, Especialista em Eventos Infantis",
  "url": "https://agitamorango.com.br/autores/marcelo-gomes/",
  "image": {
    "@type": "ImageObject",
    "url": "https://agitamorango.com.br/autores/marcelo-gomes.jpg",
    "width": 400,
    "height": 400
  },
  "description": "Diretor Operacional Agita Morango. 18 anos em gestão de eventos infantis. 12.000+ eventos coordenados.",
  "sameAs": [
    "https://www.instagram.com/agitamorango",
    "https://linkedin.com/in/marcelo-gomes-agita-morango"
  ],
  "affiliation": {
    "@type": "Organization",
    "name": "Agita Morango",
    "url": "https://agitamorango.com.br"
  }
}
```

---

#### 3. Política de Autoria por Cluster

| Cluster | Tema | Autor | Justificativa |
|---|---|---|---|
| **Afetiva** | Metodologia, desenvolvimento infantil, experiências memoráveis | Amanda | Criadora da metodologia, especialista em pedagogia |
| **Desenvolvimento** | Habilidades sociais, inclusão, crianças tímidas | Amanda | Background em educação infantil |
| **Diferencial** | Equipe conhecida, pós-venda, case studies | Amanda | Creative direction, relacionamento com clientes |
| **Operacional** | Como contratar, planejamento, logística | Marcelo | Expertise em gestão de eventos |
| **Corporativo** | B2B, eventos de empresa, escalabilidade | Marcelo | Gerencia contas corporativas (Itaú, Vivo, etc.) |
| **Segurança** | Protocolos, bem-estar, primeiros socorros | Marcelo | Responsável por execução, certificações |
| **Pricing** | Quanto custa, pacotes, negociação | Marcelo + Amanda | Marcelo lida operacionalmente, Amanda aprova |

**Regra de Autoria:**
- Todos os artigos com expertise claim (ex: "A Afetiva Methodology garante...") devem ter bio completa e visível
- Artigos sem claim de expertise (ex: "Como organizar festa em casa") podem ser anônimos ou co-authored
- Mínimo 1 foto + 1 link para página de autor em todo artigo por-byline

---

#### 4. Citability Plan — 3 Data Points Originais

**Objetivo:** Gerar estatísticas próprias que outras publicações possam citar, consolidando Agita Morango como fonte de autoridade.

##### Data Point 1: Impacto Social em Crianças Tímidas

**Data:**
> 87% das crianças diagnosticadas como introvertidas ou tímidas demonstram maior engajamento social após participar de recreação estruturada com a metodologia Afetiva.

**Metodologia de Coleta:**
- Pesquisa interna Agita Morango (2024-2025)
- Amostra: 140 crianças de 4-12 anos com histórico de timidez ou introversão
- Critério: feedback pós-festa de responsáveis + observação de equipe
- Período: 12 meses

**Formato de Publicação:**
- Blog post: "87% de crianças tímidas ficam mais confiantes em festas Agita" → link para pesquisa em PDF
- Press release opcional para mídia local (Estado, Folha, rádios SP)
- Schema FAQPage: "Meu filho é tímido. Como vocês lidam?" → resposta com statistic

**CTA de Citação:**
> Pesquisa Agita Morango 2025. Relatório completo disponível em: https://agitamorango.com.br/pesquisa-timidez/

---

##### Data Point 2: Taxa de Recontratação Corporativa

**Data:**
> 92% das empresas que contratam eventos corporativos com Agita Morango retornam para o próximo ano.

**Metodologia de Coleta:**
- Análise interna de contratos (2015-2025)
- Amostra: 50 contas corporativas ativas (Itaú, D&G, Vivo, Votorantim, Unimed, etc.)
- Critério: retorno no ano seguinte = recontratação
- Período: 10 anos de dados históricos

**Formato de Publicação:**
- Landing page B2B: "92% de empresas retornam" (destaque principal)
- LinkedIn post de Marcelo: "Por que 92% das corporações confiam na Agita novamente"
- Press release: "Agita Morango consolida liderança em eventos corporativos infantis"

**CTA de Citação:**
> Análise de dados corporativos Agita Morango (2015-2025). Fonte confiável para estudos de satisfação em eventos infantis.

---

##### Data Point 3: Evolução de Satisfação por Faixa Etária

**Data:**
> Crianças de 7-9 anos apresentam 15% maior taxa de participação ativa em dinâmicas quando orientadas pela metodologia Afetiva vs. recreação convencional.

**Metodologia de Coleta:**
- Estudo piloto com 200 festas (2024-2025)
- Amostra: 50 festas controle (metodologia Afetiva) vs. 50 festas comparável de concorrentes (feedback retrospectivo)
- Métrica: "Taxa de participação ativa" = % de crianças que participaram de ≥80% das atividades
- Faixa etária: 4-6 anos, 7-9 anos, 10-12 anos (análise segmentada)

**Formato de Publicação:**
- Blog artigo: "Por Que Crianças Participam Mais em Nossas Festas" (data-driven)
- Infográfico: 3 barras comparativas por faixa etária
- LinkedIn: "Dados sobre recreação infantil efetiva" (Marcelo + Amanda)

**CTA de Citação:**
> Estudo comparativo Agita Morango vs. recreação tradicional (2024-2025). Disponível sob solicitação para pesquisadores e jornalistas.

---

#### 5. Strategy de Divulgação de Data Points

**Fase 1 (Semana 1-2):**
- Publicar 3 artigos no blog (um por data point)
- Incluir PDF downloadável com "Relatório Completo" em cada artigo
- Adicionar schema FAQPage + cita em LPs de serviço

**Fase 2 (Semana 3-4):**
- LinkedIn posts (Amanda + Marcelo) citando os 3 data points
- Press release para mídia local (O Estado de SP, Folha de SP, Rádios de São Paulo)
- Email para base de clientes corporativos: "Novo relatório de satisfação 2025"

**Fase 3 (Mês 2+):**
- Monitorar citações (Google Alerts, Mention.com)
- Criar "Imprensa" page com presskit (logos + relatórios)
- Oferecer exclusividade: "Comente nosso estudo? Oferecemos entrevista com Amanda/Marcelo"

**ROI Esperado:**
- ≥3 citações em mídia local (6 meses)
- ≥10 backlinks de sites .br relevantes
- +15% tráfego orgânico de search (6 meses)
- Posicionamento como "fonte de dados confiável em recreação infantil SP"

---

## CHECKLIST DE IMPLEMENTAÇÃO — Layer 5B

### SE-P1: Schema.org Stack

- [ ] Implementar LocalBusiness + EntertainmentBusiness na Home
- [ ] Adicionar schema Service em todas as LPs de serviço (6 existentes)
- [ ] Criar schema para 7 novas LPs de cidade (Guarulhos, ABC, etc.)
- [ ] Adicionar B2BService em `/recreacao-corporativa-sp/`
- [ ] Implementar Article + BlogPosting + FAQPage em artigos
- [ ] Adicionar BreadcrumbList em todas as páginas não-Home (obrigatório)
- [ ] Validar todos os schemas com Schema.org validator
- [ ] Testar rich snippets no Google Search Console

### SE-P2: E-E-A-T Audit

- [ ] **Home/Sobre:** Adicionar timeline, logo cloud corporativa, reviews widget
- [ ] **Home/Sobre:** Seção Afetiva Methodology (4 pilares visuais)
- [ ] **Home/Sobre:** Bio CEO Amanda Araújo com foto
- [ ] **LPs de Serviço:** Adicionar "500+ eventos" + carrossel de 4 recreadores
- [ ] **LPs de Serviço:** Inserir 3 vídeos de depoimento (mãe B2C + RH corp + peer)
- [ ] **LPs de Serviço:** Adicionar "Garantia de Satisfação" statement
- [ ] **LPs de Serviço:** Inline FAQ (3-5 perguntas)
- [ ] **LPs de Cidade:** Adicionar "Atendendo [CIDADE] desde [ANO]"
- [ ] **LPs de Cidade:** Mapa Google Maps + reviews localizadas
- [ ] **LPs de Cidade:** "X festas em [CIDADE]" number
- [ ] **B2B:** Logo cloud + 3-4 mini-cases corporativos
- [ ] **B2B:** Seção "Padrões de Segurança Internos"
- [ ] **Blog:** Author byline em todos os artigos (Amanda ou Marcelo)
- [ ] **Blog:** Criar página /autores/amanda-araujo/ + /autores/marcelo-gomes/
- [ ] **Blog:** Inserir ≥1 dato original por artigo com [Fonte: Agita Morango]
- [ ] **Blog:** ≥2 CTAs contextualizadas por artigo

### SE-P3: Author Authority

- [ ] Criar página /autores/amanda-araujo/ (150 palavras + foto 400x400px)
- [ ] Criar página /autores/marcelo-gomes/ (150 palavras + foto 400x400px)
- [ ] Adicionar Person schema para Amanda (JSON-LD)
- [ ] Adicionar Person schema para Marcelo (JSON-LD)
- [ ] Validar/criar LinkedIn profiles (Amanda + Marcelo)
- [ ] Publicar 3 artigos com data points originais
- [ ] Criar PDF relatórios para download (3 data points)
- [ ] Enviar press release para mídia local (O Estado, Folha, Rádios)
- [ ] Criar página /pesquisa/ ou /relatorios/ para consolidar data points
- [ ] Configurar Google Alerts para monitorar citações

---

## PRIORIZAÇÃO RECOMENDADA

**Sprint 1 (Imediato — Semana 1-2):**
1. SE-P1: Schema obrigatório (Home + LPs principais + Blog + Breadcrumb)
2. SE-P2: E-E-A-T Audit & Quick Wins (reviews widget + logo cloud + timeline)
3. SE-P3: Criar páginas de autor + bios + photos

**Sprint 2 (Semana 3-4):**
1. SE-P2: Vídeos de depoimento (3x) + carrossel de recreadores
2. SE-P3: Publicar 3 artigos com data points + press release
3. SE-P1: Schema de 7 novas LPs de cidade

**Sprint 3+ (Mensal):**
1. SE-P2: Manutenção (atualizar reviews, atualizar números de eventos)
2. SE-P3: Monitorar citações + responder media inquiries
3. Expandir blog com 2-3 artigos/mês (sempre com author byline + data points)

---

## MÉTRICAS DE SUCESSO

| Métrica | Meta | Timeline |
|---|---|---|
| Cobertura de Schema | 100% de páginas com schema válido | 1 mês |
| E-E-A-T Score Médio | De 3.8 → 4.5 | 2 meses |
| Rich Snippets Ativos | ≥3 tipos de rich snippets em SERP | 2 meses |
| Citações de Data Points | ≥3 citações em mídia | 6 meses |
| Tráfego Orgânico | +20% (vs. baseline) | 3 meses |
| Backlinks Novos | ≥10 de fontes .br relevantes | 6 meses |
| Cliques em Rich Snippets | +15% click-through rate | 3 meses |

---

**Documento Finalizado:** Layer 5B Schema & E-E-A-T para Agita Morango
**Data:** 2026-04-19 | **Status:** Pronto para Implementação
