#!/usr/bin/env python3
import requests

try:
    url = input("Digite o site a ser verificado: ")
    r = requests.get(url, timeout=3)
    print(f'[*] Status HTTP: {r.status_code}')

    # VERIFICAR HEADERS DE SEGURANCA (auditoria comum!)
    headers_seguranca = [
        'Strict-Transport-Security',
        'Content-Security-Policy',
        'X-Frame-Options',
    ]
    for h in headers_seguranca:
        if h in r.headers:
            print(f'[+] {h}: presente')
        else:
            print(f'[-] {h}: AUSENTE (risco!)')
except requests.exceptions.RequestException as e:
    print(f'[!] Erro na requisicao: {e}')
 
