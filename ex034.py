a = int(input('Digite o ano que deseja analisar:'))
a1 = a % 4
a2 = a % 100
a3 = a % 400
if a % 4 == 0 and a2 != 0 or a3 == 0:
    print(f'O ano {a} é um ano bissexto')
else:
    print(f'O ano {a} não é bissexto')
