n = int(input('Digite um número inteiro:'))
print("""Selecione a conversão
[1] Conversão para Binário
[2] Conversão para Hexadecimal
[3] Conversão para Octal""")
o = int(input('Digite sua opção:'))
if o == 1:
    print(f'O número {n} em Binário é {bin(n)}')
elif o == 2:
    print(f'O número {n} em Hexadecimal é {hex(n)}')
elif o == 3:
    print(f'O número {n} em Octal é {oct(n)}')
else:
    print('Opção inválida')
