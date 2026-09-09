# importar a classe
from bc_classe import Pessoa

# importar a biblioteca para trabalhar com MySQL
import mysql.connector

def incluir_pessoa(pessoa):

    # conectar ao servidor MySQL com usuário e senha root
    conn = mysql.connector.connect(
        host="10.10.34.27",
        user="emi",
        password="emi1020"
    )

    # criar um cursor para executar comandos SQL
    cursor = conn.cursor()

    # selecionar o banco de dados
    cursor.execute("USE info2026emi")
    
    # executar o comando SQL para incluir a pessoa
    cursor.execute("INSERT INTO Jamille_pessoas (nome, email, telefone) VALUES (%s, %s, %s)", (pessoa.nome, pessoa.email, pessoa.telefone))

    # confirmar as alterações
    conn.commit()
    
    # fechar a conexão com o banco de dados
    conn.close()