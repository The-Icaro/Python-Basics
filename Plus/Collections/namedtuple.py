"""
namedtuple() - Vem do módulo Collections
As principais coisas que podemos fazer com essa função é:
    Definir um nome da Tupla -> que é o Primeiro parâmetro -> x = namedtuple('Pontos', ...........)
    Definir nome tbm para os elementos -> que é o Segundo parâmetro -> x = namedtuple('Pontos', x, y, z)
    E adicionar a eles um valor -> Pontos = x(3, 4 ,5) -> Pontos(x=3, y=4, z=5)
"""
from collections import namedtuple

p1 = namedtuple('Pontos', 'x y z')  # Segundo Parâmetro pode ser uma tupla, lista ou dict
# Nesse caso, ele vai quebrar a str='x y z' em 3 elementos
# Para Listas = ...., ['x', 'y', 'z'] -> O resultado será o mesmo
# Para Dict = ...., {'x': 0, 'y': 0, 'z': 0} -> Ele vai ignorar o 0, e o resultado vai ser o mesmo tbm
pontos = p1(7, 4, 5)  # Adiciona Valores para os elementos
print(pontos)
print()
print(pontos.x, pontos.y, pontos.z)  # Vai mostrar o valor daquele elemento depois do . Nesse caso == 7 4 5
print(pontos[0])  # Meio normal de se fazer com uma tupla
print(pontos._asdict())  # Mostra em forma de Dict, com elemento : valor -> ([('x', 7), ('y', 4), ('z', 5)])
print(pontos._fields)  # Mostra o nome dos elementos, nesse caso -> ('x' 'y' 'z')
pontos = pontos._replace(y=10)  # Cria uma nova tupla, com o mesmo nome('Pontos'), com a variação dentro do parâmetro
print(pontos)  # Então aqui -> Pontos(x=7, y=10, z=5)
pontos1 = pontos._make('ahx')  # Cria outra nova tupla, agora com os valores dos elementos antigos com esse parâmetro, mesmo formato para Listas e Dict
print(pontos1)  # Nesse caso, aqui ficaria -> x='a', y='h', z='x'
