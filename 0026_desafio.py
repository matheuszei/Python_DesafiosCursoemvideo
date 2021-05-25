#Faça um programa que leia um frase pelo teclado e mostre:
#Quantas vezes aparece a letra "A"
#Em que posição ela aparece a primeira vez
#Em que posição ela aparece a última vez

frase = input('Digite uma frase: ')
print ('Quantas vezes apareceu a letra "A": {}'.format(frase.upper().count('A')))
print('Aparece primeiramente no index: {}'.format(frase.upper().find('A')+1))
print('Aparece por última no index: {}'.format(frase.upper().rfind('A')+1))
