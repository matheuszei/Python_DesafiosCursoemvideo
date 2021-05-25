#Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO"

cidade = input('Digite o nome de uma cidade: ').strip().upper()
print('SANTO' in cidade[0:5])

#cidade = input('Digite o nome de uma cidade: ').strip()
#print(cidade[:5].upper() == 'SANTO)
