import random

print('---- | JOKENPÔ | ----')
print('Vamos jogar Pedra, Papel ou Tesoura')
print("""[0] Pedra
[1] Papel
[2] Tesoura""")
e = int(input('Seu Escolha:'))
if e > 2:
    print('ESCOLHA INVÁLIDA\nTENTE NOVAMENTE')
else:
    itens = ('Pedra', 'Papel', 'Tesoura')
    pc = random.randint(0, 2)
    print('-=' * 15)
    print(f'O Computador escolheu {itens[pc]}')
    print(f'O Jogador escolheu {itens[e]}')
    print('-=' * 15)
    if pc == 0:
        if e == 0:
            print('EMPATE!')
        elif e == 1:
            print('VOCÊ VENCEU!')
        else:
            print('VOCÊ PERDEU!')
    elif pc == 1:
        if e == 0:
            print('VOCÊ PERDEU!')
        elif e == 1:
            print('EMPATE!')
        else:
            print('VOCÊ VENCEU!')
    elif pc == 2:
        if e == 0:
            print('VOCÊ VENCEU!')
        elif e == 1:
            print('VOCÊ PERDEU!')
        else:
            print('EMPATE!')
