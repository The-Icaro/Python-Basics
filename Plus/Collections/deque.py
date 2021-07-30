"""
deque() - Vem do módulo Collections
    É como se fosse uma lista, porém um deque
    E se usa pelas variedades de funções, assim abaixo
    Como parâmetro pode ser qualquer Container
"""

from collections import deque

d = deque('ola')  # O Parâmetro pode ser qualquer Container, que o resultado vai ser o mesmo -> deque([.....])
print(d)
d.append('20')  # Funciona como um .append() normal, no fim da lista
d.append(5)
print(d)
d.appendleft('n')  # Adiciona na posição zero da lista
print(d)
d.pop()  # Remove o último elemento da lista, normal como .pop()
d.popleft()  # Remove o elemento na posição 0
print(d)
print(d.count('a'))  # .count() padrão
d.extend('456')  # Ele adiciona o que estiver no parâmetro(Qualquer Container), para o final da lista
d.extendleft([1, 6, 9, 5])  # Faz o mesmo só que na posição 0
print(d)
d.rotate(-2)  # Faz com que os elementos se movam pelo número do parâmetro, se o int = negativo (para a esquerda)
print(d)
d.rotate(5)  # Se o int = positivo (para a direita)
print(d)
a = deque('ola', maxlen=3)  # maxlen é o tamanho máximo que o deque pode chegar
print(a)
a.append(1)  # Se eu tentar acrescentar um novo elemento, ele vai dar um rotate(-1), e vai trasformar o último elemento(dps do rotate) pelo novo elemento
print(a)
a.extend([1, 2, 3])  # Nesse caso, como o maxlen=3, ele substitui todos os valores pelos novos
print(a)
a.reverse()  # igual reverse=True
print(a)