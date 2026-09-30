import datetime

class Autores:
    def __init__(self, cpf: int, nome: str, data_nascimento: datetime.date,
                 nacionalidade: str, numero: int, email: str):
        self.cpf = cpf
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.nacionalidade = nacionalidade
        self.numero = numero
        self.email = email

    def __str__(self):
        return f'''
Autor:
    CPF: {self.cpf}
    Nome: {self.nome}
    Data de nascimento: {self.data_nascimento}
    Número de telefone: {self.numero}
    Email: {self.email}
'''


class Livros:
    def __init__(self, isbn: int, titulo: str, genero: str,
                 ano_lancamento: int, editora: str, autor_nome: str):
        self.isbn = isbn
        self.titulo = titulo
        self.genero = genero
        self.ano_lancamento = ano_lancamento
        self.editora = editora
        self.autor_nome = autor_nome

    def __str__(self):
        return f'''
Livro:
    ISBN: {self.isbn}
    Título: {self.titulo}
    Autor: {self.autor_nome}
    Gênero: {self.genero}
    Ano de lançamento: {self.ano_lancamento}
    Editora: {self.editora}
'''


a1 = Autores(12345678,'Tahereh Mafi',datetime.date(1988, 11, 9),'Iraniana',932647210,'tahereh.mafi@gmail.com')

l1 = Livros(9786556090344,'Imagina-me','Distopia',2020,'Universo dos Livros','Tahereh Mafi')

print(a1)
print(l1)
