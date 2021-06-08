print('=== | Cadastro | ===')
media = 0
mulheres20 = 0
maior = 0
for p in range(1, 5):
    print(f'--- | {p}ª Pessoa | ---' )
    nome = str(input('Nome:')).strip().title()
    idade = int(input('Idade:'))
    print('Sexo:[1]Masculino [2]Feminino')
    sexo = int(input('Resposta:'))
    if sexo == 1:
        s = 'Masculino'
    elif sexo == 2:
        s = 'Feminino'
    media += idade  # ainda dividir por 4 para dar a media
    if sexo == 1 and p == 1:
        maior = idade
        n1 = nome
    if sexo == 1 and idade > maior:
        maior = idade
        n1 = nome
    if sexo == 2 and idade < 20:
        mulheres20 += 1
print(f'A média de idade do grupo é de {media/4} anos')
print(f'{n1} é o homem mais velho')
print(f'{mulheres20} mulheres tem menos de 20 anos')