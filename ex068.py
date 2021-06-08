nt = s = 0
while True:
    n = int(input('Digite um número:'))
    if n == 999:
        break
    nt += 1
    s += n
print(f'A Soma dos {nt} números, é de {s}')

