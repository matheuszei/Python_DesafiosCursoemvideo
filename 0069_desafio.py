#Crie um programa que leia a idade e o sexo de várias pessoas.
# A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar.
# No final, mostre:
#A) quantas pessoas tem mais de 18 anos.
#B) quantos homens foram cadastrados.
#C) quantas mulheres tem menos de 20 anos.

total18 = totalmasc = totalfem20 = 0
while True:
    sexo = 'X'
    cond = 'X'
    idade = int(input('Idade: '))
    while sexo != 'M' and sexo != 'F':
        sexo = input('Sexo [M/F]: ').upper()
    if idade >= 18:
        total18 += 1
    if sexo == 'M':
        totalmasc += 1
    if idade < 20 and sexo == 'F':
        totalfem20 += 1
    while cond != 'S' and cond != 'N':
        cond = input('Quer continuar? [S/N] ').upper()
    if cond == 'N':
        break
print('=== FIM DO PROGRAMA ===')
print(f'Total de pessoas com mais de 18 anos: {total18}')
print(f'Ao todo temos {totalmasc} homens cadastrados')
print(f'E temos {totalfem20} mulheres com menos de 20 anos')

