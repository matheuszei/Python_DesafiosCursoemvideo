#Crie um programa que tenha um tupla totalmente preenchida com uma contagem por extenso, de zero até
#vinte. Seu programa deverá ler um numero pelo teclado(entre 0 e 20) e mostrá-lo por extenso.

tn = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove',
      'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezesete',
      'dezoito', 'dezenove', 'vinte')

while True:
    n = int(input('Digite um número entre 0 e 20: '))
    if 0 <= n <= 20:
        break
    else:
        print('Tente novamente.',end=' ')

print(f'Você digitou o número {tn[n]}')