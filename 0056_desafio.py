#Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
# No final do programa, mostre: a média de idade do grupo,
# qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.

totalidade = 0
maioridade = 0
totalfem = 0
for c in range(0, 4):
    print('Pessoa: {}'.format(c+1))
    nome = str(input('Digite o nome da pessoa: '))
    idade = int(input('Digite a idade: '))
    sexo = str(input('Digite o sexo (F/M): ')).lower()
    totalidade += idade
    if sexo == 'm' and idade > maioridade:
        maioridade = idade
        hmvelho = nome
    if sexo == 'f' and idade < 20:
        totalfem += 1
media = totalidade / 4
print('Média de idade do grupo: {}'.format(media))
print('Homem mais velho: {}, {} anos'. format(hmvelho, maioridade))
print('Total de mulheres com menos de 20 anos: {}'.format(totalfem))

