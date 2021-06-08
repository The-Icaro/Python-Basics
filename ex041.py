from datetime import date

print('====== | ALISTAMENTO MILITAR | ======')
nome = str(input('Qual o seu nome completo?')).strip().title()
n = int(input('Qual seu ano de nascimento?'))
n1 = date.today().year - n
n2 = 17 - n1
n3 = n1 - 17
print(nome)
if n1 == 18:
    print(f'Com {n1} anos, você já deveria estar no Exército ou Dipensado!')
elif n1 == 17:
    print(f'Com {n1} anos, está na hora de se Alistar!')
elif n1 < 17:
    print(f'Com {n1} anos, ainda faltam {n2} anos para se Alistar!')
else:
    print(f'Com {n1} anos, já se passaram {n3} anos do Alistamento!')
