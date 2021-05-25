#Crie um programa que leia o ano de nascimento de sete pessoas.
# No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.

from datetime import date
anoatual = date.today().year
total = 0
for c in range(0, 8):
    anonasc = int(input('({}) Digite a data de nascimento: '.format(c)))
    if anoatual - anonasc < 18:
        total += 1
print('Total de pessoas menores de idade: {}'.format(total))
