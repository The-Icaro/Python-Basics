print('=== | P.A | ===')
p1 = int(input('Primeiro Termo:'))
p2 = int(input('Razão:'))
p3 = p1 + (10 - 1) * p2
for c in range(p1, p3+p2, p2):
    print(c, end=', ')
print('...')