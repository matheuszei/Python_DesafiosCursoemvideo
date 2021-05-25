#Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo
# com a sua idade, se ele ainda vai se alistar ao serviço militar,
# se é a hora exata de se alistar ou se já passou do tempo do alistamento.
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

from datetime import date
nome = str(input('Informe o seu nome: '))
anonasc = int(input('Informe o ano que você nasceu: '))
anoatual = date.today().year

#Processamento
if anoatual - anonasc < 18:
    anoalist = anonasc + 18
    print('{}, você deve se alistar em {}'.format(nome, anoalist))
elif anoatual - anonasc == 18:
    print('{}, você deve se alistar este ano'.format(nome))
else:
    anoalist = anonasc + 18
    print('{}, você se alistou em {}'.format(nome, anoalist))

