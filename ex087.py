valor = []
pares = []
impares = []
for v in range(0, 7):
    valor.append(int(input('Digite um valor: ')))
    for n in valor:
        if n % 2 == 0:
            pares.append(n)
            valor.clear()
            pares.sort()
        else:
            impares.append(n)
            valor.clear()
            impares.sort()
print('-'*30)
print(f'Os valores Pares encontrados foram: {pares}')
print(f'Os valores Ímpares encontrados foram: {impares}')
