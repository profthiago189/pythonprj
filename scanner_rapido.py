#!/usr/bin/env python3
"""Scanner concorrente - USO ETICO APENAS."""
import socket
from concurrent.futures import ThreadPoolExecutor

abertas = []

def escanear_porta(host, porta):
   s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
   s.settimeout(1)
   if s.connect_ex((host, porta)) == 0:
       abertas.append(porta)
   s.close()

def main():
   alvo = '127.0.0.1'
   # testar as 1024 portas conhecidas, em paralelo
   with ThreadPoolExecutor(max_workers=100) as executor:
       for porta in range(1, 1025):
           executor.submit(escanear_porta, alvo, porta)

   print(f'[*] Portas abertas: {sorted(abertas)}')

if __name__ == '__main__':
   main()
