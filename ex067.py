c = 's'
media = 0
total = 0
maior = 0
menor = 0
while c is 's':
    n = int(input('Digite um Número Inteiro:'))
    total += 1
    media += n
    if total == 1:
        maior = n
        menor = n
    if n > maior:
        maior = n
    if n < menor:
        menor = n
    c = str(input('Deseja Continuar? [S/N]:')).strip().lower()[0]
print(f'A Média dos {total} valores, é {media/total:.2f}')
print(f'O Maior valor lido é {maior}')
print(f'O Menor valor lido é {menor}')
