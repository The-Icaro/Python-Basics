palavras = ('bom dia', 'ola', 'tudo bem', 'paralelepipedo', 'estou', 'aprendendo', 'python')
vogais = ('a', 'e', 'i', 'o', 'u')
for p in palavras:
    print(f'\nNa Palavra {p.title()}, Temos as Vogais: ', end='')
    for letra in p:
        if letra in 'aeiou':
            print(letra.upper(), end=' ')