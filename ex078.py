pp = ('Pão', 0.40, 'Manteiga', 2.50, 'Leite', 3.50, 'Maionese', 3,
                  'Café', 7.50, 'Achocolatado', 5)
print('------ | Café Da Manhã | ------')
print('='*31)
for pos in range(0, len(pp)):
    if pos % 2 == 0:
        print(f'{pp[pos]:.<24}', end='')
    else:
        print(f'R${pp[pos]:>5.2f}')
print('='*31)
