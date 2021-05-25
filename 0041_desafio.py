#A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento
# de um atleta e mostre sua categoria, de acordo com a idade:
# Até 9 anos: MIRIM
# Até 14 anos: INFANTIL
# Até 19 anos: JÚNIOR
# Até 25 anos: SÊNIOR
# Acima de 25 anos: MASTER

from datetime import date
anonasc = int(input('Informe o ano de nascimento do natador: '))
anoatual = date.today().year
idade = anoatual - anonasc

#PROCESSAMENTO
if idade < 10:
    print('MIRIM')
elif idade > 9 and idade < 15:
    print('INFANTIL')
elif idade > 14 and idade < 20:
    print('JUNIOR')
else:
    print('MASTER')
