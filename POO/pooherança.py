class Pet:  # Classe Pai - Pet
    def __init__(self, nome, idade):  # Tem Atributos Presentes nas Classes Filhas
        self.nome = nome
        self.idade = idade

    def show(self):  # Aqui o Metodo se Repete no Pai, e nas Filhas
        print(f'Eu sou {self.nome}, tenho {self.idade} anos')

    def fala(self): # Aqui tbm
        print('Não sei falar!...')


class Cachorro(Pet):  # Classe Filha, pela chamada - (Pet)
    def __init__(self, nome, idade, sexo, cor):
        super().__init__(nome, idade)  # A Função Super se Apropria dos Atributos da Classe Pai, Pra Reutilizar Código
        self.sexo = sexo
        self.cor = cor

    def fala(self):  # O Python vai utilizar das filhas se a chamada for dessa Classe
        print('Au Au...')

    def show(self):  # Aqui o mesmo
        super().show()
        print(f'{self.sexo} de cor {self.cor}')


class Gato(Pet):  # Outra Classe Filha
    def fala(self):  # Aqui tbm
        print('Meow...')


c = Cachorro('Luna', 15, 'Femea', 'Preta')
c.fala()
c.show()
