from time import sleep
print('=== | CONTAGEM REGRESSIVA | ===')
n = int(input('Digite um número:'))
for c in range(n, 0, -1):
    print(c)
    sleep(1)
