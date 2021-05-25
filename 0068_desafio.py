#Faça um programa que jogue par ou ímpar com o computador.
# O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas
# que ele conquistou no final do jogo.

import random
win = 0
print('=-' * 15)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('=-' * 15)
while True:
    v = int(input('Digite um valor: '))
    c = input('Par ou Ímpar? [P/I]: ').upper()
    n = num = random.randint(1, 10)
    if (v + n) % 2 == 0:
        print(f'Você jogou {v} e o computador {n}. Total de {v + n} DEU PAR')
        print('-' * 15)
        if c == 'P':
            print('VOCÊ GANHOU')
            win += 1
        else:
            print('VOCÊ PERDEU')
            print('=-' * 15)
            print(f'GAME OVER! Você venceu {win} vezes.')
            break
    else:
        print(f'Você jogou {v} e o computador {n}. Total de {v + n} DEU IMPAR')
        print('-' * 15)
        if c == 'I':
            print('VOCÊ GANHOU')
            win += 1
        else:
            print('VOCÊ PERDEU')
            print('=-' * 15)
            print(f'GAME OVER! Você venceu {win} vezes.')
            break
        print('-' * 15)

