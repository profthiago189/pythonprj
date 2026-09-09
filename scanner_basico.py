#!/usr/bin/env python3

"""Scanner de portas basico - USO ETICO APENAS."""


import socket

from datetime import datetime


def escanear_porta(host, porta):

    """Retorna True se a porta estiver aberta."""

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    s.settimeout(1)

    resultado = s.connect_ex((host, porta))

    s.close()

    return resultado == 0


def main():

    alvo = '127.0.0.1'  # SEMPRE um alvo autorizado!

    portas = [21, 22, 80, 443, 3306, 8080]

    print(f'[*] Escaneando {alvo} em {datetime.now()}')

    for porta in portas:

        if escanear_porta(alvo, porta):

            print(f'[+] Porta {porta}: ABERTA')

        else:

            print(f'[-] Porta {porta}: fechada/filtrada')


if __name__ == "__main__":

    main()
