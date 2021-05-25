#Crie um programa que vai ler vários números e colocar em uma lista.
#Depois disso, crie duas listas extras que vão conter apenas os valores pares e impares digitados.
#Ao final, mostre o conteúdo das três listas geradas

num = []
par = []
impar = []
while True:
    num.append(int(input('Digite um valor: ')))
    resp = input('Deseja continuar? [S/N] ').upper()
    if resp == 'N':
        break
for i, v in enumerate(num):
    if v % 2 == 0:
        par.append(v)
    elif v % 2 == 1:
        impar.append(v)
print('-=' * 30)
print(f'A lista completa é {num}')
print(f'A lista de pares é {par}')
print(f'A lista de impares é {impar}')
