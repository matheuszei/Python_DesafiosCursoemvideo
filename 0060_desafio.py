#Faça um programa que leia um número qualquer e mostre o seu fatorial.

from math import factorial
n = int(input('Digite um numero: '))
c = n
f = factorial(n)
print('Calculando {}!'.format(n))
while c > 0:
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    c -= 1
print('{}'.format(f))
