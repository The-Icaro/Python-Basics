nome = str(input('Qual o seu nome?'))
n1 = nome.lower().strip().find('silva')
if n1 == -1:
    print(f"Seu nome não tem Silva")
else:
    print(f'Seu nome tem silva')
