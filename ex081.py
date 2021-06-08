numero = list()
while True:
    n = [int(input('Digite um valor:'))]
    if n not in numero:
        numero.append(n)
        print('Número Adicionado com Sucesso!')
    else:
        print('Número Já Existente! O Mesmo Não foi Adicionado na Lista!')
    n = numero
    resposta = str(input('Deseja Continuar?:')).strip().lower()[0]
    while resposta != 's' and resposta != 'n':
        resposta = str(input('RESPOSTA INVÁLIDA. Escolha entre Sim ou Não!:')).strip().lower()[0]
    if resposta == 'n':
        break
numero.sort()
for x in numero:
    print(*x, sep=' ', end='')
