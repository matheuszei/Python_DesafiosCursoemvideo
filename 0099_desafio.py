#Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores
# inteiros. Seu programa tem que analisar todos os valores e dizer qual deles é o maior

from time import sleep


def maior(*num):
    print('-=' * 15)
    print('Analisando os valores passados....')

    if len(num) <= 0:
        print(f'Foram informados {len(num)} valores ao todo. ')
        print('O maior valor informado foi 0')
    else:
        for valor in num:
            sleep(0.3)
            print(valor, end=' ')
        print(f'Foram informados {len(num)} valores ao todo. ')
        print(f'O maior valor informado foi {max(num)}')


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
