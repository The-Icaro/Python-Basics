times = ('Flamengo', 'Internacional', 'Atlético-MG', 'São Paulo', 'Fluminense', 'Grêmio', 'Palmeiras',
         'Santos', 'Atlético-PR', 'Corinthians', 'Bragantino', 'Ceará', 'Atlético-GO', 'Sport Recife', 'Bahia',
         'Fortaleza', 'Vasco Da Gama', 'Goiás', 'Coritiba', 'Botafogo')
print(f'Os Clubes Times Do Brasileirão São: ')
print(sorted(times))
print('-'*30)
print('Os Cinco Primeiros Colocados São:')
print(times[0:5])
print('-'*30)
print(f'Os 4 Últimos Colocados São:')
print(times[-4:])
print('-'*30)
print(f'O Corinthians está na {times.index("Corinthians")+1} Posição')
print('-'*30)
