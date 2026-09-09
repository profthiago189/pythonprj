#!/usr/bin/env python3
"""Reconhecimento passivo via DNS - alvos autorizados."""
import socket

def resolver_host(dominio):
    """Descobre o IP de um dominio (consulta DNS publica)."""
    try:
        return socket.gethostbyname(dominio)
    except socket.gaierror:
        return None

def descobrir_reverso(ip):
    """DNS reverso: de um IP descobre o nome associado."""
    try:
        return socket.gethostbyaddr(ip)[0]
    except socket.herror:
        return 'sem registro reverso'

dominio = 'localhost'
ip = resolver_host(dominio)
print(f'[*] {dominio} -> {ip}')
if ip:
    print(f'[*] Reverso de {ip} -> {descobrir_reverso(ip)}')
