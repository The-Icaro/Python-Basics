frase = str(input('Digite algo:'))
if frase.find('.com') == -1:
    print(f'{frase}'+'.com'.strip())
print(frase)