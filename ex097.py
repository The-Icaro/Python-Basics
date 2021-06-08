ficha = {}
registro = []
total = 0
gols = []
while True:
    ficha['nome'] = str(input('Nome: ')).strip().title()
    partidas = int(input(f'Quantas Partidas {ficha["nome"]} Jogou?: '))
    for p in range(0, partidas):
        golpartida = int(input(f'Quantos Gols na {p+1} Partida: '))
        total += golpartida
        gols.append(golpartida)
    ficha['gols'] = gols[:]
    ficha['total'] = total
    ficha['partidas'] = partidas
    registro.append(ficha.copy())
    gols.clear()
    total = 0
    pergunta = str(input('Deseja Continuar?: ')).strip().lower()[0]
    if pergunta != 's' and pergunta != 'n':
        pergunta = str(input('RESPOSTA INVÁLIDA! Escolha entre Sim ou Não!: ')).strip().lower()[0]
    if pergunta == 'n':
        break
print(registro)
print('-'*55)
print('No ', end='')
for i in ficha.keys():
    print(f'{i:<15}', end='')
print()
print('-'*55)
for k, v in enumerate(registro):
    print(f'{k:>4} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-'*55)
while True:
    dados = int(input('Mostrar dados de qual Jogador? (999 interrompe): '))
    if dados == 999:
        break
    if dados > len(registro):
        dados = int(input('ESCOLHA INVÁLIDA. Mostrar dados de qual jogador?: '))
    else:
        print(f'Levantamento do Jogador {registro[dados]["nome"]}')
        for i, v in enumerate(registro[dados]["gols"]):
            print(f'=> Na Partida {i + 1}, fez {v} Gols')
    print('-' * 55)