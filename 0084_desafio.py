#Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
#A) Quantas pessoas foram cadastradas.
#B) Uma listagem com as pessoas mais pesadas.
#C) Uma listagem com as pessoas mais leves.

cadastro = []
dados = []
maiorpeso = menorpeso = 0

while True:
    dados.append(str(input('Nome: ')))
    dados.append(int(input('Peso: ')))
    if len(cadastro) == 0:
        maiorpeso = menorpeso = dados[1]
    else:
        if dados[1] > maiorpeso:
            maiorpeso = dados[1]
        if dados[1] < menorpeso:
            menorpeso = dados[1]
    cadastro.append(dados[:])
    dados.clear()
    resp = input('Deseja continuar? [S/N] ').upper()
    if resp == 'N':
        break

print(f'Ao todo, você cadastrou {len(cadastro)} pessoas.')
print(f'O maior peso foi de {maiorpeso}. Peso de', end='')
for p in cadastro:
    if p[1] == maiorpeso:
        print(f'{p[0]} ', end='')
print(f'\nO menor peso foi de {menorpeso}. Peso de', end='')
for p in cadastro:
    if p[1] == menorpeso:
        print(f'{p[0]} ', end='')
