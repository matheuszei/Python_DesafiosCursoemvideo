#Escreva um programa que leia a velocidade de um carro.
# Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado.
# A multa vai custar R$7,00 por cada km acima do limite.

velocidade = float(input('Digite a velocidade de um carro: '))
multa = 0
if velocidade > 80.0:
    multa = (velocidade - 80) * 7.0
print('Você recebeu uma multa de: {:.2f}'.format(multa))
