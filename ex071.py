print('--- | CADASTRO DE PESSOAS | ---')
maior18 = 0
homens = 0
fmenor20 = 0
while True:
    idade = int(input('Idade:'))
    sexo = str(input('Sexo [M/F]:')).strip().upper()[0]
    while sexo != 'M' and sexo != 'F':
        sexo = str(input('SEXO INVÁLIDO. Escolha entre M ou F:')).strip().upper()[0]
    if idade >= 18:
        maior18 += 1
    if sexo is 'M':
        homens += 1
    if sexo is 'F' and idade < 20:
        fmenor20 += 1
    p = str(input('Quer Continuar Cadastrando [S/N]?')).strip().upper()[0]
    while p != 'S' and p != 'N':
        p = str(input('RESPOSTA INVÁLIDA. Escolha entre S ou N:')).strip().upper()[0]
    if p is 'N':
        break
print(f'{maior18} pessoas tem mais de 18 anos!')
print(f'{homens} homens foram cadastrados!')
print(f'{fmenor20} mulheres tem menos de 20 anos!')
