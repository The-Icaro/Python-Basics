r1 = float(input('Comprimento da primeira reta:'))
r2 = float(input('Comprimento da segunda reta:'))
r3 = float(input('Comprimento da terceira reta:'))
tr1 = (r2 - r3) < r1 < r2 + r3
tr2 = (r1 - r3) < r2 < r1 + r3
tr3 = (r1 - r2) < r3 < r1 + r2
if tr1 and tr2 and tr3 is True:
    print('Com essas medidas é possível fazer um triângulo')
else:
    print('Com essas medidas não é possível fazer um triângulo')
