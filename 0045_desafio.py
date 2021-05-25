#Crie um programa que faça o computador jogar Jokenpô com você.

import random
from time import sleep
num = random.randint(1, 3)
print('=' * 35)
print('JOKENPÔ')
print('=' * 35)
#print(num)
opcao = int(input('ESCOLHA \n1- PEDRA \n2- PAPEL \n3- TESOURA \nOPCAO: '))
print('PREOCESSANDO...')
sleep(2)
if num == 1 and opcao == 1:
    print('EMPATE')
elif num == 1 and opcao == 2:
    print('VOCÊ GANHOU!')
elif num == 1 and opcao == 3:
    print('VOCÊ PERDEU!')
if num == 2 and opcao == 2:
    print('EMPATE')
elif num == 2 and opcao == 3:
    print('VOCÊ GANHOU!')
elif num == 2 and opcao == 1:
    print('VOCÊ PERDEU!')
if num == 3 and opcao == 3:
    print('EMPATE')
elif num == 3 and opcao == 1:
    print('VOCÊ GANHOU!')
elif num == 3 and opcao == 2:
    print('VOCÊ PERDEU!')
