from random import sample
numeros = tuple(sample(range(10), 5))
print(f'Os Números Gerados são: {numeros}')
print(f'O Maior Número Gerado foi : {max(numeros)}')
print(f'O Menor Número Gerado foi : {min(numeros)}')