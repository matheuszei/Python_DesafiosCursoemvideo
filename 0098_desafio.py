#Faça um programa que tenha uma função chamada contador(), que receba
# três parâmetros: inicio, fim, passo e realize a contagem.
# Seu programa tem que realizar três contagens através da função criada:
# A) De 1 até 10, de 1 em 1
# B) De 10 até 0, de 2 em 2
# C) Uma contagem personalizada

from time import sleep


def contador(inicio, fim, passo):
    print('-=' * 30)
    print(f'Contagem de {inicio} até {fim} de {passo} em {passo}')
    if passo == 0:
        passo = 1

    if passo < 0:
        passo *= -1
        while inicio != fim:
            sleep(0.3)
            print(f'{inicio} ', end='')
            inicio -= passo

    if inicio > fim:
        while inicio >= fim:
            sleep(0.3)
            print(f'{inicio} ', end='')
            inicio -= passo
    else:
        while inicio <= fim:
            sleep(0.3)
            print(f'{inicio} ', end='')
            inicio += passo
    print('FIM!')


contador(1, 10, 1)
contador(10, 0, 2)
print('-=' * 30)
print('Agora é a sua vez de personalizar a contagem!')
i = int(input('Inicio: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
contador(i, f, p)
