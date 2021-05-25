#Crie um programa que leia vários números inteiros pelo teclado.
# No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor
# valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.

resp = True
maior = 0
menor = 9999
total = 0
soma = 0
while resp != False:
    n = int(input('Digite um valor: '))
    soma += n
    total += 1
    if n > maior:
        maior = n
    if n < menor:
        menor = n
    resp = input('Deseja continuar [S/N]? ').upper()
    if resp == 'N':
        resp = False
print('Média: {}'.format(soma / total))
print('Maior: {}'.format(maior))
print(('Menor: {}'.format(menor)))
