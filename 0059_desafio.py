#Crie um programa que leia dois valores e mostre um menu na tela:
#[ 1 ] somar
#[ 2 ] multiplicar
#[ 3 ] maior
#[ 4 ] novos números
#[ 5 ] sair do programa
#Seu programa deverá realizar a operação solicitada em cada caso.

n1 = int(input('Digite o valor 1: '))
n2 = int(input('Digite o valor 2: '))
opcao = 0
calc = 0
print('MENU')
print('[1]Somar \n[2]Multiplicar \n[3]Maior \n[4]Novos números \n[5]Sair do programa \n')
while opcao != 5:
    opcao = int(input('Digite uma opção: '))
    if opcao == 1:
       calc = n1 + n2
       print('Soma dos valores: {}'.format(calc))
    elif opcao == 2:
        calc = n1 * n2
        print('Multiplicação dos valores: {}'.format(calc))
    elif opcao == 3:
        if n1 > n2:
            print('{} é maior que {}'.format(n1, n2))
        elif n2 > n1:
            print('{} é maior que {}'.format(n2, n1))
        else:
            print('{} e {} são iguais'.format(n1, n2))
    elif opcao == 4:
        n1 = int(input('Digite o novo valor de 1: '))
        n2 = int(input('Digite o novo valor de 2: '))
print('FIM DO PROGRAMA')


