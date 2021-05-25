#Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área
#e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta, pinta uma
#área de 2m²

largura = int(input('Digite a largura da parede em metros: '))
altura = int(input('Digite a altura da parede em metros: '))
area = largura * altura
print('Área da parede: {}m²'.format(area))
print('Quantidade de tinta necessária para pintar(em litros): {}'.format(area / 2))
