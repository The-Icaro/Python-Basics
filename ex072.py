print('---- | CAIXA | ----')
precototal = 0
preco1000 = 0
menorpreco = 0
menornome = 0
while True:
    nome = str(input('Nome do Produto:')).strip().title()
    preco = float(input('Preço do Produto:'))
    precototal += preco
    if preco >= 1000:
        preco1000 += 1
    menorpreco = preco
    menornome = nome
    if preco < menorpreco:
        menorpreco = preco
        menornome = nome
    c = str(input('Algo Mais? [S/N]:')).strip().upper()[0]
    while c != 'S' and c != 'N':
        c = str(input('RESPOTA INVÁLIDA. Escolha entre S ou N:')).strip().upper()[0]
    if c is 'N':
        break
print(f'O total gasto na compra é de R${precototal}')
print(f'{preco1000} produtos, custam mais de R$1000')
print(f'O {menornome} é o produto mais barato, custando R${menorpreco}')
