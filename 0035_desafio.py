#Desenvolva um programa que leia o comprimento de três retas e diga ao usuário
# se elas podem ou não formar um triângulo

print('-=' * 20)
print('ANALISANDO TRIÂNGULO')
print('-=' * 20)
r1 = int(input('Digite o comprimento de A: '))
r2 = int(input('Digite o comprimento de B: '))
r3 = int(input('Digite o comprimento de C: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima PODEM formar um triângulo')
else:
    print('Os segmentos acima NÃO PODEM formar um triângulo')
