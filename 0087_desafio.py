#Aprimore o desafio anterior, mostrando no final:
#A) A soma de todos os valores pares digitados
#B) A soma dos valores da terceira coluna.
#C) O maior valor da segunda linha.

somaterceiracoluna = 0
somapar = 0
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para posição [{l},{c}]: '))

print('-=' * 15)
for l in range(0, 3):
    somaterceiracoluna += matriz[l][2] #Calculo - soma terceira coluna
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
        if matriz[l][c] % 2 == 0:
            somapar += matriz[l][c] #Calculo - soma números pares
    print()

print('-=' * 30)
print(f'A soma dos valores pares é {somapar}')
print(f'A soma dos valores da terceira coluna é {somaterceiracoluna}')
print(f'O maior valor da segudna linha é {max(matriz[1])}')

