#Crie uma tupla preenchida com os 20 primeiros colocados do Brasileirão 2020 na ordem de colocação.
#Mostre apenas os 5 primeiros colocados
#Mostre os últimos 4 colocados
#Liste com os times em ordem alfabética
#Mostre a posição do time Vasco da Gama no campeonato

brasileirao = ('Flamengo', 'Internacional', 'Atlético-MG', 'São Paulo', 'Fluminense',
               'Grêmio', 'Palmeiras', 'Santos', 'Athlético-PR', 'Bragantino', 'Ceará SC',
               'Corinthians', 'Atlético-GO', 'Bahia', 'Sport Recife', 'Fortaleza', 'Vasco da Gama',
               'Goiás', 'Coritiba', 'Botafogo')

print('-=' * 15)
print(brasileirao)
print('-=' * 15)
print(f'Os 5 primeiros são {brasileirao[0:5]}')
print('-=' * 15)
print(f'Os 4 últimos são: {brasileirao[-4:]}')
print('-=' * 15)
print(f'Times em ordem alfabética: {sorted(brasileirao)}')
print('-=' * 15)
print(f'O Vasco da Gama está na {brasileirao.index("Vasco da Gama")}° posição')
