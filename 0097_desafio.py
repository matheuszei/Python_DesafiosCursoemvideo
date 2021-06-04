#Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como
# parâmetro e mostre uma mensagem com tamanho adaptável.
# Ex: escreva ('Olá, Mundo!')
# Sáida:
# ~~~~~~~~
# Olá, Mundo!
# ~~~~~~~~

def mensagem(msg):
    print('~' * len(msg))
    print(msg)
    print('~' * len(msg))
    print()


mensagem('Matheus Zei')
mensagem('Curso de Python')
mensagem('teste')

