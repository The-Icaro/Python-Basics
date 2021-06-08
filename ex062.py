n = int(input('Digite um Número:'))
print(f'O Fatorial de {n}! = ', end='')
r = 1
for c in range(n, 0, -1):
    print(c, end='')
    if c > 1:
        print(' x ', end='')
    else:
        print(' = ', end='')
    r *= c
print(f'{r}')


