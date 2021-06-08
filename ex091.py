lista = []
while True:
    nome = str(input('Nome: ')).strip().title()
    notas1 = float(input('Nota do Primeiro Bimetre: '))
    notas2 = float(input('Nota do Segundo Bimetre: '))
    media = (notas1 + notas2) / 2
    lista.append([nome, [notas1, notas2], media])
    pergunta = str(input('Deseja Continuar?: ')).strip().lower()[0]
    while pergunta != 's' and pergunta != 'n':
        pergunta = str(input('Resposta Inválida! Escolha entre Sim ou Não!: ')).strip().lower()[0]
    if pergunta == 'n':
        break
print('-='*12)
print(f'{"No.":<4}{"Nome":^10}{"Média":>8}')
print('-='*12)
for i, dados in enumerate(lista):
    print(f'{i:<4}{dados[0]:^10}{dados[2]:>8.1f}')
    print('-'*24)
while True:
    opc = int(input('Deseja Mostrar as Notas de Qual Aluno? (999 interrompe): '))
    if opc == 999:
        break
    if opc <= len(lista)-1:
        print(f'{lista[opc][0]}, tirou as notas: {lista[opc][1]}')
