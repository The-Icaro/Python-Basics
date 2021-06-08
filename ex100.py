from time import sleep


def linha():
    print('-'*32)


def contador(inicio, fim, passo):
    if passo < 0:
        passo *= -1
    if passo == 0:
        passo = 1
    linha()
    print(f'Contagem de {inicio} até {fim}, de {passo} em {passo}.')
    sleep(2)
    if inicio < fim:
        cont = inicio
        while cont <= fim:
            print(f'{cont}', end=' ', flush=True)
            cont += passo
            sleep(0.3)
    else:
        cont = inicio
        while cont >= fim:
            print(f'{cont}', end=' ', flush=True)
            cont -= passo
            sleep(0.3)
    print('Fim!')


contador(1, 10, 1)
contador(10, 0, 2)
linha()
print('Sua vez Agora!')
i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
contador(i, f, p)