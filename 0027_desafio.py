#Faça um programa que leia o nome completo de uma pessoa,
# mostrando em seguida o primeiro e o último nome separadamente

nome = input('Digite o nome completo: ')
div = nome.split()
print('Primeiro nome: {}'.format(div[0]))
print('Ultimo nome: {}'.format(div[len(div)-1]))
