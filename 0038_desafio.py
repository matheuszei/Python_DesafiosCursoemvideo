#Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela
# uma mensagem:
#O primeiro valor é maior
#O segundo valor é maior
#Não existe valor maior, os dois são iguais

n1 = int(input('Digite o valor de N1: '))
n2 = int(input('Digite o valor de N2: '))
if n1 > n2:
    print('O valor de N1 é maior')
elif n2 > n1:
    print('O valor de N2 é maior')
else:
    print('Não existe valor maior, os dois são iguais')
