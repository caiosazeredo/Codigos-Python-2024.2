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
query = "SELECT nome, endereco FROM aluno;"

cursor.execute(query)
resultados = cursor.fetchall()


query2 = "select nome, idade, tipo_sanguineo from aluno"
cursor.execute(query2)
resultados2 = cursor.fetchall()


print("Nome e endereço de todos os alunos")
for nome, endereco in resultados:
        print(f"{endereco}")
print("Tipo sanguineo dos alunos que podem doar sangue para um aluno que tem o tipo sanguineo B+")
for nome, idade, tipo_sanguineo in resultados2:
        if(tipo_sanguineo in ["B+","B-","O-,O+"]):
                print("possível doador:",nome,idade)
                

# Fechando o cursor e a conexão
cursor.close()
cnx.close()
