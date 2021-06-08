import random

g1 = str(input('Grupo 1:'))
g2 = str(input('Grupo 2:'))
g3 = str(input('Grupo 3:'))
g4 = str(input('Grupo 4:'))
lista = [g1, g2, g3, g4]
random.shuffle(lista)
print(f'A ordem ficou {lista}')
