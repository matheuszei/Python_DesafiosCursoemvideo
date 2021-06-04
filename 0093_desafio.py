#Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler
# o nome do jogador e a quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em
# cada partida. No final, tudo isso será guardado em um dicionário, incuindo o total de gols feitos
# durante o campeonato.

jogador = {}
gols = []
total = 0
jogador['nome'] = str(input('Nome do jogador: '))
ptd = int(input(f'Quantas partidas {jogador["nome"]} jogou: '))
for c in range(0, ptd):
    n = int(input(f'Quantos gols na partida {c+1}: '))
    gols.append(n)
    total += n
jogador['gols'] = gols[:]
jogador['total'] = total
print('-=' * 30)
print(jogador)
print('-=' * 30)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print('-=' * 30)
print(f'O jogador {jogador["nome"]} jogou {ptd} partidas')
for i, g in enumerate(gols):
    print(f'Na partida {i+1}, fez {g}')
print(f'Foi um total de {total} gols')

'''partidas = list ()
for c in range(0, ptd):
    partidas.append(int(input(f'Quantos gols na partida {c+1}: ')))
jogador['gols'] = partidas[:]
jogador['total'] = sum(partidas)'''