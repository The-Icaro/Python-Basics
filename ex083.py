lista =[]
while True:
    numeros = int(input('Digite um Número:'))
    lista.append(numeros)
    pergunta = str(input('Deseja Continuar? ')).strip().lower()[0]
    while pergunta != 's' and pergunta != 'n':
        pergunta = str(input('Resposta Inválida! Escolha entre Sim ou Não:')).strip().lower()[0]
    if pergunta == 'n':
        break
print(*lista, sep=' ')
print(f'Foram digitados {len(lista)} números!')
lista.sort(reverse=True)
print('Lista em Ordem Decrescente', *lista, sep=' ')
if 5 in lista:
    print('O valor 5 está na lista!')
else:
    print('O valor 5 não está na lista!')

