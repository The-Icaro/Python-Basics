from datetime import date

print('====== | CONFEDERAÇÃO NACIONAL DE NATAÇÃO | ======')
nome = str(input('Nome do Atleta:')).strip().title()
nasc = int(input('Ano de Nascimento:'))
nasc1 = date.today().year - nasc
if nasc1 <= 9:
    print(f'{nome}\n--- |SUA CATEGORIA É MIRIM| ---')
elif nasc1 <= 14:
    print(f'{nome}\n--- |SUA CATEGORIA É INFATIL| ---')
elif nasc1 <= 19:
    print(f'{nome}\n--- |SUA CATEGORIA É JUNIOR| ---')
elif nasc1 <= 20:
    print(f'{nome}\n--- |SUA CATEGORIA É SÊNIOR| ---')
else:
    print(f'{nome}\n--- |SUA CATEGORIA É MASTER| ---')
