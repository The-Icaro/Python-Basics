dias = float(input('O carro foi alugado por quantos dias?'))
km = float(input('Quantos kms percorridos?'))
preco = (dias * 60) + (km * 0.15)
print(f'Você alugou o carro por {dias} dias e percorreu {km}km, dando um total de R${preco}')
