#Crie um programa que vai gerar cinco números aleatórios de 1 a 10 e colocar em uma tupla.
#Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor.

from random import randint
numeros = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
print('Os valores sorteados foram:', end=' ')
for n in numeros:
    print(f'{n}', end=' ')
print(f'\nO maior valor sorteado foi {max(numeros)}')
print(f'O menor valor sorteado foi {min(numeros)}')

