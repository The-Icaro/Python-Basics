import math
a = float(input('Valor do ângulo:'))
s = math.sin(math.radians(a))
c = math.cos(math.radians(a))
t = math.tan(math.radians(a))
print(f'Com o ângulo de {a}°, você terá:\nSeno: {s:.5f}\nCossenos: {c:.5f}\nTangente: {t:.5f}')
