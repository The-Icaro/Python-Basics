r1 = float(input('Comprimento da Primeira Reta:'))
r2 = float(input('Comprimento da Segunda Reta:'))
r3 = float(input('Comprimento da Terceira Reta:'))
tr1 = (r2 - r3) < r1 < r2 + r3
tr2 = (r1 - r3) < r2 < r1 + r3
tr3 = (r1 - r2) < r3 < r1 + r2
if tr1 and tr2 and tr3 is True:
    print(f'Com as retas {r1}, {r2} e {r3}:')
    if r1 == r2 == r3:
        print('Formamos um Triângulo Equilátero!')
    elif r1 != r2 != r3:
        print('Formamos um Triângulo Escaleno!')
    else:
        print('Formamos um Triângulo Isósceles!')
else:
    print(f'Com as medidas {r1}, {r2} e {r3} não é possível formar um Triângulo!')
