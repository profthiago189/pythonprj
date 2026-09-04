#!/usr/bin/env python3

notas=[]
soma=0

for nota in range(1,6):
  nota2 = float(input("Digite a nota %d de 5: " %nota))
  notas.append(nota2)
  soma += nota2

for nota in range[5]:
  print("Nota %d: %.2f " %(nota+1, notas[nota]))

print("A Media é %.2f " %(soma/5))
