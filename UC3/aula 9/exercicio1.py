import mysql.connector

cnx = mysql.connector.connect(
    user="python",
    password="aula@123",
    host="exemploaulacaio.mysql.database.azure.com",
    port=3306,
    database="escolasenac"
)

cursor = cnx.cursor()

idade= input("Digite a idade para buscar:")

query = "SELECT cpf,endereco FROM aluno WHERE idade = %s;"
cursor.execute(query, (idade,))

resultados = cursor.fetchall()
if resultados:
    for cpf,endereco in resultados:
        print(f"Cpf: {cpf}, Endereço: {endereco}")
else:
    print("Nenhum aluno encontrado com esse nome.")

cursor.close()
cnx.close()