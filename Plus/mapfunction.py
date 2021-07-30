"""
map function - map()
 - Utiliza-se para aplicar uma função em cada elemento de uma lista
 - Leva 2 Parâmetros : Um para a função e o Segundo a Lista
"""

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def func(x):
    return x*2


#  Maneira Tradicional de se Fazer
novalista = []
for e in lista:
    novalista.append(func(e))
print(novalista)

print('-'*35)
# Fazendo com o map()
novalista1 = list(map(func, lista))  # list : fazer uma nova lista, map : 1 = func, 2 = lista
print(novalista1)

print('-'*35)
# Ou ainda
novalista2 = ([func(x) for x in lista])
print(novalista2)