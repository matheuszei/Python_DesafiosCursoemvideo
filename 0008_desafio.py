#Escreva um programa que leia um valor em metros e exiba convetido em centímetros e milímetros

metros = int(input('Digite um valor em METROS: '))
print('Valor em centímetros: {}'.format(metros * 100))
print('Valor em milímetros: {}'.format(metros * 1000))