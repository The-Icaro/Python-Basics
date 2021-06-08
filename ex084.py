lista = []
listapares = []
listaimpares = []
while True:
    numeros = int(input('Digite um Número:'))
    lista.append(numeros)
    if numeros % 2 == 0:
        listapares.append(numeros)
    else:
        listaimpares.append(numeros)
    pergunta = str(input('Deseja Continuar? ')).strip().lower()[0]
    while pergunta != 's' and pergunta != 'n':
        pergunta = str(input('Resposta Inválida! Escolha entre Sim ou Não:')).strip().lower()[0]
    if pergunta == 'n':
        break
print(lista)
print(listapares)
print(listaimpares)
