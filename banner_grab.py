#!/usr/bin/env python3
import socket

def pegar_banner(host, porta):
    """Tenta capturar o banner de identificacao do servico."""
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(2)
        s.connect((host, porta))
        # muitos servicos se apresentam ao conectar
        banner = s.recv(1024).decode(errors='ignore').strip()
        s.close()
        return banner if banner else 'sem banner'
    except Exception:
        return 'nao identificado'

# mapa de portas para servicos esperados
SERVICOS = {21: 'FTP', 22: 'SSH', 25: 'SMTP', 80: 'HTTP',
            443: 'HTTPS', 3306: 'MySQL', 8080: 'HTTP-alt'}
porta = 22
esperado = SERVICOS.get(porta, 'desconhecido')
banner = pegar_banner('127.0.0.1', porta)
print(f'Porta {porta} | esperado: {esperado} | banner: {banner}')

 
