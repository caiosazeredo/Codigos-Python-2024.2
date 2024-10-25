#Pedir para o usuario apenas o tamanho da coleira
#tamanho do sapato = tamanho da coleira x tamanho da coleira
#fucinheira = tamanho do sapato x 3

coleira = int(input("Entre com o tamanho da coleira do seu cachorro:"))
tamanhosapato = coleira *2
tamanhofuncinheiria = tamanhosapato *3
print(f"Recomenda-se comprar o sapato no seguinte tamanho: {tamanhosapato}")
print(f"Recomenda-se comprar a funcinheira no seguinte tamanho: {tamanhofuncinheiria}")
