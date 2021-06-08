from random import randint
print('-'*30)
print('           MEGASENA         ')
print('-'*30)
lista = []
jogos = []
total = 1
vezes = int(input('Quantos Jogos você quer fazer? '))
while total <= vezes:
    contagem = 0
    while True:
        numero = randint(0, 60)
        if numero not in lista:
            lista.append(numero)
        contagem += 1
        if contagem >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    total += 1
for l, n in enumerate(jogos):
    print(f'Jogo {l+1}: {n}')
