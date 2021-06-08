print('=== | Número Primo | ===')
n = int(input('Digite um número:'))
t = 0
for c in range(1, n+1):
    if n % c == 0:
        print('\033[32m', end=' ')
        t += 1
    else:
        print('\033[31m', end=' ')
    print(c, end=' ')
print(f'\033[m\nO número {n} foi dividido {t} vezes')
if t == 2:
    print('Então ele É PRIMO')
else:
    print('Então ele NÃO É PRIMO')


