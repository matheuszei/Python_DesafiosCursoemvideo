#Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de mostrar que
# tipo de triângulo será formado:
# EQUILÁTERO: todos os lados iguais
# ISÓSCELES: dois lados iguais, um diferente
# ESCALENO: todos os lados diferentes

print('-=' * 20)
print('ANALISANDO TRIÂNGULO')
print('-=' * 20)
r1 = int(input('Digite o comprimento de A: '))
r2 = int(input('Digite o comprimento de B: '))
r3 = int(input('Digite o comprimento de C: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima PODEM formar um triângulo')
    if r1 == r2 and r1 == r3:
        print('Forma um triângulo equilátero')
    elif r1 != r2 and r1 != r3 and r2 != r3:
        print('Forma um triângulo escaleno')
    else:
         print('Forma um triângulo isósceles')
else:
    print('Os segmentos acima NÃO PODEM formar um triângulo')


