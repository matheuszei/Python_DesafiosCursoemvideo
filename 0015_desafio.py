#Escreva um programa que pergunta a quantidade de KM percorrido por um carro alugado e a quantidade
#de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia
#e R$0,15 por KM rodado.

dias = int(input('Quantos dias alugados? '))
km = int(input('Quantos KM rodados? '))
preco = ((dias * 60) + (km * 0.15))
print('O total a pagar é de {:.2f}'.format(preco))