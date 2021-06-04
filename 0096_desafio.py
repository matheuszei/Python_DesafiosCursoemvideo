#Faça um programa que tenha uma função chamada area(), que receba as dimensões de um terreno
# retangular (largura e comprimento) e mostre a área do terreno.

def area(l, c):
    a = l * c
    print(f'A área de um terreno {l}x{c} é de {a}m²')


print('Controle de Terrenos')
l = float(input('LARGURA (m): '))
c = float(input('COMPRIMENTO (m): '))
area(l, c)
