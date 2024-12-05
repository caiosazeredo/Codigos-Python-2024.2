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
query = "SELECT nome, idade from aluno where sexo= 'M' and naturalidade = 'Rio de Janeiro'"
cursor.execute(query)
resultados = cursor.fetchall()
print("todos os alunos homens cariocas")
for nome,idade in resultados:
        print(nome)

query2 = "SELECT nome from aluno where sexo= 'F' and naturalidade = 'São Paulo'"
cursor.execute(query2)
resultados2 = cursor.fetchall()     
print("todos os alunos mulheres paulistas")
for linha, in resultados2:
        print(linha)
# Fechando o cursor e a conexão
cursor.close()
cnx.close()
