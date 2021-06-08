sexo = str(input('Digite seu Sexo [M/F]:')).strip().lower()[0]
while sexo != 'm' and sexo != 'f':
    sexo = str(input('Dado Inválido, Por favor digite seu Sexo:')).strip().lower()[0]
if sexo == 'm':
    sexo = 'Masculino'
else:
    sexo = 'Feminino'
print(f'Sexo {sexo} Registrado')
