#Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla.
#No final mostre:
#A)Quantas vezes apareceu o valor 9.
#B)Em que posição foi digitado o primeiro valor 3.
#C) Quais foram os números pares
par = 0
n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
n3 = int(input('Digite mais um número: '))
n4 = int(input('Digite o último número: '))

tn = (n1, n2, n3, n4)

print(f'Você digitou os valores {tn}')
print(f'O valor 9 aparece {tn.count(9)} vezes')

if 3 in tn:
    print(f'O valor 3 apareceu na {tn.index(3) + 1}° posição')
else:
    print('O valor 3 não foi digitado em nenhuma posição')

print('Os valores pares digitados foram', end=' ')
for c in tn:
    if c % 2 == 0:
        print(f'{c}', end=' ')
