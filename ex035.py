n1 = int(input('Digite um número:'))
n2 = int(input('Digite um segundo número:'))
n3 = int(input('Digite um terceiro número:'))
menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3
maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3
print(f'O maior número é {maior}')
print(f'O menor número é {menor}')
