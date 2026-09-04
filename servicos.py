#!/usr/bin/env python3

autor = "Thiago 189"
#Lista: é uma sequencia ordenada de valores

portas_alvo = [22, 80, 443, 3306, 8080, 3000, 5000, 8000, 137, 138, 139, 445]
portas_alvo.append(21) #Adiciona a porta 21 na variavel portas_alvo
servicos = ["ssh", "https", "dns]

print("A lista de portas é:",portas_alvo)
print(f'A lista de portas é: {portas_alvo}')

for NUM in range(1,11):
  print(NUM)

#Dicionarios: é um tipo de dado que trabalho sobre chave:valor

status_servico = {
  'host': '8.8.8.8',
  'porta': '443',
  'estado': 'aberta',
  'servico': 'https',
}

print(status_servico['host'])
print(status_servico['servico'])

servicos = {
        22: 'SSH',
        80: 'HTTP',
        443: 'HTTPS',
        3306: 'MYSQL',
}
print(f'Com for aninhado')
for PORTA in portas_alvo:
        for SERV in servicos:
                if PORTA == SERV:
                        print(f' PORTA {PORTA}: Servico {SERV}')
print(f'Com GET')
for PORTA in portas_alvo:
        NOME = servicos.get(PORTA, 'desconhecido')
        print(f' PORTA {PORTA}: Servico {NOME}')
