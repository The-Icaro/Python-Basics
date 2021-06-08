contagem = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez',
            'onze', 'doze', 'treze', 'catorze', 'quinze', 'dezesseis',
            'dezessete', 'dezoito', 'dezenove', 'vinte')
numero = int(input('Digite um número [0 - 20]:'))
while numero < 0 or numero > 20:
    numero = int(input('Valor Inválido. Digite um número entre 0 e 20:'))
while True:
    print(f'Você digitou o número {contagem[numero]}.')
    r = str(input('Deseja Continuar?:')).strip().lower()[0]
    while r != 's' and r != 'n':
        r = str(input('Inválido. Escolha entre Sim ou Não:'))
    if r == 'n':
        break
    numero = int(input('Novo número entre 0 e 20:'))
