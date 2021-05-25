#Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
# Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido.

import random
n1 = input('Digite o 1° nome: ')
n2 = input('Digite o 2° nome: ')
n3 = input('Digite o 3° nome: ')
n4 = input('Digite o 4° nome: ')
lista = [n1, n2, n3, n4]
escolhido = random.choice(lista)
print('O aluno escolhido foi: {}'.format(escolhido))
