# importar o DAO: Data Access Object (camada de acesso a dados)
import bf_DAO as dao
from bc_classe import Pessoa

# criar uma pessoa
nova = Pessoa("Jamille Ferreira", "jamillef@gmail.com", "47 90135 8765")

# incluir a pessoa no BD
dao.incluir_pessoa(nova)

# mostrar mensagem de finalização
print("Término do programa de inclusão de pessoa no BD!")

'''
Pontos a refletir sobre este programa:
a) Se houver algum erro de conexão com o banco de dados
(por exemplo, o servidor MySql não está rodando), 
o que acontece?
b) Se houver algum erro na inclusão da pessoa
(por exemplo, não foi informado o email), o que acontece?
c) Após a inclusão da pessoa, qual é o ID dessa nova pessoa?
d) O campo "id" existe na tabela do banco de dados,
mas não está disponível na classe Pessoa. 
Como resolver esse problema?
'''