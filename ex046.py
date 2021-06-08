print('=== | CAIXA | ===')
n = str(input('Qual seu nome?')).strip().title()
print(f'Olá {n}, Bom Dia!')
p = float(input('Qual o valor da compra?'))
print("""Qual a forma de pagamento?
[1] Dinheiro
[2] Cheque
[3] Cartão""")
pg = int(input('Reposta:'))
if pg == 0 or pg > 3:
    print('Opção Inválida!')
else:
    print("""Quer pagar em quantas vezes?
[1] À Vista
[2] 2x no Cartão
[3] 3x no Cartão
[4] 4x no Cartão
[5] 5x no Cartão""")
    tpg = int(input('Reposta:'))
    if tpg == 0 or tpg > 5:
        print('Opção Inválida!')
    else:
        dc = p - (p * 10/100)
        cvista = p - (p * 5/100)
        c2x = p
        c345x = p + (p * 20/100)
# Dinheiro e Cheque = 1/2 e 1
        if pg == 1 or pg == 2 and tpg == 1:
            print(f'A compra de R${p}, com o desconto de 10% por ser à vista se torna R${dc:.2f}!')
# Cartão
        if pg == 3:
            if tpg == 1:
                print(f'A compra de R${p}, com o desconto de 5% por ser à vista no Cartão se torna R${cvista:.2f}')
            elif tpg == 2:
                print(f'A compra de R${p}, 2x no Cartão não tem desconto')
            elif tpg == 3 or tpg == 4 or tpg == 5:
                print(f'A compra de R${p}, se torna R${c345x:.2f} com o juros de 20%')
