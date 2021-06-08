from time import sleep as s


def maior(*num):
    cont = maior = 0
    print('Analisando os valores...')
    for valor in num:
        print(f'{valor} ', end='', flush=True)
        s(0.4)
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    print(f'\nForam informados {cont} valores ao todo.')
    print(f'O maior valor informado foi {maior}')
    print('-='*30)
    s(5)


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
