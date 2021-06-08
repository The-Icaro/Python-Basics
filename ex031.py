v = int(input('Qual sua velocidade (km/h) ?'))
m = (v - 80) * 7
if v >= 80:
    print('Você excedeu o limite de velocidade da via!')
    print(f'Sua multa é de R${m}')
if v <= 79:
    print('Por pouco você não excedeu a velocidade, tome mais cuidado!')
if v <= 70:
    print('Sua velocidade está dentro do limite permitido!')
