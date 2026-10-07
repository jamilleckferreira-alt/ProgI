import os
import datetime
import sqlite3
import mysql.connector
from dotenv import load_dotenv

load_dotenv()

# ==========================================
# 1. CLASSES DE DOMÍNIO
# ==========================================
class Autores:
    def __init__(self, cpf: int, nome: str, data_nascimento,
                 nacionalidade: str, numero: int, email: str):
        self.cpf = cpf
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.nacionalidade = nacionalidade
        self.numero = numero
        self.email = email

    def __str__(self):
        data_formatada = self.data_nascimento
        if isinstance(data_formatada, datetime.date):
            data_formatada = data_formatada.strftime("%d/%m/%Y")
        elif isinstance(data_formatada, str) and "-" in data_formatada:
            try:
                ano, mes, dia = map(int, data_formatada.split("-"))
                data_formatada = f"{dia:02d}/{mes:02d}/{ano}"
            except ValueError:
                pass

        return f'''Autor:
    CPF: {self.cpf}
    Nome: {self.nome}
    Data de nascimento: {data_formatada}
    Nacionalidade: {self.nacionalidade}
    Número de telefone: {self.numero}
    Email: {self.email}'''

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
        return f'''Livro:
    ISBN: {self.isbn}
    Título: {self.titulo}
    Autor: {self.autor_nome}
    Gênero: {self.genero}
    Ano de lançamento: {self.ano_lancamento}
    Editora: {self.editora}'''


# ==========================================
# 2. INTERFACE E MOTORES DE BANCO DE DADOS
# ==========================================
class BancoDadosInterface:
    def conectar(self): pass
    def desconectar(self): pass
    def inserir_autor(self, autor): pass
    def listar_autores(self): pass
    def inserir_livro(self, livro): pass
    def listar_livros(self): pass
    def buscar_livro_por_isbn(self, isbn): pass
    def editar_livro(self, isbn, novos_dados): pass
    def excluir_livro(self, isbn): pass

class BancoSQLite(BancoDadosInterface):
    def __init__(self):
        self.conn = None

    def conectar(self):
        self.conn = sqlite3.connect("biblioteca.db")
        self._criar_tabelas()
        print("🔌 Conectado ao banco SQLite local (biblioteca.db)!")
    
    def desconectar(self):
        if self.conn:
            self.conn.close()

    def _criar_tabelas(self):
        cursor = self.conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS autores (
            cpf INTEGER PRIMARY KEY, nome TEXT, data_nascimento TEXT, nacionalidade TEXT, numero INTEGER, email TEXT)''')
        cursor.execute('''CREATE TABLE IF NOT EXISTS livros (
            isbn INTEGER PRIMARY KEY, titulo TEXT, genero TEXT, ano_lancamento INTEGER, editora TEXT, autor_nome TEXT)''')
        self.conn.commit()

    def inserir_autor(self, autor):
        cursor = self.conn.cursor()
        cursor.execute("INSERT OR REPLACE INTO autores VALUES (?, ?, ?, ?, ?, ?)", 
                       (autor.cpf, autor.nome, str(autor.data_nascimento), autor.nacionalidade, autor.numero, autor.email))
        self.conn.commit()

    def listar_autores(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM autores")
        linhas = cursor.fetchall()
        return [Autores(l[0], l[1], l[2], l[3], l[4], l[5]) for l in linhas]

    def inserir_livro(self, livro):
        cursor = self.conn.cursor()
        cursor.execute("INSERT OR REPLACE INTO livros VALUES (?, ?, ?, ?, ?, ?)", 
                       (livro.isbn, livro.titulo, livro.genero, livro.ano_lancamento, livro.editora, livro.autor_nome))
        self.conn.commit()

    def listar_livros(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM livros")
        linhas = cursor.fetchall()
        return [Livros(l[0], l[1], l[2], l[3], l[4], l[5]) for l in linhas]

    def buscar_livro_por_isbn(self, isbn):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM livros WHERE isbn = ?", (isbn,))
        l = cursor.fetchone()
        if l:
            return Livros(l[0], l[1], l[2], l[3], l[4], l[5])
        return None

    def editar_livro(self, isbn, novos_dados):
        cursor = self.conn.cursor()
        cursor.execute("""UPDATE livros SET titulo = ?, genero = ?, ano_lancamento = ?, editora = ? 
                          WHERE isbn = ?""", 
                       (novos_dados['titulo'], novos_dados['genero'], novos_dados['ano_lancamento'], novos_dados['editora'], isbn))
        self.conn.commit()

    def excluir_livro(self, isbn):
        cursor = self.conn.cursor()
        cursor.execute("DELETE FROM livros WHERE isbn = ?", (isbn,))
        self.conn.commit()

class BancoMySQL(BancoDadosInterface):
    def __init__(self):
        self.host = os.getenv("DB_HOST", "localhost")
        self.port = int(os.getenv("DB_PORT", 3306))
        self.user = os.getenv("DB_USER", "root")
        self.password = os.getenv("DB_PASSWORD", "")
        self.database = os.getenv("DB_NAME", "biblioteca")

        self.config = {
            "host": self.host, 
            "port": self.port,
            "user": self.user, 
            "password": self.password, 
            "database": self.database
        }
        self.conn = None

    def conectar(self):
        config_sem_db = self.config.copy()
        db_nome = config_sem_db.pop("database")
        temp_conn = mysql.connector.connect(**config_sem_db)
        temp_cursor = temp_conn.cursor()
        temp_cursor.execute(f"CREATE DATABASE IF NOT EXISTS {db_nome}")
        temp_conn.close()

        self.conn = mysql.connector.connect(**self.config)
        self._criar_tabelas()
        print(f"🔌 Conectado ao servidor MySQL via .env (Banco: {db_nome})!")

    def desconectar(self):
        if self.conn:
            self.conn.close()

    def _criar_tabelas(self):
        cursor = self.conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS autores (
            cpf BIGINT PRIMARY KEY, nome VARCHAR(255), data_nascimento VARCHAR(50), nacionalidade VARCHAR(105), numero BIGINT, email VARCHAR(255))''')
        cursor.execute('''CREATE TABLE IF NOT EXISTS livros (
            isbn BIGINT PRIMARY KEY, titulo VARCHAR(255), genero VARCHAR(255), ano_lancamento INT, editora VARCHAR(255), autor_nome VARCHAR(255))''')
        self.conn.commit()

    def inserir_autor(self, autor):
        cursor = self.conn.cursor()
        query = "REPLACE INTO autores (cpf, nome, data_nascimento, nacionalidade, numero, email) VALUES (%s, %s, %s, %s, %s, %s)"
        cursor.execute(query, (autor.cpf, autor.nome, str(autor.data_nascimento), autor.nacionalidade, autor.numero, autor.email))
        self.conn.commit()

    def listar_autores(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM autores")
        linhas = cursor.fetchall()
        return [Autores(l[0], l[1], l[2], l[3], l[4], l[5]) for l in linhas]

    def inserir_livro(self, livro):
        cursor = self.conn.cursor()
        query = "REPLACE INTO livros (isbn, titulo, genero, ano_lancamento, editora, autor_nome) VALUES (%s, %s, %s, %s, %s, %s)"
        cursor.execute(query, (livro.isbn, livro.titulo, livro.genero, livro.ano_lancamento, livro.editora, livro.autor_nome))
        self.conn.commit()

    def listar_livros(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM livros")
        linhas = cursor.fetchall()
        return [Livros(l[0], l[1], l[2], l[3], l[4], l[5]) for l in linhas]

    def buscar_livro_por_isbn(self, isbn):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM livros WHERE isbn = %s", (isbn,))
        l = cursor.fetchone()
        if l:
            return Livros(l[0], l[1], l[2], l[3], l[4], l[5])
        return None

    def editar_livro(self, isbn, novos_dados):
        cursor = self.conn.cursor()
        query = "UPDATE livros SET titulo = %s, genero = %s, ano_lancamento = %s, editora = %s WHERE isbn = %s"
        cursor.execute(query, (novos_dados['titulo'], novos_dados['genero'], novos_dados['ano_lancamento'], novos_dados['editora'], isbn))
        self.conn.commit()

    def excluir_livro(self, isbn):
        cursor = self.conn.cursor()
        cursor.execute("DELETE FROM livros WHERE isbn = %s", (isbn,))
        self.conn.commit()


# ==========================================
# 3. FUNÇÕES DE INTERAÇÃO COM O USUÁRIO
# ==========================================
def cadastrar_autor(db):
    print("\n--- CADASTRO DE AUTOR ---")
    try:
        cpf = int(input("CPF (somente números): "))
        nome = input("Nome do autor: ").strip()
        
        data_str = input("Data de nascimento (DD/MM/AAAA): ")
        dia, mes, ano = map(int, data_str.split('/'))
        data_nasc = datetime.date(ano, mes, dia)
        
        nacionalidade = input("Nacionalidade: ").strip()
        numero = int(input("Telefone (somente números): "))
        email = input("Email: ").strip()
        
        novo_autor = Autores(cpf, nome, data_nasc, nacionalidade, numero, email)
        db.inserir_autor(novo_autor)
        print("Autor cadastrado com sucesso!")
    except ValueError:
        print("Formato de dados inválido (verifique números e datas).")

def cadastrar_livro(db):
    print("\n--- CADASTRO DE LIVRO ---")
    try:
        isbn = int(input("ISBN (somente números): "))
        titulo = input("Título do livro: ").strip()
        genero = input("Gênero: ").strip()
        ano_lancamento = int(input("Ano de lançamento: "))
        editora = input("Editora: ").strip()
        autor_nome = input("Nome do autor deste livro: ").strip()
        
        novo_livro = Livros(isbn, titulo, genero, ano_lancamento, editora, autor_nome)
        db.inserir_livro(novo_livro)
        print("Livro cadastrado com sucesso!")
    except ValueError:
        print("Formato de dados inválido.")

def listar_tudo(db):
    autores = db.listar_autores()
    livros = db.listar_livros()

    print("\n=== AUTORES CADASTRADOS ===")
    if not autores:
        print("Nenhum autor cadastrado.")
    else:
        for autor in autores:
            print(autor)

    print("\n=== LIVROS CADASTRADOS ===")
    if not livros:
        print("Nenhum livro cadastrado.")
    else:
        for livro in livros:
            print(livro)

def editar_livro(db):
    print("\n--- EDITAR LIVRO ---")
    try:
        isbn_busca = int(input("Digite o ISBN do livro que deseja editar: "))
        livro = db.buscar_livro_por_isbn(isbn_busca)
        
        if livro:
            print(f"\nLivro encontrado: {livro.titulo}")
            novo_titulo = input(f"Novo título [{livro.titulo}]: ").strip() or livro.titulo
            novo_genero = input(f"Novo gênero [{livro.genero}]: ").strip() or livro.genero
            
            ano_str = input(f"Novo ano [{livro.ano_lancamento}]: ").strip()
            novo_ano = int(ano_str) if ano_str else livro.ano_lancamento
            
            nova_editora = input(f"Nova editora [{livro.editora}]: ").strip() or livro.editora
            
            dados_atualizados = {
                'titulo': novo_titulo,
                'genero': novo_genero,
                'ano_lancamento': novo_ano,
                'editora': nova_editora
            }
            db.editar_livro(isbn_busca, dados_atualizados)
            print("Dados do livro atualizados com sucesso!")
        else:
            print("Livro com o ISBN informado não foi encontrado.")
    except ValueError:
        print("Entrada de dados inválida.")

def excluir_livro(db):
    print("\n--- EXCLUIR LIVRO ---")
    try:
        isbn_busca = int(input("Digite o ISBN do livro que deseja remover: "))
        livro = db.buscar_livro_por_isbn(isbn_busca)
        
        if livro:
            db.excluir_livro(isbn_busca)
            print(f"Livro '{livro.titulo}' foi removido do sistema!")
        else:
            print("Livro com o ISBN informado não foi encontrado.")
    except ValueError:
        print("Digite um ISBN numérico válido.")

def alternar_banco():
    print("\n--- SELEÇÃO DE BANCO DE DADOS ---")
    print("1. SQLite (Arquivo Local)")
    print("2. MySQL (Servidor via .env)")
    escolha = input("Escolha o banco desejado (1-2): ").strip()
    
    if escolha == "1":
        db = BancoSQLite()
        db.conectar()
        return db
    elif escolha == "2":
        try:
            db = BancoMySQL()
            db.conectar()
            return db
        except Exception as e:
            print(f"❌ Falha ao conectar ao MySQL: {e}.\nReconfigurando para o SQLite por segurança.")
            db = BancoSQLite()
            db.conectar()
            return db
    else:
        print("Opção inválida! Inicializando com SQLite por padrão.")
        db = BancoSQLite()
        db.conectar()
        return db

def exibir_menu(db_nome):
    print("\n===============================")
    print("       SISTEMA BIBLIOTECÁRIO     ")
    print(f"   [Banco Ativo: {db_nome}]")
    print("===============================")
    print("1. Cadastrar Autor")
    print("2. Cadastrar Livro")
    print("3. Listar Autores e Livros")
    print("4. Editar Livro (por ISBN)")
    print("5. Excluir Livro (por ISBN)")
    print("6. Mudar Conexão do Banco de Dados")
    print("7. Sair")
    return input("Escolha uma opção (1-7): ")


# ==========================================
# 4. FLUXO PRINCIPAL DE EXECUÇÃO
# ==========================================
def main():
    print("Inicializando o sistema...")
    banco_atual = alternar_banco()
    
    while True:
        nome_db_atual = "SQLite" if isinstance(banco_atual, BancoSQLite) else "MySQL"
        opcao = exibir_menu(nome_db_atual)
        
        if opcao == "1":
            cadastrar_autor(banco_atual)
        elif opcao == "2":
            cadastrar_livro(banco_atual)
        elif opcao == "3":
            listar_tudo(banco_atual)
        elif opcao == "4":
            editar_livro(banco_atual)
        elif opcao == "5":
            excluir_livro(banco_atual)
        elif opcao == "6":
            banco_atual.desconectar()
            banco_atual = alternar_banco()
        elif opcao == "7":
            banco_atual.desconectar()
            print("\nEncerrando o sistema de biblioteca... Até mais! 📚")
            break
        else:
            print("Opção inválida! Escolha um número de 1 a 7.")

if __name__ == "__main__":
    main()