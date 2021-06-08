f = str(input('Digite uma frase:')).strip().lower()
f1 = f.split()
f11 = ''.join(f1)
f2 = f.strip().title()
print(f'A frase {f2}, ao contrário é {f11[::-1]}')
if f11 == f11[::-1]:
    print('Por isso é um Palíndromo')
else:
    print('Por isso não é um Palíndromo')

