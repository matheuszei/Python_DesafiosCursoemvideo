#Escreva um programa em Python que leia um número inteiro qualquer
# e peça para o usuário escolher qual será a base de conversão:
# 1 para binário, 2 para octal e 3 para hexadecimal.

n = int(input('Digite um número inteiro: '))
print('=' * 35)
print('Escolha qual será a base de conversão')
print('=' * 35)
print('1 - Binário \n2- Octal \n3- Hexadecimal')
print('-' * 35)
opcao = int(input('Digite a opção: '))

#Calculo / Saida de dados
if opcao == 1:
    print('Binário: {}'.format(bin(n)[2:]))
elif opcao == 2:
    print('Octal: {}'.format(oct(n)[2:]))
elif opcao == 3:
    print('Hexadecimal: {}'.format(hex(n)[2:]))
else:
    print('Opção inválida!!')
