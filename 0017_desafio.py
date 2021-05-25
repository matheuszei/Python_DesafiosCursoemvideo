#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente
# de um triângulo, calcule e mostre o comprimento da hipotenusa

from math import hypot
op = float(input('Digite o cateto oposto: '))
ad = float(input('Digite o cateto adjacente: '))
hp = hypot(op, ad)
print('O comprimento da hipotenusa é: {:.2f}'.format(hp))