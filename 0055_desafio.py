#Faça um programa que leia o peso de cinco pessoas.
# No final, mostre qual foi o maior e o menor peso lidos.

maior = 0
menor = 500
for c in range (0, 6):
    peso = float(input('({}) - Informe o peso da pessoa: '.format(c)))
    if c == 1:
        maior = c
        menor = c
    else:
        if peso >= maior:
            maior = c
        if peso <= menor:
            menor = c
print('Maior peso informado: {}'.format(maior))
print('Menor peso informado: {}'.format(menor))
