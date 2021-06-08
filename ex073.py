print('--- | CAIXA ELETRÔNICO | ---')
print('-' * 28)
valor = int(input('Qual o Valor do Saque: R$'))
total = valor
nota = 200
totalnota = 0
while True:
    if total >= nota:
        total -= nota
        totalnota += 1
    else:
        if totalnota > 0:
            print(f'Total de {totalnota} cédulas de R${nota}')
        if nota == 200:
            nota = 100
        elif nota == 100:
            nota = 50
        elif nota == 50:
            nota = 20
        elif nota == 20:
            nota = 10
        elif nota == 10:
            nota = 5
        elif nota == 5:
            nota = 1
        totalnota = 0
        if total == 0:
            break
print('-' * 28)
print('Obrigado, Volte Sempre!')
