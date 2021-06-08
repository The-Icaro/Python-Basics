print('-'*19)
print('=== | TABUADA | ===')
print('-'*19)
c = 0
n = int(input('A Tabuada de Qual Número Você Deseja Saber?:'))
print('-'*19)
while True:
    while c is not 10:
        c += 1
        p = n * c
        print(f'{n} x {c} = {p}')
    print('-'*19)
    n1 = str(input('Quer Tentar com Outro Número? [S/N]:')).strip().lower()[0]
    while n1 != 's' and n1 != 'n':
        n1 = str(input('Inválido. Por Favor Escolha entre S ou N:'))
    if n1 == 'n':
        break
    if n1 == 's':
        n = int(input('Qual é esse outro número?:'))
        c = 0
print('Programa Tabuada Encerrado!')
