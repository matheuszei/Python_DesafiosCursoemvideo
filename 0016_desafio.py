#Crie um programa que leia um número REAL qualquer pelo teclado e
# mostre na tela sua porção inteira


from math import trunc
numero = float(input('Digite um número: '))
porcao = trunc(numero)
print('A porção de {} equivale a: {}'.format(numero, porcao))
