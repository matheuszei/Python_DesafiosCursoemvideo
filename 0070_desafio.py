#Crie um programa que leia o nome e o preço de vários produtos.
# O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
#A) qual é o total gasto na compra.
#B) quantos produtos custam mais de R$1000.
#C) qual é o nome do produto mais barato.

preco = total = mais100 = 0
maisbarato = 999999999999
nomemaisbarato = 'x'
print('-' * 15)
print('LOJA SUPER BARATAO')
print('-' * 15)
while True:
    cond = 'X'
    produto = input('Digite o nome do produto: ')
    preco = float(input('Digite o valor do produto: '))

    total += preco
    if preco >= 1000:
        mais100 += 1
    if preco <= maisbarato:
        maisbarato = preco
        nomemaisbarato = produto

    while cond != 'S' and cond != 'N':
        cond = input('Quer continuar? [S/N] ').upper()
    if cond == 'N':
        break

print('=== FIM DO PROGRAMA ===')
print(f'Total de gastos {total}')
print(f'São {mais100} produtos que custam mais de R$1000,00')
print(f'O produto mais barato é o {nomemaisbarato} e custa R${maisbarato}')
