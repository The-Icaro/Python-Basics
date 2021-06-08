def escreva(frase):
    c = 0
    linha = 4
    for l in frase:
        c += 1
    linha += c
    print('~'*linha)
    print(f'{frase.center(linha)}')
    print('~'*linha)


escreva(str(input('Escreva uma Frase: ')).strip())