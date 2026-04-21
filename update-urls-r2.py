#!/usr/bin/env python3
"""
update-urls-r2.py — Insere URLs R2 na coluna url_nova da planilha Agita Morango
Usage: python3 update-urls-r2.py [--dry-run]
"""
import sys
import gspread
from google.oauth2.service_account import Credentials

CREDENTIALS_FILE = '/Users/jrios/move-maquinas-seo/credentials.json'
SPREADSHEET_ID   = '1S5yp2mqGtbHnkmyvPPTm8bn5dHbYw4H-UM-7Axec6EY'
BASE_R2          = 'https://pub-bd2efcc812524f54a8c492f90052f3bd.r2.dev/agita-morango'

# Páginas publicadas no R2 (slug → path no R2)
PUBLISHED = {
    '/':                                                   '/index.html',
    '/sobre/':                                             '/sobre/index.html',
    '/blog/':                                              '/blog/index.html',
    '/faq/':                                               '/faq/index.html',
    '/contato/':                                           '/contato/index.html',
    '/orcamento/':                                         '/orcamento/index.html',
    '/clientes/':                                          '/clientes/index.html',
    '/trabalhe-conosco/':                                  '/trabalhe-conosco/index.html',
    '/politica-privacidade/':                              '/politica-privacidade/index.html',
    '/politica-cookies/':                                  '/politica-cookies/index.html',
    '/termos-de-uso/':                                     '/termos-de-uso/index.html',
    '/empresa-de-recreacao-em-sao-paulo/':                 '/empresa-de-recreacao-em-sao-paulo/index.html',
    '/recreacao-corporativa-sp/':                          '/recreacao-corporativa-sp/index.html',
    '/ativacoes-de-marca-com-criancas-em-sao-paulo/':      '/ativacoes-de-marca-com-criancas-em-sao-paulo/index.html',
    '/eventos-infantis-para-empresas-em-sao-paulo/':       '/eventos-infantis-para-empresas-em-sao-paulo/index.html',
    '/kids-day-e-family-day-corporativo-em-sao-paulo/':    '/kids-day-e-family-day-corporativo-em-sao-paulo/index.html',
    '/terceirizacao-recreacao-infantil-sp/':               '/terceirizacao-recreacao-infantil-sp/index.html',
    '/recreacao-infantil-corridas-de-rua-sp/':             '/recreacao-infantil-corridas-de-rua-sp/index.html',
    '/colonia-de-ferias-infantil-sp/':                     '/colonia-de-ferias-infantil-sp/index.html',
    '/animacao-infantil-para-festas-em-sp/':               '/animacao-infantil-para-festas-em-sp/index.html',
    '/espaco-baby-para-festa-sp/':                         '/espaco-baby-para-festa-sp/index.html',
    '/show-musical-infantil-em-sao-paulo/':                '/show-musical-infantil-em-sao-paulo/index.html',
    '/oficinas-criativas-infantis-em-sp/':                 '/oficinas-criativas-infantis-em-sp/index.html',
    '/aniversario-infantil-em-sao-paulo/':                 '/aniversario-infantil-em-sao-paulo/index.html',
    '/baladinha-kids-e-dj-infantil-em-sao-paulo/':         '/baladinha-kids-e-dj-infantil-em-sao-paulo/index.html',
    '/camarim-infantil-para-festas-em-sao-paulo/':         '/camarim-infantil-para-festas-em-sao-paulo/index.html',
    '/personagens-para-festas-infantis-em-sao-paulo/':     '/personagens-para-festas-infantis-em-sao-paulo/index.html',
    '/festas-tematicas-em-sao-paulo/':                     '/festas-tematicas-em-sao-paulo/index.html',
    '/festa-das-cores-em-sao-paulo/':                      '/festa-das-cores-em-sao-paulo/index.html',
    '/festa-do-pijama-em-sao-paulo/':                      '/festa-do-pijama-em-sao-paulo/index.html',
    '/dia-das-criancas-em-sao-paulo/':                     '/dia-das-criancas-em-sao-paulo/index.html',
    '/carnaval-infantil-em-sao-paulo/':                    '/carnaval-infantil-em-sao-paulo/index.html',
    '/halloween-para-festas-e-eventos-em-sao-paulo/':      '/halloween-para-festas-e-eventos-em-sao-paulo/index.html',
    '/natal-infantil-para-festas-e-eventos-em-sao-paulo/': '/natal-infantil-para-festas-e-eventos-em-sao-paulo/index.html',
    '/pascoa-para-festas-e-eventos-em-sao-paulo/':         '/pascoa-para-festas-e-eventos-em-sao-paulo/index.html',
    '/festa-de-ano-novo-infantil-em-sao-paulo/':           '/festa-de-ano-novo-infantil-em-sao-paulo/index.html',
    '/festa-junina-infantil-em-sao-paulo/':                '/festa-junina-infantil-em-sao-paulo/index.html',
    '/recreacao-para-festa-infantil-guarulhos/':            '/recreacao-para-festa-infantil-guarulhos/index.html',
    '/recreacao-para-festa-infantil-abc/':                  '/recreacao-para-festa-infantil-abc/index.html',
    '/animacao-infantil-zona-leste-sp/':                    '/animacao-infantil-zona-leste-sp/index.html',
    '/recreacao-para-festa-infantil-barueri/':              '/recreacao-para-festa-infantil-barueri/index.html',
    '/recreacao-para-festa-infantil-alphaville/':           '/recreacao-para-festa-infantil-alphaville/index.html',
    '/equipe-de-recreadores-infantis-em-sao-paulo/':        '/equipe-de-recreadores-infantis-em-sao-paulo/index.html',
    '/cases-e-clientes-de-evento-infantil/':                '/cases-e-clientes-de-evento-infantil/index.html',
    '/aluguel-de-brinquedos-para-festa-infantil-sp/':       '/aluguel-de-brinquedos-para-festa-infantil-sp/index.html',
    '/atelie-infantil-em-sao-paulo/':                       '/atelie-infantil-em-sao-paulo/index.html',
    '/mesas-e-cadeiras-infantis-em-sao-paulo/':             '/mesas-e-cadeiras-infantis-em-sao-paulo/index.html',
    '/animadores-de-festa-infantil-em-sao-paulo/':          '/animadores-de-festa-infantil-em-sao-paulo/index.html',
    '/baladinha-kids-e-dj-em-sao-paulo/':                   '/baladinha-kids-e-dj-em-sao-paulo/index.html',
    '/aniversarios-e-festas-infantis-em-sao-paulo/':        '/aniversarios-e-festas-infantis-em-sao-paulo/index.html',
    '/kids-day-e-family-day-em-sao-paulo/':                 '/kids-day-e-family-day-em-sao-paulo/index.html',
    '/ativacoes-de-marca-experiencias-sensoriais-sp/':      '/ativacoes-de-marca-experiencias-sensoriais-sp/index.html',
    # 14 novas páginas (2026-04-20)
    '/baladinha-kids-sem-dj-sp/':                           '/baladinha-kids-sem-dj-sp/index.html',
    '/dj-infantil-para-festas-em-sao-paulo/':               '/dj-infantil-para-festas-em-sao-paulo/index.html',
    '/bolha-de-sabao-gigante-sp/':                          '/bolha-de-sabao-gigante-sp/index.html',
    '/escultura-de-balao-para-festas-sp/':                  '/escultura-de-balao-para-festas-sp/index.html',
    '/pintura-artistica-infantil-sp/':                      '/pintura-artistica-infantil-sp/index.html',
    '/personalizados-para-festa-infantil-sp/':              '/personalizados-para-festa-infantil-sp/index.html',
    '/foto-polaroid-para-festa-infantil-sp/':               '/foto-polaroid-para-festa-infantil-sp/index.html',
    '/recreacao-infantil-para-escolas-sp/':                 '/recreacao-infantil-para-escolas-sp/index.html',
    '/magico-para-festa-infantil-sp/':                      '/magico-para-festa-infantil-sp/index.html',
    '/recreacao-infantil-para-hoteis-sp/':                  '/recreacao-infantil-para-hoteis-sp/index.html',
    '/recreacao-para-festa-infantil-zona-oeste-sp/':        '/recreacao-para-festa-infantil-zona-oeste-sp/index.html',
    '/recreacao-para-festa-infantil-zona-sul-sp/':          '/recreacao-para-festa-infantil-zona-sul-sp/index.html',
    '/recreacao-para-festa-infantil-zona-norte-sp/':        '/recreacao-para-festa-infantil-zona-norte-sp/index.html',
    '/aluguel-de-brinquedos-infantis-sp/':                  '/aluguel-de-brinquedos-infantis-sp/index.html',
    # Sprint 2 — Novas páginas (2026-04-20)
    '/kids-day-corporativo-em-sao-paulo/':                  '/kids-day-corporativo-em-sao-paulo/index.html',
    '/family-day-corporativo-em-sao-paulo/':                '/family-day-corporativo-em-sao-paulo/index.html',
    '/show-de-magica-infantil-em-sao-paulo/':               '/show-de-magica-infantil-em-sao-paulo/index.html',
    '/espaco-baby-infantil-para-casamentos-em-sp/':         '/espaco-baby-infantil-para-casamentos-em-sp/index.html',
    '/recreacao-a-domicilio-em-sao-paulo/':                 '/recreacao-a-domicilio-em-sao-paulo/index.html',
    '/recreacao-copa-do-mundo-infantil-sp/':                '/recreacao-copa-do-mundo-infantil-sp/index.html',
    '/kids-day-e-family-day-corporativo-em-sao-paulo/':     '/kids-day-e-family-day-corporativo-em-sao-paulo/index.html',
    '/baladinha-kids-infantil-em-sp/':                      '/baladinha-kids-infantil-em-sp/index.html',
}

DRY_RUN = '--dry-run' in sys.argv

def main():
    scopes = ['https://www.googleapis.com/auth/spreadsheets']
    creds  = Credentials.from_service_account_file(CREDENTIALS_FILE, scopes=scopes)
    gc     = gspread.authorize(creds)
    sh     = gc.open_by_key(SPREADSHEET_ID)
    ws     = sh.get_worksheet(0)

    headers = ws.row_values(1)
    # aceita variações de nome da coluna
    col_url_nova = None
    for candidate in ['url_nova', 'URL Nova', 'url nova', 'URL_NOVA']:
        if candidate in headers:
            col_url_nova = headers.index(candidate) + 1
            break
    if col_url_nova is None:
        print("ERRO: coluna url_nova não encontrada. Headers:", headers)
        return

    # Verifica se já existe coluna url_r2, senão cria
    if 'url_r2' in headers:
        col_url_r2 = headers.index('url_r2') + 1
    else:
        col_url_r2 = len(headers) + 1
        if not DRY_RUN:
            ws.update_cell(1, col_url_r2, 'url_r2')
        print(f"Coluna url_r2 criada na coluna {col_url_r2}")

    all_values = ws.get_all_values()
    updates = []

    for i, row in enumerate(all_values[1:], start=2):  # pula header
        url_nova = row[col_url_nova - 1] if len(row) >= col_url_nova else ''
        if not url_nova:
            continue
        if url_nova in PUBLISHED:
            r2_url = BASE_R2 + PUBLISHED[url_nova]
            updates.append({'range': f'{chr(64 + col_url_r2)}{i}', 'values': [[r2_url]]})
            print(f"  linha {i}: {url_nova} → {r2_url}")
        else:
            print(f"  linha {i}: {url_nova} — não publicada (skip)")

    if DRY_RUN:
        print(f"\n[DRY RUN] {len(updates)} células seriam atualizadas.")
        return

    if updates:
        ws.batch_update(updates)
        print(f"\n✅ {len(updates)} células atualizadas na planilha.")
    else:
        print("\nNenhuma atualização necessária.")

if __name__ == '__main__':
    main()
