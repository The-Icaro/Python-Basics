ficha = {}
cadastro = []
mediaidade = 0
while True:
    ficha['nome'] = str(input('Nome: ')).strip().title()
    ficha['sexo'] = str(input('Sexo (M/F): ')).strip().upper()[0]
    ficha['idade'] = int(input('Idade: '))
    cadastro.append(ficha.copy())
    pergunta = str(input('Deseja Continuar?: ')).strip().upper()[0]
    if pergunta != 'S' and pergunta != 'N':
        pergunta = str(input('INVÁLIDO. Escolha entre Sim ou Não! ')).strip().upper()[0]
    if pergunta == 'N':
        break
print(f'Foram {len(cadastro)} Pessoas Cadastradas!')
for c in range(0, len(cadastro)):
    mediaidade += cadastro[c]['idade'] / len(cadastro)
print(f'A Média de Idade do Grupo é de {mediaidade:.1f}')
print('As Mulheres Cadastradas são: ')
for c in range(0, len(cadastro)):
    if cadastro[c]["sexo"] == "F":
        print({cadastro[c]["nome"]}, end=' ')
print('\nPessoas com idade Acima da Média: ')
for c in range(0, len(cadastro)):
    if cadastro[c]["idade"] > mediaidade:
        print({cadastro[c]["nome"]}, end=' ')
