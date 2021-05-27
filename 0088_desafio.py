#Faça um programa que ajude um jogador da MEGA SENA a criar palpites. O programa vai pergutar
#quantos jogos seráo gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando
#tudo em uma lista composta.

from random import randint
import time
jogos = []
numeros = []
print('-' * 30)
print(f'{"JOGO NA MEGA SENA":^30}')
print('-' * 30)

qtdjogos = int(input('Quantos jogos você quer que eu sorteie? '))
for c in range(0, qtdjogos):
    while True:
        n = randint(1, 60)
        if n not in numeros:
            numeros.append(n)
        if len(numeros) == 6:
            break
    numeros.sort()
    jogos.append(numeros[:])
    numeros.clear()

for i in range(0, qtdjogos):
    print(f'Jogo {i+1}: {jogos[i]}')
    time.sleep(1)
print('-=' * 5, end='')
print(f' < BOA SORTE! > ', end='')
print('-=' * 5, end='')
