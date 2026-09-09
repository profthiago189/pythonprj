#!/usr/bin/env python3
import json

from datetime import datetime


# acumular os achados num dicionario estruturado

relatorio = {

    'alvo': 'servidor-lab.interno',

    'data_scan': str(datetime.now()),

    'ip': '127.0.0.1',

    'portas_abertas': [22, 80, 443],

    'servicos': {'22': 'SSH', '80': 'HTTP', '443': 'HTTPS'},

    'observacoes': ['header CSP ausente na porta 80'],

}


# salvar em arquivo JSON (legivel por humano E por maquina)

with open('recon_resultado.json', 'w') as f:

    json.dump(relatorio, f, indent=4)


print('[*] Relatorio salvo em recon_resultado.json')
 
