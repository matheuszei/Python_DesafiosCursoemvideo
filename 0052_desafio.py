#Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

n = int(input('Digite um numero: '))
v = True
cont = 0
for c in range(1, n+1):
    if n % c == 0:
        cont += 1
        if cont > 2:
            v = False
if v == True:
    print('O número {} é PRIMO'.format(n))
else:
    print('O número {} NÃO É PRIMO'.format(n))
