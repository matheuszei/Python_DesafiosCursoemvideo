#Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar()
# A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai
# mostrar a soma entre todos os valores PARES sorteados pela função anterior.

from random import randint


def sorteia(lst):
    print('Sorteando 5 valores da lista: ', end='')
    for cont in range(0, 5):
        n = randint(1, 10)
        lst.append(n)
        print(n, end=' ')
    print('PRONTO!')


def somaPar(lst):
    pos = soma = 0
    while pos < len(lst):
        if lst[pos] % 2 == 0:
            soma += lst[pos]
        pos += 1
    print(f'Somando os valores pares {lst}, temos {soma}')


valores = []
sorteia(valores)
somaPar(valores)





