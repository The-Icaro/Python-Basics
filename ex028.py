frase = str(input('Digite uma frase:')).lower().strip()
la = frase.count('a')
la1 = frase.find('a')+1
la2 = frase.rfind('a')+1
if la == 0:
    print('A letra "A" não aparece na frase')
else:
    print(f'Na frase {frase} aparece:')
    print(f'A letra "A" {la} vezes')
    print(f'Ela aparece a primeira vez na {la1}ª posição')
    print(f'E aparece a última vez na {la2}ª posição')