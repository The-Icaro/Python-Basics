vc = float(input('Qual o valor da casa?'))
s = float(input('Qual o seu salário?'))
a = float(input('Em quantos anos deseja pagar?'))
pm = vc / (a * 12)
s1 = s * (30/100)
if pm > s1:
    print(f'Para pagar uma casa de R${vc} , a prestação mensal será de R${pm:.2f}.\nEmpréstimo Negado!')
else:
    print(f'Para pagar uma casa de R${vc} , a prestação mensal será de R${pm:.2f}.\nEmpréstimo Aprovado!')
print('===|Obrigado por contar com nossos serviços!|===')
