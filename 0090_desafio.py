#Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário.
# No final, mostre o conteúdo da estrutura na tela.

dic = {}
dic['nome'] = str(input('Nome: '))
dic['media'] = float(input(f'Média de {dic["nome"]}: '))
if dic['media'] >= 7:
    dic['situacao'] = 'Aprovado'
else:
    dic['situacao'] = 'Reprovado'

for k, v in dic.items():
    print(f'{k} é igual a {v}')

