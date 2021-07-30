class Estudante:
    def __init__(self, nome, idade, nota):
        self.nome = nome
        self.idade = idade
        self.nota = nota   # 0 - 10

    def get_nota(self):
        return self.nota


class Curso:
    def __init__(self, nome, max_aluno):
        self.nome = nome
        self.max_aluno = max_aluno
        self.alunos = []

    def add_alunos(self, aluno):
        if len(self.alunos) < self.max_aluno:
            self.alunos.append(aluno)
            return True
        else:
            return False

    def get_media(self):
        media = 0
        for aluno in self.alunos:
            media += aluno.get_nota()
        return media / len(self.alunos)


curso = Curso('ITA', 3)
while True:
    nomes = str(input('Nome: ')).title().strip()
    idades = int(input('Idade: '))
    notas = int(input('Nota: '))
    a1 = Estudante(nomes, idades, notas)
    curso.add_alunos(a1)
    p = str(input('Nova Matricula?: ')).strip().lower()[0]
    while p != 's' and p != 'n':
        p = str(input('Dado Inválido! Escolha entre sim ou não!')).strip().lower()[0]
    if p == 'n':
        break

print(f'Alunos do Curso {curso.nome}:', end=' ')
for c in range(0, len(curso.alunos)):
    print(curso.alunos[c].nome, end=' ')
print(f'\n{curso.get_media()}')
