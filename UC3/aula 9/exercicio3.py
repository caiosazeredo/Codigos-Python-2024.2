import mysql.connector

cnx = mysql.connector.connect(
    user="python",
    password="aula@123",
    host="exemploaulacaio.mysql.database.azure.com",
    port=3306,
    database="escolasenac"
)

cursor = cnx.cursor()
print("Sistema de cadastro")
usuarionovo= input("Digite o usuario:")
senhanova= input("Digite a senha:")
query = "INSERT INTO usuario_secretaria (usuario, senha) VALUES (%s, %s);"
cursor.execute(query, (usuarionovo,senhanova,))
cnx.commit()
cursor.close()
cnx.close()