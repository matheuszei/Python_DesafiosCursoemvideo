#Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-os
# (com idade) em um dicionário, se por acaso a CTPS for diferente de ZERO, o dicionário receberá
# também o ano de contratação e o salário. Calcule e acrescente, além da idade, com quantos anos a
# pessoa vai se aposentar.

import datetime
trab = {}
trab['nome'] = str(input('Nome: '))
ano = int(input('Ano de nascimento: '))
trab['idade'] = datetime.date.today().year - ano
trab['ctps'] = int(input('Carteira de Trabalho (0 não tem): '))
if trab['ctps']!= 0:
    trab['contratação'] = int(input('Ano de contratação: '))
    trab['salário'] = float(input('Salário: '))
    trab['aposentadoria'] = trab['contratação'] - ano + 35

for k, v in trab.items():
    print(f'{k} tem o valor {v}')
