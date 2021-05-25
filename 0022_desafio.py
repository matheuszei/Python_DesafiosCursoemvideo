#Crie um programa que leia o nome completo de uma pessoa e mostre:
#O nome com todas as letras maiúsculas e minúsculas.
#Quantas letras ao todo sem considerar espaços.
#Quantas letras tem o primeiro nome

nome = input('Digite o seu nome completo: ')
print('Maiusculo: {}'.format(nome.upper()))
print('Minusculo: {}'.format(nome.lower()))
print('Total de letras (sem contar espaço): {}'.format(len(nome.strip())))
dividido = nome.split()
print('Total de letras do primeiro nome: {}'.format(len(dividido[0])))
