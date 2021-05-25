#Elabore um programa que calcule o valor a ser pago por um produto,
# considerando o seu preço normal e condição de pagamento:
# à vista dinheiro/cheque: 10% de desconto
# à vista no cartão: 5% de desconto
# em até 2x no cartão: preço formal
# 3x ou mais no cartão: 20% de juros

preco = float(input('Informe o preço do produto: '))
print('='*35)
print('ESCOLHA A FORMA DE PAGAMENTO')
print('='*35)
print('1- À Vista (dinheiro) \n2- À Vista (cartão) \n3- Em até 2x no cartão \n4- 3x ou mais no cartão')
print('-' * 35)
opcao = int(input('OPCAO: '))
precofinal = 0
#PROCESSAMENTO
if opcao == 1:
   precofinal = (preco * 0.90)
   print('Desconto de 10% incluso')
   print('Preço final: {:.2f}'.format(precofinal))
elif opcao == 2:
    precofinal = (preco * 0.95)
    print('Desconto de 5% incluso')
    print('Preço final: {:.2f}'.format(precofinal))
elif opcao == 3:
    precofinal = preco
    print('Sem desconto')
    print('Preço final: {:.2f}'.format(precofinal))
elif opcao == 4:
    precofinal = preco * 1.20
    print('Juros de 20% incluso')
    print('Preço final: {:.2f}'.format(precofinal))
else:
    print('Opção inválida!')