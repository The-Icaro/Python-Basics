print('=== | Balança | ===')
maior = 0
menor = 0
for p in range(1,6):
    peso = float(input('Peso:'))
    if p == 1:
        maior = peso
        menor = peso
    if peso > maior:
        maior = peso
    if peso < menor:
        menor = peso
print(f'O Maior peso foi: {maior}Kg\nO Menor peso foi: {menor}Kg')
