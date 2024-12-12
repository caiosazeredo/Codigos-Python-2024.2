import mysql.connector

cnx = mysql.connector.connect(
    user="python",
    password="aula@123",
    host="exemploaulacaio.mysql.database.azure.com",
    port=3306,
    database="escolasenac"
)

cursor = cnx.cursor()

idademenor= input("Digite a menor idade para buscar:")
idademaior= input("Digite a maior idade para buscar:")
query = "SELECT nome,idade,idturma,alergias FROM aluno WHERE idade >= %s and idade<= %s order by idade;"
cursor.execute(query, (idademenor,idademaior,))

resultados = cursor.fetchall()
if resultados:
    for nome,idade,idturma,alergias in resultados:
        if (alergias != "Leite"):
            print(f"Nome: {nome}, idade: {idade}, Turma {idturma}")
else:
    print("Nenhum aluno encontrado com esse intervalo de idade")
cursor.close()
cnx.close()