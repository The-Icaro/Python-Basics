print('=== | ÍNDICE DE MASSA CORPÓREA | ===')
a = float(input('Sua Altura em Metros:'))
p = float(input('Seu Peso:'))
imc = p / (a**2)
print(f'Seu IMC é {imc:.2f}')
if imc < 18.5:
    print('VOCÊ ESTÁ ABAIXO DO PESO!')
elif 25 < imc <= 18.5:
    print('VOCÊ ESTÁ NO PESO IDEAL!')
elif 30 < imc <= 25:
    print('VOCÊ ESTÁ COM SOBREPESO!')
elif 40 < imc <= 30:
    print('VOCÊ ESTÁ OBESO!')
else:
    print('VOCÊ TEM OBESIDADE MÓRBIDA!')
