#Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

n1 = float(input('Digite N1: '))
n2 = float(input('Digite N2: '))
n3 = float(input('Digite N3: '))
if n1 < n2 and n1 < n3:
    menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3
if n1 > n2 and n1 > n3:

    maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3
print('Maior número: {}'.format(maior))
print('Menor número: {}'.format(menor))
