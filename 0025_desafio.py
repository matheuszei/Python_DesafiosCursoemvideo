#Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.

nome = input('Digite um nome: ')
print('A pessoa possui SILVA? {}'.format('Silva' in nome.upper()))
