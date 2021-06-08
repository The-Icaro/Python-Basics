print('=== | Progressão Aritmética | ===')
n = int(input('Primeiro Termo da P.A:'))
r = int(input('Razão da P.A:'))
pa = n
c = 1
mais = 10
total = 0
while mais != 0:
    total += mais
    while c <= total:
        print(pa, end=',')
        pa += r
        c += 1
    print('...')
    mais = int(input('Deseja mostrar mais quantos termos:'))
print(f'A P.A foi finalizada com {total} termos')
