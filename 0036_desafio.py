#Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
# Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
# A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

#Entrada de dados
nome = str(input('Olá! Como você se chama? '))
valor = float(input('{} informe o valor da casa que deseja adquirir: '.format(nome)))
salario = float(input('Informe o seu salário: '))
anos = int(input('Informe em quantos anos você vai pagar: '))

#Calculos / Saida de dados
prestacao = valor / (anos * 12)
print('Valor da prestação mensal a ser paga: {:.2f}'.format(prestacao))
if prestacao > (salario * 1.3 - salario):
    print('{} devido a prestação exceder 30% o valor do seu salário, o emprestido foi NEGADO'.format(nome))
else:
    print('Emprestimo APROVADO! Parabéns {}'.format(nome))
