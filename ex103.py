# Crie um programa que tenha uma funcao chamada voto()
# que vai receber como parametro o ano de nascimento de uma pessoa,
# retornando um valor literal indicando se uma pessoa tem o voto negado, opcional
#  ou obrigatorio nas eleicoes, 65 + opcinal, 18 + obrigatorio, 16-17 opcional, 16 negado
def voto(nasc):
    from datetime import date
    n = date.today().year - nasc
    if n < 16:
        return f'Com {n} anos: Não VOTA!'
    elif 16 <= n < 18 or n > 65:
        return f'Com {n} anos: Voto OPCIONAL!'
    else:
        return f'Com {n} anos: Voto OBRIGATÓRIO!'


print('-' * 30)
print(voto(int(input('Ano de Nascimento: '))))

