d = float(input('Qual a distância da viagem?'))
v1 = d * 0.5
v2 = d * 0.45
if d <= 200:
    print(f'Pela distância de {d}km, o preço da viagem será R${v1}')
else:
    print(f'Pela distância de {d}km, o preço da viagem será R${v2}')
print('Tenha um boa viagem!!')
