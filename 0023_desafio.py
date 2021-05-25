#Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos digitos separados.

x = int(input('Digite um número de 0 a 9999: '))
u = x // 1 % 10
d = x // 10 % 10
c = x // 100 % 10
m = x // 1000 % 10
print('Unidade: {}'.format(u))
print('Dezena: {}'.format(d))
print('Centena: {}'.format(c))
print('Milhar: {}'.format(m))
