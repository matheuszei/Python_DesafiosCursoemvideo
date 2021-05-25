#Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'.
# Caso esteja errado, peça a digitação novamente até ter um valor correto.

cond = False
while cond != True:
    resp = str(input('Digite o sexo da pessoa: ')).upper()
    if resp == 'M' or resp == 'F':
        cond = True
print('Sexo digitado: {}'.format(resp))
