n1 = int(input('Digite um valor:'))
n2 = int(input('Digite outro valor:'))
s = 0
while s is not 5:
    print("""Menu:
    [1] Somar
    [2] Multiplicar
    [3] Maior
    [4] Novos Números
    [5] Sair do Programa""")
    s = int(input('O que deseja fazer?:'))
    if s == 1:
        n = n1 + n2
        print(f'A Some entre {n1} e {n2} é {n}')
    if s == 2:
        n = n1 * n2
        print(f'O Produto entre {n1} e {n2} é {n}')
    if s == 3:
        if n1 > n2:
            n = n1
        else:
            n = n2
        print(f'O Maior Valor entre {n1} e {n2} é {n}')
    if s == 4:
        n1 = int(input('Qual o Primeiro Novo Valor?:'))
        n2 = int(input('Qual o Segundo Novo Valor?:'))
    if s > 5 or s < 1:
        print('Valor Inválido, Tente Novamente!')
