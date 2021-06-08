numeros = (int(input('Digite um Número:')), int(input('Digite um Número:')), int(input('Digite um Número:')),
           int(input('Digite um Número:')))
n = numeros
print(f'O Número 9, aparece {n.count(9)} vezes')
if 3 in n:
    print(f'O Valor 3, aparece a primeira vez na {n.index(3)+1} posição')
else:
    print('O Valor 3, não foi digitado.')
print('Os Valores digitados que são pares:', end='')
for c in n:
    if c % 2 == 0:
        print(c, end=' ')
    