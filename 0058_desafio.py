#Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0 e 10.
# Só que agora o jogador vai tentar adivinhar até acertar,
# mostrando no final quantos palpites foram necessários para vencer.

import random
from time import sleep
num = random.randint(1, 5)
resp = 11
cont = 0
print('Tente adivinhar um número de 1 a 10')
while resp != num:
    resp = int(input('Digite um valor: '))
    print('PREOCESSANDO...')
    cont += 1
    sleep(3)
    if resp == num:
        print('Parabens! Você acertou, o número era {}'.format(num))
    else:
        print('Você errou. Tente novamente!')
print('Você precisou de {} tentativas para acertar'.format(cont))