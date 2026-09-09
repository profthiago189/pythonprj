#!/usr/bin/env python3

import socket

# resolver um nome para IP (como a agenda do telefone)
ip = socket.gethostbyname('localhost')
print(f'IP resolvido: {ip}')

# AF_INET = IPv4 ; SOCK_STREAM = TCP (conexao confiavel)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.settimeout(2)

# connect_ex retorna 0 se conectou, ou um codigo de erro
# (melhor que connect() que lanca excecao)
codigo = s.connect_ex(('127.0.0.1', 8080))
if codigo == 0:
    print('[+] Porta 8080 (SSH) esta ABERTA')
else:
    print('[-] Porta 8080 esta fechada ou filtrada')
s.close()

 
