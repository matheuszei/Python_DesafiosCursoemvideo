#Escreva um programa que converta uma temperatura digitada em °C e converta para °F.

c = float(input('Informe a temperatura em C: '))
f = (c * 1.80) + 32
print('A temperatura de {}°C corresponde a {:.1}°F!'.format(c, f))
