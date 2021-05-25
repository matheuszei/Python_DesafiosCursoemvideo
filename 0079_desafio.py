#Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os
#em uma lista. Caso o número já exista lá dentro, ele não será adicionado.
#No final, seráo exibidos todos os valores únicos digitados, em ordem crescente.

numero = []
while True:
    n = int(input('Digite um valor: '))
    if n in numero:
        print('Valor duplicado! Não vou adicionar...')
    else:
        numero.append(n)
        print('Valor adicionado com sucesso...')
        resp = input('Quer continuar? [S/N] ').upper()
        if resp == 'N':
            break

print('-=' * 15)
print(f'Você digitou os valores {sorted(numero)}')

#Nota - poderia usar if n not in numero:
                        #numero.append(n)
                        #print('Valor adicionado com sucesso...')
                        #resp = input('Quer continuar? [S/N] ').upper()
                        #if resp == 'N':
                         #   break