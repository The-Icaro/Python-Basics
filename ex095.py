ficha = {}
gols = []
total = 0
ficha['nome'] = str(input('Nome: ')).strip().title()
partidas = int(input(f'Quantas Partidas {ficha["nome"]} Jogou?: '))
for c in range(0, partidas):
    gol = int(input(f'Quantos Gols fez {c+1} Partida: '))
    gols.append(gol)
    total += gol
ficha['gols'] = gols
ficha['total'] = total
print(ficha)
print('-=' * 30)
for k, v in ficha.items():
    print(f'O campo {k} tem o valor {v}.')
print('-=' * 30)
print(f'O jogador {ficha["nome"]}, jogou {partidas} partidas!')
for i, v in enumerate(gols):
    print(f'=> Na Partida {i+1}, fez {v} Gols')
print(f'Foi um Total de {ficha["total"]} Gols!')
