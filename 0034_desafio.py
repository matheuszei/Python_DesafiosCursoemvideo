#Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
# Para salários superiores a R$1250,00, calcule um aumento de 10%.
# Para os inferiores ou iguais, o aumento é de 15%

salario = float(input('Digite o salário do funcionário: '))
reajuste = 0
if salario > 1250.00:
    reajuste = salario * 1.10
else:
    reajuste = salario * 1.15
print('O novo salario é: {}'.format(reajuste))
