import random

print('Estou pensando em um Número de 1 até 10, Será que você consegue advinhar?')
n = random.randrange(1,11)
r = int(input('Reposta:'))
while n != r:
    print('Errado Tente Novamente!')
    r = int(input('Reposta:'))
print(f'Parabéns, Eu estava pensando no número {n} e Você Acertou!')
