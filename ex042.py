print('====== | Média do Aluno | ======')
n = str(input('Nome completo:')).strip().title()
m1 = float(input('Nota no Primeiro Bimestre:'))
m2 = float(input('Nota no Segundo Bimestre:'))
mg = (m1 + m2) / 2
print(f'{n},pelas notas {m1} e {m2}, sua média é {mg}')
if mg < 5.0:
    print('VOCÊ ESTÁ REPROVADO!')
elif 7.0 > mg >= 5.0:
    print('VOCÊ ESTÁ DE RECUPERAÇÃO !')
else:
    print('VOCÊ ESTÁ APROVADO !')
