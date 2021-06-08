pessoas = list()
dados = list()
totalp = 0
maior = menor = 0
while True:
    dados.append(str(input('Nome: ')).strip().title())
    dados.append(float(input('Peso: ')))
    totalp += 1
    if len(pessoas) == 0:
        maior = menor = dados[1]
    else:
        if dados[1] > maior:
            maior = dados[1]
        if dados[1] < menor:
            menor = dados[1]
    pessoas.append(dados[:])
    dados.clear()
    pergunta = str(input('Deseja Continuar? ')).strip().lower()[0]
    while pergunta != 's' and pergunta != 'n':
        pergunta = str(input('RESPOSTA INVÁLIDA! Escolha entre Sim ou Não! ')).strip().lower()[0]
    if pergunta == 'n':
        break
print('-'*50)
print(f'O número total de pessoas cadastrados é de {totalp}.')
print(f'O maior peso foi de {maior}Kg. Peso de', end=' ')
for p in pessoas:
    if p[1] == maior:
        print(f'{p[0]}', end=' ')
print(f'\nO menor peso foi de {menor}Kg. Peso de', end=' ')
for p in pessoas:
    if p[1] == menor:
        print(f'{p[0]}', end=' ')

