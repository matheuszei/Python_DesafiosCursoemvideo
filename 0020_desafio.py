#O mesmo professor do desafio anterior(19) quer sortear a ordem de apresentação
# de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos
# e mostre a ordem sorteada.

from random import shuffle
n1 = input('Digite o 1° nome: ')
n2 = input('Digite o 2° nome: ')
n3 = input('Digite o 3° nome: ')
n4 = input('Digite o 4° nome: ')
lista = [n1, n2, n3, n4]
shuffle(lista)
print('A ordem de apresentação será')
print(lista)