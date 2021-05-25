#Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo
#e todas as informações possíveis sobre ele.

algo = input('Digite algo: ')
print('O que você digitou é do tipo: ', type(algo))
print("É texto?: ", algo.isalpha())
print("É númerico?: ", algo.isnumeric())
print("É alfanúmerico?: ", algo.isalnum())
