nome = str(input('Qual o seu nome?')).strip().title()
n1 = nome.split()[0]
nultimo = nome.split()
print(f'Seu primeiro nome: {n1}')
print(f'Seu último nome: {nultimo[len(nultimo)-1]}')
