import mysql.connector

# Conexão com o banco de dados
cnx = mysql.connector.connect(
    user="python",
    password="aula@123",
    host="exemploaulacaio.mysql.database.azure.com",
    port=3306,
    database="escolasenac",  
    ssl_disabled=True     
)

# Criação do cursor
cursor = cnx.cursor()

# Consulta
query = "SELECT nome, cpf_responsavel1, cpf_responsavel2 FROM aluno;"
cursor.execute(query)

for nome, cpf1, cpf2 in cursor.fetchall():
    if cpf1 and cpf2:
        print(f"{nome} tem dois responsáveis cadastrados.")

# Fechando o cursor e a conexão
cursor.close()
cnx.close()