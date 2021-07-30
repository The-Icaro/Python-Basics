"""
filter function - filter()
 - Como o nome diz, ela filtra (se for True)  os dados.py que recebem, apartir de um função
 - Recebe 2 Parâmetros :  Um para a função e o Segundo para a lista
"""


def par(x):
    return x % 2 == 0  # A função vai retornar , só se x % 2 == 0 True


a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

b = list(filter(par, a))  # filter vai receber esses dados.py, pela lista = a e se for True pela função par(), ele vai add na lista b

print(a)
print('-' * 30)
print(b)
