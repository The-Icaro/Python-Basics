s = float(input('Qual o salário do funcionário?'))
s1 = s + s * 10/100
s2 = s + s * 15/100
if s > 1250:
    print(f'O salário de R${s}, com o aumento de 10% se torna R${s1}')
else:
    print(f'O salário de R${s}, com o aumento de 15% se torna R${s2}')