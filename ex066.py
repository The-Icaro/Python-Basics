c = 0
total = 0
soma = 0
while c != 999:
    c = int(input('Digite um número inteiro, caso queira parar [999]:'))
    if c != 999:
        total += 1
        soma += c
print(f'A soma total dos {total} números lidos, foi de {soma}')
