import random

print('--- | PAR OU ÍMPAR | ---')
print('='*24)
print('Vamos Jogar Par ou Ímpar!')
print('='*24)
v = 0
npc = random.randrange(0, 11)
while True:
    poui = str(input('Você Quer Par ou Ímpar?')).strip().lower()[0]
    print('=' * 24)
    n = int(input('Seu Número:'))
    t = n + npc
    if poui is 'p':
        if t // 2 == 0:
            v += 1
            print('Você Venceu.\nVamos Jogar Novamente.')
            print('=' * 24)
        else:
            break
    if poui is 'i':
        if t // 2 != 0:
            v += 1
            print('Você Venceu.\nVamos Jogar Novamente.')
            print('=' * 24)
        else:
            break
print('='*24)
print('Você PERDEU!')
print(f'Com {v} Vitórias Consecutivas!')
