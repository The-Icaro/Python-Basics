import random

n = int(random.randrange(0, 5))
print('Estou pensando em um número de 0 a 5. Você consegue advinhar?')
r = int(input('Resposta:'))
if r == n:
    print('É... Parabéns, você ganhou. A próxima eu venço, sortudo de merda')
else:
    print('kkkkkkkkkkk Você errou, eu venci, seu lixo')
