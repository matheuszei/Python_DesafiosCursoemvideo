#Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5
# e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
# O programa deverá escrever na tela se o usuário venceu ou perdeu.

import random
from time import sleep
num = random.randint(1, 5)
#print(num)
resp = int(input('Tente adivinhar um número de 1 a 5: '))
print('PREOCESSANDO...')
sleep(3)
if resp == num:
    print('Parabens! Você acertou, o número era {}'.format(num))
else:
    print('Você errou. Tente novamente!')
