linha0 = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
pares = 0
soma = 0
maior = 0
for l in range(0, 3):
    for c in range(0, 3):
        linha0[l][c] = int(input(f'Digite um número ({l}:{c}):'))
print('-'*30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{linha0[l][c]:^5}]', end='')
        if linha0[l][c] % 2 == 0:
            pares += linha0[l][c]
    print()
for l in range(0, 3):
    soma += linha0[l][2]
for c in range(0 ,3):
    if c == 0:
        maior = linha0[1][c]
    if linha0[1][c] > maior:
        maior = linha0[1][c]
print('-'*30)
print(f'A soma dos valores na Terceira Coluna é {soma}')
print(f'A soma de todos os valores Pares é {pares}')
print(f'O maior valor da Segunda Linha é {maior}')