"""
lambda function - lambda
- É como uma função anônima, que retorna somente um valor
- Funciona como um função, então pode ter vários parâmetros, esses podendo ser variáveis
- Se utiliza para não ficar criando um monte de defs, para manter organizado e simples
"""


def add5(x):  # Função simples
    return x + 5


soma5 = lambda x, y = 0: x + y  # Lambda x,y -> Parâmetros ; x + y -> O que ela vai retornar

print(soma5(4))
print(add5(4))

print('-'*30)

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

b = list(map(lambda x: x + 5, a))  # Uso de lambda com Map()
print(b)

print('-'*30)

c = list(filter(lambda x: x % 2 == 0, a))  # Uso de lambda com Filter()
print(c)