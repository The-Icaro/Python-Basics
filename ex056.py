from datetime import date

print('=== | Grupo da Maioridade | ===')
menor = 0
maior = 0
for p in range(1,8):
    nasc = int(input('Ano de Nascimento:'))
    idade = date.today().year - nasc
    if idade >= 21:
        maior += 1
    else:
        menor += 1
print(f'Pessoas de Menor:{menor}\nPessoas de Maior:{maior}')
