parametro = 0
expressao = str(input('Digite a Expressão:')).strip()
for caractere in expressao:
    if caractere is '(':
        parametro += 1
    if caractere is ')':
        parametro -= 1
    if parametro < 0:
        break
if parametro == 0:
    print(f'A Expressão {expressao} , Está Correta!')
else:
    print(f'A Expressão {expressao} está errada!')
