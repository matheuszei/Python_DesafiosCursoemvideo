#Crie um programa onde o usuário possa digitar setes valores numéricos e cadastre-os em uma
#lista única que mantenha separados os valores pares e impares. No final, mostre os valores pares,
#e ímpares em ordem crescente.

dados = [[], []]

for c in range(0, 7):
    n = int(input(f'({c+1})Digite um valor: '))
    if n % 2 == 0:
        dados[0].append(n)
    else:
        dados[1].append(n)

dados[0].sort
dados[1].sort
print(f'Pares: {dados[0]}')
print(f'Impares: {dados[1]}')
