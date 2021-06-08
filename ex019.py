import math

co = float(input('Qual o valor do cateto oposto?'))
ca = float(input('Qual o valor do cateto adjacente?'))
h = math.hypot(co, ca)
print(f'No seu Triângulo Retângulo:\nCateto Oposto: {co}\nCateto Adjacente: {ca}\nHipotenusa: {h:.3f}')
