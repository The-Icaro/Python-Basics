cidade = str(input('Qual nome da sua cidade?'))
c1 = cidade.lower().split()[0].count('santo')
if c1 == 1:
    print(f'Sua cidade começa com Santo')
if c1 == 0:
    print(f'Sua cidade não começa com Santo')
