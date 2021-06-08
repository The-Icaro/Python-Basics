ficha = {}
ficha['Nome'] = str(input('Nome:')).strip().title()
ficha['Media'] = float(input(f'Média de {ficha["Nome"]}: '))
ficha['Situacao'] = 'Aprovado'
for k in ficha.keys():
    if ficha['Media'] >= 7:
        ficha['Situacao'] = 'Aprovado'
    else:
        ficha['Situacao'] = 'Reprovado'
for k, v in ficha.items():
    print(f'{k} é igual a {v}')
