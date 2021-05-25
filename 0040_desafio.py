# Crie um programa que leia duas notas de um aluno e calcule sua média,
# mostrando uma mensagem no final, de acordo com a média atingida:
# Média abaixo de 5.0: REPROVADO
# Média entre 5.0 e 6.9: RECUPERAÇÃO
# Média 7.0 ou superior: APROVADO

nome = str(input('Olá! Informe o nome do aluno: '))
n1 = float(input('Informe a N1: '))
n2 = float(input('Informe a N2: '))
media = (n1 + n2) / 2
#Processo!!
if media < 5.0:
    print('REPROVADO')
elif media > 5.0 and media < 6.9:
    print('RECUPERAÇÃO')
else:
    print('APROVADO. PARABÉNS {}'.format(nome))
