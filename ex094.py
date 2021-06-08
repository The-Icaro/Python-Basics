from datetime import date
ficha = {}
ficha['nome'] = str(input('Nome: ')).strip().title()
nascimento = int(input('Ano de Nascimento: '))
ficha['idade'] = date.today().year - nascimento
ficha['ctps'] = int(input('Carteira de Trabalho (0 Não Tem) : '))
if ficha['ctps'] > 0:
    ficha['contratacao'] = int(input('Ano de Contratação: '))
    ficha['salario'] = float(input('Salário: R$'))
    ficha['aposentadoria'] = (ficha['contratacao'] - nascimento) + 35
for k, v in ficha.items():
    print(f'{k} tem o valor {v}')
