from random import randint
from time import sleep as s


def sorteio():
    for c in range(0, 5):
        numero = randint(0, 5)
        numeros.append(numero)
    print('Os números sorteados foram:')
    for c in numeros:
        print(f'{c} ', end='', flush=True)
        s(0.3)


def somapar():
    cont = soma = 0
    for c in numeros:
        if c % 2 == 0:
            soma += c
        cont += 1
    print(f'\nDos {cont} valores sorteados, a soma dos valores Pares é {soma}')


numeros = []
sorteio()
somapar()
